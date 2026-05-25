---
title: สถาปัตยกรรมการผสานรวม Pi
source_url: https://docs.openclaw.ai/th/pi
scraped_at: 2026-05-25
---

OpenClaw ผสานการทำงานกับ [pi-coding-agent](<https://github.com/badlogic/pi-mono/tree/main/packages/coding-agent>) และแพ็กเกจพี่น้อง (`pi-ai`, `pi-agent-core`, `pi-tui`) เพื่อขับเคลื่อนความสามารถของเอเจนต์ AI

## ภาพรวม

OpenClaw ใช้ pi SDK เพื่อฝังเอเจนต์เขียนโค้ด AI เข้าในสถาปัตยกรรม messaging Gateway แทนที่จะเริ่ม pi เป็น subprocess หรือใช้โหมด RPC, OpenClaw นำเข้าโดยตรงและสร้างอินสแตนซ์ `AgentSession` ของ pi ผ่าน `createAgentSession()` แนวทางแบบฝังนี้ให้:

  * การควบคุมวงจรชีวิตของเซสชันและการจัดการเหตุการณ์อย่างเต็มรูปแบบ
  * การฉีดเครื่องมือแบบกำหนดเอง (การรับส่งข้อความ, sandbox, การกระทำเฉพาะช่องทาง)
  * การปรับแต่ง system prompt ตามช่องทาง/บริบท
  * การคงอยู่ของเซสชันพร้อมรองรับ branching/Compaction
  * การหมุนเวียนโปรไฟล์ auth หลายบัญชีพร้อม failover
  * การสลับโมเดลแบบไม่ผูกกับ provider


## การพึ่งพาแพ็กเกจ

jsonCopy code
[code]
    {  "@earendil-works/pi-agent-core": "0.74.0",  "@earendil-works/pi-ai": "0.74.0",  "@earendil-works/pi-coding-agent": "0.74.0",  "@earendil-works/pi-tui": "0.74.0"}
[/code]

แพ็กเกจ | วัตถุประสงค์  
---|---  
`pi-ai` | นามธรรมหลักของ LLM: `Model`, `streamSimple`, ประเภทข้อความ, API ของ provider  
`pi-agent-core` | agent loop, การเรียกใช้เครื่องมือ, ประเภท `AgentMessage`  
`pi-coding-agent` | SDK ระดับสูง: `createAgentSession`, `SessionManager`, `AuthStorage`, `ModelRegistry`, เครื่องมือในตัว  
`pi-tui` | คอมโพเนนต์ UI เทอร์มินัล (ใช้ในโหมด TUI ภายในเครื่องของ OpenClaw)  
  
## โครงสร้างไฟล์

CodeCopy code
[code]
    src/agents/├── pi-embedded-runner.ts          # Re-exports from pi-embedded-runner/├── pi-embedded-runner/│   ├── run.ts                     # Main entry: runEmbeddedPiAgent()│   ├── run/│   │   ├── attempt.ts             # Single attempt logic with session setup│   │   ├── params.ts              # RunEmbeddedPiAgentParams type│   │   ├── payloads.ts            # Build response payloads from run results│   │   ├── images.ts              # Vision model image injection│   │   └── types.ts               # EmbeddedRunAttemptResult│   ├── abort.ts                   # Abort error detection│   ├── cache-ttl.ts               # Cache TTL tracking for context pruning│   ├── compact.ts                 # Manual/auto compaction logic│   ├── extensions.ts              # Load pi extensions for embedded runs│   ├── extra-params.ts            # Provider-specific stream params│   ├── google.ts                  # Google/Gemini turn ordering fixes│   ├── history.ts                 # History limiting (DM vs group)│   ├── lanes.ts                   # Session/global command lanes│   ├── logger.ts                  # Subsystem logger│   ├── model.ts                   # Model resolution via ModelRegistry│   ├── runs.ts                    # Active run tracking, abort, queue│   ├── sandbox-info.ts            # Sandbox info for system prompt│   ├── session-manager-cache.ts   # SessionManager instance caching│   ├── session-manager-init.ts    # Session file initialization│   ├── system-prompt.ts           # System prompt builder│   ├── tool-split.ts              # Split tools into builtIn vs custom│   ├── types.ts                   # EmbeddedPiAgentMeta, EmbeddedPiRunResult│   └── utils.ts                   # ThinkLevel mapping, error description├── pi-embedded-subscribe.ts       # Session event subscription/dispatch├── pi-embedded-subscribe.types.ts # SubscribeEmbeddedPiSessionParams├── pi-embedded-subscribe.handlers.ts # Event handler factory├── pi-embedded-subscribe.handlers.lifecycle.ts├── pi-embedded-subscribe.handlers.types.ts├── pi-embedded-block-chunker.ts   # Streaming block reply chunking├── pi-embedded-messaging.ts       # Messaging tool sent tracking├── pi-embedded-helpers.ts         # Error classification, turn validation├── pi-embedded-helpers/           # Helper modules├── pi-embedded-utils.ts           # Formatting utilities├── pi-tools.ts                    # createOpenClawCodingTools()├── pi-tools.abort.ts              # AbortSignal wrapping for tools├── pi-tools.policy.ts             # Tool allowlist/denylist policy├── pi-tools.read.ts               # Read tool customizations├── pi-tools.schema.ts             # Tool schema normalization├── pi-tools.types.ts              # AnyAgentTool type alias├── pi-tool-definition-adapter.ts  # AgentTool -> ToolDefinition adapter├── pi-settings.ts                 # Settings overrides├── pi-hooks/                      # Custom pi hooks│   ├── compaction-safeguard.ts    # Safeguard extension│   ├── compaction-safeguard-runtime.ts│   ├── context-pruning.ts         # Cache-TTL context pruning extension│   └── context-pruning/├── model-auth.ts                  # Auth profile resolution├── auth-profiles.ts               # Profile store, cooldown, failover├── model-selection.ts             # Default model resolution├── models-config.ts               # models.json generation├── model-catalog.ts               # Model catalog cache├── context-window-guard.ts        # Context window validation├── failover-error.ts              # FailoverError class├── defaults.ts                    # DEFAULT_PROVIDER, DEFAULT_MODEL├── system-prompt.ts               # buildAgentSystemPrompt()├── system-prompt-params.ts        # System prompt parameter resolution├── system-prompt-report.ts        # Debug report generation├── tool-summaries.ts              # Tool description summaries├── tool-policy.ts                 # Tool policy resolution├── transcript-policy.ts           # Transcript validation policy├── skills.ts                      # Skill snapshot/prompt building├── skills/                        # Skill subsystem├── sandbox.ts                     # Sandbox context resolution├── sandbox/                       # Sandbox subsystem├── channel-tools.ts               # Channel-specific tool injection├── openclaw-tools.ts              # OpenClaw-specific tools├── bash-tools.ts                  # exec/process tools├── apply-patch.ts                 # apply_patch tool (OpenAI)├── tools/                         # Individual tool implementations│   ├── browser-tool.ts│   ├── canvas-tool.ts│   ├── cron-tool.ts│   ├── gateway-tool.ts│   ├── image-tool.ts│   ├── message-tool.ts│   ├── nodes-tool.ts│   ├── session*.ts│   ├── web-*.ts│   └── ...└── ...
[/code]

ขณะนี้ runtime ของการกระทำกับข้อความเฉพาะช่องทางอยู่ในไดเรกทอรีส่วนขยายที่ Plugin เป็นเจ้าของ แทนที่จะอยู่ใต้ `src/agents/tools` เช่น:

  * ไฟล์ runtime ของการกระทำใน Plugin ของ Discord
  * ไฟล์ runtime ของการกระทำใน Plugin ของ Slack
  * ไฟล์ runtime ของการกระทำใน Plugin ของ Telegram
  * ไฟล์ runtime ของการกระทำใน Plugin ของ WhatsApp


## โฟลว์การผสานหลัก

### 1\. การเรียกใช้เอเจนต์แบบฝัง

จุดเข้าใช้งานหลักคือ `runEmbeddedPiAgent()` ใน `pi-embedded-runner/run.ts`:

typescriptCopy code
[code]
     const result = await runEmbeddedPiAgent({  sessionId: "user-123",  sessionKey: "main:whatsapp:+1234567890",  sessionFile: "/path/to/session.jsonl",  workspaceDir: "/path/to/workspace",  config: openclawConfig,  prompt: "Hello, how are you?",  provider: "anthropic",  model: "claude-sonnet-4-6",  timeoutMs: 120_000,  runId: "run-abc",  onBlockReply: async (payload) => {    await sendToChannel(payload.text, payload.mediaUrls);  },});
[/code]

### 2\. การสร้างเซสชัน

ภายใน `runEmbeddedAttempt()` (ที่ถูกเรียกโดย `runEmbeddedPiAgent()`), มีการใช้ pi SDK:

typescriptCopy code
[code]
       createAgentSession,  DefaultResourceLoader,  SessionManager,  SettingsManager,} from "@earendil-works/pi-coding-agent"; const resourceLoader = new DefaultResourceLoader({  cwd: resolvedWorkspace,  agentDir,  settingsManager,  additionalExtensionPaths,});await resourceLoader.reload(); const { session } = await createAgentSession({  cwd: resolvedWorkspace,  agentDir,  authStorage: params.authStorage,  modelRegistry: params.modelRegistry,  model: params.model,  thinkingLevel: mapThinkingLevel(params.thinkLevel),  tools: builtInTools,  customTools: allCustomTools,  sessionManager,  settingsManager,  resourceLoader,}); applySystemPromptOverrideToSession(session, systemPromptOverride);
