---
title: macOS-ontwikkelomgeving instellen
source_url: https://docs.openclaw.ai/nl/platforms/mac/dev-setup
scraped_at: 2026-05-25
---

# macOS-ontwikkelaarsinstallatie

Bouw de OpenClaw macOS-applicatie vanuit de broncode en voer deze uit.

## Vereisten

Zorg dat je het volgende hebt geïnstalleerd voordat je de app bouwt:

  1. **Xcode 26.2+** : Vereist voor Swift-ontwikkeling.
  2. **Node.js 24 & pnpm**: Aanbevolen voor de Gateway, CLI en verpakkingsscripts. Node 22 LTS, momenteel `22.16+`, blijft ondersteund voor compatibiliteit.


## 1\. Afhankelijkheden installeren

Installeer de projectbrede afhankelijkheden:

bashCopy code
[code]
    pnpm install
[/code]

## 2\. De app bouwen en verpakken

Voer het volgende uit om de macOS-app te bouwen en te verpakken in `dist/OpenClaw.app`:

bashCopy code
[code]
    ./scripts/package-mac-app.sh
[/code]

Als je geen Apple Developer ID-certificaat hebt, gebruikt het script automatisch **ad-hoc-ondertekening** (`-`).

Zie de README van de macOS-app voor ontwikkelmodi, ondertekeningsvlaggen en probleemoplossing voor Team ID: <https://github.com/openclaw/openclaw/blob/main/apps/macos/README.md>

> **Opmerking** : Ad-hoc ondertekende apps kunnen beveiligingsmeldingen veroorzaken. Als de app onmiddellijk crasht met "Abort trap 6", zie dan de sectie Probleemoplossing.

## 3\. De CLI installeren

De macOS-app verwacht een globale installatie van de `openclaw` CLI om achtergrondtaken te beheren.

**Zo installeer je deze (aanbevolen):**

  1. Open de OpenClaw-app.
  2. Ga naar het instellingentabblad **Algemeen**.
  3. Klik op **"CLI installeren"**.


Je kunt de CLI ook handmatig installeren:

bashCopy code
[code]
    npm install -g openclaw@<version>
[/code]

`pnpm add -g openclaw@<version>` en `bun add -g openclaw@<version>` werken ook. Voor de Gateway-runtime blijft Node de aanbevolen route.

## Probleemoplossing

### Build mislukt: toolchain- of SDK-mismatch

De build van de macOS-app verwacht de nieuwste macOS SDK en de Swift 6.2-toolchain.

**Systeemafhankelijkheden (vereist):**

  * **Nieuwste macOS-versie die beschikbaar is in Software-update** (vereist door Xcode 26.2-SDK's)
  * **Xcode 26.2** (Swift 6.2-toolchain)


**Controles:**

bashCopy code
[code]
    xcodebuild -versionxcrun swift --version
[/code]

Als de versies niet overeenkomen, werk macOS/Xcode bij en voer de build opnieuw uit.

### App crasht bij toekennen van toestemming

Als de app crasht wanneer je **Spraakherkenning** of **Microfoon** -toegang probeert toe te staan, kan dit komen door een beschadigde TCC-cache of niet-overeenkomende ondertekening.

**Oplossing:**

  1. Stel de TCC-machtigingen opnieuw in:

bashCopy code
[code]tccutil reset All ai.openclaw.mac.debug
[/code]

  2. Als dat mislukt, wijzig dan tijdelijk de `BUNDLE_ID` in [`scripts/package-mac-app.sh`](<https://github.com/openclaw/openclaw/blob/main/scripts/package-mac-app.sh>) om macOS een "schone lei" af te dwingen.


### Gateway blijft eindeloos op "Starting..." staan

Als de Gateway-status op "Starting..." blijft staan, controleer dan of een zombieproces de poort bezet houdt:

bashCopy code
[code]
    openclaw gateway statusopenclaw gateway stop # If you're not using a LaunchAgent (dev mode / manual runs), find the listener:lsof -nP -iTCP:18789 -sTCP:LISTEN
[/code]

Als een handmatige run de poort bezet houdt, stop dat proces dan (Ctrl+C). Als laatste redmiddel kun je de PID beëindigen die je hierboven hebt gevonden.

## Gerelateerd

  * [macOS-app](</nl/platforms/macos>)
  * [Installatieoverzicht](</nl/install>)


Was this useful?YesNo