---
title: Plugin ランタイムヘルパー
source_url: https://docs.openclaw.ai/ja-JP/plugins/sdk-runtime
scraped_at: 2026-05-25
---

すべてのPlugin登録時に注入される `api.runtime` オブジェクトのリファレンスです。ホスト内部を直接インポートする代わりに、これらのヘルパーを使用してください。

[**Channel plugins** チャネルPluginでこれらのヘルパーを文脈に沿って使用する手順ガイド。 ](</ja-JP/plugins/sdk-channel-plugins>) [**Provider plugins** プロバイダーPluginでこれらのヘルパーを文脈に沿って使用する手順ガイド。 ](</ja-JP/plugins/sdk-provider-plugins>)

typescriptCopy code
[code]
    register(api) {  const runtime = api.runtime;}
[/code]

## 設定の読み込みと書き込み

アクティブな呼び出しパスにすでに渡されている設定を優先してください。たとえば、登録時の `api.config` や、チャネル/プロバイダーのコールバックに渡される `cfg` 引数です。これにより、ホットパスで設定を再解析するのではなく、1つのプロセススナップショットを作業全体に流せます。

長寿命のハンドラーが現在のプロセススナップショットを必要とし、その関数に設定が渡されていない場合にのみ、`api.runtime.config.current()` を使用してください。返される値は読み取り専用です。編集する前にクローンするか、変更ヘルパーを使用してください。

ツールファクトリーは `ctx.runtimeConfig` と `ctx.getRuntimeConfig()` を受け取ります。長寿命ツールの `execute` コールバック内で、ツール定義の作成後に設定が変わる可能性がある場合は、このゲッターを使用してください。

変更は `api.runtime.config.mutateConfigFile(...)` または `api.runtime.config.replaceConfigFile(...)` で永続化します。各書き込みでは、明示的な `afterWrite` ポリシーを選ぶ必要があります。

  * `afterWrite: { mode: "auto" }` はGatewayのリロードプランナーに判断を任せます。
  * `afterWrite: { mode: "restart", reason: "..." }` は、ホットリロードが安全でないと書き込み側が分かっている場合に、クリーンな再起動を強制します。
  * `afterWrite: { mode: "none", reason: "..." }` は、呼び出し側が後続処理を所有している場合にのみ、自動リロード/再起動を抑制します。


変更ヘルパーは `afterWrite` と型付きの `followUp` サマリーを返すため、呼び出し側は再起動を要求したかどうかをログ記録またはテストできます。実際にその再起動がいつ発生するかは、引き続きGatewayが所有します。

`api.runtime.config.loadConfig()` と `api.runtime.config.writeConfigFile(...)` は、`runtime-config-load-write` 配下の非推奨の互換ヘルパーです。実行時に一度だけ警告し、移行期間中は古い外部Plugin向けに引き続き利用できます。バンドルPluginはこれらを使用してはいけません。Pluginコードがこれらを呼び出したり、Plugin SDKサブパスからこれらのヘルパーをインポートしたりすると、設定境界ガードが失敗します。

直接SDKインポートでは、広範な `openclaw/plugin-sdk/config-runtime` 互換バレルではなく、焦点を絞った設定サブパスを使用してください。型には `config-contracts`、すでに読み込まれた設定のアサーションとPluginエントリー検索には `plugin-config-runtime`、現在のプロセススナップショットには `runtime-config-snapshot`、書き込みには `config-mutation` を使用します。バンドルPluginのテストでは、広範な互換バレルをモックするのではなく、これらの焦点を絞ったサブパスを直接モックしてください。

内部のOpenClawランタイムコードも同じ方針です。CLI、Gateway、またはプロセス境界で設定を一度読み込み、その値を渡していきます。成功した変更書き込みはプロセスのランタイムスナップショットを更新し、その内部リビジョンを進めます。長寿命キャッシュは、設定をローカルでシリアライズするのではなく、ランタイムが所有するキャッシュキーに基づく必要があります。長寿命ランタイムモジュールには、環境依存の `loadConfig()` 呼び出しに対するゼロトレランスのスキャナーがあります。渡された `cfg`、リクエストの `context.getRuntimeConfig()`、または明示的なプロセス境界での `getRuntimeConfig()` を使用してください。

