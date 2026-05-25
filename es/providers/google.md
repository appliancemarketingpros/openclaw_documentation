---
title: Google (Gemini)
source_url: https://docs.openclaw.ai/es/providers/google
scraped_at: 2026-05-25
---

El plugin de Google proporciona acceso a los modelos Gemini a través de Google AI Studio, además de generación de imágenes, comprensión de medios (imagen/audio/video), texto a voz y búsqueda web mediante Gemini Grounding.

  * Proveedor: `google`
  * Autenticación: `GEMINI_API_KEY` o `GOOGLE_API_KEY`
  * API: Google Gemini API
  * Opción de Runtime: proveedor/modelo `agentRuntime.id: "google-gemini-cli"` reutiliza OAuth de Gemini CLI mientras conserva las referencias de modelo canónicas como `google/*`.


## Primeros pasos

Elige tu método de autenticación preferido y sigue los pasos de configuración.

### Clave de API

**Ideal para:** acceso estándar a Gemini API a través de Google AI Studio.

* ### Ejecutar la incorporación

bashCopy code
[code]
    openclaw onboard --auth-choice gemini-api-key
[/code]

O pasa la clave directamente:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice gemini-api-key \  --gemini-api-key "$GEMINI_API_KEY"
[/code]

* ### Establecer un modelo predeterminado

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "google/gemini-3.1-pro-preview" },    },  },}
[/code]

* ### Verificar que el modelo esté disponible

bashCopy code
[code]
    openclaw models list --provider google
[/code]

### Gemini CLI (OAuth)

**Ideal para:** reutilizar un inicio de sesión existente de Gemini CLI mediante PKCE OAuth en lugar de una clave de API separada.

* ### Instalar Gemini CLI

El comando local `gemini` debe estar disponible en `PATH`.

bashCopy code
[code]
    # Homebrewbrew install gemini-cli # or npmnpm install -g @google/gemini-cli
[/code]

OpenClaw admite instalaciones de Homebrew e instalaciones globales de npm, incluidas disposiciones comunes de Windows/npm.

* ### Iniciar sesión mediante OAuth

bashCopy code
[code]
    openclaw models auth login --provider google-gemini-cli --set-default
[/code]

* ### Verificar que el modelo esté disponible

bashCopy code
[code]
    openclaw models list --provider google
[/code]

  * Modelo predeterminado: `google/gemini-3.1-pro-preview`
  * Runtime: `google-gemini-cli`
  * Alias: `gemini-cli`


El ID de modelo de Gemini API para Gemini 3.1 Pro es `gemini-3.1-pro-preview`. OpenClaw acepta el `google/gemini-3.1-pro` más corto como alias de conveniencia y lo normaliza antes de las llamadas al proveedor.

**Variables de entorno:**

  * `OPENCLAW_GEMINI_OAUTH_CLIENT_ID`
  * `OPENCLAW_GEMINI_OAUTH_CLIENT_SECRET`


(O las variantes `GEMINI_CLI_*`).

Las referencias de modelo `google-gemini-cli/*` son alias de compatibilidad heredados. Las configuraciones nuevas deben usar referencias de modelo `google/*` más el Runtime `google-gemini-cli` cuando quieran ejecución local de Gemini CLI.

## Capacidades

Capacidad | Compatible  
---|---  
Completados de chat | Sí  
Generación de imágenes | Sí  
Generación de música | Sí  
Texto a voz | Sí  
Voz en tiempo real | Sí (Google Live API)  
Comprensión de imágenes | Sí  
Transcripción de audio | Sí  
Comprensión de video | Sí  
Búsqueda web (Grounding) | Sí  
Pensamiento/razonamiento | Sí (Gemini 2.5+ / Gemini 3+)  
Modelos Gemma 4 | Sí  
  
## Búsqueda web

El proveedor de búsqueda web `gemini` incluido usa grounding de Gemini Google Search. Configura una clave de búsqueda dedicada en `plugins.entries.google.config.webSearch`, o deja que reutilice `models.providers.google.apiKey` después de `GEMINI_API_KEY`:

