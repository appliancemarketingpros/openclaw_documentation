---
title: Generación de video
source_url: https://docs.openclaw.ai/es/tools/video-generation
scraped_at: 2026-05-25
---

OpenClaw agentes pueden generar videos a partir de prompts de texto, imágenes de referencia o videos existentes. Se admiten dieciséis backends de proveedor, cada uno con diferentes opciones de modelo, modos de entrada y conjuntos de funciones. El agente elige el proveedor adecuado automáticamente según tu configuración y las claves de API disponibles.

OpenClaw trata la generación de video como tres modos de tiempo de ejecución:

  * `generate` \- solicitudes de texto a video sin medios de referencia.
  * `imageToVideo` \- la solicitud incluye una o más imágenes de referencia.
  * `videoToVideo` \- la solicitud incluye uno o más videos de referencia.


Los proveedores pueden admitir cualquier subconjunto de esos modos. La herramienta valida el modo activo antes del envío e informa los modos admitidos en `action=list`.

## Inicio rápido

* ### Configure auth

Configura una clave de API para cualquier proveedor admitido:

bashCopy code
[code]
    export GEMINI_API_KEY="your-key"
[/code]

* ### Pick a default model (optional)

bashCopy code
[code]
    openclaw config set agents.defaults.videoGenerationModel.primary "google/veo-3.1-fast-generate-preview"
[/code]

* ### Ask the agent

> Genera un video cinematográfico de 5 segundos de una langosta amigable surfeando al atardecer.

El agente llama a `video_generate` automáticamente. No es necesario incluir herramientas en una lista de permitidos.

## Cómo funciona la generación asíncrona

La generación de video es asíncrona. Cuando el agente llama a `video_generate` en una sesión:

  1. OpenClaw envía la solicitud al proveedor y devuelve de inmediato un id de tarea.
  2. El proveedor procesa el trabajo en segundo plano (normalmente de 30 segundos a varios minutos, según el proveedor y la resolución; los proveedores lentos respaldados por cola pueden ejecutarse hasta el tiempo de espera configurado).
  3. Cuando el video está listo, OpenClaw reactiva la misma sesión con un evento interno de finalización.
  4. El agente informa al usuario y adjunta el video terminado. En chats de grupo/canal que usan entrega visible únicamente mediante herramienta de mensajes, el agente transmite el resultado mediante la herramienta de mensajes en lugar de que OpenClaw lo publique directamente.


Mientras un trabajo está en curso, las llamadas duplicadas a `video_generate` en la misma sesión devuelven el estado actual de la tarea en lugar de iniciar otra generación. Usa `openclaw tasks list` u `openclaw tasks show <taskId>` para consultar el progreso desde la CLI.

Fuera de las ejecuciones de agente respaldadas por sesión (por ejemplo, invocaciones directas de herramientas), la herramienta recurre a generación en línea y devuelve la ruta final del medio en el mismo turno.

Los archivos de video generados se guardan en el almacenamiento de medios administrado por OpenClaw cuando el proveedor devuelve bytes. El límite predeterminado de guardado de videos generados sigue el límite de medios de video, y `agents.defaults.mediaMaxMb` lo aumenta para renders más grandes. Cuando un proveedor también devuelve una URL de salida alojada, OpenClaw puede entregar esa URL en lugar de fallar la tarea si la persistencia local rechaza un archivo demasiado grande.

### Ciclo de vida de la tarea

Estado | Significado  
---|---  
`queued` | Tarea creada, en espera de que el proveedor la acepte.  
`running` | El proveedor está procesando (normalmente de 30 segundos a varios minutos, según el proveedor y la resolución).  
`succeeded` | Video listo; el agente se reactiva y lo publica en la conversación.  
`failed` | Error del proveedor o tiempo de espera agotado; el agente se reactiva con detalles del error.  
  
Consulta el estado desde la CLI:

bashCopy code
[code]
    openclaw tasks listopenclaw tasks show <taskId>openclaw tasks cancel <taskId>
[/code]

Si una tarea de video ya está `queued` o `running` para la sesión actual, `video_generate` devuelve el estado de la tarea existente en lugar de iniciar una nueva. Usa `action: "status"` para consultarlo explícitamente sin activar una nueva generación.

