---
title: Alibaba Model Studio
source_url: https://docs.openclaw.ai/providers/alibaba
scraped_at: 2026-04-06
---

[OpenClaw home page](</>)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

⌘K

Search...

Navigation

Providers

Alibaba Model Studio

# 

​

Alibaba Model Studio

OpenClaw ships a bundled `alibaba` video-generation provider for Wan models on Alibaba Model Studio / DashScope.

  * Provider: `alibaba`
  * Preferred auth: `MODELSTUDIO_API_KEY`
  * Also accepted: `DASHSCOPE_API_KEY`, `QWEN_API_KEY`
  * API: DashScope / Model Studio async video generation


## 

​

Quick start

  1. Set an API key:


[code] 
    openclaw onboard --auth-choice qwen-standard-api-key
    
[/code]

  2. Set a default video model:


[code] 
    {
      agents: {
        defaults: {
          videoGenerationModel: {
            primary: "alibaba/wan2.6-t2v",
          },
        },
      },
    }
    
[/code]

## 

​

Built-in Wan models

The bundled `alibaba` provider currently registers:

  * `alibaba/wan2.6-t2v`
  * `alibaba/wan2.6-i2v`
  * `alibaba/wan2.6-r2v`
  * `alibaba/wan2.6-r2v-flash`
  * `alibaba/wan2.7-r2v`


## 

​

Current limits

  * Up to **1** output video per request
  * Up to **1** input image
  * Up to **4** input videos
  * Up to **10 seconds** duration
  * Supports `size`, `aspectRatio`, `resolution`, `audio`, and `watermark`
  * Reference image/video mode currently requires **remote http(s) URLs**


## 

​

Relationship to Qwen

The bundled `qwen` provider also uses Alibaba-hosted DashScope endpoints for Wan video generation. Use:

  * `qwen/...` when you want the canonical Qwen provider surface
  * `alibaba/...` when you want the direct vendor-owned Wan video surface


## 

​

Related

  * [Video Generation](</tools/video-generation>)
  * [Qwen](</providers/qwen>)
  * [Configuration Reference](</gateway/configuration-reference#agent-defaults>)


[Model Failover](</concepts/model-failover>)[Anthropic](</providers/anthropic>)

⌘I