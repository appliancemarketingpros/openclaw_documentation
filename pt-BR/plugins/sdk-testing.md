---
title: Testes de Plugin
source_url: https://docs.openclaw.ai/pt-BR/plugins/sdk-testing
scraped_at: 2026-05-25
---

Referência para utilitários, padrões e aplicação de lint de testes para Plugins do OpenClaw.

## Utilitários de teste

Estes subcaminhos de auxiliares de teste são entrypoints de código-fonte locais do repositório para os próprios testes de Plugins integrados do OpenClaw. Eles não são exportações de pacote para Plugins de terceiros.

**Importação do mock da API de Plugin:** `openclaw/plugin-sdk/plugin-test-api`

**Importação do contrato de runtime do agente:** `openclaw/plugin-sdk/agent-runtime-test-contracts`

**Importação do contrato de canal:** `openclaw/plugin-sdk/channel-contract-testing`

**Importação do auxiliar de teste de canal:** `openclaw/plugin-sdk/channel-test-helpers`

**Importação de teste de destino de canal:** `openclaw/plugin-sdk/channel-target-testing`

**Importação do contrato de Plugin:** `openclaw/plugin-sdk/plugin-test-contracts`

**Importação de teste de runtime de Plugin:** `openclaw/plugin-sdk/plugin-test-runtime`

**Importação do contrato de provedor:** `openclaw/plugin-sdk/provider-test-contracts`

**Importação do mock HTTP de provedor:** `openclaw/plugin-sdk/provider-http-test-mocks`

**Importação de teste de ambiente/rede:** `openclaw/plugin-sdk/test-env`

**Importação de fixture genérica:** `openclaw/plugin-sdk/test-fixtures`

**Importação do mock de builtin do Node:** `openclaw/plugin-sdk/test-node-mocks`

Prefira os subcaminhos focados abaixo para novos testes de Plugin. O barrel amplo `openclaw/plugin-sdk/testing` existe apenas para compatibilidade legada. As proteções do repositório rejeitam novas importações reais de `plugin-sdk/testing` e `plugin-sdk/test-utils`; esses nomes permanecem apenas como superfícies de compatibilidade obsoletas para testes de registros de compatibilidade.

typescriptCopy code
[code]
       shouldAckReaction,  removeAckReactionAfterReply,} from "openclaw/plugin-sdk/channel-feedback";             bundledPluginRoot,  createCliRuntimeCapture,  typedCases,} from "openclaw/plugin-sdk/test-fixtures"; 
[/code]

### Exportações disponíveis

