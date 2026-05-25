---
title: Proveedores de modelos
source_url: https://docs.openclaw.ai/es/concepts/model-providers
scraped_at: 2026-05-25
---

Referencia para **proveedores de LLM/modelos** (no canales de chat como WhatsApp/Telegram). Para las reglas de selección de modelos, consulta [Modelos](</es/concepts/models>).

## Reglas rápidas

Referencias de modelo y auxiliares de CLI

  * Las referencias de modelo usan `provider/model` (ejemplo: `opencode/claude-opus-4-6`).
  * `agents.defaults.models` actúa como lista de permitidos cuando está configurado.
  * Auxiliares de CLI: `openclaw onboard`, `openclaw models list`, `openclaw models set <provider/model>`.
  * `models.providers.*.contextWindow` / `contextTokens` / `maxTokens` establecen valores predeterminados a nivel de proveedor; `models.providers.*.models[].contextWindow` / `contextTokens` / `maxTokens` los sobrescriben por modelo.
  * Reglas de reserva, comprobaciones de enfriamiento y persistencia de sobrescrituras de sesión: [conmutación por error de modelos](</es/concepts/model-failover>).

Añadir autenticación de proveedor no cambia tu modelo principal

`openclaw configure` conserva un `agents.defaults.model.primary` existente cuando añades o vuelves a autenticar un proveedor. `openclaw models auth login` hace lo mismo a menos que pases `--set-default`. Los Plugins de proveedor todavía pueden devolver un modelo predeterminado recomendado en su parche de configuración de autenticación, pero OpenClaw lo trata como "hacer que este modelo esté disponible" cuando ya existe un modelo principal, no como "reemplazar el modelo principal actual".

Para cambiar intencionadamente el modelo predeterminado, usa `openclaw models set <provider/model>` o `openclaw models auth login --provider <id> --set-default`.

Separación de proveedor/runtime de OpenAI

Las rutas de la familia OpenAI son específicas del prefijo:

  * `openai/<model>` usa de forma predeterminada el arnés nativo de servidor de aplicaciones de Codex para turnos de agente. Esta es la configuración habitual de suscripción a ChatGPT/Codex.
  * `openai-codex/<model>` es una configuración heredada que doctor reescribe a `openai/<model>`.
  * `openai/<model>` más `agentRuntime.id: "pi"` de proveedor/modelo usa PI para rutas explícitas con clave de API o de compatibilidad.


Consulta [OpenAI](</es/providers/openai>) y [arnés de Codex](</es/plugins/codex-harness>). Si la separación de proveedor/runtime resulta confusa, lee primero [runtimes de agente](</es/concepts/agent-runtimes>).

La activación automática de Plugins sigue el mismo límite: las referencias de agente `openai/*` activan el Plugin de Codex para la ruta predeterminada, y `agentRuntime.id: "codex"` explícito de proveedor/modelo o las referencias heredadas `codex/<model>` también lo requieren.

GPT-5.5 está disponible a través del arnés nativo de servidor de aplicaciones de Codex de forma predeterminada en `openai/gpt-5.5`, y a través de PI solo cuando la política de runtime de proveedor/modelo selecciona explícitamente `pi`.

Runtimes de CLI

Los runtimes de CLI usan la misma separación: elige referencias de modelo canónicas como `anthropic/claude-*`, `google/gemini-*` u `openai/gpt-*`, y luego configura la política de runtime de proveedor/modelo como `claude-cli`, `google-gemini-cli` o `codex-cli` cuando quieras un backend de CLI local.

Las referencias heredadas `claude-cli/*`, `google-gemini-cli/*` y `codex-cli/*` migran de vuelta a referencias canónicas de proveedor con el runtime registrado por separado.

## Comportamiento de proveedor propiedad del Plugin

La mayor parte de la lógica específica de proveedor vive en Plugins de proveedor (`registerProvider(...)`), mientras OpenClaw mantiene el bucle de inferencia genérico. Los Plugins son responsables del onboarding, los catálogos de modelos, la asignación de variables de entorno de autenticación, la normalización de transporte/configuración, la limpieza de esquemas de herramientas, la clasificación de conmutación por error, la actualización de OAuth, los informes de uso, los perfiles de pensamiento/razonamiento y más.

La lista completa de hooks del SDK de proveedores y ejemplos de Plugins incluidos está en [Plugins de proveedor](</es/plugins/sdk-provider-plugins>). Un proveedor que necesita un ejecutor de solicitudes totalmente personalizado es una superficie de extensión separada y más profunda.

## Rotación de claves de API

Fuentes de claves y prioridad

Configura varias claves mediante:

  * `OPENCLAW_LIVE_&lt;PROVIDER&gt;_KEY` (sobrescritura live única, máxima prioridad)
  * `&lt;PROVIDER&gt;_API_KEYS` (lista separada por comas o punto y coma)
  * `&lt;PROVIDER&gt;_API_KEY` (clave principal)
  * `&lt;PROVIDER&gt;_API_KEY_*` (lista numerada, por ejemplo `&lt;PROVIDER&gt;_API_KEY_1`)


