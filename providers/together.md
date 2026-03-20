---
title: Together AI
source_url: https://docs.openclaw.ai/providers/together
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

Together AI

# 

​

Together AI

The [Together AI](<https://together.ai>) provides access to leading open-source models including Llama, DeepSeek, Kimi, and more through a unified API.

  * Provider: `together`
  * Auth: `TOGETHER_API_KEY`
  * API: OpenAI-compatible


## 

​

Quick start

  1. Set the API key (recommended: store it for the Gateway):


Copy
[code]
    openclaw onboard --auth-choice together-api-key
    
[/code]

  2. Set a default model:


Copy
[code]
    {
      agents: {
        defaults: {
          model: { primary: "together/moonshotai/Kimi-K2.5" },
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
      --auth-choice together-api-key \
      --together-api-key "$TOGETHER_API_KEY"
    
[/code]

This will set `together/moonshotai/Kimi-K2.5` as the default model.

## 

​

Environment note

If the Gateway runs as a daemon (launchd/systemd), make sure `TOGETHER_API_KEY` is available to that process (for example, in `~/.openclaw/.env` or via `env.shellEnv`).

## 

​

Available models

Together AI provides access to many popular open-source models:

  * **GLM 4.7 Fp8** \- Default model with 200K context window
  * **Llama 3.3 70B Instruct Turbo** \- Fast, efficient instruction following
  * **Llama 4 Scout** \- Vision model with image understanding
  * **Llama 4 Maverick** \- Advanced vision and reasoning
  * **DeepSeek V3.1** \- Powerful coding and reasoning model
  * **DeepSeek R1** \- Advanced reasoning model
  * **Kimi K2 Instruct** \- High-performance model with 262K context window

All models support standard chat completions and are OpenAI API compatible.

[Synthetic](</providers/synthetic>)[Vercel AI Gateway](</providers/vercel-ai-gateway>)

⌘I