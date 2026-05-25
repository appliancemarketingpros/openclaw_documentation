---
title: Perplexity
source_url: https://docs.openclaw.ai/it/providers/perplexity-provider
scraped_at: 2026-05-25
---

Il Plugin Perplexity fornisce funzionalità di ricerca web tramite l'API di ricerca Perplexity o Perplexity Sonar tramite OpenRouter.

Proprietà | Valore  
---|---  
Tipo | Provider di ricerca web (non un provider di modelli)  
Autenticazione | `PERPLEXITY_API_KEY` (diretta) o `OPENROUTER_API_KEY` (tramite OpenRouter)  
Percorso config | `plugins.entries.perplexity.config.webSearch.apiKey`  
  
## Per iniziare

* ### Imposta la chiave API

Esegui il flusso interattivo di configurazione della ricerca web:

bashCopy code
[code]
    openclaw configure --section web
[/code]

Oppure imposta direttamente la chiave:

bashCopy code
[code]
    openclaw config set plugins.entries.perplexity.config.webSearch.apiKey "pplx-xxxxxxxxxxxx"
[/code]

* ### Inizia a cercare

L'agente userà automaticamente Perplexity per le ricerche web una volta che la chiave è configurata. Non sono necessari passaggi aggiuntivi.

## Modalità di ricerca

Il Plugin seleziona automaticamente il trasporto in base al prefisso della chiave API:

### API Perplexity nativa (pplx-)

Quando la tua chiave inizia con `pplx-`, OpenClaw usa l'API di ricerca Perplexity nativa. Questo trasporto restituisce risultati strutturati e supporta filtri per dominio, lingua e data (vedi le opzioni di filtro sotto).

### OpenRouter / Sonar (sk-or-)

Quando la tua chiave inizia con `sk-or-`, OpenClaw instrada tramite OpenRouter usando il modello Perplexity Sonar. Questo trasporto restituisce risposte sintetizzate dall'IA con citazioni.

Prefisso chiave | Trasporto | Funzionalità  
---|---|---  
`pplx-` | API di ricerca Perplexity nativa | Risultati strutturati, filtri dominio/lingua/data  
`sk-or-` | OpenRouter (Sonar) | Risposte sintetizzate dall'IA con citazioni  
  
## Filtri dell'API nativa

Quando usi l'API Perplexity nativa, le ricerche supportano i seguenti filtri:

Filtro | Descrizione | Esempio  
---|---|---  
Paese | Codice paese a 2 lettere | `us`, `de`, `jp`  
Lingua | Codice lingua ISO 639-1 | `en`, `fr`, `zh`  
Intervallo di date | Finestra di recenza | `day`, `week`, `month`, `year`  
Filtri dominio | Allowlist o denylist (massimo 20 domini) | `example.com`  
Budget contenuto | Limiti di token per risposta / per pagina | `max_tokens`, `max_tokens_per_page`  
  
## Configurazione avanzata

Variabile d'ambiente per processi daemon

Se il Gateway OpenClaw viene eseguito come daemon (launchd/systemd), assicurati che `PERPLEXITY_API_KEY` sia disponibile per quel processo.

Configurazione proxy OpenRouter

Se preferisci instradare le ricerche Perplexity tramite OpenRouter, imposta una `OPENROUTER_API_KEY` (prefisso `sk-or-`) invece di una chiave Perplexity nativa. OpenClaw rileverà il prefisso e passerà automaticamente al trasporto Sonar.

## Correlati

[**Strumento di ricerca Perplexity** Come l'agente invoca le ricerche Perplexity e interpreta i risultati. ](</it/tools/perplexity-search>) [**Riferimento di configurazione** Riferimento completo della configurazione, incluse le voci Plugin. ](</it/gateway/configuration-reference>)

Was this useful?YesNo