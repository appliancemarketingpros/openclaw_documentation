---
title: Vercel AI Gateway
source_url: https://docs.openclaw.ai/providers/vercel-ai-gateway
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

Vercel AI Gateway

# 

​

Vercel AI Gateway

The [Vercel AI Gateway](<https://vercel.com/ai-gateway>) provides a unified API to access hundreds of models through a single endpoint.

  * Provider: `vercel-ai-gateway`
  * Auth: `AI_GATEWAY_API_KEY`
  * API: Anthropic Messages compatible
  * OpenClaw auto-discovers the Gateway `/v1/models` catalog, so `/models vercel-ai-gateway` includes current model refs such as `vercel-ai-gateway/openai/gpt-5.4`.


## 

​

Quick start

  1. Set the API key (recommended: store it for the Gateway):


Copy
[code]
    openclaw onboard --auth-choice ai-gateway-api-key
    
[/code]

  2. Set a default model:


Copy
[code]
    {
      agents: {
        defaults: {
          model: { primary: "vercel-ai-gateway/anthropic/claude-opus-4.6" },
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
      --auth-choice ai-gateway-api-key \
      --ai-gateway-api-key "$AI_GATEWAY_API_KEY"
    
[/code]

## 

​

Environment note

If the Gateway runs as a daemon (launchd/systemd), make sure `AI_GATEWAY_API_KEY` is available to that process (for example, in `~/.openclaw/.env` or via `env.shellEnv`).

## 

​

Model ID shorthand

OpenClaw accepts Vercel Claude shorthand model refs and normalizes them at runtime:

  * `vercel-ai-gateway/claude-opus-4.6` -> `vercel-ai-gateway/anthropic/claude-opus-4.6`
  * `vercel-ai-gateway/opus-4.6` -> `vercel-ai-gateway/anthropic/claude-opus-4-6`


[Together AI](</providers/together>)[Venice AI](</providers/venice>)

⌘I