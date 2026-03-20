---
title: Qwen
source_url: https://docs.openclaw.ai/providers/qwen
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

Qwen

# 

​

Qwen

Qwen provides a free-tier OAuth flow for Qwen Coder and Qwen Vision models (2,000 requests/day, subject to Qwen rate limits).

## 

​

Enable the plugin

Copy
[code]
    openclaw plugins enable qwen-portal-auth
    
[/code]

Restart the Gateway after enabling.

## 

​

Authenticate

Copy
[code]
    openclaw models auth login --provider qwen-portal --set-default
    
[/code]

This runs the Qwen device-code OAuth flow and writes a provider entry to your `models.json` (plus a `qwen` alias for quick switching).

## 

​

Model IDs

  * `qwen-portal/coder-model`
  * `qwen-portal/vision-model`

Switch models with:

Copy
[code]
    openclaw models set qwen-portal/coder-model
    
[/code]

## 

​

Reuse Qwen Code CLI login

If you already logged in with the Qwen Code CLI, OpenClaw will sync credentials from `~/.qwen/oauth_creds.json` when it loads the auth store. You still need a `models.providers.qwen-portal` entry (use the login command above to create one).

## 

​

Notes

  * Tokens auto-refresh; re-run the login command if refresh fails or access is revoked.
  * Default base URL: `https://portal.qwen.ai/v1` (override with `models.providers.qwen-portal.baseUrl` if Qwen provides a different endpoint).
  * See [Model providers](</concepts/model-providers>) for provider-wide rules.


[Qianfan](</providers/qianfan>)[SGLang](</providers/sglang>)

⌘I