---
title: Creación de plugins de proveedor
source_url: https://docs.openclaw.ai/es/plugins/sdk-provider-plugins
scraped_at: 2026-05-25
---

Esta guía explica cómo crear un plugin proveedor que agrega un proveedor de modelos (LLM) a OpenClaw. Al final tendrás un proveedor con un catálogo de modelos, autenticación con clave de API y resolución dinámica de modelos.

## Tutorial

* ### Package and manifest

### Paso 1: Paquete y manifiesto

package.jsonCopy code
[code]
    {"name": "@myorg/openclaw-acme-ai","version": "1.0.0","type": "module","openclaw": {  "extensions": ["./index.ts"],  "providers": ["acme-ai"],  "compat": {    "pluginApi": ">=2026.3.24-beta.2",    "minGatewayVersion": "2026.3.24-beta.2"  },  "build": {    "openclawVersion": "2026.3.24-beta.2",    "pluginSdkVersion": "2026.3.24-beta.2"  }}}
[/code]

openclaw.plugin.jsonCopy code
[code]
    {"id": "acme-ai","name": "Acme AI","description": "Acme AI model provider","providers": ["acme-ai"],"modelSupport": {  "modelPrefixes": ["acme-"]},"providerAuthEnvVars": {  "acme-ai": ["ACME_AI_API_KEY"]},"providerAuthAliases": {  "acme-ai-coding": "acme-ai"},"providerAuthChoices": [  {    "provider": "acme-ai",    "method": "api-key",    "choiceId": "acme-ai-api-key",    "choiceLabel": "Acme AI API key",    "groupId": "acme-ai",    "groupLabel": "Acme AI",    "cliFlag": "--acme-ai-api-key",    "cliOption": "--acme-ai-api-key <key>",    "cliDescription": "Acme AI API key"  }],"configSchema": {  "type": "object",  "additionalProperties": false}}
[/code]

El manifiesto declara `providerAuthEnvVars` para que OpenClaw pueda detectar credenciales sin cargar el runtime de tu plugin. Agrega `providerAuthAliases` cuando una variante de proveedor deba reutilizar la autenticación del id de otro proveedor. `modelSupport` es opcional y permite que OpenClaw cargue automáticamente tu plugin proveedor a partir de ids de modelo abreviados como `acme-large` antes de que existan hooks de runtime. Si publicas el proveedor en ClawHub, esos campos `openclaw.compat` y `openclaw.build` son obligatorios en `package.json`.

* ### Register the provider

Un proveedor de texto mínimo necesita un `id`, `label`, `auth` y `catalog`. `catalog` es el hook de runtime/configuración propio del proveedor; puede llamar a APIs en vivo del proveedor y devuelve entradas de `models.providers`.

index.tsCopy code
[code]
    import { definePluginEntry } from "openclaw/plugin-sdk/plugin-entry";import { createProviderApiKeyAuthMethod } from "openclaw/plugin-sdk/provider-auth"; export default definePluginEntry({  id: "acme-ai",  name: "Acme AI",  description: "Acme AI model provider",  register(api) {    api.registerProvider({      id: "acme-ai",      label: "Acme AI",      docsPath: "/providers/acme-ai",      envVars: ["ACME_AI_API_KEY"],       auth: [        createProviderApiKeyAuthMethod({          providerId: "acme-ai",          methodId: "api-key",          label: "Acme AI API key",          hint: "API key from your Acme AI dashboard",          optionKey: "acmeAiApiKey",          flagName: "--acme-ai-api-key",          envVar: "ACME_AI_API_KEY",          promptMessage: "Enter your Acme AI API key",          defaultModel: "acme-ai/acme-large",        }),      ],       catalog: {        order: "simple",        run: async (ctx) => {          const apiKey =            ctx.resolveProviderApiKey("acme-ai").apiKey;          if (!apiKey) return null;          return {            provider: {              baseUrl: "https://api.acme-ai.com/v1",              apiKey,              api: "openai-completions",              models: [                {                  id: "acme-large",                  name: "Acme Large",                  reasoning: true,                  input: ["text", "image"],                  cost: { input: 3, output: 15, cacheRead: 0.3, cacheWrite: 3.75 },                  contextWindow: 200000,                  maxTokens: 32768,                },                {                  id: "acme-small",                  name: "Acme Small",                  reasoning: false,                  input: ["text"],                  cost: { input: 1, output: 5, cacheRead: 0.1, cacheWrite: 1.25 },                  contextWindow: 128000,                  maxTokens: 8192,                },              ],            },          };        },      },    });     api.registerModelCatalogProvider({      provider: "acme-ai",      kinds: ["text"],      liveCatalog: async (ctx) => {        const apiKey = ctx.resolveProviderApiKey("acme-ai").apiKey;        if (!apiKey) return null;        return [          {            kind: "text",            provider: "acme-ai",            model: "acme-large",            label: "Acme Large",            source: "live",          },        ];      },    });  },});
