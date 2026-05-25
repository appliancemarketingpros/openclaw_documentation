---
title: Docker-VM-Laufzeit
source_url: https://docs.openclaw.ai/de/install/docker-vm-runtime
scraped_at: 2026-05-25
---

Gemeinsame Laufzeitschritte für VM-basierte Docker-Installationen wie GCP, Hetzner und ähnliche VPS-Provider.

## Erforderliche Binärdateien in das Image einbacken

Binärdateien in einem laufenden Container zu installieren, ist eine Falle. Alles, was zur Laufzeit installiert wird, geht bei einem Neustart verloren.

Alle externen Binärdateien, die von Skills benötigt werden, müssen zur Image-Build-Zeit installiert werden.

Die folgenden Beispiele zeigen nur drei gängige Binärdateien:

  * `gog` (aus `gogcli`) für Gmail-Zugriff
  * `goplaces` für Google Places
  * `wacli` für WhatsApp


Dies sind Beispiele, keine vollständige Liste. Sie können nach demselben Muster so viele Binärdateien installieren, wie nötig sind.

Wenn Sie später neue Skills hinzufügen, die von zusätzlichen Binärdateien abhängen, müssen Sie:

  1. Die Dockerfile aktualisieren
  2. Das Image neu bauen
  3. Die Container neu starten


**Beispiel-Dockerfile**

dockerfileCopy code
[code]
    FROM node:24-bookworm RUN apt-get update && apt-get install -y socat && rm -rf /var/lib/apt/lists/* # Example binary 1: Gmail CLI (gogcli — installs as `gog`)# Copy the current Linux asset URL from https://github.com/steipete/gogcli/releasesRUN curl -L https://github.com/steipete/gogcli/releases/latest/download/gogcli_linux_amd64.tar.gz \  | tar -xzO gog > /usr/local/bin/gog; \  chmod +x /usr/local/bin/gog # Example binary 2: Google Places CLI# Copy the current Linux asset URL from https://github.com/steipete/goplaces/releasesRUN curl -L https://github.com/steipete/goplaces/releases/latest/download/goplaces_linux_amd64.tar.gz \  | tar -xzO goplaces > /usr/local/bin/goplaces; \  chmod +x /usr/local/bin/goplaces # Example binary 3: WhatsApp CLI# Copy the current Linux asset URL from https://github.com/steipete/wacli/releasesRUN curl -L https://github.com/steipete/wacli/releases/latest/download/wacli-linux-amd64.tar.gz \  | tar -xzO wacli > /usr/local/bin/wacli; \  chmod +x /usr/local/bin/wacli # Add more binaries below using the same pattern WORKDIR /appCOPY package.json pnpm-lock.yaml pnpm-workspace.yaml .npmrc ./COPY ui/package.json ./ui/package.jsonCOPY scripts ./scripts RUN corepack enableRUN pnpm install --frozen-lockfile COPY . .RUN pnpm buildRUN pnpm ui:installRUN pnpm ui:build ENV NODE_ENV=production CMD ["node","dist/index.js"]
[/code]

## Bauen und starten

bashCopy code
[code]
    docker compose builddocker compose up -d openclaw-gateway
[/code]

Wenn der Build während `pnpm install --frozen-lockfile` mit `Killed` oder `exit code 137` fehlschlägt, hat die VM nicht genügend Arbeitsspeicher. Verwenden Sie eine größere Maschinenklasse, bevor Sie es erneut versuchen.

Binärdateien überprüfen:

bashCopy code
[code]
    docker compose exec openclaw-gateway which gogdocker compose exec openclaw-gateway which goplacesdocker compose exec openclaw-gateway which wacli
[/code]

Erwartete Ausgabe:

CodeCopy code
[code]
    /usr/local/bin/gog/usr/local/bin/goplaces/usr/local/bin/wacli
[/code]

Gateway überprüfen:

bashCopy code
[code]
    docker compose logs -f openclaw-gateway
[/code]

Erwartete Ausgabe:

CodeCopy code
[code]
    [gateway] listening on ws://0.0.0.0:18789
[/code]

## Was wo dauerhaft gespeichert wird

OpenClaw läuft in Docker, aber Docker ist nicht die Source of Truth. Alle langlebigen Zustände müssen Neustarts, Neubuilds und Reboots überstehen.

Komponente | Speicherort | Persistenzmechanismus | Hinweise  
---|---|---|---  
Gateway-Konfiguration | `/home/node/.openclaw/` | Host-Volume-Mount | Enthält `openclaw.json`, `.env`  
Modellauthentifizierungsprofile | `/home/node/.openclaw/agents/` | Host-Volume-Mount | `agents/<agentId>/agent/auth-profiles.json` (OAuth, API-Schlüssel)  
Schlüssel für Authentifizierungsprofile | `/home/node/.config/openclaw/` | Host-Volume-Mount | Lokaler Verschlüsselungsschlüssel für OAuth-Tokenmaterial von Authentifizierungsprofilen  
Skill-Konfigurationen | `/home/node/.openclaw/skills/` | Host-Volume-Mount | Zustand auf Skill-Ebene  
Agent-Arbeitsbereich | `/home/node/.openclaw/workspace/` | Host-Volume-Mount | Code- und Agent-Artefakte  
WhatsApp-Sitzung | `/home/node/.openclaw/` | Host-Volume-Mount | Bewahrt die QR-Anmeldung auf  
Gmail-Schlüsselbund | `/home/node/.openclaw/` | Host-Volume + Passwort | Erfordert `GOG_KEYRING_PASSWORD`  
Plugin-Pakete | `/home/node/.openclaw/npm`, `/home/node/.openclaw/git` | Host-Volume-Mount | Stammverzeichnisse für herunterladbare Plugin-Pakete  
Externe Binärdateien | `/usr/local/bin/` | Docker-Image | Müssen zur Build-Zeit eingebacken werden  
Node-Laufzeit | Container-Dateisystem | Docker-Image | Wird bei jedem Image-Build neu gebaut  
Betriebssystempakete | Container-Dateisystem | Docker-Image | Nicht zur Laufzeit installieren  
Docker-Container | Kurzlebig | Neustartbar | Kann sicher gelöscht werden  
  
## Updates

So aktualisieren Sie OpenClaw auf der VM:

bashCopy code
[code]
    git pulldocker compose builddocker compose up -d
[/code]

## Verwandte Themen

  * [Docker](</de/install/docker>)
  * [Podman](</de/install/podman>)
  * [ClawDock](</de/install/clawdock>)


Was this useful?YesNo