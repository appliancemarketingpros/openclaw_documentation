---
title: Google (Gemini)
source_url: https://docs.openclaw.ai/providers/google
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

Google (Gemini)

# 

​

Google (Gemini)

The Google plugin provides access to Gemini models through Google AI Studio, plus image generation, media understanding (image/audio/video), and web search via Gemini Grounding.

  * Provider: `google`
  * Auth: `GEMINI_API_KEY` or `GOOGLE_API_KEY`
  * API: Google Gemini API
  * Alternative provider: `google-gemini-cli` (OAuth)


## 

​

Quick start

  1. Set the API key:


Copy
[code]
    openclaw onboard --auth-choice google-api-key
    
[/code]

  2. Set a default model:


Copy
[code]
    {
      agents: {
        defaults: {
          model: { primary: "google/gemini-3.1-pro-preview" },
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
      --auth-choice google-api-key \
      --gemini-api-key "$GEMINI_API_KEY"
    
[/code]

## 

​

OAuth (Gemini CLI)

An alternative provider `google-gemini-cli` uses PKCE OAuth instead of an API key. This is an unofficial integration; some users report account restrictions. Use at your own risk. Environment variables:

  * `OPENCLAW_GEMINI_OAUTH_CLIENT_ID`
  * `OPENCLAW_GEMINI_OAUTH_CLIENT_SECRET`

(Or the `GEMINI_CLI_*` variants.)

## 

​

Capabilities

Capability| Supported  
---|---  
Chat completions| Yes  
Image generation| Yes  
Image understanding| Yes  
Audio transcription| Yes  
Video understanding| Yes  
Web search (Grounding)| Yes  
Thinking/reasoning| Yes (Gemini 3.1+)  
  
## 

​

Environment note

If the Gateway runs as a daemon (launchd/systemd), make sure `GEMINI_API_KEY` is available to that process (for example, in `~/.openclaw/.env` or via `env.shellEnv`).

[GitHub Copilot](</providers/github-copilot>)[Groq](</providers/groq>)

⌘I