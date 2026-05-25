---
title: Допоміжні засоби середовища виконання для Plugin
source_url: https://docs.openclaw.ai/uk/plugins/sdk-runtime
scraped_at: 2026-05-25
---

Довідник для об’єкта `api.runtime`, який впроваджується в кожен plugin під час реєстрації. Використовуйте ці допоміжні функції замість прямого імпорту внутрішніх модулів хоста.

[**Channel plugins** Покроковий посібник, який показує використання цих допоміжних функцій у контексті для channel plugins. ](</uk/plugins/sdk-channel-plugins>) [**Provider plugins** Покроковий посібник, який показує використання цих допоміжних функцій у контексті для provider plugins. ](</uk/plugins/sdk-provider-plugins>)

typescriptCopy code
[code]
    register(api) {  const runtime = api.runtime;}
[/code]

## Завантаження конфігурації та записи

Надавайте перевагу конфігурації, яку вже було передано в активний шлях виклику, наприклад `api.config` під час реєстрації або аргумент `cfg` у callback-функціях каналу чи провайдера. Так один знімок процесу проходитиме через усю роботу, замість повторного розбору конфігурації на гарячих шляхах.

Використовуйте `api.runtime.config.current()` лише тоді, коли довготривалому обробнику потрібен поточний знімок процесу, а конфігурацію не було передано цій функції. Повернене значення доступне лише для читання; перед редагуванням клонуйте його або скористайтеся допоміжною функцією мутації.

Фабрики інструментів отримують `ctx.runtimeConfig` і `ctx.getRuntimeConfig()`. Використовуйте getter усередині callback-функції `execute` довготривалого інструмента, коли конфігурація може змінитися після створення визначення інструмента.

Зберігайте зміни за допомогою `api.runtime.config.mutateConfigFile(...)` або `api.runtime.config.replaceConfigFile(...)`. Кожен запис має вибрати явну політику `afterWrite`:

  * `afterWrite: { mode: "auto" }` дозволяє планувальнику перезавантаження Gateway ухвалити рішення.
  * `afterWrite: { mode: "restart", reason: "..." }` примусово виконує чистий перезапуск, коли автор запису знає, що гаряче перезавантаження небезпечне.
  * `afterWrite: { mode: "none", reason: "..." }` пригнічує автоматичне перезавантаження чи перезапуск лише тоді, коли викликач сам відповідає за подальші дії.


Допоміжні функції мутації повертають `afterWrite` і типізований підсумок `followUp`, щоб викликачі могли логувати або тестувати, чи вони запитали перезапуск. Gateway і далі відповідає за те, коли цей перезапуск фактично відбудеться.

`api.runtime.config.loadConfig()` і `api.runtime.config.writeConfigFile(...)` є застарілими допоміжними функціями сумісності в межах `runtime-config-load-write`. Вони один раз попереджають під час виконання й залишаються доступними для старих зовнішніх plugins протягом вікна міграції. Вбудовані plugins не повинні їх використовувати; захист межі конфігурації завершується помилкою, якщо код plugin викликає їх або імпортує ці допоміжні функції з підшляхів plugin SDK.

Для прямих імпортів SDK використовуйте спеціалізовані підшляхи конфігурації замість широкого бареля сумісності `openclaw/plugin-sdk/config-runtime`: `config-contracts` для типів, `plugin-config-runtime` для перевірок уже завантаженої конфігурації та пошуку точки входу plugin, `runtime-config-snapshot` для поточних знімків процесу, а `config-mutation` для записів. Тести вбудованих plugin мають мокати ці спеціалізовані підшляхи безпосередньо, а не широкий барель сумісності.

Внутрішній runtime-код OpenClaw має той самий напрям: завантажити конфігурацію один раз на межі CLI, Gateway або процесу, а потім передавати це значення далі. Успішні записи мутації оновлюють runtime-знімок процесу й просувають його внутрішню ревізію; довготривалі кеші мають використовувати ключ кешу, яким володіє runtime, замість локальної серіалізації конфігурації. Довготривалі runtime-модулі мають сканер із нульовою толерантністю до неявних викликів `loadConfig()`; використовуйте переданий `cfg`, запит `context.getRuntimeConfig()` або `getRuntimeConfig()` на явній межі процесу.

