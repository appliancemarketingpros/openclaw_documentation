---
title: Afbeeldingsgeneratie
source_url: https://docs.openclaw.ai/nl/tools/image-generation
scraped_at: 2026-05-25
---

Met de tool `image_generate` kan de agent afbeeldingen maken en bewerken met je geconfigureerde providers. Gegenereerde afbeeldingen worden automatisch geleverd als mediabijlagen in het antwoord van de agent.

## Snelstart

* ### Configure auth

Stel een API-sleutel in voor minstens één provider (bijvoorbeeld `OPENAI_API_KEY`, `GEMINI_API_KEY`, `OPENROUTER_API_KEY`) of meld je aan met OpenAI Codex OAuth.

* ### Pick a default model (optional)

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "openai/gpt-image-2",        timeoutMs: 180_000,      },    },  },}
[/code]

Codex OAuth gebruikt dezelfde modelreferentie `openai/gpt-image-2`. Wanneer een OAuth-profiel `openai-codex` is geconfigureerd, routeert OpenClaw afbeeldingsverzoeken via dat OAuth-profiel in plaats van eerst `OPENAI_API_KEY` te proberen. Expliciete configuratie van `models.providers.openai` (API-sleutel, aangepaste/Azure-basis-URL) schakelt terug naar de directe route via de OpenAI Images API.

* ### Ask the agent

_"Genereer een afbeelding van een vriendelijke robotmascotte."_

De agent roept `image_generate` automatisch aan. Er is geen allow-listing voor tools nodig: deze is standaard ingeschakeld wanneer een provider beschikbaar is.

## Veelgebruikte routes

Doel | Modelreferentie | Auth  
---|---|---  
OpenAI-afbeeldingsgeneratie met API-facturering | `openai/gpt-image-2` | `OPENAI_API_KEY`  
OpenAI-afbeeldingsgeneratie met Codex-abonnementsauth | `openai/gpt-image-2` | OpenAI Codex OAuth  
OpenAI PNG/WebP met transparante achtergrond | `openai/gpt-image-1.5` | `OPENAI_API_KEY` of OpenAI Codex OAuth  
DeepInfra-afbeeldingsgeneratie | `deepinfra/black-forest-labs/FLUX-1-schnell` | `DEEPINFRA_API_KEY`  
OpenRouter-afbeeldingsgeneratie | `openrouter/google/gemini-3.1-flash-image-preview` | `OPENROUTER_API_KEY`  
LiteLLM-afbeeldingsgeneratie | `litellm/gpt-image-2` | `LITELLM_API_KEY`  
Google Gemini-afbeeldingsgeneratie | `google/gemini-3.1-flash-image-preview` | `GEMINI_API_KEY` of `GOOGLE_API_KEY`  
  
Dezelfde tool `image_generate` verwerkt tekst-naar-afbeelding en bewerking met referentieafbeeldingen. Gebruik `image` voor één referentie of `images` voor meerdere referenties. Door de provider ondersteunde uitvoerhints zoals `quality`, `outputFormat` en `background` worden doorgestuurd wanneer beschikbaar en als genegeerd gerapporteerd wanneer een provider ze niet ondersteunt. Meegeleverde ondersteuning voor transparante achtergrond is OpenAI-specifiek; andere providers kunnen nog steeds PNG-alfa behouden als hun backend dit uitvoert.

## Ondersteunde providers

Provider | Standaardmodel | Bewerkingsondersteuning | Auth  
---|---|---|---  
ComfyUI | `workflow` | Ja (1 afbeelding, geconfigureerd via workflow) | `COMFY_API_KEY` of `COMFY_CLOUD_API_KEY` voor cloud  
DeepInfra | `black-forest-labs/FLUX-1-schnell` | Ja (1 afbeelding) | `DEEPINFRA_API_KEY`  
fal | `fal-ai/flux/dev` | Ja (modelspecifieke limieten) | `FAL_KEY`  
Google | `gemini-3.1-flash-image-preview` | Ja | `GEMINI_API_KEY` of `GOOGLE_API_KEY`  
LiteLLM | `gpt-image-2` | Ja (tot 5 invoerafbeeldingen) | `LITELLM_API_KEY`  
MiniMax | `image-01` | Ja (onderwerpreferentie) | `MINIMAX_API_KEY` of MiniMax OAuth (`minimax-portal`)  
OpenAI | `gpt-image-2` | Ja (tot 4 afbeeldingen) | `OPENAI_API_KEY` of OpenAI Codex OAuth  
OpenRouter | `google/gemini-3.1-flash-image-preview` | Ja (tot 5 invoerafbeeldingen) | `OPENROUTER_API_KEY`  
Vydra | `grok-imagine` | Nee | `VYDRA_API_KEY`  
xAI | `grok-imagine-image` | Ja (tot 5 afbeeldingen) | `XAI_API_KEY`  
  
