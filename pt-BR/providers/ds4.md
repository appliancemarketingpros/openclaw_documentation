---
title: ds4
source_url: https://docs.openclaw.ai/pt-BR/providers/ds4
scraped_at: 2026-06-29
---

ModelsProviders

[ds4](<https://github.com/antirez/ds4>) serve o DeepSeek V4 Flash a partir de um backend Metal local com uma API `/v1` compatível com OpenAI. O OpenClaw se conecta ao ds4 por meio da família genérica de provedores `openai-completions`.

ds4 não é um Plugin de provedor OpenClaw incluído. Configure-o em `models.providers.ds4` e selecione `ds4/deepseek-v4-flash`.

  * ID do provedor: `ds4`
  * Plugin: nenhum
  * API: Chat Completions compatível com OpenAI (`openai-completions`)
  * URL base sugerida: `http://127.0.0.1:18000/v1`
  * ID do modelo: `deepseek-v4-flash`
  * Chamadas de ferramentas: compatíveis por meio de `tools` e `tool_calls` no estilo OpenAI
  * Raciocínio: `thinking` e `reasoning_effort` no estilo DeepSeek


## Requisitos

  * macOS com suporte a Metal.
  * Um checkout ds4 funcional com `ds4-server` e o arquivo GGUF do DeepSeek V4 Flash.
  * Memória suficiente para o contexto que você escolher. Valores maiores de `--ctx` alocam mais memória KV quando o servidor inicia.


## Início rápido

* ### Iniciar ds4-server

Substitua `&lt;DS4_DIR&gt;` pelo caminho do seu checkout ds4.

bashCopy code
[code]
    &lt;DS4_DIR&gt;/ds4-server \  --model &lt;DS4_DIR&gt;/ds4flash.gguf \  --host 127.0.0.1 \  --port 18000 \  --ctx 32768 \  --tokens 128
[/code]

* ### Verificar o endpoint compatível com OpenAI

bashCopy code
[code]
    curl http://127.0.0.1:18000/v1/models
[/code]

A resposta deve incluir `deepseek-v4-flash`.

* ### Adicionar a configuração do provedor OpenClaw

Adicione a configuração de Configuração completa e execute uma verificação pontual do modelo:

bashCopy code
[code]
    openclaw infer model run \  --local \  --model ds4/deepseek-v4-flash \  --thinking off \  --prompt "Reply with exactly: openclaw-ds4-ok" \  --json
[/code]

## Configuração completa

Use esta configuração quando o ds4 já estiver em execução em `127.0.0.1:18000`.

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "ds4/deepseek-v4-flash" },      models: {        "ds4/deepseek-v4-flash": {          alias: "DS4 local",        },      },    },  },  models: {    mode: "merge",    providers: {      ds4: {        baseUrl: "http://127.0.0.1:18000/v1",        apiKey: "ds4-local",        api: "openai-completions",        timeoutSeconds: 300,        models: [          {            id: "deepseek-v4-flash",            name: "DeepSeek V4 Flash (ds4)",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 32768,            maxTokens: 128,            compat: {              supportsUsageInStreaming: true,              supportsReasoningEffort: true,              maxTokensField: "max_tokens",              supportsStrictMode: false,              thinkingFormat: "deepseek",              supportedReasoningEfforts: ["low", "medium", "high", "xhigh"],            },          },        ],      },    },  },}
[/code]

Mantenha `contextWindow` alinhado ao valor `ds4-server --ctx`. Mantenha `maxTokens` alinhado a `--tokens`, a menos que você queira intencionalmente que o OpenClaw solicite menos saída que o padrão do servidor.

## Inicialização sob demanda

O OpenClaw pode iniciar o ds4 somente quando um modelo `ds4/...` é selecionado. Adicione `localService` à mesma entrada de provedor:

json5Copy code
[code]
    {  models: {    providers: {      ds4: {        baseUrl: "http://127.0.0.1:18000/v1",        apiKey: "ds4-local",        api: "openai-completions",        timeoutSeconds: 300,        localService: {          command: "&lt;DS4_DIR&gt;/ds4-server",          args: [            "--model",            "&lt;DS4_DIR&gt;/ds4flash.gguf",            "--host",            "127.0.0.1",            "--port",            "18000",            "--ctx",            "32768",            "--tokens",            "128",          ],          cwd: "&lt;DS4_DIR&gt;",          healthUrl: "http://127.0.0.1:18000/v1/models",          readyTimeoutMs: 300000,          idleStopMs: 0,        },        models: [          {            id: "deepseek-v4-flash",            name: "DeepSeek V4 Flash (ds4)",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 32768,            maxTokens: 128,            compat: {              supportsUsageInStreaming: true,              supportsReasoningEffort: true,              maxTokensField: "max_tokens",              supportsStrictMode: false,              thinkingFormat: "deepseek",              supportedReasoningEfforts: ["low", "medium", "high", "xhigh"],            },          },        ],      },    },  },}