json5Copy code
[code]
    {  plugins: {    entries: {      google: {        config: {          webSearch: {            apiKey: "AIza...", // optional if GEMINI_API_KEY or models.providers.google.apiKey is set            baseUrl: "https://generativelanguage.googleapis.com/v1beta", // falls back to models.providers.google.baseUrl            model: "gemini-2.5-flash",          },        },      },    },  },}
[/code]

La precedencia de credenciales es `webSearch.apiKey` dedicado, luego `GEMINI_API_KEY`, luego `models.providers.google.apiKey`. `webSearch.baseUrl` es opcional y existe para proxies de operadores o endpoints compatibles de Gemini API; cuando se omite, la búsqueda web de Gemini reutiliza `models.providers.google.baseUrl`. Consulta [Búsqueda de Gemini](</es/tools/gemini-search>) para el comportamiento de la herramienta específico del proveedor.

## Generación de imágenes

El proveedor de generación de imágenes `google` incluido usa de forma predeterminada `google/gemini-3.1-flash-image-preview`.

  * También admite `google/gemini-3-pro-image-preview`
  * Generación: hasta 4 imágenes por solicitud
  * Modo de edición: habilitado, hasta 5 imágenes de entrada
  * Controles de geometría: `size`, `aspectRatio` y `resolution`


Para usar Google como proveedor de imágenes predeterminado:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "google/gemini-3.1-flash-image-preview",      },    },  },}
[/code]

## Generación de video

El Plugin `google` incluido también registra la generación de video mediante la herramienta compartida `video_generate`.

  * Modelo de video predeterminado: `google/veo-3.1-fast-generate-preview`
  * Modos: texto a video, imagen a video y flujos de referencia de un solo video
  * Admite `aspectRatio` (`16:9`, `9:16`) y `resolution` (`720P`, `1080P`); Veo no admite salida de audio actualmente
  * Duraciones admitidas: **4, 6 u 8 segundos** (otros valores se ajustan al valor permitido más cercano)


Para usar Google como proveedor de video predeterminado:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "google/veo-3.1-fast-generate-preview",      },    },  },}
[/code]

## Generación de música

El Plugin `google` incluido también registra la generación de música mediante la herramienta compartida `music_generate`.

  * Modelo de música predeterminado: `google/lyria-3-clip-preview`
  * También admite `google/lyria-3-pro-preview`
  * Controles de prompt: `lyrics` e `instrumental`
  * Formato de salida: `mp3` de forma predeterminada, además de `wav` en `google/lyria-3-pro-preview`
  * Entradas de referencia: hasta 10 imágenes
  * Las ejecuciones respaldadas por sesión se desacoplan mediante el flujo compartido de tarea/estado, incluido `action: "status"`


Para usar Google como proveedor de música predeterminado:

json5Copy code
[code]
    {  agents: {    defaults: {      musicGenerationModel: {        primary: "google/lyria-3-clip-preview",      },    },  },}
[/code]

## Texto a voz

El proveedor de voz `google` incluido usa la ruta TTS de Gemini API con `gemini-3.1-flash-tts-preview`.

  * Voz predeterminada: `Kore`
  * Autenticación: `messages.tts.providers.google.apiKey`, `models.providers.google.apiKey`, `GEMINI_API_KEY` o `GOOGLE_API_KEY`
  * Salida: WAV para adjuntos TTS normales, Opus para destinos de notas de voz, PCM para Talk/telefonía
  * Salida de nota de voz: el PCM de Google se encapsula como WAV y se transcodifica a Opus de 48 kHz con `ffmpeg`


La ruta TTS por lotes de Gemini de Google devuelve el audio generado en la respuesta `generateContent` completada. Para conversaciones habladas con la menor latencia, usa el proveedor de voz en tiempo real de Google respaldado por Gemini Live API en lugar de TTS por lotes.

Para usar Google como proveedor TTS predeterminado:

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "google",      providers: {        google: {          model: "gemini-3.1-flash-tts-preview",          voiceName: "Kore",          audioProfile: "Speak professionally with a calm tone.",        },      },    },  },}
[/code]

Gemini API TTS usa prompting en lenguaje natural para el control de estilo. Define `audioProfile` para anteponer un prompt de estilo reutilizable antes del texto hablado. Define `speakerName` cuando el texto de tu prompt se refiera a un hablante con nombre.

Gemini API TTS también acepta etiquetas de audio expresivas entre corchetes en el texto, como `[whispers]` o `[laughs]`. Para mantener las etiquetas fuera de la respuesta visible del chat mientras se envían a TTS, colócalas dentro de un bloque `[[tts:text]]...[[/tts:text]]`:

textCopy code
[code]
    Here is the clean reply text. [[tts:text]][whispers] Here is the spoken version.[[/tts:text]]
