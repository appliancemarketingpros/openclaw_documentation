---
title: Resume
source_url: https://docs.openclaw.ai/cli/resume
scraped_at: 2026-08-10
---

ReferenceCLI commands

# `openclaw resume`

Attach the terminal UI to an existing Gateway session. The session stays on the Gateway; `resume` selects it and opens the existing [TUI](</cli/tui>).

bashCopy code
[code]
    openclaw resumeopenclaw resume <query>
[/code]

With no query, OpenClaw displays up to 50 sessions active in the last seven days. With a query, an exact session key wins; otherwise OpenClaw requires a unique substring or fuzzy match across session keys, display names, and labels.

The picker omits bare `global` rows because they do not identify an owning agent. To attach one, pass a fully qualified key such as `openclaw resume agent:main:global`.

If a query is ambiguous, OpenClaw prints the matching candidates and exits with status 1. If no recent session matches, it suggests the picker and [`openclaw sessions`](</cli/sessions>), then exits with status 1.

## Options

Flag | Default | Description  
---|---|---  
`--url <url>` | `gateway.remote.url` from config | Gateway WebSocket URL.  
`--token <token>` | (none) | Gateway token if required.  
`--password <pass>` | (none) | Gateway password if required.  
`--tls-fingerprint <sha256>` | `gateway.remote.tlsFingerprint` | Expected TLS certificate fingerprint for a pinned `wss://` Gateway.  
  
`resume` uses the same Gateway URL, authentication, and TLS resolution as [`openclaw tui`](</cli/tui>). It never starts a Gateway automatically. If the configured Gateway is unavailable, start or repair it and rerun the command.

`resume` resolves configured Gateway auth SecretRefs for token/password auth when possible (`env`/`file`/`exec` providers).

Gateway target precedence is explicit `--url`, then `OPENCLAW_GATEWAY_URL`, then `gateway.remote.url` when `gateway.mode` is `remote`, then the local loopback Gateway. For that local Gateway, `OPENCLAW_GATEWAY_PORT` takes precedence over the active port recorded by a running Gateway, which takes precedence over the configured or default `gateway.port`.

## Examples

bashCopy code
[code]
    # Choose from recent sessionsopenclaw resume # Exact keyopenclaw resume agent:main:bugfix # Unique display-name or label fragmentopenclaw resume bugfix # Remote Gateway overrideopenclaw resume bugfix --url wss://gateway.example.com --token <token>
[/code]

## Related

  * [TUI](</cli/tui>)
  * [Sessions](</cli/sessions>)
  * [TUI guide](</web/tui>)


Was this useful?YesNo

Open issue