[/code]

### 3\. การสมัครรับเหตุการณ์

`subscribeEmbeddedPiSession()` สมัครรับเหตุการณ์ของ `AgentSession` ของ pi:

typescriptCopy code
[code]
    const subscription = subscribeEmbeddedPiSession({  session: activeSession,  runId: params.runId,  verboseLevel: params.verboseLevel,  reasoningMode: params.reasoningLevel,  toolResultFormat: params.toolResultFormat,  onToolResult: params.onToolResult,  onReasoningStream: params.onReasoningStream,  onBlockReply: params.onBlockReply,  onPartialReply: params.onPartialReply,  onAgentEvent: params.onAgentEvent,});
[/code]

เหตุการณ์ที่จัดการประกอบด้วย:

  * `message_start` / `message_end` / `message_update` (ข้อความ/การคิดแบบสตรีม)
  * `tool_execution_start` / `tool_execution_update` / `tool_execution_end`
  * `turn_start` / `turn_end`
  * `agent_start` / `agent_end`
  * `compaction_start` / `compaction_end`


### 4\. การส่งพรอมป์

หลังจากตั้งค่าแล้ว จะมีการส่งพรอมป์ให้เซสชัน:

typescriptCopy code
[code]
    await session.prompt(effectivePrompt, { images: imageResult.images });
