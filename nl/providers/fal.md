---
title: Fal
source_url: https://docs.openclaw.ai/nl/providers/fal
scraped_at: 2026-05-25
---

OpenClaw levert een gebundelde `fal`-provider voor gehoste beeld- en videogeneratie.

Eigenschap | Waarde  
---|---  
Provider | `fal`  
Auth | `FAL_KEY` (canoniek; `FAL_API_KEY` werkt ook als fallback)  
API | fal-modeleindpunten  
  
## Aan de slag

* ### Stel de API-sleutel in

bashCopy code
[code]
    openclaw onboard --auth-choice fal-api-key
[/code]

* ### Stel een standaardbeeldmodel in

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "fal/fal-ai/flux/dev",      },    },  },}
[/code]

## Beeldgeneratie

De gebundelde `fal`-provider voor beeldgeneratie gebruikt standaard `fal/fal-ai/flux/dev`.

Mogelijkheid | Waarde  
---|---  
Max. afbeeldingen | 4 per aanvraag  
Bewerkingsmodus | Flux: 1 referentieafbeelding; GPT Image 2: 10; Nano Banana 2: 14  
Grootte-overschrijvingen | Ondersteund  
Beeldverhouding | Ondersteund voor genereren en GPT Image 2-/Nano Banana 2-bewerking  
Resolutie | Ondersteund  
Uitvoerformaat | `png` of `jpeg`  
  
Gebruik `outputFormat: "png"` wanneer je PNG-uitvoer wilt. fal declareert geen expliciete regeling voor transparante achtergronden in OpenClaw, dus `background: "transparent"` wordt gerapporteerd als een genegeerde overschrijving voor fal-modellen.

Om fal als standaardbeeldprovider te gebruiken:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "fal/fal-ai/flux/dev",      },    },  },}
[/code]

## Videogeneratie

De gebundelde `fal`-provider voor videogeneratie gebruikt standaard `fal/fal-ai/minimax/video-01-live`.

Mogelijkheid | Waarde  
---|---  
Modi | Tekst-naar-video, enkele-afbeeldingsreferentie, Seedance-referentie-naar-video  
Runtime | Wachtrijgebaseerde submit/status/result-flow voor langlopende taken  
  
Beschikbare videomodellen

**HeyGen video-agent:**

  * `fal/fal-ai/heygen/v2/video-agent`


**Seedance 2.0:**

  * `fal/bytedance/seedance-2.0/fast/text-to-video`
  * `fal/bytedance/seedance-2.0/fast/image-to-video`
  * `fal/bytedance/seedance-2.0/fast/reference-to-video`
  * `fal/bytedance/seedance-2.0/text-to-video`
  * `fal/bytedance/seedance-2.0/image-to-video`
  * `fal/bytedance/seedance-2.0/reference-to-video`

Configuratievoorbeeld voor Seedance 2.0 json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "fal/bytedance/seedance-2.0/fast/text-to-video",      },    },  },}
[/code]

Configuratievoorbeeld voor Seedance 2.0 reference-to-video json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "fal/bytedance/seedance-2.0/fast/reference-to-video",      },    },  },}
[/code]

Reference-to-video accepteert maximaal 9 afbeeldingen, 3 video's en 3 audioreferenties via de gedeelde `video_generate`-parameters `images`, `videos` en `audioRefs`, met maximaal 12 referentiebestanden in totaal.

Configuratievoorbeeld voor HeyGen video-agent json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "fal/fal-ai/heygen/v2/video-agent",      },    },  },}
[/code]

## Gerelateerd

[**Beeldgeneratie** Gedeelde parameters voor beeldtools en providerselectie. ](</nl/tools/image-generation>) [**Videogeneratie** Gedeelde parameters voor videotools en providerselectie. ](</nl/tools/video-generation>) [**Configuratiereferentie** Agentstandaarden, inclusief selectie van beeld- en videomodellen. ](</nl/gateway/config-agents#agent-defaults>)

Was this useful?YesNo