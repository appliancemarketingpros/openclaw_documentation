---
title: Kilo Gateway
source_url: https://docs.openclaw.ai/providers/kilocode
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

Kilo Gateway

# 

​

Kilo Gateway

Kilo Gateway provides a **unified API** that routes requests to many models behind a single endpoint and API key. It is OpenAI-compatible, so most OpenAI SDKs work by switching the base URL.

## 

​

Getting an API key

  1. Go to [app.kilo.ai](<https://app.kilo.ai>)
  2. Sign in or create an account
  3. Navigate to API Keys and generate a new key


## 

​

CLI setup

Copy
[code]
    openclaw onboard --kilocode-api-key <key>
    
[/code]

Or set the environment variable:

Copy
[code]
    export KILOCODE_API_KEY="<your-kilocode-api-key>" # pragma: allowlist secret
    
[/code]

## 

​

Config snippet

Copy
[code]
    {
      env: { KILOCODE_API_KEY: "<your-kilocode-api-key>" }, // pragma: allowlist secret
      agents: {
        defaults: {
          model: { primary: "kilocode/kilo/auto" },
        },
      },
    }
    
[/code]

## 

​

Default model

The default model is `kilocode/kilo/auto`, a smart routing model that automatically selects the best underlying model based on the task:

  * Planning, debugging, and orchestration tasks route to Claude Opus
  * Code writing and exploration tasks route to Claude Sonnet


## 

​

Available models

OpenClaw dynamically discovers available models from the Kilo Gateway at startup. Use `/models kilocode` to see the full list of models available with your account. Any model available on the gateway can be used with the `kilocode/` prefix:

Copy
[code]
    kilocode/kilo/auto              (default - smart routing)
    kilocode/anthropic/claude-sonnet-4
    kilocode/openai/gpt-5.2
    kilocode/google/gemini-3-pro-preview
    ...and many more
    
[/code]

## 

​

Notes

  * Model refs are `kilocode/<model-id>` (e.g., `kilocode/anthropic/claude-sonnet-4`).
  * Default model: `kilocode/kilo/auto`
  * Base URL: `https://api.kilo.ai/api/gateway/`
  * For more model/provider options, see [/concepts/model-providers](</concepts/model-providers>).
  * Kilo Gateway uses a Bearer token with your API key under the hood.


[Hugging Face (Inference)](</providers/huggingface>)[LiteLLM](</providers/litellm>)

⌘I