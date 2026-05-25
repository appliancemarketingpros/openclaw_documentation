---
title: Texto a voz
source_url: https://docs.openclaw.ai/es/tools/tts
scraped_at: 2026-05-25
---

OpenClaw puede convertir respuestas salientes en audio con **14 proveedores de voz** y entregar mensajes de voz nativos en Feishu, Matrix, Telegram y WhatsApp, archivos de audio adjuntos en todos los demás lugares, y flujos PCM/Ulaw para telefonía y Talk.

TTS es la mitad de salida de voz del modo `stt-tts` de Talk. Las sesiones Talk `realtime` nativas del proveedor sintetizan voz dentro del proveedor en tiempo real en lugar de llamar a esta ruta de TTS, mientras que las sesiones `transcription` no sintetizan una respuesta de voz del asistente.

## Inicio rápido

* ### Elegir un proveedor

OpenAI y ElevenLabs son las opciones alojadas más fiables. Microsoft y Local CLI funcionan sin una clave de API. Consulta la matriz de proveedores para ver la lista completa.

* ### Configurar la clave de API

Exporta la variable de entorno para tu proveedor (por ejemplo `OPENAI_API_KEY`, `ELEVENLABS_API_KEY`). Microsoft y Local CLI no necesitan clave.

* ### Activarlo en la configuración

Configura `messages.tts.auto: "always"` y `messages.tts.provider`:

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "elevenlabs",    },  },}
[/code]

* ### Probarlo en el chat

`/tts status` muestra el estado actual. `/tts audio Hello from OpenClaw` envía una respuesta de audio puntual.

## Proveedores compatibles

Proveedor | Autenticación | Notas  
---|---|---  
**Azure Speech** | `AZURE_SPEECH_KEY` \+ `AZURE_SPEECH_REGION` (también `AZURE_SPEECH_API_KEY`, `SPEECH_KEY`, `SPEECH_REGION`) | Salida nativa de nota de voz Ogg/Opus y telefonía.  
**DeepInfra** | `DEEPINFRA_API_KEY` | TTS compatible con OpenAI. Predeterminado: `hexgrad/Kokoro-82M`.  
**ElevenLabs** | `ELEVENLABS_API_KEY` o `XI_API_KEY` | Clonación de voz, multilingüe, determinista mediante `seed`; en streaming para reproducción de voz de Discord.  
**Google Gemini** | `GEMINI_API_KEY` o `GOOGLE_API_KEY` | TTS por lotes de la API de Gemini; consciente de la personalidad mediante `promptTemplate: "audio-profile-v1"`.  
**Gradium** | `GRADIUM_API_KEY` | Salida de nota de voz y telefonía.  
**Inworld** | `INWORLD_API_KEY` | API de TTS en streaming. Nota de voz Opus nativa y telefonía PCM.  
**Local CLI** | ninguna | Ejecuta un comando local de TTS configurado.  
**Microsoft** | ninguna | TTS neuronal público de Edge mediante `node-edge-tts`. De mejor esfuerzo, sin SLA.  
**MiniMax** | `MINIMAX_API_KEY` (o plan de tokens: `MINIMAX_OAUTH_TOKEN`, `MINIMAX_CODE_PLAN_KEY`, `MINIMAX_CODING_API_KEY`) | API T2A v2. Predeterminado: `speech-2.8-hd`.  
**OpenAI** | `OPENAI_API_KEY` | También se usa para resumen automático; admite `instructions` de personalidad.  
**OpenRouter** | `OPENROUTER_API_KEY` (puede reutilizar `models.providers.openrouter.apiKey`) | Modelo predeterminado `hexgrad/kokoro-82m`.  
**Volcengine** | `VOLCENGINE_TTS_API_KEY` o `BYTEPLUS_SEED_SPEECH_API_KEY` (AppID/token heredados: `VOLCENGINE_TTS_APPID`/`_TOKEN`) | API HTTP de BytePlus Seed Speech.  
**Vydra** | `VYDRA_API_KEY` | Proveedor compartido de imagen, video y voz.  
**xAI** | `XAI_API_KEY` | TTS por lotes de xAI. La nota de voz Opus nativa **no** es compatible.  
**Xiaomi MiMo** | `XIAOMI_API_KEY` | TTS de MiMo mediante completados de chat de Xiaomi.  
  
Si hay varios proveedores configurados, el seleccionado se usa primero y los demás son opciones de respaldo. El resumen automático usa `summaryModel` (o `agents.defaults.model.primary`), por lo que ese proveedor también debe estar autenticado si mantienes los resúmenes activados.

## Configuración

La configuración de TTS vive en `messages.tts` dentro de `~/.openclaw/openclaw.json`. Elige un preajuste y adapta el bloque del proveedor:

### Azure Speech

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "azure-speech",  providers: {    "azure-speech": {      apiKey: "${AZURE_SPEECH_KEY}",      region: "eastus",      voice: "en-US-JennyNeural",      lang: "en-US",      outputFormat: "audio-24khz-48kbitrate-mono-mp3",      voiceNoteOutputFormat: "ogg-24khz-16bit-mono-opus",    },  },},},}
[/code]

### ElevenLabs

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "elevenlabs",  providers: {    elevenlabs: {      apiKey: "${ELEVENLABS_API_KEY}",      model: "eleven_multilingual_v2",      voiceId: "EXAVITQu4vr4xnSDxMaL",    },  },},},}
[/code]

