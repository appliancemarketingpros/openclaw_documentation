---
title: Plugin: вспомогательные средства среды выполнения
source_url: https://docs.openclaw.ai/ru/plugins/sdk-runtime
scraped_at: 2026-06-29
---

ReferencePlugin SDK reference

Справочник по объекту `api.runtime`, внедряемому в каждый плагин при регистрации. Используйте эти помощники вместо прямого импорта внутренних модулей хоста.

[**Channel plugins** Пошаговое руководство, использующее эти помощники в контексте плагинов каналов. ](</ru/plugins/sdk-channel-plugins>) [**Provider plugins** Пошаговое руководство, использующее эти помощники в контексте плагинов провайдеров. ](</ru/plugins/sdk-provider-plugins>)

typescriptCopy code
[code]
    register(api) {  const runtime = api.runtime;}
[/code]

## Загрузка и запись конфигурации

Предпочитайте конфигурацию, которая уже была передана в активный путь вызова, например `api.config` при регистрации или аргумент `cfg` в обратных вызовах канала/провайдера. Так один снимок процесса проходит через работу без повторного разбора конфигурации на горячих путях.

Используйте `api.runtime.config.current()` только когда долгоживущему обработчику нужен текущий снимок процесса и в эту функцию не была передана конфигурация. Возвращаемое значение доступно только для чтения; перед редактированием клонируйте его или используйте помощник мутации.

Фабрики инструментов получают `ctx.runtimeConfig` и `ctx.getRuntimeConfig()`. Используйте getter внутри обратного вызова `execute` долгоживущего инструмента, когда конфигурация может измениться после создания определения инструмента.

Сохраняйте изменения с помощью `api.runtime.config.mutateConfigFile(...)` или `api.runtime.config.replaceConfigFile(...)`. Каждая запись должна выбрать явную политику `afterWrite`:

  * `afterWrite: { mode: "auto" }` позволяет механизму перезагрузки Gateway принять решение.
  * `afterWrite: { mode: "restart", reason: "..." }` принудительно выполняет чистый перезапуск, когда записывающая сторона знает, что горячая перезагрузка небезопасна.
  * `afterWrite: { mode: "none", reason: "..." }` подавляет автоматическую перезагрузку/перезапуск только когда вызывающая сторона сама отвечает за последующие действия.


Помощники мутации возвращают `afterWrite` и типизированную сводку `followUp`, чтобы вызывающие стороны могли логировать или тестировать, запросили ли они перезапуск. Gateway по-прежнему отвечает за то, когда этот перезапуск фактически произойдет.

`api.runtime.config.loadConfig()` и `api.runtime.config.writeConfigFile(...)` являются устаревшими помощниками совместимости под `runtime-config-load-write`. Они один раз предупреждают во время выполнения и остаются доступными для старых внешних плагинов в течение окна миграции. Встроенные плагины не должны их использовать; защитные проверки границы конфигурации завершаются ошибкой, если код плагина вызывает их или импортирует эти помощники из подпутей SDK плагина.

Для прямого импорта SDK используйте специализированные подпути конфигурации вместо широкого совместимого barrel `openclaw/plugin-sdk/config-runtime`: `config-contracts` для типов, `plugin-config-runtime` для утверждений уже загруженной конфигурации и поиска точки входа плагина, `runtime-config-snapshot` для текущих снимков процесса и `config-mutation` для записей. Тесты встроенных плагинов должны напрямую мокировать эти специализированные подпути вместо мокирования широкого совместимого barrel.

Внутренний runtime-код OpenClaw следует тому же направлению: загрузить конфигурацию один раз на границе CLI, Gateway или процесса, затем передавать это значение дальше. Успешные записи мутаций обновляют снимок runtime процесса и продвигают его внутреннюю ревизию; долгоживущие кэши должны использовать ключ кэша, принадлежащий runtime, вместо локальной сериализации конфигурации. Для долгоживущих runtime-модулей действует сканер с нулевой терпимостью к фоновым вызовам `loadConfig()`; используйте переданный `cfg`, request `context.getRuntimeConfig()` или `getRuntimeConfig()` на явной границе процесса.

