---
title: Metadatos
source_url: https://docs.openclaw.ai/es/providers/meta
scraped_at: 2026-07-13
---

ModelsProviders

La **API de Meta** utiliza la **API Responses** compatible con OpenAI (`POST /v1/responses`) para el modelo de razonamiento `muse-spark-1.1`. El proveedor se distribuye como un Plugin incluido con OpenClaw.

Propiedad | Valor  
---|---  
Id. del proveedor | `meta`  
Plugin | proveedor incluido  
Variable de entorno de autenticación | `MODEL_API_KEY`  
Opción de incorporación | `--auth-choice meta-api-key`  
Opción directa de la CLI | `--meta-api-key <key>`  
API | API Responses (`openai-responses`)  
URL base | `https://api.meta.ai/v1`  
Modelo predeterminado | `meta/muse-spark-1.1`  
Razonamiento predeterminado | `high` (`reasoning.effort`)  
  
## Primeros pasos

* ### Configurar la clave de API

IncorporaciónCopy code
[code]
    openclaw onboard --auth-choice meta-api-key
[/code]

Opción directaCopy code
[code]
    openclaw onboard --non-interactive --accept-risk \--auth-choice meta-api-key \--meta-api-key "$MODEL_API_KEY"
[/code]

Solo variable de entornoCopy code
[code]
    export MODEL_API_KEY=<key>
[/code]

* ### Verificar que los modelos estén disponibles

bashCopy code
[code]
    openclaw models list --provider meta
[/code]

Muestra la entrada estática `muse-spark-1.1` del catálogo. Si `MODEL_API_KEY` no se puede resolver, `openclaw models status --json` informa de la credencial que falta en `auth.unusableProfiles`.

## Configuración no interactiva

bashCopy code
[code]
    openclaw onboard --non-interactive --accept-risk \  --mode local \  --auth-choice meta-api-key \  --meta-api-key "$MODEL_API_KEY"
[/code]

## Catálogo integrado

Referencia del modelo | Nombre | Razonamiento | Ventana de contexto | Salida máxima  
---|---|---|---|---  
`meta/muse-spark-1.1` | Muse Spark 1.1 | sí | 1,048,576 | 131,072  
  
Capacidades:

  * Entrada de texto e imágenes
  * Llamadas a herramientas y transmisión
  * Nivel de razonamiento: `minimal`, `low`, `medium`, `high`, `xhigh` (predeterminado: `high`)
  * Reproducción cifrada y sin estado del razonamiento (`store: false`, `include: ["reasoning.encrypted_content"]`)


## Configuración manual

json5Copy code
[code]
    {  env: { MODEL_API_KEY: "<key>" },  agents: {    defaults: {      model: { primary: "meta/muse-spark-1.1" },      models: {        "meta/muse-spark-1.1": { alias: "Muse Spark 1.1" },      },    },  },}
[/code]

## Prueba de humo

bashCopy code
[code]
    export MODEL_API_KEY=<key>pnpm test:live -- extensions/meta/meta.live.test.ts
[/code]

Las pruebas en vivo utilizan `muse-spark-1.1` con `POST /v1/responses`.

## Contenido relacionado

[**Proveedores de modelos** Elección de proveedores, referencias de modelos y comportamiento de conmutación por error. ](</es/concepts/model-providers>) [**Modos de pensamiento** Niveles de razonamiento para muse-spark-1.1. ](</es/tools/thinking>) [**Referencia de configuración** Valores predeterminados de los agentes y configuración de modelos. ](</es/gateway/config-agents#agent-defaults>)

Was this useful?YesNo

Open issue