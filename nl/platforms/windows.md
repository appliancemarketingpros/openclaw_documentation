---
title: Windows
source_url: https://docs.openclaw.ai/nl/platforms/windows
scraped_at: 2026-05-25
---

OpenClaw ondersteunt zowel **native Windows** als **WSL2**. WSL2 is de stabielere route en wordt aanbevolen voor de volledige ervaring: de CLI, Gateway en tooling draaien binnen Linux met volledige compatibiliteit. Native Windows werkt voor basisgebruik van de CLI en Gateway, met enkele kanttekeningen hieronder.

Native Windows-companion-apps zijn gepland.

## WSL2 (aanbevolen)

  * [Aan de slag](</nl/start/getting-started>) (gebruik binnen WSL)
  * [Installatie en updates](</nl/install/updating>)
  * Officiële WSL2-handleiding (Microsoft): <https://learn.microsoft.com/windows/wsl/install>


## Status van native Windows

CLI-flows op native Windows worden beter, maar WSL2 blijft de aanbevolen route.

Wat vandaag goed werkt op native Windows:

  * website-installatieprogramma via `install.ps1`
  * lokaal CLI-gebruik zoals `openclaw --version`, `openclaw doctor` en `openclaw plugins list --json`
  * ingebouwde rooktests voor lokale agent/provider zoals:

powershellCopy code
[code]
    openclaw agent --local --agent main --thinking low -m "Reply with exactly WINDOWS-HATCH-OK."
[/code]

Huidige kanttekeningen:

  * `openclaw onboard --non-interactive` verwacht nog steeds een bereikbare lokale gateway, tenzij je `--skip-health` meegeeft
  * `openclaw onboard --non-interactive --install-daemon` en `openclaw gateway install` proberen eerst Windows Scheduled Tasks
  * als het aanmaken van een Scheduled Task wordt geweigerd, valt OpenClaw terug op een login-item in de Startup-map per gebruiker en start het de gateway direct
  * als `schtasks` zelf vastloopt of niet meer reageert, breekt OpenClaw dat pad nu snel af en valt het terug in plaats van voor altijd te blijven hangen
  * Scheduled Tasks hebben nog steeds de voorkeur wanneer ze beschikbaar zijn, omdat ze betere supervisorstatus bieden


Als je alleen de native CLI wilt, zonder installatie van de gateway-service, gebruik dan een van deze:

powershellCopy code
[code]
    openclaw onboard --non-interactive --skip-healthopenclaw gateway run
[/code]

Als je wel beheerde opstart op native Windows wilt:

powershellCopy code
[code]
    openclaw gateway installopenclaw gateway status --json
[/code]

Als het aanmaken van Scheduled Tasks wordt geblokkeerd, start de fallback-servicemodus nog steeds automatisch na aanmelding via de Startup-map van de huidige gebruiker.

## Gateway

  * [Gateway-runbook](</nl/gateway>)
  * [Configuratie](</nl/gateway/configuration>)


## Gateway-service installeren (CLI)

Binnen WSL2:

CodeCopy code
[code]
    openclaw onboard --install-daemon
[/code]

Of:

CodeCopy code
[code]
    openclaw gateway install
[/code]

Of:

CodeCopy code
[code]
    openclaw configure
[/code]

Selecteer **Gateway-service** wanneer daarom wordt gevraagd.

Herstellen/migreren:

CodeCopy code
[code]
    openclaw doctor
[/code]

## Gateway automatisch starten vóór Windows-aanmelding

Zorg er voor headless setups voor dat de volledige opstartketen draait, zelfs wanneer niemand zich aanmeldt bij Windows.

### 1) Gebruikersservices laten draaien zonder aanmelding

Binnen WSL:

bashCopy code
[code]
    sudo loginctl enable-linger "$(whoami)"
[/code]

### 2) De OpenClaw Gateway-gebruikersservice installeren

Binnen WSL:

bashCopy code
[code]
    openclaw gateway install
[/code]

### 3) WSL automatisch starten bij het opstarten van Windows

In PowerShell als Administrator:

powershellCopy code
[code]
    schtasks /create /tn "WSL Boot" /tr "wsl.exe -d Ubuntu --exec /bin/true" /sc onstart /ru SYSTEM
[/code]

Vervang `Ubuntu` door je distronaam uit:

powershellCopy code
[code]
    wsl --list --verbose
[/code]

### Opstartketen verifiëren

Controleer na een herstart (vóór Windows-aanmelding) vanuit WSL:

bashCopy code
[code]
    systemctl --user is-enabled openclaw-gateway.servicesystemctl --user status openclaw-gateway.service --no-pager
[/code]

## Geavanceerd: WSL-services via LAN beschikbaar maken (portproxy)

WSL heeft een eigen virtueel netwerk. Als een andere machine een service moet bereiken die **binnen WSL** draait (SSH, een lokale TTS-server of de Gateway), moet je een Windows-poort doorsturen naar het huidige WSL-IP. Het WSL-IP verandert na herstarts, dus mogelijk moet je de doorstuurregel vernieuwen.

