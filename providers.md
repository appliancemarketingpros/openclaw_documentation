---
title: Provider Directory
source_url: https://docs.openclaw.ai/providers
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

Provider Directory

# 

​

Model Providers

OpenClaw can use many LLM providers. Pick a provider, authenticate, then set the default model as `provider/model`. Looking for chat channel docs (WhatsApp/Telegram/Discord/Slack/Mattermost (plugin)/etc.)? See [Channels](</channels>).

## 

​

Quick start

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

Provider docs

  * [Amazon Bedrock](</providers/bedrock>)
  * [Anthropic (API + Claude Code CLI)](</providers/anthropic>)
  * [Cloudflare AI Gateway](</providers/cloudflare-ai-gateway>)
  * [GLM models](</providers/glm>)
  * [Google (Gemini)](</providers/google>)
  * [Groq (LPU inference)](</providers/groq>)
  * [Hugging Face (Inference)](</providers/huggingface>)
  * [Kilocode](</providers/kilocode>)
  * [LiteLLM (unified gateway)](</providers/litellm>)
  * [MiniMax](</providers/minimax>)
  * [Mistral](</providers/mistral>)
  * [Model Studio (Alibaba Cloud)](</providers/modelstudio>)
  * [Moonshot AI (Kimi + Kimi Coding)](</providers/moonshot>)
  * [NVIDIA](</providers/nvidia>)
  * [Ollama (cloud + local models)](</providers/ollama>)
  * [OpenAI (API + Codex)](</providers/openai>)
  * [OpenCode (Zen + Go)](</providers/opencode>)
  * [OpenRouter](</providers/openrouter>)
  * [Perplexity (web search)](</providers/perplexity-provider>)
  * [Qianfan](</providers/qianfan>)
  * [Qwen (OAuth)](</providers/qwen>)
  * [SGLang (local models)](</providers/sglang>)
  * [Together AI](</providers/together>)
  * [Vercel AI Gateway](</providers/vercel-ai-gateway>)
  * [Venice (Venice AI, privacy-focused)](</providers/venice>)
  * [vLLM (local models)](</providers/vllm>)
  * [Volcengine (Doubao)](</providers/volcengine>)
  * [xAI](</providers/xai>)
  * [Xiaomi](</providers/xiaomi>)
  * [Z.AI](</providers/zai>)


## 

​

Transcription providers

  * [Deepgram (audio transcription)](</providers/deepgram>)


## 

​

Community tools

  * [Claude Max API Proxy](</providers/claude-max-api-proxy>) \- Community proxy for Claude subscription credentials (verify Anthropic policy/terms before use)

For the full provider catalog (xAI, Groq, Mistral, etc.) and advanced configuration, see [Model providers](</concepts/model-providers>).

[Model Provider Quickstart](</providers/models>)

⌘I