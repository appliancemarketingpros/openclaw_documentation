---
title: Comprensión de medios
source_url: https://docs.openclaw.ai/es/nodes/media-understanding
scraped_at: 2026-05-25
---

OpenClaw puede **resumir medios entrantes** (imagen/audio/video) antes de que se ejecute la canalización de respuesta. Detecta automáticamente cuándo hay herramientas locales o claves de proveedor disponibles, y se puede desactivar o personalizar. Si la comprensión está desactivada, los modelos siguen recibiendo los archivos/URL originales como de costumbre.

El comportamiento de medios específico de cada proveedor lo registran los plugins de proveedor, mientras que el núcleo de OpenClaw es dueño de la configuración compartida `tools.media`, el orden de respaldo y la integración con la canalización de respuesta.

## Objetivos

  * Opcional: predigerir los medios entrantes en texto breve para un enrutamiento más rápido y mejor análisis de comandos.
  * Preservar la entrega de medios originales al modelo (siempre).
  * Admitir **API de proveedor** y **respaldos CLI**.
  * Permitir varios modelos con respaldo ordenado (error/tamaño/tiempo de espera).


## Comportamiento general

* ### Recopilar adjuntos

Recopilar adjuntos entrantes (`MediaPaths`, `MediaUrls`, `MediaTypes`).

* ### Seleccionar por capacidad

Para cada capacidad habilitada (imagen/audio/video), seleccionar adjuntos según la política (predeterminado: **primero**).

* ### Elegir modelo

Elegir la primera entrada de modelo apta (tamaño + capacidad + autenticación).

* ### Respaldo ante fallo

Si un modelo falla o el medio es demasiado grande, **recurrir a la siguiente entrada**.

* ### Aplicar bloque de éxito

En caso de éxito:

  * `Body` se convierte en bloque `[Image]`, `[Audio]` o `[Video]`.
  * El audio define `{{Transcript}}`; el análisis de comandos usa el texto del pie de foto cuando existe; de lo contrario, la transcripción.
  * Los pies de foto se preservan como `User text:` dentro del bloque.


Si la comprensión falla o está desactivada, **el flujo de respuesta continúa** con el cuerpo original + adjuntos.

## Resumen de configuración

`tools.media` admite **modelos compartidos** más sobrescrituras por capacidad:

Claves de nivel superior

  * `tools.media.models`: lista de modelos compartidos (usar `capabilities` para limitar).
  * `tools.media.image` / `tools.media.audio` / `tools.media.video`: 
    * valores predeterminados (`prompt`, `maxChars`, `maxBytes`, `timeoutSeconds`, `language`)
    * sobrescrituras de proveedor (`baseUrl`, `headers`, `providerOptions`)
    * opciones de audio de Deepgram mediante `tools.media.audio.providerOptions.deepgram`
    * controles de eco de transcripción de audio (`echoTranscript`, predeterminado `false`; `echoFormat`)
    * lista opcional **`models` por capacidad** (preferida antes de los modelos compartidos)
    * política de `attachments` (`mode`, `maxAttachments`, `prefer`)
    * `scope` (limitación opcional por canal/chatType/clave de sesión)
  * `tools.media.concurrency`: máximo de ejecuciones de capacidad concurrentes (predeterminado **2**).


json5Copy code
[code]
    {  tools: {    media: {      models: [        /* shared list */      ],      image: {        /* optional overrides */      },      audio: {        /* optional overrides */        echoTranscript: true,        echoFormat: '📝 "{transcript}"',      },      video: {        /* optional overrides */      },    },  },}
[/code]

### Entradas de modelo

Cada entrada `models[]` puede ser **proveedor** o **CLI** :

### Entrada de proveedor

