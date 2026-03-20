---
title: OpenCode Go
source_url: https://docs.openclaw.ai/providers/opencode-go
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

OpenCode Go

# 

​

OpenCode Go

OpenCode Go is the Go catalog within [OpenCode](</providers/opencode>). It uses the same `OPENCODE_API_KEY` as the Zen catalog, but keeps the runtime provider id `opencode-go` so upstream per-model routing stays correct.

## 

​

Supported models

  * `opencode-go/kimi-k2.5`
  * `opencode-go/glm-5`
  * `opencode-go/minimax-m2.5`


## 

​

CLI setup

Copy
[code]
    openclaw onboard --auth-choice opencode-go
    # or non-interactive
    openclaw onboard --opencode-go-api-key "$OPENCODE_API_KEY"
    
[/code]

## 

​

Config snippet

Copy
[code]
    {
      env: { OPENCODE_API_KEY: "YOUR_API_KEY_HERE" }, // pragma: allowlist secret
      agents: { defaults: { model: { primary: "opencode-go/kimi-k2.5" } } },
    }
    
[/code]

## 

​

Routing behavior

OpenClaw handles per-model routing automatically when the model ref uses `opencode-go/...`.

## 

​

Notes

  * Use [OpenCode](</providers/opencode>) for the shared onboarding and catalog overview.
  * Runtime refs stay explicit: `opencode/...` for Zen, `opencode-go/...` for Go.


[OpenAI](</providers/openai>)[OpenCode](</providers/opencode>)

⌘I