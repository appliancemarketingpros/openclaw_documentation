---
title: OpenAI
source_url: https://docs.openclaw.ai/es/providers/openai
scraped_at: 2026-05-25
---

OpenAI proporciona API para desarrolladores para modelos GPT, y Codex también está disponible como agente de programación de plan de ChatGPT a través de los clientes Codex de OpenAI. OpenClaw mantiene esas superficies separadas para que la configuración siga siendo predecible.

OpenClaw usa `openai/*` como la ruta canónica de modelos de OpenAI. Los turnos de agente incrustado en modelos de OpenAI se ejecutan de forma predeterminada mediante el runtime nativo del servidor de aplicaciones de Codex; la autenticación directa con clave de API de OpenAI sigue disponible para superficies de OpenAI que no son de agente, como imágenes, embeddings, voz y realtime.

  * **Modelos de agente** \- modelos `openai/*` mediante el runtime de Codex; inicia sesión con autenticación de Codex para usar una suscripción de ChatGPT/Codex, o configura una copia de seguridad con clave de API de OpenAI compatible con Codex cuando quieras usar intencionadamente autenticación con clave de API.
  * **API de OpenAI que no son de agente** \- acceso directo a OpenAI Platform con facturación basada en uso mediante `OPENAI_API_KEY` o incorporación con clave de API de OpenAI.
  * **Configuración heredada** \- las referencias de modelo `openai-codex/*` se reparan con `openclaw doctor --fix` a `openai/*` más el runtime de Codex.


OpenAI admite explícitamente el uso de OAuth de suscripción en herramientas y flujos de trabajo externos como OpenClaw.

Proveedor, modelo, runtime y canal son capas separadas. Si esas etiquetas se están mezclando, lee [runtimes de agente](</es/concepts/agent-runtimes>) antes de cambiar la configuración.

## Elección rápida

Objetivo | Usar | Notas  
---|---|---  
Suscripción ChatGPT/Codex con runtime nativo de Codex | `openai/gpt-5.5` | Configuración predeterminada de agente de OpenAI. Inicia sesión con autenticación de Codex.  
Facturación directa con clave de API para modelos de agente | `openai/gpt-5.5` más un perfil de clave de API compatible con Codex | Usa `auth.order.openai` para colocar la copia de seguridad después de la autenticación de suscripción.  
Facturación directa con clave de API mediante PI explícito | `openai/gpt-5.5` más runtime de proveedor/modelo `pi` | Selecciona un perfil normal de clave de API `openai`.  
Alias de API de ChatGPT Instant más reciente | `openai/chat-latest` | Solo clave de API directa. Alias móvil para experimentos, no el predeterminado.  
Autenticación de suscripción ChatGPT/Codex mediante PI explícito | `openai/gpt-5.5` más runtime de proveedor/modelo `pi` | Selecciona un perfil de autenticación `openai-codex` para la ruta de compatibilidad.  
Generación o edición de imágenes | `openai/gpt-image-2` | Funciona con `OPENAI_API_KEY` u OAuth de OpenAI Codex.  
Imágenes con fondo transparente | `openai/gpt-image-1.5` | Usa `outputFormat=png` o `webp` y `openai.background=transparent`.  
  
## Mapa de nombres

Los nombres son similares, pero no intercambiables:

Nombre que ves | Capa | Significado  
---|---|---  
`openai` | Prefijo de proveedor | Ruta canónica de modelos de OpenAI; los turnos de agente usan el runtime de Codex.  
`openai-codex` | Prefijo de autenticación/perfil heredado | Espacio de nombres anterior de perfiles OAuth/suscripción de OpenAI Codex. Los perfiles existentes y `auth.order.openai-codex` siguen funcionando.  
plugin `codex` | Plugin | Plugin incluido de OpenClaw que proporciona el runtime nativo del servidor de aplicaciones de Codex y controles de chat `/codex`.  
proveedor/modelo `agentRuntime.id: codex` | Runtime de agente | Fuerza el arnés nativo del servidor de aplicaciones de Codex para turnos incrustados coincidentes.  
`/codex ...` | Conjunto de comandos de chat | Vincula/controla hilos del servidor de aplicaciones de Codex desde una conversación.  
`runtime: "acp", agentId: "codex"` | Ruta de sesión ACP | Ruta de respaldo explícita que ejecuta Codex mediante ACP/acpx.  
  
Esto significa que una configuración puede contener intencionadamente referencias de modelo `openai/*` mientras los perfiles de autenticación siguen apuntando a credenciales compatibles con Codex. Prefiere `auth.order.openai` para configuraciones nuevas; los perfiles `openai-codex:*` existentes y `auth.order.openai-codex` siguen siendo compatibles. `openclaw doctor --fix` reescribe las referencias de modelo heredadas `openai-codex/*` a la ruta canónica de modelos de OpenAI.

## Cobertura de características de OpenClaw

