---
title: llama.cpp Provider
source_url: https://docs.openclaw.ai/plugins/llama-cpp
scraped_at: 2026-06-15
---

CapabilitiesBundled plugin guides

`llama-cpp` is the official external provider plugin for local GGUF embeddings. It owns the `node-llama-cpp` runtime dependency used by `memorySearch.provider: "local"`.

Install it before using local memory embeddings:

bashCopy code
[code]
    openclaw plugins install @openclaw/llama-cpp-provider
[/code]

The main `openclaw` npm package does not include `node-llama-cpp`. Keeping the native dependency in this plugin prevents normal OpenClaw npm updates from deleting a manually installed runtime inside the OpenClaw package directory.

## Configuration

Set the memory search provider to `local`:

json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        provider: "local",        local: {          modelPath: "hf:ggml-org/embeddinggemma-300m-qat-q8_0-GGUF/embeddinggemma-300m-qat-Q8_0.gguf",        },      },    },  },}
[/code]

The default model is `embeddinggemma-300m-qat-Q8_0.gguf`. You can also point `local.modelPath` at a local `.gguf` file.

## Native Runtime

Use Node 24 for the smoothest native install path. Source checkouts using pnpm may need to approve and rebuild the native dependency:

bashCopy code
[code]
    pnpm approve-buildspnpm rebuild node-llama-cpp
[/code]

For lower-friction local embeddings, use a local service provider such as Ollama or LM Studio instead.

Was this useful?YesNo

Open issue