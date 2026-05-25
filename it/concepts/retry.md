---
title: Politica di ripetizione
source_url: https://docs.openclaw.ai/it/concepts/retry
scraped_at: 2026-05-25
---

## Obiettivi

  * Riprovare per ogni richiesta HTTP, non per ogni flusso a più passaggi.
  * Preservare l'ordine riprovando solo il passaggio corrente.
  * Evitare di duplicare operazioni non idempotenti.


## Valori predefiniti

  * Tentativi: 3
  * Limite massimo del ritardo: 30000 ms
  * Variabilità casuale: 0.1 (10 percento)
  * Valori predefiniti dei provider: 
    * Ritardo minimo Telegram: 400 ms
    * Ritardo minimo Discord: 500 ms


## Comportamento

### Provider di modelli

  * OpenClaw lascia che gli SDK dei provider gestiscano i normali retry brevi.
  * Per gli SDK basati su Stainless, come Anthropic e OpenAI, le risposte retryable (`408`, `409`, `429` e `5xx`) possono includere `retry-after-ms` o `retry-after`. Quando quell'attesa è superiore a 60 secondi, OpenClaw inserisce `x-should-retry: false` così l'SDK espone immediatamente l'errore e il failover del modello può passare a un altro profilo di autenticazione o modello di fallback.
  * Sovrascrivi il limite con `OPENCLAW_SDK_RETRY_MAX_WAIT_SECONDS=<seconds>`. Impostalo su `0`, `false`, `off`, `none` o `disabled` per lasciare che gli SDK rispettino internamente le lunghe attese `Retry-After`.


### Discord

  * Riprova in caso di errori di limite di frequenza (HTTP 429), timeout delle richieste, risposte HTTP 5xx ed errori di trasporto transitori come errori di risoluzione DNS, reset della connessione, chiusure di socket ed errori di fetch.
  * Usa `retry_after` di Discord quando disponibile, altrimenti il backoff esponenziale.


### Telegram

  * Riprova in caso di errori transitori (429, timeout, connessione/reset/chiusura, temporaneamente non disponibile).
  * Usa `retry_after` quando disponibile, altrimenti il backoff esponenziale.
  * Gli errori di parsing Markdown non vengono ritentati; usano il testo normale come fallback.


## Configurazione

Imposta la policy di retry per provider in `~/.openclaw/openclaw.json`:

json5Copy code
[code]
    {  channels: {    telegram: {      retry: {        attempts: 3,        minDelayMs: 400,        maxDelayMs: 30000,        jitter: 0.1,      },    },    discord: {      retry: {        attempts: 3,        minDelayMs: 500,        maxDelayMs: 30000,        jitter: 0.1,      },    },  },}
[/code]

## Note

  * I retry si applicano per richiesta (invio di messaggi, caricamento di media, reazione, sondaggio, sticker).
  * I flussi compositi non riprovano i passaggi completati.


## Correlati

  * [Failover del modello](</it/concepts/model-failover>)
  * [Coda dei comandi](</it/concepts/queue>)


Was this useful?YesNo