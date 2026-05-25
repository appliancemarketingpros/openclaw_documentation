---
title: Oracle Cloud
source_url: https://docs.openclaw.ai/de/install/oracle
scraped_at: 2026-05-25
---

Führen Sie ein dauerhaftes OpenClaw Gateway auf der **Always Free** -ARM-Stufe von Oracle Cloud aus (bis zu 4 OCPU, 24 GB RAM, 200 GB Speicher), ohne Kosten.

## Voraussetzungen

  * Oracle Cloud-Konto ([signup](<https://www.oracle.com/cloud/free/>)) -- siehe [Community-Registrierungsleitfaden](<https://gist.github.com/rssnyder/51e3cfedd730e7dd5f4a816143b25dbd>), falls Probleme auftreten
  * Tailscale-Konto (kostenlos unter [tailscale.com](<https://tailscale.com>))
  * Ein SSH-Schlüsselpaar
  * Etwa 30 Minuten


## Einrichtung

* ### Create an OCI instance

  1. Melden Sie sich bei der [Oracle Cloud Console](<https://cloud.oracle.com/>) an.
  2. Navigieren Sie zu **Compute > Instances > Create Instance**.
  3. Konfigurieren Sie: 
     * **Name:** `openclaw`
     * **Image:** Ubuntu 24.04 (aarch64)
     * **Shape:** `VM.Standard.A1.Flex` (Ampere ARM)
     * **OCPUs:** 2 (oder bis zu 4)
     * **Memory:** 12 GB (oder bis zu 24 GB)
     * **Boot volume:** 50 GB (bis zu 200 GB kostenlos)
     * **SSH key:** Fügen Sie Ihren öffentlichen Schlüssel hinzu
  4. Klicken Sie auf **Create** und notieren Sie die öffentliche IP-Adresse.


* ### Connect and update the system

bashCopy code
[code]
    ssh ubuntu@YOUR_PUBLIC_IP sudo apt update && sudo apt upgrade -ysudo apt install -y build-essential
[/code]

`build-essential` ist für die ARM-Kompilierung einiger Abhängigkeiten erforderlich.

* ### Configure user and hostname

bashCopy code
[code]
    sudo hostnamectl set-hostname openclawsudo passwd ubuntusudo loginctl enable-linger ubuntu
[/code]

Durch das Aktivieren von linger laufen Benutzerdienste auch nach dem Abmelden weiter.

* ### Install Tailscale

bashCopy code
[code]
    curl -fsSL https://tailscale.com/install.sh | shsudo tailscale up --ssh --hostname=openclaw
[/code]

Verbinden Sie sich ab jetzt über Tailscale: `ssh ubuntu@openclaw`.

* ### Install OpenClaw

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bashsource ~/.bashrc
[/code]

Wenn Sie mit „How do you want to hatch your bot?“ gefragt werden, wählen Sie **Do this later**.

* ### Configure the gateway

Verwenden Sie Token-Authentifizierung mit Tailscale Serve für sicheren Fernzugriff.

bashCopy code
[code]
    openclaw config set gateway.bind loopbackopenclaw config set gateway.auth.mode tokenopenclaw doctor --generate-gateway-tokenopenclaw config set gateway.tailscale.mode serveopenclaw config set gateway.trustedProxies '["127.0.0.1"]' systemctl --user restart openclaw-gateway.service
[/code]

`gateway.trustedProxies=["127.0.0.1"]` dient hier nur der Forwarded-IP-/Local-Client-Verarbeitung des lokalen Tailscale Serve-Proxys. Es ist **nicht** `gateway.auth.mode: "trusted-proxy"`. Diff-Viewer-Routen behalten in dieser Einrichtung ein Fail-Closed-Verhalten bei: Rohe `127.0.0.1`-Viewer-Anfragen ohne weitergeleitete Proxy-Header können `Diff not found` zurückgeben. Verwenden Sie `mode=file` / `mode=both` für Anhänge, oder aktivieren Sie bewusst Remote-Viewer und setzen Sie `plugins.entries.diffs.config.viewerBaseUrl` (oder übergeben Sie eine Proxy-`baseUrl`), wenn Sie teilbare Viewer-Links benötigen.

* ### Lock down VCN security

Blockieren Sie am Netzwerkrand sämtlichen Traffic außer Tailscale:

  1. Gehen Sie in der OCI Console zu **Networking > Virtual Cloud Networks**.
  2. Klicken Sie auf Ihre VCN und dann auf **Security Lists > Default Security List**.
  3. **Entfernen** Sie alle Ingress-Regeln außer `0.0.0.0/0 UDP 41641` (Tailscale).
  4. Behalten Sie die standardmäßigen Egress-Regeln bei (alle ausgehenden Verbindungen erlauben).


Dadurch werden SSH auf Port 22, HTTP, HTTPS und alles Weitere am Netzwerkrand blockiert. Ab diesem Punkt können Sie sich nur noch über Tailscale verbinden.

* ### Verify

bashCopy code
[code]
    openclaw --versionsystemctl --user status openclaw-gateway.servicetailscale serve statuscurl http://localhost:18789
[/code]

Greifen Sie von jedem Gerät in Ihrem Tailnet auf die Control UI zu:

CodeCopy code
[code]
    https://openclaw.<tailnet-name>.ts.net/
[/code]

Ersetzen Sie `<tailnet-name>` durch den Namen Ihres Tailnets (sichtbar in `tailscale status`).

## Sicherheitsstatus überprüfen

Wenn die VCN abgesperrt ist (nur UDP 41641 offen) und das Gateway an loopback gebunden ist, wird öffentlicher Traffic am Netzwerkrand blockiert und Administratorzugriff ist nur über das Tailnet möglich. Dadurch entfallen mehrere klassische Schritte zur VPS-Härtung:

Klassischer Schritt | Erforderlich? | Warum  
---|---|---  
UFW-Firewall | Nein | Die VCN blockiert Traffic, bevor er die Instanz erreicht.  
fail2ban | Nein | Port 22 ist an der VCN blockiert; keine Brute-Force-Angriffsfläche.  
sshd-Härtung | Nein | Tailscale SSH verwendet kein sshd.  
Root-Login deaktivieren | Nein | Tailscale authentifiziert über Tailnet-Identität, nicht Systembenutzer.  
Nur SSH-Schlüsselauthentifizierung | Nein | Dasselbe — Tailnet-Identität ersetzt System-SSH-Schlüssel.  
IPv6-Härtung | Meist nicht | Hängt von VCN-/Subnetzeinstellungen ab; prüfen Sie, was tatsächlich zugewiesen/exponiert ist.  
  
Weiterhin empfohlen:

  * `chmod 700 ~/.openclaw`, um die Berechtigungen für Anmeldedaten-Dateien einzuschränken.
  * `openclaw security audit` für eine OpenClaw-spezifische Sicherheitsprüfung.
  * Regelmäßiges `sudo apt update && sudo apt upgrade` für OS-Patches.
  * Prüfen Sie regelmäßig Geräte in der [Tailscale-Admin-Konsole](<https://login.tailscale.com/admin>).


Schnelle Verifizierungsbefehle:

bashCopy code
[code]
    # Confirm no public ports are listeningsudo ss -tlnp | grep -v '127.0.0.1\|::1' # Verify Tailscale SSH is activetailscale status | grep -q 'offers: ssh' && echo "Tailscale SSH active" # Optional: disable sshd entirely once Tailscale SSH is confirmed workingsudo systemctl disable --now ssh
[/code]

## ARM-Hinweise

Die Always Free-Stufe ist ARM (`aarch64`). Die meisten OpenClaw-Funktionen funktionieren problemlos; eine kleine Anzahl nativer Binärdateien benötigt ARM-Builds:

  * Node.js, Telegram, WhatsApp (Baileys): reines JavaScript, keine Probleme.
  * Die meisten npm-Pakete mit nativem Code: vorgefertigte `linux-arm64`-Artefakte verfügbar.
  * Optionale CLI-Helfer (z. B. Go-/Rust-Binärdateien, die von Skills ausgeliefert werden): Prüfen Sie vor der Installation, ob ein `aarch64`\- / `linux-arm64`-Release verfügbar ist.


Überprüfen Sie die Architektur mit `uname -m` (sollte `aarch64` ausgeben). Installieren Sie Binärdateien ohne ARM-Build aus dem Quellcode oder überspringen Sie sie.

## Persistenz und Backups

Der OpenClaw-Zustand liegt unter:

  * `~/.openclaw/` — `openclaw.json`, agentenspezifische `auth-profiles.json`, Channel-/Provider-Zustand und Sitzungsdaten.
  * `~/.openclaw/workspace/` — der Agent-Arbeitsbereich ([SOUL.md](<http://SOUL.md>), Speicher, Artefakte).


Diese Daten überstehen Neustarts. So erstellen Sie einen portablen Snapshot:

bashCopy code
[code]
    openclaw backup create
[/code]

## Fallback: SSH-Tunnel

Wenn Tailscale Serve nicht funktioniert, verwenden Sie einen SSH-Tunnel von Ihrem lokalen Rechner:

bashCopy code
[code]
    ssh -L 18789:127.0.0.1:18789 ubuntu@openclaw
[/code]

Öffnen Sie anschließend `http://localhost:18789`.

## Fehlerbehebung

**Instanzerstellung schlägt fehl („Out of capacity“) ** -- ARM-Instanzen der kostenlosen Stufe sind beliebt. Versuchen Sie eine andere Availability Domain oder wiederholen Sie den Vorgang außerhalb der Spitzenzeiten.

**Tailscale verbindet sich nicht** \-- Führen Sie `sudo tailscale up --ssh --hostname=openclaw --reset` aus, um sich erneut zu authentifizieren.

**Gateway startet nicht** \-- Führen Sie `openclaw doctor --non-interactive` aus und prüfen Sie die Logs mit `journalctl --user -u openclaw-gateway.service -n 50`.

**ARM-Binärprobleme** \-- Die meisten npm-Pakete funktionieren auf ARM64. Suchen Sie bei nativen Binärdateien nach `linux-arm64`\- oder `aarch64`-Releases. Überprüfen Sie die Architektur mit `uname -m`.

## Nächste Schritte

  * [Channels](</de/channels>) \-- Telegram, WhatsApp, Discord und mehr verbinden
  * [Gateway-Konfiguration](</de/gateway/configuration>) \-- alle Konfigurationsoptionen
  * [Aktualisierung](</de/install/updating>) \-- OpenClaw aktuell halten


## Verwandte Themen

  * [Installationsübersicht](</de/install>)
  * [GCP](</de/install/gcp>)
  * [VPS-Hosting](</de/vps>)


Was this useful?YesNo