---
title: tui
source_url: https://docs.openclaw.ai/cli/tui
scraped_at: 2026-03-20
---

[OpenClaw home page](</>)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

⌘K

Search...

Navigation

Interfaces

tui

# 

​

`openclaw tui`

Open the terminal UI connected to the Gateway. Related:

  * TUI guide: [TUI](</web/tui>)

Notes:

  * `tui` resolves configured gateway auth SecretRefs for token/password auth when possible (`env`/`file`/`exec` providers).
  * When launched from inside a configured agent workspace directory, TUI auto-selects that agent for the session key default (unless `--session` is explicitly `agent:<id>:...`).


## 

​

Examples

Copy
[code]
    openclaw tui
    openclaw tui --url ws://127.0.0.1:18789 --token <token>
    openclaw tui --session main --deliver
    # when run inside an agent workspace, infers that agent automatically
    openclaw tui --session bugfix
    
[/code]

[dashboard](</cli/dashboard>)[acp](</cli/acp>)

⌘I