## Proveedores admitidos

Proveedor | Modelo predeterminado | Texto | Ref. de imagen | Ref. de video | Autenticación  
---|---|---|---|---|---  
Alibaba | `wan2.6-t2v` | ✓ | Sí (URL remota) | Sí (URL remota) | `MODELSTUDIO_API_KEY`  
BytePlus (1.0) | `seedance-1-0-pro-250528` | ✓ | Hasta 2 imágenes (solo modelos I2V; primer + último fotograma) | - | `BYTEPLUS_API_KEY`  
BytePlus Seedance 1.5 | `seedance-1-5-pro-251215` | ✓ | Hasta 2 imágenes (primer + último fotograma mediante rol) | - | `BYTEPLUS_API_KEY`  
BytePlus Seedance 2.0 | `dreamina-seedance-2-0-260128` | ✓ | Hasta 9 imágenes de referencia | Hasta 3 videos | `BYTEPLUS_API_KEY`  
ComfyUI | `workflow` | ✓ | 1 imagen | - | `COMFY_API_KEY` o `COMFY_CLOUD_API_KEY`  
DeepInfra | `Pixverse/Pixverse-T2V` | ✓ | - | - | `DEEPINFRA_API_KEY`  
fal | `fal-ai/minimax/video-01-live` | ✓ | 1 imagen; hasta 9 con referencia a video de Seedance | Hasta 3 videos con referencia a video de Seedance | `FAL_KEY`  
Google | `veo-3.1-fast-generate-preview` | ✓ | 1 imagen | 1 video | `GEMINI_API_KEY`  
MiniMax | `MiniMax-Hailuo-2.3` | ✓ | 1 imagen | - | `MINIMAX_API_KEY` o MiniMax OAuth  
OpenAI | `sora-2` | ✓ | 1 imagen | 1 video | `OPENAI_API_KEY`  
OpenRouter | `google/veo-3.1-fast` | ✓ | Hasta 4 imágenes (primer/último fotograma o referencias) | - | `OPENROUTER_API_KEY`  
Qwen | `wan2.6-t2v` | ✓ | Sí (URL remota) | Sí (URL remota) | `QWEN_API_KEY`  
Runway | `gen4.5` | ✓ | 1 imagen | 1 video | `RUNWAYML_API_SECRET`  
Together | `Wan-AI/Wan2.2-T2V-A14B` | ✓ | 1 imagen | - | `TOGETHER_API_KEY`  
Vydra | `veo3` | ✓ | 1 imagen (`kling`) | - | `VYDRA_API_KEY`  
xAI | `grok-imagine-video` | ✓ | 1 imagen de primer fotograma o hasta 7 `reference_image`s | 1 video | `XAI_API_KEY`  
  
Algunos proveedores aceptan variables de entorno de clave de API adicionales o alternativas. Consulta las páginas de proveedores individuales para obtener detalles.

Ejecuta `video_generate action=list` para inspeccionar los proveedores, modelos y modos de tiempo de ejecución disponibles en tiempo de ejecución.

### Matriz de capacidades

El contrato de modos explícito que usan `video_generate`, las pruebas de contrato y el barrido en vivo compartido:

