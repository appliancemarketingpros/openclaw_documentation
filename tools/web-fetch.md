---
title: Web fetch
source_url: https://docs.openclaw.ai/tools/web-fetch
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

Web fetch

The `web_fetch` tool does a plain HTTP GET and extracts readable content (HTML to markdown or text). It does **not** execute JavaScript. For JS-heavy sites or login-protected pages, use the [Web Browser](</tools/browser>) instead.

## 

​

Quick start

`web_fetch` is **enabled by default** — no configuration needed. The agent can call it immediately:
[code] 
    await web_fetch({ url: "https://example.com/article" });
    
[/code]

## 

​

Tool parameters

​

url

string

required

URL to fetch. `http(s)` only.

​

extractMode

'markdown' | 'text'

default:"markdown"

Output format after main-content extraction.

​

maxChars

number

Truncate output to this many characters.

## 

​

How it works

1

Fetch

Sends an HTTP GET with a Chrome-like User-Agent and `Accept-Language` header. Blocks private/internal hostnames and re-checks redirects.

2

Extract

Runs Readability (main-content extraction) on the HTML response.

3

Fallback (optional)

If Readability fails and Firecrawl is configured, retries through the Firecrawl API with bot-circumvention mode.

4

Cache

Results are cached for 15 minutes (configurable) to reduce repeated fetches of the same URL.

## 

​

Config
[code] 
    {
      tools: {
        web: {
          fetch: {
            enabled: true, // default: true
            provider: "firecrawl", // optional; omit for auto-detect
            maxChars: 50000, // max output chars
            maxCharsCap: 50000, // hard cap for maxChars param
            maxResponseBytes: 2000000, // max download size before truncation
            timeoutSeconds: 30,
            cacheTtlMinutes: 15,
            maxRedirects: 3,
            readability: true, // use Readability extraction
            userAgent: "Mozilla/5.0 ...", // override User-Agent
          },
        },
      },
    }
    
[/code]

## 

​

Firecrawl fallback

If Readability extraction fails, `web_fetch` can fall back to [Firecrawl](</tools/firecrawl>) for bot-circumvention and better extraction:
[code] 
    {
      tools: {
        web: {
          fetch: {
            provider: "firecrawl", // optional; omit for auto-detect from available credentials
          },
        },
      },
      plugins: {
        entries: {
          firecrawl: {
            enabled: true,
            config: {
              webFetch: {
                apiKey: "fc-...", // optional if FIRECRAWL_API_KEY is set
                baseUrl: "https://api.firecrawl.dev",
                onlyMainContent: true,
                maxAgeMs: 86400000, // cache duration (1 day)
                timeoutSeconds: 60,
              },
            },
          },
        },
      },
    }
    
[/code]

`plugins.entries.firecrawl.config.webFetch.apiKey` supports SecretRef objects. Legacy `tools.web.fetch.firecrawl.*` config is auto-migrated by `openclaw doctor --fix`.

If Firecrawl is enabled and its SecretRef is unresolved with no `FIRECRAWL_API_KEY` env fallback, gateway startup fails fast.

Firecrawl `baseUrl` overrides are locked down: they must use `https://` and the official Firecrawl host (`api.firecrawl.dev`).

Current runtime behavior:

  * `tools.web.fetch.provider` selects the fetch fallback provider explicitly.
  * If `provider` is omitted, OpenClaw auto-detects the first ready web-fetch provider from available credentials. Today the bundled provider is Firecrawl.
  * If Readability is disabled, `web_fetch` skips straight to the selected provider fallback. If no provider is available, it fails closed.


## 

​

Limits and safety

  * `maxChars` is clamped to `tools.web.fetch.maxCharsCap`
  * Response body is capped at `maxResponseBytes` before parsing; oversized responses are truncated with a warning
  * Private/internal hostnames are blocked
  * Redirects are checked and limited by `maxRedirects`
  * `web_fetch` is best-effort — some sites need the [Web Browser](</tools/browser>)


## 

​

Tool profiles

If you use tool profiles or allowlists, add `web_fetch` or `group:web`:
[code] 
    {
      tools: {
        allow: ["web_fetch"],
        // or: allow: ["group:web"]  (includes web_fetch, web_search, and x_search)
      },
    }
    
[/code]

## 

​

Related

  * [Web Search](</tools/web>) — search the web with multiple providers
  * [Web Browser](</tools/browser>) — full browser automation for JS-heavy sites
  * [Firecrawl](</tools/firecrawl>) — Firecrawl search and scrape tools


[WSL2 + Windows + remote Chrome CDP troubleshooting](</tools/browser-wsl2-windows-remote-cdp-troubleshooting>)[Web Search](</tools/web>)

⌘I