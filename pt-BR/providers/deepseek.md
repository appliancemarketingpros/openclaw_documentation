---
title: DeepSeek
source_url: https://docs.openclaw.ai/pt-BR/providers/deepseek
scraped_at: 2026-05-25
---

[DeepSeek](<https://www.deepseek.com>) fornece modelos de IA poderosos com uma API compatível com OpenAI.

Propriedade | Valor  
---|---  
Provedor | `deepseek`  
Autenticação | `DEEPSEEK_API_KEY`  
API | compatível com OpenAI  
URL base | `https://api.deepseek.com`  
  
## Primeiros passos

* ### Obtenha sua chave de API

Crie uma chave de API em [platform.deepseek.com](<https://platform.deepseek.com/api_keys>).

* ### Execute o onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice deepseek-api-key
[/code]

Isso solicitará sua chave de API e definirá `deepseek/deepseek-v4-flash` como o modelo padrão.

* ### Verifique se os modelos estão disponíveis

bashCopy code
[code]
    openclaw models list --provider deepseek
[/code]

Para inspecionar o catálogo estático incluído sem exigir um Gateway em execução, use:

bashCopy code
[code]
    openclaw models list --all --provider deepseek
[/code]

Configuração não interativa

Para instalações com script ou sem interface, passe todas as flags diretamente:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice deepseek-api-key \  --deepseek-api-key "$DEEPSEEK_API_KEY" \  --skip-health \  --accept-risk
[/code]

## Catálogo integrado

Ref. do modelo | Nome | Entrada | Contexto | Saída máxima | Observações  
---|---|---|---|---|---  
`deepseek/deepseek-v4-flash` | DeepSeek V4 Flash | texto | 1.000.000 | 384.000 | Modelo padrão; superfície V4 compatível com thinking  
`deepseek/deepseek-v4-pro` | DeepSeek V4 Pro | texto | 1.000.000 | 384.000 | Superfície V4 compatível com thinking  
`deepseek/deepseek-chat` | DeepSeek Chat | texto | 131.072 | 8.192 | Superfície DeepSeek V3.2 sem thinking  
`deepseek/deepseek-reasoner` | DeepSeek Reasoner | texto | 131.072 | 65.536 | Superfície V3.2 com reasoning habilitado  
  
## Thinking e ferramentas

Sessões de thinking do DeepSeek V4 têm um contrato de reprodução mais rigoroso do que a maioria dos provedores compatíveis com OpenAI: depois que um turno com thinking habilitado usa ferramentas, o DeepSeek espera que as mensagens de assistente reproduzidas desse turno incluam `reasoning_content` nas solicitações de acompanhamento. O OpenClaw lida com isso dentro do plugin DeepSeek, então o uso normal de ferramentas em múltiplos turnos funciona com `deepseek/deepseek-v4-flash` e `deepseek/deepseek-v4-pro`.

Se você alternar uma sessão existente de outro provedor compatível com OpenAI para um modelo DeepSeek V4, turnos antigos de chamadas de ferramentas do assistente podem não ter `reasoning_content` nativo do DeepSeek. O OpenClaw preenche esse campo ausente em mensagens de assistente reproduzidas para solicitações de thinking do DeepSeek V4, para que o provedor possa aceitar o histórico sem exigir `/new`.

Quando o thinking está desativado no OpenClaw (incluindo a seleção **None** na UI), o OpenClaw envia ao DeepSeek `thinking: { type: "disabled" }` e remove o `reasoning_content` reproduzido do histórico de saída. Isso mantém as sessões com thinking desativado no caminho sem thinking do DeepSeek.

Use `deepseek/deepseek-v4-flash` para o caminho rápido padrão. Use `deepseek/deepseek-v4-pro` quando quiser o modelo V4 mais forte e puder aceitar custo ou latência maiores.

## Testes ao vivo

A suíte direta de modelos ao vivo inclui o DeepSeek V4 no conjunto moderno de modelos. Para executar apenas as verificações diretas de modelos DeepSeek V4:

bashCopy code
[code]
    OPENCLAW_LIVE_PROVIDERS=deepseek \OPENCLAW_LIVE_MODELS="deepseek/deepseek-v4-flash,deepseek/deepseek-v4-pro" \pnpm test:live src/agents/models.profiles.live.test.ts
[/code]

Essa verificação ao vivo confirma que ambos os modelos V4 conseguem concluir e que os turnos de acompanhamento com thinking/ferramentas preservam a carga de reprodução exigida pelo DeepSeek.

## Exemplo de configuração

json5Copy code
[code]
    {  env: { DEEPSEEK_API_KEY: "sk-..." },  agents: {    defaults: {      model: { primary: "deepseek/deepseek-v4-flash" },    },  },}
[/code]

## Relacionados

[**Seleção de modelos** Escolha de provedores, refs. de modelo e comportamento de failover. ](</pt-BR/concepts/model-providers>) [**Referência de configuração** Referência completa de configuração para agentes, modelos e provedores. ](</pt-BR/gateway/configuration-reference>)

Was this useful?YesNo