Para proveedores de Google, `GOOGLE_API_KEY` también se incluye como reserva. El orden de selección de claves conserva la prioridad y elimina valores duplicados.

Cuándo se activa la rotación

  * Las solicitudes se reintentan con la siguiente clave solo en respuestas de límite de tasa (por ejemplo `429`, `rate_limit`, `quota`, `resource exhausted`, `Too many concurrent requests`, `ThrottlingException`, `concurrency limit reached`, `workers_ai ... quota limit exceeded` o mensajes periódicos de límite de uso).
  * Los fallos que no son de límite de tasa fallan inmediatamente; no se intenta ninguna rotación de claves.
  * Cuando todas las claves candidatas fallan, se devuelve el error final del último intento.


## Proveedores integrados (catálogo pi-ai)

OpenClaw se distribuye con el catálogo pi-ai. Estos proveedores **no** requieren configuración de `models.providers`; basta con configurar la autenticación y elegir un modelo.

### OpenAI

  * Proveedor: `openai`
  * Autenticación: `OPENAI_API_KEY`
  * Rotación opcional: `OPENAI_API_KEYS`, `OPENAI_API_KEY_1`, `OPENAI_API_KEY_2`, más `OPENCLAW_LIVE_OPENAI_KEY` (sobrescritura única)
  * Modelos de ejemplo: `openai/gpt-5.5`, `openai/gpt-5.4-mini`
  * Verifica la disponibilidad de la cuenta/modelo con `openclaw models list --provider openai` si una instalación o clave de API específica se comporta de manera distinta.
  * CLI: `openclaw onboard --auth-choice openai-api-key`
  * El transporte predeterminado es `auto`; OpenClaw pasa la elección de transporte a pi-ai.
  * Sobrescribe por modelo mediante `agents.defaults.models["openai/<model>"].params.transport` (`"sse"`, `"websocket"` o `"auto"`)
  * El procesamiento prioritario de OpenAI puede activarse mediante `agents.defaults.models["openai/<model>"].params.serviceTier`
  * `/fast` y `params.fastMode` asignan solicitudes directas de Responses `openai/*` a `service_tier=priority` en `api.openai.com`
  * Usa `params.serviceTier` cuando quieras un nivel explícito en vez del interruptor compartido `/fast`
  * Los encabezados ocultos de atribución de OpenClaw (`originator`, `version`, `User-Agent`) se aplican solo al tráfico nativo de OpenAI hacia `api.openai.com`, no a proxies genéricos compatibles con OpenAI
  * Las rutas nativas de OpenAI también conservan `store` de Responses, sugerencias de caché de prompts y modelado de payload compatible con razonamiento de OpenAI; las rutas de proxy no
  * `openai/gpt-5.3-codex-spark` se suprime intencionadamente en OpenClaw porque las solicitudes live de la API de OpenAI lo rechazan y el catálogo actual de Codex no lo expone

json5Copy code
[code]
    {  agents: { defaults: { model: { primary: "openai/gpt-5.5" } } },}
[/code]

### Anthropic

  * Proveedor: `anthropic`
  * Autenticación: `ANTHROPIC_API_KEY`
  * Rotación opcional: `ANTHROPIC_API_KEYS`, `ANTHROPIC_API_KEY_1`, `ANTHROPIC_API_KEY_2`, más `OPENCLAW_LIVE_ANTHROPIC_KEY` (sobrescritura única)
  * Modelo de ejemplo: `anthropic/claude-opus-4-6`
  * CLI: `openclaw onboard --auth-choice apiKey`
  * Las solicitudes públicas directas de Anthropic admiten el interruptor compartido `/fast` y `params.fastMode`, incluido el tráfico autenticado con clave de API y OAuth enviado a `api.anthropic.com`; OpenClaw lo asigna a `service_tier` de Anthropic (`auto` frente a `standard_only`)
  * La configuración preferida de Claude CLI mantiene la referencia de modelo canónica y selecciona el backend de CLI por separado: `anthropic/claude-opus-4-7` con `agentRuntime.id: "claude-cli"` con alcance de modelo. Las referencias heredadas `claude-cli/claude-opus-4-7` siguen funcionando por compatibilidad.

json5Copy code
[code]
    {  agents: { defaults: { model: { primary: "anthropic/claude-opus-4-6" } } },}
[/code]

