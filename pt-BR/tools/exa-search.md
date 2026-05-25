---
title: Pesquisa Exa
source_url: https://docs.openclaw.ai/pt-BR/tools/exa-search
scraped_at: 2026-05-25
---

OpenClaw oferece suporte à [Exa AI](<https://exa.ai/>) como provedor de `web_search`. A Exa oferece modos de busca neural, por palavra-chave e híbrida com extração de conteúdo integrada (destaques, texto, resumos).

## Obtenha uma chave de API

* ### Crie uma conta

Cadastre-se em [exa.ai](<https://exa.ai/>) e gere uma chave de API no seu painel.

* ### Armazene a chave

Defina `EXA_API_KEY` no ambiente do Gateway ou configure via:

bashCopy code
[code]
    openclaw configure --section web
[/code]

## Configuração

json5Copy code
[code]
    {  plugins: {    entries: {      exa: {        config: {          webSearch: {            apiKey: "exa-...", // optional if EXA_API_KEY is set            baseUrl: "https://api.exa.ai", // optional; OpenClaw appends /search          },        },      },    },  },  tools: {    web: {      search: {        provider: "exa",      },    },  },}
[/code]

**Alternativa de ambiente:** defina `EXA_API_KEY` no ambiente do Gateway. Para uma instalação do Gateway, coloque-a em `~/.openclaw/.env`.

## Substituição da URL base

Defina `plugins.entries.exa.config.webSearch.baseUrl` quando as solicitações de busca da Exa devem passar por um proxy compatível ou por um endpoint alternativo da Exa. O OpenClaw normaliza hosts simples prefixando `https://` e acrescenta `/search`, a menos que o caminho já termine assim. O endpoint resolvido é incluído na chave de cache de busca, portanto resultados de endpoints diferentes da Exa não são compartilhados.

## Parâmetros da ferramenta

Consulta de busca.

Resultados a retornar (1–100).

Modo de busca.

Filtro de tempo.

Resultados após esta data (`YYYY-MM-DD`).

Resultados antes desta data (`YYYY-MM-DD`).

Opções de extração de conteúdo (veja abaixo).

### Extração de conteúdo

A Exa pode retornar conteúdo extraído junto com os resultados de busca. Passe um objeto `contents` para habilitar:

javascriptCopy code
[code]
    await web_search({  query: "transformer architecture explained",  type: "neural",  contents: {    text: true, // full page text    highlights: { numSentences: 3 }, // key sentences    summary: true, // AI summary  },});
[/code]

Opção de conteúdo | Tipo | Descrição  
---|---|---  
`text` | `boolean | { maxCharacters }` | Extrair texto completo da página  
`highlights` | `boolean | { maxCharacters, query, numSentences, highlightsPerUrl }` | Extrair frases principais  
`summary` | `boolean | { query }` | Resumo gerado por IA  
  
### Modos de busca

Modo | Descrição  
---|---  
`auto` | A Exa escolhe o melhor modo (padrão)  
`neural` | Busca semântica/baseada em significado  
`fast` | Busca rápida por palavra-chave  
`deep` | Busca profunda e completa  
`deep-reasoning` | Busca profunda com raciocínio  
`instant` | Resultados mais rápidos  
  
## Observações

  * Se nenhuma opção `contents` for fornecida, a Exa usa `{ highlights: true }` por padrão para que os resultados incluam trechos das frases principais
  * Os resultados preservam os campos `highlightScores` e `summary` da resposta da API da Exa quando disponíveis
  * As descrições dos resultados são resolvidas primeiro a partir dos destaques, depois do resumo e, em seguida, do texto completo — o que estiver disponível
  * `freshness` e `date_after`/`date_before` não podem ser combinados — use um modo de filtro de tempo
  * Até 100 resultados podem ser retornados por consulta (sujeito aos limites de tipo de busca da Exa)
  * Os resultados são armazenados em cache por 15 minutos por padrão (configurável via `cacheTtlMinutes`)
  * A Exa é uma integração oficial de API com respostas JSON estruturadas


## Relacionado

  * [Visão geral da busca na web](</pt-BR/tools/web>) \-- todos os provedores e detecção automática
  * [Brave Search](</pt-BR/tools/brave-search>) \-- resultados estruturados com filtros de país/idioma
  * [Perplexity Search](</pt-BR/tools/perplexity-search>) \-- resultados estruturados com filtragem por domínio


Was this useful?YesNo