### Google Gemini

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "google",  providers: {    google: {      apiKey: "${GEMINI_API_KEY}",      model: "gemini-3.1-flash-tts-preview",      voiceName: "Kore",      // Optional natural-language style prompts:      // audioProfile: "Speak in a calm, podcast-host tone.",      // speakerName: "Alex",    },  },},},}
[/code]

### Gradium

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "gradium",  providers: {    gradium: {      apiKey: "${GRADIUM_API_KEY}",      voiceId: "YTpq7expH9539ERJ",    },  },},},}
[/code]

### Inworld

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "inworld",  providers: {    inworld: {      apiKey: "${INWORLD_API_KEY}",      modelId: "inworld-tts-1.5-max",      voiceId: "Sarah",      temperature: 0.7,    },  },},},}
[/code]

### Local CLI

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "tts-local-cli",  providers: {    "tts-local-cli": {      command: "say",      args: ["-o", "{{OutputPath}}", "{{Text}}"],      outputFormat: "wav",      timeoutMs: 120000,    },  },},},}
[/code]

### Microsoft (sin clave)

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "microsoft",  providers: {    microsoft: {      enabled: true,      voice: "en-US-MichelleNeural",      lang: "en-US",      outputFormat: "audio-24khz-48kbitrate-mono-mp3",      rate: "+0%",      pitch: "+0%",    },  },},},}
[/code]

### MiniMax

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "minimax",  providers: {    minimax: {      apiKey: "${MINIMAX_API_KEY}",      model: "speech-2.8-hd",      voiceId: "English_expressive_narrator",      speed: 1.0,      vol: 1.0,      pitch: 0,    },  },},},}
[/code]

### OpenAI + ElevenLabs

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "openai",  summaryModel: "openai/gpt-4.1-mini",  modelOverrides: { enabled: true },  providers: {    openai: {      apiKey: "${OPENAI_API_KEY}",      model: "gpt-4o-mini-tts",      voice: "alloy",    },    elevenlabs: {      apiKey: "${ELEVENLABS_API_KEY}",      model: "eleven_multilingual_v2",      voiceId: "EXAVITQu4vr4xnSDxMaL",      voiceSettings: { stability: 0.5, similarityBoost: 0.75, style: 0.0, useSpeakerBoost: true, speed: 1.0 },      applyTextNormalization: "auto",      languageCode: "en",    },  },},},}
[/code]

### OpenRouter

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "openrouter",  providers: {    openrouter: {      apiKey: "${OPENROUTER_API_KEY}",      model: "hexgrad/kokoro-82m",      voice: "af_alloy",      responseFormat: "mp3",    },  },},},}
[/code]

### Volcengine

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "volcengine",  providers: {    volcengine: {      apiKey: "${VOLCENGINE_TTS_API_KEY}",      resourceId: "seed-tts-1.0",      voice: "en_female_anna_mars_bigtts",    },  },},},}
[/code]

### xAI

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "xai",  providers: {    xai: {      apiKey: "${XAI_API_KEY}",      voiceId: "eve",      language: "en",      responseFormat: "mp3",    },  },},},}
[/code]

### Xiaomi MiMo

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "xiaomi",  providers: {    xiaomi: {      apiKey: "${XIAOMI_API_KEY}",      model: "mimo-v2.5-tts",      voice: "mimo_default",      format: "mp3",    },  },},},}
[/code]

### Sobrescrituras de voz por agente

Usa `agents.list[].tts` cuando un agente deba hablar con un proveedor, voz, modelo, personalidad o modo Auto-TTS diferente. El bloque del agente se fusiona en profundidad sobre `messages.tts`, por lo que las credenciales del proveedor pueden permanecer en la configuración global del proveedor:

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "elevenlabs",      providers: {        elevenlabs: { apiKey: "${ELEVENLABS_API_KEY}", model: "eleven_multilingual_v2" },      },    },  },  agents: {    list: [      {        id: "reader",        tts: {          providers: {            elevenlabs: { voiceId: "EXAVITQu4vr4xnSDxMaL" },          },        },      },    ],  },}
[/code]

Para fijar una persona por agente, define `agents.list[].tts.persona` junto con la configuración del proveedor; anula `messages.tts.persona` global solo para ese agente.

Orden de precedencia para respuestas automáticas, `/tts audio`, `/tts status` y la herramienta de agente `tts`:

  1. `messages.tts`
  2. `agents.list[].tts` activo
  3. anulación de canal, cuando el canal admite `channels.<channel>.tts`
  4. anulación de cuenta, cuando el canal pasa `channels.<channel>.accounts.<id>.tts`
  5. preferencias locales de `/tts` para este host
  6. directivas en línea `[[tts:...]]` cuando las anulaciones controladas por el modelo están habilitadas


Las anulaciones de canal y cuenta usan la misma forma que `messages.tts` y se combinan en profundidad sobre las capas anteriores, de modo que las credenciales compartidas del proveedor pueden permanecer en `messages.tts` mientras un canal o una cuenta de bot cambia solo la voz, el modelo, la persona o el modo automático:

json5Copy code
[code]
    {  messages: {    tts: {      provider: "openai",      providers: {        openai: { apiKey: "${OPENAI_API_KEY}", model: "gpt-4o-mini-tts" },      },    },  },  channels: {    feishu: {      accounts: {        english: {          tts: {            providers: {              openai: { voice: "shimmer" },            },          },        },      },    },  },}
[/code]

## Personas

Una **persona** es una identidad hablada estable que puede aplicarse de forma determinista entre proveedores. Puede preferir un proveedor, definir una intención de prompt neutral respecto al proveedor y contener vinculaciones específicas del proveedor para voces, modelos, plantillas de prompt, semillas y ajustes de voz.

