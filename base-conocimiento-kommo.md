# Base de conocimiento — Asistente Kommo CRM

Fuente: Manual de Onboarding Kommo CRM (Drive) + transcripciones de los tutoriales en Loom.
Cada ficha: **Pregunta típica → Respuesta/pasos → Video**. Categoría: [USO] [TÉCNICA] [ERROR] [DESCONEXIÓN].
Nota: en el menú nuevo de Kommo, la configuración está en la **parte inferior izquierda → Configuración del espacio de trabajo**.

---

## 1. Cuentas, licencias y usuarios

### ¿Cómo compro mi licencia de Kommo? [USO]
1. Entra con el **usuario principal (cuenta maestra)**.
2. Ajustes / Configuración → **Facturación (Billing)**.
3. Elige el plan y pon **1** (= una licencia, no un mes).
- Kommo cobra **por semestre por adelantado**; no se puede pagar mes a mes.
- Planes: Básico e Intermedio/**Avanzado** hacen casi lo mismo, pero el Avanzado permite **Salesbots y automatizaciones** (bots de fuera de oficina, recordatorios, horarios). Es el que recomendamos.
- Plan **Pro**: permite vincular la API de Conversiones de Meta (Meta ve qué leads avanzan/cierran y optimiza las campañas). Recomendado si hay presupuesto y campañas.
- Si no sabes cuántas licencias necesitas, contáctanos.
Video: https://www.loom.com/share/049d853663bf48fa9ad0d3366adc8656

### ¿Cómo agrego más licencias y usuarios (vendedores)? [USO]
1. Desde la **cuenta maestra** → parte inferior izquierda → **Facturación** → **Agregar licencias** → elige cuántas → paga (PayPal / tarjeta).
2. Después: parte inferior izquierda → **Gestión de usuarios** → arriba a la derecha **Agregar usuario** → nombre, correo, contraseña → Guardar. Repite por cada licencia.
- Solo puedes agregar usuarios si **ya pagaste** sus licencias.
Video: https://www.loom.com/share/9fc02fe385a84782a0c1effb119cf765

### ¿Cuántas licencias necesito? ¿Cómo funcionan los usuarios? [USO]
- Lo ideal: **una licencia por persona** que entra al CRM (ej. 1 director + 3 vendedores = 4 licencias).
- Ventajas: cada quien entra con su correo, se pueden crear grupos (ventas, cobranza), **reportes y filtros por usuario**.
- Teléfonos: plan **Avanzado = 2 números de WhatsApp por usuario**; plan **Pro = números ilimitados**. Los números no dependen del número de usuarios.
- Si comparten una sola licencia, no podrán filtrar/reportar por vendedor; alternativa: **etiquetar los leads con el nombre del vendedor responsable**.
- Kommo está restringiendo cada vez más el uso compartido de licencias (ver "Has alcanzado el límite de sesiones").
Video: https://www.loom.com/share/084a0d0fe0ca4290a1bc192224ed8421

### ¿Cómo cambio la contraseña de un usuario? [USO]
Parte inferior izquierda → clic en tu **usuario** → **Configuración del perfil** → campo Contraseña → nueva contraseña → **Guardar** (arriba a la derecha).
Video: https://www.loom.com/share/45844fd61f814f47b3dab413349af316

### Me sale "Has alcanzado el límite de sesiones" [ERROR]
- **Causa:** varias personas están conectadas al mismo tiempo con **una sola licencia**. Kommo cambió sus políticas para que cada persona tenga su licencia.
- **Solución inmediata:** normalmente basta con **cerrar la ventana emergente** y seguir trabajando.
- **Si ya los desconecta** a ti o a tu equipo: hay que **comprar licencias adicionales** (Facturación → Agregar licencias).
- Recomendación: compra **de forma escalonada**. Si son 3 personas con 1 licencia, agrega **una** primero y prueba; muchas veces con eso se resuelve.
Video: https://www.loom.com/share/88c6f972363740cb81cc16bbd5bbd107

---

## 2. Configuración inicial

### ¿Cómo paso del menú clásico al menú nuevo (o al revés)? [USO]
Parte superior izquierda → **Perfil** → **Menú izquierdo** → elige **Menú nuevo (Beta / New Left Menu)** o **Menú clásico** → Guardar.
En el menú nuevo: **Comunicación** (inbox; filtro "Sin respuesta" muestra los leads que esperan respuesta), **Chats de equipo** (mensajes internos), **Embudos** (desplegable para brincar entre embudos), **Tareas** y **Plantillas**.
Video: https://www.loom.com/share/02720e309df94318a40a38d792c8344b

### ¿Cómo vinculo mi celular / WhatsApp a Kommo? (WhatsApp Lite) [DESCONEXIÓN] [USO]
1. Ten tu celular con **WhatsApp Business** (de preferencia).
2. En Kommo: parte inferior izquierda → **Configuración del espacio de trabajo** → **Centro de integraciones** → busca **WhatsApp Lite**.
   - ⚠️ No elijas "WhatsApp Business" (esa es la API oficial de Meta; no es la que usamos al inicio).
3. **Agregar número** → elige Android o iPhone → aparece un **código QR**.
4. En el celular: WhatsApp → Configuración → **Dispositivos vinculados** → **Vincular nuevo dispositivo** → escanea el QR.
5. Kommo te regresa a la pantalla y el número queda conectado.
Video: https://www.loom.com/share/35a91fbe07354b29982db3282c7abb37

### ¿Cómo agrego otro número de WhatsApp y lo mando a otro embudo? [USO]
1. Crear embudo extra: **Leads → Automatizar** (arriba a la derecha) → arriba a la izquierda **Añadir pipeline / embudo** (+).
2. Vincular número: Ajustes → **Integraciones** → **WhatsApp Lite** → agrega el número y escanea el QR.
3. Al regresar a la pantalla, **elige a qué embudo deben caer** las conversaciones de ese teléfono.
4. Puedes **renombrar el dispositivo** (clic sobre él) para distinguirlos.
- Usos: embudo postventa, citas recurrentes, otra línea de negocio, otro equipo.
Video: https://www.loom.com/share/642fb8e8140747628723681ccc280726

---

## 3. Personalizar el CRM

### ¿Cómo edito mi embudo de ventas (etapas)? [USO]
Leads → arriba a la derecha **Editar embudo** → **Añadir etapa** o elimina etapas → **Guardar**.
- Recomendado: **5 a 8 etapas**.
- Colores: fríos (azul/morado) para etapas tempranas, cálidos (naranja/rojo) para las cercanas al cierre.
- Etapas finales: **Logrado con éxito / Ganado y cerrado** y **Perdido / Descalificado**. Al marcarlas, el lead sale del embudo.
- Mantén pocos leads vivos en el embudo; con más de ~100 el seguimiento se vuelve inmanejable.
Video: https://www.loom.com/share/e669e95ad58243209a9e5cf16cbc94cc

### ¿Cómo elijo qué información se ve en la tarjeta del lead en el embudo? [USO]
En el embudo → arriba a la derecha **Editar → Diseño de la tarjeta** → elige los campos (nombre de empresa, presupuesto, contacto, notas de seguimiento, servicio de interés…) → marca **Aplicar para todos los embudos**, **Mostrar avatar** y **Mostrar último mensaje** → Guardar.
Así ves lo importante de un vistazo sin abrir cada lead.
Video: https://www.loom.com/share/6985e45128804230a74cdd7b110f0003

### ¿Cómo creo campos personalizados en la ficha del prospecto? [USO]
1. Abre cualquier lead → **Configurar** (en la ficha).
2. **Agregar campo** → elige el tipo correcto: texto corto, texto largo, número, selección (desplegable), fecha, fecha y hora, URL, etc.
3. Nombre del campo → Visible → Guardar → Cerrar.
- El campo se aplica a **todos los embudos y todos los leads**.
- Ubica los campos importantes **arriba** en la ficha.
- Elige bien el formato: si el campo es "fecha" no podrás meter un link, etc.
- Los campos se pueden usar como **campos dinámicos en plantillas** (ej. "te recuerdo que el día {fecha de la llamada} tenemos Zoom").
Video: https://www.loom.com/share/f0d2608130814fd0ac12cdced12fdaa2

### ¿Cómo renombro un embudo? [USO]
- **Menú nuevo:** Pipelines/Embudos (lado izquierdo) → despliega → **tres puntitos** junto al embudo → **Renombrar**.
- **Menú clásico:** Leads → Automatizar → arriba, clic sobre el nombre del embudo para renombrarlo.
Video: https://www.loom.com/share/baf3982702c84d1285b4cb0f6338b715

### ¿Cómo doy de alta un lead manualmente? [USO]
Leads → arriba a la derecha **Nuevo lead** → nombre del lead → **Añadir contacto** (nombre, teléfono **con lada, ej. +52 1…**, correo) → servicio de interés y demás campos → **Compañía** = empresa o institución → **Guardar** → asígnalo a tu WhatsApp de ventas.
- ⚠️ Si al escribir el nombre Kommo lo vincula a un contacto existente equivocado, usa **Unlink / Desvincular**.
- Buena práctica: **primero llamar**, luego WhatsApp con plantilla.
Video: https://www.loom.com/share/556eac6d4d574beba34bd8de08368c2c

---

## 4. Problemas con leads

### ¿Por qué tengo leads duplicados y cómo los fusiono? [ERROR]
- **Causa común:** el prospecto llena un **formulario** (landing/lead form, llega con correo y más datos, a veces con etiqueta "Zapier") **y además manda WhatsApp** (llega solo con el número). Kommo crea dos leads.
- **Opción 1:** si ya conversas con él por WhatsApp, **borra** (bote de basura) el lead del formulario.
- **Opción 2:** clic en el aviso rosa **"Duplicado"** → revisa Lead 1 y Lead 2 → **Fusionar (Merge)** → Continuar.
Video: https://www.loom.com/share/6f5cb639ba844d77998aa5ebfd51c114

---

## 5. Taller de ventas

### ¿Cómo entro a los módulos grabados del taller? [USO]
1. Busca en el **correo personal que nos compartiste** un mail de **Hotmart** (revisa Spam, Promociones, Social). Si no lo encuentras, avísanos por el grupo de WhatsApp para reenviarlo.
2. Clic en **Acceder al contenido** → crea tu contraseña.
3. Con el link del curso que mandamos al grupo, entra al curso **"Leads e inscripciones"** → inicia sesión con tu correo → te llega un **código** al correo → confírmalo.
4. Dentro verás los módulos; cada módulo tiene varias sesiones.
- Pueden entrar varias personas con el mismo correo y contraseña.
- ¿Olvidaste la contraseña? hotmart.com → Login → **Acceder a mis compras** → **Olvidé mi contraseña**. (No se cobra nada extra.)
- URL del curso: https://hotmart.com/en/club/educonnect-marketing-educativo/products/
Video: https://www.loom.com/share/d1a3d3f1eeeb4c2d9e0b264c0c9c980e

---

## 6. Seguimiento de leads (uso diario)

### ¿Cómo muevo un lead a otra etapa del embudo? [USO]
- **Arrastra** la tarjeta del lead a la etapa correcta (drag & drop).
- Si no se deja arrastrar: abre el lead → en la ficha, clic en la **etapa del embudo** → elige la etapa.
Video: https://www.loom.com/share/5811ea6ea738430683d3b5af07e2b984

### ¿Cómo veo los mensajes que no he respondido? [USO]
**Chats** → botón verde (filtro) → **Sin responder / Unanswered**. Muestra todos los leads que escribieron (WhatsApp, Instagram, Facebook, web) y esperan respuesta. Ábrelos uno a uno y responde con plantilla o llamada.
- Si el lead solo contestó "ok, gracias", ábrelo y usa **Marcar como respondido (Mark as answered)** para que deje de aparecer.
- Meta de respuesta: **menos de 5 minutos** (ideal llamar en los primeros 2 minutos).
Videos: https://www.loom.com/share/c992a0fc1dbe4a1788039aa206edc921 · https://www.loom.com/share/2bb7bdb63e904bc7b9307e8b5b61133a

### Somos varios vendedores: ¿cómo veo solo MIS mensajes sin responder? [USO]
Chats → **Sin responder** → agrega el filtro **Usuario responsable** = tu usuario → Aplicar → **Guardar (Save)** el filtro con un nombre (ej. "Manu sin responder"). La próxima vez solo das clic en el filtro guardado.
- La cuenta maestra sin filtro ve los de todo el equipo (útil para auditar).
- También se puede filtrar por últimos X días o por etapa.
Video: https://www.loom.com/share/ff7577d99c864b26b251f5acc77c8bdd

### ¿Cómo cierro un lead como ganado o como perdido/descalificado? [USO]
Abre el lead → en la ficha, clic en la **etapa** → elige **Cerrado y ganado** (o como lo hayas nombrado: inscrito, logrado con éxito) → Guardar. Sale del embudo y cuenta para tus reportes y objetivos de venta.
Para descalificar: igual, elige **Cerrado y perdido / Descalificado** → elige el **motivo** (baja calidad, sin interés, sin presupuesto, no respondió) → Guardar.
Video: https://www.loom.com/share/11ac556f771a43b998ac3e1f6d037dd1

### ¿Cómo registro mis llamadas en el CRM? [USO]
Abre el lead → pestaña **Notas** → escribe el resultado (ej. "Buzón" o los acuerdos: "llamar el viernes, le interesa X") → **Añadir**. Kommo guarda fecha y hora.
- También puedes usar un campo personalizado "Notas de seguimiento".
- Con licencias avanzadas puedes filtrar el historial del lead para ver solo notas.
- Todo contacto (llamadas y WhatsApp) debe quedar registrado para poder auditar el seguimiento.
Video: https://www.loom.com/share/c757709e541d47a6a545d120d14f750e

### ¿Cómo agendo un recordatorio (tarea) para un lead? [USO]
Abre el lead → abajo cambia a **Tarea (Task)** → fecha y hora de vencimiento → asunto (ej. "Regresar llamada") → **Set / Guardar**. Kommo te manda una notificación (con sonido) a la hora indicada.
Todas tus tareas, incluidas las vencidas, se ven en **Calendario / Tareas**.
Video: https://www.loom.com/share/423cca9488b2412b8102a84e01cad06c

### ¿Cómo distingo un lead de formulario de un lead de WhatsApp? [USO]
- **Formulario** (web, Facebook/Instagram lead form): llega con **más datos** (nombre, correo, servicio/nivel de interés), a veces con etiqueta "Zapier", y **sin ícono de WhatsApp**. No puedes chatear hasta corregir el teléfono.
- **WhatsApp**: llega solo con número y mensaje, con el **ícono de WhatsApp**; ya puedes chatear.
Video: https://www.loom.com/share/c7daee64794e46f89694f654ed3f16c3

### Me llegó un lead de formulario y no puedo mandarle WhatsApp [ERROR]
**Causa:** el teléfono no viene en formato internacional de WhatsApp.
1. Abre el lead → edita el **teléfono** → agrega la lada al inicio (**México: +52 1**) → clic fuera del campo → **Guardar** (abajo a la izquierda).
2. Clic en el teléfono → **asígnalo a tu número de ventas**.
3. Se activa el campo de chat abajo a la derecha → escribe o manda plantilla.
- Hazlo desde computadora (la app móvil de Kommo no es cómoda para esto).
- Verifica en WhatsApp Web que el mensaje sí llegó.
Video: https://www.loom.com/share/c1c3c421df6c48d090eb91a1d98b87d8

### ¿Cómo mando archivos pesados (videos, PDF, cotizaciones)? [ERROR] [USO]
- No conviene mandar adjuntos grandes desde Kommo: es lento y **archivos de más de ~10 MB a veces no se envían**.
- Mejor: manda la plantilla desde Kommo y el archivo desde **WhatsApp Web** (web.whatsapp.com, escanea el QR con WhatsApp Business). Lo que mandas por WhatsApp queda vinculado automáticamente en Kommo.
- Ten ancladas las dos pestañas (Kommo y WhatsApp Web).
Video: https://www.loom.com/share/6b107cbfc679449fb7e99be213ecd4f5

### ¿Cómo actualizo muchos leads a la vez? (actualización masiva) [USO]
1. Elige el embudo (o "Todos los leads" para todos los embudos).
2. Filtra con la barra de búsqueda: periodo, etapas, etiquetas (**OR** = cualquiera de las etiquetas; **AND** = que tenga todas).
3. Arriba a la derecha **Seleccionar múltiples** → marca los leads o toda la etapa.
4. Acciones: **cambiar etapa / mover a otro embudo, reasignar vendedor, cambiar un campo, añadir etiquetas, añadir tareas, borrar**.
5. Si pregunta "solo página actual" o "toda la cuenta", **toda la cuenta = todos los leads del filtro** (no todo el CRM).
- Ejemplo: descalificar todos los leads del ciclo escolar anterior en un solo paso.
Video: https://www.loom.com/share/a1011f55af164da1912dd1b4a1cfd2a6

### ¿Cómo uso etiquetas para contar los seguimientos? [USO]
Cada vez que das un seguimiento, pon la etiqueta **Seguimiento 1, 2, 3, 4…** en el lead (arriba en la ficha), conteste o no.
- Criterio de referencia del taller: en ~3 semanas, **hasta 4 WhatsApps y 4 llamadas**. Si un lead de etapas altas (frío) no avanza, se descalifica. Los de etapas bajas (ya cotizados) se revisan caso por caso.
Video: https://www.loom.com/share/fb7d98acf41c429c8916d4ebd8450351

---

## 7. Plantillas

### ¿Cómo creo una plantilla de chat? [USO]
**Automatizaciones → Plantillas → Plantillas de chat → Nueva plantilla** → elige **Plantilla general**.
- ⚠️ No uses "Plantilla de WhatsApp": esas son las que valida Meta y solo aplican con **WhatsApp Business API**. Con WhatsApp Lite/Business normal se usa la **general**.
- **Nombre** jerárquico para encontrarla rápido: `empresa.servicio.etapa.situación` (ej. `edu.web.entrante.gracias`, `edu.web.entrante.sinrespuesta`; en un colegio: `primaria.entrante.gracias`).
- Revisa la vista previa de celular: que el texto tenga buenos espacios.
Video: https://www.loom.com/share/1d334b9928ae41aeb7b4278ef610babd

### ¿Cómo uso campos dinámicos en plantillas? (nombre, vendedor, etc.) [USO] [ERROR]
Los campos dinámicos van entre **corchetes/llaves** y se llenan solos: nombre del contacto, usuario responsable, nombre del lead, campos personalizados.
- ⚠️ Si copias la plantilla desde Excel, **Kommo no reconoce el campo**: borra el corchete y vuelve a escribirlo para que lo detecte.
- **Nombre del lead ≠ nombre del contacto**: el nombre del lead es la **oportunidad** (ej. "página web", "primaria").
Video: https://www.loom.com/share/1d334b9928ae41aeb7b4278ef610babd

### ¿Cómo mando una plantilla a un lead? [USO]
Abre el lead (desde el embudo o desde **Chats**) → abajo a la derecha escribe **/** (diagonal) → busca la plantilla por su nombre → envía.
- ⚠️ Asegúrate de estar en la pestaña **Chat** (no en Notas ni Tarea). Si no aparece "Chat", elige tu número de WhatsApp. Si estás en Notas, el mensaje **no le llega al prospecto**.
Video: https://www.loom.com/share/168257a068ae41b785b7ead3f9f37148

