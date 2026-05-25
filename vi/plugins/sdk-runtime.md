---
title: Trình trợ giúp thời gian chạy của Plugin
source_url: https://docs.openclaw.ai/vi/plugins/sdk-runtime
scraped_at: 2026-05-25
---

Tham chiếu cho đối tượng `api.runtime` được chèn vào mọi Plugin trong quá trình đăng ký. Dùng các helper này thay vì nhập trực tiếp các phần nội bộ của máy chủ.

[**Channel plugins** Hướng dẫn từng bước sử dụng các helper này trong ngữ cảnh cho Plugin kênh. ](</vi/plugins/sdk-channel-plugins>) [**Provider plugins** Hướng dẫn từng bước sử dụng các helper này trong ngữ cảnh cho Plugin nhà cung cấp. ](</vi/plugins/sdk-provider-plugins>)

typescriptCopy code
[code]
    register(api) {  const runtime = api.runtime;}
[/code]

## Tải và ghi cấu hình

Ưu tiên cấu hình đã được truyền vào đường dẫn lệnh gọi đang hoạt động, ví dụ `api.config` trong quá trình đăng ký hoặc đối số `cfg` trên các callback kênh/nhà cung cấp. Việc này giữ cho một snapshot quy trình duy nhất chảy xuyên suốt công việc thay vì phân tích lại cấu hình trên các đường dẫn nóng.

Chỉ dùng `api.runtime.config.current()` khi một handler sống lâu cần snapshot quy trình hiện tại và không có cấu hình nào được truyền vào hàm đó. Giá trị trả về là chỉ đọc; hãy sao chép hoặc dùng helper đột biến trước khi chỉnh sửa.

Các factory công cụ nhận `ctx.runtimeConfig` cùng với `ctx.getRuntimeConfig()`. Dùng getter bên trong callback `execute` của một công cụ sống lâu khi cấu hình có thể thay đổi sau khi định nghĩa công cụ đã được tạo.

Duy trì thay đổi bằng `api.runtime.config.mutateConfigFile(...)` hoặc `api.runtime.config.replaceConfigFile(...)`. Mỗi lần ghi phải chọn một chính sách `afterWrite` rõ ràng:

  * `afterWrite: { mode: "auto" }` để trình quyết định tải lại Gateway xử lý.
  * `afterWrite: { mode: "restart", reason: "..." }` buộc khởi động lại sạch khi thành phần ghi biết rằng tải lại nóng là không an toàn.
  * `afterWrite: { mode: "none", reason: "..." }` chỉ chặn tải lại/khởi động lại tự động khi bên gọi sở hữu bước theo dõi.


Các helper đột biến trả về `afterWrite` cùng với bản tóm tắt `followUp` có kiểu để bên gọi có thể ghi log hoặc kiểm thử xem họ đã yêu cầu khởi động lại hay chưa. Gateway vẫn sở hữu thời điểm việc khởi động lại đó thực sự diễn ra.

`api.runtime.config.loadConfig()` và `api.runtime.config.writeConfigFile(...)` là các helper tương thích đã lỗi thời trong `runtime-config-load-write`. Chúng cảnh báo một lần khi chạy, và vẫn có sẵn cho các Plugin bên ngoài cũ trong thời gian chuyển đổi. Các Plugin đi kèm không được dùng chúng; các guard ranh giới cấu hình sẽ lỗi nếu mã Plugin gọi chúng hoặc nhập các helper đó từ các đường dẫn con của Plugin SDK.

Đối với các import SDK trực tiếp, hãy dùng các đường dẫn con cấu hình tập trung thay vì barrel tương thích rộng `openclaw/plugin-sdk/config-runtime`: `config-contracts` cho kiểu, `plugin-config-runtime` cho các assertion cấu hình đã tải và tra cứu mục nhập Plugin, `runtime-config-snapshot` cho snapshot quy trình hiện tại, và `config-mutation` cho ghi. Kiểm thử Plugin đi kèm nên mock trực tiếp các đường dẫn con tập trung này thay vì mock barrel tương thích rộng.