### Persona mínima

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      persona: "narrator",      personas: {        narrator: {          label: "Narrator",          provider: "elevenlabs",          providers: {            elevenlabs: { voiceId: "EXAVITQu4vr4xnSDxMaL", modelId: "eleven_multilingual_v2" },          },        },      },    },  },}
[/code]

### Persona completa (prompt neutral respecto al proveedor)

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      persona: "alfred",      personas: {        alfred: {          label: "Alfred",          description: "Dry, warm British butler narrator.",          provider: "google",          fallbackPolicy: "preserve-persona",          prompt: {            profile: "A brilliant British butler. Dry, witty, warm, charming, emotionally expressive, never generic.",            scene: "A quiet late-night study. Close-mic narration for a trusted operator.",            sampleContext: "The speaker is answering a private technical request with concise confidence and dry warmth.",            style: "Refined, understated, lightly amused.",            accent: "British English.",            pacing: "Measured, with short dramatic pauses.",            constraints: ["Do not read configuration values aloud.", "Do not explain the persona."],          },          providers: {            google: {              model: "gemini-3.1-flash-tts-preview",              voiceName: "Algieba",              promptTemplate: "audio-profile-v1",            },            openai: { model: "gpt-4o-mini-tts", voice: "cedar" },            elevenlabs: {              voiceId: "voice_id",              modelId: "eleven_multilingual_v2",              seed: 42,              voiceSettings: {                stability: 0.65,                similarityBoost: 0.8,                style: 0.25,                useSpeakerBoost: true,                speed: 0.95,              },            },          },        },      },    },  },}
[/code]

### Resolución de persona

La persona activa se selecciona de forma determinista:

  1. Preferencia local `/tts persona <id>`, si está definida.
  2. `messages.tts.persona`, si está definida.
  3. Sin persona.


La selección del proveedor se ejecuta dando prioridad a lo explícito:

  1. Anulaciones directas (CLI, Gateway, Talk, directivas TTS permitidas).
  2. Preferencia local `/tts provider <id>`.
  3. `provider` de la persona activa.
  4. `messages.tts.provider`.
  5. Selección automática del registro.


Para cada intento de proveedor, OpenClaw combina las configuraciones en este orden:

  1. `messages.tts.providers.<id>`
  2. `messages.tts.personas.<persona>.providers.<id>`
  3. Anulaciones de solicitud confiables
  4. Anulaciones de directivas TTS emitidas por el modelo y permitidas


### Cómo usan los proveedores los prompts de persona

Los campos de prompt de persona (`profile`, `scene`, `sampleContext`, `style`, `accent`, `pacing`, `constraints`) son **neutrales respecto al proveedor**. Cada proveedor decide cómo usarlos:

Google Gemini

Envuelve los campos de prompt de persona en una estructura de prompt TTS de Gemini **solo cuando** la configuración efectiva del proveedor de Google establece `promptTemplate: "audio-profile-v1"` o `personaPrompt`. Los campos anteriores `audioProfile` y `speakerName` todavía se anteponen como texto de prompt específico de Google. Las etiquetas de audio en línea como `[whispers]` o `[laughs]` dentro de un bloque `[[tts:text]]` se preservan dentro de la transcripción de Gemini; OpenClaw no genera estas etiquetas.

OpenAI

Asigna los campos de prompt de persona al campo `instructions` de la solicitud **solo cuando** no hay `instructions` explícitas de OpenAI configuradas. Las `instructions` explícitas siempre tienen prioridad.

Other providers

Usan solo las vinculaciones de persona específicas del proveedor bajo `personas.<id>.providers.<provider>`. Los campos de prompt de persona se ignoran a menos que el proveedor implemente su propia asignación de prompt de persona.

### Política de fallback

`fallbackPolicy` controla el comportamiento cuando una persona **no tiene vinculación** para el proveedor intentado:

Política | Comportamiento  
---|---  
`preserve-persona` | **Predeterminado.** Los campos de prompt neutrales respecto al proveedor siguen disponibles; el proveedor puede usarlos o ignorarlos.  
`provider-defaults` | La persona se omite de la preparación del prompt para ese intento; el proveedor usa sus valores predeterminados neutros mientras continúa el fallback a otros proveedores.  
`fail` | Omite ese intento de proveedor con `reasonCode: "not_configured"` y `personaBinding: "missing"`. Los proveedores de fallback se siguen intentando.  
  
La solicitud TTS completa solo falla cuando **todos** los proveedores intentados se omiten o fallan.

La selección de proveedor de sesión de Talk tiene alcance de sesión. Un cliente de Talk debe elegir identificadores de proveedor, identificadores de modelo, identificadores de voz y configuraciones regionales desde `talk.catalog` y pasarlos mediante la sesión de Talk o la solicitud de traspaso. Abrir una sesión de voz no debe mutar `messages.tts` ni los valores predeterminados globales del proveedor de Talk.

## Directivas controladas por el modelo

De forma predeterminada, el asistente **puede** emitir directivas `[[tts:...]]` para anular la voz, el modelo o la velocidad de una sola respuesta, además de un bloque opcional `[[tts:text]]...[[/tts:text]]` para indicaciones expresivas que deben aparecer solo en el audio:

textCopy code
[code]
    Here you go. [[tts:voiceId=pMsXgVXv3BLzUgSXRplE model=eleven_v3 speed=1.1]][[tts:text]](laughs) Read the song once more.[[/tts:text]]
[/code]

Cuando `messages.tts.auto` es `"tagged"`, **se requieren directivas** para activar el audio. La entrega de bloques en streaming elimina las directivas del texto visible antes de que el canal las vea, incluso cuando están divididas entre bloques adyacentes.