Gebruik `action: "list"` om beschikbare providers en modellen tijdens runtime te inspecteren:

textCopy code
[code]
    /tool image_generate action=list
[/code]

## Providermogelijkheden

Mogelijkheid | ComfyUI | DeepInfra | fal | Google | MiniMax | OpenAI | Vydra | xAI  
---|---|---|---|---|---|---|---|---  
Genereren (max. aantal) | Door workflow bepaald | 4 | 4 | 4 | 9 | 4 | 1 | 4  
Bewerken / referentie | 1 afbeelding (workflow) | 1 afbeelding | Flux: 1; GPT: 10; NB2: 14 | Tot 5 afbeeldingen | 1 afbeelding (onderwerpreferentie) | Tot 5 afbeeldingen | - | Tot 5 afbeeldingen  
Grootteregeling | - | ✓ | ✓ | ✓ | - | Tot 4K | - | -  
Beeldverhouding | - | - | ✓ | ✓ | ✓ | - | - | ✓  
Resolutie (1K/2K/4K) | - | - | ✓ | ✓ | - | - | - | 1K, 2K  
  
## Toolparameters

Prompt voor afbeeldingsgeneratie. Vereist voor `action: "generate"`.

Gebruik `"list"` om beschikbare providers en modellen tijdens runtime te inspecteren.

Provider-/modeloverride (bijv. `openai/gpt-image-2`). Gebruik `openai/gpt-image-1.5` voor transparante OpenAI-achtergronden.

Pad of URL van één referentieafbeelding voor bewerkingsmodus.

Meerdere referentieafbeeldingen voor bewerkingsmodus (tot 5 bij ondersteunende providers).

Groottehint: `1024x1024`, `1536x1024`, `1024x1536`, `2048x2048`, `3840x2160`.

Beeldverhouding: `1:1`, `2:3`, `3:2`, `3:4`, `4:3`, `4:5`, `5:4`, `9:16`, `16:9`, `21:9`.

Kwaliteitshint wanneer de provider dit ondersteunt.

Hint voor uitvoerindeling wanneer de provider dit ondersteunt.

Achtergrondhint wanneer de provider dit ondersteunt. Gebruik `transparent` met `outputFormat: "png"` of `"webp"` voor providers die transparantie ondersteunen.

Optionele time-out voor providerverzoeken in milliseconden. Wanneer Codex `image_generate` via dynamische tools aanroept, overschrijft deze waarde per aanroep nog steeds de geconfigureerde standaardwaarde en wordt deze begrensd op 600000 ms.

Alleen-OpenAI-hints: `background`, `moderation`, `outputCompression` en `user`.

## Configuratie

### Modelselectie

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "openai/gpt-image-2",        timeoutMs: 180_000,        fallbacks: [          "openrouter/google/gemini-3.1-flash-image-preview",          "google/gemini-3.1-flash-image-preview",          "fal/fal-ai/flux/dev",        ],      },    },  },}
[/code]

### Volgorde van providerselectie

OpenClaw probeert providers in deze volgorde:

  1. **Parameter`model`** uit de toolaanroep (als de agent er een opgeeft).
  2. **`imageGenerationModel.primary`** uit de configuratie.
  3. **`imageGenerationModel.fallbacks`** op volgorde.
  4. **Autodetectie** : alleen standaardproviders met auth: 
     * huidige standaardprovider eerst;
     * resterende geregistreerde providers voor afbeeldingsgeneratie op volgorde van provider-id.


Als een provider faalt (auth-fout, rate limit, enz.), wordt automatisch de volgende geconfigureerde kandidaat geprobeerd. Als alles faalt, bevat de fout details van elke poging.

Per-call model overrides are exact

Een `model`-override per aanroep probeert alleen die provider/dat model en gaat niet door naar geconfigureerde primaire/fallback-providers of automatisch gedetecteerde providers.

Auto-detection is auth-aware

Een providerstandaard komt alleen in de kandidatenlijst wanneer OpenClaw die provider daadwerkelijk kan authenticeren. Stel `agents.defaults.mediaGenerationAutoProviderFallback: false` in om alleen expliciete items voor `model`, `primary` en `fallbacks` te gebruiken.

Timeouts

Stel `agents.defaults.imageGenerationModel.timeoutMs` in voor langzame afbeeldingsbackends. Een toolparameter `timeoutMs` per aanroep overschrijft de geconfigureerde standaardwaarde. Dynamische-toolaanroepen van Codex respecteren hetzelfde time-outbudget, begrensd door het maximum van 600000 ms van de dynamische-toolbridge van OpenClaw.

