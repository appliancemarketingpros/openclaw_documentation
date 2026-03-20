---
title: OpenRouter
source_url: https://docs.openclaw.ai/providers/openrouter
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

OpenRouter

# 

​

OpenRouter

OpenRouter provides a **unified API** that routes requests to many models behind a single endpoint and API key. It is OpenAI-compatible, so most OpenAI SDKs work by switching the base URL.

## 

​

CLI setup

Copy
[code]
    openclaw onboard --auth-choice apiKey --token-provider openrouter --token "$OPENROUTER_API_KEY"
    
[/code]

## 

​

Config snippet

Copy
[code]
    {
      env: { OPENROUTER_API_KEY: "sk-or-..." },
      agents: {
        defaults: {
          model: { primary: "openrouter/anthropic/claude-sonnet-4-6" },
        },
      },
    }
    
[/code]

## 

​

Notes

  * Model refs are `openrouter/<provider>/<model>`.
  * For more model/provider options, see [/concepts/model-providers](</concepts/model-providers>).
  * OpenRouter uses a Bearer token with your API key under the hood.


[OpenCode](</providers/opencode>)[Perplexity (Provider)](</providers/perplexity-provider>)

⌘I