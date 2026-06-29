---
title: ds4
source_url: https://docs.openclaw.ai/it/providers/ds4
scraped_at: 2026-06-29
---

ModelsProviders

[ds4](<https://github.com/antirez/ds4>) serve DeepSeek V4 Flash da un backend Metal locale con un'API `/v1` compatibile con OpenAI. OpenClaw si connette a ds4 tramite la famiglia di provider generica `openai-completions`.

ds4 non è un Plugin provider OpenClaw incluso. Configuralo sotto `models.providers.ds4`, quindi seleziona `ds4/deepseek-v4-flash`.

  * ID provider: `ds4`
  * Plugin: nessuno
  * API: Chat Completions compatibile con OpenAI (`openai-completions`)
  * URL base suggerito: `http://127.0.0.1:18000/v1`
  * ID modello: `deepseek-v4-flash`
  * Chiamate agli strumenti: supportate tramite `tools` e `tool_calls` in stile OpenAI
  * Ragionamento: `thinking` e `reasoning_effort` in stile DeepSeek


## Requisiti

  * macOS con supporto Metal.
  * Un checkout ds4 funzionante con `ds4-server` e il file GGUF di DeepSeek V4 Flash.
  * Memoria sufficiente per il contesto che scegli. Valori `--ctx` più grandi allocano più memoria KV all'avvio del server.


## Avvio rapido

* ### Start ds4-server

Sostituisci `&lt;DS4_DIR&gt;` con il percorso del tuo checkout ds4.

bashCopy code
[code]
    &lt;DS4_DIR&gt;/ds4-server \  --model &lt;DS4_DIR&gt;/ds4flash.gguf \  --host 127.0.0.1 \  --port 18000 \  --ctx 32768 \  --tokens 128
[/code]

* ### Verify the OpenAI-compatible endpoint

bashCopy code
[code]
    curl http://127.0.0.1:18000/v1/models
[/code]

La risposta dovrebbe includere `deepseek-v4-flash`.

* ### Add the OpenClaw provider config

Aggiungi la configurazione da Configurazione completa, quindi esegui un controllo del modello una tantum:

bashCopy code
[code]
    openclaw infer model run \  --local \  --model ds4/deepseek-v4-flash \  --thinking off \  --prompt "Reply with exactly: openclaw-ds4-ok" \  --json
[/code]

## Configurazione completa

Usa questa configurazione quando ds4 è già in esecuzione su `127.0.0.1:18000`.

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "ds4/deepseek-v4-flash" },      models: {        "ds4/deepseek-v4-flash": {          alias: "DS4 local",        },      },    },  },  models: {    mode: "merge",    providers: {      ds4: {        baseUrl: "http://127.0.0.1:18000/v1",        apiKey: "ds4-local",        api: "openai-completions",        timeoutSeconds: 300,        models: [          {            id: "deepseek-v4-flash",            name: "DeepSeek V4 Flash (ds4)",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 32768,            maxTokens: 128,            compat: {              supportsUsageInStreaming: true,              supportsReasoningEffort: true,              maxTokensField: "max_tokens",              supportsStrictMode: false,              thinkingFormat: "deepseek",              supportedReasoningEfforts: ["low", "medium", "high", "xhigh"],            },          },        ],      },    },  },}
[/code]

Mantieni `contextWindow` allineato al valore `ds4-server --ctx`. Mantieni `maxTokens` allineato a `--tokens`, a meno che tu non voglia intenzionalmente che OpenClaw richieda meno output rispetto al valore predefinito del server.

## Avvio su richiesta

OpenClaw può avviare ds4 solo quando viene selezionato un modello `ds4/...`. Aggiungi `localService` alla stessa voce del provider:

json5Copy code
[code]
    {  models: {    providers: {      ds4: {        baseUrl: "http://127.0.0.1:18000/v1",        apiKey: "ds4-local",        api: "openai-completions",        timeoutSeconds: 300,        localService: {          command: "&lt;DS4_DIR&gt;/ds4-server",          args: [            "--model",            "&lt;DS4_DIR&gt;/ds4flash.gguf",            "--host",            "127.0.0.1",            "--port",            "18000",            "--ctx",            "32768",            "--tokens",            "128",          ],          cwd: "&lt;DS4_DIR&gt;",          healthUrl: "http://127.0.0.1:18000/v1/models",          readyTimeoutMs: 300000,          idleStopMs: 0,        },        models: [          {            id: "deepseek-v4-flash",            name: "DeepSeek V4 Flash (ds4)",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 32768,            maxTokens: 128,            compat: {              supportsUsageInStreaming: true,              supportsReasoningEffort: true,              maxTokensField: "max_tokens",              supportsStrictMode: false,              thinkingFormat: "deepseek",              supportedReasoningEfforts: ["low", "medium", "high", "xhigh"],            },          },        ],      },    },  },}