[/code]

`command` deve ser um caminho absoluto para o executável. Busca pelo shell e expansão de `~` não são usadas. Consulte [Serviços de modelo locais](</pt-BR/gateway/local-model-services>) para ver todos os campos de `localService`.

## Think Max

O ds4 aplica Think Max somente quando as duas condições são verdadeiras:

  * `ds4-server` inicia com `--ctx 393216` ou superior.
  * A solicitação usa `reasoning_effort: "max"` ou o campo de esforço equivalente do ds4.


Se você executar esse contexto grande, atualize tanto as flags do servidor quanto os metadados do modelo OpenClaw:

json5Copy code
[code]
    {  contextWindow: 393216,  maxTokens: 384000,  compat: {    supportsUsageInStreaming: true,    supportsReasoningEffort: true,    maxTokensField: "max_tokens",    supportsStrictMode: false,    thinkingFormat: "deepseek",    supportedReasoningEfforts: ["low", "medium", "high", "xhigh", "max"],  },}
[/code]

## Teste

Comece com uma verificação HTTP direta:

bashCopy code
[code]
    curl http://127.0.0.1:18000/v1/chat/completions \  -H 'content-type: application/json' \  -d '{"model":"deepseek-v4-flash","messages":[{"role":"user","content":"Reply with exactly: ds4-ok"}],"max_tokens":16,"stream":false,"thinking":{"type":"disabled"}}'
[/code]

Depois, teste o roteamento de modelo do OpenClaw:

bashCopy code
[code]
    openclaw infer model run \  --local \  --model ds4/deepseek-v4-flash \  --thinking off \  --prompt "Reply with exactly: openclaw-ds4-ok" \  --json
[/code]

Para um teste rápido completo de agente e chamada de ferramenta, use um contexto de pelo menos 32768:

bashCopy code
[code]
    openclaw agent \  --local \  --session-id ds4-tool-smoke \  --model ds4/deepseek-v4-flash \  --thinking off \  --message "Use the shell command pwd once, then reply exactly: tool-ok <output>" \  --json \  --timeout 240
[/code]

Resultado esperado:

  * `executionTrace.winnerProvider` é `ds4`
  * `executionTrace.winnerModel` é `deepseek-v4-flash`
  * `toolSummary.calls` é pelo menos `1`
  * `finalAssistantVisibleText` começa com `tool-ok`


## Solução de problemas

curl /v1/models não consegue conectar

ds4 não está em execução ou não está vinculado ao host e à porta em `baseUrl`. Inicie `ds4-server` e tente novamente:

bashCopy code
[code]
    curl http://127.0.0.1:18000/v1/models
[/code]

500 prompt exceeds context

O `--ctx` configurado é pequeno demais para o turno do OpenClaw. Aumente `ds4-server --ctx` e atualize `models.providers.ds4.models[].contextWindow` para corresponder. Turnos completos de agente com ferramentas precisam de substancialmente mais contexto do que uma solicitação curl direta com uma única mensagem.

Think Max não é ativado

ds4 usa Think Max somente quando `--ctx` é pelo menos `393216` e a solicitação pede `reasoning_effort: "max"`. Contextos menores retornam para raciocínio alto.

A primeira solicitação é lenta

ds4 tem uma fase fria de residência em Metal e aquecimento do modelo. Use `localService.readyTimeoutMs: 300000` quando o OpenClaw iniciar o servidor sob demanda.

## Relacionado

[**Serviços de modelo locais** Inicie servidores de modelo locais sob demanda antes de solicitações de modelo. ](</pt-BR/gateway/local-model-services>) [**Modelos locais** Escolha e opere backends de modelo locais. ](</pt-BR/gateway/local-models>) [**Provedores de modelo** Configure refs de provedor, autenticação e failover. ](</pt-BR/concepts/model-providers>) [**DeepSeek** Comportamento nativo do provedor DeepSeek e controles de thinking. ](</pt-BR/providers/deepseek>)

Was this useful?YesNo

Open issue