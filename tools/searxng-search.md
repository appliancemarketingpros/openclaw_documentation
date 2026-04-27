---
title: SearXNG search
source_url: https://docs.openclaw.ai/tools/searxng-search
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

SearXNG search

OpenClaw supports [SearXNG](<https://docs.searxng.org/>) as a **self-hosted, key-free** `web_search` provider. SearXNG is an open-source meta-search engine that aggregates results from Google, Bing, DuckDuckGo, and other sources. Advantages:

  * **Free and unlimited** — no API key or commercial subscription required
  * **Privacy / air-gap** — queries never leave your network
  * **Works anywhere** — no region restrictions on commercial search APIs


## 

​

Setup

1

Run a SearXNG instance
[code]
    docker run -d -p 8888:8080 searxng/searxng
    
[/code]

Or use any existing SearXNG deployment you have access to. See the [SearXNG documentation](<https://docs.searxng.org/>) for production setup.

2

Configure
[code]
    openclaw configure --section web
    # Select "searxng" as the provider
    
[/code]

Or set the env var and let auto-detection find it:
[code]
    export SEARXNG_BASE_URL="http://localhost:8888"
    
[/code]

## 

​

Config
[code] 
    {
      tools: {
        web: {
          search: {
            provider: "searxng",
          },
        },
      },
    }
    
[/code]

Plugin-level settings for the SearXNG instance:
[code] 
    {
      plugins: {
        entries: {
          searxng: {
            config: {
              webSearch: {
                baseUrl: "http://localhost:8888",
                categories: "general,news", // optional
                language: "en", // optional
              },
            },
          },
        },
      },
    }
    
[/code]

The `baseUrl` field also accepts SecretRef objects. Transport rules:

  * `https://` works for public or private SearXNG hosts
  * `http://` is only accepted for trusted private-network or loopback hosts
  * public SearXNG hosts must use `https://`


## 

​

Environment variable

Set `SEARXNG_BASE_URL` as an alternative to config:
[code] 
    export SEARXNG_BASE_URL="http://localhost:8888"
    
[/code]

When `SEARXNG_BASE_URL` is set and no explicit provider is configured, auto-detection picks SearXNG automatically (at the lowest priority — any API-backed provider with a key wins first).

## 

​

Plugin config reference

Field| Description  
---|---  
`baseUrl`| Base URL of your SearXNG instance (required)  
`categories`| Comma-separated categories such as `general`, `news`, or `science`  
`language`| Language code for results such as `en`, `de`, or `fr`  
  
## 

​

Notes

  * **JSON API** — uses SearXNG’s native `format=json` endpoint, not HTML scraping
  * **No API key** — works with any SearXNG instance out of the box
  * **Base URL validation** — `baseUrl` must be a valid `http://` or `https://` URL; public hosts must use `https://`
  * **Auto-detection order** — SearXNG is checked last (order 200) in auto-detection. API-backed providers with configured keys run first, then DuckDuckGo (order 100), then Ollama Web Search (order 110)
  * **Self-hosted** — you control the instance, queries, and upstream search engines
  * **Categories** default to `general` when not configured


For SearXNG JSON API to work, make sure your SearXNG instance has the `json` format enabled in its `settings.yml` under `search.formats`.

## 

​

Related

  * [Web Search overview](</tools/web>) — all providers and auto-detection
  * [DuckDuckGo Search](</tools/duckduckgo-search>) — another key-free fallback
  * [Brave Search](</tools/brave-search>) — structured results with free tier


[Perplexity search](</tools/perplexity-search>)[Tavily](</tools/tavily>)

⌘I