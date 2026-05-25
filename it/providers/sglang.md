---
title: SGLang
source_url: https://docs.openclaw.ai/it/providers/sglang
scraped_at: 2026-05-25
---

SGLang serve modelli open-weight tramite un'API HTTP compatibile con OpenAI. OpenClaw si connette a SGLang usando la famiglia di provider `openai-completions` con rilevamento automatico dei modelli disponibili.

Proprietà | Valore  
---|---  
ID provider | `sglang`  
Plugin | incluso, `enabledByDefault: true`  
Variabile env di auth | `SGLANG_API_KEY` (qualsiasi valore non vuoto se il server non ha auth)  
Flag di onboarding | `--auth-choice sglang`  
API | compatibile con OpenAI (`openai-completions`)  
URL di base predefinito | `http://127.0.0.1:30000/v1`  
Segnaposto modello predefinito | `sglang/Qwen/Qwen3-8B`  
Uso dello streaming | Sì (`supportsStreamingUsage: true`)  
Prezzi | Contrassegnato come esterno gratuito (`modelPricing.external: false`)  
  
OpenClaw **rileva automaticamente** anche i modelli disponibili da SGLang quando aderisci impostando `SGLANG_API_KEY`. Usa `sglang/*` in `agents.defaults.models` per mantenere dinamico il rilevamento quando configuri anche un URL di base SGLang personalizzato. Vedi Rilevamento dei modelli (provider implicito) sotto.

## Per iniziare

* ### Start SGLang

Avvia SGLang con un server compatibile con OpenAI. Il tuo URL di base dovrebbe esporre endpoint `/v1` (per esempio `/v1/models`, `/v1/chat/completions`). SGLang viene comunemente eseguito su:

  * `http://127.0.0.1:30000/v1`


* ### Set an API key

Qualsiasi valore funziona se sul server non è configurata auth:

bashCopy code
[code]
    export SGLANG_API_KEY="sglang-local"
[/code]

* ### Run onboarding or set a model directly

bashCopy code
[code]
    openclaw onboard
[/code]

Oppure configura il modello manualmente:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "sglang/your-model-id" },    },  },}
[/code]

## Rilevamento dei modelli (provider implicito)

Quando `SGLANG_API_KEY` è impostato (o esiste un profilo auth) e **non** definisci `models.providers.sglang`, OpenClaw interrogherà:

  * `GET http://127.0.0.1:30000/v1/models`


e convertirà gli ID restituiti in voci di modello.

## Configurazione esplicita (modelli manuali)

Usa una configurazione esplicita quando:

  * SGLang viene eseguito su un host/porta diversi.
  * Vuoi fissare i valori `contextWindow`/`maxTokens`.
  * Il tuo server richiede una vera chiave API (o vuoi controllare gli header).

json5Copy code
[code]
    {  models: {    providers: {      sglang: {        baseUrl: "http://127.0.0.1:30000/v1",        apiKey: "${SGLANG_API_KEY}",        api: "openai-completions",        models: [          {            id: "your-model-id",            name: "Local SGLang Model",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 128000,            maxTokens: 8192,          },        ],      },    },  },}
[/code]

## Configurazione avanzata

Proxy-style behavior

SGLang viene trattato come backend `/v1` compatibile con OpenAI in stile proxy, non come endpoint OpenAI nativo.

Comportamento | SGLang  
---|---  
Modellazione delle richieste solo OpenAI | Non applicata  
`service_tier`, Responses `store`, suggerimenti prompt-cache | Non inviati  
Modellazione del payload compatibile con il reasoning | Non applicata  
Header di attribuzione nascosti (`originator`, `version`, `User-Agent`) | Non iniettati sugli URL di base SGLang personalizzati  
Troubleshooting

**Server non raggiungibile**

Verifica che il server sia in esecuzione e risponda:

bashCopy code
[code]
    curl http://127.0.0.1:30000/v1/models
[/code]

**Errori di auth**

Se le richieste falliscono con errori di auth, imposta una vera `SGLANG_API_KEY` che corrisponda alla configurazione del tuo server, oppure configura esplicitamente il provider sotto `models.providers.sglang`.

## Correlati

[**Model selection** Scelta di provider, riferimenti dei modelli e comportamento di failover. ](</it/concepts/model-providers>) [**Configuration reference** Schema di configurazione completo, incluse le voci provider. ](</it/gateway/configuration-reference>)

Was this useful?YesNo