Capacidad de OpenAI | Superficie de OpenClaw | Estado  
---|---|---  
Chat / Responses | Proveedor de modelos `openai/<model>` | Sí  
Modelos de suscripción de Codex | `openai/<model>` con OAuth `openai-codex` | Sí  
Referencias de modelo Codex heredadas | `openai-codex/<model>` | Reparadas por doctor a `openai/<model>`  
Arnés de servidor de aplicaciones de Codex | `openai/<model>` con runtime omitido o proveedor/modelo `agentRuntime.id: codex` | Sí  
Búsqueda web del lado del servidor | Herramienta nativa Responses de OpenAI | Sí, cuando la búsqueda web está habilitada y no hay proveedor fijado  
Imágenes | `image_generate` | Sí  
Videos | `video_generate` | Sí  
Texto a voz | `messages.tts.provider: "openai"` / `tts` | Sí  
Voz a texto por lotes | `tools.media.audio` / comprensión multimedia | Sí  
Voz a texto en streaming | Voice Call `streaming.provider: "openai"` | Sí  
Voz en realtime | Voice Call `realtime.provider: "openai"` / Control UI Talk | Sí  
Embeddings | Proveedor de embeddings de memoria | Sí  
  
## Embeddings de memoria

OpenClaw puede usar OpenAI, o un endpoint de embeddings compatible con OpenAI, para la indexación de `memory_search` y los embeddings de consulta:

json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        provider: "openai",        model: "text-embedding-3-small",      },    },  },}
[/code]

