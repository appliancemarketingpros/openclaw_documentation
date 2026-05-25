---
title: Canale QA
source_url: https://docs.openclaw.ai/it/channels/qa-channel
scraped_at: 2026-05-25
---

`qa-channel` è un trasporto di messaggi sintetico incluso per la QA automatizzata di OpenClaw. Non è un canale di produzione: esiste per esercitare lo stesso confine del Plugin di canale usato dai trasporti reali, mantenendo al tempo stesso lo stato deterministico e completamente ispezionabile.

## Cosa fa

  * Grammatica dei target in stile Slack: 
    * `dm:<user>`
    * `channel:<room>`
    * `group:<room>`
    * `thread:<room>/<thread>`
  * Le conversazioni condivise `channel:` e `group:` vengono esposte agli agenti come turni di stanze gruppo/canale, quindi esercitano la stessa policy di routing per risposte visibili e strumenti di messaggistica usata da Discord, Slack, Telegram e trasporti simili.
  * Bus sintetico basato su HTTP per iniezione di messaggi in ingresso, acquisizione della trascrizione in uscita, creazione di thread, reazioni, modifiche, eliminazioni e azioni di ricerca/lettura.
  * Runner di autoverifica lato host che scrive un report Markdown in `.artifacts/qa-e2e/`.


## Configurazione

jsonCopy code
[code]
    {  "channels": {    "qa-channel": {      "baseUrl": "http://127.0.0.1:43123",      "botUserId": "openclaw",      "botDisplayName": "OpenClaw QA",      "allowFrom": ["*"],      "pollTimeoutMs": 1000    }  }}
[/code]

Chiavi dell'account:

  * `enabled` \- interruttore principale per questo account.
  * `name` \- etichetta di visualizzazione opzionale.
  * `baseUrl` \- URL del bus sintetico.
  * `botUserId` \- id utente del bot in stile Matrix usato nella grammatica dei target.
  * `botDisplayName` \- nome visualizzato per i messaggi in uscita.
  * `pollTimeoutMs` \- finestra di attesa long-poll. Intero tra 100 e 30000.
  * `allowFrom` \- allowlist dei mittenti (id utente o `"*"`). I messaggi diretti e la policy di gruppo con allowlist usano entrambi questi id mittente sintetici.
  * `groupPolicy` \- policy delle stanze condivise: `"open"` (predefinita), `"allowlist"` o `"disabled"`.
  * `groupAllowFrom` \- allowlist opzionale dei mittenti per le stanze condivise. Quando è omessa con `"allowlist"`, QA Channel ripiega su `allowFrom`.
  * `groups.<room>.requireMention` \- richiede una menzione del bot prima di rispondere in una stanza gruppo/canale specifica. `groups."*"` imposta il valore predefinito.
  * `defaultTo` \- target di fallback quando non ne viene fornito nessuno.
  * `actions.messages` / `actions.reactions` / `actions.search` / `actions.threads` \- gating degli strumenti per azione.


Chiavi multi-account al livello superiore:

  * `accounts` \- record di override per account denominati, indicizzati per id account.
  * `defaultAccount` \- id account preferito quando ne sono configurati più di uno.


## Runner

Autoverifica lato host (scrive un report Markdown in `.artifacts/qa-e2e/`):

bashCopy code
[code]
    pnpm qa:e2e
[/code]

Questo passa attraverso `qa-lab`, avvia il bus QA interno al repository, esegue il boot della slice runtime `qa-channel` inclusa ed esegue un'autoverifica deterministica.

Suite completa di scenari basata sul repository:

bashCopy code
[code]
    pnpm openclaw qa suite
[/code]

Esegue scenari in parallelo sulla lane del Gateway QA. Vedi [Panoramica QA](</it/concepts/qa-e2e-automation>) per scenari, profili e modalità provider.

Sito QA basato su Docker (Gateway + UI del debugger QA Lab in un unico stack):

bashCopy code
[code]
    pnpm qa:lab:up
[/code]

Compila il sito QA, avvia lo stack Gateway + QA Lab basato su Docker e stampa l'URL di QA Lab. Da lì puoi scegliere scenari, selezionare la lane del modello, avviare esecuzioni individuali e osservare i risultati in tempo reale. Il debugger QA Lab è separato dal bundle Control UI distribuito.

## Correlati

  * [Panoramica QA](</it/concepts/qa-e2e-automation>) \- stack complessivo, adattatori di trasporto, authoring degli scenari
  * [QA Matrix](</it/concepts/qa-matrix>) \- esempio di runner con trasporto live che pilota un canale reale
  * [Abbinamento](</it/channels/pairing>)
  * [Gruppi](</it/channels/groups>)
  * [Panoramica dei canali](</it/channels>)


Was this useful?YesNo