### ¿Qué es un flujo de conversación con plantillas? [USO]
Una serie de plantillas encadenadas (ej. `agendar.paso1`, `agendar.paso2`…) que guían al prospecto a dar sus datos o tomar una acción (agendar, enviar correo). Consejo: **fusiona pasos** para tener menos plantillas.
Ruta mencionada en el video (menú anterior): Ajustes → Herramientas de comunicación → Agregar plantilla.
Video: https://www.loom.com/share/32df6471625e4287be55f1c93c032659

### ¿Cómo lleno el Excel de plantillas (línea recta)? [USO]
- El Excel replica las **etapas de tu embudo**; cada etapa tiene su criterio y sus plantillas.
- **Entrante:** primero llamar (atender en los primeros minutos). Dos plantillas: "Gracias por tomar la llamada" y "No logré encontrarte" (con prueba social: fotos, página, redes).
- **Contactado/Respondió:** los seguimientos 1–4/5 dentro del ciclo que definiste (ej. 15 días). El 1º y 2º seguimiento en las primeras 24 h (si llegó en viernes, el lunes).
- **Etapa media** (cotización, visita, examen): recordatorios (al agendar, un día antes, unas horas antes).
- **Etapa baja:** cierre (documentación, pago) con sus seguimientos.
Video: https://www.loom.com/share/8d90c33fafb4460faea1535c02036e55