Para endpoints compatibles con OpenAI que requieren etiquetas de embedding asimétricas, define `queryInputType` y `documentInputType` en `memorySearch`. OpenClaw los reenvía como campos de solicitud `input_type` específicos del proveedor: los embeddings de consulta usan `queryInputType`; los fragmentos de memoria indexados y la indexación por lotes usan `documentInputType`. Consulta la [referencia de configuración de memoria](</es/reference/memory-config#provider-specific-config>) para ver el ejemplo completo.

## Primeros pasos

Elige tu método de autenticación preferido y sigue los pasos de configuración.

### Clave de API (OpenAI Platform)

**Ideal para:** acceso directo a API y facturación basada en uso.

* ### Obtén tu clave de API

Crea o copia una clave de API desde el [panel de OpenAI Platform](<https://platform.openai.com/api-keys>).

* ### Ejecuta la incorporación

bashCopy code
[code]
    openclaw onboard --auth-choice openai-api-key
[/code]

O pasa la clave directamente:

bashCopy code
[code]
    openclaw onboard --openai-api-key "$OPENAI_API_KEY"
[/code]

* ### Verifica que el modelo esté disponible

bashCopy code
[code]
    openclaw models list --provider openai
[/code]

### Resumen de rutas

Referencia de modelo | Configuración de runtime | Ruta | Autenticación  
---|---|---|---  
`openai/gpt-5.5` | omitida / proveedor/modelo `agentRuntime.id: "codex"` | Arnés de servidor de aplicaciones de Codex | Perfil de OpenAI compatible con Codex  
`openai/gpt-5.4-mini` | omitida / proveedor/modelo `agentRuntime.id: "codex"` | Arnés de servidor de aplicaciones de Codex | Perfil de OpenAI compatible con Codex  
`openai/gpt-5.5` | proveedor/modelo `agentRuntime.id: "pi"` | Runtime incrustado PI | Perfil `openai` o perfil `openai-codex` seleccionado  
  
### Ejemplo de configuración

json5Copy code
[code]
    {  env: { OPENAI_API_KEY: "sk-..." },  agents: { defaults: { model: { primary: "openai/gpt-5.5" } } },}
[/code]

Para probar el modelo Instant actual de ChatGPT desde la API de OpenAI, establece el modelo en `openai/chat-latest`:

json5Copy code
[code]
    {  env: { OPENAI_API_KEY: "sk-..." },  agents: { defaults: { model: { primary: "openai/chat-latest" } } },}
[/code]

`chat-latest` es un alias móvil. OpenAI lo documenta como el modelo Instant más reciente usado en ChatGPT y recomienda `gpt-5.5` para uso de API en producción, así que mantén `openai/gpt-5.5` como valor predeterminado estable salvo que quieras explícitamente ese comportamiento de alias. Actualmente, el alias solo acepta verbosidad de texto `medium`, por lo que OpenClaw normaliza las anulaciones incompatibles de verbosidad de texto de OpenAI para este modelo.

### Codex subscription

**Ideal para:** usar tu suscripción de ChatGPT/Codex con ejecución nativa del servidor de aplicación de Codex en lugar de una clave de API separada. La nube de Codex requiere iniciar sesión en ChatGPT.

* ### Run Codex OAuth

bashCopy code
[code]
    openclaw onboard --auth-choice openai-codex
[/code]

O ejecuta OAuth directamente:

bashCopy code
[code]
    openclaw models auth login --provider openai-codex
[/code]

Para configuraciones sin interfaz o incompatibles con callbacks, agrega `--device-code` para iniciar sesión con un flujo de código de dispositivo de ChatGPT en lugar del callback del navegador localhost:

bashCopy code
[code]
    openclaw models auth login --provider openai-codex --device-code
[/code]

* ### Use the canonical OpenAI model route

bashCopy code
[code]
    openclaw config set agents.defaults.model.primary openai/gpt-5.5
[/code]

No se requiere configuración de runtime para la ruta predeterminada. Los turnos de agente de OpenAI seleccionan automáticamente el runtime nativo del servidor de aplicación de Codex, y OpenClaw instala o repara el Plugin de Codex incluido cuando se elige esta ruta.

* ### Verify Codex auth is available

bashCopy code
[code]
    openclaw models list --provider openai-codex
[/code]

Después de que el Gateway esté en ejecución, envía `/codex status` o `/codex models` en el chat para verificar el runtime nativo del servidor de aplicación.

### Resumen de rutas

Ref. de modelo | Configuración de runtime | Ruta | Autenticación  
---|---|---|---  
`openai/gpt-5.5` | omitida / proveedor/modelo `agentRuntime.id: "codex"` | Arnés nativo del servidor de aplicación de Codex | Inicio de sesión de Codex o perfil de autenticación `openai` ordenado  
`openai/gpt-5.5` | proveedor/modelo `agentRuntime.id: "pi"` | Runtime integrado de PI con transporte interno de autenticación de Codex | Perfil `openai-codex` seleccionado  
`openai-codex/gpt-5.5` | reparada por doctor | Ruta heredada reescrita a `openai/gpt-5.5` | Perfil `openai-codex` existente  
  
### Ejemplo de configuración

json5Copy code
[code]
    {  plugins: { entries: { codex: { enabled: true } } },  agents: {    defaults: {      model: { primary: "openai/gpt-5.5" },    },  },}
[/code]

Con un respaldo de clave de API, conserva el modelo en `openai/gpt-5.5` y pon el orden de autenticación en `openai`. OpenClaw probará primero la suscripción y luego la clave de API, mientras permanece en el arnés de Codex:

json5Copy code
[code]
    {  plugins: { entries: { codex: { enabled: true } } },  agents: {    defaults: {      model: { primary: "openai/gpt-5.5" },    },  },  auth: {    order: {      openai: [        "openai-codex:user@example.com",        "openai:api-key-backup",      ],    },  },}
[/code]

### Comprobar y recuperar el enrutamiento OAuth de Codex

Usa estos comandos para ver qué modelo, runtime y ruta de autenticación está usando tu agente predeterminado:

bashCopy code
[code]
    openclaw models statusopenclaw models auth list --provider openai-codexopenclaw config get agents.defaults.model --jsonopenclaw config get models.providers.openai.agentRuntime --json
[/code]

Para un agente específico, agrega `--agent <id>`:

bashCopy code
[code]
    openclaw models status --agent <id>openclaw models auth list --agent <id> --provider openai-codex
[/code]

Si una configuración antigua aún tiene `openai-codex/gpt-*` o un pin de sesión PI de OpenAI obsoleto sin configuración de runtime explícita, repárala:

bashCopy code
[code]
    openclaw doctor --fixopenclaw config validate
[/code]

Si `models auth list --provider openai-codex` no muestra ningún perfil utilizable, inicia sesión de nuevo:

bashCopy code
[code]
    openclaw models auth login --provider openai-codexopenclaw models status --probe --probe-provider openai-codex
[/code]

`openai/*` es la ruta de modelo para turnos de agente de OpenAI a través de Codex. El id de proveedor de autenticación/perfil `openai-codex` sigue aceptándose para perfiles existentes y listados de CLI.

### Indicador de estado

El chat `/status` muestra qué runtime de modelo está activo para la sesión actual. El arnés del servidor de aplicación de Codex incluido aparece como `Runtime: OpenAI Codex` para turnos de modelo de agente de OpenAI. Los pines de sesión PI obsoletos se reparan a Codex salvo que la configuración fije PI explícitamente.

### Advertencia de doctor

Si las rutas `openai-codex/*` o los pines PI de OpenAI obsoletos permanecen en la configuración o el estado de sesión, `openclaw doctor --fix` los reescribe a `openai/*` con el runtime de Codex salvo que PI esté configurado explícitamente.

### Límite de ventana de contexto

OpenClaw trata los metadatos de modelo y el límite de contexto del runtime como valores separados.

Para `openai/gpt-5.5` a través del catálogo OAuth de Codex:

  * `contextWindow` nativa: `1000000`
  * Límite predeterminado de runtime `contextTokens`: `272000`


En la práctica, el límite predeterminado más pequeño tiene mejores características de latencia y calidad. Sobrescríbelo con `contextTokens`:

json5Copy code
[code]
    {  models: {    providers: {      "openai-codex": {        models: [{ id: "gpt-5.5", contextTokens: 160000 }],      },    },  },}
[/code]

### Recuperación del catálogo

OpenClaw usa metadatos del catálogo upstream de Codex para `gpt-5.5` cuando están presentes. Si el descubrimiento en vivo de Codex omite la fila `gpt-5.5` mientras la cuenta está autenticada, OpenClaw sintetiza esa fila de modelo OAuth para que las ejecuciones de cron, subagente y modelo predeterminado configurado no fallen con `Unknown model`.

## Autenticación nativa del servidor de aplicación de Codex

El arnés nativo del servidor de aplicación de Codex usa refs. de modelo `openai/*` más configuración de runtime omitida o proveedor/modelo `agentRuntime.id: "codex"`, pero su autenticación sigue estando basada en cuenta. OpenClaw selecciona la autenticación en este orden:

  1. Perfiles de autenticación de OpenAI ordenados para el agente, preferiblemente en `auth.order.openai`. Los perfiles existentes `openai-codex:*` y `auth.order.openai-codex` siguen siendo válidos para instalaciones antiguas.
  2. La cuenta existente del servidor de aplicación, como un inicio de sesión local de ChatGPT en Codex CLI.
  3. Solo para lanzamientos locales del servidor de aplicación por stdio, `CODEX_API_KEY` y luego `OPENAI_API_KEY`, cuando el servidor de aplicación informa que no hay cuenta y todavía requiere autenticación de OpenAI.


Eso significa que un inicio de sesión local con suscripción de ChatGPT/Codex no se reemplaza solo porque el proceso del Gateway también tenga `OPENAI_API_KEY` para modelos directos de OpenAI o embeddings. El respaldo de clave de API por env solo es la ruta local stdio sin cuenta; no se envía a conexiones WebSocket del servidor de aplicación. Cuando se selecciona un perfil de Codex de tipo suscripción, OpenClaw también mantiene `CODEX_API_KEY` y `OPENAI_API_KEY` fuera del proceso hijo stdio del servidor de aplicación generado y envía las credenciales seleccionadas mediante el RPC de inicio de sesión del servidor de aplicación. Cuando ese perfil de suscripción está bloqueado por un límite de uso de Codex, OpenClaw puede rotar al siguiente perfil de clave de API `openai:*` ordenado sin cambiar el modelo seleccionado ni salir del arnés de Codex. Una vez que pasa la hora de restablecimiento de la suscripción, el perfil de suscripción vuelve a ser elegible.

## Generación de imágenes

El Plugin `openai` incluido registra la generación de imágenes mediante la herramienta `image_generate`. Admite generación de imágenes tanto con clave de API de OpenAI como con OAuth de Codex mediante la misma ref. de modelo `openai/gpt-image-2`.

Capacidad | Clave de API de OpenAI | OAuth de Codex  
---|---|---  
Ref. de modelo | `openai/gpt-image-2` | `openai/gpt-image-2`  
Autenticación | `OPENAI_API_KEY` | Inicio de sesión OAuth de OpenAI Codex  
Transporte | API de imágenes de OpenAI | Backend de Responses de Codex  
Máx. imágenes por solicitud | 4 | 4  
Modo de edición | Habilitado (hasta 5 imágenes de referencia) | Habilitado (hasta 5 imágenes de referencia)  
Sobrescrituras de tamaño | Compatibles, incluidos tamaños 2K/4K | Compatibles, incluidos tamaños 2K/4K  
Relación de aspecto / resolución | No se reenvía a la API de imágenes de OpenAI | Se asigna a un tamaño compatible cuando es seguro  
json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: { primary: "openai/gpt-image-2" },    },  },}
[/code]

