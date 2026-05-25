---
title: Ayudantes de tiempo de ejecución de Plugin
source_url: https://docs.openclaw.ai/es/plugins/sdk-runtime
scraped_at: 2026-05-25
---

Referencia para el objeto `api.runtime` inyectado en cada plugin durante el registro. Usa estos helpers en lugar de importar directamente componentes internos del host.

[**Plugins de canales** Guía paso a paso que usa estos helpers en contexto para plugins de canales. ](</es/plugins/sdk-channel-plugins>) [**Plugins de proveedores** Guía paso a paso que usa estos helpers en contexto para plugins de proveedores. ](</es/plugins/sdk-provider-plugins>)

typescriptCopy code
[code]
    register(api) {  const runtime = api.runtime;}
[/code]

## Carga y escrituras de configuración

Prefiere la configuración que ya se pasó a la ruta de llamada activa, por ejemplo `api.config` durante el registro o un argumento `cfg` en callbacks de canal/proveedor. Esto mantiene una instantánea de proceso fluyendo por el trabajo en lugar de volver a analizar la configuración en rutas críticas.

Usa `api.runtime.config.current()` solo cuando un manejador de larga duración necesite la instantánea actual del proceso y no se haya pasado ninguna configuración a esa función. El valor devuelto es de solo lectura; clónalo o usa un helper de mutación antes de editarlo.

Las fábricas de herramientas reciben `ctx.runtimeConfig` además de `ctx.getRuntimeConfig()`. Usa el getter dentro del callback `execute` de una herramienta de larga duración cuando la configuración pueda cambiar después de que se haya creado la definición de la herramienta.

Persiste los cambios con `api.runtime.config.mutateConfigFile(...)` o `api.runtime.config.replaceConfigFile(...)`. Cada escritura debe elegir una política explícita `afterWrite`:

  * `afterWrite: { mode: "auto" }` permite que el planificador de recarga del Gateway decida.
  * `afterWrite: { mode: "restart", reason: "..." }` fuerza un reinicio limpio cuando el escritor sabe que la recarga en caliente no es segura.
  * `afterWrite: { mode: "none", reason: "..." }` suprime la recarga o reinicio automático solo cuando el llamador se hace cargo del seguimiento.


Los helpers de mutación devuelven `afterWrite` además de un resumen tipado `followUp` para que los llamadores puedan registrar o probar si solicitaron un reinicio. El Gateway sigue siendo responsable de cuándo ocurre realmente ese reinicio.

`api.runtime.config.loadConfig()` y `api.runtime.config.writeConfigFile(...)` son helpers de compatibilidad obsoletos bajo `runtime-config-load-write`. Emiten una advertencia una vez en tiempo de ejecución y siguen disponibles para plugins externos antiguos durante la ventana de migración. Los plugins incluidos no deben usarlos; las protecciones del límite de configuración fallan si el código del plugin los llama o importa esos helpers desde subrutas del SDK de plugins.

Para importaciones directas del SDK, usa las subrutas de configuración específicas en lugar del barril de compatibilidad amplio `openclaw/plugin-sdk/config-runtime`: `config-contracts` para tipos, `plugin-config-runtime` para aserciones de configuración ya cargada y búsqueda de entradas de plugin, `runtime-config-snapshot` para instantáneas actuales del proceso, y `config-mutation` para escrituras. Las pruebas de plugins incluidos deben simular directamente estas subrutas específicas en lugar de simular el barril de compatibilidad amplio.

El código interno de tiempo de ejecución de OpenClaw sigue la misma dirección: cargar la configuración una vez en el límite de CLI, Gateway o proceso, y luego pasar ese valor. Las escrituras de mutación correctas actualizan la instantánea de tiempo de ejecución del proceso y avanzan su revisión interna; las cachés de larga duración deben basarse en la clave de caché propiedad del tiempo de ejecución en lugar de serializar la configuración localmente. Los módulos de tiempo de ejecución de larga duración tienen un escáner de tolerancia cero para llamadas ambientales a `loadConfig()`; usa un `cfg` pasado, un `context.getRuntimeConfig()` de solicitud o `getRuntimeConfig()` en un límite de proceso explícito.