json5Copy code
[code]
    {  type: "provider", // default if omitted  provider: "openai",  model: "gpt-5.5",  prompt: "Describe the image in <= 500 chars.",  maxChars: 500,  maxBytes: 10485760,  timeoutSeconds: 60,  capabilities: ["image"], // optional, used for multi-modal entries  profile: "vision-profile",  preferredProfile: "vision-fallback",}
[/code]

### Entrada CLI

json5Copy code
[code]
    {  type: "cli",  command: "gemini",  args: [    "-m",    "gemini-3-flash",    "--allowed-tools",    "read_file",    "Read the media at {{MediaPath}} and describe it in <= {{MaxChars}} characters.",  ],  maxChars: 500,  maxBytes: 52428800,  timeoutSeconds: 120,  capabilities: ["video", "image"],}
[/code]

Las plantillas CLI también pueden usar:

  * `{{MediaDir}}` (directorio que contiene el archivo de medios)
  * `{{OutputDir}}` (directorio temporal creado para esta ejecución)
  * `{{OutputBase}}` (ruta base del archivo temporal, sin extensión)


## Valores predeterminados y límites

Valores predeterminados recomendados:

  * `maxChars`: **500** para imagen/video (breve, apto para comandos)
  * `maxChars`: **sin definir** para audio (transcripción completa salvo que definas un límite)
  * `maxBytes`: 
    * imagen: **10MB**
    * audio: **20MB**
    * video: **50MB**


Reglas

  * Si el medio supera `maxBytes`, ese modelo se omite y se **prueba el siguiente modelo**.
  * Los archivos de audio menores que **1024 bytes** se tratan como vacíos/corruptos y se omiten antes de la transcripción por proveedor/CLI; el contexto de respuesta entrante recibe una transcripción marcador determinista para que el agente sepa que la nota era demasiado pequeña.
  * Si el modelo devuelve más de `maxChars`, la salida se recorta.
  * `prompt` usa de forma predeterminada un simple "Describe the {media}." más la guía de `maxChars` (solo imagen/video).
  * Si el modelo de imagen principal activo ya admite visión de forma nativa, OpenClaw omite el bloque de resumen `[Image]` y pasa la imagen original al modelo en su lugar.
  * Si un modelo principal Gateway/WebChat es solo texto, los adjuntos de imagen se preservan como referencias descargadas `media://inbound/*` para que las herramientas de imagen/PDF o el modelo de imagen configurado aún puedan inspeccionarlos en lugar de perder el adjunto.
  * Las solicitudes explícitas `openclaw infer image describe --model <provider/model>` son diferentes: ejecutan directamente ese proveedor/modelo con capacidad de imagen, incluidas referencias de Ollama como `ollama/qwen2.5vl:7b`.
  * Si `<capability>.enabled: true` pero no hay modelos configurados, OpenClaw prueba el **modelo de respuesta activo** cuando su proveedor admite la capacidad.


### Detectar automáticamente la comprensión de medios (predeterminado)

Si `tools.media.<capability>.enabled` **no** está establecido en `false` y no has configurado modelos, OpenClaw detecta automáticamente en este orden y **se detiene en la primera opción que funcione** :

* ### Modelo de respuesta activo

Modelo de respuesta activo cuando su proveedor admite la capacidad.

* ### agents.defaults.imageModel

Referencias principales/de respaldo de `agents.defaults.imageModel` (solo imagen). Preferir referencias `provider/model`. Las referencias simples se califican a partir de entradas configuradas de modelo de proveedor con capacidad de imagen solo cuando la coincidencia es única.

* ### CLI locales (solo audio)

CLI locales (si están instaladas):

  * `sherpa-onnx-offline` (requiere `SHERPA_ONNX_MODEL_DIR` con encoder/decoder/joiner/tokens)
  * `whisper-cli` (`whisper-cpp`; usa `WHISPER_CPP_MODEL` o el modelo tiny incluido)
  * `whisper` (CLI de Python; descarga modelos automáticamente)


* ### CLI de Gemini

`gemini` usando `read_many_files`.

* ### Autenticación de proveedor

  * Las entradas configuradas `models.providers.*` que admiten la capacidad se prueban antes del orden de respaldo incluido.
  * Los proveedores de configuración solo de imagen con un modelo con capacidad de imagen se registran automáticamente para comprensión de medios incluso cuando no son un plugin de proveedor incluido.
  * La comprensión de imágenes de Ollama está disponible cuando se selecciona explícitamente, por ejemplo mediante `agents.defaults.imageModel` o `openclaw infer image describe --model ollama/<vision-model>`.


Orden de respaldo incluido:

  * Audio: OpenAI → Groq → xAI → Deepgram → OpenRouter → Google → SenseAudio → ElevenLabs → Mistral
  * Imagen: OpenAI → Anthropic → Google → MiniMax → MiniMax Portal → [Z.AI](<http://Z.AI>)
  * Video: Google → Qwen → Moonshot


Para desactivar la detección automática, define:

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: false,      },    },  },}
[/code]

