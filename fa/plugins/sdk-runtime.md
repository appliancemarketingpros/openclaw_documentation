---
title: کمک‌کننده‌های زمان اجرای Plugin
source_url: https://docs.openclaw.ai/fa/plugins/sdk-runtime
scraped_at: 2026-05-25
---

مرجع شیء `api.runtime` که هنگام ثبت، به هر Plugin تزریق می‌شود. از این helperها به‌جای وارد کردن مستقیم داخلی‌های میزبان استفاده کنید.

[**Channel plugins** راهنمای گام‌به‌گام که از این helperها در زمینهٔ Pluginهای کانال استفاده می‌کند. ](</fa/plugins/sdk-channel-plugins>) [**Provider plugins** راهنمای گام‌به‌گام که از این helperها در زمینهٔ Pluginهای ارائه‌دهنده استفاده می‌کند. ](</fa/plugins/sdk-provider-plugins>)

typescriptCopy code
[code]
    register(api) {  const runtime = api.runtime;}
[/code]

## بارگذاری و نوشتن پیکربندی

پیکربندی‌ای را ترجیح دهید که از قبل به مسیر فراخوانی فعال پاس داده شده است؛ برای مثال `api.config` هنگام ثبت، یا آرگومان `cfg` در callbackهای کانال/ارائه‌دهنده. این کار باعث می‌شود به‌جای پارس دوبارهٔ پیکربندی در مسیرهای داغ، یک snapshot فرایندی در طول کار جریان داشته باشد.

فقط وقتی از `api.runtime.config.current()` استفاده کنید که یک handler بلندعمر به snapshot فعلی فرایند نیاز دارد و هیچ پیکربندی‌ای به آن تابع پاس داده نشده است. مقدار برگشتی readonly است؛ پیش از ویرایش، آن را clone کنید یا از یک helper جهش استفاده کنید.

factoryهای ابزار `ctx.runtimeConfig` به‌علاوهٔ `ctx.getRuntimeConfig()` را دریافت می‌کنند. وقتی پیکربندی می‌تواند پس از ساخته شدن تعریف ابزار تغییر کند، از getter داخل callback `execute` یک ابزار بلندعمر استفاده کنید.

تغییرات را با `api.runtime.config.mutateConfigFile(...)` یا `api.runtime.config.replaceConfigFile(...)` پایدار کنید. هر نوشتن باید یک policy صریح `afterWrite` انتخاب کند:

  * `afterWrite: { mode: "auto" }` اجازه می‌دهد تصمیم reload برنامه‌ریز Gateway انجام شود.
  * `afterWrite: { mode: "restart", reason: "..." }` وقتی نویسنده می‌داند hot reload ناامن است، یک restart تمیز را اجبار می‌کند.
  * `afterWrite: { mode: "none", reason: "..." }` فقط وقتی reload/restart خودکار را سرکوب می‌کند که فراخواننده مالک پیگیری باشد.


helperهای جهش، `afterWrite` به‌علاوهٔ یک خلاصهٔ typed به نام `followUp` برمی‌گردانند تا فراخواننده‌ها بتوانند ثبت یا آزمایش کنند که آیا restart درخواست کرده‌اند یا نه. Gateway همچنان مالک این است که آن restart عملا چه زمانی رخ دهد.

`api.runtime.config.loadConfig()` و `api.runtime.config.writeConfigFile(...)` helperهای سازگاری منسوخ‌شده تحت `runtime-config-load-write` هستند. آن‌ها در زمان اجرا یک‌بار هشدار می‌دهند و طی پنجرهٔ مهاجرت برای Pluginهای خارجی قدیمی در دسترس می‌مانند. Pluginهای bundled نباید از آن‌ها استفاده کنند؛ اگر کد Plugin آن‌ها را فراخوانی کند یا آن helperها را از subpathهای SDK Plugin وارد کند، نگهبان‌های مرز پیکربندی fail می‌شوند.

