---
title: Busca paralela
source_url: https://docs.openclaw.ai/pt-BR/tools/parallel-search
scraped_at: 2026-06-29
---

CapabilitiesTools

O Plugin Parallel fornece dois provedores `web_search` da [Parallel](<https://parallel.ai/>):

  * **Busca Parallel (Grátis)** (`parallel-free`) -- o [Search MCP](<https://docs.parallel.ai/integrations/mcp/search-mcp>) gratuito da Parallel. Não requer conta nem chave de API. Selecione-o explicitamente quando quiser o caminho de busca hospedado da Parallel sem chave.
  * **Busca Parallel** (`parallel`) -- a API de Busca paga da Parallel. Requer uma `PARALLEL_API_KEY` e oferece limites de taxa maiores e ajuste de objetivo.


Ambos retornam trechos ranqueados e otimizados para LLM de um índice da web criado para agentes de IA. Defina `tools.web.search.provider` como `parallel-free` ou `parallel` para escolher um explicitamente.

## Instalar Plugin

Instale o Plugin oficial e reinicie o Gateway:

bashCopy code
[code]
    openclaw plugins install @openclaw/parallel-pluginopenclaw gateway restart
[/code]

## Chave de API (provedor pago)

`parallel-free` não requer chave de API, mas ainda precisa ser selecionado como o provedor gerenciado. O provedor pago `parallel` precisa de uma chave de API:

* ### Criar uma conta

Cadastre-se em [platform.parallel.ai](<https://platform.parallel.ai>) e gere uma chave de API no seu painel.

* ### Armazenar a chave

Defina `PARALLEL_API_KEY` no ambiente do Gateway, ou configure via:

bashCopy code
[code]
    openclaw configure --section web
[/code]

## Configuração

json5Copy code
[code]
    {  plugins: {    entries: {      parallel: {        config: {          webSearch: {            apiKey: "par-...", // optional if PARALLEL_API_KEY is set            baseUrl: "https://api.parallel.ai", // optional; OpenClaw appends /v1/search          },        },      },    },  },  tools: {    web: {      search: {        // Use "parallel-free" for the free Search MCP, or "parallel" for        // the paid API-backed provider shown here.        provider: "parallel",      },    },  },}
[/code]

**Alternativa de ambiente:** defina `PARALLEL_API_KEY` no ambiente do Gateway. Para uma instalação do gateway, coloque-a em `~/.openclaw/.env`.

## Substituição da URL base

A substituição da URL base se aplica apenas ao provedor pago `parallel`. O provedor gratuito `parallel-free` sempre usa `https://search.parallel.ai/mcp`.

Defina `plugins.entries.parallel.config.webSearch.baseUrl` quando as solicitações da Parallel devem passar por um proxy compatível ou endpoint alternativo da Parallel (por exemplo, o Cloudflare AI Gateway). O OpenClaw normaliza hosts simples prefixando `https://` e acrescenta `/v1/search`, a menos que o caminho já termine assim. O endpoint resolvido é incluído na chave de cache de busca, então resultados de endpoints diferentes da Parallel não são compartilhados.

## Parâmetros da ferramenta

O OpenClaw expõe o formato de busca nativo da Parallel para que o modelo possa preencher tanto o objetivo em linguagem natural quanto algumas consultas curtas por palavras-chave — a combinação que a Parallel [recomenda](<https://docs.parallel.ai/search/best-practices>) para melhores resultados.

Descrição em linguagem natural da pergunta ou objetivo subjacente (máx. 5000 caracteres). Deve ser autocontida.

Consultas de busca concisas por palavras-chave, com 3 a 6 palavras cada (1 a 5 entradas, máx. 200 caracteres cada). Forneça 2 a 3 consultas diversas para obter melhores resultados.

Resultados a retornar (1 a 40).

ID de sessão opcional da Parallel (máx. 1000 caracteres em `parallel`; o Search MCP gratuito `parallel-free` limita a 100). Passe o `sessionId` de um resultado anterior da Parallel em buscas de acompanhamento que fazem parte da mesma tarefa, para que a Parallel possa agrupar chamadas relacionadas e melhorar resultados subsequentes. Um ID acima do limite é descartado e um novo é gerado.

Identificador opcional do modelo que faz a chamada (por exemplo, `claude-opus-4-7`, `gpt-5.5`). Permite que a Parallel ajuste as configurações padrão para as capacidades do seu modelo. Passe o slug exato do modelo ativo; não encurte para um alias de família.

## Observações

  * A Parallel ranqueia e comprime resultados com base na utilidade para raciocínio de LLM, não em cliques humanos; espere trechos densos em cada resultado, em vez de conteúdo de página completa
  * Trechos de resultado retornam como o array `excerpts` e também são unidos no campo `description` para compatibilidade com o contrato genérico `web_search`
  * A Parallel retorna um `session_id` em toda resposta; o OpenClaw o expõe como `sessionId` no payload da ferramenta para que chamadores possam agrupar buscas de acompanhamento
  * `searchId`, `warnings` e `usage` da Parallel são repassados quando presentes
  * O OpenClaw sempre encaminha uma contagem de resultados resolvida para a Parallel como `advanced_settings.max_results`. O arg `count` do chamador prevalece, depois a configuração de nível superior `tools.web.search.maxResults`; caso contrário, é usado o padrão genérico de `web_search` do OpenClaw (5). Isso mantém o volume de resultados consistente ao alternar entre provedores; a Parallel, por conta própria, usa 10 por padrão
  * Os resultados ficam em cache por 15 minutos por padrão (configurável via `cacheTtlMinutes`)
  * O provedor gratuito `parallel-free` aceita os mesmos parâmetros. Ele aplica `count` no lado do cliente e gera um `session_id` por chamada quando nenhum é fornecido.


## Relacionados

  * [Visão geral de Busca Web](</pt-BR/tools/web>) \-- todos os provedores e detecção automática
  * [Busca Exa](</pt-BR/tools/exa-search>) \-- busca neural com extração de conteúdo
  * [Busca Perplexity](</pt-BR/tools/perplexity-search>) \-- resultados estruturados com filtragem por domínio


Was this useful?YesNo

Open issue