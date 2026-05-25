---
title: GCP
source_url: https://docs.openclaw.ai/nl/install/gcp
scraped_at: 2026-05-25
---

Voer een permanente OpenClaw Gateway uit op een GCP Compute Engine-VM met Docker, met duurzame status, ingebakken binaries en veilig herstartgedrag.

Als je "OpenClaw 24/7 voor ~$5-12/mnd" wilt, is dit een betrouwbare installatie op Google Cloud. Prijzen verschillen per machinetype en regio; kies de kleinste VM die bij je workload past en schaal op als je OOM's tegenkomt.

## Wat doen we (in eenvoudige woorden)?

  * Maak een GCP-project en schakel facturering in
  * Maak een Compute Engine-VM
  * Installeer Docker (geisoleerde app-runtime)
  * Start de OpenClaw Gateway in Docker
  * Bewaar `~/.openclaw` \+ `~/.openclaw/workspace` op de host (overleeft herstarts/herbuilds)
  * Open de Control UI vanaf je laptop via een SSH-tunnel


Die gekoppelde status `~/.openclaw` bevat `openclaw.json`, per agent `agents/<agentId>/agent/auth-profiles.json` en `.env`.

De Gateway is toegankelijk via:

  * SSH-poortdoorschakeling vanaf je laptop
  * Directe poortblootstelling als je firewalls en tokens zelf beheert


Deze gids gebruikt Debian op GCP Compute Engine. Ubuntu werkt ook; stem pakketten overeenkomstig af. Zie [Docker](</nl/install/docker>) voor de generieke Docker-flow.

* * *

## Snelle route (ervaren operators)

  1. Maak een GCP-project + schakel de Compute Engine API in
  2. Maak een Compute Engine-VM (e2-small, Debian 12, 20GB)
  3. SSH naar de VM
  4. Installeer Docker
  5. Kloon de OpenClaw-repository
  6. Maak permanente hostmappen
  7. Configureer `.env` en `docker-compose.yml`
  8. Bak vereiste binaries in, bouw en start


* * *

## Wat je nodig hebt

  * GCP-account (free tier geschikt voor e2-micro)
  * gcloud CLI geinstalleerd (of gebruik Cloud Console)
  * SSH-toegang vanaf je laptop
  * Basisvertrouwdheid met SSH + kopieren/plakken
  * ~20-30 minuten
  * Docker en Docker Compose
  * Model-authenticatiegegevens
  * Optionele providerreferenties 
    * WhatsApp-QR
    * Telegram-bottoken
    * Gmail OAuth


* * *

* ### gcloud CLI installeren (of Console gebruiken)

**Optie A: gcloud CLI** (aanbevolen voor automatisering)

Installeer vanaf <https://cloud.google.com/sdk/docs/install>

Initialiseer en authenticeer:

bashCopy code
[code]
    gcloud initgcloud auth login
[/code]

**Optie B: Cloud Console**

Alle stappen kunnen via de web-UI op <https://console.cloud.google.com> worden uitgevoerd

* ### Een GCP-project maken

**CLI:**

bashCopy code
[code]
    gcloud projects create my-openclaw-project --name="OpenClaw Gateway"gcloud config set project my-openclaw-project
[/code]

Schakel facturering in op <https://console.cloud.google.com/billing> (vereist voor Compute Engine).

Schakel de Compute Engine API in:

bashCopy code
[code]
    gcloud services enable compute.googleapis.com
[/code]

**Console:**

  1. Ga naar IAM & Admin > Create Project
  2. Geef het een naam en maak het aan
  3. Schakel facturering in voor het project
  4. Navigeer naar APIs & Services > Enable APIs > zoek "Compute Engine API" > Enable


* ### De VM maken

**Machinetypen:**

Type | Specificaties | Kosten | Opmerkingen  
---|---|---|---  
e2-medium | 2 vCPU, 4GB RAM | ~$25/mnd | Meest betrouwbaar voor lokale Docker-builds  
e2-small | 2 vCPU, 2GB RAM | ~$12/mnd | Minimaal aanbevolen voor Docker-build  
e2-micro | 2 vCPU (gedeeld), 1GB RAM | Geschikt voor free tier | Mislukt vaak met Docker-build-OOM (exit 137)  
  
**CLI:**

bashCopy code
[code]
    gcloud compute instances create openclaw-gateway \  --zone=us-central1-a \  --machine-type=e2-small \  --boot-disk-size=20GB \  --image-family=debian-12 \  --image-project=debian-cloud
[/code]

**Console:**

  1. Ga naar Compute Engine > VM instances > Create instance
  2. Naam: `openclaw-gateway`
  3. Regio: `us-central1`, Zone: `us-central1-a`
  4. Machinetype: `e2-small`
  5. Opstartschijf: Debian 12, 20GB
  6. Maak aan


* ### Via SSH verbinden met de VM

**CLI:**

bashCopy code
[code]
    gcloud compute ssh openclaw-gateway --zone=us-central1-a
