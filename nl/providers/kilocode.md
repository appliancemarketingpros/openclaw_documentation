---
title: Kilo Gateway
source_url: https://docs.openclaw.ai/nl/providers/kilocode
scraped_at: 2026-05-25
---

Kilo Gateway biedt een **uniforme API** die verzoeken naar veel modellen achter één endpoint en API-sleutel routeert. Deze is OpenAI-compatibel, waardoor de meeste OpenAI-SDK's werken door de basis-URL te wijzigen.

Eigenschap | Waarde  
---|---  
Provider | `kilocode`  
Auth | `KILOCODE_API_KEY`  
API | OpenAI-compatibel  
Basis-URL | `https://api.kilo.ai/api/gateway/`  
  
## Aan de slag

* ### Maak een account aan

Ga naar [app.kilo.ai](<https://app.kilo.ai>), meld je aan of maak een account aan, navigeer daarna naar API Keys en genereer een nieuwe sleutel.

* ### Voer onboarding uit

bashCopy code
[code]
    openclaw onboard --auth-choice kilocode-api-key
[/code]

Of stel de omgevingsvariabele rechtstreeks in:

bashCopy code
[code]
    export KILOCODE_API_KEY="<your-kilocode-api-key>" # pragma: allowlist secret
[/code]

* ### Controleer of het model beschikbaar is

bashCopy code
[code]
    openclaw models list --provider kilocode
[/code]

## Standaardmodel

Het standaardmodel is `kilocode/kilo/auto`, een provider-eigen smart-routing model dat door Kilo Gateway wordt beheerd.

## Ingebouwde catalogus

OpenClaw ontdekt beschikbare modellen dynamisch vanuit de Kilo Gateway bij het opstarten. Gebruik `/models kilocode` om de volledige lijst met modellen te zien die beschikbaar zijn met je account.

Elk model dat beschikbaar is op de Gateway kan worden gebruikt met het prefix `kilocode/`:

Modelreferentie | Opmerkingen  
---|---  
`kilocode/kilo/auto` | Standaard — smart routing  
`kilocode/anthropic/claude-sonnet-4` | Anthropic via Kilo  
`kilocode/openai/gpt-5.5` | OpenAI via Kilo  
`kilocode/google/gemini-3.1-pro-preview` | Google via Kilo  
...en nog veel meer | Gebruik `/models kilocode` om alles te tonen  
  
## Configuratievoorbeeld

json5Copy code
[code]
    {  env: { KILOCODE_API_KEY: "<your-kilocode-api-key>" }, // pragma: allowlist secret  agents: {    defaults: {      model: { primary: "kilocode/kilo/auto" },    },  },}
[/code]

Transport en compatibiliteit

Kilo Gateway is in de bron gedocumenteerd als OpenRouter-compatibel, waardoor deze op het proxy-achtige OpenAI-compatibele pad blijft in plaats van native OpenAI-verzoeksvorming te gebruiken.

  * Gemini-backed Kilo-referenties blijven op het proxy-Gemini-pad, zodat OpenClaw daar Gemini thought-signature sanitation behoudt zonder native Gemini replay-validatie of bootstrap-herschrijvingen in te schakelen.
  * Kilo Gateway gebruikt onder de motorkap een Bearer-token met je API-sleutel.

Stream-wrapper en redenering

Kilo's gedeelde stream-wrapper voegt de app-header van de provider toe en normaliseert proxy-reasoning-payloads voor ondersteunde concrete modelreferenties.

Probleemoplossing

  * Als modeldetectie bij het opstarten mislukt, valt OpenClaw terug op de gebundelde statische catalogus met `kilocode/kilo/auto`.
  * Controleer of je API-sleutel geldig is en dat je Kilo-account de gewenste modellen heeft ingeschakeld.
  * Wanneer de Gateway als daemon draait, zorg er dan voor dat `KILOCODE_API_KEY` beschikbaar is voor dat proces (bijvoorbeeld in `~/.openclaw/.env` of via `env.shellEnv`).


## Gerelateerd

[**Modelselectie** Providers, modelreferenties en failover-gedrag kiezen. ](</nl/concepts/model-providers>) [**Configuratiereferentie** Volledige OpenClaw-configuratiereferentie. ](</nl/gateway/configuration-reference>) [**Kilo Gateway** Dashboard, API-sleutels en accountbeheer van Kilo Gateway. ](<https://app.kilo.ai>)

Was this useful?YesNo