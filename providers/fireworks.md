---
title: Fireworks
source_url: https://docs.openclaw.ai/providers/fireworks
scraped_at: 2026-04-06
---

[OpenClaw home page](</>)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

⌘K

Search...

Navigation

# 

​

Fireworks

[Fireworks](<https://fireworks.ai>) exposes open-weight and routed models through an OpenAI-compatible API. OpenClaw now includes a bundled Fireworks provider plugin.

  * Provider: `fireworks`
  * Auth: `FIREWORKS_API_KEY`
  * API: OpenAI-compatible chat/completions
  * Base URL: `https://api.fireworks.ai/inference/v1`
  * Default model: `fireworks/accounts/fireworks/routers/kimi-k2p5-turbo`


## 

​

Quick start

Set up Fireworks auth through onboarding:
[code] 
    openclaw onboard --auth-choice fireworks-api-key
    
[/code]

This stores your Fireworks key in OpenClaw config and sets the Fire Pass starter model as the default.

## 

​

Non-interactive example
[code] 
    openclaw onboard --non-interactive \
      --mode local \
      --auth-choice fireworks-api-key \
      --fireworks-api-key "$FIREWORKS_API_KEY" \
      --skip-health \
      --accept-risk
    
[/code]

## 

​

Environment note

If the Gateway runs outside your interactive shell, make sure `FIREWORKS_API_KEY` is available to that process too. A key sitting only in `~/.profile` will not help a launchd/systemd daemon unless that environment is imported there as well.

## 

​

Built-in catalog

Model ref| Name| Input| Context| Max output| Notes  
---|---|---|---|---|---  
`fireworks/accounts/fireworks/routers/kimi-k2p5-turbo`| Kimi K2.5 Turbo (Fire Pass)| text,image| 256,000| 256,000| Default bundled starter model on Fireworks  
  
## 

​

Custom Fireworks model ids

OpenClaw accepts dynamic Fireworks model ids too. Use the exact model or router id shown by Fireworks and prefix it with `fireworks/`. Example:
[code] 
    {
      agents: {
        defaults: {
          model: {
            primary: "fireworks/accounts/fireworks/routers/kimi-k2p5-turbo",
          },
        },
      },
    }
    
[/code]

If Fireworks publishes a newer model such as a fresh Qwen or Gemma release, you can switch to it directly by using its Fireworks model id without waiting for a bundled catalog update.

⌘I