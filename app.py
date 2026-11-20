"""Asistente de soporte de Kommo CRM - servidor web.

Sirve la página del chat (static/index.html) y un endpoint /api/chat que
responde en streaming (Server-Sent Events) usando la API de Claude, con la
base de conocimiento en las instrucciones del sistema. Usa la API de Gemini
(Google); Gemini guarda en caché automáticamente el prefijo repetido.

Variables de entorno:
  GEMINI_API_KEY           clave de la API de Gemini (obligatoria salvo MOCK_MODE=1)
  MODEL                    modelo (por defecto gemini-3.8-flash)
  EFFORT                   nivel de razonamiento: low | medium | high (por defecto medium)
  CONTACTO_ESCALAMIENTO    a quién derivar (texto que va en el prompt)
  RATE_LIMIT_PER_10MIN     mensajes por IP cada 10 minutos (por defecto 30)
  ALLOWED_ORIGINS          dominios que pueden incrustar/llamar el chat, separados por coma
  MOCK_MODE                "1" para probar la interfaz sin llamar a la API
"""

import asyncio
import json
import logging
import os
import time
from collections import defaultdict, deque
from pathlib import Path
from typing import List, Literal

from google import genai
from google.genai import errors, types
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

BASE_DIR = Path(__file__).parent
MODEL = os.getenv("MODEL", "gemini-3.8-flash")
EFFORT = os.getenv("EFFORT", "medium")
MOCK_MODE = os.getenv("MOCK_MODE") == "1"
CONTACTO = os.getenv(
    "CONTACTO_ESCALAMIENTO",
    "Digital Crew / EduConnect por el grupo de WhatsApp de tu taller",
)
RATE_LIMIT = int(os.getenv("RATE_LIMIT_PER_10MIN", "30"))
ALLOWED_ORIGINS = [o.strip() for o in os.getenv("ALLOWED_ORIGINS", "").split(",") if o.strip()]

MAX_TURNS = 20          # mensajes de historial que se envían al modelo
MAX_CHARS = 2000        # largo máximo de cada mensaje del usuario

logging.basicConfig(level=logging.INFO, format="%(message)s")
log = logging.getLogger("asistente")

# --- System prompt: instrucciones + base de conocimiento --------------------
# Se construye una sola vez al arrancar. Es texto fijo (sin fechas ni IDs) para
# que el prefijo se mantenga idéntico entre peticiones y el caché funcione.
instrucciones = (BASE_DIR / "prompt.md").read_text(encoding="utf-8").replace(
    "{{CONTACTO_ESCALAMIENTO}}", CONTACTO
)
base_conocimiento = (BASE_DIR / "base-conocimiento-kommo.md").read_text(encoding="utf-8")
SYSTEM = (
    f"{instrucciones}\n\n<base_de_conocimiento>\n{base_conocimiento}\n</base_de_conocimiento>"
)
CONFIG = types.GenerateContentConfig(
    system_instruction=SYSTEM,
    max_output_tokens=8000,
    thinking_config=types.ThinkingConfig(thinking_level=EFFORT),
)

MENSAJE_RECHAZO = (
    "No puedo ayudarte con eso. Si tu duda es sobre Kommo, cuéntamela de otra forma "
    "o escríbele a tu asesor de " + CONTACTO + "."
)
MENSAJE_ERROR = (
    "Tuve un problema técnico para responder. Intenta de nuevo en un momento; si sigue "
    "fallando, escríbele a tu asesor de " + CONTACTO + "."
)

client = None if MOCK_MODE else genai.Client(api_key=os.environ["GEMINI_API_KEY"])

app = FastAPI(title="Asistente Kommo")
if ALLOWED_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=ALLOWED_ORIGINS,
        allow_methods=["POST"],
        allow_headers=["Content-Type"],
    )


class Mensaje(BaseModel):
    role: Literal["user", "assistant"]
    content: str = Field(min_length=1, max_length=8000)


class ChatRequest(BaseModel):
    messages: List[Mensaje] = Field(min_length=1, max_length=100)


# --- Límite simple por IP (en memoria; suficiente para una sola instancia) ---
_hits: dict = defaultdict(deque)


def _ip(request: Request) -> str:
    fwd = request.headers.get("x-forwarded-for")
    return fwd.split(",")[0].strip() if fwd else (request.client.host if request.client else "?")


def _check_rate(ip: str) -> bool:
    now = time.time()
    q = _hits[ip]
    while q and now - q[0] > 600:
        q.popleft()
    if len(q) >= RATE_LIMIT:
        return False
    q.append(now)
    return True