`gpt-image-2` es el valor predeterminado tanto para la generación de texto a imagen de OpenAI como para la edición de imágenes. `gpt-image-1.5`, `gpt-image-1` y `gpt-image-1-mini` siguen siendo utilizables como sobrescrituras explícitas de modelo. Usa `openai/gpt-image-1.5` para salida PNG/WebP con fondo transparente; la API actual de `gpt-image-2` rechaza `background: "transparent"`.

Para una solicitud con fondo transparente, los agentes deben llamar a `image_generate` con `model: "openai/gpt-image-1.5"`, `outputFormat: "png"` o `"webp"`, y `background: "transparent"`; la opción de proveedor antigua `openai.background` todavía se acepta. OpenClaw también protege las rutas públicas de OpenAI y OAuth de OpenAI Codex reescribiendo las solicitudes transparentes predeterminadas `openai/gpt-image-2` a `gpt-image-1.5`; Azure y los endpoints personalizados compatibles con OpenAI conservan sus nombres de implementación/modelo configurados.

La misma configuración se expone para ejecuciones de CLI sin interfaz:

bashCopy code
[code]
    openclaw infer image generate \  --model openai/gpt-image-1.5 \  --output-format png \  --background transparent \  --prompt "A simple red circle sticker on a transparent background" \  --json
