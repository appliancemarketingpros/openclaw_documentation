---
title: Funkcje pomocnicze środowiska uruchomieniowego Plugin
source_url: https://docs.openclaw.ai/pl/plugins/sdk-runtime
scraped_at: 2026-05-25
---

Dokumentacja referencyjna obiektu `api.runtime` wstrzykiwanego do każdego pluginu podczas rejestracji. Używaj tych helperów zamiast bezpośrednio importować wewnętrzne moduły hosta.

[**Pluginy kanałów** Przewodnik krok po kroku, który pokazuje użycie tych helperów w kontekście pluginów kanałów. ](</pl/plugins/sdk-channel-plugins>) [**Pluginy dostawców** Przewodnik krok po kroku, który pokazuje użycie tych helperów w kontekście pluginów dostawców. ](</pl/plugins/sdk-provider-plugins>)

typescriptCopy code
[code]
    register(api) {  const runtime = api.runtime;}
[/code]

## Ładowanie i zapisywanie konfiguracji

Preferuj konfigurację, która została już przekazana do aktywnej ścieżki wywołania, na przykład `api.config` podczas rejestracji albo argument `cfg` w callbackach kanału/dostawcy. Dzięki temu przez pracę przepływa jedna migawka procesu zamiast ponownego parsowania konfiguracji na gorących ścieżkach.

Używaj `api.runtime.config.current()` tylko wtedy, gdy długotrwały handler potrzebuje bieżącej migawki procesu, a do tej funkcji nie przekazano konfiguracji. Zwrócona wartość jest tylko do odczytu; sklonuj ją albo użyj helpera mutacji przed edycją.

Fabryki narzędzi otrzymują `ctx.runtimeConfig` oraz `ctx.getRuntimeConfig()`. Używaj gettera wewnątrz callbacku `execute` długotrwałego narzędzia, gdy konfiguracja może zmienić się po utworzeniu definicji narzędzia.

Utrwalaj zmiany za pomocą `api.runtime.config.mutateConfigFile(...)` albo `api.runtime.config.replaceConfigFile(...)`. Każdy zapis musi wybrać jawną politykę `afterWrite`:

  * `afterWrite: { mode: "auto" }` pozwala mechanizmowi przeładowania gatewaya zdecydować.
  * `afterWrite: { mode: "restart", reason: "..." }` wymusza czysty restart, gdy zapisujący wie, że przeładowanie na gorąco jest niebezpieczne.
  * `afterWrite: { mode: "none", reason: "..." }` pomija automatyczne przeładowanie/restart tylko wtedy, gdy wywołujący odpowiada za dalsze działania.


Helpery mutacji zwracają `afterWrite` oraz typowane podsumowanie `followUp`, aby wywołujący mogli logować lub testować, czy zażądali restartu. Gateway nadal odpowiada za to, kiedy ten restart faktycznie nastąpi.

`api.runtime.config.loadConfig()` oraz `api.runtime.config.writeConfigFile(...)` to przestarzałe helpery zgodności w ramach `runtime-config-load-write`. Ostrzegają raz w czasie działania i pozostają dostępne dla starych zewnętrznych pluginów w okresie migracji. Wbudowane pluginy nie mogą ich używać; strażnicy granicy konfiguracji kończą się niepowodzeniem, jeśli kod pluginu je wywołuje albo importuje te helpery z podścieżek SDK pluginów.

Przy bezpośrednich importach SDK używaj wyspecjalizowanych podścieżek konfiguracji zamiast szerokiego barrela zgodności `openclaw/plugin-sdk/config-runtime`: `config-contracts` dla typów, `plugin-config-runtime` dla asercji już załadowanej konfiguracji i wyszukiwania wpisu pluginu, `runtime-config-snapshot` dla bieżących migawek procesu oraz `config-mutation` dla zapisów. Testy wbudowanych pluginów powinny mockować te wyspecjalizowane podścieżki bezpośrednio zamiast mockować szeroki barrel zgodności.

Wewnętrzny kod runtime OpenClaw podąża w tym samym kierunku: załaduj konfigurację raz na granicy CLI, Gatewaya lub procesu, a następnie przekazuj tę wartość dalej. Udane zapisy mutacji odświeżają migawkę runtime procesu i zwiększają jej wewnętrzną rewizję; długotrwałe cache powinny używać klucza cache należącego do runtime zamiast lokalnie serializować konfigurację. Długotrwałe moduły runtime mają skaner o zerowej tolerancji dla otaczających wywołań `loadConfig()`; użyj przekazanego `cfg`, żądania `context.getRuntimeConfig()` albo `getRuntimeConfig()` na jawnej granicy procesu.