def _sse(payload: dict) -> str:
    return f"data: {json.dumps(payload, ensure_ascii=False)}\n\n"


def _preparar_historial(msgs: List[Mensaje]) -> list:
    """Recorta el historial, valida el orden de turnos y el largo del último mensaje."""
    msgs = msgs[-MAX_TURNS:]
    while msgs and msgs[0].role != "user":
        msgs = msgs[1:]
    if not msgs or msgs[-1].role != "user":
        raise HTTPException(400, "La conversación debe terminar con un mensaje del usuario.")
    if len(msgs[-1].content) > MAX_CHARS:
        raise HTTPException(400, f"El mensaje es demasiado largo (máximo {MAX_CHARS} caracteres).")
    return [{"role": m.role, "content": m.content} for m in msgs]


def _a_gemini(mensajes: list) -> list:
    # Gemini llama "model" al rol del asistente.
    return [
        types.Content(
            role="model" if m["role"] == "assistant" else "user",
            parts=[types.Part(text=m["content"])],
        )
        for m in mensajes
    ]


async def _stream_mock(pregunta: str):
    texto = (
        "**Modo de prueba** (sin conexión a la IA).\n\n"
        f"Recibí tu pregunta: _{pregunta[:120]}_\n\n"
        "1. Así se verían los **pasos numerados**.\n"
        "2. Con los menús en **negritas**.\n\n"
        "Video: https://www.loom.com/share/88c6f972363740cb81cc16bbd5bbd107"
    )
    for palabra in texto.split(" "):
        yield _sse({"t": palabra + " "})
        await asyncio.sleep(0.03)
    yield _sse({"done": True})


BLOQUEOS = {"SAFETY", "PROHIBITED_CONTENT", "BLOCKLIST", "SPII", "RECITATION"}


async def _stream_gemini(mensajes: list, ip: str):
    inicio = time.time()
    hubo_texto = False
    motivo = None
    uso = None
    try:
        stream = await client.aio.models.generate_content_stream(
            model=MODEL, contents=_a_gemini(mensajes), config=CONFIG
        )
        async for chunk in stream:
            if chunk.usage_metadata:
                uso = chunk.usage_metadata
            if chunk.candidates and chunk.candidates[0].finish_reason:
                motivo = chunk.candidates[0].finish_reason.name
            if chunk.prompt_feedback and chunk.prompt_feedback.block_reason:
                motivo = "BLOQUEO_PREGUNTA"
            texto = chunk.text if chunk.candidates else None
            if texto:
                hubo_texto = True
                yield _sse({"t": texto})

        if not hubo_texto:
            yield _sse({"t": MENSAJE_RECHAZO if (motivo in BLOQUEOS or motivo == "BLOQUEO_PREGUNTA") else MENSAJE_ERROR})
        log.info(json.dumps({
            "evento": "respuesta",
            "ip": ip,
            "pregunta": mensajes[-1]["content"][:500],
            "fin": motivo,
            "segundos": round(time.time() - inicio, 1),
            "tokens_entrada": getattr(uso, "prompt_token_count", None),
            "tokens_cache": getattr(uso, "cached_content_token_count", None),
            "tokens_razonamiento": getattr(uso, "thoughts_token_count", None),
            "tokens_salida": getattr(uso, "candidates_token_count", None),
        }, ensure_ascii=False))
        yield _sse({"done": True})

    except errors.APIError as e:
        log.error(json.dumps({"evento": "error_api", "status": e.code, "detalle": str(e.message)[:300]}))
        if e.code == 429:
            yield _sse({"error": "Hay mucha demanda en este momento. Intenta de nuevo en un minuto."})
        else:
            yield _sse({"error": MENSAJE_ERROR})
    except Exception as e:  # red caída, timeouts, etc.
        log.error(json.dumps({"evento": "error_conexion", "detalle": repr(e)[:300]}))
        yield _sse({"error": MENSAJE_ERROR})


@app.post("/api/chat")
async def chat(req: ChatRequest, request: Request):
    ip = _ip(request)
    if not _check_rate(ip):
        raise HTTPException(429, "Enviaste muchos mensajes seguidos. Espera unos minutos.")
    mensajes = _preparar_historial(req.messages)
    gen = _stream_mock(mensajes[-1]["content"]) if MOCK_MODE else _stream_gemini(mensajes, ip)
    return StreamingResponse(
        gen,
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
    )


@app.get("/health")
async def health():
    return {"ok": True, "modelo": MODEL, "mock": MOCK_MODE}


@app.get("/")
async def index():
    return FileResponse(BASE_DIR / "static" / "index.html")


app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
