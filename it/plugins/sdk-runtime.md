---
title: Helper di runtime del Plugin
source_url: https://docs.openclaw.ai/it/plugins/sdk-runtime
scraped_at: 2026-05-25
---

Riferimento per l'oggetto `api.runtime` iniettato in ogni Plugin durante la registrazione. Usa questi helper invece di importare direttamente gli internals dell'host.

[**Plugin di canale** Guida dettagliata che usa questi helper nel contesto dei Plugin di canale. ](</it/plugins/sdk-channel-plugins>) [**Plugin provider** Guida dettagliata che usa questi helper nel contesto dei Plugin provider. ](</it/plugins/sdk-provider-plugins>)

typescriptCopy code
[code]
    register(api) {  const runtime = api.runtime;}
[/code]

## Caricamento e scritture della configurazione

Preferisci la configurazione già passata al percorso di chiamata attivo, per esempio `api.config` durante la registrazione o un argomento `cfg` nei callback di canale/provider. Questo mantiene un unico snapshot del processo attraverso il lavoro invece di rieseguire il parsing della configurazione nei percorsi critici.

Usa `api.runtime.config.current()` solo quando un handler di lunga durata ha bisogno dello snapshot corrente del processo e a quella funzione non è stata passata alcuna configurazione. Il valore restituito è readonly; clonalo o usa un helper di mutazione prima di modificarlo.

Le factory degli strumenti ricevono `ctx.runtimeConfig` più `ctx.getRuntimeConfig()`. Usa il getter dentro il callback `execute` di uno strumento di lunga durata quando la configurazione può cambiare dopo la creazione della definizione dello strumento.

Rendi persistenti le modifiche con `api.runtime.config.mutateConfigFile(...)` o `api.runtime.config.replaceConfigFile(...)`. Ogni scrittura deve scegliere una policy `afterWrite` esplicita:

  * `afterWrite: { mode: "auto" }` lascia decidere al ricaricamento planner del Gateway.
  * `afterWrite: { mode: "restart", reason: "..." }` forza un riavvio pulito quando chi scrive sa che l'hot reload non è sicuro.
  * `afterWrite: { mode: "none", reason: "..." }` sopprime ricaricamento/riavvio automatici solo quando il chiamante possiede il follow-up.


Gli helper di mutazione restituiscono `afterWrite` più un riepilogo `followUp` tipizzato, così i chiamanti possono registrare nei log o testare se hanno richiesto un riavvio. Il Gateway resta comunque responsabile di quando quel riavvio avviene effettivamente.

`api.runtime.config.loadConfig()` e `api.runtime.config.writeConfigFile(...)` sono helper di compatibilità deprecati sotto `runtime-config-load-write`. Emettono un avviso una sola volta a runtime e restano disponibili per i vecchi Plugin esterni durante la finestra di migrazione. I Plugin in bundle non devono usarli; le guardie del confine di configurazione falliscono se il codice del Plugin li chiama o importa quegli helper dai sottopercorsi del Plugin SDK.

Per import diretti dell'SDK, usa i sottopercorsi di configurazione mirati invece del barrel di compatibilità ampio `openclaw/plugin-sdk/config-runtime`: `config-contracts` per i tipi, `plugin-config-runtime` per le asserzioni sulla configurazione già caricata e la ricerca delle entry dei Plugin, `runtime-config-snapshot` per gli snapshot correnti del processo, e `config-mutation` per le scritture. I test dei Plugin in bundle dovrebbero fare mock direttamente di questi sottopercorsi mirati invece di fare mock del barrel di compatibilità ampio.

Il codice runtime interno di OpenClaw segue la stessa direzione: carica la configurazione una volta al confine della CLI, del Gateway o del processo, poi passa quel valore attraverso il flusso. Le scritture di mutazione riuscite aggiornano lo snapshot runtime del processo e avanzano la sua revisione interna; le cache di lunga durata dovrebbero usare come chiave la chiave cache posseduta dal runtime invece di serializzare localmente la configurazione. I moduli runtime di lunga durata hanno uno scanner a tolleranza zero per le chiamate ambientali a `loadConfig()`; usa un `cfg` passato, un `context.getRuntimeConfig()` della richiesta o `getRuntimeConfig()` a un confine esplicito del processo.

