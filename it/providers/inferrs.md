---
title: Inferisce
source_url: https://docs.openclaw.ai/it/providers/inferrs
scraped_at: 2026-05-25
---

[inferrs](<https://github.com/ericcurtin/inferrs>) può servire modelli locali dietro un'API `/v1` compatibile con OpenAI. OpenClaw funziona con `inferrs` tramite il percorso generico `openai-completions`.

Proprietà | Valore  
---|---  
ID provider | `inferrs` (personalizzato; configura in `models.providers.inferrs`)  
Plugin | nessuno — `inferrs` non è un provider plugin OpenClaw incluso  
Variabile env auth | Facoltativa. Qualsiasi valore funziona se il server inferrs non ha auth  
API | compatibile con OpenAI (`openai-completions`)  
URL base suggerito | `http://127.0.0.1:8080/v1` (o dovunque risieda il server inferrs)  
  
## Introduzione

* ### Avvia inferrs con un modello

bashCopy code
[code]
    inferrs serve google/gemma-4-E2B-it \  --host 127.0.0.1 \  --port 8080 \  --device metal
[/code]

* ### Verifica che il server sia raggiungibile

bashCopy code
[code]
    curl http://127.0.0.1:8080/healthcurl http://127.0.0.1:8080/v1/models
[/code]

* ### Aggiungi una voce provider OpenClaw

Aggiungi una voce provider esplicita e punta il tuo modello predefinito a essa. Consulta l'esempio di configurazione completo qui sotto.

## Esempio di configurazione completo

Questo esempio usa Gemma 4 su un server `inferrs` locale.

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "inferrs/google/gemma-4-E2B-it" },      models: {        "inferrs/google/gemma-4-E2B-it": {          alias: "Gemma 4 (inferrs)",        },      },    },  },  models: {    mode: "merge",    providers: {      inferrs: {        baseUrl: "http://127.0.0.1:8080/v1",        apiKey: "inferrs-local",        api: "openai-completions",        models: [          {            id: "google/gemma-4-E2B-it",            name: "Gemma 4 E2B (inferrs)",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 131072,            maxTokens: 4096,            compat: {              requiresStringContent: true,            },          },        ],      },    },  },}
[/code]

## Avvio on demand

Inferrs può anche essere avviato da OpenClaw solo quando viene selezionato un modello `inferrs/...`. Aggiungi `localService` alla stessa voce provider:

json5Copy code
[code]
    {  models: {    providers: {      inferrs: {        baseUrl: "http://127.0.0.1:8080/v1",        apiKey: "inferrs-local",        api: "openai-completions",        timeoutSeconds: 300,        localService: {          command: "/opt/homebrew/bin/inferrs",          args: [            "serve",            "google/gemma-4-E2B-it",            "--host",            "127.0.0.1",            "--port",            "8080",            "--device",            "metal",          ],          healthUrl: "http://127.0.0.1:8080/v1/models",          readyTimeoutMs: 180000,          idleStopMs: 0,        },        models: [          {            id: "google/gemma-4-E2B-it",            name: "Gemma 4 E2B (inferrs)",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 131072,            maxTokens: 4096,            compat: {              requiresStringContent: true,            },          },        ],      },    },  },}
[/code]

`command` deve essere assoluto. Usa `which inferrs` sull'host Gateway e inserisci quel percorso nella configurazione. Per il riferimento completo dei campi, consulta [Servizi di modelli locali](</it/gateway/local-model-services>).

## Configurazione avanzata

Perché requiresStringContent è importante

Alcune route Chat Completions di `inferrs` accettano solo `messages[].content` come stringa, non array strutturati di parti di contenuto.

json5Copy code
[code]
    compat: {  requiresStringContent: true}
[/code]

OpenClaw appiattirà le parti di contenuto di solo testo in stringhe semplici prima di inviare la richiesta.

Avvertenza su Gemma e schema degli strumenti

Alcune combinazioni attuali di `inferrs` \+ Gemma accettano piccole richieste dirette a `/v1/chat/completions`, ma falliscono ancora nei turni completi del runtime agente OpenClaw.

Se succede, prova prima questo:

json5Copy code
[code]
    compat: {  requiresStringContent: true,  supportsTools: false}
[/code]

Questo disabilita la superficie dello schema degli strumenti di OpenClaw per il modello e può ridurre la pressione del prompt su backend locali più rigidi.

Se le piccole richieste dirette continuano a funzionare ma i normali turni agente OpenClaw continuano a bloccarsi dentro `inferrs`, il problema restante è di solito il comportamento del modello/server upstream anziché il livello di trasporto di OpenClaw.

Smoke test manuale

Dopo la configurazione, testa entrambi i livelli:

bashCopy code
[code]
    curl http://127.0.0.1:8080/v1/chat/completions \  -H 'content-type: application/json' \  -d '{"model":"google/gemma-4-E2B-it","messages":[{"role":"user","content":"What is 2 + 2?"}],"stream":false}'
[/code]

bashCopy code
[code]
    openclaw infer model run \  --model inferrs/google/gemma-4-E2B-it \  --prompt "What is 2 + 2? Reply with one short sentence." \  --json
[/code]

Se il primo comando funziona ma il secondo fallisce, controlla la sezione di risoluzione dei problemi qui sotto.

Comportamento in stile proxy

`inferrs` viene trattato come backend `/v1` compatibile con OpenAI in stile proxy, non come endpoint OpenAI nativo.

  * La formattazione delle richieste solo per OpenAI nativo non si applica qui
  * Nessun `service_tier`, nessun `store` Responses, nessun suggerimento di cache del prompt e nessuna formattazione del payload di compatibilità con il reasoning OpenAI
  * Gli header di attribuzione OpenClaw nascosti (`originator`, `version`, `User-Agent`) non vengono iniettati sugli URL base `inferrs` personalizzati


## Risoluzione dei problemi

curl /v1/models fallisce

`inferrs` non è in esecuzione, non è raggiungibile o non è associato all'host/porta previsto. Assicurati che il server sia avviato e in ascolto sull'indirizzo che hai configurato.

messages[].content expected a string

Imposta `compat.requiresStringContent: true` nella voce del modello. Consulta la sezione `requiresStringContent` sopra per i dettagli.

Le chiamate dirette a /v1/chat/completions riescono ma openclaw infer model run fallisce

Prova a impostare `compat.supportsTools: false` per disabilitare la superficie dello schema degli strumenti. Consulta l'avvertenza sullo schema degli strumenti di Gemma sopra.

inferrs continua a bloccarsi su turni agente più grandi

Se OpenClaw non riceve più errori di schema ma `inferrs` continua a bloccarsi su turni agente più grandi, trattalo come una limitazione upstream di `inferrs` o del modello. Riduci la pressione del prompt oppure passa a un backend locale o modello diverso.

## Correlati

[**Modelli locali** Esecuzione di OpenClaw con server di modelli locali. ](</it/gateway/local-models>) [**Servizi di modelli locali** Avvio on demand di server di modelli locali per provider configurati. ](</it/gateway/local-model-services>) [**Risoluzione dei problemi Gateway** Debug di backend locali compatibili con OpenAI che superano le sonde ma falliscono nelle esecuzioni agente. ](</it/gateway/troubleshooting#local-openai-compatible-backend-passes-direct-probes-but-agent-runs-fail>) [**Selezione del modello** Panoramica di tutti i provider, riferimenti dei modelli e comportamento di failover. ](</it/concepts/model-providers>)

Was this useful?YesNo