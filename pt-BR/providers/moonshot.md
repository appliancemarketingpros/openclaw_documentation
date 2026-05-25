---
title: Moonshot AI
source_url: https://docs.openclaw.ai/pt-BR/providers/moonshot
scraped_at: 2026-05-25
---

A Moonshot fornece a API Kimi com endpoints compatíveis com OpenAI. Configure o provedor e defina o modelo padrão como `moonshot/kimi-k2.6`, ou use Kimi Coding com `kimi/kimi-for-coding`.

## Catálogo de modelos integrado

Ref do modelo | Nome | Raciocínio | Entrada | Contexto | Saída máx.  
---|---|---|---|---|---  
`moonshot/kimi-k2.6` | Kimi K2.6 | Não | texto, imagem | 262,144 | 262,144  
`moonshot/kimi-k2.5` | Kimi K2.5 | Não | texto, imagem | 262,144 | 262,144  
`moonshot/kimi-k2-thinking` | Kimi K2 Thinking | Sim | texto | 262,144 | 262,144  
`moonshot/kimi-k2-thinking-turbo` | Kimi K2 Thinking Turbo | Sim | texto | 262,144 | 262,144  
`moonshot/kimi-k2-turbo` | Kimi K2 Turbo | Não | texto | 256,000 | 16,384  
  
As estimativas de custo incluídas para os modelos K2 atuais hospedados pela Moonshot usam as tarifas publicadas de pagamento conforme o uso da Moonshot: Kimi K2.6 custa $0.16/MTok por acerto de cache, $0.95/MTok de entrada e $4.00/MTok de saída; Kimi K2.5 custa $0.10/MTok por acerto de cache, $0.60/MTok de entrada e $3.00/MTok de saída. Outras entradas legadas do catálogo mantêm placeholders de custo zero, a menos que você as substitua na configuração.

## Primeiros passos

Escolha seu provedor e siga as etapas de configuração.

### API Moonshot

**Melhor para:** modelos Kimi K2 via Moonshot Open Platform.

* ### Escolha sua região de endpoint

Opção de autenticação | Endpoint | Região  
---|---|---  
`moonshot-api-key` | `https://api.moonshot.ai/v1` | Internacional  
`moonshot-api-key-cn` | `https://api.moonshot.cn/v1` | China  
* ### Execute o onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice moonshot-api-key
[/code]

Ou para o endpoint da China:

bashCopy code
[code]
    openclaw onboard --auth-choice moonshot-api-key-cn
[/code]

* ### Defina um modelo padrão

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "moonshot/kimi-k2.6" },    },  },}
[/code]

* ### Verifique se os modelos estão disponíveis

bashCopy code
[code]
    openclaw models list --provider moonshot
[/code]

* ### Execute um teste rápido ao vivo

Use um diretório de estado isolado quando quiser verificar o acesso ao modelo e o acompanhamento de custos sem tocar nas suas sessões normais:

bashCopy code
[code]
    OPENCLAW_CONFIG_PATH=/tmp/openclaw-kimi/openclaw.json \OPENCLAW_STATE_DIR=/tmp/openclaw-kimi \openclaw agent --local \  --session-id live-kimi-cost \  --message 'Reply exactly: KIMI_LIVE_OK' \  --thinking off \  --json
[/code]

A resposta JSON deve relatar `provider: "moonshot"` e `model: "kimi-k2.6"`. A entrada de transcrição do assistente armazena o uso normalizado de tokens mais o custo estimado em `usage.cost` quando a Moonshot retorna metadados de uso.

### Exemplo de configuração

json5Copy code
[code]
    {  env: { MOONSHOT_API_KEY: "sk-..." },  agents: {    defaults: {      model: { primary: "moonshot/kimi-k2.6" },      models: {        // moonshot-kimi-k2-aliases:start        "moonshot/kimi-k2.6": { alias: "Kimi K2.6" },        "moonshot/kimi-k2.5": { alias: "Kimi K2.5" },        "moonshot/kimi-k2-thinking": { alias: "Kimi K2 Thinking" },        "moonshot/kimi-k2-thinking-turbo": { alias: "Kimi K2 Thinking Turbo" },        "moonshot/kimi-k2-turbo": { alias: "Kimi K2 Turbo" },        // moonshot-kimi-k2-aliases:end      },    },  },  models: {    mode: "merge",    providers: {      moonshot: {        baseUrl: "https://api.moonshot.ai/v1",        apiKey: "${MOONSHOT_API_KEY}",        api: "openai-completions",        models: [          // moonshot-kimi-k2-models:start          {            id: "kimi-k2.6",            name: "Kimi K2.6",            reasoning: false,            input: ["text", "image"],            cost: { input: 0.95, output: 4, cacheRead: 0.16, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 262144,          },          {            id: "kimi-k2.5",            name: "Kimi K2.5",            reasoning: false,            input: ["text", "image"],            cost: { input: 0.6, output: 3, cacheRead: 0.1, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 262144,          },          {            id: "kimi-k2-thinking",            name: "Kimi K2 Thinking",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 262144,          },          {            id: "kimi-k2-thinking-turbo",            name: "Kimi K2 Thinking Turbo",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 262144,          },          {            id: "kimi-k2-turbo",            name: "Kimi K2 Turbo",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 256000,            maxTokens: 16384,          },          // moonshot-kimi-k2-models:end        ],      },    },  },}
[/code]

### Kimi Coding

**Melhor para:** tarefas com foco em código via endpoint Kimi Coding.

* ### Execute o onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice kimi-code-api-key
[/code]

* ### Defina um modelo padrão

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "kimi/kimi-for-coding" },    },  },}
[/code]

* ### Verifique se o modelo está disponível

