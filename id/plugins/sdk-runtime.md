---
title: Pembantu waktu eksekusi Plugin
source_url: https://docs.openclaw.ai/id/plugins/sdk-runtime
scraped_at: 2026-05-25
---

Referensi untuk objek `api.runtime` yang disuntikkan ke setiap plugin selama registrasi. Gunakan helper ini alih-alih mengimpor internal host secara langsung.

[**Channel plugins** Panduan langkah demi langkah yang menggunakan helper ini dalam konteks untuk plugin channel. ](</id/plugins/sdk-channel-plugins>) [**Provider plugins** Panduan langkah demi langkah yang menggunakan helper ini dalam konteks untuk plugin provider. ](</id/plugins/sdk-provider-plugins>)

typescriptCopy code
[code]
    register(api) {  const runtime = api.runtime;}
[/code]

## Pemuatan dan penulisan konfigurasi

Utamakan konfigurasi yang sudah diteruskan ke jalur panggilan aktif, misalnya `api.config` saat registrasi atau argumen `cfg` pada callback channel/provider. Ini menjaga satu snapshot proses mengalir melalui pekerjaan alih-alih memparsing ulang konfigurasi pada hot path.

Gunakan `api.runtime.config.current()` hanya ketika handler yang berumur panjang memerlukan snapshot proses saat ini dan tidak ada konfigurasi yang diteruskan ke fungsi tersebut. Nilai yang dikembalikan bersifat readonly; clone atau gunakan helper mutasi sebelum mengedit.

Factory tool menerima `ctx.runtimeConfig` plus `ctx.getRuntimeConfig()`. Gunakan getter di dalam callback `execute` milik tool yang berumur panjang ketika konfigurasi dapat berubah setelah definisi tool dibuat.

Pertahankan perubahan dengan `api.runtime.config.mutateConfigFile(...)` atau `api.runtime.config.replaceConfigFile(...)`. Setiap penulisan harus memilih kebijakan `afterWrite` yang eksplisit:

  * `afterWrite: { mode: "auto" }` membiarkan pemuat ulang gateway menentukan.
  * `afterWrite: { mode: "restart", reason: "..." }` memaksa restart bersih ketika penulis mengetahui hot reload tidak aman.
  * `afterWrite: { mode: "none", reason: "..." }` menekan reload/restart otomatis hanya ketika pemanggil memiliki tindak lanjutnya.


Helper mutasi mengembalikan `afterWrite` plus ringkasan `followUp` bertipe agar pemanggil dapat mencatat log atau menguji apakah mereka meminta restart. Gateway tetap memiliki kewenangan atas kapan restart itu benar-benar terjadi.

`api.runtime.config.loadConfig()` dan `api.runtime.config.writeConfigFile(...)` adalah helper kompatibilitas yang sudah deprecated di bawah `runtime-config-load-write`. Keduanya memperingatkan sekali saat runtime, dan tetap tersedia untuk plugin eksternal lama selama jendela migrasi. Plugin bawaan tidak boleh menggunakannya; penjaga batas konfigurasi gagal jika kode plugin memanggilnya atau mengimpor helper tersebut dari subpath SDK plugin.

Untuk impor SDK langsung, gunakan subpath konfigurasi yang terfokus alih-alih barrel kompatibilitas luas `openclaw/plugin-sdk/config-runtime`: `config-contracts` untuk tipe, `plugin-config-runtime` untuk asersi konfigurasi yang sudah dimuat dan pencarian entri plugin, `runtime-config-snapshot` untuk snapshot proses saat ini, dan `config-mutation` untuk penulisan. Pengujian plugin bawaan harus me-mock subpath terfokus ini secara langsung alih-alih me-mock barrel kompatibilitas luas.

Kode runtime internal OpenClaw memiliki arah yang sama: muat konfigurasi sekali di batas CLI, gateway, atau proses, lalu teruskan nilai itu. Penulisan mutasi yang berhasil memperbarui snapshot runtime proses dan memajukan revisi internalnya; cache yang berumur panjang harus menggunakan kunci cache milik runtime alih-alih menserialisasi konfigurasi secara lokal. Modul runtime yang berumur panjang memiliki pemindai tanpa toleransi untuk panggilan ambient `loadConfig()`; gunakan `cfg` yang diteruskan, `context.getRuntimeConfig()` permintaan, atau `getRuntimeConfig()` pada batas proses eksplisit.