[/code]

**Console:**

Klik op de knop "SSH" naast je VM in het Compute Engine-dashboard.

Opmerking: verspreiding van SSH-sleutels kan na het maken van de VM 1-2 minuten duren. Als de verbinding wordt geweigerd, wacht dan en probeer opnieuw.

* ### Docker installeren (op de VM)

bashCopy code
[code]
    sudo apt-get updatesudo apt-get install -y git curl ca-certificatescurl -fsSL https://get.docker.com | sudo shsudo usermod -aG docker $USER
[/code]

Log uit en opnieuw in zodat de groepswijziging van kracht wordt:

bashCopy code
[code]
    exit
[/code]

Verbind daarna opnieuw via SSH:

bashCopy code
[code]
    gcloud compute ssh openclaw-gateway --zone=us-central1-a
[/code]

Controleer:

bashCopy code
[code]
    docker --versiondocker compose version
[/code]

* ### De OpenClaw-repository klonen

bashCopy code
[code]
    git clone https://github.com/openclaw/openclaw.gitcd openclaw
[/code]

Deze gids gaat ervan uit dat je een aangepaste image bouwt om binaire persistentie te garanderen.

* ### Permanente hostmappen maken

Docker-containers zijn vluchtig. Alle langlevende status moet op de host staan.

bashCopy code
[code]
    mkdir -p ~/.openclawmkdir -p ~/.openclaw/workspace
[/code]

* ### Omgevingsvariabelen configureren

Maak `.env` in de repositoryroot.

bashCopy code
[code]
    OPENCLAW_IMAGE=openclaw:latestOPENCLAW_GATEWAY_TOKEN=OPENCLAW_GATEWAY_BIND=lanOPENCLAW_GATEWAY_PORT=18789 OPENCLAW_CONFIG_DIR=/home/$USER/.openclawOPENCLAW_WORKSPACE_DIR=/home/$USER/.openclaw/workspace GOG_KEYRING_PASSWORD=XDG_CONFIG_HOME=/home/node/.openclaw
[/code]

Stel `OPENCLAW_GATEWAY_TOKEN` in wanneer je het stabiele Gateway-token via `.env` wilt beheren; configureer anders `gateway.auth.token` voordat je op clients over herstarts heen vertrouwt. Als geen van beide bronnen bestaat, gebruikt OpenClaw een runtime-only token voor die start. Genereer een keyringwachtwoord en plak het in `GOG_KEYRING_PASSWORD`:

bashCopy code
[code]
    openssl rand -hex 32
[/code]

**Commit dit bestand niet.**

Dit `.env`-bestand is bedoeld voor container-/runtime-env zoals `OPENCLAW_GATEWAY_TOKEN`. Opgeslagen provider-OAuth/API-key-authenticatie staat in het gekoppelde `~/.openclaw/agents/<agentId>/agent/auth-profiles.json`.

* ### Docker Compose-configuratie

Maak of update `docker-compose.yml`.

yamlCopy code
[code]
    services:  openclaw-gateway:    image: ${OPENCLAW_IMAGE}    build: .    restart: unless-stopped    env_file:      - .env    environment:      - HOME=/home/node      - NODE_ENV=production      - TERM=xterm-256color      - OPENCLAW_GATEWAY_BIND=${OPENCLAW_GATEWAY_BIND}      - OPENCLAW_GATEWAY_PORT=${OPENCLAW_GATEWAY_PORT}      - OPENCLAW_GATEWAY_TOKEN=${OPENCLAW_GATEWAY_TOKEN}      - GOG_KEYRING_PASSWORD=${GOG_KEYRING_PASSWORD}      - XDG_CONFIG_HOME=${XDG_CONFIG_HOME}      - PATH=/home/linuxbrew/.linuxbrew/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin    volumes:      - ${OPENCLAW_CONFIG_DIR}:/home/node/.openclaw      - ${OPENCLAW_WORKSPACE_DIR}:/home/node/.openclaw/workspace    ports:      # Recommended: keep the Gateway loopback-only on the VM; access via SSH tunnel.      # To expose it publicly, remove the `127.0.0.1:` prefix and firewall accordingly.      - "127.0.0.1:${OPENCLAW_GATEWAY_PORT}:18789"    command:      [        "node",        "dist/index.js",        "gateway",        "--bind",        "${OPENCLAW_GATEWAY_BIND}",        "--port",        "${OPENCLAW_GATEWAY_PORT}",        "--allow-unconfigured",      ]
[/code]

`--allow-unconfigured` is alleen bedoeld voor gemakkelijk bootstrappen; het is geen vervanging voor een juiste Gateway-configuratie. Stel nog steeds auth in (`gateway.auth.token` of wachtwoord) en gebruik veilige bindinstellingen voor je deployment.

* ### Gedeelde Docker-VM-runtimestappen

