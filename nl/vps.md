---
title: Linux-server
source_url: https://docs.openclaw.ai/nl/vps
scraped_at: 2026-05-25
---

Voer de OpenClaw Gateway uit op elke Linux-server of cloud-VPS. Deze pagina helpt je een provider te kiezen, legt uit hoe cloudimplementaties werken en behandelt generieke Linux- tuning die overal van toepassing is.

## Kies een provider

[**Railway** [**Northflank** [**DigitalOcean** [**Oracle Cloud** [**Fly.io** [**Hetzner** [**Hostinger** [**GCP** [**Azure** [**exe.dev** [**Raspberry Pi** **AWS (EC2 / Lightsail / free tier)** werkt ook goed. Een video-uitleg van de community is beschikbaar op [x.com/techfrenAJ/status/2014934471095812547](<https://x.com/techfrenAJ/status/2014934471095812547>) (communitybron -- kan onbeschikbaar worden). Hoe cloudopstellingen werken

  * De **Gateway draait op de VPS** en beheert status + workspace.
  * Je maakt verbinding vanaf je laptop of telefoon via de **Control UI** of **Tailscale/SSH**.
  * Behandel de VPS als de bron van waarheid en **maak regelmatig een back-up** van de status + workspace.
  * Veilige standaard: houd de Gateway op loopback en benader deze via een SSH-tunnel of Tailscale Serve. Als je bindt aan `lan` of `tailnet`, vereis dan `gateway.auth.token` of `gateway.auth.password`.

Gerelateerde pagina's: [Gateway-toegang op afstand](</nl/gateway/remote>), [Platformhub](</nl/platforms>). Beveilig eerst beheertoegang Voordat je OpenClaw op een openbare VPS installeert, bepaal je hoe je de machine zelf wilt beheren.

  * Als je alleen Tailnet-beheertoegang wilt, installeer dan eerst Tailscale, voeg de VPS toe aan je tailnet, verifieer een tweede SSH-sessie via het Tailscale-IP-adres of de MagicDNS-naam en beperk daarna openbare SSH.
  * Als je Tailscale niet gebruikt, pas dan gelijkwaardige beveiliging toe voor je SSH- pad voordat je meer services blootstelt.
  * Dit staat los van Gateway-toegang. Je kunt OpenClaw nog steeds gebonden houden aan loopback en een SSH-tunnel of Tailscale Serve gebruiken voor het dashboard.

Tailscale-specifieke Gateway-opties staan in [Tailscale](</nl/gateway/tailscale>). Gedeelde bedrijfsagent op een VPS Een enkele agent voor een team uitvoeren is een geldige opstelling wanneer elke gebruiker binnen dezelfde vertrouwensgrens valt en de agent alleen zakelijk wordt gebruikt.

  * Houd deze op een toegewezen runtime (VPS/VM/container + toegewezen OS-gebruiker/accounts).
  * Meld die runtime niet aan bij persoonlijke Apple-/Google-accounts of persoonlijke browser-/wachtwoordmanagerprofielen.
  * Als gebruikers vijandig tegenover elkaar kunnen staan, splits dan per Gateway/host/OS-gebruiker.

Details van het beveiligingsmodel: [Beveiliging](</nl/gateway/security>). Nodes gebruiken met een VPS Je kunt de Gateway in de cloud houden en **nodes** koppelen op je lokale apparaten (Mac/iOS/Android/headless). Nodes bieden lokaal scherm/camera/canvas en `system.run`\- mogelijkheden terwijl de Gateway in de cloud blijft. Docs: [Nodes](</nl/nodes>), [Nodes CLI](</nl/cli/nodes>). Opstarttuning voor kleine VM's en ARM-hosts Als CLI-opdrachten traag aanvoelen op VM's met weinig vermogen (of ARM-hosts), schakel dan Node's modulecompilecache in: bashCopy code
[code]
    grep -q 'NODE_COMPILE_CACHE=/var/tmp/openclaw-compile-cache' ~/.bashrc || cat >> ~/.bashrc <<'EOF'export NODE_COMPILE_CACHE=/var/tmp/openclaw-compile-cachemkdir -p /var/tmp/openclaw-compile-cacheexport OPENCLAW_NO_RESPAWN=1EOFsource ~/.bashrc
[/code]

  * `NODE_COMPILE_CACHE` verbetert de opstarttijden van herhaalde opdrachten.
  * `OPENCLAW_NO_RESPAWN=1` voorkomt extra opstartoverhead van een zelf-herstartpad.
  * De eerste opdrachtuitvoering warmt de cache op; volgende uitvoeringen zijn sneller.
  * Zie [Raspberry Pi](</nl/install/raspberry-pi>) voor Raspberry Pi-specifieke informatie.

systemd-tuningchecklist (optioneel) Voor VM-hosts die `systemd` gebruiken, overweeg:

  * Voeg service-env toe voor een stabiel opstartpad: 
    * `OPENCLAW_NO_RESPAWN=1`
    * `NODE_COMPILE_CACHE=/var/tmp/openclaw-compile-cache`
  * Houd herstartgedrag expliciet: 
    * `Restart=always`
    * `RestartSec=2`
    * `TimeoutStartSec=90`
  * Geef de voorkeur aan SSD-ondersteunde schijven voor status-/cachepaden om random-I/O-opstartvertragingen te verminderen.

Voor het standaardpad `openclaw onboard --install-daemon` bewerk je de gebruikerseenheid: bashCopy code
[code]
    systemctl --user edit openclaw-gateway.service
[/code]

iniCopy code
[code]
    [Service]Environment=OPENCLAW_NO_RESPAWN=1Environment=NODE_COMPILE_CACHE=/var/tmp/openclaw-compile-cacheRestart=alwaysRestartSec=2TimeoutStartSec=90
[/code]

Als je bewust een systeemeenheid hebt geïnstalleerd, bewerk dan `openclaw-gateway.service` via `sudo systemctl edit openclaw-gateway.service`. Hoe `Restart=`-beleid geautomatiseerd herstel helpt: [systemd kan serviceherstel automatiseren](<https://www.redhat.com/en/blog/systemd-automate-recovery>). Zie voor Linux-OOM-gedrag, slachtofferselectie voor childprocessen en `exit 137`\- diagnostiek [Linux-geheugendruk en OOM-kills](</nl/platforms/linux#memory-pressure-and-oom-kills>). Gerelateerd

  * [Installatieoverzicht](</nl/install>)
  * [DigitalOcean](</nl/install/digitalocean>)
  * [Fly.io](</nl/install/fly>)
  * [Hetzner](</nl/install/hetzner>)

](</nl/install/raspberry-pi>) Was this useful?YesNo ](</nl/install/exe-dev>)](</nl/install/azure>)](</nl/install/gcp>)](</nl/install/hostinger>)](</nl/install/hetzner>)](</nl/install/fly>)](</nl/install/oracle>)](</nl/install/digitalocean>)](</nl/install/northflank>)](</nl/install/railway>)