---
title: Pesquisa do Gemini
source_url: https://docs.openclaw.ai/pt-BR/tools/gemini-search
scraped_at: 2026-05-25
---

OpenClaw oferece suporte a modelos Gemini com [fundamentação do Google Search](<https://ai.google.dev/gemini-api/docs/grounding>) integrada, que retorna respostas sintetizadas por IA com base em resultados ao vivo do Google Search com citações.

## Obtenha uma chave de API

* ### Create a key

Acesse o [Google AI Studio](<https://aistudio.google.com/apikey>) e crie uma chave de API.

* ### Store the key

Defina `GEMINI_API_KEY` no ambiente do Gateway, reutilize `models.providers.google.apiKey` ou configure uma chave dedicada para pesquisa na web via:

bashCopy code
[code]
    openclaw configure --section web
[/code]

## Configuração

json5Copy code
[code]
    {  plugins: {    entries: {      google: {        config: {          webSearch: {            apiKey: "AIza...", // optional if GEMINI_API_KEY or models.providers.google.apiKey is set            baseUrl: "https://generativelanguage.googleapis.com/v1beta", // optional; falls back to models.providers.google.baseUrl            model: "gemini-2.5-flash", // default          },        },      },    },  },  tools: {    web: {      search: {        provider: "gemini",      },    },  },}
[/code]

**Precedência de credenciais:** a pesquisa na web do Gemini usa `plugins.entries.google.config.webSearch.apiKey` primeiro, depois `GEMINI_API_KEY`, e então `models.providers.google.apiKey`. Para URLs base, a opção dedicada `plugins.entries.google.config.webSearch.baseUrl` tem precedência sobre `models.providers.google.baseUrl`.

Para uma instalação do Gateway, coloque as chaves de ambiente em `~/.openclaw/.env`.

## Como funciona

Diferentemente de provedores de pesquisa tradicionais que retornam uma lista de links e trechos, o Gemini usa a fundamentação do Google Search para produzir respostas sintetizadas por IA com citações em linha. Os resultados incluem tanto a resposta sintetizada quanto os URLs de origem.

  * URLs de citação da fundamentação do Gemini são resolvidos automaticamente de URLs de redirecionamento do Google para URLs diretos.
  * A resolução de redirecionamento usa o caminho de proteção contra SSRF (HEAD + verificações de redirecionamento + validação de http/https) antes de retornar o URL de citação final.
  * A resolução de redirecionamento usa padrões estritos de SSRF, portanto redirecionamentos para destinos privados/internos são bloqueados.


## Parâmetros compatíveis

A pesquisa do Gemini oferece suporte a `query`, `freshness`, `date_after` e `date_before`.

`count` é aceito para compatibilidade com o `web_search` compartilhado, mas a fundamentação do Gemini ainda retorna uma resposta sintetizada com citações, em vez de uma lista de N resultados.

`freshness` aceita `day`, `week`, `month`, `year` e os atalhos compartilhados `pd`, `pw`, `pm` e `py`. O OpenClaw converte esses valores, ou um intervalo explícito `date_after`/`date_before`, no `timeRangeFilter` da fundamentação do Google Search do Gemini. `country`, `language` e `domain_filter` não são compatíveis.

## Seleção de modelo

O modelo padrão é `gemini-2.5-flash` (rápido e econômico). Qualquer modelo Gemini compatível com fundamentação pode ser usado via `plugins.entries.google.config.webSearch.model`.

## Substituições de URL base

Defina `plugins.entries.google.config.webSearch.baseUrl` quando a pesquisa na web do Gemini precisar ser roteada por um proxy de operador ou endpoint personalizado compatível com Gemini. Se isso não estiver definido, a pesquisa na web do Gemini reutiliza `models.providers.google.baseUrl`. Um valor simples `https://generativelanguage.googleapis.com` é normalizado para `https://generativelanguage.googleapis.com/v1beta`; caminhos de proxy personalizados são mantidos como fornecidos após remover barras finais.

## Relacionado

  * [Visão geral da Pesquisa na Web](</pt-BR/tools/web>) \-- todos os provedores e detecção automática
  * [Brave Search](</pt-BR/tools/brave-search>) \-- resultados estruturados com trechos
  * [Perplexity Search](</pt-BR/tools/perplexity-search>) \-- resultados estruturados + extração de conteúdo


Was this useful?YesNo