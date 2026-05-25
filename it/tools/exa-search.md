---
title: Ricerca Exa
source_url: https://docs.openclaw.ai/it/tools/exa-search
scraped_at: 2026-05-25
---

OpenClaw supporta [Exa AI](<https://exa.ai/>) come provider `web_search`. Exa offre modalità di ricerca neurale, per parole chiave e ibrida con estrazione dei contenuti integrata (evidenziazioni, testo, riassunti).

## Ottieni una chiave API

* ### Crea un account

Registrati su [exa.ai](<https://exa.ai/>) e genera una chiave API dal tuo pannello di controllo.

* ### Archivia la chiave

Imposta `EXA_API_KEY` nell'ambiente del Gateway oppure configura tramite:

bashCopy code
[code]
    openclaw configure --section web
[/code]

## Configurazione

json5Copy code
[code]
    {  plugins: {    entries: {      exa: {        config: {          webSearch: {            apiKey: "exa-...", // optional if EXA_API_KEY is set            baseUrl: "https://api.exa.ai", // optional; OpenClaw appends /search          },        },      },    },  },  tools: {    web: {      search: {        provider: "exa",      },    },  },}
[/code]

**Alternativa con ambiente:** imposta `EXA_API_KEY` nell'ambiente del Gateway. Per un'installazione del Gateway, inseriscila in `~/.openclaw/.env`.

## Override dell'URL di base

Imposta `plugins.entries.exa.config.webSearch.baseUrl` quando le richieste di ricerca Exa devono passare attraverso un proxy compatibile o un endpoint Exa alternativo. OpenClaw normalizza gli host semplici anteponendo `https://` e aggiunge `/search` a meno che il percorso non termini già così. L'endpoint risolto è incluso nella chiave della cache di ricerca, quindi i risultati da endpoint Exa diversi non vengono condivisi.

## Parametri dello strumento

Query di ricerca.

Risultati da restituire (1–100).

Modalità di ricerca.

Filtro temporale.

Risultati successivi a questa data (`YYYY-MM-DD`).

Risultati precedenti a questa data (`YYYY-MM-DD`).

Opzioni di estrazione dei contenuti (vedi sotto).

### Estrazione dei contenuti

Exa può restituire contenuti estratti insieme ai risultati di ricerca. Passa un oggetto `contents` per abilitare:

javascriptCopy code
[code]
    await web_search({  query: "transformer architecture explained",  type: "neural",  contents: {    text: true, // full page text    highlights: { numSentences: 3 }, // key sentences    summary: true, // AI summary  },});
[/code]

Opzione contents | Tipo | Descrizione  
---|---|---  
`text` | `boolean | { maxCharacters }` | Estrae il testo completo della pagina  
`highlights` | `boolean | { maxCharacters, query, numSentences, highlightsPerUrl }` | Estrae le frasi chiave  
`summary` | `boolean | { query }` | Riassunto generato dall'AI  
  
### Modalità di ricerca

Modalità | Descrizione  
---|---  
`auto` | Exa sceglie la modalità migliore (predefinita)  
`neural` | Ricerca semantica/basata sul significato  
`fast` | Ricerca rapida per parole chiave  
`deep` | Ricerca approfondita completa  
`deep-reasoning` | Ricerca approfondita con reasoning  
`instant` | Risultati più rapidi  
  
## Note

  * Se non viene fornita alcuna opzione `contents`, Exa usa come impostazione predefinita `{ highlights: true }`, così i risultati includono estratti di frasi chiave
  * I risultati preservano i campi `highlightScores` e `summary` dalla risposta dell'API Exa quando disponibili
  * Le descrizioni dei risultati vengono ricavate prima dalle evidenziazioni, poi dal riassunto, poi dal testo completo, a seconda di ciò che è disponibile
  * `freshness` e `date_after`/`date_before` non possono essere combinati: usa una sola modalità di filtro temporale
  * È possibile restituire fino a 100 risultati per query (soggetto ai limiti del tipo di ricerca Exa)
  * I risultati vengono memorizzati nella cache per 15 minuti per impostazione predefinita (configurabile tramite `cacheTtlMinutes`)
  * Exa è un'integrazione API ufficiale con risposte JSON strutturate


## Correlati

  * [Panoramica di Web Search](</it/tools/web>) \-- tutti i provider e rilevamento automatico
  * [Brave Search](</it/tools/brave-search>) \-- risultati strutturati con filtri per paese/lingua
  * [Perplexity Search](</it/tools/perplexity-search>) \-- risultati strutturati con filtro per dominio


Was this useful?YesNo