`provider=...` se ignora a menos que `modelOverrides.allowProvider: true`. Cuando una respuesta declara `provider=...`, las demás claves de esa directiva solo las analiza ese proveedor; las claves no admitidas se eliminan y se informan como advertencias de directiva TTS.

**Claves de directiva disponibles:**

  * `provider` (identificador de proveedor registrado; requiere `allowProvider: true`)
  * `voice` / `voiceName` / `voice_name` / `google_voice` / `voiceId`
  * `model` / `google_model`
  * `stability`, `similarityBoost`, `style`, `speed`, `useSpeakerBoost`
  * `vol` / `volume` (volumen de MiniMax, 0–10)
  * `pitch` (tono entero de MiniMax, −12 a 12; los valores fraccionarios se truncan)
  * `emotion` (etiqueta de emoción de Volcengine)
  * `applyTextNormalization` (`auto|on|off`)
  * `languageCode` (ISO 639-1)
  * `seed`


**Deshabilitar por completo las anulaciones del modelo:**

json5Copy code
[code]
    { messages: { tts: { modelOverrides: { enabled: false } } } }
[/code]

**Permitir el cambio de proveedor mientras se mantienen configurables los demás controles:**

json5Copy code
[code]
    { messages: { tts: { modelOverrides: { enabled: true, allowProvider: true, allowSeed: false } } } }
[/code]

## Comandos de barra

Un único comando `/tts`. En Discord, OpenClaw también registra `/voice` porque `/tts` es un comando integrado de Discord; el texto `/tts ...` sigue funcionando.

textCopy code
[code]
    /tts off | on | status/tts chat on | off | default/tts latest/tts provider <id>/tts persona <id> | off/tts limit <chars>/tts summary off/tts audio <text>
[/code]

Notas de comportamiento:

  * `/tts on` escribe la preferencia TTS local en `always`; `/tts off` la escribe en `off`.
  * `/tts chat on|off|default` escribe una anulación de TTS automática con alcance de sesión para el chat actual.
  * `/tts persona <id>` escribe la preferencia de persona local; `/tts persona off` la borra.
  * `/tts latest` lee la última respuesta del asistente de la transcripción de la sesión actual y la envía como audio una vez. Almacena solo un hash de esa respuesta en la entrada de sesión para evitar envíos de voz duplicados.
  * `/tts audio` genera una respuesta de audio puntual (no activa TTS).
  * `limit` y `summary` se almacenan en **preferencias locales** , no en la configuración principal.
  * `/tts status` incluye diagnósticos de fallback para el último intento: `Fallback: <primary> -> <used>`, `Attempts: ...` y detalle por intento (`provider:outcome(reasonCode) latency`).
  * `/status` muestra el modo TTS activo junto con el proveedor, el modelo, la voz y los metadatos saneados del endpoint personalizado configurados cuando TTS está habilitado.


## Preferencias por usuario

Los comandos de barra escriben anulaciones locales en `prefsPath`. El valor predeterminado es `~/.openclaw/settings/tts.json`; anúlalo con la variable de entorno `OPENCLAW_TTS_PREFS` o `messages.tts.prefsPath`.

Campo almacenado | Efecto  
---|---  
`auto` | Anulación local de TTS automático (`always`, `off`, …)  
`provider` | Anulación local del proveedor primario  
`persona` | Anulación local de persona  
`maxLength` | Umbral de resumen (`1500` caracteres predeterminado)  
`summarize` | Activación de resumen (`true` predeterminado)  
  
Estos anulan la configuración efectiva de `messages.tts` más el bloque `agents.list[].tts` activo para ese host.

## Formatos de salida (fijos)

La entrega de voz TTS está controlada por las capacidades del canal. Los plugins de canal anuncian si la TTS de estilo voz debe pedir a los proveedores un destino nativo `voice-note` o mantener la síntesis normal `audio-file` y solo marcar la salida compatible para entrega de voz.

  * **Canales compatibles con notas de voz** : las respuestas de nota de voz prefieren Opus (`opus_48000_64` de ElevenLabs, `opus` de OpenAI). 
    * 48kHz / 64kbps ofrece un buen equilibrio para mensajes de voz.
  * **Feishu / WhatsApp** : cuando una respuesta de nota de voz se genera como MP3/WebM/WAV/M4A u otro archivo probablemente de audio, el Plugin del canal la transcodifica a Ogg/Opus de 48kHz con `ffmpeg` antes de enviar el mensaje de voz nativo. WhatsApp envía el resultado mediante la carga útil `audio` de Baileys con `ptt: true` y `audio/ogg; codecs=opus`. Si la conversión falla, Feishu recibe el archivo original como adjunto; el envío de WhatsApp falla en lugar de publicar una carga útil PTT incompatible.
  * **Otros canales** : MP3 (`mp3_44100_128` de ElevenLabs, `mp3` de OpenAI). 
    * 44.1kHz / 128kbps es el equilibrio predeterminado para la claridad del habla.
  * **MiniMax** : MP3 (modelo `speech-2.8-hd`, frecuencia de muestreo de 32kHz) para adjuntos de audio normales. Para destinos de nota de voz anunciados por el canal, OpenClaw transcodifica el MP3 de MiniMax a Opus de 48kHz con `ffmpeg` antes de la entrega cuando el canal anuncia transcodificación.
  * **Xiaomi MiMo** : MP3 de forma predeterminada, o WAV cuando se configura. Para destinos de nota de voz anunciados por el canal, OpenClaw transcodifica la salida de Xiaomi a Opus de 48kHz con `ffmpeg` antes de la entrega cuando el canal anuncia transcodificación.
  * **CLI local** : usa el `outputFormat` configurado. Los destinos de nota de voz se convierten a Ogg/Opus y la salida de telefonía se convierte a PCM mono sin procesar de 16 kHz con `ffmpeg`.
  * **Google Gemini** : TTS de la API de Gemini devuelve PCM sin procesar de 24kHz. OpenClaw lo envuelve como WAV para adjuntos de audio, lo transcodifica a Opus de 48kHz para destinos de nota de voz y devuelve PCM directamente para Talk/telefonía.
  * **Gradium** : WAV para adjuntos de audio, Opus para destinos de nota de voz y `ulaw_8000` a 8 kHz para telefonía.
  * **Inworld** : MP3 para adjuntos de audio normales, `OGG_OPUS` nativo para destinos de nota de voz y `PCM` sin procesar a 22050 Hz para Talk/telefonía.
  * **xAI** : MP3 de forma predeterminada; `responseFormat` puede ser `mp3`, `wav`, `pcm`, `mulaw` o `alaw`. OpenClaw usa el endpoint REST TTS por lotes de xAI y devuelve un adjunto de audio completo; el WebSocket TTS de streaming de xAI no se usa en esta ruta de proveedor. Esta ruta no admite formato Opus nativo para notas de voz.
  * **Microsoft** : usa `microsoft.outputFormat` (predeterminado `audio-24khz-48kbitrate-mono-mp3`). 
    * El transporte incluido acepta un `outputFormat`, pero no todos los formatos están disponibles en el servicio.
    * Los valores de formato de salida siguen los formatos de salida de Microsoft Speech (incluido Ogg/WebM Opus).
    * Telegram `sendVoice` acepta OGG/MP3/M4A; usa OpenAI/ElevenLabs si necesitas mensajes de voz Opus garantizados.
    * Si el formato de salida configurado de Microsoft falla, OpenClaw reintenta con MP3.


