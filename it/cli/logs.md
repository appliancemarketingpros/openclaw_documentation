---
title: Log
source_url: https://docs.openclaw.ai/it/cli/logs
scraped_at: 2026-05-25
---

# `openclaw logs`

Segui in coda i log su file del Gateway tramite RPC (funziona in modalità remota).

Correlati:

  * Panoramica della registrazione: [Registrazione](</it/logging>)
  * CLI Gateway: [gateway](</it/cli/gateway>)


## Opzioni

  * `--limit <n>`: numero massimo di righe di log da restituire (predefinito `200`)
  * `--max-bytes <n>`: byte massimi da leggere dal file di log (predefinito `250000`)
  * `--follow`: segue il flusso dei log
  * `--interval <ms>`: intervallo di polling durante il follow (predefinito `1000`)
  * `--json`: emette eventi JSON delimitati da righe
  * `--plain`: output in testo semplice senza formattazione stilizzata
  * `--no-color`: disabilita i colori ANSI
  * `--local-time`: renderizza i timestamp nel tuo fuso orario locale


## Opzioni RPC Gateway condivise

`openclaw logs` accetta anche i flag standard del client Gateway:

  * `--url <url>`: URL WebSocket del Gateway
  * `--token <token>`: token del Gateway
  * `--timeout <ms>`: timeout in ms (predefinito `30000`)
  * `--expect-final`: attende una risposta finale quando la chiamata al Gateway è supportata da un agent


Quando passi `--url`, la CLI non applica automaticamente le credenziali di configurazione o di ambiente. Includi `--token` esplicitamente se il Gateway di destinazione richiede autenticazione.

## Esempi

bashCopy code
[code]
    openclaw logsopenclaw logs --followopenclaw logs --follow --interval 2000openclaw logs --limit 500 --max-bytes 500000openclaw logs --jsonopenclaw logs --plainopenclaw logs --no-coloropenclaw logs --limit 500openclaw logs --local-timeopenclaw logs --follow --local-timeopenclaw logs --url ws://127.0.0.1:18789 --token "$OPENCLAW_GATEWAY_TOKEN"
[/code]

## Note

  * Usa `--local-time` per renderizzare i timestamp nel tuo fuso orario locale.
  * Se il Gateway local loopback implicito richiede l'abbinamento, si chiude durante la connessione o va in timeout prima che `logs.tail` risponda, `openclaw logs` ripiega automaticamente sul log su file del Gateway configurato. Le destinazioni `--url` esplicite non usano questo fallback.
  * Quando usi `--follow`, le disconnessioni transitorie del gateway (chiusura WebSocket, timeout, interruzione della connessione) attivano la riconnessione automatica con backoff esponenziale (fino a 8 tentativi, con limite di 30 s tra i tentativi). A ogni tentativo viene stampato un avviso su stderr e, quando un polling riesce, viene stampata una notifica `[logs] gateway reconnected`. In modalità `--json`, sia l'avviso di nuovo tentativo sia la transizione di riconnessione vengono emessi come record `{"type":"notice"}` su stderr. Gli errori non recuperabili (errore di autenticazione, configurazione errata) terminano comunque immediatamente.


## Correlati

  * [Riferimento CLI](</it/cli>)
  * [Registrazione del Gateway](</it/gateway/logging>)


Was this useful?YesNo