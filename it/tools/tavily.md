---
title: Tavily
source_url: https://docs.openclaw.ai/it/tools/tavily
scraped_at: 2026-05-25
---

[Tavily](<https://tavily.com>) è un'API di ricerca progettata per applicazioni di IA. OpenClaw la espone in due modi:

  * come provider `web_search` per lo strumento di ricerca generico
  * come strumenti espliciti del Plugin: `tavily_search` e `tavily_extract`


Tavily restituisce risultati strutturati ottimizzati per il consumo da parte degli LLM, con profondità di ricerca configurabile, filtro per argomento, filtri di dominio, riepiloghi di risposte generati dall'IA ed estrazione di contenuti dagli URL (incluse le pagine renderizzate con JavaScript).

Proprietà | Valore  
---|---  
ID Plugin | `tavily`  
Autenticazione | `TAVILY_API_KEY` o config `apiKey`  
URL di base | `https://api.tavily.com` (predefinito)  
Strumenti inclusi | `tavily_search`, `tavily_extract`  
  
## Per iniziare

* ### Ottieni una chiave API

Crea un account Tavily su [tavily.com](<https://tavily.com>), quindi genera una chiave API nella dashboard.

* ### Configura il Plugin e il provider

json5Copy code
[code]
    {  plugins: {    entries: {      tavily: {        enabled: true,        config: {          webSearch: {            apiKey: "tvly-...", // optional if TAVILY_API_KEY is set            baseUrl: "https://api.tavily.com",          },        },      },    },  },  tools: {    web: {      search: {        provider: "tavily",      },    },  },}
[/code]

* ### Verifica l'esecuzione della ricerca

Attiva una `web_search` da qualsiasi agente oppure chiama direttamente `tavily_search`.

## Riferimento degli strumenti

### `tavily_search`

Usalo quando vuoi controlli di ricerca specifici di Tavily invece della `web_search` generica.

Parametro | Tipo | Vincoli / predefinito | Descrizione  
---|---|---|---  
`query` | string | obbligatorio | Stringa della query di ricerca. Mantienila sotto i 400 caratteri.  
`search_depth` | enum | `basic` (predefinito), `advanced` | `advanced` è più lento ma offre maggiore rilevanza.  
`topic` | enum | `general` (predefinito), `news`, `finance` | Filtra per famiglia di argomenti.  
`max_results` | integer | 1-20 | Numero di risultati.  
`include_answer` | boolean | predefinito `false` | Include un riepilogo della risposta generato dall'IA di Tavily.  
`time_range` | enum | `day`, `week`, `month`, `year` | Filtra i risultati per recenza.  
`include_domains` | string array | (nessuno) | Include solo risultati da questi domini.  
`exclude_domains` | string array | (nessuno) | Esclude i risultati da questi domini.  
  
Compromesso della profondità di ricerca:

Profondità | Velocità | Rilevanza | Ideale per  
---|---|---|---  
`basic` | Più veloce | Alta | Query generiche (predefinito).  
`advanced` | Più lenta | Massima | Ricerca di precisione e verifica dei fatti.  
  
### `tavily_extract`

Usalo per estrarre contenuti puliti da uno o più URL. Gestisce pagine renderizzate con JavaScript e supporta la suddivisione in blocchi focalizzata sulla query per un'estrazione mirata.

Parametro | Tipo | Vincoli / predefinito | Descrizione  
---|---|---|---  
`urls` | string array | obbligatorio, 1-20 | URL da cui estrarre contenuti.  
`query` | string | (facoltativo) | Riordina i blocchi estratti in base alla rilevanza rispetto a questa query.  
`extract_depth` | enum | `basic` (predefinito), `advanced` | Usa `advanced` per pagine con molto JS, SPA o tabelle dinamiche.  
`chunks_per_source` | integer | 1-5; **richiede`query`** | Blocchi restituiti per URL. Genera un errore se impostato senza `query`.  
`include_images` | boolean | predefinito `false` | Include gli URL delle immagini nei risultati.  
  
Compromesso della profondità di estrazione:

Profondità | Quando usarla  
---|---  
`basic` | Pagine semplici. Provala per prima.  
`advanced` | SPA renderizzate con JS, contenuti dinamici, tabelle.  
  
## Scegliere lo strumento giusto

Esigenza | Strumento  
---|---  
Ricerca web rapida, senza opzioni speciali | `web_search`  
Ricerca con profondità, argomento, risposte IA | `tavily_search`  
Estrarre contenuti da URL specifici | `tavily_extract`  
  
## Configurazione avanzata

Ordine di risoluzione della chiave API

Il client Tavily cerca la sua chiave API in questo ordine:

  1. `plugins.entries.tavily.config.webSearch.apiKey` (risolta tramite SecretRefs).
  2. `TAVILY_API_KEY` dall'ambiente del Gateway.


`tavily_extract` genera un errore di configurazione se non è presente nessuna delle due.

URL di base personalizzato

Sovrascrivi `plugins.entries.tavily.config.webSearch.baseUrl` se instradi Tavily tramite un proxy. Il valore predefinito è `https://api.tavily.com`.

`chunks_per_source` richiede `query`

`tavily_extract` rifiuta le chiamate che passano `chunks_per_source` senza una `query`. Tavily classifica i blocchi in base alla rilevanza rispetto alla query, quindi il parametro non ha significato senza una query.

## Correlati

[**Panoramica di Web Search** Tutti i provider e le regole di rilevamento automatico. ](</it/tools/web>) [**Firecrawl** Ricerca più scraping con estrazione di contenuti. ](</it/tools/firecrawl>) [**Exa Search** Ricerca neurale con estrazione di contenuti. ](</it/tools/exa-search>) [**Configurazione** Schema di configurazione completo per le voci del Plugin e il routing degli strumenti. ](</it/gateway/configuration>)

Was this useful?YesNo