---
title: Referência de configuração de memória
source_url: https://docs.openclaw.ai/pt-BR/reference/memory-config
scraped_at: 2026-05-25
---

Esta página lista todos os controles de configuração para a busca de memória do OpenClaw. Para visões gerais conceituais, consulte:

[**Visão geral da memória** Como a memória funciona. ](</pt-BR/concepts/memory>) [**Motor integrado** Backend SQLite padrão. ](</pt-BR/concepts/memory-builtin>) [**Motor QMD** Sidecar local-first. ](</pt-BR/concepts/memory-qmd>) [**Busca de memória** Pipeline de busca e ajuste. ](</pt-BR/concepts/memory-search>) [**Memória ativa** Subagente de memória para sessões interativas. ](</pt-BR/concepts/active-memory>)

Todas as configurações de busca de memória ficam em `agents.defaults.memorySearch` no `openclaw.json`, salvo indicação em contrário.

* * *

## Seleção do provedor

Chave | Tipo | Padrão | Descrição  
---|---|---|---  
`provider` | `string` | detectado automaticamente | ID do adaptador de embedding, como `bedrock`, `deepinfra`, `gemini`, `github-copilot`, `local`, `mistral`, `ollama`, `openai` ou `voyage`; também pode ser um `models.providers.<id>` configurado cujo `api` aponta para um desses adaptadores  
`model` | `string` | padrão do provedor | Nome do modelo de embedding  
`fallback` | `string` | `"none"` | ID do adaptador de fallback quando o principal falha  
`enabled` | `boolean` | `true` | Habilita ou desabilita a busca de memória  
  
### Ordem de detecção automática

Quando `provider` não está definido, o OpenClaw seleciona o primeiro disponível:

* ### local

Selecionado se `memorySearch.local.modelPath` estiver configurado e o arquivo existir.

* ### github-copilot

Selecionado se um token do GitHub Copilot puder ser resolvido (variável de ambiente ou perfil de autenticação).

* ### openai

Selecionado se uma chave da OpenAI puder ser resolvida.

* ### gemini

Selecionado se uma chave do Gemini puder ser resolvida.

* ### voyage

Selecionado se uma chave do Voyage puder ser resolvida.

* ### mistral

Selecionado se uma chave do Mistral puder ser resolvida.

* ### deepinfra

Selecionado se uma chave do DeepInfra puder ser resolvida.

* ### bedrock

Selecionado se a cadeia de credenciais do AWS SDK for resolvida (função de instância, chaves de acesso, perfil, SSO, identidade web ou configuração compartilhada).

`ollama` é compatível, mas não é detectado automaticamente (defina explicitamente).

### IDs de provedores personalizados

`memorySearch.provider` pode apontar para uma entrada personalizada `models.providers.<id>`. O OpenClaw resolve o proprietário `api` desse provedor para o adaptador de embedding, preservando o ID personalizado do provedor para o tratamento de endpoint, autenticação e prefixo de modelo. Isso permite que configurações com múltiplas GPUs ou múltiplos hosts dediquem embeddings de memória a um endpoint local específico:

json5Copy code
[code]
    {  models: {    providers: {      "ollama-5080": {        api: "ollama",        baseUrl: "http://gpu-box.local:11435",        apiKey: "ollama-local",        models: [{ id: "qwen3-embedding:0.6b" }],      },    },  },  agents: {    defaults: {      memorySearch: {        provider: "ollama-5080",        model: "qwen3-embedding:0.6b",      },    },  },}
[/code]

### Resolução de chave de API

Embeddings remotos exigem uma chave de API. Em vez disso, o Bedrock usa a cadeia de credenciais padrão do AWS SDK (funções de instância, SSO, chaves de acesso).

