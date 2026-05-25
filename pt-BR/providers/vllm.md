---
title: vLLM
source_url: https://docs.openclaw.ai/pt-BR/providers/vllm
scraped_at: 2026-05-25
---

vLLM pode servir modelos de código aberto (e alguns personalizados) por meio de uma API HTTP **compatível com OpenAI**. O OpenClaw se conecta ao vLLM usando a API `openai-completions`.

O OpenClaw também pode **descobrir automaticamente** os modelos disponíveis do vLLM quando você opta por isso com `VLLM_API_KEY` (qualquer valor funciona se o seu servidor não exigir autenticação). Use `vllm/*` em `agents.defaults.models` para manter a descoberta dinâmica quando você também configura uma URL base personalizada do vLLM.

O OpenClaw trata `vllm` como um provedor local compatível com OpenAI que oferece suporte à contabilização de uso em streaming, para que as contagens de tokens de status/contexto possam ser atualizadas a partir de respostas `stream_options.include_usage`.

Propriedade | Valor  
---|---  
ID do provedor | `vllm`  
API | `openai-completions` (compatível com OpenAI)  
Autenticação | variável de ambiente `VLLM_API_KEY`  
URL base padrão | `http://127.0.0.1:8000/v1`  
  
## Primeiros passos

* ### Iniciar o vLLM com um servidor compatível com OpenAI

Sua URL base deve expor endpoints `/v1` (por exemplo, `/v1/models`, `/v1/chat/completions`). O vLLM geralmente é executado em:

CodeCopy code
[code]
    http://127.0.0.1:8000/v1
[/code]

* ### Definir a variável de ambiente da chave de API

Qualquer valor funciona se o seu servidor não exigir autenticação:

bashCopy code
[code]
    export VLLM_API_KEY="vllm-local"
[/code]

* ### Selecionar um modelo

Substitua por um dos seus IDs de modelo do vLLM:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "vllm/your-model-id" },    },  },}
[/code]

* ### Verificar se o modelo está disponível

bashCopy code
[code]
    openclaw models list --provider vllm
[/code]

## Descoberta de modelos (provedor implícito)

Quando `VLLM_API_KEY` está definido (ou existe um perfil de autenticação) e você **não** define `models.providers.vllm`, o OpenClaw consulta:

CodeCopy code
[code]
    GET http://127.0.0.1:8000/v1/models
[/code]

e converte os IDs retornados em entradas de modelo.

## Configuração explícita (modelos manuais)

Use configuração explícita quando:

  * o vLLM é executado em outro host ou porta
  * você quer fixar valores de `contextWindow` ou `maxTokens`
  * seu servidor exige uma chave de API real (ou você quer controlar cabeçalhos)
  * você se conecta a um endpoint vLLM confiável de loopback, LAN ou Tailscale

json5Copy code
[code]
    {  models: {    providers: {      vllm: {        baseUrl: "http://127.0.0.1:8000/v1",        apiKey: "${VLLM_API_KEY}",        api: "openai-completions",        request: { allowPrivateNetwork: true },        timeoutSeconds: 300, // Optional: extend connect/header/body/request timeout for slow local models        models: [          {            id: "your-model-id",            name: "Local vLLM Model",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 128000,            maxTokens: 8192,          },        ],      },    },  },}
[/code]

Para manter esse provedor dinâmico sem listar manualmente todos os modelos, adicione um curinga de provedor ao catálogo de modelos visível:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "vllm/*": {},      },    },  },}
[/code]

## Configuração avançada

Comportamento no estilo proxy

O vLLM é tratado como um backend `/v1` compatível com OpenAI no estilo proxy, não como um endpoint OpenAI nativo. Isso significa:

Comportamento | Aplicado?  
---|---  
Formatação nativa de requisição OpenAI | Não  
`service_tier` | Não enviado  
`store` de Responses | Não enviado  
Dicas de cache de prompt | Não enviadas  
Formatação de payload compatível com raciocínio da OpenAI | Não aplicada  
Cabeçalhos ocultos de atribuição do OpenClaw | Não injetados em URLs base personalizadas  
Controles de thinking do Qwen

Para modelos Qwen servidos pelo vLLM, defina `params.qwenThinkingFormat: "chat-template"` na entrada do modelo quando o servidor espera kwargs de chat-template do Qwen. O OpenClaw mapeia `/think off` para:

jsonCopy code
[code]
    {  "chat_template_kwargs": {    "enable_thinking": false,    "preserve_thinking": true  }}
[/code]

Níveis de thinking diferentes de `off` enviam `enable_thinking: true`. Se o seu endpoint espera flags de nível superior no estilo DashScope, use `params.qwenThinkingFormat: "top-level"` para enviar `enable_thinking` na raiz da requisição. Snake-case `params.qwen_thinking_format` também é aceito.

Controles de thinking do Nemotron 3

vLLM/Nemotron 3 pode usar kwargs de chat-template para controlar se o raciocínio é retornado como raciocínio oculto ou texto visível da resposta. Quando uma sessão do OpenClaw usa `vllm/nemotron-3-*` com thinking desativado, o Plugin vLLM incluído envia:

jsonCopy code
[code]
    {  "chat_template_kwargs": {    "enable_thinking": false,    "force_nonempty_content": true  }}
[/code]

Para personalizar esses valores, defina `chat_template_kwargs` nos parâmetros do modelo. Se você também definir `params.extra_body.chat_template_kwargs`, esse valor terá precedência final porque `extra_body` é a última substituição do corpo da requisição.

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "vllm/nemotron-3-super": {          params: {            chat_template_kwargs: {              enable_thinking: false,              force_nonempty_content: true,            },          },        },      },    },  },}
[/code]

