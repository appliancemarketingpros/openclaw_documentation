---
title: Execução de código
source_url: https://docs.openclaw.ai/pt-BR/tools/code-execution
scraped_at: 2026-05-25
---

`code_execution` executa análise Python remota em sandbox na API Responses da xAI. Ele é registrado pelo Plugin `xai` incluído (sob o contrato `tools`) e encaminha para o mesmo endpoint `https://api.x.ai/v1/responses` usado por `x_search`.

Propriedade | Valor  
---|---  
Nome da ferramenta | `code_execution`  
Plugin provedor | `xai` (incluído, `enabledByDefault: true`)  
Autenticação | perfil de autenticação xAI, `XAI_API_KEY` ou `plugins.entries.xai.config.webSearch.apiKey`  
Modelo padrão | `grok-4-1-fast`  
Timeout padrão | 30 segundos  
`maxTurns` padrão | não definido (a xAI aplica seu próprio limite interno)  
  
Isso é diferente do [`exec`](</pt-BR/tools/exec>) local:

  * `exec` executa comandos de shell na sua máquina ou no Node pareado.
  * `code_execution` executa Python no sandbox remoto da xAI.


Use `code_execution` para:

  * Cálculos.
  * Tabulação.
  * Estatísticas rápidas.
  * Análise no estilo de gráficos.
  * Analisar dados retornados por `x_search` ou `web_search`.


**Não** use quando precisar de arquivos locais, seu shell, seu repositório ou dispositivos pareados. Use [`exec`](</pt-BR/tools/exec>) para isso.

## Configuração

* ### Forneça uma chave de API da xAI

Execute `openclaw onboard --auth-choice xai-api-key` para `code_execution` e `x_search`, ou defina `XAI_API_KEY` / configure a chave no Plugin xAI quando também quiser que a pesquisa web do Grok use a mesma credencial:

bashCopy code
[code]
    export XAI_API_KEY=xai-...
[/code]

Ou via configuração:

json5Copy code
[code]
    {  plugins: {    entries: {      xai: {        config: {          webSearch: {            apiKey: "xai-...",          },        },      },    },  },}
[/code]

* ### Habilite e ajuste code_execution

A ferramenta é controlada por `plugins.entries.xai.config.codeExecution.enabled`. O padrão é desativado.

json5Copy code
[code]
    {  plugins: {    entries: {      xai: {        config: {          codeExecution: {            enabled: true,            model: "grok-4-1-fast", // override the default xAI code-execution model            maxTurns: 2,            // optional cap on internal tool turns            timeoutSeconds: 30,     // request timeout (default: 30)          },        },      },    },  },}
[/code]

* ### Reinicie o Gateway

bashCopy code
[code]
    openclaw gateway restart
[/code]

`code_execution` aparece na lista de ferramentas do agente quando o Plugin xAI se registra novamente com `enabled: true`.

## Como usar

Peça naturalmente e deixe explícita a intenção da análise:

textCopy code
[code]
    Use code_execution to calculate the 7-day moving average for these numbers: ...
[/code]

textCopy code
[code]
    Use x_search to find posts mentioning OpenClaw this week, then use code_execution to count them by day.
[/code]

textCopy code
[code]
    Use web_search to gather the latest AI benchmark numbers, then use code_execution to compare percent changes.
[/code]

A ferramenta usa internamente um único parâmetro `task`, portanto o agente deve enviar a solicitação de análise completa e quaisquer dados inline em um único prompt.

## Erros

Quando a ferramenta é executada sem autenticação, ela retorna um erro estruturado `missing_xai_api_key` apontando para as opções de perfil de autenticação, variável de ambiente e configuração. O erro é JSON, não uma exceção lançada, portanto o agente pode se autocorrigir:

jsonCopy code
[code]
    {  "error": "missing_xai_api_key",  "message": "code_execution needs an xAI API key. Run openclaw onboard --auth-choice xai-api-key, set XAI_API_KEY in the Gateway environment, or configure plugins.entries.xai.config.webSearch.apiKey.",  "docs": "https://docs.openclaw.ai/tools/code-execution"}
[/code]

## Limites

  * Isso é execução remota da xAI, não execução de processo local.
  * Trate os resultados como análise efêmera, não como uma sessão persistente de notebook.
  * Não assuma acesso a arquivos locais ou ao seu espaço de trabalho.
  * Para dados X recentes, use [`x_search`](</pt-BR/tools/web#x_search>) primeiro e encaminhe o resultado para `code_execution`.


## Relacionados

[**Ferramenta Exec** Execução de shell local na sua máquina ou no Node pareado. ](</pt-BR/tools/exec>) [**Aprovações de exec** Política de permitir/negar para execução de shell. ](</pt-BR/tools/exec-approvals>) [**Ferramentas web** `web_search`, `x_search` e `web_fetch`. ](</pt-BR/tools/web>) [**Provedor xAI** Modelos Grok, pesquisa web/X e configuração de execução de código. ](</pt-BR/providers/xai>)

Was this useful?YesNo