Proveedor | `generate` | `imageToVideo` | `videoToVideo` | Lanes en vivo compartidos hoy  
---|---|---|---|---  
Alibaba | ✓ | ✓ | ✓ | `generate`, `imageToVideo`; `videoToVideo` se omite porque este proveedor necesita URL de video `http(s)` remotas  
BytePlus | ✓ | ✓ | - | `generate`, `imageToVideo`  
ComfyUI | ✓ | ✓ | - | No está en el barrido compartido; la cobertura específica del flujo de trabajo vive con las pruebas de Comfy  
DeepInfra | ✓ | - | - | `generate`; los esquemas de video nativos de DeepInfra son de texto a video en el contrato incluido  
fal | ✓ | ✓ | ✓ | `generate`, `imageToVideo`; `videoToVideo` solo cuando se usa referencia a video de Seedance  
Google | ✓ | ✓ | ✓ | `generate`, `imageToVideo`; `videoToVideo` compartido se omite porque el barrido actual de Gemini/Veo respaldado por búfer no acepta esa entrada  
MiniMax | ✓ | ✓ | - | `generate`, `imageToVideo`  
OpenAI | ✓ | ✓ | ✓ | `generate`, `imageToVideo`; `videoToVideo` compartido se omite porque esta organización/ruta de entrada actualmente necesita acceso a inpaint/remix del lado del proveedor  
OpenRouter | ✓ | ✓ | - | `generate`, `imageToVideo`  
Qwen | ✓ | ✓ | ✓ | `generate`, `imageToVideo`; `videoToVideo` se omite porque este proveedor necesita URL de video `http(s)` remotas  
Runway | ✓ | ✓ | ✓ | `generate`, `imageToVideo`; `videoToVideo` se ejecuta solo cuando el modelo seleccionado es `runway/gen4_aleph`  
Together | ✓ | ✓ | - | `generate`, `imageToVideo`  
Vydra | ✓ | ✓ | - | `generate`; `imageToVideo` compartido se omite porque el `veo3` incluido solo acepta texto y el `kling` incluido requiere una URL de imagen remota  
xAI | ✓ | ✓ | ✓ | `generate`, `imageToVideo`; `videoToVideo` se omite porque este proveedor actualmente necesita una URL MP4 remota  
  
## Parámetros de la herramienta

### Obligatorio

Descripción de texto del video que se generará. Obligatorio para `action: "generate"`.

### Entradas de contenido

Indicaciones de rol opcionales por posición, paralelas a la lista combinada de imágenes. Valores canónicos: `first_frame`, `last_frame`, `reference_image`.

Indicaciones de rol opcionales por posición, paralelas a la lista combinada de videos. Valor canónico: `reference_video`.

Audio de referencia único (ruta o URL). Se usa para música de fondo o como referencia de voz cuando el proveedor admite entradas de audio.

Indicaciones de rol opcionales por posición, paralelas a la lista combinada de audios. Valor canónico: `reference_audio`.

### Controles de estilo

Indicación de relación de aspecto como `1:1`, `16:9`, `9:16`, `adaptive` o un valor específico del proveedor. OpenClaw normaliza o ignora los valores no admitidos según el proveedor.

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InJlc29sdXRpb24iIHR5cGU9InN0cmluZyI Indicación de resolución como `480P`, `720P`, `768P`, `1080P`, `4K` o un valor específico del proveedor. OpenClaw normaliza o ignora los valores no admitidos según el proveedor. OPENCLAW_DOCS_MARKER:paramClose:

Duración objetivo en segundos (redondeada al valor más cercano admitido por el proveedor).

Activa el audio generado en la salida cuando sea compatible. Es distinto de `audioRef*` (entradas).

`adaptive` es un centinela específico del proveedor: se reenvía tal como está a los proveedores que declaran `adaptive` en sus capacidades (por ejemplo, BytePlus Seedance lo usa para detectar automáticamente la relación a partir de las dimensiones de la imagen de entrada). Los proveedores que no lo declaran muestran el valor mediante `details.ignoredOverrides` en el resultado de la herramienta para que el descarte sea visible.

### Avanzado