Los formatos de salida de OpenAI/ElevenLabs son fijos por canal (consulta lo anterior).

## Comportamiento de Auto-TTS

Cuando `messages.tts.auto` está habilitado, OpenClaw:

  * Omite TTS si la respuesta ya contiene contenido multimedia o una directiva `MEDIA:`.
  * Omite respuestas muy cortas (menos de 10 caracteres).
  * Resume respuestas largas cuando los resúmenes están habilitados, usando `summaryModel` (o `agents.defaults.model.primary`).
  * Adjunta el audio generado a la respuesta.
  * En `mode: "final"`, sigue enviando TTS solo de audio para respuestas finales transmitidas después de que se completa el flujo de texto; el contenido multimedia generado pasa por la misma normalización de contenido multimedia del canal que los adjuntos de respuesta normales.


Si la respuesta supera `maxLength` y el resumen está desactivado (o no hay clave de API para el modelo de resumen), se omite el audio y se envía la respuesta de texto normal.

textCopy code
[code]
    Reply -> TTS enabled?  no  -> send text  yes -> has media / MEDIA: / short?          yes -> send text          no  -> length > limit?                   no  -> TTS -> attach audio                   yes -> summary enabled?                            no  -> send text                            yes -> summarize -> TTS -> attach audio
[/code]

## Formatos de salida por canal

Destino | Formato  
---|---  
Feishu / Matrix / Telegram / WhatsApp | Las respuestas de nota de voz prefieren **Opus** (`opus_48000_64` de ElevenLabs, `opus` de OpenAI). 48 kHz / 64 kbps equilibra claridad y tamaño.  
Otros canales | **MP3** (`mp3_44100_128` de ElevenLabs, `mp3` de OpenAI). 44,1 kHz / 128 kbps es el valor predeterminado para voz.  
Talk / telefonía | **PCM** nativo del proveedor (Inworld 22050 Hz, Google 24 kHz), o `ulaw_8000` de Gradium para telefonía.  
  
Notas por proveedor:

  * **Transcodificación de Feishu / WhatsApp:** Cuando una respuesta de nota de voz llega como MP3/WebM/WAV/M4A, el plugin del canal la transcodifica a Ogg/Opus de 48 kHz con `ffmpeg`. WhatsApp envía mediante Baileys con `ptt: true` y `audio/ogg; codecs=opus`. Si la conversión falla: Feishu recurre a adjuntar el archivo original; el envío de WhatsApp falla en lugar de publicar una carga PTT incompatible.
  * **MiniMax / Xiaomi MiMo:** MP3 predeterminado (32 kHz para MiniMax `speech-2.8-hd`); se transcodifica a Opus de 48 kHz para destinos de nota de voz mediante `ffmpeg`.
  * **CLI local:** Usa el `outputFormat` configurado. Los destinos de nota de voz se convierten a Ogg/Opus y la salida de telefonía a PCM mono sin procesar de 16 kHz.
  * **Google Gemini:** Devuelve PCM sin procesar de 24 kHz. OpenClaw lo envuelve como WAV para adjuntos, lo transcodifica a Opus de 48 kHz para destinos de nota de voz y devuelve PCM directamente para Talk/telefonía.
  * **Inworld:** Adjuntos MP3, nota de voz nativa `OGG_OPUS`, `PCM` sin procesar de 22050 Hz para Talk/telefonía.
  * **xAI:** MP3 de forma predeterminada; `responseFormat` puede ser `mp3|wav|pcm|mulaw|alaw`. Usa el endpoint REST por lotes de xAI; **no** se usa TTS por WebSocket en streaming. El formato nativo de nota de voz Opus **no** es compatible.
  * **Microsoft:** Usa `microsoft.outputFormat` (predeterminado `audio-24khz-48kbitrate-mono-mp3`). Telegram `sendVoice` acepta OGG/MP3/M4A; usa OpenAI/ElevenLabs si necesitas mensajes de voz Opus garantizados. Si el formato de Microsoft configurado falla, OpenClaw reintenta con MP3.


