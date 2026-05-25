---
title: Raspberry Pi
source_url: https://docs.openclaw.ai/de/install/raspberry-pi
scraped_at: 2026-05-25
---

Führen Sie einen persistenten, dauerhaft aktiven OpenClaw Gateway auf einem Raspberry Pi aus. Da der Pi nur der Gateway ist (Modelle laufen in der Cloud über API), bewältigt selbst ein einfacher Pi die Arbeitslast gut — die typischen Hardwarekosten betragen **35–80 $ einmalig** , ohne monatliche Gebühren.

## Hardwarekompatibilität

Pi-Modell | RAM | Funktioniert? | Hinweise  
---|---|---|---  
Pi 5 | 4/8 GB | Am besten | Am schnellsten, empfohlen.  
Pi 4 | 4 GB | Gut | Idealer Bereich für die meisten Benutzer.  
Pi 4 | 2 GB | OK | Swap hinzufügen.  
Pi 4 | 1 GB | Knapp | Mit Swap möglich, minimale Konfiguration.  
Pi 3B+ | 1 GB | Langsam | Funktioniert, aber träge.  
Pi Zero 2 W | 512 MB | Nein | Nicht empfohlen.  
  
**Minimum:** 1 GB RAM, 1 Kern, 500 MB freier Speicherplatz, 64-Bit-Betriebssystem. **Empfohlen:** 2 GB+ RAM, 16 GB+ SD-Karte (oder USB-SSD), Ethernet.

## Voraussetzungen

  * Raspberry Pi 4 oder 5 mit 2 GB+ RAM (4 GB empfohlen)
  * MicroSD-Karte (16 GB+) oder USB-SSD (bessere Leistung)
  * Offizielles Pi-Netzteil
  * Netzwerkverbindung (Ethernet oder WLAN)
  * 64-Bit-Raspberry Pi OS (erforderlich -- verwenden Sie kein 32-Bit)
  * Etwa 30 Minuten


## Einrichtung

* ### Betriebssystem flashen