برای importهای مستقیم SDK، به‌جای barrel سازگاری گستردهٔ `openclaw/plugin-sdk/config-runtime` از subpathهای متمرکز پیکربندی استفاده کنید: `config-contracts` برای typeها، `plugin-config-runtime` برای assertionهای پیکربندی از قبل بارگذاری‌شده و lookup ورودی Plugin، `runtime-config-snapshot` برای snapshotهای فعلی فرایند، و `config-mutation` برای نوشتن‌ها. تست‌های Pluginهای bundled باید همین subpathهای متمرکز را مستقیما mock کنند، نه barrel سازگاری گسترده را.

کد داخلی runtime OpenClaw نیز همین جهت را دارد: پیکربندی را یک‌بار در مرز CLI، Gateway، یا فرایند بارگذاری کنید، سپس آن مقدار را عبور دهید. نوشتن‌های جهش موفق، snapshot runtime فرایند را refresh می‌کنند و revision داخلی آن را جلو می‌برند؛ cacheهای بلندعمر باید به‌جای serialize کردن محلی پیکربندی، بر اساس کلید cache متعلق به runtime key شوند. ماژول‌های runtime بلندعمر برای فراخوانی‌های ambient `loadConfig()` اسکنر با تحمل صفر دارند؛ از `cfg` پاس‌داده‌شده، `context.getRuntimeConfig()` درخواست، یا `getRuntimeConfig()` در یک مرز صریح فرایند استفاده کنید.

مسیرهای اجرای ارائه‌دهنده و کانال باید از snapshot پیکربندی runtime فعال استفاده کنند، نه snapshot فایل که برای readback یا ویرایش پیکربندی برگردانده شده است. snapshotهای فایل مقدارهای منبع مانند نشانگرهای SecretRef را برای UI و نوشتن‌ها حفظ می‌کنند؛ callbackهای ارائه‌دهنده به نمای runtime حل‌شده نیاز دارند. وقتی یک helper ممکن است با snapshot منبع فعال یا snapshot runtime فعال فراخوانی شود، پیش از خواندن credentials از مسیر `selectApplicableRuntimeConfig()` عبور دهید.

## namespaceهای runtime

api.runtime.agent

هویت agent، دایرکتوری‌ها، و مدیریت session.

typescriptCopy code
[code]
    // Resolve the agent's working directoryconst agentDir = api.runtime.agent.resolveAgentDir(cfg); // Resolve agent workspaceconst workspaceDir = api.runtime.agent.resolveAgentWorkspaceDir(cfg); // Get agent identityconst identity = api.runtime.agent.resolveAgentIdentity(cfg); // Get default thinking levelconst thinking = api.runtime.agent.resolveThinkingDefault({  cfg,  provider,  model,}); // Validate a user-provided thinking level against the active provider profileconst policy = api.runtime.agent.resolveThinkingPolicy({ provider, model });const level = api.runtime.agent.normalizeThinkingLevel("extra high");if (level && policy.levels.some((entry) => entry.id === level)) {  // pass level to an embedded run} // Get agent timeoutconst timeoutMs = api.runtime.agent.resolveAgentTimeoutMs(cfg); // Ensure workspace existsawait api.runtime.agent.ensureAgentWorkspace(cfg); // Run an embedded agent turnconst agentDir = api.runtime.agent.resolveAgentDir(cfg);const result = await api.runtime.agent.runEmbeddedAgent({  sessionId: "my-plugin:task-1",  runId: crypto.randomUUID(),  sessionFile: path.join(agentDir, "sessions", "my-plugin-task-1.jsonl"),  workspaceDir: api.runtime.agent.resolveAgentWorkspaceDir(cfg),  prompt: "Summarize the latest changes",  timeoutMs: api.runtime.agent.resolveAgentTimeoutMs(cfg),});
[/code]

