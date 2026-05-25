---
title: Z.AI
source_url: https://docs.openclaw.ai/nl/providers/zai
scraped_at: 2026-05-25
---

[Z.AI](<http://Z.AI>) is het API-platform voor **GLM** -modellen. Het biedt REST-API's voor GLM en gebruikt API-sleutels voor authenticatie. Maak je API-sleutel aan in de Z.AI-console. OpenClaw gebruikt de `zai`-provider met een [Z.AI](<http://Z.AI>) API-sleutel.

  * Provider: `zai`
  * Auth: `ZAI_API_KEY`
  * API: [Z.AI](<http://Z.AI>) Chat Completions (Bearer-auth)


## Aan de slag

### Eindpunt automatisch detecteren

**Het beste voor:** de meeste gebruikers. OpenClaw detecteert het bijpassende Z.AI-eindpunt op basis van de sleutel en past automatisch de juiste basis-URL toe.

* ### Onboarding uitvoeren

bashCopy code
[code]
    openclaw onboard --auth-choice zai-api-key
[/code]

* ### Een standaardmodel instellen

json5Copy code
[code]
    {  env: { ZAI_API_KEY: "sk-..." },  agents: { defaults: { model: { primary: "zai/glm-5.1" } } },}
[/code]

* ### Controleren of het model wordt vermeld

bashCopy code
[code]
    openclaw models list --all --provider zai
[/code]

### Expliciet regionaal eindpunt

**Het beste voor:** gebruikers die een specifiek Coding Plan of algemeen API-oppervlak willen afdwingen.

* ### Kies de juiste onboardingoptie

bashCopy code
[code]
    # Coding Plan Global (recommended for Coding Plan users)openclaw onboard --auth-choice zai-coding-global # Coding Plan CN (China region)openclaw onboard --auth-choice zai-coding-cn # General APIopenclaw onboard --auth-choice zai-global # General API CN (China region)openclaw onboard --auth-choice zai-cn
[/code]

* ### Een standaardmodel instellen

json5Copy code
[code]
    {  env: { ZAI_API_KEY: "sk-..." },  agents: { defaults: { model: { primary: "zai/glm-5.1" } } },}
[/code]

* ### Controleren of het model wordt vermeld

bashCopy code
[code]
    openclaw models list --all --provider zai
[/code]

## Ingebouwde catalogus

OpenClaw levert de gebundelde `zai`-providercatalogus in het Plugin-manifest, zodat alleen-lezen vermelding bekende GLM-rijen kan tonen zonder de providerruntime te laden:

bashCopy code
[code]
    openclaw models list --all --provider zai
[/code]

De manifestgebaseerde catalogus bevat momenteel:

Modelreferentie | Opmerkingen  
---|---  
`zai/glm-5.1` | Standaardmodel  
`zai/glm-5` |   
`zai/glm-5-turbo` |   
`zai/glm-5v-turbo` |   
`zai/glm-4.7` |   
`zai/glm-4.7-flash` |   
`zai/glm-4.7-flashx` |   
`zai/glm-4.6` |   
`zai/glm-4.6v` |   
`zai/glm-4.5` |   
`zai/glm-4.5-air` |   
`zai/glm-4.5-flash` |   
`zai/glm-4.5v` |   
  
## Geavanceerde configuratie

Onbekende GLM-5-modellen vooruit oplossend verwerken

Onbekende `glm-5*`-id's worden nog steeds vooruit oplossend verwerkt op het gebundelde providerpad door provider-eigen metadata te synthetiseren op basis van de `glm-4.7`-sjabloon wanneer de id overeenkomt met de huidige vorm van de GLM-5-familie.

Tool-call-streaming

`tool_stream` is standaard ingeschakeld voor Z.AI-tool-call-streaming. Om dit uit te schakelen:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "zai/<model>": {          params: { tool_stream: false },        },      },    },  },}
[/code]

Denken en behouden denken

Z.AI-denken volgt de `/think`-regelaars van OpenClaw. Met denken uitgeschakeld verzendt OpenClaw `thinking: { type: "disabled" }` om reacties te voorkomen die het uitvoerbudget besteden aan `reasoning_content` vóór zichtbare tekst.

Behouden denken is opt-in omdat [Z.AI](<http://Z.AI>) vereist dat de volledige historische `reasoning_content` opnieuw wordt afgespeeld, wat prompttokens verhoogt. Schakel dit per model in:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "zai/glm-5.1": {          params: { preserveThinking: true },        },      },    },  },}
[/code]

Wanneer dit is ingeschakeld en denken aan staat, verzendt OpenClaw `thinking: { type: "enabled", clear_thinking: false }` en speelt eerdere `reasoning_content` opnieuw af voor hetzelfde OpenAI-compatibele transcript.

Geavanceerde gebruikers kunnen nog steeds de exacte providerpayload overschrijven met `params.extra_body.thinking`.

Begrip van afbeeldingen

De gebundelde Z.AI-Plugin registreert begrip van afbeeldingen.

Eigenschap | Waarde  
---|---  
Model | `glm-4.6v`  
  
Begrip van afbeeldingen wordt automatisch opgelost op basis van de geconfigureerde Z.AI-authenticatie; er is geen aanvullende configuratie nodig.

Authenticatiedetails

  * [Z.AI](<http://Z.AI>) gebruikt Bearer-auth met je API-sleutel.
  * De onboardingoptie `zai-api-key` detecteert automatisch het bijpassende Z.AI-eindpunt op basis van het sleutelvoorvoegsel.
  * Gebruik de expliciete regionale opties (`zai-coding-global`, `zai-coding-cn`, `zai-global`, `zai-cn`) wanneer je een specifiek API-oppervlak wilt afdwingen.


## Gerelateerd

[**GLM-modelfamilie** Overzicht van de modelfamilie voor GLM. ](</nl/providers/glm>) [**Modelselectie** Providers, modelreferenties en failovergedrag kiezen. ](</nl/concepts/model-providers>)

Was this useful?YesNo