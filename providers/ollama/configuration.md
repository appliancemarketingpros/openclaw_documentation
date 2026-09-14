---
title: Ollama configuration
source_url: https://docs.openclaw.ai/providers/ollama/configuration
scraped_at: 2026-09-14
---

ModelsProviders

## Configuration

### Basic (implicit discovery)

bashCopy code
[code]
    export OLLAMA_API_KEY="ollama-local"
[/code]

### Explicit (manual models)

Use explicit config for hosted cloud setup, a non-default host/port, forced context windows, or fully manual model lists:

json5Copy code
[code]
    {  models: {    providers: {      ollama: {        baseUrl: "https://ollama.com",        apiKey: "OLLAMA_API_KEY",        api: "ollama",        models: [          {            id: "kimi-k2.5:cloud",            name: "kimi-k2.5:cloud",            reasoning: false,            input: ["text", "image"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 128000,            maxTokens: 8192          }        ]      }    }  }}
[/code]

### Custom base URL

This example uses a nonempty manual model list, so it skips discovery:

json5Copy code
[code]
    {  models: {    providers: {      ollama: {        apiKey: "ollama-local",        baseUrl: "http://ollama-host:11434", // No /v1 - native Ollama API URL        api: "ollama", // Explicit: guarantees native tool-calling behavior        timeoutSeconds: 300, // Optional: longer connect/stream budget for cold local models        models: [          {            id: "qwen3:32b",            name: "qwen3:32b",            params: {              keep_alive: "15m", // Optional: keep the model loaded between turns            },          },        ],      },    },  },}
[/code]

Was this useful?YesNo

Open issue