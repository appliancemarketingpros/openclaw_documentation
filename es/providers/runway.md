---
title: Pista
source_url: https://docs.openclaw.ai/es/providers/runway
scraped_at: 2026-05-25
---

OpenClaw incluye un proveedor `runway` integrado para generación de video alojada. El Plugin está habilitado de forma predeterminada y registra el proveedor `runway` con el contrato `videoGenerationProviders`.

Propiedad | Valor  
---|---  
ID del proveedor | `runway`  
Plugin | integrado, `enabledByDefault: true`  
Variables de entorno de autenticación | `RUNWAYML_API_SECRET` (canónica) o `RUNWAY_API_KEY`  
Opción de incorporación | `--auth-choice runway-api-key`  
Opción directa de CLI | `--runway-api-key <key>`  
API | Generación de video basada en tareas de Runway (sondeo de `GET /v1/tasks/{id}`)  
Modelo predeterminado | `runway/gen4.5`  
  
## Primeros pasos

* ### Set the API key

bashCopy code
[code]
    openclaw onboard --auth-choice runway-api-key
[/code]

* ### Set Runway as the default video provider

bashCopy code
[code]
    openclaw config set agents.defaults.videoGenerationModel.primary "runway/gen4.5"
[/code]

* ### Generate a video

Pídele al agente que genere un video. Runway se usará automáticamente.

## Modos y modelos compatibles

El proveedor expone siete modelos de Runway divididos en tres modos. El mismo ID de modelo puede servir para más de un modo (por ejemplo, `gen4.5` funciona tanto para texto a video como para imagen a video).

Modo | Modelos | Entrada de referencia  
---|---|---  
Texto a video | `gen4.5` (predeterminado), `veo3.1`, `veo3.1_fast`, `veo3` | Ninguna  
Imagen a video | `gen4.5`, `gen4_turbo`, `gen3a_turbo`, `veo3.1`, `veo3.1_fast`, `veo3` | 1 imagen local o remota  
Video a video | `gen4_aleph` | 1 video local o remoto  
  
Las referencias locales de imagen y video son compatibles mediante URI de datos.

Relaciones de aspecto | Valores permitidos  
---|---  
Texto a video | `16:9`, `9:16`  
Ediciones de imagen y video | `1:1`, `16:9`, `9:16`, `3:4`, `4:3`, `21:9`  
  
## Configuración

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "runway/gen4.5",      },    },  },}
[/code]

## Configuración avanzada

Environment variable aliases

OpenClaw reconoce tanto `RUNWAYML_API_SECRET` (canónica) como `RUNWAY_API_KEY`. Cualquiera de las dos variables autenticará el proveedor de Runway.

Task polling

Runway usa una API basada en tareas. Después de enviar una solicitud de generación, OpenClaw sondea `GET /v1/tasks/{id}` hasta que el video esté listo. No se necesita configuración adicional para el comportamiento de sondeo.

## Relacionado

[**Video generation** Parámetros de herramienta compartidos, selección de proveedor y comportamiento asíncrono. ](</es/tools/video-generation>) [**Configuration reference** Configuración predeterminada del agente, incluido el modelo de generación de video. ](</es/gateway/config-agents#agent-defaults>)

Was this useful?YesNo