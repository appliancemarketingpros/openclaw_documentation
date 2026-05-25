---
title: Infere
source_url: https://docs.openclaw.ai/pt-BR/providers/inferrs
scraped_at: 2026-05-25
---

[inferrs](<https://github.com/ericcurtin/inferrs>) pode servir modelos locais por trás de uma API `/v1` compatível com OpenAI. O OpenClaw funciona com `inferrs` pelo caminho genérico `openai-completions`.

Propriedade | Valor  
---|---  
ID do provedor | `inferrs` (personalizado; configure em `models.providers.inferrs`)  
Plugin | nenhum — `inferrs` não é um plugin de provedor OpenClaw incluído  
Var. env de auth | Opcional. Qualquer valor funciona se o seu servidor inferrs não tiver auth  
API | compatível com OpenAI (`openai-completions`)  
URL base sugerida | `http://127.0.0.1:8080/v1` (ou onde quer que seu servidor inferrs esteja)  
  
## Primeiros passos

* ### Start inferrs with a model

bashCopy code
[code]
    inferrs serve google/gemma-4-E2B-it \  --host 127.0.0.1 \  --port 8080 \  --device metal
[/code]

* ### Verify the server is reachable

bashCopy code
[code]
    curl http://127.0.0.1:8080/healthcurl http://127.0.0.1:8080/v1/models
[/code]

* ### Add an OpenClaw provider entry

Adicione uma entrada explícita de provedor e aponte seu modelo padrão para ela. Veja o exemplo completo de configuração abaixo.

## Exemplo completo de configuração

Este exemplo usa Gemma 4 em um servidor `inferrs` local.

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "inferrs/google/gemma-4-E2B-it" },      models: {        "inferrs/google/gemma-4-E2B-it": {          alias: "Gemma 4 (inferrs)",        },      },    },  },  models: {    mode: "merge",    providers: {      inferrs: {        baseUrl: "http://127.0.0.1:8080/v1",        apiKey: "inferrs-local",        api: "openai-completions",        models: [          {            id: "google/gemma-4-E2B-it",            name: "Gemma 4 E2B (inferrs)",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 131072,            maxTokens: 4096,            compat: {              requiresStringContent: true,            },          },        ],      },    },  },}
[/code]

## Inicialização sob demanda

O Inferrs também pode ser iniciado pelo OpenClaw apenas quando um modelo `inferrs/...` for selecionado. Adicione `localService` à mesma entrada de provedor:

json5Copy code
[code]
    {  models: {    providers: {      inferrs: {        baseUrl: "http://127.0.0.1:8080/v1",        apiKey: "inferrs-local",        api: "openai-completions",        timeoutSeconds: 300,        localService: {          command: "/opt/homebrew/bin/inferrs",          args: [            "serve",            "google/gemma-4-E2B-it",            "--host",            "127.0.0.1",            "--port",            "8080",            "--device",            "metal",          ],          healthUrl: "http://127.0.0.1:8080/v1/models",          readyTimeoutMs: 180000,          idleStopMs: 0,        },        models: [          {            id: "google/gemma-4-E2B-it",            name: "Gemma 4 E2B (inferrs)",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 131072,            maxTokens: 4096,            compat: {              requiresStringContent: true,            },          },        ],      },    },  },}
[/code]

`command` deve ser absoluto. Use `which inferrs` no host do Gateway e coloque esse caminho na configuração. Para a referência completa dos campos, veja [Serviços de modelos locais](</pt-BR/gateway/local-model-services>).

## Configuração avançada

Why requiresStringContent matters

Algumas rotas de Chat Completions do `inferrs` aceitam apenas `messages[].content` como string, não arrays estruturados de partes de conteúdo.

json5Copy code
[code]
    compat: {  requiresStringContent: true}
[/code]

O OpenClaw transformará partes de conteúdo de texto puro em strings simples antes de enviar a solicitação.

Gemma and tool-schema caveat

Algumas combinações atuais de `inferrs` \+ Gemma aceitam pequenas solicitações diretas para `/v1/chat/completions`, mas ainda falham em turnos completos de agent-runtime do OpenClaw.

Se isso acontecer, tente isto primeiro:

json5Copy code
[code]
    compat: {  requiresStringContent: true,  supportsTools: false}
[/code]

Isso desativa a superfície de esquema de ferramentas do OpenClaw para o modelo e pode reduzir a pressão do prompt em backends locais mais restritos.

Se solicitações diretas mínimas ainda funcionarem, mas turnos normais de agente do OpenClaw continuarem travando dentro do `inferrs`, o problema restante normalmente está no comportamento upstream do modelo/servidor, e não na camada de transporte do OpenClaw.

Manual smoke test

Depois de configurado, teste as duas camadas:

bashCopy code
[code]
    curl http://127.0.0.1:8080/v1/chat/completions \  -H 'content-type: application/json' \  -d '{"model":"google/gemma-4-E2B-it","messages":[{"role":"user","content":"What is 2 + 2?"}],"stream":false}'
[/code]

bashCopy code
[code]
    openclaw infer model run \  --model inferrs/google/gemma-4-E2B-it \  --prompt "What is 2 + 2? Reply with one short sentence." \  --json
[/code]

Se o primeiro comando funcionar, mas o segundo falhar, consulte a seção de solução de problemas abaixo.

Proxy-style behavior

`inferrs` é tratado como um backend `/v1` compatível com OpenAI em estilo proxy, não como um endpoint OpenAI nativo.

  * A modelagem de solicitações exclusiva da OpenAI nativa não se aplica aqui
  * Sem `service_tier`, sem `store` de Responses, sem dicas de cache de prompt e sem modelagem de payload de compatibilidade de raciocínio da OpenAI
  * Cabeçalhos ocultos de atribuição do OpenClaw (`originator`, `version`, `User-Agent`) não são injetados em URLs base personalizadas do `inferrs`


## Solução de problemas

curl /v1/models fails

`inferrs` não está em execução, não está acessível ou não está vinculado ao host/porta esperado. Verifique se o servidor foi iniciado e está escutando no endereço que você configurou.

messages[].content expected a string

Defina `compat.requiresStringContent: true` na entrada do modelo. Veja a seção `requiresStringContent` acima para detalhes.

Direct /v1/chat/completions calls pass but openclaw infer model run fails

Tente definir `compat.supportsTools: false` para desativar a superfície de esquema de ferramentas. Veja a observação sobre o esquema de ferramentas do Gemma acima.

inferrs still crashes on larger agent turns

Se o OpenClaw não recebe mais erros de esquema, mas `inferrs` ainda trava em turnos maiores de agente, trate isso como uma limitação upstream do `inferrs` ou do modelo. Reduza a pressão do prompt ou mude para outro backend ou modelo local.

## Relacionados

[**Local models** Executando o OpenClaw com servidores de modelos locais. ](</pt-BR/gateway/local-models>) [**Local model services** Iniciando servidores de modelos locais sob demanda para provedores configurados. ](</pt-BR/gateway/local-model-services>) [**Gateway troubleshooting** Depurando backends locais compatíveis com OpenAI que passam nas sondagens, mas falham em execuções de agente. ](</pt-BR/gateway/troubleshooting#local-openai-compatible-backend-passes-direct-probes-but-agent-runs-fail>) [**Model selection** Visão geral de todos os provedores, refs de modelo e comportamento de failover. ](</pt-BR/concepts/model-providers>)

Was this useful?YesNo