bashCopy code
[code]
    openclaw models list --provider kimi
[/code]

### Exemplo de configuração

json5Copy code
[code]
    {  env: { KIMI_API_KEY: "sk-..." },  agents: {    defaults: {      model: { primary: "kimi/kimi-for-coding" },      models: {        "kimi/kimi-for-coding": { alias: "Kimi" },      },    },  },}
[/code]

## Busca na web do Kimi

O OpenClaw também inclui **Kimi** como um provedor de `web_search`, apoiado pela busca na web da Moonshot.

* ### Execute a configuração interativa da busca na web

bashCopy code
[code]
    openclaw configure --section web
[/code]

Escolha **Kimi** na seção de busca na web para armazenar `plugins.entries.moonshot.config.webSearch.*`.

* ### Configure a região e o modelo da busca na web

A configuração interativa solicita:

Configuração | Opções  
---|---  
Região da API | `https://api.moonshot.ai/v1` (internacional) ou `https://api.moonshot.cn/v1` (China)  
Modelo de busca na web | O padrão é `kimi-k2.6`  
  
A configuração fica em `plugins.entries.moonshot.config.webSearch`:

json5Copy code
[code]
    {  plugins: {    entries: {      moonshot: {        config: {          webSearch: {            apiKey: "sk-...", // or use KIMI_API_KEY / MOONSHOT_API_KEY            baseUrl: "https://api.moonshot.ai/v1",            model: "kimi-k2.6",          },        },      },    },  },  tools: {    web: {      search: {        provider: "kimi",      },    },  },}
[/code]

## Configuração avançada

Modo de pensamento nativo

O Moonshot Kimi oferece suporte a pensamento nativo binário:

  * `thinking: { type: "enabled" }`
  * `thinking: { type: "disabled" }`


Configure-o por modelo via `agents.defaults.models.<provider/model>.params`:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "moonshot/kimi-k2.6": {          params: {            thinking: { type: "disabled" },          },        },      },    },  },}
[/code]

O OpenClaw também mapeia níveis de `/think` em tempo de execução para a Moonshot:

Nível de `/think` | Comportamento da Moonshot  
---|---  
`/think off` | `thinking.type=disabled`  
Qualquer nível que não seja off | `thinking.type=enabled`  
  
O Kimi K2.6 também aceita um campo opcional `thinking.keep` que controla a retenção de múltiplos turnos de `reasoning_content`. Defina-o como `"all"` para manter o raciocínio completo entre turnos; omita-o (ou deixe-o como `null`) para usar a estratégia padrão do servidor. O OpenClaw só encaminha `thinking.keep` para `moonshot/kimi-k2.6` e o remove de outros modelos.

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "moonshot/kimi-k2.6": {          params: {            thinking: { type: "enabled", keep: "all" },          },        },      },    },  },}
[/code]

Sanitização de ids de chamada de ferramenta

O Moonshot Kimi serve ids de tool_call no formato `functions.<name>:<index>`. O OpenClaw os preserva sem alterações para que chamadas de ferramenta de múltiplos turnos continuem funcionando.

Para forçar sanitização estrita em um provedor personalizado compatível com OpenAI, defina `sanitizeToolCallIds: true`:

json5Copy code
[code]
    {  models: {    providers: {      "my-kimi-proxy": {        api: "openai-completions",        sanitizeToolCallIds: true,      },    },  },}
[/code]

Compatibilidade de uso em streaming

Endpoints nativos da Moonshot (`https://api.moonshot.ai/v1` e `https://api.moonshot.cn/v1`) anunciam compatibilidade de uso em streaming no transporte compartilhado `openai-completions`. O OpenClaw baseia isso nas capacidades do endpoint, então ids de provedores personalizados compatíveis que miram os mesmos hosts nativos da Moonshot herdam o mesmo comportamento de uso em streaming.

Com o preço incluído do K2.6, o uso transmitido por streaming que inclui tokens de entrada, saída e leitura de cache também é convertido em custo local estimado em USD para `/status`, `/usage full`, `/usage cost` e contabilidade de sessão baseada em transcrição.

Referência de endpoint e referência de modelo Provedor | Prefixo da referência do modelo | Endpoint | Variável de ambiente de autenticação  
---|---|---|---  
Moonshot | `moonshot/` | `https://api.moonshot.ai/v1` | `MOONSHOT_API_KEY`  
Moonshot CN | `moonshot/` | `https://api.moonshot.cn/v1` | `MOONSHOT_API_KEY`  
Kimi Coding | `kimi/` | Endpoint do Kimi Coding | `KIMI_API_KEY`  
Busca na Web | N/A | Igual à região da API da Moonshot | `KIMI_API_KEY` ou `MOONSHOT_API_KEY`  
  
  * A busca na Web do Kimi usa `KIMI_API_KEY` ou `MOONSHOT_API_KEY`, e usa como padrão `https://api.moonshot.ai/v1` com o modelo `kimi-k2.6`.
  * Substitua os metadados de preço e contexto em `models.providers`, se necessário.
  * Se a Moonshot publicar limites de contexto diferentes para um modelo, ajuste `contextWindow` de acordo.


## Relacionados

[**Seleção de modelos** Escolhendo provedores, referências de modelo e comportamento de failover. ](</pt-BR/concepts/model-providers>) [**Busca na Web** Configurando provedores de busca na Web, incluindo Kimi. ](</pt-BR/tools/web>) [**Referência de configuração** Esquema de configuração completo para provedores, modelos e plugins. ](</pt-BR/gateway/configuration-reference>) [**Moonshot Open Platform** Gerenciamento e documentação de chaves de API da Moonshot. ](<https://platform.moonshot.ai>)

Was this useful?YesNo