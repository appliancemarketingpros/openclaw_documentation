---
title: Alibaba Model Studio
source_url: https://docs.openclaw.ai/nl/providers/alibaba
scraped_at: 2026-05-25
---

OpenClaw levert een meegeleverde `alibaba`-Plugin die een videogeneratieprovider registreert voor Wan-modellen op Alibaba Model Studio (de internationale naam voor DashScope). De Plugin is standaard ingeschakeld; je hoeft alleen een API-sleutel in te stellen.

Eigenschap | Waarde  
---|---  
Provider-id | `alibaba`  
Plugin | meegeleverd, `enabledByDefault: true`  
Auth-env-vars | `MODELSTUDIO_API_KEY` → `DASHSCOPE_API_KEY` → `QWEN_API_KEY` (eerste match wint)  
Onboarding-flag | `--auth-choice alibaba-model-studio-api-key`  
Directe CLI-flag | `--alibaba-model-studio-api-key <key>`  
Standaardmodel | `alibaba/wan2.6-t2v`  
Standaardbasis-URL | `https://dashscope-intl.aliyuncs.com`  
  
## Aan de slag

* ### Set an API key

Gebruik onboarding om de sleutel op te slaan voor de `alibaba`-provider:

bashCopy code
[code]
    openclaw onboard --auth-choice alibaba-model-studio-api-key
[/code]

Of geef de sleutel direct door tijdens installatie/onboarding:

bashCopy code
[code]
    openclaw onboard --alibaba-model-studio-api-key <your-key>
[/code]

Of exporteer een van de geaccepteerde env-vars voordat je de Gateway start:

bashCopy code
[code]
    export MODELSTUDIO_API_KEY=sk-...# or DASHSCOPE_API_KEY=...# or QWEN_API_KEY=...
[/code]

* ### Set a default video model

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "alibaba/wan2.6-t2v",      },    },  },}
[/code]

* ### Verify the provider is configured

bashCopy code
[code]
    openclaw models list --provider alibaba
[/code]

De lijst moet alle vijf meegeleverde Wan-modellen bevatten. Als `MODELSTUDIO_API_KEY` niet kan worden herleid, meldt `openclaw models status --json` de ontbrekende credential onder `auth.unusableProfiles`.

## Ingebouwde Wan-modellen

Modelverwijzing | Modus  
---|---  
`alibaba/wan2.6-t2v` | Tekst-naar-video (standaard)  
`alibaba/wan2.6-i2v` | Afbeelding-naar-video  
`alibaba/wan2.6-r2v` | Referentie-naar-video  
`alibaba/wan2.6-r2v-flash` | Referentie-naar-video (snel)  
`alibaba/wan2.7-r2v` | Referentie-naar-video  
  
## Mogelijkheden en limieten

De meegeleverde provider weerspiegelt de limieten van DashScope's Wan-video-API. Alle drie modi delen hetzelfde maximum voor het aantal video's per request en dezelfde duurlimiet; alleen de invoervorm verschilt.

Modus | Max. uitvoervideo's | Max. invoerafbeeldingen | Max. invoervideo's | Max. duur | Ondersteunde instellingen  
---|---|---|---|---|---  
Tekst-naar-video | 1 | n.v.t. | n.v.t. | 10 s | `size`, `aspectRatio`, `resolution`, `audio`, `watermark`  
Afbeelding-naar-video | 1 | 1 | n.v.t. | 10 s | `size`, `aspectRatio`, `resolution`, `audio`, `watermark`  
Referentie-naar-video | 1 | n.v.t. | 4 | 10 s | `size`, `aspectRatio`, `resolution`, `audio`, `watermark`  
  
Wanneer een request `durationSeconds` weglaat, stuurt de provider DashScope's geaccepteerde standaard van **5 seconden**. Stel `durationSeconds` expliciet in op de [videogeneratietool](</nl/tools/video-generation>) om dit te verlengen tot maximaal 10 s.

## Geavanceerde configuratie

Override the DashScope base URL

De provider gebruikt standaard het internationale DashScope-endpoint. Stel dit in om het endpoint voor de China-regio te gebruiken:

json5Copy code
[code]
    {  models: {    providers: {      alibaba: {        baseUrl: "https://dashscope.aliyuncs.com",      },    },  },}
[/code]

De provider verwijdert afsluitende schuine strepen voordat AIGC-taak-URL's worden opgebouwd.

Auth env priority

OpenClaw herleidt de Alibaba API-sleutel uit omgevingsvariabelen in deze volgorde en gebruikt de eerste niet-lege waarde:

  1. `MODELSTUDIO_API_KEY`
  2. `DASHSCOPE_API_KEY`
  3. `QWEN_API_KEY`


Geconfigureerde `auth.profiles`-vermeldingen (ingesteld via `openclaw models auth login`) overschrijven env-var-resolutie. Zie [Auth-profielen in de modellen-FAQ](</nl/help/faq-models#what-is-an-auth-profile>) voor profielrotatie, cooldown en override-mechanismen.

Relationship to the Qwen plugin

Beide meegeleverde Plugins praten met DashScope en accepteren overlappende API-sleutels. Gebruik:

  * `alibaba/wan*.*`-id's om de specifieke Wan-videoprovider aan te sturen die op deze pagina wordt beschreven.
  * `qwen/*`-id's voor Qwen-chat, embeddings en mediabegrip (zie [Qwen](</nl/providers/qwen>)).


Door `MODELSTUDIO_API_KEY` één keer in te stellen, worden beide Plugins geauthenticeerd omdat de lijst met auth-env-vars bewust overlapt; je hoeft niet elke Plugin afzonderlijk te onboarden.

## Gerelateerd

[**Video generation** Gedeelde parameters voor videotools en providerselectie. ](</nl/tools/video-generation>) [**Qwen** Qwen-chat, embeddings en configuratie voor mediabegrip met dezelfde DashScope-authenticatie. ](</nl/providers/qwen>) [**Configuration reference** Agentstandaarden en modelconfiguratie. ](</nl/gateway/config-agents#agent-defaults>) [**Models FAQ** Auth-profielen, wisselen van model en oplossen van fouten over "geen profiel". ](</nl/help/faq-models>)

Was this useful?YesNo