### ¿Cómo creo mis plantillas con ChatGPT? [USO]
Prompt base: "Eres experto en ventas, trabajas en **[dónde]**, ofreces **[qué]** a **[a quién]**. Propuesta de valor: **[4–5 puntos]**. Tu objetivo es dar seguimiento por WhatsApp Business generando valor, atacando un punto de dolor, generando FOMO o resaltando beneficios. Nuestro embudo: **[etapas con su descripción]**. Crea 5 plantillas de WhatsApp por cada etapa para empujar al lead al cierre."
- Hazlo **servicio por servicio**.
- Después: "Mejora esta plantilla que enviaremos por WhatsApp, hazla más persuasiva."
- Úsalo como base y corrígelo; no lo copies tal cual.
Video: https://www.loom.com/share/161b34893b954244b4546614a1d27892

---

## 8. Embudos

### ¿Cómo creo un embudo postventa sin afectar mis reportes de ventas? [USO]
1. Marca el lead original como **Cerrado y ganado / Inscrito** (pon en **Presupuesto** el monto, ej. la primera mensualidad).
2. En ese lead: **tres puntitos → Abrir detalle** → ve a la **compañía/familia** → **Agregar lead rápido** con un **nombre nuevo** (ej. "POST 2026 Secundaria – Daniel"), **sin presupuesto**, en el embudo **Postventa** y su etapa inicial.
3. Da seguimiento postventa ahí (útiles, uniformes, fechas, comunicados). Al terminar, mándalo a una etapa **"Finalizado"**, no a "Cerrado y ganado".
- ⚠️ **No muevas el lead ganado al embudo postventa**: eso lo saca de "ganado" y descuadra tus inscritos/ventas. Siempre crea un lead nuevo.
- Estructura: **Compañía** = familia; **Contactos** = papá/mamá; **Lead** = cada aspirante/oportunidad.
Video: https://www.loom.com/share/bdc215d6666849f5b0f9761684846f4a

### ¿Cómo registro varias compras de un mismo cliente o empresa? [USO]
Crea un **lead nuevo por cada compra/oportunidad**, ligado a la misma **compañía** y contacto (mismo principio que el embudo postventa).
Video (sin transcripción, revisar): https://www.loom.com/share/6f6daff0c45748dd9f34e125a335717a

---

## 9. Gerencia: auditar la ejecución comercial

### ¿Qué reviso para auditar el seguimiento de mi equipo? (indicadores) [USO]
1. **Ningún lead entrante abierto más de 5 minutos** (fines de semana: al día siguiente).
2. **Frecuencia de contacto** constante (sin huecos de días/semanas).
3. **Llamadas registradas** (no solo WhatsApp).
4. **Calidad de las plantillas** (que aporten valor: casos de éxito, prueba social, beneficios; no robóticas).
5. **Número de seguimientos** según el criterio acordado (ej. 4 WhatsApps + 4 llamadas en ~3 semanas, o 5 toques en 15 días). Si no avanza, se descalifica.
Video: https://www.loom.com/share/ee107672cc254f87889f87c59ffb4c89

### Línea de defensa 1: reporte fecha de creación vs. última modificación [USO]
Leads → **Todos los leads** → filtra embudos, **todas las etapas** y un **periodo** (ej. 1–31 de agosto) → Aplicar → vista de lista → **Ajustes de lista**: agrega Nombre del lead, Contacto principal, **Fecha de creación**, **Última modificación**, Estatus (arrastrar y soltar) → marca "aplicar para todos los usuarios".
- Si **creación y última modificación están muy cerca** (ej. 1 y 4 de agosto) → no hubo seguimiento.
- Leads de hace 2 meses **no deberían seguir vivos**: ya debieron ganarse o descalificarse.
Video: https://www.loom.com/share/92f12d15f01743158fbdbca83ab13543