`runEmbeddedAgent(...)` helper خنثی برای شروع یک نوبت agent معمولی OpenClaw از کد Plugin است. از همان resolution ارائه‌دهنده/مدل و انتخاب agent-harness استفاده می‌کند که پاسخ‌های triggerشده توسط کانال استفاده می‌کنند.

`runEmbeddedPiAgent(...)` به‌عنوان alias سازگاری باقی می‌ماند.

`resolveThinkingPolicy(...)` سطح‌های thinking پشتیبانی‌شدهٔ ارائه‌دهنده/مدل و default اختیاری را برمی‌گرداند. Pluginهای ارائه‌دهنده مالک profile اختصاصی مدل از طریق hookهای thinking خود هستند، بنابراین Pluginهای ابزار باید به‌جای import یا تکرار فهرست‌های ارائه‌دهنده، این helper runtime را فراخوانی کنند.

`normalizeThinkingLevel(...)` متن کاربر مانند `on`، `x-high`، یا `extra high` را پیش از بررسی در برابر policy حل‌شده، به سطح ذخیره‌شدهٔ canonical تبدیل می‌کند.

**helperهای session store** زیر `api.runtime.agent.session` هستند:

typescriptCopy code
[code]
    const storePath = api.runtime.agent.session.resolveStorePath(cfg);const store = api.runtime.agent.session.loadSessionStore(storePath);await api.runtime.agent.session.updateSessionStore(storePath, (nextStore) => {  // Patch one entry without replacing the whole file from stale state.  nextStore[sessionKey] = { ...nextStore[sessionKey], thinkingLevel: "high" };});const filePath = api.runtime.agent.session.resolveSessionFilePath(cfg, sessionId);
[/code]

برای نوشتن‌های runtime، `updateSessionStore(...)` یا `updateSessionStoreEntry(...)` را ترجیح دهید. آن‌ها از writer session-store متعلق به Gateway عبور می‌کنند، updateهای همزمان را حفظ می‌کنند، و hot cache را دوباره استفاده می‌کنند. `saveSessionStore(...)` برای سازگاری و بازنویسی‌های سبک نگهداشت offline در دسترس می‌ماند.

api.runtime.agent.defaults

ثابت‌های default مدل و ارائه‌دهنده:

typescriptCopy code
[code]
    const model = api.runtime.agent.defaults.model; // e.g. "anthropic/claude-sonnet-4-6"const provider = api.runtime.agent.defaults.provider; // e.g. "anthropic"
[/code]

api.runtime.llm

بدون import کردن داخلی‌های ارائه‌دهنده یا تکرار آماده‌سازی مدل/auth/base URL در OpenClaw، یک text completion متعلق به میزبان اجرا کنید.

typescriptCopy code
[code]
    const result = await api.runtime.llm.complete({  messages: [{ role: "user", content: "Summarize this transcript." }],  purpose: "my-plugin.summary",  maxTokens: 512,  temperature: 0.2,});
[/code]

این helper از همان مسیر آماده‌سازی simple-completion استفاده می‌کند که runtime داخلی OpenClaw و snapshot پیکربندی runtime متعلق به میزبان استفاده می‌کنند. موتورهای context قابلیت session-bound `llm.complete` دریافت می‌کنند، بنابراین فراخوانی‌های مدل از agent session فعال استفاده می‌کنند و بی‌صدا به agent default fallback نمی‌کنند. نتیجه شامل انتساب ارائه‌دهنده/مدل/agent به‌علاوهٔ token نرمال‌شده، cache، و مصرف هزینهٔ تخمینی در صورت دسترس بودن است.

api.runtime.subagent

اجرای subagentهای پس‌زمینه را راه‌اندازی و مدیریت کنید.

typescriptCopy code
[code]
    // Start a subagent runconst { runId } = await api.runtime.subagent.run({  sessionKey: "agent:main:subagent:search-helper",  message: "Expand this query into focused follow-up searches.",  provider: "openai", // optional override  model: "gpt-4.1-mini", // optional override  deliver: false,}); // Wait for completionconst result = await api.runtime.subagent.waitForRun({ runId, timeoutMs: 30000 }); // Read session messagesconst { messages } = await api.runtime.subagent.getSessionMessages({  sessionKey: "agent:main:subagent:search-helper",  limit: 10,}); // Delete a sessionawait api.runtime.subagent.deleteSession({  sessionKey: "agent:main:subagent:search-helper",});
[/code]

`deleteSession(...)` می‌تواند sessionهایی را حذف کند که همان Plugin از طریق `api.runtime.subagent.run(...)` ساخته است. حذف sessionهای دلخواه کاربر یا اپراتور همچنان به یک درخواست Gateway با scope ادمین نیاز دارد.

api.runtime.nodes

nodeهای متصل را فهرست کنید و یک فرمان node-host را از کد Plugin بارگذاری‌شده در Gateway یا از فرمان‌های CLI Plugin فراخوانی کنید. وقتی یک Plugin مالک کار محلی روی یک دستگاه paired است، مثلا یک bridge مرورگر یا صوت روی Mac دیگر، از این استفاده کنید.

typescriptCopy code
[code]
    const { nodes } = await api.runtime.nodes.list({ connected: true }); const result = await api.runtime.nodes.invoke({  nodeId: "mac-studio",  command: "my-plugin.command",  params: { action: "start" },  timeoutMs: 30000,});
[/code]

داخل Gateway این runtime درون‌فرایندی است. در فرمان‌های CLI Plugin، Gateway پیکربندی‌شده را از طریق RPC فراخوانی می‌کند، بنابراین فرمان‌هایی مانند `openclaw googlemeet recover-tab` می‌توانند nodeهای paired را از terminal بررسی کنند. فرمان‌های Node همچنان از مسیر pairing عادی node در Gateway، allowlistهای فرمان، policyهای node-invoke در Plugin، و مدیریت فرمان محلی node عبور می‌کنند.

Pluginهایی که فرمان‌های خطرناک node-host را expose می‌کنند باید یک policy node-invoke با `api.registerNodeInvokePolicy(...)` ثبت کنند. این policy در Gateway پس از بررسی‌های allowlist فرمان و پیش از forward شدن فرمان به node اجرا می‌شود، بنابراین فراخوانی‌های مستقیم `node.invoke` و ابزارهای سطح بالاتر Plugin مسیر enforcement یکسانی را به اشتراک می‌گذارند.

api.runtime.tasks.managedFlows

یک runtime Task Flow را به یک کلید session موجود OpenClaw یا context ابزار مورد اعتماد bind کنید، سپس Task Flowها را بدون پاس دادن owner در هر فراخوانی بسازید و مدیریت کنید.

Task Flow وضعیت workflow چندمرحله‌ای پایدار را دنبال می‌کند. scheduler نیست: برای wakeupهای آینده از Cron یا `api.session.workflow.scheduleSessionTurn(...)` استفاده کنید، سپس وقتی آن کار به flow state، taskهای child، waitها، یا cancellation نیاز دارد، از `managedFlows` در نوبت زمان‌بندی‌شده استفاده کنید.

typescriptCopy code
[code]
    const taskFlow = api.runtime.tasks.managedFlows.fromToolContext(ctx); const created = taskFlow.createManaged({  controllerId: "my-plugin/review-batch",  goal: "Review new pull requests",}); const child = taskFlow.runTask({  flowId: created.flowId,  runtime: "acp",  childSessionKey: "agent:main:subagent:reviewer",  task: "Review PR #123",  status: "running",  startedAt: Date.now(),}); const waiting = taskFlow.setWaiting({  flowId: created.flowId,  expectedRevision: created.revision,  currentStep: "await-human-reply",  waitJson: { kind: "reply", channel: "telegram" },});
[/code]

وقتی از لایه‌ی اتصال خودتان یک کلید نشست معتبر OpenClaw دارید، از `bindSession({ sessionKey, requesterOrigin })` استفاده کنید. از ورودی خام کاربر اتصال انجام ندهید.

api.runtime.tts

سنتز متن به گفتار.

typescriptCopy code
[code]
    // Standard TTSconst clip = await api.runtime.tts.textToSpeech({  text: "Hello from OpenClaw",  cfg: api.config,}); // Telephony-optimized TTSconst telephonyClip = await api.runtime.tts.textToSpeechTelephony({  text: "Hello from OpenClaw",  cfg: api.config,}); // List available voicesconst voices = await api.runtime.tts.listVoices({  provider: "elevenlabs",  cfg: api.config,});
[/code]

از پیکربندی هسته‌ی `messages.tts` و انتخاب ارائه‌دهنده استفاده می‌کند. بافر صوتی PCM و نرخ نمونه‌برداری را برمی‌گرداند.

api.runtime.mediaUnderstanding

تحلیل تصویر، صدا و ویدئو.

typescriptCopy code
[code]
    // Describe an imageconst image = await api.runtime.mediaUnderstanding.describeImageFile({  filePath: "/tmp/inbound-photo.jpg",  cfg: api.config,  agentDir: "/tmp/agent",}); // Transcribe audioconst { text } = await api.runtime.mediaUnderstanding.transcribeAudioFile({  filePath: "/tmp/inbound-audio.ogg",  cfg: api.config,  mime: "audio/ogg", // optional, for when MIME cannot be inferred}); // Describe a videoconst video = await api.runtime.mediaUnderstanding.describeVideoFile({  filePath: "/tmp/inbound-video.mp4",  cfg: api.config,}); // Generic file analysisconst result = await api.runtime.mediaUnderstanding.runFile({  filePath: "/tmp/inbound-file.pdf",  cfg: api.config,}); // Structured image extraction through a specific provider/model.// Include at least one image; text inputs are supplemental context.const evidence = await api.runtime.mediaUnderstanding.extractStructuredWithModel({  provider: "codex",  model: "gpt-5.5",  input: [    {      type: "image",      buffer: receiptImageBuffer,      fileName: "receipt.png",      mime: "image/png",    },    { type: "text", text: "Prefer the printed total over handwritten notes." },  ],  instructions: "Extract vendor, total, and searchable tags.",  schemaName: "receipt.evidence",  jsonSchema: {    type: "object",    properties: {      vendor: { type: "string" },      total: { type: "number" },      tags: { type: "array", items: { type: "string" } },    },    required: ["vendor", "total"],  },  cfg: api.config,});
[/code]

وقتی خروجی تولید نشود، برای نمونه ورودی رد شده باشد، `{ text: undefined }` را برمی‌گرداند.

api.runtime.imageGeneration

تولید تصویر.

typescriptCopy code
[code]
    const result = await api.runtime.imageGeneration.generate({  prompt: "A robot painting a sunset",  cfg: api.config,}); const providers = api.runtime.imageGeneration.listProviders({ cfg: api.config });
[/code]

api.runtime.webSearch

جست‌وجوی وب.

typescriptCopy code
[code]
    const providers = api.runtime.webSearch.listProviders({ config: api.config }); const result = await api.runtime.webSearch.search({  config: api.config,  args: { query: "OpenClaw plugin SDK", count: 5 },});
[/code]

api.runtime.media

ابزارهای رسانه‌ای سطح پایین.

typescriptCopy code
[code]
    const webMedia = await api.runtime.media.loadWebMedia(url);const mime = await api.runtime.media.detectMime(buffer);const kind = api.runtime.media.mediaKindFromMime("image/jpeg"); // "image"const isVoice = api.runtime.media.isVoiceCompatibleAudio(filePath);const metadata = await api.runtime.media.getImageMetadata(filePath);const resized = await api.runtime.media.resizeToJpeg(buffer, { maxWidth: 800 });const terminalQr = await api.runtime.media.renderQrTerminal("https://openclaw.ai");const pngQr = await api.runtime.media.renderQrPngBase64("https://openclaw.ai", {  scale: 6, // 1-12  marginModules: 4, // 0-16});const pngQrDataUrl = await api.runtime.media.renderQrPngDataUrl("https://openclaw.ai");const tmpRoot = resolvePreferredOpenClawTmpDir();const pngQrFile = await api.runtime.media.writeQrPngTempFile("https://openclaw.ai", {  tmpRoot,  dirPrefix: "my-plugin-qr-",  fileName: "qr.png",});
[/code]

api.runtime.config

عکس فوری پیکربندی runtime فعلی و نوشتن‌های تراکنشی پیکربندی. پیکربندی‌ای را ترجیح دهید که از قبل به مسیر فراخوانی فعال پاس داده شده است؛ فقط وقتی handler مستقیما به عکس فوری پردازه نیاز دارد از `current()` استفاده کنید.

typescriptCopy code
[code]
    const cfg = api.runtime.config.current();await api.runtime.config.mutateConfigFile({  afterWrite: { mode: "auto" },  mutate(draft) {    draft.plugins ??= {};  },});
[/code]

`mutateConfigFile(...)` و `replaceConfigFile(...)` یک مقدار `followUp` برمی‌گردانند، برای نمونه `{ mode: "restart", requiresRestart: true, reason }`، که نیت نویسنده را بدون گرفتن کنترل راه‌اندازی مجدد از Gateway ثبت می‌کند.

api.runtime.system

ابزارهای سطح سیستم.

typescriptCopy code
[code]
    await api.runtime.system.enqueueSystemEvent(event);api.runtime.system.requestHeartbeat({  source: "other",  intent: "event",  reason: "plugin-event",});api.runtime.system.requestHeartbeatNow({ reason: "plugin-event" }); // Deprecated compatibility alias.const output = await api.runtime.system.runCommandWithTimeout(cmd, args, opts);const hint = api.runtime.system.formatNativeDependencyHint(pkg);
[/code]

api.runtime.events

اشتراک‌های رویداد.

typescriptCopy code
[code]
    api.runtime.events.onAgentEvent((event) => {  /* ... */});api.runtime.events.onSessionTranscriptUpdate((update) => {  /* ... */});
[/code]

api.runtime.logging

ثبت لاگ.

typescriptCopy code
[code]
    const verbose = api.runtime.logging.shouldLogVerbose();const childLogger = api.runtime.logging.getChildLogger({ plugin: "my-plugin" }, { level: "debug" });
[/code]

api.runtime.modelAuth

حل احراز هویت مدل و ارائه‌دهنده.

typescriptCopy code
[code]
    const auth = await api.runtime.modelAuth.getApiKeyForModel({ model, cfg });const providerAuth = await api.runtime.modelAuth.resolveApiKeyForProvider({  provider: "openai",  cfg,});
[/code]

api.runtime.state

حل مسیر دایرکتوری وضعیت و ذخیره‌سازی کلیددار مبتنی بر SQLite.

typescriptCopy code
[code]
    const stateDir = api.runtime.state.resolveStateDir(process.env);const store = api.runtime.state.openKeyedStore&lt;MyRecord&gt;({  namespace: "my-feature",  maxEntries: 200,  defaultTtlMs: 15 * 60_000,}); await store.register("key-1", { value: "hello" });const claimed = await store.registerIfAbsent("dedupe-key", { value: "first" });const value = await store.lookup("key-1");await store.consume("key-1");await store.clear();
[/code]

ذخیره‌گاه‌های کلیددار پس از راه‌اندازی مجدد باقی می‌مانند و با شناسه‌ی Plugin متصل به runtime ایزوله می‌شوند. برای ادعاهای اتمیک حذف تکراری‌ها از `registerIfAbsent(...)` استفاده کنید: وقتی کلید وجود نداشته یا منقضی شده و ثبت شده باشد `true` برمی‌گرداند، یا وقتی یک مقدار زنده از قبل وجود داشته باشد بدون بازنویسی مقدار، زمان ایجاد یا TTL آن `false` برمی‌گرداند. محدودیت‌ها: `maxEntries` برای هر namespace، ۱٬۰۰۰ ردیف زنده برای هر Plugin، مقدارهای JSON کمتر از ۶۴KB، و انقضای اختیاری TTL.

api.runtime.tools

کارخانه‌های ابزار حافظه و CLI.

typescriptCopy code
[code]
    const getTool = api.runtime.tools.createMemoryGetTool(/* ... */);const searchTool = api.runtime.tools.createMemorySearchTool(/* ... */);api.runtime.tools.registerMemoryCli(/* ... */);
[/code]

api.runtime.channel

کمک‌کننده‌های runtime ویژه‌ی کانال، وقتی یک Plugin کانال بارگذاری شده باشد در دسترس هستند.

`api.runtime.channel.mentions` سطح مشترک سیاست اشاره‌ی ورودی برای Pluginهای کانال همراه است که از تزریق runtime استفاده می‌کنند:

typescriptCopy code
[code]
    const mentionMatch = api.runtime.channel.mentions.matchesMentionWithExplicit(text, {  mentionRegexes,  mentionPatterns,}); const decision = api.runtime.channel.mentions.resolveInboundMentionDecision({  facts: {    canDetectMention: true,    wasMentioned: mentionMatch.matched,    implicitMentionKinds: api.runtime.channel.mentions.implicitMentionKindWhen(      "reply_to_bot",      isReplyToBot,    ),  },  policy: {    isGroup,    requireMention,    allowTextCommands,    hasControlCommand,    commandAuthorized,  },});
[/code]

کمک‌کننده‌های اشاره‌ی در دسترس:

  * `buildMentionRegexes`
  * `matchesMentionPatterns`
  * `matchesMentionWithExplicit`
  * `implicitMentionKindWhen`
  * `resolveInboundMentionDecision`


`api.runtime.channel.mentions` عمدا کمک‌کننده‌های سازگاری قدیمی‌تر `resolveMentionGating*` را نمایان نمی‌کند. مسیر نرمال‌شده‌ی `{ facts, policy }` را ترجیح دهید.

## ذخیره‌سازی ارجاع‌های runtime

برای ذخیره‌سازی ارجاع runtime جهت استفاده خارج از callback `register` از `createPluginRuntimeStore` استفاده کنید:

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

## دیگر فیلدهای سطح بالای `api`

فراتر از `api.runtime`، شیء API این موارد را نیز فراهم می‌کند:

شناسهٔ Plugin.

نام نمایشی Plugin.

عکس‌فوری پیکربندی فعلی (در صورت وجود، عکس‌فوری زمان اجرای درون‌حافظه‌ای فعال).

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaS5wbHVnaW5Db25maWciIHR5cGU9IlJlY29yZDxzdHJpbmcsIHVua25vd24 "> پیکربندی اختصاصی Plugin از `plugins.entries.<id>.config`.

ثبت‌کنندهٔ گزارش دامنه‌دار (`debug`, `info`, `warn`, `error`).

حالت بارگذاری فعلی؛ `"setup-runtime"` پنجرهٔ سبک راه‌اندازی/تنظیم پیش از ورودی کامل است.

## مرتبط

  * [جزئیات داخلی Plugin](</fa/plugins/architecture>) — مدل قابلیت و رجیستری
  * [نقاط ورود SDK](</fa/plugins/sdk-entrypoints>) — گزینه‌های `definePluginEntry`
  * [نمای کلی SDK](</fa/plugins/sdk-overview>) — مرجع زیرمسیر


Was this useful?YesNo