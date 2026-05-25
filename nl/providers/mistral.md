---
title: Mistral
source_url: https://docs.openclaw.ai/nl/providers/mistral
scraped_at: 2026-05-25
---

OpenClaw bevat een gebundelde Mistral-Plugin die vier contracten registreert: chataanvullingen, mediabegrip (Voxtral-batchtranscriptie), realtime STT voor Voice Call (Voxtral Realtime) en geheugenembeddings (`mistral-embed`).

Eigenschap | Waarde  
---|---  
Provider-id | `mistral`  
Plugin | gebundeld, `enabledByDefault: true`  
Auth-env-var | `MISTRAL_API_KEY`  
Onboarding-vlag | `--auth-choice mistral-api-key`  
Directe CLI-vlag | `--mistral-api-key <key>`  
API | OpenAI-compatibel (`openai-completions`)  
Basis-URL | `https://api.mistral.ai/v1`  
Standaardmodel | `mistral/mistral-large-latest`  
Embeddingmodel | `mistral-embed`  
Voxtral-batch | `voxtral-mini-latest` (audiotranscriptie)  
Voxtral-realtime | `voxtral-mini-transcribe-realtime-2602`  
  
## Aan de slag

* ### Haal je API-sleutel op

Maak een API-sleutel aan in de [Mistral Console](<https://console.mistral.ai/>).

* ### Voer onboarding uit

bashCopy code
[code]
    openclaw onboard --auth-choice mistral-api-key
[/code]

Of geef de sleutel rechtstreeks door:

bashCopy code
[code]
    openclaw onboard --mistral-api-key "$MISTRAL_API_KEY"
[/code]

* ### Stel een standaardmodel in

json5Copy code
[code]
    {  env: { MISTRAL_API_KEY: "sk-..." },  agents: { defaults: { model: { primary: "mistral/mistral-large-latest" } } },}
[/code]

* ### Controleer of het model beschikbaar is

bashCopy code
[code]
    openclaw models list --provider mistral
[/code]

## Ingebouwde LLM-catalogus

[Mistral Medium 3.5](<https://docs.mistral.ai/models/model-cards/mistral-medium-3-5-26-04>) is het huidige gecombineerde Medium-model in de gebundelde catalogus: 128B dense gewichten, tekst- en beeldinvoer, 256K context, functieaanroepen, gestructureerde uitvoer, coderen en instelbare reasoning via de Chat Completions API. Gebruik `mistral/mistral-medium-3-5` wanneer je Mistrals nieuwere uniforme agentic/coding-model wilt in plaats van de standaard `mistral/mistral-large-latest`.

OpenClaw levert momenteel deze gebundelde Mistral-catalogus:

Model-ref | Invoer | Context | Max. uitvoer | Opmerkingen  
---|---|---|---|---  
`mistral/mistral-large-latest` | tekst, beeld | 262,144 | 16,384 | Standaardmodel  
`mistral/mistral-medium-2508` | tekst, beeld | 262,144 | 8,192 | Mistral Medium 3.1  
`mistral/mistral-medium-3-5` | tekst, beeld | 262,144 | 8,192 | Mistral Medium 3.5; instelbare reasoning  
`mistral/mistral-small-latest` | tekst, beeld | 128,000 | 16,384 | Mistral Small 4; instelbare reasoning via API `reasoning_effort`  
`mistral/pixtral-large-latest` | tekst, beeld | 128,000 | 32,768 | Pixtral  
`mistral/codestral-latest` | tekst | 256,000 | 4,096 | Coderen  
`mistral/devstral-medium-latest` | tekst | 262,144 | 32,768 | Devstral 2  
`mistral/magistral-small` | tekst | 128,000 | 40,000 | Reasoning ingeschakeld  
  
Smoke-test na onboarding Medium 3.5 zonder de Gateway te starten:

bashCopy code
[code]
    openclaw infer model run --local \  --model mistral/mistral-medium-3-5 \  --prompt "Reply with exactly: mistral-ok" \  --json
[/code]

Om de gebundelde catalogusrij te bekijken voordat je de configuratie wijzigt:

bashCopy code
[code]
    openclaw models list --all --provider mistral --plain
[/code]

## Audiotranscriptie (Voxtral)

Gebruik Voxtral voor batch-audiotranscriptie via de pijplijn voor mediabegrip.

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "mistral", model: "voxtral-mini-latest" }],      },    },  },}
[/code]

## Voice Call streaming STT

De gebundelde `mistral`-Plugin registreert Voxtral Realtime als streaming-STT-provider voor Voice Call.

Instelling | Configuratiepad | Standaard  
---|---|---  
API-sleutel | `plugins.entries.voice-call.config.streaming.providers.mistral.apiKey` | Valt terug op `MISTRAL_API_KEY`  
Model | `...mistral.model` | `voxtral-mini-transcribe-realtime-2602`  
Codering | `...mistral.encoding` | `pcm_mulaw`  
Samplefrequentie | `...mistral.sampleRate` | `8000`  
Doelvertraging | `...mistral.targetStreamingDelayMs` | `800`  
json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        config: {          streaming: {            enabled: true,            provider: "mistral",            providers: {              mistral: {                apiKey: "${MISTRAL_API_KEY}",                targetStreamingDelayMs: 800,              },            },          },        },      },    },  },}
[/code]

## Geavanceerde configuratie

Instelbare reasoning

`mistral/mistral-small-latest` (Mistral Small 4) en `mistral/mistral-medium-3-5` ondersteunen [instelbare reasoning](<https://docs.mistral.ai/studio-api/conversations/reasoning/adjustable>) op de Chat Completions API via `reasoning_effort` (`none` minimaliseert extra denkwerk in de uitvoer; `high` toont volledige denksporen vóór het definitieve antwoord). Mistral raadt `reasoning_effort="high"` aan voor agentic- en code-usecases met Medium 3.5.

OpenClaw koppelt het **thinking** -niveau van de sessie aan Mistrals API:

OpenClaw thinking-niveau | Mistral `reasoning_effort`  
---|---  
**off** / **minimal** | `none`  
**low** / **medium** / **high** / **xhigh** / **adaptive** / **max** | `high`  
  
Voorbeeld van modelspecifieke configuratie voor Medium 3.5-reasoning:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "mistral/mistral-medium-3-5" },      models: {        "mistral/mistral-medium-3-5": {          params: { thinking: "high" },        },      },    },  },}
[/code]

Geheugenembeddings

Mistral kan geheugenembeddings leveren via `/v1/embeddings` (standaardmodel: `mistral-embed`).

json5Copy code
[code]
    {  memorySearch: { provider: "mistral" },}
[/code]

Auth en basis-URL

  * Mistral-auth gebruikt `MISTRAL_API_KEY` (Bearer-header).
  * De basis-URL van de provider is standaard `https://api.mistral.ai/v1` en accepteert de standaard OpenAI-compatibele chat-completions-requestvorm.
  * Het standaardmodel voor onboarding is `mistral/mistral-large-latest`.
  * Overschrijf de basis-URL onder `models.providers.mistral.baseUrl` alleen wanneer Mistral expliciet een regionale endpoint publiceert die je nodig hebt.


## Gerelateerd

[**Modelselectie** Providers, model-refs en failover-gedrag kiezen. ](</nl/concepts/model-providers>) [**Mediabegrip** Instellen van audiotranscriptie en providerselectie. ](</nl/nodes/media-understanding>)

Was this useful?YesNo