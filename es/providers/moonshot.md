---
title: Moonshot AI
source_url: https://docs.openclaw.ai/es/providers/moonshot
scraped_at: 2026-05-25
---

Moonshot proporciona la API de Kimi con endpoints compatibles con OpenAI. Configura el proveedor y establece el modelo predeterminado en `moonshot/kimi-k2.6`, o usa Kimi Coding con `kimi/kimi-for-coding`.

## Catálogo de modelos integrado

Ref de modelo | Nombre | Razonamiento | Entrada | Contexto | Salida máx.  
---|---|---|---|---|---  
`moonshot/kimi-k2.6` | Kimi K2.6 | No | texto, imagen | 262,144 | 262,144  
`moonshot/kimi-k2.5` | Kimi K2.5 | No | texto, imagen | 262,144 | 262,144  
`moonshot/kimi-k2-thinking` | Kimi K2 Thinking | Sí | texto | 262,144 | 262,144  
`moonshot/kimi-k2-thinking-turbo` | Kimi K2 Thinking Turbo | Sí | texto | 262,144 | 262,144  
`moonshot/kimi-k2-turbo` | Kimi K2 Turbo | No | texto | 256,000 | 16,384  
  
Las estimaciones de costo incluidas para los modelos K2 actuales alojados en Moonshot usan las tarifas publicadas de pago por uso de Moonshot: Kimi K2.6 cuesta $0.16/MTok por acierto de caché, $0.95/MTok de entrada y $4.00/MTok de salida; Kimi K2.5 cuesta $0.10/MTok por acierto de caché, $0.60/MTok de entrada y $3.00/MTok de salida. Otras entradas heredadas del catálogo mantienen marcadores de posición de costo cero salvo que los sobrescribas en la configuración.

## Primeros pasos

Elige tu proveedor y sigue los pasos de configuración.

### API de Moonshot

**Ideal para:** modelos Kimi K2 mediante Moonshot Open Platform.

* ### Elige la región de tu endpoint

Opción de autenticación | Endpoint | Región  
---|---|---  
`moonshot-api-key` | `https://api.moonshot.ai/v1` | Internacional  
`moonshot-api-key-cn` | `https://api.moonshot.cn/v1` | China  
* ### Ejecuta la incorporación

bashCopy code
[code]
    openclaw onboard --auth-choice moonshot-api-key
[/code]

O para el endpoint de China:

bashCopy code
[code]
    openclaw onboard --auth-choice moonshot-api-key-cn
[/code]

* ### Establece un modelo predeterminado

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "moonshot/kimi-k2.6" },    },  },}
[/code]

* ### Verifica que los modelos estén disponibles

bashCopy code
[code]
    openclaw models list --provider moonshot
[/code]

* ### Ejecuta una prueba rápida en vivo

Usa un directorio de estado aislado cuando quieras verificar el acceso al modelo y el seguimiento de costos sin tocar tus sesiones normales:

bashCopy code
[code]
    OPENCLAW_CONFIG_PATH=/tmp/openclaw-kimi/openclaw.json \OPENCLAW_STATE_DIR=/tmp/openclaw-kimi \openclaw agent --local \  --session-id live-kimi-cost \  --message 'Reply exactly: KIMI_LIVE_OK' \  --thinking off \  --json
[/code]

La respuesta JSON debe informar `provider: "moonshot"` y `model: "kimi-k2.6"`. La entrada de la transcripción del asistente almacena el uso de tokens normalizado más el costo estimado en `usage.cost` cuando Moonshot devuelve metadatos de uso.

### Ejemplo de configuración

json5Copy code
[code]
    {  env: { MOONSHOT_API_KEY: "sk-..." },  agents: {    defaults: {      model: { primary: "moonshot/kimi-k2.6" },      models: {        // moonshot-kimi-k2-aliases:start        "moonshot/kimi-k2.6": { alias: "Kimi K2.6" },        "moonshot/kimi-k2.5": { alias: "Kimi K2.5" },        "moonshot/kimi-k2-thinking": { alias: "Kimi K2 Thinking" },        "moonshot/kimi-k2-thinking-turbo": { alias: "Kimi K2 Thinking Turbo" },        "moonshot/kimi-k2-turbo": { alias: "Kimi K2 Turbo" },        // moonshot-kimi-k2-aliases:end      },    },  },  models: {    mode: "merge",    providers: {      moonshot: {        baseUrl: "https://api.moonshot.ai/v1",        apiKey: "${MOONSHOT_API_KEY}",        api: "openai-completions",        models: [          // moonshot-kimi-k2-models:start          {            id: "kimi-k2.6",            name: "Kimi K2.6",            reasoning: false,            input: ["text", "image"],            cost: { input: 0.95, output: 4, cacheRead: 0.16, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 262144,          },          {            id: "kimi-k2.5",            name: "Kimi K2.5",            reasoning: false,            input: ["text", "image"],            cost: { input: 0.6, output: 3, cacheRead: 0.1, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 262144,          },          {            id: "kimi-k2-thinking",            name: "Kimi K2 Thinking",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 262144,          },          {            id: "kimi-k2-thinking-turbo",            name: "Kimi K2 Thinking Turbo",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 262144,          },          {            id: "kimi-k2-turbo",            name: "Kimi K2 Turbo",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 256000,            maxTokens: 16384,          },          // moonshot-kimi-k2-models:end        ],      },    },  },}
[/code]

### Kimi Coding

**Ideal para:** tareas centradas en código mediante el endpoint de Kimi Coding.

* ### Ejecuta la incorporación

bashCopy code
[code]
    openclaw onboard --auth-choice kimi-code-api-key
[/code]

* ### Establece un modelo predeterminado

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "kimi/kimi-for-coding" },    },  },}
[/code]

