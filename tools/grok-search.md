---
title: Grok search
source_url: https://docs.openclaw.ai/tools/grok-search
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

Grok search

OpenClaw supports Grok as a `web_search` provider, using xAI web-grounded responses to produce AI-synthesized answers backed by live search results with citations. The same `XAI_API_KEY` can also power the built-in `x_search` tool for X (formerly Twitter) post search. If you store the key under `plugins.entries.xai.config.webSearch.apiKey`, OpenClaw now reuses it as a fallback for the bundled xAI model provider too. For post-level X metrics such as reposts, replies, bookmarks, or views, prefer `x_search` with the exact post URL or status ID instead of a broad search query.

## 

​

Onboarding and configure

If you choose **Grok** during:

  * `openclaw onboard`
  * `openclaw configure --section web`

OpenClaw can show a separate follow-up step to enable `x_search` with the same `XAI_API_KEY`. That follow-up:

  * only appears after you choose Grok for `web_search`
  * is not a separate top-level web-search provider choice
  * can optionally set the `x_search` model during the same flow

If you skip it, you can enable or change `x_search` later in config.

## 

​

Get an API key

1

Create a key

Get an API key from [xAI](<https://console.x.ai/>).

2

Store the key

Set `XAI_API_KEY` in the Gateway environment, or configure via:
[code]
    openclaw configure --section web
    
[/code]

## 

​

Config
[code] 
    {
      plugins: {
        entries: {
          xai: {
            config: {
              webSearch: {
                apiKey: "xai-...", // optional if XAI_API_KEY is set
              },
            },
          },
        },
      },
      tools: {
        web: {
          search: {
            provider: "grok",
          },
        },
      },
    }
    
[/code]

**Environment alternative:** set `XAI_API_KEY` in the Gateway environment. For a gateway install, put it in `~/.openclaw/.env`.

## 

​

How it works

Grok uses xAI web-grounded responses to synthesize answers with inline citations, similar to Gemini’s Google Search grounding approach.

## 

​

Supported parameters

Grok search supports `query`. `count` is accepted for shared `web_search` compatibility, but Grok still returns one synthesized answer with citations rather than an N-result list. Provider-specific filters are not currently supported.

## 

​

Related

  * [Web Search overview](</tools/web>) — all providers and auto-detection
  * [x_search in Web Search](</tools/web#x_search>) — first-class X search via xAI
  * [Gemini Search](</tools/gemini-search>) — AI-synthesized answers via Google grounding


[Gemini search](</tools/gemini-search>)[Kimi search](</tools/kimi-search>)

⌘I