`"status"` devuelve la tarea de la sesión actual; `"list"` inspecciona los proveedores.

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci Anulación de proveedor/modelo (por ejemplo, `runway/gen4.5`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InRpbWVvdXRNcyIgdHlwZT0ibnVtYmVyIg Tiempo de espera opcional de la operación del proveedor en milisegundos. Cuando se omite, OpenClaw usa `agents.defaults.videoGenerationModel.timeoutMs` si está configurado. OPENCLAW_DOCS_MARKER:paramClose:

Opciones específicas del proveedor como objeto JSON (por ejemplo, `{"seed": 42, "draft": true}`). Los proveedores que declaran un esquema tipado validan las claves y los tipos; las claves desconocidas o las discrepancias omiten el candidato durante el respaldo. Los proveedores sin un esquema declarado reciben las opciones tal como están. Ejecuta `video_generate action=list` para ver qué acepta cada proveedor.

Las entradas de referencia seleccionan el modo en tiempo de ejecución:

  * Sin medios de referencia → `generate`
  * Cualquier referencia de imagen → `imageToVideo`
  * Cualquier referencia de video → `videoToVideo`
  * Las entradas de audio de referencia **no** cambian el modo resuelto; se aplican encima del modo que seleccionen las referencias de imagen/video, y solo funcionan con proveedores que declaran `maxInputAudios`.


Las referencias mixtas de imagen y video no son una superficie de capacidad compartida estable. Prefiere un tipo de referencia por solicitud.

#### Respaldo y opciones tipadas

Algunas comprobaciones de capacidad se aplican en la capa de respaldo, no en el límite de la herramienta, por lo que una solicitud que excede los límites del proveedor principal aún puede ejecutarse en un respaldo capaz:

  * El candidato activo que no declara `maxInputAudios` (o declara `0`) se omite cuando la solicitud contiene referencias de audio; se prueba el siguiente candidato.
  * El `maxDurationSeconds` del candidato activo por debajo del `durationSeconds` solicitado sin una lista `supportedDurationSeconds` declarada → se omite.
  * La solicitud contiene `providerOptions` y el candidato activo declara explícitamente un esquema `providerOptions` tipado → se omite si las claves suministradas no están en el esquema o los tipos de valores no coinciden. Los proveedores sin un esquema declarado reciben las opciones tal como están (transferencia directa compatible con versiones anteriores). Un proveedor puede excluirse de todas las opciones de proveedor declarando un esquema vacío (`capabilities.providerOptions: {}`), lo que causa la misma omisión que una discrepancia de tipo.


El primer motivo de omisión en una solicitud se registra en `warn` para que los operadores vean cuándo se pasó por alto su proveedor principal; las omisiones posteriores se registran en `debug` para mantener silenciosas las cadenas de respaldo largas. Si se omiten todos los candidatos, el error agregado incluye el motivo de omisión de cada uno.

## Acciones

Acción | Qué hace  
---|---  
`generate` | Predeterminado. Crea un video a partir del prompt dado y las entradas de referencia opcionales.  
`status` | Comprueba el estado de la tarea de video en curso para la sesión actual sin iniciar otra generación.  
`list` | Muestra los proveedores, modelos y sus capacidades disponibles.  
  
## Selección de modelo

OpenClaw resuelve el modelo en este orden:

  1. **Parámetro de herramienta`model`** \- si el agente especifica uno en la llamada.
  2. **`videoGenerationModel.primary`** de la configuración.
  3. **`videoGenerationModel.fallbacks`** en orden.
  4. **Detección automática** \- proveedores que tienen autenticación válida, empezando por el proveedor predeterminado actual y luego el resto de proveedores en orden alfabético.


Si un proveedor falla, se prueba automáticamente el siguiente candidato. Si todos los candidatos fallan, el error incluye detalles de cada intento.

Establece `agents.defaults.mediaGenerationAutoProviderFallback: false` para usar solo las entradas explícitas `model`, `primary` y `fallbacks`.

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "google/veo-3.1-fast-generate-preview",        fallbacks: ["runway/gen4.5", "qwen/wan2.6-t2v"],      },    },  },}
[/code]

## Notas de proveedores

Alibaba

Usa el endpoint asíncrono de DashScope / Model Studio. Las imágenes y videos de referencia deben ser URL `http(s)` remotas.

BytePlus (1.0)

ID de proveedor: `byteplus`.

Modelos: `seedance-1-0-pro-250528` (predeterminado), `seedance-1-0-pro-t2v-250528`, `seedance-1-0-pro-fast-251015`, `seedance-1-0-lite-t2v-250428`, `seedance-1-0-lite-i2v-250428`.

Los modelos T2V (`*-t2v-*`) no aceptan entradas de imagen; los modelos I2V y los modelos generales `*-pro-*` admiten una sola imagen de referencia (primer fotograma). Pasa la imagen por posición o establece `role: "first_frame"`. Los ID de modelo T2V se cambian automáticamente a la variante I2V correspondiente cuando se proporciona una imagen.

Claves `providerOptions` admitidas: `seed` (number), `draft` (boolean - fuerza 480p), `camera_fixed` (boolean).

BytePlus Seedance 1.5

