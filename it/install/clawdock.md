---
title: ClawDock
source_url: https://docs.openclaw.ai/it/install/clawdock
scraped_at: 2026-05-25
---

ClawDock è un piccolo livello di helper shell per installazioni di OpenClaw basate su Docker.

Ti offre comandi brevi come `clawdock-start`, `clawdock-dashboard` e `clawdock-fix-token` invece di invocazioni più lunghe `docker compose ...`.

Se non hai ancora configurato Docker, inizia da [Docker](</it/install/docker>).

## Installazione

Usa il percorso helper canonico:

bashCopy code
[code]
    mkdir -p ~/.clawdock && curl -sL https://raw.githubusercontent.com/openclaw/openclaw/main/scripts/clawdock/clawdock-helpers.sh -o ~/.clawdock/clawdock-helpers.shecho 'source ~/.clawdock/clawdock-helpers.sh' >> ~/.zshrc && source ~/.zshrc
[/code]

Se in precedenza hai installato ClawDock da `scripts/shell-helpers/clawdock-helpers.sh`, reinstalla dal nuovo percorso `scripts/clawdock/clawdock-helpers.sh`. Il vecchio percorso raw GitHub è stato rimosso.

## Cosa ottieni

### Operazioni di base

Comando | Descrizione  
---|---  
`clawdock-start` | Avvia il Gateway  
`clawdock-stop` | Arresta il Gateway  
`clawdock-restart` | Riavvia il Gateway  
`clawdock-status` | Controlla lo stato container  
`clawdock-logs` | Segui i log del Gateway  
  
### Accesso al container

Comando | Descrizione  
---|---  
`clawdock-shell` | Apri una shell dentro il container del Gateway  
`clawdock-cli <command>` | Esegui comandi CLI di OpenClaw in Docker  
`clawdock-exec <command>` | Esegui un comando arbitrario nel container  
  
### UI web e abbinamento

Comando | Descrizione  
---|---  
`clawdock-dashboard` | Apri l'URL della UI di controllo  
`clawdock-devices` | Elenca gli abbinamenti dispositivi in attesa  
`clawdock-approve <id>` | Approva una richiesta di abbinamento  
  
### Configurazione e manutenzione

Comando | Descrizione  
---|---  
`clawdock-fix-token` | Configura il token del Gateway dentro il container  
`clawdock-update` | Scarica, ricompila e riavvia  
`clawdock-rebuild` | Ricompila solo l'immagine Docker  
`clawdock-clean` | Rimuovi container e volumi  
  
### Utilità

Comando | Descrizione  
---|---  
`clawdock-health` | Esegui un controllo di integrità del Gateway  
`clawdock-token` | Stampa il token del Gateway  
`clawdock-cd` | Vai alla directory del progetto OpenClaw  
`clawdock-config` | Apri `~/.openclaw`  
`clawdock-show-config` | Stampa i file di configurazione con valori oscurati  
`clawdock-workspace` | Apri la directory dello workspace  
  
## Flusso al primo utilizzo

bashCopy code
[code]
    clawdock-startclawdock-fix-tokenclawdock-dashboard
[/code]

Se il browser indica che l'abbinamento è richiesto:

bashCopy code
[code]
    clawdock-devicesclawdock-approve <request-id>
[/code]

## Configurazione e segreti

ClawDock funziona con la stessa separazione della configurazione Docker descritta in [Docker](</it/install/docker>):

  * `<project>/.env` per valori specifici di Docker come nome dell'immagine, porte e token del Gateway
  * `~/.openclaw/.env` per chiavi dei provider basate su variabili d'ambiente e token dei bot
  * `~/.openclaw/agents/<agentId>/agent/auth-profiles.json` per l'autenticazione OAuth/API-key dei provider memorizzata
  * `~/.openclaw/openclaw.json` per la configurazione del comportamento


Usa `clawdock-show-config` quando vuoi ispezionare rapidamente i file `.env` e `openclaw.json`. Oscura i valori `.env` nell'output stampato.

## Correlati

[**Docker** Installazione Docker canonica per OpenClaw. ](</it/install/docker>) [**Runtime VM Docker** Runtime VM gestito da Docker per isolamento rafforzato. ](</it/install/docker-vm-runtime>) [**Aggiornamento** Aggiornamento del pacchetto OpenClaw e dei servizi gestiti. ](</it/install/updating>)

Was this useful?YesNo