Verwenden Sie **Raspberry Pi OS Lite (64-bit)** \-- für einen Headless-Server wird kein Desktop benötigt.

  1. Laden Sie den [Raspberry Pi Imager](<https://www.raspberrypi.com/software/>) herunter.
  2. Wählen Sie das Betriebssystem: **Raspberry Pi OS Lite (64-bit)**.
  3. Konfigurieren Sie im Einstellungsdialog vorab: 
     * Hostname: `gateway-host`
     * SSH aktivieren
     * Benutzername und Passwort festlegen
     * WLAN konfigurieren (wenn Sie kein Ethernet verwenden)
  4. Flashen Sie auf Ihre SD-Karte oder Ihr USB-Laufwerk, setzen Sie es ein und starten Sie den Pi.


* ### Per SSH verbinden

bashCopy code
[code]
    ssh user@gateway-host
[/code]

* ### System aktualisieren

bashCopy code
[code]
    sudo apt update && sudo apt upgrade -ysudo apt install -y git curl build-essential # Set timezone (important for cron and reminders)sudo timedatectl set-timezone America/Chicago
[/code]

* ### Node.js 24 installieren

bashCopy code
[code]
    curl -fsSL https://deb.nodesource.com/setup_24.x | sudo -E bash -sudo apt install -y nodejsnode --version
[/code]

* ### Swap hinzufügen (wichtig bei 2 GB oder weniger)

bashCopy code
[code]
    sudo fallocate -l 2G /swapfilesudo chmod 600 /swapfilesudo mkswap /swapfilesudo swapon /swapfileecho '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab # Reduce swappiness for low-RAM devicesecho 'vm.swappiness=10' | sudo tee -a /etc/sysctl.confsudo sysctl -p
[/code]

* ### OpenClaw installieren

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash
[/code]

* ### Onboarding ausführen

bashCopy code
[code]
    openclaw onboard --install-daemon
[/code]

Folgen Sie dem Assistenten. API-Schlüssel werden für Headless-Geräte gegenüber OAuth empfohlen. Telegram ist der einfachste Kanal für den Einstieg.

* ### Überprüfen

bashCopy code
[code]
    openclaw statussystemctl --user status openclaw-gateway.servicejournalctl --user -u openclaw-gateway.service -f
[/code]

* ### Auf die Control UI zugreifen

Rufen Sie auf Ihrem Computer eine Dashboard-URL vom Pi ab:

bashCopy code
[code]
    ssh user@gateway-host 'openclaw dashboard --no-open'
[/code]

Erstellen Sie dann in einem anderen Terminal einen SSH-Tunnel:

bashCopy code
[code]
    ssh -N -L 18789:127.0.0.1:18789 user@gateway-host
[/code]

Öffnen Sie die ausgegebene URL in Ihrem lokalen Browser. Für dauerhaft aktiven Remote-Zugriff siehe [Tailscale-Integration](</de/gateway/tailscale>).

## Leistungstipps

**Verwenden Sie eine USB-SSD** \-- SD-Karten sind langsam und verschleißen. Eine USB-SSD verbessert die Leistung deutlich. Siehe den [Pi-USB-Boot-Leitfaden](<https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#usb-mass-storage-boot>).

**Modul-Compile-Cache aktivieren** \-- Beschleunigt wiederholte CLI-Aufrufe auf leistungsschwächeren Pi-Hosts:

bashCopy code
[code]
    grep -q 'NODE_COMPILE_CACHE=/var/tmp/openclaw-compile-cache' ~/.bashrc || cat >> ~/.bashrc <<'EOF' # pragma: allowlist secretexport NODE_COMPILE_CACHE=/var/tmp/openclaw-compile-cachemkdir -p /var/tmp/openclaw-compile-cacheexport OPENCLAW_NO_RESPAWN=1EOFsource ~/.bashrc
[/code]

**Speichernutzung reduzieren** \-- Geben Sie bei Headless-Setups GPU-Speicher frei und deaktivieren Sie ungenutzte Dienste:

bashCopy code
[code]
    echo 'gpu_mem=16' | sudo tee -a /boot/config.txtsudo systemctl disable bluetooth
[/code]

**systemd-Drop-in für stabile Neustarts** \-- Wenn dieser Pi hauptsächlich OpenClaw ausführt, fügen Sie ein Service-Drop-in hinzu:

bashCopy code
[code]
    systemctl --user edit openclaw-gateway.service
[/code]

iniCopy code
[code]
    [Service]Environment=OPENCLAW_NO_RESPAWN=1Environment=NODE_COMPILE_CACHE=/var/tmp/openclaw-compile-cacheRestart=alwaysRestartSec=2TimeoutStartSec=90
[/code]

Führen Sie anschließend `systemctl --user daemon-reload && systemctl --user restart openclaw-gateway.service` aus. Aktivieren Sie auf einem Headless-Pi außerdem einmalig Lingering, damit der Benutzerdienst eine Abmeldung übersteht: `sudo loginctl enable-linger "$(whoami)"`.

## Empfohlene Modelleinrichtung

Da der Pi nur den Gateway ausführt, verwenden Sie cloudgehostete API-Modelle:

jsonCopy code
[code]
    {  "agents": {    "defaults": {      "model": {        "primary": "anthropic/claude-sonnet-4-6",        "fallbacks": ["openai/gpt-5.4-mini"]      }    }  }}
[/code]

Führen Sie keine lokalen LLMs auf einem Pi aus — selbst kleine Modelle sind zu langsam, um nützlich zu sein. Lassen Sie Claude oder GPT die Modellarbeit übernehmen.

## Hinweise zu ARM-Binärdateien

Die meisten OpenClaw-Funktionen funktionieren auf ARM64 ohne Änderungen (Node.js, Telegram, WhatsApp/Baileys, Chromium). Die Binärdateien, für die gelegentlich ARM-Builds fehlen, sind typischerweise optionale Go/Rust-CLI-Tools, die von Skills ausgeliefert werden. Prüfen Sie die Release-Seite einer fehlenden Binärdatei auf `linux-arm64`\- / `aarch64`-Artefakte, bevor Sie auf das Erstellen aus dem Quellcode zurückgreifen.

## Persistenz und Backups

Der OpenClaw-Zustand liegt unter:

  * `~/.openclaw/` — `openclaw.json`, agentenspezifische `auth-profiles.json`, Kanal-/Provider-Zustand, Sitzungen.
  * `~/.openclaw/workspace/` — Agenten-Workspace ([SOUL.md](<http://SOUL.md>), Speicher, Artefakte).


Diese überstehen Neustarts. Erstellen Sie einen portablen Snapshot mit:

bashCopy code
[code]
    openclaw backup create
[/code]

Wenn Sie diese auf einer SSD speichern, verbessern sich sowohl Leistung als auch Lebensdauer im Vergleich zur SD-Karte.

## Fehlerbehebung

**Nicht genügend Arbeitsspeicher** \-- Überprüfen Sie mit `free -h`, ob Swap aktiv ist. Deaktivieren Sie ungenutzte Dienste (`sudo systemctl disable cups bluetooth avahi-daemon`). Verwenden Sie ausschließlich API-basierte Modelle.

**Langsame Leistung** \-- Verwenden Sie statt einer SD-Karte eine USB-SSD. Prüfen Sie CPU-Drosselung mit `vcgencmd get_throttled` (sollte `0x0` zurückgeben).

**Service startet nicht** \-- Prüfen Sie die Logs mit `journalctl --user -u openclaw-gateway.service --no-pager -n 100` und führen Sie `openclaw doctor --non-interactive` aus. Wenn dies ein Headless-Pi ist, prüfen Sie außerdem, ob Lingering aktiviert ist: `sudo loginctl enable-linger "$(whoami)"`.

**ARM-Binärprobleme** \-- Wenn ein Skill mit "exec format error" fehlschlägt, prüfen Sie, ob die Binärdatei einen ARM64-Build hat. Überprüfen Sie die Architektur mit `uname -m` (sollte `aarch64` anzeigen).

**WLAN-Verbindungsabbrüche** \-- Deaktivieren Sie WLAN-Energieverwaltung: `sudo iwconfig wlan0 power off`.

## Nächste Schritte

  * [Kanäle](</de/channels>) \-- Telegram, WhatsApp, Discord und weitere verbinden
  * [Gateway-Konfiguration](</de/gateway/configuration>) \-- alle Konfigurationsoptionen
  * [Aktualisieren](</de/install/updating>) \-- OpenClaw aktuell halten


## Verwandte Themen

  * [Installationsübersicht](</de/install>)
  * [Linux-Server](</de/vps>)
  * [Plattformen](</de/platforms>)


Was this useful?YesNo