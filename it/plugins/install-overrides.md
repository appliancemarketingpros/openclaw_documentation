---
title: Override di installazione dei Plugin
source_url: https://docs.openclaw.ai/it/plugins/install-overrides
scraped_at: 2026-05-25
---

Gli override di installazione dei Plugin consentono ai maintainer di testare le installazioni dei Plugin al momento della configurazione rispetto a uno specifico pacchetto npm o a un tarball locale prodotto con npm-pack. Sono destinati solo alla validazione E2E e dei pacchetti. Gli utenti normali dovrebbero installare i Plugin con [`openclaw plugins install`](</it/cli/plugins>).

## Ambiente

Gli override sono disabilitati a meno che entrambe le variabili siano impostate:

bashCopy code
[code]
    export OPENCLAW_ALLOW_PLUGIN_INSTALL_OVERRIDES=1export OPENCLAW_PLUGIN_INSTALL_OVERRIDES='{  "codex": "npm-pack:/tmp/openclaw-codex-2026.5.8.tgz",  "openclaw-web-search": "npm:@openclaw/web-search@2026.5.8"}'
[/code]

La mappa degli override è JSON indicizzato per id del Plugin. I valori supportano:

  * `npm:<registry-spec>` per pacchetti di registro e versioni esatte o tag
  * `npm-pack:<path.tgz>` per tarball locali prodotti da `npm pack`


I percorsi relativi `npm-pack:` vengono risolti dalla directory di lavoro corrente.

## Comportamento

Quando un flusso al momento della configurazione richiede di installare un Plugin il cui id compare nella mappa, OpenClaw usa la sorgente di override invece della sorgente npm da catalogo, inclusa nel bundle o predefinita. Questo si applica all'onboarding e ad altri flussi che usano il programma condiviso di installazione dei Plugin al momento della configurazione.

Gli override applicano comunque l'id del Plugin previsto. Un tarball mappato a `codex` deve installare un Plugin il cui id nel manifest è `codex`.

Gli override non ereditano lo stato ufficiale di sorgente attendibile. Anche quando la voce del catalogo rappresenta normalmente un pacchetto di proprietà di OpenClaw, un override viene trattato come input di test fornito dall'operatore.

I file `.env` del workspace non possono abilitare gli override di installazione. Imposta queste variabili nella shell attendibile, nel job CI o nel comando di test remoto che avvia OpenClaw.

## E2E pacchetto

Usa una directory di stato isolata in modo che le installazioni dei pacchetti e i record di installazione non tocchino il tuo normale stato di OpenClaw:

bashCopy code
[code]
    npm pack extensions/codex --pack-destination /tmp OPENCLAW_STATE_DIR="$(mktemp -d)" \OPENCLAW_ALLOW_PLUGIN_INSTALL_OVERRIDES=1 \OPENCLAW_PLUGIN_INSTALL_OVERRIDES='{"codex":"npm-pack:/tmp/openclaw-codex-2026.5.8.tgz"}' \pnpm openclaw onboard --mode local
[/code]

Verifica il pacchetto installato nella directory di stato:

bashCopy code
[code]
    find "$OPENCLAW_STATE_DIR/npm/node_modules" -maxdepth 3 -name package.json -printgrep -R '"@openclaw/codex"' "$OPENCLAW_STATE_DIR/npm/package-lock.json"
[/code]

Per E2E con provider live, carica la chiave API reale da una shell attendibile o da un segreto CI prima di avviare il comando di test. Non stampare le chiavi; riporta solo la sorgente e se la chiave era presente.

Was this useful?YesNo