[/code]

Usa las mismas flags `--output-format` y `--background` con `openclaw infer image edit` al partir de un archivo de entrada. `--openai-background` sigue disponible como alias específico de OpenAI.

Para instalaciones con OAuth de Codex, conserva la misma ref. `openai/gpt-image-2`. Cuando se configura un perfil OAuth `openai-codex`, OpenClaw resuelve ese token de acceso OAuth almacenado y envía las solicitudes de imagen a través del backend de Responses de Codex. No prueba primero `OPENAI_API_KEY` ni recurre silenciosamente a una clave de API para esa solicitud. Configura `models.providers.openai` explícitamente con una clave de API, URL base personalizada o endpoint de Azure cuando quieras usar la ruta directa de la API de imágenes de OpenAI en su lugar. Si ese endpoint de imagen personalizado está en una dirección LAN/privada de confianza, configura también `browser.ssrfPolicy.dangerouslyAllowPrivateNetwork: true`; OpenClaw mantiene bloqueados los endpoints de imagen privados/internos compatibles con OpenAI salvo que esta adhesión explícita esté presente.

Generar:

CodeCopy code
[code]
    /tool image_generate model=openai/gpt-image-2 prompt="A polished launch poster for OpenClaw on macOS" size=3840x2160 count=1
[/code]

Generar un PNG transparente:

CodeCopy code
[code]
    /tool image_generate model=openai/gpt-image-1.5 prompt="A simple red circle sticker on a transparent background" outputFormat=png background=transparent
[/code]

Editar:

CodeCopy code
[code]
    /tool image_generate model=openai/gpt-image-2 prompt="Preserve the object shape, change the material to translucent glass" image=/path/to/reference.png size=1024x1536
[/code]

## Generación de video

El plugin `openai` incluido registra la generación de video mediante la herramienta `video_generate`.

Capacidad | Valor  
---|---  
Modelo predeterminado | `openai/sora-2`  
Modos | Texto a video, imagen a video, edición de un solo video  
Entradas de referencia | 1 imagen o 1 video  
Sobrescrituras de tamaño | Admitidas  
Otras sobrescrituras | `aspectRatio`, `resolution`, `audio`, `watermark` se ignoran con una advertencia de la herramienta  
json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: { primary: "openai/sora-2" },    },  },}
[/code]

## Contribución de prompt de GPT-5

OpenClaw añade una contribución compartida de prompt de GPT-5 para ejecuciones de la familia GPT-5 en distintos proveedores. Se aplica por id de modelo, por lo que `openai/gpt-5.5`, referencias heredadas previas a la reparación como `openai-codex/gpt-5.5`, `openrouter/openai/gpt-5.5`, `opencode/gpt-5.5` y otras referencias compatibles con GPT-5 reciben la misma superposición. Los modelos GPT-4.x anteriores no.

El arnés nativo de Codex incluido usa el mismo comportamiento de GPT-5 y la misma superposición de Heartbeat mediante las instrucciones de desarrollador del servidor de aplicaciones de Codex, por lo que las sesiones `openai/gpt-5.x` enrutadas a través de Codex conservan la misma guía de seguimiento y Heartbeat proactivo, aunque Codex controla el resto del prompt del arnés.

La contribución de GPT-5 añade un contrato de comportamiento etiquetado para la persistencia de la persona, la seguridad de ejecución, la disciplina de herramientas, la forma de salida, las comprobaciones de finalización y la verificación. El comportamiento de respuestas específico del canal y de mensajes silenciosos permanece en el prompt compartido del sistema de OpenClaw y en la política de entrega saliente. La guía de GPT-5 siempre está habilitada para los modelos coincidentes. La capa de estilo de interacción amistoso es independiente y configurable.

Valor | Efecto  
---|---  
`"friendly"` (predeterminado) | Habilita la capa de estilo de interacción amistoso  
`"on"` | Alias de `"friendly"`  
`"off"` | Deshabilita solo la capa de estilo amistoso  
  
### Configuración

json5Copy code
[code]
    {  agents: {    defaults: {      promptOverlays: {        gpt5: { personality: "friendly" },      },    },  },}
[/code]

### CLI

bashCopy code
[code]
    openclaw config set agents.defaults.promptOverlays.gpt5.personality off
[/code]

## Voz y habla

Síntesis de voz (TTS)

El plugin `openai` incluido registra la síntesis de voz para la superficie `messages.tts`.