Provedor | Variável de ambiente | Chave de configuração  
---|---|---  
Bedrock | Cadeia de credenciais da AWS | Nenhuma chave de API necessária  
DeepInfra | `DEEPINFRA_API_KEY` | `models.providers.deepinfra.apiKey`  
Gemini | `GEMINI_API_KEY` | `models.providers.google.apiKey`  
GitHub Copilot | `COPILOT_GITHUB_TOKEN`, `GH_TOKEN`, `GITHUB_TOKEN` | Perfil de autenticação via login por dispositivo  
Mistral | `MISTRAL_API_KEY` | `models.providers.mistral.apiKey`  
Ollama | `OLLAMA_API_KEY` (placeholder) | \--  
OpenAI | `OPENAI_API_KEY` | `models.providers.openai.apiKey`  
Voyage | `VOYAGE_API_KEY` | `models.providers.voyage.apiKey`  
  
* * *

## Configuração de endpoint remoto

Para endpoints personalizados compatíveis com OpenAI ou para substituir os padrões do provedor:

URL base personalizada da API.

Substitui a chave de API.

Cabeçalhos HTTP extras (mesclados com os padrões do provedor).

json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        provider: "openai",        model: "text-embedding-3-small",        remote: {          baseUrl: "https://api.example.com/v1/",          apiKey: "YOUR_KEY",        },      },    },  },}
[/code]

* * *

## Configuração específica do provedor

Gemini Chave | Tipo | Padrão | Descrição  
---|---|---|---  
`model` | `string` | `gemini-embedding-001` | Também oferece suporte a `gemini-embedding-2-preview`  
`outputDimensionality` | `number` | `3072` | Para Embedding 2: 768, 1536 ou 3072  
Tipos de entrada compatíveis com OpenAI

Endpoints de embedding compatíveis com OpenAI podem optar por campos de solicitação `input_type` específicos do provedor. Isso é útil para modelos de embedding assimétricos que exigem rótulos diferentes para embeddings de consulta e documento.

Chave | Tipo | Padrão | Descrição  
---|---|---|---  
`inputType` | `string` | não definido | `input_type` compartilhado para embeddings de consulta e documento  
`queryInputType` | `string` | não definido | `input_type` em tempo de consulta; substitui `inputType`  
`documentInputType` | `string` | não definido | `input_type` de índice/documento; substitui `inputType`  
json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        provider: "openai",        remote: {          baseUrl: "https://embeddings.example/v1",          apiKey: "env:EMBEDDINGS_API_KEY",        },        model: "asymmetric-embedder",        queryInputType: "query",        documentInputType: "passage",      },    },  },}
[/code]

Alterar esses valores afeta a identidade do cache de embedding para indexação em lote do provedor e deve ser seguido por uma reindexação da memória quando o modelo upstream trata os rótulos de forma diferente.

Bedrock

### Configuração de embedding do Bedrock

O Bedrock usa a cadeia de credenciais padrão do AWS SDK — nenhuma chave de API é necessária. Se o OpenClaw for executado no EC2 com uma função de instância habilitada para Bedrock, basta definir o provedor e o modelo:

json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        provider: "bedrock",        model: "amazon.titan-embed-text-v2:0",      },    },  },}
[/code]

Chave | Tipo | Padrão | Descrição  
---|---|---|---  
`model` | `string` | `amazon.titan-embed-text-v2:0` | Qualquer ID de modelo de embedding do Bedrock  
`outputDimensionality` | `number` | padrão do modelo | Para Titan V2: 256, 512 ou 1024  
  
**Modelos compatíveis** (com detecção de família e dimensões padrão):

ID do modelo | Provedor | Dimensões padrão | Dimensões configuráveis  
---|---|---|---  
`amazon.titan-embed-text-v2:0` | Amazon | 1024 | 256, 512, 1024  
`amazon.titan-embed-text-v1` | Amazon | 1536 | \--  
`amazon.titan-embed-g1-text-02` | Amazon | 1536 | \--  
`amazon.titan-embed-image-v1` | Amazon | 1024 | \--  
`amazon.nova-2-multimodal-embeddings-v1:0` | Amazon | 1024 | 256, 384, 1024, 3072  
`cohere.embed-english-v3` | Cohere | 1024 | \--  
`cohere.embed-multilingual-v3` | Cohere | 1024 | \--  
`cohere.embed-v4:0` | Cohere | 1536 | 256-1536  
`twelvelabs.marengo-embed-3-0-v1:0` | TwelveLabs | 512 | \--  
`twelvelabs.marengo-embed-2-7-v1:0` | TwelveLabs | 1024 | \--  
  
