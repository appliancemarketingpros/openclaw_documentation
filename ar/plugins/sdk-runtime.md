---
title: مساعدات وقت تشغيل Plugin
source_url: https://docs.openclaw.ai/ar/plugins/sdk-runtime
scraped_at: 2026-05-25
---

مرجع لكائن `api.runtime` الذي يُحقن في كل Plugin أثناء التسجيل. استخدم هذه الأدوات المساعدة بدلاً من استيراد مكوّنات المضيف الداخلية مباشرة.

[**Plugins القنوات** دليل خطوة بخطوة يستخدم هذه الأدوات المساعدة ضمن سياق Plugins القنوات. ](</ar/plugins/sdk-channel-plugins>) [**Plugins المزوّدين** دليل خطوة بخطوة يستخدم هذه الأدوات المساعدة ضمن سياق Plugins المزوّدين. ](</ar/plugins/sdk-provider-plugins>)

typescriptCopy code
[code]
    register(api) {  const runtime = api.runtime;}
[/code]

## تحميل الإعدادات والكتابة

فضّل الإعدادات التي مُرّرت مسبقاً إلى مسار الاستدعاء النشط، مثل `api.config` أثناء التسجيل أو وسيطة `cfg` في استدعاءات القناة/المزوّد الراجعة. هذا يُبقي لقطة عملية واحدة متدفقة عبر العمل بدلاً من إعادة تحليل الإعدادات في المسارات الساخنة.

استخدم `api.runtime.config.current()` فقط عندما يحتاج معالج طويل العمر إلى لقطة العملية الحالية ولم تُمرَّر أي إعدادات إلى تلك الدالة. القيمة المُعادة للقراءة فقط؛ انسخها أو استخدم أداة مساعدة للتعديل قبل التحرير.

تتلقى مصانع الأدوات `ctx.runtimeConfig` إضافة إلى `ctx.getRuntimeConfig()`. استخدم دالة الجلب داخل استدعاء `execute` الراجع لأداة طويلة العمر عندما يمكن أن تتغير الإعدادات بعد إنشاء تعريف الأداة.

استمر في حفظ التغييرات باستخدام `api.runtime.config.mutateConfigFile(...)` أو `api.runtime.config.replaceConfigFile(...)`. يجب أن تختار كل عملية كتابة سياسة `afterWrite` صريحة:

  * يترك `afterWrite: { mode: "auto" }` قرار إعادة التحميل لمخطِّط Gateway.
  * يفرض `afterWrite: { mode: "restart", reason: "..." }` إعادة تشغيل نظيفة عندما يعرف الكاتب أن إعادة التحميل الساخنة غير آمنة.
  * يمنع `afterWrite: { mode: "none", reason: "..." }` إعادة التحميل/إعادة التشغيل التلقائية فقط عندما يملك المستدعي المتابعة.


تعيد أدوات التعديل المساعدة `afterWrite` إضافة إلى ملخص `followUp` نمطي بحيث يستطيع المستدعون تسجيل أو اختبار ما إذا كانوا قد طلبوا إعادة تشغيل. يبقى Gateway هو مالك توقيت حدوث إعادة التشغيل فعلياً.

`api.runtime.config.loadConfig()` و`api.runtime.config.writeConfigFile(...)` هما أداتان مساعدتان مهجورتان للتوافق ضمن `runtime-config-load-write`. تعرضان تحذيراً مرة واحدة أثناء التشغيل، وتبقيان متاحتين لـ Plugins خارجية قديمة خلال نافذة الترحيل. يجب ألا تستخدمهما Plugins المضمّنة؛ تفشل حواجز حدود الإعدادات إذا استدعى كود Plugin هذه الأدوات أو استورد تلك الأدوات المساعدة من مسارات فرعية في Plugin SDK.

للاستيرادات المباشرة من SDK، استخدم المسارات الفرعية المركّزة للإعدادات بدلاً من برميل التوافق الواسع `openclaw/plugin-sdk/config-runtime`: استخدم `config-contracts` للأنواع، و`plugin-config-runtime` لتوكيدات الإعدادات المحمّلة مسبقاً والبحث عن مدخل Plugin، و`runtime-config-snapshot` للقطات العملية الحالية، و`config-mutation` للكتابات. يجب أن تحاكي اختبارات Plugins المضمّنة هذه المسارات الفرعية المركّزة مباشرة بدلاً من محاكاة برميل التوافق الواسع.

