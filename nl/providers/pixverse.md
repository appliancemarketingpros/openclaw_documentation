---
title: PixVerse
source_url: https://docs.openclaw.ai/nl/providers/pixverse
scraped_at: 2026-06-29
---

ModelsProviders

OpenClaw biedt `pixverse` als officiële externe plugin voor gehoste PixVerse-videogeneratie. De plugin registreert de `pixverse`-provider tegen het `videoGenerationProviders`-contract.

Eigenschap | Waarde  
---|---  
Provider-id | `pixverse`  
Pluginpakket | `@openclaw/pixverse-provider`  
Auth-omgevingsvariabele | `PIXVERSE_API_KEY`  
Onboarding-vlag | `--auth-choice pixverse-api-key`  
Directe CLI-vlag | `--pixverse-api-key <key>`  
API | PixVerse Platform API v2 (`video_id`-indiening plus resultaatpolling)  
Standaardmodel | `pixverse/v6`  
Standaard-API-regio | Internationaal  
  
## Aan de slag

* ### De plugin installeren

bashCopy code
[code]
    openclaw plugins install clawhub:@openclaw/pixverse-provideropenclaw gateway restart
[/code]

* ### De API-sleutel instellen

bashCopy code
[code]
    openclaw onboard --auth-choice pixverse-api-key
[/code]

De wizard vraagt of het internationale endpoint (`https://app-api.pixverse.ai/openapi/v2`) of het CN-endpoint (`https://app-api.pixverseai.cn/openapi/v2`) moet worden gebruikt voordat `region` en `baseUrl` naar de providerconfiguratie worden geschreven.

* ### PixVerse instellen als standaard videoprovider

bashCopy code
[code]
    openclaw config set agents.defaults.videoGenerationModel.primary "pixverse/v6"
[/code]

* ### Een video genereren

Vraag de agent om een video te genereren. PixVerse wordt automatisch gebruikt.

## Ondersteunde modi en modellen

De provider stelt PixVerse-generatiemodellen beschikbaar via de gedeelde videotool van OpenClaw.

Modus | Modellen | Referentie-invoer  
---|---|---  
Tekst-naar-video | `v6` (standaard), `c1` | Geen  
Afbeelding-naar-video | `v6` (standaard), `c1` | 1 lokale of externe afbeelding  
  
Lokale afbeeldingsreferenties worden naar PixVerse geüpload voordat het afbeelding-naar-videoverzoek wordt gedaan. Externe afbeeldings-URL's worden via het PixVerse-endpoint voor afbeeldingsuploads doorgegeven als `image_url`.

Optie | Ondersteunde waarden  
---|---  
Duur | 1-15 seconden  
Resolutie | `360P`, `540P`, `720P`, `1080P`  
Beeldverhouding | `16:9`, `4:3`, `1:1`, `3:4`, `9:16`, `2:3`, `3:2`, `21:9` voor tekst-naar-video  
Gegenereerde audio | `audio: true`  
  
## Provideropties

De videoprovider accepteert deze optionele providerspecifieke sleutels:

Optie | Type | Effect  
---|---|---  
`seed` | number | Deterministische seed wanneer ondersteund  
`negativePrompt` / `negative_prompt` | string | Negatieve prompt  
`quality` | string | PixVerse-kwaliteit zoals `720p`  
`motionMode` / `motion_mode` | string | Bewegingsmodus voor afbeelding-naar-video  
`cameraMovement` / `camera_movement` | string | PixVerse-preset voor camerabeweging  
`templateId` / `template_id` | number | Geactiveerde PixVerse-template-id  
  
## Configuratie

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "pixverse/v6",      },    },  },}
[/code]

## Geavanceerde configuratie

API-regio

OpenClaw gebruikt standaard de internationale PixVerse-API. Stel `models.providers.pixverse.region` handmatig in wanneer je sleutel bij een specifieke PixVerse-platformregio hoort, of gebruik `openclaw onboard --auth-choice pixverse-api-key` om er een te kiezen in de installatiewizard:

Regiowaarde | Basis-URL van PixVerse-API  
---|---  
`international` | `https://app-api.pixverse.ai/openapi/v2`  
`cn` | `https://app-api.pixverseai.cn/openapi/v2`  
  
json5Copy code
[code]
    {  models: {    providers: {      pixverse: {        region: "cn", // "international" or "cn"        baseUrl: "https://app-api.pixverseai.cn/openapi/v2",        models: [],      },    },  },}
[/code]

Aangepaste basis-URL

Stel `models.providers.pixverse.baseUrl` alleen in wanneer je routeert via een vertrouwde compatibele proxy. `baseUrl` heeft voorrang op `region`.

json5Copy code
[code]
    {  models: {    providers: {      pixverse: {        baseUrl: "https://app-api.pixverse.ai/openapi/v2",      },    },  },}
[/code]

Taakpolling

PixVerse retourneert een `video_id` vanuit het generatieverzoek. OpenClaw pollt `/openapi/v2/video/result/{video_id}` totdat de taak slaagt, mislukt, of een time-out bereikt.

## Gerelateerd

[**Videogeneratie** Gedeelde toolparameters, providerselectie en asynchroon gedrag. ](</nl/tools/video-generation>) [**Configuratiereferentie** Standaardinstellingen voor agents, inclusief videogeneratiemodel. ](</nl/gateway/config-agents#agent-defaults>)

Was this useful?YesNo

Open issue