Exportação | Finalidade  
---|---  
`createTestPluginApi` | Cria um mock mínimo da API de Plugin para testes de unidade de registro direto. Importe de `plugin-sdk/plugin-test-api`  
`AUTH_PROFILE_RUNTIME_CONTRACT` | Fixture compartilhada do contrato de perfil de autenticação para adaptadores de runtime de agente nativos. Importe de `plugin-sdk/agent-runtime-test-contracts`  
`DELIVERY_NO_REPLY_RUNTIME_CONTRACT` | Fixture compartilhada do contrato de supressão de entrega para adaptadores de runtime de agente nativos. Importe de `plugin-sdk/agent-runtime-test-contracts`  
`OUTCOME_FALLBACK_RUNTIME_CONTRACT` | Fixture compartilhada do contrato de classificação de fallback para adaptadores de runtime de agente nativos. Importe de `plugin-sdk/agent-runtime-test-contracts`  
`createParameterFreeTool` | Cria fixtures de esquema de ferramenta dinâmica para testes de contrato de runtime nativo. Importe de `plugin-sdk/agent-runtime-test-contracts`  
`expectChannelInboundContextContract` | Verifica o formato do contexto de entrada do canal. Importe de `plugin-sdk/channel-contract-testing`  
`installChannelOutboundPayloadContractSuite` | Instala casos de contrato de payload de saída do canal. Importe de `plugin-sdk/channel-contract-testing`  
`createStartAccountContext` | Cria contextos de ciclo de vida de conta do canal. Importe de `plugin-sdk/channel-test-helpers`  
`installChannelActionsContractSuite` | Instala casos genéricos de contrato de ação de mensagem do canal. Importe de `plugin-sdk/channel-test-helpers`  
`installChannelSetupContractSuite` | Instala casos genéricos de contrato de configuração do canal. Importe de `plugin-sdk/channel-test-helpers`  
`installChannelStatusContractSuite` | Instala casos genéricos de contrato de status do canal. Importe de `plugin-sdk/channel-test-helpers`  
`expectDirectoryIds` | Verifica ids do diretório do canal a partir de uma função de listagem de diretório. Importe de `plugin-sdk/channel-test-helpers`  
`assertBundledChannelEntries` | Verifica se os entrypoints de canal incluídos expõem o contrato público esperado. Importe de `plugin-sdk/channel-test-helpers`  
`formatEnvelopeTimestamp` | Formata timestamps determinísticos de envelopes. Importe de `plugin-sdk/channel-test-helpers`  
`expectPairingReplyText` | Verifica o texto de resposta de pareamento do canal e extrai seu código. Importe de `plugin-sdk/channel-test-helpers`  
`describePluginRegistrationContract` | Instala verificações de contrato de registro de Plugin. Importe de `plugin-sdk/plugin-test-contracts`  
`registerSingleProviderPlugin` | Registra um Plugin de provedor em testes smoke do carregador. Importe de `plugin-sdk/plugin-test-runtime`  
`registerProviderPlugin` | Captura todos os tipos de provedor de um Plugin. Importe de `plugin-sdk/plugin-test-runtime`  
`registerProviderPlugins` | Captura registros de provedores entre múltiplos plugins. Importe de `plugin-sdk/plugin-test-runtime`  
`requireRegisteredProvider` | Verifica se uma coleção de provedores contém um id. Importe de `plugin-sdk/plugin-test-runtime`  
`createRuntimeEnv` | Cria um ambiente de runtime de CLI/Plugin mockado. Importe de `plugin-sdk/plugin-test-runtime`  
`createPluginSetupWizardStatus` | Cria auxiliares de status de configuração para plugins de canal. Importe de `plugin-sdk/plugin-test-runtime`  
`describeOpenAIProviderRuntimeContract` | Instala verificações de contrato de runtime da família de provedores. Importe de `plugin-sdk/provider-test-contracts`  
`expectPassthroughReplayPolicy` | Verifica se políticas de replay de provedor repassam ferramentas e metadados pertencentes ao provedor. Importe de `plugin-sdk/provider-test-contracts`  
`runRealtimeSttLiveTest` | Executa um teste ao vivo de provedor STT em tempo real com fixtures de áudio compartilhadas. Importe de `plugin-sdk/provider-test-contracts`  
`normalizeTranscriptForMatch` | Normaliza a saída de transcrição ao vivo antes de asserções aproximadas. Importe de `plugin-sdk/provider-test-contracts`  
`expectExplicitVideoGenerationCapabilities` | Verifica se provedores de vídeo declaram capacidades explícitas de modo de geração. Importe de `plugin-sdk/provider-test-contracts`  
`expectExplicitMusicGenerationCapabilities` | Verifica se provedores de música declaram capacidades explícitas de geração/edição. Importe de `plugin-sdk/provider-test-contracts`  
`mockSuccessfulDashscopeVideoTask` | Instala uma resposta bem-sucedida de tarefa de vídeo compatível com DashScope. Importe de `plugin-sdk/provider-test-contracts`  
`getProviderHttpMocks` | Acessa mocks Vitest HTTP/autenticação de provedor com adesão explícita. Importe de `plugin-sdk/provider-http-test-mocks`  
`installProviderHttpMockCleanup` | Redefine mocks HTTP/autenticação de provedor após cada teste. Importe de `plugin-sdk/provider-http-test-mocks`  
`installCommonResolveTargetErrorCases` | Casos de teste compartilhados para tratamento de erros de resolução de destino. Importe de `plugin-sdk/channel-target-testing`  
`shouldAckReaction` | Verifica se um canal deve adicionar uma reação de confirmação. Importe de `plugin-sdk/channel-feedback`  
`removeAckReactionAfterReply` | Remove a reação de confirmação após a entrega da resposta. Importe de `plugin-sdk/channel-feedback`  
`createTestRegistry` | Cria uma fixture de registro de Plugin de canal. Importe de `plugin-sdk/plugin-test-runtime` ou `plugin-sdk/channel-test-helpers`  
`createEmptyPluginRegistry` | Cria uma fixture de registro de Plugin vazio. Importe de `plugin-sdk/plugin-test-runtime` ou `plugin-sdk/channel-test-helpers`  
`setActivePluginRegistry` | Instala uma fixture de registro para testes de runtime de Plugin. Importe de `plugin-sdk/plugin-test-runtime` ou `plugin-sdk/channel-test-helpers`  
`createRequestCaptureJsonFetch` | Captura requisições JSON de fetch em testes de auxiliares de mídia. Importe de `plugin-sdk/test-env`  
`withServer` | Executa testes contra um servidor HTTP local descartável. Importe de `plugin-sdk/test-env`  
`createMockIncomingRequest` | Cria um objeto mínimo de requisição HTTP de entrada. Importe de `plugin-sdk/test-env`  
`withFetchPreconnect` | Executa testes de fetch com hooks de preconexão instalados. Importe de `plugin-sdk/test-env`  
`withEnv` / `withEnvAsync` | Altera temporariamente variáveis de ambiente. Importe de `plugin-sdk/test-env`  
`createTempHomeEnv` / `withTempHome` / `withTempDir` | Cria fixtures isoladas de teste do sistema de arquivos. Importe de `plugin-sdk/test-env`  
`createMockServerResponse` | Cria um mock mínimo de resposta de servidor HTTP. Importe de `plugin-sdk/test-env`  
`createCliRuntimeCapture` | Captura a saída de runtime da CLI em testes. Importe de `plugin-sdk/test-fixtures`  
`importFreshModule` | Importa um módulo ESM com um token de consulta novo para ignorar o cache de módulos. Importe de `plugin-sdk/test-fixtures`  
`bundledPluginRoot` / `bundledPluginFile` | Resolve caminhos de fixture de origem ou dist de Plugin incluído. Importe de `plugin-sdk/test-fixtures`  
`mockNodeBuiltinModule` | Instala mocks Vitest restritos de módulos embutidos do Node. Importe de `plugin-sdk/test-node-mocks`  
`createSandboxTestContext` | Cria contextos de teste de sandbox. Importe de `plugin-sdk/test-fixtures`  
`writeSkill` | Grava fixtures de skill. Importe de `plugin-sdk/test-fixtures`  
`makeAgentAssistantMessage` | Cria fixtures de mensagem de transcrição de agente. Importe de `plugin-sdk/test-fixtures`  
`peekSystemEvents` / `resetSystemEventsForTest` | Inspeciona e redefine fixtures de eventos do sistema. Importe de `plugin-sdk/test-fixtures`  
`sanitizeTerminalText` | Sanitiza a saída do terminal para asserções. Importe de `plugin-sdk/test-fixtures`  
`countLines` / `hasBalancedFences` | Verifica o formato da saída de fragmentação. Importe de `plugin-sdk/test-fixtures`  
`runProviderCatalog` | Executa um hook de catálogo de provedor com dependências de teste  
`resolveProviderWizardOptions` | Resolve escolhas do assistente de configuração de provedor em testes de contrato  
`resolveProviderModelPickerEntries` | Resolve entradas do seletor de modelos de provedor em testes de contrato  
`buildProviderPluginMethodChoice` | Cria ids de escolha do assistente de provedor para asserções  
`setProviderWizardProvidersResolverForTest` | Injeta provedores do assistente de provedor para testes isolados  
`createProviderUsageFetch` | Criar fixtures de busca de uso do provedor  
`useFrozenTime` / `useRealTime` | Congelar e restaurar temporizadores para testes sensíveis ao tempo. Importe de `plugin-sdk/test-env`  
`createTestWizardPrompter` | Criar um prompter simulado do assistente de configuração  
`createRuntimeTaskFlow` | Criar estado isolado de fluxo de tarefas em tempo de execução  
`typedCases` | Preservar tipos literais para testes orientados por tabela. Importe de `plugin-sdk/test-fixtures`  
  
