---
title: CLI dell'ambiente isolato
source_url: https://docs.openclaw.ai/it/cli/sandbox
scraped_at: 2026-05-25
---

Gestisci i runtime sandbox per l'esecuzione isolata degli agenti.

## Panoramica

OpenClaw può eseguire gli agenti in runtime sandbox isolati per sicurezza. I comandi `sandbox` ti aiutano a ispezionare e ricreare questi runtime dopo aggiornamenti o modifiche alla configurazione.

Oggi questo di solito significa:

  * container sandbox Docker
  * runtime sandbox SSH quando `agents.defaults.sandbox.backend = "ssh"`
  * runtime sandbox OpenShell quando `agents.defaults.sandbox.backend = "openshell"`


Per `ssh` e OpenShell `remote`, la ricreazione conta più che con Docker:

  * la workspace remota è canonica dopo il seed iniziale
  * `openclaw sandbox recreate` elimina quella workspace remota canonica per l'ambito selezionato
  * l'uso successivo la sottopone di nuovo a seed dalla workspace locale corrente


## Comandi

### `openclaw sandbox explain`

Ispeziona la modalità, l'ambito, l'accesso alla workspace, la policy degli strumenti sandbox e i gate elevati **effettivi** (con percorsi delle chiavi di configurazione per la correzione).

bashCopy code
[code]
    openclaw sandbox explainopenclaw sandbox explain --session agent:main:mainopenclaw sandbox explain --agent workopenclaw sandbox explain --json
[/code]

### `openclaw sandbox list`

Elenca tutti i runtime sandbox con il loro stato e la loro configurazione.

bashCopy code
[code]
    openclaw sandbox listopenclaw sandbox list --browser  # List only browser containersopenclaw sandbox list --json     # JSON output
[/code]

**L'output include:**

  * Nome e stato del runtime
  * Backend (`docker`, `openshell`, ecc.)
  * Etichetta di configurazione e se corrisponde alla configurazione corrente
  * Età (tempo dalla creazione)
  * Tempo di inattività (tempo dall'ultimo utilizzo)
  * Sessione/agente associato


### `openclaw sandbox recreate`

Rimuovi i runtime sandbox per forzarne la ricreazione con la configurazione aggiornata.

bashCopy code
[code]
    openclaw sandbox recreate --all                # Recreate all containersopenclaw sandbox recreate --session main       # Specific sessionopenclaw sandbox recreate --agent mybot        # Specific agentopenclaw sandbox recreate --browser            # Only browser containersopenclaw sandbox recreate --all --force        # Skip confirmation
[/code]

**Opzioni:**

  * `--all`: ricrea tutti i container sandbox
  * `--session <key>`: ricrea il container per una sessione specifica
  * `--agent <id>`: ricrea i container per un agente specifico
  * `--browser`: ricrea solo i container del browser
  * `--force`: salta la richiesta di conferma


## Casi d'uso

### Dopo l'aggiornamento di un'immagine Docker

bashCopy code
[code]
    # Pull new imagedocker pull openclaw-sandbox:latestdocker tag openclaw-sandbox:latest openclaw-sandbox:bookworm-slim # Update config to use new image# Edit config: agents.defaults.sandbox.docker.image (or agents.list[].sandbox.docker.image) # Recreate containersopenclaw sandbox recreate --all
[/code]

### Dopo la modifica della configurazione sandbox

bashCopy code
[code]
    # Edit config: agents.defaults.sandbox.* (or agents.list[].sandbox.*) # Recreate to apply new configopenclaw sandbox recreate --all
[/code]

### Dopo la modifica della destinazione SSH o del materiale di autenticazione SSH

bashCopy code
[code]
    # Edit config:# - agents.defaults.sandbox.backend# - agents.defaults.sandbox.ssh.target# - agents.defaults.sandbox.ssh.workspaceRoot# - agents.defaults.sandbox.ssh.identityFile / certificateFile / knownHostsFile# - agents.defaults.sandbox.ssh.identityData / certificateData / knownHostsData openclaw sandbox recreate --all
[/code]

Per il backend `ssh` core, la ricreazione elimina la radice della workspace remota per ambito sulla destinazione SSH. L'esecuzione successiva la sottopone di nuovo a seed dalla workspace locale.

### Dopo la modifica di origine, policy o modalità OpenShell

bashCopy code
[code]
    # Edit config:# - agents.defaults.sandbox.backend# - plugins.entries.openshell.config.from# - plugins.entries.openshell.config.mode# - plugins.entries.openshell.config.policy openclaw sandbox recreate --all
[/code]

Per la modalità OpenShell `remote`, la ricreazione elimina la workspace remota canonica per quell'ambito. L'esecuzione successiva la sottopone di nuovo a seed dalla workspace locale.

### Dopo la modifica di setupCommand

bashCopy code
[code]
    openclaw sandbox recreate --all# or just one agent:openclaw sandbox recreate --agent family
[/code]

### Solo per un agente specifico

bashCopy code
[code]
    # Update only one agent's containersopenclaw sandbox recreate --agent alfred
[/code]

## Perché è necessario

Quando aggiorni la configurazione sandbox:

  * I runtime esistenti continuano a funzionare con le vecchie impostazioni.
  * I runtime vengono rimossi solo dopo 24 ore di inattività.
  * Gli agenti usati regolarmente mantengono attivi i vecchi runtime a tempo indeterminato.


Usa `openclaw sandbox recreate` per forzare la rimozione dei vecchi runtime. Vengono ricreati automaticamente con le impostazioni correnti quando sono nuovamente necessari.

## Migrazione del registro

OpenClaw archivia i metadati dei runtime sandbox come uno shard JSON per ogni voce di container/browser nella directory dello stato sandbox. Le installazioni meno recenti potrebbero avere ancora file legacy monolitici:

  * `~/.openclaw/sandbox/containers.json`
  * `~/.openclaw/sandbox/browsers.json`


Le normali letture dei runtime sandbox non riscrivono quei file. Esegui `openclaw doctor --fix` per migrare le voci legacy valide nelle directory del registro partizionato in shard. I file legacy non validi vengono messi in quarantena, così un vecchio registro difettoso non può nascondere le voci di runtime correnti.

## Configurazione

Le impostazioni sandbox si trovano in `~/.openclaw/openclaw.json` sotto `agents.defaults.sandbox` (gli override per agente vanno in `agents.list[].sandbox`):

jsoncCopy code
[code]
    {  "agents": {    "defaults": {      "sandbox": {        "mode": "all", // off, non-main, all        "backend": "docker", // docker, ssh, openshell        "scope": "agent", // session, agent, shared        "docker": {          "image": "openclaw-sandbox:bookworm-slim",          "containerPrefix": "openclaw-sbx-",          // ... more Docker options        },        "prune": {          "idleHours": 24, // Auto-prune after 24h idle          "maxAgeDays": 7, // Auto-prune after 7 days        },      },    },  },}
[/code]

## Correlati

  * [Riferimento CLI](</it/cli>)
  * [Sandboxing](</it/gateway/sandboxing>)
  * [Workspace dell'agente](</it/concepts/agent-workspace>)
  * [Doctor](</it/gateway/doctor>): controlla la configurazione sandbox.


Was this useful?YesNo