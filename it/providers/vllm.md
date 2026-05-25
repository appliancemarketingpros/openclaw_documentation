---
title: vLLM
source_url: https://docs.openclaw.ai/it/providers/vllm
scraped_at: 2026-05-25
---

vLLM può servire modelli open-source (e alcuni personalizzati) tramite un'API HTTP **compatibile con OpenAI**. OpenClaw si connette a vLLM usando l'API `openai-completions`.

OpenClaw può anche **rilevare automaticamente** i modelli disponibili da vLLM quando lo abiliti con `VLLM_API_KEY` (qualsiasi valore funziona se il tuo server non applica l'autenticazione). Usa `vllm/*` in `agents.defaults.models` per mantenere dinamico il rilevamento quando configuri anche un URL di base vLLM personalizzato.

OpenClaw tratta `vllm` come un provider locale compatibile con OpenAI che supporta la contabilizzazione dell'uso in streaming, quindi i conteggi dei token di stato/contesto possono aggiornarsi dalle risposte `stream_options.include_usage`.

Proprietà | Valore  
---|---  
ID provider | `vllm`  
API | `openai-completions` (compatibile con OpenAI)  
Autenticazione | Variabile d'ambiente `VLLM_API_KEY`  
URL di base predefinito | `http://127.0.0.1:8000/v1`  
  
## Per iniziare

* ### Avvia vLLM con un server compatibile con OpenAI

Il tuo URL di base dovrebbe esporre endpoint `/v1` (ad es. `/v1/models`, `/v1/chat/completions`). vLLM viene comunemente eseguito su:

CodeCopy code
[code]
    http://127.0.0.1:8000/v1
[/code]

* ### Imposta la variabile d'ambiente della chiave API

Qualsiasi valore funziona se il tuo server non applica l'autenticazione:

bashCopy code
[code]
    export VLLM_API_KEY="vllm-local"
[/code]

* ### Seleziona un modello

Sostituisci con uno degli ID modello di vLLM:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "vllm/your-model-id" },    },  },}
[/code]

* ### Verifica che il modello sia disponibile

bashCopy code
[code]
    openclaw models list --provider vllm
[/code]

## Rilevamento dei modelli (provider implicito)

Quando `VLLM_API_KEY` è impostata (o esiste un profilo di autenticazione) e **non** definisci `models.providers.vllm`, OpenClaw interroga:

CodeCopy code
[code]
    GET http://127.0.0.1:8000/v1/models
[/code]

e converte gli ID restituiti in voci di modello.

## Configurazione esplicita (modelli manuali)

Usa una configurazione esplicita quando:

  * vLLM viene eseguito su un host o una porta diversi
  * Vuoi fissare i valori `contextWindow` o `maxTokens`
  * Il tuo server richiede una chiave API reale (o vuoi controllare le intestazioni)
  * Ti connetti a un endpoint vLLM trusted loopback, LAN o Tailscale

json5Copy code
[code]
    {  models: {    providers: {      vllm: {        baseUrl: "http://127.0.0.1:8000/v1",        apiKey: "${VLLM_API_KEY}",        api: "openai-completions",        request: { allowPrivateNetwork: true },        timeoutSeconds: 300, // Optional: extend connect/header/body/request timeout for slow local models        models: [          {            id: "your-model-id",            name: "Local vLLM Model",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 128000,            maxTokens: 8192,          },        ],      },    },  },}
[/code]

Per mantenere dinamico questo provider senza elencare manualmente ogni modello, aggiungi un carattere jolly del provider al catalogo dei modelli visibile:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "vllm/*": {},      },    },  },}
[/code]

## Configurazione avanzata

Comportamento in stile proxy

vLLM viene trattato come backend `/v1` compatibile con OpenAI in stile proxy, non come endpoint OpenAI nativo. Questo significa:

Comportamento | Applicato?  
---|---  
Modellazione delle richieste OpenAI nativa | No  
`service_tier` | Non inviato  
`store` delle risposte | Non inviato  
Suggerimenti per la prompt-cache | Non inviati  
Modellazione del payload compatibile con il reasoning OpenAI | Non applicata  
Intestazioni di attribuzione OpenClaw nascoste | Non iniettate negli URL di base personalizzati  
Controlli di thinking Qwen

Per i modelli Qwen serviti tramite vLLM, imposta `params.qwenThinkingFormat: "chat-template"` nella voce del modello quando il server si aspetta kwargs del chat-template Qwen. OpenClaw mappa `/think off` a:

jsonCopy code
[code]
    {  "chat_template_kwargs": {    "enable_thinking": false,    "preserve_thinking": true  }}
[/code]

I livelli di thinking diversi da `off` inviano `enable_thinking: true`. Se il tuo endpoint si aspetta invece flag di primo livello in stile DashScope, usa `params.qwenThinkingFormat: "top-level"` per inviare `enable_thinking` alla radice della richiesta. È accettato anche `params.qwen_thinking_format` in snake-case.

Controlli di thinking Nemotron 3

vLLM/Nemotron 3 può usare kwargs del chat-template per controllare se il reasoning viene restituito come reasoning nascosto o come testo di risposta visibile. Quando una sessione OpenClaw usa `vllm/nemotron-3-*` con thinking disattivato, il Plugin vLLM in bundle invia:

jsonCopy code
[code]
    {  "chat_template_kwargs": {    "enable_thinking": false,    "force_nonempty_content": true  }}
[/code]

Per personalizzare questi valori, imposta `chat_template_kwargs` nei params del modello. Se imposti anche `params.extra_body.chat_template_kwargs`, quel valore ha precedenza finale perché `extra_body` è l'ultima sovrascrittura del corpo della richiesta.

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "vllm/nemotron-3-super": {          params: {            chat_template_kwargs: {              enable_thinking: false,              force_nonempty_content: true,            },          },        },      },    },  },}
[/code]

Le chiamate agli strumenti Qwen appaiono come testo

Per prima cosa assicurati che vLLM sia stato avviato con il parser delle chiamate agli strumenti e il chat template corretti per il modello. Ad esempio, vLLM documenta `hermes` per i modelli Qwen2.5 e `qwen3_xml` per i modelli Qwen3-Coder.

Sintomi:

  * Skills o strumenti non vengono mai eseguiti
  * l'assistente stampa JSON/XML grezzo come `{"name":"read","arguments":...}`
  * vLLM restituisce un array `tool_calls` vuoto quando OpenClaw invia `tool_choice: "auto"`


Alcune combinazioni Qwen/vLLM restituiscono chiamate agli strumenti strutturate solo quando la richiesta usa `tool_choice: "required"`. Per quelle voci di modello, forza il campo della richiesta compatibile con OpenAI con `params.extra_body`:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "vllm/Qwen-Qwen2.5-Coder-32B-Instruct": {          params: {            extra_body: {              tool_choice: "required",            },          },        },      },    },  },}
[/code]

Sostituisci `Qwen-Qwen2.5-Coder-32B-Instruct` con l'ID esatto restituito da:

bashCopy code
[code]
    openclaw models list --provider vllm
[/code]

Puoi applicare la stessa sovrascrittura dalla CLI:

bashCopy code
[code]
    openclaw config set agents.defaults.models '{"vllm/Qwen-Qwen2.5-Coder-32B-Instruct":{"params":{"extra_body":{"tool_choice":"required"}}}}' --strict-json --merge
[/code]

Questa è una soluzione alternativa di compatibilità opt-in. Fa sì che ogni turno del modello con strumenti richieda una chiamata a uno strumento, quindi usala solo per una voce di modello locale dedicata dove quel comportamento è accettabile. Non usarla come impostazione predefinita globale per tutti i modelli vLLM e non usare un proxy che converte ciecamente testo arbitrario dell'assistente in chiamate agli strumenti eseguibili.

