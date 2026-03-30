---
title: Deepseek
source_url: https://docs.openclaw.ai/providers/deepseek
scraped_at: 2026-03-30
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

DeepSeek

[DeepSeek](<https://www.deepseek.com>) provides powerful AI models with an OpenAI-compatible API.

  * Provider: `deepseek`
  * Auth: `DEEPSEEK_API_KEY`
  * API: OpenAI-compatible


## 

​

Quick start

Set the API key (recommended: store it for the Gateway):
[code] 
    openclaw onboard --auth-choice deepseek-api-key
    
[/code]

This will prompt for your API key and set `deepseek/deepseek-chat` as the default model.

## 

​

Non-interactive example
[code] 
    openclaw onboard --non-interactive \
      --mode local \
      --auth-choice deepseek-api-key \
      --deepseek-api-key "$DEEPSEEK_API_KEY" \
      --skip-health \
      --accept-risk
    
[/code]

## 

​

Environment note

If the Gateway runs as a daemon (launchd/systemd), make sure `DEEPSEEK_API_KEY` is available to that process (for example, in `~/.openclaw/.env` or via `env.shellEnv`).

## 

​

Available models

Model ID| Name| Type| Context  
---|---|---|---  
`deepseek-chat`| DeepSeek Chat (V3.2)| General| 128K  
`deepseek-reasoner`| DeepSeek Reasoner (V3.2)| Reasoning| 128K  
  
  * **deepseek-chat** corresponds to DeepSeek-V3.2 in non-thinking mode.
  * **deepseek-reasoner** corresponds to DeepSeek-V3.2 in thinking mode with chain-of-thought reasoning.

Get your API key at [platform.deepseek.com](<https://platform.deepseek.com/api_keys>).

[Deepgram](</providers/deepgram>)[GitHub Copilot](</providers/github-copilot>)

⌘I