Variantes com sufixo de taxa de transferência (por exemplo, `amazon.titan-embed-text-v1:2:8k`) herdam a configuração do modelo base.

**Autenticação:** a autenticação do Bedrock usa a ordem padrão de resolução de credenciais do AWS SDK:

  1. Variáveis de ambiente (`AWS_ACCESS_KEY_ID` \+ `AWS_SECRET_ACCESS_KEY`)
  2. Cache de token SSO
  3. Credenciais de token de identidade web
  4. Arquivos compartilhados de credenciais e configuração
  5. Credenciais de metadados ECS ou EC2


A região é resolvida a partir de `AWS_REGION`, `AWS_DEFAULT_REGION`, do `baseUrl` do provedor `amazon-bedrock` ou usa `us-east-1` como padrão.

**Permissões IAM:** a função ou o usuário IAM precisa de:

jsonCopy code
[code]
    {  "Effect": "Allow",  "Action": "bedrock:InvokeModel",  "Resource": "*"}
[/code]

Para privilégio mínimo, restrinja `InvokeModel` ao modelo específico:

CodeCopy code
[code]
    arn:aws:bedrock:*::foundation-model/amazon.titan-embed-text-v2:0
[/code]

Local (GGUF + node-llama-cpp) Chave | Tipo | Padrão | Descrição  
---|---|---|---  
`local.modelPath` | `string` | baixado automaticamente | Caminho para o arquivo de modelo GGUF  
`local.modelCacheDir` | `string` | padrão do node-llama-cpp | Diretório de cache para modelos baixados  
`local.contextSize` | `number | "auto"` | `4096` | Tamanho da janela de contexto para o contexto de incorporação. 4096 cobre blocos típicos (128–512 tokens) enquanto limita a VRAM que não é de pesos. Reduza para 1024–2048 em hosts restritos. `"auto"` usa o máximo treinado do modelo — não recomendado para modelos 8B+ (Qwen3-Embedding-8B: 40.960 tokens → ~32 GB de VRAM contra ~8,8 GB em 4096).  
  
Modelo padrão: `embeddinggemma-300m-qat-Q8_0.gguf` (~0,6 GB, baixado automaticamente). Checkouts do código-fonte ainda exigem aprovação de compilação nativa: `pnpm approve-builds` e depois `pnpm rebuild node-llama-cpp`.

Use a CLI independente para verificar o mesmo caminho de provedor que o Gateway usa:

bashCopy code
[code]
    openclaw memory status --deep --agent mainopenclaw memory index --force --agent main
[/code]

Se `provider` for `auto`, `local` será selecionado apenas quando `local.modelPath` apontar para um arquivo local existente. Referências de modelo `hf:` e HTTP(S) ainda podem ser usadas explicitamente com `provider: "local"`, mas elas não fazem `auto` selecionar local antes que o modelo esteja disponível em disco.

### Tempo limite de incorporação em linha

Substitui o tempo limite para lotes de incorporação em linha durante a indexação de memória.

Quando não definido, usa o padrão do provedor: 600 segundos para provedores locais/auto-hospedados, como `local`, `ollama` e `lmstudio`, e 120 segundos para provedores hospedados. Aumente isso quando os lotes de incorporação locais limitados por CPU estiverem íntegros, mas lentos.

* * *

## Configuração de busca híbrida

Tudo em `memorySearch.query.hybrid`:

Chave | Tipo | Padrão | Descrição  
---|---|---|---  
`enabled` | `boolean` | `true` | Habilita busca híbrida BM25 + vetorial  
`vectorWeight` | `number` | `0.7` | Peso das pontuações vetoriais (0-1)  
`textWeight` | `number` | `0.3` | Peso das pontuações BM25 (0-1)  
`candidateMultiplier` | `number` | `4` | Multiplicador do tamanho do conjunto de candidatos  
  
### MMR (diversidade)

Chave | Tipo | Padrão | Descrição  
---|---|---|---  
`mmr.enabled` | `boolean` | `false` | Habilita reclassificação por MMR  
`mmr.lambda` | `number` | `0.7` | 0 = diversidade máx., 1 = relevância máx.  
  
