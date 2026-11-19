"""Asistente de soporte de Kommo CRM - servidor web.

Sirve la página del chat (static/index.html) y un endpoint /api/chat que
responde en streaming (Server-Sent Events) usando la API de Claude, con la
base de conocimiento en el system prompt (cacheada).

Variables de entorno:
  ANTHROPIC_API_KEY        clave de la API de Anthropic (obligatoria salvo MOCK_MODE=1)
  MODEL                    modelo (por defecto claude-opus-5-5)
  EFFORT                   low | medium | high (por defecto medium)
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

import anthropic
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

BASE_DIR = Path(__file__).parent
MODEL = os.getenv("MODEL", "claude-opus-5-5")
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
SYSTEM = [
    {"type": "text", "text": instrucciones},
    {
        "type": "text",
        "text": f"<base_de_conocimiento>\n{base_conocimiento}\n</base_de_conocimiento>",
        "cache_control": {"type": "ephemeral", "ttl": "1h"},
    },
]

MENSAJE_RECHAZO = (
    "No puedo ayudarte con eso. Si tu duda es sobre Kommo, cuéntamela de otra forma "
    "o escríbele a tu asesor de " + CONTACTO + "."
)
MENSAJE_ERROR = (
    "Tuve un problema técnico para responder. Intenta de nuevo en un momento; si sigue "
    "fallando, escríbele a tu asesor de " + CONTACTO + "."
)

client = None if MOCK_MODE else anthropic.AsyncAnthropic()

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


async def _stream_claude(mensajes: list, ip: str):
    inicio = time.time()
    try:
        async with client.beta.messages.stream(
            model=MODEL,
            max_tokens=16000,
            system=SYSTEM,
            messages=mensajes,
            output_config={"effort": EFFORT},
            # Si el modelo rechaza la petición por política, la API la reintenta
            # en otro modelo dentro de la misma llamada.
            betas=["server-side-fallback-2026-07-01"],
            fallbacks="default",
        ) as stream:
            async for texto in stream.text_stream:
                yield _sse({"t": texto})
            final = await stream.get_final_message()

        if final.stop_reason == "refusal":
            yield _sse({"t": MENSAJE_RECHAZO})
        u = final.usage
        log.info(json.dumps({
            "evento": "respuesta",
            "ip": ip,
            "pregunta": mensajes[-1]["content"][:500],
            "stop_reason": final.stop_reason,
            "segundos": round(time.time() - inicio, 1),
            "tokens_entrada": u.input_tokens,
            "tokens_cache_leidos": u.cache_read_input_tokens,
            "tokens_cache_escritos": u.cache_creation_input_tokens,
            "tokens_salida": u.output_tokens,
        }, ensure_ascii=False))
        yield _sse({"done": True})

    except anthropic.RateLimitError:
        log.warning(json.dumps({"evento": "rate_limit_api", "ip": ip}))
        yield _sse({"error": "Hay mucha demanda en este momento. Intenta de nuevo en un minuto."})
    except anthropic.APIStatusError as e:
        log.error(json.dumps({"evento": "error_api", "status": e.status_code, "detalle": str(e.message)[:300]}))
        yield _sse({"error": MENSAJE_ERROR})
    except anthropic.APIConnectionError:
        log.error(json.dumps({"evento": "error_conexion"}))
        yield _sse({"error": MENSAJE_ERROR})


@app.post("/api/chat")
async def chat(req: ChatRequest, request: Request):
    ip = _ip(request)
    if not _check_rate(ip):
        raise HTTPException(429, "Enviaste muchos mensajes seguidos. Espera unos minutos.")
    mensajes = _preparar_historial(req.messages)
    gen = _stream_mock(mensajes[-1]["content"]) if MOCK_MODE else _stream_claude(mensajes, ip)
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
