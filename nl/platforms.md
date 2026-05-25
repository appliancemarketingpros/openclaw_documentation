---
title: Platformen
source_url: https://docs.openclaw.ai/nl/platforms
scraped_at: 2026-05-25
---

OpenClaw core is geschreven in TypeScript. **Node is de aanbevolen runtime**. Bun wordt niet aanbevolen voor de Gateway — bekende problemen met WhatsApp- en Telegram-kanalen; zie [Bun (experimenteel)](</nl/install/bun>) voor details.

Er bestaan companion-apps voor macOS (menubalk-app) en mobiele nodes (iOS/Android). Windows- en Linux-companion-apps zijn gepland, maar de Gateway wordt vandaag volledig ondersteund. Native companion-apps voor Windows zijn ook gepland; de Gateway wordt aanbevolen via WSL2.

## Kies je besturingssysteem

  * macOS: [macOS](</nl/platforms/macos>)
  * iOS: [iOS](</nl/platforms/ios>)
  * Android: [Android](</nl/platforms/android>)
  * Windows: [Windows](</nl/platforms/windows>)
  * Linux: [Linux](</nl/platforms/linux>)


## VPS en hosting

  * VPS-hub: [VPS-hosting](</nl/vps>)
  * [Fly.io](<http://Fly.io>): [Fly.io](</nl/install/fly>)
  * Hetzner (Docker): [Hetzner](</nl/install/hetzner>)
  * GCP (Compute Engine): [GCP](</nl/install/gcp>)
  * Azure (Linux-VM): [Azure](</nl/install/azure>)
  * exe.dev (VM + HTTPS-proxy): [exe.dev](</nl/install/exe-dev>)


## Algemene links

  * Installatiehandleiding: [Aan de slag](</nl/start/getting-started>)
  * Gateway-runbook: [Gateway](</nl/gateway>)
  * Gateway-configuratie: [Configuratie](</nl/gateway/configuration>)
  * Servicestatus: `openclaw gateway status`


## Gateway-service installeren (CLI)

Gebruik een van deze opties (allemaal ondersteund):

  * Wizard (aanbevolen): `openclaw onboard --install-daemon`
  * Direct: `openclaw gateway install`
  * Configuratieflow: `openclaw configure` → selecteer **Gateway-service**
  * Repareren/migreren: `openclaw doctor` (biedt aan om de service te installeren of te herstellen)


Het servicedoel hangt af van het besturingssysteem:

  * macOS: LaunchAgent (`ai.openclaw.gateway` of `ai.openclaw.<profile>`; legacy `com.openclaw.*`)
  * Linux/WSL2: systemd-gebruikersservice (`openclaw-gateway[-<profile>].service`)
  * Native Windows: geplande taak (`OpenClaw Gateway` of `OpenClaw Gateway (<profile>)`), met een fallback voor een loginitem in de Startup-map per gebruiker als het maken van de taak wordt geweigerd


## Gerelateerd

  * [Installatieoverzicht](</nl/install>)
  * [macOS-app](</nl/platforms/macos>)
  * [iOS-app](</nl/platforms/ios>)


Was this useful?YesNo