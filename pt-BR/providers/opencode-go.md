---
title: OpenCode Go
source_url: https://docs.openclaw.ai/pt-BR/providers/opencode-go
scraped_at: 2026-05-25
---

OpenCode Go é o catálogo Go dentro do [OpenCode](</pt-BR/providers/opencode>). Ele usa a mesma `OPENCODE_API_KEY` do catálogo Zen, mas mantém o id de provedor de runtime `opencode-go` para que o roteamento upstream por modelo permaneça correto.

Propriedade | Valor  
---|---  
Provedor de runtime | `opencode-go`  
Auth | `OPENCODE_API_KEY`  
Configuração pai | [OpenCode](</pt-BR/providers/opencode>)  
  
## Catálogo integrado

O OpenClaw obtém a maior parte das linhas do catálogo Go a partir do registro de modelos Pi empacotado e complementa linhas upstream atuais enquanto o registro é atualizado. Execute `openclaw models list --provider opencode-go` para ver a lista atual de modelos.

O provedor inclui:

Ref de modelo | Nome  
---|---  
`opencode-go/glm-5` | GLM-5  
`opencode-go/glm-5.1` | GLM-5.1  
`opencode-go/kimi-k2.5` | Kimi K2.5  
`opencode-go/kimi-k2.6` | Kimi K2.6 (limites 3x)  
`opencode-go/deepseek-v4-pro` | DeepSeek V4 Pro  
`opencode-go/deepseek-v4-flash` | DeepSeek V4 Flash  
`opencode-go/mimo-v2-omni` | MiMo V2 Omni  
`opencode-go/mimo-v2-pro` | MiMo V2 Pro  
`opencode-go/minimax-m2.5` | MiniMax M2.5  
`opencode-go/minimax-m2.7` | MiniMax M2.7  
`opencode-go/qwen3.5-plus` | Qwen3.5 Plus  
`opencode-go/qwen3.6-plus` | Qwen3.6 Plus  
  
## Primeiros passos

### Interativo

* ### Executar o onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice opencode-go
[/code]

* ### Definir um modelo Go como padrão

bashCopy code
[code]
    openclaw config set agents.defaults.model.primary "opencode-go/kimi-k2.6"
[/code]

* ### Verificar se os modelos estão disponíveis

bashCopy code
[code]
    openclaw models list --provider opencode-go
[/code]

### Não interativo

* ### Passar a chave diretamente

bashCopy code
[code]
    openclaw onboard --opencode-go-api-key "$OPENCODE_API_KEY"
[/code]

* ### Verificar se os modelos estão disponíveis

bashCopy code
[code]
    openclaw models list --provider opencode-go
[/code]

## Exemplo de configuração

json5Copy code
[code]
    {  env: { OPENCODE_API_KEY: "YOUR_API_KEY_HERE" }, // pragma: allowlist secret  agents: { defaults: { model: { primary: "opencode-go/kimi-k2.6" } } },}
[/code]

## Configuração avançada

Comportamento de roteamento

O OpenClaw cuida automaticamente do roteamento por modelo quando a ref do modelo usa `opencode-go/...`. Nenhuma configuração adicional de provedor é necessária.

Convenção de ref de runtime

As refs de runtime permanecem explícitas: `opencode/...` para Zen, `opencode-go/...` para Go. Isso mantém correto o roteamento upstream por modelo em ambos os catálogos.

Credenciais compartilhadas

A mesma `OPENCODE_API_KEY` é usada pelos catálogos Zen e Go. Informar a chave durante a configuração armazena credenciais para ambos os provedores de runtime.

## Relacionado

[**OpenCode (pai)** Onboarding compartilhado, visão geral do catálogo e observações avançadas. ](</pt-BR/providers/opencode>) [**Seleção de modelo** Como escolher provedores, refs de modelo e comportamento de failover. ](</pt-BR/concepts/model-providers>)

Was this useful?YesNo