### Línea de defensa 2: leads que se están enfriando [USO]
En el embudo, ordena por **Último evento**: arriba los contactados más recientemente, **abajo los más fríos**. Abre los de abajo de cada etapa y revisa: ¿cuándo fue el último contacto, hubo solución de objeciones, se condujo al siguiente paso, los seguimientos aportaban valor?
- "Si no está en el CRM, no existe" (lo que está solo en el celular personal no cuenta).
Video: https://www.loom.com/share/026bb2153d4a479191cc3cbaf01b5740

### Línea de defensa 3: auditar por número de toques (etiquetas) [USO]
Compara la **etiqueta de seguimiento** (Seguimiento 1, 2, 3…) con la **fecha de creación** del lead: ¿lleva los toques que le tocan en ese tiempo?
- Cada etapa tiene su número de toques (ej. cita agendada = 2 recordatorios + confirmación el mismo día).
- Tip: colores en etiquetas (1–2 gris, 3–4 naranja, 5 rojo).
Video: https://www.loom.com/share/4bfb1eaa23da421fb12d72c5bdbc5c0d

### Línea de defensa 4: vista de lista por embudo [USO]
En cada embudo → **vista de lista** → revisa **Última modificación**. Regla general: leads de la parte alta contactados **cada 2–3 días**; **ningún lead más de una semana sin contacto** (los de decisión, al menos 1 vez por semana). Si hay tarea/recordatorio agendado con un compromiso, puede estar bien.
Video: https://www.loom.com/share/8b656c36a31f4b2abd8eb1adb0b2d60e

---

## 10. Reportes

### Me bloquearon WhatsApp / ¿cómo veo cuántos mensajes mandamos? [ERROR] [DESCONEXIÓN]
Cuando hay un bloqueo de WhatsApp Business, lo primero es revisar el volumen de mensajes:
**Insights (Reportes) → Registro de actividades** → filtro arriba: **periodo**, **usuarios**, **todos los objetos**, tipo de evento: **Mensaje entrante, Mensaje saliente, Conversación comenzada** → OK → **Guardar** el reporte.
- Según el video, el límite de referencia de Meta es **~200 mensajes al día** (verificar política vigente).
- Causas comunes de bloqueo: exceder el volumen, **listas de difusión**, copiar y reenviar el mismo mensaje a muchos contactos, o que uno o varios contactos te **reporten como spam**.
Video: https://www.loom.com/share/a08142815da1410db5126024cb08dacc

### ¿Cómo pongo objetivos de venta por equipo o vendedor? [USO]
Requiere **plan Avanzado** o superior. Parte inferior izquierda → **Reporte de objetivos (Goal report)** → arriba a la derecha **Setear objetivos** → elige periodo (mes, trimestre, año) → monto global por oficina y/o por vendedor; en **pesos** o en **cantidad** de ventas → **Save**.
- El tacómetro del Dashboard sube conforme marcas leads como **Cerrado y ganado**.
- Si el dashboard muestra 0: revisa que esté **filtrado por el usuario correcto**.
Video: https://www.loom.com/share/ddcf236a6ec3434e9ef3268b6aff600e

### ¿Dónde aprendo sobre los widgets del Dashboard? [USO]
Documentación oficial de Kommo: https://www.kommo.com/support/crm/dashboard-widgets-advanced/

---

## 11. Integraciones

### ¿Cómo conecto Facebook e Instagram a Kommo? [USO] [DESCONEXIÓN]
Ajustes → **Integraciones** → **Facebook** → Instalar → inicia sesión con el **perfil personal que administra la Fan Page** → elige la(s) Fan Page(s) y cuenta(s) de Instagram → activa **Messenger, comentarios** y DMs de Instagram. Se pueden agregar varias páginas.
- Necesitas usuario y contraseña de Facebook (administrador de la página) e Instagram.
- Si anuncias en Meta, es obligatorio tener Fan Page.
- Si manejamos tu publicidad y no sabes qué formularios elegir, pregunta a tu administrador de cuenta.
Video: https://www.loom.com/share/ef3d733d553f4f8087dbe6d48d029c67

### ¿Cómo hago que los lead forms de Meta caigan a un embudo específico? [USO]
En la integración de Facebook → pestaña de **Lead forms** → agrega los formularios de tus campañas → **Mapear campos** (nombre → nombre, programa de interés → campo/nombre del lead) → **Ajustes del formulario**: agrega **etiquetas** (ej. "Campaña enero 2026") y elige el **embudo** destino.
Video: https://www.loom.com/share/f5e2c34ad5dc4ccf8a673cf162c2cc7f

### ¿Cómo conecto mi correo (Gmail) a Kommo? [USO]
Configuración del espacio de trabajo → **Centro de integraciones** → busca **Gmail / Google** → Instalar → Conectar → inicia sesión con tu cuenta.
- Solo funciona con **Gmail o Google Workspace** (correos empresariales que se ven en Gmail).
- Después aparece **Inbox de correo** en Comunicación. Desde la tarjeta del lead: clic en el correo → **Escribir desde Kommo**. Muestra si el correo fue **leído**.
Video: https://www.loom.com/share/7ff6f63790c14d9cb2f32d1883d07aee

### ¿Cómo creo plantillas de correo y mi firma? [USO]
**Automatizaciones → Plantillas → Plantillas de correo → Agregar** → nombre, **Tema (asunto)** atractivo, cuerpo → Guardar.
- Pocos campos dinámicos disponibles en correo (nombre del contacto, nombre del lead, usuario responsable).
- No admite HTML ni formato de Word avanzado.
- **Firma:** Inbox de correo → **tres puntitos** → agregar firma. Copia y pega desde Word; las firmas de varias columnas no se pegan bien (usa formato vertical).
Video: https://www.loom.com/share/905c40b93f094bdd8fe77039293af89b

### Twilio (llamadas desde Kommo): pasos de configuración [TÉCNICA]
1. Crear cuenta gratuita en Twilio. 2. Upgrade a cuenta de pago y verificación de datos. 3. **Paquete de regulaciones** (México: constancia de situación fiscal + comprobante de domicilio). 4. Comprar número local. 5. Instalar la app de Twilio en Kommo y poner **Account SID** y **Auth Token** (están en el Dashboard de Twilio). 6. Si no funciona, revisa **permisos geográficos** en Twilio. 7. Llamada de prueba. 8. Recargar saldo.
(Fuente: texto del manual. Uso y recarga: ver sección 16.)

---

## 12. Automatizaciones

### ¿Cómo creo un bot de fuera de oficina? [USO]
Requiere plan con **Salesbots** (Avanzado o superior).
1. (Opcional) Crea la plantilla: Automatizaciones → Plantillas → Plantillas de chat → **Plantilla general** (no "de WhatsApp", esa es para la API).
2. Automatizaciones (o en menú clásico: Ajustes → Herramientas de comunicación) → **Crear** → **"Take a message when you're offline / Toma un mensaje fuera de oficina"** → nombre "Bot fuera de oficina" → mensaje o plantilla → Guardar y continuar.
3. Disparador: **Cuando se crea en una etapa** → etapa **Lead entrante** (recomendado solo para leads nuevos, no para conversaciones activas).
4. Horario: lun–vie de 00:00 a tu hora de entrada y de tu hora de salida a 23:30; sáb y dom todo el día.
5. Activa **"Dejar el mensaje sin respuesta"** para que tu equipo vea esos leads como pendientes. **No** marques "aplicar a todos los leads en esta etapa". → Finalizado.
Video: https://www.loom.com/share/e9d57a7811e948639147ca967d93f90b

---

## 13. Pendientes

**Sin transcripción en Loom (revisar el video a mano):**
- "Actualizar nombre/producto de interés de cada prospecto": https://www.loom.com/share/9f0f96338cd14987ac0c6759f4024671
- "Varias compras de una misma compañía": https://www.loom.com/share/6f6daff0c45748dd9f34e125a335717a
- "Registrar llamadas y mensajes es importante": https://www.loom.com/share/fe3dfe4a1f9641e993de82c2fbc3a31b (contenido cubierto por "¿Cómo registro mis llamadas?")