### Decaimento temporal (recentidade)

Chave | Tipo | Padrão | Descrição  
---|---|---|---  
`temporalDecay.enabled` | `boolean` | `false` | Habilita reforço por recentidade  
`temporalDecay.halfLifeDays` | `number` | `30` | A pontuação é reduzida pela metade a cada N dias  
  
Arquivos perenes (`MEMORY.md`, arquivos sem data em `memory/`) nunca sofrem decaimento.

### Exemplo completo

json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        query: {          hybrid: {            vectorWeight: 0.7,            textWeight: 0.3,            mmr: { enabled: true, lambda: 0.7 },            temporalDecay: { enabled: true, halfLifeDays: 30 },          },        },      },    },  },}
[/code]

* * *

## Caminhos de memória adicionais

Chave | Tipo | Descrição  
---|---|---  
`extraPaths` | `string[]` | Diretórios ou arquivos adicionais para indexar  
json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        extraPaths: ["../team-docs", "/srv/shared-notes"],      },    },  },}
[/code]

Os caminhos podem ser absolutos ou relativos ao workspace. Diretórios são varridos recursivamente em busca de arquivos `.md`. O tratamento de symlinks depende do backend ativo: o mecanismo integrado ignora symlinks, enquanto o QMD segue o comportamento do scanner QMD subjacente.

Para busca de transcrições entre agentes com escopo de agente, use `agents.list[].memorySearch.qmd.extraCollections` em vez de `memory.qmd.paths`. Essas coleções extras seguem o mesmo formato `{ path, name, pattern? }`, mas são mescladas por agente e podem preservar nomes compartilhados explícitos quando o caminho aponta para fora do workspace atual. Se o mesmo caminho resolvido aparecer em `memory.qmd.paths` e `memorySearch.qmd.extraCollections`, o QMD mantém a primeira entrada e pula a duplicata.

* * *

## Memória multimodal (Gemini)

Indexe imagens e áudio junto com Markdown usando Gemini Embedding 2:

Chave | Tipo | Padrão | Descrição  
---|---|---|---  
`multimodal.enabled` | `boolean` | `false` | Habilita indexação multimodal  
`multimodal.modalities` | `string[]` | \-- | `["image"]`, `["audio"]` ou `["all"]`  
`multimodal.maxFileBytes` | `number` | `10000000` | Tamanho máximo de arquivo para indexação  
  
Formatos compatíveis: `.jpg`, `.jpeg`, `.png`, `.webp`, `.gif`, `.heic`, `.heif` (imagens); `.mp3`, `.wav`, `.ogg`, `.opus`, `.m4a`, `.aac`, `.flac` (áudio).

* * *

## Cache de embeddings

Chave | Tipo | Padrão | Descrição  
---|---|---|---  
`cache.enabled` | `boolean` | `false` | Armazena embeddings de chunks em SQLite  
`cache.maxEntries` | `number` | `50000` | Máximo de embeddings em cache  
  
Impede a regeração de embeddings de texto inalterado durante reindexação ou atualizações de transcrições.

* * *

## Indexação em lote

Chave | Tipo | Padrão | Descrição  
---|---|---|---  
`remote.nonBatchConcurrency` | `number` | `4` | Embeddings inline paralelos  
`remote.batch.enabled` | `boolean` | `false` | Habilita API de embedding em lote  
`remote.batch.concurrency` | `number` | `2` | Jobs em lote paralelos  
`remote.batch.wait` | `boolean` | `true` | Aguarda a conclusão do lote  
`remote.batch.pollIntervalMs` | `number` | \-- | Intervalo de sondagem  
`remote.batch.timeoutMinutes` | `number` | \-- | Timeout do lote  
  
Disponível para `openai`, `gemini` e `voyage`. O lote da OpenAI costuma ser o mais rápido e barato para grandes preenchimentos retroativos.

`remote.nonBatchConcurrency` controla chamadas de embedding inline usadas por provedores locais/auto-hospedados e provedores hospedados quando APIs de lote do provedor não estão ativas. O Ollama usa `1` por padrão para indexação sem lote para evitar sobrecarregar hosts locais menores; defina um valor maior em máquinas mais robustas.

