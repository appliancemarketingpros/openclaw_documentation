---
title: Plugin çalışma zamanı yardımcıları
source_url: https://docs.openclaw.ai/tr/plugins/sdk-runtime
scraped_at: 2026-05-25
---

Kayıt sırasında her Plugin'e enjekte edilen `api.runtime` nesnesi için başvuru. Bu yardımcıları, ana bilgisayar iç bileşenlerini doğrudan içe aktarmak yerine kullanın.

[**Kanal Plugin'leri** Kanal Plugin'leri için bu yardımcıları bağlam içinde kullanan adım adım kılavuz. ](</tr/plugins/sdk-channel-plugins>) [**Sağlayıcı Plugin'leri** Sağlayıcı Plugin'leri için bu yardımcıları bağlam içinde kullanan adım adım kılavuz. ](</tr/plugins/sdk-provider-plugins>)

typescriptCopy code
[code]
    register(api) {  const runtime = api.runtime;}
[/code]

## Yapılandırma yükleme ve yazma

Etkin çağrı yoluna zaten geçirilmiş yapılandırmayı tercih edin; örneğin kayıt sırasında `api.config` veya kanal/sağlayıcı geri çağrılarında bir `cfg` bağımsız değişkeni. Bu, sıcak yollarda yapılandırmayı yeniden ayrıştırmak yerine tek bir süreç anlık görüntüsünün iş boyunca akmasını sağlar.

`api.runtime.config.current()` öğesini yalnızca uzun ömürlü bir işleyicinin geçerli süreç anlık görüntüsüne ihtiyaç duyduğu ve bu işleve hiçbir yapılandırma geçirilmediği durumlarda kullanın. Döndürülen değer salt okunurdur; düzenlemeden önce kopyalayın veya bir mutasyon yardımcısı kullanın.

Araç fabrikaları `ctx.runtimeConfig` ve `ctx.getRuntimeConfig()` alır. Yapılandırma, araç tanımı oluşturulduktan sonra değişebiliyorsa uzun ömürlü bir aracın `execute` geri çağrısı içinde getter'ı kullanın.

Değişiklikleri `api.runtime.config.mutateConfigFile(...)` veya `api.runtime.config.replaceConfigFile(...)` ile kalıcı hale getirin. Her yazma açık bir `afterWrite` ilkesi seçmelidir:

  * `afterWrite: { mode: "auto" }`, gateway yeniden yükleme planlayıcısının karar vermesine izin verir.
  * `afterWrite: { mode: "restart", reason: "..." }`, yazıcı sıcak yeniden yüklemenin güvensiz olduğunu bildiğinde temiz bir yeniden başlatmayı zorunlu kılar.
  * `afterWrite: { mode: "none", reason: "..." }`, otomatik yeniden yükleme/yeniden başlatmayı yalnızca çağıran taraf takip işlemini üstlendiğinde bastırır.


Mutasyon yardımcıları, çağıranların yeniden başlatma isteyip istemediklerini günlüğe yazabilmesi veya test edebilmesi için `afterWrite` ile birlikte türlendirilmiş bir `followUp` özeti döndürür. Yeniden başlatmanın gerçekte ne zaman gerçekleşeceğinin sahibi yine Gateway'dir.

`api.runtime.config.loadConfig()` ve `api.runtime.config.writeConfigFile(...)`, `runtime-config-load-write` altındaki kullanımdan kaldırılmış uyumluluk yardımcılarıdır. Çalışma zamanında bir kez uyarı verirler ve geçiş penceresi sırasında eski harici Plugin'ler için kullanılabilir kalırlar. Paketlenmiş Plugin'ler bunları kullanmamalıdır; Plugin kodu bunları çağırırsa veya bu yardımcıları Plugin SDK alt yollarından içe aktarırsa yapılandırma sınırı korumaları başarısız olur.

Doğrudan SDK içe aktarmaları için, geniş `openclaw/plugin-sdk/config-runtime` uyumluluk barrel'ı yerine odaklı yapılandırma alt yollarını kullanın: türler için `config-contracts`, zaten yüklenmiş yapılandırma doğrulamaları ve Plugin giriş araması için `plugin-config-runtime`, geçerli süreç anlık görüntüleri için `runtime-config-snapshot` ve yazmalar için `config-mutation`. Paketlenmiş Plugin testleri, geniş uyumluluk barrel'ını taklit etmek yerine bu odaklı alt yolları doğrudan taklit etmelidir.