Шляхи виконання провайдера й каналу мають використовувати активний знімок runtime-конфігурації, а не файловий знімок, повернений для зворотного читання чи редагування конфігурації. Файлові знімки зберігають вихідні значення, як-от маркери SecretRef, для UI та записів; callback-функціям провайдера потрібне розв’язане runtime-представлення. Коли допоміжну функцію можна викликати як з активним вихідним знімком, так і з активним runtime-знімком, перед читанням облікових даних маршрутизуйте через `selectApplicableRuntimeConfig()`.

## Простори імен runtime

api.runtime.agent

Ідентичність агента, каталоги та керування сесіями.

typescriptCopy code
[code]
    // Resolve the agent's working directoryconst agentDir = api.runtime.agent.resolveAgentDir(cfg); // Resolve agent workspaceconst workspaceDir = api.runtime.agent.resolveAgentWorkspaceDir(cfg); // Get agent identityconst identity = api.runtime.agent.resolveAgentIdentity(cfg); // Get default thinking levelconst thinking = api.runtime.agent.resolveThinkingDefault({  cfg,  provider,  model,}); // Validate a user-provided thinking level against the active provider profileconst policy = api.runtime.agent.resolveThinkingPolicy({ provider, model });const level = api.runtime.agent.normalizeThinkingLevel("extra high");if (level && policy.levels.some((entry) => entry.id === level)) {  // pass level to an embedded run} // Get agent timeoutconst timeoutMs = api.runtime.agent.resolveAgentTimeoutMs(cfg); // Ensure workspace existsawait api.runtime.agent.ensureAgentWorkspace(cfg); // Run an embedded agent turnconst agentDir = api.runtime.agent.resolveAgentDir(cfg);const result = await api.runtime.agent.runEmbeddedAgent({  sessionId: "my-plugin:task-1",  runId: crypto.randomUUID(),  sessionFile: path.join(agentDir, "sessions", "my-plugin-task-1.jsonl"),  workspaceDir: api.runtime.agent.resolveAgentWorkspaceDir(cfg),  prompt: "Summarize the latest changes",  timeoutMs: api.runtime.agent.resolveAgentTimeoutMs(cfg),});
[/code]

`runEmbeddedAgent(...)` — нейтральна допоміжна функція для запуску звичайного ходу агента OpenClaw з коду plugin. Вона використовує те саме розв’язання провайдера й моделі та вибір agent-harness, що й відповіді, запущені каналом.

`runEmbeddedPiAgent(...)` залишається alias сумісності.

`resolveThinkingPolicy(...)` повертає підтримувані рівні мислення провайдера й моделі та необов’язкове значення за замовчуванням. Provider plugins володіють специфічним для моделі профілем через свої thinking hooks, тому tool plugins мають викликати цю runtime-допоміжну функцію замість імпорту чи дублювання списків провайдерів.

`normalizeThinkingLevel(...)` перетворює користувацький текст, як-от `on`, `x-high` або `extra high`, на канонічний збережений рівень перед перевіркою його за розв’язаною політикою.

**Допоміжні функції сховища сесій** розташовані в `api.runtime.agent.session`:

typescriptCopy code
[code]
    const storePath = api.runtime.agent.session.resolveStorePath(cfg);const store = api.runtime.agent.session.loadSessionStore(storePath);await api.runtime.agent.session.updateSessionStore(storePath, (nextStore) => {  // Patch one entry without replacing the whole file from stale state.  nextStore[sessionKey] = { ...nextStore[sessionKey], thinkingLevel: "high" };});const filePath = api.runtime.agent.session.resolveSessionFilePath(cfg, sessionId);
[/code]

Для записів під час виконання надавайте перевагу `updateSessionStore(...)` або `updateSessionStoreEntry(...)`. Вони проходять через записувач сховища сесій, яким володіє Gateway, зберігають паралельні оновлення та повторно використовують гарячий кеш. `saveSessionStore(...)` залишається доступною для сумісності та офлайн-перезаписів у стилі обслуговування.

api.runtime.agent.defaults

Константи стандартної моделі та постачальника:

typescriptCopy code
[code]
    const model = api.runtime.agent.defaults.model; // e.g. "anthropic/claude-sonnet-4-6"const provider = api.runtime.agent.defaults.provider; // e.g. "anthropic"
[/code]

api.runtime.llm

Запустіть текстове завершення, яким володіє хост, без імпорту внутрішніх компонентів постачальника або дублювання підготовки моделі, автентифікації чи базової URL-адреси OpenClaw.

typescriptCopy code
[code]
    const result = await api.runtime.llm.complete({  messages: [{ role: "user", content: "Summarize this transcript." }],  purpose: "my-plugin.summary",  maxTokens: 512,  temperature: 0.2,});
[/code]

Допоміжна функція використовує той самий шлях підготовки простого завершення, що й вбудоване середовище виконання OpenClaw, а також знімок конфігурації середовища виконання, яким володіє хост. Рушії контексту отримують прив’язану до сесії можливість `llm.complete`, тому виклики моделі використовують агента активної сесії та не повертаються непомітно до стандартного агента. Результат містить атрибуцію постачальника, моделі й агента, а також нормалізоване використання токенів, кешу та орієнтовної вартості, якщо доступно.

api.runtime.subagent

Запускайте та керуйте фоновими виконаннями підагентів.

typescriptCopy code
[code]
    // Start a subagent runconst { runId } = await api.runtime.subagent.run({  sessionKey: "agent:main:subagent:search-helper",  message: "Expand this query into focused follow-up searches.",  provider: "openai", // optional override  model: "gpt-4.1-mini", // optional override  deliver: false,}); // Wait for completionconst result = await api.runtime.subagent.waitForRun({ runId, timeoutMs: 30000 }); // Read session messagesconst { messages } = await api.runtime.subagent.getSessionMessages({  sessionKey: "agent:main:subagent:search-helper",  limit: 10,}); // Delete a sessionawait api.runtime.subagent.deleteSession({  sessionKey: "agent:main:subagent:search-helper",});
[/code]

`deleteSession(...)` може видаляти сесії, створені тим самим плагіном через `api.runtime.subagent.run(...)`. Видалення довільних користувацьких або операторських сесій усе ще потребує Gateway-запиту з областю адміністратора.

api.runtime.nodes

Перелічуйте підключені вузли та викликайте команду, розміщену на вузлі, з коду плагіна, завантаженого Gateway, або з CLI-команд плагіна. Використовуйте це, коли плагін володіє локальною роботою на спареному пристрої, наприклад мостом браузера чи аудіо на іншому Mac.

typescriptCopy code
[code]
    const { nodes } = await api.runtime.nodes.list({ connected: true }); const result = await api.runtime.nodes.invoke({  nodeId: "mac-studio",  command: "my-plugin.command",  params: { action: "start" },  timeoutMs: 30000,});
[/code]

Усередині Gateway це середовище виконання є внутрішньопроцесним. У CLI-командах плагіна воно викликає налаштований Gateway через RPC, тож команди на кшталт `openclaw googlemeet recover-tab` можуть перевіряти спарені вузли з термінала. Команди вузлів і надалі проходять через звичайне спарювання вузлів Gateway, списки дозволених команд, політики виклику вузлів плагіна та локальну обробку команд вузла.

Плагіни, які надають небезпечні команди, розміщені на вузлі, мають зареєструвати політику виклику вузлів за допомогою `api.registerNodeInvokePolicy(...)`. Політика виконується в Gateway після перевірок списку дозволених команд і перед пересиланням команди вузлу, тому прямі виклики `node.invoke` та інструменти плагінів вищого рівня використовують той самий шлях примусового застосування.

api.runtime.tasks.managedFlows

Прив’яжіть середовище виконання Task Flow до наявного ключа сесії OpenClaw або довіреного контексту інструмента, а потім створюйте й керуйте Task Flows без передавання власника в кожному виклику.

Task Flow відстежує довговічний стан багатоетапного робочого процесу. Це не планувальник: використовуйте Cron або `api.session.workflow.scheduleSessionTurn(...)` для майбутніх пробуджень, а потім використовуйте `managedFlows` із запланованого ходу, коли ця робота потребує стану потоку, дочірніх завдань, очікувань або скасування.

typescriptCopy code
[code]
    const taskFlow = api.runtime.tasks.managedFlows.fromToolContext(ctx); const created = taskFlow.createManaged({  controllerId: "my-plugin/review-batch",  goal: "Review new pull requests",}); const child = taskFlow.runTask({  flowId: created.flowId,  runtime: "acp",  childSessionKey: "agent:main:subagent:reviewer",  task: "Review PR #123",  status: "running",  startedAt: Date.now(),}); const waiting = taskFlow.setWaiting({  flowId: created.flowId,  expectedRevision: created.revision,  currentStep: "await-human-reply",  waitJson: { kind: "reply", channel: "telegram" },});
[/code]

Використовуйте `bindSession({ sessionKey, requesterOrigin })`, коли у вас уже є довірений ключ сесії OpenClaw із власного шару прив’язування. Не прив’язуйте з необробленого введення користувача.

api.runtime.tts

Синтез мовлення з тексту.

typescriptCopy code
[code]
    // Standard TTSconst clip = await api.runtime.tts.textToSpeech({  text: "Hello from OpenClaw",  cfg: api.config,}); // Telephony-optimized TTSconst telephonyClip = await api.runtime.tts.textToSpeechTelephony({  text: "Hello from OpenClaw",  cfg: api.config,}); // List available voicesconst voices = await api.runtime.tts.listVoices({  provider: "elevenlabs",  cfg: api.config,});
[/code]

Використовує основну конфігурацію `messages.tts` і вибір провайдера. Повертає аудіобуфер PCM + частоту дискретизації.

api.runtime.mediaUnderstanding

Аналіз зображень, аудіо та відео.

typescriptCopy code
[code]
    // Describe an imageconst image = await api.runtime.mediaUnderstanding.describeImageFile({  filePath: "/tmp/inbound-photo.jpg",  cfg: api.config,  agentDir: "/tmp/agent",}); // Transcribe audioconst { text } = await api.runtime.mediaUnderstanding.transcribeAudioFile({  filePath: "/tmp/inbound-audio.ogg",  cfg: api.config,  mime: "audio/ogg", // optional, for when MIME cannot be inferred}); // Describe a videoconst video = await api.runtime.mediaUnderstanding.describeVideoFile({  filePath: "/tmp/inbound-video.mp4",  cfg: api.config,}); // Generic file analysisconst result = await api.runtime.mediaUnderstanding.runFile({  filePath: "/tmp/inbound-file.pdf",  cfg: api.config,}); // Structured image extraction through a specific provider/model.// Include at least one image; text inputs are supplemental context.const evidence = await api.runtime.mediaUnderstanding.extractStructuredWithModel({  provider: "codex",  model: "gpt-5.5",  input: [    {      type: "image",      buffer: receiptImageBuffer,      fileName: "receipt.png",      mime: "image/png",    },    { type: "text", text: "Prefer the printed total over handwritten notes." },  ],  instructions: "Extract vendor, total, and searchable tags.",  schemaName: "receipt.evidence",  jsonSchema: {    type: "object",    properties: {      vendor: { type: "string" },      total: { type: "number" },      tags: { type: "array", items: { type: "string" } },    },    required: ["vendor", "total"],  },  cfg: api.config,});
[/code]

Повертає `{ text: undefined }`, коли результат не створено (наприклад, пропущене введення).

api.runtime.imageGeneration

Генерація зображень.

typescriptCopy code
[code]
    const result = await api.runtime.imageGeneration.generate({  prompt: "A robot painting a sunset",  cfg: api.config,}); const providers = api.runtime.imageGeneration.listProviders({ cfg: api.config });
[/code]

api.runtime.webSearch

Вебпошук.

typescriptCopy code
[code]
    const providers = api.runtime.webSearch.listProviders({ config: api.config }); const result = await api.runtime.webSearch.search({  config: api.config,  args: { query: "OpenClaw plugin SDK", count: 5 },});
[/code]

api.runtime.media

Низькорівневі медіаутиліти.

typescriptCopy code
[code]
    const webMedia = await api.runtime.media.loadWebMedia(url);const mime = await api.runtime.media.detectMime(buffer);const kind = api.runtime.media.mediaKindFromMime("image/jpeg"); // "image"const isVoice = api.runtime.media.isVoiceCompatibleAudio(filePath);const metadata = await api.runtime.media.getImageMetadata(filePath);const resized = await api.runtime.media.resizeToJpeg(buffer, { maxWidth: 800 });const terminalQr = await api.runtime.media.renderQrTerminal("https://openclaw.ai");const pngQr = await api.runtime.media.renderQrPngBase64("https://openclaw.ai", {  scale: 6, // 1-12  marginModules: 4, // 0-16});const pngQrDataUrl = await api.runtime.media.renderQrPngDataUrl("https://openclaw.ai");const tmpRoot = resolvePreferredOpenClawTmpDir();const pngQrFile = await api.runtime.media.writeQrPngTempFile("https://openclaw.ai", {  tmpRoot,  dirPrefix: "my-plugin-qr-",  fileName: "qr.png",});
[/code]

api.runtime.config

Поточний знімок конфігурації runtime і транзакційні записи конфігурації. Надавайте перевагу конфігурації, яку вже передано в активний шлях виклику; використовуйте `current()` лише тоді, коли обробнику безпосередньо потрібен знімок процесу.

typescriptCopy code
[code]
    const cfg = api.runtime.config.current();await api.runtime.config.mutateConfigFile({  afterWrite: { mode: "auto" },  mutate(draft) {    draft.plugins ??= {};  },});
[/code]

`mutateConfigFile(...)` і `replaceConfigFile(...)` повертають значення `followUp`, наприклад `{ mode: "restart", requiresRestart: true, reason }`, яке фіксує намір записувача, не забираючи керування перезапуском у gateway.

api.runtime.system

Утиліти системного рівня.

typescriptCopy code
[code]
    await api.runtime.system.enqueueSystemEvent(event);api.runtime.system.requestHeartbeat({  source: "other",  intent: "event",  reason: "plugin-event",});api.runtime.system.requestHeartbeatNow({ reason: "plugin-event" }); // Deprecated compatibility alias.const output = await api.runtime.system.runCommandWithTimeout(cmd, args, opts);const hint = api.runtime.system.formatNativeDependencyHint(pkg);
[/code]

api.runtime.events

Підписки на події.

typescriptCopy code
[code]
    api.runtime.events.onAgentEvent((event) => {  /* ... */});api.runtime.events.onSessionTranscriptUpdate((update) => {  /* ... */});
[/code]

api.runtime.logging

Журналювання.

typescriptCopy code
[code]
    const verbose = api.runtime.logging.shouldLogVerbose();const childLogger = api.runtime.logging.getChildLogger({ plugin: "my-plugin" }, { level: "debug" });
[/code]

api.runtime.modelAuth

Розв’язання автентифікації моделі та провайдера.

typescriptCopy code
[code]
    const auth = await api.runtime.modelAuth.getApiKeyForModel({ model, cfg });const providerAuth = await api.runtime.modelAuth.resolveApiKeyForProvider({  provider: "openai",  cfg,});
[/code]

api.runtime.state

Розв’язання каталогу стану та сховище ключів на базі SQLite.

typescriptCopy code
[code]
    const stateDir = api.runtime.state.resolveStateDir(process.env);const store = api.runtime.state.openKeyedStore&lt;MyRecord&gt;({  namespace: "my-feature",  maxEntries: 200,  defaultTtlMs: 15 * 60_000,}); await store.register("key-1", { value: "hello" });const claimed = await store.registerIfAbsent("dedupe-key", { value: "first" });const value = await store.lookup("key-1");await store.consume("key-1");await store.clear();
[/code]

Сховища ключів переживають перезапуски й ізолюються за прив’язаним до runtime ідентифікатором plugin. Використовуйте `registerIfAbsent(...)` для атомарних заявок дедуплікації: він повертає `true`, коли ключ був відсутній або прострочений і зареєстрований, або `false`, коли активне значення вже існує без перезапису його значення, часу створення чи TTL. Обмеження: `maxEntries` на простір імен, 1 000 активних рядків на plugin, JSON-значення до 64KB і необов’язкове завершення строку TTL.

api.runtime.tools

Фабрики інструментів пам’яті та CLI.

typescriptCopy code
[code]
    const getTool = api.runtime.tools.createMemoryGetTool(/* ... */);const searchTool = api.runtime.tools.createMemorySearchTool(/* ... */);api.runtime.tools.registerMemoryCli(/* ... */);
[/code]

api.runtime.channel

Допоміжні засоби runtime для конкретного каналу (доступні, коли завантажено plugin каналу).

`api.runtime.channel.mentions` — це спільна поверхня політики вхідних згадок для вбудованих plugins каналів, які використовують ін’єкцію runtime:

typescriptCopy code
[code]
    const mentionMatch = api.runtime.channel.mentions.matchesMentionWithExplicit(text, {  mentionRegexes,  mentionPatterns,}); const decision = api.runtime.channel.mentions.resolveInboundMentionDecision({  facts: {    canDetectMention: true,    wasMentioned: mentionMatch.matched,    implicitMentionKinds: api.runtime.channel.mentions.implicitMentionKindWhen(      "reply_to_bot",      isReplyToBot,    ),  },  policy: {    isGroup,    requireMention,    allowTextCommands,    hasControlCommand,    commandAuthorized,  },});
[/code]

Доступні допоміжні засоби для згадок:

  * `buildMentionRegexes`
  * `matchesMentionPatterns`
  * `matchesMentionWithExplicit`
  * `implicitMentionKindWhen`
  * `resolveInboundMentionDecision`


`api.runtime.channel.mentions` навмисно не надає старі допоміжні засоби сумісності `resolveMentionGating*`. Надавайте перевагу нормалізованому шляху `{ facts, policy }`.

## Зберігання посилань runtime

Використовуйте `createPluginRuntimeStore`, щоб зберегти посилання runtime для використання поза callback-функцією `register`:

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

## Інші поля верхнього рівня `api`

Окрім `api.runtime`, об’єкт API також надає:

Ідентифікатор Plugin.

Відображувана назва Plugin.

Поточний знімок конфігурації (активний знімок runtime у пам'яті, коли доступний).

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaS5wbHVnaW5Db25maWciIHR5cGU9IlJlY29yZDxzdHJpbmcsIHVua25vd24 "> Конфігурація, специфічна для Plugin, з `plugins.entries.<id>.config`.

Логер із заданою областю (`debug`, `info`, `warn`, `error`).

Поточний режим завантаження; `"setup-runtime"` — це полегшене вікно запуску/налаштування перед повним входом.

## Пов'язане

  * [Внутрішні механізми Plugin](</uk/plugins/architecture>) — модель можливостей і реєстр
  * [Точки входу SDK](</uk/plugins/sdk-entrypoints>) — параметри `definePluginEntry`
  * [Огляд SDK](</uk/plugins/sdk-overview>) — довідник підшляхів


Was this useful?YesNo