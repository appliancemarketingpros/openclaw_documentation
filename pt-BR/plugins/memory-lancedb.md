---
title: Memória LanceDB
source_url: https://docs.openclaw.ai/pt-BR/plugins/memory-lancedb
scraped_at: 2026-05-25
---

`memory-lancedb` é um plugin de memória incluído que armazena memória de longo prazo no LanceDB e usa embeddings para recuperação. Ele pode recuperar automaticamente memórias relevantes antes de uma rodada do modelo e capturar fatos importantes após uma resposta.

Use-o quando quiser um banco de dados vetorial local para memória, precisar de um endpoint de embedding compatível com OpenAI ou quiser manter um banco de dados de memória fora do armazenamento de memória integrado padrão.

## Início rápido

json5Copy code
[code]
    {  plugins: {    slots: {      memory: "memory-lancedb",    },    entries: {      "memory-lancedb": {        enabled: true,        config: {          embedding: {            provider: "openai",            model: "text-embedding-3-small",          },          autoRecall: true,          autoCapture: false,        },      },    },  },}
[/code]

Reinicie o Gateway depois de alterar a configuração do plugin:

bashCopy code
[code]
    openclaw gateway restart
[/code]

Depois verifique se o plugin foi carregado:

bashCopy code
[code]
    openclaw plugins list
[/code]

## Embeddings com suporte de provedores

`memory-lancedb` pode usar os mesmos adaptadores de provedor de embedding de memória que `memory-core`. Defina `embedding.provider` e omita `embedding.apiKey` para usar o perfil de autenticação configurado do provedor, a variável de ambiente ou `models.providers.<provider>.apiKey`.

json5Copy code
[code]
    {  plugins: {    slots: {      memory: "memory-lancedb",    },    entries: {      "memory-lancedb": {        enabled: true,        config: {          embedding: {            provider: "openai",            model: "text-embedding-3-small",          },          autoRecall: true,        },      },    },  },}
[/code]

Esse caminho funciona com perfis de autenticação de provedores que expõem credenciais de embedding. Por exemplo, o GitHub Copilot pode ser usado quando o perfil/plano do Copilot oferece suporte a embeddings:

json5Copy code
[code]
    {  plugins: {    slots: {      memory: "memory-lancedb",    },    entries: {      "memory-lancedb": {        enabled: true,        config: {          embedding: {            provider: "github-copilot",            model: "text-embedding-3-small",          },        },      },    },  },}
[/code]

OAuth do OpenAI Codex / ChatGPT (`openai-codex`) não é uma credencial de embeddings da OpenAI Platform. Para embeddings da OpenAI, use um perfil de autenticação com chave de API da OpenAI, `OPENAI_API_KEY` ou `models.providers.openai.apiKey`. Usuários somente com OAuth podem usar outro provedor compatível com embeddings, como GitHub Copilot ou Ollama.

## Embeddings do Ollama

Para embeddings do Ollama, prefira o provedor de embedding Ollama incluído. Ele usa o endpoint nativo `/api/embed` do Ollama e segue as mesmas regras de autenticação/URL base que o provedor Ollama documentado em [Ollama](</pt-BR/providers/ollama>).

json5Copy code
[code]
    {  plugins: {    slots: {      memory: "memory-lancedb",    },    entries: {      "memory-lancedb": {        enabled: true,        config: {          embedding: {            provider: "ollama",            baseUrl: "http://127.0.0.1:11434",            model: "mxbai-embed-large",            dimensions: 1024,          },          recallMaxChars: 400,          autoRecall: true,          autoCapture: false,        },      },    },  },}
[/code]

Defina `dimensions` para modelos de embedding não padrão. O OpenClaw conhece as dimensões de `text-embedding-3-small` e `text-embedding-3-large`; modelos personalizados precisam do valor na configuração para que o LanceDB possa criar a coluna vetorial.

Para modelos locais pequenos de embedding, reduza `recallMaxChars` se você vir erros de tamanho de contexto vindos do servidor local.

## Provedores compatíveis com OpenAI

Alguns provedores de embedding compatíveis com OpenAI rejeitam o parâmetro `encoding_format`, enquanto outros o ignoram e sempre retornam vetores `number[]`. Por isso, `memory-lancedb` omite `encoding_format` nas solicitações de embedding e aceita respostas tanto de arrays de floats quanto de float32 codificados em base64.

Se você tiver um endpoint bruto de embeddings compatível com OpenAI que não tenha um adaptador de provedor incluído, omita `embedding.provider` (ou deixe-o como `openai`) e defina `embedding.apiKey` mais `embedding.baseUrl`. Isso preserva o caminho direto do cliente compatível com OpenAI.

Defina `embedding.dimensions` para provedores cujas dimensões de modelo não sejam integradas. Por exemplo, o `embedding-3` da ZhiPu usa `2048` dimensões:

json5Copy code
[code]
    {  plugins: {    entries: {      "memory-lancedb": {        enabled: true,        config: {          embedding: {            apiKey: "${ZHIPU_API_KEY}",            baseUrl: "https://open.bigmodel.cn/api/paas/v4",            model: "embedding-3",            dimensions: 2048,          },        },      },    },  },}
[/code]

## Limites de recuperação e captura

`memory-lancedb` tem dois limites de texto separados:

Configuração | Padrão | Intervalo | Aplica-se a  
---|---|---|---  
`recallMaxChars` | `1000` | 100-10000 | texto enviado à API de embedding para recuperação  
`captureMaxChars` | `500` | 100-10000 | tamanho da mensagem do assistente elegível para captura  
  