Dahili OpenClaw çalışma zamanı kodu da aynı yöndedir: yapılandırmayı CLI, Gateway veya süreç sınırında bir kez yükleyin, ardından bu değeri iletin. Başarılı mutasyon yazmaları süreç çalışma zamanı anlık görüntüsünü yeniler ve dahili revizyonunu ilerletir; uzun ömürlü önbellekler yapılandırmayı yerel olarak serileştirmek yerine çalışma zamanının sahip olduğu önbellek anahtarını temel almalıdır. Uzun ömürlü çalışma zamanı modüllerinde ortamdan `loadConfig()` çağrılarına karşı sıfır toleranslı bir tarayıcı vardır; geçirilmiş bir `cfg`, bir istek `context.getRuntimeConfig()` öğesi veya açık bir süreç sınırında `getRuntimeConfig()` kullanın.

Sağlayıcı ve kanal yürütme yolları, yapılandırma geri okuması veya düzenleme için döndürülen bir dosya anlık görüntüsünü değil, etkin çalışma zamanı yapılandırma anlık görüntüsünü kullanmalıdır. Dosya anlık görüntüleri, kullanıcı arayüzü ve yazmalar için SecretRef işaretçileri gibi kaynak değerleri korur; sağlayıcı geri çağrıları çözümlenmiş çalışma zamanı görünümüne ihtiyaç duyar. Bir yardımcı, etkin kaynak anlık görüntüsü veya etkin çalışma zamanı anlık görüntüsü ile çağrılabiliyorsa kimlik bilgilerini okumadan önce `selectApplicableRuntimeConfig()` üzerinden yönlendirin.

## Çalışma zamanı ad alanları

api.runtime.agent

Aracı kimliği, dizinler ve oturum yönetimi.

typescriptCopy code
[code]
    // Resolve the agent's working directoryconst agentDir = api.runtime.agent.resolveAgentDir(cfg); // Resolve agent workspaceconst workspaceDir = api.runtime.agent.resolveAgentWorkspaceDir(cfg); // Get agent identityconst identity = api.runtime.agent.resolveAgentIdentity(cfg); // Get default thinking levelconst thinking = api.runtime.agent.resolveThinkingDefault({  cfg,  provider,  model,}); // Validate a user-provided thinking level against the active provider profileconst policy = api.runtime.agent.resolveThinkingPolicy({ provider, model });const level = api.runtime.agent.normalizeThinkingLevel("extra high");if (level && policy.levels.some((entry) => entry.id === level)) {  // pass level to an embedded run} // Get agent timeoutconst timeoutMs = api.runtime.agent.resolveAgentTimeoutMs(cfg); // Ensure workspace existsawait api.runtime.agent.ensureAgentWorkspace(cfg); // Run an embedded agent turnconst agentDir = api.runtime.agent.resolveAgentDir(cfg);const result = await api.runtime.agent.runEmbeddedAgent({  sessionId: "my-plugin:task-1",  runId: crypto.randomUUID(),  sessionFile: path.join(agentDir, "sessions", "my-plugin-task-1.jsonl"),  workspaceDir: api.runtime.agent.resolveAgentWorkspaceDir(cfg),  prompt: "Summarize the latest changes",  timeoutMs: api.runtime.agent.resolveAgentTimeoutMs(cfg),});
[/code]

`runEmbeddedAgent(...)`, Plugin kodundan normal bir OpenClaw aracı sırası başlatmak için tarafsız yardımcıdır. Kanal tarafından tetiklenen yanıtlarla aynı sağlayıcı/model çözümlemesini ve aracı donanımı seçimini kullanır.

`runEmbeddedPiAgent(...)` uyumluluk diğer adı olarak kalır.

`resolveThinkingPolicy(...)`, sağlayıcı/modelin desteklenen düşünme düzeylerini ve isteğe bağlı varsayılanı döndürür. Sağlayıcı Plugin'leri, düşünme kancaları aracılığıyla modele özgü profilin sahibidir; bu nedenle araç Plugin'leri sağlayıcı listelerini içe aktarmak veya çoğaltmak yerine bu çalışma zamanı yardımcısını çağırmalıdır.

`normalizeThinkingLevel(...)`, `on`, `x-high` veya `extra high` gibi kullanıcı metnini, çözümlenen ilkeye göre denetlemeden önce kanonik depolanmış düzeye dönüştürür.