Mã thời gian chạy nội bộ của OpenClaw cũng đi theo hướng đó: tải cấu hình một lần tại ranh giới CLI, Gateway, hoặc quy trình, rồi truyền giá trị đó xuyên suốt. Các lần ghi đột biến thành công làm mới snapshot thời gian chạy của quy trình và tăng revision nội bộ của nó; cache sống lâu nên dùng khóa cache do thời gian chạy sở hữu thay vì tuần tự hóa cấu hình cục bộ. Các mô-đun thời gian chạy sống lâu có trình quét không khoan nhượng với các lệnh gọi `loadConfig()` môi trường xung quanh; hãy dùng `cfg` đã truyền vào, `context.getRuntimeConfig()` của yêu cầu, hoặc `getRuntimeConfig()` tại một ranh giới quy trình rõ ràng.

Các đường dẫn thực thi nhà cung cấp và kênh phải dùng snapshot cấu hình thời gian chạy đang hoạt động, không phải snapshot tệp được trả về để đọc lại hoặc chỉnh sửa cấu hình. Snapshot tệp giữ nguyên các giá trị nguồn như marker SecretRef cho UI và ghi; callback nhà cung cấp cần chế độ xem thời gian chạy đã được phân giải. Khi một helper có thể được gọi bằng snapshot nguồn đang hoạt động hoặc snapshot thời gian chạy đang hoạt động, hãy định tuyến qua `selectApplicableRuntimeConfig()` trước khi đọc thông tin xác thực.

## Không gian tên thời gian chạy

api.runtime.agent

Danh tính agent, thư mục, và quản lý phiên.

typescriptCopy code
[code]
    // Resolve the agent's working directoryconst agentDir = api.runtime.agent.resolveAgentDir(cfg); // Resolve agent workspaceconst workspaceDir = api.runtime.agent.resolveAgentWorkspaceDir(cfg); // Get agent identityconst identity = api.runtime.agent.resolveAgentIdentity(cfg); // Get default thinking levelconst thinking = api.runtime.agent.resolveThinkingDefault({  cfg,  provider,  model,}); // Validate a user-provided thinking level against the active provider profileconst policy = api.runtime.agent.resolveThinkingPolicy({ provider, model });const level = api.runtime.agent.normalizeThinkingLevel("extra high");if (level && policy.levels.some((entry) => entry.id === level)) {  // pass level to an embedded run} // Get agent timeoutconst timeoutMs = api.runtime.agent.resolveAgentTimeoutMs(cfg); // Ensure workspace existsawait api.runtime.agent.ensureAgentWorkspace(cfg); // Run an embedded agent turnconst agentDir = api.runtime.agent.resolveAgentDir(cfg);const result = await api.runtime.agent.runEmbeddedAgent({  sessionId: "my-plugin:task-1",  runId: crypto.randomUUID(),  sessionFile: path.join(agentDir, "sessions", "my-plugin-task-1.jsonl"),  workspaceDir: api.runtime.agent.resolveAgentWorkspaceDir(cfg),  prompt: "Summarize the latest changes",  timeoutMs: api.runtime.agent.resolveAgentTimeoutMs(cfg),});
[/code]

`runEmbeddedAgent(...)` là helper trung lập để bắt đầu một lượt agent OpenClaw bình thường từ mã Plugin. Nó dùng cùng quy trình phân giải nhà cung cấp/mô hình và lựa chọn agent-harness như các câu trả lời được kích hoạt bởi kênh.

`runEmbeddedPiAgent(...)` vẫn là alias tương thích.

`resolveThinkingPolicy(...)` trả về các mức suy nghĩ được hỗ trợ của nhà cung cấp/mô hình và mặc định tùy chọn. Plugin nhà cung cấp sở hữu hồ sơ theo mô hình thông qua các hook suy nghĩ của chúng, vì vậy Plugin công cụ nên gọi helper thời gian chạy này thay vì nhập hoặc sao chép danh sách nhà cung cấp.

`normalizeThinkingLevel(...)` chuyển văn bản người dùng như `on`, `x-high`, hoặc `extra high` thành mức lưu trữ chuẩn trước khi kiểm tra nó với chính sách đã phân giải.

**Các helper kho phiên** nằm dưới `api.runtime.agent.session`:

