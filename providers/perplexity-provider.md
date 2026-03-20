---
title: Perplexity (Provider)
source_url: https://docs.openclaw.ai/providers/perplexity-provider
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

Perplexity (Provider)

# 

​

Perplexity (Web Search Provider)

The Perplexity plugin provides web search capabilities through the Perplexity Search API or Perplexity Sonar via OpenRouter.

This page covers the Perplexity **provider** setup. For the Perplexity **tool** (how the agent uses it), see [Perplexity tool](</tools/perplexity-search>).

  * Type: web search provider (not a model provider)
  * Auth: `PERPLEXITY_API_KEY` (direct) or `OPENROUTER_API_KEY` (via OpenRouter)
  * Config path: `plugins.entries.perplexity.config.webSearch.apiKey`


## 

​

Quick start

  1. Set the API key:


Copy
[code]
    openclaw configure --section web
    
[/code]

Or set it directly:

Copy
[code]
    openclaw config set plugins.entries.perplexity.config.webSearch.apiKey "pplx-xxxxxxxxxxxx"
    
[/code]

  2. The agent will automatically use Perplexity for web searches when configured.


## 

​

Search modes

The plugin auto-selects the transport based on API key prefix:

Key prefix| Transport| Features  
---|---|---  
`pplx-`| Native Perplexity Search API| Structured results, domain/language/date filters  
`sk-or-`| OpenRouter (Sonar)| AI-synthesized answers with citations  
  
## 

​

Native API filtering

When using the native Perplexity API (`pplx-` key), searches support:

  * **Country** : 2-letter country code
  * **Language** : ISO 639-1 language code
  * **Date range** : day, week, month, year
  * **Domain filters** : allowlist/denylist (max 20 domains)
  * **Content budget** : `max_tokens`, `max_tokens_per_page`


## 

​

Environment note

If the Gateway runs as a daemon (launchd/systemd), make sure `PERPLEXITY_API_KEY` is available to that process (for example, in `~/.openclaw/.env` or via `env.shellEnv`).

[OpenRouter](</providers/openrouter>)[Qianfan](</providers/qianfan>)

⌘I