---
title: Pi-Integrationsarchitektur
source_url: https://docs.openclaw.ai/de/pi
scraped_at: 2026-05-25
---

OpenClaw integriert sich mit [pi-coding-agent](<https://github.com/badlogic/pi-mono/tree/main/packages/coding-agent>) und den zugehörigen Paketen (`pi-ai`, `pi-agent-core`, `pi-tui`), um seine KI-Agent-Funktionen bereitzustellen.

## Überblick

OpenClaw verwendet das pi SDK, um einen KI-Coding-Agent in seine Messaging-Gateway-Architektur einzubetten. Anstatt pi als Unterprozess zu starten oder den RPC-Modus zu verwenden, importiert und instanziiert OpenClaw pi's `AgentSession` direkt über `createAgentSession()`. Dieser eingebettete Ansatz bietet:

  * Vollständige Kontrolle über Sitzungslebenszyklus und Event-Behandlung
  * Benutzerdefinierte Tool-Injektion (Messaging, Sandbox, kanalspezifische Aktionen)
  * Anpassung des System-Prompts pro Kanal/Kontext
  * Sitzungspersistenz mit Unterstützung für Branching/Compaction
  * Rotation von Multi-Account-Auth-Profilen mit Failover
  * Provider-agnostisches Modellwechseln


## Paketabhängigkeiten

jsonCopy code
[code]
    {  "@earendil-works/pi-agent-core": "0.74.0",  "@earendil-works/pi-ai": "0.74.0",  "@earendil-works/pi-coding-agent": "0.74.0",  "@earendil-works/pi-tui": "0.74.0"}
[/code]

Paket | Zweck  
---|---  
`pi-ai` | Zentrale LLM-Abstraktionen: `Model`, `streamSimple`, Nachrichtentypen, Provider-APIs  
`pi-agent-core` | Agent-Schleife, Tool-Ausführung, `AgentMessage`-Typen  
`pi-coding-agent` | High-Level-SDK: `createAgentSession`, `SessionManager`, `AuthStorage`, `ModelRegistry`, integrierte Tools  
`pi-tui` | Terminal-UI-Komponenten (verwendet im lokalen TUI-Modus von OpenClaw)  
  
## Dateistruktur

CodeCopy code
[code]
    src/agents/├── pi-embedded-runner.ts          # Re-exports from pi-embedded-runner/├── pi-embedded-runner/│   ├── run.ts                     # Main entry: runEmbeddedPiAgent()│   ├── run/│   │   ├── attempt.ts             # Single attempt logic with session setup│   │   ├── params.ts              # RunEmbeddedPiAgentParams type│   │   ├── payloads.ts            # Build response payloads from run results│   │   ├── images.ts              # Vision model image injection│   │   └── types.ts               # EmbeddedRunAttemptResult│   ├── abort.ts                   # Abort error detection│   ├── cache-ttl.ts               # Cache TTL tracking for context pruning│   ├── compact.ts                 # Manual/auto compaction logic│   ├── extensions.ts              # Load pi extensions for embedded runs│   ├── extra-params.ts            # Provider-specific stream params│   ├── google.ts                  # Google/Gemini turn ordering fixes│   ├── history.ts                 # History limiting (DM vs group)│   ├── lanes.ts                   # Session/global command lanes│   ├── logger.ts                  # Subsystem logger│   ├── model.ts                   # Model resolution via ModelRegistry│   ├── runs.ts                    # Active run tracking, abort, queue│   ├── sandbox-info.ts            # Sandbox info for system prompt│   ├── session-manager-cache.ts   # SessionManager instance caching│   ├── session-manager-init.ts    # Session file initialization│   ├── system-prompt.ts           # System prompt builder│   ├── tool-split.ts              # Split tools into builtIn vs custom│   ├── types.ts                   # EmbeddedPiAgentMeta, EmbeddedPiRunResult│   └── utils.ts                   # ThinkLevel mapping, error description├── pi-embedded-subscribe.ts       # Session event subscription/dispatch├── pi-embedded-subscribe.types.ts # SubscribeEmbeddedPiSessionParams├── pi-embedded-subscribe.handlers.ts # Event handler factory├── pi-embedded-subscribe.handlers.lifecycle.ts├── pi-embedded-subscribe.handlers.types.ts├── pi-embedded-block-chunker.ts   # Streaming block reply chunking├── pi-embedded-messaging.ts       # Messaging tool sent tracking├── pi-embedded-helpers.ts         # Error classification, turn validation├── pi-embedded-helpers/           # Helper modules├── pi-embedded-utils.ts           # Formatting utilities├── pi-tools.ts                    # createOpenClawCodingTools()├── pi-tools.abort.ts              # AbortSignal wrapping for tools├── pi-tools.policy.ts             # Tool allowlist/denylist policy├── pi-tools.read.ts               # Read tool customizations├── pi-tools.schema.ts             # Tool schema normalization├── pi-tools.types.ts              # AnyAgentTool type alias├── pi-tool-definition-adapter.ts  # AgentTool -> ToolDefinition adapter├── pi-settings.ts                 # Settings overrides├── pi-hooks/                      # Custom pi hooks│   ├── compaction-safeguard.ts    # Safeguard extension│   ├── compaction-safeguard-runtime.ts│   ├── context-pruning.ts         # Cache-TTL context pruning extension│   └── context-pruning/├── model-auth.ts                  # Auth profile resolution├── auth-profiles.ts               # Profile store, cooldown, failover├── model-selection.ts             # Default model resolution├── models-config.ts               # models.json generation├── model-catalog.ts               # Model catalog cache├── context-window-guard.ts        # Context window validation├── failover-error.ts              # FailoverError class├── defaults.ts                    # DEFAULT_PROVIDER, DEFAULT_MODEL├── system-prompt.ts               # buildAgentSystemPrompt()├── system-prompt-params.ts        # System prompt parameter resolution├── system-prompt-report.ts        # Debug report generation├── tool-summaries.ts              # Tool description summaries├── tool-policy.ts                 # Tool policy resolution├── transcript-policy.ts           # Transcript validation policy├── skills.ts                      # Skill snapshot/prompt building├── skills/                        # Skill subsystem├── sandbox.ts                     # Sandbox context resolution├── sandbox/                       # Sandbox subsystem├── channel-tools.ts               # Channel-specific tool injection├── openclaw-tools.ts              # OpenClaw-specific tools├── bash-tools.ts                  # exec/process tools├── apply-patch.ts                 # apply_patch tool (OpenAI)├── tools/                         # Individual tool implementations│   ├── browser-tool.ts│   ├── canvas-tool.ts│   ├── cron-tool.ts│   ├── gateway-tool.ts│   ├── image-tool.ts│   ├── message-tool.ts│   ├── nodes-tool.ts│   ├── session*.ts│   ├── web-*.ts│   └── ...└── ...
[/code]

Kanalspezifische Message-Action-Runtimes befinden sich jetzt in den vom Plugin verwalteten Erweiterungsverzeichnissen statt unter `src/agents/tools`, zum Beispiel:

  * die Runtime-Dateien für Aktionen des Discord-Plugins
  * die Runtime-Datei für Aktionen des Slack-Plugins
  * die Runtime-Datei für Aktionen des Telegram-Plugins
  * die Runtime-Datei für Aktionen des WhatsApp-Plugins


## Zentraler Integrationsablauf

### 1\. Einen eingebetteten Agent ausführen

Der Haupteinstiegspunkt ist `runEmbeddedPiAgent()` in `pi-embedded-runner/run.ts`:

typescriptCopy code
[code]
     const result = await runEmbeddedPiAgent({  sessionId: "user-123",  sessionKey: "main:whatsapp:+1234567890",  sessionFile: "/path/to/session.jsonl",  workspaceDir: "/path/to/workspace",  config: openclawConfig,  prompt: "Hello, how are you?",  provider: "anthropic",  model: "claude-sonnet-4-6",  timeoutMs: 120_000,  runId: "run-abc",  onBlockReply: async (payload) => {    await sendToChannel(payload.text, payload.mediaUrls);  },});
[/code]

### 2\. Sitzungserstellung

In `runEmbeddedAttempt()` (aufgerufen von `runEmbeddedPiAgent()`) wird das pi SDK verwendet:

typescriptCopy code
[code]
       createAgentSession,  DefaultResourceLoader,  SessionManager,  SettingsManager,} from "@earendil-works/pi-coding-agent"; const resourceLoader = new DefaultResourceLoader({  cwd: resolvedWorkspace,  agentDir,  settingsManager,  additionalExtensionPaths,});await resourceLoader.reload(); const { session } = await createAgentSession({  cwd: resolvedWorkspace,  agentDir,  authStorage: params.authStorage,  modelRegistry: params.modelRegistry,  model: params.model,  thinkingLevel: mapThinkingLevel(params.thinkLevel),  tools: builtInTools,  customTools: allCustomTools,  sessionManager,  settingsManager,  resourceLoader,}); applySystemPromptOverrideToSession(session, systemPromptOverride);
