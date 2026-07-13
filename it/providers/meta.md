---
title: Meta
source_url: https://docs.openclaw.ai/it/providers/meta
scraped_at: 2026-07-13
---

ModelsProviders

La **Meta API** utilizza la **Responses API** compatibile con OpenAI (`POST /v1/responses`) per il modello di ragionamento `muse-spark-1.1`. Il provider viene distribuito come Plugin OpenClaw incluso.

Proprietà | Valore  
---|---  
ID provider | `meta`  
Plugin | provider incluso  
Variabile d'ambiente di autenticazione | `MODEL_API_KEY`  
Flag di configurazione iniziale | `--auth-choice meta-api-key`  
Flag CLI diretto | `--meta-api-key <key>`  
API | Responses API (`openai-responses`)  
URL di base | `https://api.meta.ai/v1`  
Modello predefinito | `meta/muse-spark-1.1`  
Ragionamento predefinito | `high` (`reasoning.effort`)  
  
## Per iniziare

* ### Imposta la chiave API

OnboardingCopy code
[code]
    openclaw onboard --auth-choice meta-api-key
[/code]

Direct flagCopy code
[code]
    openclaw onboard --non-interactive --accept-risk \--auth-choice meta-api-key \--meta-api-key "$MODEL_API_KEY"
[/code]

Env onlyCopy code
[code]
    export MODEL_API_KEY=<key>
[/code]

* ### Verifica che i modelli siano disponibili

bashCopy code
[code]
    openclaw models list --provider meta
[/code]

Elenca la voce statica del catalogo `muse-spark-1.1`. Se `MODEL_API_KEY` non viene risolta, `openclaw models status --json` segnala la credenziale mancante in `auth.unusableProfiles`.

## Configurazione non interattiva

bashCopy code
[code]
    openclaw onboard --non-interactive --accept-risk \  --mode local \  --auth-choice meta-api-key \  --meta-api-key "$MODEL_API_KEY"
[/code]

## Catalogo integrato

Riferimento modello | Nome | Ragionamento | Finestra di contesto | Output massimo  
---|---|---|---|---  
`meta/muse-spark-1.1` | Muse Spark 1.1 | sì | 1,048,576 | 131,072  
  
Funzionalità:

  * Input di testo e immagini
  * Chiamata di strumenti e streaming
  * Livello di ragionamento: `minimal`, `low`, `medium`, `high`, `xhigh` (predefinito: `high`)
  * Riproduzione senza stato del ragionamento crittografato (`store: false`, `include: ["reasoning.encrypted_content"]`)


## Configurazione manuale

json5Copy code
[code]
    {  env: { MODEL_API_KEY: "<key>" },  agents: {    defaults: {      model: { primary: "meta/muse-spark-1.1" },      models: {        "meta/muse-spark-1.1": { alias: "Muse Spark 1.1" },      },    },  },}
[/code]

## Test rapido

bashCopy code
[code]
    export MODEL_API_KEY=<key>pnpm test:live -- extensions/meta/meta.live.test.ts
[/code]

I test in tempo reale utilizzano `muse-spark-1.1` con `POST /v1/responses`.

## Risorse correlate

[**Provider di modelli** Scelta dei provider, dei riferimenti ai modelli e del comportamento di failover. ](</it/concepts/model-providers>) [**Modalità di ragionamento** Livelli di ragionamento per muse-spark-1.1. ](</it/tools/thinking>) [**Riferimento per la configurazione** Impostazioni predefinite dell'agente e configurazione del modello. ](</it/gateway/config-agents#agent-defaults>)

Was this useful?YesNo

Open issue