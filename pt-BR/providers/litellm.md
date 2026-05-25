---
title: LiteLLM
source_url: https://docs.openclaw.ai/pt-BR/providers/litellm
scraped_at: 2026-05-25
---

[LiteLLM](<https://litellm.ai>) é um gateway de LLM de código aberto que fornece uma API unificada para mais de 100 provedores de modelos. Encaminhe o OpenClaw pelo LiteLLM para obter rastreamento centralizado de custos, logs e a flexibilidade de trocar backends sem alterar sua configuração do OpenClaw.

## Início rápido

### Onboarding (recomendado)

**Ideal para:** o caminho mais rápido para uma configuração funcional do LiteLLM.

* ### Execute o onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice litellm-api-key
[/code]

Para configuração não interativa com um proxy remoto, passe explicitamente a URL do proxy:

bashCopy code
[code]
    openclaw onboard --non-interactive --auth-choice litellm-api-key --litellm-api-key "$LITELLM_API_KEY" --custom-base-url "https://litellm.example/v1"
[/code]

### Configuração manual

**Ideal para:** controle total sobre instalação e configuração.

* ### Inicie o proxy do LiteLLM

bashCopy code
[code]
    pip install 'litellm[proxy]'litellm --model claude-opus-4-6
[/code]

* ### Aponte o OpenClaw para o LiteLLM

bashCopy code
[code]
    export LITELLM_API_KEY="your-litellm-key" openclaw
[/code]

Pronto. Agora o OpenClaw roteia pelo LiteLLM.

## Configuração

### Variáveis de ambiente

bashCopy code
[code]
    export LITELLM_API_KEY="sk-litellm-key"
[/code]

### Arquivo de configuração

json5Copy code
[code]
    {  models: {    providers: {      litellm: {        baseUrl: "http://localhost:4000",        apiKey: "${LITELLM_API_KEY}",        api: "openai-completions",        models: [          {            id: "claude-opus-4-6",            name: "Claude Opus 4.6",            reasoning: true,            input: ["text", "image"],            contextWindow: 200000,            maxTokens: 64000,          },          {            id: "gpt-4o",            name: "GPT-4o",            reasoning: false,            input: ["text", "image"],            contextWindow: 128000,            maxTokens: 8192,          },        ],      },    },  },  agents: {    defaults: {      model: { primary: "litellm/claude-opus-4-6" },    },  },}
[/code]

## Configuração avançada

### Geração de imagens

O LiteLLM também pode dar suporte à ferramenta `image_generate` por meio de rotas `/images/generations` e `/images/edits` compatíveis com OpenAI. Configure um modelo de imagem do LiteLLM em `agents.defaults.imageGenerationModel`:

json5Copy code
[code]
    {  models: {    providers: {      litellm: {        baseUrl: "http://localhost:4000",        apiKey: "${LITELLM_API_KEY}",      },    },  },  agents: {    defaults: {      imageGenerationModel: {        primary: "litellm/gpt-image-2",        timeoutMs: 180_000,      },    },  },}
[/code]

URLs de local loopback do LiteLLM, como `http://localhost:4000`, funcionam sem uma substituição global de rede privada. Para um proxy hospedado em LAN, defina `models.providers.litellm.request.allowPrivateNetwork: true` porque a chave de API será enviada ao host de proxy configurado.

Chaves virtuais

Crie uma chave dedicada para o OpenClaw com limites de gasto:

bashCopy code
[code]
    curl -X POST "http://localhost:4000/key/generate" \  -H "Authorization: Bearer $LITELLM_MASTER_KEY" \  -H "Content-Type: application/json" \  -d '{    "key_alias": "openclaw",    "max_budget": 50.00,    "budget_duration": "monthly"  }'
[/code]

Use a chave gerada como `LITELLM_API_KEY`.

Roteamento de modelos

O LiteLLM pode rotear solicitações de modelos para diferentes backends. Configure no seu `config.yaml` do LiteLLM:

yamlCopy code
[code]
    model_list:  - model_name: claude-opus-4-6    litellm_params:      model: claude-opus-4-6      api_key: os.environ/ANTHROPIC_API_KEY   - model_name: gpt-4o    litellm_params:      model: gpt-4o      api_key: os.environ/OPENAI_API_KEY
[/code]

O OpenClaw continua solicitando `claude-opus-4-6` — o LiteLLM cuida do roteamento.

Visualização de uso

Verifique o painel ou a API do LiteLLM:

bashCopy code
[code]
    # Key infocurl "http://localhost:4000/key/info" \  -H "Authorization: Bearer sk-litellm-key" # Spend logscurl "http://localhost:4000/spend/logs" \  -H "Authorization: Bearer $LITELLM_MASTER_KEY"
[/code]

Observações sobre o comportamento do proxy

  * O LiteLLM é executado em `http://localhost:4000` por padrão
  * O OpenClaw se conecta pelo endpoint `/v1` compatível com OpenAI em estilo de proxy do LiteLLM
  * A modelagem de solicitações nativa somente para OpenAI não se aplica pelo LiteLLM: sem `service_tier`, sem `store` de Responses, sem dicas de cache de prompt e sem modelagem de payload de compatibilidade de raciocínio da OpenAI
  * Cabeçalhos ocultos de atribuição do OpenClaw (`originator`, `version`, `User-Agent`) não são injetados em URLs base personalizadas do LiteLLM


## Relacionados

[**Documentação do LiteLLM** Documentação oficial do LiteLLM e referência da API. ](<https://docs.litellm.ai>) [**Seleção de modelos** Visão geral de todos os provedores, referências de modelos e comportamento de failover. ](</pt-BR/concepts/model-providers>) [**Configuração** Referência completa de configuração. ](</pt-BR/gateway/configuration>) [**Seleção de modelos** Como escolher e configurar modelos. ](</pt-BR/concepts/models>)

Was this useful?YesNo