Los formatos de salida de OpenAI y ElevenLabs son fijos por canal, como se indica arriba.

## Referencia de campos

Top-level messages.tts.*

Modo Auto-TTS. `inbound` solo envía audio después de un mensaje de voz entrante; `tagged` solo envía audio cuando la respuesta incluye directivas `[[tts:...]]` o un bloque `[[tts:text]]`.

Conmutador heredado. `openclaw doctor --fix` migra esto a `auto`.

`"all"` incluye respuestas de herramientas/bloques además de las respuestas finales.

Id. del proveedor de voz. Cuando no se define, OpenClaw usa el primer proveedor configurado en el orden de selección automática del registro. El `provider: "edge"` heredado se reescribe como `"microsoft"` mediante `openclaw doctor --fix`.

Id. de persona activa de `personas`. Normalizado a minúsculas.

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InBlcnNvbmFzLjxpZA " type="object"> Identidad hablada estable. Campos: `label`, `description`, `provider`, `fallbackPolicy`, `prompt`, `providers.<provider>`. Consulta Personas.

Modelo económico para resumen automático; el valor predeterminado es `agents.defaults.model.primary`. Acepta `provider/model` o un alias de modelo configurado.

Permite que el modelo emita directivas TTS. El valor predeterminado de `enabled` es `true`; el valor predeterminado de `allowProvider` es `false`.

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InByb3ZpZGVycy48aWQ " type="object"> Configuración propiedad del proveedor indexada por id. de proveedor de voz. Los bloques directos heredados (`messages.tts.openai`, `.elevenlabs`, `.microsoft`, `.edge`) se reescriben mediante `openclaw doctor --fix`; confirma solo `messages.tts.providers.<id>`.

Límite estricto para caracteres de entrada de TTS. `/tts audio` falla si se supera.

Tiempo de espera de solicitud en milisegundos.

Sobrescribe la ruta JSON de preferencias locales (proveedor/límite/resumen). Valor predeterminado `~/.openclaw/settings/tts.json`.

Azure Speech

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Env: `AZURE_SPEECH_KEY`, `AZURE_SPEECH_API_KEY` o `SPEECH_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InJlZ2lvbiIgdHlwZT0ic3RyaW5nIg Región de Azure Speech (por ejemplo, `eastus`). Env: `AZURE_SPEECH_REGION` o `SPEECH_REGION`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImVuZHBvaW50IiB0eXBlPSJzdHJpbmci Sobrescritura opcional del endpoint de Azure Speech (alias `baseUrl`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlIiB0eXBlPSJzdHJpbmci ShortName de voz de Azure. Valor predeterminado `en-US-JennyNeural`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImxhbmciIHR5cGU9InN0cmluZyI Código de idioma SSML. Valor predeterminado `en-US`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im91dHB1dEZvcm1hdCIgdHlwZT0ic3RyaW5nIg `X-Microsoft-OutputFormat` de Azure para audio estándar. Valor predeterminado `audio-24khz-48kbitrate-mono-mp3`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlTm90ZU91dHB1dEZvcm1hdCIgdHlwZT0ic3RyaW5nIg `X-Microsoft-OutputFormat` de Azure para salida de nota de voz. Valor predeterminado `ogg-24khz-16bit-mono-opus`. OPENCLAW_DOCS_MARKER:paramClose:

ElevenLabs

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Recurrirá a `ELEVENLABS_API_KEY` o `XI_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci Id. de modelo (por ejemplo, `eleven_multilingual_v2`, `eleven_v3`). OPENCLAW_DOCS_MARKER:paramClose:

