---
title: Pesquisa MiniMax
source_url: https://docs.openclaw.ai/pt-BR/tools/minimax-search
scraped_at: 2026-05-25
---

O OpenClaw oferece suporte ao MiniMax como provedor de `web_search` por meio da API de busca MiniMax Token Plan. Ela retorna resultados de busca estruturados com títulos, URLs, trechos e consultas relacionadas.

## Obtenha uma credencial do Token Plan

* ### Crie uma chave

Crie ou copie uma chave MiniMax Token Plan na [Plataforma MiniMax](<https://platform.minimax.io/user-center/basic-information/interface-key>). Configurações de OAuth podem reutilizar `MINIMAX_OAUTH_TOKEN` em vez disso.

* ### Armazene a chave

Defina `MINIMAX_CODE_PLAN_KEY` no ambiente do Gateway ou configure via:

bashCopy code
[code]
    openclaw configure --section web
[/code]

O OpenClaw também aceita `MINIMAX_CODING_API_KEY`, `MINIMAX_OAUTH_TOKEN` e `MINIMAX_API_KEY` como aliases de ambiente. `MINIMAX_API_KEY` deve apontar para uma credencial Token Plan com busca habilitada; chaves comuns da API de modelos MiniMax podem não ser aceitas pelo endpoint de busca do Token Plan.

## Configuração

json5Copy code
[code]
    {  plugins: {    entries: {      minimax: {        config: {          webSearch: {            apiKey: "sk-cp-...", // optional if a MiniMax Token Plan env var is set            region: "global", // or "cn"          },        },      },    },  },  tools: {    web: {      search: {        provider: "minimax",      },    },  },}
[/code]

**Alternativa de ambiente:** defina `MINIMAX_CODE_PLAN_KEY`, `MINIMAX_CODING_API_KEY`, `MINIMAX_OAUTH_TOKEN` ou `MINIMAX_API_KEY` no ambiente do Gateway. Para uma instalação de gateway, coloque-a em `~/.openclaw/.env`.

## Seleção de região

O MiniMax Search usa estes endpoints:

  * Global: `https://api.minimax.io/v1/coding_plan/search`
  * CN: `https://api.minimaxi.com/v1/coding_plan/search`


Se `plugins.entries.minimax.config.webSearch.region` não estiver definido, o OpenClaw resolve a região nesta ordem:

  1. `tools.web.search.minimax.region` / `webSearch.region` pertencente ao Plugin
  2. `MINIMAX_API_HOST`
  3. `models.providers.minimax.baseUrl`
  4. `models.providers.minimax-portal.baseUrl`


Isso significa que a integração inicial para CN ou `MINIMAX_API_HOST=https://api.minimaxi.com/...` também mantém automaticamente o MiniMax Search no host CN.

Mesmo quando você autenticou o MiniMax pelo caminho OAuth `minimax-portal`, a busca na web ainda é registrada com o ID de provedor `minimax`; a URL base do provedor OAuth é usada como dica de região para seleção de host CN/global, e `MINIMAX_OAUTH_TOKEN` pode satisfazer a credencial bearer do MiniMax Search.

## Parâmetros compatíveis

Parâmetro | Tipo | Restrições | Descrição  
---|---|---|---  
`query` | string | obrigatório | String de consulta de busca.  
`count` | inteiro | 1-10 | Número de resultados a retornar. O OpenClaw reduz a lista retornada para esse tamanho.  
  
Filtros específicos do provedor não são compatíveis no momento.

## Relacionado

  * [Visão geral da busca na web](</pt-BR/tools/web>) \-- todos os provedores e detecção automática
  * [MiniMax](</pt-BR/providers/minimax>) \-- configuração de modelo, imagem, fala e autenticação


Was this useful?YesNo