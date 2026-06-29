---
title: llama.cpp-provider
source_url: https://docs.openclaw.ai/nl/plugins/llama-cpp
scraped_at: 2026-06-29
---

CapabilitiesBundled plugin guides

`llama-cpp` is de officiële externe provider-Plugin voor lokale GGUF-embeddings. Deze is eigenaar van de runtime-afhankelijkheid `node-llama-cpp` die wordt gebruikt door `memorySearch.provider: "local"`.

Installeer deze voordat je lokale geheugenembeddings gebruikt:

bashCopy code
[code]
    openclaw plugins install @openclaw/llama-cpp-provider
[/code]

Het hoofd-npm-pakket `openclaw` bevat `node-llama-cpp` niet. Door de native afhankelijkheid in deze Plugin te houden, wordt voorkomen dat normale OpenClaw npm-updates een handmatig geïnstalleerde runtime in de OpenClaw-pakketmap verwijderen.

## Configuratie

Stel de provider voor geheugenzoekopdrachten in op `local`:

json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        provider: "local",        local: {          modelPath: "hf:ggml-org/embeddinggemma-300m-qat-q8_0-GGUF/embeddinggemma-300m-qat-Q8_0.gguf",        },      },    },  },}
[/code]

Het standaardmodel is `embeddinggemma-300m-qat-Q8_0.gguf`. Je kunt `local.modelPath` ook laten verwijzen naar een lokaal `.gguf`-bestand.

## Native runtime

Gebruik Node 24 voor het soepelste native installatiepad. Source-checkouts die pnpm gebruiken, moeten mogelijk de native afhankelijkheid goedkeuren en opnieuw bouwen:

bashCopy code
[code]
    pnpm approve-buildspnpm rebuild node-llama-cpp
[/code]

Voor lokale embeddings met minder frictie kun je in plaats daarvan een lokale serviceprovider gebruiken, zoals Ollama of LM Studio.

Was this useful?YesNo

Open issue