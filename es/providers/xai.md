---
title: xAI
source_url: https://docs.openclaw.ai/es/providers/xai
scraped_at: 2026-05-25
---

OpenClaw incluye un Plugin de proveedor `xai` integrado para modelos Grok.

## Primeros pasos

* ### Crear una clave de API

Crea una clave de API en la [consola de xAI](<https://console.x.ai/>).

* ### Configurar tu clave de API

Configura `XAI_API_KEY` o ejecuta:

bashCopy code
[code]
    openclaw onboard --auth-choice xai-api-key
[/code]

* ### Elegir un modelo

json5Copy code
[code]
    {  agents: { defaults: { model: { primary: "xai/grok-4.3" } } },}
[/code]

## Catálogo integrado

OpenClaw incluye estas familias de modelos xAI listas para usar:

Familia | Ids de modelo  
---|---  
Grok 3 | `grok-3`, `grok-3-fast`, `grok-3-mini`, `grok-3-mini-fast`  
Grok 4.3 | `grok-4.3`  
Grok 4 | `grok-4`, `grok-4-0709`  
Grok 4 Fast | `grok-4-fast`, `grok-4-fast-non-reasoning`  
Grok 4.1 Fast | `grok-4-1-fast`, `grok-4-1-fast-non-reasoning`  
Grok 4.20 Beta | `grok-4.20-beta-latest-reasoning`, `grok-4.20-beta-latest-non-reasoning`  
Grok Code | `grok-code-fast-1`  
  
El Plugin también resuelve hacia adelante ids `grok-4*` y `grok-code-fast*` más recientes cuando siguen la misma forma de API.

## Cobertura de funciones de OpenClaw

El Plugin integrado asigna la superficie pública actual de la API de xAI a los contratos compartidos de proveedor y herramientas de OpenClaw. Las capacidades que no encajan en el contrato compartido (por ejemplo, TTS en streaming y voz en tiempo real) no se exponen; consulta la tabla siguiente.

Capacidad de xAI | Superficie de OpenClaw | Estado  
---|---|---  
Chat / Responses | proveedor de modelos `xai/<model>` | Sí  
Búsqueda web del servidor | proveedor `web_search` `grok` | Sí  
Búsqueda X del servidor | herramienta `x_search` | Sí  
Ejecución de código del servidor | herramienta `code_execution` | Sí  
Imágenes | `image_generate` | Sí  
Vídeos | `video_generate` | Sí  
Texto a voz por lotes | `messages.tts.provider: "xai"` / `tts` | Sí  
TTS en streaming | - | No expuesto; el contrato TTS de OpenClaw devuelve búferes de audio completos  
Voz a texto por lotes | `tools.media.audio` / comprensión de medios | Sí  
Voz a texto en streaming | Voice Call `streaming.provider: "xai"` | Sí  
Voz en tiempo real | - | Aún no expuesto; contrato de sesión/WebSocket diferente  
Archivos / lotes | Solo compatibilidad genérica con la API de modelos | No es una herramienta OpenClaw de primera clase  
  
### Asignaciones de modo rápido

`/fast on` o `agents.defaults.models["xai/<model>"].params.fastMode: true` reescribe las solicitudes nativas de xAI de la siguiente manera:

Modelo de origen | Destino de modo rápido  
---|---  
`grok-3` | `grok-3-fast`  
`grok-3-mini` | `grok-3-mini-fast`  
`grok-4` | `grok-4-fast`  
`grok-4-0709` | `grok-4-fast`  
  
### Alias de compatibilidad heredados

Los alias heredados aún se normalizan a los ids integrados canónicos:

Alias heredado | Id canónico  
---|---  
`grok-4-fast-reasoning` | `grok-4-fast`  
`grok-4-1-fast-reasoning` | `grok-4-1-fast`  
`grok-4.20-reasoning` | `grok-4.20-beta-latest-reasoning`  
`grok-4.20-non-reasoning` | `grok-4.20-beta-latest-non-reasoning`  
  
## Funciones

Búsqueda web

El proveedor de búsqueda web `grok` integrado puede usar `XAI_API_KEY` o una clave de búsqueda web del Plugin:

bashCopy code
[code]
    openclaw config set tools.web.search.provider grok
[/code]

Generación de vídeo

El Plugin `xai` integrado registra la generación de vídeo mediante la herramienta compartida `video_generate`.

  * Modelo de vídeo predeterminado: `xai/grok-imagine-video`
  * Modos: texto a vídeo, imagen a vídeo, generación con imagen de referencia, edición de vídeo remoto y extensión de vídeo remoto
  * Relaciones de aspecto: `1:1`, `16:9`, `9:16`, `4:3`, `3:4`, `3:2`, `2:3`
  * Resoluciones: `480P`, `720P`
  * Duración: 1-15 segundos para generación/imagen a vídeo, 1-10 segundos al usar roles `reference_image`, 2-10 segundos para extensión
  * Generación con imagen de referencia: configura `imageRoles` como `reference_image` para cada imagen proporcionada; xAI acepta hasta 7 imágenes de este tipo


Para usar xAI como proveedor de vídeo predeterminado:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "xai/grok-imagine-video",      },    },  },}
[/code]

