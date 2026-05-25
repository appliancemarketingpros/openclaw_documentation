---
title: OpenRouter
source_url: https://docs.openclaw.ai/es/providers/openrouter
scraped_at: 2026-05-25
---

OpenRouter proporciona una **API unificada** que enruta solicitudes a muchos modelos detrás de un único endpoint y clave de API. Es compatible con OpenAI, por lo que la mayoría de los SDK de OpenAI funcionan cambiando la URL base.

## Primeros pasos

* ### Obtén tu clave de API

Crea una clave de API en [openrouter.ai/keys](<https://openrouter.ai/keys>).

* ### Ejecuta la incorporación

bashCopy code
[code]
    openclaw onboard --auth-choice openrouter-api-key
[/code]

* ### (Opcional) Cambia a un modelo específico

La incorporación usa `openrouter/auto` de forma predeterminada. Elige un modelo concreto más adelante:

bashCopy code
[code]
    openclaw models set openrouter/<provider>/<model>
[/code]

## Ejemplo de configuración

json5Copy code
[code]
    {  env: { OPENROUTER_API_KEY: "sk-or-..." },  agents: {    defaults: {      model: { primary: "openrouter/auto" },    },  },}
[/code]

## Referencias de modelos

Ejemplos de respaldo incluidos:

Referencia de modelo | Notas  
---|---  
`openrouter/auto` | Enrutamiento automático de OpenRouter  
`openrouter/moonshotai/kimi-k2.6` | Kimi K2.6 mediante MoonshotAI  
`openrouter/moonshotai/kimi-k2.5` | Kimi K2.5 mediante MoonshotAI  
  
## Generación de imágenes

OpenRouter también puede respaldar la herramienta `image_generate`. Usa un modelo de imagen de OpenRouter en `agents.defaults.imageGenerationModel`:

json5Copy code
[code]
    {  env: { OPENROUTER_API_KEY: "sk-or-..." },  agents: {    defaults: {      imageGenerationModel: {        primary: "openrouter/google/gemini-3.1-flash-image-preview",        timeoutMs: 180_000,      },    },  },}
[/code]

OpenClaw envía solicitudes de imagen a la API de imágenes de completions de chat de OpenRouter con `modalities: ["image", "text"]`. Los modelos de imagen Gemini reciben sugerencias compatibles de `aspectRatio` y `resolution` mediante `image_config` de OpenRouter. Usa `agents.defaults.imageGenerationModel.timeoutMs` para modelos de imagen de OpenRouter más lentos; el parámetro `timeoutMs` por llamada de la herramienta `image_generate` sigue teniendo prioridad.

## Generación de video

OpenRouter también puede respaldar la herramienta `video_generate` mediante su API asíncrona `/videos`. Usa un modelo de video de OpenRouter en `agents.defaults.videoGenerationModel`:

json5Copy code
[code]
    {  env: { OPENROUTER_API_KEY: "sk-or-..." },  agents: {    defaults: {      videoGenerationModel: {        primary: "openrouter/google/veo-3.1-fast",      },    },  },}
[/code]

OpenClaw envía trabajos de texto a video y de imagen a video a OpenRouter, consulta la `polling_url` devuelta y descarga el video completado desde los `unsigned_urls` de OpenRouter o el endpoint documentado de contenido del trabajo. Las imágenes de referencia se envían como imágenes de primer/último fotograma de forma predeterminada; las imágenes etiquetadas con `reference_image` se envían como referencias de entrada de OpenRouter. El valor predeterminado incluido `google/veo-3.1-fast` anuncia las duraciones actualmente compatibles de 4/6/8 segundos, las resoluciones `720P`/`1080P` y las relaciones de aspecto `16:9`/`9:16`. Video a video no está registrado para OpenRouter porque la API upstream de generación de video actualmente acepta referencias de texto e imagen.

## Texto a voz

OpenRouter también puede usarse como proveedor TTS mediante su endpoint compatible con OpenAI `/audio/speech`.

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "openrouter",      providers: {        openrouter: {          model: "hexgrad/kokoro-82m",          voice: "af_alloy",          responseFormat: "mp3",        },      },    },  },}
[/code]

Si se omite `messages.tts.providers.openrouter.apiKey`, TTS reutiliza `models.providers.openrouter.apiKey` y luego `OPENROUTER_API_KEY`.

## Voz a texto (audio entrante)

OpenRouter puede transcribir adjuntos entrantes de voz/audio mediante la ruta compartida `tools.media.audio` usando su endpoint STT (`/audio/transcriptions`). Esto se aplica a cualquier Plugin de canal que reenvíe voz/audio entrante a la verificación previa de comprensión multimedia.

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "openrouter", model: "openai/whisper-large-v3-turbo" }],      },    },  },}
[/code]