プロバイダーとチャネルの実行パスでは、設定の読み戻しや編集のために返されたファイルスナップショットではなく、アクティブなランタイム設定スナップショットを使用する必要があります。ファイルスナップショットは、UIや書き込み向けにSecretRefマーカーなどのソース値を保持します。プロバイダーコールバックには解決済みのランタイムビューが必要です。ヘルパーがアクティブなソーススナップショットまたはアクティブなランタイムスナップショットのどちらでも呼び出される可能性がある場合は、認証情報を読む前に `selectApplicableRuntimeConfig()` を経由してください。

## ランタイム名前空間

api.runtime.agent

エージェントID、ディレクトリ、セッション管理。

typescriptCopy code
[code]
    // Resolve the agent's working directoryconst agentDir = api.runtime.agent.resolveAgentDir(cfg); // Resolve agent workspaceconst workspaceDir = api.runtime.agent.resolveAgentWorkspaceDir(cfg); // Get agent identityconst identity = api.runtime.agent.resolveAgentIdentity(cfg); // Get default thinking levelconst thinking = api.runtime.agent.resolveThinkingDefault({  cfg,  provider,  model,}); // Validate a user-provided thinking level against the active provider profileconst policy = api.runtime.agent.resolveThinkingPolicy({ provider, model });const level = api.runtime.agent.normalizeThinkingLevel("extra high");if (level && policy.levels.some((entry) => entry.id === level)) {  // pass level to an embedded run} // Get agent timeoutconst timeoutMs = api.runtime.agent.resolveAgentTimeoutMs(cfg); // Ensure workspace existsawait api.runtime.agent.ensureAgentWorkspace(cfg); // Run an embedded agent turnconst agentDir = api.runtime.agent.resolveAgentDir(cfg);const result = await api.runtime.agent.runEmbeddedAgent({  sessionId: "my-plugin:task-1",  runId: crypto.randomUUID(),  sessionFile: path.join(agentDir, "sessions", "my-plugin-task-1.jsonl"),  workspaceDir: api.runtime.agent.resolveAgentWorkspaceDir(cfg),  prompt: "Summarize the latest changes",  timeoutMs: api.runtime.agent.resolveAgentTimeoutMs(cfg),});
[/code]

`runEmbeddedAgent(...)` は、Pluginコードから通常のOpenClawエージェントターンを開始するための中立的なヘルパーです。チャネルからトリガーされた返信と同じプロバイダー/モデル解決とエージェントハーネス選択を使用します。

`runEmbeddedPiAgent(...)` は互換エイリアスとして残っています。

`resolveThinkingPolicy(...)` は、プロバイダー/モデルがサポートする思考レベルと任意のデフォルトを返します。プロバイダーPluginは思考フックを通じてモデル固有のプロファイルを所有するため、ツールPluginはプロバイダー一覧をインポートまたは重複させるのではなく、このランタイムヘルパーを呼び出してください。

`normalizeThinkingLevel(...)` は、`on`、`x-high`、`extra high` などのユーザーテキストを、解決済みポリシーと照合する前に正規の保存レベルへ変換します。

**セッションストアヘルパー** は `api.runtime.agent.session` の下にあります。

