---
title: Qianfan
source_url: https://docs.openclaw.ai/nl/providers/qianfan
scraped_at: 2026-05-25
---

Qianfan is Baidu's MaaS-platform, dat een **uniforme API** biedt die aanvragen naar veel modellen achter één endpoint en API-sleutel routeert. Het is OpenAI-compatibel, dus de meeste OpenAI-SDK's werken door de basis-URL te wijzigen.

Eigenschap | Waarde  
---|---  
Provider | `qianfan`  
Auth | `QIANFAN_API_KEY`  
API | OpenAI-compatibel  
Basis-URL | `https://qianfan.baidubce.com/v2`  
  
## Aan de slag

* ### Maak een Baidu Cloud-account aan

Registreer je of log in bij de [Qianfan Console](<https://console.bce.baidu.com/qianfan/ais/console/apiKey>) en zorg dat je Qianfan API-toegang is ingeschakeld.

* ### Genereer een API-sleutel

Maak een nieuwe applicatie aan of selecteer een bestaande, en genereer vervolgens een API-sleutel. De sleutelindeling is `bce-v3/ALTAK-...`.

* ### Voer onboarding uit

bashCopy code
[code]
    openclaw onboard --auth-choice qianfan-api-key
[/code]

* ### Controleer of het model beschikbaar is

bashCopy code
[code]
    openclaw models list --provider qianfan
[/code]

## Ingebouwde catalogus

Modelreferentie | Invoer | Context | Maximale uitvoer | Redeneren | Opmerkingen  
---|---|---|---|---|---  
`qianfan/deepseek-v3.2` | tekst | 98,304 | 32,768 | Ja | Standaardmodel  
`qianfan/ernie-5.0-thinking-preview` | tekst, afbeelding | 119,000 | 64,000 | Ja | Multimodaal  
  
## Configuratievoorbeeld

json5Copy code
[code]
    {  env: { QIANFAN_API_KEY: "bce-v3/ALTAK-..." },  agents: {    defaults: {      model: { primary: "qianfan/deepseek-v3.2" },      models: {        "qianfan/deepseek-v3.2": { alias: "QIANFAN" },      },    },  },  models: {    providers: {      qianfan: {        baseUrl: "https://qianfan.baidubce.com/v2",        api: "openai-completions",        models: [          {            id: "deepseek-v3.2",            name: "DEEPSEEK V3.2",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 98304,            maxTokens: 32768,          },          {            id: "ernie-5.0-thinking-preview",            name: "ERNIE-5.0-Thinking-Preview",            reasoning: true,            input: ["text", "image"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 119000,            maxTokens: 64000,          },        ],      },    },  },}
[/code]

Transport en compatibiliteit

Qianfan gebruikt het OpenAI-compatibele transportpad, niet native OpenAI-aanvraagvorming. Dit betekent dat standaardfuncties van OpenAI-SDK's werken, maar providerspecifieke parameters mogelijk niet worden doorgestuurd.

Catalogus en overschrijvingen

De meegeleverde catalogus bevat momenteel `deepseek-v3.2` en `ernie-5.0-thinking-preview`. Voeg `models.providers.qianfan` alleen toe of overschrijf het alleen wanneer je een aangepaste basis-URL of modelmetadata nodig hebt.

Probleemoplossing

  * Zorg dat je API-sleutel begint met `bce-v3/ALTAK-` en dat Qianfan API-toegang is ingeschakeld in de Baidu Cloud-console.
  * Als modellen niet worden weergegeven, controleer dan of de Qianfan-service voor je account is geactiveerd.
  * De standaard basis-URL is `https://qianfan.baidubce.com/v2`. Wijzig deze alleen als je een aangepast endpoint of een proxy gebruikt.


## Gerelateerd

[**Modelselectie** Providers, modelreferenties en failovergedrag kiezen. ](</nl/concepts/model-providers>) [**Configuratiereferentie** Volledige OpenClaw-configuratiereferentie. ](</nl/gateway/configuration-reference>) [**Agentconfiguratie** Agentstandaarden en modeltoewijzingen configureren. ](</nl/concepts/agent>) [**Qianfan API-documentatie** Officiële Qianfan API-documentatie. ](<https://cloud.baidu.com/doc/qianfan-api/s/3m7of64lb>)

Was this useful?YesNo