Ajuste | Ruta de configuración | Predeterminado  
---|---|---  
Modelo | `messages.tts.providers.openai.model` | `gpt-4o-mini-tts`  
Voz | `messages.tts.providers.openai.voice` | `coral`  
Velocidad | `messages.tts.providers.openai.speed` | (sin definir)  
Instrucciones | `messages.tts.providers.openai.instructions` | (sin definir, solo `gpt-4o-mini-tts`)  
Formato | `messages.tts.providers.openai.responseFormat` | `opus` para notas de voz, `mp3` para archivos  
Clave de API | `messages.tts.providers.openai.apiKey` | Recurre a `OPENAI_API_KEY`  
URL base | `messages.tts.providers.openai.baseUrl` | `https://api.openai.com/v1`  
Cuerpo adicional | `messages.tts.providers.openai.extraBody` / `extra_body` | (sin definir)  
  
Modelos disponibles: `gpt-4o-mini-tts`, `tts-1`, `tts-1-hd`. Voces disponibles: `alloy`, `ash`, `ballad`, `cedar`, `coral`, `echo`, `fable`, `juniper`, `marin`, `onyx`, `nova`, `sage`, `shimmer`, `verse`.

`extraBody` se fusiona en el JSON de la solicitud `/audio/speech` después de los campos generados por OpenClaw, así que úsalo para endpoints compatibles con OpenAI que requieren claves adicionales como `lang`. Las claves de prototipo se ignoran.

json5Copy code
[code]
    {  messages: {    tts: {      providers: {        openai: { model: "gpt-4o-mini-tts", voice: "coral" },      },    },  },}
[/code]

Voz a texto

El plugin `openai` incluido registra la voz a texto por lotes mediante la superficie de transcripción de comprensión de medios de OpenClaw.

  * Modelo predeterminado: `gpt-4o-transcribe`
  * Endpoint: REST de OpenAI `/v1/audio/transcriptions`
  * Ruta de entrada: carga de archivo de audio multipart
  * Admitido por OpenClaw siempre que la transcripción de audio entrante use `tools.media.audio`, incluidos segmentos de canales de voz de Discord y archivos adjuntos de audio de canal


Para forzar OpenAI para la transcripción de audio entrante:

json5Copy code
[code]
    {  tools: {    media: {      audio: {        models: [          {            type: "provider",            provider: "openai",            model: "gpt-4o-transcribe",          },        ],      },    },  },}
[/code]

Las sugerencias de idioma y prompt se reenvían a OpenAI cuando las proporciona la configuración compartida de medios de audio o la solicitud de transcripción por llamada.

Transcripción en tiempo real

El plugin `openai` incluido registra la transcripción en tiempo real para el plugin Voice Call.

Ajuste | Ruta de configuración | Valor predeterminado  
---|---|---  
Modelo | `plugins.entries.voice-call.config.streaming.providers.openai.model` | `gpt-4o-transcribe`  
Idioma | `...openai.language` | (sin establecer)  
Prompt | `...openai.prompt` | (sin establecer)  
Duración del silencio | `...openai.silenceDurationMs` | `800`  
Umbral de VAD | `...openai.vadThreshold` | `0.5`  
Autenticación | `...openai.apiKey`, `OPENAI_API_KEY`, u OAuth de `openai-codex` | Las claves de API se conectan directamente; OAuth emite un secreto de cliente de transcripción Realtime  
Voz en tiempo real

El plugin `openai` incluido registra voz en tiempo real para el plugin Voice Call.

Ajuste | Ruta de configuración | Valor predeterminado  
---|---|---  
Modelo | `plugins.entries.voice-call.config.realtime.providers.openai.model` | `gpt-realtime-2`  
Voz | `...openai.voice` | `alloy`  
Temperatura (puente de despliegue de Azure) | `...openai.temperature` | `0.8`  
Umbral de VAD | `...openai.vadThreshold` | `0.5`  
Duración del silencio | `...openai.silenceDurationMs` | `500`  
Relleno de prefijo | `...openai.prefixPaddingMs` | `300`  
Esfuerzo de razonamiento | `...openai.reasoningEffort` | (sin establecer)  
Autenticación | `...openai.apiKey`, `OPENAI_API_KEY`, u OAuth de `openai-codex` | Browser Talk y los puentes de backend no Azure pueden usar OAuth de Codex  
  
Voces Realtime integradas disponibles para `gpt-realtime-2`: `alloy`, `ash`, `ballad`, `coral`, `echo`, `sage`, `shimmer`, `verse`, `marin`, `cedar`. OpenAI recomienda `marin` y `cedar` para obtener la mejor calidad Realtime. Este es un conjunto independiente de las voces de texto a voz anteriores; no asumas que una voz TTS como `fable`, `nova` u `onyx` es válida para sesiones Realtime.

## Endpoints de Azure OpenAI

El proveedor `openai` incluido puede apuntar a un recurso de Azure OpenAI para la generación de imágenes sobrescribiendo la URL base. En la ruta de generación de imágenes, OpenClaw detecta nombres de host de Azure en `models.providers.openai.baseUrl` y cambia a la forma de solicitud de Azure automáticamente.

Usa Azure OpenAI cuando:

  * Ya tengas una suscripción, cuota o acuerdo empresarial de Azure OpenAI
  * Necesites residencia regional de datos o controles de cumplimiento que Azure proporciona
  * Quieras mantener el tráfico dentro de una tenencia de Azure existente


