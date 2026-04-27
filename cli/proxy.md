---
title: Proxy
source_url: https://docs.openclaw.ai/cli/proxy
scraped_at: 2026-04-27
---

[OpenClaw home page](</>)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

⌘K

Search...

Navigation

Utility

Proxy

# 

​

`openclaw proxy`

Run the local explicit debug proxy and inspect captured traffic. This is a debugging command for transport-level investigation. It can start a local proxy, run a child command with capture enabled, list capture sessions, query common traffic patterns, read captured blobs, and purge local capture data.

## 

​

Commands
[code] 
    openclaw proxy start [--host <host>] [--port <port>]
    openclaw proxy run [--host <host>] [--port <port>] -- <cmd...>
    openclaw proxy coverage
    openclaw proxy sessions [--limit <count>]
    openclaw proxy query --preset <name> [--session <id>]
    openclaw proxy blob --id <blobId>
    openclaw proxy purge
    
[/code]

## 

​

Query presets

`openclaw proxy query --preset <name>` accepts:

  * `double-sends`
  * `retry-storms`
  * `cache-busting`
  * `ws-duplicate-frames`
  * `missing-ack`
  * `error-bursts`


## 

​

Notes

  * `start` defaults to `127.0.0.1` unless `--host` is set.
  * `run` starts a local debug proxy and then runs the command after `--`.
  * Captures are local debugging data; use `openclaw proxy purge` when finished.


## 

​

Related

  * [CLI reference](</cli>)
  * [Trusted proxy auth](</gateway/trusted-proxy-auth>)


[MCP](</cli/mcp>)[Wiki](</cli/wiki>)

⌘I