Пути выполнения провайдера и канала должны использовать активный снимок runtime-конфигурации, а не файловый снимок, возвращенный для чтения или редактирования конфигурации. Файловые снимки сохраняют исходные значения, такие как маркеры SecretRef, для UI и записей; обратным вызовам провайдера нужен разрешенный runtime-вид. Когда помощник может быть вызван как с активным исходным снимком, так и с активным runtime-снимком, перед чтением учетных данных направляйте вызов через `selectApplicableRuntimeConfig()`.

## Переиспользуемые runtime-утилиты

Используйте входящие факты `botLoopProtection` для входящих сообщений, созданных ботом. Core применяет общий in-memory sliding-window guard до записи сессии и dispatch, не привязывая политику к одному каналу. Guard отслеживает ключи `(scopeId, conversationId, participant pair)`, считает оба направления пары вместе, применяет cooldown после превышения бюджета окна и оппортунистически удаляет неактивные записи.

Плагины каналов, которые раскрывают это поведение операторам, должны предпочитать общую форму `channels.defaults.botLoopProtection` для базовых бюджетов, а затем накладывать сверху переопределения, специфичные для канала/провайдера. Общая конфигурация использует секунды, потому что она видима пользователю:

typescriptCopy code
[code]
    type ChannelBotLoopProtectionConfig = {  enabled?: boolean;  maxEventsPerWindow?: number;  windowSeconds?: number;  cooldownSeconds?: number;};
[/code]

Передавайте нормализованные факты пары ботов вместе с разрешенным turn. Core разрешает значения по умолчанию, преобразование единиц и семантику `enabled`:

typescriptCopy code
[code]
    return {  channel: "example",  routeSessionKey,  storePath,  ctxPayload,  recordInboundSession,  runDispatch,  botLoopProtection: {    scopeId: "account-1",    conversationId: "channel-1",    senderId: "bot-a",    receiverId: "bot-b",    config: channelConfig.botLoopProtection,    defaultsConfig: runtimeConfig.channels?.defaults?.botLoopProtection,    defaultEnabled: allowBotsMode !== "off",  },};
[/code]

Используйте `openclaw/plugin-sdk/pair-loop-guard-runtime` напрямую только для пользовательских двухсторонних event loop, которые не проходят через общий inbound reply runner.

## Пространства имен runtime

api.runtime.agent

Идентичность агента, каталоги и управление сессиями.

typescriptCopy code
[code]
    // Resolve the agent's working directoryconst agentDir = api.runtime.agent.resolveAgentDir(cfg); // Resolve agent workspaceconst workspaceDir = api.runtime.agent.resolveAgentWorkspaceDir(cfg); // Get agent identityconst identity = api.runtime.agent.resolveAgentIdentity(cfg); // Get default thinking levelconst thinking = api.runtime.agent.resolveThinkingDefault({  cfg,  provider,  model,}); // Validate a user-provided thinking level against the active provider profileconst policy = api.runtime.agent.resolveThinkingPolicy({ provider, model });const level = api.runtime.agent.normalizeThinkingLevel("extra high");if (level && policy.levels.some((entry) => entry.id === level)) {  // pass level to an embedded run} // Get agent timeoutconst timeoutMs = api.runtime.agent.resolveAgentTimeoutMs(cfg); // Ensure workspace existsawait api.runtime.agent.ensureAgentWorkspace(cfg); // Run an embedded agent turnconst result = await api.runtime.agent.runEmbeddedAgent({  sessionId: "my-plugin:task-1",  runId: crypto.randomUUID(),  workspaceDir: api.runtime.agent.resolveAgentWorkspaceDir(cfg),  prompt: "Summarize the latest changes",  timeoutMs: api.runtime.agent.resolveAgentTimeoutMs(cfg),});
[/code]

`runEmbeddedAgent(...)` — нейтральный помощник для запуска обычного хода агента OpenClaw из кода плагина. Он использует то же разрешение провайдера/модели и выбор agent-harness, что и ответы, запущенные каналом.