**Sin video en el manual:** "Reporte de leads ganados/inscritos/cerrados".

**Desconexiones:** cubiertas en la sección 17 (fuentes oficiales de Kommo y WhatsApp). Validar con casos reales de clientes.

---

## 14. Soporte técnico y errores

### ¿Cómo contacto al soporte técnico de Kommo? [TÉCNICA]
Parte inferior izquierda → **Ayuda (Help Center)** → **Chatear con soporte (Chat with support)** → describe el problema y **adjunta captura de pantalla**.
- Nosotros (Digital Crew / EduConnect) somos expertos en ventas e implementación; las **fallas de la plataforma** (intermitencias, sincronización, licencias, funciones que no responden) las resuelve el **soporte de Kommo**.
- ⚠️ No suelen llegar notificaciones cuando soporte responde: **revisa el chat cada 30–60 minutos**.
- Suelen responder en **1–2 horas entre semana**; los fines de semana tardan un poco más.
Video: https://www.loom.com/share/753d83b6cf484491be9bd871fd089d32

### ¿Cuántas personas pueden entrar con una licencia? (ventana emergente de sesiones) [ERROR]
Kommo ya no permite conexiones ilimitadas con una sola licencia. Lo que hemos observado:
- **Hasta 2 personas simultáneas por licencia**: funciona; si sale la ventana emergente, solo **ciérrala** y sigue trabajando.
- **3 o más personas**: Kommo **saca (desconecta) a alguien**. Solución: comprar más licencias (de una en una).
Video: https://www.loom.com/share/e91b78fb7a544a189179c9056513d758

### No me llegan los mensajes de WhatsApp a Kommo, o llegan tarde [DESCONEXIÓN] [ERROR]
Tranquilidad: **ningún mensaje se pierde**; siempre quedan en tu WhatsApp del celular. Suele pasar en mantenimientos de Kommo (aprox. cada dos meses).
1. **Revisa que tu número esté conectado:** Ajustes → Integraciones → **WhatsApp Lite** → tu número debe tener **palomita** (no círculo gris).
2. **Refresca** la página.
3. Si sigue igual: arriba a la izquierda **cierra sesión**, cierra la pestaña, ábrela de nuevo y vuelve a entrar.
4. Si no se resuelve: **levanta un ticket con soporte de Kommo** (Ayuda → Chatear con soporte).
Video: https://www.loom.com/share/568bc8b9022647989c97fa5e4b1cd8e8

### No se envían mis mensajes desde Kommo [ERROR]
**Cómo saber si se envió:** un mensaje enviado aparece en **globo blanco** con palomita (enviado/leído). Si aparece con **fondo gris**, **no se envió**: quedó como nota interna.
- **Caso 1 – fondo gris / quedó como nota o Salesbot:** abajo, en el selector de canal, elige **Chat** → clic en el número del lead → elige tu **número de ventas** → reenvía (texto, audio o plantilla con "/").
- **Caso 2 – leads de Instagram o Facebook (error "la ventana permitida por Meta se cerró"):** Meta cierra la conversación si el lead pasa varios días sin responder (en el ejemplo, ~15 días). No es falla de Kommo. Solución: escríbele **directamente desde la app de Instagram/Messenger** en el celular para reabrir la conversación.
- **Caso 3 – error "número desconectado de WhatsApp Business" o "debes enviar una plantilla para reactivar la conversación":** pasa cuando se instaló **WhatsApp Business API** (la oficial de Meta). En la API: Meta **cobra por mensaje**, la ventana es de **24 horas** y si el lead no contesta solo puedes escribirle con una **plantilla aprobada por Meta**. Recomendación: usar **WhatsApp Lite** (vinculado a tu WhatsApp Business del celular), que no tiene esas restricciones. Si apareció "desconectado", revisa también la palomita de tu número en WhatsApp Lite.
Video: https://www.loom.com/share/2a45e25948be46cbb9287707fb9a3fd4

### Mando mensajes desde mi número pero salen del celular de mi compañero [DESCONEXIÓN] [ERROR]
**Causa:** tu celular **se desvinculó** de Kommo. Cuando eso pasa, Kommo manda el mensaje desde el número de la **cuenta maestra** u otro número conectado.
1. Ajustes → **Integraciones** → **WhatsApp Lite** (instalado).
2. Revisa tu número: **palomita = conectado**; **círculo gris = desvinculado**.
3. Si está gris: dale a la **X** (desvincular) y **vuelve a agregarlo** escaneando el QR (Dispositivos vinculados en tu WhatsApp).
4. **Ponle nombre** al teléfono (ej. el nombre del asesor) para identificar desde qué número sale cada mensaje.
Video: https://www.loom.com/share/4dfc715ad2964bb2a248ef4f8fe1c37e

### Edito un embudo y los cambios no se guardan (o se borran en otro embudo) [ERROR]
Pasa en cuentas con **varios embudos**: al editar desde el menú de **tres puntitos → Editar embudo**, al guardar uno se revierte el otro.
**Solución:** edita desde **Leads → Automatizar** (arriba a la derecha) → elige el embudo correcto (arriba a la izquierda) → haz los cambios → **Guardar**. Luego cambia al otro embudo y repite.
Video: https://www.loom.com/share/e05dc16c961941e7b0595dc22664ae66

### Mis leads tienen un candado / no puedo crear ni editar leads [ERROR]
Causas posibles, en este orden:
1. **Pago de licencia atrasado o recién reactivado:** el sistema puede tardar **1–2 días** en detectar el pago. Truco sugerido por soporte de Kommo: Ajustes → **Generales** → cambia la **zona horaria** (ej. a otra de México) → Guardar.
2. **Excediste el número de licencias** (Facturación muestra "excediste tus licencias"): **compra más licencias** o **elimina/desactiva un usuario** en Gestión de usuarios → Remove user.
3. **Excediste el número de leads** permitido en tu plan.
Si nada funciona: ticket con soporte de Kommo.
Video: https://www.loom.com/share/cd8a88f1295240139b4639b9c142ddae

### ¿Cómo fusiono leads duplicados manualmente? [ERROR]
1. Busca por **teléfono** en la barra de búsqueda + Enter (a veces uno está con +52 y otro sin él). Ábrelos en pestañas para comparar.
2. Arriba a la derecha **Seleccionar varios** → marca los dos → **Combinar / Fusionar**.
3. En la pantalla de fusión, elige todas las etiquetas y, en el **contacto/teléfono, el que tiene la conversación (con +52)**. ⚠️ No elijas el que no tiene conversación.
4. Fusionar → espera unos segundos → Continuar.
Video: https://www.loom.com/share/27380e4f852a4f9896d3fb42fee69ab4

### Cada mensaje del mismo cliente me crea un lead nuevo (demasiados duplicados) [ERROR]
**Causa habitual:** se usa **"Cerrar conversación" (Close conversation)** cuando el lead solo dijo "gracias". Al volver a escribir, Kommo crea un lead nuevo.
- Usa **"Marcar como respondido / resuelto" (Mark as answered)**, no "Cerrar conversación".
- Para evitarlo del todo: Ajustes → **Herramientas de comunicación** → hasta abajo ("cuando un lead te mande un mensaje y no tengas una conversación vigente…") → elige **"Añadir la conversación a un lead existente"** → Guardar.
Video: https://www.loom.com/share/06aa45a6374549b7ad1aa7163b3a1cb6

### ¿Cómo hago que los campos personalizados queden en el orden que quiero? [TÉCNICA]
Kommo no permite reordenarlos fácilmente. El truco:
1. Ten la lista de campos escrita (ej. en Word).
2. **Créalos todos de una sola vez** (sin cerrar la ventana de configuración a la mitad).
3. **Créalos en orden inverso** (del último al primero): Kommo los voltea y quedan en orden.
4. Elige bien el **tipo de campo** (fecha, texto, texto largo, número…): después no se puede cambiar y tendrías que rehacerlo todo. Texto largo para respuestas extensas (con texto normal se ve cortado).
Video: https://www.loom.com/share/8a677473aab14fa186b4e58f18ced04a

