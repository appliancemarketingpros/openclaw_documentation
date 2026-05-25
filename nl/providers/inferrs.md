---
title: Leidt af
source_url: https://docs.openclaw.ai/nl/providers/inferrs
scraped_at: 2026-05-25
---

[inferrs](<https://github.com/ericcurtin/inferrs>) kan lokale modellen aanbieden achter een OpenAI-compatibele `/v1`-API. OpenClaw werkt met `inferrs` via het generieke `openai-completions`-pad.

Eigenschap | Waarde  
---|---  
Provider-id | `inferrs` (aangepast; configureer onder `models.providers.inferrs`)  
Plugin | geen — `inferrs` is geen gebundelde OpenClaw-provider-Plugin  
Auth-env-var | Optioneel. Elke waarde werkt als je inferrs-server geen auth heeft  
API | OpenAI-compatibel (`openai-completions`)  
Voorgestelde base-URL | `http://127.0.0.1:8080/v1` (of waar je inferrs-server ook draait)  
  
## Aan de slag

* ### Start inferrs met een model

bashCopy code
[code]
    inferrs serve google/gemma-4-E2B-it \  --host 127.0.0.1 \  --port 8080 \  --device metal
[/code]

* ### Controleer of de server bereikbaar is

bashCopy code
[code]
    curl http://127.0.0.1:8080/healthcurl http://127.0.0.1:8080/v1/models
[/code]

* ### Voeg een OpenClaw-providervermelding toe

Voeg een expliciete providervermelding toe en laat je standaardmodel ernaar verwijzen. Zie het volledige configuratievoorbeeld hieronder.

## Volledig configuratievoorbeeld

Dit voorbeeld gebruikt Gemma 4 op een lokale `inferrs`-server.

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "inferrs/google/gemma-4-E2B-it" },      models: {        "inferrs/google/gemma-4-E2B-it": {          alias: "Gemma 4 (inferrs)",        },      },    },  },  models: {    mode: "merge",    providers: {      inferrs: {        baseUrl: "http://127.0.0.1:8080/v1",        apiKey: "inferrs-local",        api: "openai-completions",        models: [          {            id: "google/gemma-4-E2B-it",            name: "Gemma 4 E2B (inferrs)",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 131072,            maxTokens: 4096,            compat: {              requiresStringContent: true,            },          },        ],      },    },  },}
[/code]

## Opstarten op aanvraag

Inferrs kan ook alleen door OpenClaw worden gestart wanneer een `inferrs/...`-model is geselecteerd. Voeg `localService` toe aan dezelfde providervermelding:

json5Copy code
[code]
    {  models: {    providers: {      inferrs: {        baseUrl: "http://127.0.0.1:8080/v1",        apiKey: "inferrs-local",        api: "openai-completions",        timeoutSeconds: 300,        localService: {          command: "/opt/homebrew/bin/inferrs",          args: [            "serve",            "google/gemma-4-E2B-it",            "--host",            "127.0.0.1",            "--port",            "8080",            "--device",            "metal",          ],          healthUrl: "http://127.0.0.1:8080/v1/models",          readyTimeoutMs: 180000,          idleStopMs: 0,        },        models: [          {            id: "google/gemma-4-E2B-it",            name: "Gemma 4 E2B (inferrs)",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 131072,            maxTokens: 4096,            compat: {              requiresStringContent: true,            },          },        ],      },    },  },}
[/code]

`command` moet absoluut zijn. Gebruik `which inferrs` op de Gateway-host en zet dat pad in de configuratie. Zie voor de volledige veldreferentie [Lokale modelservices](</nl/gateway/local-model-services>).

## Geavanceerde configuratie

Waarom requiresStringContent belangrijk is

Sommige `inferrs` Chat Completions-routes accepteren alleen string `messages[].content`, geen gestructureerde arrays met contentonderdelen.

json5Copy code
[code]
    compat: {  requiresStringContent: true}
