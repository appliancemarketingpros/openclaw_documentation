---
title: Installeren
source_url: https://docs.openclaw.ai/nl/install
scraped_at: 2026-05-25
---

## Systeemvereisten

  * **Node 24** (aanbevolen) of Node 22.16+ - het installatiescript regelt dit automatisch
  * **macOS, Linux of Windows** \- zowel native Windows als WSL2 worden ondersteund; WSL2 is stabieler. Zie [Windows](</nl/platforms/windows>).
  * `pnpm` is alleen nodig als je vanuit de broncode bouwt


## Aanbevolen: installatiescript

De snelste manier om te installeren. Het detecteert je OS, installeert Node indien nodig, installeert OpenClaw en start de onboarding.

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

Installeren zonder onboarding uit te voeren:

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

Zie [Interne werking van de installer](</nl/install/installer>) voor alle vlaggen en CI-/automatiseringsopties.

## Alternatieve installatiemethoden

### Lokale prefix-installer (`install-cli.sh`)

Gebruik dit wanneer je OpenClaw en Node onder een lokale prefix zoals `~/.openclaw` wilt houden, zonder afhankelijk te zijn van een systeembrede Node-installatie:

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install-cli.sh | bash
[/code]

Standaard worden npm-installaties ondersteund, plus git-checkout-installaties onder dezelfde prefix-flow. Volledige referentie: [Interne werking van de installer](</nl/install/installer#install-clish>).

Al geinstalleerd? Wissel tussen package- en git-installaties met `openclaw update --channel dev` en `openclaw update --channel stable`. Zie [Bijwerken](</nl/install/updating#switch-between-npm-and-git-installs>).

### npm, pnpm of bun

Als je Node al zelf beheert:

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

Probleemoplossing: sharp-buildfouten (npm)

Als `sharp` mislukt door een globaal geinstalleerde libvips:

bashCopy code
[code]
    SHARP_IGNORE_GLOBAL_LIBVIPS=1 npm install -g openclaw@latest
[/code]

### Vanuit broncode

Voor bijdragers of iedereen die vanuit een lokale checkout wil draaien:

bashCopy code
[code]
    git clone https://github.com/openclaw/openclaw.gitcd openclawpnpm install && pnpm build && pnpm ui:buildpnpm link --globalopenclaw onboard --install-daemon
[/code]

Of sla de link over en gebruik `pnpm openclaw ...` vanuit de repo. Zie [Setup](</nl/start/setup>) voor volledige ontwikkelworkflows.

### Installeren vanaf GitHub main

bashCopy code
[code]
    npm install -g github:openclaw/openclaw#main
[/code]

### Containers en packagemanagers

[**Docker** Gecontaineriseerde of headless deployments. ](</nl/install/docker>) [**Podman** Containeralternatief zonder rootrechten voor Docker. ](</nl/install/podman>) [**Nix** Declaratieve installatie via Nix flake. ](</nl/install/nix>) [**Ansible** Geautomatiseerde fleet-provisioning. ](</nl/install/ansible>) [**Bun** Alleen CLI-gebruik via de Bun-runtime. ](</nl/install/bun>)

## De installatie verifieren

bashCopy code
[code]
    openclaw --version      # confirm the CLI is availableopenclaw doctor         # check for config issuesopenclaw gateway status # verify the Gateway is running
[/code]

Als je beheerde opstart na installatie wilt:

  * macOS: LaunchAgent via `openclaw onboard --install-daemon` of `openclaw gateway install`
  * Linux/WSL2: systemd-gebruikersservice via dezelfde opdrachten
  * Native Windows: eerst Scheduled Task, met een login-item in de Startup-map per gebruiker als fallback als het maken van de taak wordt geweigerd


## Hosting en deployment

Deploy OpenClaw op een cloudserver of VPS:

[**VPS** [**Docker-VM** [**Kubernetes** OPENCLAW_DOCS_MARKER:cardOpen:IHRpdGxlPSJGbHkuaW8iIGhyZWY9Ii9ubC9pbnN0YWxsL2ZseSI [Fly.io](<http://Fly.io>) OPENCLAW_DOCS_MARKER:cardClose: [**Hetzner** [**GCP** [**Azure** [**Railway** [**Render** [**Northflank** Bijwerken, migreren of verwijderen [**Bijwerken** Houd OpenClaw up-to-date. ](</nl/install/updating>) [**Migreren** Verplaats naar een nieuwe machine. ](</nl/install/migrating>) [**Verwijderen** Verwijder OpenClaw volledig. ](</nl/install/uninstall>) Probleemoplossing: `openclaw` niet gevonden Als de installatie is geslaagd, maar `openclaw` niet wordt gevonden in je terminal: bashCopy code
[code]
    node -v           # Node installed?npm prefix -g     # Where are global packages?echo "$PATH"      # Is the global bin dir in PATH?
[/code]

Als `$(npm prefix -g)/bin` niet in je `$PATH` staat, voeg dit dan toe aan je shell-startupbestand (`~/.zshrc` of `~/.bashrc`): bashCopy code
[code]
    export PATH="$(npm prefix -g)/bin:$PATH"
[/code]

Open daarna een nieuwe terminal. Zie [Node-setup](</nl/install/node>) voor meer details. ](</nl/install/northflank>) Was this useful?YesNo ](</nl/install/render>)](</nl/install/railway>)](</nl/install/azure>)](</nl/install/gcp>)](</nl/install/hetzner>)](</nl/install/kubernetes>)](</nl/install/docker-vm-runtime>)](</nl/vps>)