[/code]

### 3\. Event-Abonnement

`subscribeEmbeddedPiSession()` abonniert die Events von pi's `AgentSession`:

typescriptCopy code
[code]
    const subscription = subscribeEmbeddedPiSession({  session: activeSession,  runId: params.runId,  verboseLevel: params.verboseLevel,  reasoningMode: params.reasoningLevel,  toolResultFormat: params.toolResultFormat,  onToolResult: params.onToolResult,  onReasoningStream: params.onReasoningStream,  onBlockReply: params.onBlockReply,  onPartialReply: params.onPartialReply,  onAgentEvent: params.onAgentEvent,});
[/code]

Behandelte Events umfassen:

  * `message_start` / `message_end` / `message_update` (Streaming-Text/Thinking)
  * `tool_execution_start` / `tool_execution_update` / `tool_execution_end`
  * `turn_start` / `turn_end`
  * `agent_start` / `agent_end`
  * `compaction_start` / `compaction_end`


### 4\. Prompting

Nach der Einrichtung wird die Sitzung mit einem Prompt angesteuert:

typescriptCopy code
[code]
    await session.prompt(effectivePrompt, { images: imageResult.images });
[/code]

Das SDK behandelt die vollständige Agent-Schleife: Senden an das LLM, Ausführen von Tool-Aufrufen und Streamen von Antworten.

