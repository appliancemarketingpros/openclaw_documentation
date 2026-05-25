---
title: Guida introduttiva
source_url: https://docs.openclaw.ai/it/start/getting-started
scraped_at: 2026-05-25
---

Installa OpenClaw, esegui l'onboarding e chatta con il tuo assistente IA — tutto in circa 5 minuti. Alla fine avrai un Gateway in esecuzione, l'autenticazione configurata e una sessione di chat funzionante.

## Cosa ti serve

  * **Node.js** — Node 24 consigliato (supportato anche Node 22.16+)
  * **Una chiave API** da un provider di modelli (Anthropic, OpenAI, Google, ecc.) — l'onboarding te la richiederà


## Configurazione rapida

* ### Installa OpenClaw

### macOS / Linux

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash
[/code]

![Processo dello script di installazione](/assets/install-script.svg)

### Windows (PowerShell)

powershellCopy code
[code]
    iwr -useb https://openclaw.ai/install.ps1 | iex
[/code]

* ### Esegui l'onboarding

bashCopy code
[code]
    openclaw onboard --install-daemon
[/code]

La procedura guidata ti accompagna nella scelta di un provider di modelli, nell'impostazione di una chiave API e nella configurazione del Gateway. Richiede circa 2 minuti.

Vedi [Onboarding (CLI)](</it/start/wizard>) per il riferimento completo.

* ### Verifica che il Gateway sia in esecuzione

bashCopy code
[code]
    openclaw gateway status
[/code]

Dovresti vedere il Gateway in ascolto sulla porta 18789.

* ### Apri la dashboard

bashCopy code
[code]
    openclaw dashboard
[/code]

Questo apre la Control UI nel tuo browser. Se si carica, tutto funziona.

* ### Invia il tuo primo messaggio

Digita un messaggio nella chat della Control UI e dovresti ricevere una risposta dall'IA.

Vuoi invece chattare dal telefono? Il canale più veloce da configurare è [Telegram](</it/channels/telegram>) (serve solo un token bot). Vedi [Canali](</it/channels>) per tutte le opzioni.

Avanzato: monta una build personalizzata della Control UI

Se mantieni una build della dashboard localizzata o personalizzata, punta `gateway.controlUi.root` a una directory che contiene i tuoi asset statici compilati e `index.html`.

bashCopy code
[code]
    mkdir -p "$HOME/.openclaw/control-ui-custom"# Copy your built static files into that directory.
[/code]

Poi imposta:

jsonCopy code
[code]
    {"gateway": {  "controlUi": {    "enabled": true,    "root": "$HOME/.openclaw/control-ui-custom"  }}}
[/code]

Riavvia il gateway e riapri la dashboard:

bashCopy code
[code]
    openclaw gateway restartopenclaw dashboard
[/code]

## Cosa fare dopo

[**Collega un canale** Discord, Feishu, iMessage, Matrix, Microsoft Teams, Signal, Slack, Telegram, WhatsApp, Zalo e altro ancora. ](</it/channels>) [**Associazione e sicurezza** Controlla chi può inviare messaggi al tuo agent. ](</it/channels/pairing>) [**Configura il Gateway** Modelli, strumenti, sandbox e impostazioni avanzate. ](</it/gateway/configuration>) [**Sfoglia gli strumenti** Browser, exec, ricerca web, Skills e Plugin. ](</it/tools>)

Avanzato: variabili d'ambiente

Se esegui OpenClaw come account di servizio o vuoi percorsi personalizzati:

  * `OPENCLAW_HOME` — directory home per la risoluzione dei percorsi interni
  * `OPENCLAW_STATE_DIR` — sovrascrive la directory di stato
  * `OPENCLAW_CONFIG_PATH` — sovrascrive il percorso del file di configurazione


Riferimento completo: [Variabili d'ambiente](</it/help/environment>).

## Correlati

  * [Panoramica dell'installazione](</it/install>)
  * [Panoramica dei canali](</it/channels>)
  * [Configurazione](</it/start/setup>)


Was this useful?YesNo