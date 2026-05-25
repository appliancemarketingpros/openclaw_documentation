---
title: SGLang
source_url: https://docs.openclaw.ai/nl/providers/sglang
scraped_at: 2026-05-25
---

SGLang serveert open-weightmodellen via een OpenAI-compatibele HTTP-API. OpenClaw maakt verbinding met SGLang met de providerfamilie `openai-completions` en autodetectie van beschikbare modellen.

Eigenschap | Waarde  
---|---  
Provider-id | `sglang`  
Plugin | gebundeld, `enabledByDefault: true`  
Auth-env-var | `SGLANG_API_KEY` (elke niet-lege waarde als de server geen auth heeft)  
Onboardingvlag | `--auth-choice sglang`  
API | OpenAI-compatibel (`openai-completions`)  
Standaardbasis-URL | `http://127.0.0.1:30000/v1`  
Standaardmodel-placeholder | `sglang/Qwen/Qwen3-8B`  
Streaminggebruik | Ja (`supportsStreamingUsage: true`)  
Prijzen | Gemarkeerd als extern-gratis (`modelPricing.external: false`)  
  
OpenClaw detecteert ook **automatisch** beschikbare modellen van SGLang wanneer je je aanmeldt met `SGLANG_API_KEY`. Gebruik `sglang/*` in `agents.defaults.models` om detectie dynamisch te houden wanneer je ook een aangepaste SGLang-basis-URL configureert. Zie Modeldetectie (impliciete provider) hieronder.

## Aan de slag

* ### Start SGLang

Start SGLang met een OpenAI-compatibele server. Je basis-URL moet `/v1`-endpoints beschikbaar maken (bijvoorbeeld `/v1/models`, `/v1/chat/completions`). SGLang draait vaak op:

  * `http://127.0.0.1:30000/v1`


* ### Stel een API-sleutel in

Elke waarde werkt als er geen auth op je server is geconfigureerd:

bashCopy code
[code]
    export SGLANG_API_KEY="sglang-local"
[/code]

* ### Voer onboarding uit of stel direct een model in

bashCopy code
[code]
    openclaw onboard
[/code]

Of configureer het model handmatig:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "sglang/your-model-id" },    },  },}
[/code]

## Modeldetectie (impliciete provider)

Wanneer `SGLANG_API_KEY` is ingesteld (of er een auth-profiel bestaat) en je `models.providers.sglang` **niet** definieert, vraagt OpenClaw het volgende op:

  * `GET http://127.0.0.1:30000/v1/models`


en zet de geretourneerde ID's om in modelvermeldingen.

## Expliciete configuratie (handmatige modellen)

Gebruik expliciete configuratie wanneer:

  * SGLang op een andere host/poort draait.
  * Je `contextWindow`/`maxTokens`-waarden wilt vastzetten.
  * Je server een echte API-sleutel vereist (of je headers wilt beheren).

json5Copy code
[code]
    {  models: {    providers: {      sglang: {        baseUrl: "http://127.0.0.1:30000/v1",        apiKey: "${SGLANG_API_KEY}",        api: "openai-completions",        models: [          {            id: "your-model-id",            name: "Local SGLang Model",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 128000,            maxTokens: 8192,          },        ],      },    },  },}
[/code]

## Geavanceerde configuratie

Proxy-achtig gedrag

SGLang wordt behandeld als een proxy-achtige OpenAI-compatibele `/v1`-backend, niet als een native OpenAI-endpoint.

Gedrag | SGLang  
---|---  
OpenAI-only request shaping | Niet toegepast  
`service_tier`, Responses `store`, prompt-cache hints | Niet verzonden  
Reasoning-compat payload shaping | Niet toegepast  
Verborgen attributieheaders (`originator`, `version`, `User-Agent`) | Niet geïnjecteerd op aangepaste SGLang-basis-URL's  
Probleemoplossing

**Server niet bereikbaar**

Controleer of de server draait en reageert:

bashCopy code
[code]
    curl http://127.0.0.1:30000/v1/models
[/code]

**Auth-fouten**

Als aanvragen mislukken met auth-fouten, stel dan een echte `SGLANG_API_KEY` in die overeenkomt met je serverconfiguratie, of configureer de provider expliciet onder `models.providers.sglang`.

## Gerelateerd

[**Modelselectie** Providers, modelrefs en failovergedrag kiezen. ](</nl/concepts/model-providers>) [**Configuratiereferentie** Volledig configuratieschema inclusief providervermeldingen. ](</nl/gateway/configuration-reference>)

Was this useful?YesNo