Jalur eksekusi provider dan channel harus menggunakan snapshot konfigurasi runtime aktif, bukan snapshot file yang dikembalikan untuk pembacaan ulang atau pengeditan konfigurasi. Snapshot file mempertahankan nilai sumber seperti marker SecretRef untuk UI dan penulisan; callback provider memerlukan tampilan runtime yang sudah di-resolve. Ketika helper dapat dipanggil dengan snapshot sumber aktif atau snapshot runtime aktif, rute melalui `selectApplicableRuntimeConfig()` sebelum membaca kredensial.

## Namespace runtime

api.runtime.agent

Identitas agent, direktori, dan manajemen sesi.

typescriptCopy code
[code]
    // Resolve the agent's working directoryconst agentDir = api.runtime.agent.resolveAgentDir(cfg); // Resolve agent workspaceconst workspaceDir = api.runtime.agent.resolveAgentWorkspaceDir(cfg); // Get agent identityconst identity = api.runtime.agent.resolveAgentIdentity(cfg); // Get default thinking levelconst thinking = api.runtime.agent.resolveThinkingDefault({  cfg,  provider,  model,}); // Validate a user-provided thinking level against the active provider profileconst policy = api.runtime.agent.resolveThinkingPolicy({ provider, model });const level = api.runtime.agent.normalizeThinkingLevel("extra high");if (level && policy.levels.some((entry) => entry.id === level)) {  // pass level to an embedded run} // Get agent timeoutconst timeoutMs = api.runtime.agent.resolveAgentTimeoutMs(cfg); // Ensure workspace existsawait api.runtime.agent.ensureAgentWorkspace(cfg); // Run an embedded agent turnconst agentDir = api.runtime.agent.resolveAgentDir(cfg);const result = await api.runtime.agent.runEmbeddedAgent({  sessionId: "my-plugin:task-1",  runId: crypto.randomUUID(),  sessionFile: path.join(agentDir, "sessions", "my-plugin-task-1.jsonl"),  workspaceDir: api.runtime.agent.resolveAgentWorkspaceDir(cfg),  prompt: "Summarize the latest changes",  timeoutMs: api.runtime.agent.resolveAgentTimeoutMs(cfg),});
[/code]

`runEmbeddedAgent(...)` adalah helper netral untuk memulai giliran agent OpenClaw normal dari kode plugin. Helper ini menggunakan resolusi provider/model dan pemilihan agent-harness yang sama seperti balasan yang dipicu channel.

`runEmbeddedPiAgent(...)` tetap menjadi alias kompatibilitas.

`resolveThinkingPolicy(...)` mengembalikan tingkat thinking yang didukung provider/model dan default opsional. Plugin provider memiliki profil khusus model melalui hook thinking mereka, jadi plugin tool harus memanggil helper runtime ini alih-alih mengimpor atau menduplikasi daftar provider.

`normalizeThinkingLevel(...)` mengonversi teks pengguna seperti `on`, `x-high`, atau `extra high` ke tingkat tersimpan kanonis sebelum memeriksanya terhadap kebijakan yang sudah di-resolve.

**Helper penyimpanan sesi** berada di bawah `api.runtime.agent.session`:

typescriptCopy code
[code]
    const storePath = api.runtime.agent.session.resolveStorePath(cfg);const store = api.runtime.agent.session.loadSessionStore(storePath);await api.runtime.agent.session.updateSessionStore(storePath, (nextStore) => {  // Patch one entry without replacing the whole file from stale state.  nextStore[sessionKey] = { ...nextStore[sessionKey], thinkingLevel: "high" };});const filePath = api.runtime.agent.session.resolveSessionFilePath(cfg, sessionId);
[/code]

Utamakan `updateSessionStore(...)` atau `updateSessionStoreEntry(...)` untuk penulisan runtime. Keduanya dirutekan melalui penulis session-store milik Gateway, mempertahankan pembaruan bersamaan, dan menggunakan ulang cache panas. `saveSessionStore(...)` tetap tersedia untuk kompatibilitas dan penulisan ulang bergaya pemeliharaan offline.

api.runtime.agent.defaults

Konstanta model dan provider default:

typescriptCopy code
[code]
    const model = api.runtime.agent.defaults.model; // e.g. "anthropic/claude-sonnet-4-6"const provider = api.runtime.agent.defaults.provider; // e.g. "anthropic"
[/code]

api.runtime.llm

Jalankan text completion milik host tanpa mengimpor internal provider atau menduplikasi persiapan model/auth/base URL OpenClaw.

typescriptCopy code
[code]
    const result = await api.runtime.llm.complete({  messages: [{ role: "user", content: "Summarize this transcript." }],  purpose: "my-plugin.summary",  maxTokens: 512,  temperature: 0.2,});
[/code]

Helper ini menggunakan jalur persiapan simple-completion yang sama seperti runtime bawaan OpenClaw dan snapshot konfigurasi runtime milik host. Engine konteks menerima kapabilitas `llm.complete` yang terikat sesi, sehingga panggilan model menggunakan agent sesi aktif dan tidak diam-diam fallback ke agent default. Hasilnya mencakup atribusi provider/model/agent plus penggunaan token, cache, dan estimasi biaya yang dinormalisasi saat tersedia.

api.runtime.subagent

Luncurkan dan kelola run subagent latar belakang.

typescriptCopy code
[code]
    // Start a subagent runconst { runId } = await api.runtime.subagent.run({  sessionKey: "agent:main:subagent:search-helper",  message: "Expand this query into focused follow-up searches.",  provider: "openai", // optional override  model: "gpt-4.1-mini", // optional override  deliver: false,}); // Wait for completionconst result = await api.runtime.subagent.waitForRun({ runId, timeoutMs: 30000 }); // Read session messagesconst { messages } = await api.runtime.subagent.getSessionMessages({  sessionKey: "agent:main:subagent:search-helper",  limit: 10,}); // Delete a sessionawait api.runtime.subagent.deleteSession({  sessionKey: "agent:main:subagent:search-helper",});
[/code]

`deleteSession(...)` dapat menghapus sesi yang dibuat oleh plugin yang sama melalui `api.runtime.subagent.run(...)`. Menghapus sesi pengguna atau operator sembarang tetap memerlukan permintaan Gateway dengan cakupan admin.

api.runtime.nodes

Daftar node yang terhubung dan panggil perintah node-host dari kode plugin yang dimuat Gateway atau dari perintah CLI plugin. Gunakan ini ketika plugin memiliki pekerjaan lokal pada perangkat yang dipasangkan, misalnya browser atau bridge audio di Mac lain.

typescriptCopy code
[code]
    const { nodes } = await api.runtime.nodes.list({ connected: true }); const result = await api.runtime.nodes.invoke({  nodeId: "mac-studio",  command: "my-plugin.command",  params: { action: "start" },  timeoutMs: 30000,});
[/code]

Di dalam Gateway, runtime ini berada dalam proses. Dalam perintah CLI plugin, ia memanggil Gateway yang dikonfigurasi melalui RPC, sehingga perintah seperti `openclaw googlemeet recover-tab` dapat memeriksa node yang dipasangkan dari terminal. Perintah Node tetap melalui pairing node Gateway normal, allowlist perintah, kebijakan node-invoke plugin, dan penanganan perintah lokal node.

Plugin yang mengekspos perintah node-host berbahaya harus mendaftarkan kebijakan node-invoke dengan `api.registerNodeInvokePolicy(...)`. Kebijakan berjalan di Gateway setelah pemeriksaan allowlist perintah dan sebelum perintah diteruskan ke node, sehingga panggilan `node.invoke` langsung dan tool plugin tingkat lebih tinggi berbagi jalur penegakan yang sama.

api.runtime.tasks.managedFlows

Ikat runtime Task Flow ke kunci sesi OpenClaw yang ada atau konteks tool tepercaya, lalu buat dan kelola Task Flow tanpa meneruskan owner pada setiap panggilan.

Task Flow melacak state workflow multi-langkah yang tahan lama. Ini bukan scheduler: gunakan Cron atau `api.session.workflow.scheduleSessionTurn(...)` untuk wakeup masa depan, lalu gunakan `managedFlows` dari giliran terjadwal ketika pekerjaan itu memerlukan state flow, child task, penantian, atau pembatalan.

typescriptCopy code
[code]
    const taskFlow = api.runtime.tasks.managedFlows.fromToolContext(ctx); const created = taskFlow.createManaged({  controllerId: "my-plugin/review-batch",  goal: "Review new pull requests",}); const child = taskFlow.runTask({  flowId: created.flowId,  runtime: "acp",  childSessionKey: "agent:main:subagent:reviewer",  task: "Review PR #123",  status: "running",  startedAt: Date.now(),}); const waiting = taskFlow.setWaiting({  flowId: created.flowId,  expectedRevision: created.revision,  currentStep: "await-human-reply",  waitJson: { kind: "reply", channel: "telegram" },});
[/code]

Gunakan `bindSession({ sessionKey, requesterOrigin })` ketika Anda sudah memiliki kunci sesi OpenClaw tepercaya dari lapisan binding Anda sendiri. Jangan lakukan binding dari input pengguna mentah.

api.runtime.tts

Sintesis teks-ke-ucapan.

typescriptCopy code
[code]
    // Standard TTSconst clip = await api.runtime.tts.textToSpeech({  text: "Hello from OpenClaw",  cfg: api.config,}); // Telephony-optimized TTSconst telephonyClip = await api.runtime.tts.textToSpeechTelephony({  text: "Hello from OpenClaw",  cfg: api.config,}); // List available voicesconst voices = await api.runtime.tts.listVoices({  provider: "elevenlabs",  cfg: api.config,});
[/code]

Menggunakan konfigurasi inti `messages.tts` dan pemilihan penyedia. Mengembalikan buffer audio PCM + laju sampel.

api.runtime.mediaUnderstanding

Analisis gambar, audio, dan video.

typescriptCopy code
[code]
    // Describe an imageconst image = await api.runtime.mediaUnderstanding.describeImageFile({  filePath: "/tmp/inbound-photo.jpg",  cfg: api.config,  agentDir: "/tmp/agent",}); // Transcribe audioconst { text } = await api.runtime.mediaUnderstanding.transcribeAudioFile({  filePath: "/tmp/inbound-audio.ogg",  cfg: api.config,  mime: "audio/ogg", // optional, for when MIME cannot be inferred}); // Describe a videoconst video = await api.runtime.mediaUnderstanding.describeVideoFile({  filePath: "/tmp/inbound-video.mp4",  cfg: api.config,}); // Generic file analysisconst result = await api.runtime.mediaUnderstanding.runFile({  filePath: "/tmp/inbound-file.pdf",  cfg: api.config,}); // Structured image extraction through a specific provider/model.// Include at least one image; text inputs are supplemental context.const evidence = await api.runtime.mediaUnderstanding.extractStructuredWithModel({  provider: "codex",  model: "gpt-5.5",  input: [    {      type: "image",      buffer: receiptImageBuffer,      fileName: "receipt.png",      mime: "image/png",    },    { type: "text", text: "Prefer the printed total over handwritten notes." },  ],  instructions: "Extract vendor, total, and searchable tags.",  schemaName: "receipt.evidence",  jsonSchema: {    type: "object",    properties: {      vendor: { type: "string" },      total: { type: "number" },      tags: { type: "array", items: { type: "string" } },    },    required: ["vendor", "total"],  },  cfg: api.config,});
[/code]

Mengembalikan `{ text: undefined }` ketika tidak ada output yang dihasilkan (misalnya input dilewati).

api.runtime.imageGeneration

Pembuatan gambar.

typescriptCopy code
[code]
    const result = await api.runtime.imageGeneration.generate({  prompt: "A robot painting a sunset",  cfg: api.config,}); const providers = api.runtime.imageGeneration.listProviders({ cfg: api.config });
[/code]

api.runtime.webSearch

Pencarian web.

typescriptCopy code
[code]
    const providers = api.runtime.webSearch.listProviders({ config: api.config }); const result = await api.runtime.webSearch.search({  config: api.config,  args: { query: "OpenClaw plugin SDK", count: 5 },});
[/code]

api.runtime.media

Utilitas media tingkat rendah.

typescriptCopy code
[code]
    const webMedia = await api.runtime.media.loadWebMedia(url);const mime = await api.runtime.media.detectMime(buffer);const kind = api.runtime.media.mediaKindFromMime("image/jpeg"); // "image"const isVoice = api.runtime.media.isVoiceCompatibleAudio(filePath);const metadata = await api.runtime.media.getImageMetadata(filePath);const resized = await api.runtime.media.resizeToJpeg(buffer, { maxWidth: 800 });const terminalQr = await api.runtime.media.renderQrTerminal("https://openclaw.ai");const pngQr = await api.runtime.media.renderQrPngBase64("https://openclaw.ai", {  scale: 6, // 1-12  marginModules: 4, // 0-16});const pngQrDataUrl = await api.runtime.media.renderQrPngDataUrl("https://openclaw.ai");const tmpRoot = resolvePreferredOpenClawTmpDir();const pngQrFile = await api.runtime.media.writeQrPngTempFile("https://openclaw.ai", {  tmpRoot,  dirPrefix: "my-plugin-qr-",  fileName: "qr.png",});
[/code]

api.runtime.config

Snapshot konfigurasi runtime saat ini dan penulisan konfigurasi transaksional. Utamakan konfigurasi yang sudah diteruskan ke jalur panggilan aktif; gunakan `current()` hanya ketika handler membutuhkan snapshot proses secara langsung.

typescriptCopy code
[code]
    const cfg = api.runtime.config.current();await api.runtime.config.mutateConfigFile({  afterWrite: { mode: "auto" },  mutate(draft) {    draft.plugins ??= {};  },});
[/code]

`mutateConfigFile(...)` dan `replaceConfigFile(...)` mengembalikan nilai `followUp`, misalnya `{ mode: "restart", requiresRestart: true, reason }`, yang mencatat intensi penulis tanpa mengambil alih kontrol restart dari Gateway.

api.runtime.system

Utilitas tingkat sistem.

typescriptCopy code
[code]
    await api.runtime.system.enqueueSystemEvent(event);api.runtime.system.requestHeartbeat({  source: "other",  intent: "event",  reason: "plugin-event",});api.runtime.system.requestHeartbeatNow({ reason: "plugin-event" }); // Deprecated compatibility alias.const output = await api.runtime.system.runCommandWithTimeout(cmd, args, opts);const hint = api.runtime.system.formatNativeDependencyHint(pkg);
[/code]

api.runtime.events

Langganan peristiwa.

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

Resolusi autentikasi model dan penyedia.

typescriptCopy code
[code]
    const auth = await api.runtime.modelAuth.getApiKeyForModel({ model, cfg });const providerAuth = await api.runtime.modelAuth.resolveApiKeyForProvider({  provider: "openai",  cfg,});
[/code]

api.runtime.state

Resolusi direktori state dan penyimpanan berbasis kunci yang didukung SQLite.

typescriptCopy code
[code]
    const stateDir = api.runtime.state.resolveStateDir(process.env);const store = api.runtime.state.openKeyedStore&lt;MyRecord&gt;({  namespace: "my-feature",  maxEntries: 200,  defaultTtlMs: 15 * 60_000,}); await store.register("key-1", { value: "hello" });const claimed = await store.registerIfAbsent("dedupe-key", { value: "first" });const value = await store.lookup("key-1");await store.consume("key-1");await store.clear();
[/code]

Penyimpanan berbasis kunci tetap bertahan setelah restart dan diisolasi oleh id Plugin yang terikat runtime. Gunakan `registerIfAbsent(...)` untuk klaim deduplikasi atomik: fungsi ini mengembalikan `true` ketika kunci tidak ada atau sudah kedaluwarsa dan didaftarkan, atau `false` ketika nilai aktif sudah ada tanpa menimpa nilainya, waktu pembuatannya, atau TTL. Batasan: `maxEntries` per namespace, 1.000 baris aktif per Plugin, nilai JSON di bawah 64KB, dan kedaluwarsa TTL opsional.

api.runtime.tools

Factory alat memori dan CLI.

typescriptCopy code
[code]
    const getTool = api.runtime.tools.createMemoryGetTool(/* ... */);const searchTool = api.runtime.tools.createMemorySearchTool(/* ... */);api.runtime.tools.registerMemoryCli(/* ... */);
[/code]

api.runtime.channel

Helper runtime khusus channel (tersedia ketika Plugin channel dimuat).

`api.runtime.channel.mentions` adalah surface kebijakan mention inbound bersama untuk Plugin channel bundel yang menggunakan injeksi runtime:

typescriptCopy code
[code]
    const mentionMatch = api.runtime.channel.mentions.matchesMentionWithExplicit(text, {  mentionRegexes,  mentionPatterns,}); const decision = api.runtime.channel.mentions.resolveInboundMentionDecision({  facts: {    canDetectMention: true,    wasMentioned: mentionMatch.matched,    implicitMentionKinds: api.runtime.channel.mentions.implicitMentionKindWhen(      "reply_to_bot",      isReplyToBot,    ),  },  policy: {    isGroup,    requireMention,    allowTextCommands,    hasControlCommand,    commandAuthorized,  },});
[/code]

Helper mention yang tersedia:

  * `buildMentionRegexes`
  * `matchesMentionPatterns`
  * `matchesMentionWithExplicit`
  * `implicitMentionKindWhen`
  * `resolveInboundMentionDecision`


`api.runtime.channel.mentions` sengaja tidak mengekspos helper kompatibilitas `resolveMentionGating*` yang lebih lama. Utamakan jalur `{ facts, policy }` yang ternormalisasi.

## Menyimpan referensi runtime

Gunakan `createPluginRuntimeStore` untuk menyimpan referensi runtime agar dapat digunakan di luar callback `register`:

* ### Buat penyimpanan

typescriptCopy code
[code]
    import { createPluginRuntimeStore } from "openclaw/plugin-sdk/runtime-store";import type { PluginRuntime } from "openclaw/plugin-sdk/runtime-store"; const store = createPluginRuntimeStore&lt;PluginRuntime&gt;({  pluginId: "my-plugin",  errorMessage: "my-plugin runtime not initialized",});
[/code]

* ### Hubungkan ke entry point

typescriptCopy code
[code]
    export default defineChannelPluginEntry({  id: "my-plugin",  name: "My Plugin",  description: "Example",  plugin: myPlugin,  setRuntime: store.setRuntime,});
[/code]

* ### Akses dari file lain

typescriptCopy code
[code]
    export function getRuntime() {  return store.getRuntime(); // throws if not initialized} export function tryGetRuntime() {  return store.tryGetRuntime(); // returns null if not initialized}
[/code]

## Field `api` tingkat atas lainnya

Selain `api.runtime`, objek API juga menyediakan:

ID Plugin.

Nama tampilan Plugin.

Snapshot konfigurasi saat ini (snapshot runtime dalam memori yang aktif bila tersedia).

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaS5wbHVnaW5Db25maWciIHR5cGU9IlJlY29yZDxzdHJpbmcsIHVua25vd24 "> Konfigurasi khusus Plugin dari `plugins.entries.<id>.config`.

Logger dengan cakupan (`debug`, `info`, `warn`, `error`).

Mode pemuatan saat ini; `"setup-runtime"` adalah jendela startup/penyiapan ringan sebelum entri penuh.

## Terkait

  * [Internal Plugin](</id/plugins/architecture>) — model kapabilitas dan registri
  * [Titik masuk SDK](</id/plugins/sdk-entrypoints>) — opsi `definePluginEntry`
  * [Ringkasan SDK](</id/plugins/sdk-overview>) — referensi subpath


Was this useful?YesNo