لكود تشغيل OpenClaw الداخلي الاتجاه نفسه: حمّل الإعدادات مرة واحدة عند حدود CLI أو Gateway أو العملية، ثم مرّر تلك القيمة عبر المسار. تؤدي عمليات التعديل الناجحة إلى تحديث لقطة تشغيل العملية وتقديم مراجعتها الداخلية؛ يجب أن تعتمد التخزينات المؤقتة طويلة العمر على مفتاح التخزين المؤقت المملوك لبيئة التشغيل بدلاً من تسلسل الإعدادات محلياً. لدى وحدات التشغيل طويلة العمر ماسح بلا تسامح مع استدعاءات `loadConfig()` المحيطة؛ استخدم `cfg` ممرَّرة، أو `context.getRuntimeConfig()` للطلب، أو `getRuntimeConfig()` عند حد عملية صريح.

يجب أن تستخدم مسارات تنفيذ المزوّد والقناة لقطة إعدادات التشغيل النشطة، لا لقطة ملف مُعادة لقراءة الإعدادات أو تحريرها. تحفظ لقطات الملفات قيم المصدر مثل علامات SecretRef لواجهة المستخدم والكتابات؛ تحتاج استدعاءات المزوّد الراجعة إلى عرض التشغيل المحلول. عندما يمكن استدعاء أداة مساعدة إما بلقطة المصدر النشطة أو بلقطة التشغيل النشطة، مرّر المسار عبر `selectApplicableRuntimeConfig()` قبل قراءة بيانات الاعتماد.

## فضاءات أسماء التشغيل

api.runtime.agent

هوية الوكيل، والأدلة، وإدارة الجلسات.

typescriptCopy code
[code]
    // Resolve the agent's working directoryconst agentDir = api.runtime.agent.resolveAgentDir(cfg); // Resolve agent workspaceconst workspaceDir = api.runtime.agent.resolveAgentWorkspaceDir(cfg); // Get agent identityconst identity = api.runtime.agent.resolveAgentIdentity(cfg); // Get default thinking levelconst thinking = api.runtime.agent.resolveThinkingDefault({  cfg,  provider,  model,}); // Validate a user-provided thinking level against the active provider profileconst policy = api.runtime.agent.resolveThinkingPolicy({ provider, model });const level = api.runtime.agent.normalizeThinkingLevel("extra high");if (level && policy.levels.some((entry) => entry.id === level)) {  // pass level to an embedded run} // Get agent timeoutconst timeoutMs = api.runtime.agent.resolveAgentTimeoutMs(cfg); // Ensure workspace existsawait api.runtime.agent.ensureAgentWorkspace(cfg); // Run an embedded agent turnconst agentDir = api.runtime.agent.resolveAgentDir(cfg);const result = await api.runtime.agent.runEmbeddedAgent({  sessionId: "my-plugin:task-1",  runId: crypto.randomUUID(),  sessionFile: path.join(agentDir, "sessions", "my-plugin-task-1.jsonl"),  workspaceDir: api.runtime.agent.resolveAgentWorkspaceDir(cfg),  prompt: "Summarize the latest changes",  timeoutMs: api.runtime.agent.resolveAgentTimeoutMs(cfg),});
[/code]

`runEmbeddedAgent(...)` هي الأداة المساعدة المحايدة لبدء دورة وكيل OpenClaw عادية من كود Plugin. تستخدم المسار نفسه لحل المزوّد/النموذج واختيار عُدّة الوكيل كما في الردود المُشغّلة من القناة.

يبقى `runEmbeddedPiAgent(...)` اسماً مستعاراً للتوافق.

يعيد `resolveThinkingPolicy(...)` مستويات التفكير المدعومة للمزوّد/النموذج والقيمة الافتراضية الاختيارية. تمتلك Plugins المزوّدين ملف التعريف الخاص بالنموذج عبر خطافات التفكير الخاصة بها، لذلك يجب أن تستدعي Plugins الأدوات هذه الأداة المساعدة في التشغيل بدلاً من استيراد قوائم المزوّدين أو تكرارها.

يحوّل `normalizeThinkingLevel(...)` نص المستخدم مثل `on` أو `x-high` أو `extra high` إلى المستوى المخزّن القياسي قبل التحقق منه مقابل السياسة المحلولة.

**أدوات مخزن الجلسات المساعدة** تقع ضمن `api.runtime.agent.session`:

