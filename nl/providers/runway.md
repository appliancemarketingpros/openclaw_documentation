---
title: Startbaan
source_url: https://docs.openclaw.ai/nl/providers/runway
scraped_at: 2026-05-25
---

OpenClaw levert een gebundelde `runway`-provider voor gehoste videogeneratie. De Plugin is standaard ingeschakeld en registreert de `runway`-provider voor het `videoGenerationProviders`-contract.

Eigenschap | Waarde  
---|---  
Provider-ID | `runway`  
Plugin | gebundeld, `enabledByDefault: true`  
Auth-env-vars | `RUNWAYML_API_SECRET` (canoniek) of `RUNWAY_API_KEY`  
Onboarding-vlag | `--auth-choice runway-api-key`  
Directe CLI-vlag | `--runway-api-key <key>`  
API | Taakgebaseerde videogeneratie van Runway (`GET /v1/tasks/{id}` polling)  
Standaardmodel | `runway/gen4.5`  
  
## Aan de slag

* ### Stel de API-sleutel in

bashCopy code
[code]
    openclaw onboard --auth-choice runway-api-key
[/code]

* ### Stel Runway in als de standaard videoprovider

bashCopy code
[code]
    openclaw config set agents.defaults.videoGenerationModel.primary "runway/gen4.5"
[/code]

* ### Genereer een video

Vraag de agent om een video te genereren. Runway wordt automatisch gebruikt.

## Ondersteunde modi en modellen

De provider biedt zeven Runway-modellen verdeeld over drie modi. Dezelfde model-ID kan meer dan één modus bedienen (bijvoorbeeld `gen4.5` werkt voor zowel tekst-naar-video als afbeelding-naar-video).

Modus | Modellen | Referentie-invoer  
---|---|---  
Tekst-naar-video | `gen4.5` (standaard), `veo3.1`, `veo3.1_fast`, `veo3` | Geen  
Afbeelding-naar-video | `gen4.5`, `gen4_turbo`, `gen3a_turbo`, `veo3.1`, `veo3.1_fast`, `veo3` | 1 lokale of externe afbeelding  
Video-naar-video | `gen4_aleph` | 1 lokale of externe video  
  
Lokale afbeeldings- en videoreferenties worden ondersteund via data-URI's.

Beeldverhoudingen | Toegestane waarden  
---|---  
Tekst-naar-video | `16:9`, `9:16`  
Afbeeldings- en videobewerkingen | `1:1`, `16:9`, `9:16`, `3:4`, `4:3`, `21:9`  
  
## Configuratie

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "runway/gen4.5",      },    },  },}
[/code]

## Geavanceerde configuratie

Aliassen voor omgevingsvariabelen

OpenClaw herkent zowel `RUNWAYML_API_SECRET` (canoniek) als `RUNWAY_API_KEY`. Beide variabelen authenticeren de Runway-provider.

Task polling

Runway gebruikt een taakgebaseerde API. Na het indienen van een generatieaanvraag pollt OpenClaw `GET /v1/tasks/{id}` totdat de video klaar is. Er is geen aanvullende configuratie nodig voor het polling-gedrag.

## Gerelateerd

[**Videogeneratie** Gedeelde toolparameters, providerselectie en asynchroon gedrag. ](</nl/tools/video-generation>) [**Configuratiereferentie** Standaardinstellingen voor agents, inclusief videogeneratiemodel. ](</nl/gateway/config-agents#agent-defaults>)

Was this useful?YesNo