Inspect at runtime

Gebruik `action: "list"` om de momenteel geregistreerde providers, hun standaardmodellen en hints voor auth-omgevingsvariabelen te inspecteren.

### Afbeeldingen bewerken

OpenAI, OpenRouter, Google, DeepInfra, fal, MiniMax, ComfyUI en xAI ondersteunen het bewerken van referentieafbeeldingen. Geef een pad of URL van een referentieafbeelding door:

textCopy code
[code]
    "Genereer een aquarelversie van deze foto" + image: "/path/to/photo.jpg"
[/code]

OpenAI, OpenRouter, Google en xAI ondersteunen maximaal 5 referentieafbeeldingen via de parameter `images`. fal ondersteunt 1 referentieafbeelding voor Flux image-to-image, tot 10 voor GPT Image 2-bewerkingen en tot 14 voor Nano Banana 2-bewerkingen. MiniMax en ComfyUI ondersteunen er 1.

## Diepgaande provideruitleg

OpenAI gpt-image-2 (and gpt-image-1.5)

OpenAI-afbeeldingsgeneratie gebruikt standaard `openai/gpt-image-2`. Als een OAuth-profiel voor `openai-codex` is geconfigureerd, hergebruikt OpenClaw hetzelfde OAuth-profiel dat door Codex-abonnementchatmodellen wordt gebruikt en stuurt het de afbeeldingsaanvraag via de Codex Responses-backend. Verouderde Codex-basis-URL's zoals `https://chatgpt.com/backend-api` worden voor afbeeldingsaanvragen gecanonicaliseerd naar `https://chatgpt.com/backend-api/codex`. OpenClaw valt voor die aanvraag **niet** stilzwijgend terug op `OPENAI_API_KEY` \- om directe routering via de OpenAI Images API af te dwingen, configureer je `models.providers.openai` expliciet met een API-sleutel, aangepaste basis-URL of Azure-eindpunt.

De modellen `openai/gpt-image-1.5`, `openai/gpt-image-1` en `openai/gpt-image-1-mini` kunnen nog steeds expliciet worden geselecteerd. Gebruik `gpt-image-1.5` voor PNG/WebP-uitvoer met transparante achtergrond; de huidige `gpt-image-2`-API weigert `background: "transparent"`.

`gpt-image-2` ondersteunt zowel tekst-naar-afbeeldinggeneratie als bewerking met referentieafbeeldingen via dezelfde tool `image_generate`. OpenClaw stuurt `prompt`, `count`, `size`, `quality`, `outputFormat` en referentieafbeeldingen door naar OpenAI. OpenAI ontvangt `aspectRatio` of `resolution` **niet** rechtstreeks; waar mogelijk zet OpenClaw die om naar een ondersteunde `size`, anders meldt de tool ze als genegeerde overrides.

OpenAI-specifieke opties staan onder het object `openai`:

jsonCopy code
[code]
    {  "quality": "low",  "outputFormat": "jpeg",  "openai": {    "background": "opaque",    "moderation": "low",    "outputCompression": 60,    "user": "end-user-42"  }}
[/code]

`openai.background` accepteert `transparent`, `opaque` of `auto`; transparante uitvoer vereist `outputFormat` `png` of `webp` en een OpenAI-afbeeldingsmodel dat transparantie ondersteunt. OpenClaw routeert standaard aanvragen met `gpt-image-2` voor transparante achtergronden naar `gpt-image-1.5`. `openai.outputCompression` is van toepassing op JPEG/WebP-uitvoer.

De toplevel hint `background` is providerneutraal en wordt momenteel gekoppeld aan hetzelfde OpenAI-aanvraagveld `background` wanneer de OpenAI-provider is geselecteerd. Providers die geen achtergrondondersteuning declareren, retourneren deze in `ignoredOverrides` in plaats van de niet-ondersteunde parameter te ontvangen.

Zie [Azure OpenAI-eindpunten](</nl/providers/openai#azure-openai-endpoints>) om OpenAI-afbeeldingsgeneratie via een Azure OpenAI-implementatie te routeren in plaats van via `api.openai.com`.

OpenRouter image models

OpenRouter-afbeeldingsgeneratie gebruikt dezelfde `OPENROUTER_API_KEY` en routeert via de chat completions image-API van OpenRouter. Selecteer OpenRouter-afbeeldingsmodellen met het prefix `openrouter/`:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "openrouter/google/gemini-3.1-flash-image-preview",      },    },  },}
[/code]

