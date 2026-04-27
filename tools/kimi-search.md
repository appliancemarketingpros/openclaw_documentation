---
title: Kimi search
source_url: https://docs.openclaw.ai/tools/kimi-search
scraped_at: 2026-04-27
---

[OpenClaw home page](</>)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

⌘K

Search...

Navigation

Web tools

Kimi search

OpenClaw supports Kimi as a `web_search` provider, using Moonshot web search to produce AI-synthesized answers with citations.

## 

​

Get an API key

1

Create a key

Get an API key from [Moonshot AI](<https://platform.moonshot.cn/>).

2

Store the key

Set `KIMI_API_KEY` or `MOONSHOT_API_KEY` in the Gateway environment, or configure via:
[code]
    openclaw configure --section web
    
[/code]

When you choose **Kimi** during `openclaw onboard` or `openclaw configure --section web`, OpenClaw can also ask for:

  * the Moonshot API region:
    * `https://api.moonshot.ai/v1`
    * `https://api.moonshot.cn/v1`
  * the default Kimi web-search model (defaults to `kimi-k2.6`)


## 

​

Config
[code] 
    {
      plugins: {
        entries: {
          moonshot: {
            config: {
              webSearch: {
                apiKey: "sk-...", // optional if KIMI_API_KEY or MOONSHOT_API_KEY is set
                baseUrl: "https://api.moonshot.ai/v1",
                model: "kimi-k2.6",
              },
            },
          },
        },
      },
      tools: {
        web: {
          search: {
            provider: "kimi",
          },
        },
      },
    }
    
[/code]

If you use the China API host for chat (`models.providers.moonshot.baseUrl`: `https://api.moonshot.cn/v1`), OpenClaw reuses that same host for Kimi `web_search` when `tools.web.search.kimi.baseUrl` is omitted, so keys from [platform.moonshot.cn](<https://platform.moonshot.cn/>) do not hit the international endpoint by mistake (which often returns HTTP 401). Override with `tools.web.search.kimi.baseUrl` when you need a different search base URL. **Environment alternative:** set `KIMI_API_KEY` or `MOONSHOT_API_KEY` in the Gateway environment. For a gateway install, put it in `~/.openclaw/.env`. If you omit `baseUrl`, OpenClaw defaults to `https://api.moonshot.ai/v1`. If you omit `model`, OpenClaw defaults to `kimi-k2.6`.

## 

​

How it works

Kimi uses Moonshot web search to synthesize answers with inline citations, similar to Gemini and Grok’s grounded response approach.

## 

​

Supported parameters

Kimi search supports `query`. `count` is accepted for shared `web_search` compatibility, but Kimi still returns one synthesized answer with citations rather than an N-result list. Provider-specific filters are not currently supported.

## 

​

Related

  * [Web Search overview](</tools/web>) — all providers and auto-detection
  * [Moonshot AI](</providers/moonshot>) — Moonshot model + Kimi Coding provider docs
  * [Gemini Search](</tools/gemini-search>) — AI-synthesized answers via Google grounding
  * [Grok Search](</tools/grok-search>) — AI-synthesized answers via xAI grounding


[Grok search](</tools/grok-search>)[MiniMax search](</tools/minimax-search>)

⌘I