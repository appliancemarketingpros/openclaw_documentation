---
title: ComfyUI
source_url: https://docs.openclaw.ai/nl/providers/comfy
scraped_at: 2026-05-25
---

OpenClaw levert een gebundelde `comfy` plugin voor workflow-gestuurde ComfyUI-runs. De plugin is volledig workflow-gestuurd, dus OpenClaw probeert geen generieke `size`-, `aspectRatio`-, `resolution`-, `durationSeconds`\- of TTS-achtige bedieningselementen op je grafiek te mappen.

Eigenschap | Detail  
---|---  
Provider | `comfy`  
Modellen | `comfy/workflow`  
Gedeelde oppervlakken | `image_generate`, `video_generate`, `music_generate`  
Auth | Geen voor lokale ComfyUI; `COMFY_API_KEY` of `COMFY_CLOUD_API_KEY` voor Comfy Cloud  
API | ComfyUI `/prompt` / `/history` / `/view` en Comfy Cloud `/api/*`  
  
## Wat het ondersteunt

  * Afbeeldingen genereren vanuit een workflow-JSON
  * Afbeeldingen bewerken met 1 geüploade referentieafbeelding
  * Video's genereren vanuit een workflow-JSON
  * Video's genereren met 1 geüploade referentieafbeelding
  * Muziek- of audiogeneratie via de gedeelde tool `music_generate`
  * Uitvoer downloaden vanaf een geconfigureerd knooppunt of alle overeenkomende uitvoerknooppunten


## Aan de slag

Kies tussen ComfyUI draaien op je eigen machine of Comfy Cloud gebruiken.

### Lokaal

**Beste voor:** je eigen ComfyUI-instantie draaien op je machine of LAN.

* ### Start ComfyUI lokaal

Zorg dat je lokale ComfyUI-instantie draait (standaard `http://127.0.0.1:8188`).

* ### Bereid je workflow-JSON voor

Exporteer of maak een ComfyUI-workflow-JSON-bestand. Noteer de knooppunt-ID's voor het promptinvoerknooppunt en het uitvoerknooppunt waaruit je OpenClaw wilt laten lezen.

* ### Configureer de provider

Stel `mode: "local"` in en verwijs naar je workflowbestand. Hier is een minimaal afbeeldingsvoorbeeld:

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          mode: "local",          baseUrl: "http://127.0.0.1:8188",          image: {            workflowPath: "./workflows/flux-api.json",            promptNodeId: "6",            outputNodeId: "9",          },        },      },    },  },}
[/code]

* ### Stel het standaardmodel in

Verwijs OpenClaw naar het model `comfy/workflow` voor de capability die je hebt geconfigureerd:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "comfy/workflow",      },    },  },}
[/code]

* ### Verifieer

bashCopy code
[code]
    openclaw models list --provider comfy
[/code]

### Comfy Cloud

**Beste voor:** workflows draaien op Comfy Cloud zonder lokale GPU-bronnen te beheren.

* ### Haal een API-sleutel op

Meld je aan op [comfy.org](<https://comfy.org>) en genereer een API-sleutel vanuit je accountdashboard.

* ### Stel de API-sleutel in

Geef je sleutel op via een van deze methoden:

bashCopy code
[code]
    # Environment variable (preferred)export COMFY_API_KEY="your-key" # Alternative environment variableexport COMFY_CLOUD_API_KEY="your-key" # Or inline in configopenclaw config set plugins.entries.comfy.config.apiKey "your-key"
[/code]

* ### Bereid je workflow-JSON voor

Exporteer of maak een ComfyUI-workflow-JSON-bestand. Noteer de knooppunt-ID's voor het promptinvoerknooppunt en het uitvoerknooppunt.

* ### Configureer de provider

Stel `mode: "cloud"` in en verwijs naar je workflowbestand:

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          mode: "cloud",          image: {            workflowPath: "./workflows/flux-api.json",            promptNodeId: "6",            outputNodeId: "9",          },        },      },    },  },}
[/code]

* ### Stel het standaardmodel in

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "comfy/workflow",      },    },  },}
[/code]

* ### Verifieer

bashCopy code
[code]
    openclaw models list --provider comfy
[/code]

## Configuratie

Comfy ondersteunt gedeelde verbindingsinstellingen op topniveau plus workflowsecties per capability (`image`, `video`, `music`):

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          mode: "local",          baseUrl: "http://127.0.0.1:8188",          image: {            workflowPath: "./workflows/flux-api.json",            promptNodeId: "6",            outputNodeId: "9",          },          video: {            workflowPath: "./workflows/video-api.json",            promptNodeId: "12",            outputNodeId: "21",          },          music: {            workflowPath: "./workflows/music-api.json",            promptNodeId: "3",            outputNodeId: "18",          },        },      },    },  },}
[/code]

### Gedeelde sleutels

