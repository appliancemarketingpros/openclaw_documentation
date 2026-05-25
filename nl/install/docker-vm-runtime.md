---
title: Docker-VM-uitvoeringsomgeving
source_url: https://docs.openclaw.ai/nl/install/docker-vm-runtime
scraped_at: 2026-05-25
---

Gedeelde runtime-stappen voor VM-gebaseerde Docker-installaties zoals GCP, Hetzner en vergelijkbare VPS-providers.

## Neem vereiste binaire bestanden op in de image

Binaire bestanden installeren in een draaiende container is een valkuil. Alles wat tijdens runtime wordt geïnstalleerd, gaat verloren bij een herstart.

Alle externe binaire bestanden die door Skills worden vereist, moeten tijdens het bouwen van de image worden geïnstalleerd.

De onderstaande voorbeelden tonen slechts drie veelgebruikte binaire bestanden:

  * `gog` (van `gogcli`) voor Gmail-toegang
  * `goplaces` voor Google Places
  * `wacli` voor WhatsApp


Dit zijn voorbeelden, geen volledige lijst. Je kunt zoveel binaire bestanden installeren als nodig is met hetzelfde patroon.

Als je later nieuwe Skills toevoegt die afhankelijk zijn van aanvullende binaire bestanden, moet je:

  1. Het Dockerfile bijwerken
  2. De image opnieuw bouwen
  3. De containers herstarten


**Voorbeeld-Dockerfile**

dockerfileCopy code
[code]
    FROM node:24-bookworm RUN apt-get update && apt-get install -y socat && rm -rf /var/lib/apt/lists/* # Example binary 1: Gmail CLI (gogcli — installs as `gog`)# Copy the current Linux asset URL from https://github.com/steipete/gogcli/releasesRUN curl -L https://github.com/steipete/gogcli/releases/latest/download/gogcli_linux_amd64.tar.gz \  | tar -xzO gog > /usr/local/bin/gog; \  chmod +x /usr/local/bin/gog # Example binary 2: Google Places CLI# Copy the current Linux asset URL from https://github.com/steipete/goplaces/releasesRUN curl -L https://github.com/steipete/goplaces/releases/latest/download/goplaces_linux_amd64.tar.gz \  | tar -xzO goplaces > /usr/local/bin/goplaces; \  chmod +x /usr/local/bin/goplaces # Example binary 3: WhatsApp CLI# Copy the current Linux asset URL from https://github.com/steipete/wacli/releasesRUN curl -L https://github.com/steipete/wacli/releases/latest/download/wacli-linux-amd64.tar.gz \  | tar -xzO wacli > /usr/local/bin/wacli; \  chmod +x /usr/local/bin/wacli # Add more binaries below using the same pattern WORKDIR /appCOPY package.json pnpm-lock.yaml pnpm-workspace.yaml .npmrc ./COPY ui/package.json ./ui/package.jsonCOPY scripts ./scripts RUN corepack enableRUN pnpm install --frozen-lockfile COPY . .RUN pnpm buildRUN pnpm ui:installRUN pnpm ui:build ENV NODE_ENV=production CMD ["node","dist/index.js"]
[/code]

## Bouwen en starten

bashCopy code
[code]
    docker compose builddocker compose up -d openclaw-gateway
[/code]

Als de build mislukt met `Killed` of `exit code 137` tijdens `pnpm install --frozen-lockfile`, heeft de VM onvoldoende geheugen. Gebruik een grotere machineklasse voordat je het opnieuw probeert.

Controleer binaire bestanden:

bashCopy code
[code]
    docker compose exec openclaw-gateway which gogdocker compose exec openclaw-gateway which goplacesdocker compose exec openclaw-gateway which wacli
[/code]

Verwachte uitvoer:

CodeCopy code
[code]
    /usr/local/bin/gog/usr/local/bin/goplaces/usr/local/bin/wacli
[/code]

Controleer Gateway:

bashCopy code
[code]
    docker compose logs -f openclaw-gateway
[/code]

Verwachte uitvoer:

CodeCopy code
[code]
    [gateway] listening on ws://0.0.0.0:18789
[/code]

## Wat waar blijft bestaan

OpenClaw draait in Docker, maar Docker is niet de bron van waarheid. Alle duurzame state moet herstarts, rebuilds en reboots overleven.

Component | Locatie | Persistentiemethode | Opmerkingen  
---|---|---|---  
Gateway-config | `/home/node/.openclaw/` | Host-volumemount | Bevat `openclaw.json`, `.env`  
Modelauth-profielen | `/home/node/.openclaw/agents/` | Host-volumemount | `agents/<agentId>/agent/auth-profiles.json` (OAuth, API keys)  
Auth-profielsleutel | `/home/node/.config/openclaw/` | Host-volumemount | Lokale encryptiesleutel voor tokenmateriaal van OAuth-auth-profielen  
Skill-configuraties | `/home/node/.openclaw/skills/` | Host-volumemount | State op Skill-niveau  
Agentwerkruimte | `/home/node/.openclaw/workspace/` | Host-volumemount | Code en agentartefacten  
WhatsApp-sessie | `/home/node/.openclaw/` | Host-volumemount | Behoudt QR-login  
Gmail-keyring | `/home/node/.openclaw/` | Host-volume + wachtwoord | Vereist `GOG_KEYRING_PASSWORD`  
Plugin-pakketten | `/home/node/.openclaw/npm`, `/home/node/.openclaw/git` | Host-volumemount | Roots van downloadbare Plugin-pakketten  
Externe binaire bestanden | `/usr/local/bin/` | Docker-image | Moeten tijdens het bouwen worden ingebakken  
Node-runtime | Containerbestandssysteem | Docker-image | Wordt bij elke image-build opnieuw gebouwd  
OS-pakketten | Containerbestandssysteem | Docker-image | Niet tijdens runtime installeren  
Docker-container | Vluchtig | Herstartbaar | Veilig om te vernietigen  
  
## Updates

Om OpenClaw op de VM bij te werken:

bashCopy code
[code]
    git pulldocker compose builddocker compose up -d
[/code]

## Gerelateerd

  * [Docker](</nl/install/docker>)
  * [Podman](</nl/install/podman>)
  * [ClawDock](</nl/install/clawdock>)


Was this useful?YesNo