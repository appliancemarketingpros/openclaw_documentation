---
title: DigitalOcean
source_url: https://docs.openclaw.ai/de/install/digitalocean
scraped_at: 2026-05-25
---

Führen Sie einen persistenten OpenClaw Gateway auf einem DigitalOcean Droplet aus (~6 USD/Monat für den 1-GB-Basic-Tarif).

DigitalOcean ist der einfachste kostenpflichtige VPS-Weg. Wenn Sie günstigere oder kostenlose Optionen bevorzugen:

  * [Hetzner](</de/install/hetzner>) — 3,79 €/Monat, mehr Kerne/RAM pro Dollar.
  * [Oracle Cloud](</de/install/oracle>) — Always Free ARM (bis zu 4 OCPU, 24 GB RAM), die Registrierung kann jedoch hakelig sein und ist nur ARM.


## Voraussetzungen

  * DigitalOcean-Konto ([Registrierung](<https://cloud.digitalocean.com/registrations/new>))
  * SSH-Schlüsselpaar (oder Bereitschaft, Passwortauthentifizierung zu verwenden)
  * Etwa 20 Minuten


## Einrichtung

* ### Droplet erstellen

  1. Melden Sie sich bei [DigitalOcean](<https://cloud.digitalocean.com/>) an.
  2. Klicken Sie auf **Create > Droplets**.
  3. Wählen Sie: 
     * **Region:** Am nächsten bei Ihnen
     * **Image:** Ubuntu 24.04 LTS
     * **Size:** Basic, Regular, 1 vCPU / 1 GB RAM / 25 GB SSD
     * **Authentication:** SSH-Schlüssel (empfohlen) oder Passwort
  4. Klicken Sie auf **Create Droplet** und notieren Sie die IP-Adresse.


* ### Verbinden und installieren

bashCopy code
[code]
    ssh root@YOUR_DROPLET_IP apt update && apt upgrade -y # Install Node.js 24curl -fsSL https://deb.nodesource.com/setup_24.x | bash -apt install -y nodejs # Install OpenClawcurl -fsSL https://openclaw.ai/install.sh | bash # Create the non-root user that will own OpenClaw state and services.adduser openclawusermod -aG sudo openclawloginctl enable-linger openclaw su - openclawopenclaw --version
[/code]

Verwenden Sie die Root-Shell nur für das System-Bootstrap. Führen Sie OpenClaw-Befehle als Nicht-Root-Benutzer `openclaw` aus, damit der Zustand unter `/home/openclaw/.openclaw/` liegt und der Gateway als systemd-Dienst dieses Benutzers installiert wird.

* ### Onboarding ausführen

bashCopy code
[code]
    openclaw onboard --install-daemon
[/code]

Der Assistent führt Sie durch die Modellauthentifizierung, die Channel-Einrichtung, die Gateway-Token-Erstellung und die Daemon-Installation (systemd).

* ### Swap hinzufügen (für 1-GB-Droplets empfohlen)

bashCopy code
[code]
    fallocate -l 2G /swapfilechmod 600 /swapfilemkswap /swapfileswapon /swapfileecho '/swapfile none swap sw 0 0' >> /etc/fstab
[/code]

* ### Gateway prüfen

bashCopy code
[code]
    openclaw statussystemctl --user status openclaw-gateway.servicejournalctl --user -u openclaw-gateway.service -f
[/code]

* ### Auf die Control UI zugreifen

Der Gateway bindet standardmäßig an loopback. Wählen Sie eine dieser Optionen.

**Option A: SSH-Tunnel (am einfachsten)**

bashCopy code
[code]
    # From your local machinessh -L 18789:localhost:18789 root@YOUR_DROPLET_IP
[/code]

Öffnen Sie anschließend `http://localhost:18789`.

**Option B: Tailscale Serve**

bashCopy code
[code]
    curl -fsSL https://tailscale.com/install.sh | sudo shsudo tailscale upopenclaw config set gateway.tailscale.mode serveopenclaw gateway restart
[/code]

Öffnen Sie anschließend `https://<magicdns>/` von einem beliebigen Gerät in Ihrem Tailnet.

Tailscale Serve authentifiziert Control UI- und WebSocket-Datenverkehr über Tailnet-Identitätsheader, wobei vorausgesetzt wird, dass der Gateway-Host selbst vertrauenswürdig ist. HTTP-API-Endpunkte folgen unabhängig davon dem normalen Authentifizierungsmodus des Gateways (Token/Passwort). Um explizite Shared-Secret-Zugangsdaten über Serve zu erzwingen, setzen Sie `gateway.auth.allowTailscale: false` und verwenden Sie `gateway.auth.mode: "token"` oder `"password"`.

**Option C: Tailnet-Bindung (ohne Serve)**

bashCopy code
[code]
    openclaw config set gateway.bind tailnetopenclaw gateway restart
[/code]

Öffnen Sie anschließend `http://<tailscale-ip>:18789` (Token erforderlich).

## Persistenz und Backups

Der OpenClaw-Zustand liegt unter:

  * `~/.openclaw/` — `openclaw.json`, agentenspezifische `auth-profiles.json`, Channel-/Provider-Zustand und Sitzungsdaten.
  * `~/.openclaw/workspace/` — der Agent-Arbeitsbereich ([SOUL.md](<http://SOUL.md>), Speicher, Artefakte).


Diese Daten überstehen Droplet-Neustarts. So erstellen Sie einen portablen Snapshot:

bashCopy code
[code]
    openclaw backup create
[/code]

DigitalOcean-Snapshots sichern das gesamte Droplet; `openclaw backup create` ist über Hosts hinweg portabel.

## Tipps für 1 GB RAM

Das 6-USD-Droplet hat nur 1 GB RAM. Damit alles reibungslos läuft:

  * Stellen Sie sicher, dass der obige Swap-Schritt in `/etc/fstab` steht, damit er Neustarts übersteht.
  * Bevorzugen Sie API-basierte Modelle (Claude, GPT) gegenüber lokalen Modellen — lokale LLM-Inferenz passt nicht in 1 GB.
  * Setzen Sie `agents.defaults.model.primary` auf ein kleineres Modell, wenn bei großen Prompts OOMs auftreten.
  * Überwachen Sie mit `free -h` und `htop`.


## Fehlerbehebung

**Gateway startet nicht** \-- Führen Sie `openclaw doctor --non-interactive` aus und prüfen Sie die Logs mit `journalctl --user -u openclaw-gateway.service -n 50`.

**Port bereits in Verwendung** \-- Führen Sie `lsof -i :18789` aus, um den Prozess zu finden, und stoppen Sie ihn dann.

**Nicht genügend Arbeitsspeicher** \-- Prüfen Sie mit `free -h`, ob Swap aktiv ist. Wenn weiterhin OOM auftritt, verwenden Sie API-basierte Modelle (Claude, GPT) statt lokaler Modelle oder wechseln Sie zu einem 2-GB-Droplet.

## Nächste Schritte

  * [Channels](</de/channels>) \-- Telegram, WhatsApp, Discord und weitere verbinden
  * [Gateway-Konfiguration](</de/gateway/configuration>) \-- alle Konfigurationsoptionen
  * [Aktualisierung](</de/install/updating>) \-- OpenClaw aktuell halten


## Verwandt

  * [Installationsübersicht](</de/install>)
  * [Fly.io](</de/install/fly>)
  * [Hetzner](</de/install/hetzner>)
  * [VPS-Hosting](</de/vps>)


Was this useful?YesNo