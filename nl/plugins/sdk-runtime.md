---
title: Plugin-runtimehulpfuncties
source_url: https://docs.openclaw.ai/nl/plugins/sdk-runtime
scraped_at: 2026-05-25
---

Referentie voor het `api.runtime`-object dat tijdens registratie in elke plugin wordt geinjecteerd. Gebruik deze helpers in plaats van host-internals rechtstreeks te importeren.

[**Channel plugins** Stapsgewijze gids die deze helpers in context gebruikt voor kanaalplugins. ](</nl/plugins/sdk-channel-plugins>) [**Provider plugins** Stapsgewijze gids die deze helpers in context gebruikt voor providerplugins. ](</nl/plugins/sdk-provider-plugins>)

typescriptCopy code
[code]
    register(api) {  const runtime = api.runtime;}
[/code]

## Config laden en schrijven

Geef de voorkeur aan config die al aan het actieve aanroeppad is doorgegeven, bijvoorbeeld `api.config` tijdens registratie of een `cfg`-argument op kanaal-/providercallbacks. Zo blijft er een processnapshot door het werk stromen in plaats van config opnieuw te parsen op hot paths.

Gebruik `api.runtime.config.current()` alleen wanneer een langlevende handler de huidige processnapshot nodig heeft en er geen config aan die functie is doorgegeven. De geretourneerde waarde is alleen-lezen; kloon deze of gebruik een mutatiehelper voordat je bewerkt.

Toolfactories ontvangen `ctx.runtimeConfig` plus `ctx.getRuntimeConfig()`. Gebruik de getter binnen de `execute`-callback van een langlevende tool wanneer config kan veranderen nadat de tooldefinitie is gemaakt.

Sla wijzigingen op met `api.runtime.config.mutateConfigFile(...)` of `api.runtime.config.replaceConfigFile(...)`. Elke schrijfactie moet een expliciet `afterWrite`-beleid kiezen:

  * `afterWrite: { mode: "auto" }` laat de Gateway-herlaadplanner beslissen.
  * `afterWrite: { mode: "restart", reason: "..." }` dwingt een schone herstart af wanneer de schrijver weet dat hot reload onveilig is.
  * `afterWrite: { mode: "none", reason: "..." }` onderdrukt automatisch herladen/herstarten alleen wanneer de aanroeper de opvolging bezit.


De mutatiehelpers retourneren `afterWrite` plus een getypeerde `followUp`-samenvatting, zodat aanroepers kunnen loggen of testen of ze een herstart hebben aangevraagd. De Gateway blijft bepalen wanneer die herstart daadwerkelijk plaatsvindt.

`api.runtime.config.loadConfig()` en `api.runtime.config.writeConfigFile(...)` zijn verouderde compatibiliteitshelpers onder `runtime-config-load-write`. Ze waarschuwen eenmaal tijdens runtime en blijven beschikbaar voor oude externe plugins tijdens het migratievenster. Gebundelde plugins mogen ze niet gebruiken; de configgrensbewakers falen als plugincode ze aanroept of die helpers importeert uit Plugin SDK-subpaden.

Gebruik voor rechtstreekse SDK-imports de gerichte configsubpaden in plaats van de brede compatibiliteitsbarrel `openclaw/plugin-sdk/config-runtime`: `config-contracts` voor typen, `plugin-config-runtime` voor reeds geladen configasserties en plugin- entrylookup, `runtime-config-snapshot` voor huidige processnapshots en `config-mutation` voor schrijfoperaties. Tests van gebundelde plugins moeten deze gerichte subpaden rechtstreeks mocken in plaats van de brede compatibiliteitsbarrel te mocken.

Interne OpenClaw-runtimecode volgt dezelfde richting: laad config eenmaal aan de CLI-, Gateway- of procesgrens en geef die waarde daarna door. Succesvolle mutatieschrijfacties vernieuwen de procesruntime-snapshot en verhogen de interne revisie; langlevende caches moeten sleutelen op de runtime-eigen cachesleutel in plaats van config lokaal te serialiseren. Langlevende runtimemodules hebben een zero-tolerance scanner voor omgevingsaanroepen naar `loadConfig()`; gebruik een doorgegeven `cfg`, een request-`context.getRuntimeConfig()` of `getRuntimeConfig()` aan een expliciete procesgrens.