Las rutas de ejecución de proveedores y canales deben usar la instantánea activa de configuración de tiempo de ejecución, no una instantánea de archivo devuelta para lectura o edición de configuración. Las instantáneas de archivo preservan valores fuente como marcadores SecretRef para la UI y las escrituras; los callbacks de proveedor necesitan la vista de tiempo de ejecución resuelta. Cuando un helper pueda llamarse con la instantánea fuente activa o con la instantánea de tiempo de ejecución activa, enruta mediante `selectApplicableRuntimeConfig()` antes de leer credenciales.

## Espacios de nombres de tiempo de ejecución

api.runtime.agent

Identidad del agente, directorios y administración de sesiones.

typescriptCopy code
[code]
    // Resolve the agent's working directoryconst agentDir = api.runtime.agent.resolveAgentDir(cfg); // Resolve agent workspaceconst workspaceDir = api.runtime.agent.resolveAgentWorkspaceDir(cfg); // Get agent identityconst identity = api.runtime.agent.resolveAgentIdentity(cfg); // Get default thinking levelconst thinking = api.runtime.agent.resolveThinkingDefault({  cfg,  provider,  model,}); // Validate a user-provided thinking level against the active provider profileconst policy = api.runtime.agent.resolveThinkingPolicy({ provider, model });const level = api.runtime.agent.normalizeThinkingLevel("extra high");if (level && policy.levels.some((entry) => entry.id === level)) {  // pass level to an embedded run} // Get agent timeoutconst timeoutMs = api.runtime.agent.resolveAgentTimeoutMs(cfg); // Ensure workspace existsawait api.runtime.agent.ensureAgentWorkspace(cfg); // Run an embedded agent turnconst agentDir = api.runtime.agent.resolveAgentDir(cfg);const result = await api.runtime.agent.runEmbeddedAgent({  sessionId: "my-plugin:task-1",  runId: crypto.randomUUID(),  sessionFile: path.join(agentDir, "sessions", "my-plugin-task-1.jsonl"),  workspaceDir: api.runtime.agent.resolveAgentWorkspaceDir(cfg),  prompt: "Summarize the latest changes",  timeoutMs: api.runtime.agent.resolveAgentTimeoutMs(cfg),});
[/code]

`runEmbeddedAgent(...)` es el helper neutral para iniciar un turno normal de agente de OpenClaw desde código de plugin. Usa la misma resolución de proveedor/modelo y selección de arnés de agente que las respuestas activadas por canales.

`runEmbeddedPiAgent(...)` permanece como alias de compatibilidad.

`resolveThinkingPolicy(...)` devuelve los niveles de razonamiento admitidos por el proveedor/modelo y el valor predeterminado opcional. Los plugins de proveedor son responsables del perfil específico del modelo mediante sus hooks de razonamiento, por lo que los plugins de herramientas deben llamar a este helper de tiempo de ejecución en lugar de importar o duplicar listas de proveedores.

`normalizeThinkingLevel(...)` convierte texto de usuario como `on`, `x-high` o `extra high` al nivel almacenado canónico antes de comprobarlo contra la política resuelta.

Los **helpers del almacén de sesiones** están bajo `api.runtime.agent.session`:

typescriptCopy code
[code]
    const storePath = api.runtime.agent.session.resolveStorePath(cfg);const store = api.runtime.agent.session.loadSessionStore(storePath);await api.runtime.agent.session.updateSessionStore(storePath, (nextStore) => {  // Patch one entry without replacing the whole file from stale state.  nextStore[sessionKey] = { ...nextStore[sessionKey], thinkingLevel: "high" };});const filePath = api.runtime.agent.session.resolveSessionFilePath(cfg, sessionId);
[/code]

Prefiere `updateSessionStore(...)` o `updateSessionStoreEntry(...)` para escrituras en tiempo de ejecución. Enrutan por el escritor del almacén de sesiones propiedad del Gateway, preservan actualizaciones simultáneas y reutilizan la caché activa. `saveSessionStore(...)` sigue disponible para compatibilidad y reescrituras de estilo mantenimiento sin conexión.

api.runtime.agent.defaults

Constantes de modelo y proveedor predeterminadas:

typescriptCopy code
[code]
    const model = api.runtime.agent.defaults.model; // e.g. "anthropic/claude-sonnet-4-6"const provider = api.runtime.agent.defaults.provider; // e.g. "anthropic"
[/code]

api.runtime.llm

Ejecuta una finalización de texto propiedad del host sin importar componentes internos del proveedor ni duplicar la preparación de modelo/autenticación/URL base de OpenClaw.

typescriptCopy code
[code]
    const result = await api.runtime.llm.complete({  messages: [{ role: "user", content: "Summarize this transcript." }],  purpose: "my-plugin.summary",  maxTokens: 512,  temperature: 0.2,});
[/code]

El helper usa la misma ruta de preparación de finalización simple que el tiempo de ejecución integrado de OpenClaw y la instantánea de configuración de tiempo de ejecución propiedad del host. Los motores de contexto reciben una capacidad `llm.complete` vinculada a la sesión, de modo que las llamadas a modelos usan el agente de la sesión activa y no recurren silenciosamente al agente predeterminado. El resultado incluye atribución de proveedor/modelo/agente además de uso normalizado de tokens, caché y costo estimado cuando esté disponible.

api.runtime.subagent

Inicia y administra ejecuciones de subagentes en segundo plano.

typescriptCopy code
[code]
    // Start a subagent runconst { runId } = await api.runtime.subagent.run({  sessionKey: "agent:main:subagent:search-helper",  message: "Expand this query into focused follow-up searches.",  provider: "openai", // optional override  model: "gpt-4.1-mini", // optional override  deliver: false,}); // Wait for completionconst result = await api.runtime.subagent.waitForRun({ runId, timeoutMs: 30000 }); // Read session messagesconst { messages } = await api.runtime.subagent.getSessionMessages({  sessionKey: "agent:main:subagent:search-helper",  limit: 10,}); // Delete a sessionawait api.runtime.subagent.deleteSession({  sessionKey: "agent:main:subagent:search-helper",});
[/code]

`deleteSession(...)` puede eliminar sesiones creadas por el mismo plugin mediante `api.runtime.subagent.run(...)`. Eliminar sesiones arbitrarias de usuarios u operadores todavía requiere una solicitud de Gateway con alcance de administrador.

api.runtime.nodes

Lista los nodos conectados e invoca un comando alojado en un nodo desde código de plugin cargado por Gateway o desde comandos de CLI del plugin. Usa esto cuando un plugin es responsable de trabajo local en un dispositivo emparejado, por ejemplo un puente de navegador o audio en otra Mac.

typescriptCopy code
[code]
    const { nodes } = await api.runtime.nodes.list({ connected: true }); const result = await api.runtime.nodes.invoke({  nodeId: "mac-studio",  command: "my-plugin.command",  params: { action: "start" },  timeoutMs: 30000,});
[/code]

Dentro del Gateway, este tiempo de ejecución está en proceso. En comandos de CLI del plugin, llama al Gateway configurado mediante RPC, de modo que comandos como `openclaw googlemeet recover-tab` pueden inspeccionar nodos emparejados desde la terminal. Los comandos de Node siguen pasando por el emparejamiento normal de nodos del Gateway, las listas de comandos permitidos, las políticas de invocación de nodos del plugin y el manejo de comandos locales del nodo.

Los plugins que exponen comandos peligrosos alojados en nodos deben registrar una política de invocación de nodos con `api.registerNodeInvokePolicy(...)`. La política se ejecuta en el Gateway después de las comprobaciones de la lista de comandos permitidos y antes de reenviar el comando al nodo, de modo que las llamadas directas a `node.invoke` y las herramientas de plugin de nivel superior comparten la misma ruta de cumplimiento.

api.runtime.tasks.managedFlows

Vincula un tiempo de ejecución de flujo de tareas a una clave de sesión existente de OpenClaw o a un contexto de herramienta de confianza, y luego crea y administra flujos de tareas sin pasar un propietario en cada llamada.

El flujo de tareas rastrea estado duradero de flujos de trabajo de varios pasos. No es un programador: usa Cron o `api.session.workflow.scheduleSessionTurn(...)` para despertares futuros, y luego usa `managedFlows` desde el turno programado cuando ese trabajo necesite estado de flujo, tareas secundarias, esperas o cancelación.

typescriptCopy code
[code]
    const taskFlow = api.runtime.tasks.managedFlows.fromToolContext(ctx); const created = taskFlow.createManaged({  controllerId: "my-plugin/review-batch",  goal: "Review new pull requests",}); const child = taskFlow.runTask({  flowId: created.flowId,  runtime: "acp",  childSessionKey: "agent:main:subagent:reviewer",  task: "Review PR #123",  status: "running",  startedAt: Date.now(),}); const waiting = taskFlow.setWaiting({  flowId: created.flowId,  expectedRevision: created.revision,  currentStep: "await-human-reply",  waitJson: { kind: "reply", channel: "telegram" },});
[/code]

Usa `bindSession({ sessionKey, requesterOrigin })` cuando ya tengas una clave de sesión de OpenClaw de confianza desde tu propia capa de vinculación. No vincules desde la entrada sin procesar del usuario.

api.runtime.tts

Síntesis de texto a voz.

typescriptCopy code
[code]
    // Standard TTSconst clip = await api.runtime.tts.textToSpeech({  text: "Hello from OpenClaw",  cfg: api.config,}); // Telephony-optimized TTSconst telephonyClip = await api.runtime.tts.textToSpeechTelephony({  text: "Hello from OpenClaw",  cfg: api.config,}); // List available voicesconst voices = await api.runtime.tts.listVoices({  provider: "elevenlabs",  cfg: api.config,});
[/code]

Usa la configuración principal `messages.tts` y la selección de proveedor. Devuelve un búfer de audio PCM + frecuencia de muestreo.

api.runtime.mediaUnderstanding

Análisis de imágenes, audio y video.

typescriptCopy code
[code]
    // Describe an imageconst image = await api.runtime.mediaUnderstanding.describeImageFile({  filePath: "/tmp/inbound-photo.jpg",  cfg: api.config,  agentDir: "/tmp/agent",}); // Transcribe audioconst { text } = await api.runtime.mediaUnderstanding.transcribeAudioFile({  filePath: "/tmp/inbound-audio.ogg",  cfg: api.config,  mime: "audio/ogg", // optional, for when MIME cannot be inferred}); // Describe a videoconst video = await api.runtime.mediaUnderstanding.describeVideoFile({  filePath: "/tmp/inbound-video.mp4",  cfg: api.config,}); // Generic file analysisconst result = await api.runtime.mediaUnderstanding.runFile({  filePath: "/tmp/inbound-file.pdf",  cfg: api.config,}); // Structured image extraction through a specific provider/model.// Include at least one image; text inputs are supplemental context.const evidence = await api.runtime.mediaUnderstanding.extractStructuredWithModel({  provider: "codex",  model: "gpt-5.5",  input: [    {      type: "image",      buffer: receiptImageBuffer,      fileName: "receipt.png",      mime: "image/png",    },    { type: "text", text: "Prefer the printed total over handwritten notes." },  ],  instructions: "Extract vendor, total, and searchable tags.",  schemaName: "receipt.evidence",  jsonSchema: {    type: "object",    properties: {      vendor: { type: "string" },      total: { type: "number" },      tags: { type: "array", items: { type: "string" } },    },    required: ["vendor", "total"],  },  cfg: api.config,});
[/code]

Devuelve `{ text: undefined }` cuando no se produce ninguna salida (por ejemplo, entrada omitida).

api.runtime.imageGeneration

Generación de imágenes.

typescriptCopy code
[code]
    const result = await api.runtime.imageGeneration.generate({  prompt: "A robot painting a sunset",  cfg: api.config,}); const providers = api.runtime.imageGeneration.listProviders({ cfg: api.config });
[/code]

api.runtime.webSearch

Búsqueda web.

typescriptCopy code
[code]
    const providers = api.runtime.webSearch.listProviders({ config: api.config }); const result = await api.runtime.webSearch.search({  config: api.config,  args: { query: "OpenClaw plugin SDK", count: 5 },});
[/code]

api.runtime.media

Utilidades multimedia de bajo nivel.

typescriptCopy code
[code]
    const webMedia = await api.runtime.media.loadWebMedia(url);const mime = await api.runtime.media.detectMime(buffer);const kind = api.runtime.media.mediaKindFromMime("image/jpeg"); // "image"const isVoice = api.runtime.media.isVoiceCompatibleAudio(filePath);const metadata = await api.runtime.media.getImageMetadata(filePath);const resized = await api.runtime.media.resizeToJpeg(buffer, { maxWidth: 800 });const terminalQr = await api.runtime.media.renderQrTerminal("https://openclaw.ai");const pngQr = await api.runtime.media.renderQrPngBase64("https://openclaw.ai", {  scale: 6, // 1-12  marginModules: 4, // 0-16});const pngQrDataUrl = await api.runtime.media.renderQrPngDataUrl("https://openclaw.ai");const tmpRoot = resolvePreferredOpenClawTmpDir();const pngQrFile = await api.runtime.media.writeQrPngTempFile("https://openclaw.ai", {  tmpRoot,  dirPrefix: "my-plugin-qr-",  fileName: "qr.png",});
[/code]

api.runtime.config

Instantánea actual de configuración en tiempo de ejecución y escrituras transaccionales de configuración. Prefiere la configuración que ya se pasó a la ruta de llamada activa; usa `current()` solo cuando el controlador necesite directamente la instantánea del proceso.

typescriptCopy code
[code]
    const cfg = api.runtime.config.current();await api.runtime.config.mutateConfigFile({  afterWrite: { mode: "auto" },  mutate(draft) {    draft.plugins ??= {};  },});
[/code]

`mutateConfigFile(...)` y `replaceConfigFile(...)` devuelven un valor `followUp`, por ejemplo `{ mode: "restart", requiresRestart: true, reason }`, que registra la intención del escritor sin quitarle el control de reinicio al gateway.

api.runtime.system

Utilidades de nivel de sistema.

typescriptCopy code
[code]
    await api.runtime.system.enqueueSystemEvent(event);api.runtime.system.requestHeartbeat({  source: "other",  intent: "event",  reason: "plugin-event",});api.runtime.system.requestHeartbeatNow({ reason: "plugin-event" }); // Deprecated compatibility alias.const output = await api.runtime.system.runCommandWithTimeout(cmd, args, opts);const hint = api.runtime.system.formatNativeDependencyHint(pkg);
[/code]

api.runtime.events

Suscripciones a eventos.

typescriptCopy code
[code]
    api.runtime.events.onAgentEvent((event) => {  /* ... */});api.runtime.events.onSessionTranscriptUpdate((update) => {  /* ... */});
[/code]

api.runtime.logging

Registro.

typescriptCopy code
[code]
    const verbose = api.runtime.logging.shouldLogVerbose();const childLogger = api.runtime.logging.getChildLogger({ plugin: "my-plugin" }, { level: "debug" });
[/code]

api.runtime.modelAuth

Resolución de autenticación de modelos y proveedores.

typescriptCopy code
[code]
    const auth = await api.runtime.modelAuth.getApiKeyForModel({ model, cfg });const providerAuth = await api.runtime.modelAuth.resolveApiKeyForProvider({  provider: "openai",  cfg,});
[/code]

api.runtime.state

Resolución del directorio de estado y almacenamiento con claves respaldado por SQLite.

typescriptCopy code
[code]
    const stateDir = api.runtime.state.resolveStateDir(process.env);const store = api.runtime.state.openKeyedStore&lt;MyRecord&gt;({  namespace: "my-feature",  maxEntries: 200,  defaultTtlMs: 15 * 60_000,}); await store.register("key-1", { value: "hello" });const claimed = await store.registerIfAbsent("dedupe-key", { value: "first" });const value = await store.lookup("key-1");await store.consume("key-1");await store.clear();
[/code]

Los almacenes con claves sobreviven a los reinicios y están aislados por el id del plugin vinculado al tiempo de ejecución. Usa `registerIfAbsent(...)` para reclamaciones atómicas de deduplicación: devuelve `true` cuando la clave faltaba o había expirado y se registró, o `false` cuando ya existe un valor activo sin sobrescribir su valor, hora de creación ni TTL. Límites: `maxEntries` por espacio de nombres, 1000 filas activas por plugin, valores JSON de menos de 64 KB y vencimiento TTL opcional.

api.runtime.tools

Fábricas de herramientas de memoria y CLI.

typescriptCopy code
[code]
    const getTool = api.runtime.tools.createMemoryGetTool(/* ... */);const searchTool = api.runtime.tools.createMemorySearchTool(/* ... */);api.runtime.tools.registerMemoryCli(/* ... */);
[/code]

api.runtime.channel

Ayudantes de tiempo de ejecución específicos del canal (disponibles cuando se carga un plugin de canal).

`api.runtime.channel.mentions` es la superficie compartida de política de menciones entrantes para los plugins de canal incluidos que usan inyección en tiempo de ejecución:

typescriptCopy code
[code]
    const mentionMatch = api.runtime.channel.mentions.matchesMentionWithExplicit(text, {  mentionRegexes,  mentionPatterns,}); const decision = api.runtime.channel.mentions.resolveInboundMentionDecision({  facts: {    canDetectMention: true,    wasMentioned: mentionMatch.matched,    implicitMentionKinds: api.runtime.channel.mentions.implicitMentionKindWhen(      "reply_to_bot",      isReplyToBot,    ),  },  policy: {    isGroup,    requireMention,    allowTextCommands,    hasControlCommand,    commandAuthorized,  },});
[/code]

Ayudantes de mención disponibles:

  * `buildMentionRegexes`
  * `matchesMentionPatterns`
  * `matchesMentionWithExplicit`
  * `implicitMentionKindWhen`
  * `resolveInboundMentionDecision`


`api.runtime.channel.mentions` no expone intencionalmente los ayudantes de compatibilidad antiguos `resolveMentionGating*`. Prefiere la ruta normalizada `{ facts, policy }`.

## Almacenar referencias de tiempo de ejecución

Usa `createPluginRuntimeStore` para almacenar la referencia de tiempo de ejecución y usarla fuera del callback `register`:

* ### Create the store

typescriptCopy code
[code]
    import { createPluginRuntimeStore } from "openclaw/plugin-sdk/runtime-store";import type { PluginRuntime } from "openclaw/plugin-sdk/runtime-store"; const store = createPluginRuntimeStore&lt;PluginRuntime&gt;({  pluginId: "my-plugin",  errorMessage: "my-plugin runtime not initialized",});
[/code]

* ### Wire into the entry point

typescriptCopy code
[code]
    export default defineChannelPluginEntry({  id: "my-plugin",  name: "My Plugin",  description: "Example",  plugin: myPlugin,  setRuntime: store.setRuntime,});
[/code]

* ### Access from other files

typescriptCopy code
[code]
    export function getRuntime() {  return store.getRuntime(); // throws if not initialized} export function tryGetRuntime() {  return store.tryGetRuntime(); // returns null if not initialized}
[/code]

## Otros campos `api` de nivel superior

Más allá de `api.runtime`, el objeto API también proporciona:

Id del Plugin.

Nombre visible del Plugin.

Instantánea de configuración actual (instantánea del runtime en memoria activo cuando está disponible).

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaS5wbHVnaW5Db25maWciIHR5cGU9IlJlY29yZDxzdHJpbmcsIHVua25vd24 "> Configuración específica del Plugin desde `plugins.entries.<id>.config`.

Logger con ámbito (`debug`, `info`, `warn`, `error`).

Modo de carga actual; `"setup-runtime"` es la ventana ligera de inicio/configuración previa a la entrada completa.

## Relacionado

  * [Elementos internos del Plugin](</es/plugins/architecture>) — modelo de capacidades y registro
  * [Puntos de entrada del SDK](</es/plugins/sdk-entrypoints>) — opciones de `definePluginEntry`
  * [Descripción general del SDK](</es/plugins/sdk-overview>) — referencia de subrutas


Was this useful?YesNo