I percorsi di esecuzione di provider e canali devono usare lo snapshot di configurazione runtime attivo, non uno snapshot di file restituito per rilettura o modifica della configurazione. Gli snapshot di file preservano valori sorgente come i marker SecretRef per UI e scritture; i callback provider hanno bisogno della vista runtime risolta. Quando un helper può essere chiamato sia con lo snapshot sorgente attivo sia con lo snapshot runtime attivo, passa attraverso `selectApplicableRuntimeConfig()` prima di leggere le credenziali.

## Namespace runtime

api.runtime.agent

Identità dell'agente, directory e gestione delle sessioni.

typescriptCopy code
[code]
    // Resolve the agent's working directoryconst agentDir = api.runtime.agent.resolveAgentDir(cfg); // Resolve agent workspaceconst workspaceDir = api.runtime.agent.resolveAgentWorkspaceDir(cfg); // Get agent identityconst identity = api.runtime.agent.resolveAgentIdentity(cfg); // Get default thinking levelconst thinking = api.runtime.agent.resolveThinkingDefault({  cfg,  provider,  model,}); // Validate a user-provided thinking level against the active provider profileconst policy = api.runtime.agent.resolveThinkingPolicy({ provider, model });const level = api.runtime.agent.normalizeThinkingLevel("extra high");if (level && policy.levels.some((entry) => entry.id === level)) {  // pass level to an embedded run} // Get agent timeoutconst timeoutMs = api.runtime.agent.resolveAgentTimeoutMs(cfg); // Ensure workspace existsawait api.runtime.agent.ensureAgentWorkspace(cfg); // Run an embedded agent turnconst agentDir = api.runtime.agent.resolveAgentDir(cfg);const result = await api.runtime.agent.runEmbeddedAgent({  sessionId: "my-plugin:task-1",  runId: crypto.randomUUID(),  sessionFile: path.join(agentDir, "sessions", "my-plugin-task-1.jsonl"),  workspaceDir: api.runtime.agent.resolveAgentWorkspaceDir(cfg),  prompt: "Summarize the latest changes",  timeoutMs: api.runtime.agent.resolveAgentTimeoutMs(cfg),});
[/code]

`runEmbeddedAgent(...)` è l'helper neutrale per avviare un normale turno di agente OpenClaw dal codice del Plugin. Usa la stessa risoluzione provider/model e la stessa selezione dell'agent harness delle risposte attivate dal canale.

`runEmbeddedPiAgent(...)` rimane come alias di compatibilità.

`resolveThinkingPolicy(...)` restituisce i livelli di ragionamento supportati dal provider/model e l'eventuale predefinito. I Plugin provider possiedono il profilo specifico del modello tramite i propri hook di ragionamento, quindi i Plugin di strumenti dovrebbero chiamare questo helper runtime invece di importare o duplicare gli elenchi dei provider.

`normalizeThinkingLevel(...)` converte testo utente come `on`, `x-high` o `extra high` nel livello canonico memorizzato prima di verificarlo rispetto alla policy risolta.

Gli **helper dello store delle sessioni** sono sotto `api.runtime.agent.session`:

typescriptCopy code
[code]
    const storePath = api.runtime.agent.session.resolveStorePath(cfg);const store = api.runtime.agent.session.loadSessionStore(storePath);await api.runtime.agent.session.updateSessionStore(storePath, (nextStore) => {  // Patch one entry without replacing the whole file from stale state.  nextStore[sessionKey] = { ...nextStore[sessionKey], thinkingLevel: "high" };});const filePath = api.runtime.agent.session.resolveSessionFilePath(cfg, sessionId);
[/code]

Preferisci `updateSessionStore(...)` o `updateSessionStoreEntry(...)` per le scritture runtime. Passano attraverso il writer dello store delle sessioni posseduto dal Gateway, preservano gli aggiornamenti concorrenti e riutilizzano la cache hot. `saveSessionStore(...)` resta disponibile per compatibilità e riscritture in stile manutenzione offline.

api.runtime.agent.defaults

Costanti predefinite di modello e provider:

typescriptCopy code
[code]
    const model = api.runtime.agent.defaults.model; // e.g. "anthropic/claude-sonnet-4-6"const provider = api.runtime.agent.defaults.provider; // e.g. "anthropic"
[/code]

api.runtime.llm

Esegui un completamento testuale posseduto dall'host senza importare internals del provider o duplicare la preparazione di modello/autenticazione/base URL di OpenClaw.

typescriptCopy code
[code]
    const result = await api.runtime.llm.complete({  messages: [{ role: "user", content: "Summarize this transcript." }],  purpose: "my-plugin.summary",  maxTokens: 512,  temperature: 0.2,});
[/code]

L'helper usa lo stesso percorso di preparazione dei completamenti semplici del runtime integrato di OpenClaw e lo snapshot di configurazione runtime posseduto dall'host. I motori di contesto ricevono una capability `llm.complete` vincolata alla sessione, quindi le chiamate al modello usano l'agente della sessione attiva e non ricadono silenziosamente sull'agente predefinito. Il risultato include attribuzione provider/model/agente più uso normalizzato di token, cache e costo stimato quando disponibile.

api.runtime.subagent

Avvia e gestisci esecuzioni subagent in background.

typescriptCopy code
[code]
    // Start a subagent runconst { runId } = await api.runtime.subagent.run({  sessionKey: "agent:main:subagent:search-helper",  message: "Expand this query into focused follow-up searches.",  provider: "openai", // optional override  model: "gpt-4.1-mini", // optional override  deliver: false,}); // Wait for completionconst result = await api.runtime.subagent.waitForRun({ runId, timeoutMs: 30000 }); // Read session messagesconst { messages } = await api.runtime.subagent.getSessionMessages({  sessionKey: "agent:main:subagent:search-helper",  limit: 10,}); // Delete a sessionawait api.runtime.subagent.deleteSession({  sessionKey: "agent:main:subagent:search-helper",});
[/code]

`deleteSession(...)` può eliminare sessioni create dallo stesso Plugin tramite `api.runtime.subagent.run(...)`. L'eliminazione di sessioni arbitrarie di utenti o operatori richiede comunque una richiesta Gateway con ambito admin.

api.runtime.nodes

Elenca i nodi connessi e invoca un comando ospitato dal nodo dal codice del Plugin caricato dal Gateway o dai comandi CLI del Plugin. Usalo quando un Plugin possiede lavoro locale su un dispositivo associato, per esempio un bridge browser o audio su un altro Mac.

typescriptCopy code
[code]
    const { nodes } = await api.runtime.nodes.list({ connected: true }); const result = await api.runtime.nodes.invoke({  nodeId: "mac-studio",  command: "my-plugin.command",  params: { action: "start" },  timeoutMs: 30000,});
[/code]

Dentro il Gateway questo runtime è in-process. Nei comandi CLI del Plugin chiama il Gateway configurato tramite RPC, quindi comandi come `openclaw googlemeet recover-tab` possono ispezionare i nodi associati dal terminale. I comandi Node passano comunque attraverso il normale pairing dei nodi del Gateway, le allowlist dei comandi, le policy node-invoke dei Plugin e la gestione dei comandi locale al nodo.

I Plugin che espongono comandi per host Node pericolosi dovrebbero registrare una policy node-invoke con `api.registerNodeInvokePolicy(...)`. La policy viene eseguita nel Gateway dopo i controlli della allowlist dei comandi e prima che il comando venga inoltrato al nodo, quindi le chiamate dirette a `node.invoke` e gli strumenti Plugin di livello superiore condividono lo stesso percorso di enforcement.

api.runtime.tasks.managedFlows

Associa un runtime Task Flow a una chiave di sessione OpenClaw esistente o a un contesto strumento attendibile, poi crea e gestisci Task Flow senza passare un owner a ogni chiamata.

Task Flow traccia lo stato durevole dei workflow multi-step. Non è uno scheduler: usa Cron o `api.session.workflow.scheduleSessionTurn(...)` per i risvegli futuri, poi usa `managedFlows` dal turno pianificato quando quel lavoro richiede stato del flow, attività figlie, attese o annullamento.

typescriptCopy code
[code]
    const taskFlow = api.runtime.tasks.managedFlows.fromToolContext(ctx); const created = taskFlow.createManaged({  controllerId: "my-plugin/review-batch",  goal: "Review new pull requests",}); const child = taskFlow.runTask({  flowId: created.flowId,  runtime: "acp",  childSessionKey: "agent:main:subagent:reviewer",  task: "Review PR #123",  status: "running",  startedAt: Date.now(),}); const waiting = taskFlow.setWaiting({  flowId: created.flowId,  expectedRevision: created.revision,  currentStep: "await-human-reply",  waitJson: { kind: "reply", channel: "telegram" },});
[/code]

Usa `bindSession({ sessionKey, requesterOrigin })` quando hai già una chiave di sessione OpenClaw attendibile dal tuo livello di binding. Non effettuare il binding da input utente grezzo.

api.runtime.tts

Sintesi vocale da testo.

typescriptCopy code
[code]
    // Standard TTSconst clip = await api.runtime.tts.textToSpeech({  text: "Hello from OpenClaw",  cfg: api.config,}); // Telephony-optimized TTSconst telephonyClip = await api.runtime.tts.textToSpeechTelephony({  text: "Hello from OpenClaw",  cfg: api.config,}); // List available voicesconst voices = await api.runtime.tts.listVoices({  provider: "elevenlabs",  cfg: api.config,});
[/code]

Usa la configurazione core `messages.tts` e la selezione del provider. Restituisce un buffer audio PCM + frequenza di campionamento.

api.runtime.mediaUnderstanding

Analisi di immagini, audio e video.

typescriptCopy code
[code]
    // Describe an imageconst image = await api.runtime.mediaUnderstanding.describeImageFile({  filePath: "/tmp/inbound-photo.jpg",  cfg: api.config,  agentDir: "/tmp/agent",}); // Transcribe audioconst { text } = await api.runtime.mediaUnderstanding.transcribeAudioFile({  filePath: "/tmp/inbound-audio.ogg",  cfg: api.config,  mime: "audio/ogg", // optional, for when MIME cannot be inferred}); // Describe a videoconst video = await api.runtime.mediaUnderstanding.describeVideoFile({  filePath: "/tmp/inbound-video.mp4",  cfg: api.config,}); // Generic file analysisconst result = await api.runtime.mediaUnderstanding.runFile({  filePath: "/tmp/inbound-file.pdf",  cfg: api.config,}); // Structured image extraction through a specific provider/model.// Include at least one image; text inputs are supplemental context.const evidence = await api.runtime.mediaUnderstanding.extractStructuredWithModel({  provider: "codex",  model: "gpt-5.5",  input: [    {      type: "image",      buffer: receiptImageBuffer,      fileName: "receipt.png",      mime: "image/png",    },    { type: "text", text: "Prefer the printed total over handwritten notes." },  ],  instructions: "Extract vendor, total, and searchable tags.",  schemaName: "receipt.evidence",  jsonSchema: {    type: "object",    properties: {      vendor: { type: "string" },      total: { type: "number" },      tags: { type: "array", items: { type: "string" } },    },    required: ["vendor", "total"],  },  cfg: api.config,});
[/code]

Restituisce `{ text: undefined }` quando non viene prodotto alcun output (ad esempio input saltato).

api.runtime.imageGeneration

Generazione di immagini.

typescriptCopy code
[code]
    const result = await api.runtime.imageGeneration.generate({  prompt: "A robot painting a sunset",  cfg: api.config,}); const providers = api.runtime.imageGeneration.listProviders({ cfg: api.config });
[/code]

api.runtime.webSearch

Ricerca web.

typescriptCopy code
[code]
    const providers = api.runtime.webSearch.listProviders({ config: api.config }); const result = await api.runtime.webSearch.search({  config: api.config,  args: { query: "OpenClaw plugin SDK", count: 5 },});
[/code]

api.runtime.media

Utilità multimediali di basso livello.

typescriptCopy code
[code]
    const webMedia = await api.runtime.media.loadWebMedia(url);const mime = await api.runtime.media.detectMime(buffer);const kind = api.runtime.media.mediaKindFromMime("image/jpeg"); // "image"const isVoice = api.runtime.media.isVoiceCompatibleAudio(filePath);const metadata = await api.runtime.media.getImageMetadata(filePath);const resized = await api.runtime.media.resizeToJpeg(buffer, { maxWidth: 800 });const terminalQr = await api.runtime.media.renderQrTerminal("https://openclaw.ai");const pngQr = await api.runtime.media.renderQrPngBase64("https://openclaw.ai", {  scale: 6, // 1-12  marginModules: 4, // 0-16});const pngQrDataUrl = await api.runtime.media.renderQrPngDataUrl("https://openclaw.ai");const tmpRoot = resolvePreferredOpenClawTmpDir();const pngQrFile = await api.runtime.media.writeQrPngTempFile("https://openclaw.ai", {  tmpRoot,  dirPrefix: "my-plugin-qr-",  fileName: "qr.png",});
[/code]

api.runtime.config

Snapshot della configurazione runtime corrente e scritture di configurazione transazionali. Preferisci la configurazione già passata nel percorso di chiamata attivo; usa `current()` solo quando il gestore ha bisogno direttamente dello snapshot del processo.

typescriptCopy code
[code]
    const cfg = api.runtime.config.current();await api.runtime.config.mutateConfigFile({  afterWrite: { mode: "auto" },  mutate(draft) {    draft.plugins ??= {};  },});
[/code]

`mutateConfigFile(...)` e `replaceConfigFile(...)` restituiscono un valore `followUp`, per esempio `{ mode: "restart", requiresRestart: true, reason }`, che registra l'intento dello scrivente senza sottrarre al Gateway il controllo del riavvio.

api.runtime.system

Utilità a livello di sistema.

typescriptCopy code
[code]
    await api.runtime.system.enqueueSystemEvent(event);api.runtime.system.requestHeartbeat({  source: "other",  intent: "event",  reason: "plugin-event",});api.runtime.system.requestHeartbeatNow({ reason: "plugin-event" }); // Deprecated compatibility alias.const output = await api.runtime.system.runCommandWithTimeout(cmd, args, opts);const hint = api.runtime.system.formatNativeDependencyHint(pkg);
[/code]

api.runtime.events

Sottoscrizioni agli eventi.

typescriptCopy code
[code]
    api.runtime.events.onAgentEvent((event) => {  /* ... */});api.runtime.events.onSessionTranscriptUpdate((update) => {  /* ... */});
[/code]

api.runtime.logging

Logging.

typescriptCopy code
[code]
    const verbose = api.runtime.logging.shouldLogVerbose();const childLogger = api.runtime.logging.getChildLogger({ plugin: "my-plugin" }, { level: "debug" });
[/code]

api.runtime.modelAuth

Risoluzione dell'autenticazione di modello e provider.

typescriptCopy code
[code]
    const auth = await api.runtime.modelAuth.getApiKeyForModel({ model, cfg });const providerAuth = await api.runtime.modelAuth.resolveApiKeyForProvider({  provider: "openai",  cfg,});
[/code]

api.runtime.state

Risoluzione della directory di stato e archiviazione con chiavi basata su SQLite.

typescriptCopy code
[code]
    const stateDir = api.runtime.state.resolveStateDir(process.env);const store = api.runtime.state.openKeyedStore&lt;MyRecord&gt;({  namespace: "my-feature",  maxEntries: 200,  defaultTtlMs: 15 * 60_000,}); await store.register("key-1", { value: "hello" });const claimed = await store.registerIfAbsent("dedupe-key", { value: "first" });const value = await store.lookup("key-1");await store.consume("key-1");await store.clear();
[/code]

Gli store con chiavi sopravvivono ai riavvii e sono isolati dall'id del Plugin associato al runtime. Usa `registerIfAbsent(...)` per rivendicazioni atomiche di deduplicazione: restituisce `true` quando la chiave era assente o scaduta ed è stata registrata, oppure `false` quando esiste già un valore attivo senza sovrascriverne valore, ora di creazione o TTL. Limiti: `maxEntries` per namespace, 1.000 righe attive per Plugin, valori JSON inferiori a 64 KB e scadenza TTL facoltativa.

api.runtime.tools

Factory di strumenti di memoria e CLI.

typescriptCopy code
[code]
    const getTool = api.runtime.tools.createMemoryGetTool(/* ... */);const searchTool = api.runtime.tools.createMemorySearchTool(/* ... */);api.runtime.tools.registerMemoryCli(/* ... */);
[/code]

api.runtime.channel

Helper runtime specifici del canale (disponibili quando viene caricato un Plugin di canale).

`api.runtime.channel.mentions` è la superficie condivisa delle policy di menzione in ingresso per i Plugin di canale in bundle che usano l'iniezione runtime:

typescriptCopy code
[code]
    const mentionMatch = api.runtime.channel.mentions.matchesMentionWithExplicit(text, {  mentionRegexes,  mentionPatterns,}); const decision = api.runtime.channel.mentions.resolveInboundMentionDecision({  facts: {    canDetectMention: true,    wasMentioned: mentionMatch.matched,    implicitMentionKinds: api.runtime.channel.mentions.implicitMentionKindWhen(      "reply_to_bot",      isReplyToBot,    ),  },  policy: {    isGroup,    requireMention,    allowTextCommands,    hasControlCommand,    commandAuthorized,  },});
[/code]

Helper di menzione disponibili:

  * `buildMentionRegexes`
  * `matchesMentionPatterns`
  * `matchesMentionWithExplicit`
  * `implicitMentionKindWhen`
  * `resolveInboundMentionDecision`


`api.runtime.channel.mentions` intenzionalmente non espone i vecchi helper di compatibilità `resolveMentionGating*`. Preferisci il percorso normalizzato `{ facts, policy }`.

## Archiviazione dei riferimenti runtime

Usa `createPluginRuntimeStore` per archiviare il riferimento runtime da usare fuori dalla callback `register`:

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

## Altri campi `api` di primo livello

Oltre a `api.runtime`, l'oggetto API fornisce anche:

ID del Plugin.

Nome visualizzato del Plugin.

Snapshot della configurazione corrente (snapshot runtime attivo in memoria quando disponibile).

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaS5wbHVnaW5Db25maWciIHR5cGU9IlJlY29yZDxzdHJpbmcsIHVua25vd24 "> Configurazione specifica del Plugin da `plugins.entries.<id>.config`.

Logger con ambito (`debug`, `info`, `warn`, `error`).

Modalità di caricamento corrente; `"setup-runtime"` è la finestra leggera di avvio/configurazione precedente all'entry completa.

## Correlati

  * [Interni del Plugin](</it/plugins/architecture>) — modello di capability e registro
  * [Punti di ingresso SDK](</it/plugins/sdk-entrypoints>) — opzioni di `definePluginEntry`
  * [Panoramica dell'SDK](</it/plugins/sdk-overview>) — riferimento ai sottopercorsi


Was this useful?YesNo