### Compatibilidad con entorno de proxy (modelos de proveedor)

Cuando la comprensión de medios basada en proveedor para **audio** y **video** está habilitada, OpenClaw respeta las variables de entorno de proxy saliente estándar para llamadas HTTP de proveedor:

  * `HTTPS_PROXY`
  * `HTTP_PROXY`
  * `ALL_PROXY`
  * `https_proxy`
  * `http_proxy`
  * `all_proxy`


Si no hay variables de entorno de proxy definidas, la comprensión de medios usa salida directa. Si el valor del proxy tiene un formato incorrecto, OpenClaw registra una advertencia y vuelve a la obtención directa.

## Capacidades (opcional)

Si defines `capabilities`, la entrada solo se ejecuta para esos tipos de medios. Para listas compartidas, OpenClaw puede inferir valores predeterminados:

  * `openai`, `anthropic`, `minimax`: **imagen**
  * `minimax-portal`: **imagen**
  * `moonshot`: **imagen + video**
  * `openrouter`: **imagen + audio**
  * `google` (API de Gemini): **imagen + audio + video**
  * `qwen`: **imagen + video**
  * `mistral`: **audio**
  * `zai`: **imagen**
  * `groq`: **audio**
  * `xai`: **audio**
  * `deepgram`: **audio**
  * Cualquier catálogo `models.providers.<id>.models[]` con un modelo con capacidad de imagen: **imagen**


Para entradas CLI, **define`capabilities` explícitamente** para evitar coincidencias inesperadas. Si omites `capabilities`, la entrada es apta para la lista en la que aparece.

## Matriz de soporte de proveedores (integraciones de OpenClaw)

Capacidad | Integración de proveedor | Notas  
---|---|---  
Imagen | OpenAI, OpenAI Codex OAuth, Codex app-server, OpenRouter, Anthropic, Google, MiniMax, Moonshot, Qwen, [Z.AI](<http://Z.AI>), proveedores de configuración | Los plugins de proveedor registran soporte de imagen; `openai-codex/*` usa la infraestructura del proveedor OAuth; `codex/*` usa un turno acotado de Codex app-server; MiniMax y MiniMax OAuth usan `MiniMax-VL-01`; los proveedores de configuración con capacidad de imagen se registran automáticamente.  
Audio | OpenAI, Groq, xAI, Deepgram, OpenRouter, Google, SenseAudio, ElevenLabs, Mistral | Transcripción de proveedor (Whisper/Groq/xAI/Deepgram/OpenRouter STT/Gemini/SenseAudio/Scribe/Voxtral).  
Video | Google, Qwen, Moonshot | Comprensión de video de proveedor mediante plugins de proveedor; la comprensión de video de Qwen usa los endpoints Standard DashScope.  
  
## Guía de selección de modelos

  * Prefiere el modelo más potente de generación reciente disponible para cada capacidad de medios cuando importen la calidad y la seguridad.
  * Para agentes con herramientas habilitadas que manejan entradas no confiables, evita modelos de medios antiguos o más débiles.
  * Mantén al menos un respaldo por capacidad para disponibilidad (modelo de calidad + modelo más rápido/barato).
  * Los respaldos CLI (`whisper-cli`, `whisper`, `gemini`) son útiles cuando las API de proveedor no están disponibles.
  * Nota de `parakeet-mlx`: con `--output-dir`, OpenClaw lee `<output-dir>/<media-basename>.txt` cuando el formato de salida es `txt` (o no se especifica); los formatos que no son `txt` recurren a stdout.


## Política de adjuntos

`attachments` por capacidad controla qué adjuntos se procesan:

Si se debe procesar el primer adjunto seleccionado o todos.

Limita el número procesado.

Preferencia de selección entre los adjuntos candidatos.

Cuando `mode: "all"`, las salidas se etiquetan como `[Image 1/2]`, `[Audio 2/2]`, etc.

File-attachment extraction behavior

  * El texto extraído de archivos se envuelve como **contenido externo no confiable** antes de anexarlo al prompt multimedia.
  * El bloque insertado usa marcadores de límite explícitos como `<<&lt;EXTERNAL_UNTRUSTED_CONTENT id=&quot;...&quot;&gt;>>` / `<<&lt;END_EXTERNAL_UNTRUSTED_CONTENT id=&quot;...&quot;&gt;>>` e incluye una línea de metadatos `Source: External`.
  * Esta ruta de extracción de adjuntos omite intencionalmente el banner largo `SECURITY NOTICE:` para evitar inflar el prompt multimedia; los marcadores de límite y los metadatos permanecen.
  * Si un archivo no tiene texto extraíble, OpenClaw inserta `[No extractable text]`.
  * Si un PDF recurre a imágenes de página renderizadas en esta ruta, el prompt multimedia conserva el marcador de posición `[PDF content rendered to images; images not forwarded to model]` porque este paso de extracción de adjuntos reenvía bloques de texto, no las imágenes renderizadas del PDF.


## Ejemplos de configuración

### Shared models + overrides

json5Copy code
[code]
    {  tools: {    media: {      models: [        { provider: "openai", model: "gpt-5.5", capabilities: ["image"] },        {          provider: "google",          model: "gemini-3-flash-preview",          capabilities: ["image", "audio", "video"],        },        {          type: "cli",          command: "gemini",          args: [            "-m",            "gemini-3-flash",            "--allowed-tools",            "read_file",            "Read the media at {{MediaPath}} and describe it in <= {{MaxChars}} characters.",          ],          capabilities: ["image", "video"],        },      ],      audio: {        attachments: { mode: "all", maxAttachments: 2 },      },      video: {        maxChars: 500,      },    },  },}
[/code]

### Audio + video only

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [          { provider: "openai", model: "gpt-4o-mini-transcribe" },          {            type: "cli",            command: "whisper",            args: ["--model", "base", "{{MediaPath}}"],          },        ],      },      video: {        enabled: true,        maxChars: 500,        models: [          { provider: "google", model: "gemini-3-flash-preview" },          {            type: "cli",            command: "gemini",            args: [              "-m",              "gemini-3-flash",              "--allowed-tools",              "read_file",              "Read the media at {{MediaPath}} and describe it in <= {{MaxChars}} characters.",            ],          },        ],      },    },  },}
[/code]