[/code]

OpenClaw maakt van pure tekstcontentonderdelen platte strings voordat het verzoek wordt verzonden.

Kanttekening bij Gemma en toolschema's

Sommige huidige combinaties van `inferrs` \+ Gemma accepteren kleine directe `/v1/chat/completions`-verzoeken, maar mislukken nog steeds bij volledige OpenClaw agent-runtime beurten.

Als dat gebeurt, probeer dan eerst dit:

json5Copy code
[code]
    compat: {  requiresStringContent: true,  supportsTools: false}
[/code]

Dat schakelt OpenClaw's toolschema-oppervlak voor het model uit en kan de promptdruk op strengere lokale backends verlagen.

Als heel kleine directe verzoeken nog steeds werken, maar normale OpenClaw-agentbeurten blijven crashen binnen `inferrs`, ligt het resterende probleem meestal bij upstream model-/servergedrag en niet bij OpenClaw's transportlaag.

Handmatige smoke-test

Test na configuratie beide lagen:

bashCopy code
[code]
    curl http://127.0.0.1:8080/v1/chat/completions \  -H 'content-type: application/json' \  -d '{"model":"google/gemma-4-E2B-it","messages":[{"role":"user","content":"What is 2 + 2?"}],"stream":false}'
[/code]

bashCopy code
[code]
    openclaw infer model run \  --model inferrs/google/gemma-4-E2B-it \  --prompt "What is 2 + 2? Reply with one short sentence." \  --json
[/code]

Als de eerste opdracht werkt maar de tweede mislukt, raadpleeg dan de probleemoplossingssectie hieronder.

Proxy-achtig gedrag

`inferrs` wordt behandeld als een proxy-achtige OpenAI-compatibele `/v1`-backend, niet als een native OpenAI-eindpunt.

  * Native OpenAI-specifieke request shaping is hier niet van toepassing
  * Geen `service_tier`, geen Responses `store`, geen prompt-cache-hints en geen OpenAI reasoning-compat payload shaping
  * Verborgen OpenClaw-attributieheaders (`originator`, `version`, `User-Agent`) worden niet geïnjecteerd op aangepaste `inferrs` base-URL's


## Probleemoplossing

curl /v1/models mislukt

`inferrs` draait niet, is niet bereikbaar of is niet gebonden aan de verwachte host/poort. Zorg dat de server is gestart en luistert op het adres dat je hebt geconfigureerd.

messages[].content verwachtte een string

Stel `compat.requiresStringContent: true` in de modelvermelding in. Zie de sectie `requiresStringContent` hierboven voor details.

Directe /v1/chat/completions-aanroepen slagen, maar openclaw infer model run mislukt

Probeer `compat.supportsTools: false` in te stellen om het toolschema-oppervlak uit te schakelen. Zie de kanttekening bij Gemma-toolschema's hierboven.

inferrs crasht nog steeds bij grotere agentbeurten

Als OpenClaw geen schemafouten meer krijgt, maar `inferrs` nog steeds crasht bij grotere agentbeurten, behandel dit dan als een upstream `inferrs`\- of modelbeperking. Verminder de promptdruk of stap over op een andere lokale backend of een ander model.

## Gerelateerd

[**Lokale modellen** OpenClaw uitvoeren tegen lokale modelservers. ](</nl/gateway/local-models>) [**Lokale modelservices** Lokale modelservers op aanvraag starten voor geconfigureerde providers. ](</nl/gateway/local-model-services>) [**Gateway-probleemoplossing** Lokale OpenAI-compatibele backends debuggen die probes doorstaan maar agent-runs laten mislukken. ](</nl/gateway/troubleshooting#local-openai-compatible-backend-passes-direct-probes-but-agent-runs-fail>) [**Modelselectie** Overzicht van alle providers, modelrefs en failovergedrag. ](</nl/concepts/model-providers>)

Was this useful?YesNo