Isso é separado de `sync.embeddingBatchTimeoutSeconds`, que controla o timeout para chamadas de embedding inline.

* * *

## Busca na memória de sessão (experimental)

Indexa transcrições de sessão e as expõe via `memory_search`:

Chave | Tipo | Padrão | Descrição  
---|---|---|---  
`experimental.sessionMemory` | `boolean` | `false` | Habilita a indexação de sessões  
`sources` | `string[]` | `["memory"]` | Adicione `"sessions"` para incluir transcrições  
`sync.sessions.deltaBytes` | `number` | `100000` | Limite de bytes para reindexação  
`sync.sessions.deltaMessages` | `number` | `50` | Limite de mensagens para reindexação  
  
* * *

## Aceleração vetorial do SQLite (sqlite-vec)

Chave | Tipo | Padrão | Descrição  
---|---|---|---  
`store.vector.enabled` | `boolean` | `true` | Usa sqlite-vec para consultas vetoriais  
`store.vector.extensionPath` | `string` | bundled | Substitui o caminho do sqlite-vec  
  
Quando sqlite-vec está indisponível, o OpenClaw recorre automaticamente à similaridade de cosseno em processo.

* * *

## Armazenamento do índice

Chave | Tipo | Padrão | Descrição  
---|---|---|---  
`store.path` | `string` | `~/.openclaw/memory/{agentId}.sqlite` | Local do índice (compatível com token `{agentId}`)  
`store.fts.tokenizer` | `string` | `unicode61` | Tokenizador FTS5 (`unicode61` ou `trigram`)  
  
* * *

## Configuração do backend QMD

Defina `memory.backend = "qmd"` para habilitar. Todas as configurações de QMD ficam em `memory.qmd`:

Chave | Tipo | Padrão | Descrição  
---|---|---|---  
`command` | `string` | `qmd` | Caminho do executável QMD; defina um caminho absoluto quando o `PATH` do serviço diferir do seu shell  
`searchMode` | `string` | `search` | Comando de busca: `search`, `vsearch`, `query`  
`includeDefaultMemory` | `boolean` | `true` | Indexa automaticamente `MEMORY.md` \+ `memory/**/*.md`  
`paths[]` | `array` | \-- | Caminhos extras: `{ name, path, pattern? }`  
`sessions.enabled` | `boolean` | `false` | Indexa transcrições de sessão  
`sessions.retentionDays` | `number` | \-- | Retenção de transcrições  
`sessions.exportDir` | `string` | \-- | Diretório de exportação  
  
`searchMode: "search"` é apenas lexical/BM25. O OpenClaw não executa sondagens de prontidão de vetores semânticos nem manutenção de embeddings do QMD para esse modo, inclusive durante `memory status --deep`; `vsearch` e `query` continuam exigindo prontidão de vetores e embeddings do QMD.

O OpenClaw prefere a coleção atual do QMD e os formatos de consulta MCP, mas mantém versões antigas do QMD funcionando ao tentar flags de padrão de coleção compatíveis e nomes de ferramentas MCP mais antigos quando necessário. Quando o QMD anuncia suporte a vários filtros de coleção, coleções da mesma origem são pesquisadas com um único processo do QMD; builds antigos do QMD mantêm o caminho de compatibilidade por coleção. Mesma origem significa que coleções de memória durável são agrupadas, enquanto coleções de transcrições de sessão permanecem em um grupo separado para que a diversificação de origem ainda tenha ambas as entradas.

