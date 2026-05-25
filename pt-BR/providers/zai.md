---
title: Z.AI
source_url: https://docs.openclaw.ai/pt-BR/providers/zai
scraped_at: 2026-05-25
---

[Z.AI](<http://Z.AI>) é a plataforma de API para modelos **GLM**. Ela fornece APIs REST para GLM e usa chaves de API para autenticação. Crie sua chave de API no console da [Z.AI](<http://Z.AI>). OpenClaw usa o provedor `zai` com uma chave de API da [Z.AI](<http://Z.AI>).

  * Provedor: `zai`
  * Autenticação: `ZAI_API_KEY`
  * API: [Z.AI](<http://Z.AI>) Chat Completions (autenticação Bearer)


## Primeiros passos

### Detectar endpoint automaticamente

**Ideal para:** a maioria dos usuários. OpenClaw detecta o endpoint [Z.AI](<http://Z.AI>) correspondente a partir da chave e aplica a URL base correta automaticamente.

* ### Execute o onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice zai-api-key
[/code]

* ### Defina um modelo padrão

json5Copy code
[code]
    {  env: { ZAI_API_KEY: "sk-..." },  agents: { defaults: { model: { primary: "zai/glm-5.1" } } },}
[/code]

* ### Verifique se o modelo está listado

bashCopy code
[code]
    openclaw models list --all --provider zai
[/code]

### Endpoint regional explícito

**Ideal para:** usuários que desejam forçar um Coding Plan específico ou uma superfície geral de API.

* ### Escolha a opção de onboarding correta

bashCopy code
[code]
    # Coding Plan Global (recommended for Coding Plan users)openclaw onboard --auth-choice zai-coding-global # Coding Plan CN (China region)openclaw onboard --auth-choice zai-coding-cn # General APIopenclaw onboard --auth-choice zai-global # General API CN (China region)openclaw onboard --auth-choice zai-cn
[/code]

* ### Defina um modelo padrão

json5Copy code
[code]
    {  env: { ZAI_API_KEY: "sk-..." },  agents: { defaults: { model: { primary: "zai/glm-5.1" } } },}
[/code]

* ### Verifique se o modelo está listado

bashCopy code
[code]
    openclaw models list --all --provider zai
[/code]

## Catálogo integrado

OpenClaw inclui o catálogo do provedor `zai` empacotado no manifesto do Plugin, para que a listagem somente leitura possa mostrar linhas GLM conhecidas sem carregar o runtime do provedor:

bashCopy code
[code]
    openclaw models list --all --provider zai
[/code]

O catálogo baseado no manifesto atualmente inclui:

Referência do modelo | Observações  
---|---  
`zai/glm-5.1` | Modelo padrão  
`zai/glm-5` |   
`zai/glm-5-turbo` |   
`zai/glm-5v-turbo` |   
`zai/glm-4.7` |   
`zai/glm-4.7-flash` |   
`zai/glm-4.7-flashx` |   
`zai/glm-4.6` |   
`zai/glm-4.6v` |   
`zai/glm-4.5` |   
`zai/glm-4.5-air` |   
`zai/glm-4.5-flash` |   
`zai/glm-4.5v` |   
  
## Configuração avançada

Resolução futura de modelos GLM-5 desconhecidos

IDs `glm-5*` desconhecidos ainda são resolvidos futuramente no caminho do provedor empacotado ao sintetizar metadados pertencentes ao provedor a partir do modelo `glm-4.7` quando o ID corresponde ao formato atual da família GLM-5.

Streaming de chamadas de ferramenta

`tool_stream` é habilitado por padrão para streaming de chamadas de ferramenta da [Z.AI](<http://Z.AI>). Para desabilitá-lo:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "zai/<model>": {          params: { tool_stream: false },        },      },    },  },}
[/code]

Thinking e thinking preservado

O thinking da [Z.AI](<http://Z.AI>) segue os controles `/think` do OpenClaw. Com thinking desativado, OpenClaw envia `thinking: { type: "disabled" }` para evitar respostas que gastem o orçamento de saída em `reasoning_content` antes do texto visível.

O thinking preservado é opcional porque a [Z.AI](<http://Z.AI>) exige que todo o histórico de `reasoning_content` seja repetido, o que aumenta os tokens do prompt. Habilite-o por modelo:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "zai/glm-5.1": {          params: { preserveThinking: true },        },      },    },  },}
[/code]

Quando habilitado e o thinking está ativo, OpenClaw envia `thinking: { type: "enabled", clear_thinking: false }` e repete o `reasoning_content` anterior para a mesma transcrição compatível com OpenAI.

Usuários avançados ainda podem substituir o payload exato do provedor com `params.extra_body.thinking`.

Compreensão de imagens

O Plugin [Z.AI](<http://Z.AI>) empacotado registra compreensão de imagens.

Propriedade | Valor  
---|---  
Modelo | `glm-4.6v`  
  
A compreensão de imagens é resolvida automaticamente a partir da autenticação [Z.AI](<http://Z.AI>) configurada, sem necessidade de configuração adicional.

Detalhes de autenticação

  * [Z.AI](<http://Z.AI>) usa autenticação Bearer com sua chave de API.
  * A opção de onboarding `zai-api-key` detecta automaticamente o endpoint [Z.AI](<http://Z.AI>) correspondente a partir do prefixo da chave.
  * Use as opções regionais explícitas (`zai-coding-global`, `zai-coding-cn`, `zai-global`, `zai-cn`) quando quiser forçar uma superfície de API específica.


## Relacionado

[**Família de modelos GLM** Visão geral da família de modelos GLM. ](</pt-BR/providers/glm>) [**Seleção de modelo** Como escolher provedores, referências de modelo e comportamento de failover. ](</pt-BR/concepts/model-providers>)

Was this useful?YesNo