Provider- en kanaaluitvoeringspaden moeten de actieve runtime-configsnapshot gebruiken, niet een bestandssnapshot die is geretourneerd voor configteruglezing of bewerking. Bestandssnapshots behouden bronwaarden zoals SecretRef-markeringen voor UI en schrijfoperaties; providercallbacks hebben de opgeloste runtimeweergave nodig. Wanneer een helper kan worden aangeroepen met de actieve bronsnapshot of de actieve runtime-snapshot, routeer dan via `selectApplicableRuntimeConfig()` voordat je credentials leest.

## Runtimenamespaces

api.runtime.agent

Agentidentiteit, directories en sessiebeheer.

typescriptCopy code
[code]
    // Resolve the agent's working directoryconst agentDir = api.runtime.agent.resolveAgentDir(cfg); // Resolve agent workspaceconst workspaceDir = api.runtime.agent.resolveAgentWorkspaceDir(cfg); // Get agent identityconst identity = api.runtime.agent.resolveAgentIdentity(cfg); // Get default thinking levelconst thinking = api.runtime.agent.resolveThinkingDefault({  cfg,  provider,  model,}); // Validate a user-provided thinking level against the active provider profileconst policy = api.runtime.agent.resolveThinkingPolicy({ provider, model });const level = api.runtime.agent.normalizeThinkingLevel("extra high");if (level && policy.levels.some((entry) => entry.id === level)) {  // pass level to an embedded run} // Get agent timeoutconst timeoutMs = api.runtime.agent.resolveAgentTimeoutMs(cfg); // Ensure workspace existsawait api.runtime.agent.ensureAgentWorkspace(cfg); // Run an embedded agent turnconst agentDir = api.runtime.agent.resolveAgentDir(cfg);const result = await api.runtime.agent.runEmbeddedAgent({  sessionId: "my-plugin:task-1",  runId: crypto.randomUUID(),  sessionFile: path.join(agentDir, "sessions", "my-plugin-task-1.jsonl"),  workspaceDir: api.runtime.agent.resolveAgentWorkspaceDir(cfg),  prompt: "Summarize the latest changes",  timeoutMs: api.runtime.agent.resolveAgentTimeoutMs(cfg),});
[/code]

`runEmbeddedAgent(...)` is de neutrale helper voor het starten van een normale OpenClaw-agentbeurt vanuit plugincode. Deze gebruikt dezelfde provider-/modelresolutie en agent-harnessselectie als kanaalgetriggerde antwoorden.

`runEmbeddedPiAgent(...)` blijft beschikbaar als compatibiliteitsalias.

`resolveThinkingPolicy(...)` retourneert de ondersteunde thinking-niveaus en optionele standaard van de provider/het model. Providerplugins beheren het modelspecifieke profiel via hun thinking-hooks, dus toolplugins moeten deze runtimehelper aanroepen in plaats van providerlijsten te importeren of te dupliceren.

`normalizeThinkingLevel(...)` zet gebruikerstekst zoals `on`, `x-high` of `extra high` om naar het canonieke opgeslagen niveau voordat dit wordt gecontroleerd tegen het opgeloste beleid.

**Sessieopslaghelpers** staan onder `api.runtime.agent.session`:

typescriptCopy code
[code]
    const storePath = api.runtime.agent.session.resolveStorePath(cfg);const store = api.runtime.agent.session.loadSessionStore(storePath);await api.runtime.agent.session.updateSessionStore(storePath, (nextStore) => {  // Patch one entry without replacing the whole file from stale state.  nextStore[sessionKey] = { ...nextStore[sessionKey], thinkingLevel: "high" };});const filePath = api.runtime.agent.session.resolveSessionFilePath(cfg, sessionId);
[/code]

Geef de voorkeur aan `updateSessionStore(...)` of `updateSessionStoreEntry(...)` voor runtime-schrijfoperaties. Ze routeren via de sessieopslagschrijver die eigendom is van de Gateway, behouden gelijktijdige updates en hergebruiken de hot cache. `saveSessionStore(...)` blijft beschikbaar voor compatibiliteit en offline onderhoudsachtige herschrijfacties.

api.runtime.agent.defaults

Standaardmodel- en providerconstanten:

typescriptCopy code
[code]
    const model = api.runtime.agent.defaults.model; // e.g. "anthropic/claude-sonnet-4-6"const provider = api.runtime.agent.defaults.provider; // e.g. "anthropic"
[/code]

api.runtime.llm

Voer een tekstaanduiding uit die eigendom is van de host zonder providerinternals te importeren of OpenClaw-model-/auth-/basis-URL-voorbereiding te dupliceren.

typescriptCopy code
[code]
    const result = await api.runtime.llm.complete({  messages: [{ role: "user", content: "Summarize this transcript." }],  purpose: "my-plugin.summary",  maxTokens: 512,  temperature: 0.2,});
[/code]

De helper gebruikt hetzelfde eenvoudige completion-voorbereidingspad als de ingebouwde runtime van OpenClaw en de runtime-configsnapshot die eigendom is van de host. Contextengines ontvangen een sessiegebonden `llm.complete`-capability, zodat modelaanroepen de agent van de actieve sessie gebruiken en niet stilzwijgend terugvallen op de standaardagent. Het resultaat bevat provider-/model-/agenttoeschrijving plus genormaliseerd token-, cache- en geschat kostengebruik wanneer beschikbaar.

api.runtime.subagent

Start en beheer subagent-runs op de achtergrond.

typescriptCopy code
[code]
    // Start a subagent runconst { runId } = await api.runtime.subagent.run({  sessionKey: "agent:main:subagent:search-helper",  message: "Expand this query into focused follow-up searches.",  provider: "openai", // optional override  model: "gpt-4.1-mini", // optional override  deliver: false,}); // Wait for completionconst result = await api.runtime.subagent.waitForRun({ runId, timeoutMs: 30000 }); // Read session messagesconst { messages } = await api.runtime.subagent.getSessionMessages({  sessionKey: "agent:main:subagent:search-helper",  limit: 10,}); // Delete a sessionawait api.runtime.subagent.deleteSession({  sessionKey: "agent:main:subagent:search-helper",});
[/code]

`deleteSession(...)` kan sessies verwijderen die door dezelfde plugin zijn gemaakt via `api.runtime.subagent.run(...)`. Het verwijderen van willekeurige gebruikers- of operatorsessies vereist nog steeds een admin-scoped Gateway-request.

api.runtime.nodes

Toon verbonden nodes en roep een node-hostcommando aan vanuit door de Gateway geladen plugincode of vanuit Plugin CLI-commando's. Gebruik dit wanneer een plugin lokaal werk bezit op een gekoppeld apparaat, bijvoorbeeld een browser- of audiobridge op een andere Mac.

typescriptCopy code
[code]
    const { nodes } = await api.runtime.nodes.list({ connected: true }); const result = await api.runtime.nodes.invoke({  nodeId: "mac-studio",  command: "my-plugin.command",  params: { action: "start" },  timeoutMs: 30000,});
[/code]

Binnen de Gateway draait deze runtime in-process. In Plugin CLI-commando's roept deze de geconfigureerde Gateway aan via RPC, zodat commando's zoals `openclaw googlemeet recover-tab` gekoppelde nodes vanuit de terminal kunnen inspecteren. Node-commando's lopen nog steeds via normale Gateway-nodekoppeling, commando-allowlists, plugin-node-invoke-beleid en node-lokale commandoafhandeling.

Plugins die gevaarlijke node-hostcommando's blootstellen, moeten een node-invoke-beleid registreren met `api.registerNodeInvokePolicy(...)`. Het beleid draait in de Gateway na allowlistcontroles voor commando's en voordat het commando naar de node wordt doorgestuurd, zodat rechtstreekse `node.invoke`-aanroepen en hogere plugin-tools hetzelfde handhavingspad delen.

api.runtime.tasks.managedFlows

Bind een Task Flow-runtime aan een bestaande OpenClaw-sessiesleutel of vertrouwde toolcontext en maak en beheer daarna Task Flows zonder bij elke aanroep een eigenaar door te geven.

Task Flow volgt duurzame workflowstatus over meerdere stappen. Het is geen planner: gebruik Cron of `api.session.workflow.scheduleSessionTurn(...)` voor toekomstige wakeups en gebruik daarna `managedFlows` vanuit de geplande beurt wanneer dat werk flowstatus, child-tasks, waits of annulering nodig heeft.

typescriptCopy code
[code]
    const taskFlow = api.runtime.tasks.managedFlows.fromToolContext(ctx); const created = taskFlow.createManaged({  controllerId: "my-plugin/review-batch",  goal: "Review new pull requests",}); const child = taskFlow.runTask({  flowId: created.flowId,  runtime: "acp",  childSessionKey: "agent:main:subagent:reviewer",  task: "Review PR #123",  status: "running",  startedAt: Date.now(),}); const waiting = taskFlow.setWaiting({  flowId: created.flowId,  expectedRevision: created.revision,  currentStep: "await-human-reply",  waitJson: { kind: "reply", channel: "telegram" },});
[/code]

Gebruik `bindSession({ sessionKey, requesterOrigin })` wanneer je al een vertrouwde OpenClaw-sessiesleutel hebt vanuit je eigen koppelingslaag. Koppel niet vanuit ruwe gebruikersinvoer.

api.runtime.tts

Tekst-naar-spraaksynthese.

typescriptCopy code
[code]
    // Standard TTSconst clip = await api.runtime.tts.textToSpeech({  text: "Hello from OpenClaw",  cfg: api.config,}); // Telephony-optimized TTSconst telephonyClip = await api.runtime.tts.textToSpeechTelephony({  text: "Hello from OpenClaw",  cfg: api.config,}); // List available voicesconst voices = await api.runtime.tts.listVoices({  provider: "elevenlabs",  cfg: api.config,});
[/code]

Gebruikt de kernconfiguratie `messages.tts` en providerselectie. Retourneert PCM-audiobuffer + samplefrequentie.

api.runtime.mediaUnderstanding

Analyse van afbeeldingen, audio en video.

typescriptCopy code
[code]
    // Describe an imageconst image = await api.runtime.mediaUnderstanding.describeImageFile({  filePath: "/tmp/inbound-photo.jpg",  cfg: api.config,  agentDir: "/tmp/agent",}); // Transcribe audioconst { text } = await api.runtime.mediaUnderstanding.transcribeAudioFile({  filePath: "/tmp/inbound-audio.ogg",  cfg: api.config,  mime: "audio/ogg", // optional, for when MIME cannot be inferred}); // Describe a videoconst video = await api.runtime.mediaUnderstanding.describeVideoFile({  filePath: "/tmp/inbound-video.mp4",  cfg: api.config,}); // Generic file analysisconst result = await api.runtime.mediaUnderstanding.runFile({  filePath: "/tmp/inbound-file.pdf",  cfg: api.config,}); // Structured image extraction through a specific provider/model.// Include at least one image; text inputs are supplemental context.const evidence = await api.runtime.mediaUnderstanding.extractStructuredWithModel({  provider: "codex",  model: "gpt-5.5",  input: [    {      type: "image",      buffer: receiptImageBuffer,      fileName: "receipt.png",      mime: "image/png",    },    { type: "text", text: "Prefer the printed total over handwritten notes." },  ],  instructions: "Extract vendor, total, and searchable tags.",  schemaName: "receipt.evidence",  jsonSchema: {    type: "object",    properties: {      vendor: { type: "string" },      total: { type: "number" },      tags: { type: "array", items: { type: "string" } },    },    required: ["vendor", "total"],  },  cfg: api.config,});
[/code]

Retourneert `{ text: undefined }` wanneer er geen uitvoer wordt geproduceerd (bijvoorbeeld overgeslagen invoer).

api.runtime.imageGeneration

Afbeeldingen genereren.

typescriptCopy code
[code]
    const result = await api.runtime.imageGeneration.generate({  prompt: "A robot painting a sunset",  cfg: api.config,}); const providers = api.runtime.imageGeneration.listProviders({ cfg: api.config });
[/code]

api.runtime.webSearch

Webzoekopdracht.

typescriptCopy code
[code]
    const providers = api.runtime.webSearch.listProviders({ config: api.config }); const result = await api.runtime.webSearch.search({  config: api.config,  args: { query: "OpenClaw plugin SDK", count: 5 },});
[/code]

api.runtime.media

Laag-niveau mediahulpprogramma's.

typescriptCopy code
[code]
    const webMedia = await api.runtime.media.loadWebMedia(url);const mime = await api.runtime.media.detectMime(buffer);const kind = api.runtime.media.mediaKindFromMime("image/jpeg"); // "image"const isVoice = api.runtime.media.isVoiceCompatibleAudio(filePath);const metadata = await api.runtime.media.getImageMetadata(filePath);const resized = await api.runtime.media.resizeToJpeg(buffer, { maxWidth: 800 });const terminalQr = await api.runtime.media.renderQrTerminal("https://openclaw.ai");const pngQr = await api.runtime.media.renderQrPngBase64("https://openclaw.ai", {  scale: 6, // 1-12  marginModules: 4, // 0-16});const pngQrDataUrl = await api.runtime.media.renderQrPngDataUrl("https://openclaw.ai");const tmpRoot = resolvePreferredOpenClawTmpDir();const pngQrFile = await api.runtime.media.writeQrPngTempFile("https://openclaw.ai", {  tmpRoot,  dirPrefix: "my-plugin-qr-",  fileName: "qr.png",});
[/code]

api.runtime.config

Huidige snapshot van de runtimeconfiguratie en transactionele configuratieschrijfbewerkingen. Geef de voorkeur aan configuratie die al aan het actieve aanroeppad is doorgegeven; gebruik `current()` alleen wanneer de handler de processnapshot direct nodig heeft.

typescriptCopy code
[code]
    const cfg = api.runtime.config.current();await api.runtime.config.mutateConfigFile({  afterWrite: { mode: "auto" },  mutate(draft) {    draft.plugins ??= {};  },});
[/code]

`mutateConfigFile(...)` en `replaceConfigFile(...)` retourneren een `followUp`\- waarde, bijvoorbeeld `{ mode: "restart", requiresRestart: true, reason }`, die de intentie van de schrijver vastlegt zonder de herstartcontrole van de Gateway over te nemen.

api.runtime.system

Systeemhulpprogramma's.

typescriptCopy code
[code]
    await api.runtime.system.enqueueSystemEvent(event);api.runtime.system.requestHeartbeat({  source: "other",  intent: "event",  reason: "plugin-event",});api.runtime.system.requestHeartbeatNow({ reason: "plugin-event" }); // Deprecated compatibility alias.const output = await api.runtime.system.runCommandWithTimeout(cmd, args, opts);const hint = api.runtime.system.formatNativeDependencyHint(pkg);
[/code]

api.runtime.events

Gebeurtenisabonnementen.

typescriptCopy code
[code]
    api.runtime.events.onAgentEvent((event) => {  /* ... */});api.runtime.events.onSessionTranscriptUpdate((update) => {  /* ... */});
[/code]

api.runtime.logging

Logboekregistratie.

typescriptCopy code
[code]
    const verbose = api.runtime.logging.shouldLogVerbose();const childLogger = api.runtime.logging.getChildLogger({ plugin: "my-plugin" }, { level: "debug" });
[/code]

api.runtime.modelAuth

Resolutie van model- en providerauthenticatie.

typescriptCopy code
[code]
    const auth = await api.runtime.modelAuth.getApiKeyForModel({ model, cfg });const providerAuth = await api.runtime.modelAuth.resolveApiKeyForProvider({  provider: "openai",  cfg,});
[/code]

api.runtime.state

Resolutie van de statusmap en SQLite-ondersteunde opslag met sleutels.

typescriptCopy code
[code]
    const stateDir = api.runtime.state.resolveStateDir(process.env);const store = api.runtime.state.openKeyedStore&lt;MyRecord&gt;({  namespace: "my-feature",  maxEntries: 200,  defaultTtlMs: 15 * 60_000,}); await store.register("key-1", { value: "hello" });const claimed = await store.registerIfAbsent("dedupe-key", { value: "first" });const value = await store.lookup("key-1");await store.consume("key-1");await store.clear();
[/code]

Opslagen met sleutels overleven herstarts en zijn geïsoleerd per runtime-gebonden Plugin-id. Gebruik `registerIfAbsent(...)` voor atomaire deduplicatieclaims: dit retourneert `true` wanneer de sleutel ontbrak of verlopen was en is geregistreerd, of `false` wanneer er al een live waarde bestaat zonder de waarde, aanmaaktijd of TTL te overschrijven. Limieten: `maxEntries` per naamruimte, 1.000 live rijen per Plugin, JSON-waarden onder 64 KB en optionele TTL-vervaldatum.

api.runtime.tools

Geheugentoolfactories en CLI.

typescriptCopy code
[code]
    const getTool = api.runtime.tools.createMemoryGetTool(/* ... */);const searchTool = api.runtime.tools.createMemorySearchTool(/* ... */);api.runtime.tools.registerMemoryCli(/* ... */);
[/code]

api.runtime.channel

Kanaalspecifieke runtimehelpers (beschikbaar wanneer een kanaalplugin is geladen).

`api.runtime.channel.mentions` is het gedeelde oppervlak voor inkomend vermeldingsbeleid voor gebundelde kanaalplugins die runtime-injectie gebruiken:

typescriptCopy code
[code]
    const mentionMatch = api.runtime.channel.mentions.matchesMentionWithExplicit(text, {  mentionRegexes,  mentionPatterns,}); const decision = api.runtime.channel.mentions.resolveInboundMentionDecision({  facts: {    canDetectMention: true,    wasMentioned: mentionMatch.matched,    implicitMentionKinds: api.runtime.channel.mentions.implicitMentionKindWhen(      "reply_to_bot",      isReplyToBot,    ),  },  policy: {    isGroup,    requireMention,    allowTextCommands,    hasControlCommand,    commandAuthorized,  },});
[/code]

Beschikbare vermeldingshelpers:

  * `buildMentionRegexes`
  * `matchesMentionPatterns`
  * `matchesMentionWithExplicit`
  * `implicitMentionKindWhen`
  * `resolveInboundMentionDecision`


`api.runtime.channel.mentions` stelt bewust niet de oudere compatibiliteitshelpers `resolveMentionGating*` bloot. Geef de voorkeur aan het genormaliseerde pad `{ facts, policy }`.

## Runtimeverwijzingen opslaan

Gebruik `createPluginRuntimeStore` om de runtimeverwijzing op te slaan voor gebruik buiten de callback `register`:

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

## Andere top-level `api`-velden

Naast `api.runtime` biedt het API-object ook:

Plugin-id.

Weergavenaam van de Plugin.

Huidige configuratie-snapshot (actieve runtime-snapshot in het geheugen indien beschikbaar).

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaS5wbHVnaW5Db25maWciIHR5cGU9IlJlY29yZDxzdHJpbmcsIHVua25vd24 "> Plugin-specifieke configuratie uit `plugins.entries.<id>.config`.

Scoped logger (`debug`, `info`, `warn`, `error`).

Huidige laadmodus; `"setup-runtime"` is het lichtgewicht opstart-/setupvenster vóór de volledige entry.

## Gerelateerd

  * [Interne Plugin-werking](</nl/plugins/architecture>) — mogelijkhedenmodel en register
  * [SDK-entrypoints](</nl/plugins/sdk-entrypoints>) — `definePluginEntry`-opties
  * [SDK-overzicht](</nl/plugins/sdk-overview>) — subpadreferentie


Was this useful?YesNo