### Mis campos personalizados se ven cortados [USO]
1. **Pasa el cursor** sobre el campo: aparece el nombre completo.
2. **Arrastra la barra divisoria** de la tarjeta del lead hacia la derecha para ensanchar la columna (queda así para todos los leads).
3. Si aún se cortan: **acorta el nombre** de los campos.
Video: https://www.loom.com/share/5e13be60dae448b2b5b84179148ef646

---

## 15. Más configuración y uso diario

### ¿Por qué anclar Kommo y WhatsApp Web en el navegador? [USO]
- **Ancla la pestaña de Kommo** (clic derecho en la pestaña → Fijar/Anclar) para no tener que volver a iniciar sesión cada día.
- **Ancla también WhatsApp Web** (web.whatsapp.com) con el **mismo celular que está vinculado a Kommo**. Úsalo para notas de voz y archivos pesados (PDF, videos, portafolio).
- Todo lo que mandes por WhatsApp se sincroniza solo con Kommo; no se pierde nada.
Video: https://www.loom.com/share/7e17c584f6ec421bb63c99d6870e7818

### ¿Cómo configuro mi perfil y mi foto? [USO]
Cada vendedor entra con **su propio usuario** → arriba a la izquierda **Perfil** → idioma, **tu nombre** (a veces aparece el de la empresa), correo, contraseña y **foto** (clic en el ícono de la foto). Ayuda a distinguir quién atiende a cada lead.
Video: https://www.loom.com/share/9150cdc11813426289148a8b83d2679a

### ¿Cómo reasigno un lead a otro vendedor? [USO]
Abre el lead → en la ficha elige el **embudo y la etapa** correctos → cambia **Usuario responsable** al nuevo vendedor → **Guardar**.
Para muchos leads a la vez: actualización masiva (Seleccionar múltiples → reasignar).
Video: https://www.loom.com/share/70b60e66e2c5479ea88637b3cd998bdf

### ¿Cómo mando mensajes internos a mi equipo sobre un lead? [USO]
Abre el lead → en el chat escribe **@** y elige al compañero (requiere 2 o más usuarios) → escribe el mensaje → Send.
- ⚠️ Confirma que se marcó como **chat interno**: se ve en un tono **más claro** (gris claro o azul tenue), distinto a los mensajes enviados al prospecto. Si no, ¡se lo mandas al cliente!
- Revisa los mensajes internos en **Comunicación → Chats de equipo (Team chat)** → ordena por no leídos. Las alertas no siempre suenan; revísalo seguido.
Video: https://www.loom.com/share/a28e90e41c9640b9a7e25d412d1bf1ed

### ¿Cómo organizo mis plantillas por etapa del embudo? [USO]
- Crea plantillas para **cada etapa** (contactado: seguimiento 1–5; cotización: seguimiento 1–4; visita: recordatorios…).
- El **nombre empieza con la etapa**, luego el tipo: `contactado.seguimiento1`, `envio.cotizacion.web`, `cotizacion.seguimiento2`. Así al escribir **/contactado** solo aparecen las de esa etapa.
- Cada seguimiento debe aportar **valor** (portafolio, casos de éxito, datos, video), no solo "¿qué te pareció?".
Video: https://www.loom.com/share/a002a1c080ea443bbfbbff3f0fcfb986

### ¿Cómo encuentro los leads que llevan más tiempo sin contacto? [USO]
1. **Chats → Sin responder** (y filtros guardados por vendedor).
2. En el embudo: **tres puntitos → ordenar por Último evento** → los más fríos quedan **abajo**.
3. **Editar tarjeta del lead → Mostrar último mensaje**: aparece un globito en los leads que te escribieron.
4. **Vista de lista** → tres puntitos → **Ajustes de lista** → agrega **Última modificación** → ordena de más antiguo a más reciente.
- Un lead con meses sin contacto puede estar bien si está calificado a largo plazo; en etapas calientes (cotización enviada) es un error.
Video: https://www.loom.com/share/7f94e5ef95654ba29d51d01d9cd3d18a

### ¿Cuál es un proceso rápido para atender leads entrantes? [USO]
Mientras suena la llamada: 1) corrige el teléfono a **+52 1…**, 2) **asígnalo a tu número de WhatsApp**, 3) si no contesta, deja **nota "Buzón"**, 4) manda la plantilla **inicio / no respondió la llamada**, 5) mueve a **Contactado** y guarda. Siguiente lead. Así se atienden ~35 leads por hora.
Video: https://www.loom.com/share/2212eff2214c45fa93f1fa05d96c3c9d

### ¿Cómo hago que mis plantillas generen valor? [USO]
No digas "somos expertos": **demuéstralo** con evidencia en plantillas listas para momentos clave: **casos de éxito** con resultados, **portafolio en PDF**, **reseñas de Google**, redes y YouTube, videos (en colegios: primaria, extracurriculares; en servicios: instalaciones, equipo). Algo que la competencia no pueda mostrar.
Video: https://www.loom.com/share/56a509ddef2b4c90bc850bb7f60db14e

### ¿Cómo creo, ordeno o borro embudos y muevo leads entre ellos? [USO]
- **Crear:** Leads → arriba a la izquierda (lista de embudos) → **+** → nombre.
- **Mover un lead:** ábrelo → en la ficha elige otro **embudo y etapa** → Guardar.
- **Mover varios:** **Seleccionar múltiples** → **Cambiar etapa** → elige embudo y etapa → Guardar.
- **Ordenar o borrar:** Leads → **Automatizar** → arriba a la izquierda → **lápiz** → reordena o **Borrar** → Guardar.
- ⚠️ **No puedes borrar un embudo con leads activos**: muévelos primero a otro embudo.
Video: https://www.loom.com/share/a13f314f6cf64c84b5df365e07d80e8b

### ¿Cómo agrego varios contactos a un mismo lead? [USO]
Abre el lead → **Añadir contacto** → nombre y teléfono (formato +52 1…) → Guardar. Para escribirle a cada uno, elige el contacto y tu número arriba del chat. Toda la conversación de la oportunidad queda en un solo lead (ej. director + asistente + marketing; papá y mamá).
Video: https://www.loom.com/share/fc47bf1a110949ae887d950254d0d5a9

### ¿Qué son las etiquetas (tags) y para qué sirven? [USO]
Sirven para **agrupar leads con características similares** y filtrarlos: empresa/línea de negocio, nivel (primaria, secundaria, prepa), valor (alto/bajo ticket), **Seguimiento 1–4**, "hot", "mal seguimiento", campaña, etc. Se filtran desde la barra de búsqueda.
Video: https://www.loom.com/share/d31c63b3ade14fc8bf691f29b2afda6b

### ¿Cómo busco un lead o filtro mis leads? [USO]
- **Por nombre/apellido/teléfono:** escribe en la **barra de búsqueda** y presiona **Enter** (sin Enter solo ves sugerencias). "Activo/Current" = el lead vivo en el embudo.
- **Por etiqueta, fecha o etapa:** abre los filtros de la barra → elige etiquetas, periodo (ej. últimos 30 días; ⚠️ un filtro de fecha puede ocultar leads) y etapas (quita ganados/perdidos para ver solo activos) → Aplicar.
Video: https://www.loom.com/share/fe0803d1897941e0a38a31966436e22b

### ¿Cómo agrego o edito los motivos para descalificar un lead? [USO]
Leads → **Automatizar** → en la etapa **Venta perdida / Descalificado** → **Configuración** → agrega/edita motivos (sin presupuesto, proyecto en pausa, perdido con la competencia, no respondió…) → Guardar.
Útil después para campañas de remarketing por motivo.
Video: https://www.loom.com/share/2f0e07a94b4f4c0c9378815270adbda0

### ¿Cómo saco mi ciclo promedio de venta? [USO]
1. En el embudo, filtra **Leads ganados** y un **periodo reciente** (ej. últimos 2 meses).
2. **Vista de lista** → Ajustes de lista: Estatus, **Fecha de creación**, **Cerrado el**, contacto, nombre del lead.
3. **Exportar** (con **filtro activo**) a Excel.
4. Calcula el promedio entre fecha de creación y fecha de cierre (o pídeselo a ChatGPT con el archivo).
- ⚠️ Si registras varias compras en el **mismo lead** (en vez de crear un lead por oportunidad), el cálculo sale distorsionado. Usa datos recientes.
Video: https://www.loom.com/share/d8eddecbe62e4b0396c8e2853a184b0b