### Image-only

json5Copy code
[code]
    {  tools: {    media: {      image: {        enabled: true,        maxBytes: 10485760,        maxChars: 500,        models: [          { provider: "openai", model: "gpt-5.5" },          { provider: "anthropic", model: "claude-opus-4-6" },          {            type: "cli",            command: "gemini",            args: [              "-m",              "gemini-3-flash",              "--allowed-tools",              "read_file",              "Read the media at {{MediaPath}} and describe it in <= {{MaxChars}} characters.",            ],          },        ],      },    },  },}
[/code]

### Multi-modal single entry

json5Copy code
[code]
    {  tools: {    media: {      image: {        models: [          {            provider: "google",            model: "gemini-3.1-pro-preview",            capabilities: ["image", "video", "audio"],          },        ],      },      audio: {        models: [          {            provider: "google",            model: "gemini-3.1-pro-preview",            capabilities: ["image", "video", "audio"],          },        ],      },      video: {        models: [          {            provider: "google",            model: "gemini-3.1-pro-preview",            capabilities: ["image", "video", "audio"],          },        ],      },    },  },}
[/code]

## Salida de estado

Cuando se ejecuta la comprensión multimedia, `/status` incluye una línea de resumen breve:

CodeCopy code
[code]
    📎 Media: image ok (openai/gpt-5.4) · audio skipped (maxBytes)
[/code]

Esto muestra los resultados por capacidad y el proveedor/modelo elegido cuando corresponda.

## Notas

  * La comprensión es **de mejor esfuerzo**. Los errores no bloquean las respuestas.
  * Los adjuntos se siguen pasando a los modelos incluso cuando la comprensión está deshabilitada.
  * Usa `scope` para limitar dónde se ejecuta la comprensión (por ejemplo, solo mensajes directos).


## Relacionado

  * [Configuración](</es/gateway/configuration>)
  * [Compatibilidad con imágenes y multimedia](</es/nodes/images>)


Was this useful?YesNo