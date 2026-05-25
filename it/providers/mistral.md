---
title: Mistral
source_url: https://docs.openclaw.ai/it/providers/mistral
scraped_at: 2026-05-25
---

OpenClaw include un Plugin Mistral in bundle che registra quattro contratti: completamenti chat, comprensione dei media (trascrizione batch Voxtral), STT in tempo reale per Voice Call (Voxtral Realtime) ed embedding di memoria (`mistral-embed`).

Proprietà | Valore  
---|---  
ID provider | `mistral`  
Plugin | in bundle, `enabledByDefault: true`  
Variabile env di autenticazione | `MISTRAL_API_KEY`  
Flag di onboarding | `--auth-choice mistral-api-key`  
Flag CLI diretto | `--mistral-api-key <key>`  
API | compatibile con OpenAI (`openai-completions`)  
URL di base | `https://api.mistral.ai/v1`  
Modello predefinito | `mistral/mistral-large-latest`  
Modello di embedding | `mistral-embed`  
Batch Voxtral | `voxtral-mini-latest` (trascrizione audio)  
Realtime Voxtral | `voxtral-mini-transcribe-realtime-2602`  
  
## Primi passi

* ### Get your API key

Crea una chiave API nella [Console Mistral](<https://console.mistral.ai/>).

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice mistral-api-key
[/code]

Oppure passa direttamente la chiave:

bashCopy code
[code]
    openclaw onboard --mistral-api-key "$MISTRAL_API_KEY"
[/code]

* ### Set a default model

json5Copy code
[code]
    {  env: { MISTRAL_API_KEY: "sk-..." },  agents: { defaults: { model: { primary: "mistral/mistral-large-latest" } } },}
[/code]

* ### Verify the model is available

bashCopy code
[code]
    openclaw models list --provider mistral
[/code]

## Catalogo LLM integrato

[Mistral Medium 3.5](<https://docs.mistral.ai/models/model-cards/mistral-medium-3-5-26-04>) è l'attuale modello Medium combinato nel catalogo in bundle: 128B di pesi densi, input di testo e immagini, contesto 256K, function calling, output strutturato, coding e ragionamento regolabile tramite l'API Chat Completions. Usa `mistral/mistral-medium-3-5` quando vuoi il modello agentic/coding unificato più recente di Mistral invece del predefinito `mistral/mistral-large-latest`.

OpenClaw attualmente distribuisce questo catalogo Mistral in bundle:

Rif. modello | Input | Contesto | Output max | Note  
---|---|---|---|---  
`mistral/mistral-large-latest` | testo, immagine | 262,144 | 16,384 | Modello predefinito  
`mistral/mistral-medium-2508` | testo, immagine | 262,144 | 8,192 | Mistral Medium 3.1  
`mistral/mistral-medium-3-5` | testo, immagine | 262,144 | 8,192 | Mistral Medium 3.5; ragionamento regolabile  
`mistral/mistral-small-latest` | testo, immagine | 128,000 | 16,384 | Mistral Small 4; ragionamento regolabile tramite API `reasoning_effort`  
`mistral/pixtral-large-latest` | testo, immagine | 128,000 | 32,768 | Pixtral  
`mistral/codestral-latest` | testo | 256,000 | 4,096 | Coding  
`mistral/devstral-medium-latest` | testo | 262,144 | 32,768 | Devstral 2  
`mistral/magistral-small` | testo | 128,000 | 40,000 | Con ragionamento abilitato  
  
Dopo l'onboarding, esegui uno smoke test di Medium 3.5 senza avviare il Gateway:

bashCopy code
[code]
    openclaw infer model run --local \  --model mistral/mistral-medium-3-5 \  --prompt "Reply with exactly: mistral-ok" \  --json
[/code]

Per consultare la riga del catalogo in bundle prima di modificare la configurazione:

bashCopy code
[code]
    openclaw models list --all --provider mistral --plain
[/code]

## Trascrizione audio (Voxtral)

Usa Voxtral per la trascrizione audio batch tramite la pipeline di comprensione dei media.

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "mistral", model: "voxtral-mini-latest" }],      },    },  },}
[/code]

## STT in streaming per Voice Call

Il Plugin `mistral` in bundle registra Voxtral Realtime come provider STT in streaming per Voice Call.

Impostazione | Percorso di configurazione | Predefinito  
---|---|---  
Chiave API | `plugins.entries.voice-call.config.streaming.providers.mistral.apiKey` | Usa come fallback `MISTRAL_API_KEY`  
Modello | `...mistral.model` | `voxtral-mini-transcribe-realtime-2602`  
Codifica | `...mistral.encoding` | `pcm_mulaw`  
Frequenza di campionamento | `...mistral.sampleRate` | `8000`  
Ritardo target | `...mistral.targetStreamingDelayMs` | `800`  
json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        config: {          streaming: {            enabled: true,            provider: "mistral",            providers: {              mistral: {                apiKey: "${MISTRAL_API_KEY}",                targetStreamingDelayMs: 800,              },            },          },        },      },    },  },}
[/code]

## Configurazione avanzata

Adjustable reasoning

`mistral/mistral-small-latest` (Mistral Small 4) e `mistral/mistral-medium-3-5` supportano il [ragionamento regolabile](<https://docs.mistral.ai/studio-api/conversations/reasoning/adjustable>) sull'API Chat Completions tramite `reasoning_effort` (`none` minimizza il pensiero aggiuntivo nell'output; `high` espone tracce di pensiero complete prima della risposta finale). Mistral consiglia `reasoning_effort="high"` per i casi d'uso agentic e di codice con Medium 3.5.

OpenClaw mappa il livello di **thinking** della sessione all'API di Mistral:

Livello di thinking OpenClaw | Mistral `reasoning_effort`  
---|---  
**off** / **minimal** | `none`  
**low** / **medium** / **high** / **xhigh** / **adaptive** / **max** | `high`  
  
Esempio di configurazione con ambito modello per il ragionamento di Medium 3.5:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "mistral/mistral-medium-3-5" },      models: {        "mistral/mistral-medium-3-5": {          params: { thinking: "high" },        },      },    },  },}
[/code]

Memory embeddings

Mistral può fornire embedding di memoria tramite `/v1/embeddings` (modello predefinito: `mistral-embed`).

json5Copy code
[code]
    {  memorySearch: { provider: "mistral" },}
[/code]

Auth and base URL

  * L'autenticazione Mistral usa `MISTRAL_API_KEY` (header Bearer).
  * L'URL di base del provider è predefinito su `https://api.mistral.ai/v1` e accetta la forma di richiesta chat-completions standard compatibile con OpenAI.
  * Il modello predefinito di onboarding è `mistral/mistral-large-latest`.
  * Sovrascrivi l'URL di base sotto `models.providers.mistral.baseUrl` solo quando Mistral pubblica esplicitamente un endpoint regionale di cui hai bisogno.


## Correlati

[**Model selection** Scelta di provider, riferimenti modello e comportamento di failover. ](</it/concepts/model-providers>) [**Media understanding** Configurazione della trascrizione audio e selezione del provider. ](</it/nodes/media-understanding>)

Was this useful?YesNo