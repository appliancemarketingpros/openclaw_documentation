---
title: Pesquisa SearXNG
source_url: https://docs.openclaw.ai/pt-BR/tools/searxng-search
scraped_at: 2026-05-25
---

OpenClaw oferece suporte ao [SearXNG](<https://docs.searxng.org/>) como um provedor `web_search` **auto-hospedado e sem chave**. SearXNG é um mecanismo de metabusca de código aberto que agrega resultados do Google, Bing, DuckDuckGo e outras fontes.

Vantagens:

  * **Gratuito e ilimitado** \-- não requer chave de API nem assinatura comercial
  * **Privacidade / isolamento de rede** \-- as consultas nunca saem da sua rede
  * **Funciona em qualquer lugar** \-- sem restrições regionais em APIs de busca comerciais


## Configuração

* ### Execute uma instância do SearXNG

bashCopy code
[code]
    docker run -d -p 8888:8080 searxng/searxng
[/code]

Ou use qualquer implantação existente do SearXNG à qual você tenha acesso. Consulte a [documentação do SearXNG](<https://docs.searxng.org/>) para configuração de produção.

* ### Configure

bashCopy code
[code]
    openclaw configure --section web# Select "searxng" as the provider
[/code]

Ou defina a variável de ambiente e deixe a detecção automática encontrá-la:

bashCopy code
[code]
    export SEARXNG_BASE_URL="http://localhost:8888"
[/code]

## Configuração

json5Copy code
[code]
    {  tools: {    web: {      search: {        provider: "searxng",      },    },  },}
[/code]

Configurações no nível do Plugin para a instância do SearXNG:

json5Copy code
[code]
    {  plugins: {    entries: {      searxng: {        config: {          webSearch: {            baseUrl: "http://localhost:8888",            categories: "general,news", // optional            language: "en", // optional          },        },      },    },  },}
[/code]

O campo `baseUrl` também aceita objetos SecretRef.

Regras de transporte:

  * `https://` funciona para hosts SearXNG públicos ou privados
  * `http://` só é aceito para hosts confiáveis em rede privada ou loopback
  * hosts SearXNG públicos devem usar `https://`
  * hosts privados/internos usam a proteção de rede auto-hospedada; hosts públicos `https://` permanecem na proteção rigorosa de busca na web e não podem redirecionar para endereços privados


## Variável de ambiente

Defina `SEARXNG_BASE_URL` como alternativa à configuração:

bashCopy code
[code]
    export SEARXNG_BASE_URL="http://localhost:8888"
[/code]

Quando `SEARXNG_BASE_URL` está definida e nenhum provedor explícito está configurado, a detecção automática seleciona o SearXNG automaticamente (na prioridade mais baixa -- qualquer provedor baseado em API com uma chave vence primeiro).

## Referência de configuração do Plugin

Campo | Descrição  
---|---  
`baseUrl` | URL base da sua instância do SearXNG (obrigatório)  
`categories` | Categorias separadas por vírgula, como `general`, `news` ou `science`  
`language` | Código de idioma para resultados, como `en`, `de` ou `fr`  
  
## Observações

  * **API JSON** \-- usa o endpoint nativo `format=json` do SearXNG, não raspagem de HTML
  * **URLs de resultados de imagem** \-- resultados da categoria de imagens incluem `img_src` quando o SearXNG retorna uma URL direta de imagem
  * **Sem chave de API** \-- funciona imediatamente com qualquer instância do SearXNG
  * **Validação da URL base** \-- `baseUrl` deve ser uma URL `http://` ou `https://` válida; hosts públicos devem usar `https://`
  * **Proteção de rede** \-- endpoints SearXNG privados/internos aderem ao acesso de rede privada; endpoints SearXNG públicos `https://` mantêm proteção SSRF rigorosa
  * **Ordem de detecção automática** \-- SearXNG é verificado por último (ordem 200) na detecção automática. Provedores baseados em API com chaves configuradas são executados primeiro, depois DuckDuckGo (ordem 100), depois Ollama Web Search (ordem 110)
  * **Auto-hospedado** \-- você controla a instância, as consultas e os mecanismos de busca upstream
  * **Categorias** usam `general` por padrão quando não configuradas
  * **Fallback de categoria** \-- se uma solicitação de categoria não `general` tiver sucesso, mas retornar zero resultados, OpenClaw tenta novamente a mesma consulta uma vez com `general` antes de retornar um conjunto de resultados vazio


## Relacionados

  * [Visão geral da busca na web](</pt-BR/tools/web>) \-- todos os provedores e detecção automática
  * [Busca DuckDuckGo](</pt-BR/tools/duckduckgo-search>) \-- outro fallback sem chave
  * [Brave Search](</pt-BR/tools/brave-search>) \-- resultados estruturados com camada gratuita


Was this useful?YesNo