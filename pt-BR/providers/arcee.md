---
title: Arcee AI
source_url: https://docs.openclaw.ai/pt-BR/providers/arcee
scraped_at: 2026-05-25
---

[Arcee AI](<https://arcee.ai>) fornece acesso à família Trinity de modelos mixture-of-experts por meio de uma API compatível com OpenAI. Todos os modelos Trinity são licenciados sob Apache 2.0.

Os modelos da Arcee AI podem ser acessados diretamente pela plataforma Arcee ou por meio do [OpenRouter](</pt-BR/providers/openrouter>).

Propriedade | Valor  
---|---  
Provedor | `arcee`  
Autenticação | `ARCEEAI_API_KEY` (direto) ou `OPENROUTER_API_KEY` (via OpenRouter)  
API | Compatível com OpenAI  
URL base | `https://api.arcee.ai/api/v1` (direto) ou `https://openrouter.ai/api/v1` (OpenRouter)  
  
## Primeiros passos

### Direto (plataforma Arcee)

* ### Obtenha uma chave de API

Crie uma chave de API em [Arcee AI](<https://chat.arcee.ai/>).

* ### Execute a integração inicial

bashCopy code
[code]
    openclaw onboard --auth-choice arceeai-api-key
[/code]

* ### Defina um modelo padrão

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "arcee/trinity-large-thinking" },    },  },}
[/code]

### Via OpenRouter

* ### Obtenha uma chave de API

Crie uma chave de API em [OpenRouter](<https://openrouter.ai/keys>).

* ### Execute a integração inicial

bashCopy code
[code]
    openclaw onboard --auth-choice arceeai-openrouter
[/code]

* ### Defina um modelo padrão

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "arcee/trinity-large-thinking" },    },  },}
[/code]

As mesmas refs de modelo funcionam tanto para configurações diretas quanto via OpenRouter (por exemplo, `arcee/trinity-large-thinking`).

## Configuração não interativa

### Direto (plataforma Arcee)

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice arceeai-api-key \  --arceeai-api-key "$ARCEEAI_API_KEY"
[/code]

### Via OpenRouter

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice arceeai-openrouter \  --openrouter-api-key "$OPENROUTER_API_KEY"
[/code]

## Catálogo integrado

Atualmente, o OpenClaw inclui este catálogo Arcee bundled:

Ref do modelo | Nome | Entrada | Contexto | Custo (entrada/saída por 1M) | Observações  
---|---|---|---|---|---  
`arcee/trinity-large-thinking` | Trinity Large Thinking | texto | 256K | $0.25 / $0.90 | Modelo padrão; raciocínio habilitado  
`arcee/trinity-large-preview` | Trinity Large Preview | texto | 128K | $0.25 / $1.00 | Uso geral; 400B parâmetros, 13B ativos  
`arcee/trinity-mini` | Trinity Mini 26B | texto | 128K | $0.045 / $0.15 | Rápido e econômico; chamada de funções  
  
## Recursos compatíveis

Recurso | Compatível  
---|---  
Streaming | Sim  
Uso de ferramentas / chamada de funções | Sim (Trinity Mini, Trinity Large Preview)  
Saída estruturada (modo JSON e esquema JSON) | Sim  
Extended thinking | Sim (Trinity Large Thinking; ferramentas desabilitadas)  
  
Observação sobre o ambiente

Se o Gateway for executado como daemon (launchd/systemd), certifique-se de que `ARCEEAI_API_KEY` (ou `OPENROUTER_API_KEY`) esteja disponível para esse processo (por exemplo, em `~/.openclaw/.env` ou via `env.shellEnv`).

Roteamento do OpenRouter

Ao usar modelos Arcee via OpenRouter, aplicam-se as mesmas refs de modelo `arcee/*`. O OpenClaw gerencia o roteamento de forma transparente com base na sua escolha de autenticação. Consulte a [documentação do provedor OpenRouter](</pt-BR/providers/openrouter>) para detalhes de configuração específicos do OpenRouter.

## Relacionados

[**OpenRouter** Acesse modelos Arcee e muitos outros por meio de uma única chave de API. ](</pt-BR/providers/openrouter>) [**Seleção de modelo** Escolha de provedores, refs de modelo e comportamento de failover. ](</pt-BR/concepts/model-providers>)

Was this useful?YesNo