As suítes de contrato de plugins incluídos também usam subcaminhos de teste do SDK para helpers de fixture de registro, manifesto, artefato público e runtime usados apenas em testes. Suítes somente do core que dependem do inventário incluído do OpenClaw permanecem em `src/plugins/contracts`. Mantenha novos testes de extensões em um subcaminho focado e documentado do SDK, como `plugin-sdk/plugin-test-api`, `plugin-sdk/channel-contract-testing`, `plugin-sdk/agent-runtime-test-contracts`, `plugin-sdk/channel-test-helpers`, `plugin-sdk/plugin-test-contracts`, `plugin-sdk/plugin-test-runtime`, `plugin-sdk/provider-test-contracts`, `plugin-sdk/provider-http-test-mocks`, `plugin-sdk/test-env` ou `plugin-sdk/test-fixtures`, em vez de importar diretamente o barrel amplo de compatibilidade `plugin-sdk/testing`, arquivos `src/**` do repositório ou pontes `test/helpers/*` do repositório.

### Tipos

Subcaminhos focados de teste também reexportam tipos úteis em arquivos de teste:

typescriptCopy code
[code]
       ChannelAccountSnapshot,  ChannelGatewayContext,} from "openclaw/plugin-sdk/channel-contract";  
[/code]

## Resolução de destino em testes

