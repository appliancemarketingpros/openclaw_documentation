---
title: Windows
source_url: https://docs.openclaw.ai/de/platforms/windows
scraped_at: 2026-05-25
---

OpenClaw unterstützt sowohl **natives Windows** als auch **WSL2**. WSL2 ist der stabilere Weg und wird für die vollständige Erfahrung empfohlen — CLI, Gateway und Tooling laufen mit vollständiger Kompatibilität innerhalb von Linux. Natives Windows funktioniert für die Kernnutzung von CLI und Gateway, mit einigen unten aufgeführten Einschränkungen.

Native Windows-Begleit-Apps sind geplant.

## WSL2 (empfohlen)

  * [Erste Schritte](</de/start/getting-started>) (innerhalb von WSL verwenden)
  * [Installation und Updates](</de/install/updating>)
  * Offizielle WSL2-Anleitung (Microsoft): <https://learn.microsoft.com/windows/wsl/install>


## Status unter nativem Windows

CLI-Flows unter nativem Windows werden verbessert, aber WSL2 ist weiterhin der empfohlene Weg.

Was heute unter nativem Windows gut funktioniert:

  * Website-Installer über `install.ps1`
  * lokale CLI-Nutzung wie `openclaw --version`, `openclaw doctor` und `openclaw plugins list --json`
  * eingebetteter lokaler Agent/Provider-Smoke-Test wie:

powershellCopy code
[code]
    openclaw agent --local --agent main --thinking low -m "Reply with exactly WINDOWS-HATCH-OK."
[/code]

Aktuelle Einschränkungen:

  * `openclaw onboard --non-interactive` erwartet weiterhin ein erreichbares lokales Gateway, sofern Sie nicht `--skip-health` übergeben
  * `openclaw onboard --non-interactive --install-daemon` und `openclaw gateway install` versuchen zuerst Windows Scheduled Tasks
  * wenn das Erstellen eines Scheduled Task verweigert wird, fällt OpenClaw auf ein Login-Element im Startup-Ordner des aktuellen Benutzers zurück und startet das Gateway sofort
  * wenn `schtasks` selbst hängen bleibt oder nicht mehr reagiert, bricht OpenClaw diesen Pfad jetzt schnell ab und verwendet den Fallback, statt unbegrenzt zu hängen
  * Scheduled Tasks werden weiterhin bevorzugt, wenn sie verfügbar sind, weil sie einen besseren Supervisor-Status bereitstellen


Wenn Sie nur die native CLI ohne Installation des Gateway-Dienstes möchten, verwenden Sie eines hiervon:

powershellCopy code
[code]
    openclaw onboard --non-interactive --skip-healthopenclaw gateway run
[/code]

Wenn Sie einen verwalteten Start unter nativem Windows möchten:

powershellCopy code
[code]
    openclaw gateway installopenclaw gateway status --json
[/code]

Wenn das Erstellen eines Scheduled Task blockiert ist, startet der Fallback-Dienstmodus nach der Anmeldung weiterhin automatisch über den Startup-Ordner des aktuellen Benutzers.

## Gateway

  * [Gateway-Runbook](</de/gateway>)
  * [Konfiguration](</de/gateway/configuration>)


## Gateway-Dienst installieren (CLI)

Innerhalb von WSL2:

CodeCopy code
[code]
    openclaw onboard --install-daemon
[/code]

Oder:

CodeCopy code
[code]
    openclaw gateway install
[/code]

Oder:

CodeCopy code
[code]
    openclaw configure
[/code]

Wählen Sie **Gateway-Dienst** , wenn Sie dazu aufgefordert werden.

Reparieren/migrieren:

CodeCopy code
[code]
    openclaw doctor
[/code]

## Gateway-Autostart vor der Windows-Anmeldung

Stellen Sie bei Headless-Setups sicher, dass die vollständige Boot-Kette auch dann läuft, wenn sich niemand bei Windows anmeldet.

### 1) Benutzerdienste ohne Anmeldung weiterlaufen lassen

Innerhalb von WSL:

bashCopy code
[code]
    sudo loginctl enable-linger "$(whoami)"
[/code]

### 2) OpenClaw-Gateway-Benutzerdienst installieren

Innerhalb von WSL:

bashCopy code
[code]
    openclaw gateway install
[/code]

### 3) WSL beim Windows-Start automatisch starten

In PowerShell als Administrator:

powershellCopy code
[code]
    schtasks /create /tn "WSL Boot" /tr "wsl.exe -d Ubuntu --exec /bin/true" /sc onstart /ru SYSTEM
[/code]

Ersetzen Sie `Ubuntu` durch den Namen Ihrer Distribution aus:

powershellCopy code
[code]
    wsl --list --verbose
[/code]

### Startkette überprüfen

Prüfen Sie nach einem Neustart (vor der Windows-Anmeldung) aus WSL:

bashCopy code
[code]
    systemctl --user is-enabled openclaw-gateway.servicesystemctl --user status openclaw-gateway.service --no-pager
[/code]

## Erweitert: WSL-Dienste über das LAN verfügbar machen (portproxy)

WSL hat ein eigenes virtuelles Netzwerk. Wenn ein anderer Rechner einen Dienst erreichen muss, der **innerhalb von WSL** läuft (SSH, ein lokaler TTS-Server oder das Gateway), müssen Sie einen Windows-Port an die aktuelle WSL-IP weiterleiten. Die WSL-IP ändert sich nach Neustarts, daher müssen Sie die Weiterleitungsregel möglicherweise aktualisieren.

