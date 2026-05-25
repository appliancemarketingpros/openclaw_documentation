---
title: Cerebras
source_url: https://docs.openclaw.ai/nl/providers/cerebras
scraped_at: 2026-05-25
---

[Cerebras](<https://www.cerebras.ai>) biedt snelle OpenAI-compatibele inference op aangepaste inferencehardware. OpenClaw bevat een gebundelde Cerebras-provider-Plugin met een statische catalogus van vier modellen.

Eigenschap | Waarde  
---|---  
Provider-id | `cerebras`  
Plugin | gebundeld, `enabledByDefault: true`  
Auth-env-var | `CEREBRAS_API_KEY`  
Onboarding-vlag | `--auth-choice cerebras-api-key`  
Directe CLI-vlag | `--cerebras-api-key <key>`  
API | OpenAI-compatibel (`openai-completions`)  
Basis-URL | `https://api.cerebras.ai/v1`  
Standaardmodel | `cerebras/zai-glm-4.7`  
  
## Aan de slag

* ### Een API-sleutel ophalen

Maak een API-sleutel aan in de [Cerebras Cloud Console](<https://cloud.cerebras.ai>).

* ### Onboarding uitvoeren

OnboardingCopy code
[code]
    openclaw onboard --auth-choice cerebras-api-key
[/code]

Directe vlagCopy code
[code]
    openclaw onboard --non-interactive \--auth-choice cerebras-api-key \--cerebras-api-key "$CEREBRAS_API_KEY"
[/code]

Alleen envCopy code
[code]
    export CEREBRAS_API_KEY=csk-...
[/code]

* ### Controleren of modellen beschikbaar zijn

bashCopy code
[code]
    openclaw models list --provider cerebras
[/code]

De lijst moet alle vier gebundelde modellen bevatten. Als `CEREBRAS_API_KEY` niet kan worden opgelost, meldt `openclaw models status --json` de ontbrekende referentie onder `auth.unusableProfiles`.

## Niet-interactieve installatie

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice cerebras-api-key \  --cerebras-api-key "$CEREBRAS_API_KEY"
[/code]

## Ingebouwde catalogus

OpenClaw levert een statische Cerebras-catalogus mee die het openbare OpenAI-compatibele endpoint weerspiegelt. Alle vier modellen delen een context van 128k en 8.192 maximale outputtokens.

Modelref | Naam | Redeneren | Opmerkingen  
---|---|---|---  
`cerebras/zai-glm-4.7` | [Z.ai](<http://Z.ai>) GLM 4.7 | ja | Standaardmodel; preview-redeneermodel  
`cerebras/gpt-oss-120b` | GPT OSS 120B | ja | Productie-redeneermodel  
`cerebras/qwen-3-235b-a22b-instruct-2507` | Qwen 3 235B Instruct | nee | Previewmodel zonder redeneren  
`cerebras/llama3.1-8b` | Llama 3.1 8B | nee | Productiemodel gericht op snelheid  
  
## Handmatige configuratie

Door de gebundelde Plugin heb je meestal alleen de API-sleutel nodig. Gebruik expliciete `models.providers.cerebras`-configuratie wanneer je modelmetadata wilt overschrijven of in `mode: "merge"` tegen de statische catalogus wilt draaien:

json5Copy code
[code]
    {  env: { CEREBRAS_API_KEY: "csk-..." },  agents: {    defaults: {      model: { primary: "cerebras/zai-glm-4.7" },    },  },  models: {    mode: "merge",    providers: {      cerebras: {        baseUrl: "https://api.cerebras.ai/v1",        apiKey: "${CEREBRAS_API_KEY}",        api: "openai-completions",        models: [          { id: "zai-glm-4.7", name: "Z.ai GLM 4.7" },          { id: "gpt-oss-120b", name: "GPT OSS 120B" },        ],      },    },  },}
[/code]

## Gerelateerd

[**Modelproviders** Providers, modelrefs en failovergedrag kiezen. ](</nl/concepts/model-providers>) [**Denkmodi** Redeneerinspanningsniveaus voor de twee redeneercapabele Cerebras-modellen. ](</nl/tools/thinking>) [**Configuratiereferentie** Agentstandaarden en modelconfiguratie. ](</nl/gateway/config-agents#agent-defaults>) [**Modellen-FAQ** Auth-profielen, modellen wisselen en fouten met "no profile" oplossen. ](</nl/help/faq-models>)

Was this useful?YesNo