typescriptCopy code
[code]
    const storePath = api.runtime.agent.session.resolveStorePath(cfg);const store = api.runtime.agent.session.loadSessionStore(storePath);await api.runtime.agent.session.updateSessionStore(storePath, (nextStore) => {  // Patch one entry without replacing the whole file from stale state.  nextStore[sessionKey] = { ...nextStore[sessionKey], thinkingLevel: "high" };});const filePath = api.runtime.agent.session.resolveSessionFilePath(cfg, sessionId);
[/code]

ランタイムの書き込みには `updateSessionStore(...)` または `updateSessionStoreEntry(...)` を優先してください。これらは Gateway が所有するセッションストアライターを経由し、同時更新を保持し、ホットキャッシュを再利用します。`saveSessionStore(...)` は互換性とオフラインメンテナンス形式の書き換えのために引き続き利用できます。

api.runtime.agent.defaults

デフォルトモデルとプロバイダー定数:

typescriptCopy code
[code]
    const model = api.runtime.agent.defaults.model; // e.g. "anthropic/claude-sonnet-4-6"const provider = api.runtime.agent.defaults.provider; // e.g. "anthropic"
[/code]

api.runtime.llm

プロバイダー内部をインポートしたり、OpenClaw のモデル、認証、ベース URL の準備を重複させたりせずに、ホスト所有のテキスト補完を実行します。

typescriptCopy code
[code]
    const result = await api.runtime.llm.complete({  messages: [{ role: "user", content: "Summarize this transcript." }],  purpose: "my-plugin.summary",  maxTokens: 512,  temperature: 0.2,});
[/code]

このヘルパーは、OpenClaw の組み込みランタイムと同じシンプル補完の準備パス、およびホスト所有のランタイム設定スナップショットを使用します。コンテキストエンジンはセッションに紐づいた `llm.complete` capability を受け取るため、モデル呼び出しはアクティブなセッションのエージェントを使用し、デフォルトエージェントへ暗黙にフォールバックしません。結果には、プロバイダー、モデル、エージェントの帰属に加えて、利用可能な場合は正規化済みのトークン、キャッシュ、推定コストの使用量が含まれます。

api.runtime.subagent

バックグラウンドのサブエージェント実行を起動して管理します。

typescriptCopy code
[code]
    // Start a subagent runconst { runId } = await api.runtime.subagent.run({  sessionKey: "agent:main:subagent:search-helper",  message: "Expand this query into focused follow-up searches.",  provider: "openai", // optional override  model: "gpt-4.1-mini", // optional override  deliver: false,}); // Wait for completionconst result = await api.runtime.subagent.waitForRun({ runId, timeoutMs: 30000 }); // Read session messagesconst { messages } = await api.runtime.subagent.getSessionMessages({  sessionKey: "agent:main:subagent:search-helper",  limit: 10,}); // Delete a sessionawait api.runtime.subagent.deleteSession({  sessionKey: "agent:main:subagent:search-helper",});
[/code]

`deleteSession(...)` は、同じ Plugin が `api.runtime.subagent.run(...)` を通じて作成したセッションを削除できます。任意のユーザーセッションまたはオペレーターセッションの削除には、引き続き管理者スコープの Gateway リクエストが必要です。

api.runtime.nodes

接続済みノードを一覧表示し、Gateway にロードされた Plugin コードまたは Plugin CLI コマンドからノードホストコマンドを呼び出します。ペアリング済みデバイス上のローカル作業を Plugin が所有している場合に使用します。たとえば、別の Mac 上のブラウザーやオーディオブリッジです。

typescriptCopy code
[code]
    const { nodes } = await api.runtime.nodes.list({ connected: true }); const result = await api.runtime.nodes.invoke({  nodeId: "mac-studio",  command: "my-plugin.command",  params: { action: "start" },  timeoutMs: 30000,});
[/code]

Gateway 内では、このランタイムはインプロセスです。Plugin CLI コマンドでは、設定済みの Gateway を RPC 経由で呼び出すため、`openclaw googlemeet recover-tab` のようなコマンドでターミナルからペアリング済みノードを検査できます。ノードコマンドは引き続き、通常の Gateway ノードペアリング、コマンド許可リスト、Plugin のノード呼び出しポリシー、ノードローカルのコマンド処理を通ります。

危険なノードホストコマンドを公開する Plugin は、`api.registerNodeInvokePolicy(...)` でノード呼び出しポリシーを登録する必要があります。このポリシーは Gateway 内で、コマンド許可リストチェックの後、コマンドがノードへ転送される前に実行されるため、直接の `node.invoke` 呼び出しと高レベルの Plugin ツールで同じ強制パスが共有されます。

api.runtime.tasks.managedFlows

Task Flow ランタイムを既存の OpenClaw セッションキーまたは信頼済みツールコンテキストにバインドし、呼び出しごとに所有者を渡さずに Task Flow を作成および管理します。

Task Flow は永続的な複数ステップのワークフロー状態を追跡します。これはスケジューラーではありません。 将来のウェイクアップには Cron または `api.session.workflow.scheduleSessionTurn(...)` を使用し、その作業でフロー状態、子タスク、待機、キャンセルが必要な場合に、スケジュールされたターンから `managedFlows` を使用します。

typescriptCopy code
[code]
    const taskFlow = api.runtime.tasks.managedFlows.fromToolContext(ctx); const created = taskFlow.createManaged({  controllerId: "my-plugin/review-batch",  goal: "Review new pull requests",}); const child = taskFlow.runTask({  flowId: created.flowId,  runtime: "acp",  childSessionKey: "agent:main:subagent:reviewer",  task: "Review PR #123",  status: "running",  startedAt: Date.now(),}); const waiting = taskFlow.setWaiting({  flowId: created.flowId,  expectedRevision: created.revision,  currentStep: "await-human-reply",  waitJson: { kind: "reply", channel: "telegram" },});
[/code]

独自のバインディング層から取得した信頼済みの OpenClaw セッションキーをすでに持っている場合は、`bindSession({ sessionKey, requesterOrigin })` を使用します。生のユーザー入力からバインドしないでください。

api.runtime.tts

テキスト読み上げ合成。

typescriptCopy code
[code]
    // Standard TTSconst clip = await api.runtime.tts.textToSpeech({  text: "Hello from OpenClaw",  cfg: api.config,}); // Telephony-optimized TTSconst telephonyClip = await api.runtime.tts.textToSpeechTelephony({  text: "Hello from OpenClaw",  cfg: api.config,}); // List available voicesconst voices = await api.runtime.tts.listVoices({  provider: "elevenlabs",  cfg: api.config,});
[/code]

コアの `messages.tts` 設定とプロバイダー選択を使用します。PCM 音声バッファー + サンプルレートを返します。

api.runtime.mediaUnderstanding

画像、音声、動画の分析。

typescriptCopy code
[code]
    // Describe an imageconst image = await api.runtime.mediaUnderstanding.describeImageFile({  filePath: "/tmp/inbound-photo.jpg",  cfg: api.config,  agentDir: "/tmp/agent",}); // Transcribe audioconst { text } = await api.runtime.mediaUnderstanding.transcribeAudioFile({  filePath: "/tmp/inbound-audio.ogg",  cfg: api.config,  mime: "audio/ogg", // optional, for when MIME cannot be inferred}); // Describe a videoconst video = await api.runtime.mediaUnderstanding.describeVideoFile({  filePath: "/tmp/inbound-video.mp4",  cfg: api.config,}); // Generic file analysisconst result = await api.runtime.mediaUnderstanding.runFile({  filePath: "/tmp/inbound-file.pdf",  cfg: api.config,}); // Structured image extraction through a specific provider/model.// Include at least one image; text inputs are supplemental context.const evidence = await api.runtime.mediaUnderstanding.extractStructuredWithModel({  provider: "codex",  model: "gpt-5.5",  input: [    {      type: "image",      buffer: receiptImageBuffer,      fileName: "receipt.png",      mime: "image/png",    },    { type: "text", text: "Prefer the printed total over handwritten notes." },  ],  instructions: "Extract vendor, total, and searchable tags.",  schemaName: "receipt.evidence",  jsonSchema: {    type: "object",    properties: {      vendor: { type: "string" },      total: { type: "number" },      tags: { type: "array", items: { type: "string" } },    },    required: ["vendor", "total"],  },  cfg: api.config,});
[/code]

出力が生成されない場合（例: 入力がスキップされた場合）は `{ text: undefined }` を返します。

api.runtime.imageGeneration

画像生成。

typescriptCopy code
[code]
    const result = await api.runtime.imageGeneration.generate({  prompt: "A robot painting a sunset",  cfg: api.config,}); const providers = api.runtime.imageGeneration.listProviders({ cfg: api.config });
[/code]

api.runtime.webSearch

Web 検索。

typescriptCopy code
[code]
    const providers = api.runtime.webSearch.listProviders({ config: api.config }); const result = await api.runtime.webSearch.search({  config: api.config,  args: { query: "OpenClaw plugin SDK", count: 5 },});
[/code]

api.runtime.media

低レベルのメディアユーティリティ。

typescriptCopy code
[code]
    const webMedia = await api.runtime.media.loadWebMedia(url);const mime = await api.runtime.media.detectMime(buffer);const kind = api.runtime.media.mediaKindFromMime("image/jpeg"); // "image"const isVoice = api.runtime.media.isVoiceCompatibleAudio(filePath);const metadata = await api.runtime.media.getImageMetadata(filePath);const resized = await api.runtime.media.resizeToJpeg(buffer, { maxWidth: 800 });const terminalQr = await api.runtime.media.renderQrTerminal("https://openclaw.ai");const pngQr = await api.runtime.media.renderQrPngBase64("https://openclaw.ai", {  scale: 6, // 1-12  marginModules: 4, // 0-16});const pngQrDataUrl = await api.runtime.media.renderQrPngDataUrl("https://openclaw.ai");const tmpRoot = resolvePreferredOpenClawTmpDir();const pngQrFile = await api.runtime.media.writeQrPngTempFile("https://openclaw.ai", {  tmpRoot,  dirPrefix: "my-plugin-qr-",  fileName: "qr.png",});
[/code]

api.runtime.config

現在のランタイム設定スナップショットとトランザクション形式の設定書き込み。アクティブな呼び出し経路にすでに渡されている設定を優先してください。ハンドラーがプロセススナップショットを直接必要とする場合にのみ、`current()` を使用します。

typescriptCopy code
[code]
    const cfg = api.runtime.config.current();await api.runtime.config.mutateConfigFile({  afterWrite: { mode: "auto" },  mutate(draft) {    draft.plugins ??= {};  },});
[/code]

`mutateConfigFile(...)` と `replaceConfigFile(...)` は `followUp` 値を返します。たとえば `{ mode: "restart", requiresRestart: true, reason }` です。 これは、再起動制御を Gateway から奪わずに、書き込み側の意図を記録します。

api.runtime.system

システムレベルのユーティリティ。

typescriptCopy code
[code]
    await api.runtime.system.enqueueSystemEvent(event);api.runtime.system.requestHeartbeat({  source: "other",  intent: "event",  reason: "plugin-event",});api.runtime.system.requestHeartbeatNow({ reason: "plugin-event" }); // Deprecated compatibility alias.const output = await api.runtime.system.runCommandWithTimeout(cmd, args, opts);const hint = api.runtime.system.formatNativeDependencyHint(pkg);
[/code]

api.runtime.events

イベント購読。

typescriptCopy code
[code]
    api.runtime.events.onAgentEvent((event) => {  /* ... */});api.runtime.events.onSessionTranscriptUpdate((update) => {  /* ... */});
[/code]

api.runtime.logging

ロギング。

typescriptCopy code
[code]
    const verbose = api.runtime.logging.shouldLogVerbose();const childLogger = api.runtime.logging.getChildLogger({ plugin: "my-plugin" }, { level: "debug" });
[/code]

api.runtime.modelAuth

モデルとプロバイダー認証の解決。

typescriptCopy code
[code]
    const auth = await api.runtime.modelAuth.getApiKeyForModel({ model, cfg });const providerAuth = await api.runtime.modelAuth.resolveApiKeyForProvider({  provider: "openai",  cfg,});
[/code]

api.runtime.state

状態ディレクトリの解決と、SQLite をバックエンドとするキー付きストレージ。

typescriptCopy code
[code]
    const stateDir = api.runtime.state.resolveStateDir(process.env);const store = api.runtime.state.openKeyedStore&lt;MyRecord&gt;({  namespace: "my-feature",  maxEntries: 200,  defaultTtlMs: 15 * 60_000,}); await store.register("key-1", { value: "hello" });const claimed = await store.registerIfAbsent("dedupe-key", { value: "first" });const value = await store.lookup("key-1");await store.consume("key-1");await store.clear();
[/code]

キー付きストアは再起動後も保持され、ランタイムにバインドされた Plugin ID によって分離されます。アトミックな重複排除の主張には `registerIfAbsent(...)` を使用します。キーが存在しない、または期限切れで登録された場合は `true` を返し、生きている値がすでに存在する場合は、その値、作成時刻、TTL を上書きせずに `false` を返します。制限: 名前空間ごとの `maxEntries`、Plugin ごとに 1,000 件の生きている行、64KB 未満の JSON 値、任意の TTL 期限切れ。

api.runtime.tools

Memory ツールファクトリと CLI。

typescriptCopy code
[code]
    const getTool = api.runtime.tools.createMemoryGetTool(/* ... */);const searchTool = api.runtime.tools.createMemorySearchTool(/* ... */);api.runtime.tools.registerMemoryCli(/* ... */);
[/code]

api.runtime.channel

チャンネル固有のランタイムヘルパー（チャンネル Plugin が読み込まれている場合に利用可能）。

`api.runtime.channel.mentions` は、ランタイム注入を使用するバンドル済みチャンネル Plugin 向けの共有インバウンドメンションポリシー面です。

typescriptCopy code
[code]
    const mentionMatch = api.runtime.channel.mentions.matchesMentionWithExplicit(text, {  mentionRegexes,  mentionPatterns,}); const decision = api.runtime.channel.mentions.resolveInboundMentionDecision({  facts: {    canDetectMention: true,    wasMentioned: mentionMatch.matched,    implicitMentionKinds: api.runtime.channel.mentions.implicitMentionKindWhen(      "reply_to_bot",      isReplyToBot,    ),  },  policy: {    isGroup,    requireMention,    allowTextCommands,    hasControlCommand,    commandAuthorized,  },});
[/code]

利用可能なメンションヘルパー:

  * `buildMentionRegexes`
  * `matchesMentionPatterns`
  * `matchesMentionWithExplicit`
  * `implicitMentionKindWhen`
  * `resolveInboundMentionDecision`


`api.runtime.channel.mentions` は、古い `resolveMentionGating*` 互換ヘルパーを意図的に公開していません。正規化された `{ facts, policy }` 経路を優先してください。

## ランタイム参照の保存

`register` コールバックの外部で使用するために、`createPluginRuntimeStore` を使ってランタイム参照を保存します。

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

## その他のトップレベル `api` フィールド

`api.runtime` に加えて、API オブジェクトは次も提供します。

Plugin ID。

Plugin 表示名。

現在の設定スナップショット（利用可能な場合は、アクティブなメモリ内ランタイムスナップショット）。

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaS5wbHVnaW5Db25maWciIHR5cGU9IlJlY29yZDxzdHJpbmcsIHVua25vd24 "> `plugins.entries.<id>.config` からの Plugin 固有の設定。

スコープ付きロガー（`debug`、`info`、`warn`、`error`）。

現在のロードモード。`"setup-runtime"` は、完全なエントリの前にある軽量な起動/セットアップ期間です。

## 関連

  * [Plugin 内部](</ja-JP/plugins/architecture>) — 機能モデルとレジストリ
  * [SDK エントリポイント](</ja-JP/plugins/sdk-entrypoints>) — `definePluginEntry` オプション
  * [SDK 概要](</ja-JP/plugins/sdk-overview>) — サブパスリファレンス


Was this useful?YesNo