---

## 16. Integraciones, telefonía, importación y automatizaciones

### ¿Cómo conecto formularios de Meta o de mi página web a Kommo con Zapier? [TÉCNICA]
**Lead forms de Meta:**
1. En Zapier: **Create → New Zap**. (El formulario de Meta ya debe existir.)
2. **Trigger:** *Facebook Lead Ads* → evento *New Lead* → conecta la cuenta de Facebook que administra la Fan Page → elige **página y formulario** → Test (si no hay leads reales sale un "test lead"; está bien) → Continue.
3. **Action:** *Kommo* → **Create new lead with contact** → conecta tu cuenta de Kommo.
4. **Mapea** los campos con "/": nombre, teléfono, correo (y opcionales: etiquetas como "Campaña Meta", presupuesto, servicio). Campos obligatorios: **responsable**, **embudo** y **estatus/etapa** (normalmente *Incoming leads / Lead entrante*).
5. **Test** → revisa que llegó a Kommo → renombra el Zap → **Publish**.
**Formulario de landing page/web:**
- **Trigger:** *Webhooks by Zapier* → **Catch Hook** → copia la URL del webhook.
- Pide a tu desarrollador que la pegue en el formulario (en WordPress + Elementor: Formulario → Acciones después de enviar → **Webhook**). Llena el formulario de prueba.
- **Action:** Kommo → Create lead with contact → mapea los campos del webhook.
Video: https://www.loom.com/share/bf79939b7d8941f18975221ad56a3aaf

### ¿Cómo hago llamadas desde Kommo con Twilio? [USO] [TÉCNICA]
Abre el lead → clic en el **teléfono** → **Llamar con Twilio**. Al colgar aparece una ventana para registrar el **resultado** (buzón, acuerdos) → Guardar. Las llamadas quedan registradas y, si contestaron, se pueden **escuchar y descargar**.
- Reporte: **Insights → Reporte de llamadas** (por usuario y periodo).
- **Si sale la ventana pero la llamada no conecta:** refresca la página e intenta de nuevo.
- **Durante la llamada no des clic en nada más** del lead (etiquetas, menús), o no aparece la ventana para registrar el resultado.
- Si sigue fallando: cierra sesión y vuelve a entrar; si persiste, ticket con soporte de Kommo.
Video: https://www.loom.com/share/1ed0065e91824169b7e4c80a4c86a58b

### ¿Cómo recargo saldo en Twilio? [TÉCNICA]
Normalmente Twilio tiene **recarga automática** (cuando baja de unos USD 5–10 recarga ~USD 10). Si falló (ej. tarjeta bloqueada):
twilio.com → inicia sesión → **Admin → Billing (Account billing)** → **Add more funds** → monto (recomendado USD 20) → método de pago (puedes dejarla como principal y con cargo automático) → **Confirm payment**. El saldo puede tardar **hasta un par de horas** en reflejarse.
Videos: https://www.loom.com/share/1e9d02bad3954698bedbdb02ecc8753f · https://www.loom.com/share/74def539413d42669045dfad5b60e0fd

### ¿Cómo hago llamadas desde Kommo con GoTo? [USO] [TÉCNICA]
Ajustes → Integraciones → instala **GoTo** (la integración es gratis; GoTo cobra una mensualidad aprox. de MXN 600–700 por un número virtual con la lada que elijas). Instala la app de GoTo en tu computadora.
Abre el lead → teléfono en formato **+52 1…** → **Call**. Después registra el resultado en **Notas**.
- El número de llamadas (GoTo) es **distinto** al de WhatsApp; no causa problema.
- Diferencia: **Twilio** registra las llamadas dentro de Kommo y da reporte por vendedor; **GoTo** no tiene ese nivel de integración.
Video: https://www.loom.com/share/068a617dfbd647beafcf543b14b06e0c

### ¿Cómo escucho las grabaciones de llamadas de GoTo? [USO]
Abre la **app de GoTo** → **Reporte de llamadas** → elige el periodo → clic en la llamada → espera unos segundos → **Play**. Útil para capacitar al equipo.
Video: https://www.loom.com/share/8eb94bff2a4447a9ad9e70d335a5043e

### ¿Qué integraciones (apps) recomiendan? [USO]
Ajustes → Integraciones. Las que usamos:
- **WhatsApp Lite**: seguimiento diario (vinculado a tu WhatsApp Business del celular).
- **WhatsApp Business API**: solo en un **número aparte** para envíos masivos.
- **Facebook/Instagram**: Messenger, DMs, comentarios y lead forms.
- **Twilio** (o GoTo): llamadas desde el CRM.
- **Google Workspace**: Gmail y calendario.
Muchas apps de terceros duplican funciones o tienen costo; pruébalas antes de depender de ellas.
Video: https://www.loom.com/share/f2fa13eaf9984300aad61ca57d1fea2e

### ¿Cómo importo una base de datos (Excel) a Kommo? [TÉCNICA]
1. Usa el **formato base** (pídenoslo si no lo tienes). Las **columnas deben llamarse igual que los campos de Kommo**: nombre del lead (la oportunidad), contacto (nombre, apellido), compañía, **usuario responsable**, **embudo**, **estatus/etapa**, etiquetas (ej. "importado 13 mayo"), correo, teléfono, campos personalizados.
2. ⚠️ El texto de responsable, embudo y etapa debe coincidir **exacto** (acentos y mayúsculas incluidos). Teléfonos con **+52 1** y la celda en formato **texto**.
3. Haz primero una **prueba con 2–3 registros**.
4. Guarda como **CSV**. En Kommo: Leads → arriba **Importar** → sube el archivo → **mapea** cada columna con su campo (Contacto → nombre/apellido, correo, teléfono; Compañía → teléfono, web, dirección) → deja marcado **"no importar la primera fila"** (encabezados) → Siguiente. No cierres la ventana mientras importa.
5. Revisa algunos leads importados.
- **Varios contactos de una misma empresa:** una fila por contacto con los mismos datos de empresa. Después, en **Listas → Compañías**, **une** las compañías duplicadas y **borra los leads duplicados** que se crearon.
- No se importan conversaciones ni chats.
Videos: https://www.loom.com/share/0d677a10733545deac2915e11297df3e · https://www.loom.com/share/c333d76e6a484cfa99b39fbe5777da3a

### ¿Cómo creo recordatorios automáticos? (ej. seguimiento después de enviar cotización) [USO]
Desde la **cuenta maestra** → el embudo → **Automatizar** → en la etapa (ej. *Cotización enviada*) **agrega un disparador → Añadir tarea (Add a task)** → ejecutar **inmediatamente al entrar a la etapa** → vencimiento (ej. **en 3 días**) → asignar al **usuario responsable** → Done → **Save**.
Cada lead que muevas a esa etapa recibe la tarea y el vendedor recibe la alerta. Para cambiar los días, edita el disparador igual.
Video: https://www.loom.com/share/5674764bba2b4a168ca4f5e04cb29cf1

### ¿Puedo mandar mensajes masivos o listas de difusión por WhatsApp? [TÉCNICA]
- **WhatsApp Lite NO permite masivos ni listas de difusión** (y hacerlo desde tu WhatsApp normal puede causar **bloqueo**).
- Para masivos se necesita **WhatsApp Business API** (oficial de Meta): requiere **Meta Business Suite**, solicitud y validación del número, **cobro por mensaje**, **plantillas aprobadas por Meta** y **ventana de 24 horas** (si el lead no contesta, solo puedes reabrir con plantilla aprobada).
- **Recomendación:** **no migres tus números de ventas** a la API. Compra un **chip nuevo**, úsalo una semana con mensajes normales y después dalo de alta en la API solo para masivos.
- Configurar la API no está incluido en el taller.
Video: https://www.loom.com/share/35339d278b4349c28f61959d6c69fe1c

---

## 17. Desconexiones (diagnóstico paso a paso)

> Fuentes: tutoriales internos + centro de ayuda oficial de Kommo (support.kommo.com) + ayuda de WhatsApp (faq.whatsapp.com). Kommo cambia sus pantallas con frecuencia; si un menú no coincide, sigue el paso equivalente o contacta a soporte de Kommo.

