---
title: Installazione
source_url: https://docs.openclaw.ai/it/install
scraped_at: 2026-05-25
---

## Requisiti di sistema

  * **Node 24** (consigliato) o Node 22.16+ - lo script di installazione lo gestisce automaticamente
  * **macOS, Linux o Windows** \- sono supportati sia Windows nativo sia WSL2; WSL2 è più stabile. Vedi [Windows](</it/platforms/windows>).
  * `pnpm` è necessario solo se compili dal sorgente


## Consigliato: script di installazione

Il modo più rapido per installare. Rileva il tuo sistema operativo, installa Node se necessario, installa OpenClaw e avvia l'onboarding.

### macOS / Linux / WSL2

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash
[/code]

### Windows (PowerShell)

powershellCopy code
[code]
    iwr -useb https://openclaw.ai/install.ps1 | iex
[/code]

Per installare senza eseguire l'onboarding:

### macOS / Linux / WSL2

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash -s -- --no-onboard
[/code]

### Windows (PowerShell)

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -NoOnboard
[/code]

Per tutti i flag e le opzioni CI/automazione, vedi [Dettagli interni dell'installer](</it/install/installer>).

## Metodi di installazione alternativi

### Installer con prefisso locale (`install-cli.sh`)

Usalo quando vuoi mantenere OpenClaw e Node sotto un prefisso locale come `~/.openclaw`, senza dipendere da un'installazione Node a livello di sistema:

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install-cli.sh | bash
[/code]

Supporta installazioni npm per impostazione predefinita, oltre a installazioni da checkout git nello stesso flusso con prefisso. Riferimento completo: [Dettagli interni dell'installer](</it/install/installer#install-clish>).

Già installato? Passa tra installazioni da pacchetto e da git con `openclaw update --channel dev` e `openclaw update --channel stable`. Vedi [Aggiornamento](</it/install/updating#switch-between-npm-and-git-installs>).

### npm, pnpm o bun

Se gestisci già Node autonomamente:

### npm

bashCopy code
[code]
    npm install -g openclaw@latestopenclaw onboard --install-daemon
[/code]

### pnpm

bashCopy code
[code]
    pnpm add -g openclaw@latestpnpm approve-builds -gopenclaw onboard --install-daemon
[/code]

### bun

bashCopy code
[code]
    bun add -g openclaw@latestopenclaw onboard --install-daemon
[/code]

Risoluzione dei problemi: errori di build di sharp (npm)

Se `sharp` non riesce a causa di una libvips installata globalmente:

bashCopy code
[code]
    SHARP_IGNORE_GLOBAL_LIBVIPS=1 npm install -g openclaw@latest
[/code]

### Dal sorgente

Per i collaboratori o chiunque voglia eseguire da un checkout locale:

bashCopy code
[code]
    git clone https://github.com/openclaw/openclaw.gitcd openclawpnpm install && pnpm build && pnpm ui:buildpnpm link --globalopenclaw onboard --install-daemon
[/code]

Oppure salta il link e usa `pnpm openclaw ...` dall'interno del repository. Vedi [Configurazione](</it/start/setup>) per i flussi di sviluppo completi.

### Installa da GitHub main

bashCopy code
[code]
    npm install -g github:openclaw/openclaw#main
[/code]

### Container e package manager

[**Docker** Distribuzioni containerizzate o headless. ](</it/install/docker>) [**Podman** Alternativa container rootless a Docker. ](</it/install/podman>) [**Nix** Installazione dichiarativa tramite Nix flake. ](</it/install/nix>) [**Ansible** Provisioning automatizzato di flotte. ](</it/install/ansible>) [**Bun** Uso solo CLI tramite il runtime Bun. ](</it/install/bun>)

## Verifica l'installazione

bashCopy code
[code]
    openclaw --version      # confirm the CLI is availableopenclaw doctor         # check for config issuesopenclaw gateway status # verify the Gateway is running
[/code]

Se vuoi l'avvio gestito dopo l'installazione:

  * macOS: LaunchAgent tramite `openclaw onboard --install-daemon` o `openclaw gateway install`
  * Linux/WSL2: servizio utente systemd tramite gli stessi comandi
  * Windows nativo: prima Scheduled Task, con fallback a un elemento di login nella cartella Startup per utente se la creazione dell'attività viene negata


## Hosting e distribuzione

Distribuisci OpenClaw su un server cloud o VPS:

[**VPS** [**Docker VM** [**Kubernetes** OPENCLAW_DOCS_MARKER:cardOpen:IHRpdGxlPSJGbHkuaW8iIGhyZWY9Ii9pdC9pbnN0YWxsL2ZseSI [Fly.io](<http://Fly.io>) OPENCLAW_DOCS_MARKER:cardClose: [**Hetzner** [**GCP** [**Azure** [**Railway** [**Render** [**Northflank** Aggiorna, migra o disinstalla [**Aggiornamento** Mantieni OpenClaw aggiornato. ](</it/install/updating>) [**Migrazione** Sposta su una nuova macchina. ](</it/install/migrating>) [**Disinstalla** Rimuovi OpenClaw completamente. ](</it/install/uninstall>) Risoluzione dei problemi: `openclaw` non trovato Se l'installazione è riuscita ma `openclaw` non viene trovato nel terminale: bashCopy code
[code]
    node -v           # Node installed?npm prefix -g     # Where are global packages?echo "$PATH"      # Is the global bin dir in PATH?
[/code]

Se `$(npm prefix -g)/bin` non è nel tuo `$PATH`, aggiungilo al file di avvio della shell (`~/.zshrc` o `~/.bashrc`): bashCopy code
[code]
    export PATH="$(npm prefix -g)/bin:$PATH"
[/code]

Poi apri un nuovo terminale. Vedi [Configurazione di Node](</it/install/node>) per maggiori dettagli. ](</it/install/northflank>) Was this useful?YesNo ](</it/install/render>)](</it/install/railway>)](</it/install/azure>)](</it/install/gcp>)](</it/install/hetzner>)](</it/install/kubernetes>)](</it/install/docker-vm-runtime>)](</it/vps>)