Generación de imágenes

El Plugin `xai` integrado registra la generación de imágenes mediante la herramienta compartida `image_generate`.

  * Modelo de imagen predeterminado: `xai/grok-imagine-image`
  * Modelo adicional: `xai/grok-imagine-image-pro`
  * Modos: texto a imagen y edición con imagen de referencia
  * Entradas de referencia: una `image` o hasta cinco `images`
  * Relaciones de aspecto: `1:1`, `16:9`, `9:16`, `4:3`, `3:4`, `2:3`, `3:2`
  * Resoluciones: `1K`, `2K`
  * Recuento: hasta 4 imágenes


OpenClaw solicita a xAI respuestas de imagen `b64_json` para que los medios generados puedan almacenarse y entregarse mediante la ruta normal de adjuntos de canal. Las imágenes de referencia locales se convierten en URL de datos; las referencias `http(s)` remotas se transmiten sin cambios.

Para usar xAI como proveedor de imágenes predeterminado:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "xai/grok-imagine-image",      },    },  },}
[/code]

Texto a voz

El Plugin `xai` integrado registra texto a voz mediante la superficie de proveedor `tts` compartida.

  * Voces: `eve`, `ara`, `rex`, `sal`, `leo`, `una`
  * Voz predeterminada: `eve`
  * Formatos: `mp3`, `wav`, `pcm`, `mulaw`, `alaw`
  * Idioma: código BCP-47 o `auto`
  * Velocidad: anulación de velocidad nativa del proveedor
  * El formato nativo Opus de nota de voz no es compatible


Para usar xAI como proveedor TTS predeterminado:

json5Copy code
[code]
    {  messages: {    tts: {      provider: "xai",      providers: {        xai: {          voiceId: "eve",        },      },    },  },}
[/code]

Voz a texto

El Plugin `xai` integrado registra voz a texto por lotes mediante la superficie de transcripción de comprensión de medios de OpenClaw.

  * Modelo predeterminado: `grok-stt`
  * Endpoint: REST de xAI `/v1/stt`
  * Ruta de entrada: carga de archivo de audio multipart
  * Compatible en OpenClaw dondequiera que la transcripción de audio entrante use `tools.media.audio`, incluidos segmentos de canales de voz de Discord y adjuntos de audio de canales


Para forzar xAI para la transcripción de audio entrante:

json5Copy code
[code]
    {  tools: {    media: {      audio: {        models: [          {            type: "provider",            provider: "xai",            model: "grok-stt",          },        ],      },    },  },}
[/code]

El idioma puede proporcionarse mediante la configuración compartida de medios de audio o por solicitud de transcripción individual. La superficie compartida de OpenClaw acepta indicaciones de prompt, pero la integración STT REST de xAI solo reenvía archivo, modelo e idioma porque se asignan claramente al endpoint público actual de xAI.

Voz a texto en streaming

El Plugin `xai` integrado también registra un proveedor de transcripción en tiempo real para audio de llamadas de voz en vivo.

  * Endpoint: WebSocket de xAI `wss://api.x.ai/v1/stt`
  * Codificación predeterminada: `mulaw`
  * Frecuencia de muestreo predeterminada: `8000`
  * Detección de finalización predeterminada: `800ms`
  * Transcripciones provisionales: habilitadas de forma predeterminada


El flujo de medios de Twilio de Voice Call envía tramas de audio G.711 µ-law, por lo que el proveedor de xAI puede reenviar esas tramas directamente sin transcodificación:

json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        config: {          streaming: {            enabled: true,            provider: "xai",            providers: {              xai: {                apiKey: "${XAI_API_KEY}",                endpointingMs: 800,                language: "en",              },            },          },        },      },    },  },}
[/code]

La configuración propiedad del proveedor se encuentra en `plugins.entries.voice-call.config.streaming.providers.xai`. Las claves admitidas son `apiKey`, `baseUrl`, `sampleRate`, `encoding` (`pcm`, `mulaw` o `alaw`), `interimResults`, `endpointingMs` y `language`.

Configuración de x_search

El Plugin xAI incluido expone `x_search` como una herramienta de OpenClaw para buscar contenido de X (antes Twitter) mediante Grok.

Ruta de configuración: `plugins.entries.xai.config.xSearch`

Clave | Tipo | Predeterminado | Descripción  
---|---|---|---  
`enabled` | boolean | - | Habilita o deshabilita x_search  
`model` | string | `grok-4-1-fast` | Modelo usado para solicitudes x_search  
`baseUrl` | string | - | Anulación de URL base de xAI Responses  
`inlineCitations` | boolean | - | Incluye citas en línea en los resultados  
`maxTurns` | number | - | Número máximo de turnos de conversación  
`timeoutSeconds` | number | - | Tiempo de espera de la solicitud en segundos  
`cacheTtlMinutes` | number | - | Tiempo de vida de la caché en minutos  
json5Copy code
[code]
    {  plugins: {    entries: {      xai: {        config: {          xSearch: {            enabled: true,            model: "grok-4-1-fast",            baseUrl: "https://api.x.ai/v1",            inlineCitations: true,          },        },      },    },  },}
