---
title: reset
source_url: https://docs.openclaw.ai/cli/reset
scraped_at: 2026-03-20
---

[OpenClaw home page](</>)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

⌘K

Search...

Navigation

Gateway and service

reset

# 

​

`openclaw reset`

Reset local config/state (keeps the CLI installed).

Copy
[code]
    openclaw backup create
    openclaw reset
    openclaw reset --dry-run
    openclaw reset --scope config+creds+sessions --yes --non-interactive
    
[/code]

Run `openclaw backup create` first if you want a restorable snapshot before removing local state.

[onboard](</cli/onboard>)[secrets](</cli/secrets>)

⌘I