`recallMaxChars` controla a recuperação automática, a ferramenta `memory_recall`, o caminho de consulta de `memory_forget` e `openclaw ltm search`. A recuperação automática prefere a mensagem de usuário mais recente da rodada e recorre ao prompt completo somente quando nenhuma mensagem de usuário está disponível. Isso mantém metadados de canal e blocos grandes de prompt fora da solicitação de embedding.

`captureMaxChars` controla se uma resposta é curta o suficiente para ser considerada para captura automática. Ele não limita embeddings de consultas de recuperação.

## Comandos

Quando `memory-lancedb` é o plugin de Active Memory, ele registra o namespace `ltm` da CLI:

bashCopy code
[code]
    openclaw ltm listopenclaw ltm search "project preferences"openclaw ltm stats
[/code]

O plugin também estende `openclaw memory` com um subcomando `query` não vetorial que é executado diretamente contra a tabela do LanceDB:

bashCopy code
[code]
    openclaw memory query --cols id,text,createdAt --limit 20openclaw memory query --filter "category = 'preference'" --order-by createdAt:desc
[/code]

  * `--cols <columns>`: lista permitida de colunas separadas por vírgulas (o padrão é `id`, `text`, `importance`, `category`, `createdAt`).
  * `--filter <condition>`: cláusula WHERE no estilo SQL; limitada a 200 caracteres e restrita a alfanuméricos, operadores de comparação, aspas, parênteses e um pequeno conjunto de pontuação segura.
  * `--limit <n>`: inteiro positivo; padrão `10`.
  * `--order-by <column>:<asc|desc>`: ordenação em memória aplicada após o filtro; a coluna de ordenação é incluída automaticamente na projeção.


Agentes também recebem ferramentas de memória do LanceDB a partir do plugin de Active Memory:

  * `memory_recall` para recuperação com suporte do LanceDB
  * `memory_store` para salvar fatos importantes, preferências, decisões e entidades
  * `memory_forget` para remover memórias correspondentes


## Armazenamento

Por padrão, os dados do LanceDB ficam em `~/.openclaw/memory/lancedb`. Substitua o caminho com `dbPath`:

json5Copy code
[code]
    {  plugins: {    entries: {      "memory-lancedb": {        enabled: true,        config: {          dbPath: "~/.openclaw/memory/lancedb",          embedding: {            apiKey: "${OPENAI_API_KEY}",            model: "text-embedding-3-small",          },        },      },    },  },}
[/code]

`storageOptions` aceita pares chave/valor em string para backends de armazenamento do LanceDB e oferece suporte à expansão `${ENV_VAR}`:

json5Copy code
[code]
    {  plugins: {    entries: {      "memory-lancedb": {        enabled: true,        config: {          dbPath: "s3://memory-bucket/openclaw",          storageOptions: {            access_key: "${AWS_ACCESS_KEY_ID}",            secret_key: "${AWS_SECRET_ACCESS_KEY}",            endpoint: "${AWS_ENDPOINT_URL}",          },          embedding: {            apiKey: "${OPENAI_API_KEY}",            model: "text-embedding-3-small",          },        },      },    },  },}
[/code]

## Dependências de runtime

`memory-lancedb` depende do pacote nativo `@lancedb/lancedb`. O OpenClaw empacotado trata esse pacote como parte do pacote do plugin. A inicialização do Gateway não repara dependências de plugins; se a dependência estiver ausente, reinstale ou atualize o pacote do plugin e reinicie o Gateway.

Se uma instalação mais antiga registrar um erro de `dist/package.json` ausente ou de `@lancedb/lancedb` ausente durante o carregamento do plugin, atualize o OpenClaw e reinicie o Gateway.

Se o plugin registrar que o LanceDB está indisponível em `darwin-x64`, use o backend de memória padrão nessa máquina, mova o Gateway para uma plataforma compatível ou desabilite `memory-lancedb`.

## Solução de problemas

### O tamanho da entrada excede o tamanho do contexto

Isso geralmente significa que o modelo de embedding rejeitou a consulta de recuperação:

textCopy code
[code]
    memory-lancedb: recall failed: Error: 400 the input length exceeds the context length
[/code]

Defina um `recallMaxChars` menor e reinicie o Gateway:

json5Copy code
[code]
    {  plugins: {    entries: {      "memory-lancedb": {        config: {          recallMaxChars: 400,        },      },    },  },}
[/code]

Para Ollama, verifique também se o servidor de embedding está acessível a partir do host do Gateway:

bashCopy code
[code]
    curl http://127.0.0.1:11434/v1/embeddings \  -H "Content-Type: application/json" \  -d '{"model":"mxbai-embed-large","input":"hello"}'
[/code]

### Modelo de embedding sem suporte

Sem `dimensions`, somente as dimensões integradas de embedding da OpenAI são conhecidas. Para modelos locais ou personalizados de embedding, defina `embedding.dimensions` como o tamanho do vetor informado por esse modelo.

### O plugin carrega, mas nenhuma memória aparece

Verifique se `plugins.slots.memory` aponta para `memory-lancedb` e depois execute:

bashCopy code
[code]
    openclaw ltm statsopenclaw ltm search "recent preference"
[/code]

Se `autoCapture` estiver desabilitado, o plugin recuperará memórias existentes, mas não armazenará novas automaticamente. Use a ferramenta `memory_store` ou habilite `autoCapture` se quiser captura automática.

## Relacionados

  * [Visão geral de memória](</pt-BR/concepts/memory>)
  * [Active Memory](</pt-BR/concepts/active-memory>)
  * [Busca de memória](</pt-BR/concepts/memory-search>)
  * [Memory Wiki](</pt-BR/plugins/memory-wiki>)
  * [Ollama](</pt-BR/providers/ollama>)


Was this useful?YesNo