Requiere el Plugin [`@openclaw/byteplus-modelark`](<https://www.npmjs.com/package/@openclaw/byteplus-modelark>). ID de proveedor: `byteplus-seedance15`. Modelo: `seedance-1-5-pro-251215`.

Usa la API unificada `content[]`. Admite como máximo 2 imágenes de entrada (`first_frame` \+ `last_frame`). Todas las entradas deben ser URL `https://` remotas. Establece `role: "first_frame"` / `"last_frame"` en cada imagen, o pasa las imágenes por posición.

`aspectRatio: "adaptive"` detecta automáticamente la relación a partir de la imagen de entrada. `audio: true` se asigna a `generate_audio`. `providerOptions.seed` (number) se reenvía.

BytePlus Seedance 2.0

Requiere el Plugin [`@openclaw/byteplus-modelark`](<https://www.npmjs.com/package/@openclaw/byteplus-modelark>). ID de proveedor: `byteplus-seedance2`. Modelos: `dreamina-seedance-2-0-260128`, `dreamina-seedance-2-0-fast-260128`.

Usa la API unificada `content[]`. Admite hasta 9 imágenes de referencia, 3 videos de referencia y 3 audios de referencia. Todas las entradas deben ser URL `https://` remotas. Establece `role` en cada recurso - valores admitidos: `"first_frame"`, `"last_frame"`, `"reference_image"`, `"reference_video"`, `"reference_audio"`.

`aspectRatio: "adaptive"` detecta automáticamente la relación a partir de la imagen de entrada. `audio: true` se asigna a `generate_audio`. `providerOptions.seed` (number) se reenvía.

ComfyUI

Ejecución local o en la nube basada en flujos de trabajo. Admite texto a video e imagen a video mediante el grafo configurado.

fal

Usa un flujo respaldado por cola para trabajos de larga duración. OpenClaw espera hasta 20 minutos de forma predeterminada antes de tratar un trabajo de cola de fal en curso como agotado por tiempo de espera. La mayoría de los modelos de video de fal aceptan una sola referencia de imagen. Los modelos Seedance 2.0 de referencia a video aceptan hasta 9 imágenes, 3 videos y 3 referencias de audio, con un máximo de 12 archivos de referencia en total.

Google (Gemini / Veo)

Admite una referencia de imagen o una referencia de video. Las solicitudes de audio generado se ignoran con una advertencia en la ruta de la API de Gemini porque esa API rechaza el parámetro `generateAudio` para la generación de video actual de Veo.

MiniMax

Solo una referencia de imagen. MiniMax acepta resoluciones `768P` y `1080P`; las solicitudes como `720P` se normalizan al valor compatible más cercano antes del envío.

OpenAI

Solo se reenvía la anulación de `size`. Otras anulaciones de estilo (`aspectRatio`, `resolution`, `audio`, `watermark`) se ignoran con una advertencia.

OpenRouter

Usa la API asíncrona `/videos` de OpenRouter. OpenClaw envía el trabajo, sondea `polling_url` y descarga `unsigned_urls` o el endpoint documentado de contenido del trabajo. El valor predeterminado incluido `google/veo-3.1-fast` anuncia duraciones de 4/6/8 segundos, resoluciones `720P`/`1080P` y relaciones de aspecto `16:9`/`9:16`.

Qwen

El mismo backend DashScope que Alibaba. Las entradas de referencia deben ser URL remotas `http(s)`; los archivos locales se rechazan por adelantado.

Runway

Admite archivos locales mediante URI de datos. Video a video requiere `runway/gen4_aleph`. Las ejecuciones solo de texto exponen relaciones de aspecto `16:9` y `9:16`.

Together

Solo una referencia de imagen.

Vydra

Usa `https://www.vydra.ai/api/v1` directamente para evitar redirecciones que pierdan la autenticación. `veo3` se incluye solo como texto a video; `kling` requiere una URL de imagen remota.

xAI

Admite texto a video, imagen a video con un único primer fotograma, hasta 7 entradas `reference_image` mediante `reference_images` de xAI, y flujos remotos de edición/extensión de video.

## Modos de capacidad del proveedor

El contrato compartido de generación de video admite capacidades específicas por modo en lugar de solo límites agregados planos. Las nuevas implementaciones de proveedores deberían preferir bloques de modo explícitos:

typescriptCopy code
[code]
    capabilities: {  generate: {    maxVideos: 1,    maxDurationSeconds: 10,    supportsResolution: true,  },  imageToVideo: {    enabled: true,    maxVideos: 1,    maxInputImages: 1,    maxInputImagesByModel: { "provider/reference-to-video": 9 },    maxDurationSeconds: 5,  },  videoToVideo: {    enabled: true,    maxVideos: 1,    maxInputVideos: 1,    maxDurationSeconds: 5,  },}
[/code]

Los campos agregados planos como `maxInputImages` y `maxInputVideos` **no** son suficientes para anunciar compatibilidad con modos de transformación. Los proveedores deberían declarar `generate`, `imageToVideo` y `videoToVideo` explícitamente para que las pruebas en vivo, las pruebas de contrato y la herramienta compartida `video_generate` puedan validar la compatibilidad de modo de forma determinista.

Cuando un modelo de un proveedor admite más entradas de referencia que el resto, usa `maxInputImagesByModel`, `maxInputVideosByModel` o `maxInputAudiosByModel` en lugar de aumentar el límite de todo el modo.

## Pruebas en vivo

Cobertura en vivo opcional para los proveedores incluidos compartidos:

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 pnpm test:live -- extensions/video-generation-providers.live.test.ts
[/code]

Wrapper del repo:

bashCopy code
[code]
    pnpm test:live:media video
[/code]

Este archivo en vivo carga las variables de entorno de proveedor faltantes desde `~/.profile`, prefiere claves de API en vivo/de entorno por delante de los perfiles de autenticación almacenados de forma predeterminada, y ejecuta un smoke seguro para release de forma predeterminada:

  * `generate` para cada proveedor que no sea FAL en el barrido.
  * Prompt de langosta de un segundo.
  * Límite de operación por proveedor desde `OPENCLAW_LIVE_VIDEO_GENERATION_TIMEOUT_MS` (`180000` de forma predeterminada).


FAL es opcional porque la latencia de la cola del lado del proveedor puede dominar el tiempo de release:

bashCopy code
[code]
    pnpm test:live:media video --video-providers fal
[/code]

Establece `OPENCLAW_LIVE_VIDEO_GENERATION_FULL_MODES=1` para ejecutar también los modos de transformación declarados que el barrido compartido puede ejercitar de forma segura con medios locales:

  * `imageToVideo` cuando `capabilities.imageToVideo.enabled`.
  * `videoToVideo` cuando `capabilities.videoToVideo.enabled` y el proveedor/modelo acepta entrada de video local respaldada por búfer en el barrido compartido.


Hoy, la vía en vivo compartida de `videoToVideo` cubre `runway` solo cuando seleccionas `runway/gen4_aleph`.

## Configuración

Establece el modelo predeterminado de generación de video en tu configuración de OpenClaw:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "qwen/wan2.6-t2v",        fallbacks: ["qwen/wan2.6-r2v-flash"],      },    },  },}
[/code]

O mediante la CLI:

bashCopy code
[code]
    openclaw config set agents.defaults.videoGenerationModel.primary "qwen/wan2.6-t2v"
[/code]

## Relacionado

  * [Alibaba Model Studio](</es/providers/alibaba>)
  * [Tareas en segundo plano](</es/automation/tasks>) \- seguimiento de tareas para generación de video asíncrona
  * [BytePlus](</es/concepts/model-providers#byteplus-international>)
  * [ComfyUI](</es/providers/comfy>)
  * [Referencia de configuración](</es/gateway/config-agents#agent-defaults>)
  * [fal](</es/providers/fal>)
  * [Google (Gemini)](</es/providers/google>)
  * [MiniMax](</es/providers/minimax>)
  * [Modelos](</es/concepts/models>)
  * [OpenAI](</es/providers/openai>)
  * [Qwen](</es/providers/qwen>)
  * [Runway](</es/providers/runway>)
  * [Together AI](</es/providers/together>)
  * [Descripción general de herramientas](</es/tools>)
  * [Vydra](</es/providers/vydra>)
  * [xAI](</es/providers/xai>)


Was this useful?YesNo