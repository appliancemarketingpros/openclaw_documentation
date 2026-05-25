---
title: Windows
source_url: https://docs.openclaw.ai/it/platforms/windows
scraped_at: 2026-05-25
---

OpenClaw supporta sia **Windows nativo** sia **WSL2**. WSL2 è il percorso più stabile ed è consigliato per l'esperienza completa: CLI, Gateway e strumenti vengono eseguiti dentro Linux con piena compatibilità. Windows nativo funziona per l'uso di base della CLI e del Gateway, con alcune limitazioni indicate sotto.

Le app companion native per Windows sono pianificate.

## WSL2 (consigliato)

  * [Guida introduttiva](</it/start/getting-started>) (da usare dentro WSL)
  * [Installazione e aggiornamenti](</it/install/updating>)
  * Guida WSL2 ufficiale (Microsoft): <https://learn.microsoft.com/windows/wsl/install>


## Stato di Windows nativo

I flussi della CLI su Windows nativo stanno migliorando, ma WSL2 resta il percorso consigliato.

Cosa funziona bene oggi su Windows nativo:

  * installer dal sito web tramite `install.ps1`
  * uso locale della CLI, ad esempio `openclaw --version`, `openclaw doctor` e `openclaw plugins list --json`
  * smoke test incorporato per local-agent/provider, ad esempio:

powershellCopy code
[code]
    openclaw agent --local --agent main --thinking low -m "Reply with exactly WINDOWS-HATCH-OK."
[/code]

Limitazioni attuali:

  * `openclaw onboard --non-interactive` si aspetta ancora un gateway locale raggiungibile, a meno che tu non passi `--skip-health`
  * `openclaw onboard --non-interactive --install-daemon` e `openclaw gateway install` provano prima le Attività pianificate di Windows
  * se la creazione dell'Attività pianificata viene negata, OpenClaw ripiega su un elemento di accesso per utente nella cartella Esecuzione automatica e avvia immediatamente il gateway
  * se `schtasks` stesso si blocca o smette di rispondere, OpenClaw ora interrompe rapidamente quel percorso e ripiega invece di restare bloccato per sempre
  * le Attività pianificate restano preferite quando disponibili, perché forniscono uno stato di supervisione migliore


Se vuoi solo la CLI nativa, senza installazione del servizio gateway, usa uno di questi:

powershellCopy code
[code]
    openclaw onboard --non-interactive --skip-healthopenclaw gateway run
[/code]

Se invece vuoi l'avvio gestito su Windows nativo:

powershellCopy code
[code]
    openclaw gateway installopenclaw gateway status --json
[/code]

Se la creazione dell'Attività pianificata è bloccata, la modalità servizio di fallback si avvia comunque automaticamente dopo l'accesso tramite la cartella Esecuzione automatica dell'utente corrente.

## Gateway

  * [Runbook del Gateway](</it/gateway>)
  * [Configurazione](</it/gateway/configuration>)


## Installazione del servizio Gateway (CLI)

Dentro WSL2:

CodeCopy code
[code]
    openclaw onboard --install-daemon
[/code]

Oppure:

CodeCopy code
[code]
    openclaw gateway install
[/code]

Oppure:

CodeCopy code
[code]
    openclaw configure
[/code]

Seleziona **Servizio Gateway** quando richiesto.

Ripara/migra:

CodeCopy code
[code]
    openclaw doctor
[/code]

## Avvio automatico del Gateway prima dell'accesso a Windows

Per configurazioni headless, assicurati che l'intera catena di avvio venga eseguita anche quando nessuno accede a Windows.

### 1) Mantieni in esecuzione i servizi utente senza accesso

Dentro WSL:

bashCopy code
[code]
    sudo loginctl enable-linger "$(whoami)"
[/code]

### 2) Installa il servizio utente del gateway OpenClaw

Dentro WSL:

bashCopy code
[code]
    openclaw gateway install
[/code]

### 3) Avvia WSL automaticamente all'avvio di Windows

In PowerShell come Amministratore:

powershellCopy code
[code]
    schtasks /create /tn "WSL Boot" /tr "wsl.exe -d Ubuntu --exec /bin/true" /sc onstart /ru SYSTEM
[/code]

Sostituisci `Ubuntu` con il nome della tua distro da:

powershellCopy code
[code]
    wsl --list --verbose
[/code]

### Verifica la catena di avvio