Gebruik de gedeelde runtimegids voor de algemene Docker-hostflow:

  * [Vereiste binaries in de image bakken](</nl/install/docker-vm-runtime#bake-required-binaries-into-the-image>)
  * [Bouwen en starten](</nl/install/docker-vm-runtime#build-and-launch>)
  * [Wat waar persistent blijft](</nl/install/docker-vm-runtime#what-persists-where>)
  * [Updates](</nl/install/docker-vm-runtime#updates>)


* ### GCP-specifieke startnotities

Als de build op GCP tijdens `pnpm install --frozen-lockfile` mislukt met `Killed` of `exit code 137`, heeft de VM onvoldoende geheugen. Gebruik minimaal `e2-small`, of `e2-medium` voor betrouwbaardere eerste builds.

Configureer bij binden aan LAN (`OPENCLAW_GATEWAY_BIND=lan`) een vertrouwde browser-origin voordat je doorgaat:

bashCopy code
[code]
    docker compose run --rm openclaw-cli config set gateway.controlUi.allowedOrigins '["http://127.0.0.1:18789"]' --strict-json
[/code]

Als je de Gateway-poort hebt gewijzigd, vervang dan `18789` door je geconfigureerde poort.

* ### Toegang vanaf je laptop

Maak een SSH-tunnel om de Gateway-poort door te sturen:

bashCopy code
[code]
    gcloud compute ssh openclaw-gateway --zone=us-central1-a -- -L 18789:127.0.0.1:18789
[/code]

Open in je browser:

`http://127.0.0.1:18789/`

Druk opnieuw een schone dashboardlink af:

bashCopy code
[code]
    docker compose run --rm openclaw-cli dashboard --no-open
[/code]

Als de UI om shared-secret-authenticatie vraagt, plak dan het geconfigureerde token of wachtwoord in de Control UI-instellingen. Deze Docker-flow schrijft standaard een token; als je de containerconfiguratie overschakelt naar wachtwoordauthenticatie, gebruik dan in plaats daarvan dat wachtwoord.

Als Control UI `unauthorized` of `disconnected (1008): pairing required` toont, keur dan het browserapparaat goed:

bashCopy code
[code]
    docker compose run --rm openclaw-cli devices listdocker compose run --rm openclaw-cli devices approve <requestId>
[/code]

Heb je de gedeelde referentie voor persistentie en updates opnieuw nodig? Zie [Docker VM Runtime](</nl/install/docker-vm-runtime#what-persists-where>) en [Docker VM Runtime-updates](</nl/install/docker-vm-runtime#updates>).

* * *

## Problemen oplossen

**SSH-verbinding geweigerd**

Verspreiding van SSH-sleutels kan na het maken van de VM 1-2 minuten duren. Wacht en probeer opnieuw.

**Problemen met OS Login**

Controleer je OS Login-profiel:

bashCopy code
[code]
    gcloud compute os-login describe-profile
[/code]

Zorg ervoor dat je account de vereiste IAM-machtigingen heeft (Compute OS Login of Compute OS Admin Login).

**Onvoldoende geheugen (OOM)**

Als de Docker-build mislukt met `Killed` en `exit code 137`, is de VM door OOM beeindigd. Upgrade naar e2-small (minimum) of e2-medium (aanbevolen voor betrouwbare lokale builds):

bashCopy code
[code]
    # Stop the VM firstgcloud compute instances stop openclaw-gateway --zone=us-central1-a # Change machine typegcloud compute instances set-machine-type openclaw-gateway \  --zone=us-central1-a \  --machine-type=e2-small # Start the VMgcloud compute instances start openclaw-gateway --zone=us-central1-a
[/code]

* * *

## Serviceaccounts (best practice voor beveiliging)

Voor persoonlijk gebruik werkt je standaardgebruikersaccount prima.

Maak voor automatisering of CI/CD-pijplijnen een speciaal serviceaccount met minimale machtigingen:

  1. Maak een serviceaccount:

bashCopy code
[code]gcloud iam service-accounts create openclaw-deploy \  --display-name="OpenClaw Deployment"
[/code]

  2. Ken de rol Compute Instance Admin toe (of een beperktere aangepaste rol):

bashCopy code
[code]gcloud projects add-iam-policy-binding my-openclaw-project \  --member="serviceAccount:openclaw-deploy@my-openclaw-project.iam.gserviceaccount.com" \  --role="roles/compute.instanceAdmin.v1"
[/code]


Vermijd het gebruik van de Owner-rol voor automatisering. Gebruik het principe van minimale rechten.

Zie <https://cloud.google.com/iam/docs/understanding-roles> voor details over IAM-rollen.

* * *

## Volgende stappen

  * Stel berichtenkanalen in: [Kanalen](</nl/channels>)
  * Koppel lokale apparaten als nodes: [Nodes](</nl/nodes>)
  * Configureer de Gateway: [Gateway-configuratie](</nl/gateway/configuration>)


## Gerelateerd

  * [Installatieoverzicht](</nl/install>)
  * [Azure](</nl/install/azure>)
  * [VPS-hosting](</nl/vps>)


Was this useful?YesNo