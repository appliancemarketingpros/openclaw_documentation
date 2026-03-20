---
title: GLM Models
source_url: https://docs.openclaw.ai/providers/glm
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

GLM Models

# 

​

GLM models

GLM is a **model family** (not a company) available through the Z.AI platform. In OpenClaw, GLM models are accessed via the `zai` provider and model IDs like `zai/glm-5`.

## 

​

CLI setup

Copy
[code]
    # Coding Plan Global, recommended for Coding Plan users
    openclaw onboard --auth-choice zai-coding-global
    
    # Coding Plan CN (China region), recommended for Coding Plan users
    openclaw onboard --auth-choice zai-coding-cn
    
    # General API
    openclaw onboard --auth-choice zai-global
    
    # General API CN (China region)
    openclaw onboard --auth-choice zai-cn
    
[/code]

## 

​

Config snippet

Copy
[code]
    {
      env: { ZAI_API_KEY: "sk-..." },
      agents: { defaults: { model: { primary: "zai/glm-5" } } },
    }
    
[/code]

## 

​

Notes

  * GLM versions and availability can change; check Z.AI’s docs for the latest.
  * Example model IDs include `glm-5`, `glm-4.7`, and `glm-4.6`.
  * For provider details, see [/providers/zai](</providers/zai>).


[LiteLLM](</providers/litellm>)[MiniMax](</providers/minimax>)

⌘I