Beispiel (PowerShell **als Administrator**):

powershellCopy code
[code]
    $Distro = "Ubuntu-24.04"$ListenPort = 2222$TargetPort = 22 $WslIp = (wsl -d $Distro -- hostname -I).Trim().Split(" ")[0]if (-not $WslIp) { throw "WSL IP not found." } netsh interface portproxy add v4tov4 listenaddress=0.0.0.0 listenport=$ListenPort `  connectaddress=$WslIp connectport=$TargetPort
[/code]

Lassen Sie den Port durch die Windows-Firewall zu (einmalig):

powershellCopy code
[code]
    New-NetFirewallRule -DisplayName "WSL SSH $ListenPort" -Direction Inbound `  -Protocol TCP -LocalPort $ListenPort -Action Allow
[/code]

Aktualisieren Sie den portproxy nach WSL-Neustarts:

powershellCopy code
[code]
    netsh interface portproxy delete v4tov4 listenport=$ListenPort listenaddress=0.0.0.0 | Out-Nullnetsh interface portproxy add v4tov4 listenport=$ListenPort listenaddress=0.0.0.0 `  connectaddress=$WslIp connectport=$TargetPort | Out-Null
[/code]

Hinweise:

  * SSH von einem anderen Rechner zielt auf die **Windows-Host-IP** (Beispiel: `ssh user@windows-host -p 2222`).
  * Remote-Knoten müssen auf eine **erreichbare** Gateway-URL zeigen (nicht `127.0.0.1`); verwenden Sie `openclaw status --all` zur Bestätigung.
  * Verwenden Sie `listenaddress=0.0.0.0` für LAN-Zugriff; `127.0.0.1` hält ihn nur lokal.
  * Wenn Sie dies automatisieren möchten, registrieren Sie einen Scheduled Task, der den Aktualisierungsschritt bei der Anmeldung ausführt.


## Schrittweise WSL2-Installation

### 1) WSL2 + Ubuntu installieren

Öffnen Sie PowerShell (Admin):

powershellCopy code
[code]
    wsl --install# Or pick a distro explicitly:wsl --list --onlinewsl --install -d Ubuntu-24.04
[/code]

Starten Sie neu, wenn Windows Sie dazu auffordert.

### 2) systemd aktivieren (für die Gateway-Installation erforderlich)

In Ihrem WSL-Terminal:

bashCopy code
[code]
    sudo tee /etc/wsl.conf >/dev/null <<'EOF'[boot]systemd=trueEOF
[/code]

Dann aus PowerShell:

powershellCopy code
[code]
    wsl --shutdown
[/code]

Öffnen Sie Ubuntu erneut und prüfen Sie dann:

bashCopy code
[code]
    systemctl --user status
[/code]

### 3) OpenClaw installieren (innerhalb von WSL)

Folgen Sie für eine normale Ersteinrichtung innerhalb von WSL dem Linux-Flow für Erste Schritte:

bashCopy code
[code]
    git clone https://github.com/openclaw/openclaw.gitcd openclawpnpm installpnpm buildpnpm ui:buildpnpm openclaw onboard --install-daemon
[/code]

Wenn Sie statt des ersten Onboardings aus dem Quellcode entwickeln, verwenden Sie den Source-Dev-Loop aus [Einrichtung](</de/start/setup>):

bashCopy code
[code]
    pnpm install# First run only (or after resetting local OpenClaw config/workspace)pnpm openclaw setuppnpm gateway:watch
[/code]

Vollständige Anleitung: [Erste Schritte](</de/start/getting-started>)

## Windows-Begleit-App

Wir haben noch keine Windows-Begleit-App. Beiträge sind willkommen, wenn Sie helfen möchten, sie umzusetzen.

## Git- und GitHub-Konnektivität (Mitwirkende)

Einige Netzwerke blockieren oder drosseln HTTPS zu GitHub. Wenn `git clone` mit Timeouts oder Verbindungsabbrüchen fehlschlägt, versuchen Sie ein anderes Netzwerk, ein VPN oder einen HTTP/HTTPS-Proxy, den Ihre Organisation bereitstellt.

Wenn `gh auth login` während des Browser-Device-Flows fehlschlägt (zum Beispiel durch ein Timeout beim Erreichen von `github.com:443`), authentifizieren Sie sich stattdessen mit einem persönlichen Zugriffstoken:

  1. Erstellen Sie ein Token mit mindestens dem `repo`-Scope (klassischer PAT) oder entsprechendem fein abgestuftem Zugriff.
  2. In PowerShell für die aktuelle Sitzung:

powershellCopy code
[code]
    $env:GH_TOKEN="<your-token>"gh auth statusgh auth setup-git
[/code]

  3. Wenn `gh auth status` vor fehlendem `read:org` warnt, erstellen Sie ein Token, das diesen Scope enthält, und weisen Sie die Variable erneut zu:

powershellCopy code
[code]
    $env:GH_TOKEN="<your-token-with-repo-and-read:org>"gh auth status
[/code]

`gh auth refresh -s read:org` gilt nur, wenn Sie sich über `gh auth login` authentifiziert haben und gespeicherte Anmeldedaten zum Aktualisieren vorhanden sind (nicht bei Verwendung von `GH_TOKEN`).

Committen Sie niemals Tokens und fügen Sie sie nicht in Issues oder Pull Requests ein.

## Verwandt

  * [Installationsübersicht](</de/install>)
  * [Plattformen](</de/platforms>)


Was this useful?YesNo