---
title: Plugin-Laufzeit-Hilfsfunktionen
source_url: https://docs.openclaw.ai/de/plugins/sdk-runtime
scraped_at: 2026-05-25
---

Referenz für das `api.runtime`-Objekt, das bei der Registrierung in jedes Plugin injiziert wird. Verwenden Sie diese Hilfsfunktionen, statt Host-Interna direkt zu importieren.

[**Kanal-Plugins** Schritt-für-Schritt-Anleitung, die diese Hilfsfunktionen im Kontext von Kanal-Plugins verwendet. ](</de/plugins/sdk-channel-plugins>) [**Provider-Plugins** Schritt-für-Schritt-Anleitung, die diese Hilfsfunktionen im Kontext von Provider-Plugins verwendet. ](</de/plugins/sdk-provider-plugins>)

typescriptCopy code
[code]
    register(api) {  const runtime = api.runtime;}
[/code]

## Laden und Schreiben der Konfiguration

Bevorzugen Sie Konfiguration, die bereits an den aktiven Aufrufpfad übergeben wurde, zum Beispiel `api.config` während der Registrierung oder ein `cfg`-Argument in Kanal-/Provider-Callbacks. Dadurch fließt ein Prozess-Snapshot durch die Arbeit, statt Konfiguration in heißen Pfaden erneut zu parsen.

Verwenden Sie `api.runtime.config.current()` nur, wenn ein langlebiger Handler den aktuellen Prozess-Snapshot benötigt und keine Konfiguration an diese Funktion übergeben wurde. Der zurückgegebene Wert ist schreibgeschützt; klonen Sie ihn oder verwenden Sie vor der Bearbeitung eine Mutations-Hilfsfunktion.

Tool-Fabriken erhalten `ctx.runtimeConfig` sowie `ctx.getRuntimeConfig()`. Verwenden Sie den Getter im `execute`-Callback eines langlebigen Tools, wenn sich die Konfiguration ändern kann, nachdem die Tool-Definition erstellt wurde.

Persistieren Sie Änderungen mit `api.runtime.config.mutateConfigFile(...)` oder `api.runtime.config.replaceConfigFile(...)`. Jeder Schreibvorgang muss eine explizite `afterWrite`-Policy wählen:

  * `afterWrite: { mode: "auto" }` lässt den Reload-Planer des Gateway entscheiden.
  * `afterWrite: { mode: "restart", reason: "..." }` erzwingt einen sauberen Neustart, wenn der schreibende Aufrufer weiß, dass Hot Reload unsicher ist.
  * `afterWrite: { mode: "none", reason: "..." }` unterdrückt automatisches Reloaden/Neustarten nur, wenn der Aufrufer die Nachbearbeitung verantwortet.


Die Mutations-Hilfsfunktionen geben `afterWrite` sowie eine typisierte `followUp`-Zusammenfassung zurück, damit Aufrufer protokollieren oder testen können, ob sie einen Neustart angefordert haben. Das Gateway entscheidet weiterhin, wann dieser Neustart tatsächlich erfolgt.

`api.runtime.config.loadConfig()` und `api.runtime.config.writeConfigFile(...)` sind veraltete Kompatibilitäts-Hilfsfunktionen unter `runtime-config-load-write`. Sie warnen einmal zur Laufzeit und bleiben während des Migrationsfensters für alte externe Plugins verfügbar. Gebündelte Plugins dürfen sie nicht verwenden; die Konfigurationsgrenzen-Prüfungen schlagen fehl, wenn Plugin-Code sie aufruft oder diese Hilfsfunktionen aus Unterpfaden des Plugin SDK importiert.

Verwenden Sie bei direkten SDK-Importen die fokussierten Konfigurations-Unterpfade statt des breiten Kompatibilitäts-Barrels `openclaw/plugin-sdk/config-runtime`: `config-contracts` für Typen, `plugin-config-runtime` für Assertions zu bereits geladener Konfiguration und die Plugin- Eintragssuche, `runtime-config-snapshot` für aktuelle Prozess-Snapshots und `config-mutation` für Schreibvorgänge. Tests gebündelter Plugins sollten diese fokussierten Unterpfade direkt mocken, statt das breite Kompatibilitäts-Barrel zu mocken.

