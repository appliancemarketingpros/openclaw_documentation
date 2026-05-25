---
title: Vuurwerk
source_url: https://docs.openclaw.ai/nl/providers/fireworks
scraped_at: 2026-05-25
---

[Fireworks](<https://fireworks.ai>) biedt open-weight en gerouteerde modellen via een OpenAI-compatibele API. OpenClaw bevat een gebundelde Fireworks-provider-Plugin met twee vooraf gecatalogiseerde Kimi-modellen en accepteert elke Fireworks-model- of router-id tijdens runtime.

Eigenschap | Waarde  
---|---  
Provider-id | `fireworks` (alias: `fireworks-ai`)  
Plugin | gebundeld, `enabledByDefault: true`  
Auth-env-var | `FIREWORKS_API_KEY`  
Onboarding-vlag | `--auth-choice fireworks-api-key`  
Directe CLI-vlag | `--fireworks-api-key <key>`  
API | OpenAI-compatibel (`openai-completions`)  
Basis-URL | `https://api.fireworks.ai/inference/v1`  
Standaardmodel | `fireworks/accounts/fireworks/routers/kimi-k2p5-turbo`  
Standaardalias | `Kimi K2.5 Turbo`  
  
## Aan de slag

* ### Set the Fireworks API key

OnboardingCopy code
[code]
    openclaw onboard --auth-choice fireworks-api-key
[/code]

Direct flagCopy code
[code]
    openclaw onboard --non-interactive \--auth-choice fireworks-api-key \--fireworks-api-key "$FIREWORKS_API_KEY"
[/code]

Env onlyCopy code
[code]
    export FIREWORKS_API_KEY=fw-...
[/code]

Onboarding slaat de sleutel op voor de `fireworks`-provider in je auth-profielen en stelt de **Fire Pass** Kimi K2.5 Turbo-router in als standaardmodel.

* ### Verify the model is available

bashCopy code
[code]
    openclaw models list --provider fireworks
[/code]

De lijst moet `Kimi K2.6` en `Kimi K2.5 Turbo (Fire Pass)` bevatten. Als `FIREWORKS_API_KEY` niet kan worden opgelost, rapporteert `openclaw models status --json` de ontbrekende referentie onder `auth.unusableProfiles`.

## Niet-interactieve installatie

Geef voor gescripte of CI-installaties alles mee op de opdrachtregel:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice fireworks-api-key \  --fireworks-api-key "$FIREWORKS_API_KEY" \  --skip-health \  --accept-risk
[/code]

## Ingebouwde catalogus

Modelref | Naam | Invoer | Context | Max. uitvoer | Thinking  
---|---|---|---|---|---  
`fireworks/accounts/fireworks/models/kimi-k2p6` | Kimi K2.6 | tekst + beeld | 262,144 | 262,144 | Geforceerd uit  
`fireworks/accounts/fireworks/routers/kimi-k2p5-turbo` | Kimi K2.5 Turbo (Fire Pass) | tekst + beeld | 256,000 | 256,000 | Geforceerd uit (standaard)  
  
## Aangepaste Fireworks-model-id's

OpenClaw accepteert elke Fireworks-model- of router-id tijdens runtime. Gebruik de exacte id die Fireworks toont en voeg het voorvoegsel `fireworks/` toe. Dynamische resolutie kloont de Fire Pass-template (tekst- en beeldinvoer, OpenAI-compatibele API, standaardkosten nul) en schakelt thinking automatisch uit wanneer de id overeenkomt met het Kimi-patroon.

json5Copy code
[code]
    {  agents: {    defaults: {      model: {        primary: "fireworks/accounts/fireworks/models/<your-model-id>",      },    },  },}
[/code]

How model id prefixing works

Elke Fireworks-modelref in OpenClaw begint met `fireworks/`, gevolgd door de exacte id of het routerpad van het Fireworks-platform. Bijvoorbeeld:

  * Routermodel: `fireworks/accounts/fireworks/routers/kimi-k2p5-turbo`
  * Direct model: `fireworks/accounts/fireworks/models/<model-name>`


OpenClaw verwijdert het voorvoegsel `fireworks/` bij het samenstellen van de API-aanvraag en stuurt het resterende pad naar het Fireworks-eindpunt als het OpenAI-compatibele `model`-veld.

Why thinking is forced off for Kimi

Fireworks K2.6 retourneert een 400 als de aanvraag `reasoning_*`-parameters bevat, ook al ondersteunt Kimi thinking via Moonshots eigen API. Het gebundelde beleid (`extensions/fireworks/thinking-policy.ts`) adverteert alleen het thinking-niveau `off` voor Kimi-model-id's, zodat handmatige `/think`-schakelaars en providerbeleidsoppervlakken afgestemd blijven op het runtimecontract.

Om Kimi-reasoning end-to-end te gebruiken, configureer je de [Moonshot-provider](</nl/providers/moonshot>) en routeer je hetzelfde model via die provider.

Environment availability for the daemon

Als de Gateway als beheerde service draait (launchd, systemd, Docker), moet de Fireworks-sleutel zichtbaar zijn voor dat proces, niet alleen voor je interactieve shell.

Op macOS koppelt `openclaw gateway install` `~/.openclaw/.env` al aan het LaunchAgent-omgevingsbestand. Voer install opnieuw uit (of `openclaw doctor --fix`) nadat je de sleutel hebt geroteerd.

## Gerelateerd

[**Model providers** Providers, modelrefs en failovergedrag kiezen. ](</nl/concepts/model-providers>) [**Thinking modes** `/think`-niveaus, providerbeleid en het routeren van modellen met reasoning-mogelijkheden. ](</nl/tools/thinking>) [**Moonshot** Voer Kimi uit met native thinking-uitvoer via Moonshots eigen API. ](</nl/providers/moonshot>) [**Troubleshooting** Algemene probleemoplossing en FAQ. ](</nl/help/troubleshooting>)

Was this useful?YesNo