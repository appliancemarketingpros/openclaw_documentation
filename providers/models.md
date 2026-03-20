---
title: Model Provider Quickstart
source_url: https://docs.openclaw.ai/providers/models
scraped_at: 2026-03-20
---

[OpenClaw home page](</>)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

⌘K

Search...

Navigation

Overview

Model Provider Quickstart

# 

​

Model Providers

OpenClaw can use many LLM providers. Pick one, authenticate, then set the default model as `provider/model`.

## 

​

Quick start (two steps)

  1. Authenticate with the provider (usually via `openclaw onboard`).
  2. Set the default model:


Copy
[code]
    {
      agents: { defaults: { model: { primary: "anthropic/claude-opus-4-6" } } },
    }
    
[/code]

## 

​

Supported providers (starter set)

  * [OpenAI (API + Codex)](</providers/openai>)
  * [Anthropic (API + Claude Code CLI)](</providers/anthropic>)
  * [OpenRouter](</providers/openrouter>)
  * [Vercel AI Gateway](</providers/vercel-ai-gateway>)
  * [Cloudflare AI Gateway](</providers/cloudflare-ai-gateway>)
  * [Moonshot AI (Kimi + Kimi Coding)](</providers/moonshot>)
  * [Mistral](</providers/mistral>)
  * [Synthetic](</providers/synthetic>)
  * [OpenCode (Zen + Go)](</providers/opencode>)
  * [Z.AI](</providers/zai>)
  * [GLM models](</providers/glm>)
  * [MiniMax](</providers/minimax>)
  * [Venice (Venice AI)](</providers/venice>)
  * [Amazon Bedrock](</providers/bedrock>)
  * [Qianfan](</providers/qianfan>)
  * [xAI](</providers/xai>)

For the full provider catalog (xAI, Groq, Mistral, etc.) and advanced configuration, see [Model providers](</concepts/model-providers>).

[Provider Directory](</providers>)[Models CLI](</concepts/models>)

⌘I