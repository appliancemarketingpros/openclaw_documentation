---
title: Diagnostics Flags
source_url: https://docs.openclaw.ai/diagnostics/flags
scraped_at: 2026-03-20
---

[OpenClaw home page](</>)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

⌘K

Search...

Navigation

Environment and debugging

Diagnostics Flags

# 

​

Diagnostics Flags

Diagnostics flags let you enable targeted debug logs without turning on verbose logging everywhere. Flags are opt-in and have no effect unless a subsystem checks them.

## 

​

How it works

  * Flags are strings (case-insensitive).
  * You can enable flags in config or via an env override.
  * Wildcards are supported:
    * `telegram.*` matches `telegram.http`
    * `*` enables all flags


## 

​

Enable via config

Copy
[code]
    {
      "diagnostics": {
        "flags": ["telegram.http"]
      }
    }
    
[/code]

Multiple flags:

Copy
[code]
    {
      "diagnostics": {
        "flags": ["telegram.http", "gateway.*"]
      }
    }
    
[/code]

Restart the gateway after changing flags.

## 

​

Env override (one-off)

Copy
[code]
    OPENCLAW_DIAGNOSTICS=telegram.http,telegram.payload
    
[/code]

Disable all flags:

Copy
[code]
    OPENCLAW_DIAGNOSTICS=0
    
[/code]

## 

​

Where logs go

Flags emit logs into the standard diagnostics log file. By default:

Copy
[code]
    /tmp/openclaw/openclaw-YYYY-MM-DD.log
    
[/code]

If you set `logging.file`, use that path instead. Logs are JSONL (one JSON object per line). Redaction still applies based on `logging.redactSensitive`.

## 

​

Extract logs

Pick the latest log file:

Copy
[code]
    ls -t /tmp/openclaw/openclaw-*.log | head -n 1
    
[/code]

Filter for Telegram HTTP diagnostics:

Copy
[code]
    rg "telegram http error" /tmp/openclaw/openclaw-*.log
    
[/code]

Or tail while reproducing:

Copy
[code]
    tail -f /tmp/openclaw/openclaw-$(date +%F).log | rg "telegram http error"
    
[/code]

For remote gateways, you can also use `openclaw logs --follow` (see [/cli/logs](</cli/logs>)).

## 

​

Notes

  * If `logging.level` is set higher than `warn`, these logs may be suppressed. Default `info` is fine.
  * Flags are safe to leave enabled; they only affect log volume for the specific subsystem.
  * Use [/logging](</logging>) to change log destinations, levels, and redaction.


[Node + tsx Crash](</debug/node-issue>)[Session Management Deep Dive](</reference/session-management-compaction>)

⌘I