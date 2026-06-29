---
title: PixVerse
source_url: https://docs.openclaw.ai/es/providers/pixverse
scraped_at: 2026-06-29
---

ModelsProviders

OpenClaw proporciona `pixverse` como Plugin externo oficial para la generación de video alojada de PixVerse. El Plugin registra el proveedor `pixverse` contra el contrato `videoGenerationProviders`.

Propiedad | Valor  
---|---  
Id. de proveedor | `pixverse`  
Paquete del Plugin | `@openclaw/pixverse-provider`  
Variable de entorno de auth | `PIXVERSE_API_KEY`  
Marca de onboarding | `--auth-choice pixverse-api-key`  
Marca directa de CLI | `--pixverse-api-key <key>`  
API | PixVerse Platform API v2 (envío de `video_id` más sondeo de resultados)  
Modelo predeterminado | `pixverse/v6`  
Región de API predeterminada | Internacional  
  
## Primeros pasos

* ### Instalar el Plugin

bashCopy code
[code]
    openclaw plugins install clawhub:@openclaw/pixverse-provideropenclaw gateway restart
[/code]

* ### Configurar la clave de API

bashCopy code
[code]
    openclaw onboard --auth-choice pixverse-api-key
[/code]

El asistente pregunta si se debe usar el endpoint internacional (`https://app-api.pixverse.ai/openapi/v2`) o el endpoint de CN (`https://app-api.pixverseai.cn/openapi/v2`) antes de escribir `region` y `baseUrl` en la configuración del proveedor.

* ### Configurar PixVerse como proveedor de video predeterminado

bashCopy code
[code]
    openclaw config set agents.defaults.videoGenerationModel.primary "pixverse/v6"
[/code]

* ### Generar un video

Pide al agente que genere un video. PixVerse se usará automáticamente.

## Modos y modelos compatibles

El proveedor expone modelos de generación de PixVerse mediante la herramienta de video compartida de OpenClaw.

Modo | Modelos | Entrada de referencia  
---|---|---  
Texto a video | `v6` (predeterminado), `c1` | Ninguna  
Imagen a video | `v6` (predeterminado), `c1` | 1 imagen local o remota  
  
Las referencias de imágenes locales se cargan en PixVerse antes de la solicitud de imagen a video. Las URL de imágenes remotas se pasan a través del endpoint de carga de imágenes de PixVerse como `image_url`.

Opción | Valores compatibles  
---|---  
Duración | 1-15 segundos  
Resolución | `360P`, `540P`, `720P`, `1080P`  
Relación de aspecto | `16:9`, `4:3`, `1:1`, `3:4`, `9:16`, `2:3`, `3:2`, `21:9` para texto a video  
Audio generado | `audio: true`  
  
## Opciones del proveedor

El proveedor de video acepta estas claves opcionales específicas del proveedor:

Opción | Tipo | Efecto  
---|---|---  
`seed` | number | Semilla determinista cuando sea compatible  
`negativePrompt` / `negative_prompt` | string | Prompt negativo  
`quality` | string | Calidad de PixVerse como `720p`  
`motionMode` / `motion_mode` | string | Modo de movimiento de imagen a video  
`cameraMovement` / `camera_movement` | string | Preajuste de movimiento de cámara de PixVerse  
`templateId` / `template_id` | number | Id. de plantilla activada de PixVerse  
  
## Configuración

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "pixverse/v6",      },    },  },}
[/code]

## Configuración avanzada

Región de API

OpenClaw usa de forma predeterminada la API internacional de PixVerse. Configura `models.providers.pixverse.region` manualmente cuando tu clave pertenezca a una región específica de la plataforma PixVerse, o usa `openclaw onboard --auth-choice pixverse-api-key` para elegir una en el asistente de configuración:

Valor de región | URL base de la API de PixVerse  
---|---  
`international` | `https://app-api.pixverse.ai/openapi/v2`  
`cn` | `https://app-api.pixverseai.cn/openapi/v2`  
  
json5Copy code
[code]
    {  models: {    providers: {      pixverse: {        region: "cn", // "international" or "cn"        baseUrl: "https://app-api.pixverseai.cn/openapi/v2",        models: [],      },    },  },}
[/code]

URL base personalizada

Configura `models.providers.pixverse.baseUrl` solo al enrutar a través de un proxy compatible de confianza. `baseUrl` tiene prioridad sobre `region`.

json5Copy code
[code]
    {  models: {    providers: {      pixverse: {        baseUrl: "https://app-api.pixverse.ai/openapi/v2",      },    },  },}
[/code]

Sondeo de tareas

PixVerse devuelve un `video_id` desde la solicitud de generación. OpenClaw sondea `/openapi/v2/video/result/{video_id}` hasta que la tarea se realiza correctamente, falla o agota el tiempo de espera.

## Relacionado

[**Generación de video** Parámetros de herramienta compartida, selección de proveedor y comportamiento asíncrono. ](</es/tools/video-generation>) [**Referencia de configuración** Configuración predeterminada del agente, incluido el modelo de generación de video. ](</es/gateway/config-agents#agent-defaults>)

Was this useful?YesNo

Open issue