Sleutel | Type | Beschrijving  
---|---|---  
`mode` | `"local"` of `"cloud"` | Verbindingsmodus.  
`baseUrl` | string | Standaard `http://127.0.0.1:8188` voor lokaal of `https://cloud.comfy.org` voor cloud.  
`apiKey` | string | Optionele inline sleutel, alternatief voor de env-vars `COMFY_API_KEY` / `COMFY_CLOUD_API_KEY`.  
`allowPrivateNetwork` | boolean | Sta een privé-/LAN-`baseUrl` toe in cloudmodus.  
  
### Sleutels per capability

Deze sleutels zijn van toepassing binnen de secties `image`, `video` of `music`:

Sleutel | Vereist | Standaard | Beschrijving  
---|---|---|---  
`workflow` of `workflowPath` | Ja | \-- | Pad naar het ComfyUI-workflow-JSON-bestand.  
`promptNodeId` | Ja | \-- | Knooppunt-ID dat de tekstprompt ontvangt.  
`promptInputName` | Nee | `"text"` | Invoernaam op het promptknooppunt.  
`outputNodeId` | Nee | \-- | Knooppunt-ID om uitvoer uit te lezen. Indien weggelaten, worden alle overeenkomende uitvoerknooppunten gebruikt.  
`pollIntervalMs` | Nee | \-- | Pollinginterval in milliseconden voor voltooiing van de taak.  
`timeoutMs` | Nee | \-- | Timeout in milliseconden voor de workflow-run.  
  
De secties `image` en `video` ondersteunen ook:

Sleutel | Vereist | Standaard | Beschrijving  
---|---|---|---  
`inputImageNodeId` | Ja (bij het doorgeven van een referentieafbeelding) | \-- | Knooppunt-ID dat de geüploade referentieafbeelding ontvangt.  
`inputImageInputName` | Nee | `"image"` | Invoernaam op het afbeeldingsknooppunt.  
  
## Workflowdetails

Afbeeldingsworkflows

Stel het standaardafbeeldingsmodel in op `comfy/workflow`:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "comfy/workflow",      },    },  },}
[/code]

**Voorbeeld voor bewerken met referentieafbeelding:**

Voeg `inputImageNodeId` toe aan je afbeeldingsconfiguratie om afbeeldingsbewerking met een geüploade referentieafbeelding in te schakelen:

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          image: {            workflowPath: "./workflows/edit-api.json",            promptNodeId: "6",            inputImageNodeId: "7",            inputImageInputName: "image",            outputNodeId: "9",          },        },      },    },  },}
[/code]

Videoworkflows

Stel het standaardvideomodel in op `comfy/workflow`:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "comfy/workflow",      },    },  },}
[/code]

Comfy-videoworkflows ondersteunen tekst-naar-video en afbeelding-naar-video via de geconfigureerde grafiek.

Muziekworkflows

De gebundelde plugin registreert een provider voor muziekgeneratie voor door workflows gedefinieerde audio- of muziekuitvoer, beschikbaar via de gedeelde tool `music_generate`:

textCopy code
[code]
    /tool music_generate prompt="Warm ambient synth loop with soft tape texture"
[/code]

Gebruik de configuratiesectie `music` om naar je audio-workflow-JSON en uitvoerknooppunt te verwijzen.

Achterwaartse compatibiliteit

Bestaande afbeeldingsconfiguratie op topniveau (zonder de geneste sectie `image`) werkt nog steeds:

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          workflowPath: "./workflows/flux-api.json",          promptNodeId: "6",          outputNodeId: "9",        },      },    },  },}
[/code]

OpenClaw behandelt die verouderde vorm als de afbeeldingsworkflowconfiguratie. Je hoeft niet onmiddellijk te migreren, maar de geneste secties `image` / `video` / `music` worden aanbevolen voor nieuwe setups.

Live tests

Opt-in live dekking bestaat voor de gebundelde plugin:

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 COMFY_LIVE_TEST=1 pnpm test:live -- extensions/comfy/comfy.live.test.ts
[/code]

De live test slaat afzonderlijke afbeeldings-, video- of muziekgevallen over tenzij de overeenkomende Comfy-workflowsectie is geconfigureerd.

## Gerelateerd

[**Afbeeldingen genereren** Configuratie en gebruik van de tool voor het genereren van afbeeldingen. ](</nl/tools/image-generation>) [**Video's genereren** Configuratie en gebruik van de tool voor het genereren van video's. ](</nl/tools/video-generation>) [**Muziek genereren** Instelling van de tool voor het genereren van muziek en audio. ](</nl/tools/music-generation>) [**Provideroverzicht** Overzicht van alle providers en modelreferenties. ](</nl/providers>) [**Configuratiereferentie** Volledige configuratiereferentie inclusief standaardwaarden voor agents. ](</nl/gateway/config-agents#agent-defaults>)

Was this useful?YesNo