Voorbeeld (PowerShell **als Administrator**):

powershellCopy code
[code]
    $Distro = "Ubuntu-24.04"$ListenPort = 2222$TargetPort = 22 $WslIp = (wsl -d $Distro -- hostname -I).Trim().Split(" ")[0]if (-not $WslIp) { throw "WSL IP not found." } netsh interface portproxy add v4tov4 listenaddress=0.0.0.0 listenport=$ListenPort `  connectaddress=$WslIp connectport=$TargetPort
[/code]

Sta de poort toe via Windows Firewall (eenmalig):

powershellCopy code
[code]
    New-NetFirewallRule -DisplayName "WSL SSH $ListenPort" -Direction Inbound `  -Protocol TCP -LocalPort $ListenPort -Action Allow
[/code]

Vernieuw de portproxy nadat WSL opnieuw is gestart:

powershellCopy code
[code]
    netsh interface portproxy delete v4tov4 listenport=$ListenPort listenaddress=0.0.0.0 | Out-Nullnetsh interface portproxy add v4tov4 listenport=$ListenPort listenaddress=0.0.0.0 `  connectaddress=$WslIp connectport=$TargetPort | Out-Null
[/code]

Opmerkingen:

  * SSH vanaf een andere machine richt zich op het **Windows-host-IP** (voorbeeld: `ssh user@windows-host -p 2222`).
  * Remote nodes moeten naar een **bereikbare** Gateway-URL verwijzen (niet `127.0.0.1`); gebruik `openclaw status --all` om dit te bevestigen.
  * Gebruik `listenaddress=0.0.0.0` voor LAN-toegang; `127.0.0.1` houdt het alleen lokaal.
  * Als je dit automatisch wilt, registreer dan een Scheduled Task om de vernieuwingsstap bij aanmelding uit te voeren.


## Stapsgewijze WSL2-installatie

### 1) WSL2 + Ubuntu installeren

Open PowerShell (Admin):

powershellCopy code
[code]
    wsl --install# Or pick a distro explicitly:wsl --list --onlinewsl --install -d Ubuntu-24.04
[/code]

Herstart als Windows daarom vraagt.

### 2) systemd inschakelen (vereist voor gateway-installatie)

In je WSL-terminal:

bashCopy code
[code]
    sudo tee /etc/wsl.conf >/dev/null <<'EOF'[boot]systemd=trueEOF
[/code]

Daarna vanuit PowerShell:

powershellCopy code
[code]
    wsl --shutdown
[/code]

Open Ubuntu opnieuw en verifieer daarna:

bashCopy code
[code]
    systemctl --user status
[/code]

### 3) OpenClaw installeren (binnen WSL)

Volg voor een normale eerste setup binnen WSL de Linux-flow Aan de slag:

bashCopy code
[code]
    git clone https://github.com/openclaw/openclaw.gitcd openclawpnpm installpnpm buildpnpm ui:buildpnpm openclaw onboard --install-daemon
[/code]

Als je vanuit de broncode ontwikkelt in plaats van een eerste onboarding uit te voeren, gebruik dan de source-dev-loop uit [Setup](</nl/start/setup>):

bashCopy code
[code]
    pnpm install# First run only (or after resetting local OpenClaw config/workspace)pnpm openclaw setuppnpm gateway:watch
[/code]

Volledige handleiding: [Aan de slag](</nl/start/getting-started>)

## Windows-companion-app

We hebben nog geen Windows-companion-app. Bijdragen zijn welkom als je wilt helpen om dit mogelijk te maken.

## Git- en GitHub-connectiviteit (contributors)

Sommige netwerken blokkeren of beperken HTTPS naar GitHub. Als `git clone` mislukt met time-outs of verbindingsresets, probeer dan een ander netwerk, een VPN of een HTTP/HTTPS-proxy die je organisatie aanbiedt.

Als `gh auth login` mislukt tijdens de browser-device-flow (bijvoorbeeld een time-out bij het bereiken van `github.com:443`), authenticeer dan in plaats daarvan met een persoonlijk toegangstoken:

  1. Maak een token met ten minste de `repo`-scope (classic PAT) of equivalente fijnmazige toegang.
  2. In PowerShell voor de huidige sessie:

powershellCopy code
[code]
    $env:GH_TOKEN="<your-token>"gh auth statusgh auth setup-git
[/code]

  3. Als `gh auth status` waarschuwt voor ontbrekende `read:org`, maak dan een token aan dat die scope bevat en wijs de variabele opnieuw toe:

powershellCopy code
[code]
    $env:GH_TOKEN="<your-token-with-repo-and-read:org>"gh auth status
[/code]

`gh auth refresh -s read:org` is alleen van toepassing wanneer je via `gh auth login` bent geauthenticeerd en opgeslagen credentials hebt om te vernieuwen (niet wanneer je `GH_TOKEN` gebruikt).

Commit nooit tokens en plak ze niet in issues of pull requests.

## Gerelateerd

  * [Installatieoverzicht](</nl/install>)
  * [Platforms](</nl/platforms>)


Was this useful?YesNo