---
title: Meta
source_url: https://docs.openclaw.ai/nl/providers/meta
scraped_at: 2026-07-13
---

ModelsProviders

De **Meta API** gebruikt de OpenAI-compatibele **Responses API** (`POST /v1/responses`) voor het redeneermodel `muse-spark-1.1`. De provider wordt geleverd als een gebundelde OpenClaw- plugin.

Eigenschap | Waarde  
---|---  
Provider-id | `meta`  
Plugin | gebundelde provider  
Omgevingsvariabele voor authenticatie | `MODEL_API_KEY`  
Onboarding-vlag | `--auth-choice meta-api-key`  
Directe CLI-vlag | `--meta-api-key <key>`  
API | Responses API (`openai-responses`)  
Basis-URL | `https://api.meta.ai/v1`  
Standaardmodel | `meta/muse-spark-1.1`  
Standaardredenering | `high` (`reasoning.effort`)  
  
## Aan de slag

* ### Stel de API-sleutel in

OnboardingCopy code
[code]
    openclaw onboard --auth-choice meta-api-key
[/code]

Directe vlagCopy code
[code]
    openclaw onboard --non-interactive --accept-risk \--auth-choice meta-api-key \--meta-api-key "$MODEL_API_KEY"
[/code]

Alleen omgevingsvariabeleCopy code
[code]
    export MODEL_API_KEY=<key>
[/code]

* ### Controleer of modellen beschikbaar zijn

bashCopy code
[code]
    openclaw models list --provider meta
[/code]

Toont de statische catalogusvermelding voor `muse-spark-1.1`. Als `MODEL_API_KEY` niet kan worden gevonden, meldt `openclaw models status --json` de ontbrekende referentie onder `auth.unusableProfiles`.

## Niet-interactieve configuratie

bashCopy code
[code]
    openclaw onboard --non-interactive --accept-risk \  --mode local \  --auth-choice meta-api-key \  --meta-api-key "$MODEL_API_KEY"
[/code]

## Ingebouwde catalogus

Modelreferentie | Naam | Redenering | Contextvenster | Maximale uitvoer  
---|---|---|---|---  
`meta/muse-spark-1.1` | Muse Spark 1.1 | ja | 1,048,576 | 131,072  
  
Mogelijkheden:

  * Tekst- en afbeeldingsinvoer
  * Toolaanroepen en streaming
  * Redeneerinspanning: `minimal`, `low`, `medium`, `high`, `xhigh` (standaard: `high`)
  * Statusloze, versleutelde herhaling van redeneringen (`store: false`, `include: ["reasoning.encrypted_content"]`)


## Handmatige configuratie

json5Copy code
[code]
    {  env: { MODEL_API_KEY: "<key>" },  agents: {    defaults: {      model: { primary: "meta/muse-spark-1.1" },      models: {        "meta/muse-spark-1.1": { alias: "Muse Spark 1.1" },      },    },  },}
[/code]

## Snelle test

bashCopy code
[code]
    export MODEL_API_KEY=<key>pnpm test:live -- extensions/meta/meta.live.test.ts
[/code]

Live-tests gebruiken `muse-spark-1.1` met `POST /v1/responses`.

## Gerelateerd

[**Modelproviders** Providers, modelreferenties en failovergedrag kiezen. ](</nl/concepts/model-providers>) [**Denkmodi** Niveaus voor redeneerinspanning voor muse-spark-1.1. ](</nl/tools/thinking>) [**Configuratiereferentie** Standaardinstellingen voor agents en modelconfiguratie. ](</nl/gateway/config-agents#agent-defaults>)

Was this useful?YesNo

Open issue