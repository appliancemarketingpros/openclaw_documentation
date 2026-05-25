---
title: Oracle Cloud
source_url: https://docs.openclaw.ai/nl/install/oracle
scraped_at: 2026-05-25
---

Voer een persistente OpenClaw Gateway uit op de **Always Free** ARM-laag van Oracle Cloud (tot 4 OCPU, 24 GB RAM, 200 GB opslag) zonder kosten.

## Vereisten

  * Oracle Cloud-account ([registreren](<https://www.oracle.com/cloud/free/>)) -- zie de [registratiegids van de community](<https://gist.github.com/rssnyder/51e3cfedd730e7dd5f4a816143b25dbd>) als je problemen ondervindt
  * Tailscale-account (gratis op [tailscale.com](<https://tailscale.com>))
  * Een SSH-sleutelpaar
  * Ongeveer 30 minuten


## Installatie

* ### Maak een OCI-instantie aan

  1. Log in op de [Oracle Cloud Console](<https://cloud.oracle.com/>).
  2. Ga naar **Compute > Instances > Create Instance**.
  3. Configureer: 
     * **Naam:** `openclaw`
     * **Image:** Ubuntu 24.04 (aarch64)
     * **Shape:** `VM.Standard.A1.Flex` (Ampere ARM)
     * **OCPU's:** 2 (of tot 4)
     * **Geheugen:** 12 GB (of tot 24 GB)
     * **Bootvolume:** 50 GB (tot 200 GB gratis)
     * **SSH-sleutel:** Voeg je publieke sleutel toe
  4. Klik op **Create** en noteer het openbare IP-adres.


* ### Maak verbinding en werk het systeem bij

bashCopy code
[code]
    ssh ubuntu@YOUR_PUBLIC_IP sudo apt update && sudo apt upgrade -ysudo apt install -y build-essential
[/code]

`build-essential` is vereist voor ARM-compilatie van sommige afhankelijkheden.

* ### Configureer gebruiker en hostnaam

bashCopy code
[code]
    sudo hostnamectl set-hostname openclawsudo passwd ubuntusudo loginctl enable-linger ubuntu
[/code]

Het inschakelen van linger houdt gebruikersservices actief na afmelden.

* ### Installeer Tailscale

bashCopy code
[code]
    curl -fsSL https://tailscale.com/install.sh | shsudo tailscale up --ssh --hostname=openclaw
[/code]

Maak vanaf nu verbinding via Tailscale: `ssh ubuntu@openclaw`.

* ### Installeer OpenClaw

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bashsource ~/.bashrc
[/code]

Wanneer je wordt gevraagd "How do you want to hatch your bot?", selecteer je **Do this later**.

* ### Configureer de Gateway

Gebruik token-authenticatie met Tailscale Serve voor veilige externe toegang.

bashCopy code
[code]
    openclaw config set gateway.bind loopbackopenclaw config set gateway.auth.mode tokenopenclaw doctor --generate-gateway-tokenopenclaw config set gateway.tailscale.mode serveopenclaw config set gateway.trustedProxies '["127.0.0.1"]' systemctl --user restart openclaw-gateway.service
[/code]

`gateway.trustedProxies=["127.0.0.1"]` is hier alleen bedoeld voor de verwerking van doorgestuurde IP's/lokale clients door de lokale Tailscale Serve-proxy. Het is **niet** `gateway.auth.mode: "trusted-proxy"`. Diff-viewerroutes behouden fail-closed gedrag in deze configuratie: ruwe viewerverzoeken naar `127.0.0.1` zonder doorgestuurde proxyheaders kunnen `Diff not found` retourneren. Gebruik `mode=file` / `mode=both` voor bijlagen, of schakel bewust externe viewers in en stel `plugins.entries.diffs.config.viewerBaseUrl` in (of geef een proxy-`baseUrl` door) als je deelbare viewerlinks nodig hebt.

* ### Vergrendel VCN-beveiliging

Blokkeer al het verkeer behalve Tailscale aan de netwerkrand:

  1. Ga naar **Networking > Virtual Cloud Networks** in de OCI Console.
  2. Klik op je VCN en daarna op **Security Lists > Default Security List**.
  3. **Verwijder** alle ingress-regels behalve `0.0.0.0/0 UDP 41641` (Tailscale).
  4. Behoud de standaard egress-regels (alle uitgaande verbindingen toestaan).


Dit blokkeert SSH op poort 22, HTTP, HTTPS en al het andere aan de netwerkrand. Vanaf dit punt kun je alleen nog via Tailscale verbinding maken.

* ### Verifieer

bashCopy code
[code]
    openclaw --versionsystemctl --user status openclaw-gateway.servicetailscale serve statuscurl http://localhost:18789
[/code]

Open de Control UI vanaf elk apparaat op je tailnet:

CodeCopy code
[code]
    https://openclaw.<tailnet-name>.ts.net/
[/code]

Vervang `<tailnet-name>` door je tailnetnaam (zichtbaar in `tailscale status`).

## Verifieer de beveiligingshouding

Met de VCN vergrendeld (alleen UDP 41641 open) en de Gateway gebonden aan loopback, wordt openbaar verkeer aan de netwerkrand geblokkeerd en is beheertoegang alleen via het tailnet mogelijk. Daardoor zijn meerdere traditionele VPS-hardeningstappen niet meer nodig:

Traditionele stap | Nodig? | Waarom  
---|---|---  
UFW-firewall | Nee | De VCN blokkeert verkeer voordat het de instantie bereikt.  
fail2ban | Nee | Poort 22 is geblokkeerd op de VCN; geen brute-force-oppervlak.  
sshd-hardening | Nee | Tailscale SSH gebruikt geen sshd.  
Root-login uitschakelen | Nee | Tailscale authenticeert via tailnetidentiteit, niet via systeemgebruikers.  
Alleen SSH-sleutel-auth | Nee | Hetzelfde — tailnetidentiteit vervangt systeem-SSH-sleutels.  
IPv6-hardening | Meestal niet | Afhankelijk van VCN-/subnetinstellingen; verifieer wat werkelijk is toegewezen/blootgesteld.  
  
Nog steeds aanbevolen:

  * `chmod 700 ~/.openclaw` om machtigingen voor credentialbestanden te beperken.
  * `openclaw security audit` voor een OpenClaw-specifieke controle van de beveiligingshouding.
  * Regelmatig `sudo apt update && sudo apt upgrade` voor OS-patches.
  * Controleer periodiek apparaten in de [Tailscale-beheerconsole](<https://login.tailscale.com/admin>).


Snelle verificatieopdrachten:

bashCopy code
[code]
    # Confirm no public ports are listeningsudo ss -tlnp | grep -v '127.0.0.1\|::1' # Verify Tailscale SSH is activetailscale status | grep -q 'offers: ssh' && echo "Tailscale SSH active" # Optional: disable sshd entirely once Tailscale SSH is confirmed workingsudo systemctl disable --now ssh
[/code]

## ARM-opmerkingen

De Always Free-laag is ARM (`aarch64`). De meeste OpenClaw-functies werken prima; een klein aantal native binaries heeft ARM-builds nodig:

  * Node.js, Telegram, WhatsApp (Baileys): pure JavaScript, geen problemen.
  * De meeste npm-pakketten met native code: vooraf gebouwde `linux-arm64`-artefacten beschikbaar.
  * Optionele CLI-helpers (bijv. Go-/Rust-binaries geleverd door Skills): controleer op een `aarch64`\- / `linux-arm64`-release voordat je ze installeert.


Verifieer de architectuur met `uname -m` (moet `aarch64` afdrukken). Installeer binaries zonder ARM-build vanuit broncode of sla ze over.

## Persistentie en back-ups

OpenClaw-status bevindt zich onder:

  * `~/.openclaw/` — `openclaw.json`, per-agent `auth-profiles.json`, kanaal-/providerstatus en sessiegegevens.
  * `~/.openclaw/workspace/` — de agentworkspace ([SOUL.md](<http://SOUL.md>), geheugen, artefacten).


Deze blijven behouden na herstarts. Maak een draagbare snapshot met:

bashCopy code
[code]
    openclaw backup create
[/code]

## Fallback: SSH-tunnel

Als Tailscale Serve niet werkt, gebruik dan een SSH-tunnel vanaf je lokale machine:

bashCopy code
[code]
    ssh -L 18789:127.0.0.1:18789 ubuntu@openclaw
[/code]

Open daarna `http://localhost:18789`.

## Probleemoplossing

**Het aanmaken van de instantie mislukt ("Out of capacity")** \-- Gratis ARM-instanties zijn populair. Probeer een ander beschikbaarheidsdomein of probeer het opnieuw buiten piekuren.

**Tailscale maakt geen verbinding** \-- Voer `sudo tailscale up --ssh --hostname=openclaw --reset` uit om opnieuw te authenticeren.

**Gateway start niet** \-- Voer `openclaw doctor --non-interactive` uit en controleer logs met `journalctl --user -u openclaw-gateway.service -n 50`.

**ARM-binaryproblemen** \-- De meeste npm-pakketten werken op ARM64. Zoek voor native binaries naar `linux-arm64`\- of `aarch64`-releases. Verifieer de architectuur met `uname -m`.

## Volgende stappen

  * [Kanalen](</nl/channels>) \-- verbind Telegram, WhatsApp, Discord en meer
  * [Gateway-configuratie](</nl/gateway/configuration>) \-- alle configuratieopties
  * [Bijwerken](</nl/install/updating>) \-- houd OpenClaw up-to-date


## Gerelateerd

  * [Installatieoverzicht](</nl/install>)
  * [GCP](</nl/install/gcp>)
  * [VPS-hosting](</nl/vps>)


Was this useful?YesNo