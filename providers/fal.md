---
title: fal
source_url: https://docs.openclaw.ai/providers/fal
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

fal

# 

​

fal

OpenClaw ships a bundled `fal` provider for hosted image and video generation.

  * Provider: `fal`
  * Auth: `FAL_KEY` (canonical; `FAL_API_KEY` also works as a fallback)
  * API: fal model endpoints


## 

​

Quick start

  1. Set the API key:


[code] 
    openclaw onboard --auth-choice fal-api-key
    
[/code]

  2. Set a default image model:


[code] 
    {
      agents: {
        defaults: {
          imageGenerationModel: {
            primary: "fal/fal-ai/flux/dev",
          },
        },
      },
    }
    
[/code]

## 

​

Image generation

The bundled `fal` image-generation provider defaults to `fal/fal-ai/flux/dev`.

  * Generate: up to 4 images per request
  * Edit mode: enabled, 1 reference image
  * Supports `size`, `aspectRatio`, and `resolution`
  * Current edit caveat: the fal image edit endpoint does **not** support `aspectRatio` overrides

To use fal as the default image provider:
[code] 
    {
      agents: {
        defaults: {
          imageGenerationModel: {
            primary: "fal/fal-ai/flux/dev",
          },
        },
      },
    }
    
[/code]

## 

​

Video generation

The bundled `fal` video-generation provider defaults to `fal/fal-ai/minimax/video-01-live`.

  * Modes: text-to-video and single-image reference flows
  * Runtime: queue-backed submit/status/result flow for long-running jobs

To use fal as the default video provider:
[code] 
    {
      agents: {
        defaults: {
          videoGenerationModel: {
            primary: "fal/fal-ai/minimax/video-01-live",
          },
        },
      },
    }
    
[/code]

## 

​

Related

  * [Image Generation](</tools/image-generation>)
  * [Video Generation](</tools/video-generation>)
  * [Configuration Reference](</gateway/configuration-reference#agent-defaults>)


[Deepseek](</providers/deepseek>)[GitHub Copilot](</providers/github-copilot>)

⌘I