[/code]

`registerModelCatalogProvider` es la superficie de catálogo de plano de control más reciente para interfaces de lista/ayuda/selector. Úsala para filas de texto, generación de imágenes, generación de video y generación de música. Mantén las llamadas a endpoints del proveedor y el mapeo de respuestas en el plugin; OpenClaw controla la forma de fila compartida, las etiquetas de origen y el renderizado de ayuda.

Este es un proveedor funcional. Ahora los usuarios pueden ejecutar `openclaw onboard --acme-ai-api-key <key>` y seleccionar `acme-ai/acme-large` como su modelo.

Si el proveedor upstream usa tokens de control distintos a los de OpenClaw, agrega una pequeña transformación de texto bidireccional en lugar de reemplazar la ruta de streaming:

typescriptCopy code
[code]
    api.registerTextTransforms({  input: [    { from: /red basket/g, to: "blue basket" },    { from: /paper ticket/g, to: "digital ticket" },    { from: /left shelf/g, to: "right shelf" },  ],  output: [    { from: /blue basket/g, to: "red basket" },    { from: /digital ticket/g, to: "paper ticket" },    { from: /right shelf/g, to: "left shelf" },  ],});
[/code]

`input` reescribe el prompt de sistema final y el contenido de mensajes de texto antes del transporte. `output` reescribe los deltas de texto del asistente y el texto final antes de que OpenClaw analice sus propios marcadores de control o la entrega del canal.

Para proveedores incluidos que solo registran un proveedor de texto con autenticación por clave de API más un único runtime respaldado por catálogo, prefiere el helper más específico `defineSingleProviderPluginEntry(...)`:

typescriptCopy code
[code]
    import { defineSingleProviderPluginEntry } from "openclaw/plugin-sdk/provider-entry"; export default defineSingleProviderPluginEntry({  id: "acme-ai",  name: "Acme AI",  description: "Acme AI model provider",  provider: {    label: "Acme AI",    docsPath: "/providers/acme-ai",    auth: [      {        methodId: "api-key",        label: "Acme AI API key",        hint: "API key from your Acme AI dashboard",        optionKey: "acmeAiApiKey",        flagName: "--acme-ai-api-key",        envVar: "ACME_AI_API_KEY",        promptMessage: "Enter your Acme AI API key",        defaultModel: "acme-ai/acme-large",      },    ],    catalog: {      buildProvider: () => ({        api: "openai-completions",        baseUrl: "https://api.acme-ai.com/v1",        models: [{ id: "acme-large", name: "Acme Large" }],      }),      buildStaticProvider: () => ({        api: "openai-completions",        baseUrl: "https://api.acme-ai.com/v1",        models: [{ id: "acme-large", name: "Acme Large" }],      }),    },  },});
[/code]

`buildProvider` es la ruta de catálogo en vivo que se usa cuando OpenClaw puede resolver la autenticación real del proveedor. Puede realizar descubrimiento específico del proveedor. Usa `buildStaticProvider` solo para filas offline que sean seguras de mostrar antes de configurar la autenticación; no debe requerir credenciales ni hacer solicitudes de red. La pantalla actual de `models list --all` de OpenClaw ejecuta catálogos estáticos solo para plugins proveedores incluidos, con configuración vacía, entorno vacío y sin rutas de agente/espacio de trabajo.

Si tu flujo de autenticación también necesita parchear `models.providers.*`, alias y el modelo predeterminado del agente durante el onboarding, usa los helpers de preset de `openclaw/plugin-sdk/provider-onboard`. Los helpers más específicos son `createDefaultModelPresetAppliers(...)`, `createDefaultModelsPresetAppliers(...)` y `createModelCatalogPresetAppliers(...)`.

