---
title: Vydra
source_url: https://docs.openclaw.ai/providers/vydra
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

Vydra

# 

​

Vydra

The bundled Vydra plugin adds:

  * image generation via `vydra/grok-imagine`
  * video generation via `vydra/veo3` and `vydra/kling`
  * speech synthesis via Vydra’s ElevenLabs-backed TTS route

OpenClaw uses the same `VYDRA_API_KEY` for all three capabilities.

## 

​

Important base URL

Use `https://www.vydra.ai/api/v1`. Vydra’s apex host (`https://vydra.ai/api/v1`) currently redirects to `www`. Some HTTP clients drop `Authorization` on that cross-host redirect, which turns a valid API key into a misleading auth failure. The bundled plugin uses the `www` base URL directly to avoid that.

## 

​

Setup

Interactive onboarding:
[code] 
    openclaw onboard --auth-choice vydra-api-key
    
[/code]

Or set the env var directly:
[code] 
    export VYDRA_API_KEY="vydra_live_..."
    
[/code]

## 

​

Image generation

Default image model:

  * `vydra/grok-imagine`

Set it as the default image provider:
[code] 
    {
      agents: {
        defaults: {
          imageGenerationModel: {
            primary: "vydra/grok-imagine",
          },
        },
      },
    }
    
[/code]

Current bundled support is text-to-image only. Vydra’s hosted edit routes expect remote image URLs, and OpenClaw does not add a Vydra-specific upload bridge in the bundled plugin yet. See [Image Generation](</tools/image-generation>) for shared tool behavior.

## 

​

Video generation

Registered video models:

  * `vydra/veo3` for text-to-video
  * `vydra/kling` for image-to-video

Set Vydra as the default video provider:
[code] 
    {
      agents: {
        defaults: {
          videoGenerationModel: {
            primary: "vydra/veo3",
          },
        },
      },
    }
    
[/code]

Notes:

  * `vydra/veo3` is bundled as text-to-video only.
  * `vydra/kling` currently requires a remote image URL reference. Local file uploads are rejected up front.
  * The bundled plugin stays conservative and does not forward undocumented style knobs such as aspect ratio, resolution, watermark, or generated audio.

See [Video Generation](</tools/video-generation>) for shared tool behavior.

## 

​

Speech synthesis

Set Vydra as the speech provider:
[code] 
    {
      messages: {
        tts: {
          provider: "vydra",
          providers: {
            vydra: {
              apiKey: "${VYDRA_API_KEY}",
              voiceId: "21m00Tcm4TlvDq8ikWAM",
            },
          },
        },
      },
    }
    
[/code]

Defaults:

  * model: `elevenlabs/tts`
  * voice id: `21m00Tcm4TlvDq8ikWAM`

The bundled plugin currently exposes one known-good default voice and returns MP3 audio files.

## 

​

Related

  * [Provider Directory](</providers/index>)
  * [Image Generation](</tools/image-generation>)
  * [Video Generation](</tools/video-generation>)


[Vercel AI Gateway](</providers/vercel-ai-gateway>)[vLLM](</providers/vllm>)

⌘I