OpenClaw envía las solicitudes STT de OpenRouter como JSON con audio en base64 en `input_audio` (contrato STT de OpenRouter), no como cargas de formulario multipart de OpenAI.

## Autenticación y encabezados

OpenRouter usa internamente un token Bearer con tu clave de API.

En solicitudes reales de OpenRouter (`https://openrouter.ai/api/v1`), OpenClaw también agrega los encabezados documentados de atribución de aplicación de OpenRouter:

Encabezado | Valor  
---|---  
`HTTP-Referer` | `https://openclaw.ai`  
`X-OpenRouter-Title` | `OpenClaw`  
`X-OpenRouter-Categories` | `cli-agent,cloud-agent,programming-app,creative-writing,writing-assistant,general-chat,personal-agent`  
  
## Configuración avanzada

Caché de respuestas

La caché de respuestas de OpenRouter es opcional. Actívala por modelo de OpenRouter con parámetros de modelo:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "openrouter/auto": {          params: {            responseCache: true,            responseCacheTtlSeconds: 300,          },        },      },    },  },}
[/code]

OpenClaw envía `X-OpenRouter-Cache: true` y, cuando está configurado, `X-OpenRouter-Cache-TTL`. `responseCacheClear: true` fuerza una actualización para la solicitud actual y almacena la respuesta de reemplazo. También se aceptan alias en snake_case (`response_cache`, `response_cache_ttl_seconds` y `response_cache_clear`).

Esto es independiente de la caché de prompts del proveedor y de los marcadores `cache_control` de Anthropic de OpenRouter. Solo se aplica en rutas `openrouter.ai` verificadas, no en URLs base de proxy personalizadas.

Marcadores de caché de Anthropic

En rutas verificadas de OpenRouter, las referencias de modelos Anthropic conservan los marcadores `cache_control` específicos de Anthropic de OpenRouter que OpenClaw usa para mejorar la reutilización de la caché de prompts en bloques de prompts de sistema/desarrollador.

Precarga de razonamiento de Anthropic

En rutas verificadas de OpenRouter, las referencias de modelos Anthropic con razonamiento activado eliminan los turnos finales de precarga del assistant antes de que la solicitud llegue a OpenRouter, cumpliendo el requisito de Anthropic de que las conversaciones con razonamiento terminen con un turno de usuario.

Inyección de pensamiento / razonamiento

En rutas no `auto` compatibles, OpenClaw asigna el nivel de pensamiento seleccionado a payloads de razonamiento del proxy de OpenRouter. Las sugerencias de modelos no compatibles y `openrouter/auto` omiten esa inyección de razonamiento. Hunter Alpha también omite el razonamiento de proxy para referencias de modelo configuradas obsoletas porque OpenRouter podría devolver texto de respuesta final en campos de razonamiento para esa ruta retirada.

Reproducción de razonamiento de DeepSeek V4

En rutas verificadas de OpenRouter, `openrouter/deepseek/deepseek-v4-flash` y `openrouter/deepseek/deepseek-v4-pro` completan `reasoning_content` faltante en turnos de assistant reproducidos para que las conversaciones de pensamiento/herramientas mantengan la forma de seguimiento requerida por DeepSeek V4. OpenClaw envía valores `reasoning_effort` compatibles con OpenRouter para estas rutas; `xhigh` es el nivel anunciado más alto, y las sobrescrituras obsoletas de `max` se asignan a `xhigh`.

Modelado de solicitudes solo de OpenAI

OpenRouter sigue pasando por la ruta compatible con OpenAI de estilo proxy, por lo que no se reenvía el modelado de solicitudes nativo solo de OpenAI, como `serviceTier`, `store` de Responses, payloads de compatibilidad de razonamiento de OpenAI y sugerencias de caché de prompts.

Rutas respaldadas por Gemini

Las referencias de OpenRouter respaldadas por Gemini permanecen en la ruta proxy-Gemini: OpenClaw mantiene allí el saneamiento de firmas de pensamiento de Gemini, pero no activa la validación de reproducción nativa de Gemini ni reescrituras de arranque.

Metadatos de enrutamiento del proveedor

Si pasas enrutamiento de proveedor de OpenRouter en los parámetros del modelo, OpenClaw lo reenvía como metadatos de enrutamiento de OpenRouter antes de que se ejecuten los contenedores de streaming compartidos.

## Relacionado

[**Selección de modelos** Elección de proveedores, referencias de modelo y comportamiento de conmutación por error. ](</es/concepts/model-providers>) [**Referencia de configuración** Referencia completa de configuración para agentes, modelos y proveedores. ](</es/gateway/configuration-reference>)

Was this useful?YesNo