Use `installCommonResolveTargetErrorCases` para adicionar casos de erro padrão para resolução de destino de canal:

typescriptCopy code
[code]
      describe("my-channel target resolution", () => {  installCommonResolveTargetErrorCases({    resolveTarget: ({ to, mode, allowFrom }) => {      // Your channel's target resolution logic      return myChannelResolveTarget({ to, mode, allowFrom });    },    implicitAllowFrom: ["user1", "user2"],  });   // Add channel-specific test cases  it("should resolve @username targets", () => {    // ...  });});
[/code]

## Padrões de teste

### Testando contratos de registro

Testes unitários que passam um mock `api` escrito manualmente para `register(api)` não exercitam as portas de aceitação do loader do OpenClaw. Adicione pelo menos um teste de fumaça com loader para cada superfície de registro da qual seu plugin depende, especialmente hooks e capacidades exclusivas, como memória.

O loader real falha o registro do plugin quando metadados obrigatórios estão ausentes ou quando um plugin chama uma API de capacidade que ele não possui. Por exemplo, `api.registerHook(...)` exige um nome de hook, e `api.registerMemoryCapability(...)` exige que o manifesto do plugin ou a entrada exportada declare `kind: "memory"`.

### Testando acesso à configuração de runtime

Prefira o mock compartilhado de runtime de plugin de `openclaw/plugin-sdk/channel-test-helpers` ao testar plugins de canal incluídos. Os mocks obsoletos `runtime.config.loadConfig()` e `runtime.config.writeConfigFile(...)` lançam erro por padrão para que os testes capturem novos usos de APIs de compatibilidade. Sobrescreva esses mocks apenas quando o teste estiver cobrindo explicitamente comportamento legado de compatibilidade.

### Teste unitário de um plugin de canal

typescriptCopy code
[code]
     describe("my-channel plugin", () => {  it("should resolve account from config", () => {    const cfg = {      channels: {        "my-channel": {          token: "test-token",          allowFrom: ["user1"],        },      },    };     const account = myPlugin.setup.resolveAccount(cfg, undefined);    expect(account.token).toBe("test-token");  });   it("should inspect account without materializing secrets", () => {    const cfg = {      channels: {        "my-channel": { token: "test-token" },      },    };     const inspection = myPlugin.setup.inspectAccount(cfg, undefined);    expect(inspection.configured).toBe(true);    expect(inspection.tokenStatus).toBe("available");    // No token value exposed    expect(inspection).not.toHaveProperty("token");  });});
[/code]

### Teste unitário de um plugin de provedor

typescriptCopy code
[code]
     describe("my-provider plugin", () => {  it("should resolve dynamic models", () => {    const model = myProvider.resolveDynamicModel({      modelId: "custom-model-v2",      // ... context    });     expect(model.id).toBe("custom-model-v2");    expect(model.provider).toBe("my-provider");    expect(model.api).toBe("openai-completions");  });   it("should return catalog when API key is available", async () => {    const result = await myProvider.catalog.run({      resolveProviderApiKey: () => ({ apiKey: "test-key" }),      // ... context    });     expect(result?.provider?.models).toHaveLength(2);  });});
[/code]

### Fazendo mock do runtime do plugin

Para código que usa `createPluginRuntimeStore`, faça mock do runtime nos testes:

typescriptCopy code
[code]
      const store = createPluginRuntimeStore&lt;PluginRuntime&gt;({  pluginId: "test-plugin",  errorMessage: "test runtime not set",}); // In test setupconst mockRuntime = {  agent: {    resolveAgentDir: vi.fn().mockReturnValue("/tmp/agent"),    // ... other mocks  },  config: {    current: vi.fn(() => ({}) as const),    mutateConfigFile: vi.fn(),    replaceConfigFile: vi.fn(),  },  // ... other namespaces} as unknown as PluginRuntime; store.setRuntime(mockRuntime); // After testsstore.clearRuntime();
[/code]

### Testando com stubs por instância

Prefira stubs por instância em vez de mutação de prototype:

typescriptCopy code
[code]
    // Preferred: per-instance stubconst client = new MyChannelClient();client.sendMessage = vi.fn().mockResolvedValue({ id: "msg-1" }); // Avoid: prototype mutation// MyChannelClient.prototype.sendMessage = vi.fn();
[/code]

## Testes de contrato (plugins no repositório)

Plugins incluídos têm testes de contrato que verificam a propriedade do registro:

bashCopy code
[code]
    pnpm test -- src/plugins/contracts/
[/code]

Esses testes validam:

  * Quais plugins registram quais provedores
  * Quais plugins registram quais provedores de fala
  * Correção do formato de registro
  * Conformidade com o contrato de runtime


### Executando testes com escopo

Para um plugin específico:

bashCopy code
[code]
    pnpm test -- <bundled-plugin-root>/my-channel/
[/code]

Somente para testes de contrato:

bashCopy code
[code]
    pnpm test -- src/plugins/contracts/shape.contract.test.tspnpm test -- src/plugins/contracts/auth-choice.contract.test.tspnpm test -- src/plugins/contracts/runtime-seams.contract.test.ts
[/code]

## Aplicação de lint (plugins no repositório)

Três regras são aplicadas por `pnpm check` para plugins no repositório:

  1. **Sem imports monolíticos da raiz** \-- o barrel raiz `openclaw/plugin-sdk` é rejeitado
  2. **Sem imports diretos de`src/`** \-- plugins não podem importar `../../src/` diretamente
  3. **Sem autoimports** \-- plugins não podem importar seu próprio subcaminho `plugin-sdk/<name>`


Plugins externos não estão sujeitos a essas regras de lint, mas seguir os mesmos padrões é recomendado.

## Configuração de testes

OpenClaw usa Vitest com limites de cobertura V8. Para testes de plugins:

bashCopy code
[code]
    # Run all testspnpm test # Run specific plugin testspnpm test -- <bundled-plugin-root>/my-channel/src/channel.test.ts # Run with a specific test name filterpnpm test -- <bundled-plugin-root>/my-channel/ -t "resolves account" # Run with coveragepnpm test:coverage
[/code]

Se execuções locais causarem pressão de memória:

bashCopy code
[code]
    OPENCLAW_VITEST_MAX_WORKERS=1 pnpm test
[/code]

## Relacionado

  * [Visão geral do SDK](</pt-BR/plugins/sdk-overview>) \-- convenções de importação
  * [Plugins de canal do SDK](</pt-BR/plugins/sdk-channel-plugins>) \-- interface de plugin de canal
  * [Plugins de provedor do SDK](</pt-BR/plugins/sdk-provider-plugins>) \-- hooks de plugin de provedor
  * [Criando plugins](</pt-BR/plugins/building-plugins>) \-- guia de primeiros passos


Was this useful?YesNo