---
title: Tavily
source_url: https://docs.openclaw.ai/pt-BR/tools/tavily
scraped_at: 2026-05-25
---

[Tavily](<https://tavily.com>) é uma API de busca projetada para aplicações de IA. O OpenClaw a expõe de duas formas:

  * como o provedor `web_search` para a ferramenta genérica de busca
  * como ferramentas explícitas de Plugin: `tavily_search` e `tavily_extract`


A Tavily retorna resultados estruturados otimizados para consumo por LLMs, com profundidade de busca configurável, filtragem por tópico, filtros de domínio, resumos de resposta gerados por IA e extração de conteúdo de URLs (incluindo páginas renderizadas por JavaScript).

Propriedade | Valor  
---|---  
ID do Plugin | `tavily`  
Autenticação | `TAVILY_API_KEY` ou config `apiKey`  
URL base | `https://api.tavily.com` (padrão)  
Ferramentas incluídas | `tavily_search`, `tavily_extract`  
  
## Primeiros passos

* ### Obtenha uma chave de API

Crie uma conta da Tavily em [tavily.com](<https://tavily.com>) e, em seguida, gere uma chave de API no painel.

* ### Configure o Plugin e o provedor

json5Copy code
[code]
    {  plugins: {    entries: {      tavily: {        enabled: true,        config: {          webSearch: {            apiKey: "tvly-...", // optional if TAVILY_API_KEY is set            baseUrl: "https://api.tavily.com",          },        },      },    },  },  tools: {    web: {      search: {        provider: "tavily",      },    },  },}
[/code]

* ### Verifique se a busca é executada

Acione uma `web_search` a partir de qualquer agente ou chame `tavily_search` diretamente.

## Referência das ferramentas

### `tavily_search`

Use isto quando quiser controles de busca específicos da Tavily em vez do `web_search` genérico.

Parâmetro | Tipo | Restrições / padrão | Descrição  
---|---|---|---  
`query` | string | obrigatório | String da consulta de busca. Mantenha abaixo de 400 caracteres.  
`search_depth` | enum | `basic` (padrão), `advanced` | `advanced` é mais lento, mas tem maior relevância.  
`topic` | enum | `general` (padrão), `news`, `finance` | Filtre por família de tópicos.  
`max_results` | integer | 1-20 | Número de resultados.  
`include_answer` | boolean | padrão `false` | Inclua um resumo de resposta gerado por IA pela Tavily.  
`time_range` | enum | `day`, `week`, `month`, `year` | Filtre os resultados por recência.  
`include_domains` | string array | (nenhum) | Inclua apenas resultados destes domínios.  
`exclude_domains` | string array | (nenhum) | Exclua resultados destes domínios.  
  
Compromisso da profundidade de busca:

Profundidade | Velocidade | Relevância | Melhor para  
---|---|---|---  
`basic` | Mais rápida | Alta | Consultas de uso geral (padrão).  
`advanced` | Mais lenta | Mais alta | Pesquisa precisa e apuração de fatos.  
  
### `tavily_extract`

Use isto para extrair conteúdo limpo de uma ou mais URLs. Lida com páginas renderizadas por JavaScript e oferece suporte a fragmentação focada em consulta para extração direcionada.

Parâmetro | Tipo | Restrições / padrão | Descrição  
---|---|---|---  
`urls` | string array | obrigatório, 1-20 | URLs das quais extrair conteúdo.  
`query` | string | (opcional) | Reclassifique os trechos extraídos por relevância para esta consulta.  
`extract_depth` | enum | `basic` (padrão), `advanced` | Use `advanced` para páginas pesadas em JS, SPAs ou tabelas dinâmicas.  
`chunks_per_source` | integer | 1-5; **requer`query`** | Trechos retornados por URL. Gera erro se definido sem `query`.  
`include_images` | boolean | padrão `false` | Inclua URLs de imagens nos resultados.  
  
Compromisso da profundidade de extração:

Profundidade | Quando usar  
---|---  
`basic` | Páginas simples. Tente isto primeiro.  
`advanced` | SPAs renderizadas por JS, conteúdo dinâmico, tabelas.  
  
## Escolhendo a ferramenta certa

Necessidade | Ferramenta  
---|---  
Busca rápida na web, sem opções especiais | `web_search`  
Busca com profundidade, tópico, respostas de IA | `tavily_search`  
Extrair conteúdo de URLs específicas | `tavily_extract`  
  
## Configuração avançada

Ordem de resolução da chave de API

O cliente Tavily procura sua chave de API nesta ordem:

  1. `plugins.entries.tavily.config.webSearch.apiKey` (resolvida por meio de SecretRefs).
  2. `TAVILY_API_KEY` do ambiente do gateway.


`tavily_extract` gera um erro de configuração se nenhum dos dois estiver presente.

URL base personalizada

Substitua `plugins.entries.tavily.config.webSearch.baseUrl` se você encaminhar a Tavily por meio de um proxy. O padrão é `https://api.tavily.com`.

`chunks_per_source` requer `query`

`tavily_extract` rejeita chamadas que passam `chunks_per_source` sem uma `query`. A Tavily classifica os trechos por relevância da consulta, portanto o parâmetro não tem sentido sem uma.

## Relacionados

[**Visão geral do Web Search** Todos os provedores e regras de detecção automática. ](</pt-BR/tools/web>) [**Firecrawl** Busca mais scraping com extração de conteúdo. ](</pt-BR/tools/firecrawl>) [**Exa Search** Busca neural com extração de conteúdo. ](</pt-BR/tools/exa-search>) [**Configuração** Esquema de configuração completo para entradas de Plugin e roteamento de ferramentas. ](</pt-BR/gateway/configuration>)

Was this useful?YesNo