### OAuth de OpenAI Codex

  * Proveedor: `openai-codex`
  * Autenticación: OAuth (ChatGPT)
  * Referencia de modelo heredada de PI: `openai-codex/gpt-5.5`
  * Referencia del arnés nativo de servidor de aplicaciones de Codex: `openai/gpt-5.5`
  * Documentación del arnés nativo de servidor de aplicaciones de Codex: [arnés de Codex](</es/plugins/codex-harness>)
  * Referencias de modelo heredadas: `codex/gpt-*`
  * Límite de Plugin: `openai-codex/*` carga el Plugin de OpenAI; el Plugin nativo de servidor de aplicaciones de Codex se selecciona solo mediante el runtime del arnés de Codex o referencias heredadas `codex/*`.
  * CLI: `openclaw onboard --auth-choice openai-codex` o `openclaw models auth login --provider openai-codex`
  * El transporte predeterminado es `auto` (WebSocket primero, SSE como reserva)
  * Sobrescribe por modelo de PI mediante `agents.defaults.models["openai-codex/<model>"].params.transport` (`"sse"`, `"websocket"` o `"auto"`)
  * `params.serviceTier` también se reenvía en solicitudes nativas de Responses de Codex (`chatgpt.com/backend-api`)
  * Los encabezados ocultos de atribución de OpenClaw (`originator`, `version`, `User-Agent`) solo se adjuntan en tráfico nativo de Codex hacia `chatgpt.com/backend-api`, no en proxies genéricos compatibles con OpenAI
  * Comparte la misma configuración de interruptor `/fast` y `params.fastMode` que `openai/*` directo; OpenClaw la asigna a `service_tier=priority`
  * `openai-codex/gpt-5.5` usa el `contextWindow = 400000` nativo del catálogo de Codex y el runtime predeterminado `contextTokens = 272000`; sobrescribe el límite de runtime con `models.providers.openai-codex.models[].contextTokens`
  * Nota de política: OpenAI Codex OAuth es compatible explícitamente con herramientas/flujos de trabajo externos como OpenClaw.
  * Para la ruta común de suscripción más runtime nativo de Codex, inicia sesión con autenticación `openai-codex` pero configura `openai/gpt-5.5`; los turnos de agente de OpenAI seleccionan Codex de forma predeterminada.
  * Usa `agentRuntime.id: "pi"` de proveedor/modelo solo cuando quieras una ruta de compatibilidad a través de PI; de lo contrario, mantén `openai/gpt-5.5` en el arnés de Codex predeterminado.
  * Las referencias antiguas `openai-codex/gpt-5.1*`, `openai-codex/gpt-5.2*` y `openai-codex/gpt-5.3*` se suprimen porque las cuentas OAuth de ChatGPT/Codex las rechazan; usa `openai-codex/gpt-5.5` o la ruta de runtime nativo de Codex en su lugar.

json5Copy code
[code]
    {  plugins: { entries: { codex: { enabled: true } } },  agents: {    defaults: {      model: { primary: "openai/gpt-5.5" },    },  },}
[/code]

json5Copy code
[code]
    {  models: {    providers: {      "openai-codex": {        models: [{ id: "gpt-5.5", contextTokens: 160000 }],      },    },  },}
[/code]

### Otras opciones alojadas de estilo suscripción