**Oturum deposu yardımcıları** `api.runtime.agent.session` altındadır:

typescriptCopy code
[code]
    const storePath = api.runtime.agent.session.resolveStorePath(cfg);const store = api.runtime.agent.session.loadSessionStore(storePath);await api.runtime.agent.session.updateSessionStore(storePath, (nextStore) => {  // Patch one entry without replacing the whole file from stale state.  nextStore[sessionKey] = { ...nextStore[sessionKey], thinkingLevel: "high" };});const filePath = api.runtime.agent.session.resolveSessionFilePath(cfg, sessionId);
[/code]

Çalışma zamanı yazmaları için `updateSessionStore(...)` veya `updateSessionStoreEntry(...)` tercih edin. Bunlar Gateway'in sahip olduğu oturum deposu yazıcısından geçer, eşzamanlı güncellemeleri korur ve sıcak önbelleği yeniden kullanır. `saveSessionStore(...)`, uyumluluk ve çevrimdışı bakım tarzı yeniden yazmalar için kullanılabilir kalır.

api.runtime.agent.defaults

Varsayılan model ve sağlayıcı sabitleri:

typescriptCopy code
[code]
    const model = api.runtime.agent.defaults.model; // e.g. "anthropic/claude-sonnet-4-6"const provider = api.runtime.agent.defaults.provider; // e.g. "anthropic"
[/code]

api.runtime.llm

Sağlayıcı iç bileşenlerini içe aktarmadan veya OpenClaw model/kimlik doğrulama/temel URL hazırlığını çoğaltmadan, ana bilgisayarın sahip olduğu bir metin tamamlama çalıştırın.

typescriptCopy code
[code]
    const result = await api.runtime.llm.complete({  messages: [{ role: "user", content: "Summarize this transcript." }],  purpose: "my-plugin.summary",  maxTokens: 512,  temperature: 0.2,});
[/code]

Yardımcı, OpenClaw'ın yerleşik çalışma zamanı ile aynı basit tamamlama hazırlık yolunu ve ana bilgisayarın sahip olduğu çalışma zamanı yapılandırma anlık görüntüsünü kullanır. Bağlam motorları oturuma bağlı bir `llm.complete` yeteneği alır; böylece model çağrıları etkin oturumun aracısını kullanır ve sessizce varsayılan aracıya geri düşmez. Sonuç, sağlayıcı/model/aracı atıfının yanı sıra kullanılabildiğinde normalleştirilmiş token, önbellek ve tahmini maliyet kullanımını içerir.

api.runtime.subagent

Arka plan alt aracı çalışmalarını başlatın ve yönetin.

typescriptCopy code
[code]
    // Start a subagent runconst { runId } = await api.runtime.subagent.run({  sessionKey: "agent:main:subagent:search-helper",  message: "Expand this query into focused follow-up searches.",  provider: "openai", // optional override  model: "gpt-4.1-mini", // optional override  deliver: false,}); // Wait for completionconst result = await api.runtime.subagent.waitForRun({ runId, timeoutMs: 30000 }); // Read session messagesconst { messages } = await api.runtime.subagent.getSessionMessages({  sessionKey: "agent:main:subagent:search-helper",  limit: 10,}); // Delete a sessionawait api.runtime.subagent.deleteSession({  sessionKey: "agent:main:subagent:search-helper",});
[/code]

`deleteSession(...)`, aynı Plugin tarafından `api.runtime.subagent.run(...)` aracılığıyla oluşturulan oturumları silebilir. Rastgele kullanıcı veya operatör oturumlarını silmek yine de yönetici kapsamlı bir Gateway isteği gerektirir.

api.runtime.nodes

Bağlı düğümleri listeleyin ve Gateway tarafından yüklenen Plugin kodundan veya Plugin CLI komutlarından düğüm ana bilgisayar komutu çağırın. Bir Plugin eşleştirilmiş bir cihazda yerel işi üstlendiğinde, örneğin başka bir Mac'te bir tarayıcı veya ses köprüsü olduğunda bunu kullanın.

typescriptCopy code
[code]
    const { nodes } = await api.runtime.nodes.list({ connected: true }); const result = await api.runtime.nodes.invoke({  nodeId: "mac-studio",  command: "my-plugin.command",  params: { action: "start" },  timeoutMs: 30000,});
[/code]

Gateway içinde bu çalışma zamanı süreç içindedir. Plugin CLI komutlarında yapılandırılmış Gateway'i RPC üzerinden çağırır; böylece `openclaw googlemeet recover-tab` gibi komutlar terminalden eşleştirilmiş düğümleri inceleyebilir. Node komutları yine normal Gateway düğüm eşleştirmesinden, komut izin listelerinden, Plugin düğüm çağırma ilkelerinden ve düğüm yerel komut işleme sürecinden geçer.

Tehlikeli düğüm ana bilgisayar komutları açığa çıkaran Plugin'ler, `api.registerNodeInvokePolicy(...)` ile bir düğüm çağırma ilkesi kaydetmelidir. İlke, komut izin listesi denetimlerinden sonra ve komut düğüme iletilmeden önce Gateway içinde çalışır; böylece doğrudan `node.invoke` çağrıları ve daha üst düzey Plugin araçları aynı yaptırım yolunu paylaşır.

api.runtime.tasks.managedFlows

Task Flow çalışma zamanını mevcut bir OpenClaw oturum anahtarına veya güvenilir araç bağlamına bağlayın; ardından her çağrıda sahip geçirmeden Task Flow'lar oluşturun ve yönetin.

Task Flow dayanıklı çok adımlı iş akışı durumunu izler. Bir zamanlayıcı değildir: gelecekteki uyandırmalar için Cron veya `api.session.workflow.scheduleSessionTurn(...)` kullanın; ardından bu iş akış durumuna, alt görevlere, beklemelere veya iptale ihtiyaç duyduğunda zamanlanmış sıradan `managedFlows` kullanın.

typescriptCopy code
[code]
    const taskFlow = api.runtime.tasks.managedFlows.fromToolContext(ctx); const created = taskFlow.createManaged({  controllerId: "my-plugin/review-batch",  goal: "Review new pull requests",}); const child = taskFlow.runTask({  flowId: created.flowId,  runtime: "acp",  childSessionKey: "agent:main:subagent:reviewer",  task: "Review PR #123",  status: "running",  startedAt: Date.now(),}); const waiting = taskFlow.setWaiting({  flowId: created.flowId,  expectedRevision: created.revision,  currentStep: "await-human-reply",  waitJson: { kind: "reply", channel: "telegram" },});
[/code]

Kendi bağlama katmanınızdan güvenilir bir OpenClaw oturum anahtarınız zaten olduğunda `bindSession({ sessionKey, requesterOrigin })` kullanın. Ham kullanıcı girdisinden bağlama yapmayın.

api.runtime.tts

Metinden konuşmaya sentezi.

typescriptCopy code
[code]
    // Standard TTSconst clip = await api.runtime.tts.textToSpeech({  text: "Hello from OpenClaw",  cfg: api.config,}); // Telephony-optimized TTSconst telephonyClip = await api.runtime.tts.textToSpeechTelephony({  text: "Hello from OpenClaw",  cfg: api.config,}); // List available voicesconst voices = await api.runtime.tts.listVoices({  provider: "elevenlabs",  cfg: api.config,});
[/code]

Çekirdek `messages.tts` yapılandırmasını ve sağlayıcı seçimini kullanır. PCM ses arabelleği + örnekleme hızını döndürür.

api.runtime.mediaUnderstanding

Görüntü, ses ve video analizi.

typescriptCopy code
[code]
    // Describe an imageconst image = await api.runtime.mediaUnderstanding.describeImageFile({  filePath: "/tmp/inbound-photo.jpg",  cfg: api.config,  agentDir: "/tmp/agent",}); // Transcribe audioconst { text } = await api.runtime.mediaUnderstanding.transcribeAudioFile({  filePath: "/tmp/inbound-audio.ogg",  cfg: api.config,  mime: "audio/ogg", // optional, for when MIME cannot be inferred}); // Describe a videoconst video = await api.runtime.mediaUnderstanding.describeVideoFile({  filePath: "/tmp/inbound-video.mp4",  cfg: api.config,}); // Generic file analysisconst result = await api.runtime.mediaUnderstanding.runFile({  filePath: "/tmp/inbound-file.pdf",  cfg: api.config,}); // Structured image extraction through a specific provider/model.// Include at least one image; text inputs are supplemental context.const evidence = await api.runtime.mediaUnderstanding.extractStructuredWithModel({  provider: "codex",  model: "gpt-5.5",  input: [    {      type: "image",      buffer: receiptImageBuffer,      fileName: "receipt.png",      mime: "image/png",    },    { type: "text", text: "Prefer the printed total over handwritten notes." },  ],  instructions: "Extract vendor, total, and searchable tags.",  schemaName: "receipt.evidence",  jsonSchema: {    type: "object",    properties: {      vendor: { type: "string" },      total: { type: "number" },      tags: { type: "array", items: { type: "string" } },    },    required: ["vendor", "total"],  },  cfg: api.config,});
[/code]

Hiç çıktı üretilmediğinde `{ text: undefined }` döndürür (ör. atlanan girdi).

api.runtime.imageGeneration

Görüntü oluşturma.

typescriptCopy code
[code]
    const result = await api.runtime.imageGeneration.generate({  prompt: "A robot painting a sunset",  cfg: api.config,}); const providers = api.runtime.imageGeneration.listProviders({ cfg: api.config });
[/code]

api.runtime.webSearch

Web araması.

typescriptCopy code
[code]
    const providers = api.runtime.webSearch.listProviders({ config: api.config }); const result = await api.runtime.webSearch.search({  config: api.config,  args: { query: "OpenClaw plugin SDK", count: 5 },});
[/code]

api.runtime.media

Düşük düzey medya yardımcıları.

typescriptCopy code
[code]
    const webMedia = await api.runtime.media.loadWebMedia(url);const mime = await api.runtime.media.detectMime(buffer);const kind = api.runtime.media.mediaKindFromMime("image/jpeg"); // "image"const isVoice = api.runtime.media.isVoiceCompatibleAudio(filePath);const metadata = await api.runtime.media.getImageMetadata(filePath);const resized = await api.runtime.media.resizeToJpeg(buffer, { maxWidth: 800 });const terminalQr = await api.runtime.media.renderQrTerminal("https://openclaw.ai");const pngQr = await api.runtime.media.renderQrPngBase64("https://openclaw.ai", {  scale: 6, // 1-12  marginModules: 4, // 0-16});const pngQrDataUrl = await api.runtime.media.renderQrPngDataUrl("https://openclaw.ai");const tmpRoot = resolvePreferredOpenClawTmpDir();const pngQrFile = await api.runtime.media.writeQrPngTempFile("https://openclaw.ai", {  tmpRoot,  dirPrefix: "my-plugin-qr-",  fileName: "qr.png",});
[/code]

api.runtime.config

Geçerli runtime yapılandırma anlık görüntüsü ve işlemsel yapılandırma yazımları. Etkin çağrı yoluna zaten geçirilmiş olan yapılandırmayı tercih edin; `current()` yalnızca işleyicinin süreç anlık görüntüsüne doğrudan ihtiyaç duyması durumunda kullanın.

typescriptCopy code
[code]
    const cfg = api.runtime.config.current();await api.runtime.config.mutateConfigFile({  afterWrite: { mode: "auto" },  mutate(draft) {    draft.plugins ??= {};  },});
[/code]

`mutateConfigFile(...)` ve `replaceConfigFile(...)`, örneğin `{ mode: "restart", requiresRestart: true, reason }` gibi bir `followUp` değeri döndürür; bu değer, yeniden başlatma denetimini Gateway’den almadan yazar niyetini kaydeder.

api.runtime.system

Sistem düzeyi yardımcılar.

typescriptCopy code
[code]
    await api.runtime.system.enqueueSystemEvent(event);api.runtime.system.requestHeartbeat({  source: "other",  intent: "event",  reason: "plugin-event",});api.runtime.system.requestHeartbeatNow({ reason: "plugin-event" }); // Deprecated compatibility alias.const output = await api.runtime.system.runCommandWithTimeout(cmd, args, opts);const hint = api.runtime.system.formatNativeDependencyHint(pkg);
[/code]

api.runtime.events

Olay abonelikleri.

typescriptCopy code
[code]
    api.runtime.events.onAgentEvent((event) => {  /* ... */});api.runtime.events.onSessionTranscriptUpdate((update) => {  /* ... */});
[/code]

api.runtime.logging

Günlükleme.

typescriptCopy code
[code]
    const verbose = api.runtime.logging.shouldLogVerbose();const childLogger = api.runtime.logging.getChildLogger({ plugin: "my-plugin" }, { level: "debug" });
[/code]

api.runtime.modelAuth

Model ve sağlayıcı kimlik doğrulama çözümlemesi.

typescriptCopy code
[code]
    const auth = await api.runtime.modelAuth.getApiKeyForModel({ model, cfg });const providerAuth = await api.runtime.modelAuth.resolveApiKeyForProvider({  provider: "openai",  cfg,});
[/code]

api.runtime.state

Durum dizini çözümlemesi ve SQLite destekli anahtarlı depolama.

typescriptCopy code
[code]
    const stateDir = api.runtime.state.resolveStateDir(process.env);const store = api.runtime.state.openKeyedStore&lt;MyRecord&gt;({  namespace: "my-feature",  maxEntries: 200,  defaultTtlMs: 15 * 60_000,}); await store.register("key-1", { value: "hello" });const claimed = await store.registerIfAbsent("dedupe-key", { value: "first" });const value = await store.lookup("key-1");await store.consume("key-1");await store.clear();
[/code]

Anahtarlı depolar yeniden başlatmalardan sonra korunur ve runtime’a bağlı Plugin kimliğine göre yalıtılır. Atomik tekilleştirme talepleri için `registerIfAbsent(...)` kullanın: anahtar eksikse veya süresi dolmuşsa ve kaydedildiyse `true`, canlı bir değer zaten varsa ve değeri, oluşturulma zamanı veya TTL’si üzerine yazılmadan korunuyorsa `false` döndürür. Sınırlar: ad alanı başına `maxEntries`, Plugin başına 1.000 canlı satır, 64 KB altındaki JSON değerleri ve isteğe bağlı TTL sona ermesi.

api.runtime.tools

Bellek aracı fabrikaları ve CLI.

typescriptCopy code
[code]
    const getTool = api.runtime.tools.createMemoryGetTool(/* ... */);const searchTool = api.runtime.tools.createMemorySearchTool(/* ... */);api.runtime.tools.registerMemoryCli(/* ... */);
[/code]

api.runtime.channel

Kanala özgü runtime yardımcıları (bir kanal Plugin’i yüklendiğinde kullanılabilir).

`api.runtime.channel.mentions`, runtime enjeksiyonu kullanan paketli kanal plugins için paylaşılan gelen bahsetme ilkesi yüzeyidir:

typescriptCopy code
[code]
    const mentionMatch = api.runtime.channel.mentions.matchesMentionWithExplicit(text, {  mentionRegexes,  mentionPatterns,}); const decision = api.runtime.channel.mentions.resolveInboundMentionDecision({  facts: {    canDetectMention: true,    wasMentioned: mentionMatch.matched,    implicitMentionKinds: api.runtime.channel.mentions.implicitMentionKindWhen(      "reply_to_bot",      isReplyToBot,    ),  },  policy: {    isGroup,    requireMention,    allowTextCommands,    hasControlCommand,    commandAuthorized,  },});
[/code]

Kullanılabilir bahsetme yardımcıları:

  * `buildMentionRegexes`
  * `matchesMentionPatterns`
  * `matchesMentionWithExplicit`
  * `implicitMentionKindWhen`
  * `resolveInboundMentionDecision`


`api.runtime.channel.mentions`, eski `resolveMentionGating*` uyumluluk yardımcılarını bilerek açığa çıkarmaz. Normalleştirilmiş `{ facts, policy }` yolunu tercih edin.

## Runtime referanslarını saklama

`register` geri çağrısı dışında kullanmak üzere runtime referansını saklamak için `createPluginRuntimeStore` kullanın:

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

## Diğer üst düzey `api` alanları

`api.runtime` dışında, API nesnesi şunları da sağlar:

Plugin kimliği.

Plugin görünen adı.

Geçerli yapılandırma anlık görüntüsü (varsa bellekte etkin çalışma zamanı anlık görüntüsü).

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaS5wbHVnaW5Db25maWciIHR5cGU9IlJlY29yZDxzdHJpbmcsIHVua25vd24 "> `plugins.entries.<id>.config` içinden Plugin’e özgü yapılandırma.

Kapsamlı günlükleyici (`debug`, `info`, `warn`, `error`).

Geçerli yükleme modu; `"setup-runtime"` hafif, tam giriş öncesi başlangıç/kurulum penceresidir.

## İlgili

  * [Plugin iç yapısı](</tr/plugins/architecture>) — yetenek modeli ve kayıt defteri
  * [SDK giriş noktaları](</tr/plugins/sdk-entrypoints>) — `definePluginEntry` seçenekleri
  * [SDK genel bakışı](</tr/plugins/sdk-overview>) — alt yol başvurusu


Was this useful?YesNo