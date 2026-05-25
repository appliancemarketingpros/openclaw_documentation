---
title: Kilo Gateway
source_url: https://docs.openclaw.ai/pt-BR/providers/kilocode
scraped_at: 2026-05-25
---

Kilo Gateway fornece uma **API unificada** que roteia solicitações para muitos modelos por trás de um único endpoint e chave de API. Ela é compatível com OpenAI, então a maioria dos SDKs da OpenAI funciona ao trocar a URL base.

Propriedade | Valor  
---|---  
Provedor | `kilocode`  
Autenticação | `KILOCODE_API_KEY`  
API | Compatível com OpenAI  
URL base | `https://api.kilo.ai/api/gateway/`  
  
## Primeiros passos

* ### Crie uma conta

Acesse [app.kilo.ai](<https://app.kilo.ai>), entre ou crie uma conta, depois navegue até Chaves de API e gere uma nova chave.

* ### Execute o onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice kilocode-api-key
[/code]

Ou defina a variável de ambiente diretamente:

bashCopy code
[code]
    export KILOCODE_API_KEY="<your-kilocode-api-key>" # pragma: allowlist secret
[/code]

* ### Verifique se o modelo está disponível

bashCopy code
[code]
    openclaw models list --provider kilocode
[/code]

## Modelo padrão

O modelo padrão é `kilocode/kilo/auto`, um modelo de roteamento inteligente pertencente ao provedor e gerenciado pelo Kilo Gateway.

## Catálogo integrado

O OpenClaw descobre dinamicamente os modelos disponíveis no Kilo Gateway na inicialização. Use `/models kilocode` para ver a lista completa de modelos disponíveis com sua conta.

Qualquer modelo disponível no Gateway pode ser usado com o prefixo `kilocode/`:

Referência do modelo | Observações  
---|---  
`kilocode/kilo/auto` | Padrão — roteamento inteligente  
`kilocode/anthropic/claude-sonnet-4` | Anthropic via Kilo  
`kilocode/openai/gpt-5.5` | OpenAI via Kilo  
`kilocode/google/gemini-3.1-pro-preview` | Google via Kilo  
...e muitos outros | Use `/models kilocode` para listar todos  
  
## Exemplo de configuração

json5Copy code
[code]
    {  env: { KILOCODE_API_KEY: "<your-kilocode-api-key>" }, // pragma: allowlist secret  agents: {    defaults: {      model: { primary: "kilocode/kilo/auto" },    },  },}
[/code]

Transporte e compatibilidade

O Kilo Gateway é documentado no código-fonte como compatível com OpenRouter, então ele permanece no caminho compatível com OpenAI em estilo de proxy, em vez de usar formatação nativa de solicitações da OpenAI.

  * Referências Kilo baseadas em Gemini permanecem no caminho proxy-Gemini, então o OpenClaw mantém a sanitização de assinaturas de pensamento do Gemini ali sem habilitar a validação nativa de replay do Gemini nem reescritas de bootstrap.
  * O Kilo Gateway usa um token Bearer com sua chave de API internamente.

Wrapper de stream e raciocínio

O wrapper de stream compartilhado do Kilo adiciona o cabeçalho do app do provedor e normaliza payloads de raciocínio de proxy para referências de modelos concretos compatíveis.

Solução de problemas

  * Se a descoberta de modelos falhar na inicialização, o OpenClaw recorre ao catálogo estático incluído que contém `kilocode/kilo/auto`.
  * Confirme se sua chave de API é válida e se sua conta Kilo tem os modelos desejados habilitados.
  * Quando o Gateway roda como daemon, garanta que `KILOCODE_API_KEY` esteja disponível para esse processo (por exemplo, em `~/.openclaw/.env` ou via `env.shellEnv`).


## Relacionados

[**Seleção de modelos** Escolha de provedores, referências de modelo e comportamento de failover. ](</pt-BR/concepts/model-providers>) [**Referência de configuração** Referência completa de configuração do OpenClaw. ](</pt-BR/gateway/configuration-reference>) [**Kilo Gateway** Painel do Kilo Gateway, chaves de API e gerenciamento da conta. ](<https://app.kilo.ai>)

Was this useful?YesNo