[**Modelos GLM** [Z.AI](<http://Z.AI>) Coding Plan o endpoints de API generales. ](</es/providers/glm>) [**MiniMax** OAuth de MiniMax Coding Plan o acceso con clave de API. ](</es/providers/minimax>) [**Qwen Cloud** Superficie de proveedor de Qwen Cloud más asignación de endpoints de Alibaba DashScope y Coding Plan. ](</es/providers/qwen>)

### OpenCode

  * Autenticación: `OPENCODE_API_KEY` (o `OPENCODE_ZEN_API_KEY`)
  * Proveedor de runtime Zen: `opencode`
  * Proveedor de runtime Go: `opencode-go`
  * Modelos de ejemplo: `opencode/claude-opus-4-6`, `opencode-go/kimi-k2.6`
  * CLI: `openclaw onboard --auth-choice opencode-zen` o `openclaw onboard --auth-choice opencode-go`

json5Copy code
[code]
    {  agents: { defaults: { model: { primary: "opencode/claude-opus-4-6" } } },}
[/code]

### Google Gemini (clave de API)

  * Proveedor: `google`
  * Autenticación: `GEMINI_API_KEY`
  * Rotación opcional: `GEMINI_API_KEYS`, `GEMINI_API_KEY_1`, `GEMINI_API_KEY_2`, respaldo de `GOOGLE_API_KEY` y `OPENCLAW_LIVE_GEMINI_KEY` (anulación única)
  * Modelos de ejemplo: `google/gemini-3.1-pro-preview`, `google/gemini-3-flash-preview`
  * Compatibilidad: la configuración heredada de OpenClaw que usa `google/gemini-3.1-flash-preview` se normaliza a `google/gemini-3-flash-preview`
  * Alias: `google/gemini-3.1-pro` se acepta y se normaliza al id de la API de Gemini en vivo de Google, `google/gemini-3.1-pro-preview`
  * CLI: `openclaw onboard --auth-choice gemini-api-key`
  * Razonamiento: `/think adaptive` usa el razonamiento dinámico de Google. Gemini 3/3.1 omiten un `thinkingLevel` fijo; Gemini 2.5 envía `thinkingBudget: -1`.
  * Las ejecuciones directas de Gemini también aceptan `agents.defaults.models["google/<model>"].params.cachedContent` (o el heredado `cached_content`) para reenviar un identificador nativo del proveedor `cachedContents/...`; los aciertos de caché de Gemini aparecen como `cacheRead` de OpenClaw


### Google Vertex y Gemini CLI

  * Proveedores: `google-vertex`, `google-gemini-cli`
  * Autenticación: Vertex usa gcloud ADC; Gemini CLI usa su flujo de OAuth


Gemini CLI OAuth se distribuye como parte del Plugin `google` incluido.

* ### Instalar Gemini CLI

### brew

bashCopy code
[code]
    brew install gemini-cli
[/code]

### npm

bashCopy code
[code]
    npm install -g @google/gemini-cli
[/code]

* ### Habilitar Plugin

bashCopy code
[code]
    openclaw plugins enable google
[/code]

* ### Iniciar sesión

bashCopy code
[code]
    openclaw models auth login --provider google-gemini-cli --set-default
[/code]

Modelo predeterminado: `google-gemini-cli/gemini-3-flash-preview`. **No** pegas un id de cliente ni un secreto en `openclaw.json`. El flujo de inicio de sesión de la CLI almacena tokens en perfiles de autenticación en el host del Gateway.

* ### Configurar proyecto (si es necesario)

Si las solicitudes fallan después de iniciar sesión, configura `GOOGLE_CLOUD_PROJECT` o `GOOGLE_CLOUD_PROJECT_ID` en el host del Gateway.

Las respuestas JSON de Gemini CLI se analizan desde `response`; el uso recurre a `stats`, con `stats.cached` normalizado en `cacheRead` de OpenClaw.

### [Z.AI](<http://Z.AI>) (GLM)

  * Proveedor: `zai`
  * Autenticación: `ZAI_API_KEY`
  * Modelo de ejemplo: `zai/glm-5.1`
  * CLI: `openclaw onboard --auth-choice zai-api-key`
    * Alias: `z.ai/*` y `z-ai/*` se normalizan a `zai/*`
    * `zai-api-key` detecta automáticamente el endpoint de [Z.AI](<http://Z.AI>) correspondiente; `zai-coding-global`, `zai-coding-cn`, `zai-global` y `zai-cn` fuerzan una superficie específica


### Vercel AI Gateway

  * Proveedor: `vercel-ai-gateway`
  * Autenticación: `AI_GATEWAY_API_KEY`
  * Modelos de ejemplo: `vercel-ai-gateway/anthropic/claude-opus-4.6`, `vercel-ai-gateway/moonshotai/kimi-k2.6`
  * CLI: `openclaw onboard --auth-choice ai-gateway-api-key`


### Kilo Gateway

  * Proveedor: `kilocode`
  * Autenticación: `KILOCODE_API_KEY`
  * Modelo de ejemplo: `kilocode/kilo/auto`
  * CLI: `openclaw onboard --auth-choice kilocode-api-key`
  * URL base: `https://api.kilo.ai/api/gateway/`
  * El catálogo de respaldo estático incluye `kilocode/kilo/auto`; el descubrimiento en vivo de `https://api.kilo.ai/api/gateway/models` puede ampliar aún más el catálogo en tiempo de ejecución.
  * El enrutamiento ascendente exacto detrás de `kilocode/kilo/auto` pertenece a Kilo Gateway, no está codificado de forma fija en OpenClaw.


Consulta [/providers/kilocode](</es/providers/kilocode>) para ver los detalles de configuración.

### Otros Plugins de proveedores incluidos

Proveedor | Id | Entorno de autenticación | Modelo de ejemplo  
---|---|---|---  
BytePlus | `byteplus` / `byteplus-plan` | `BYTEPLUS_API_KEY` | `byteplus-plan/ark-code-latest`  
Cerebras | `cerebras` | `CEREBRAS_API_KEY` | `cerebras/zai-glm-4.7`  
Cloudflare AI Gateway | `cloudflare-ai-gateway` | `CLOUDFLARE_AI_GATEWAY_API_KEY` | -  
DeepInfra | `deepinfra` | `DEEPINFRA_API_KEY` | `deepinfra/deepseek-ai/DeepSeek-V3.2`  
DeepSeek | `deepseek` | `DEEPSEEK_API_KEY` | `deepseek/deepseek-v4-flash`  
GitHub Copilot | `github-copilot` | `COPILOT_GITHUB_TOKEN` / `GH_TOKEN` / `GITHUB_TOKEN` | -  
Groq | `groq` | `GROQ_API_KEY` | -  
Hugging Face Inference | `huggingface` | `HUGGINGFACE_HUB_TOKEN` o `HF_TOKEN` | `huggingface/deepseek-ai/DeepSeek-R1`  
Kilo Gateway | `kilocode` | `KILOCODE_API_KEY` | `kilocode/kilo/auto`  
Kimi Coding | `kimi` | `KIMI_API_KEY` o `KIMICODE_API_KEY` | `kimi/kimi-for-coding`  
MiniMax | `minimax` / `minimax-portal` | `MINIMAX_API_KEY` / `MINIMAX_OAUTH_TOKEN` | `minimax/MiniMax-M2.7`  
Mistral | `mistral` | `MISTRAL_API_KEY` | `mistral/mistral-large-latest`  
Moonshot | `moonshot` | `MOONSHOT_API_KEY` | `moonshot/kimi-k2.6`  
NVIDIA | `nvidia` | `NVIDIA_API_KEY` | `nvidia/nvidia/nemotron-3-super-120b-a12b`  
OpenRouter | `openrouter` | `OPENROUTER_API_KEY` | `openrouter/auto`  
Qianfan | `qianfan` | `QIANFAN_API_KEY` | `qianfan/deepseek-v3.2`  
Qwen Cloud | `qwen` | `QWEN_API_KEY` / `MODELSTUDIO_API_KEY` / `DASHSCOPE_API_KEY` | `qwen/qwen3.5-plus`  
StepFun | `stepfun` / `stepfun-plan` | `STEPFUN_API_KEY` | `stepfun/step-3.5-flash`  
Together | `together` | `TOGETHER_API_KEY` | `together/moonshotai/Kimi-K2.5`  
Venice | `venice` | `VENICE_API_KEY` | -  
Vercel AI Gateway | `vercel-ai-gateway` | `AI_GATEWAY_API_KEY` | `vercel-ai-gateway/anthropic/claude-opus-4.6`  
Volcano Engine (Doubao) | `volcengine` / `volcengine-plan` | `VOLCANO_ENGINE_API_KEY` | `volcengine-plan/ark-code-latest`  
xAI | `xai` | `XAI_API_KEY` | `xai/grok-4.3`  
Xiaomi | `xiaomi` | `XIAOMI_API_KEY` | `xiaomi/mimo-v2-flash`  
  
#### Particularidades que conviene conocer

OpenRouter

Aplica sus encabezados de atribución de app y marcadores Anthropic `cache_control` solo en rutas `openrouter.ai` verificadas. Las refs DeepSeek, Moonshot y ZAI son elegibles para cache-TTL en el almacenamiento en caché de prompts gestionado por OpenRouter, pero no reciben marcadores de caché Anthropic. Como ruta estilo proxy compatible con OpenAI, omite el modelado exclusivo de OpenAI nativo (`serviceTier`, Responses `store`, sugerencias de caché de prompts, compatibilidad de razonamiento de OpenAI). Las refs respaldadas por Gemini conservan solo el saneamiento de firmas de pensamiento de proxy-Gemini.

Kilo Gateway

Las refs respaldadas por Gemini siguen la misma ruta de saneamiento de proxy-Gemini; `kilocode/kilo/auto` y otras refs de proxy sin soporte de razonamiento omiten la inyección de razonamiento de proxy.

MiniMax

La incorporación con clave API escribe definiciones explícitas de modelos de chat M2.7 solo de texto; la comprensión de imágenes permanece en el proveedor de medios `MiniMax-VL-01` propiedad del plugin.

NVIDIA

Los ids de modelo usan un espacio de nombres `nvidia/<vendor>/<model>` (por ejemplo, `nvidia/nvidia/nemotron-...` junto con `nvidia/moonshotai/kimi-k2.5`); los selectores preservan la composición literal `<provider>/<model-id>`, mientras que la clave canónica enviada a la API conserva un solo prefijo.

xAI

Usa la ruta Responses de xAI. `grok-4.3` es el modelo de chat predeterminado incluido. `/fast` o `params.fastMode: true` reescribe `grok-3`, `grok-3-mini`, `grok-4` y `grok-4-0709` a sus variantes `*-fast`. `tool_stream` está activado de forma predeterminada; desactívalo mediante `agents.defaults.models["xai/<model>"].params.tool_stream=false`.

Cerebras

Se distribuye como el plugin de proveedor `cerebras` incluido. GLM usa `zai-glm-4.7`; la URL base compatible con OpenAI es `https://api.cerebras.ai/v1`.

## Proveedores mediante `models.providers` (URL personalizada/base)

Usa `models.providers` (o `models.json`) para agregar proveedores **personalizados** o proxies compatibles con OpenAI/Anthropic.

Muchos de los plugins de proveedor incluidos a continuación ya publican un catálogo predeterminado. Usa entradas explícitas `models.providers.<id>` solo cuando quieras sobrescribir la URL base predeterminada, los encabezados o la lista de modelos.

Las comprobaciones de capacidades de modelo del Gateway también leen metadatos explícitos de `models.providers.<id>.models[]`. Si un modelo personalizado o de proxy acepta imágenes, define `input: ["text", "image"]` en ese modelo para que WebChat y las rutas de adjuntos originadas en nodos pasen imágenes como entradas nativas del modelo en lugar de refs de medios solo de texto.

`agents.defaults.models["provider/model"]` solo controla la visibilidad del modelo, los alias y los metadatos por modelo para los agentes. No registra por sí mismo un nuevo modelo en tiempo de ejecución. Para modelos de proveedor personalizados, agrega también `models.providers.<provider>.models[]` con al menos el `id` coincidente.

### Moonshot AI (Kimi)

Moonshot se distribuye como un plugin de proveedor incluido. Usa el proveedor integrado de forma predeterminada y agrega una entrada explícita `models.providers.moonshot` solo cuando necesites sobrescribir la URL base o los metadatos del modelo:

  * Proveedor: `moonshot`
  * Autenticación: `MOONSHOT_API_KEY`
  * Modelo de ejemplo: `moonshot/kimi-k2.6`
  * CLI: `openclaw onboard --auth-choice moonshot-api-key` o `openclaw onboard --auth-choice moonshot-api-key-cn`


IDs de modelo Kimi K2:

  * `moonshot/kimi-k2.6`
  * `moonshot/kimi-k2.5`
  * `moonshot/kimi-k2-thinking`
  * `moonshot/kimi-k2-thinking-turbo`
  * `moonshot/kimi-k2-turbo`

json5Copy code
[code]
    {  agents: {    defaults: { model: { primary: "moonshot/kimi-k2.6" } },  },  models: {    mode: "merge",    providers: {      moonshot: {        baseUrl: "https://api.moonshot.ai/v1",        apiKey: "${MOONSHOT_API_KEY}",        api: "openai-completions",        models: [{ id: "kimi-k2.6", name: "Kimi K2.6" }],      },    },  },}
[/code]

### Kimi coding

Kimi Coding usa el endpoint compatible con Anthropic de Moonshot AI:

  * Proveedor: `kimi`
  * Autenticación: `KIMI_API_KEY`
  * Modelo de ejemplo: `kimi/kimi-for-coding`

json5Copy code
[code]
    {  env: { KIMI_API_KEY: "sk-..." },  agents: {    defaults: { model: { primary: "kimi/kimi-for-coding" } },  },}
[/code]

Los `kimi/kimi-code` y `kimi/k2p5` heredados siguen aceptándose como ids de modelo de compatibilidad y se normalizan al id de modelo estable de la API de Kimi.

### Volcano Engine (Doubao)

Volcano Engine (火山引擎) proporciona acceso a Doubao y otros modelos en China.

  * Proveedor: `volcengine` (codificación: `volcengine-plan`)
  * Autenticación: `VOLCANO_ENGINE_API_KEY`
  * Modelo de ejemplo: `volcengine-plan/ark-code-latest`
  * CLI: `openclaw onboard --auth-choice volcengine-api-key`

json5Copy code
[code]
    {  agents: {    defaults: { model: { primary: "volcengine-plan/ark-code-latest" } },  },}
[/code]

La incorporación usa de forma predeterminada la superficie de codificación, pero el catálogo general `volcengine/*` se registra al mismo tiempo.

En los selectores de modelo de incorporación/configuración, la opción de autenticación de Volcengine prefiere las filas `volcengine/*` y `volcengine-plan/*`. Si esos modelos aún no están cargados, OpenClaw recurre al catálogo sin filtrar en lugar de mostrar un selector vacío limitado al proveedor.

### Modelos estándar

  * `volcengine/doubao-seed-1-8-251228` (Doubao Seed 1.8)
  * `volcengine/doubao-seed-code-preview-251028`
  * `volcengine/kimi-k2-5-260127` (Kimi K2.5)
  * `volcengine/glm-4-7-251222` (GLM 4.7)
  * `volcengine/deepseek-v3-2-251201` (DeepSeek V3.2 128K)


### Modelos de codificación (volcengine-plan)

  * `volcengine-plan/ark-code-latest`
  * `volcengine-plan/doubao-seed-code`
  * `volcengine-plan/kimi-k2.5`
  * `volcengine-plan/kimi-k2-thinking`
  * `volcengine-plan/glm-4.7`


### BytePlus (Internacional)

BytePlus ARK proporciona acceso a los mismos modelos que Volcano Engine para usuarios internacionales.

  * Proveedor: `byteplus` (codificación: `byteplus-plan`)
  * Autenticación: `BYTEPLUS_API_KEY`
  * Modelo de ejemplo: `byteplus-plan/ark-code-latest`
  * CLI: `openclaw onboard --auth-choice byteplus-api-key`

json5Copy code
[code]
    {  agents: {    defaults: { model: { primary: "byteplus-plan/ark-code-latest" } },  },}
[/code]

La incorporación usa de forma predeterminada la superficie de codificación, pero el catálogo general `byteplus/*` se registra al mismo tiempo.

En los selectores de modelo de incorporación/configuración, la opción de autenticación de BytePlus prefiere las filas `byteplus/*` y `byteplus-plan/*`. Si esos modelos aún no están cargados, OpenClaw recurre al catálogo sin filtrar en lugar de mostrar un selector vacío limitado al proveedor.

### Modelos estándar

  * `byteplus/seed-1-8-251228` (Seed 1.8)
  * `byteplus/kimi-k2-5-260127` (Kimi K2.5)
  * `byteplus/glm-4-7-251222` (GLM 4.7)


### Modelos de codificación (byteplus-plan)

  * `byteplus-plan/ark-code-latest`
  * `byteplus-plan/doubao-seed-code`
  * `byteplus-plan/kimi-k2.5`
  * `byteplus-plan/kimi-k2-thinking`
  * `byteplus-plan/glm-4.7`


### Synthetic

Synthetic proporciona modelos compatibles con Anthropic detrás del proveedor `synthetic`:

  * Proveedor: `synthetic`
  * Autenticación: `SYNTHETIC_API_KEY`
  * Modelo de ejemplo: `synthetic/hf:MiniMaxAI/MiniMax-M2.5`
  * CLI: `openclaw onboard --auth-choice synthetic-api-key`

json5Copy code
[code]
    {  agents: {    defaults: { model: { primary: "synthetic/hf:MiniMaxAI/MiniMax-M2.5" } },  },  models: {    mode: "merge",    providers: {      synthetic: {        baseUrl: "https://api.synthetic.new/anthropic",        apiKey: "${SYNTHETIC_API_KEY}",        api: "anthropic-messages",        models: [{ id: "hf:MiniMaxAI/MiniMax-M2.5", name: "MiniMax M2.5" }],      },    },  },}
[/code]

### MiniMax

MiniMax se configura mediante `models.providers` porque usa endpoints personalizados:

  * MiniMax OAuth (Global): `--auth-choice minimax-global-oauth`
  * MiniMax OAuth (CN): `--auth-choice minimax-cn-oauth`
  * Clave de API de MiniMax (Global): `--auth-choice minimax-global-api`
  * Clave de API de MiniMax (CN): `--auth-choice minimax-cn-api`
  * Autenticación: `MINIMAX_API_KEY` para `minimax`; `MINIMAX_OAUTH_TOKEN` o `MINIMAX_API_KEY` para `minimax-portal`


Consulta [/providers/minimax](</es/providers/minimax>) para detalles de configuración, opciones de modelo y fragmentos de configuración.

División de capacidades propiedad del Plugin:

  * Los valores predeterminados de texto/chat permanecen en `minimax/MiniMax-M2.7`
  * La generación de imágenes es `minimax/image-01` o `minimax-portal/image-01`
  * La comprensión de imágenes es `MiniMax-VL-01`, propiedad del Plugin, en ambas rutas de autenticación de MiniMax
  * La búsqueda web permanece en el id de proveedor `minimax`


### LM Studio

LM Studio se distribuye como un Plugin de proveedor incluido que usa la API nativa:

  * Proveedor: `lmstudio`
  * Autenticación: `LM_API_TOKEN`
  * URL base de inferencia predeterminada: `http://localhost:1234/v1`


Luego configura un modelo (reemplázalo por uno de los IDs devueltos por `http://localhost:1234/api/v1/models`):

json5Copy code
[code]
    {  agents: {    defaults: { model: { primary: "lmstudio/openai/gpt-oss-20b" } },  },}
[/code]

OpenClaw usa los endpoints nativos de LM Studio `/api/v1/models` y `/api/v1/models/load` para descubrimiento y carga automática, con `/v1/chat/completions` para inferencia de forma predeterminada. Si quieres que la carga JIT, el TTL y la expulsión automática de LM Studio sean dueños del ciclo de vida del modelo, configura `models.providers.lmstudio.params.preload: false`. Consulta [/providers/lmstudio](</es/providers/lmstudio>) para configuración y solución de problemas.

### Ollama

Ollama se distribuye como un Plugin de proveedor incluido y usa la API nativa de Ollama:

  * Proveedor: `ollama`
  * Autenticación: No requerida (servidor local)
  * Modelo de ejemplo: `ollama/llama3.3`
  * Instalación: <https://ollama.com/download>

bashCopy code
[code]
    # Install Ollama, then pull a model:ollama pull llama3.3
[/code]

json5Copy code
[code]
    {  agents: {    defaults: { model: { primary: "ollama/llama3.3" } },  },}
[/code]

Ollama se detecta localmente en `http://127.0.0.1:11434` cuando lo habilitas con `OLLAMA_API_KEY`, y el Plugin de proveedor incluido añade Ollama directamente a `openclaw onboard` y al selector de modelos. Consulta [/providers/ollama](</es/providers/ollama>) para incorporación, modo en la nube/local y configuración personalizada.

### vLLM

vLLM se distribuye como un Plugin de proveedor incluido para servidores locales/autohospedados compatibles con OpenAI:

  * Proveedor: `vllm`
  * Autenticación: Opcional (depende de tu servidor)
  * URL base predeterminada: `http://127.0.0.1:8000/v1`


Para habilitar el descubrimiento automático localmente (cualquier valor funciona si tu servidor no aplica autenticación):

bashCopy code
[code]
    export VLLM_API_KEY="vllm-local"
[/code]

Luego configura un modelo (reemplázalo por uno de los IDs devueltos por `/v1/models`):

json5Copy code
[code]
    {  agents: {    defaults: { model: { primary: "vllm/your-model-id" } },  },}
[/code]

Consulta [/providers/vllm](</es/providers/vllm>) para más detalles.

### SGLang

SGLang se distribuye como un Plugin de proveedor incluido para servidores rápidos autohospedados compatibles con OpenAI:

  * Proveedor: `sglang`
  * Autenticación: Opcional (depende de tu servidor)
  * URL base predeterminada: `http://127.0.0.1:30000/v1`


Para habilitar el descubrimiento automático localmente (cualquier valor funciona si tu servidor no aplica autenticación):

bashCopy code
[code]
    export SGLANG_API_KEY="sglang-local"
[/code]

Luego configura un modelo (reemplázalo por uno de los IDs devueltos por `/v1/models`):

json5Copy code
[code]
    {  agents: {    defaults: { model: { primary: "sglang/your-model-id" } },  },}
[/code]

Consulta [/providers/sglang](</es/providers/sglang>) para más detalles.

### Proxies locales (LM Studio, vLLM, LiteLLM, etc.)

Ejemplo (compatible con OpenAI):

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "lmstudio/my-local-model" },      models: { "lmstudio/my-local-model": { alias: "Local" } },    },  },  models: {    providers: {      lmstudio: {        baseUrl: "http://localhost:1234/v1",        apiKey: "${LM_API_TOKEN}",        api: "openai-completions",        timeoutSeconds: 300,        models: [          {            id: "my-local-model",            name: "Local Model",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 200000,            maxTokens: 8192,          },        ],      },    },  },}
[/code]