`runEmbeddedPiAgent(...)` остается устаревшим совместимым алиасом для существующих плагинов. Новый код должен использовать `runEmbeddedAgent(...)`.

`resolveThinkingPolicy(...)` возвращает поддерживаемые провайдером/моделью уровни thinking и необязательное значение по умолчанию. Плагины провайдеров владеют профилем конкретной модели через свои thinking hooks, поэтому плагины инструментов должны вызывать этот runtime-помощник вместо импорта или дублирования списков провайдеров.

`normalizeThinkingLevel(...)` преобразует пользовательский текст, такой как `on`, `x-high` или `extra high`, в канонический сохраняемый уровень перед проверкой по разрешенной политике.

**Помощники хранилища сессий** находятся в `api.runtime.agent.session`:

typescriptCopy code
[code]
    const entry = api.runtime.agent.session.getSessionEntry({ agentId, sessionKey });for (const { sessionKey, entry } of api.runtime.agent.session.listSessionEntries({ agentId })) {  // Iterate session rows without depending on the legacy sessions.json shape.}await api.runtime.agent.session.patchSessionEntry({  agentId,  sessionKey,  update: (entry) => ({ thinkingLevel: "high" }),});
[/code]

Предпочитайте `getSessionEntry(...)`, `listSessionEntries(...)`, `patchSessionEntry(...)` или `upsertSessionEntry(...)` для рабочих процессов сессий. Эти помощники адресуют сессии по идентичности агента/сессии, чтобы плагины не зависели от устаревшей формы хранилища `sessions.json`. Используйте `preserveActivity: true` для патчей только метаданных, которые не должны обновлять активность сессии, и `replaceEntry: true` только когда обратный вызов возвращает полную запись, а удаленные поля должны остаться удаленными.

Для чтения и записи транскриптов импортируйте `openclaw/plugin-sdk/session-transcript-runtime` и используйте `resolveSessionTranscriptIdentity(...)`, `resolveSessionTranscriptTarget(...)`, `readSessionTranscriptEvents(...)`, `appendSessionTranscriptMessageByIdentity(...)`, `publishSessionTranscriptUpdateByIdentity(...)` или `withSessionTranscriptWriteLock(...)` с `{ agentId, sessionKey, sessionId }`. Эти API позволяют плагинам идентифицировать транскрипт, читать его события, добавлять сообщения, публиковать обновления и выполнять связанные операции под той же блокировкой записи транскрипта. Передача `sessionFile`, использование `resolveSessionTranscriptLegacyFileTarget(...)` или импорт низкоуровневых `appendSessionTranscriptMessage(...)` / `emitSessionTranscriptUpdate(...)` из `openclaw/plugin-sdk/agent-harness-runtime` устарели; эти пути существуют только для legacy-кода, который уже получает активный артефакт транскрипта.

`loadSessionStore(...)`, `saveSessionStore(...)`, `updateSessionStore(...)`, `resolveSessionFilePath(...)` и `resolveAndPersistSessionFile(...)` являются устаревшими помощниками совместимости для плагинов, которые все еще намеренно зависят от устаревшей формы всего хранилища или файла транскрипта. Новый код плагина не должен использовать эти помощники, а существующие вызывающие стороны должны мигрировать на помощники записей и помощники идентичности транскриптов.

api.runtime.agent.defaults

Константы модели и провайдера по умолчанию:

typescriptCopy code
[code]
    const model = api.runtime.agent.defaults.model; // e.g. "anthropic/claude-sonnet-4-6"const provider = api.runtime.agent.defaults.provider; // e.g. "anthropic"
[/code]

api.runtime.llm

Запустите текстовое completion, принадлежащее хосту, без импорта внутренних модулей провайдера или дублирования подготовки модели/аутентификации/base URL OpenClaw.

typescriptCopy code
[code]
    const result = await api.runtime.llm.complete({  messages: [{ role: "user", content: "Summarize this transcript." }],  purpose: "my-plugin.summary",  maxTokens: 512,  temperature: 0.2,});
[/code]

Помощник использует тот же путь подготовки простого completion, что и встроенный runtime OpenClaw, а также принадлежащий хосту снимок runtime-конфигурации. Context engines получают привязанную к сессии возможность `llm.complete`, поэтому вызовы модели используют агента активной сессии и не выполняют молчаливый fallback к агенту по умолчанию. Результат включает атрибуцию провайдера/модели/агента, а также нормализованные данные об использовании токенов, кэша и оценочной стоимости, когда они доступны.

api.runtime.subagent

Запуск и управление фоновыми запусками subagent.

typescriptCopy code
[code]
    // Start a subagent runconst { runId } = await api.runtime.subagent.run({  sessionKey: "agent:main:subagent:search-helper",  message: "Expand this query into focused follow-up searches.",  provider: "openai", // optional override  model: "gpt-4.1-mini", // optional override  deliver: false,}); // Wait for completionconst result = await api.runtime.subagent.waitForRun({ runId, timeoutMs: 30000 }); // Read session messagesconst { messages } = await api.runtime.subagent.getSessionMessages({  sessionKey: "agent:main:subagent:search-helper",  limit: 10,}); // Delete a sessionawait api.runtime.subagent.deleteSession({  sessionKey: "agent:main:subagent:search-helper",});
[/code]

`deleteSession(...)` может удалять сеансы, созданные тем же plugin через `api.runtime.subagent.run(...)`. Удаление произвольных пользовательских или операторских сеансов по-прежнему требует запроса Gateway с областью администратора.

api.runtime.nodes

Выводит список подключенных узлов и вызывает команду хоста узла из кода plugin, загруженного Gateway, или из CLI-команд plugin. Используйте это, когда plugin владеет локальной работой на сопряженном устройстве, например браузером или аудиомостом на другом Mac.

typescriptCopy code
[code]
    const { nodes } = await api.runtime.nodes.list({ connected: true }); const result = await api.runtime.nodes.invoke({  nodeId: "mac-studio",  command: "my-plugin.command",  params: { action: "start" },  timeoutMs: 30000,});
[/code]

Внутри Gateway эта среда выполнения работает внутри процесса. В CLI-командах plugin она вызывает настроенный Gateway через RPC, поэтому команды вроде `openclaw googlemeet recover-tab` могут проверять сопряженные узлы из терминала. Команды узлов по-прежнему проходят через обычное сопряжение узлов Gateway, списки разрешенных команд, политики вызова узлов plugin и локальную обработку команд на узле.

Plugins, которые предоставляют опасные команды хоста узла, должны зарегистрировать политику вызова узлов с помощью `api.registerNodeInvokePolicy(...)`. Политика выполняется в Gateway после проверок списка разрешенных команд и до пересылки команды на узел, поэтому прямые вызовы `node.invoke` и высокоуровневые инструменты plugin используют один и тот же путь принудительного применения.

api.runtime.tasks.managedFlows

Привяжите среду выполнения Task Flow к существующему ключу сеанса OpenClaw или доверенному контексту инструмента, затем создавайте Task Flows и управляйте ими без передачи владельца при каждом вызове.

Task Flow отслеживает долговечное состояние многошагового рабочего процесса. Это не планировщик: используйте Cron или `api.session.workflow.scheduleSessionTurn(...)` для будущих пробуждений, затем используйте `managedFlows` из запланированного хода, когда этой работе нужны состояние потока, дочерние задачи, ожидания или отмена.

typescriptCopy code
[code]
    const taskFlow = api.runtime.tasks.managedFlows.fromToolContext(ctx); const created = taskFlow.createManaged({  controllerId: "my-plugin/review-batch",  goal: "Review new pull requests",}); const child = taskFlow.runTask({  flowId: created.flowId,  runtime: "acp",  childSessionKey: "agent:main:subagent:reviewer",  task: "Review PR #123",  status: "running",  startedAt: Date.now(),}); const waiting = taskFlow.setWaiting({  flowId: created.flowId,  expectedRevision: created.revision,  currentStep: "await-human-reply",  waitJson: { kind: "reply", channel: "telegram" },});
[/code]

Используйте `bindSession({ sessionKey, requesterOrigin })`, когда у вас уже есть доверенный ключ сеанса OpenClaw из собственного слоя привязки. Не выполняйте привязку из необработанного пользовательского ввода.

api.runtime.tts

Синтез речи из текста.

typescriptCopy code
[code]
    // Standard TTSconst clip = await api.runtime.tts.textToSpeech({  text: "Hello from OpenClaw",  cfg: api.config,}); // Telephony-optimized TTSconst telephonyClip = await api.runtime.tts.textToSpeechTelephony({  text: "Hello from OpenClaw",  cfg: api.config,}); // List available voicesconst voices = await api.runtime.tts.listVoices({  provider: "elevenlabs",  cfg: api.config,});
[/code]

Использует базовую конфигурацию `messages.tts` и выбор провайдера. Возвращает аудиобуфер PCM и частоту дискретизации.

api.runtime.mediaUnderstanding

Анализ изображений, аудио и видео.

typescriptCopy code
[code]
    // Describe an imageconst image = await api.runtime.mediaUnderstanding.describeImageFile({  filePath: "/tmp/inbound-photo.jpg",  cfg: api.config,  agentDir: "/tmp/agent",}); // Transcribe audioconst { text } = await api.runtime.mediaUnderstanding.transcribeAudioFile({  filePath: "/tmp/inbound-audio.ogg",  cfg: api.config,  mime: "audio/ogg", // optional, for when MIME cannot be inferred}); // Describe a videoconst video = await api.runtime.mediaUnderstanding.describeVideoFile({  filePath: "/tmp/inbound-video.mp4",  cfg: api.config,}); // Generic file analysisconst result = await api.runtime.mediaUnderstanding.runFile({  filePath: "/tmp/inbound-file.pdf",  cfg: api.config,}); // Structured image extraction through a specific provider/model.// Include at least one image; text inputs are supplemental context.const evidence = await api.runtime.mediaUnderstanding.extractStructuredWithModel({  provider: "codex",  model: "gpt-5.5",  input: [    {      type: "image",      buffer: receiptImageBuffer,      fileName: "receipt.png",      mime: "image/png",    },    { type: "text", text: "Prefer the printed total over handwritten notes." },  ],  instructions: "Extract vendor, total, and searchable tags.",  schemaName: "receipt.evidence",  jsonSchema: {    type: "object",    properties: {      vendor: { type: "string" },      total: { type: "number" },      tags: { type: "array", items: { type: "string" } },    },    required: ["vendor", "total"],  },  cfg: api.config,});
[/code]

Возвращает `{ text: undefined }`, когда вывод не создан (например, входные данные пропущены).

api.runtime.imageGeneration

Генерация изображений.

typescriptCopy code
[code]
    const result = await api.runtime.imageGeneration.generate({  prompt: "A robot painting a sunset",  cfg: api.config,}); const providers = api.runtime.imageGeneration.listProviders({ cfg: api.config });
[/code]

api.runtime.webSearch

Веб-поиск.

typescriptCopy code
[code]
    const providers = api.runtime.webSearch.listProviders({ config: api.config }); const result = await api.runtime.webSearch.search({  config: api.config,  args: { query: "OpenClaw plugin SDK", count: 5 },});
[/code]

api.runtime.media

Низкоуровневые медиаутилиты.

typescriptCopy code
[code]
    const webMedia = await api.runtime.media.loadWebMedia(url);const mime = await api.runtime.media.detectMime(buffer);const kind = api.runtime.media.mediaKindFromMime("image/jpeg"); // "image"const isVoice = api.runtime.media.isVoiceCompatibleAudio(filePath);const metadata = await api.runtime.media.getImageMetadata(filePath);const resized = await api.runtime.media.resizeToJpeg(buffer, { maxWidth: 800 });const terminalQr = await api.runtime.media.renderQrTerminal("https://openclaw.ai");const pngQr = await api.runtime.media.renderQrPngBase64("https://openclaw.ai", {  scale: 6, // 1-12  marginModules: 4, // 0-16});const pngQrDataUrl = await api.runtime.media.renderQrPngDataUrl("https://openclaw.ai");const tmpRoot = resolvePreferredOpenClawTmpDir();const pngQrFile = await api.runtime.media.writeQrPngTempFile("https://openclaw.ai", {  tmpRoot,  dirPrefix: "my-plugin-qr-",  fileName: "qr.png",});
[/code]

api.runtime.config

Текущий снимок конфигурации среды выполнения и транзакционные записи конфигурации. Предпочитайте конфигурацию, которая уже была передана в активный путь вызова; используйте `current()` только когда обработчику напрямую нужен снимок процесса.

typescriptCopy code
[code]
    const cfg = api.runtime.config.current();await api.runtime.config.mutateConfigFile({  afterWrite: { mode: "auto" },  mutate(draft) {    draft.plugins ??= {};  },});
[/code]

`mutateConfigFile(...)` и `replaceConfigFile(...)` возвращают значение `followUp`, например `{ mode: "restart", requiresRestart: true, reason }`, которое фиксирует намерение автора записи, не забирая управление перезапуском у gateway.

api.runtime.system

Утилиты системного уровня.

typescriptCopy code
[code]
    await api.runtime.system.enqueueSystemEvent(event);api.runtime.system.requestHeartbeat({  source: "other",  intent: "event",  reason: "plugin-event",});api.runtime.system.requestHeartbeatNow({ reason: "plugin-event" }); // Deprecated compatibility alias.const output = await api.runtime.system.runCommandWithTimeout(cmd, args, opts);const hint = api.runtime.system.formatNativeDependencyHint(pkg);
[/code]

`runCommandWithTimeout(...)` возвращает захваченные `stdout` и `stderr`, необязательные счетчики усечения, `code`, `signal`, `killed`, `termination` и `noOutputTimedOut`. Результаты тайм-аута и тайм-аута отсутствия вывода сообщают `code: 124`, когда дочерний процесс не предоставляет ненулевой код выхода. Выходы по сигналу без тайм-аута всё еще могут возвращать `code: null`, поэтому используйте `termination` и `noOutputTimedOut`, чтобы различать причины тайм-аута.

api.runtime.events

Подписки на события.

typescriptCopy code
[code]
    api.runtime.events.onAgentEvent((event) => {  /* ... */});api.runtime.events.onSessionTranscriptUpdate((update) => {  /* ... */});
[/code]

api.runtime.logging

Логирование.

typescriptCopy code
[code]
    const verbose = api.runtime.logging.shouldLogVerbose();const childLogger = api.runtime.logging.getChildLogger({ plugin: "my-plugin" }, { level: "debug" });
[/code]

api.runtime.modelAuth

Разрешение аутентификации модели и провайдера.

typescriptCopy code
[code]
    const auth = await api.runtime.modelAuth.getApiKeyForModel({ model, cfg });const providerAuth = await api.runtime.modelAuth.resolveApiKeyForProvider({  provider: "openai",  cfg,});
[/code]

api.runtime.state

Разрешение каталога состояния и хранилище ключей на базе SQLite.

typescriptCopy code
[code]
    const stateDir = api.runtime.state.resolveStateDir(process.env);const store = api.runtime.state.openKeyedStore&lt;MyRecord&gt;({  namespace: "my-feature",  maxEntries: 200,  defaultTtlMs: 15 * 60_000,}); await store.register("key-1", { value: "hello" });const claimed = await store.registerIfAbsent("dedupe-key", { value: "first" });const value = await store.lookup("key-1");await store.consume("key-1");await store.clear();
[/code]

Хранилища с ключами переживают перезапуски и изолированы идентификатором плагина, привязанным к среде выполнения. Используйте `registerIfAbsent(...)` для атомарных заявок дедупликации: он возвращает `true`, когда ключ отсутствовал или истек и был зарегистрирован, либо `false`, когда уже существует активное значение без перезаписи его значения, времени создания или TTL. Ограничения: `maxEntries` на пространство имен, 6 000 активных строк на плагин, JSON-значения меньше 64 КБ и необязательное истечение по TTL. Когда запись превысила бы лимит строк плагина, среда выполнения может вытеснить самые старые активные строки из пространства имен, в которое выполняется запись; соседние пространства имен при этой записи не вытесняются, и запись все равно завершается ошибкой, если пространство имен не может освободить достаточно строк.

api.runtime.tools

Фабрики инструментов памяти и CLI.

typescriptCopy code
[code]
    const getTool = api.runtime.tools.createMemoryGetTool(/* ... */);const searchTool = api.runtime.tools.createMemorySearchTool(/* ... */);api.runtime.tools.registerMemoryCli(/* ... */);
[/code]

api.runtime.channel

Вспомогательные функции среды выполнения для конкретного канала (доступны, когда загружен плагин канала).

`api.runtime.channel.media` — предпочтительная поверхность для загрузок и хранения медиа канала:

typescriptCopy code
[code]
    const saved = await api.runtime.channel.media.saveRemoteMedia({  url,  subdir: "inbound",  maxBytes,  filePathHint: fileName,});
[/code]

Используйте `saveRemoteMedia(...)`, когда удаленный URL должен стать медиа OpenClaw. Используйте `saveResponseMedia(...)`, когда плагин уже получил `Response` с собственной обработкой авторизации, перенаправлений или allowlist. Используйте `readRemoteMediaBuffer(...)` только когда плагину нужны необработанные байты для проверки, преобразований, расшифровки или повторной загрузки. `fetchRemoteMedia(...)` остается устаревшим совместимым псевдонимом для `readRemoteMediaBuffer(...)`.

`api.runtime.channel.mentions` — общая поверхность политики входящих упоминаний для встроенных плагинов каналов, которые используют внедрение среды выполнения:

typescriptCopy code
[code]
    const mentionMatch = api.runtime.channel.mentions.matchesMentionWithExplicit(text, {  mentionRegexes,  mentionPatterns,}); const decision = api.runtime.channel.mentions.resolveInboundMentionDecision({  facts: {    canDetectMention: true,    wasMentioned: mentionMatch.matched,    implicitMentionKinds: api.runtime.channel.mentions.implicitMentionKindWhen(      "reply_to_bot",      isReplyToBot,    ),  },  policy: {    isGroup,    requireMention,    allowTextCommands,    hasControlCommand,    commandAuthorized,  },});
[/code]

Доступные вспомогательные функции упоминаний:

  * `buildMentionRegexes`
  * `matchesMentionPatterns`
  * `matchesMentionWithExplicit`
  * `implicitMentionKindWhen`
  * `resolveInboundMentionDecision`


`api.runtime.channel.mentions` намеренно не предоставляет старые совместимые вспомогательные функции `resolveMentionGating*`. Предпочитайте нормализованный путь `{ facts, policy }`.

## Хранение ссылок среды выполнения

Используйте `createPluginRuntimeStore`, чтобы хранить ссылку среды выполнения для использования вне callback-функции `register`:

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

## Другие поля `api` верхнего уровня

Помимо `api.runtime`, объект API также предоставляет:

Идентификатор Plugin.

Отображаемое имя Plugin.

Текущий снимок конфигурации (активный снимок среды выполнения в памяти, когда доступен).

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaS5wbHVnaW5Db25maWciIHR5cGU9IlJlY29yZDxzdHJpbmcsIHVua25vd24 "> Конфигурация, специфичная для Plugin, из `plugins.entries.<id>.config`.

Логгер с областью (`debug`, `info`, `warn`, `error`).

Текущий режим загрузки; `"setup-runtime"` — легковесное окно запуска/настройки перед полной точкой входа.

## Связанные материалы

  * [Внутреннее устройство Plugin](</ru/plugins/architecture>) — модель возможностей и реестр
  * [Точки входа SDK](</ru/plugins/sdk-entrypoints>) — параметры `definePluginEntry`
  * [Обзор SDK](</ru/plugins/sdk-overview>) — справочник подпутей


Was this useful?YesNo

Open issue