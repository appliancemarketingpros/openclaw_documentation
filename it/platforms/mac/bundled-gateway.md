---
title: Gateway su macOS
source_url: https://docs.openclaw.ai/it/platforms/mac/bundled-gateway
scraped_at: 2026-05-25
---

OpenClaw.app non include più Node/Bun né il runtime del Gateway. L'app macOS si aspetta un'installazione **esterna** della CLI `openclaw`, non avvia il Gateway come processo figlio e gestisce un servizio launchd per utente per mantenere il Gateway in esecuzione (oppure si collega a un Gateway locale esistente, se uno è già in esecuzione).

## Installa la CLI (richiesta per la modalità locale)

Node 24 è il runtime predefinito su Mac. Node 22 LTS, attualmente `22.16+`, funziona ancora per compatibilità. Quindi installa `openclaw` globalmente:

bashCopy code
[code]
    npm install -g openclaw@<version>
[/code]

Il pulsante **Installa CLI** dell'app macOS esegue lo stesso flusso di installazione globale che l'app usa internamente: preferisce prima npm, poi pnpm, poi bun se è l'unico gestore di pacchetti rilevato. Node rimane il runtime consigliato per il Gateway.

## Launchd (Gateway come LaunchAgent)

Etichetta:

  * `ai.openclaw.gateway` (oppure `ai.openclaw.<profile>`; il legacy `com.openclaw.*` può rimanere)


Posizione del plist (per utente):

  * `~/Library/LaunchAgents/ai.openclaw.gateway.plist` (oppure `~/Library/LaunchAgents/ai.openclaw.<profile>.plist`)


Gestore:

  * L'app macOS gestisce l'installazione/aggiornamento del LaunchAgent in modalità locale.
  * Anche la CLI può installarlo: `openclaw gateway install`.


Comportamento:

  * "OpenClaw attivo" abilita/disabilita il LaunchAgent.
  * L'uscita dall'app **non** arresta il gateway (launchd lo mantiene attivo).
  * Se un Gateway è già in esecuzione sulla porta configurata, l'app si collega a esso invece di avviarne uno nuovo.


Registrazione:

  * stdout/err di launchd: `/tmp/openclaw/openclaw-gateway.log`


## Compatibilità delle versioni

L'app macOS controlla la versione del gateway rispetto alla propria versione. Se sono incompatibili, aggiorna la CLI globale in modo che corrisponda alla versione dell'app.

## Controllo smoke

bashCopy code
[code]
    openclaw --version OPENCLAW_SKIP_CHANNELS=1 \OPENCLAW_SKIP_CANVAS_HOST=1 \openclaw gateway --port 18999 --bind loopback
[/code]

Poi:

bashCopy code
[code]
    openclaw gateway call health --url ws://127.0.0.1:18999 --timeout 3000
[/code]

## Correlati

  * [App macOS](</it/platforms/macos>)
  * [Runbook del Gateway](</it/gateway>)


Was this useful?YesNo