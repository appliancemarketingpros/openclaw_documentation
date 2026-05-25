---
title: Auxiliares de tempo de execução do Plugin
source_url: https://docs.openclaw.ai/pt-BR/plugins/sdk-runtime
scraped_at: 2026-05-25
---

Referência para o objeto `api.runtime` injetado em todo plugin durante o registro. Use esses auxiliares em vez de importar componentes internos do host diretamente.

[**Plugins de canal** Guia passo a passo que usa esses auxiliares no contexto de plugins de canal. ](</pt-BR/plugins/sdk-channel-plugins>) [**Plugins de provedor** Guia passo a passo que usa esses auxiliares no contexto de plugins de provedor. ](</pt-BR/plugins/sdk-provider-plugins>)

typescriptCopy code
[code]
    register(api) {  const runtime = api.runtime;}
[/code]

## Carregamento e gravações de configuração

Prefira a configuração que já foi passada para o caminho de chamada ativo, por exemplo `api.config` durante o registro ou um argumento `cfg` em callbacks de canal/provedor. Isso mantém um snapshot de processo fluindo pelo trabalho em vez de reanalisar a configuração em caminhos críticos.

Use `api.runtime.config.current()` somente quando um manipulador de longa duração precisar do snapshot atual do processo e nenhuma configuração tiver sido passada para essa função. O valor retornado é somente leitura; clone ou use um auxiliar de mutação antes de editar.

Fábricas de ferramentas recebem `ctx.runtimeConfig` mais `ctx.getRuntimeConfig()`. Use o getter dentro do callback `execute` de uma ferramenta de longa duração quando a configuração puder mudar depois que a definição da ferramenta foi criada.

Persista alterações com `api.runtime.config.mutateConfigFile(...)` ou `api.runtime.config.replaceConfigFile(...)`. Cada gravação deve escolher uma política explícita de `afterWrite`:

  * `afterWrite: { mode: "auto" }` permite que o decisor de recarregamento do Gateway decida.
  * `afterWrite: { mode: "restart", reason: "..." }` força uma reinicialização limpa quando o gravador sabe que hot reload não é seguro.
  * `afterWrite: { mode: "none", reason: "..." }` suprime o recarregamento/reinicialização automático somente quando o chamador é responsável pelo acompanhamento.


Os auxiliares de mutação retornam `afterWrite` mais um resumo tipado `followUp`, para que chamadores possam registrar ou testar se solicitaram uma reinicialização. O Gateway ainda controla quando essa reinicialização realmente acontece.

`api.runtime.config.loadConfig()` e `api.runtime.config.writeConfigFile(...)` são auxiliares de compatibilidade obsoletos sob `runtime-config-load-write`. Eles avisam uma vez em runtime e permanecem disponíveis para plugins externos antigos durante a janela de migração. Plugins integrados não devem usá-los; as proteções de limite de configuração falham se o código do plugin os chamar ou importar esses auxiliares de subcaminhos do SDK de plugins.

Para importações diretas do SDK, use os subcaminhos focados de configuração em vez do barrel amplo de compatibilidade `openclaw/plugin-sdk/config-runtime`: `config-contracts` para tipos, `plugin-config-runtime` para asserções de configuração já carregada e consulta de entrada de plugin, `runtime-config-snapshot` para snapshots atuais do processo e `config-mutation` para gravações. Testes de plugins integrados devem simular esses subcaminhos focados diretamente, em vez de simular o barrel amplo de compatibilidade.

O código interno de runtime do OpenClaw segue a mesma direção: carregue a configuração uma vez na CLI, no Gateway ou no limite do processo e, em seguida, passe esse valor adiante. Gravações de mutação bem-sucedidas atualizam o snapshot de runtime do processo e avançam sua revisão interna; caches de longa duração devem usar a chave de cache pertencente ao runtime em vez de serializar a configuração localmente. Módulos de runtime de longa duração têm um scanner de tolerância zero para chamadas ambientes de `loadConfig()`; use um `cfg` passado, um `context.getRuntimeConfig()` de solicitação ou `getRuntimeConfig()` em um limite explícito de processo.

Caminhos de execução de provedor e canal devem usar o snapshot de configuração de runtime ativo, não um snapshot de arquivo retornado para releitura ou edição de configuração. Snapshots de arquivo preservam valores de origem, como marcadores SecretRef, para UI e gravações; callbacks de provedor precisam da visão de runtime resolvida. Quando um auxiliar puder ser chamado com o snapshot de origem ativo ou com o snapshot de runtime ativo, encaminhe por `selectApplicableRuntimeConfig()` antes de ler credenciais.

