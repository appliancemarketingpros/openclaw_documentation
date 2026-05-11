---
title: Troubleshooting
source_url: https://docs.openclaw.ai/clawhub/troubleshooting
scraped_at: 2026-05-11
---

[OpenClaw home page](</>)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

⌘K

Search...

Navigation

> ## Documentation Index
> 
> Fetch the complete documentation index at: <https://docs.openclaw.ai/llms.txt>
> 
> Use this file to discover all available pages before exploring further.

# 

​

Troubleshooting

## 

​

`clawhub login` opens a browser but never completes

The CLI starts a short-lived local callback server during browser login.

  * Make sure your browser can reach `http://127.0.0.1:<port>/callback`.
  * Check local firewall, VPN, and proxy rules if the callback never arrives.
  * In headless environments, create an API token in the ClawHub web UI and run:


[code] 
    clawhub login --token clh_...
    
[/code]

## 

​

`whoami` or `publish` returns `Unauthorized` (401)

  * Sign in again with `clawhub login`.
  * If you use a custom config path, confirm `CLAWHUB_CONFIG_PATH` points at the file that contains your current token.
  * If you use an API token, confirm it was not revoked in the web UI.


## 

​

Search or install returns `Rate limit exceeded` (429)

Read the retry information in the response:

  * `Retry-After`: seconds to wait before retrying.
  * `RateLimit-Remaining` and `RateLimit-Limit`: your current budget.
  * `RateLimit-Reset` or `X-RateLimit-Reset`: reset timing.

If many users share one egress IP, anonymous IP limits can be hit even when each person only sends a few requests. Sign in where possible and retry after the reported delay.

## 

​

Search or install fails behind a proxy

The CLI respects standard proxy variables:
[code] 
    export HTTPS_PROXY=http://proxy.example.com:3128
    clawhub search "my query"
    
[/code]

Supported names include `HTTPS_PROXY`, `HTTP_PROXY`, `https_proxy`, and `http_proxy`.

## 

​

A skill does not appear in search

  * Check the exact slug or owner page if you know it.
  * Confirm the release is public and not held by scan or moderation.
  * If you own the skill, sign in and inspect it:


[code] 
    clawhub inspect <skill-slug>
    
[/code]

Owner-visible diagnostics may explain scan, upload-gate, or moderation state.

## 

​

Publish fails because required metadata is missing

For skills, check `SKILL.md` frontmatter. Required environment variables and tools should be declared so users and scanners can understand the package. For plugins, check `package.json` compatibility metadata. Code-plugin publishes need OpenClaw compatibility fields such as `openclaw.compat.pluginApi` and `openclaw.build.openclawVersion`. Preview the publish payload first:
[code] 
    clawhub package publish <source> --family code-plugin --dry-run
    
[/code]

## 

​

Publish fails with a GitHub owner or source error

ClawHub uses GitHub identity and source attribution to connect packages to their publishers.

  * Make sure you are signed in with the GitHub account that owns or can publish the package.
  * Check that the source URL is public or accessible to ClawHub.
  * For GitHub sources, use `owner/repo`, `owner/repo@ref`, or a full GitHub URL.


## 

​

`sync` says no skills were found

`sync` looks for folders containing `SKILL.md` or `skill.md`. Point it at the roots you want to scan:
[code] 
    clawhub sync --root /path/to/skills
    
[/code]

Preview first if you are unsure what will publish:
[code] 
    clawhub sync --all --dry-run --no-input
    
[/code]

## 

​

`update` refuses because of local changes

The local files do not match any version ClawHub knows about. Choose one:

  * Keep local edits and skip the update.
  * Overwrite with the published version:


[code] 
    clawhub update <slug> --force
    
[/code]

  * Publish your edited copy as a new slug or fork.


## 

​

A plugin install fails in OpenClaw

  * Use an explicit ClawHub source:


[code] 
    openclaw plugins install clawhub:<package>
    
[/code]

  * Check the package detail page for scan status and compatibility metadata.
  * Confirm your OpenClaw version satisfies the package’s advertised compatibility range.
  * If the package is hidden, held, or blocked, it may not be installable until the owner resolves the issue.


## 

​

Public API requests fail

  * Respect `429` retry headers and cache public list/search responses.
  * Link users back to the canonical ClawHub listing.
  * Do not mirror hidden, private, held, or moderation-blocked content outside the public API surface.

See [HTTP API](</clawhub/http-api>) for endpoint details.

[Telemetry](</clawhub/telemetry>)[Api](</clawhub/api>)

⌘I