URL di base personalizzato

Se il tuo server vLLM viene eseguito su un host o una porta non predefiniti, imposta `baseUrl` nella configurazione esplicita del provider:

json5Copy code
[code]
    {  models: {    providers: {      vllm: {        baseUrl: "http://192.168.1.50:9000/v1",        apiKey: "${VLLM_API_KEY}",        api: "openai-completions",        request: { allowPrivateNetwork: true },        timeoutSeconds: 300,        models: [          {            id: "my-custom-model",            name: "Remote vLLM Model",            reasoning: false,            input: ["text"],            contextWindow: 64000,            maxTokens: 4096,          },        ],      },    },  },}
[/code]

## Risoluzione dei problemi

Prima risposta lenta o timeout del server remoto

Per modelli locali di grandi dimensioni, host LAN remoti o collegamenti tailnet, imposta un timeout della richiesta con ambito provider:

json5Copy code
[code]
    {  models: {    providers: {      vllm: {        baseUrl: "http://192.168.1.50:8000/v1",        apiKey: "${VLLM_API_KEY}",        api: "openai-completions",        request: { allowPrivateNetwork: true },        timeoutSeconds: 300,        models: [{ id: "your-model-id", name: "Local vLLM Model" }],      },    },  },}
[/code]

`timeoutSeconds` si applica solo alle richieste HTTP dei modelli vLLM, inclusi configurazione della connessione, intestazioni della risposta, streaming del corpo e l'abort totale del guarded-fetch. Preferiscilo prima di aumentare `agents.defaults.timeoutSeconds`, che controlla l'intera esecuzione dell'agente.

Server non raggiungibile

Controlla che il server vLLM sia in esecuzione e accessibile:

bashCopy code
[code]
    curl http://127.0.0.1:8000/v1/models
[/code]

Se vedi un errore di connessione, verifica l'host, la porta e che vLLM sia stato avviato con la modalità server compatibile con OpenAI. Per endpoint espliciti loopback, LAN o Tailscale, imposta anche `models.providers.vllm.request.allowPrivateNetwork: true`; le richieste del provider bloccano per impostazione predefinita gli URL di rete privata a meno che il provider non sia esplicitamente attendibile.

Errori di autenticazione nelle richieste

Se le richieste falliscono con errori di autenticazione, imposta una `VLLM_API_KEY` reale che corrisponda alla configurazione del tuo server, oppure configura il provider esplicitamente in `models.providers.vllm`.

Nessun modello rilevato

Il rilevamento automatico richiede che `VLLM_API_KEY` sia impostata. Se hai definito `models.providers.vllm`, OpenClaw usa solo i tuoi modelli dichiarati a meno che `agents.defaults.models` non includa `"vllm/*": {}`.

Gli strumenti vengono renderizzati come testo grezzo

Se un modello Qwen stampa la sintassi degli strumenti JSON/XML invece di eseguire una skill, controlla le indicazioni per Qwen nella Configurazione avanzata sopra. La correzione abituale è:

  * avviare vLLM con il parser/template corretto per quel modello
  * confermare l'ID esatto del modello con `openclaw models list --provider vllm`
  * aggiungere una sovrascrittura dedicata per modello `params.extra_body.tool_choice: "required"` solo se `tool_choice: "auto"` restituisce ancora chiamate agli strumenti vuote o solo testuali


## Correlati

[**Selezione del modello** Scelta dei provider, dei riferimenti ai modelli e del comportamento di failover. ](</it/concepts/model-providers>) [**OpenAI** Provider OpenAI nativo e comportamento delle route compatibili con OpenAI. ](</it/providers/openai>) [**OAuth e autenticazione** Dettagli dell'autenticazione e regole di riutilizzo delle credenziali. ](</it/gateway/authentication>) [**Risoluzione dei problemi** Problemi comuni e come risolverli. ](</it/help/troubleshooting>)

Was this useful?YesNo