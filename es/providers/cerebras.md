---
title: Cerebras
source_url: https://docs.openclaw.ai/es/providers/cerebras
scraped_at: 2026-05-25
---

[Cerebras](<https://www.cerebras.ai>) proporciona inferencia de alta velocidad compatible con OpenAI en hardware de inferencia personalizado. OpenClaw incluye un Plugin de proveedor de Cerebras integrado con un catálogo estático de cuatro modelos.

Propiedad | Valor  
---|---  
ID de proveedor | `cerebras`  
Plugin | integrado, `enabledByDefault: true`  
Variable de entorno de autenticación | `CEREBRAS_API_KEY`  
Marca de incorporación | `--auth-choice cerebras-api-key`  
Marca directa de CLI | `--cerebras-api-key <key>`  
API | compatible con OpenAI (`openai-completions`)  
URL base | `https://api.cerebras.ai/v1`  
Modelo predeterminado | `cerebras/zai-glm-4.7`  
  
## Primeros pasos

* ### Obtener una clave de API

Crea una clave de API en la [Cerebras Cloud Console](<https://cloud.cerebras.ai>).

* ### Ejecutar la incorporación

OnboardingCopy code
[code]
    openclaw onboard --auth-choice cerebras-api-key
[/code]

Direct flagCopy code
[code]
    openclaw onboard --non-interactive \--auth-choice cerebras-api-key \--cerebras-api-key "$CEREBRAS_API_KEY"
[/code]

Env onlyCopy code
[code]
    export CEREBRAS_API_KEY=csk-...
[/code]

* ### Verificar que los modelos estén disponibles

bashCopy code
[code]
    openclaw models list --provider cerebras
[/code]

La lista debe incluir los cuatro modelos integrados. Si `CEREBRAS_API_KEY` no se resuelve, `openclaw models status --json` informa la credencial faltante en `auth.unusableProfiles`.

## Configuración no interactiva

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice cerebras-api-key \  --cerebras-api-key "$CEREBRAS_API_KEY"
[/code]

## Catálogo integrado

OpenClaw incluye un catálogo estático de Cerebras que replica el endpoint público compatible con OpenAI. Los cuatro modelos comparten un contexto de 128k y 8192 tokens de salida máxima.

Referencia del modelo | Nombre | Razonamiento | Notas  
---|---|---|---  
`cerebras/zai-glm-4.7` | [Z.ai](<http://Z.ai>) GLM 4.7 | sí | Modelo predeterminado; modelo de razonamiento en vista previa  
`cerebras/gpt-oss-120b` | GPT OSS 120B | sí | Modelo de razonamiento de producción  
`cerebras/qwen-3-235b-a22b-instruct-2507` | Qwen 3 235B Instruct | no | Modelo sin razonamiento en vista previa  
`cerebras/llama3.1-8b` | Llama 3.1 8B | no | Modelo de producción enfocado en velocidad  
  
## Configuración manual

El Plugin integrado normalmente significa que solo necesitas la clave de API. Usa la configuración explícita de `models.providers.cerebras` cuando quieras sobrescribir metadatos de modelos o ejecutar en `mode: "merge"` con el catálogo estático:

json5Copy code
[code]
    {  env: { CEREBRAS_API_KEY: "csk-..." },  agents: {    defaults: {      model: { primary: "cerebras/zai-glm-4.7" },    },  },  models: {    mode: "merge",    providers: {      cerebras: {        baseUrl: "https://api.cerebras.ai/v1",        apiKey: "${CEREBRAS_API_KEY}",        api: "openai-completions",        models: [          { id: "zai-glm-4.7", name: "Z.ai GLM 4.7" },          { id: "gpt-oss-120b", name: "GPT OSS 120B" },        ],      },    },  },}
[/code]

## Relacionado

[**Proveedores de modelos** Elegir proveedores, referencias de modelos y comportamiento de conmutación por error. ](</es/concepts/model-providers>) [**Modos de pensamiento** Niveles de esfuerzo de razonamiento para los dos modelos de Cerebras con capacidad de razonamiento. ](</es/tools/thinking>) [**Referencia de configuración** Valores predeterminados de agentes y configuración de modelos. ](</es/gateway/config-agents#agent-defaults>) [**Preguntas frecuentes sobre modelos** Perfiles de autenticación, cambio de modelos y resolución de errores de "sin perfil". ](</es/help/faq-models>)

Was this useful?YesNo