[/code]

SDK จัดการ agent loop เต็มรูปแบบ: ส่งไปยัง LLM, เรียกใช้ tool calls, สตรีมคำตอบ

การฉีดรูปภาพเป็นแบบเฉพาะพรอมป์: OpenClaw โหลด image refs จากพรอมป์ปัจจุบันและ ส่งผ่าน `images` สำหรับรอบนั้นเท่านั้น โดยจะไม่สแกนรอบประวัติเก่าอีกครั้ง เพื่อฉีด payload รูปภาพซ้ำ

## สถาปัตยกรรมเครื่องมือ

### ไปป์ไลน์เครื่องมือ

  1. **เครื่องมือฐาน** : `codingTools` ของ pi (read, bash, edit, write)
  2. **การแทนที่แบบกำหนดเอง** : OpenClaw แทนที่ bash ด้วย `exec`/`process`, ปรับแต่ง read/edit/write สำหรับ sandbox
  3. **เครื่องมือ OpenClaw** : การรับส่งข้อความ, browser, canvas, sessions, Cron, Gateway และอื่นๆ
  4. **เครื่องมือช่องทาง** : เครื่องมือการกระทำเฉพาะ Discord/Telegram/Slack/WhatsApp
  5. **การกรองตามนโยบาย** : เครื่องมือถูกกรองตามโปรไฟล์, provider, agent, กลุ่ม, นโยบาย sandbox
  6. **การทำให้สคีมาเป็นมาตรฐาน** : สคีมาถูกทำความสะอาดสำหรับความเฉพาะของ Gemini/OpenAI
  7. **การห่อ AbortSignal** : เครื่องมือถูกห่อเพื่อเคารพ abort signals


### อะแดปเตอร์นิยามเครื่องมือ

`AgentTool` ของ pi-agent-core มี signature ของ `execute` ที่ต่างจาก `ToolDefinition` ของ pi-coding-agent อะแดปเตอร์ใน `pi-tool-definition-adapter.ts` เชื่อมส่วนนี้:

typescriptCopy code
[code]
    export function toToolDefinitions(tools: AnyAgentTool[]): ToolDefinition[] {  return tools.map((tool) => ({    name: tool.name,    label: tool.label ?? name,    description: tool.description ?? "",    parameters: tool.parameters,    execute: async (toolCallId, params, onUpdate, _ctx, signal) => {      // pi-coding-agent signature differs from pi-agent-core      return await tool.execute(toolCallId, params, signal, onUpdate);    },  }));}
[/code]

### กลยุทธ์การแยกเครื่องมือ

`splitSdkTools()` ส่งเครื่องมือทั้งหมดผ่าน `customTools`:

typescriptCopy code
[code]
    export function splitSdkTools(options: { tools: AnyAgentTool[]; sandboxEnabled: boolean }) {  return {    builtInTools: [], // Empty. We override everything    customTools: toToolDefinitions(options.tools),  };}
[/code]

สิ่งนี้ทำให้การกรองนโยบาย การผสานกับแซนด์บ็อกซ์ และชุดเครื่องมือเพิ่มเติมของ OpenClaw ยังคงสอดคล้องกันข้ามผู้ให้บริการ

## การสร้างพรอมป์ระบบ

พรอมป์ระบบถูกสร้างใน `buildAgentSystemPrompt()` (`system-prompt.ts`) โดยประกอบพรอมป์แบบเต็มพร้อมส่วนต่าง ๆ ได้แก่ Tooling, Tool Call Style, Safety guardrails, OpenClaw Control, Skills, Docs, Workspace, Sandbox, Messaging, Assistant Output Directives, Voice, Silent Replies, Heartbeats, Runtime metadata รวมถึง Memory และ Reactions เมื่อเปิดใช้งาน และไฟล์บริบททางเลือกกับเนื้อหาพรอมป์ระบบเพิ่มเติม ส่วนต่าง ๆ จะถูกตัดให้สั้นลงสำหรับโหมดพรอมป์ขั้นต่ำที่ใช้โดยเอเจนต์ย่อย

พรอมป์ถูกใช้หลังการสร้างเซสชันผ่าน `applySystemPromptOverrideToSession()`:

typescriptCopy code
[code]
    const systemPromptOverride = createSystemPromptOverride(appendPrompt);applySystemPromptOverrideToSession(session, systemPromptOverride);
[/code]

## การจัดการเซสชัน

### ไฟล์เซสชัน

เซสชันเป็นไฟล์ JSONL ที่มีโครงสร้างแบบต้นไม้ (เชื่อมด้วย id/parentId) `SessionManager` ของ Pi จัดการการคงข้อมูล:

typescriptCopy code
[code]
    const sessionManager = SessionManager.open(params.sessionFile);
[/code]

OpenClaw ห่อสิ่งนี้ด้วย `guardSessionManager()` เพื่อความปลอดภัยของผลลัพธ์เครื่องมือ

### การแคชเซสชัน

`session-manager-cache.ts` แคชอินสแตนซ์ SessionManager เพื่อหลีกเลี่ยงการแยกวิเคราะห์ไฟล์ซ้ำ:

typescriptCopy code
[code]
    await prewarmSessionFile(params.sessionFile);sessionManager = SessionManager.open(params.sessionFile);trackSessionManagerAccess(params.sessionFile);
[/code]

### การจำกัดประวัติ

`limitHistoryTurns()` ตัดทอนประวัติการสนทนาตามชนิดช่องทาง (DM เทียบกับกลุ่ม)

### Compaction

Compaction อัตโนมัติจะทำงานเมื่อบริบทล้น ลายเซ็นการล้นที่พบบ่อย รวมถึง `request_too_large`, `context length exceeded`, `input exceeds the maximum number of tokens`, `input token count exceeds the maximum number of input tokens`, `input is too long for the model` และ `ollama error: context length exceeded` `compactEmbeddedPiSessionDirect()` จัดการ Compaction ด้วยตนเอง:

typescriptCopy code
[code]
    const compactResult = await compactEmbeddedPiSessionDirect({  sessionId, sessionFile, provider, model, ...});
[/code]

## การยืนยันตัวตนและการระบุโมเดล

### โปรไฟล์การยืนยันตัวตน

OpenClaw ดูแลที่เก็บโปรไฟล์การยืนยันตัวตนที่มีคีย์ API หลายรายการต่อผู้ให้บริการ:

typescriptCopy code
[code]
    const authStore = ensureAuthProfileStore(agentDir, { allowKeychainPrompt: false });const profileOrder = resolveAuthProfileOrder({ cfg, store: authStore, provider, preferredProfile });
[/code]

โปรไฟล์จะหมุนเวียนเมื่อเกิดความล้มเหลวพร้อมการติดตามช่วงพัก:

typescriptCopy code
[code]
    await markAuthProfileFailure({ store, profileId, reason, cfg, agentDir });const rotated = await advanceAuthProfile();
[/code]

### การระบุโมเดล

typescriptCopy code
[code]
     const { model, error, authStorage, modelRegistry } = resolveModel(  provider,  modelId,  agentDir,  config,); // Uses pi's ModelRegistry and AuthStorageauthStorage.setRuntimeApiKey(model.provider, apiKeyInfo.apiKey);
[/code]

### การสลับสำรองเมื่อผิดพลาด

`FailoverError` ทริกเกอร์การ fallback ของโมเดลเมื่อกำหนดค่าไว้:

typescriptCopy code
[code]
    if (fallbackConfigured && isFailoverErrorMessage(errorText)) {  throw new FailoverError(errorText, {    reason: promptFailoverReason ?? "unknown",    provider,    model: modelId,    profileId,    status: resolveFailoverStatus(promptFailoverReason),  });}
[/code]

## ส่วนขยายของ Pi

OpenClaw โหลดส่วนขยาย pi แบบกำหนดเองสำหรับพฤติกรรมเฉพาะทาง:

### มาตรการป้องกัน Compaction

`src/agents/pi-hooks/compaction-safeguard.ts` เพิ่ม guardrails ให้กับ Compaction รวมถึงการจัดงบประมาณโทเค็นแบบปรับตัวได้ พร้อมสรุปความล้มเหลวของเครื่องมือและการดำเนินการกับไฟล์:

typescriptCopy code
[code]
    if (resolveCompactionMode(params.cfg) === "safeguard") {  setCompactionSafeguardRuntime(params.sessionManager, { maxHistoryShare });  paths.push(resolvePiExtensionPath("compaction-safeguard"));}
[/code]

### การตัดแต่งบริบท

`src/agents/pi-hooks/context-pruning.ts` ใช้การตัดแต่งบริบทตาม cache-TTL:

typescriptCopy code
[code]
    if (cfg?.agents?.defaults?.contextPruning?.mode === "cache-ttl") {  setContextPruningRuntime(params.sessionManager, {    settings,    contextWindowTokens,    isToolPrunable,    lastCacheTouchAt,  });  paths.push(resolvePiExtensionPath("context-pruning"));}
[/code]

## การสตรีมและการตอบกลับแบบบล็อก

### การแบ่งก้อนบล็อก

`EmbeddedBlockChunker` จัดการข้อความสตรีมให้เป็นบล็อกคำตอบแยกส่วน:

typescriptCopy code
[code]
    const blockChunker = blockChunking ? new EmbeddedBlockChunker(blockChunking) : null;
[/code]

### การลบแท็ก Thinking/Final

เอาต์พุตสตรีมมิงถูกประมวลผลเพื่อลบ `<think>`/`<thinking>` block และดึงเนื้อหา `<final>`:

typescriptCopy code
[code]
    const stripBlockTags = (text: string, state: { thinking: boolean; final: boolean }) => {  // Strip <think>...</think> content  // If enforceFinalTag, only return <final>...</final> content};
[/code]

### คำสั่งกำกับการตอบกลับ

คำสั่งกำกับการตอบกลับ เช่น `[[media:url]]`, `[[voice]]`, `[[reply:id]]` ถูกแยกวิเคราะห์และดึงออกมา:

typescriptCopy code
[code]
    const { text: cleanedText, mediaUrls, audioAsVoice, replyToId } = consumeReplyDirectives(chunk);
[/code]

## การจัดการข้อผิดพลาด

### การจัดประเภทข้อผิดพลาด

`pi-embedded-helpers.ts` จัดประเภทข้อผิดพลาดเพื่อการจัดการที่เหมาะสม:

typescriptCopy code
[code]
    isContextOverflowError(errorText)     // Context too largeisCompactionFailureError(errorText)   // Compaction failedisAuthAssistantError(lastAssistant)   // Auth failureisRateLimitAssistantError(...)        // Rate limitedisFailoverAssistantError(...)         // Should failoverclassifyFailoverReason(errorText)     // "auth" | "rate_limit" | "quota" | "timeout" | ...
[/code]

### การ fallback ของระดับ thinking

หากระดับ thinking ไม่รองรับ ระบบจะ fallback:

typescriptCopy code
[code]
    const fallbackThinking = pickFallbackThinkingLevel({  message: errorText,  attempted: attemptedThinking,});if (fallbackThinking) {  thinkLevel = fallbackThinking;  continue;}
[/code]

## การผสานกับแซนด์บ็อกซ์

เมื่อเปิดใช้งานโหมดแซนด์บ็อกซ์ เครื่องมือและพาธจะถูกจำกัด:

typescriptCopy code
[code]
    const sandbox = await resolveSandboxContext({  config: params.config,  sessionKey: sandboxSessionKey,  workspaceDir: resolvedWorkspace,}); if (sandboxRoot) {  // Use sandboxed read/edit/write tools  // Exec runs in container  // Browser uses bridge URL}
[/code]

## การจัดการเฉพาะผู้ให้บริการ

### Anthropic

  * การล้างสตริงพิเศษของการปฏิเสธ
  * การตรวจสอบเทิร์นสำหรับบทบาทที่ต่อเนื่องกัน
  * การตรวจสอบพารามิเตอร์เครื่องมือของ Pi ต้นทางอย่างเข้มงวด


### Google/Gemini

  * การทำความสะอาดสคีมาเครื่องมือที่ Plugin เป็นเจ้าของ


### OpenAI

  * เครื่องมือ `apply_patch` สำหรับโมเดล Codex
  * การจัดการการลดระดับ thinking


## การผสานกับ TUI

OpenClaw ยังมีโหมด TUI ในเครื่องที่ใช้คอมโพเนนต์ pi-tui โดยตรง:

typescriptCopy code
[code]
    // src/tui/tui.ts 
[/code]

สิ่งนี้มอบประสบการณ์เทอร์มินัลแบบโต้ตอบที่คล้ายกับโหมดเนทีฟของ pi

## ความแตกต่างหลักจาก Pi CLI

ด้าน | Pi CLI | OpenClaw แบบฝัง  
---|---|---  
การเรียกใช้ | คำสั่ง `pi` / RPC | SDK ผ่าน `createAgentSession()`  
เครื่องมือ | เครื่องมือเขียนโค้ดเริ่มต้น | ชุดเครื่องมือ OpenClaw แบบกำหนดเอง  
พรอมป์ระบบ | [AGENTS.md](<http://AGENTS.md>) \+ พรอมป์ | ไดนามิกต่อช่องทาง/บริบท  
ที่เก็บเซสชัน | `~/.pi/agent/sessions/` | `~/.openclaw/agents/<agentId>/sessions/` (หรือ `$OPENCLAW_STATE_DIR/agents/<agentId>/sessions/`)  
การยืนยันตัวตน | ข้อมูลรับรองเดียว | หลายโปรไฟล์พร้อมการหมุนเวียน  
ส่วนขยาย | โหลดจากดิสก์ | เชิงโปรแกรม + พาธดิสก์  
การจัดการเหตุการณ์ | การเรนเดอร์ TUI | อิงคอลแบ็ก (onBlockReply ฯลฯ)  
  
## ข้อควรพิจารณาในอนาคต

พื้นที่ที่อาจปรับปรุงใหม่:

  1. **การจัดแนวลายเซ็นเครื่องมือ** : ปัจจุบันปรับแปลงระหว่างลายเซ็นของ pi-agent-core และ pi-coding-agent
  2. **การห่อ session manager** : `guardSessionManager` เพิ่มความปลอดภัย แต่เพิ่มความซับซ้อน
  3. **การโหลดส่วนขยาย** : อาจใช้ `ResourceLoader` ของ pi โดยตรงมากขึ้น
  4. **ความซับซ้อนของตัวจัดการสตรีมมิง** : `subscribeEmbeddedPiSession` มีขนาดใหญ่ขึ้นมาก
  5. **ลักษณะเฉพาะของผู้ให้บริการ** : มี codepath เฉพาะผู้ให้บริการจำนวนมากที่ pi อาจจัดการได้


## การทดสอบ

ความครอบคลุมของการผสานกับ Pi ครอบคลุมชุดทดสอบเหล่านี้:

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


แบบ live/เลือกเปิดใช้:

  * `src/agents/pi-embedded-runner-extraparams.live.test.ts` (เปิดใช้งาน `OPENCLAW_LIVE_TEST=1`)


สำหรับคำสั่งรันปัจจุบัน โปรดดู [เวิร์กโฟลว์การพัฒนา Pi](</th/pi-dev>)

## ที่เกี่ยวข้อง

  * [เวิร์กโฟลว์การพัฒนา Pi](</th/pi-dev>)
  * [ภาพรวมการติดตั้ง](</th/install>)


Was this useful?YesNo