---
title: Fornitore llama.cpp
source_url: https://docs.openclaw.ai/it/plugins/llama-cpp
scraped_at: 2026-06-29
---

CapabilitiesBundled plugin guides

`llama-cpp` è il Plugin provider esterno ufficiale per gli embedding GGUF locali. Possiede la dipendenza runtime `node-llama-cpp` usata da `memorySearch.provider: "local"`.

Installalo prima di usare gli embedding di memoria locali:

bashCopy code
[code]
    openclaw plugins install @openclaw/llama-cpp-provider
[/code]

Il pacchetto npm principale `openclaw` non include `node-llama-cpp`. Mantenere la dipendenza nativa in questo Plugin impedisce ai normali aggiornamenti npm di OpenClaw di eliminare un runtime installato manualmente all'interno della directory del pacchetto OpenClaw.

## Configurazione

Imposta il provider di ricerca in memoria su `local`:

json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        provider: "local",        local: {          modelPath: "hf:ggml-org/embeddinggemma-300m-qat-q8_0-GGUF/embeddinggemma-300m-qat-Q8_0.gguf",        },      },    },  },}
[/code]

Il modello predefinito è `embeddinggemma-300m-qat-Q8_0.gguf`. Puoi anche puntare `local.modelPath` a un file `.gguf` locale.

## Runtime nativo

Usa Node 24 per il percorso di installazione nativa più fluido. Le copie di lavoro del sorgente che usano pnpm potrebbero dover approvare e ricostruire la dipendenza nativa:

bashCopy code
[code]
    pnpm approve-buildspnpm rebuild node-llama-cpp
[/code]

Per embedding locali con meno attrito, usa invece un provider di servizi locale come Ollama o LM Studio.

Was this useful?YesNo

Open issue