### Configuración

Para la generación de imágenes de Azure mediante el proveedor `openai` incluido, apunta `models.providers.openai.baseUrl` a tu recurso de Azure y establece `apiKey` en la clave de Azure OpenAI (no una clave de OpenAI Platform):

json5Copy code
[code]
    {  models: {    providers: {      openai: {        baseUrl: "https://<your-resource>.openai.azure.com",        apiKey: "<azure-openai-api-key>",      },    },  },}
[/code]

OpenClaw reconoce estos sufijos de host de Azure para la ruta de generación de imágenes de Azure:

  * `*.openai.azure.com`
  * `*.services.ai.azure.com`
  * `*.cognitiveservices.azure.com`


Para solicitudes de generación de imágenes en un host de Azure reconocido, OpenClaw:

  * Envía el encabezado `api-key` en lugar de `Authorization: Bearer`
  * Usa rutas con ámbito de despliegue (`/openai/deployments/{deployment}/...`)
  * Añade `?api-version=...` a cada solicitud
  * Usa un tiempo de espera de solicitud predeterminado de 600 s para llamadas de generación de imágenes de Azure. Los valores `timeoutMs` por llamada siguen sobrescribiendo este valor predeterminado.


Otras URL base (OpenAI público, proxies compatibles con OpenAI) conservan la forma de solicitud estándar de imágenes de OpenAI.

### Versión de la API

Configura `AZURE_OPENAI_API_VERSION` para fijar una versión específica de Azure en vista previa o GA para la ruta de generación de imágenes de Azure:

bashCopy code
[code]
    export AZURE_OPENAI_API_VERSION="2024-12-01-preview"
[/code]

El valor predeterminado es `2024-12-01-preview` cuando la variable no está definida.

### Los nombres de modelo son nombres de despliegue

Azure OpenAI vincula los modelos a despliegues. Para las solicitudes de generación de imágenes de Azure enrutadas a través del proveedor `openai` incluido, el campo `model` en OpenClaw debe ser el **nombre de despliegue de Azure** que configuraste en el portal de Azure, no el id público del modelo de OpenAI.

Si creas un despliegue llamado `gpt-image-2-prod` que sirve `gpt-image-2`:

CodeCopy code
[code]
    /tool image_generate model=openai/gpt-image-2-prod prompt="A clean poster" size=1024x1024 count=1
[/code]

La misma regla de nombre de despliegue se aplica a las llamadas de generación de imágenes enrutadas a través del proveedor `openai` incluido.

### Disponibilidad regional

La generación de imágenes de Azure actualmente solo está disponible en un subconjunto de regiones (por ejemplo `eastus2`, `swedencentral`, `polandcentral`, `westus3`, `uaenorth`). Consulta la lista actual de regiones de Microsoft antes de crear un despliegue y confirma que el modelo específico se ofrezca en tu región.

### Diferencias de parámetros

Azure OpenAI y OpenAI público no siempre aceptan los mismos parámetros de imagen. Azure puede rechazar opciones que OpenAI público permite (por ejemplo, ciertos valores de `background` en `gpt-image-2`) o exponerlas solo en versiones de modelo específicas. Estas diferencias provienen de Azure y del modelo subyacente, no de OpenClaw. Si una solicitud de Azure falla con un error de validación, consulta el conjunto de parámetros admitido por tu despliegue y versión de API específicos en el portal de Azure.

## Configuración avanzada

Transport (WebSocket vs SSE)

OpenClaw usa WebSocket primero con reserva SSE (`"auto"`) para `openai/*`.

En modo `"auto"`, OpenClaw:

  * Reintenta una falla temprana de WebSocket antes de recurrir a SSE
  * Después de una falla, marca WebSocket como degradado durante ~60 segundos y usa SSE durante el enfriamiento
  * Adjunta encabezados estables de identidad de sesión y turno para reintentos y reconexiones
  * Normaliza los contadores de uso (`input_tokens` / `prompt_tokens`) entre variantes de transporte

Valor | Comportamiento  
---|---  
`"auto"` (predeterminado) | WebSocket primero, reserva SSE  
`"sse"` | Forzar solo SSE  
`"websocket"` | Forzar solo WebSocket  
json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "openai/gpt-5.5": {          params: { transport: "auto" },        },      },    },  },}
[/code]

Documentación relacionada de OpenAI:

  * [API en tiempo real con WebSocket](<https://platform.openai.com/docs/guides/realtime-websocket>)
  * [Respuestas de API en streaming (SSE)](<https://platform.openai.com/docs/guides/streaming-responses>)

Fast mode

OpenClaw expone un interruptor compartido de modo rápido para `openai/*`:

  * **Chat/IU:** `/fast status|on|off`
  * **Configuración:** `agents.defaults.models["<provider>/<model>"].params.fastMode`


Cuando está habilitado, OpenClaw asigna el modo rápido al procesamiento prioritario de OpenAI (`service_tier = "priority"`). Los valores existentes de `service_tier` se conservan, y el modo rápido no reescribe `reasoning` ni `text.verbosity`.

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "openai/gpt-5.5": { params: { fastMode: true } },      },    },  },}
[/code]

