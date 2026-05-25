---
title: Ricerca SearXNG
source_url: https://docs.openclaw.ai/it/tools/searxng-search
scraped_at: 2026-05-25
---

OpenClaw supporta [SearXNG](<https://docs.searxng.org/>) come provider `web_search` **autogestito, senza chiave**. SearXNG è un metamotore di ricerca open source che aggrega risultati da Google, Bing, DuckDuckGo e altre fonti.

Vantaggi:

  * **Gratuito e illimitato** \-- non richiede una chiave API o un abbonamento commerciale
  * **Privacy / isolamento** \-- le query non lasciano mai la tua rete
  * **Funziona ovunque** \-- nessuna restrizione regionale sulle API di ricerca commerciali


## Configurazione

* ### Esegui un'istanza SearXNG

bashCopy code
[code]
    docker run -d -p 8888:8080 searxng/searxng
[/code]

Oppure usa qualsiasi distribuzione SearXNG esistente a cui hai accesso. Consulta la [documentazione di SearXNG](<https://docs.searxng.org/>) per la configurazione in produzione.

* ### Configura

bashCopy code
[code]
    openclaw configure --section web# Select "searxng" as the provider
[/code]

Oppure imposta la variabile d'ambiente e lascia che il rilevamento automatico la trovi:

bashCopy code
[code]
    export SEARXNG_BASE_URL="http://localhost:8888"
[/code]

## Configurazione

json5Copy code
[code]
    {  tools: {    web: {      search: {        provider: "searxng",      },    },  },}
[/code]

Impostazioni a livello di Plugin per l'istanza SearXNG:

json5Copy code
[code]
    {  plugins: {    entries: {      searxng: {        config: {          webSearch: {            baseUrl: "http://localhost:8888",            categories: "general,news", // optional            language: "en", // optional          },        },      },    },  },}
[/code]

Il campo `baseUrl` accetta anche oggetti SecretRef.

Regole di trasporto:

  * `https://` funziona per host SearXNG pubblici o privati
  * `http://` è accettato solo per host di rete privata attendibili o loopback
  * gli host SearXNG pubblici devono usare `https://`
  * gli host privati/interni usano la protezione di rete autogestita; gli host pubblici `https://` restano sulla protezione rigorosa per la ricerca web e non possono reindirizzare a indirizzi privati


## Variabile d'ambiente

Imposta `SEARXNG_BASE_URL` come alternativa alla configurazione:

bashCopy code
[code]
    export SEARXNG_BASE_URL="http://localhost:8888"
[/code]

Quando `SEARXNG_BASE_URL` è impostata e non è configurato alcun provider esplicito, il rilevamento automatico sceglie SearXNG automaticamente (con la priorità più bassa -- qualsiasi provider basato su API con una chiave vince per primo).

## Riferimento alla configurazione del Plugin

Campo | Descrizione  
---|---  
`baseUrl` | URL di base della tua istanza SearXNG (obbligatorio)  
`categories` | Categorie separate da virgole come `general`, `news` o `science`  
`language` | Codice lingua per i risultati come `en`, `de` o `fr`  
  
## Note

  * **API JSON** \-- usa l'endpoint nativo `format=json` di SearXNG, non lo scraping HTML
  * **URL dei risultati immagine** \-- i risultati della categoria immagini includono `img_src` quando SearXNG restituisce un URL immagine diretto
  * **Nessuna chiave API** \-- funziona subito con qualsiasi istanza SearXNG
  * **Convalida dell'URL di base** \-- `baseUrl` deve essere un URL `http://` o `https://` valido; gli host pubblici devono usare `https://`
  * **Protezione di rete** \-- gli endpoint SearXNG privati/interni aderiscono all'accesso alla rete privata; gli endpoint SearXNG pubblici `https://` mantengono una protezione SSRF rigorosa
  * **Ordine del rilevamento automatico** \-- SearXNG viene controllato per ultimo (ordine 200) nel rilevamento automatico. I provider basati su API con chiavi configurate vengono eseguiti per primi, poi DuckDuckGo (ordine 100), poi Ollama Web Search (ordine 110)
  * **Autogestito** \-- controlli l'istanza, le query e i motori di ricerca upstream
  * **Categorie** usa `general` come valore predefinito quando non configurato
  * **Fallback della categoria** \-- se una richiesta per una categoria diversa da `general` riesce ma restituisce zero risultati, OpenClaw riprova la stessa query una volta con `general` prima di restituire un set di risultati vuoto


## Correlati

  * [Panoramica di Web Search](</it/tools/web>) \-- tutti i provider e il rilevamento automatico
  * [DuckDuckGo Search](</it/tools/duckduckgo-search>) \-- un altro fallback senza chiave
  * [Brave Search](</it/tools/brave-search>) \-- risultati strutturati con piano gratuito


Was this useful?YesNo