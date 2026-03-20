---
title: Volcengine (Doubao)
source_url: https://docs.openclaw.ai/providers/volcengine
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

Volcengine (Doubao)

# 

​

Volcengine (Doubao)

The Volcengine provider gives access to Doubao models and third-party models hosted on Volcano Engine, with separate endpoints for general and coding workloads.

  * Providers: `volcengine` (general) + `volcengine-plan` (coding)
  * Auth: `VOLCANO_ENGINE_API_KEY`
  * API: OpenAI-compatible


## 

​

Quick start

  1. Set the API key:


Copy
[code]
    openclaw onboard --auth-choice volcengine-api-key
    
[/code]

  2. Set a default model:


Copy
[code]
    {
      agents: {
        defaults: {
          model: { primary: "volcengine-plan/ark-code-latest" },
        },
      },
    }
    
[/code]

## 

​

Non-interactive example

Copy
[code]
    openclaw onboard --non-interactive \
      --mode local \
      --auth-choice volcengine-api-key \
      --volcengine-api-key "$VOLCANO_ENGINE_API_KEY"
    
[/code]

## 

​

Providers and endpoints

Provider| Endpoint| Use case  
---|---|---  
`volcengine`| `ark.cn-beijing.volces.com/api/v3`| General models  
`volcengine-plan`| `ark.cn-beijing.volces.com/api/coding/v3`| Coding models  
  
Both providers are configured from a single API key. Setup registers both automatically.

## 

​

Available models

  * **doubao-seed-1-8** \- Doubao Seed 1.8 (general, default)
  * **doubao-seed-code-preview** \- Doubao coding model
  * **ark-code-latest** \- Coding plan default
  * **Kimi K2.5** \- Moonshot AI via Volcano Engine
  * **GLM-4.7** \- GLM via Volcano Engine
  * **DeepSeek V3.2** \- DeepSeek via Volcano Engine

Most models support text + image input. Context windows range from 128K to 256K tokens.

## 

​

Environment note

If the Gateway runs as a daemon (launchd/systemd), make sure `VOLCANO_ENGINE_API_KEY` is available to that process (for example, in `~/.openclaw/.env` or via `env.shellEnv`).

[vLLM](</providers/vllm>)[xAI](</providers/xai>)

⌘I