Cronograma de atualização Chave | Tipo | Padrão | Descrição  
---|---|---|---  
`update.interval` | `string` | `5m` | Intervalo de atualização  
`update.debounceMs` | `number` | `15000` | Aplica debounce a alterações de arquivos  
`update.onBoot` | `boolean` | `true` | Atualiza quando o gerenciador QMD de longa duração abre; também controla a atualização de inicialização opcional  
`update.startup` | `string` | `off` | Atualização opcional ao iniciar o gateway: `off`, `idle` ou `immediate`  
`update.startupDelayMs` | `number` | `120000` | Atraso antes da execução da atualização `startup: "idle"`  
`update.waitForBootSync` | `boolean` | `false` | Bloqueia a abertura do gerenciador até que a atualização inicial seja concluída  
`update.embedInterval` | `string` | \-- | Cadência separada de embed  
`update.commandTimeoutMs` | `number` | \-- | Timeout para comandos QMD  
`update.updateTimeoutMs` | `number` | \-- | Timeout para operações de atualização do QMD  
`update.embedTimeoutMs` | `number` | \-- | Timeout para operações de embed do QMD  
Limites Chave | Tipo | Padrão | Descrição  
---|---|---|---  
`limits.maxResults` | `number` | `6` | Máximo de resultados de busca  
`limits.maxSnippetChars` | `number` | \-- | Limita o tamanho do snippet  
`limits.maxInjectedChars` | `number` | \-- | Limita o total de caracteres injetados  
`limits.timeoutMs` | `number` | `4000` | Timeout de busca  
Escopo

Controla quais sessões podem receber resultados de busca QMD. Mesmo esquema de [`session.sendPolicy`](</pt-BR/gateway/config-agents#session>):

json5Copy code
[code]
    {  memory: {    qmd: {      scope: {        default: "deny",        rules: [{ action: "allow", match: { chatType: "direct" } }],      },    },  },}
[/code]

O padrão entregue permite sessões diretas e de canal, enquanto ainda nega grupos.

O padrão é apenas DM. `match.keyPrefix` corresponde à chave de sessão normalizada; `match.rawKeyPrefix` corresponde à chave bruta incluindo `agent:<id>:`.

Citações

`memory.citations` se aplica a todos os backends:

Valor | Comportamento  
---|---  
`auto` (padrão) | Inclui rodapé `Source: <path#line>` nos snippets  
`on` | Sempre inclui rodapé  
`off` | Omite rodapé (o caminho ainda é passado ao agente internamente)  
  
Atualizações de boot do QMD usam um caminho de subprocesso único durante a inicialização do gateway. O gerenciador QMD de longa duração ainda é responsável pelo observador de arquivos regular e pelos temporizadores de intervalo quando a busca de memória é aberta para uso interativo.

### Exemplo completo de QMD

json5Copy code
[code]
    {  memory: {    backend: "qmd",    citations: "auto",    qmd: {      includeDefaultMemory: true,      update: { interval: "5m", debounceMs: 15000 },      limits: { maxResults: 6, timeoutMs: 4000 },      scope: {        default: "deny",        rules: [{ action: "allow", match: { chatType: "direct" } }],      },      paths: [{ name: "docs", path: "~/notes", pattern: "**/*.md" }],    },  },}
[/code]

* * *

## Dreaming

Dreaming é configurado em `plugins.entries.memory-core.config.dreaming`, não em `agents.defaults.memorySearch`.

Dreaming executa uma única varredura agendada e usa fases internas leve/profunda/REM como detalhe de implementação.

Para comportamento conceitual e comandos de barra, consulte [Dreaming](</pt-BR/concepts/dreaming>).

### Configurações de usuário

Chave | Tipo | Padrão | Descrição  
---|---|---|---  
`enabled` | `boolean` | `false` | Ativa ou desativa dreaming completamente  
`frequency` | `string` | `0 3 * * *` | Cadência cron opcional para a varredura completa de dreaming  
`model` | `string` | modelo padrão | Substituição opcional do modelo do subagente Dream Diary  
  
### Exemplo

json5Copy code
[code]
    {  plugins: {    entries: {      "memory-core": {        subagent: {          allowModelOverride: true,          allowedModels: ["anthropic/claude-sonnet-4-6"],        },        config: {          dreaming: {            enabled: true,            frequency: "0 3 * * *",            model: "anthropic/claude-sonnet-4-6",          },        },      },    },  },}
[/code]

## Relacionados

  * [Referência de configuração](</pt-BR/gateway/configuration-reference>)
  * [Visão geral de memória](</pt-BR/concepts/memory>)
  * [Busca de memória](</pt-BR/concepts/memory-search>)


Was this useful?YesNo