## Namespaces de runtime

api.runtime.agent

Identidade do agente, diretórios e gerenciamento de sessão.

typescriptCopy code
[code]
    // Resolve the agent's working directoryconst agentDir = api.runtime.agent.resolveAgentDir(cfg); // Resolve agent workspaceconst workspaceDir = api.runtime.agent.resolveAgentWorkspaceDir(cfg); // Get agent identityconst identity = api.runtime.agent.resolveAgentIdentity(cfg); // Get default thinking levelconst thinking = api.runtime.agent.resolveThinkingDefault({  cfg,  provider,  model,}); // Validate a user-provided thinking level against the active provider profileconst policy = api.runtime.agent.resolveThinkingPolicy({ provider, model });const level = api.runtime.agent.normalizeThinkingLevel("extra high");if (level && policy.levels.some((entry) => entry.id === level)) {  // pass level to an embedded run} // Get agent timeoutconst timeoutMs = api.runtime.agent.resolveAgentTimeoutMs(cfg); // Ensure workspace existsawait api.runtime.agent.ensureAgentWorkspace(cfg); // Run an embedded agent turnconst agentDir = api.runtime.agent.resolveAgentDir(cfg);const result = await api.runtime.agent.runEmbeddedAgent({  sessionId: "my-plugin:task-1",  runId: crypto.randomUUID(),  sessionFile: path.join(agentDir, "sessions", "my-plugin-task-1.jsonl"),  workspaceDir: api.runtime.agent.resolveAgentWorkspaceDir(cfg),  prompt: "Summarize the latest changes",  timeoutMs: api.runtime.agent.resolveAgentTimeoutMs(cfg),});
[/code]

`runEmbeddedAgent(...)` é o auxiliar neutro para iniciar uma rodada normal do agente OpenClaw a partir do código de plugin. Ele usa a mesma resolução de provedor/modelo e seleção de harness de agente que as respostas acionadas por canal.

`runEmbeddedPiAgent(...)` permanece como alias de compatibilidade.

`resolveThinkingPolicy(...)` retorna os níveis de pensamento compatíveis do provedor/modelo e o padrão opcional. Plugins de provedor são responsáveis pelo perfil específico do modelo por meio de seus hooks de pensamento, portanto plugins de ferramentas devem chamar esse auxiliar de runtime em vez de importar ou duplicar listas de provedores.

`normalizeThinkingLevel(...)` converte texto do usuário como `on`, `x-high` ou `extra high` para o nível armazenado canônico antes de verificá-lo contra a política resolvida.

**Auxiliares de armazenamento de sessão** ficam em `api.runtime.agent.session`:

typescriptCopy code
[code]
    const storePath = api.runtime.agent.session.resolveStorePath(cfg);const store = api.runtime.agent.session.loadSessionStore(storePath);await api.runtime.agent.session.updateSessionStore(storePath, (nextStore) => {  // Patch one entry without replacing the whole file from stale state.  nextStore[sessionKey] = { ...nextStore[sessionKey], thinkingLevel: "high" };});const filePath = api.runtime.agent.session.resolveSessionFilePath(cfg, sessionId);
[/code]

Prefira `updateSessionStore(...)` ou `updateSessionStoreEntry(...)` para gravações de runtime. Eles passam pelo gravador de armazenamento de sessão pertencente ao Gateway, preservam atualizações concorrentes e reutilizam o cache quente. `saveSessionStore(...)` permanece disponível para compatibilidade e regravações em estilo manutenção offline.

api.runtime.agent.defaults

Constantes padrão de modelo e provedor:

typescriptCopy code
[code]
    const model = api.runtime.agent.defaults.model; // e.g. "anthropic/claude-sonnet-4-6"const provider = api.runtime.agent.defaults.provider; // e.g. "anthropic"
[/code]

api.runtime.llm

Execute uma conclusão de texto pertencente ao host sem importar componentes internos de provedor nem duplicar a preparação de modelo/autenticação/URL base do OpenClaw.

typescriptCopy code
[code]
    const result = await api.runtime.llm.complete({  messages: [{ role: "user", content: "Summarize this transcript." }],  purpose: "my-plugin.summary",  maxTokens: 512,  temperature: 0.2,});
[/code]

O auxiliar usa o mesmo caminho de preparação de conclusão simples que o runtime integrado do OpenClaw e o snapshot de configuração de runtime pertencente ao host. Mecanismos de contexto recebem uma capacidade `llm.complete` vinculada à sessão, portanto chamadas de modelo usam o agente da sessão ativa e não recorrem silenciosamente ao agente padrão. O resultado inclui atribuição de provedor/modelo/agente, além de uso normalizado de tokens, cache e custo estimado quando disponível.

api.runtime.subagent

Inicie e gerencie execuções de subagente em segundo plano.

typescriptCopy code
[code]
    // Start a subagent runconst { runId } = await api.runtime.subagent.run({  sessionKey: "agent:main:subagent:search-helper",  message: "Expand this query into focused follow-up searches.",  provider: "openai", // optional override  model: "gpt-4.1-mini", // optional override  deliver: false,}); // Wait for completionconst result = await api.runtime.subagent.waitForRun({ runId, timeoutMs: 30000 }); // Read session messagesconst { messages } = await api.runtime.subagent.getSessionMessages({  sessionKey: "agent:main:subagent:search-helper",  limit: 10,}); // Delete a sessionawait api.runtime.subagent.deleteSession({  sessionKey: "agent:main:subagent:search-helper",});
[/code]

`deleteSession(...)` pode excluir sessões criadas pelo mesmo plugin por meio de `api.runtime.subagent.run(...)`. Excluir sessões arbitrárias de usuário ou operador ainda exige uma solicitação do Gateway com escopo de administrador.

api.runtime.nodes

Liste nodes conectados e invoque um comando hospedado em node a partir de código de plugin carregado pelo Gateway ou de comandos de CLI de plugin. Use isto quando um plugin for responsável por trabalho local em um dispositivo pareado, por exemplo uma ponte de navegador ou áudio em outro Mac.

typescriptCopy code
[code]
    const { nodes } = await api.runtime.nodes.list({ connected: true }); const result = await api.runtime.nodes.invoke({  nodeId: "mac-studio",  command: "my-plugin.command",  params: { action: "start" },  timeoutMs: 30000,});
[/code]

Dentro do Gateway, este runtime é no processo. Em comandos de CLI de plugin, ele chama o Gateway configurado por RPC, então comandos como `openclaw googlemeet recover-tab` podem inspecionar nodes pareados pelo terminal. Comandos de node ainda passam pelo pareamento normal de nodes do Gateway, allowlists de comandos, políticas de invocação de node de plugin e manipulação de comandos local ao node.

Plugins que expõem comandos perigosos hospedados em node devem registrar uma política de invocação de node com `api.registerNodeInvokePolicy(...)`. A política é executada no Gateway após verificações de allowlist de comandos e antes que o comando seja encaminhado para o node, de modo que chamadas diretas de `node.invoke` e ferramentas de plugin de nível mais alto compartilhem o mesmo caminho de aplicação.

api.runtime.tasks.managedFlows

Vincule um runtime de fluxo de tarefas a uma chave de sessão OpenClaw existente ou a um contexto de ferramenta confiável e, em seguida, crie e gerencie fluxos de tarefas sem passar um proprietário em cada chamada.

Fluxo de tarefas rastreia estado durável de workflows em várias etapas. Ele não é um agendador: use Cron ou `api.session.workflow.scheduleSessionTurn(...)` para despertares futuros e, em seguida, use `managedFlows` a partir da rodada agendada quando esse trabalho precisar de estado de fluxo, tarefas filhas, esperas ou cancelamento.

typescriptCopy code
[code]
    const taskFlow = api.runtime.tasks.managedFlows.fromToolContext(ctx); const created = taskFlow.createManaged({  controllerId: "my-plugin/review-batch",  goal: "Review new pull requests",}); const child = taskFlow.runTask({  flowId: created.flowId,  runtime: "acp",  childSessionKey: "agent:main:subagent:reviewer",  task: "Review PR #123",  status: "running",  startedAt: Date.now(),}); const waiting = taskFlow.setWaiting({  flowId: created.flowId,  expectedRevision: created.revision,  currentStep: "await-human-reply",  waitJson: { kind: "reply", channel: "telegram" },});
[/code]

Use `bindSession({ sessionKey, requesterOrigin })` quando você já tiver uma chave de sessão confiável do OpenClaw da sua própria camada de vinculação. Não vincule a partir de entrada bruta do usuário.

api.runtime.tts

Síntese de texto em fala.

typescriptCopy code
[code]
    // Standard TTSconst clip = await api.runtime.tts.textToSpeech({  text: "Hello from OpenClaw",  cfg: api.config,}); // Telephony-optimized TTSconst telephonyClip = await api.runtime.tts.textToSpeechTelephony({  text: "Hello from OpenClaw",  cfg: api.config,}); // List available voicesconst voices = await api.runtime.tts.listVoices({  provider: "elevenlabs",  cfg: api.config,});
[/code]

Usa a configuração principal `messages.tts` e a seleção de provedor. Retorna buffer de áudio PCM + taxa de amostragem.

api.runtime.mediaUnderstanding

Análise de imagens, áudio e vídeo.

typescriptCopy code
[code]
    // Describe an imageconst image = await api.runtime.mediaUnderstanding.describeImageFile({  filePath: "/tmp/inbound-photo.jpg",  cfg: api.config,  agentDir: "/tmp/agent",}); // Transcribe audioconst { text } = await api.runtime.mediaUnderstanding.transcribeAudioFile({  filePath: "/tmp/inbound-audio.ogg",  cfg: api.config,  mime: "audio/ogg", // optional, for when MIME cannot be inferred}); // Describe a videoconst video = await api.runtime.mediaUnderstanding.describeVideoFile({  filePath: "/tmp/inbound-video.mp4",  cfg: api.config,}); // Generic file analysisconst result = await api.runtime.mediaUnderstanding.runFile({  filePath: "/tmp/inbound-file.pdf",  cfg: api.config,}); // Structured image extraction through a specific provider/model.// Include at least one image; text inputs are supplemental context.const evidence = await api.runtime.mediaUnderstanding.extractStructuredWithModel({  provider: "codex",  model: "gpt-5.5",  input: [    {      type: "image",      buffer: receiptImageBuffer,      fileName: "receipt.png",      mime: "image/png",    },    { type: "text", text: "Prefer the printed total over handwritten notes." },  ],  instructions: "Extract vendor, total, and searchable tags.",  schemaName: "receipt.evidence",  jsonSchema: {    type: "object",    properties: {      vendor: { type: "string" },      total: { type: "number" },      tags: { type: "array", items: { type: "string" } },    },    required: ["vendor", "total"],  },  cfg: api.config,});
[/code]

Retorna `{ text: undefined }` quando nenhuma saída é produzida (por exemplo, entrada ignorada).

api.runtime.imageGeneration

Geração de imagem.

typescriptCopy code
[code]
    const result = await api.runtime.imageGeneration.generate({  prompt: "A robot painting a sunset",  cfg: api.config,}); const providers = api.runtime.imageGeneration.listProviders({ cfg: api.config });
[/code]

api.runtime.webSearch

Pesquisa na web.

typescriptCopy code
[code]
    const providers = api.runtime.webSearch.listProviders({ config: api.config }); const result = await api.runtime.webSearch.search({  config: api.config,  args: { query: "OpenClaw plugin SDK", count: 5 },});
[/code]

api.runtime.media

Utilitários de mídia de baixo nível.

typescriptCopy code
[code]
    const webMedia = await api.runtime.media.loadWebMedia(url);const mime = await api.runtime.media.detectMime(buffer);const kind = api.runtime.media.mediaKindFromMime("image/jpeg"); // "image"const isVoice = api.runtime.media.isVoiceCompatibleAudio(filePath);const metadata = await api.runtime.media.getImageMetadata(filePath);const resized = await api.runtime.media.resizeToJpeg(buffer, { maxWidth: 800 });const terminalQr = await api.runtime.media.renderQrTerminal("https://openclaw.ai");const pngQr = await api.runtime.media.renderQrPngBase64("https://openclaw.ai", {  scale: 6, // 1-12  marginModules: 4, // 0-16});const pngQrDataUrl = await api.runtime.media.renderQrPngDataUrl("https://openclaw.ai");const tmpRoot = resolvePreferredOpenClawTmpDir();const pngQrFile = await api.runtime.media.writeQrPngTempFile("https://openclaw.ai", {  tmpRoot,  dirPrefix: "my-plugin-qr-",  fileName: "qr.png",});
[/code]

api.runtime.config

Snapshot da configuração de runtime atual e gravações transacionais de configuração. Prefira a configuração que já foi passada para o caminho de chamada ativo; use `current()` somente quando o manipulador precisar diretamente do snapshot do processo.

typescriptCopy code
[code]
    const cfg = api.runtime.config.current();await api.runtime.config.mutateConfigFile({  afterWrite: { mode: "auto" },  mutate(draft) {    draft.plugins ??= {};  },});
[/code]

`mutateConfigFile(...)` e `replaceConfigFile(...)` retornam um valor `followUp`, por exemplo `{ mode: "restart", requiresRestart: true, reason }`, que registra a intenção do gravador sem tirar o controle de reinicialização do Gateway.

api.runtime.system

Utilitários em nível de sistema.

typescriptCopy code
[code]
    await api.runtime.system.enqueueSystemEvent(event);api.runtime.system.requestHeartbeat({  source: "other",  intent: "event",  reason: "plugin-event",});api.runtime.system.requestHeartbeatNow({ reason: "plugin-event" }); // Deprecated compatibility alias.const output = await api.runtime.system.runCommandWithTimeout(cmd, args, opts);const hint = api.runtime.system.formatNativeDependencyHint(pkg);
[/code]

api.runtime.events

Assinaturas de eventos.

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

Resolução de autenticação de modelo e provedor.

typescriptCopy code
[code]
    const auth = await api.runtime.modelAuth.getApiKeyForModel({ model, cfg });const providerAuth = await api.runtime.modelAuth.resolveApiKeyForProvider({  provider: "openai",  cfg,});
[/code]

api.runtime.state

Resolução de diretório de estado e armazenamento chaveado baseado em SQLite.

typescriptCopy code
[code]
    const stateDir = api.runtime.state.resolveStateDir(process.env);const store = api.runtime.state.openKeyedStore&lt;MyRecord&gt;({  namespace: "my-feature",  maxEntries: 200,  defaultTtlMs: 15 * 60_000,}); await store.register("key-1", { value: "hello" });const claimed = await store.registerIfAbsent("dedupe-key", { value: "first" });const value = await store.lookup("key-1");await store.consume("key-1");await store.clear();
[/code]

Armazenamentos chaveados sobrevivem a reinicializações e são isolados pelo id do Plugin vinculado ao runtime. Use `registerIfAbsent(...)` para reivindicações atômicas de desduplicação: ele retorna `true` quando a chave estava ausente ou expirada e foi registrada, ou `false` quando um valor ativo já existe sem sobrescrever seu valor, horário de criação ou TTL. Limites: `maxEntries` por namespace, 1.000 linhas ativas por Plugin, valores JSON abaixo de 64 KB e expiração opcional por TTL.

api.runtime.tools

Fábricas de ferramentas de Memory e CLI.

typescriptCopy code
[code]
    const getTool = api.runtime.tools.createMemoryGetTool(/* ... */);const searchTool = api.runtime.tools.createMemorySearchTool(/* ... */);api.runtime.tools.registerMemoryCli(/* ... */);
[/code]

api.runtime.channel

Auxiliares de runtime específicos de canal (disponíveis quando um Plugin de canal é carregado).

`api.runtime.channel.mentions` é a superfície compartilhada de política de menção recebida para plugins de canal incluídos que usam injeção de runtime:

typescriptCopy code
[code]
    const mentionMatch = api.runtime.channel.mentions.matchesMentionWithExplicit(text, {  mentionRegexes,  mentionPatterns,}); const decision = api.runtime.channel.mentions.resolveInboundMentionDecision({  facts: {    canDetectMention: true,    wasMentioned: mentionMatch.matched,    implicitMentionKinds: api.runtime.channel.mentions.implicitMentionKindWhen(      "reply_to_bot",      isReplyToBot,    ),  },  policy: {    isGroup,    requireMention,    allowTextCommands,    hasControlCommand,    commandAuthorized,  },});
[/code]

Auxiliares de menção disponíveis:

  * `buildMentionRegexes`
  * `matchesMentionPatterns`
  * `matchesMentionWithExplicit`
  * `implicitMentionKindWhen`
  * `resolveInboundMentionDecision`


`api.runtime.channel.mentions` intencionalmente não expõe os auxiliares de compatibilidade `resolveMentionGating*` mais antigos. Prefira o caminho normalizado `{ facts, policy }`.

## Armazenando referências de runtime

Use `createPluginRuntimeStore` para armazenar a referência de runtime para uso fora do callback `register`:

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

## Outros campos `api` de nível superior

Além de `api.runtime`, o objeto de API também fornece:

ID do Plugin.

Nome de exibição do Plugin.

Instantâneo da configuração atual (instantâneo ativo em memória do ambiente de execução quando disponível).

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaS5wbHVnaW5Db25maWciIHR5cGU9IlJlY29yZDxzdHJpbmcsIHVua25vd24 "> Configuração específica do Plugin de `plugins.entries.<id>.config`.

Registrador com escopo (`debug`, `info`, `warn`, `error`).

Modo de carregamento atual; `"setup-runtime"` é a janela leve de inicialização/configuração anterior à entrada completa.

## Relacionados

  * [Componentes internos do Plugin](</pt-BR/plugins/architecture>) — modelo de capacidades e registro
  * [Pontos de entrada do SDK](</pt-BR/plugins/sdk-entrypoints>) — opções de `definePluginEntry`
  * [Visão geral do SDK](</pt-BR/plugins/sdk-overview>) — referência de subcaminho


Was this useful?YesNo