Cuando el endpoint nativo de un proveedor admite bloques de uso en streaming en el transporte normal `openai-completions`, prefiere los helpers de catálogo compartidos en `openclaw/plugin-sdk/provider-catalog-shared` en lugar de codificar comprobaciones de id de proveedor. `supportsNativeStreamingUsageCompat(...)` y `applyProviderNativeStreamingUsageCompat(...)` detectan el soporte desde el mapa de capacidades del endpoint, por lo que endpoints nativos estilo Moonshot/DashScope siguen optando por participar aunque un plugin use un id de proveedor personalizado.

* ### Add dynamic model resolution

Si tu proveedor acepta IDs de modelo arbitrarios (como un proxy o router), agrega `resolveDynamicModel`:

typescriptCopy code
[code]
    api.registerProvider({  // ... id, label, auth, catalog from above   resolveDynamicModel: (ctx) => ({    id: ctx.modelId,    name: ctx.modelId,    provider: "acme-ai",    api: "openai-completions",    baseUrl: "https://api.acme-ai.com/v1",    reasoning: false,    input: ["text"],    cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },    contextWindow: 128000,    maxTokens: 8192,  }),});
[/code]

Si la resolución requiere una llamada de red, usa `prepareDynamicModel` para el calentamiento asíncrono; `resolveDynamicModel` se ejecuta de nuevo después de que termine.

* ### Add runtime hooks (as needed)

La mayoría de los proveedores solo necesitan `catalog` \+ `resolveDynamicModel`. Agrega hooks incrementalmente a medida que tu proveedor los requiera.

Los builders de helpers compartidos ahora cubren las familias de replay/compatibilidad de herramientas más comunes, por lo que los plugins normalmente no necesitan conectar cada hook manualmente uno por uno:

typescriptCopy code
[code]
    import { buildProviderReplayFamilyHooks } from "openclaw/plugin-sdk/provider-model-shared";import { buildProviderStreamFamilyHooks } from "openclaw/plugin-sdk/provider-stream";import { buildProviderToolCompatFamilyHooks } from "openclaw/plugin-sdk/provider-tools"; const GOOGLE_FAMILY_HOOKS = {  ...buildProviderReplayFamilyHooks({ family: "google-gemini" }),  ...buildProviderStreamFamilyHooks("google-thinking"),  ...buildProviderToolCompatFamilyHooks("gemini"),}; api.registerProvider({  id: "acme-gemini-compatible",  // ...  ...GOOGLE_FAMILY_HOOKS,});
[/code]

Familias de replay disponibles hoy:

Familia | Lo que integra | Ejemplos incluidos  
---|---|---  
`openai-compatible` | Política compartida de reproducción al estilo de OpenAI para transportes compatibles con OpenAI, incluida la limpieza de identificadores de llamadas a herramientas, correcciones del orden con el asistente primero y validación genérica de turnos de Gemini cuando el transporte la necesita | `moonshot`, `ollama`, `xai`, `zai`  
`anthropic-by-model` | Política de reproducción consciente de Claude elegida por `modelId`, de modo que los transportes de mensajes de Anthropic solo reciben limpieza de bloques de pensamiento específica de Claude cuando el modelo resuelto es realmente un id de Claude | `amazon-bedrock`, `anthropic-vertex`  
`google-gemini` | Política de reproducción nativa de Gemini más limpieza de reproducción de arranque y modo de salida de razonamiento etiquetada | `google`, `google-gemini-cli`  
`passthrough-gemini` | Limpieza de firmas de pensamiento de Gemini para modelos Gemini que se ejecutan mediante transportes proxy compatibles con OpenAI; no habilita validación de reproducción nativa de Gemini ni reescrituras de arranque | `openrouter`, `kilocode`, `opencode`, `opencode-go`  
`hybrid-anthropic-openai` | Política híbrida para proveedores que mezclan superficies de modelos de mensajes de Anthropic y compatibles con OpenAI en un plugin; la eliminación opcional de bloques de pensamiento solo para Claude permanece acotada al lado de Anthropic | `minimax`  
  
Familias de transmisión disponibles actualmente:

Familia | Lo que integra | Ejemplos incluidos  
---|---|---  
`google-thinking` | Normalización de cargas útiles de pensamiento de Gemini en la ruta de transmisión compartida | `google`, `google-gemini-cli`  
`kilocode-thinking` | Envoltorio de razonamiento de Kilo en la ruta de transmisión proxy compartida, con `kilo/auto` y los identificadores de razonamiento proxy no compatibles omitiendo el pensamiento inyectado | `kilocode`  
`moonshot-thinking` | Asignación de carga útil de pensamiento nativo binario de Moonshot desde la configuración + nivel `/think` | `moonshot`  
`minimax-fast-mode` | Reescritura del modelo de modo rápido de MiniMax en la ruta de transmisión compartida | `minimax`, `minimax-portal`  
`openai-responses-defaults` | Envoltorios compartidos nativos de Responses de OpenAI/Codex: encabezados de atribución, `/fast`/`serviceTier`, verbosidad del texto, búsqueda web nativa de Codex, conformación de cargas útiles de compatibilidad de razonamiento y gestión de contexto de Responses | `openai`, `openai-codex`  
`openrouter-thinking` | Envoltorio de razonamiento de OpenRouter para rutas proxy, con omisiones de modelos no compatibles/`auto` gestionadas centralmente | `openrouter`  
`tool-stream-default-on` | Envoltorio `tool_stream` activado de forma predeterminada para proveedores como [Z.AI](<http://Z.AI>) que quieren transmisión de herramientas salvo que se desactive explícitamente | `zai`  
Puntos de extensión del SDK que impulsan los constructores de familias

Cada constructor de familia se compone de funciones auxiliares públicas de menor nivel exportadas desde el mismo paquete, a las que puedes recurrir cuando un proveedor necesita apartarse del patrón común:

  * `openclaw/plugin-sdk/provider-model-shared` \- `ProviderReplayFamily`, `buildProviderReplayFamilyHooks(...)` y los constructores de reproducción sin procesar (`buildOpenAICompatibleReplayPolicy`, `buildAnthropicReplayPolicyForModel`, `buildGoogleGeminiReplayPolicy`, `buildHybridAnthropicOrOpenAIReplayPolicy`). También exporta funciones auxiliares de reproducción de Gemini (`sanitizeGoogleGeminiReplayHistory`, `resolveTaggedReasoningOutputMode`) y funciones auxiliares de punto de conexión/modelo (`resolveProviderEndpoint`, `normalizeProviderId`, `normalizeGooglePreviewModelId`).
  * `openclaw/plugin-sdk/provider-stream` \- `ProviderStreamFamily`, `buildProviderStreamFamilyHooks(...)`, `composeProviderStreamWrappers(...)`, además de los envoltorios compartidos de OpenAI/Codex (`createOpenAIAttributionHeadersWrapper`, `createOpenAIFastModeWrapper`, `createOpenAIServiceTierWrapper`, `createOpenAIResponsesContextManagementWrapper`, `createCodexNativeWebSearchWrapper`), el envoltorio compatible con OpenAI de DeepSeek V4 (`createDeepSeekV4OpenAICompatibleThinkingWrapper`), la limpieza de prellenado de pensamiento de Anthropic Messages (`createAnthropicThinkingPrefillPayloadWrapper`) y los envoltorios compartidos de proxy/proveedor (`createOpenRouterWrapper`, `createToolStreamWrapper`, `createMinimaxFastModeWrapper`).
  * `openclaw/plugin-sdk/provider-tools` \- `ProviderToolCompatFamily`, `buildProviderToolCompatFamilyHooks("gemini")` y las funciones auxiliares subyacentes de esquemas de Gemini (`normalizeGeminiToolSchemas`, `inspectGeminiToolSchemas`).


Algunas funciones auxiliares de transmisión permanecen locales al proveedor a propósito. `@openclaw/anthropic-provider` mantiene `wrapAnthropicProviderStream`, `resolveAnthropicBetas`, `resolveAnthropicFastMode`, `resolveAnthropicServiceTier` y los constructores de envoltorios de Anthropic de menor nivel en su propio punto de extensión público `api.ts` / `contract-api.ts` porque codifican el manejo de betas de OAuth de Claude y el control de `context1m`. De manera similar, el plugin xAI mantiene la conformación nativa de Responses de xAI en su propio `wrapStreamFn` (alias de `/fast`, `tool_stream` predeterminado, limpieza de herramientas estrictas no compatibles, eliminación de cargas útiles de razonamiento específica de xAI).

El mismo patrón de raíz de paquete también respalda `@openclaw/openai-provider` (constructores de proveedor, funciones auxiliares de modelo predeterminado, constructores de proveedor en tiempo real) y `@openclaw/openrouter-provider` (constructor de proveedor más funciones auxiliares de incorporación/configuración).

### Intercambio de tokens

Para proveedores que necesitan un intercambio de tokens antes de cada llamada de inferencia:

typescriptCopy code
[code]
    prepareRuntimeAuth: async (ctx) => {  const exchanged = await exchangeToken(ctx.apiKey);  return {    apiKey: exchanged.token,    baseUrl: exchanged.baseUrl,    expiresAt: exchanged.expiresAt,  };},
[/code]

### Encabezados personalizados

Para proveedores que necesitan encabezados de solicitud personalizados o modificaciones del cuerpo:

typescriptCopy code
[code]
    // wrapStreamFn returns a StreamFn derived from ctx.streamFnwrapStreamFn: (ctx) => {  if (!ctx.streamFn) return undefined;  const inner = ctx.streamFn;  return async (params) => {    params.headers = {      ...params.headers,      "X-Acme-Version": "2",    };    return inner(params);  };},
[/code]

### Identidad de transporte nativa

Para proveedores que necesitan encabezados nativos de solicitud/sesión o metadatos en transportes genéricos HTTP o WebSocket:

typescriptCopy code
[code]
    resolveTransportTurnState: (ctx) => ({  headers: {    "x-request-id": ctx.turnId,  },  metadata: {    session_id: ctx.sessionId ?? "",    turn_id: ctx.turnId,  },}),resolveWebSocketSessionPolicy: (ctx) => ({  headers: {    "x-session-id": ctx.sessionId ?? "",  },  degradeCooldownMs: 60_000,}),
[/code]

### Uso y facturación

Para proveedores que exponen datos de uso/facturación:

typescriptCopy code
[code]
    resolveUsageAuth: async (ctx) => {  const auth = await ctx.resolveOAuthToken();  return auth ? { token: auth.token } : null;},fetchUsageSnapshot: async (ctx) => {  return await fetchAcmeUsage(ctx.token, ctx.timeoutMs);},
[/code]

Todos los puntos de extensión de proveedor disponibles

OpenClaw llama a los puntos de extensión en este orden. La mayoría de los proveedores solo usan 2 o 3: Los campos de proveedor solo para compatibilidad que OpenClaw ya no invoca, como `ProviderPlugin.capabilities` y `suppressBuiltInModel`, no se enumeran aquí.

# | Punto de extensión | Cuándo usarlo  
---|---|---  
1 | `catalog` | Catálogo de modelos o valores predeterminados de URL base  
2 | `applyConfigDefaults` | Valores predeterminados globales propios del proveedor durante la materialización de la configuración  
3 | `normalizeModelId` | Limpieza de alias de id de modelo heredado/vista previa antes de la búsqueda  
4 | `normalizeTransport` | Limpieza de `api` / `baseUrl` de familia de proveedor antes del ensamblado genérico del modelo  
5 | `normalizeConfig` | Normalizar la configuración `models.providers.<id>`  
6 | `applyNativeStreamingUsageCompat` | Reescrituras de compatibilidad de uso de transmisión nativa para proveedores de configuración  
7 | `resolveConfigApiKey` | Resolución de autenticación con marcador de entorno propia del proveedor  
8 | `resolveSyntheticAuth` | Autenticación sintética local/autohospedada o respaldada por configuración  
9 | `shouldDeferSyntheticProfileAuth` | Relegar los marcadores de posición sintéticos de perfiles almacenados por detrás de la autenticación de entorno/configuración  
10 | `resolveDynamicModel` | Aceptar IDs de modelo de origen arbitrarios  
11 | `prepareDynamicModel` | Obtención asíncrona de metadatos antes de resolver  
12 | `normalizeResolvedModel` | Reescrituras de transporte antes del ejecutor  
13 | `contributeResolvedModelCompat` | Indicadores de compatibilidad para modelos de proveedor detrás de otro transporte compatible  
14 | `normalizeToolSchemas` | Limpieza de esquemas de herramientas propia del proveedor antes del registro  
15 | `inspectToolSchemas` | Diagnósticos de esquemas de herramientas propios del proveedor  
16 | `resolveReasoningOutputMode` | Contrato de salida de razonamiento etiquetada frente a nativa  
17 | `prepareExtraParams` | Parámetros de solicitud predeterminados  
18 | `createStreamFn` | Transporte StreamFn totalmente personalizado  
19 | `wrapStreamFn` | Envoltorios personalizados de encabezados/cuerpo en la ruta de transmisión normal  
20 | `resolveTransportTurnState` | Encabezados/metadatos nativos por turno  
21 | `resolveWebSocketSessionPolicy` | Encabezados nativos de sesión WS/periodo de enfriamiento  
22 | `formatApiKey` | Forma de token de tiempo de ejecución personalizada  
23 | `refreshOAuth` | Actualización OAuth personalizada  
24 | `buildAuthDoctorHint` | Guía de reparación de autenticación  
25 | `matchesContextOverflowError` | Detección de desbordamiento propia del proveedor  
26 | `classifyFailoverReason` | Clasificación de límite de tasa/sobrecarga propia del proveedor  
27 | `isCacheTtlEligible` | Control de TTL de caché de indicaciones  
28 | `buildMissingAuthMessage` | Sugerencia personalizada para autenticación ausente  
29 | `augmentModelCatalog` | Filas sintéticas de compatibilidad futura  
30 | `resolveThinkingProfile` | Conjunto de opciones `/think` específico del modelo  
31 | `isBinaryThinking` | Compatibilidad de pensamiento binario activado/desactivado  
32 | `supportsXHighThinking` | Compatibilidad de soporte de razonamiento `xhigh`  
33 | `resolveDefaultThinkingLevel` | Compatibilidad de política `/think` predeterminada  
34 | `isModernModelRef` | Coincidencia de modelos en vivo/de prueba de humo  
35 | `prepareRuntimeAuth` | Intercambio de tokens antes de la inferencia  
36 | `resolveUsageAuth` | Análisis de credenciales de uso personalizadas  
37 | `fetchUsageSnapshot` | Punto de conexión de uso personalizado  
38 | `createEmbeddingProvider` | Adaptador de incrustaciones propio del proveedor para memoria/búsqueda  
39 | `buildReplayPolicy` | Política personalizada de reproducción/Compaction de transcripción  
40 | `sanitizeReplayHistory` | Reescrituras de reproducción específicas del proveedor después de la limpieza genérica  
41 | `validateReplayTurns` | Validación estricta de turnos de reproducción antes del ejecutor integrado  
42 | `onModelSelected` | Devolución de llamada posterior a la selección (p. ej., telemetría)  
  
Notas de alternativa en tiempo de ejecución:

  * `normalizeConfig` comprueba primero el proveedor coincidente y luego otros plugins de proveedor con capacidad de puntos de extensión hasta que uno cambia realmente la configuración. Si ningún punto de extensión de proveedor reescribe una entrada de configuración compatible de la familia Google, el normalizador de configuración de Google incluido aún se aplica.
  * `resolveConfigApiKey` usa el punto de extensión del proveedor cuando está expuesto. La ruta incluida de `amazon-bedrock` también tiene aquí un resolutor integrado de marcadores de entorno de AWS, aunque la autenticación en tiempo de ejecución de Bedrock en sí aún usa la cadena predeterminada del AWS SDK.
  * `resolveSystemPromptContribution` permite que un proveedor inyecte guía de indicación del sistema consciente de la caché para una familia de modelos. Prefiérelo sobre `before_prompt_build` cuando el comportamiento pertenece a un proveedor/familia de modelos y debe preservar la división de caché estable/dinámica.


Para ver descripciones detalladas y ejemplos del mundo real, consulta [Detalles internos: puntos de extensión de tiempo de ejecución de proveedores](</es/plugins/architecture-internals#provider-runtime-hooks>).

* ### Agregar capacidades adicionales (opcional)

### Paso 5: Agregar capacidades adicionales

Un plugin de proveedor puede registrar voz, transcripción en tiempo real, voz en tiempo real, comprensión de medios, generación de imágenes, generación de video, obtención web y búsqueda web junto con inferencia de texto. OpenClaw clasifica esto como un plugin de **capacidad híbrida** , el patrón recomendado para plugins de empresa (un plugin por proveedor). Consulta [Internals: Capability Ownership](</es/plugins/architecture#capability-ownership-model>).

Registra cada capacidad dentro de `register(api)` junto con tu llamada existente a `api.registerProvider(...)`. Elige solo las pestañas que necesitas:

### Speech (TTS)

typescriptCopy code
[code]
    import {  assertOkOrThrowProviderError,  postJsonRequest,} from "openclaw/plugin-sdk/provider-http"; api.registerSpeechProvider({  id: "acme-ai",  label: "Acme Speech",  isConfigured: ({ config }) => Boolean(config.messages?.tts),  synthesize: async (req) => {    const { response, release } = await postJsonRequest({      url: "https://api.example.com/v1/speech",      headers: new Headers({ "Content-Type": "application/json" }),      body: { text: req.text },      timeoutMs: req.timeoutMs,      fetchFn: fetch,      auditContext: "acme speech",    });    try {      await assertOkOrThrowProviderError(response, "Acme Speech API error");      return {        audioBuffer: Buffer.from(await response.arrayBuffer()),        outputFormat: "mp3",        fileExtension: ".mp3",        voiceCompatible: false,      };    } finally {      await release();    }  },});
[/code]

Usa `assertOkOrThrowProviderError(...)` para errores HTTP del proveedor, de modo que los plugins compartan lecturas acotadas del cuerpo de error, análisis de errores JSON y sufijos de id. de solicitud.

### Realtime transcription

Prefiere `createRealtimeTranscriptionWebSocketSession(...)`: el asistente compartido gestiona la captura de proxy, el retroceso de reconexión, el vaciado al cerrar, los handshakes de preparación, la cola de audio y los diagnósticos de eventos de cierre. Tu plugin solo asigna los eventos del servicio upstream.

typescriptCopy code
[code]
    api.registerRealtimeTranscriptionProvider({  id: "acme-ai",  label: "Acme Realtime Transcription",  isConfigured: () => true,  createSession: (req) => {    const apiKey = String(req.providerConfig.apiKey ?? "");    return createRealtimeTranscriptionWebSocketSession({      providerId: "acme-ai",      callbacks: req,      url: "wss://api.example.com/v1/realtime-transcription",      headers: { Authorization: `Bearer ${apiKey}` },      onMessage: (event, transport) => {        if (event.type === "session.created") {          transport.sendJson({ type: "session.update" });          transport.markReady();          return;        }        if (event.type === "transcript.final") {          req.onTranscript?.(event.text);        }      },      sendAudio: (audio, transport) => {        transport.sendJson({          type: "audio.append",          audio: audio.toString("base64"),        });      },      onClose: (transport) => {        transport.sendJson({ type: "audio.end" });      },    });  },});
[/code]

Los proveedores STT por lotes que hacen POST de audio multipart deben usar `buildAudioTranscriptionFormData(...)` de `openclaw/plugin-sdk/provider-http`. El asistente normaliza los nombres de archivo de subida, incluidas las subidas AAC que necesitan un nombre de archivo estilo M4A para APIs de transcripción compatibles.

### Realtime voice

typescriptCopy code
[code]
    api.registerRealtimeVoiceProvider({  id: "acme-ai",  label: "Acme Realtime Voice",  capabilities: {    transports: ["gateway-relay"],    inputAudioFormats: [{ encoding: "pcm16", sampleRateHz: 24000, channels: 1 }],    outputAudioFormats: [{ encoding: "pcm16", sampleRateHz: 24000, channels: 1 }],    supportsBargeIn: true,    supportsToolCalls: true,  },  isConfigured: ({ providerConfig }) => Boolean(providerConfig.apiKey),  createBridge: (req) => ({    // Set this only if the provider accepts multiple tool responses for    // one call, for example an immediate "working" response followed by    // the final result.    supportsToolResultContinuation: false,    connect: async () => {},    sendAudio: () => {},    setMediaTimestamp: () => {},    handleBargeIn: () => {},    submitToolResult: () => {},    acknowledgeMark: () => {},    close: () => {},    isConnected: () => true,  }),});
[/code]

Declara `capabilities` para que `talk.catalog` pueda exponer modos, transportes, formatos de audio y marcas de características válidos a clientes Talk de navegador y nativos. Implementa `handleBargeIn` cuando un transporte pueda detectar que una persona está interrumpiendo la reproducción del asistente y el proveedor admita truncar o borrar la respuesta de audio activa.

### Media understanding

typescriptCopy code
[code]
    api.registerMediaUnderstandingProvider({  id: "acme-ai",  capabilities: ["image", "audio"],  describeImage: async (req) => ({ text: "A photo of..." }),  transcribeAudio: async (req) => ({ text: "Transcript..." }),});
[/code]

### Image and video generation

Las capacidades de video usan una forma **consciente del modo** : `generate`, `imageToVideo` y `videoToVideo`. Los campos agregados planos como `maxInputImages` / `maxInputVideos` / `maxDurationSeconds` no bastan para anunciar compatibilidad con modos de transformación o modos deshabilitados de forma clara. La generación de música sigue el mismo patrón con bloques explícitos `generate` / `edit`.

typescriptCopy code
[code]
    api.registerImageGenerationProvider({  id: "acme-ai",  label: "Acme Images",  generate: async (req) => ({ /* image result */ }),}); api.registerVideoGenerationProvider({  id: "acme-ai",  label: "Acme Video",  capabilities: {    generate: { maxVideos: 1, maxDurationSeconds: 10, supportsResolution: true },    imageToVideo: {      enabled: true,      maxVideos: 1,      maxInputImages: 1,      maxInputImagesByModel: { "acme/reference-to-video": 9 },      maxDurationSeconds: 5,    },    videoToVideo: { enabled: false },  },  generateVideo: async (req) => ({ videos: [] }),});
[/code]

### Web fetch and search

typescriptCopy code
[code]
    api.registerWebFetchProvider({  id: "acme-ai-fetch",  label: "Acme Fetch",  hint: "Fetch pages through Acme's rendering backend.",  envVars: ["ACME_FETCH_API_KEY"],  placeholder: "acme-...",  signupUrl: "https://acme.example.com/fetch",  credentialPath: "plugins.entries.acme.config.webFetch.apiKey",  getCredentialValue: (fetchConfig) => fetchConfig?.acme?.apiKey,  setCredentialValue: (fetchConfigTarget, value) => {    const acme = (fetchConfigTarget.acme ??= {});    acme.apiKey = value;  },  createTool: () => ({    description: "Fetch a page through Acme Fetch.",    parameters: {},    execute: async (args) => ({ content: [] }),  }),}); api.registerWebSearchProvider({  id: "acme-ai-search",  label: "Acme Search",  search: async (req) => ({ content: [] }),});
[/code]

* ### Test

### Paso 6: Probar

src/provider.test.tsCopy code
[code]
    import { describe, it, expect } from "vitest";// Export your provider config object from index.ts or a dedicated fileimport { acmeProvider } from "./provider.js"; describe("acme-ai provider", () => {  it("resolves dynamic models", () => {    const model = acmeProvider.resolveDynamicModel!({      modelId: "acme-beta-v3",    } as any);    expect(model.id).toBe("acme-beta-v3");    expect(model.provider).toBe("acme-ai");  });   it("returns catalog when key is available", async () => {    const result = await acmeProvider.catalog!.run({      resolveProviderApiKey: () => ({ apiKey: "test-key" }),    } as any);    expect(result?.provider?.models).toHaveLength(2);  });   it("returns null catalog when no key", async () => {    const result = await acmeProvider.catalog!.run({      resolveProviderApiKey: () => ({ apiKey: undefined }),    } as any);    expect(result).toBeNull();  });});
[/code]

## Publicar en ClawHub

Los plugins de proveedor se publican de la misma forma que cualquier otro plugin de código externo:

bashCopy code
[code]
    clawhub package publish your-org/your-plugin --dry-runclawhub package publish your-org/your-plugin
[/code]

No uses aquí el alias de publicación heredado solo para skills; los paquetes de plugin deben usar `clawhub package publish`.

## Estructura de archivos

CodeCopy code
[code]
    <bundled-plugin-root>/acme-ai/├── package.json              # openclaw.providers metadata├── openclaw.plugin.json      # Manifest with provider auth metadata├── index.ts                  # definePluginEntry + registerProvider└── src/    ├── provider.test.ts      # Tests    └── usage.ts              # Usage endpoint (optional)
[/code]

## Referencia del orden del catálogo

`catalog.order` controla cuándo se fusiona tu catálogo en relación con los proveedores integrados:

Orden | Cuándo | Caso de uso  
---|---|---  
`simple` | Primera pasada | Proveedores sencillos con clave API  
`profile` | Después de simple | Proveedores condicionados a perfiles de autenticación  
`paired` | Después de profile | Sintetizar varias entradas relacionadas  
`late` | Última pasada | Anular proveedores existentes (gana en colisiones)  
  
## Próximos pasos

  * [Plugins de canal](</es/plugins/sdk-channel-plugins>) \- si tu plugin también proporciona un canal
  * [Runtime del SDK](</es/plugins/sdk-runtime>) \- asistentes de `api.runtime` (TTS, búsqueda, subagent)
  * [Descripción general del SDK](</es/plugins/sdk-overview>) \- referencia completa de importación de subrutas
  * [Aspectos internos de plugins](</es/plugins/architecture-internals#provider-runtime-hooks>) \- detalles de hooks y ejemplos integrados


## Relacionado

  * [Configuración del SDK de plugins](</es/plugins/sdk-setup>)
  * [Crear plugins](</es/plugins/building-plugins>)
  * [Crear plugins de canal](</es/plugins/sdk-channel-plugins>)


Was this useful?YesNo