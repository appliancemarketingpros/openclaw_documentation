---
title: Pi entegrasyon mimarisi
source_url: https://docs.openclaw.ai/tr/pi
scraped_at: 2026-05-25
---

OpenClaw, yapay zeka ajanı yeteneklerini sağlamak için [pi-coding-agent](<https://github.com/badlogic/pi-mono/tree/main/packages/coding-agent>) ve kardeş paketleri (`pi-ai`, `pi-agent-core`, `pi-tui`) ile entegre olur.

## Genel Bakış

OpenClaw, mesajlaşma Gateway mimarisine bir yapay zeka kodlama ajanı yerleştirmek için pi SDK'sını kullanır. pi'yi bir alt süreç olarak başlatmak veya RPC modunu kullanmak yerine OpenClaw, pi'nin `AgentSession` bileşenini `createAgentSession()` aracılığıyla doğrudan içe aktarır ve örnekler. Bu yerleşik yaklaşım şunları sağlar:

  * Oturum yaşam döngüsü ve olay işleme üzerinde tam denetim
  * Özel araç enjeksiyonu (mesajlaşma, korumalı alan, kanala özgü eylemler)
  * Kanal/bağlam başına sistem istemi özelleştirmesi
  * Dallanma/Compaction desteğiyle oturum kalıcılığı
  * Yük devretmeli çok hesaplı kimlik doğrulama profili rotasyonu
  * Sağlayıcıdan bağımsız model değiştirme


## Paket bağımlılıkları

jsonCopy code
[code]
    {  "@earendil-works/pi-agent-core": "0.74.0",  "@earendil-works/pi-ai": "0.74.0",  "@earendil-works/pi-coding-agent": "0.74.0",  "@earendil-works/pi-tui": "0.74.0"}
[/code]

Paket | Amaç  
---|---  
`pi-ai` | Temel LLM soyutlamaları: `Model`, `streamSimple`, mesaj türleri, sağlayıcı API'leri  
`pi-agent-core` | Ajan döngüsü, araç yürütme, `AgentMessage` türleri  
`pi-coding-agent` | Üst düzey SDK: `createAgentSession`, `SessionManager`, `AuthStorage`, `ModelRegistry`, yerleşik araçlar  
`pi-tui` | Terminal UI bileşenleri (OpenClaw'ın yerel TUI modunda kullanılır)  
  
## Dosya yapısı

CodeCopy code
[code]
    src/agents/├── pi-embedded-runner.ts          # Re-exports from pi-embedded-runner/├── pi-embedded-runner/│   ├── run.ts                     # Main entry: runEmbeddedPiAgent()│   ├── run/│   │   ├── attempt.ts             # Single attempt logic with session setup│   │   ├── params.ts              # RunEmbeddedPiAgentParams type│   │   ├── payloads.ts            # Build response payloads from run results│   │   ├── images.ts              # Vision model image injection│   │   └── types.ts               # EmbeddedRunAttemptResult│   ├── abort.ts                   # Abort error detection│   ├── cache-ttl.ts               # Cache TTL tracking for context pruning│   ├── compact.ts                 # Manual/auto compaction logic│   ├── extensions.ts              # Load pi extensions for embedded runs│   ├── extra-params.ts            # Provider-specific stream params│   ├── google.ts                  # Google/Gemini turn ordering fixes│   ├── history.ts                 # History limiting (DM vs group)│   ├── lanes.ts                   # Session/global command lanes│   ├── logger.ts                  # Subsystem logger│   ├── model.ts                   # Model resolution via ModelRegistry│   ├── runs.ts                    # Active run tracking, abort, queue│   ├── sandbox-info.ts            # Sandbox info for system prompt│   ├── session-manager-cache.ts   # SessionManager instance caching│   ├── session-manager-init.ts    # Session file initialization│   ├── system-prompt.ts           # System prompt builder│   ├── tool-split.ts              # Split tools into builtIn vs custom│   ├── types.ts                   # EmbeddedPiAgentMeta, EmbeddedPiRunResult│   └── utils.ts                   # ThinkLevel mapping, error description├── pi-embedded-subscribe.ts       # Session event subscription/dispatch├── pi-embedded-subscribe.types.ts # SubscribeEmbeddedPiSessionParams├── pi-embedded-subscribe.handlers.ts # Event handler factory├── pi-embedded-subscribe.handlers.lifecycle.ts├── pi-embedded-subscribe.handlers.types.ts├── pi-embedded-block-chunker.ts   # Streaming block reply chunking├── pi-embedded-messaging.ts       # Messaging tool sent tracking├── pi-embedded-helpers.ts         # Error classification, turn validation├── pi-embedded-helpers/           # Helper modules├── pi-embedded-utils.ts           # Formatting utilities├── pi-tools.ts                    # createOpenClawCodingTools()├── pi-tools.abort.ts              # AbortSignal wrapping for tools├── pi-tools.policy.ts             # Tool allowlist/denylist policy├── pi-tools.read.ts               # Read tool customizations├── pi-tools.schema.ts             # Tool schema normalization├── pi-tools.types.ts              # AnyAgentTool type alias├── pi-tool-definition-adapter.ts  # AgentTool -> ToolDefinition adapter├── pi-settings.ts                 # Settings overrides├── pi-hooks/                      # Custom pi hooks│   ├── compaction-safeguard.ts    # Safeguard extension│   ├── compaction-safeguard-runtime.ts│   ├── context-pruning.ts         # Cache-TTL context pruning extension│   └── context-pruning/├── model-auth.ts                  # Auth profile resolution├── auth-profiles.ts               # Profile store, cooldown, failover├── model-selection.ts             # Default model resolution├── models-config.ts               # models.json generation├── model-catalog.ts               # Model catalog cache├── context-window-guard.ts        # Context window validation├── failover-error.ts              # FailoverError class├── defaults.ts                    # DEFAULT_PROVIDER, DEFAULT_MODEL├── system-prompt.ts               # buildAgentSystemPrompt()├── system-prompt-params.ts        # System prompt parameter resolution├── system-prompt-report.ts        # Debug report generation├── tool-summaries.ts              # Tool description summaries├── tool-policy.ts                 # Tool policy resolution├── transcript-policy.ts           # Transcript validation policy├── skills.ts                      # Skill snapshot/prompt building├── skills/                        # Skill subsystem├── sandbox.ts                     # Sandbox context resolution├── sandbox/                       # Sandbox subsystem├── channel-tools.ts               # Channel-specific tool injection├── openclaw-tools.ts              # OpenClaw-specific tools├── bash-tools.ts                  # exec/process tools├── apply-patch.ts                 # apply_patch tool (OpenAI)├── tools/                         # Individual tool implementations│   ├── browser-tool.ts│   ├── canvas-tool.ts│   ├── cron-tool.ts│   ├── gateway-tool.ts│   ├── image-tool.ts│   ├── message-tool.ts│   ├── nodes-tool.ts│   ├── session*.ts│   ├── web-*.ts│   └── ...└── ...
[/code]

Kanala özgü mesaj eylemi çalışma zamanları artık `src/agents/tools` altında değil, Plugin sahibi uzantı dizinlerinde bulunur; örneğin:

  * Discord Plugin eylemi çalışma zamanı dosyaları
  * Slack Plugin eylemi çalışma zamanı dosyası
  * Telegram Plugin eylemi çalışma zamanı dosyası
  * WhatsApp Plugin eylemi çalışma zamanı dosyası


## Temel entegrasyon akışı

### 1\. Yerleşik Bir Ajanı Çalıştırma

Ana giriş noktası, `pi-embedded-runner/run.ts` içindeki `runEmbeddedPiAgent()` işlevidir:

typescriptCopy code
[code]
     const result = await runEmbeddedPiAgent({  sessionId: "user-123",  sessionKey: "main:whatsapp:+1234567890",  sessionFile: "/path/to/session.jsonl",  workspaceDir: "/path/to/workspace",  config: openclawConfig,  prompt: "Hello, how are you?",  provider: "anthropic",  model: "claude-sonnet-4-6",  timeoutMs: 120_000,  runId: "run-abc",  onBlockReply: async (payload) => {    await sendToChannel(payload.text, payload.mediaUrls);  },});
[/code]

### 2\. Oturum Oluşturma

`runEmbeddedAttempt()` içinde (`runEmbeddedPiAgent()` tarafından çağrılır), pi SDK kullanılır:

typescriptCopy code
[code]
       createAgentSession,  DefaultResourceLoader,  SessionManager,  SettingsManager,} from "@earendil-works/pi-coding-agent"; const resourceLoader = new DefaultResourceLoader({  cwd: resolvedWorkspace,  agentDir,  settingsManager,  additionalExtensionPaths,});await resourceLoader.reload(); const { session } = await createAgentSession({  cwd: resolvedWorkspace,  agentDir,  authStorage: params.authStorage,  modelRegistry: params.modelRegistry,  model: params.model,  thinkingLevel: mapThinkingLevel(params.thinkLevel),  tools: builtInTools,  customTools: allCustomTools,  sessionManager,  settingsManager,  resourceLoader,}); applySystemPromptOverrideToSession(session, systemPromptOverride);
[/code]

### 3\. Olay Aboneliği

`subscribeEmbeddedPiSession()`, pi'nin `AgentSession` olaylarına abone olur:

typescriptCopy code
[code]
    const subscription = subscribeEmbeddedPiSession({  session: activeSession,  runId: params.runId,  verboseLevel: params.verboseLevel,  reasoningMode: params.reasoningLevel,  toolResultFormat: params.toolResultFormat,  onToolResult: params.onToolResult,  onReasoningStream: params.onReasoningStream,  onBlockReply: params.onBlockReply,  onPartialReply: params.onPartialReply,  onAgentEvent: params.onAgentEvent,});
[/code]

İşlenen olaylar şunları içerir:

  * `message_start` / `message_end` / `message_update` (akış metni/düşünme)
  * `tool_execution_start` / `tool_execution_update` / `tool_execution_end`
  * `turn_start` / `turn_end`
  * `agent_start` / `agent_end`
  * `compaction_start` / `compaction_end`


### 4\. İstem Gönderme

Kurulumdan sonra oturuma istem gönderilir:

typescriptCopy code
[code]
    await session.prompt(effectivePrompt, { images: imageResult.images });
[/code]

SDK, tam ajan döngüsünü yönetir: LLM'ye gönderme, araç çağrılarını yürütme, yanıtları akışla iletme.

Görüntü enjeksiyonu isteme yereldir: OpenClaw, geçerli istemden görüntü başvurularını yükler ve bunları yalnızca o tur için `images` aracılığıyla iletir. Görüntü yüklerini yeniden enjekte etmek için eski geçmiş turlarını yeniden taramaz.

## Araç mimarisi

### Araç işlem hattı

  1. **Temel Araçlar** : pi'nin `codingTools` araçları (read, bash, edit, write)
  2. **Özel Değiştirmeler** : OpenClaw, bash'i `exec`/`process` ile değiştirir; read/edit/write araçlarını korumalı alan için özelleştirir
  3. **OpenClaw Araçları** : mesajlaşma, tarayıcı, canvas, oturumlar, Cron, Gateway vb.
  4. **Kanal Araçları** : Discord/Telegram/Slack/WhatsApp'a özgü eylem araçları
  5. **İlke Filtreleme** : Araçlar profil, sağlayıcı, ajan, grup ve korumalı alan ilkelerine göre filtrelenir
  6. **Şema Normalleştirme** : Şemalar Gemini/OpenAI özelliklerine göre temizlenir
  7. **AbortSignal Sarmalama** : Araçlar, iptal sinyallerine uyacak şekilde sarmalanır


### Araç tanımı bağdaştırıcısı

pi-agent-core'un `AgentTool` türü, pi-coding-agent'ın `ToolDefinition` türünden farklı bir `execute` imzasına sahiptir. `pi-tool-definition-adapter.ts` içindeki bağdaştırıcı bunu köprüler:

typescriptCopy code
[code]
    export function toToolDefinitions(tools: AnyAgentTool[]): ToolDefinition[] {  return tools.map((tool) => ({    name: tool.name,    label: tool.label ?? name,    description: tool.description ?? "",    parameters: tool.parameters,    execute: async (toolCallId, params, onUpdate, _ctx, signal) => {      // pi-coding-agent signature differs from pi-agent-core      return await tool.execute(toolCallId, params, signal, onUpdate);    },  }));}
[/code]

### Araç bölme stratejisi

`splitSdkTools()`, tüm araçları `customTools` aracılığıyla iletir:

typescriptCopy code
[code]
    export function splitSdkTools(options: { tools: AnyAgentTool[]; sandboxEnabled: boolean }) {  return {    builtInTools: [], // Empty. We override everything    customTools: toToolDefinitions(options.tools),  };}
[/code]

Bu, OpenClaw'ın ilke filtrelemesinin, sandbox entegrasyonunun ve genişletilmiş araç setinin sağlayıcılar arasında tutarlı kalmasını sağlar.

## Sistem prompt'u oluşturma

Sistem prompt'u `buildAgentSystemPrompt()` içinde oluşturulur (`system-prompt.ts`). Tooling, Tool Call Style, Safety guardrails, OpenClaw Control, Skills, Docs, Workspace, Sandbox, Messaging, Assistant Output Directives, Voice, Silent Replies, Heartbeats, Runtime metadata dahil bölümlerin yanı sıra etkinleştirildiğinde Memory ve Reactions ile isteğe bağlı bağlam dosyaları ve ek sistem prompt'u içeriğini içeren tam bir prompt derler. Bölümler, alt aracılar tarafından kullanılan minimum prompt modu için kırpılır.

Prompt, oturum oluşturulduktan sonra `applySystemPromptOverrideToSession()` aracılığıyla uygulanır:

typescriptCopy code
[code]
    const systemPromptOverride = createSystemPromptOverride(appendPrompt);applySystemPromptOverrideToSession(session, systemPromptOverride);
[/code]

## Oturum yönetimi

### Oturum dosyaları

Oturumlar, ağaç yapısına sahip JSONL dosyalarıdır (id/parentId bağlantısı). Pi'nin `SessionManager`'ı kalıcılığı yönetir:

typescriptCopy code
[code]
    const sessionManager = SessionManager.open(params.sessionFile);
[/code]

OpenClaw bunu araç sonucu güvenliği için `guardSessionManager()` ile sarmalar.

### Oturum önbelleğe alma

`session-manager-cache.ts`, dosyaların tekrar tekrar ayrıştırılmasını önlemek için SessionManager örneklerini önbelleğe alır:

typescriptCopy code
[code]
    await prewarmSessionFile(params.sessionFile);sessionManager = SessionManager.open(params.sessionFile);trackSessionManagerAccess(params.sessionFile);
[/code]

### Geçmişi sınırlama

`limitHistoryTurns()`, konuşma geçmişini kanal türüne göre (DM ve grup) kırpar.

### Compaction

Otomatik Compaction, bağlam taşmasında tetiklenir. Yaygın taşma imzaları `request_too_large`, `context length exceeded`, `input exceeds the maximum number of tokens`, `input token count exceeds the maximum number of input tokens`, `input is too long for the model` ve `ollama error: context length exceeded` içerir. `compactEmbeddedPiSessionDirect()` manuel compaction işlemini yönetir:

typescriptCopy code
[code]
    const compactResult = await compactEmbeddedPiSessionDirect({  sessionId, sessionFile, provider, model, ...});
[/code]

## Kimlik doğrulama ve model çözümleme

### Kimlik doğrulama profilleri

OpenClaw, sağlayıcı başına birden fazla API anahtarı içeren bir kimlik doğrulama profili deposu tutar:

typescriptCopy code
[code]
    const authStore = ensureAuthProfileStore(agentDir, { allowKeychainPrompt: false });const profileOrder = resolveAuthProfileOrder({ cfg, store: authStore, provider, preferredProfile });
[/code]

Profiller, soğuma süresi takibiyle hatalarda döndürülür:

typescriptCopy code
[code]
    await markAuthProfileFailure({ store, profileId, reason, cfg, agentDir });const rotated = await advanceAuthProfile();
[/code]

### Model çözümleme

typescriptCopy code
[code]
     const { model, error, authStorage, modelRegistry } = resolveModel(  provider,  modelId,  agentDir,  config,); // Uses pi's ModelRegistry and AuthStorageauthStorage.setRuntimeApiKey(model.provider, apiKeyInfo.apiKey);
[/code]

### Yedek sağlayıcıya geçiş

`FailoverError`, yapılandırıldığında model yedeğine geçişi tetikler:

typescriptCopy code
[code]
    if (fallbackConfigured && isFailoverErrorMessage(errorText)) {  throw new FailoverError(errorText, {    reason: promptFailoverReason ?? "unknown",    provider,    model: modelId,    profileId,    status: resolveFailoverStatus(promptFailoverReason),  });}
[/code]

## Pi uzantıları

OpenClaw, özelleştirilmiş davranış için özel pi uzantıları yükler:

### Compaction koruması

`src/agents/pi-hooks/compaction-safeguard.ts`, uyarlanabilir token bütçelemesinin yanı sıra araç hatası ve dosya işlemi özetleri dahil olmak üzere Compaction için koruma sınırları ekler:

typescriptCopy code
[code]
    if (resolveCompactionMode(params.cfg) === "safeguard") {  setCompactionSafeguardRuntime(params.sessionManager, { maxHistoryShare });  paths.push(resolvePiExtensionPath("compaction-safeguard"));}
[/code]

### Bağlam budama

`src/agents/pi-hooks/context-pruning.ts`, cache-TTL tabanlı bağlam budamayı uygular:

typescriptCopy code
[code]
    if (cfg?.agents?.defaults?.contextPruning?.mode === "cache-ttl") {  setContextPruningRuntime(params.sessionManager, {    settings,    contextWindowTokens,    isToolPrunable,    lastCacheTouchAt,  });  paths.push(resolvePiExtensionPath("context-pruning"));}
[/code]

## Akış ve blok yanıtları

### Blok parçalama

`EmbeddedBlockChunker`, akış metnini ayrı yanıt bloklarına yönetir:

typescriptCopy code
[code]
    const blockChunker = blockChunking ? new EmbeddedBlockChunker(blockChunking) : null;
[/code]

### Thinking/Final Etiketlerini Ayıklama

Akış çıktısı, `<think>`/`<thinking>` bloklarını ayıklamak ve `<final>` içeriğini çıkarmak için işlenir:

typescriptCopy code
[code]
    const stripBlockTags = (text: string, state: { thinking: boolean; final: boolean }) => {  // Strip <think>...</think> content  // If enforceFinalTag, only return <final>...</final> content};
[/code]

### Yanıt yönergeleri

`[[media:url]]`, `[[voice]]`, `[[reply:id]]` gibi yanıt yönergeleri ayrıştırılır ve çıkarılır:

typescriptCopy code
[code]
    const { text: cleanedText, mediaUrls, audioAsVoice, replyToId } = consumeReplyDirectives(chunk);
[/code]

## Hata işleme

### Hata sınıflandırması

`pi-embedded-helpers.ts`, uygun işleme için hataları sınıflandırır:

typescriptCopy code
[code]
    isContextOverflowError(errorText)     // Context too largeisCompactionFailureError(errorText)   // Compaction failedisAuthAssistantError(lastAssistant)   // Auth failureisRateLimitAssistantError(...)        // Rate limitedisFailoverAssistantError(...)         // Should failoverclassifyFailoverReason(errorText)     // "auth" | "rate_limit" | "quota" | "timeout" | ...
[/code]

### Thinking düzeyi yedeği

Bir thinking düzeyi desteklenmiyorsa, yedeğe düşer:

typescriptCopy code
[code]
    const fallbackThinking = pickFallbackThinkingLevel({  message: errorText,  attempted: attemptedThinking,});if (fallbackThinking) {  thinkLevel = fallbackThinking;  continue;}
[/code]

## Sandbox entegrasyonu

Sandbox modu etkin olduğunda, araçlar ve yollar kısıtlanır:

typescriptCopy code
[code]
    const sandbox = await resolveSandboxContext({  config: params.config,  sessionKey: sandboxSessionKey,  workspaceDir: resolvedWorkspace,}); if (sandboxRoot) {  // Use sandboxed read/edit/write tools  // Exec runs in container  // Browser uses bridge URL}
[/code]

## Sağlayıcıya Özgü İşleme

### Anthropic

  * Reddetme sihirli dizesini temizleme
  * Ardışık roller için tur doğrulaması
  * Katı upstream Pi araç parametresi doğrulaması


### Google/Gemini

  * Plugin'e ait araç şeması temizleme


### OpenAI

  * Codex modelleri için `apply_patch` aracı
  * Thinking düzeyi düşürme işleme


## TUI Entegrasyonu

OpenClaw ayrıca pi-tui bileşenlerini doğrudan kullanan yerel bir TUI moduna sahiptir:

typescriptCopy code
[code]
    // src/tui/tui.ts 
[/code]

Bu, pi'nin yerel moduna benzer etkileşimli terminal deneyimi sağlar.

## Pi CLI'dan temel farklar

Boyut | Pi CLI | OpenClaw Gömülü  
---|---|---  
Çağırma | `pi` komutu / RPC | `createAgentSession()` üzerinden SDK  
Araçlar | Varsayılan kodlama araçları | Özel OpenClaw araç paketi  
Sistem prompt'u | [AGENTS.md](<http://AGENTS.md>) \+ prompt'lar | Kanal/bağlam başına dinamik  
Oturum depolama | `~/.pi/agent/sessions/` | `~/.openclaw/agents/<agentId>/sessions/` (veya `$OPENCLAW_STATE_DIR/agents/<agentId>/sessions/`)  
Kimlik doğrulama | Tek kimlik bilgisi | Döndürmeli çoklu profil  
Uzantılar | Diskten yüklenir | Programatik + disk yolları  
Olay işleme | TUI render etme | Callback tabanlı (onBlockReply vb.)  
  
## Gelecekte değerlendirilecekler

Olası yeniden çalışma alanları:

  1. **Araç imzası hizalaması** : Şu anda pi-agent-core ve pi-coding-agent imzaları arasında uyarlama yapılıyor
  2. **Oturum yöneticisi sarmalama** : `guardSessionManager` güvenlik ekler ancak karmaşıklığı artırır
  3. **Uzantı yükleme** : Pi'nin `ResourceLoader`'ı daha doğrudan kullanılabilir
  4. **Akış işleyicisi karmaşıklığı** : `subscribeEmbeddedPiSession` büyüdü
  5. **Sağlayıcı özel durumları** : Pi'nin potansiyel olarak yönetebileceği birçok sağlayıcıya özgü kod yolu


## Testler

Pi entegrasyon kapsamı şu test paketlerini içerir:

  * `src/agents/pi-*.test.ts`
  * `src/agents/pi-auth-json.test.ts`
  * `src/agents/pi-embedded-*.test.ts`
  * `src/agents/pi-embedded-helpers*.test.ts`
  * `src/agents/pi-embedded-runner*.test.ts`
  * `src/agents/pi-embedded-runner/**/*.test.ts`
  * `src/agents/pi-embedded-subscribe*.test.ts`
  * `src/agents/pi-tools*.test.ts`
  * `src/agents/pi-tool-definition-adapter*.test.ts`
  * `src/agents/pi-settings.test.ts`
  * `src/agents/pi-hooks/**/*.test.ts`


Canlı/isteğe bağlı:

  * `src/agents/pi-embedded-runner-extraparams.live.test.ts` (`OPENCLAW_LIVE_TEST=1` ile etkinleştirin)


Geçerli çalıştırma komutları için [Pi Geliştirme İş Akışı](</tr/pi-dev>) bölümüne bakın.

## İlgili

  * [Pi geliştirme iş akışı](</tr/pi-dev>)
  * [Kurulum genel bakışı](</tr/install>)


Was this useful?YesNo