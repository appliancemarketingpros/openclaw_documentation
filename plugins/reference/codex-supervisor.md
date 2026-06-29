---
title: Codex Supervisor plugin
source_url: https://docs.openclaw.ai/plugins/reference/codex-supervisor
scraped_at: 2026-06-29
---

Get started

# Codex Supervisor plugin

Supervise Codex app-server sessions from OpenClaw.

## Distribution

  * Package: `@openclaw/codex-supervisor`
  * Install route: included in OpenClaw


## Surface

contracts: tools

## Session Listing

`codex_sessions_list` defaults to loaded Codex sessions only. Set `include_stored` to include stored history; the plugin uses Codex app-server's state-DB-only listing path and caps stored results at 200 by default. Pass `max_stored_sessions` to lower or raise that cap, up to 1000.

Was this useful?YesNo

Open issue