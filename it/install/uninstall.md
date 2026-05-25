---
title: Disinstallazione
source_url: https://docs.openclaw.ai/it/install/uninstall
scraped_at: 2026-05-25
---

Due percorsi:

  * **Percorso semplice** se `openclaw` è ancora installato.
  * **Rimozione manuale del servizio** se la CLI non c'è più ma il servizio è ancora in esecuzione.


## Percorso semplice (CLI ancora installata)

Consigliato: usa il disinstallatore integrato:

bashCopy code
[code]
    openclaw uninstall
[/code]

Non interattivo (automazione / npx):

bashCopy code
[code]
    openclaw uninstall --all --yes --non-interactivenpx -y openclaw uninstall --all --yes --non-interactive
[/code]

Passaggi manuali (stesso risultato):

  1. Ferma il servizio Gateway:

bashCopy code
[code]
    openclaw gateway stop
[/code]

  2. Disinstalla il servizio Gateway (launchd/systemd/schtasks):

bashCopy code
[code]
    openclaw gateway uninstall
[/code]

  3. Elimina stato + configurazione:

bashCopy code
[code]
    rm -rf "${OPENCLAW_STATE_DIR:-$HOME/.openclaw}"
[/code]

Se hai impostato `OPENCLAW_CONFIG_PATH` su una posizione personalizzata fuori dalla directory di stato, elimina anche quel file.

  4. Elimina il tuo workspace (facoltativo, rimuove i file dell'agente):

bashCopy code
[code]
    rm -rf ~/.openclaw/workspace
[/code]

  5. Rimuovi l'installazione della CLI (scegli quella che hai usato):

bashCopy code
[code]
    npm rm -g openclawpnpm remove -g openclawbun remove -g openclaw
[/code]

  6. Se hai installato l'app macOS:

bashCopy code
[code]
    rm -rf /Applications/OpenClaw.app
[/code]

Note:

  * Se hai usato profili (`--profile` / `OPENCLAW_PROFILE`), ripeti il passaggio 3 per ogni directory di stato (i valori predefiniti sono `~/.openclaw-<profile>`).
  * In modalità remota, la directory di stato si trova sull'**host del gateway** , quindi esegui lì anche i passaggi 1-4.


## Rimozione manuale del servizio (CLI non installata)

Usa questo percorso se il servizio gateway continua a essere in esecuzione ma `openclaw` manca.

### macOS (launchd)

La label predefinita è `ai.openclaw.gateway` (oppure `ai.openclaw.<profile>`; i vecchi `com.openclaw.*` potrebbero ancora esistere):

bashCopy code
[code]
    launchctl bootout gui/$UID/ai.openclaw.gatewayrm -f ~/Library/LaunchAgents/ai.openclaw.gateway.plist
[/code]

Se hai usato un profilo, sostituisci label e nome plist con `ai.openclaw.<profile>`. Rimuovi eventuali plist legacy `com.openclaw.*` se presenti.

### Linux (unità utente systemd)

Il nome unità predefinito è `openclaw-gateway.service` (oppure `openclaw-gateway-<profile>.service`):

bashCopy code
[code]
    systemctl --user disable --now openclaw-gateway.servicerm -f ~/.config/systemd/user/openclaw-gateway.servicesystemctl --user daemon-reload
[/code]

### Windows (Attività pianificata)

Il nome attività predefinito è `OpenClaw Gateway` (oppure `OpenClaw Gateway (<profile>)`). Lo script dell'attività si trova nella tua directory di stato.

powershellCopy code
[code]
    schtasks /Delete /F /TN "OpenClaw Gateway"Remove-Item -Force "$env:USERPROFILE\.openclaw\gateway.cmd"
[/code]

Se hai usato un profilo, elimina il nome attività corrispondente e `~\.openclaw-<profile>\gateway.cmd`.

## Installazione normale vs checkout del sorgente

### Installazione normale ([install.sh](<http://install.sh>) / npm / pnpm / bun)

Se hai usato `https://openclaw.ai/install.sh` o `install.ps1`, la CLI è stata installata con `npm install -g openclaw@latest`. Rimuovila con `npm rm -g openclaw` (oppure `pnpm remove -g` / `bun remove -g` se hai installato in quel modo).

### Checkout del sorgente (git clone)

Se esegui da un checkout del repo (`git clone` \+ `openclaw ...` / `bun run openclaw ...`):

  1. Disinstalla il servizio Gateway **prima** di eliminare il repo (usa il percorso semplice sopra o la rimozione manuale del servizio).
  2. Elimina la directory del repo.
  3. Rimuovi stato + workspace come mostrato sopra.


## Correlati

  * [Panoramica dell'installazione](</it/install>)
  * [Guida alla migrazione](</it/install/migrating>)


Was this useful?YesNo