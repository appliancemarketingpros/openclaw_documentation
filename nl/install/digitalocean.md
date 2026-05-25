---
title: DigitalOcean
source_url: https://docs.openclaw.ai/nl/install/digitalocean
scraped_at: 2026-05-25
---

Voer een persistente OpenClaw Gateway uit op een DigitalOcean Droplet (~$6/maand voor het 1 GB Basic-abonnement).

DigitalOcean is de eenvoudigste betaalde VPS-route. Als je goedkopere of gratis opties verkiest:

  * [Hetzner](</nl/install/hetzner>) — €3,79/mnd, meer cores/RAM per dollar.
  * [Oracle Cloud](</nl/install/oracle>) — Always Free ARM (tot 4 OCPU, 24 GB RAM), maar aanmelden kan lastig zijn en is alleen ARM.


## Vereisten

  * DigitalOcean-account ([aanmelden](<https://cloud.digitalocean.com/registrations/new>))
  * SSH-sleutelpaar (of bereidheid om wachtwoordauthenticatie te gebruiken)
  * Ongeveer 20 minuten


## Instellen

* ### Een Droplet maken

  1. Log in bij [DigitalOcean](<https://cloud.digitalocean.com/>).
  2. Klik op **Create > Droplets**.
  3. Kies: 
     * **Regio:** Dichtst bij jou
     * **Image:** Ubuntu 24.04 LTS
     * **Grootte:** Basic, Regular, 1 vCPU / 1 GB RAM / 25 GB SSD
     * **Authenticatie:** SSH-sleutel (aanbevolen) of wachtwoord
  4. Klik op **Create Droplet** en noteer het IP-adres.


* ### Verbinden en installeren

bashCopy code
[code]
    ssh root@YOUR_DROPLET_IP apt update && apt upgrade -y # Install Node.js 24curl -fsSL https://deb.nodesource.com/setup_24.x | bash -apt install -y nodejs # Install OpenClawcurl -fsSL https://openclaw.ai/install.sh | bash # Create the non-root user that will own OpenClaw state and services.adduser openclawusermod -aG sudo openclawloginctl enable-linger openclaw su - openclawopenclaw --version
[/code]

Gebruik de root-shell alleen voor de systeem-bootstrap. Voer OpenClaw-opdrachten uit als de niet-rootgebruiker `openclaw`, zodat de status onder `/home/openclaw/.openclaw/` staat en de Gateway wordt geïnstalleerd als systemd-service van die gebruiker.

* ### Onboarding uitvoeren

bashCopy code
[code]
    openclaw onboard --install-daemon
[/code]

De wizard leidt je door modelauthenticatie, kanaalconfiguratie, het genereren van een gateway-token en daemoninstallatie (systemd).

* ### Swap toevoegen (aanbevolen voor 1 GB Droplets)

bashCopy code
[code]
    fallocate -l 2G /swapfilechmod 600 /swapfilemkswap /swapfileswapon /swapfileecho '/swapfile none swap sw 0 0' >> /etc/fstab
[/code]

* ### De gateway verifiëren

bashCopy code
[code]
    openclaw statussystemctl --user status openclaw-gateway.servicejournalctl --user -u openclaw-gateway.service -f
[/code]

* ### Toegang tot de Control UI

De gateway bindt standaard aan loopback. Kies een van deze opties.

**Optie A: SSH-tunnel (eenvoudigst)**

bashCopy code
[code]
    # From your local machinessh -L 18789:localhost:18789 root@YOUR_DROPLET_IP
[/code]

Open daarna `http://localhost:18789`.

**Optie B: Tailscale Serve**

bashCopy code
[code]
    curl -fsSL https://tailscale.com/install.sh | sudo shsudo tailscale upopenclaw config set gateway.tailscale.mode serveopenclaw gateway restart
[/code]

Open daarna `https://<magicdns>/` vanaf elk apparaat op je tailnet.

Tailscale Serve authenticeert Control UI- en WebSocket-verkeer via tailnet-identiteitsheaders, waarbij wordt aangenomen dat de gateway-host zelf vertrouwd is. HTTP API-eindpunten volgen ongeacht dit de normale auth-modus van de gateway (token/wachtwoord). Stel `gateway.auth.allowTailscale: false` in en gebruik `gateway.auth.mode: "token"` of `"password"` om expliciete gedeelde-geheime aanmeldgegevens via Serve te vereisen.

**Optie C: Tailnet-bind (geen Serve)**

bashCopy code
[code]
    openclaw config set gateway.bind tailnetopenclaw gateway restart
[/code]

Open daarna `http://<tailscale-ip>:18789` (token vereist).

## Persistentie en back-ups

OpenClaw-status staat onder:

  * `~/.openclaw/` — `openclaw.json`, per-agent `auth-profiles.json`, kanaal-/providerstatus en sessiegegevens.
  * `~/.openclaw/workspace/` — de agentwerkruimte ([SOUL.md](<http://SOUL.md>), geheugen, artefacten).


Deze blijven behouden na herstarts van de Droplet. Een draagbare snapshot maken:

bashCopy code
[code]
    openclaw backup create
[/code]

DigitalOcean-snapshots maken een back-up van de hele Droplet; `openclaw backup create` is overdraagbaar tussen hosts.

## Tips voor 1 GB RAM

De Droplet van $6 heeft slechts 1 GB RAM. Om alles soepel te houden:

  * Zorg ervoor dat de swapstap hierboven in `/etc/fstab` staat, zodat deze herstarts overleeft.
  * Geef de voorkeur aan API-gebaseerde modellen (Claude, GPT) boven lokale modellen — lokale LLM-inferentie past niet in 1 GB.
  * Stel `agents.defaults.model.primary` in op een kleiner model als je OOMs krijgt bij grote prompts.
  * Monitor met `free -h` en `htop`.


## Problemen oplossen

**Gateway start niet** \-- Voer `openclaw doctor --non-interactive` uit en controleer logs met `journalctl --user -u openclaw-gateway.service -n 50`.

**Poort is al in gebruik** \-- Voer `lsof -i :18789` uit om het proces te vinden en stop het daarna.

**Onvoldoende geheugen** \-- Controleer met `free -h` of swap actief is. Als je nog steeds OOM krijgt, gebruik dan API-gebaseerde modellen (Claude, GPT) in plaats van lokale modellen, of upgrade naar een 2 GB Droplet.

## Volgende stappen

  * [Kanalen](</nl/channels>) \-- verbind Telegram, WhatsApp, Discord en meer
  * [Gateway-configuratie](</nl/gateway/configuration>) \-- alle configuratieopties
  * [Bijwerken](</nl/install/updating>) \-- houd OpenClaw up-to-date


## Gerelateerd

  * [Installatieoverzicht](</nl/install>)
  * [Fly.io](</nl/install/fly>)
  * [Hetzner](</nl/install/hetzner>)
  * [VPS-hosting](</nl/vps>)


Was this useful?YesNo