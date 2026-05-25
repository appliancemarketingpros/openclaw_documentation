---
title: Qianfan
source_url: https://docs.openclaw.ai/pt-BR/providers/qianfan
scraped_at: 2026-05-25
---

Qianfan é a plataforma MaaS da Baidu, fornecendo uma **API unificada** que encaminha solicitações para muitos modelos por trás de um único endpoint e chave de API. Ela é compatível com OpenAI, então a maioria dos SDKs da OpenAI funciona ao trocar a URL base.

Propriedade | Valor  
---|---  
Provedor | `qianfan`  
Autenticação | `QIANFAN_API_KEY`  
API | Compatível com OpenAI  
URL base | `https://qianfan.baidubce.com/v2`  
  
## Primeiros passos

* ### Criar uma conta da Baidu Cloud

Cadastre-se ou faça login no [Console do Qianfan](<https://console.bce.baidu.com/qianfan/ais/console/apiKey>) e verifique se você tem o acesso à API do Qianfan habilitado.

* ### Gerar uma chave de API

Crie uma nova aplicação ou selecione uma existente e, em seguida, gere uma chave de API. O formato da chave é `bce-v3/ALTAK-...`.

* ### Executar a integração

bashCopy code
[code]
    openclaw onboard --auth-choice qianfan-api-key
[/code]

* ### Verificar se o modelo está disponível

bashCopy code
[code]
    openclaw models list --provider qianfan
[/code]

## Catálogo integrado

Ref do modelo | Entrada | Contexto | Saída máxima | Raciocínio | Observações  
---|---|---|---|---|---  
`qianfan/deepseek-v3.2` | texto | 98,304 | 32,768 | Sim | Modelo padrão  
`qianfan/ernie-5.0-thinking-preview` | texto, imagem | 119,000 | 64,000 | Sim | Multimodal  
  
## Exemplo de configuração

json5Copy code
[code]
    {  env: { QIANFAN_API_KEY: "bce-v3/ALTAK-..." },  agents: {    defaults: {      model: { primary: "qianfan/deepseek-v3.2" },      models: {        "qianfan/deepseek-v3.2": { alias: "QIANFAN" },      },    },  },  models: {    providers: {      qianfan: {        baseUrl: "https://qianfan.baidubce.com/v2",        api: "openai-completions",        models: [          {            id: "deepseek-v3.2",            name: "DEEPSEEK V3.2",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 98304,            maxTokens: 32768,          },          {            id: "ernie-5.0-thinking-preview",            name: "ERNIE-5.0-Thinking-Preview",            reasoning: true,            input: ["text", "image"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 119000,            maxTokens: 64000,          },        ],      },    },  },}
[/code]

Transporte e compatibilidade

O Qianfan é executado pelo caminho de transporte compatível com OpenAI, não pela formatação nativa de solicitações da OpenAI. Isso significa que os recursos padrão dos SDKs da OpenAI funcionam, mas parâmetros específicos do provedor podem não ser encaminhados.

Catálogo e substituições

No momento, o catálogo incluído inclui `deepseek-v3.2` e `ernie-5.0-thinking-preview`. Adicione ou substitua `models.providers.qianfan` somente quando precisar de uma URL base personalizada ou metadados de modelo.

Solução de problemas

  * Verifique se sua chave de API começa com `bce-v3/ALTAK-` e se tem acesso à API do Qianfan habilitado no console da Baidu Cloud.
  * Se os modelos não estiverem listados, confirme que sua conta tem o serviço Qianfan ativado.
  * A URL base padrão é `https://qianfan.baidubce.com/v2`. Altere-a somente se você usar um endpoint ou proxy personalizado.


## Relacionado

[**Seleção de modelo** Escolha de provedores, refs de modelo e comportamento de failover. ](</pt-BR/concepts/model-providers>) [**Referência de configuração** Referência completa de configuração do OpenClaw. ](</pt-BR/gateway/configuration-reference>) [**Configuração do agente** Configuração de padrões de agente e atribuições de modelo. ](</pt-BR/concepts/agent>) [**Documentação da API do Qianfan** Documentação oficial da API do Qianfan. ](<https://cloud.baidu.com/doc/qianfan-api/s/3m7of64lb>)

Was this useful?YesNo