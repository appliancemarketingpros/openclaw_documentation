---
title: SGLang
source_url: https://docs.openclaw.ai/providers/sglang
scraped_at: 2026-03-20
---

[OpenClaw home page](</>)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

⌘K

Search...

Navigation

Providers

SGLang

# 

​

SGLang

SGLang can serve open-source models via an **OpenAI-compatible** HTTP API. OpenClaw can connect to SGLang using the `openai-completions` API. OpenClaw can also **auto-discover** available models from SGLang when you opt in with `SGLANG_API_KEY` (any value works if your server does not enforce auth) and you do not define an explicit `models.providers.sglang` entry.

## 

​

Quick start

  1. Start SGLang with an OpenAI-compatible server.

Your base URL should expose `/v1` endpoints (for example `/v1/models`, `/v1/chat/completions`). SGLang commonly runs on:

  * `http://127.0.0.1:30000/v1`


  2. Opt in (any value works if no auth is configured):


Copy
[code]
    export SGLANG_API_KEY="sglang-local"
    
[/code]

  3. Run onboarding and choose `SGLang`, or set a model directly:


Copy
[code]
    openclaw onboard
    
[/code]

Copy
[code]
    {
      agents: {
        defaults: {
          model: { primary: "sglang/your-model-id" },
        },
      },
    }
    
[/code]

## 

​

Model discovery (implicit provider)

When `SGLANG_API_KEY` is set (or an auth profile exists) and you **do not** define `models.providers.sglang`, OpenClaw will query:

  * `GET http://127.0.0.1:30000/v1/models`

and convert the returned IDs into model entries. If you set `models.providers.sglang` explicitly, auto-discovery is skipped and you must define models manually.

## 

​

Explicit configuration (manual models)

Use explicit config when:

  * SGLang runs on a different host/port.
  * You want to pin `contextWindow`/`maxTokens` values.
  * Your server requires a real API key (or you want to control headers).


Copy
[code]
    {
      models: {
        providers: {
          sglang: {
            baseUrl: "http://127.0.0.1:30000/v1",
            apiKey: "${SGLANG_API_KEY}",
            api: "openai-completions",
            models: [
              {
                id: "your-model-id",
                name: "Local SGLang Model",
                reasoning: false,
                input: ["text"],
                cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },
                contextWindow: 128000,
                maxTokens: 8192,
              },
            ],
          },
        },
      },
    }
    
[/code]

## 

​

Troubleshooting

  * Check the server is reachable:


Copy
[code]
    curl http://127.0.0.1:30000/v1/models
    
[/code]

  * If requests fail with auth errors, set a real `SGLANG_API_KEY` that matches your server configuration, or configure the provider explicitly under `models.providers.sglang`.


[Qwen](</providers/qwen>)[Synthetic](</providers/synthetic>)

⌘I