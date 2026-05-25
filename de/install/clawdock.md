---
title: ClawDock
source_url: https://docs.openclaw.ai/de/install/clawdock
scraped_at: 2026-05-25
---

ClawDock ist eine kleine Shell-Helferebene für Docker-basierte OpenClaw-Installationen.

Sie stellt Ihnen kurze Befehle wie `clawdock-start`, `clawdock-dashboard` und `clawdock-fix-token` bereit, statt längerer `docker compose ...`-Aufrufe.

Wenn Sie Docker noch nicht eingerichtet haben, beginnen Sie mit [Docker](</de/install/docker>).

## Installation

Verwenden Sie den kanonischen Helferpfad:

bashCopy code
[code]
    mkdir -p ~/.clawdock && curl -sL https://raw.githubusercontent.com/openclaw/openclaw/main/scripts/clawdock/clawdock-helpers.sh -o ~/.clawdock/clawdock-helpers.shecho 'source ~/.clawdock/clawdock-helpers.sh' >> ~/.zshrc && source ~/.zshrc
[/code]

Wenn Sie ClawDock zuvor aus `scripts/shell-helpers/clawdock-helpers.sh` installiert haben, installieren Sie es erneut aus dem neuen Pfad `scripts/clawdock/clawdock-helpers.sh`. Der alte Raw-GitHub-Pfad wurde entfernt.

## Was Sie erhalten

### Grundlegende Vorgänge

Befehl | Beschreibung  
---|---  
`clawdock-start` | Gateway starten  
`clawdock-stop` | Gateway stoppen  
`clawdock-restart` | Gateway neu starten  
`clawdock-status` | Containerstatus prüfen  
`clawdock-logs` | Gateway-Protokollen folgen  
  
### Containerzugriff

Befehl | Beschreibung  
---|---  
`clawdock-shell` | Eine Shell im Gateway-Container öffnen  
`clawdock-cli <command>` | OpenClaw-CLI-Befehle in Docker ausführen  
`clawdock-exec <command>` | Einen beliebigen Befehl im Container ausführen  
  
### Web-UI und Kopplung

Befehl | Beschreibung  
---|---  
`clawdock-dashboard` | Control-UI-URL öffnen  
`clawdock-devices` | Ausstehende Gerätekopplungen auflisten  
`clawdock-approve <id>` | Eine Kopplungsanfrage genehmigen  
  
### Einrichtung und Wartung

Befehl | Beschreibung  
---|---  
`clawdock-fix-token` | Gateway-Token im Container konfigurieren  
`clawdock-update` | Abrufen, neu bauen und neu starten  
`clawdock-rebuild` | Nur das Docker-Image neu bauen  
`clawdock-clean` | Container und Volumes entfernen  
  
### Dienstprogramme

Befehl | Beschreibung  
---|---  
`clawdock-health` | Gateway-Integritätsprüfung ausführen  
`clawdock-token` | Gateway-Token ausgeben  
`clawdock-cd` | In das OpenClaw-Projektverzeichnis springen  
`clawdock-config` | `~/.openclaw` öffnen  
`clawdock-show-config` | Konfigurationsdateien mit redigierten Werten ausgeben  
`clawdock-workspace` | Arbeitsbereichsverzeichnis öffnen  
  
## Ablauf bei der ersten Verwendung

bashCopy code
[code]
    clawdock-startclawdock-fix-tokenclawdock-dashboard
[/code]

Wenn der Browser meldet, dass eine Kopplung erforderlich ist:

bashCopy code
[code]
    clawdock-devicesclawdock-approve <request-id>
[/code]

## Konfiguration und Secrets

ClawDock arbeitet mit derselben Docker-Konfigurationsaufteilung, die in [Docker](</de/install/docker>) beschrieben ist:

  * `<project>/.env` für Docker-spezifische Werte wie Image-Name, Ports und das Gateway-Token
  * `~/.openclaw/.env` für env-gestützte Provider-Schlüssel und Bot-Tokens
  * `~/.openclaw/agents/<agentId>/agent/auth-profiles.json` für gespeicherte Provider-OAuth/API-Key-Authentifizierung
  * `~/.openclaw/openclaw.json` für Verhaltenskonfiguration


Verwenden Sie `clawdock-show-config`, wenn Sie die `.env`-Dateien und `openclaw.json` schnell prüfen möchten. Der Befehl redigiert `.env`-Werte in der ausgegebenen Darstellung.

## Verwandte Themen

[**Docker** Kanonische Docker-Installation für OpenClaw. ](</de/install/docker>) [**Docker-VM-Runtime** Docker-verwaltete VM-Runtime für gehärtete Isolation. ](</de/install/docker-vm-runtime>) [**Aktualisierung** Aktualisierung des OpenClaw-Pakets und der verwalteten Dienste. ](</de/install/updating>)

Was this useful?YesNo