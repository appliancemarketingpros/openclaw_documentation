---
title: OpenCode
source_url: https://docs.openclaw.ai/providers/opencode
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

OpenCode

# 

​

OpenCode

OpenCode exposes two hosted catalogs in OpenClaw:

  * `opencode/...` for the **Zen** catalog
  * `opencode-go/...` for the **Go** catalog

Both catalogs use the same OpenCode API key. OpenClaw keeps the runtime provider ids split so upstream per-model routing stays correct, but onboarding and docs treat them as one OpenCode setup.

## 

​

CLI setup

### 

​

Zen catalog

Copy
[code]
    openclaw onboard --auth-choice opencode-zen
    openclaw onboard --opencode-zen-api-key "$OPENCODE_API_KEY"
    
[/code]

### 

​

Go catalog

Copy
[code]
    openclaw onboard --auth-choice opencode-go
    openclaw onboard --opencode-go-api-key "$OPENCODE_API_KEY"
    
[/code]

## 

​

Config snippet

Copy
[code]
    {
      env: { OPENCODE_API_KEY: "sk-..." },
      agents: { defaults: { model: { primary: "opencode/claude-opus-4-6" } } },
    }
    
[/code]

## 

​

Catalogs

### 

​

Zen

  * Runtime provider: `opencode`
  * Example models: `opencode/claude-opus-4-6`, `opencode/gpt-5.2`, `opencode/gemini-3-pro`
  * Best when you want the curated OpenCode multi-model proxy


### 

​

Go

  * Runtime provider: `opencode-go`
  * Example models: `opencode-go/kimi-k2.5`, `opencode-go/glm-5`, `opencode-go/minimax-m2.5`
  * Best when you want the OpenCode-hosted Kimi/GLM/MiniMax lineup


## 

​

Notes

  * `OPENCODE_ZEN_API_KEY` is also supported.
  * Entering one OpenCode key during setup stores credentials for both runtime providers.
  * You sign in to OpenCode, add billing details, and copy your API key.
  * Billing and catalog availability are managed from the OpenCode dashboard.


[OpenCode Go](</providers/opencode-go>)[OpenRouter](</providers/openrouter>)

⌘I