`stability`, `similarityBoost`, `style` (cada uno `0..1`), `useSpeakerBoost` (`true|false`), `speed` (`0.5..2.0`, `1.0` = normal).

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Imxhbmd1YWdlQ29kZSIgdHlwZT0ic3RyaW5nIg ISO 639-1 de 2 letras (por ejemplo, `en`, `de`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InNlZWQiIHR5cGU9Im51bWJlciI Entero `0..4294967295` para determinismo de mejor esfuerzo. OPENCLAW_DOCS_MARKER:paramClose:

Google Gemini

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Recurrirá a `GEMINI_API_KEY` / `GOOGLE_API_KEY`. Si se omite, TTS puede reutilizar `models.providers.google.apiKey` antes de recurrir al entorno. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci Modelo TTS de Gemini. Valor predeterminado `gemini-3.1-flash-tts-preview`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlTmFtZSIgdHlwZT0ic3RyaW5nIg Nombre de voz preconstruida de Gemini. Valor predeterminado `Kore`. Alias: `voice`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InByb21wdFRlbXBsYXRlIiB0eXBlPSciYXVkaW8tcHJvZmlsZS12MSIn Establécelo en `audio-profile-v1` para envolver los campos de prompt de persona activa en una estructura de prompt TTS de Gemini determinista. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI Solo se acepta `https://generativelanguage.googleapis.com`. OPENCLAW_DOCS_MARKER:paramClose:

Gradium

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Entorno: `GRADIUM_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI Predeterminado `https://api.gradium.ai`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlSWQiIHR5cGU9InN0cmluZyI Predeterminado Emma (`YTpq7expH9539ERJ`). OPENCLAW_DOCS_MARKER:paramClose:

Inworld

### Inworld principal

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Entorno: `INWORLD_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI Predeterminado `https://api.inworld.ai`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsSWQiIHR5cGU9InN0cmluZyI Predeterminado `inworld-tts-1.5-max`. También: `inworld-tts-1.5-mini`, `inworld-tts-1-max`, `inworld-tts-1`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlSWQiIHR5cGU9InN0cmluZyI Predeterminado `Sarah`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InRlbXBlcmF0dXJlIiB0eXBlPSJudW1iZXIi Temperatura de muestreo `0..2`. OPENCLAW_DOCS_MARKER:paramClose:

CLI local (tts-local-cli)

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFyZ3MiIHR5cGU9InN0cmluZ1tdIg Argumentos del comando. Admite los marcadores de posición `{{Text}}`, `{{OutputPath}}`, `{{OutputDir}}`, `{{OutputBase}}`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im91dHB1dEZvcm1hdCIgdHlwZT0nIm1wMyIgfCAib3B1cyIgfCAid2F2Iic Formato de salida esperado de la CLI. Predeterminado `mp3` para archivos adjuntos de audio. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InRpbWVvdXRNcyIgdHlwZT0ibnVtYmVyIg Tiempo de espera del comando en milisegundos. Predeterminado `120000`. OPENCLAW_DOCS_MARKER:paramClose:

Microsoft (sin clave de API)

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlIiB0eXBlPSJzdHJpbmci Nombre de voz neuronal de Microsoft (p. ej., `en-US-MichelleNeural`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImxhbmciIHR5cGU9InN0cmluZyI Código de idioma (p. ej., `en-US`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im91dHB1dEZvcm1hdCIgdHlwZT0ic3RyaW5nIg Formato de salida de Microsoft. Predeterminado `audio-24khz-48kbitrate-mono-mp3`. No todos los formatos son compatibles con el transporte incluido respaldado por Edge. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InJhdGUgLyBwaXRjaCAvIHZvbHVtZSIgdHlwZT0ic3RyaW5nIg Cadenas de porcentaje (p. ej., `+10%`, `-5%`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImVkZ2UuKiIgdHlwZT0ib2JqZWN0IiBkZXByZWNhdGVk Alias heredado. Ejecuta `openclaw doctor --fix` para reescribir la configuración persistida en `providers.microsoft`. OPENCLAW_DOCS_MARKER:paramClose:

MiniMax

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Recurrirá a `MINIMAX_API_KEY`. Autenticación Token Plan mediante `MINIMAX_OAUTH_TOKEN`, `MINIMAX_CODE_PLAN_KEY` o `MINIMAX_CODING_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI Predeterminado `https://api.minimax.io`. Entorno: `MINIMAX_API_HOST`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci Predeterminado `speech-2.8-hd`. Entorno: `MINIMAX_TTS_MODEL`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlSWQiIHR5cGU9InN0cmluZyI Predeterminado `English_expressive_narrator`. Entorno: `MINIMAX_TTS_VOICE_ID`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InNwZWVkIiB0eXBlPSJudW1iZXIi `0.5..2.0`. Predeterminado `1.0`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvbCIgdHlwZT0ibnVtYmVyIg `(0, 10]`. Predeterminado `1.0`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InBpdGNoIiB0eXBlPSJudW1iZXIi Entero `-12..12`. Predeterminado `0`. Los valores fraccionarios se truncan antes de la solicitud. OPENCLAW_DOCS_MARKER:paramClose:

OpenAI

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Recurrirá a `OPENAI_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci Id. de modelo TTS de OpenAI (p. ej., `gpt-4o-mini-tts`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlIiB0eXBlPSJzdHJpbmci Nombre de voz (p. ej., `alloy`, `cedar`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Imluc3RydWN0aW9ucyIgdHlwZT0ic3RyaW5nIg Campo `instructions` explícito de OpenAI. Cuando se establece, los campos de prompt de persona **no** se asignan automáticamente. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImV4dHJhQm9keSAvIGV4dHJhX2JvZHkiIHR5cGU9IlJlY29yZDxzdHJpbmcsIHVua25vd24 ">Campos JSON adicionales fusionados en los cuerpos de solicitud `/audio/speech` después de los campos TTS de OpenAI generados. Usa esto para endpoints compatibles con OpenAI, como Kokoro, que requieren claves específicas del proveedor como `lang`; las claves de prototipo no seguras se ignoran. OPENCLAW_DOCS_MARKER:paramClose:

Sobrescribe el endpoint TTS de OpenAI. Orden de resolución: configuración → `OPENAI_TTS_BASE_URL` → `https://api.openai.com/v1`. Los valores no predeterminados se tratan como endpoints TTS compatibles con OpenAI, por lo que se aceptan nombres de modelo y voz personalizados.

OpenRouter

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Entorno: `OPENROUTER_API_KEY`. Puede reutilizar `models.providers.openrouter.apiKey`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI Predeterminado `https://openrouter.ai/api/v1`. El heredado `https://openrouter.ai/v1` se normaliza. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci Predeterminado `hexgrad/kokoro-82m`. Alias: `modelId`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlIiB0eXBlPSJzdHJpbmci Predeterminado `af_alloy`. Alias: `voiceId`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InJlc3BvbnNlRm9ybWF0IiB0eXBlPScibXAzIiB8ICJwY20iJw Predeterminado `mp3`. OPENCLAW_DOCS_MARKER:paramClose:

Volcengine (BytePlus Seed Speech)

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Entorno: `VOLCENGINE_TTS_API_KEY` o `BYTEPLUS_SEED_SPEECH_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InJlc291cmNlSWQiIHR5cGU9InN0cmluZyI Predeterminado `seed-tts-1.0`. Entorno: `VOLCENGINE_TTS_RESOURCE_ID`. Usa `seed-tts-2.0` cuando tu proyecto tenga autorización de TTS 2.0. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwcEtleSIgdHlwZT0ic3RyaW5nIg Encabezado de clave de aplicación. Predeterminado `aGjiRDfUWi`. Entorno: `VOLCENGINE_TTS_APP_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI Sobrescribe el endpoint HTTP de TTS de Seed Speech. Entorno: `VOLCENGINE_TTS_BASE_URL`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlIiB0eXBlPSJzdHJpbmci Tipo de voz. Predeterminado `en_female_anna_mars_bigtts`. Entorno: `VOLCENGINE_TTS_VOICE`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwcElkIC8gdG9rZW4gLyBjbHVzdGVyIiB0eXBlPSJzdHJpbmciIGRlcHJlY2F0ZWQ Campos heredados de Volcengine Speech Console. Entorno: `VOLCENGINE_TTS_APPID`, `VOLCENGINE_TTS_TOKEN`, `VOLCENGINE_TTS_CLUSTER` (predeterminado `volcano_tts`). OPENCLAW_DOCS_MARKER:paramClose:

xAI

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Entorno: `XAI_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI Predeterminado `https://api.x.ai/v1`. Entorno: `XAI_BASE_URL`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlSWQiIHR5cGU9InN0cmluZyI Predeterminado `eve`. Voces en vivo: `ara`, `eve`, `leo`, `rex`, `sal`, `una`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Imxhbmd1YWdlIiB0eXBlPSJzdHJpbmci Código de idioma BCP-47 o `auto`. Predeterminado `en`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InJlc3BvbnNlRm9ybWF0IiB0eXBlPScibXAzIiB8ICJ3YXYiIHwgInBjbSIgfCAibXVsYXciIHwgImFsYXciJw Predeterminado `mp3`. OPENCLAW_DOCS_MARKER:paramClose:

Xiaomi MiMo

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Entorno: `XIAOMI_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI Predeterminado `https://api.xiaomimimo.com/v1`. Entorno: `XIAOMI_BASE_URL`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci Predeterminado `mimo-v2.5-tts`. Entorno: `XIAOMI_TTS_MODEL`. También admite `mimo-v2-tts`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlIiB0eXBlPSJzdHJpbmci Predeterminado `mimo_default`. Entorno: `XIAOMI_TTS_VOICE`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImZvcm1hdCIgdHlwZT0nIm1wMyIgfCAid2F2Iic Predeterminado `mp3`. Entorno: `XIAOMI_TTS_FORMAT`. OPENCLAW_DOCS_MARKER:paramClose:

## Herramienta de agente

La herramienta `tts` convierte texto a voz y devuelve un adjunto de audio para entregar la respuesta. En Feishu, Matrix, Telegram y WhatsApp, el audio se entrega como mensaje de voz en lugar de como archivo adjunto. Feishu y WhatsApp pueden transcodificar salidas TTS que no sean Opus en esta ruta cuando `ffmpeg` está disponible.

WhatsApp envía audio mediante Baileys como nota de voz PTT (`audio` con `ptt: true`) y envía el texto visible **por separado** del audio PTT porque los clientes no siempre renderizan subtítulos en las notas de voz.

La herramienta acepta los campos opcionales `channel` y `timeoutMs`; `timeoutMs` es un tiempo de espera de solicitud del proveedor por llamada en milisegundos.

## RPC de Gateway

Método | Propósito  
---|---  
`tts.status` | Lee el estado actual de TTS y el último intento.  
`tts.enable` | Establece la preferencia automática local en `always`.  
`tts.disable` | Establece la preferencia automática local en `off`.  
`tts.convert` | Texto a audio de una sola vez.  
`tts.setProvider` | Establece la preferencia local de proveedor.  
`tts.setPersona` | Establece la preferencia local de persona.  
`tts.providers` | Lista los proveedores configurados y su estado.  
  
## Enlaces de servicio

  * [Guía de texto a voz de OpenAI](<https://platform.openai.com/docs/guides/text-to-speech>)
  * [Referencia de la API de audio de OpenAI](<https://platform.openai.com/docs/api-reference/audio>)
  * [Texto a voz REST de Azure Speech](<https://learn.microsoft.com/azure/ai-services/speech-service/rest-text-to-speech>)
  * [Proveedor de Azure Speech](</es/providers/azure-speech>)
  * [Texto a voz de ElevenLabs](<https://elevenlabs.io/docs/api-reference/text-to-speech>)
  * [Autenticación de ElevenLabs](<https://elevenlabs.io/docs/api-reference/authentication>)
  * [Gradium](</es/providers/gradium>)
  * [API de TTS de Inworld](<https://docs.inworld.ai/tts/tts>)
  * [API T2A v2 de MiniMax](<https://platform.minimaxi.com/document/T2A%20V2>)
  * [API HTTP de TTS de Volcengine](</es/providers/volcengine#text-to-speech>)
  * [Síntesis de voz de Xiaomi MiMo](</es/providers/xiaomi#text-to-speech>)
  * [node-edge-tts](<https://github.com/SchneeHertz/node-edge-tts>)
  * [Formatos de salida de Microsoft Speech](<https://learn.microsoft.com/azure/ai-services/speech-service/rest-text-to-speech#audio-outputs>)
  * [Texto a voz de xAI](<https://docs.x.ai/developers/rest-api-reference/inference/voice#text-to-speech-rest>)


## Relacionado

  * [Resumen de medios](</es/tools/media-overview>)
  * [Generación de música](</es/tools/music-generation>)
  * [Generación de video](</es/tools/video-generation>)
  * [Comandos slash](</es/tools/slash-commands>)
  * [Plugin de llamada de voz](</es/plugins/voice-call>)


Was this useful?YesNo