* ### Verifica que el modelo esté disponible

bashCopy code
[code]
    openclaw models list --provider kimi
[/code]

### Ejemplo de configuración

json5Copy code
[code]
    {  env: { KIMI_API_KEY: "sk-..." },  agents: {    defaults: {      model: { primary: "kimi/kimi-for-coding" },      models: {        "kimi/kimi-for-coding": { alias: "Kimi" },      },    },  },}
[/code]

## Búsqueda web de Kimi

OpenClaw también incluye **Kimi** como proveedor de `web_search`, respaldado por la búsqueda web de Moonshot.

* ### Run interactive web search setup

bashCopy code
[code]
    openclaw configure --section web
[/code]

Elige **Kimi** en la sección de búsqueda web para almacenar `plugins.entries.moonshot.config.webSearch.*`.

* ### Configure the web search region and model

La configuración interactiva solicita:

Configuración | Opciones  
---|---  
Región de API | `https://api.moonshot.ai/v1` (internacional) o `https://api.moonshot.cn/v1` (China)  
Modelo de búsqueda web | Predeterminado en `kimi-k2.6`  
  
La configuración se encuentra en `plugins.entries.moonshot.config.webSearch`:

json5Copy code
[code]
    {  plugins: {    entries: {      moonshot: {        config: {          webSearch: {            apiKey: "sk-...", // or use KIMI_API_KEY / MOONSHOT_API_KEY            baseUrl: "https://api.moonshot.ai/v1",            model: "kimi-k2.6",          },        },      },    },  },  tools: {    web: {      search: {        provider: "kimi",      },    },  },}
[/code]

## Configuración avanzada

Native thinking mode

Moonshot Kimi admite el modo de pensamiento nativo binario:

  * `thinking: { type: "enabled" }`
  * `thinking: { type: "disabled" }`


Configúralo por modelo mediante `agents.defaults.models.<provider/model>.params`:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "moonshot/kimi-k2.6": {          params: {            thinking: { type: "disabled" },          },        },      },    },  },}
[/code]

OpenClaw también asigna niveles `/think` en tiempo de ejecución para Moonshot:

nivel de `/think` | comportamiento de Moonshot  
---|---  
`/think off` | `thinking.type=disabled`  
Cualquier nivel que no sea off | `thinking.type=enabled`  
  
Kimi K2.6 también acepta un campo opcional `thinking.keep` que controla la retención de varios turnos de `reasoning_content`. Configúralo como `"all"` para conservar el razonamiento completo entre turnos; omítelo (o déjalo como `null`) para usar la estrategia predeterminada del servidor. OpenClaw solo reenvía `thinking.keep` para `moonshot/kimi-k2.6` y lo elimina de otros modelos.

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "moonshot/kimi-k2.6": {          params: {            thinking: { type: "enabled", keep: "all" },          },        },      },    },  },}
[/code]

Saneamiento de id de llamadas a herramientas

Moonshot Kimi sirve ids de tool_call con la forma `functions.<name>:<index>`. OpenClaw los conserva sin cambios para que las llamadas a herramientas de varios turnos sigan funcionando.

Para forzar un saneamiento estricto en un proveedor personalizado compatible con OpenAI, configura `sanitizeToolCallIds: true`:

json5Copy code
[code]
    {  models: {    providers: {      "my-kimi-proxy": {        api: "openai-completions",        sanitizeToolCallIds: true,      },    },  },}
[/code]

Compatibilidad de uso en streaming

Los endpoints nativos de Moonshot (`https://api.moonshot.ai/v1` y `https://api.moonshot.cn/v1`) anuncian compatibilidad de uso en streaming en el transporte compartido `openai-completions`. OpenClaw determina eso a partir de las capacidades del endpoint, por lo que los ids de proveedores personalizados compatibles que apuntan a los mismos hosts nativos de Moonshot heredan el mismo comportamiento de uso en streaming.

Con los precios incluidos de K2.6, el uso en streaming que incluye tokens de entrada, salida y lectura de caché también se convierte en un costo local estimado en USD para `/status`, `/usage full`, `/usage cost` y la contabilidad de sesiones respaldada por transcripciones.

Referencia de punto de conexión y referencia de modelo Proveedor | Prefijo de referencia de modelo | Punto de conexión | Variable de entorno de autenticación  
---|---|---|---  
Moonshot | `moonshot/` | `https://api.moonshot.ai/v1` | `MOONSHOT_API_KEY`  
Moonshot CN | `moonshot/` | `https://api.moonshot.cn/v1` | `MOONSHOT_API_KEY`  
Kimi Coding | `kimi/` | Punto de conexión de Kimi Coding | `KIMI_API_KEY`  
Búsqueda web | N/D | Igual que la región de la API de Moonshot | `KIMI_API_KEY` o `MOONSHOT_API_KEY`  
  
  * La búsqueda web de Kimi usa `KIMI_API_KEY` o `MOONSHOT_API_KEY`, y de forma predeterminada usa `https://api.moonshot.ai/v1` con el modelo `kimi-k2.6`.
  * Sobrescribe los precios y los metadatos de contexto en `models.providers` si es necesario.
  * Si Moonshot publica límites de contexto distintos para un modelo, ajusta `contextWindow` según corresponda.


## Relacionado

[**Selección de modelo** Elegir proveedores, referencias de modelo y comportamiento de conmutación por error. ](</es/concepts/model-providers>) [**Búsqueda web** Configurar proveedores de búsqueda web, incluido Kimi. ](</es/tools/web>) [**Referencia de configuración** Esquema de configuración completo para proveedores, modelos y plugins. ](</es/gateway/configuration-reference>) [**Moonshot Open Platform** Gestión de claves de API de Moonshot y documentación. ](<https://platform.moonshot.ai>)

Was this useful?YesNo