[/code]

Configuración de ejecución de código

El Plugin xAI incluido expone `code_execution` como una herramienta de OpenClaw para la ejecución remota de código en el entorno sandbox de xAI.

Ruta de configuración: `plugins.entries.xai.config.codeExecution`

Clave | Tipo | Predeterminado | Descripción  
---|---|---|---  
`enabled` | boolean | `true` (si la clave está disponible) | Habilita o deshabilita la ejecución de código  
`model` | string | `grok-4-1-fast` | Modelo usado para solicitudes de ejecución de código  
`maxTurns` | number | - | Número máximo de turnos de conversación  
`timeoutSeconds` | number | - | Tiempo de espera de la solicitud en segundos  
json5Copy code
[code]
    {  plugins: {    entries: {      xai: {        config: {          codeExecution: {            enabled: true,            model: "grok-4-1-fast",          },        },      },    },  },}
[/code]

Límites conocidos

  * Actualmente, la autenticación solo admite clave de API. La clave de API se puede almacenar en un perfil de autenticación de xAI, una variable de entorno o la configuración del Plugin; todavía no hay OAuth de xAI ni flujo de código de dispositivo en OpenClaw.
  * `grok-4.20-multi-agent-experimental-beta-0304` no es compatible con la ruta normal del proveedor xAI porque requiere una superficie de API ascendente distinta de la del transporte xAI estándar de OpenClaw.
  * La voz en tiempo real de xAI todavía no está registrada como proveedor de OpenClaw. Necesita un contrato de sesión de voz bidireccional distinto del STT por lotes o la transcripción por streaming.
  * La `quality` de imagen de xAI, el `mask` de imagen y las relaciones de aspecto adicionales solo nativas no se exponen hasta que la herramienta compartida `image_generate` tenga los controles correspondientes entre proveedores.

Notas avanzadas

  * OpenClaw aplica automáticamente correcciones de compatibilidad específicas de xAI para esquemas de herramientas y llamadas a herramientas en la ruta del ejecutor compartido.
  * Las solicitudes nativas de xAI usan `tool_stream: true` de forma predeterminada. Define `agents.defaults.models["xai/<model>"].params.tool_stream` como `false` para deshabilitarlo.
  * El wrapper xAI incluido elimina marcas estrictas de esquemas de herramientas no admitidas y claves de payload de razonamiento antes de enviar solicitudes nativas de xAI.
  * `web_search`, `x_search` y `code_execution` se exponen como herramientas de OpenClaw. OpenClaw habilita la función integrada específica de xAI que necesita dentro de cada solicitud de herramienta, en lugar de adjuntar todas las herramientas nativas a cada turno de chat.
  * `web_search` de Grok lee `plugins.entries.xai.config.webSearch.baseUrl`. `x_search` lee `plugins.entries.xai.config.xSearch.baseUrl` y luego recurre a la URL base de búsqueda web de Grok.
  * `x_search` y `code_execution` son propiedad del Plugin xAI incluido, en lugar de estar codificados de forma rígida en el runtime del modelo principal.
  * `code_execution` es ejecución remota en el sandbox de xAI, no [`exec`](</es/tools/exec>) local.


## Pruebas en vivo

Las rutas multimedia de xAI están cubiertas por pruebas unitarias y suites en vivo opcionales. Los comandos en vivo cargan secretos desde tu shell de inicio de sesión, incluido `~/.profile`, antes de sondear `XAI_API_KEY`.

bashCopy code
[code]
    pnpm test extensions/xaiOPENCLAW_LIVE_TEST=1 OPENCLAW_LIVE_TEST_QUIET=1 pnpm test:live -- extensions/xai/xai.live.test.tsOPENCLAW_LIVE_TEST=1 OPENCLAW_LIVE_TEST_QUIET=1 OPENCLAW_LIVE_IMAGE_GENERATION_PROVIDERS=xai pnpm test:live -- test/image-generation.runtime.live.test.ts
[/code]

El archivo en vivo específico del proveedor sintetiza TTS normal, TTS PCM apto para telefonía, transcribe audio mediante STT por lotes de xAI, transmite el mismo PCM mediante STT en tiempo real de xAI, genera salida de texto a imagen y edita una imagen de referencia. El archivo en vivo de imagen compartida verifica el mismo proveedor xAI mediante la selección de runtime, fallback, normalización y ruta de adjuntos multimedia de OpenClaw.

## Relacionado

[**Selección de modelos** Elección de proveedores, referencias de modelo y comportamiento de conmutación por error. ](</es/concepts/model-providers>) [**Generación de video** Parámetros de herramienta de video compartida y selección de proveedor. ](</es/tools/video-generation>) [**Todos los proveedores** La descripción general más amplia de proveedores. ](</es/providers>) [**Solución de problemas** Problemas comunes y correcciones. ](</es/help/troubleshooting>)

Was this useful?YesNo