# Asistente Kommo (chatbot web)

Chatbot que responde dudas de uso, errores, configuración y desconexiones de Kommo CRM para los clientes de Digital Crew / EduConnect. Usa la API de Gemini de Google (modelo `gemini-3.8-flash`) con la base de conocimiento completa en las instrucciones.

## Archivos

| Archivo | Para qué sirve |
|---|---|
| `base-conocimiento-kommo.md` | Las fichas (pregunta → pasos → video). **Aquí se agregan los tutoriales nuevos.** |
| `prompt.md` | Instrucciones del asistente: tono, formato, cuándo derivar, límites. |
| `app.py` | Servidor (FastAPI). Página del chat en `/`, API en `/api/chat`, estado en `/health`. |
| `static/index.html` | La página del chat (funciona en celular y computadora). |
| `Dockerfile`, `requirements.txt` | Para desplegar en Easypanel o cualquier servidor con Docker. |
| `.env.example` | Variables de configuración. |

## Desplegar en Easypanel

1. Sube esta carpeta a un repositorio de GitHub (privado).
2. En Easypanel: **+ Servicio → App** → fuente **GitHub** → elige el repo → construcción **Dockerfile**.
3. En **Entorno (Environment)** agrega como mínimo:
   ```
   GEMINI_API_KEY=tu_clave
   CONTACTO_ESCALAMIENTO=Digital Crew / EduConnect por el grupo de WhatsApp de tu taller
   ```
   La clave se crea en Google AI Studio (https://aistudio.google.com → API keys). No la pongas en el código ni en el repo.
4. En **Dominios**, apunta un dominio o subdominio (ej. `soporte.tudominio.com`) al puerto **8000**.
5. Despliega y abre `https://soporte.tudominio.com/health`: debe responder `{"ok": true, ...}`.

## Ponerlo en tu página web

La forma más sencilla es un iframe:

```html
<iframe src="https://soporte.tudominio.com/" style="width:100%;max-width:420px;height:640px;border:0;border-radius:12px"></iframe>
```

O simplemente comparte el link directo con los clientes (en el grupo de WhatsApp o en el manual de onboarding).

## Actualizar la base de conocimiento (cada 15 días)

1. Agrega las fichas nuevas en `base-conocimiento-kommo.md` con el mismo formato (`### Pregunta [CATEGORÍA]`, pasos, `Video:`).
2. Haz push al repo; Easypanel vuelve a desplegar.

Claude puede extraer las transcripciones de los Loom nuevos y redactar las fichas: solo pásale los links.

## Configuración opcional

| Variable | Default | Notas |
|---|---|---|
| `MODEL` | `gemini-3.8-flash` | Modelo de Gemini. |
| `EFFORT` | `medium` | Nivel de razonamiento: `low` responde más rápido y gasta menos; `high` razona más. |
| `RATE_LIMIT_PER_10MIN` | `30` | Mensajes máximos por IP cada 10 minutos (evita abusos). |
| `ALLOWED_ORIGINS` | vacío | Solo si llamas a `/api/chat` desde otro dominio sin iframe. |
| `MOCK_MODE` | `0` | `1` = prueba la interfaz sin llamar a la IA (no gasta). |

## Costos

- Cada pregunta envía la base de conocimiento (~17,000 tokens) más el historial. Gemini guarda en caché automáticamente esa parte repetida y la cobra más barata cuando hay preguntas seguidas.
- El costo por respuesta depende de los precios vigentes de `gemini-3.8-flash` en Google AI Studio; revísalo ahí con el uso real de las primeras semanas.
- Los registros del servidor (en Easypanel, pestaña de logs) muestran en cada respuesta los tokens usados y la pregunta, para revisar costos y detectar dudas que la base no cubre.

## Probar en tu computadora

```bash
pip install -r requirements.txt
MOCK_MODE=1 uvicorn app:app --port 8000        # interfaz sin IA
GEMINI_API_KEY=tu_clave uvicorn app:app --port 8000   # con IA
```

Requiere Python 3.10 o superior.
