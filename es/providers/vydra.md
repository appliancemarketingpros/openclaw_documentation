---
title: Vydra
source_url: https://docs.openclaw.ai/es/providers/vydra
scraped_at: 2026-05-25
---

El Plugin Vydra incluido añade:

  * Generación de imágenes mediante `vydra/grok-imagine`
  * Generación de video mediante `vydra/veo3` y `vydra/kling`
  * Síntesis de voz mediante la ruta TTS de Vydra respaldada por ElevenLabs


OpenClaw usa la misma `VYDRA_API_KEY` para las tres capacidades.

Propiedad | Valor  
---|---  
Id de proveedor | `vydra`  
Plugin | incluido, `enabledByDefault: true`  
Variable de entorno de autenticación | `VYDRA_API_KEY`  
Indicador de incorporación | `--auth-choice vydra-api-key`  
Indicador directo de CLI | `--vydra-api-key <key>`  
Contratos | `imageGenerationProviders`, `videoGenerationProviders`, `speechProviders`  
URL base | `https://www.vydra.ai/api/v1` (usa el host `www`)  
  
## Configuración

* ### Ejecutar la incorporación interactiva

bashCopy code
[code]
    openclaw onboard --auth-choice vydra-api-key
[/code]

O define la variable de entorno directamente:

bashCopy code
[code]
    export VYDRA_API_KEY="vydra_live_..."
[/code]

* ### Elegir una capacidad predeterminada

Elige una o más de las capacidades siguientes (imagen, video o voz) y aplica la configuración correspondiente.

## Capacidades

Generación de imágenes

Modelo de imagen predeterminado:

  * `vydra/grok-imagine`


Defínelo como el proveedor de imágenes predeterminado:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "vydra/grok-imagine",      },    },  },}
[/code]

El soporte incluido actual solo es de texto a imagen. Las rutas de edición alojadas de Vydra esperan URLs de imágenes remotas, y OpenClaw todavía no añade un puente de carga específico de Vydra en el Plugin incluido.

Generación de video

Modelos de video registrados:

  * `vydra/veo3` para texto a video
  * `vydra/kling` para imagen a video


Define Vydra como el proveedor de video predeterminado:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "vydra/veo3",      },    },  },}
[/code]

Notas:

  * `vydra/veo3` se incluye solo como texto a video.
  * `vydra/kling` actualmente requiere una referencia de URL de imagen remota. Las cargas de archivos locales se rechazan desde el inicio.
  * La ruta HTTP `kling` actual de Vydra ha sido inconsistente sobre si requiere `image_url` o `video_url`; el proveedor incluido asigna la misma URL de imagen remota a ambos campos.
  * El Plugin incluido se mantiene conservador y no reenvía controles de estilo no documentados como relación de aspecto, resolución, marca de agua o audio generado.

Pruebas en vivo de video

Cobertura en vivo específica del proveedor:

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 \OPENCLAW_LIVE_VYDRA_VIDEO=1 \pnpm test:live -- extensions/vydra/vydra.live.test.ts
[/code]

El archivo en vivo de Vydra incluido ahora cubre:

  * `vydra/veo3` de texto a video
  * `vydra/kling` de imagen a video usando una URL de imagen remota


Sustituye el fixture de imagen remota cuando sea necesario:

bashCopy code
[code]
    export OPENCLAW_LIVE_VYDRA_KLING_IMAGE_URL="https://example.com/reference.png"
[/code]

Síntesis de voz

Define Vydra como proveedor de voz:

json5Copy code
[code]
    {  messages: {    tts: {      provider: "vydra",      providers: {        vydra: {          apiKey: "${VYDRA_API_KEY}",          voiceId: "21m00Tcm4TlvDq8ikWAM",        },      },    },  },}
[/code]

Valores predeterminados:

  * Modelo: `elevenlabs/tts`
  * Id de voz: `21m00Tcm4TlvDq8ikWAM`


El Plugin incluido actualmente expone una voz predeterminada conocida y fiable, y devuelve archivos de audio MP3.

## Relacionado

[**Directorio de proveedores** Explora todos los proveedores disponibles. ](</es/providers>) [**Generación de imágenes** Parámetros compartidos de la herramienta de imagen y selección de proveedor. ](</es/tools/image-generation>) [**Generación de video** Parámetros compartidos de la herramienta de video y selección de proveedor. ](</es/tools/video-generation>) [**Referencia de configuración** Valores predeterminados del agente y configuración de modelo. ](</es/gateway/config-agents#agent-defaults>)

Was this useful?YesNo