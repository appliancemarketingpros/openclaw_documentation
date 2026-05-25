---
title: Gestire i Plugin
source_url: https://docs.openclaw.ai/it/plugins/manage-plugins
scraped_at: 2026-05-25
---

La maggior parte dei flussi di lavoro dei Plugin richiede pochi comandi: cercare, installare, riavviare il Gateway, verificare e disinstallare quando il Plugin non serve piu.

## Elenca i Plugin

bashCopy code
[code]
    openclaw plugins listopenclaw plugins list --enabledopenclaw plugins list --verboseopenclaw plugins list --json
[/code]

Usa `--json` per gli script. Include la diagnostica del registro e il `dependencyStatus` statico di ciascun Plugin quando il pacchetto del Plugin dichiara `dependencies` o `optionalDependencies`.

bashCopy code
[code]
    openclaw plugins list --json \  | jq '.plugins[] | {id, enabled, format, source, dependencyStatus}'
[/code]

`plugins list` e un controllo di inventario a freddo. Mostra cio che OpenClaw puo scoprire dalla configurazione, dai manifest e dal registro dei Plugin; non dimostra che un processo Gateway gia in esecuzione abbia importato il runtime del Plugin.

## Installa i Plugin

bashCopy code
[code]
    # Search ClawHub for plugin packages.openclaw plugins search "calendar" # Bare package specs try ClawHub first, then npm fallback.openclaw plugins install <package> # Force one source.openclaw plugins install clawhub:<package>openclaw plugins install npm:<package> # Install a specific version or dist-tag.openclaw plugins install clawhub:<package>@1.2.3openclaw plugins install clawhub:<package>@betaopenclaw plugins install npm:@scope/openclaw-plugin@1.2.3openclaw plugins install npm:@openclaw/codex # Install from git or a local development checkout.openclaw plugins install git:github.com/acme/openclaw-plugin@v1.0.0openclaw plugins install ./my-pluginopenclaw plugins install --link ./my-plugin
[/code]

Dopo aver installato il codice del Plugin, riavvia il Gateway che serve i tuoi canali:

bashCopy code
[code]
    openclaw gateway restartopenclaw plugins inspect <plugin-id> --runtime --json
[/code]

Usa `inspect --runtime` quando ti serve una prova che il Plugin abbia registrato superfici runtime come strumenti, hook, servizi, metodi Gateway o comandi CLI di proprieta del Plugin.

## Aggiorna i Plugin

bashCopy code
[code]
    openclaw plugins update <plugin-id>openclaw plugins update <npm-package-or-spec>openclaw plugins update --all
[/code]

Se un Plugin e stato installato da un dist-tag npm come `@beta`, le successive chiamate `update <plugin-id>` riutilizzano quel tag registrato. Passare una specifica npm esplicita sposta l'installazione tracciata su quella specifica per gli aggiornamenti futuri.

bashCopy code
[code]
    openclaw plugins update @scope/openclaw-plugin@betaopenclaw plugins update @scope/openclaw-plugin
[/code]

Il secondo comando riporta un Plugin alla linea di rilascio predefinita del registro quando era stato precedentemente fissato a una versione esatta o a un tag.

Quando `openclaw update` viene eseguito sul canale beta, i record dei Plugin npm e ClawHub della linea predefinita provano prima la release `@beta` del Plugin corrispondente. Se quella release beta non esiste, OpenClaw torna alla specifica predefinita/latest registrata. Per i Plugin npm, OpenClaw torna indietro anche quando il pacchetto beta esiste ma non supera la validazione dell'installazione. Le versioni esatte e i tag espliciti come `@rc` o `@beta` vengono preservati.

## Disinstalla i Plugin

bashCopy code
[code]
    openclaw plugins uninstall <plugin-id> --dry-runopenclaw plugins uninstall <plugin-id>openclaw plugins uninstall <plugin-id> --keep-filesopenclaw gateway restart
[/code]

La disinstallazione rimuove la voce di configurazione del Plugin, il record dell'indice dei Plugin, le voci delle liste allow/deny e, quando applicabile, i percorsi di caricamento collegati. Le directory di installazione gestite vengono rimosse a meno che non passi `--keep-files`.

In modalita Nix (`OPENCLAW_NIX_MODE=1`), i comandi di installazione, aggiornamento, disinstallazione, abilitazione e disabilitazione dei Plugin sono disabilitati. Gestisci invece queste scelte nella sorgente Nix dell'installazione; per nix-openclaw, usa la [Guida rapida](<https://github.com/openclaw/nix-openclaw#quick-start>) agent-first.

## Pubblica i Plugin

Puoi pubblicare Plugin esterni su [ClawHub](<https://clawhub.ai>), [npmjs.com](<http://npmjs.com>) o entrambi.

### Pubblica su ClawHub

ClawHub e la superficie primaria di scoperta pubblica per i Plugin OpenClaw. Offre agli utenti metadati ricercabili, cronologia delle versioni e risultati delle scansioni del registro prima dell'installazione.

bashCopy code
[code]
    npm i -g clawhubclawhub loginclawhub package publish your-org/your-plugin --dry-runclawhub package publish your-org/your-pluginclawhub package publish your-org/your-plugin@v1.0.0
[/code]

Gli utenti installano da ClawHub con:

bashCopy code
[code]
    openclaw plugins install clawhub:<package>openclaw plugins install <package>
[/code]

La forma senza prefisso controlla comunque prima ClawHub.

### Pubblica su [npmjs.com](<http://npmjs.com>)

I Plugin npm nativi devono includere un manifest del Plugin e i metadati dell'entrypoint OpenClaw in `package.json`.

package.jsonCopy code
[code]
    {  "name": "@acme/openclaw-plugin",  "version": "1.0.0",  "type": "module",  "openclaw": {    "extensions": ["./dist/index.js"]  }}
[/code]

bashCopy code
[code]
    npm publish --access public
[/code]

Gli utenti installano solo da npm con:

bashCopy code
[code]
    openclaw plugins install npm:@acme/openclaw-pluginopenclaw plugins install npm:@acme/openclaw-plugin@betaopenclaw plugins install npm:@acme/openclaw-plugin@1.0.0
[/code]

Se lo stesso pacchetto e disponibile anche su ClawHub, `npm:` salta la ricerca su ClawHub e forza la risoluzione npm.

## Scelta della sorgente

  * **ClawHub** : usalo quando vuoi scoperta nativa OpenClaw, riepiloghi delle scansioni, versioni e suggerimenti di installazione.
  * **[npmjs.com](<http://npmjs.com>)** : usalo quando distribuisci gia pacchetti JavaScript o hai bisogno di flussi di lavoro con dist-tag/registri privati npm.
  * **Git** : usalo quando vuoi installare direttamente da un branch, un tag o un commit.
  * **Percorso locale** : usalo quando sviluppi o testi un Plugin sulla stessa macchina.


## Correlati

  * [Plugin](</it/tools/plugin>) \- panoramica e risoluzione dei problemi
  * [`openclaw plugins`](</it/cli/plugins>) \- riferimento CLI completo
  * [ClawHub](</it/clawhub/cli>) \- pubblicazione e operazioni sul registro
  * [Creare Plugin](</it/plugins/building-plugins>) \- crea un pacchetto Plugin
  * [Manifest del Plugin](</it/plugins/manifest>) \- manifest e metadati del pacchetto


Was this useful?YesNo