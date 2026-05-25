---
title: Installieren
source_url: https://docs.openclaw.ai/de/install
scraped_at: 2026-05-25
---

## Systemanforderungen

  * **Node 24** (empfohlen) oder Node 22.16+ - das Installationsskript erledigt dies automatisch
  * **macOS, Linux oder Windows** \- sowohl natives Windows als auch WSL2 werden unterstützt; WSL2 ist stabiler. Siehe [Windows](</de/platforms/windows>).
  * `pnpm` wird nur benötigt, wenn Sie aus dem Quellcode bauen


## Empfohlen: Installationsskript

Der schnellste Weg zur Installation. Es erkennt Ihr Betriebssystem, installiert Node bei Bedarf, installiert OpenClaw und startet das Onboarding.

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

Installation ohne Onboarding:

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

Alle Flags und Optionen für CI/Automatisierung finden Sie unter [Installer-Interna](</de/install/installer>).

## Alternative Installationsmethoden

### Installer mit lokalem Präfix (`install-cli.sh`)

Verwenden Sie dies, wenn OpenClaw und Node unter einem lokalen Präfix wie `~/.openclaw` bleiben sollen, ohne von einer systemweiten Node-Installation abhängig zu sein:

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install-cli.sh | bash
[/code]

Er unterstützt standardmäßig npm-Installationen sowie Git-Checkout-Installationen im gleichen Präfix-Ablauf. Vollständige Referenz: [Installer-Interna](</de/install/installer#install-clish>).

Bereits installiert? Wechseln Sie mit `openclaw update --channel dev` und `openclaw update --channel stable` zwischen Paket- und Git-Installationen. Siehe [Aktualisieren](</de/install/updating#switch-between-npm-and-git-installs>).

### npm, pnpm oder bun

Wenn Sie Node bereits selbst verwalten:

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

Fehlerbehebung: sharp-Buildfehler (npm)

Wenn `sharp` aufgrund eines global installierten libvips fehlschlägt:

bashCopy code
[code]
    SHARP_IGNORE_GLOBAL_LIBVIPS=1 npm install -g openclaw@latest
[/code]

### Aus dem Quellcode

Für Mitwirkende oder alle, die aus einem lokalen Checkout ausführen möchten:

bashCopy code
[code]
    git clone https://github.com/openclaw/openclaw.gitcd openclawpnpm install && pnpm build && pnpm ui:buildpnpm link --globalopenclaw onboard --install-daemon
[/code]

Oder überspringen Sie den Link und verwenden Sie `pnpm openclaw ...` innerhalb des Repos. Vollständige Entwicklungsabläufe finden Sie unter [Einrichtung](</de/start/setup>).

### Von GitHub main installieren

bashCopy code
[code]
    npm install -g github:openclaw/openclaw#main
[/code]

### Container und Paketmanager

[**Docker** Containerisierte oder headless Deployments. ](</de/install/docker>) [**Podman** Rootless-Container-Alternative zu Docker. ](</de/install/podman>) [**Nix** Deklarative Installation per Nix-Flake. ](</de/install/nix>) [**Ansible** Automatisierte Flottenbereitstellung. ](</de/install/ansible>) [**Bun** Reine CLI-Nutzung über die Bun-Laufzeit. ](</de/install/bun>)

## Installation überprüfen

bashCopy code
[code]
    openclaw --version      # confirm the CLI is availableopenclaw doctor         # check for config issuesopenclaw gateway status # verify the Gateway is running
[/code]

Wenn Sie nach der Installation einen verwalteten Start wünschen:

  * macOS: LaunchAgent über `openclaw onboard --install-daemon` oder `openclaw gateway install`
  * Linux/WSL2: systemd-Benutzerdienst über dieselben Befehle
  * Natives Windows: zuerst Geplante Aufgabe, mit einem Login-Element im Startup-Ordner pro Benutzer als Fallback, falls die Aufgabenerstellung verweigert wird


## Hosting und Deployment

Stellen Sie OpenClaw auf einem Cloud-Server oder VPS bereit:

[**VPS** [**Docker VM** [**Kubernetes** OPENCLAW_DOCS_MARKER:cardOpen:IHRpdGxlPSJGbHkuaW8iIGhyZWY9Ii9kZS9pbnN0YWxsL2ZseSI [Fly.io](<http://Fly.io>) OPENCLAW_DOCS_MARKER:cardClose: [**Hetzner** [**GCP** [**Azure** [**Railway** [**Render** [**Northflank** Aktualisieren, migrieren oder deinstallieren [**Aktualisieren** Halten Sie OpenClaw aktuell. ](</de/install/updating>) [**Migrieren** Auf einen neuen Rechner umziehen. ](</de/install/migrating>) [**Deinstallieren** OpenClaw vollständig entfernen. ](</de/install/uninstall>) Fehlerbehebung: `openclaw` nicht gefunden Wenn die Installation erfolgreich war, `openclaw` aber in Ihrem Terminal nicht gefunden wird: bashCopy code
[code]
    node -v           # Node installed?npm prefix -g     # Where are global packages?echo "$PATH"      # Is the global bin dir in PATH?
[/code]

Wenn `$(npm prefix -g)/bin` nicht in Ihrem `$PATH` enthalten ist, fügen Sie es Ihrer Shell-Startdatei (`~/.zshrc` oder `~/.bashrc`) hinzu: bashCopy code
[code]
    export PATH="$(npm prefix -g)/bin:$PATH"
[/code]

Öffnen Sie danach ein neues Terminal. Weitere Details finden Sie unter [Node-Einrichtung](</de/install/node>). ](</de/install/northflank>) Was this useful?YesNo ](</de/install/render>)](</de/install/railway>)](</de/install/azure>)](</de/install/gcp>)](</de/install/hetzner>)](</de/install/kubernetes>)](</de/install/docker-vm-runtime>)](</de/vps>)