Dopo un riavvio (prima dell'accesso a Windows), controlla da WSL:

bashCopy code
[code]
    systemctl --user is-enabled openclaw-gateway.servicesystemctl --user status openclaw-gateway.service --no-pager
[/code]

## Avanzato: esporre i servizi WSL sulla LAN (portproxy)

WSL ha una propria rete virtuale. Se un'altra macchina deve raggiungere un servizio in esecuzione **dentro WSL** (SSH, un server TTS locale o il Gateway), devi inoltrare una porta Windows all'IP WSL corrente. L'IP WSL cambia dopo i riavvii, quindi potresti dover aggiornare la regola di inoltro.

Esempio (PowerShell **come Amministratore**):

powershellCopy code
[code]
    $Distro = "Ubuntu-24.04"$ListenPort = 2222$TargetPort = 22 $WslIp = (wsl -d $Distro -- hostname -I).Trim().Split(" ")[0]if (-not $WslIp) { throw "WSL IP not found." } netsh interface portproxy add v4tov4 listenaddress=0.0.0.0 listenport=$ListenPort `  connectaddress=$WslIp connectport=$TargetPort
[/code]

Consenti la porta tramite Windows Firewall (una sola volta):

powershellCopy code
[code]
    New-NetFirewallRule -DisplayName "WSL SSH $ListenPort" -Direction Inbound `  -Protocol TCP -LocalPort $ListenPort -Action Allow
[/code]

Aggiorna il portproxy dopo il riavvio di WSL:

powershellCopy code
[code]
    netsh interface portproxy delete v4tov4 listenport=$ListenPort listenaddress=0.0.0.0 | Out-Nullnetsh interface portproxy add v4tov4 listenport=$ListenPort listenaddress=0.0.0.0 `  connectaddress=$WslIp connectport=$TargetPort | Out-Null
[/code]

Note:

  * SSH da un'altra macchina punta all'**IP dell'host Windows** (esempio: `ssh user@windows-host -p 2222`).
  * I nodi remoti devono puntare a un URL Gateway **raggiungibile** (non `127.0.0.1`); usa `openclaw status --all` per confermare.
  * Usa `listenaddress=0.0.0.0` per l'accesso LAN; `127.0.0.1` lo mantiene solo locale.
  * Se vuoi renderlo automatico, registra un'Attività pianificata per eseguire il passaggio di aggiornamento all'accesso.


## Installazione WSL2 passo passo

### 1) Installa WSL2 + Ubuntu

Apri PowerShell (Amministratore):

powershellCopy code
[code]
    wsl --install# Or pick a distro explicitly:wsl --list --onlinewsl --install -d Ubuntu-24.04
[/code]

Riavvia se Windows lo richiede.

### 2) Abilita systemd (necessario per l'installazione del gateway)

Nel tuo terminale WSL:

bashCopy code
[code]
    sudo tee /etc/wsl.conf >/dev/null <<'EOF'[boot]systemd=trueEOF
[/code]

Poi da PowerShell:

powershellCopy code
[code]
    wsl --shutdown
[/code]

Riapri Ubuntu, quindi verifica:

bashCopy code
[code]
    systemctl --user status
[/code]

### 3) Installa OpenClaw (dentro WSL)

Per una normale configurazione iniziale dentro WSL, segui il flusso Linux della Guida introduttiva:

bashCopy code
[code]
    git clone https://github.com/openclaw/openclaw.gitcd openclawpnpm installpnpm buildpnpm ui:buildpnpm openclaw onboard --install-daemon
[/code]

Se stai sviluppando dal sorgente invece di eseguire l'onboarding iniziale, usa il loop di sviluppo dal sorgente da [Configurazione](</it/start/setup>):

bashCopy code
[code]
    pnpm install# First run only (or after resetting local OpenClaw config/workspace)pnpm openclaw setuppnpm gateway:watch
[/code]

Guida completa: [Guida introduttiva](</it/start/getting-started>)

## App companion per Windows

Non abbiamo ancora un'app companion per Windows. I contributi sono benvenuti se vuoi aiutare a realizzarla.

## Connettività Git e GitHub (contributori)

Alcune reti bloccano o limitano HTTPS verso GitHub. Se `git clone` fallisce con timeout o reset della connessione, prova un'altra rete, una VPN o un proxy HTTP/HTTPS fornito dalla tua organizzazione.

Se `gh auth login` fallisce durante il flusso dispositivo del browser (ad esempio per un timeout nel raggiungere `github.com:443`), autenticati invece con un token di accesso personale:

  1. Crea un token con almeno lo scope `repo` (PAT classico) o un accesso fine-grained equivalente.
  2. In PowerShell per la sessione corrente:

powershellCopy code
[code]
    $env:GH_TOKEN="<your-token>"gh auth statusgh auth setup-git
[/code]

  3. Se `gh auth status` avvisa della mancanza di `read:org`, crea un token che includa quello scope e riassegna la variabile:

powershellCopy code
[code]
    $env:GH_TOKEN="<your-token-with-repo-and-read:org>"gh auth status
[/code]

`gh auth refresh -s read:org` si applica solo quando ti sei autenticato tramite `gh auth login` e hai credenziali salvate da aggiornare (non quando usi `GH_TOKEN`).

Non commettere mai token né incollarli in issue o pull request.

## Correlati

  * [Panoramica dell'installazione](</it/install>)
  * [Piattaforme](</it/platforms>)


Was this useful?YesNo