Ścieżki wykonania dostawców i kanałów muszą używać aktywnej migawki konfiguracji runtime, a nie migawki pliku zwróconej do odczytu zwrotnego lub edycji konfiguracji. Migawki pliku zachowują wartości źródłowe, takie jak markery SecretRef, dla UI i zapisów; callbacki dostawców potrzebują rozwiązanego widoku runtime. Gdy helper może zostać wywołany zarówno z aktywną migawką źródłową, jak i aktywną migawką runtime, przed odczytem poświadczeń przejdź przez `selectApplicableRuntimeConfig()`.

## Przestrzenie nazw runtime

api.runtime.agent

Tożsamość agenta, katalogi i zarządzanie sesją.

typescriptCopy code
[code]
    // Resolve the agent's working directoryconst agentDir = api.runtime.agent.resolveAgentDir(cfg); // Resolve agent workspaceconst workspaceDir = api.runtime.agent.resolveAgentWorkspaceDir(cfg); // Get agent identityconst identity = api.runtime.agent.resolveAgentIdentity(cfg); // Get default thinking levelconst thinking = api.runtime.agent.resolveThinkingDefault({  cfg,  provider,  model,}); // Validate a user-provided thinking level against the active provider profileconst policy = api.runtime.agent.resolveThinkingPolicy({ provider, model });const level = api.runtime.agent.normalizeThinkingLevel("extra high");if (level && policy.levels.some((entry) => entry.id === level)) {  // pass level to an embedded run} // Get agent timeoutconst timeoutMs = api.runtime.agent.resolveAgentTimeoutMs(cfg); // Ensure workspace existsawait api.runtime.agent.ensureAgentWorkspace(cfg); // Run an embedded agent turnconst agentDir = api.runtime.agent.resolveAgentDir(cfg);const result = await api.runtime.agent.runEmbeddedAgent({  sessionId: "my-plugin:task-1",  runId: crypto.randomUUID(),  sessionFile: path.join(agentDir, "sessions", "my-plugin-task-1.jsonl"),  workspaceDir: api.runtime.agent.resolveAgentWorkspaceDir(cfg),  prompt: "Summarize the latest changes",  timeoutMs: api.runtime.agent.resolveAgentTimeoutMs(cfg),});
[/code]

`runEmbeddedAgent(...)` to neutralny helper do uruchamiania zwykłej tury agenta OpenClaw z kodu pluginu. Używa tego samego rozwiązywania dostawcy/modelu i wyboru harnessu agenta co odpowiedzi wyzwalane przez kanał.

`runEmbeddedPiAgent(...)` pozostaje aliasem zgodności.

`resolveThinkingPolicy(...)` zwraca obsługiwane poziomy thinking dostawcy/modelu oraz opcjonalną wartość domyślną. Pluginy dostawców odpowiadają za profil specyficzny dla modelu poprzez swoje hooki thinking, więc pluginy narzędziowe powinny wywoływać ten helper runtime zamiast importować lub duplikować listy dostawców.

`normalizeThinkingLevel(...)` konwertuje tekst użytkownika, taki jak `on`, `x-high` lub `extra high`, na kanoniczny zapisany poziom przed sprawdzeniem go względem rozwiązanej polityki.

**Helpery magazynu sesji** znajdują się w `api.runtime.agent.session`:

typescriptCopy code
[code]
    const storePath = api.runtime.agent.session.resolveStorePath(cfg);const store = api.runtime.agent.session.loadSessionStore(storePath);await api.runtime.agent.session.updateSessionStore(storePath, (nextStore) => {  // Patch one entry without replacing the whole file from stale state.  nextStore[sessionKey] = { ...nextStore[sessionKey], thinkingLevel: "high" };});const filePath = api.runtime.agent.session.resolveSessionFilePath(cfg, sessionId);
[/code]

Do zapisów runtime preferuj `updateSessionStore(...)` albo `updateSessionStoreEntry(...)`. Przechodzą przez writer magazynu sesji należący do Gatewaya, zachowują równoległe aktualizacje i ponownie używają gorącego cache. `saveSessionStore(...)` pozostaje dostępne dla zgodności i przeróbek w stylu konserwacji offline.

api.runtime.agent.defaults

Domyślne stałe modelu i dostawcy:

typescriptCopy code
[code]
    const model = api.runtime.agent.defaults.model; // e.g. "anthropic/claude-sonnet-4-6"const provider = api.runtime.agent.defaults.provider; // e.g. "anthropic"
[/code]

api.runtime.llm

Uruchom uzupełnianie tekstu należące do hosta bez importowania wewnętrznych modułów dostawcy ani duplikowania przygotowania modelu/auth/base URL OpenClaw.

typescriptCopy code
[code]
    const result = await api.runtime.llm.complete({  messages: [{ role: "user", content: "Summarize this transcript." }],  purpose: "my-plugin.summary",  maxTokens: 512,  temperature: 0.2,});
[/code]

Helper używa tej samej ścieżki przygotowania prostego uzupełniania co wbudowany runtime OpenClaw oraz migawki konfiguracji runtime należącej do hosta. Silniki kontekstu otrzymują powiązaną z sesją capability `llm.complete`, więc wywołania modelu używają agenta aktywnej sesji i nie przełączają się po cichu na agenta domyślnego. Wynik obejmuje atrybucję dostawcy/modelu/agenta oraz znormalizowane użycie tokenów, cache i szacowanego kosztu, gdy są dostępne.

api.runtime.subagent

Uruchamiaj i zarządzaj działaniami subagentów w tle.

typescriptCopy code
[code]
    // Start a subagent runconst { runId } = await api.runtime.subagent.run({  sessionKey: "agent:main:subagent:search-helper",  message: "Expand this query into focused follow-up searches.",  provider: "openai", // optional override  model: "gpt-4.1-mini", // optional override  deliver: false,}); // Wait for completionconst result = await api.runtime.subagent.waitForRun({ runId, timeoutMs: 30000 }); // Read session messagesconst { messages } = await api.runtime.subagent.getSessionMessages({  sessionKey: "agent:main:subagent:search-helper",  limit: 10,}); // Delete a sessionawait api.runtime.subagent.deleteSession({  sessionKey: "agent:main:subagent:search-helper",});
[/code]

`deleteSession(...)` może usuwać sesje utworzone przez ten sam plugin przez `api.runtime.subagent.run(...)`. Usuwanie dowolnych sesji użytkownika lub operatora nadal wymaga żądania Gatewaya o zakresie administratora.

api.runtime.nodes

Wyświetl połączone węzły i wywołaj polecenie hosta węzła z kodu pluginu załadowanego przez Gateway albo z poleceń CLI pluginu. Użyj tego, gdy plugin odpowiada za lokalną pracę na sparowanym urządzeniu, na przykład most przeglądarki lub audio na innym Macu.

typescriptCopy code
[code]
    const { nodes } = await api.runtime.nodes.list({ connected: true }); const result = await api.runtime.nodes.invoke({  nodeId: "mac-studio",  command: "my-plugin.command",  params: { action: "start" },  timeoutMs: 30000,});
[/code]

Wewnątrz Gatewaya ten runtime działa w procesie. W poleceniach CLI pluginu wywołuje skonfigurowany Gateway przez RPC, więc polecenia takie jak `openclaw googlemeet recover-tab` mogą sprawdzać sparowane węzły z terminala. Polecenia Node nadal przechodzą przez zwykłe parowanie węzłów Gatewaya, listy dozwolonych poleceń, polityki node-invoke pluginów i lokalną obsługę poleceń węzła.

Pluginy, które udostępniają niebezpieczne polecenia hosta węzła, powinny zarejestrować politykę node-invoke za pomocą `api.registerNodeInvokePolicy(...)`. Polityka działa w Gatewayu po sprawdzeniu listy dozwolonych poleceń i przed przekazaniem polecenia do węzła, więc bezpośrednie wywołania `node.invoke` i narzędzia pluginów wyższego poziomu współdzielą tę samą ścieżkę egzekwowania.

api.runtime.tasks.managedFlows

Powiąż runtime Task Flow z istniejącym kluczem sesji OpenClaw lub zaufanym kontekstem narzędzia, a następnie twórz i zarządzaj Task Flows bez przekazywania właściciela przy każdym wywołaniu.

Task Flow śledzi trwały stan wieloetapowego workflow. Nie jest schedulerem: użyj Cron albo `api.session.workflow.scheduleSessionTurn(...)` dla przyszłych wybudzeń, a następnie użyj `managedFlows` z zaplanowanej tury, gdy ta praca potrzebuje stanu flow, zadań podrzędnych, oczekiwań lub anulowania.

typescriptCopy code
[code]
    const taskFlow = api.runtime.tasks.managedFlows.fromToolContext(ctx); const created = taskFlow.createManaged({  controllerId: "my-plugin/review-batch",  goal: "Review new pull requests",}); const child = taskFlow.runTask({  flowId: created.flowId,  runtime: "acp",  childSessionKey: "agent:main:subagent:reviewer",  task: "Review PR #123",  status: "running",  startedAt: Date.now(),}); const waiting = taskFlow.setWaiting({  flowId: created.flowId,  expectedRevision: created.revision,  currentStep: "await-human-reply",  waitJson: { kind: "reply", channel: "telegram" },});
[/code]

Używaj `bindSession({ sessionKey, requesterOrigin })`, gdy masz już zaufany klucz sesji OpenClaw z własnej warstwy wiązania. Nie wiąż na podstawie surowych danych wejściowych użytkownika.

api.runtime.tts

Synteza mowy z tekstu.

typescriptCopy code
[code]
    // Standard TTSconst clip = await api.runtime.tts.textToSpeech({  text: "Hello from OpenClaw",  cfg: api.config,}); // Telephony-optimized TTSconst telephonyClip = await api.runtime.tts.textToSpeechTelephony({  text: "Hello from OpenClaw",  cfg: api.config,}); // List available voicesconst voices = await api.runtime.tts.listVoices({  provider: "elevenlabs",  cfg: api.config,});
[/code]

Używa podstawowej konfiguracji `messages.tts` i wyboru dostawcy. Zwraca bufor audio PCM + częstotliwość próbkowania.

api.runtime.mediaUnderstanding

Analiza obrazu, dźwięku i wideo.

typescriptCopy code
[code]
    // Describe an imageconst image = await api.runtime.mediaUnderstanding.describeImageFile({  filePath: "/tmp/inbound-photo.jpg",  cfg: api.config,  agentDir: "/tmp/agent",}); // Transcribe audioconst { text } = await api.runtime.mediaUnderstanding.transcribeAudioFile({  filePath: "/tmp/inbound-audio.ogg",  cfg: api.config,  mime: "audio/ogg", // optional, for when MIME cannot be inferred}); // Describe a videoconst video = await api.runtime.mediaUnderstanding.describeVideoFile({  filePath: "/tmp/inbound-video.mp4",  cfg: api.config,}); // Generic file analysisconst result = await api.runtime.mediaUnderstanding.runFile({  filePath: "/tmp/inbound-file.pdf",  cfg: api.config,}); // Structured image extraction through a specific provider/model.// Include at least one image; text inputs are supplemental context.const evidence = await api.runtime.mediaUnderstanding.extractStructuredWithModel({  provider: "codex",  model: "gpt-5.5",  input: [    {      type: "image",      buffer: receiptImageBuffer,      fileName: "receipt.png",      mime: "image/png",    },    { type: "text", text: "Prefer the printed total over handwritten notes." },  ],  instructions: "Extract vendor, total, and searchable tags.",  schemaName: "receipt.evidence",  jsonSchema: {    type: "object",    properties: {      vendor: { type: "string" },      total: { type: "number" },      tags: { type: "array", items: { type: "string" } },    },    required: ["vendor", "total"],  },  cfg: api.config,});
[/code]

Zwraca `{ text: undefined }`, gdy nie zostanie wygenerowane żadne wyjście (np. pominięte wejście).

api.runtime.imageGeneration

Generowanie obrazów.

typescriptCopy code
[code]
    const result = await api.runtime.imageGeneration.generate({  prompt: "A robot painting a sunset",  cfg: api.config,}); const providers = api.runtime.imageGeneration.listProviders({ cfg: api.config });
[/code]

api.runtime.webSearch

Wyszukiwanie w sieci.

typescriptCopy code
[code]
    const providers = api.runtime.webSearch.listProviders({ config: api.config }); const result = await api.runtime.webSearch.search({  config: api.config,  args: { query: "OpenClaw plugin SDK", count: 5 },});
[/code]

api.runtime.media

Niskopoziomowe narzędzia do obsługi multimediów.

typescriptCopy code
[code]
    const webMedia = await api.runtime.media.loadWebMedia(url);const mime = await api.runtime.media.detectMime(buffer);const kind = api.runtime.media.mediaKindFromMime("image/jpeg"); // "image"const isVoice = api.runtime.media.isVoiceCompatibleAudio(filePath);const metadata = await api.runtime.media.getImageMetadata(filePath);const resized = await api.runtime.media.resizeToJpeg(buffer, { maxWidth: 800 });const terminalQr = await api.runtime.media.renderQrTerminal("https://openclaw.ai");const pngQr = await api.runtime.media.renderQrPngBase64("https://openclaw.ai", {  scale: 6, // 1-12  marginModules: 4, // 0-16});const pngQrDataUrl = await api.runtime.media.renderQrPngDataUrl("https://openclaw.ai");const tmpRoot = resolvePreferredOpenClawTmpDir();const pngQrFile = await api.runtime.media.writeQrPngTempFile("https://openclaw.ai", {  tmpRoot,  dirPrefix: "my-plugin-qr-",  fileName: "qr.png",});
[/code]

api.runtime.config

Bieżąca migawka konfiguracji środowiska uruchomieniowego i transakcyjne zapisy konfiguracji. Preferuj konfigurację, która została już przekazana do aktywnej ścieżki wywołania; używaj `current()` tylko wtedy, gdy procedura obsługi potrzebuje bezpośrednio migawki procesu.

typescriptCopy code
[code]
    const cfg = api.runtime.config.current();await api.runtime.config.mutateConfigFile({  afterWrite: { mode: "auto" },  mutate(draft) {    draft.plugins ??= {};  },});
[/code]

`mutateConfigFile(...)` i `replaceConfigFile(...)` zwracają wartość `followUp`, na przykład `{ mode: "restart", requiresRestart: true, reason }`, która rejestruje intencję zapisującego bez odbierania kontroli nad restartem Gateway.

api.runtime.system

Narzędzia poziomu systemowego.

typescriptCopy code
[code]
    await api.runtime.system.enqueueSystemEvent(event);api.runtime.system.requestHeartbeat({  source: "other",  intent: "event",  reason: "plugin-event",});api.runtime.system.requestHeartbeatNow({ reason: "plugin-event" }); // Deprecated compatibility alias.const output = await api.runtime.system.runCommandWithTimeout(cmd, args, opts);const hint = api.runtime.system.formatNativeDependencyHint(pkg);
[/code]

api.runtime.events

Subskrypcje zdarzeń.

typescriptCopy code
[code]
    api.runtime.events.onAgentEvent((event) => {  /* ... */});api.runtime.events.onSessionTranscriptUpdate((update) => {  /* ... */});
[/code]

api.runtime.logging

Rejestrowanie.

typescriptCopy code
[code]
    const verbose = api.runtime.logging.shouldLogVerbose();const childLogger = api.runtime.logging.getChildLogger({ plugin: "my-plugin" }, { level: "debug" });
[/code]

api.runtime.modelAuth

Rozwiązywanie uwierzytelniania modelu i dostawcy.

typescriptCopy code
[code]
    const auth = await api.runtime.modelAuth.getApiKeyForModel({ model, cfg });const providerAuth = await api.runtime.modelAuth.resolveApiKeyForProvider({  provider: "openai",  cfg,});
[/code]

api.runtime.state

Rozwiązywanie katalogu stanu i magazyn kluczowany oparty na SQLite.

typescriptCopy code
[code]
    const stateDir = api.runtime.state.resolveStateDir(process.env);const store = api.runtime.state.openKeyedStore&lt;MyRecord&gt;({  namespace: "my-feature",  maxEntries: 200,  defaultTtlMs: 15 * 60_000,}); await store.register("key-1", { value: "hello" });const claimed = await store.registerIfAbsent("dedupe-key", { value: "first" });const value = await store.lookup("key-1");await store.consume("key-1");await store.clear();
[/code]

Magazyny kluczowane przetrwają restarty i są izolowane według identyfikatora pluginu powiązanego ze środowiskiem uruchomieniowym. Używaj `registerIfAbsent(...)` do atomowego zajmowania kluczy deduplikacji: zwraca `true`, gdy brakowało klucza albo wygasł i został zarejestrowany, albo `false`, gdy aktywna wartość już istnieje, bez nadpisywania jej wartości, czasu utworzenia ani TTL. Limity: `maxEntries` na przestrzeń nazw, 1000 aktywnych wierszy na plugin, wartości JSON poniżej 64 KB oraz opcjonalne wygasanie TTL.

api.runtime.tools

Fabryki narzędzi pamięci i CLI.

typescriptCopy code
[code]
    const getTool = api.runtime.tools.createMemoryGetTool(/* ... */);const searchTool = api.runtime.tools.createMemorySearchTool(/* ... */);api.runtime.tools.registerMemoryCli(/* ... */);
[/code]

api.runtime.channel

Pomocniki środowiska uruchomieniowego specyficzne dla kanału (dostępne, gdy załadowany jest plugin kanału).

`api.runtime.channel.mentions` to wspólny interfejs zasad obsługi przychodzących wzmianek dla dołączonych pluginów kanałów, które używają wstrzykiwania środowiska uruchomieniowego:

typescriptCopy code
[code]
    const mentionMatch = api.runtime.channel.mentions.matchesMentionWithExplicit(text, {  mentionRegexes,  mentionPatterns,}); const decision = api.runtime.channel.mentions.resolveInboundMentionDecision({  facts: {    canDetectMention: true,    wasMentioned: mentionMatch.matched,    implicitMentionKinds: api.runtime.channel.mentions.implicitMentionKindWhen(      "reply_to_bot",      isReplyToBot,    ),  },  policy: {    isGroup,    requireMention,    allowTextCommands,    hasControlCommand,    commandAuthorized,  },});
[/code]

Dostępne pomocniki wzmianek:

  * `buildMentionRegexes`
  * `matchesMentionPatterns`
  * `matchesMentionWithExplicit`
  * `implicitMentionKindWhen`
  * `resolveInboundMentionDecision`


`api.runtime.channel.mentions` celowo nie udostępnia starszych pomocników zgodności `resolveMentionGating*`. Preferuj znormalizowaną ścieżkę `{ facts, policy }`.

## Przechowywanie odwołań do środowiska uruchomieniowego

Użyj `createPluginRuntimeStore`, aby przechowywać odwołanie do środowiska uruchomieniowego do użycia poza wywołaniem zwrotnym `register`:

* ### Utwórz magazyn

typescriptCopy code
[code]
    import { createPluginRuntimeStore } from "openclaw/plugin-sdk/runtime-store";import type { PluginRuntime } from "openclaw/plugin-sdk/runtime-store"; const store = createPluginRuntimeStore&lt;PluginRuntime&gt;({  pluginId: "my-plugin",  errorMessage: "my-plugin runtime not initialized",});
[/code]

* ### Podłącz w punkcie wejścia

typescriptCopy code
[code]
    export default defineChannelPluginEntry({  id: "my-plugin",  name: "My Plugin",  description: "Example",  plugin: myPlugin,  setRuntime: store.setRuntime,});
[/code]

* ### Uzyskaj dostęp z innych plików

typescriptCopy code
[code]
    export function getRuntime() {  return store.getRuntime(); // throws if not initialized} export function tryGetRuntime() {  return store.tryGetRuntime(); // returns null if not initialized}
[/code]

## Inne pola najwyższego poziomu `api`

Poza `api.runtime` obiekt API udostępnia także:

Identyfikator Plugin.

Nazwa wyświetlana Plugin.

Bieżąca migawka konfiguracji (aktywna migawka środowiska uruchomieniowego w pamięci, gdy jest dostępna).

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaS5wbHVnaW5Db25maWciIHR5cGU9IlJlY29yZDxzdHJpbmcsIHVua25vd24 "> Konfiguracja specyficzna dla Plugin z `plugins.entries.<id>.config`.

Logger o określonym zakresie (`debug`, `info`, `warn`, `error`).

Bieżący tryb ładowania; `"setup-runtime"` to lekkie okno uruchamiania/konfiguracji przed pełnym punktem wejścia.

## Powiązane

  * [Wewnętrzne mechanizmy Plugin](</pl/plugins/architecture>) — model możliwości i rejestr
  * [Punkty wejścia SDK](</pl/plugins/sdk-entrypoints>) — opcje `definePluginEntry`
  * [Omówienie SDK](</pl/plugins/sdk-overview>) — dokumentacja ścieżek podrzędnych


Was this useful?YesNo