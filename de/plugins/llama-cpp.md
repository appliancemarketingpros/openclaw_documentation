---
title: llama.cpp-Provider
source_url: https://docs.openclaw.ai/de/plugins/llama-cpp
scraped_at: 2026-06-29
---

CapabilitiesBundled plugin guides

`llama-cpp` ist das offizielle externe Provider-Plugin für lokale GGUF-Embeddings. Es besitzt die von `memorySearch.provider: "local"` verwendete `node-llama-cpp`-Runtime-Abhängigkeit.

Installieren Sie es, bevor Sie lokale Memory-Embeddings verwenden:

bashCopy code
[code]
    openclaw plugins install @openclaw/llama-cpp-provider
[/code]

Das Haupt-npm-Paket `openclaw` enthält `node-llama-cpp` nicht. Die native Abhängigkeit in diesem Plugin zu halten, verhindert, dass normale OpenClaw-npm-Updates eine manuell installierte Runtime im OpenClaw-Paketverzeichnis löschen.

## Konfiguration

Setzen Sie den Provider für die Memory-Suche auf `local`:

json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        provider: "local",        local: {          modelPath: "hf:ggml-org/embeddinggemma-300m-qat-q8_0-GGUF/embeddinggemma-300m-qat-Q8_0.gguf",        },      },    },  },}
[/code]

Das Standardmodell ist `embeddinggemma-300m-qat-Q8_0.gguf`. Sie können `local.modelPath` auch auf eine lokale `.gguf`-Datei verweisen lassen.

## Native Runtime

Verwenden Sie Node 24 für den reibungslosesten nativen Installationspfad. Source-Checkouts mit pnpm müssen die native Abhängigkeit möglicherweise genehmigen und neu bauen:

bashCopy code
[code]
    pnpm approve-buildspnpm rebuild node-llama-cpp
[/code]

Für lokale Embeddings mit weniger Aufwand verwenden Sie stattdessen einen lokalen Service-Provider wie Ollama oder LM Studio.

Was this useful?YesNo

Open issue