Procesamiento prioritario (service_tier)

La API de OpenAI expone el procesamiento prioritario mediante `service_tier`. Configúralo por modelo en OpenClaw:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "openai/gpt-5.5": { params: { serviceTier: "priority" } },      },    },  },}
[/code]

Valores admitidos: `auto`, `default`, `flex`, `priority`.

Compaction del lado del servidor (Responses API)

Para modelos directos de OpenAI Responses (`openai/*` en `api.openai.com`), el envoltorio de flujo del arnés Pi del plugin de OpenAI habilita automáticamente la Compaction del lado del servidor:

  * Fuerza `store: true` (a menos que la compatibilidad del modelo establezca `supportsStore: false`)
  * Inyecta `context_management: [{ type: "compaction", compact_threshold: ... }]`
  * `compact_threshold` predeterminado: 70 % de `contextWindow` (o `80000` cuando no está disponible)


Esto se aplica a la ruta del arnés Pi integrado y a los hooks del proveedor OpenAI usados por ejecuciones embebidas. El arnés nativo del servidor de aplicaciones Codex gestiona su propio contexto mediante Codex y se configura mediante la ruta de agente predeterminada de OpenAI o la política de tiempo de ejecución del proveedor/modelo.

### Habilitar explícitamente

Útil para endpoints compatibles como Azure OpenAI Responses:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "azure-openai-responses/gpt-5.5": {          params: { responsesServerCompaction: true },        },      },    },  },}
[/code]

### Umbral personalizado

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "openai/gpt-5.5": {          params: {            responsesServerCompaction: true,            responsesCompactThreshold: 120000,          },        },      },    },  },}
[/code]

### Deshabilitar

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "openai/gpt-5.5": {          params: { responsesServerCompaction: false },        },      },    },  },}
[/code]

Modo GPT agentivo estricto

Para ejecuciones de la familia GPT-5 en `openai/*`, OpenClaw puede usar un contrato de ejecución embebida más estricto:

json5Copy code
[code]
    {  agents: {    defaults: {      embeddedPi: { executionContract: "strict-agentic" },    },  },}
[/code]

Con `strict-agentic`, OpenClaw:

  * Ya no trata un turno solo de plan como progreso correcto cuando hay una acción de herramienta disponible
  * Reintenta el turno con una orientación para actuar ahora
  * Habilita automáticamente `update_plan` para trabajo sustancial
  * Muestra un estado bloqueado explícito si el modelo sigue planificando sin actuar

Rutas nativas frente a rutas compatibles con OpenAI

OpenClaw trata los endpoints directos de OpenAI, Codex y Azure OpenAI de forma diferente a los proxies genéricos `/v1` compatibles con OpenAI:

**Rutas nativas** (`openai/*`, Azure OpenAI):

  * Conservan `reasoning: { effort: "none" }` solo para modelos que admiten el esfuerzo `none` de OpenAI
  * Omiten el razonamiento deshabilitado para modelos o proxies que rechazan `reasoning.effort: "none"`
  * Establecen los esquemas de herramientas en modo estricto de forma predeterminada
  * Adjuntan encabezados de atribución ocultos solo en hosts nativos verificados
  * Conservan el modelado de solicitudes exclusivo de OpenAI (`service_tier`, `store`, compatibilidad de razonamiento, indicaciones de caché de prompts)


**Rutas proxy/compatibles:**

  * Usan un comportamiento de compatibilidad más flexible
  * Eliminan `store` de Completions de las cargas útiles `openai-completions` no nativas
  * Aceptan JSON de paso directo avanzado `params.extra_body`/`params.extraBody` para proxies de Completions compatibles con OpenAI
  * Aceptan `params.chat_template_kwargs` para proxies de Completions compatibles con OpenAI, como vLLM
  * No fuerzan esquemas de herramientas estrictos ni encabezados exclusivos de rutas nativas


Azure OpenAI usa transporte nativo y comportamiento de compatibilidad, pero no recibe los encabezados de atribución ocultos.

## Relacionado

[**Selección de modelos** Elección de proveedores, referencias de modelo y comportamiento de conmutación por error. ](</es/concepts/model-providers>) [**Generación de imágenes** Parámetros compartidos de la herramienta de imagen y selección de proveedor. ](</es/tools/image-generation>) [**Generación de vídeo** Parámetros compartidos de la herramienta de vídeo y selección de proveedor. ](</es/tools/video-generation>) [**OAuth y autenticación** Detalles de autenticación y reglas de reutilización de credenciales. ](</es/gateway/authentication>)

Was this useful?YesNo