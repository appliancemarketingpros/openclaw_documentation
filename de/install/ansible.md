---
title: Ansible
source_url: https://docs.openclaw.ai/de/install/ansible
scraped_at: 2026-05-25
---

Stellen Sie OpenClaw mit **[openclaw-ansible](<https://github.com/openclaw/openclaw-ansible>)** auf Produktionsservern bereit -- einem automatisierten Installer mit sicherheitsorientierter Architektur.

## Voraussetzungen

Anforderung | Details  
---|---  
**OS** | Debian 11+ oder Ubuntu 20.04+  
**Zugriff** | Root- oder sudo-Rechte  
**Netzwerk** | Internetverbindung für die Paketinstallation  
**Ansible** | 2.14+ (wird automatisch vom Schnellstartskript installiert)  
  
## Was Sie erhalten

  * **Firewall-First-Sicherheit** \-- UFW + Docker-Isolierung (nur SSH + Tailscale zugänglich)
  * **Tailscale-VPN** \-- sicherer Remote-Zugriff, ohne Dienste öffentlich freizugeben
  * **Docker** \-- isolierte Sandbox-Container, nur localhost-Bindungen
  * **Defense in Depth** \-- 4-Schichten-Sicherheitsarchitektur
  * **Systemd-Integration** \-- automatischer Start beim Booten mit Härtung
  * **Ein-Befehl-Einrichtung** \-- vollständige Bereitstellung in Minuten


## Schnellstart

Installation mit einem Befehl:

bashCopy code
[code]
    curl -fsSL https://raw.githubusercontent.com/openclaw/openclaw-ansible/main/install.sh | bash
[/code]

## Was installiert wird

Das Ansible-Playbook installiert und konfiguriert:

  1. **Tailscale** \-- Mesh-VPN für sicheren Remote-Zugriff
  2. **UFW-Firewall** \-- nur SSH- + Tailscale-Ports
  3. **Docker CE + Compose V2** \-- für das Standard-Backend der Agent-Sandbox
  4. **Node.js 24 + pnpm** \-- Laufzeitabhängigkeiten (Node 22 LTS, derzeit `22.16+`, bleibt unterstützt)
  5. **OpenClaw** \-- hostbasiert, nicht containerisiert
  6. **Systemd-Dienst** \-- automatischer Start mit Sicherheitshärtung


## Einrichtung nach der Installation

* ### Zum openclaw-Benutzer wechseln

bashCopy code
[code]
    sudo -i -u openclaw
[/code]

* ### Onboarding-Assistenten ausführen

Das Skript nach der Installation führt Sie durch die Konfiguration der OpenClaw-Einstellungen.

* ### Messaging-Provider verbinden

Melden Sie sich bei WhatsApp, Telegram, Discord oder Signal an:

bashCopy code
[code]
    openclaw channels login
[/code]

* ### Installation überprüfen

bashCopy code
[code]
    sudo systemctl status openclawsudo journalctl -u openclaw -f
[/code]

* ### Mit Tailscale verbinden

Treten Sie Ihrem VPN-Mesh für sicheren Remote-Zugriff bei.

### Schnellbefehle

bashCopy code
[code]
    # Dienststatus prüfensudo systemctl status openclaw # Live-Logs anzeigensudo journalctl -u openclaw -f # Gateway neu startensudo systemctl restart openclaw # Provider-Anmeldung (als openclaw-Benutzer ausführen)sudo -i -u openclawopenclaw channels login
[/code]

## Sicherheitsarchitektur

Die Bereitstellung verwendet ein 4-Schichten-Verteidigungsmodell:

  1. **Firewall (UFW)** \-- nur SSH (22) + Tailscale (41641/udp) öffentlich freigegeben
  2. **VPN (Tailscale)** \-- Gateway nur über das VPN-Mesh erreichbar
  3. **Docker-Isolierung** \-- DOCKER-USER-iptables-Kette verhindert externe Portfreigaben
  4. **Systemd-Härtung** \-- NoNewPrivileges, PrivateTmp, nicht privilegierter Benutzer


So überprüfen Sie Ihre externe Angriffsfläche:

bashCopy code
[code]
    nmap -p- YOUR_SERVER_IP
[/code]

Nur Port 22 (SSH) sollte geöffnet sein. Alle anderen Dienste (Gateway, Docker) sind abgesichert.

Docker wird für Agent-Sandboxes (isolierte Tool-Ausführung) installiert, nicht für den Betrieb des Gateways selbst. Siehe [Multi-Agent-Sandbox und Tools](</de/tools/multi-agent-sandbox-tools>) zur Sandbox-Konfiguration.

## Manuelle Installation

Wenn Sie die Automatisierung lieber manuell steuern möchten:

* ### Voraussetzungen installieren

bashCopy code
[code]
    sudo apt update && sudo apt install -y ansible git
[/code]

* ### Repository klonen

bashCopy code
[code]
    git clone https://github.com/openclaw/openclaw-ansible.gitcd openclaw-ansible
[/code]

* ### Ansible-Collections installieren

bashCopy code
[code]
    ansible-galaxy collection install -r requirements.yml
[/code]

* ### Playbook ausführen

bashCopy code
[code]
    ./run-playbook.sh
[/code]

Alternativ direkt ausführen und anschließend das Einrichtungsskript manuell ausführen:

bashCopy code
[code]
    ansible-playbook playbook.yml --ask-become-pass# Danach ausführen: /tmp/openclaw-setup.sh
[/code]

## Aktualisierung

Der Ansible-Installer richtet OpenClaw für manuelle Updates ein. Siehe [Aktualisierung](</de/install/updating>) für den standardmäßigen Aktualisierungsablauf.

So führen Sie das Ansible-Playbook erneut aus (zum Beispiel für Konfigurationsänderungen):

bashCopy code
[code]
    cd openclaw-ansible./run-playbook.sh
[/code]

Dies ist idempotent und kann sicher mehrfach ausgeführt werden.

## Fehlerbehebung

Firewall blockiert meine Verbindung

  * Stellen Sie sicher, dass Sie zuerst über das Tailscale-VPN zugreifen können
  * SSH-Zugriff (Port 22) ist immer erlaubt
  * Der Gateway ist absichtlich nur über Tailscale erreichbar

Dienst startet nicht bashCopy code
[code]
    # Logs prüfensudo journalctl -u openclaw -n 100 # Berechtigungen überprüfensudo ls -la /opt/openclaw # Manuellen Start testensudo -i -u openclawcd ~/openclawopenclaw gateway run
[/code]

Probleme mit der Docker-Sandbox bashCopy code
[code]
    # Überprüfen, ob Docker läuftsudo systemctl status docker # Sandbox-Image prüfensudo docker images | grep openclaw-sandbox # Sandbox-Image erstellen, falls es fehlt (erfordert Source-Checkout)cd /opt/openclaw/openclawsudo -u openclaw ./scripts/sandbox-setup.sh# Für npm-Installationen ohne Source-Checkout siehe# https://docs.openclaw.ai/gateway/sandboxing#images-and-setup
[/code]

Provider-Anmeldung schlägt fehl

Stellen Sie sicher, dass Sie als Benutzer `openclaw` ausführen:

bashCopy code
[code]
    sudo -i -u openclawopenclaw channels login
[/code]

## Erweiterte Konfiguration

Ausführliche Informationen zur Sicherheitsarchitektur und Fehlerbehebung finden Sie im openclaw-ansible-Repo:

  * [Sicherheitsarchitektur](<https://github.com/openclaw/openclaw-ansible/blob/main/docs/security.md>)
  * [Technische Details](<https://github.com/openclaw/openclaw-ansible/blob/main/docs/architecture.md>)
  * [Fehlerbehebungsleitfaden](<https://github.com/openclaw/openclaw-ansible/blob/main/docs/troubleshooting.md>)


## Verwandte Themen

  * [openclaw-ansible](<https://github.com/openclaw/openclaw-ansible>) \-- vollständiger Bereitstellungsleitfaden
  * [Docker](</de/install/docker>) \-- containerisierte Gateway-Einrichtung
  * [Sandboxing](</de/gateway/sandboxing>) \-- Agent-Sandbox-Konfiguration
  * [Multi-Agent-Sandbox und Tools](</de/tools/multi-agent-sandbox-tools>) \-- Isolierung pro Agent


Was this useful?YesNo