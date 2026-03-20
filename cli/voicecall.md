---
title: voicecall
source_url: https://docs.openclaw.ai/cli/voicecall
scraped_at: 2026-03-20
---

[OpenClaw home page](</>)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

⌘K

Search...

Navigation

Channels and messaging

voicecall

# 

​

`openclaw voicecall`

`voicecall` is a plugin-provided command. It only appears if the voice-call plugin is installed and enabled. Primary doc:

  * Voice-call plugin: [Voice Call](</plugins/voice-call>)


## 

​

Common commands

Copy
[code]
    openclaw voicecall status --call-id <id>
    openclaw voicecall call --to "+15555550123" --message "Hello" --mode notify
    openclaw voicecall continue --call-id <id> --message "Any questions?"
    openclaw voicecall end --call-id <id>
    
[/code]

## 

​

Exposing webhooks (Tailscale)

Copy
[code]
    openclaw voicecall expose --mode serve
    openclaw voicecall expose --mode funnel
    openclaw voicecall expose --mode off
    
[/code]

Security note: only expose the webhook endpoint to networks you trust. Prefer Tailscale Serve over Funnel when possible.

[qr](</cli/qr>)[approvals](</cli/approvals>)

⌘I