Chamadas de ferramenta do Qwen aparecem como texto

Primeiro, confira se o vLLM foi iniciado com o parser de chamadas de ferramenta e o template de chat corretos para o modelo. Por exemplo, a documentação do vLLM indica `hermes` para modelos Qwen2.5 e `qwen3_xml` para modelos Qwen3-Coder.

Sintomas:

  * Skills ou ferramentas nunca são executadas
  * o assistente imprime JSON/XML bruto, como `{"name":"read","arguments":...}`
  * o vLLM retorna uma matriz `tool_calls` vazia quando o OpenClaw envia `tool_choice: "auto"`


Algumas combinações Qwen/vLLM retornam chamadas de ferramenta estruturadas somente quando a requisição usa `tool_choice: "required"`. Para essas entradas de modelo, force o campo de requisição compatível com OpenAI com `params.extra_body`:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "vllm/Qwen-Qwen2.5-Coder-32B-Instruct": {          params: {            extra_body: {              tool_choice: "required",            },          },        },      },    },  },}
[/code]

Substitua `Qwen-Qwen2.5-Coder-32B-Instruct` pelo ID exato retornado por:

bashCopy code
[code]
    openclaw models list --provider vllm
[/code]

Você pode aplicar a mesma substituição pela CLI:

bashCopy code
[code]
    openclaw config set agents.defaults.models '{"vllm/Qwen-Qwen2.5-Coder-32B-Instruct":{"params":{"extra_body":{"tool_choice":"required"}}}}' --strict-json --merge
[/code]

Esta é uma solução alternativa de compatibilidade opcional. Ela faz com que todo turno de modelo com ferramentas exija uma chamada de ferramenta; portanto, use-a somente para uma entrada de modelo local dedicada em que esse comportamento seja aceitável. Não a use como padrão global para todos os modelos vLLM e não use um proxy que converta cegamente texto arbitrário do assistente em chamadas de ferramenta executáveis.

URL base personalizada

Se o seu servidor vLLM for executado em um host ou porta não padrão, defina `baseUrl` na configuração explícita do provedor:

json5Copy code
[code]
    {  models: {    providers: {      vllm: {        baseUrl: "http://192.168.1.50:9000/v1",        apiKey: "${VLLM_API_KEY}",        api: "openai-completions",        request: { allowPrivateNetwork: true },        timeoutSeconds: 300,        models: [          {            id: "my-custom-model",            name: "Remote vLLM Model",            reasoning: false,            input: ["text"],            contextWindow: 64000,            maxTokens: 4096,          },        ],      },    },  },}
[/code]

## Solução de problemas

Primeira resposta lenta ou timeout do servidor remoto

Para modelos locais grandes, hosts LAN remotos ou links tailnet, defina um timeout de requisição com escopo no provedor:

json5Copy code
[code]
    {  models: {    providers: {      vllm: {        baseUrl: "http://192.168.1.50:8000/v1",        apiKey: "${VLLM_API_KEY}",        api: "openai-completions",        request: { allowPrivateNetwork: true },        timeoutSeconds: 300,        models: [{ id: "your-model-id", name: "Local vLLM Model" }],      },    },  },}
[/code]

`timeoutSeconds` se aplica somente às requisições HTTP de modelo vLLM, incluindo configuração da conexão, cabeçalhos de resposta, streaming do corpo e a interrupção total de guarded-fetch. Prefira isso antes de aumentar `agents.defaults.timeoutSeconds`, que controla toda a execução do agente.

Servidor inacessível

Verifique se o servidor vLLM está em execução e acessível:

bashCopy code
[code]
    curl http://127.0.0.1:8000/v1/models
[/code]

Se você vir um erro de conexão, confira o host, a porta e se o vLLM foi iniciado no modo de servidor compatível com OpenAI. Para endpoints explícitos de loopback, LAN ou Tailscale, defina também `models.providers.vllm.request.allowPrivateNetwork: true`; requisições do provedor bloqueiam URLs de rede privada por padrão, a menos que o provedor seja explicitamente confiável.

Erros de autenticação em requisições

Se as requisições falharem com erros de autenticação, defina uma `VLLM_API_KEY` real que corresponda à configuração do seu servidor ou configure o provedor explicitamente em `models.providers.vllm`.

Nenhum modelo descoberto

A descoberta automática exige que `VLLM_API_KEY` esteja definida. Se você definiu `models.providers.vllm`, o OpenClaw usa somente seus modelos declarados, a menos que `agents.defaults.models` inclua `"vllm/*": {}`.

Ferramentas renderizadas como texto bruto

Se um modelo Qwen imprimir sintaxe de ferramenta JSON/XML em vez de executar uma skill, confira as orientações sobre Qwen na Configuração avançada acima. A correção usual é:

  * iniciar o vLLM com o parser/template correto para esse modelo
  * confirmar o ID exato do modelo com `openclaw models list --provider vllm`
  * adicionar uma substituição dedicada por modelo `params.extra_body.tool_choice: "required"` somente se `tool_choice: "auto"` ainda retornar chamadas de ferramenta vazias ou apenas em texto


## Relacionado

[**Seleção de modelos** Escolha de provedores, referências de modelo e comportamento de failover. ](</pt-BR/concepts/model-providers>) [**OpenAI** Provedor OpenAI nativo e comportamento de rota compatível com OpenAI. ](</pt-BR/providers/openai>) [**OAuth e autenticação** Detalhes de autenticação e regras de reutilização de credenciais. ](</pt-BR/gateway/authentication>) [**Solução de problemas** Problemas comuns e como resolvê-los. ](</pt-BR/help/troubleshooting>)

Was this useful?YesNo