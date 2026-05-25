---
title: Fal
source_url: https://docs.openclaw.ai/es/providers/fal
scraped_at: 2026-05-25
---

OpenClaw incluye un proveedor `fal` integrado para generación alojada de imágenes y video.

Propiedad | Valor  
---|---  
Proveedor | `fal`  
Autenticación | `FAL_KEY` (canónica; `FAL_API_KEY` también funciona como alternativa)  
API | Endpoints de modelos fal  
  
## Primeros pasos

* ### Configurar la clave de API

bashCopy code
[code]
    openclaw onboard --auth-choice fal-api-key
[/code]

* ### Configurar un modelo de imagen predeterminado

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "fal/fal-ai/flux/dev",      },    },  },}
[/code]

## Generación de imágenes

El proveedor integrado de generación de imágenes `fal` usa de forma predeterminada `fal/fal-ai/flux/dev`.

Capacidad | Valor  
---|---  
Imágenes máximas | 4 por solicitud  
Modo de edición | Flux: 1 imagen de referencia; GPT Image 2: 10; Nano Banana 2: 14  
Sustituciones de tamaño | Compatibles  
Relación de aspecto | Compatible para generación y edición de GPT Image 2/Nano Banana 2  
Resolución | Compatible  
Formato de salida | `png` o `jpeg`  
  
Usa `outputFormat: "png"` cuando quieras una salida PNG. fal no declara un control explícito de fondo transparente en OpenClaw, por lo que `background: "transparent"` se informa como una sustitución ignorada para los modelos fal.

Para usar fal como proveedor de imágenes predeterminado:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "fal/fal-ai/flux/dev",      },    },  },}
[/code]

## Generación de video

El proveedor integrado de generación de video `fal` usa de forma predeterminada `fal/fal-ai/minimax/video-01-live`.

Capacidad | Valor  
---|---  
Modos | Texto a video, referencia de una sola imagen, referencia a video de Seedance  
Runtime | Flujo de envío/estado/resultado respaldado por cola para trabajos de larga duración  
  
Modelos de video disponibles

**HeyGen video-agent:**

  * `fal/fal-ai/heygen/v2/video-agent`


**Seedance 2.0:**

  * `fal/bytedance/seedance-2.0/fast/text-to-video`
  * `fal/bytedance/seedance-2.0/fast/image-to-video`
  * `fal/bytedance/seedance-2.0/fast/reference-to-video`
  * `fal/bytedance/seedance-2.0/text-to-video`
  * `fal/bytedance/seedance-2.0/image-to-video`
  * `fal/bytedance/seedance-2.0/reference-to-video`

Ejemplo de configuración de Seedance 2.0 json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "fal/bytedance/seedance-2.0/fast/text-to-video",      },    },  },}
[/code]

Ejemplo de configuración de referencia a video de Seedance 2.0 json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "fal/bytedance/seedance-2.0/fast/reference-to-video",      },    },  },}
[/code]

Referencia a video acepta hasta 9 imágenes, 3 videos y 3 referencias de audio mediante los parámetros compartidos `video_generate` `images`, `videos` y `audioRefs`, con un máximo de 12 archivos de referencia en total.

Ejemplo de configuración de HeyGen video-agent json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "fal/fal-ai/heygen/v2/video-agent",      },    },  },}
[/code]

## Relacionado

[**Generación de imágenes** Parámetros compartidos de la herramienta de imágenes y selección de proveedor. ](</es/tools/image-generation>) [**Generación de video** Parámetros compartidos de la herramienta de video y selección de proveedor. ](</es/tools/video-generation>) [**Referencia de configuración** Valores predeterminados del agente, incluida la selección de modelos de imagen y video. ](</es/gateway/config-agents#agent-defaults>)

Was this useful?YesNo