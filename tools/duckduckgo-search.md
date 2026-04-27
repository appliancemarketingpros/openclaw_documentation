---
title: DuckDuckGo search
source_url: https://docs.openclaw.ai/tools/duckduckgo-search
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

DuckDuckGo search

OpenClaw supports DuckDuckGo as a **key-free** `web_search` provider. No API key or account is required.

DuckDuckGo is an **experimental, unofficial** integration that pulls results from DuckDuckGo’s non-JavaScript search pages — not an official API. Expect occasional breakage from bot-challenge pages or HTML changes.

## 

​

Setup

No API key needed — just set DuckDuckGo as your provider:

1

Configure
[code]
    openclaw configure --section web
    # Select "duckduckgo" as the provider
    
[/code]

## 

​

Config
[code] 
    {
      tools: {
        web: {
          search: {
            provider: "duckduckgo",
          },
        },
      },
    }
    
[/code]

Optional plugin-level settings for region and SafeSearch:
[code] 
    {
      plugins: {
        entries: {
          duckduckgo: {
            config: {
              webSearch: {
                region: "us-en", // DuckDuckGo region code
                safeSearch: "moderate", // "strict", "moderate", or "off"
              },
            },
          },
        },
      },
    }
    
[/code]

## 

​

Tool parameters

​

query

string

required

Search query.

​

count

number

default:"5"

Results to return (1–10).

​

region

string

DuckDuckGo region code (e.g. `us-en`, `uk-en`, `de-de`).

​

safeSearch

'strict' | 'moderate' | 'off'

default:"moderate"

SafeSearch level.

Region and SafeSearch can also be set in plugin config (see above) — tool parameters override config values per-query.

## 

​

Notes

  * **No API key** — works out of the box, zero configuration
  * **Experimental** — gathers results from DuckDuckGo’s non-JavaScript HTML search pages, not an official API or SDK
  * **Bot-challenge risk** — DuckDuckGo may serve CAPTCHAs or block requests under heavy or automated use
  * **HTML parsing** — results depend on page structure, which can change without notice
  * **Auto-detection order** — DuckDuckGo is the first key-free fallback (order 100) in auto-detection. API-backed providers with configured keys run first, then Ollama Web Search (order 110), then SearXNG (order 200)
  * **SafeSearch defaults to moderate** when not configured


For production use, consider [Brave Search](</tools/brave-search>) (free tier available) or another API-backed provider.

## 

​

Related

  * [Web Search overview](</tools/web>) — all providers and auto-detection
  * [Brave Search](</tools/brave-search>) — structured results with free tier
  * [Exa Search](</tools/exa-search>) — neural search with content extraction


[Brave search](</tools/brave-search>)[Exa search](</tools/exa-search>)

⌘I