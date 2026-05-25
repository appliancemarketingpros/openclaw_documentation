---
title: Qianfan
source_url: https://docs.openclaw.ai/es/providers/qianfan
scraped_at: 2026-05-25
---

Qianfan es la plataforma MaaS de Baidu, que proporciona una **API unificada** que enruta solicitudes a muchos modelos detrás de un único punto de conexión y clave de API. Es compatible con OpenAI, por lo que la mayoría de los SDK de OpenAI funcionan cambiando la URL base.

Propiedad | Valor  
---|---  
Proveedor | `qianfan`  
Autenticación | `QIANFAN_API_KEY`  
API | Compatible con OpenAI  
URL base | `https://qianfan.baidubce.com/v2`  
  
## Primeros pasos

* ### Create a Baidu Cloud account

Regístrate o inicia sesión en la [consola de Qianfan](<https://console.bce.baidu.com/qianfan/ais/console/apiKey>) y asegúrate de tener habilitado el acceso a la API de Qianfan.

* ### Generate an API key

Crea una aplicación nueva o selecciona una existente y luego genera una clave de API. El formato de la clave es `bce-v3/ALTAK-...`.

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice qianfan-api-key
[/code]

* ### Verify the model is available

bashCopy code
[code]
    openclaw models list --provider qianfan
[/code]

## Catálogo integrado

Referencia del modelo | Entrada | Contexto | Salida máxima | Razonamiento | Notas  
---|---|---|---|---|---  
`qianfan/deepseek-v3.2` | texto | 98,304 | 32,768 | Sí | Modelo predeterminado  
`qianfan/ernie-5.0-thinking-preview` | texto, imagen | 119,000 | 64,000 | Sí | Multimodal  
  
## Ejemplo de configuración

json5Copy code
[code]
    {  env: { QIANFAN_API_KEY: "bce-v3/ALTAK-..." },  agents: {    defaults: {      model: { primary: "qianfan/deepseek-v3.2" },      models: {        "qianfan/deepseek-v3.2": { alias: "QIANFAN" },      },    },  },  models: {    providers: {      qianfan: {        baseUrl: "https://qianfan.baidubce.com/v2",        api: "openai-completions",        models: [          {            id: "deepseek-v3.2",            name: "DEEPSEEK V3.2",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 98304,            maxTokens: 32768,          },          {            id: "ernie-5.0-thinking-preview",            name: "ERNIE-5.0-Thinking-Preview",            reasoning: true,            input: ["text", "image"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 119000,            maxTokens: 64000,          },        ],      },    },  },}
[/code]

Transport and compatibility

Qianfan se ejecuta mediante la ruta de transporte compatible con OpenAI, no mediante la conformación nativa de solicitudes de OpenAI. Esto significa que las funciones estándar de los SDK de OpenAI funcionan, pero es posible que no se reenvíen los parámetros específicos del proveedor.

Catalog and overrides

El catálogo incluido actualmente incluye `deepseek-v3.2` y `ernie-5.0-thinking-preview`. Añade o sobrescribe `models.providers.qianfan` solo cuando necesites una URL base personalizada o metadatos de modelo.

Troubleshooting

  * Asegúrate de que tu clave de API empiece por `bce-v3/ALTAK-` y tenga habilitado el acceso a la API de Qianfan en la consola de Baidu Cloud.
  * Si los modelos no aparecen en la lista, confirma que tu cuenta tenga activado el servicio Qianfan.
  * La URL base predeterminada es `https://qianfan.baidubce.com/v2`. Cámbiala solo si usas un punto de conexión personalizado o un proxy.


## Relacionado

[**Model selection** Elegir proveedores, referencias de modelo y comportamiento de conmutación por error. ](</es/concepts/model-providers>) [**Configuration reference** Referencia completa de configuración de OpenClaw. ](</es/gateway/configuration-reference>) [**Agent setup** Configurar valores predeterminados de agentes y asignaciones de modelos. ](</es/concepts/agent>) [**Qianfan API docs** Documentación oficial de la API de Qianfan. ](<https://cloud.baidu.com/doc/qianfan-api/s/3m7of64lb>)

Was this useful?YesNo