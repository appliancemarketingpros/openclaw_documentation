---
title: Ricerca DuckDuckGo
source_url: https://docs.openclaw.ai/it/tools/duckduckgo-search
scraped_at: 2026-05-25
---

OpenClaw supporta DuckDuckGo come provider `web_search` **senza chiave**. Non sono richiesti una chiave API o un account.

## Configurazione

Non è necessaria alcuna chiave API - imposta semplicemente DuckDuckGo come provider:

* ### Configura

bashCopy code
[code]
    openclaw configure --section web# Select "duckduckgo" as the provider
[/code]

## Configurazione

json5Copy code
[code]
    {  tools: {    web: {      search: {        provider: "duckduckgo",      },    },  },}
[/code]

Impostazioni opzionali a livello di plugin per area geografica e SafeSearch:

json5Copy code
[code]
    {  plugins: {    entries: {      duckduckgo: {        config: {          webSearch: {            region: "us-en", // DuckDuckGo region code            safeSearch: "moderate", // "strict", "moderate", or "off"          },        },      },    },  },}
[/code]

## Parametri dello strumento

Query di ricerca.

Risultati da restituire (1-10).

Codice area geografica DuckDuckGo (ad es. `us-en`, `uk-en`, `de-de`).

Livello SafeSearch.

Area geografica e SafeSearch possono essere impostati anche nella configurazione del plugin (vedi sopra) - i parametri dello strumento sovrascrivono i valori di configurazione per ogni query.

## Note

  * **Nessuna chiave API** \- funziona subito, senza configurazione
  * **Sperimentale** \- raccoglie risultati dalle pagine HTML non JavaScript di ricerca di DuckDuckGo, non da un'API o SDK ufficiale
  * **Rischio di verifica anti-bot** \- DuckDuckGo può mostrare CAPTCHA o bloccare le richieste in caso di uso intenso o automatizzato
  * **Parsing HTML** \- i risultati dipendono dalla struttura della pagina, che può cambiare senza preavviso
  * **Ordine di rilevamento automatico** \- DuckDuckGo è il primo fallback senza chiave (ordine 100) nel rilevamento automatico. I provider basati su API con chiavi configurate vengono eseguiti per primi, poi Ollama Web Search (ordine 110), poi SearXNG (ordine 200)
  * **SafeSearch ha come valore predefinito moderate** quando non è configurato


## Correlati

  * [Panoramica Web Search](</it/tools/web>) \-- tutti i provider e il rilevamento automatico
  * [Brave Search](</it/tools/brave-search>) \-- risultati strutturati con piano gratuito
  * [Exa Search](</it/tools/exa-search>) \-- ricerca neurale con estrazione dei contenuti


Was this useful?YesNo