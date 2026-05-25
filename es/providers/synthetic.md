---
title: Synthetic
source_url: https://docs.openclaw.ai/es/providers/synthetic
scraped_at: 2026-05-25
---

[Synthetic](<https://synthetic.new>) expone endpoints compatibles con Anthropic. OpenClaw lo registra como proveedor `synthetic` y usa la API Anthropic Messages.

Propiedad | Valor  
---|---  
Proveedor | `synthetic`  
Autenticación | `SYNTHETIC_API_KEY`  
API | Anthropic Messages  
URL base | `https://api.synthetic.new/anthropic`  
  
## Primeros pasos

* ### Obtén una clave de API

Obtén una `SYNTHETIC_API_KEY` desde tu cuenta de Synthetic, o deja que el asistente de incorporación te la solicite.

* ### Ejecuta la incorporación

bashCopy code
[code]
    openclaw onboard --auth-choice synthetic-api-key
[/code]

* ### Verifica el modelo predeterminado

Después de la incorporación, el modelo predeterminado se establece en:

textCopy code
[code]
    synthetic/hf:MiniMaxAI/MiniMax-M2.5
[/code]

## Ejemplo de configuración

json5Copy code
[code]
    {  env: { SYNTHETIC_API_KEY: "sk-..." },  agents: {    defaults: {      model: { primary: "synthetic/hf:MiniMaxAI/MiniMax-M2.5" },      models: { "synthetic/hf:MiniMaxAI/MiniMax-M2.5": { alias: "MiniMax M2.5" } },    },  },  models: {    mode: "merge",    providers: {      synthetic: {        baseUrl: "https://api.synthetic.new/anthropic",        apiKey: "${SYNTHETIC_API_KEY}",        api: "anthropic-messages",        models: [          {            id: "hf:MiniMaxAI/MiniMax-M2.5",            name: "MiniMax M2.5",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 192000,            maxTokens: 65536,          },        ],      },    },  },}
[/code]

## Catálogo integrado

Todos los modelos de Synthetic usan coste `0` (entrada/salida/caché).

ID del modelo | Ventana de contexto | Máx. tokens | Reasoning | Entrada  
---|---|---|---|---  
`hf:MiniMaxAI/MiniMax-M2.5` | 192,000 | 65,536 | no | text  
`hf:moonshotai/Kimi-K2-Thinking` | 256,000 | 8,192 | sí | text  
`hf:zai-org/GLM-4.7` | 198,000 | 128,000 | no | text  
`hf:deepseek-ai/DeepSeek-R1-0528` | 128,000 | 8,192 | no | text  
`hf:deepseek-ai/DeepSeek-V3-0324` | 128,000 | 8,192 | no | text  
`hf:deepseek-ai/DeepSeek-V3.1` | 128,000 | 8,192 | no | text  
`hf:deepseek-ai/DeepSeek-V3.1-Terminus` | 128,000 | 8,192 | no | text  
`hf:deepseek-ai/DeepSeek-V3.2` | 159,000 | 8,192 | no | text  
`hf:meta-llama/Llama-3.3-70B-Instruct` | 128,000 | 8,192 | no | text  
`hf:meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8` | 524,000 | 8,192 | no | text  
`hf:moonshotai/Kimi-K2-Instruct-0905` | 256,000 | 8,192 | no | text  
`hf:moonshotai/Kimi-K2.5` | 256,000 | 8,192 | sí | text + image  
`hf:openai/gpt-oss-120b` | 128,000 | 8,192 | no | text  
`hf:Qwen/Qwen3-235B-A22B-Instruct-2507` | 256,000 | 8,192 | no | text  
`hf:Qwen/Qwen3-Coder-480B-A35B-Instruct` | 256,000 | 8,192 | no | text  
`hf:Qwen/Qwen3-VL-235B-A22B-Instruct` | 250,000 | 8,192 | no | text + image  
`hf:zai-org/GLM-4.5` | 128,000 | 128,000 | no | text  
`hf:zai-org/GLM-4.6` | 198,000 | 128,000 | no | text  
`hf:zai-org/GLM-5` | 256,000 | 128,000 | sí | text + image  
`hf:deepseek-ai/DeepSeek-V3` | 128,000 | 8,192 | no | text  
`hf:Qwen/Qwen3-235B-A22B-Thinking-2507` | 256,000 | 8,192 | sí | text  
  
Lista de permitidos de modelos

Si habilitas una lista de permitidos de modelos (`agents.defaults.models`), añade cada modelo de Synthetic que planees usar. Los modelos que no estén en la lista de permitidos quedarán ocultos para el agente.

Anulación de URL base

Si Synthetic cambia su endpoint de API, anula la URL base en tu configuración:

json5Copy code
[code]
    {  models: {    providers: {      synthetic: {        baseUrl: "https://new-api.synthetic.new/anthropic",      },    },  },}
[/code]

Recuerda que OpenClaw añade `/v1` automáticamente.

## Relacionado

[**Selección de modelos** Reglas de proveedores, referencias de modelos y comportamiento de alternativas. ](</es/concepts/model-providers>) [**Referencia de configuración** Esquema completo de configuración, incluida la configuración del proveedor. ](</es/gateway/configuration-reference>) [**Synthetic** Panel de Synthetic y documentación de la API. ](<https://synthetic.new>)

Was this useful?YesNo