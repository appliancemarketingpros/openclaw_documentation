---
title: Qwen / Model Studio
source_url: https://docs.openclaw.ai/providers/qwen_modelstudio
scraped_at: 2026-03-30
---

[OpenClaw home page](</>)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

⌘K

Search...

Navigation

Providers

Qwen / Model Studio

# 

​

Qwen / Model Studio (Alibaba Cloud)

The Model Studio provider gives access to Alibaba Cloud models including Qwen and third-party models hosted on the platform. Two billing plans are supported: **Standard** (pay-as-you-go) and **Coding Plan** (subscription).

  * Provider: `modelstudio`
  * Auth: `MODELSTUDIO_API_KEY`
  * API: OpenAI-compatible


## 

​

Quick start

### 

​

Standard (pay-as-you-go)
[code] 
    # China endpoint
    openclaw onboard --auth-choice modelstudio-standard-api-key-cn
    
    # Global/Intl endpoint
    openclaw onboard --auth-choice modelstudio-standard-api-key
    
[/code]

### 

​

Coding Plan (subscription)
[code] 
    # China endpoint
    openclaw onboard --auth-choice modelstudio-api-key-cn
    
    # Global/Intl endpoint
    openclaw onboard --auth-choice modelstudio-api-key
    
[/code]

After onboarding, set a default model:
[code] 
    {
      agents: {
        defaults: {
          model: { primary: "modelstudio/qwen3.5-plus" },
        },
      },
    }
    
[/code]

## 

​

Plan types and endpoints

Plan| Region| Auth choice| Endpoint  
---|---|---|---  
Standard (pay-as-you-go)| China| `modelstudio-standard-api-key-cn`| `dashscope.aliyuncs.com/compatible-mode/v1`  
Standard (pay-as-you-go)| Global| `modelstudio-standard-api-key`| `dashscope-intl.aliyuncs.com/compatible-mode/v1`  
Coding Plan (subscription)| China| `modelstudio-api-key-cn`| `coding.dashscope.aliyuncs.com/v1`  
Coding Plan (subscription)| Global| `modelstudio-api-key`| `coding-intl.dashscope.aliyuncs.com/v1`  
  
The provider auto-selects the endpoint based on your auth choice. You can override with a custom `baseUrl` in config.

## 

​

Get your API key

  * **China** : [bailian.console.aliyun.com](<https://bailian.console.aliyun.com/>)
  * **Global/Intl** : [modelstudio.console.alibabacloud.com](<https://modelstudio.console.alibabacloud.com/>)


## 

​

Available models

  * **qwen3.5-plus** (default) — Qwen 3.5 Plus
  * **qwen3-coder-plus** , **qwen3-coder-next** — Qwen coding models
  * **GLM-5** — GLM models via Alibaba
  * **Kimi K2.5** — Moonshot AI via Alibaba
  * **MiniMax-M2.7** — MiniMax via Alibaba

Some models (qwen3.5-plus, kimi-k2.5) support image input. Context windows range from 200K to 1M tokens.

## 

​

Environment note

If the Gateway runs as a daemon (launchd/systemd), make sure `MODELSTUDIO_API_KEY` is available to that process (for example, in `~/.openclaw/.env` or via `env.shellEnv`).

[Qianfan](</providers/qianfan>)[Qwen](</providers/qwen>)

⌘I