Die Bildinjektion ist promptlokal: OpenClaw lädt Bildreferenzen aus dem aktuellen Prompt und übergibt sie nur für diesen Turn über `images`. Ältere History-Turns werden nicht erneut gescannt, um Bild-Payloads erneut zu injizieren.

## Tool-Architektur

### Tool-Pipeline

  1. **Basis-Tools** : pi's `codingTools` (read, bash, edit, write)
  2. **Benutzerdefinierte Ersetzungen** : OpenClaw ersetzt bash durch `exec`/`process` und passt read/edit/write für die Sandbox an
  3. **OpenClaw-Tools** : Messaging, Browser, Canvas, Sitzungen, Cron, Gateway usw.
  4. **Kanal-Tools** : Discord-/Telegram-/Slack-/WhatsApp-spezifische Action-Tools
  5. **Policy-Filterung** : Tools werden nach Profil, Provider, Agent, Gruppe und Sandbox-Policies gefiltert
  6. **Schema-Normalisierung** : Schemas werden für Gemini-/OpenAI-Besonderheiten bereinigt
  7. **AbortSignal-Wrapping** : Tools werden so gekapselt, dass sie Abort-Signale berücksichtigen


### Tool-Definition-Adapter

pi-agent-core's `AgentTool` hat eine andere `execute`-Signatur als pi-coding-agent's `ToolDefinition`. Der Adapter in `pi-tool-definition-adapter.ts` überbrückt dies:

typescriptCopy code
[code]
    export function toToolDefinitions(tools: AnyAgentTool[]): ToolDefinition[] {  return tools.map((tool) => ({    name: tool.name,    label: tool.label ?? name,    description: tool.description ?? "",    parameters: tool.parameters,    execute: async (toolCallId, params, onUpdate, _ctx, signal) => {      // pi-coding-agent signature differs from pi-agent-core      return await tool.execute(toolCallId, params, signal, onUpdate);    },  }));}
[/code]

### Tool-Split-Strategie

`splitSdkTools()` übergibt alle Tools über `customTools`:

typescriptCopy code
[code]
    export function splitSdkTools(options: { tools: AnyAgentTool[]; sandboxEnabled: boolean }) {  return {    builtInTools: [], // Empty. We override everything    customTools: toToolDefinitions(options.tools),  };}
[/code]

Dadurch bleiben OpenClaws Richtlinienfilterung, Sandbox-Integration und erweiterter Toolset über Provider hinweg konsistent.

## Aufbau des System-Prompts

Der System-Prompt wird in `buildAgentSystemPrompt()` (`system-prompt.ts`) erstellt. Er setzt einen vollständigen Prompt aus Abschnitten wie Tooling, Tool Call Style, Sicherheitsleitplanken, OpenClaw Control, Skills, Docs, Workspace, Sandbox, Messaging, Assistant Output Directives, Voice, Silent Replies, Heartbeats, Runtime-Metadaten sowie, wenn aktiviert, Memory und Reactions zusammen, ergänzt um optionale Kontextdateien und zusätzliche System-Prompt-Inhalte. Für den von Subagents verwendeten Minimal-Prompt-Modus werden Abschnitte gekürzt.

Der Prompt wird nach der Sitzungserstellung über `applySystemPromptOverrideToSession()` angewendet:

typescriptCopy code
[code]
    const systemPromptOverride = createSystemPromptOverride(appendPrompt);applySystemPromptOverrideToSession(session, systemPromptOverride);
[/code]

## Sitzungsverwaltung

### Sitzungsdateien

Sitzungen sind JSONL-Dateien mit Baumstruktur (Verknüpfung über id/parentId). Pis `SessionManager` übernimmt die Persistenz:

typescriptCopy code
[code]
    const sessionManager = SessionManager.open(params.sessionFile);
[/code]

OpenClaw kapselt dies mit `guardSessionManager()` für die Sicherheit von Tool-Ergebnissen.

### Sitzungscaching

`session-manager-cache.ts` cached SessionManager-Instanzen, um wiederholtes Parsen von Dateien zu vermeiden:

typescriptCopy code
[code]
    await prewarmSessionFile(params.sessionFile);sessionManager = SessionManager.open(params.sessionFile);trackSessionManagerAccess(params.sessionFile);
[/code]

### Verlaufsbegrenzung

`limitHistoryTurns()` kürzt den Gesprächsverlauf basierend auf dem Kanaltyp (DM gegenüber Gruppe).

### Compaction

Auto-Compaction wird bei Kontextüberlauf ausgelöst. Häufige Überlaufsignaturen sind `request_too_large`, `context length exceeded`, `input exceeds the maximum number of tokens`, `input token count exceeds the maximum number of input tokens`, `input is too long for the model` und `ollama error: context length exceeded`. `compactEmbeddedPiSessionDirect()` verarbeitet manuelle Compaction:

typescriptCopy code
[code]
    const compactResult = await compactEmbeddedPiSessionDirect({  sessionId, sessionFile, provider, model, ...});
[/code]

## Authentifizierung und Modellauflösung

### Auth-Profile

OpenClaw verwaltet einen Auth-Profilspeicher mit mehreren API-Schlüsseln pro Provider:

typescriptCopy code
[code]
    const authStore = ensureAuthProfileStore(agentDir, { allowKeychainPrompt: false });const profileOrder = resolveAuthProfileOrder({ cfg, store: authStore, provider, preferredProfile });
[/code]

Profile rotieren bei Fehlern mit Cooldown-Tracking:

typescriptCopy code
[code]
    await markAuthProfileFailure({ store, profileId, reason, cfg, agentDir });const rotated = await advanceAuthProfile();
[/code]

### Modellauflösung

typescriptCopy code
[code]
     const { model, error, authStorage, modelRegistry } = resolveModel(  provider,  modelId,  agentDir,  config,); // Uses pi's ModelRegistry and AuthStorageauthStorage.setRuntimeApiKey(model.provider, apiKeyInfo.apiKey);
[/code]

### Failover

`FailoverError` löst einen Modell-Fallback aus, wenn er konfiguriert ist:

typescriptCopy code
[code]
    if (fallbackConfigured && isFailoverErrorMessage(errorText)) {  throw new FailoverError(errorText, {    reason: promptFailoverReason ?? "unknown",    provider,    model: modelId,    profileId,    status: resolveFailoverStatus(promptFailoverReason),  });}
[/code]

## Pi-Erweiterungen

OpenClaw lädt benutzerdefinierte Pi-Erweiterungen für spezialisiertes Verhalten:

### Compaction-Schutzmaßnahme

`src/agents/pi-hooks/compaction-safeguard.ts` fügt Schutzmaßnahmen zur Compaction hinzu, einschließlich adaptiver Token-Budgetierung sowie Zusammenfassungen von Tool-Fehlern und Dateioperationen:

typescriptCopy code
[code]
    if (resolveCompactionMode(params.cfg) === "safeguard") {  setCompactionSafeguardRuntime(params.sessionManager, { maxHistoryShare });  paths.push(resolvePiExtensionPath("compaction-safeguard"));}
[/code]

### Kontextbereinigung

`src/agents/pi-hooks/context-pruning.ts` implementiert cache-TTL-basierte Kontextbereinigung:

typescriptCopy code
[code]
    if (cfg?.agents?.defaults?.contextPruning?.mode === "cache-ttl") {  setContextPruningRuntime(params.sessionManager, {    settings,    contextWindowTokens,    isToolPrunable,    lastCacheTouchAt,  });  paths.push(resolvePiExtensionPath("context-pruning"));}
[/code]

## Streaming und Blockantworten

### Block-Chunking

`EmbeddedBlockChunker` verwaltet das Streaming von Text in getrennte Antwortblöcke:

typescriptCopy code
[code]
    const blockChunker = blockChunking ? new EmbeddedBlockChunker(blockChunking) : null;
[/code]

### Entfernen von Thinking/Final-Tags

Streaming-Ausgabe wird verarbeitet, um `<think>`-/`<thinking>`-Blöcke zu entfernen und `<final>`-Inhalte zu extrahieren:

typescriptCopy code
[code]
    const stripBlockTags = (text: string, state: { thinking: boolean; final: boolean }) => {  // Strip <think>...</think> content  // If enforceFinalTag, only return <final>...</final> content};
[/code]

### Antwortdirektiven

Antwortdirektiven wie `[[media:url]]`, `[[voice]]`, `[[reply:id]]` werden geparst und extrahiert:

typescriptCopy code
[code]
    const { text: cleanedText, mediaUrls, audioAsVoice, replyToId } = consumeReplyDirectives(chunk);
[/code]

## Fehlerbehandlung

### Fehlerklassifizierung

`pi-embedded-helpers.ts` klassifiziert Fehler für eine passende Behandlung:

typescriptCopy code
[code]
    isContextOverflowError(errorText)     // Context too largeisCompactionFailureError(errorText)   // Compaction failedisAuthAssistantError(lastAssistant)   // Auth failureisRateLimitAssistantError(...)        // Rate limitedisFailoverAssistantError(...)         // Should failoverclassifyFailoverReason(errorText)     // "auth" | "rate_limit" | "quota" | "timeout" | ...
[/code]

### Fallback für Thinking-Level

Wenn ein Thinking-Level nicht unterstützt wird, wird ein Fallback verwendet:

typescriptCopy code
[code]
    const fallbackThinking = pickFallbackThinkingLevel({  message: errorText,  attempted: attemptedThinking,});if (fallbackThinking) {  thinkLevel = fallbackThinking;  continue;}
[/code]

## Sandbox-Integration

Wenn der Sandbox-Modus aktiviert ist, werden Tools und Pfade eingeschränkt:

typescriptCopy code
[code]
    const sandbox = await resolveSandboxContext({  config: params.config,  sessionKey: sandboxSessionKey,  workspaceDir: resolvedWorkspace,}); if (sandboxRoot) {  // Use sandboxed read/edit/write tools  // Exec runs in container  // Browser uses bridge URL}
[/code]

## Provider-spezifische Behandlung

### Anthropic

  * Bereinigung des magischen Strings für Ablehnungen
  * Turn-Validierung für aufeinanderfolgende Rollen
  * Strenge Upstream-Pi-Validierung von Tool-Parametern


### Google/Gemini

  * Plugin-eigene Bereinigung von Tool-Schemas


### OpenAI

  * `apply_patch`-Tool für Codex-Modelle
  * Behandlung von Thinking-Level-Downgrades


## TUI-Integration

OpenClaw verfügt außerdem über einen lokalen TUI-Modus, der pi-tui-Komponenten direkt verwendet:

typescriptCopy code
[code]
    // src/tui/tui.ts 
[/code]

Dies stellt ein interaktives Terminal-Erlebnis ähnlich dem nativen Modus von Pi bereit.

## Wichtige Unterschiede zur Pi-CLI

Aspekt | Pi-CLI | Eingebettetes OpenClaw  
---|---|---  
Aufruf | `pi`-Befehl / RPC | SDK über `createAgentSession()`  
Tools | Standard-Coding-Tools | Benutzerdefinierte OpenClaw-Tool-Suite  
System-Prompt | [AGENTS.md](<http://AGENTS.md>) \+ Prompts | Dynamisch pro Kanal/Kontext  
Sitzungsspeicher | `~/.pi/agent/sessions/` | `~/.openclaw/agents/<agentId>/sessions/` (oder `$OPENCLAW_STATE_DIR/agents/<agentId>/sessions/`)  
Authentifizierung | Einzelne Anmeldeinformation | Mehrere Profile mit Rotation  
Erweiterungen | Von Datenträger geladen | Programmatisch + Datenträgerpfade  
Ereignisbehandlung | TUI-Rendering | Callback-basiert (onBlockReply usw.)  
  
## Zukünftige Überlegungen

Bereiche für potenzielle Überarbeitung:

  1. **Abgleich von Tool-Signaturen** : Derzeitige Anpassung zwischen pi-agent-core- und pi-coding-agent-Signaturen
  2. **Kapselung des Session Managers** : `guardSessionManager` erhöht die Sicherheit, steigert aber die Komplexität
  3. **Laden von Erweiterungen** : Könnte Pis `ResourceLoader` direkter nutzen
  4. **Komplexität des Streaming-Handlers** : `subscribeEmbeddedPiSession` ist umfangreich geworden
  5. **Provider-Besonderheiten** : Viele Provider-spezifische Codepfade, die Pi potenziell übernehmen könnte


## Tests

Die Pi-Integrationsabdeckung umfasst diese Suites:

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


Live/Opt-in:

  * `src/agents/pi-embedded-runner-extraparams.live.test.ts` (aktivieren mit `OPENCLAW_LIVE_TEST=1`)


Aktuelle Ausführungsbefehle finden Sie unter [Pi-Entwicklungsworkflow](</de/pi-dev>).

## Verwandt

  * [Pi-Entwicklungsworkflow](</de/pi-dev>)
  * [Installationsübersicht](</de/install>)


Was this useful?YesNo