---
title: Perplexity
source_url: https://docs.openclaw.ai/pt-BR/providers/perplexity-provider
scraped_at: 2026-05-25
---

O Plugin Perplexity fornece recursos de busca na web por meio da API de Busca do Perplexity ou do Perplexity Sonar via OpenRouter.

Propriedade | Valor  
---|---  
Tipo | Provedor de busca na web (não é um provedor de modelo)  
Auth | `PERPLEXITY_API_KEY` (direto) ou `OPENROUTER_API_KEY` (via OpenRouter)  
Caminho de configuração | `plugins.entries.perplexity.config.webSearch.apiKey`  
  
## Introdução

* ### Set the API key

Execute o fluxo interativo de configuração de busca na web:

bashCopy code
[code]
    openclaw configure --section web
[/code]

Ou defina a chave diretamente:

bashCopy code
[code]
    openclaw config set plugins.entries.perplexity.config.webSearch.apiKey "pplx-xxxxxxxxxxxx"
[/code]

* ### Start searching

O agente usará automaticamente o Perplexity para buscas na web assim que a chave estiver configurada. Nenhuma etapa adicional é necessária.

## Modos de busca

O Plugin seleciona automaticamente o transporte com base no prefixo da chave de API:

### Native Perplexity API (pplx-)

Quando sua chave começa com `pplx-`, o OpenClaw usa a API de Busca Perplexity nativa. Esse transporte retorna resultados estruturados e oferece suporte a filtros de domínio, idioma e data (veja as opções de filtragem abaixo).

### OpenRouter / Sonar (sk-or-)

Quando sua chave começa com `sk-or-`, o OpenClaw encaminha por meio do OpenRouter usando o modelo Perplexity Sonar. Esse transporte retorna respostas sintetizadas por IA com citações.

Prefixo da chave | Transporte | Recursos  
---|---|---  
`pplx-` | API de Busca Perplexity nativa | Resultados estruturados, filtros de domínio/idioma/data  
`sk-or-` | OpenRouter (Sonar) | Respostas sintetizadas por IA com citações  
  
## Filtragem da API nativa

Ao usar a API Perplexity nativa, as buscas oferecem suporte aos seguintes filtros:

Filtro | Descrição | Exemplo  
---|---|---  
País | Código de país de 2 letras | `us`, `de`, `jp`  
Idioma | Código de idioma ISO 639-1 | `en`, `fr`, `zh`  
Intervalo de datas | Janela de recência | `day`, `week`, `month`, `year`  
Filtros de domínio | Lista de permissões ou de bloqueios (máx. 20 domínios) | `example.com`  
Orçamento de conteúdo | Limites de tokens por resposta / por página | `max_tokens`, `max_tokens_per_page`  
  
## Configuração avançada

Environment variable for daemon processes

Se o OpenClaw Gateway for executado como daemon (launchd/systemd), certifique-se de que `PERPLEXITY_API_KEY` esteja disponível para esse processo.

OpenRouter proxy setup

Se você preferir encaminhar buscas do Perplexity pelo OpenRouter, defina uma `OPENROUTER_API_KEY` (prefixo `sk-or-`) em vez de uma chave Perplexity nativa. O OpenClaw detectará o prefixo e alternará para o transporte Sonar automaticamente.

## Relacionado

[**Perplexity search tool** Como o agente invoca buscas do Perplexity e interpreta resultados. ](</pt-BR/tools/perplexity-search>) [**Configuration reference** Referência completa de configuração, incluindo entradas de Plugin. ](</pt-BR/gateway/configuration-reference>)

Was this useful?YesNo