---
title: Runway
source_url: https://docs.openclaw.ai/providers/runway
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

Runway

# 

​

Runway

OpenClaw ships a bundled `runway` provider for hosted video generation.

  * Provider id: `runway`
  * Auth: `RUNWAYML_API_SECRET` (canonical) or `RUNWAY_API_KEY`
  * API: Runway task-based video generation (`GET /v1/tasks/{id}` polling)


## 

​

Quick start

  1. Set the API key:


[code] 
    openclaw onboard --auth-choice runway-api-key
    
[/code]

  2. Set Runway as the default video provider:


[code] 
    openclaw config set agents.defaults.videoGenerationModel.primary "runway/gen4.5"
    
[/code]

  3. Ask the agent to generate a video. Runway will be used automatically.


## 

​

Supported modes

Mode| Model| Reference input  
---|---|---  
Text-to-video| `gen4.5` (default)| None  
Image-to-video| `gen4.5`| 1 local or remote image  
Video-to-video| `gen4_aleph`| 1 local or remote video  
  
  * Local image and video references are supported via data URIs.
  * Video-to-video currently requires `runway/gen4_aleph` specifically.
  * Text-only runs currently expose `16:9` and `9:16` aspect ratios.


## 

​

Configuration
[code] 
    {
      agents: {
        defaults: {
          videoGenerationModel: {
            primary: "runway/gen4.5",
          },
        },
      },
    }
    
[/code]

## 

​

Related

  * [Video Generation](</tools/video-generation>) — shared tool parameters, provider selection, and async behavior
  * [Configuration Reference](</gateway/configuration-reference#agent-defaults>)


[Qwen](</providers/qwen>)[SGLang](</providers/sglang>)

⌘I