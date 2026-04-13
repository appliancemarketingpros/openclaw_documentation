---
title: Arcee AI
source_url: https://docs.openclaw.ai/providers/arcee
scraped_at: 2026-04-13
---

[OpenClaw home page](</>)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

⌘K

Search...

Navigation

Providers

Arcee AI

# 

​

Arcee AI

[Arcee AI](<https://arcee.ai>) provides access to the Trinity family of mixture-of-experts models through an OpenAI-compatible API. All Trinity models are Apache 2.0 licensed. Arcee AI models can be accessed directly via the Arcee platform or through [OpenRouter](</providers/openrouter>).

Property| Value  
---|---  
Provider| `arcee`  
Auth| `ARCEEAI_API_KEY` (direct) or `OPENROUTER_API_KEY` (via OpenRouter)  
API| OpenAI-compatible  
Base URL| `https://api.arcee.ai/api/v1` (direct) or `https://openrouter.ai/api/v1` (OpenRouter)  
  
## 

​

Getting started

  * Direct (Arcee platform)

  * Via OpenRouter


1

Get an API key

Create an API key at [Arcee AI](<https://chat.arcee.ai/>).

2

Run onboarding
[code]
    openclaw onboard --auth-choice arceeai-api-key
    
[/code]

3

Set a default model
[code]
    {
      agents: {
        defaults: {
          model: { primary: "arcee/trinity-large-thinking" },
        },
      },
    }
    
[/code]

1

Get an API key

Create an API key at [OpenRouter](<https://openrouter.ai/keys>).

2

Run onboarding
[code]
    openclaw onboard --auth-choice arceeai-openrouter
    
[/code]

3

Set a default model
[code]
    {
      agents: {
        defaults: {
          model: { primary: "arcee/trinity-large-thinking" },
        },
      },
    }
    
[/code]

The same model refs work for both direct and OpenRouter setups (for example `arcee/trinity-large-thinking`).

## 

​

Non-interactive setup

  * Direct (Arcee platform)

  * Via OpenRouter


[code]
    openclaw onboard --non-interactive \
      --mode local \
      --auth-choice arceeai-api-key \
      --arceeai-api-key "$ARCEEAI_API_KEY"
    
[/code]
[code]
    openclaw onboard --non-interactive \
      --mode local \
      --auth-choice arceeai-openrouter \
      --openrouter-api-key "$OPENROUTER_API_KEY"
    
[/code]

## 

​

Built-in catalog

OpenClaw currently ships this bundled Arcee catalog:

Model ref| Name| Input| Context| Cost (in/out per 1M)| Notes  
---|---|---|---|---|---  
`arcee/trinity-large-thinking`| Trinity Large Thinking| text| 256K| 0.25/0.25 / 0.25/0.90| Default model; reasoning enabled  
`arcee/trinity-large-preview`| Trinity Large Preview| text| 128K| 0.25/0.25 / 0.25/1.00| General-purpose; 400B params, 13B active  
`arcee/trinity-mini`| Trinity Mini 26B| text| 128K| 0.045/0.045 / 0.045/0.15| Fast and cost-efficient; function calling  
  
The onboarding preset sets `arcee/trinity-large-thinking` as the default model.

## 

​

Supported features

Feature| Supported  
---|---  
Streaming| Yes  
Tool use / function calling| Yes  
Structured output (JSON mode and JSON schema)| Yes  
Extended thinking| Yes (Trinity Large Thinking)  
  
Environment note

If the Gateway runs as a daemon (launchd/systemd), make sure `ARCEEAI_API_KEY` (or `OPENROUTER_API_KEY`) is available to that process (for example, in `~/.openclaw/.env` or via `env.shellEnv`).

OpenRouter routing

When using Arcee models via OpenRouter, the same `arcee/*` model refs apply. OpenClaw handles routing transparently based on your auth choice. See the [OpenRouter provider docs](</providers/openrouter>) for OpenRouter-specific configuration details.

## 

​

Related

## OpenRouter

Access Arcee models and many others through a single API key.

## Model selection

Choosing providers, model refs, and failover behavior.

[Anthropic](</providers/anthropic>)[Chutes](</providers/chutes>)

⌘I