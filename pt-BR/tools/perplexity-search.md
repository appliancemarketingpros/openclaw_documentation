---
title: Pesquisa do Perplexity
source_url: https://docs.openclaw.ai/pt-BR/tools/perplexity-search
scraped_at: 2026-05-25
---

OpenClaw oferece suporte à Perplexity Search API como um provedor `web_search`. Ela retorna resultados estruturados com os campos `title`, `url` e `snippet`.

Para compatibilidade, OpenClaw também oferece suporte a configurações legadas do Perplexity Sonar/OpenRouter. Se você usar `OPENROUTER_API_KEY`, uma chave `sk-or-...` em `plugins.entries.perplexity.config.webSearch.apiKey` ou definir `plugins.entries.perplexity.config.webSearch.baseUrl` / `model`, o provedor muda para o caminho de chat completions e retorna respostas sintetizadas por IA com citações em vez de resultados estruturados da Search API.

## Obtendo uma chave de API da Perplexity

  1. Crie uma conta da Perplexity em [perplexity.ai/settings/api](<https://www.perplexity.ai/settings/api>)
  2. Gere uma chave de API no painel
  3. Armazene a chave na configuração ou defina `PERPLEXITY_API_KEY` no ambiente do Gateway.


## Compatibilidade com OpenRouter

Se você já usava OpenRouter para o Perplexity Sonar, mantenha `provider: "perplexity"` e defina `OPENROUTER_API_KEY` no ambiente do Gateway, ou armazene uma chave `sk-or-...` em `plugins.entries.perplexity.config.webSearch.apiKey`.

Controles opcionais de compatibilidade:

  * `plugins.entries.perplexity.config.webSearch.baseUrl`
  * `plugins.entries.perplexity.config.webSearch.model`


## Exemplos de configuração

### Perplexity Search API nativa

json5Copy code
[code]
    {  plugins: {    entries: {      perplexity: {        config: {          webSearch: {            apiKey: "pplx-...",          },        },      },    },  },  tools: {    web: {      search: {        provider: "perplexity",      },    },  },}
[/code]

### Compatibilidade com OpenRouter / Sonar

json5Copy code
[code]
    {  plugins: {    entries: {      perplexity: {        config: {          webSearch: {            apiKey: "<openrouter-api-key>",            baseUrl: "https://openrouter.ai/api/v1",            model: "perplexity/sonar-pro",          },        },      },    },  },  tools: {    web: {      search: {        provider: "perplexity",      },    },  },}
[/code]

## Onde definir a chave

**Via configuração:** execute `openclaw configure --section web`. Isso armazena a chave em `~/.openclaw/openclaw.json` em `plugins.entries.perplexity.config.webSearch.apiKey`. Esse campo também aceita objetos SecretRef.

**Via ambiente:** defina `PERPLEXITY_API_KEY` ou `OPENROUTER_API_KEY` no ambiente do processo do Gateway. Para uma instalação do gateway, coloque-a em `~/.openclaw/.env` (ou no ambiente do seu serviço). Consulte [Variáveis de ambiente](</pt-BR/help/faq#env-vars-and-env-loading>).

Se `provider: "perplexity"` estiver configurado e o SecretRef da chave da Perplexity não puder ser resolvido sem fallback de env, a inicialização/recarregamento falha rapidamente.

## Parâmetros da ferramenta

Estes parâmetros se aplicam ao caminho nativo da Perplexity Search API.

Consulta de pesquisa.

Número de resultados a retornar (1-10).

Código de país ISO de 2 letras (por exemplo, `US`, `DE`).

Código de idioma ISO 639-1 (por exemplo, `en`, `de`, `fr`).

Filtro de tempo - `day` é 24 horas.

Somente resultados publicados após esta data (`YYYY-MM-DD`).

Somente resultados publicados antes desta data (`YYYY-MM-DD`).

Array de lista de permissão/bloqueio de domínios (máx. 20).

Orçamento total de conteúdo (máx. 1000000).

Limite de tokens por página.

Para o caminho legado de compatibilidade Sonar/OpenRouter:

  * `query`, `count` e `freshness` são aceitos
  * `count` existe apenas para compatibilidade nesse caminho; a resposta ainda é uma única resposta sintetizada com citações, em vez de uma lista com N resultados
  * Filtros exclusivos da Search API, como `country`, `language`, `date_after`, `date_before`, `domain_filter`, `max_tokens` e `max_tokens_per_page` retornam erros explícitos


**Exemplos:**

javascriptCopy code
[code]
    // Country and language-specific searchawait web_search({  query: "renewable energy",  country: "DE",  language: "de",}); // Recent results (past week)await web_search({  query: "AI news",  freshness: "week",}); // Date range searchawait web_search({  query: "AI developments",  date_after: "2024-01-01",  date_before: "2024-06-30",}); // Domain filtering (allowlist)await web_search({  query: "climate research",  domain_filter: ["nature.com", "science.org", ".edu"],}); // Domain filtering (denylist - prefix with -)await web_search({  query: "product reviews",  domain_filter: ["-reddit.com", "-pinterest.com"],}); // More content extractionawait web_search({  query: "detailed AI research",  max_tokens: 50000,  max_tokens_per_page: 4096,});
[/code]

### Regras de filtro de domínio

  * Máximo de 20 domínios por filtro
  * Não é possível misturar lista de permissão e lista de bloqueio na mesma solicitação
  * Use o prefixo `-` para entradas de lista de bloqueio (por exemplo, `["-reddit.com"]`)


## Observações

  * A Perplexity Search API retorna resultados estruturados de pesquisa na web (`title`, `url`, `snippet`)
  * OpenRouter ou `plugins.entries.perplexity.config.webSearch.baseUrl` / `model` explícito muda a Perplexity de volta para chat completions do Sonar por compatibilidade
  * A compatibilidade Sonar/OpenRouter retorna uma resposta sintetizada com citações, não linhas de resultados estruturados
  * Os resultados são armazenados em cache por 15 minutos por padrão (configurável via `cacheTtlMinutes`)


## Relacionados

[**Visão geral da pesquisa na web** Todos os provedores e regras de autodetecção. ](</pt-BR/tools/web>) [**Pesquisa Brave** Resultados estruturados com filtros de país e idioma. ](</pt-BR/tools/brave-search>) [**Pesquisa Exa** Pesquisa neural com extração de conteúdo. ](</pt-BR/tools/exa-search>) [**Documentação da Perplexity Search API** Início rápido e referência oficiais da Perplexity Search API. ](<https://docs.perplexity.ai/docs/search/quickstart>)

Was this useful?YesNo