typescriptCopy code
[code]
    const storePath = api.runtime.agent.session.resolveStorePath(cfg);const store = api.runtime.agent.session.loadSessionStore(storePath);await api.runtime.agent.session.updateSessionStore(storePath, (nextStore) => {  // Patch one entry without replacing the whole file from stale state.  nextStore[sessionKey] = { ...nextStore[sessionKey], thinkingLevel: "high" };});const filePath = api.runtime.agent.session.resolveSessionFilePath(cfg, sessionId);
[/code]

Ưu tiên `updateSessionStore(...)` hoặc `updateSessionStoreEntry(...)` cho các lần ghi thời gian chạy. Chúng định tuyến qua trình ghi kho phiên do Gateway sở hữu, giữ lại các cập nhật đồng thời, và tái sử dụng cache nóng. `saveSessionStore(...)` vẫn có sẵn cho khả năng tương thích và các lần ghi lại kiểu bảo trì ngoại tuyến.

api.runtime.agent.defaults

Các hằng số mô hình và nhà cung cấp mặc định:

typescriptCopy code
[code]
    const model = api.runtime.agent.defaults.model; // e.g. "anthropic/claude-sonnet-4-6"const provider = api.runtime.agent.defaults.provider; // e.g. "anthropic"
[/code]

api.runtime.llm

Chạy một hoàn tất văn bản do máy chủ sở hữu mà không nhập nội bộ nhà cung cấp hoặc sao chép phần chuẩn bị mô hình/xác thực/base URL của OpenClaw.

typescriptCopy code
[code]
    const result = await api.runtime.llm.complete({  messages: [{ role: "user", content: "Summarize this transcript." }],  purpose: "my-plugin.summary",  maxTokens: 512,  temperature: 0.2,});
[/code]

Helper này dùng cùng đường dẫn chuẩn bị hoàn tất đơn giản như thời gian chạy tích hợp sẵn của OpenClaw và snapshot cấu hình thời gian chạy do máy chủ sở hữu. Các engine ngữ cảnh nhận capability `llm.complete` gắn với phiên, vì vậy các lệnh gọi mô hình dùng agent của phiên đang hoạt động và không âm thầm rơi về agent mặc định. Kết quả bao gồm quy thuộc nhà cung cấp/mô hình/agent cùng với mức sử dụng token, cache, và chi phí ước tính đã chuẩn hóa khi có sẵn.

api.runtime.subagent

Khởi chạy và quản lý các lần chạy subagent nền.

typescriptCopy code
[code]
    // Start a subagent runconst { runId } = await api.runtime.subagent.run({  sessionKey: "agent:main:subagent:search-helper",  message: "Expand this query into focused follow-up searches.",  provider: "openai", // optional override  model: "gpt-4.1-mini", // optional override  deliver: false,}); // Wait for completionconst result = await api.runtime.subagent.waitForRun({ runId, timeoutMs: 30000 }); // Read session messagesconst { messages } = await api.runtime.subagent.getSessionMessages({  sessionKey: "agent:main:subagent:search-helper",  limit: 10,}); // Delete a sessionawait api.runtime.subagent.deleteSession({  sessionKey: "agent:main:subagent:search-helper",});
[/code]

`deleteSession(...)` có thể xóa các phiên được tạo bởi cùng Plugin thông qua `api.runtime.subagent.run(...)`. Việc xóa các phiên người dùng hoặc người vận hành tùy ý vẫn yêu cầu một yêu cầu Gateway phạm vi quản trị viên.

api.runtime.nodes

Liệt kê các Node đã kết nối và gọi một lệnh do Node lưu trữ từ mã Plugin được Gateway tải hoặc từ các lệnh CLI của Plugin. Dùng cơ chế này khi Plugin sở hữu công việc cục bộ trên một thiết bị đã ghép cặp, ví dụ cầu nối trình duyệt hoặc âm thanh trên một máy Mac khác.

typescriptCopy code
[code]
    const { nodes } = await api.runtime.nodes.list({ connected: true }); const result = await api.runtime.nodes.invoke({  nodeId: "mac-studio",  command: "my-plugin.command",  params: { action: "start" },  timeoutMs: 30000,});
[/code]

Bên trong Gateway, thời gian chạy này là trong quy trình. Trong các lệnh CLI của Plugin, nó gọi Gateway đã cấu hình qua RPC, vì vậy các lệnh như `openclaw googlemeet recover-tab` có thể kiểm tra các Node đã ghép cặp từ terminal. Các lệnh Node vẫn đi qua quy trình ghép cặp Node Gateway bình thường, danh sách cho phép lệnh, chính sách gọi Node của Plugin, và xử lý lệnh cục bộ trên Node.

Các Plugin phơi bày lệnh do Node lưu trữ nguy hiểm nên đăng ký chính sách gọi Node bằng `api.registerNodeInvokePolicy(...)`. Chính sách chạy trong Gateway sau các kiểm tra danh sách cho phép lệnh và trước khi lệnh được chuyển tiếp đến Node, vì vậy các lệnh gọi `node.invoke` trực tiếp và các công cụ Plugin cấp cao hơn dùng chung cùng một đường dẫn thực thi.

api.runtime.tasks.managedFlows

Gắn một thời gian chạy Task Flow vào khóa phiên OpenClaw hiện có hoặc ngữ cảnh công cụ tin cậy, rồi tạo và quản lý Task Flow mà không truyền chủ sở hữu trên mọi lệnh gọi.

Task Flow theo dõi trạng thái quy trình làm việc nhiều bước bền vững. Nó không phải là bộ lập lịch: dùng Cron hoặc `api.session.workflow.scheduleSessionTurn(...)` cho các lần đánh thức trong tương lai, rồi dùng `managedFlows` từ lượt đã lập lịch khi công việc đó cần trạng thái flow, tác vụ con, chờ, hoặc hủy.

typescriptCopy code
[code]
    const taskFlow = api.runtime.tasks.managedFlows.fromToolContext(ctx); const created = taskFlow.createManaged({  controllerId: "my-plugin/review-batch",  goal: "Review new pull requests",}); const child = taskFlow.runTask({  flowId: created.flowId,  runtime: "acp",  childSessionKey: "agent:main:subagent:reviewer",  task: "Review PR #123",  status: "running",  startedAt: Date.now(),}); const waiting = taskFlow.setWaiting({  flowId: created.flowId,  expectedRevision: created.revision,  currentStep: "await-human-reply",  waitJson: { kind: "reply", channel: "telegram" },});
[/code]

Sử dụng `bindSession({ sessionKey, requesterOrigin })` khi bạn đã có khóa phiên OpenClaw đáng tin cậy từ lớp ràng buộc riêng của mình. Không ràng buộc từ đầu vào thô của người dùng.

api.runtime.tts

Tổng hợp văn bản thành giọng nói.

typescriptCopy code
[code]
    // Standard TTSconst clip = await api.runtime.tts.textToSpeech({  text: "Hello from OpenClaw",  cfg: api.config,}); // Telephony-optimized TTSconst telephonyClip = await api.runtime.tts.textToSpeechTelephony({  text: "Hello from OpenClaw",  cfg: api.config,}); // List available voicesconst voices = await api.runtime.tts.listVoices({  provider: "elevenlabs",  cfg: api.config,});
[/code]

Sử dụng cấu hình lõi `messages.tts` và lựa chọn nhà cung cấp. Trả về bộ đệm âm thanh PCM + tốc độ lấy mẫu.

api.runtime.mediaUnderstanding

Phân tích hình ảnh, âm thanh và video.

typescriptCopy code
[code]
    // Describe an imageconst image = await api.runtime.mediaUnderstanding.describeImageFile({  filePath: "/tmp/inbound-photo.jpg",  cfg: api.config,  agentDir: "/tmp/agent",}); // Transcribe audioconst { text } = await api.runtime.mediaUnderstanding.transcribeAudioFile({  filePath: "/tmp/inbound-audio.ogg",  cfg: api.config,  mime: "audio/ogg", // optional, for when MIME cannot be inferred}); // Describe a videoconst video = await api.runtime.mediaUnderstanding.describeVideoFile({  filePath: "/tmp/inbound-video.mp4",  cfg: api.config,}); // Generic file analysisconst result = await api.runtime.mediaUnderstanding.runFile({  filePath: "/tmp/inbound-file.pdf",  cfg: api.config,}); // Structured image extraction through a specific provider/model.// Include at least one image; text inputs are supplemental context.const evidence = await api.runtime.mediaUnderstanding.extractStructuredWithModel({  provider: "codex",  model: "gpt-5.5",  input: [    {      type: "image",      buffer: receiptImageBuffer,      fileName: "receipt.png",      mime: "image/png",    },    { type: "text", text: "Prefer the printed total over handwritten notes." },  ],  instructions: "Extract vendor, total, and searchable tags.",  schemaName: "receipt.evidence",  jsonSchema: {    type: "object",    properties: {      vendor: { type: "string" },      total: { type: "number" },      tags: { type: "array", items: { type: "string" } },    },    required: ["vendor", "total"],  },  cfg: api.config,});
[/code]

Trả về `{ text: undefined }` khi không tạo ra đầu ra nào (ví dụ: đầu vào bị bỏ qua).

api.runtime.imageGeneration

Tạo hình ảnh.

typescriptCopy code
[code]
    const result = await api.runtime.imageGeneration.generate({  prompt: "A robot painting a sunset",  cfg: api.config,}); const providers = api.runtime.imageGeneration.listProviders({ cfg: api.config });
[/code]

api.runtime.webSearch

Tìm kiếm web.

typescriptCopy code
[code]
    const providers = api.runtime.webSearch.listProviders({ config: api.config }); const result = await api.runtime.webSearch.search({  config: api.config,  args: { query: "OpenClaw plugin SDK", count: 5 },});
[/code]

api.runtime.media

Tiện ích phương tiện cấp thấp.

typescriptCopy code
[code]
    const webMedia = await api.runtime.media.loadWebMedia(url);const mime = await api.runtime.media.detectMime(buffer);const kind = api.runtime.media.mediaKindFromMime("image/jpeg"); // "image"const isVoice = api.runtime.media.isVoiceCompatibleAudio(filePath);const metadata = await api.runtime.media.getImageMetadata(filePath);const resized = await api.runtime.media.resizeToJpeg(buffer, { maxWidth: 800 });const terminalQr = await api.runtime.media.renderQrTerminal("https://openclaw.ai");const pngQr = await api.runtime.media.renderQrPngBase64("https://openclaw.ai", {  scale: 6, // 1-12  marginModules: 4, // 0-16});const pngQrDataUrl = await api.runtime.media.renderQrPngDataUrl("https://openclaw.ai");const tmpRoot = resolvePreferredOpenClawTmpDir();const pngQrFile = await api.runtime.media.writeQrPngTempFile("https://openclaw.ai", {  tmpRoot,  dirPrefix: "my-plugin-qr-",  fileName: "qr.png",});
[/code]

api.runtime.config

Ảnh chụp cấu hình runtime hiện tại và các thao tác ghi cấu hình theo giao dịch. Ưu tiên cấu hình đã được truyền vào đường dẫn gọi đang hoạt động; chỉ sử dụng `current()` khi trình xử lý cần trực tiếp ảnh chụp của tiến trình.

typescriptCopy code
[code]
    const cfg = api.runtime.config.current();await api.runtime.config.mutateConfigFile({  afterWrite: { mode: "auto" },  mutate(draft) {    draft.plugins ??= {};  },});
[/code]

`mutateConfigFile(...)` và `replaceConfigFile(...)` trả về một giá trị `followUp`, ví dụ `{ mode: "restart", requiresRestart: true, reason }`, ghi lại ý định của trình ghi mà không lấy quyền điều khiển khởi động lại khỏi Gateway.

api.runtime.system

Tiện ích cấp hệ thống.

typescriptCopy code
[code]
    await api.runtime.system.enqueueSystemEvent(event);api.runtime.system.requestHeartbeat({  source: "other",  intent: "event",  reason: "plugin-event",});api.runtime.system.requestHeartbeatNow({ reason: "plugin-event" }); // Deprecated compatibility alias.const output = await api.runtime.system.runCommandWithTimeout(cmd, args, opts);const hint = api.runtime.system.formatNativeDependencyHint(pkg);
[/code]

api.runtime.events

Đăng ký sự kiện.

typescriptCopy code
[code]
    api.runtime.events.onAgentEvent((event) => {  /* ... */});api.runtime.events.onSessionTranscriptUpdate((update) => {  /* ... */});
[/code]

api.runtime.logging

Ghi log.

typescriptCopy code
[code]
    const verbose = api.runtime.logging.shouldLogVerbose();const childLogger = api.runtime.logging.getChildLogger({ plugin: "my-plugin" }, { level: "debug" });
[/code]

api.runtime.modelAuth

Phân giải xác thực mô hình và nhà cung cấp.

typescriptCopy code
[code]
    const auth = await api.runtime.modelAuth.getApiKeyForModel({ model, cfg });const providerAuth = await api.runtime.modelAuth.resolveApiKeyForProvider({  provider: "openai",  cfg,});
[/code]

api.runtime.state

Phân giải thư mục trạng thái và lưu trữ theo khóa dựa trên SQLite.

typescriptCopy code
[code]
    const stateDir = api.runtime.state.resolveStateDir(process.env);const store = api.runtime.state.openKeyedStore&lt;MyRecord&gt;({  namespace: "my-feature",  maxEntries: 200,  defaultTtlMs: 15 * 60_000,}); await store.register("key-1", { value: "hello" });const claimed = await store.registerIfAbsent("dedupe-key", { value: "first" });const value = await store.lookup("key-1");await store.consume("key-1");await store.clear();
[/code]

Kho lưu trữ theo khóa tồn tại qua các lần khởi động lại và được cô lập theo id Plugin được ràng buộc với runtime. Sử dụng `registerIfAbsent(...)` cho các yêu cầu khử trùng lặp nguyên tử: hàm này trả về `true` khi khóa bị thiếu hoặc đã hết hạn và được đăng ký, hoặc `false` khi một giá trị còn hiệu lực đã tồn tại mà không ghi đè giá trị, thời gian tạo hoặc TTL của nó. Giới hạn: `maxEntries` cho mỗi namespace, 1.000 hàng còn hiệu lực cho mỗi Plugin, giá trị JSON dưới 64KB và tùy chọn hết hạn TTL.

api.runtime.tools

Factory công cụ bộ nhớ và CLI.

typescriptCopy code
[code]
    const getTool = api.runtime.tools.createMemoryGetTool(/* ... */);const searchTool = api.runtime.tools.createMemorySearchTool(/* ... */);api.runtime.tools.registerMemoryCli(/* ... */);
[/code]

api.runtime.channel

Trình trợ giúp runtime dành riêng cho kênh (có sẵn khi một Plugin kênh được tải).

`api.runtime.channel.mentions` là bề mặt chính sách nhắc đến đầu vào dùng chung cho các Plugin kênh đi kèm sử dụng tiêm runtime:

typescriptCopy code
[code]
    const mentionMatch = api.runtime.channel.mentions.matchesMentionWithExplicit(text, {  mentionRegexes,  mentionPatterns,}); const decision = api.runtime.channel.mentions.resolveInboundMentionDecision({  facts: {    canDetectMention: true,    wasMentioned: mentionMatch.matched,    implicitMentionKinds: api.runtime.channel.mentions.implicitMentionKindWhen(      "reply_to_bot",      isReplyToBot,    ),  },  policy: {    isGroup,    requireMention,    allowTextCommands,    hasControlCommand,    commandAuthorized,  },});
[/code]

Các trình trợ giúp nhắc đến có sẵn:

  * `buildMentionRegexes`
  * `matchesMentionPatterns`
  * `matchesMentionWithExplicit`
  * `implicitMentionKindWhen`
  * `resolveInboundMentionDecision`


`api.runtime.channel.mentions` cố ý không phơi bày các trình trợ giúp tương thích `resolveMentionGating*` cũ hơn. Ưu tiên đường dẫn `{ facts, policy }` đã chuẩn hóa.

## Lưu trữ tham chiếu runtime

Sử dụng `createPluginRuntimeStore` để lưu trữ tham chiếu runtime nhằm dùng bên ngoài callback `register`:

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

## Các trường `api` cấp cao nhất khác

Ngoài `api.runtime`, đối tượng API cũng cung cấp:

ID Plugin.

Tên hiển thị của Plugin.

Ảnh chụp nhanh cấu hình hiện tại (ảnh chụp nhanh thời gian chạy trong bộ nhớ đang hoạt động khi có sẵn).

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaS5wbHVnaW5Db25maWciIHR5cGU9IlJlY29yZDxzdHJpbmcsIHVua25vd24 "> Cấu hình dành riêng cho Plugin từ `plugins.entries.<id>.config`.

Trình ghi nhật ký theo phạm vi (`debug`, `info`, `warn`, `error`).

Chế độ tải hiện tại; `"setup-runtime"` là cửa sổ khởi động/thiết lập nhẹ trước mục nhập đầy đủ.

## Liên quan

  * [Nội bộ Plugin](</vi/plugins/architecture>) — mô hình năng lực và registry
  * [Điểm vào SDK](</vi/plugins/sdk-entrypoints>) — tùy chọn `definePluginEntry`
  * [Tổng quan SDK](</vi/plugins/sdk-overview>) — tham chiếu đường dẫn con


Was this useful?YesNo