[/code]

## Voz en tiempo real

El Plugin `google` incluido registra un proveedor de voz en tiempo real respaldado por Gemini Live API para puentes de audio de backend como Voice Call y Google Meet.

Ajuste | Ruta de configuración | Valor predeterminado  
---|---|---  
Modelo | `plugins.entries.voice-call.config.realtime.providers.google.model` | `gemini-2.5-flash-native-audio-preview-12-2025`  
Voz | `...google.voice` | `Kore`  
Temperatura | `...google.temperature` | (sin definir)  
Sensibilidad de inicio de VAD | `...google.startSensitivity` | (sin definir)  
Sensibilidad de fin de VAD | `...google.endSensitivity` | (sin definir)  
Duración del silencio | `...google.silenceDurationMs` | (sin definir)  
Manejo de actividad | `...google.activityHandling` | Predeterminado de Google, `start-of-activity-interrupts`  
Cobertura de turno | `...google.turnCoverage` | Predeterminado de Google, `only-activity`  
Desactivar VAD automático | `...google.automaticActivityDetectionDisabled` | `false`  
Reanudación de sesión | `...google.sessionResumption` | `true`  
Compresión de contexto | `...google.contextWindowCompression` | `true`  
Clave de API | `...google.apiKey` | Recurre a `models.providers.google.apiKey`, `GEMINI_API_KEY` o `GOOGLE_API_KEY`  
  
Ejemplo de configuración en tiempo real de Voice Call:

json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        enabled: true,        config: {          realtime: {            enabled: true,            provider: "google",            providers: {              google: {                model: "gemini-2.5-flash-native-audio-preview-12-2025",                voice: "Kore",                activityHandling: "start-of-activity-interrupts",                turnCoverage: "only-activity",              },            },          },        },      },    },  },}
[/code]

Para la verificación en vivo de mantenedores, ejecuta `OPENAI_API_KEY=... GEMINI_API_KEY=... node --import tsx scripts/dev/realtime-talk-live-smoke.ts`. La prueba smoke también cubre rutas de backend/WebRTC de OpenAI; el tramo de Google emite la misma forma de token restringido de Live API que usa Control UI Talk, abre el endpoint WebSocket del navegador, envía la carga inicial de configuración y espera `setupComplete`.

## Configuración avanzada

Direct Gemini cache reuse

Para ejecuciones directas de Gemini API (`api: "google-generative-ai"`), OpenClaw pasa un identificador `cachedContent` configurado a las solicitudes de Gemini.

  * Configura parámetros por modelo o globales con `cachedContent` o el heredado `cached_content`
  * Si ambos están presentes, `cachedContent` tiene prioridad
  * Valor de ejemplo: `cachedContents/prebuilt-context`
  * El uso de aciertos de caché de Gemini se normaliza en `cacheRead` de OpenClaw desde el `cachedContentTokenCount` ascendente

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "google/gemini-2.5-pro": {          params: {            cachedContent: "cachedContents/prebuilt-context",          },        },      },    },  },}
[/code]

Gemini CLI JSON usage notes

Al usar el proveedor OAuth `google-gemini-cli`, OpenClaw normaliza la salida JSON de la CLI de la siguiente manera:

  * El texto de respuesta proviene del campo `response` del JSON de la CLI.
  * El uso recurre a `stats` cuando la CLI deja `usage` vacío.
  * `stats.cached` se normaliza en `cacheRead` de OpenClaw.
  * Si falta `stats.input`, OpenClaw deriva los tokens de entrada de `stats.input_tokens - stats.cached`.

Environment and daemon setup

Si el Gateway se ejecuta como daemon (launchd/systemd), asegúrate de que `GEMINI_API_KEY` esté disponible para ese proceso (por ejemplo, en `~/.openclaw/.env` o mediante `env.shellEnv`).

## Relacionado

[**Model selection** Elegir proveedores, referencias de modelo y comportamiento de conmutación por error. ](</es/concepts/model-providers>) [**Image generation** Parámetros compartidos de la herramienta de imagen y selección de proveedor. ](</es/tools/image-generation>) [**Video generation** Parámetros compartidos de la herramienta de video y selección de proveedor. ](</es/tools/video-generation>) [**Music generation** Parámetros compartidos de la herramienta de música y selección de proveedor. ](</es/tools/music-generation>)

Was this useful?YesNo