typescriptCopy code
[code]
    const storePath = api.runtime.agent.session.resolveStorePath(cfg);const store = api.runtime.agent.session.loadSessionStore(storePath);await api.runtime.agent.session.updateSessionStore(storePath, (nextStore) => {  // Patch one entry without replacing the whole file from stale state.  nextStore[sessionKey] = { ...nextStore[sessionKey], thinkingLevel: "high" };});const filePath = api.runtime.agent.session.resolveSessionFilePath(cfg, sessionId);
[/code]

فضّل `updateSessionStore(...)` أو `updateSessionStoreEntry(...)` لكتابات التشغيل. تمر عبر كاتب مخزن الجلسات المملوك لـ Gateway، وتحافظ على التحديثات المتزامنة، وتعيد استخدام التخزين المؤقت الساخن. يبقى `saveSessionStore(...)` متاحاً للتوافق وإعادة الكتابة بأسلوب الصيانة دون اتصال.

api.runtime.agent.defaults

ثوابت النموذج والمزوّد الافتراضية:

typescriptCopy code
[code]
    const model = api.runtime.agent.defaults.model; // e.g. "anthropic/claude-sonnet-4-6"const provider = api.runtime.agent.defaults.provider; // e.g. "anthropic"
[/code]

api.runtime.llm

شغّل إكمال نص مملوكاً للمضيف من دون استيراد مكوّنات المزوّد الداخلية أو تكرار إعداد النموذج/المصادقة/عنوان URL الأساسي الخاص بـ OpenClaw.

typescriptCopy code
[code]
    const result = await api.runtime.llm.complete({  messages: [{ role: "user", content: "Summarize this transcript." }],  purpose: "my-plugin.summary",  maxTokens: 512,  temperature: 0.2,});
[/code]

تستخدم الأداة المساعدة مسار إعداد الإكمال البسيط نفسه كما في بيئة تشغيل OpenClaw المدمجة ولقطة إعدادات التشغيل المملوكة للمضيف. تتلقى محركات السياق قدرة `llm.complete` مرتبطة بالجلسة، لذلك تستخدم استدعاءات النماذج وكيل الجلسة النشط ولا تعود بصمت إلى الوكيل الافتراضي. تتضمن النتيجة إسناد المزوّد/النموذج/الوكيل إضافة إلى استخدام الرموز، والتخزين المؤقت، والتكلفة المقدّرة بعد التطبيع عند توفرها.

api.runtime.subagent

شغّل وأدر عمليات وكلاء فرعيين في الخلفية.

typescriptCopy code
[code]
    // Start a subagent runconst { runId } = await api.runtime.subagent.run({  sessionKey: "agent:main:subagent:search-helper",  message: "Expand this query into focused follow-up searches.",  provider: "openai", // optional override  model: "gpt-4.1-mini", // optional override  deliver: false,}); // Wait for completionconst result = await api.runtime.subagent.waitForRun({ runId, timeoutMs: 30000 }); // Read session messagesconst { messages } = await api.runtime.subagent.getSessionMessages({  sessionKey: "agent:main:subagent:search-helper",  limit: 10,}); // Delete a sessionawait api.runtime.subagent.deleteSession({  sessionKey: "agent:main:subagent:search-helper",});
[/code]

يستطيع `deleteSession(...)` حذف الجلسات التي أنشأها Plugin نفسه عبر `api.runtime.subagent.run(...)`. لا يزال حذف جلسات مستخدمين أو مشغّلين اعتباطية يتطلب طلب Gateway بنطاق إداري.

api.runtime.nodes

اسرد العقد المتصلة واستدعِ أمراً مستضافاً على عقدة من كود Plugin المحمّل عبر Gateway أو من أوامر CLI الخاصة بـ Plugin. استخدم هذا عندما يمتلك Plugin عملاً محلياً على جهاز مقترن، مثل جسر متصفح أو صوت على Mac آخر.

typescriptCopy code
[code]
    const { nodes } = await api.runtime.nodes.list({ connected: true }); const result = await api.runtime.nodes.invoke({  nodeId: "mac-studio",  command: "my-plugin.command",  params: { action: "start" },  timeoutMs: 30000,});
[/code]

داخل Gateway تكون بيئة التشغيل هذه داخل العملية. في أوامر CLI الخاصة بـ Plugin تستدعي Gateway المضبوط عبر RPC، لذلك يمكن لأوامر مثل `openclaw googlemeet recover-tab` فحص العقد المقترنة من الطرفية. ما زالت أوامر Node تمر عبر اقتران عقد Gateway العادي، وقوائم السماح للأوامر، وسياسات استدعاء العقد في Plugin، ومعالجة الأوامر المحلية في العقدة.

يجب على Plugins التي تعرض أوامر خطرة مستضافة على العقدة تسجيل سياسة استدعاء عقدة باستخدام `api.registerNodeInvokePolicy(...)`. تعمل السياسة في Gateway بعد فحوصات قائمة سماح الأوامر وقبل تمرير الأمر إلى العقدة، لذلك تشترك استدعاءات `node.invoke` المباشرة وأدوات Plugin الأعلى مستوى في مسار الإنفاذ نفسه.

api.runtime.tasks.managedFlows

اربط بيئة تشغيل Task Flow بمفتاح جلسة OpenClaw موجود أو بسياق أداة موثوق، ثم أنشئ وأدر Task Flows من دون تمرير مالك في كل استدعاء.

يتتبع Task Flow حالة سير عمل متينة متعددة الخطوات. إنه ليس مجدولاً: استخدم Cron أو `api.session.workflow.scheduleSessionTurn(...)` لعمليات الإيقاظ المستقبلية، ثم استخدم `managedFlows` من الدورة المجدولة عندما يحتاج ذلك العمل إلى حالة تدفق، أو مهام فرعية، أو انتظارات، أو إلغاء.

typescriptCopy code
[code]
    const taskFlow = api.runtime.tasks.managedFlows.fromToolContext(ctx); const created = taskFlow.createManaged({  controllerId: "my-plugin/review-batch",  goal: "Review new pull requests",}); const child = taskFlow.runTask({  flowId: created.flowId,  runtime: "acp",  childSessionKey: "agent:main:subagent:reviewer",  task: "Review PR #123",  status: "running",  startedAt: Date.now(),}); const waiting = taskFlow.setWaiting({  flowId: created.flowId,  expectedRevision: created.revision,  currentStep: "await-human-reply",  waitJson: { kind: "reply", channel: "telegram" },});
[/code]

استخدم `bindSession({ sessionKey, requesterOrigin })` عندما يكون لديك بالفعل مفتاح جلسة OpenClaw موثوق من طبقة الربط الخاصة بك. لا تربط من إدخال مستخدم خام.

api.runtime.tts

تركيب تحويل النص إلى كلام.

typescriptCopy code
[code]
    // Standard TTSconst clip = await api.runtime.tts.textToSpeech({  text: "Hello from OpenClaw",  cfg: api.config,}); // Telephony-optimized TTSconst telephonyClip = await api.runtime.tts.textToSpeechTelephony({  text: "Hello from OpenClaw",  cfg: api.config,}); // List available voicesconst voices = await api.runtime.tts.listVoices({  provider: "elevenlabs",  cfg: api.config,});
[/code]

يستخدم تهيئة `messages.tts` الأساسية واختيار المزوّد. يُرجع مخزنًا مؤقتًا صوتيًا بصيغة PCM + معدل العينة.

api.runtime.mediaUnderstanding

تحليل الصور والصوت والفيديو.

typescriptCopy code
[code]
    // Describe an imageconst image = await api.runtime.mediaUnderstanding.describeImageFile({  filePath: "/tmp/inbound-photo.jpg",  cfg: api.config,  agentDir: "/tmp/agent",}); // Transcribe audioconst { text } = await api.runtime.mediaUnderstanding.transcribeAudioFile({  filePath: "/tmp/inbound-audio.ogg",  cfg: api.config,  mime: "audio/ogg", // optional, for when MIME cannot be inferred}); // Describe a videoconst video = await api.runtime.mediaUnderstanding.describeVideoFile({  filePath: "/tmp/inbound-video.mp4",  cfg: api.config,}); // Generic file analysisconst result = await api.runtime.mediaUnderstanding.runFile({  filePath: "/tmp/inbound-file.pdf",  cfg: api.config,}); // Structured image extraction through a specific provider/model.// Include at least one image; text inputs are supplemental context.const evidence = await api.runtime.mediaUnderstanding.extractStructuredWithModel({  provider: "codex",  model: "gpt-5.5",  input: [    {      type: "image",      buffer: receiptImageBuffer,      fileName: "receipt.png",      mime: "image/png",    },    { type: "text", text: "Prefer the printed total over handwritten notes." },  ],  instructions: "Extract vendor, total, and searchable tags.",  schemaName: "receipt.evidence",  jsonSchema: {    type: "object",    properties: {      vendor: { type: "string" },      total: { type: "number" },      tags: { type: "array", items: { type: "string" } },    },    required: ["vendor", "total"],  },  cfg: api.config,});
[/code]

يُرجع `{ text: undefined }` عندما لا يُنتَج أي خرج (مثل الإدخال المتجاوز).

api.runtime.imageGeneration

توليد الصور.

typescriptCopy code
[code]
    const result = await api.runtime.imageGeneration.generate({  prompt: "A robot painting a sunset",  cfg: api.config,}); const providers = api.runtime.imageGeneration.listProviders({ cfg: api.config });
[/code]

api.runtime.webSearch

البحث على الويب.

typescriptCopy code
[code]
    const providers = api.runtime.webSearch.listProviders({ config: api.config }); const result = await api.runtime.webSearch.search({  config: api.config,  args: { query: "OpenClaw plugin SDK", count: 5 },});
[/code]

api.runtime.media

أدوات وسائط منخفضة المستوى.

typescriptCopy code
[code]
    const webMedia = await api.runtime.media.loadWebMedia(url);const mime = await api.runtime.media.detectMime(buffer);const kind = api.runtime.media.mediaKindFromMime("image/jpeg"); // "image"const isVoice = api.runtime.media.isVoiceCompatibleAudio(filePath);const metadata = await api.runtime.media.getImageMetadata(filePath);const resized = await api.runtime.media.resizeToJpeg(buffer, { maxWidth: 800 });const terminalQr = await api.runtime.media.renderQrTerminal("https://openclaw.ai");const pngQr = await api.runtime.media.renderQrPngBase64("https://openclaw.ai", {  scale: 6, // 1-12  marginModules: 4, // 0-16});const pngQrDataUrl = await api.runtime.media.renderQrPngDataUrl("https://openclaw.ai");const tmpRoot = resolvePreferredOpenClawTmpDir();const pngQrFile = await api.runtime.media.writeQrPngTempFile("https://openclaw.ai", {  tmpRoot,  dirPrefix: "my-plugin-qr-",  fileName: "qr.png",});
[/code]

api.runtime.config

لقطة تهيئة وقت التشغيل الحالية وكتابات التهيئة المعاملاتية. فضّل التهيئة التي مُرّرت بالفعل إلى مسار الاستدعاء النشط؛ استخدم `current()` فقط عندما يحتاج المعالج إلى لقطة العملية مباشرة.

typescriptCopy code
[code]
    const cfg = api.runtime.config.current();await api.runtime.config.mutateConfigFile({  afterWrite: { mode: "auto" },  mutate(draft) {    draft.plugins ??= {};  },});
[/code]

يُرجع `mutateConfigFile(...)` و`replaceConfigFile(...)` قيمة `followUp`، مثل `{ mode: "restart", requiresRestart: true, reason }`، والتي تسجل نية الكاتب دون سحب التحكم في إعادة التشغيل من Gateway.

api.runtime.system

أدوات مساعدة على مستوى النظام.

typescriptCopy code
[code]
    await api.runtime.system.enqueueSystemEvent(event);api.runtime.system.requestHeartbeat({  source: "other",  intent: "event",  reason: "plugin-event",});api.runtime.system.requestHeartbeatNow({ reason: "plugin-event" }); // Deprecated compatibility alias.const output = await api.runtime.system.runCommandWithTimeout(cmd, args, opts);const hint = api.runtime.system.formatNativeDependencyHint(pkg);
[/code]

api.runtime.events

اشتراكات الأحداث.

typescriptCopy code
[code]
    api.runtime.events.onAgentEvent((event) => {  /* ... */});api.runtime.events.onSessionTranscriptUpdate((update) => {  /* ... */});
[/code]

api.runtime.logging

التسجيل.

typescriptCopy code
[code]
    const verbose = api.runtime.logging.shouldLogVerbose();const childLogger = api.runtime.logging.getChildLogger({ plugin: "my-plugin" }, { level: "debug" });
[/code]

api.runtime.modelAuth

حل مصادقة النموذج والمزوّد.

typescriptCopy code
[code]
    const auth = await api.runtime.modelAuth.getApiKeyForModel({ model, cfg });const providerAuth = await api.runtime.modelAuth.resolveApiKeyForProvider({  provider: "openai",  cfg,});
[/code]

api.runtime.state

حل دليل الحالة وتخزين مفاتيح مدعوم بـ SQLite.

typescriptCopy code
[code]
    const stateDir = api.runtime.state.resolveStateDir(process.env);const store = api.runtime.state.openKeyedStore&lt;MyRecord&gt;({  namespace: "my-feature",  maxEntries: 200,  defaultTtlMs: 15 * 60_000,}); await store.register("key-1", { value: "hello" });const claimed = await store.registerIfAbsent("dedupe-key", { value: "first" });const value = await store.lookup("key-1");await store.consume("key-1");await store.clear();
[/code]

تبقى مخازن المفاتيح بعد إعادة التشغيل وتُعزل حسب معرّف Plugin المرتبط بوقت التشغيل. استخدم `registerIfAbsent(...)` لمطالبات إزالة التكرار الذرية: فهي تُرجع `true` عندما يكون المفتاح مفقودًا أو منتهي الصلاحية وتم تسجيله، أو `false` عندما توجد قيمة حية بالفعل دون استبدال قيمتها أو وقت إنشائها أو TTL الخاص بها. الحدود: `maxEntries` لكل مساحة أسماء، و1,000 صف حي لكل Plugin، وقيم JSON أقل من 64KB، وانتهاء صلاحية TTL اختياري.

api.runtime.tools

مصانع أدوات الذاكرة وCLI.

typescriptCopy code
[code]
    const getTool = api.runtime.tools.createMemoryGetTool(/* ... */);const searchTool = api.runtime.tools.createMemorySearchTool(/* ... */);api.runtime.tools.registerMemoryCli(/* ... */);
[/code]

api.runtime.channel

مساعدات وقت التشغيل الخاصة بالقناة (تتوفر عند تحميل Plugin قناة).

`api.runtime.channel.mentions` هو سطح سياسة الإشارة الواردة المشترك لـ Plugins القنوات المضمنة التي تستخدم حقن وقت التشغيل:

typescriptCopy code
[code]
    const mentionMatch = api.runtime.channel.mentions.matchesMentionWithExplicit(text, {  mentionRegexes,  mentionPatterns,}); const decision = api.runtime.channel.mentions.resolveInboundMentionDecision({  facts: {    canDetectMention: true,    wasMentioned: mentionMatch.matched,    implicitMentionKinds: api.runtime.channel.mentions.implicitMentionKindWhen(      "reply_to_bot",      isReplyToBot,    ),  },  policy: {    isGroup,    requireMention,    allowTextCommands,    hasControlCommand,    commandAuthorized,  },});
[/code]

مساعدات الإشارة المتاحة:

  * `buildMentionRegexes`
  * `matchesMentionPatterns`
  * `matchesMentionWithExplicit`
  * `implicitMentionKindWhen`
  * `resolveInboundMentionDecision`


لا يعرض `api.runtime.channel.mentions` عمدًا مساعدات التوافق الأقدم `resolveMentionGating*`. فضّل المسار الموحد `{ facts, policy }`.

## تخزين مراجع وقت التشغيل

استخدم `createPluginRuntimeStore` لتخزين مرجع وقت التشغيل للاستخدام خارج استدعاء `register`:

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

## حقول `api` علوية أخرى

إلى جانب `api.runtime`، يوفر كائن API أيضًا:

معرّف Plugin.

اسم العرض لـ Plugin.

لقطة التكوين الحالية (لقطة وقت التشغيل النشطة في الذاكرة عند توفرها).

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaS5wbHVnaW5Db25maWciIHR5cGU9IlJlY29yZDxzdHJpbmcsIHVua25vd24 "> التكوين الخاص بـ Plugin من `plugins.entries.<id>.config`.

مسجّل محدود النطاق (`debug`، `info`، `warn`، `error`).

وضع التحميل الحالي؛ `"setup-runtime"` هي نافذة بدء/إعداد خفيفة قبل الإدخال الكامل.

## ذات صلة

  * [الأجزاء الداخلية لـ Plugin](</ar/plugins/architecture>) — نموذج القدرات والسجل
  * [نقاط دخول SDK](</ar/plugins/sdk-entrypoints>) — خيارات `definePluginEntry`
  * [نظرة عامة على SDK](</ar/plugins/sdk-overview>) — مرجع المسارات الفرعية


Was this useful?YesNo