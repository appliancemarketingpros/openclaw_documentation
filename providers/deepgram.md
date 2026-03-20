---
title: Deepgram
source_url: https://docs.openclaw.ai/providers/deepgram
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

Deepgram

# 

​

Deepgram (Audio Transcription)

Deepgram is a speech-to-text API. In OpenClaw it is used for **inbound audio/voice note transcription** via `tools.media.audio`. When enabled, OpenClaw uploads the audio file to Deepgram and injects the transcript into the reply pipeline (`{{Transcript}}` \+ `[Audio]` block). This is **not streaming** ; it uses the pre-recorded transcription endpoint. Website: <https://deepgram.com>  
Docs: <https://developers.deepgram.com>

## 

​

Quick start

  1. Set your API key:


Copy
[code]
    DEEPGRAM_API_KEY=dg_...
    
[/code]

  2. Enable the provider:


Copy
[code]
    {
      tools: {
        media: {
          audio: {
            enabled: true,
            models: [{ provider: "deepgram", model: "nova-3" }],
          },
        },
      },
    }
    
[/code]

## 

​

Options

  * `model`: Deepgram model id (default: `nova-3`)
  * `language`: language hint (optional)
  * `tools.media.audio.providerOptions.deepgram.detect_language`: enable language detection (optional)
  * `tools.media.audio.providerOptions.deepgram.punctuate`: enable punctuation (optional)
  * `tools.media.audio.providerOptions.deepgram.smart_format`: enable smart formatting (optional)

Example with language:

Copy
[code]
    {
      tools: {
        media: {
          audio: {
            enabled: true,
            models: [{ provider: "deepgram", model: "nova-3", language: "en" }],
          },
        },
      },
    }
    
[/code]

Example with Deepgram options:

Copy
[code]
    {
      tools: {
        media: {
          audio: {
            enabled: true,
            providerOptions: {
              deepgram: {
                detect_language: true,
                punctuate: true,
                smart_format: true,
              },
            },
            models: [{ provider: "deepgram", model: "nova-3" }],
          },
        },
      },
    }
    
[/code]

## 

​

Notes

  * Authentication follows the standard provider auth order; `DEEPGRAM_API_KEY` is the simplest path.
  * Override endpoints or headers with `tools.media.audio.baseUrl` and `tools.media.audio.headers` when using a proxy.
  * Output follows the same audio rules as other providers (size caps, timeouts, transcript injection).


[Claude Max API Proxy](</providers/claude-max-api-proxy>)[GitHub Copilot](</providers/github-copilot>)

⌘I