Interner OpenClaw-Laufzeitcode folgt derselben Richtung: Konfiguration einmal an der CLI-, Gateway- oder Prozessgrenze laden und diesen Wert dann weiterreichen. Erfolgreiche Mutationsschreibvorgänge aktualisieren den Prozess-Laufzeit-Snapshot und erhöhen seine interne Revision; langlebige Caches sollten den Laufzeit-eigenen Cache-Schlüssel verwenden, statt Konfiguration lokal zu serialisieren. Langlebige Laufzeitmodule haben einen Null-Toleranz-Scanner für umgebende `loadConfig()`-Aufrufe; verwenden Sie ein übergebenes `cfg`, ein Anfrage-`context.getRuntimeConfig()` oder `getRuntimeConfig()` an einer expliziten Prozessgrenze.

Provider- und Kanal-Ausführungspfade müssen den aktiven Laufzeit-Konfigurations-Snapshot verwenden, nicht einen Datei-Snapshot, der für Konfigurations-Rücklesen oder Bearbeitung zurückgegeben wurde. Datei-Snapshots erhalten Quellwerte wie SecretRef-Markierungen für UI und Schreibvorgänge; Provider-Callbacks benötigen die aufgelöste Laufzeitansicht. Wenn eine Hilfsfunktion entweder mit dem aktiven Quell-Snapshot oder dem aktiven Laufzeit-Snapshot aufgerufen werden kann, leiten Sie vor dem Lesen von Anmeldedaten über `selectApplicableRuntimeConfig()` weiter.

## Laufzeit-Namespaces

api.runtime.agent

Agent-Identität, Verzeichnisse und Sitzungsverwaltung.

typescriptCopy code
[code]
    // Resolve the agent's working directoryconst agentDir = api.runtime.agent.resolveAgentDir(cfg); // Resolve agent workspaceconst workspaceDir = api.runtime.agent.resolveAgentWorkspaceDir(cfg); // Get agent identityconst identity = api.runtime.agent.resolveAgentIdentity(cfg); // Get default thinking levelconst thinking = api.runtime.agent.resolveThinkingDefault({  cfg,  provider,  model,}); // Validate a user-provided thinking level against the active provider profileconst policy = api.runtime.agent.resolveThinkingPolicy({ provider, model });const level = api.runtime.agent.normalizeThinkingLevel("extra high");if (level && policy.levels.some((entry) => entry.id === level)) {  // pass level to an embedded run} // Get agent timeoutconst timeoutMs = api.runtime.agent.resolveAgentTimeoutMs(cfg); // Ensure workspace existsawait api.runtime.agent.ensureAgentWorkspace(cfg); // Run an embedded agent turnconst agentDir = api.runtime.agent.resolveAgentDir(cfg);const result = await api.runtime.agent.runEmbeddedAgent({  sessionId: "my-plugin:task-1",  runId: crypto.randomUUID(),  sessionFile: path.join(agentDir, "sessions", "my-plugin-task-1.jsonl"),  workspaceDir: api.runtime.agent.resolveAgentWorkspaceDir(cfg),  prompt: "Summarize the latest changes",  timeoutMs: api.runtime.agent.resolveAgentTimeoutMs(cfg),});
[/code]

`runEmbeddedAgent(...)` ist die neutrale Hilfsfunktion, um aus Plugin-Code eine normale OpenClaw-Agent-Runde zu starten. Sie verwendet dieselbe Provider-/Modellauflösung und Agent-Harness-Auswahl wie kanalgetriggerte Antworten.

`runEmbeddedPiAgent(...)` bleibt als Kompatibilitätsalias erhalten.

`resolveThinkingPolicy(...)` gibt die vom Provider/Modell unterstützten Thinking-Level und den optionalen Standardwert zurück. Provider-Plugins besitzen das modellspezifische Profil über ihre Thinking-Hooks, daher sollten Tool-Plugins diese Laufzeit-Hilfsfunktion aufrufen, statt Provider-Listen zu importieren oder zu duplizieren.

`normalizeThinkingLevel(...)` konvertiert Benutzereingaben wie `on`, `x-high` oder `extra high` vor der Prüfung gegen die aufgelöste Policy in das kanonisch gespeicherte Level.

**Hilfsfunktionen für den Sitzungsspeicher** befinden sich unter `api.runtime.agent.session`:

typescriptCopy code
[code]
    const storePath = api.runtime.agent.session.resolveStorePath(cfg);const store = api.runtime.agent.session.loadSessionStore(storePath);await api.runtime.agent.session.updateSessionStore(storePath, (nextStore) => {  // Patch one entry without replacing the whole file from stale state.  nextStore[sessionKey] = { ...nextStore[sessionKey], thinkingLevel: "high" };});const filePath = api.runtime.agent.session.resolveSessionFilePath(cfg, sessionId);
[/code]

Bevorzugen Sie `updateSessionStore(...)` oder `updateSessionStoreEntry(...)` für Laufzeit-Schreibvorgänge. Sie laufen über den Gateway-eigenen Sitzungsspeicher-Writer, erhalten parallele Aktualisierungen und verwenden den Hot Cache erneut. `saveSessionStore(...)` bleibt für Kompatibilität und Offline-Wartungs-Rewrites verfügbar.

api.runtime.agent.defaults

Standardmodell- und Provider-Konstanten:

typescriptCopy code
[code]
    const model = api.runtime.agent.defaults.model; // e.g. "anthropic/claude-sonnet-4-6"const provider = api.runtime.agent.defaults.provider; // e.g. "anthropic"
[/code]

api.runtime.llm

Führen Sie eine Host-eigene Textvervollständigung aus, ohne Provider-Interna zu importieren oder OpenClaw-Modell-/Auth-/Basis-URL-Vorbereitung zu duplizieren.

typescriptCopy code
[code]
    const result = await api.runtime.llm.complete({  messages: [{ role: "user", content: "Summarize this transcript." }],  purpose: "my-plugin.summary",  maxTokens: 512,  temperature: 0.2,});
[/code]

Die Hilfsfunktion verwendet denselben Vorbereitungspfad für einfache Vervollständigungen wie die integrierte OpenClaw-Laufzeit und den Host-eigenen Laufzeit-Konfigurations-Snapshot. Kontext-Engines erhalten eine sitzungsgebundene `llm.complete`-Fähigkeit, sodass Modellaufrufe den Agent der aktiven Sitzung verwenden und nicht unbemerkt auf den Standard-Agent zurückfallen. Das Ergebnis enthält Provider-/Modell-/Agent-Zuordnung sowie normalisierte Token-, Cache- und geschätzte Kostennutzung, wenn verfügbar.

api.runtime.subagent

Starten und verwalten Sie Subagent-Läufe im Hintergrund.

typescriptCopy code
[code]
    // Start a subagent runconst { runId } = await api.runtime.subagent.run({  sessionKey: "agent:main:subagent:search-helper",  message: "Expand this query into focused follow-up searches.",  provider: "openai", // optional override  model: "gpt-4.1-mini", // optional override  deliver: false,}); // Wait for completionconst result = await api.runtime.subagent.waitForRun({ runId, timeoutMs: 30000 }); // Read session messagesconst { messages } = await api.runtime.subagent.getSessionMessages({  sessionKey: "agent:main:subagent:search-helper",  limit: 10,}); // Delete a sessionawait api.runtime.subagent.deleteSession({  sessionKey: "agent:main:subagent:search-helper",});
[/code]

`deleteSession(...)` kann Sitzungen löschen, die dasselbe Plugin über `api.runtime.subagent.run(...)` erstellt hat. Das Löschen beliebiger Benutzer- oder Operator-Sitzungen erfordert weiterhin eine Gateway-Anfrage mit Admin-Scope.

api.runtime.nodes

Listen Sie verbundene Nodes auf und rufen Sie einen Node-Host-Befehl aus Gateway-geladenem Plugin-Code oder aus Plugin-CLI-Befehlen auf. Verwenden Sie dies, wenn ein Plugin lokale Arbeit auf einem gekoppelten Gerät besitzt, zum Beispiel eine Browser- oder Audio-Bridge auf einem anderen Mac.

typescriptCopy code
[code]
    const { nodes } = await api.runtime.nodes.list({ connected: true }); const result = await api.runtime.nodes.invoke({  nodeId: "mac-studio",  command: "my-plugin.command",  params: { action: "start" },  timeoutMs: 30000,});
[/code]

Innerhalb des Gateway läuft diese Laufzeit im Prozess. In Plugin-CLI-Befehlen ruft sie das konfigurierte Gateway über RPC auf, sodass Befehle wie `openclaw googlemeet recover-tab` gekoppelte Nodes vom Terminal aus prüfen können. Node-Befehle durchlaufen weiterhin normales Gateway-Node-Pairing, Befehls-Allowlists, Plugin-Node-Invoke-Policies und node-lokale Befehlsbehandlung.

Plugins, die gefährliche Node-Host-Befehle bereitstellen, sollten eine Node-Invoke-Policy mit `api.registerNodeInvokePolicy(...)` registrieren. Die Policy läuft im Gateway nach den Befehls-Allowlist-Prüfungen und bevor der Befehl an die Node weitergeleitet wird, sodass direkte `node.invoke`-Aufrufe und höherstufige Plugin-Tools denselben Durchsetzungspfad teilen.

api.runtime.tasks.managedFlows

Binden Sie eine Task-Flow-Laufzeit an einen vorhandenen OpenClaw-Sitzungsschlüssel oder einen vertrauenswürdigen Tool-Kontext und erstellen und verwalten Sie dann Task Flows, ohne bei jedem Aufruf einen Owner zu übergeben.

Task Flow verfolgt dauerhaften Zustand mehrstufiger Workflows. Es ist kein Scheduler: Verwenden Sie Cron oder `api.session.workflow.scheduleSessionTurn(...)` für zukünftige Wakeups und verwenden Sie dann `managedFlows` aus der geplanten Runde, wenn diese Arbeit Flow-Zustand, Child-Tasks, Warteoperationen oder Abbruch benötigt.

typescriptCopy code
[code]
    const taskFlow = api.runtime.tasks.managedFlows.fromToolContext(ctx); const created = taskFlow.createManaged({  controllerId: "my-plugin/review-batch",  goal: "Review new pull requests",}); const child = taskFlow.runTask({  flowId: created.flowId,  runtime: "acp",  childSessionKey: "agent:main:subagent:reviewer",  task: "Review PR #123",  status: "running",  startedAt: Date.now(),}); const waiting = taskFlow.setWaiting({  flowId: created.flowId,  expectedRevision: created.revision,  currentStep: "await-human-reply",  waitJson: { kind: "reply", channel: "telegram" },});
[/code]

Verwenden Sie `bindSession({ sessionKey, requesterOrigin })`, wenn Sie bereits einen vertrauenswürdigen OpenClaw-Sitzungsschlüssel aus Ihrer eigenen Binding-Schicht haben. Binden Sie nicht aus rohen Benutzereingaben.

api.runtime.tts

Text-to-Speech-Synthese.

typescriptCopy code
[code]
    // Standard TTSconst clip = await api.runtime.tts.textToSpeech({  text: "Hello from OpenClaw",  cfg: api.config,}); // Telephony-optimized TTSconst telephonyClip = await api.runtime.tts.textToSpeechTelephony({  text: "Hello from OpenClaw",  cfg: api.config,}); // List available voicesconst voices = await api.runtime.tts.listVoices({  provider: "elevenlabs",  cfg: api.config,});
[/code]

Verwendet die Core-Konfiguration `messages.tts` und die Provider-Auswahl. Gibt PCM-Audiopuffer + Abtastrate zurück.

api.runtime.mediaUnderstanding

Bild-, Audio- und Videoanalyse.

typescriptCopy code
[code]
    // Describe an imageconst image = await api.runtime.mediaUnderstanding.describeImageFile({  filePath: "/tmp/inbound-photo.jpg",  cfg: api.config,  agentDir: "/tmp/agent",}); // Transcribe audioconst { text } = await api.runtime.mediaUnderstanding.transcribeAudioFile({  filePath: "/tmp/inbound-audio.ogg",  cfg: api.config,  mime: "audio/ogg", // optional, for when MIME cannot be inferred}); // Describe a videoconst video = await api.runtime.mediaUnderstanding.describeVideoFile({  filePath: "/tmp/inbound-video.mp4",  cfg: api.config,}); // Generic file analysisconst result = await api.runtime.mediaUnderstanding.runFile({  filePath: "/tmp/inbound-file.pdf",  cfg: api.config,}); // Structured image extraction through a specific provider/model.// Include at least one image; text inputs are supplemental context.const evidence = await api.runtime.mediaUnderstanding.extractStructuredWithModel({  provider: "codex",  model: "gpt-5.5",  input: [    {      type: "image",      buffer: receiptImageBuffer,      fileName: "receipt.png",      mime: "image/png",    },    { type: "text", text: "Prefer the printed total over handwritten notes." },  ],  instructions: "Extract vendor, total, and searchable tags.",  schemaName: "receipt.evidence",  jsonSchema: {    type: "object",    properties: {      vendor: { type: "string" },      total: { type: "number" },      tags: { type: "array", items: { type: "string" } },    },    required: ["vendor", "total"],  },  cfg: api.config,});
[/code]

Gibt `{ text: undefined }` zurück, wenn keine Ausgabe erzeugt wird (z. B. bei übersprungener Eingabe).

api.runtime.imageGeneration

Bildgenerierung.

typescriptCopy code
[code]
    const result = await api.runtime.imageGeneration.generate({  prompt: "A robot painting a sunset",  cfg: api.config,}); const providers = api.runtime.imageGeneration.listProviders({ cfg: api.config });
[/code]

api.runtime.webSearch

Websuche.

typescriptCopy code
[code]
    const providers = api.runtime.webSearch.listProviders({ config: api.config }); const result = await api.runtime.webSearch.search({  config: api.config,  args: { query: "OpenClaw plugin SDK", count: 5 },});
[/code]

api.runtime.media

Low-Level-Medienwerkzeuge.

typescriptCopy code
[code]
    const webMedia = await api.runtime.media.loadWebMedia(url);const mime = await api.runtime.media.detectMime(buffer);const kind = api.runtime.media.mediaKindFromMime("image/jpeg"); // "image"const isVoice = api.runtime.media.isVoiceCompatibleAudio(filePath);const metadata = await api.runtime.media.getImageMetadata(filePath);const resized = await api.runtime.media.resizeToJpeg(buffer, { maxWidth: 800 });const terminalQr = await api.runtime.media.renderQrTerminal("https://openclaw.ai");const pngQr = await api.runtime.media.renderQrPngBase64("https://openclaw.ai", {  scale: 6, // 1-12  marginModules: 4, // 0-16});const pngQrDataUrl = await api.runtime.media.renderQrPngDataUrl("https://openclaw.ai");const tmpRoot = resolvePreferredOpenClawTmpDir();const pngQrFile = await api.runtime.media.writeQrPngTempFile("https://openclaw.ai", {  tmpRoot,  dirPrefix: "my-plugin-qr-",  fileName: "qr.png",});
[/code]

api.runtime.config

Aktueller Laufzeit-Konfigurationssnapshot und transaktionale Konfigurationsschreibvorgänge. Bevorzugen Sie Konfiguration, die bereits in den aktiven Aufrufpfad übergeben wurde; verwenden Sie `current()` nur, wenn der Handler den Prozesssnapshot direkt benötigt.

typescriptCopy code
[code]
    const cfg = api.runtime.config.current();await api.runtime.config.mutateConfigFile({  afterWrite: { mode: "auto" },  mutate(draft) {    draft.plugins ??= {};  },});
[/code]

`mutateConfigFile(...)` und `replaceConfigFile(...)` geben einen `followUp`\- Wert zurück, zum Beispiel `{ mode: "restart", requiresRestart: true, reason }`, der die Absicht des Schreibers festhält, ohne dem Gateway die Neustartkontrolle zu entziehen.

api.runtime.system

Werkzeuge auf Systemebene.

typescriptCopy code
[code]
    await api.runtime.system.enqueueSystemEvent(event);api.runtime.system.requestHeartbeat({  source: "other",  intent: "event",  reason: "plugin-event",});api.runtime.system.requestHeartbeatNow({ reason: "plugin-event" }); // Deprecated compatibility alias.const output = await api.runtime.system.runCommandWithTimeout(cmd, args, opts);const hint = api.runtime.system.formatNativeDependencyHint(pkg);
[/code]

api.runtime.events

Ereignisabonnements.

typescriptCopy code
[code]
    api.runtime.events.onAgentEvent((event) => {  /* ... */});api.runtime.events.onSessionTranscriptUpdate((update) => {  /* ... */});
[/code]

api.runtime.logging

Protokollierung.

typescriptCopy code
[code]
    const verbose = api.runtime.logging.shouldLogVerbose();const childLogger = api.runtime.logging.getChildLogger({ plugin: "my-plugin" }, { level: "debug" });
[/code]

api.runtime.modelAuth

Auflösung der Modell- und Provider-Authentifizierung.

typescriptCopy code
[code]
    const auth = await api.runtime.modelAuth.getApiKeyForModel({ model, cfg });const providerAuth = await api.runtime.modelAuth.resolveApiKeyForProvider({  provider: "openai",  cfg,});
[/code]

api.runtime.state

Auflösung des Zustandsverzeichnisses und SQLite-gestützter schlüsselbasierter Speicher.

typescriptCopy code
[code]
    const stateDir = api.runtime.state.resolveStateDir(process.env);const store = api.runtime.state.openKeyedStore&lt;MyRecord&gt;({  namespace: "my-feature",  maxEntries: 200,  defaultTtlMs: 15 * 60_000,}); await store.register("key-1", { value: "hello" });const claimed = await store.registerIfAbsent("dedupe-key", { value: "first" });const value = await store.lookup("key-1");await store.consume("key-1");await store.clear();
[/code]

Schlüsselbasierte Speicher überstehen Neustarts und sind durch die laufzeitgebundene Plugin-ID isoliert. Verwenden Sie `registerIfAbsent(...)` für atomare Deduplizierungs-Claims: Es gibt `true` zurück, wenn der Schlüssel fehlte oder abgelaufen war und registriert wurde, oder `false`, wenn bereits ein aktiver Wert vorhanden ist, ohne dessen Wert, Erstellungszeit oder TTL zu überschreiben. Grenzen: `maxEntries` pro Namespace, 1.000 aktive Zeilen pro Plugin, JSON-Werte unter 64 KB und optionaler TTL-Ablauf.

api.runtime.tools

Memory-Tool-Factories und CLI.

typescriptCopy code
[code]
    const getTool = api.runtime.tools.createMemoryGetTool(/* ... */);const searchTool = api.runtime.tools.createMemorySearchTool(/* ... */);api.runtime.tools.registerMemoryCli(/* ... */);
[/code]

api.runtime.channel

Channelspezifische Laufzeit-Hilfsfunktionen (verfügbar, wenn ein Channel-Plugin geladen ist).

`api.runtime.channel.mentions` ist die gemeinsame Eingangs-Erwähnungsrichtlinienoberfläche für gebündelte Channel-Plugins, die Laufzeitinjektion verwenden:

typescriptCopy code
[code]
    const mentionMatch = api.runtime.channel.mentions.matchesMentionWithExplicit(text, {  mentionRegexes,  mentionPatterns,}); const decision = api.runtime.channel.mentions.resolveInboundMentionDecision({  facts: {    canDetectMention: true,    wasMentioned: mentionMatch.matched,    implicitMentionKinds: api.runtime.channel.mentions.implicitMentionKindWhen(      "reply_to_bot",      isReplyToBot,    ),  },  policy: {    isGroup,    requireMention,    allowTextCommands,    hasControlCommand,    commandAuthorized,  },});
[/code]

Verfügbare Erwähnungs-Hilfsfunktionen:

  * `buildMentionRegexes`
  * `matchesMentionPatterns`
  * `matchesMentionWithExplicit`
  * `implicitMentionKindWhen`
  * `resolveInboundMentionDecision`


`api.runtime.channel.mentions` legt die älteren `resolveMentionGating*`-Kompatibilitäts-Hilfsfunktionen absichtlich nicht offen. Bevorzugen Sie den normalisierten `{ facts, policy }`-Pfad.

## Laufzeitreferenzen speichern

Verwenden Sie `createPluginRuntimeStore`, um die Laufzeitreferenz für die Verwendung außerhalb des `register`-Callbacks zu speichern:

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

## Weitere Top-Level-`api`-Felder

Über `api.runtime` hinaus stellt das API-Objekt außerdem Folgendes bereit:

Plugin-ID.

Anzeigename des Plugins.

Aktueller Konfigurations-Snapshot (aktiver In-Memory-Runtime-Snapshot, wenn verfügbar).

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaS5wbHVnaW5Db25maWciIHR5cGU9IlJlY29yZDxzdHJpbmcsIHVua25vd24 "> Plugin-spezifische Konfiguration aus `plugins.entries.<id>.config`.

Bereichsgebundener Logger (`debug`, `info`, `warn`, `error`).

Aktueller Lademodus; `"setup-runtime"` ist das leichtgewichtige Start-/Setup-Fenster vor dem vollständigen Entry.

## Verwandt

  * [Plugin-Interna](</de/plugins/architecture>) — Capability-Modell und Registry
  * [SDK-Einstiegspunkte](</de/plugins/sdk-entrypoints>) — `definePluginEntry`-Optionen
  * [SDK-Überblick](</de/plugins/sdk-overview>) — Subpath-Referenz


Was this useful?YesNo