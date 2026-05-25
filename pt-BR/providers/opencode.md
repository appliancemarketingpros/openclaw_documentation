---
title: OpenCode
source_url: https://docs.openclaw.ai/pt-BR/providers/opencode
scraped_at: 2026-05-25
---

O OpenCode expõe dois catálogos hospedados no OpenClaw:

Catálogo | Prefixo | Provedor de runtime  
---|---|---  
**Zen** | `opencode/...` | `opencode`  
**Go** | `opencode-go/...` | `opencode-go`  
  
Ambos os catálogos usam a mesma chave de API do OpenCode. O OpenClaw mantém os ids de provedor de runtime separados para que o roteamento upstream por modelo permaneça correto, mas onboarding e documentação tratam isso como uma única configuração do OpenCode.

## Primeiros passos

### Catálogo Zen

**Ideal para:** o proxy multimodelo curado do OpenCode (Claude, GPT, Gemini).

* ### Execute o onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice opencode-zen
[/code]

Ou passe a chave diretamente:

bashCopy code
[code]
    openclaw onboard --opencode-zen-api-key "$OPENCODE_API_KEY"
[/code]

* ### Defina um modelo Zen como padrão

bashCopy code
[code]
    openclaw config set agents.defaults.model.primary "opencode/claude-opus-4-6"
[/code]

* ### Verifique se os modelos estão disponíveis

bashCopy code
[code]
    openclaw models list --provider opencode
[/code]

### Catálogo Go

**Ideal para:** a linha de modelos Kimi, GLM e MiniMax hospedada pelo OpenCode.

* ### Execute o onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice opencode-go
[/code]

Ou passe a chave diretamente:

bashCopy code
[code]
    openclaw onboard --opencode-go-api-key "$OPENCODE_API_KEY"
[/code]

* ### Defina um modelo Go como padrão

bashCopy code
[code]
    openclaw config set agents.defaults.model.primary "opencode-go/kimi-k2.6"
[/code]

* ### Verifique se os modelos estão disponíveis

bashCopy code
[code]
    openclaw models list --provider opencode-go
[/code]

## Exemplo de configuração

json5Copy code
[code]
    {  env: { OPENCODE_API_KEY: "sk-..." },  agents: { defaults: { model: { primary: "opencode/claude-opus-4-6" } } },}
[/code]

## Catálogos incluídos

### Zen

Propriedade | Valor  
---|---  
Provedor de runtime | `opencode`  
Modelos de exemplo | `opencode/claude-opus-4-6`, `opencode/gpt-5.5`, `opencode/gemini-3-pro`  
  
### Go

Propriedade | Valor  
---|---  
Provedor de runtime | `opencode-go`  
Modelos de exemplo | `opencode-go/kimi-k2.6`, `opencode-go/glm-5`, `opencode-go/minimax-m2.5`  
  
## Configuração avançada

Aliases de chave de API

`OPENCODE_ZEN_API_KEY` também é compatível como alias de `OPENCODE_API_KEY`.

Credenciais compartilhadas

Informar uma chave OpenCode durante o setup armazena credenciais para ambos os provedores de runtime. Você não precisa fazer onboarding de cada catálogo separadamente.

Cobrança e painel

Você entra no OpenCode, adiciona detalhes de cobrança e copia sua chave de API. A cobrança e a disponibilidade do catálogo são gerenciadas pelo painel do OpenCode.

Comportamento de replay do Gemini

Refs do OpenCode com base em Gemini permanecem no caminho proxy-Gemini, então o OpenClaw mantém ali a sanitização de assinatura de pensamento do Gemini sem habilitar validação de replay nativo do Gemini nem reescritas de bootstrap.

Comportamento de replay não Gemini

Refs do OpenCode não Gemini mantêm a política mínima de replay compatível com OpenAI.

## Relacionado

[**Seleção de modelo** Escolhendo provedores, model refs e comportamento de failover. ](</pt-BR/concepts/model-providers>) [**Referência de configuração** Referência completa de configuração para agentes, modelos e provedores. ](</pt-BR/gateway/configuration-reference>)

Was this useful?YesNo