### Diagnóstico rápido: "Kommo se desconectó" / "no me llegan ni salen mensajes" [DESCONEXIÓN]
Antes de nada, pregunta **qué canal** falla (WhatsApp Lite, WhatsApp Business API, Instagram, Facebook) y **qué ve** el usuario (mensaje de error, número en gris, chats vacíos). Luego:
1. **¿Es Kommo en general?** Revisa el estado de Kommo: https://status.kommo.com/ . Si hay una incidencia, solo queda esperar.
2. **¿El canal está conectado?** Ajustes → **Integraciones (Integration marketplace) → Instalados** → abre el canal. En WhatsApp Lite tu número debe tener **palomita**; si está en **gris**, está desvinculado (ver la ficha siguiente).
3. **¿Faltan chats pero el canal está bien?** En **Chats**, **quita todos los filtros**. Si eres usuario no administrador, puede que no tengas **permisos** para ver esos chats: pide al administrador que los revise.
4. **Arreglos generales:** refresca el navegador o borra caché → **cierra sesión y vuelve a entrar** → prueba en **otro navegador**.
5. **Si sigue igual:** ticket con soporte de Kommo (Ayuda → Chatear con soporte) con **captura de pantalla**, qué pasó, desde cuándo, qué ya probaste y a qué usuarios afecta (administradores o no).
- Solo se puede conectar **una cuenta por canal** (una cuenta de Facebook, de Instagram, etc.).
Fuente: https://support.kommo.com/docs/troubleshooting-chat-inboxes

### Mi WhatsApp Lite aparece desconectado (número en gris) [DESCONEXIÓN]
**Causas comunes:**
- **El celular principal no se ha usado en 14 días o más:** WhatsApp **cierra la sesión de los dispositivos vinculados** (Kommo cuenta como uno). Fuente: https://faq.whatsapp.com/378279804439436
- Se cerró la sesión desde el celular (Dispositivos vinculados → cerrar sesión), se cambió de celular, se reinstaló WhatsApp o se cambió el número.
- Mantenimiento o intermitencia de Kommo.

**Solución:**
1. Abre **WhatsApp Business en el celular** y confirma que funciona (con internet y la sesión activa).
2. En el celular: **Configuración → Dispositivos vinculados**. Revisa si Kommo aparece; si no, se desvinculó.
3. En Kommo: Ajustes → Integraciones → **WhatsApp Lite** → si el número está en gris, **elimínalo (X)** y **agrégalo de nuevo** escaneando el **QR** desde Dispositivos vinculados → Vincular nuevo dispositivo.
4. Vuelve a elegir el **embudo** al que caen sus conversaciones y **ponle nombre** al dispositivo.
- **No se pierde nada:** el historial queda en el celular y en Kommo. Lo que se recibió mientras estuvo desconectado puede no reflejarse en Kommo; revísalo en el celular.
- **Prevención:** usa el celular de ventas al menos cada pocos días; no cierres sesión de "dispositivos vinculados"; avisa antes de cambiar de celular o de número.
- **Mientras esté desconectado**, los mensajes que mandes pueden salir desde **otro número conectado** (ej. el de la cuenta maestra). Ver la ficha "Mando mensajes pero salen del celular de mi compañero".

### El QR no carga, caducó o no escanea [DESCONEXIÓN]
- El QR caduca en segundos: **cierra la ventana y vuelve a generarlo** en Kommo (WhatsApp Lite → Agregar número).
- Escanéalo desde **WhatsApp → Configuración → Dispositivos vinculados → Vincular un dispositivo**, no con la cámara del celular.
- Elige bien **Android o iPhone** en la ventana de Kommo.
- Celular y computadora con **internet estable**; actualiza WhatsApp a la última versión.
- Revisa que no tengas el **máximo de dispositivos vinculados** (cierra sesión de alguno que no uses).
- Si no funciona: refresca Kommo, cierra sesión y vuelve a entrar, o prueba en otro navegador.

### Error "número ya no conectado", "reconecta tu cuenta de Facebook" (WhatsApp Business API) [DESCONEXIÓN] [ERROR]
Aplica **solo si usas WhatsApp Business API** (la oficial de Meta), no WhatsApp Lite.
- **Error 3117 – "Tu cuenta de Facebook debe reconectarse una vez al año" (token vencido):** desconecta y reconecta todo.
  1. En Kommo: integración **WhatsApp Business → Ajustes** → elimina el número y **desvincula el perfil de Facebook**.
  2. En **Meta Business Suite → Configuración → Socios (Partners)** → elimina a Kommo.
  3. En Kommo: **Embudo → Automatizar** → quita el número si sigue activo.
  4. Vuelve a conectar el número.
  - Si conectaste por la **app de WhatsApp Business** (coexistencia): primero, en la app, **Configuración → Cuenta → Business Platform** → elimina a Kommo.
  - ⚠️ Quitar a Kommo de Meta **desconecta también los demás números de WhatsApp y las cuentas de Instagram** conectados con esa autorización: reconéctalos todos.
- **Error 3120 / 3137 – "número ya no conectado" o "número eliminado de la integración pero en uso":** asegúrate de que la conexión anterior quedó eliminada (en Kommo **y** en Meta) y reconecta el número. Si escribes desde un chat viejo de un número anterior, desconecta el viejo y reconecta el nuevo.
- **Error 3136 – número desconectado o WhatsApp Manager eliminado:** si hay una migración de portafolio en proceso, espera; si no, desconecta y reconecta.
- **Error 3108 – ventana de 24 horas cerrada:** no es desconexión; solo puedes escribir con una **plantilla aprobada por Meta** (Automatizaciones → Plantillas → Plantillas de chat → + Nueva → Plantilla de WhatsApp → Enviar a revisión).
- Mientras un número de la API está desconectado, Kommo **pausa los bots y automatizaciones** de ese número; las plantillas, contactos e historial se conservan.
Fuente: https://support.kommo.com/docs/troubleshoot-whatsapp-message-errors

### Instagram dejó de llegar a Kommo / dice "Reconectar" [DESCONEXIÓN]
**Requisitos:** cuenta de **Instagram Business** y acceso al **portafolio comercial de Meta** donde está esa cuenta (debe aparecer en Meta Business Suite → Configuración → Cuentas → Cuentas de Instagram). Solo puede haber **un método de conexión activo** por cuenta.
**Si la autorización venció (Kommo muestra "Reconectar"):**
1. Ajustes → **Integraciones → Instagram** (o Embudo → Automatizar → tarjeta de Instagram).
2. **Cerrar sesión (Log out)** → **Desinstalar**.
3. **Instalar** de nuevo → **Continuar con Instagram** → **Reconectar**.
4. En Meta, elige el **portafolio comercial** y las **cuentas de Instagram** → revisa permisos → **Guardar**.
5. Confirma en la pestaña **Ajustes** de la integración que la cuenta aparece.
- Si Meta dice "No puedes iniciar sesión con esta cuenta de Instagram", conéctala por **autorización de Facebook**.
- Para iniciar el proceso, la interfaz de Kommo puede requerir estar **en inglés**.
- Si el problema es que **no puedes responder** a un lead viejo ("la ventana permitida por Meta se cerró"), no es desconexión: escríbele desde la app de Instagram (ver "No se envían mis mensajes desde Kommo").
Fuente: https://support.kommo.com/docs/connect-instagram-to-kommo

### Facebook Messenger o los lead forms dejaron de llegar [DESCONEXIÓN]
1. Ajustes → Integraciones → **Facebook**: revisa que la **Fan Page** siga conectada y que estén activos Messenger, comentarios y los **lead forms**.
2. Si cambió la contraseña de Facebook, se quitaron permisos de administrador de la página o venció la autorización: **cierra sesión en la integración y vuelve a conectar** con el perfil que **administra la Fan Page**, y vuelve a elegir páginas y formularios.
3. **Lead forms:** confirma que el **formulario nuevo de la campaña** esté agregado (cada formulario nuevo de Meta se tiene que agregar) y que esté mapeado al embudo correcto.
4. Si los leads entran por **Zapier**, revisa en Zapier que el Zap esté **encendido** y sin errores (la conexión de Facebook en Zapier también puede vencer).
5. Si administramos tu publicidad, confirma con tu administrador de cuenta cuál es el formulario activo.