[/code]

`command` deve essere un percorso eseguibile assoluto. La ricerca della shell e l'espansione di `~` non vengono usate. Vedi [Servizi di modelli locali](</it/gateway/local-model-services>) per ogni campo `localService`.

## Think Max

ds4 applica Think Max solo quando entrambe le condizioni sono vere:

  * `ds4-server` viene avviato con `--ctx 393216` o superiore.
  * La richiesta usa `reasoning_effort: "max"` o il campo di effort ds4 equivalente.


Se esegui quel contesto grande, aggiorna sia i flag del server sia i metadati del modello OpenClaw:

json5Copy code
[code]
    {  contextWindow: 393216,  maxTokens: 384000,  compat: {    supportsUsageInStreaming: true,    supportsReasoningEffort: true,    maxTokensField: "max_tokens",    supportsStrictMode: false,    thinkingFormat: "deepseek",    supportedReasoningEfforts: ["low", "medium", "high", "xhigh", "max"],  },}
[/code]

## Test

Inizia con un controllo HTTP diretto:

bashCopy code
[code]
    curl http://127.0.0.1:18000/v1/chat/completions \  -H 'content-type: application/json' \  -d '{"model":"deepseek-v4-flash","messages":[{"role":"user","content":"Reply with exactly: ds4-ok"}],"max_tokens":16,"stream":false,"thinking":{"type":"disabled"}}'
[/code]

Quindi testa l'instradamento del modello OpenClaw:

bashCopy code
[code]
    openclaw infer model run \  --local \  --model ds4/deepseek-v4-flash \  --thinking off \  --prompt "Reply with exactly: openclaw-ds4-ok" \  --json
[/code]

Per uno smoke test completo di agente e chiamata agli strumenti, usa un contesto di almeno 32768:

bashCopy code
[code]
    openclaw agent \  --local \  --session-id ds4-tool-smoke \  --model ds4/deepseek-v4-flash \  --thinking off \  --message "Use the shell command pwd once, then reply exactly: tool-ok <output>" \  --json \  --timeout 240
[/code]

Risultato previsto:

  * `executionTrace.winnerProvider` è `ds4`
  * `executionTrace.winnerModel` è `deepseek-v4-flash`
  * `toolSummary.calls` è almeno `1`
  * `finalAssistantVisibleText` inizia con `tool-ok`


## Risoluzione dei problemi

curl /v1/models cannot connect

ds4 non è in esecuzione o non è associato all'host e alla porta in `baseUrl`. Avvia `ds4-server`, quindi riprova:

bashCopy code
[code]
    curl http://127.0.0.1:18000/v1/models
[/code]

500 prompt exceeds context

Il valore `--ctx` configurato è troppo piccolo per il turno OpenClaw. Aumenta `ds4-server --ctx`, quindi aggiorna `models.providers.ds4.models[].contextWindow` in modo che corrisponda. I turni completi degli agenti con strumenti richiedono molto più contesto rispetto a una richiesta curl diretta con un solo messaggio.

Think Max does not activate

ds4 usa Think Max solo quando `--ctx` è almeno `393216` e la richiesta richiede `reasoning_effort: "max"`. I contesti più piccoli ripiegano sul ragionamento alto.

The first request is slow

ds4 ha una fase di residenza Metal a freddo e di riscaldamento del modello. Usa `localService.readyTimeoutMs: 300000` quando OpenClaw avvia il server su richiesta.

## Correlati

[**Local model services** Avvia server di modelli locali su richiesta prima delle richieste ai modelli. ](</it/gateway/local-model-services>) [**Local models** Scegli e gestisci backend di modelli locali. ](</it/gateway/local-models>) [**Model providers** Configura riferimenti provider, autenticazione e failover. ](</it/concepts/model-providers>) [**DeepSeek** Comportamento del provider DeepSeek nativo e controlli di thinking. ](</it/providers/deepseek>)

Was this useful?YesNo

Open issue