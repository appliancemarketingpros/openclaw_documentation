---
title: NVIDIA
source_url: https://docs.openclaw.ai/it/providers/nvidia
scraped_at: 2026-05-25
---

NVIDIA fornisce un'API compatibile con OpenAI all'indirizzo `https://integrate.api.nvidia.com/v1` per modelli aperti gratuiti. Esegui l'autenticazione con una chiave API da [build.nvidia.com](<https://build.nvidia.com/settings/api-keys>).

## Per iniziare

* ### Ottieni la tua chiave API

Crea una chiave API su [build.nvidia.com](<https://build.nvidia.com/settings/api-keys>).

* ### Esporta la chiave ed esegui l'onboarding

bashCopy code
[code]
    export NVIDIA_API_KEY="nvapi-..."openclaw onboard --auth-choice nvidia-api-key
[/code]

* ### Imposta un modello NVIDIA

bashCopy code
[code]
    openclaw models set nvidia/nvidia/nemotron-3-super-120b-a12b
[/code]

Per la configurazione non interattiva, puoi anche passare direttamente la chiave:

bashCopy code
[code]
    openclaw onboard --auth-choice nvidia-api-key --nvidia-api-key "nvapi-..."
[/code]

## Esempio di configurazione

json5Copy code
[code]
    {  env: { NVIDIA_API_KEY: "nvapi-..." },  models: {    providers: {      nvidia: {        baseUrl: "https://integrate.api.nvidia.com/v1",        api: "openai-completions",      },    },  },  agents: {    defaults: {      model: { primary: "nvidia/nvidia/nemotron-3-super-120b-a12b" },    },  },}
[/code]

## Catalogo integrato

Riferimento modello | Nome | Contesto | Output massimo  
---|---|---|---  
`nvidia/nvidia/nemotron-3-super-120b-a12b` | NVIDIA Nemotron 3 Super 120B | 262,144 | 8,192  
`nvidia/moonshotai/kimi-k2.5` | Kimi K2.5 | 262,144 | 8,192  
`nvidia/minimaxai/minimax-m2.5` | Minimax M2.5 | 196,608 | 8,192  
`nvidia/z-ai/glm5` | GLM 5 | 202,752 | 8,192  
  
## Configurazione avanzata

Comportamento di abilitazione automatica

Il provider si abilita automaticamente quando la variabile di ambiente `NVIDIA_API_KEY` è impostata. Non è richiesta alcuna configurazione esplicita del provider oltre alla chiave.

Catalogo e prezzi

Il catalogo incluso è statico. I costi hanno valore predefinito `0` nel sorgente, poiché NVIDIA attualmente offre accesso API gratuito per i modelli elencati.

Endpoint compatibile con OpenAI

NVIDIA usa l'endpoint completions standard `/v1`. Qualsiasi strumento compatibile con OpenAI dovrebbe funzionare subito con l'URL di base NVIDIA.

Risposte lente dei provider personalizzati

Alcuni modelli personalizzati ospitati da NVIDIA possono richiedere più tempo del watchdog di inattività predefinito del modello prima di emettere il primo frammento di risposta. Per le voci di provider NVIDIA personalizzate, aumenta il timeout del provider invece di aumentare il timeout dell'intero runtime dell'agent:

json5Copy code
[code]
    {  models: {    providers: {      "custom-integrate-api-nvidia-com": {        baseUrl: "https://integrate.api.nvidia.com/v1",        api: "openai-completions",        apiKey: "NVIDIA_API_KEY",        timeoutSeconds: 300,      },    },  },  agents: {    defaults: {      models: {        "custom-integrate-api-nvidia-com/meta/llama-3.1-70b-instruct": {          params: { thinking: "off" },        },      },    },  },}
[/code]

## Correlati

[**Selezione del modello** Scelta di provider, riferimenti modello e comportamento di failover. ](</it/concepts/model-providers>) [**Riferimento alla configurazione** Riferimento completo alla configurazione per agent, modelli e provider. ](</it/gateway/configuration-reference>)

Was this useful?YesNo