OpenClaw stuurt `prompt`, `count`, referentieafbeeldingen en Gemini-compatibele hints voor `aspectRatio` / `resolution` door naar OpenRouter. Huidige ingebouwde snelkoppelingen voor OpenRouter-afbeeldingsmodellen omvatten `google/gemini-3.1-flash-image-preview`, `google/gemini-3-pro-image-preview` en `openai/gpt-5.4-image-2`. Gebruik `action: "list"` om te zien wat je geconfigureerde Plugin aanbiedt.

MiniMax dual-auth

MiniMax-afbeeldingsgeneratie is beschikbaar via beide gebundelde MiniMax- authenticatiepaden:

  * `minimax/image-01` voor configuraties met API-sleutel
  * `minimax-portal/image-01` voor OAuth-configuraties

xAI grok-imagine-image

De gebundelde xAI-provider gebruikt `/v1/images/generations` voor aanvragen met alleen een prompt en `/v1/images/edits` wanneer `image` of `images` aanwezig is.

  * Modellen: `xai/grok-imagine-image`, `xai/grok-imagine-image-pro`
  * Aantal: maximaal 4
  * Referenties: één `image` of maximaal vijf `images`
  * Beeldverhoudingen: `1:1`, `16:9`, `9:16`, `4:3`, `3:4`, `2:3`, `3:2`
  * Resoluties: `1K`, `2K`
  * Uitvoer: geretourneerd als door OpenClaw beheerde afbeeldingsbijlagen


OpenClaw stelt xAI-eigen `quality`, `mask`, `user` of extra, alleen native beeldverhoudingen bewust niet beschikbaar totdat die besturingselementen bestaan in het gedeelde cross-providercontract `image_generate`.

## Voorbeelden

### Generate (4K landscape)

textCopy code
[code]
    /tool image_generate action=generate model=openai/gpt-image-2 prompt="A clean editorial poster for OpenClaw image generation" size=3840x2160 count=1
[/code]

### Generate (transparent PNG)

textCopy code
[code]
    /tool image_generate action=generate model=openai/gpt-image-1.5 prompt="A simple red circle sticker on a transparent background" outputFormat=png background=transparent
[/code]

Equivalente CLI:

bashCopy code
[code]
    openclaw infer image generate \--model openai/gpt-image-1.5 \--output-format png \--background transparent \--prompt "A simple red circle sticker on a transparent background" \--json
[/code]

### Generate (two square)

textCopy code
[code]
    /tool image_generate action=generate model=openai/gpt-image-2 prompt="Two visual directions for a calm productivity app icon" size=1024x1024 count=2
[/code]

### Edit (one reference)

textCopy code
[code]
    /tool image_generate action=generate model=openai/gpt-image-2 prompt="Keep the subject, replace the background with a bright studio setup" image=/path/to/reference.png size=1024x1536
[/code]

### Edit (multiple references)

textCopy code
[code]
    /tool image_generate action=generate model=openai/gpt-image-2 prompt="Combine the character identity from the first image with the color palette from the second" images='["/path/to/character.png","/path/to/palette.jpg"]' size=1536x1024
[/code]

Dezelfde vlaggen `--output-format` en `--background` zijn beschikbaar op `openclaw infer image edit`; `--openai-background` blijft beschikbaar als OpenAI-specifieke alias. Gebundelde providers anders dan OpenAI declareren momenteel geen expliciete achtergrondbesturing, dus `background: "transparent"` wordt voor hen als genegeerd gemeld.

## Gerelateerd

  * [Tooloverzicht](</nl/tools>) \- alle beschikbare agenttools
  * [ComfyUI](</nl/providers/comfy>) \- configuratie van lokale ComfyUI- en Comfy Cloud-workflows
  * [fal](</nl/providers/fal>) \- configuratie van fal-afbeeldings- en videoprovider
  * [Google (Gemini)](</nl/providers/google>) \- configuratie van Gemini-afbeeldingsprovider
  * [MiniMax](</nl/providers/minimax>) \- configuratie van MiniMax-afbeeldingsprovider
  * [OpenAI](</nl/providers/openai>) \- configuratie van OpenAI Images-provider
  * [Vydra](</nl/providers/vydra>) \- configuratie van Vydra voor afbeeldingen, video en spraak
  * [xAI](</nl/providers/xai>) \- configuratie van Grok voor afbeeldingen, video, zoeken, code-uitvoering en TTS
  * [Configuratiereferentie](</nl/gateway/config-agents#agent-defaults>) \- `imageGenerationModel`-configuratie
  * [Modellen](</nl/concepts/models>) \- modelconfiguratie en failover


Was this useful?YesNo