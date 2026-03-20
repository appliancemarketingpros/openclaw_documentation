---
title: Mistral
source_url: https://docs.openclaw.ai/providers/mistral
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

Mistral

# 

​

Mistral

OpenClaw supports Mistral for both text/image model routing (`mistral/...`) and audio transcription via Voxtral in media understanding. Mistral can also be used for memory embeddings (`memorySearch.provider = "mistral"`).

## 

​

CLI setup

Copy
[code]
    openclaw onboard --auth-choice mistral-api-key
    # or non-interactive
    openclaw onboard --mistral-api-key "$MISTRAL_API_KEY"
    
[/code]

## 

​

Config snippet (LLM provider)

Copy
[code]
    {
      env: { MISTRAL_API_KEY: "sk-..." },
      agents: { defaults: { model: { primary: "mistral/mistral-large-latest" } } },
    }
    
[/code]

## 

​

Config snippet (audio transcription with Voxtral)

Copy
[code]
    {
      tools: {
        media: {
          audio: {
            enabled: true,
            models: [{ provider: "mistral", model: "voxtral-mini-latest" }],
          },
        },
      },
    }
    
[/code]

## 

​

Notes

  * Mistral auth uses `MISTRAL_API_KEY`.
  * Provider base URL defaults to `https://api.mistral.ai/v1`.
  * Onboarding default model is `mistral/mistral-large-latest`.
  * Media-understanding default audio model for Mistral is `voxtral-mini-latest`.
  * Media transcription path uses `/v1/audio/transcriptions`.
  * Memory embeddings path uses `/v1/embeddings` (default model: `mistral-embed`).


[Moonshot AI](</providers/moonshot>)[NVIDIA](</providers/nvidia>)

⌘I