Campos opcionales predeterminados

Para proveedores personalizados, `reasoning`, `input`, `cost`, `contextWindow` y `maxTokens` son opcionales. Cuando se omiten, OpenClaw usa de forma predeterminada:

  * `reasoning: false`
  * `input: ["text"]`
  * `cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 }`
  * `contextWindow: 200000`
  * `maxTokens: 8192`


Recomendado: configura valores explícitos que coincidan con los límites de tu proxy/modelo.

Reglas de conformación de rutas de proxy

  * Para `api: "openai-completions"` en endpoints no nativos (cualquier `baseUrl` no vacío cuyo host no sea `api.openai.com`), OpenClaw fuerza `compat.supportsDeveloperRole: false` para evitar errores 400 del proveedor por roles `developer` no compatibles.
  * Las rutas de proxy compatibles con OpenAI también omiten la conformación de solicitudes exclusiva de OpenAI nativo: sin `service_tier`, sin `store` de Responses, sin `store` de Completions, sin sugerencias de caché de prompts, sin conformación de payload de compatibilidad de razonamiento de OpenAI y sin encabezados de atribución ocultos de OpenClaw.
  * Para proxies de Completions compatibles con OpenAI que necesitan campos específicos del proveedor, configura `agents.defaults.models["provider/model"].params.extra_body` (o `extraBody`) para fusionar JSON adicional en el cuerpo de la solicitud saliente.
  * Para controles de plantilla de chat de vLLM, configura `agents.defaults.models["provider/model"].params.chat_template_kwargs`. El Plugin de vLLM incluido envía automáticamente `enable_thinking: false` y `force_nonempty_content: true` para `vllm/nemotron-3-*` cuando el nivel de razonamiento de la sesión está desactivado.
  * Para modelos locales lentos o hosts LAN/tailnet remotos, configura `models.providers.<id>.timeoutSeconds`. Esto amplía el manejo de solicitudes HTTP del modelo del proveedor, incluyendo conexión, encabezados, streaming del cuerpo y la cancelación total de fetch protegido, sin aumentar el tiempo de espera de todo el runtime del agente.
  * Las llamadas HTTP del proveedor de modelos permiten respuestas DNS de IP falsa de Surge, Clash y sing-box en `198.18.0.0/15` y `fc00::/7` solo para el nombre de host `baseUrl` del proveedor configurado. Otros destinos privados, loopback, link-local y de metadatos siguen requiriendo una habilitación explícita con `models.providers.<id>.request.allowPrivateNetwork: true`.
  * Si `baseUrl` está vacío/se omite, OpenClaw mantiene el comportamiento predeterminado de OpenAI (que resuelve a `api.openai.com`).
  * Por seguridad, un `compat.supportsDeveloperRole: true` explícito se sigue sobrescribiendo en endpoints `openai-completions` no nativos.
  * Para `api: "anthropic-messages"` en endpoints no directos (cualquier proveedor que no sea el `anthropic` canónico, o un `models.providers.anthropic.baseUrl` personalizado cuyo host no sea un endpoint público de `api.anthropic.com`), OpenClaw suprime encabezados beta implícitos de Anthropic como `claude-code-20250219`, `interleaved-thinking-2025-05-14` y marcadores OAuth, para que los proxies personalizados compatibles con Anthropic no rechacen flags beta no compatibles. Configura `models.providers.<id>.headers["anthropic-beta"]` explícitamente si tu proxy necesita funciones beta específicas.


## Ejemplos de CLI

bashCopy code
[code]
    openclaw onboard --auth-choice opencode-zenopenclaw models set opencode/claude-opus-4-6openclaw models list
[/code]

Consulta también: [Configuración](</es/gateway/configuration>) para ejemplos completos de configuración.

## Relacionado

  * [Referencia de configuración](</es/gateway/config-agents#agent-defaults>) \- claves de configuración de modelo
  * [Conmutación por error de modelos](</es/concepts/model-failover>) \- cadenas de respaldo y comportamiento de reintentos
  * [Modelos](</es/concepts/models>) \- configuración de modelos y alias
  * [Proveedores](</es/providers>) \- guías de configuración por proveedor


Was this useful?YesNo