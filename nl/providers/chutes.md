---
title: Chutes
source_url: https://docs.openclaw.ai/nl/providers/chutes
scraped_at: 2026-05-25
---

[Chutes](<https://chutes.ai>) biedt opensource-modelcatalogi aan via een OpenAI-compatibele API. OpenClaw ondersteunt zowel browser-OAuth als directe API-sleutel-authenticatie voor de meegeleverde `chutes`-provider.

Eigenschap | Waarde  
---|---  
Provider | `chutes`  
API | OpenAI-compatibel  
Basis-URL | `https://llm.chutes.ai/v1`  
Auth | OAuth of API-sleutel (zie hieronder)  
  
## Aan de slag

### OAuth

* ### Voer de OAuth-onboardingflow uit

bashCopy code
[code]
    openclaw onboard --auth-choice chutes
[/code]

OpenClaw start de browserflow lokaal, of toont een URL + flow voor het plakken van de redirect op externe/headless hosts. OAuth-tokens worden automatisch vernieuwd via OpenClaw-authenticatieprofielen.

* ### Controleer het standaardmodel

Na onboarding wordt het standaardmodel ingesteld op `chutes/zai-org/GLM-4.7-TEE` en wordt de meegeleverde Chutes-catalogus geregistreerd.

### API-sleutel

* ### Haal een API-sleutel op

Maak een sleutel aan op [chutes.ai/settings/api-keys](<https://chutes.ai/settings/api-keys>).

* ### Voer de onboardingflow voor de API-sleutel uit

bashCopy code
[code]
    openclaw onboard --auth-choice chutes-api-key
[/code]

* ### Controleer het standaardmodel

Na onboarding wordt het standaardmodel ingesteld op `chutes/zai-org/GLM-4.7-TEE` en wordt de meegeleverde Chutes-catalogus geregistreerd.

## Detectiegedrag

Wanneer Chutes-authenticatie beschikbaar is, bevraagt OpenClaw de Chutes-catalogus met die referentie en gebruikt het de gevonden modellen. Als detectie mislukt, valt OpenClaw terug op een meegeleverde statische catalogus, zodat onboarding en opstarten blijven werken.

## Standaardaliassen

OpenClaw registreert drie handige aliassen voor de meegeleverde Chutes-catalogus:

Alias | Doelmodel  
---|---  
`chutes-fast` | `chutes/zai-org/GLM-4.7-FP8`  
`chutes-pro` | `chutes/deepseek-ai/DeepSeek-V3.2-TEE`  
`chutes-vision` | `chutes/chutesai/Mistral-Small-3.2-24B-Instruct-2506`  
  
## Ingebouwde startercatalogus

De meegeleverde fallback-catalogus bevat huidige Chutes-refs:

Model-ref  
---  
`chutes/zai-org/GLM-4.7-TEE`  
`chutes/zai-org/GLM-5-TEE`  
`chutes/deepseek-ai/DeepSeek-V3.2-TEE`  
`chutes/deepseek-ai/DeepSeek-R1-0528-TEE`  
`chutes/moonshotai/Kimi-K2.5-TEE`  
`chutes/chutesai/Mistral-Small-3.2-24B-Instruct-2506`  
`chutes/Qwen/Qwen3-Coder-Next-TEE`  
`chutes/openai/gpt-oss-120b-TEE`  
  
## Configuratievoorbeeld

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "chutes/zai-org/GLM-4.7-TEE" },      models: {        "chutes/zai-org/GLM-4.7-TEE": { alias: "Chutes GLM 4.7" },        "chutes/deepseek-ai/DeepSeek-V3.2-TEE": { alias: "Chutes DeepSeek V3.2" },      },    },  },}
[/code]

OAuth-overschrijvingen

Je kunt de OAuth-flow aanpassen met optionele omgevingsvariabelen:

Variabele | Doel  
---|---  
`CHUTES_CLIENT_ID` | Aangepaste OAuth-client-ID  
`CHUTES_CLIENT_SECRET` | Aangepast OAuth-clientgeheim  
`CHUTES_OAUTH_REDIRECT_URI` | Aangepaste redirect-URI  
`CHUTES_OAUTH_SCOPES` | Aangepaste OAuth-scopes  
  
Zie de [Chutes OAuth-documentatie](<https://chutes.ai/docs/sign-in-with-chutes/overview>) voor vereisten en hulp voor redirect-apps.

Opmerkingen

  * API-sleutel- en OAuth-detectie gebruiken beide dezelfde provider-ID `chutes`.
  * Chutes-modellen worden geregistreerd als `chutes/<model-id>`.
  * Als detectie bij het opstarten mislukt, wordt de meegeleverde statische catalogus automatisch gebruikt.


## Gerelateerd

[**Modelselectie** Providerregels, model-refs en failovergedrag. ](</nl/concepts/model-providers>) [**Configuratiereferentie** Volledig configuratieschema, inclusief providerinstellingen. ](</nl/gateway/configuration-reference>) [**Chutes** Chutes-dashboard en API-documentatie. ](<https://chutes.ai>) [**Chutes API-sleutels** Chutes API-sleutels aanmaken en beheren. ](<https://chutes.ai/settings/api-keys>)

Was this useful?YesNo