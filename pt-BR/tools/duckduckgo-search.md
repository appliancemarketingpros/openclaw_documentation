---
title: Pesquisa no DuckDuckGo
source_url: https://docs.openclaw.ai/pt-BR/tools/duckduckgo-search
scraped_at: 2026-05-25
---

OpenClaw é compatível com DuckDuckGo como provedor `web_search` **sem chave**. Nenhuma chave de API ou conta é necessária.

## Configuração

Nenhuma chave de API é necessária; basta definir DuckDuckGo como seu provedor:

* ### Configurar

bashCopy code
[code]
    openclaw configure --section web# Select "duckduckgo" as the provider
[/code]

## Configuração

json5Copy code
[code]
    {  tools: {    web: {      search: {        provider: "duckduckgo",      },    },  },}
[/code]

Configurações opcionais no nível do plugin para região e SafeSearch:

json5Copy code
[code]
    {  plugins: {    entries: {      duckduckgo: {        config: {          webSearch: {            region: "us-en", // DuckDuckGo region code            safeSearch: "moderate", // "strict", "moderate", or "off"          },        },      },    },  },}
[/code]

## Parâmetros da ferramenta

Consulta de busca.

Resultados a retornar (1-10).

Código de região do DuckDuckGo (por exemplo, `us-en`, `uk-en`, `de-de`).

Nível do SafeSearch.

Região e SafeSearch também podem ser definidos na configuração do plugin (veja acima); os parâmetros da ferramenta substituem os valores de configuração por consulta.

## Observações

  * **Nenhuma chave de API** : funciona imediatamente, sem nenhuma configuração
  * **Experimental** : coleta resultados das páginas de busca HTML sem JavaScript do DuckDuckGo, não de uma API ou SDK oficial
  * **Risco de desafio contra bots** : o DuckDuckGo pode servir CAPTCHAs ou bloquear solicitações sob uso intenso ou automatizado
  * **Análise de HTML** : os resultados dependem da estrutura da página, que pode mudar sem aviso
  * **Ordem de detecção automática** : DuckDuckGo é a primeira alternativa sem chave (ordem 100) na detecção automática. Provedores baseados em API com chaves configuradas executam primeiro, depois Ollama Web Search (ordem 110) e, em seguida, SearXNG (ordem 200)
  * **SafeSearch usa moderate por padrão** quando não configurado


## Relacionados

  * [Visão geral da Web Search](</pt-BR/tools/web>) \-- todos os provedores e detecção automática
  * [Brave Search](</pt-BR/tools/brave-search>) \-- resultados estruturados com camada gratuita
  * [Exa Search](</pt-BR/tools/exa-search>) \-- busca neural com extração de conteúdo


Was this useful?YesNo