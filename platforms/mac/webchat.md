---
title: WebChat (macOS)
source_url: https://docs.openclaw.ai/platforms/mac/webchat
scraped_at: 2026-03-20
---

[OpenClaw home page](</>)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

⌘K

Search...

Navigation

macOS companion app

WebChat (macOS)

# 

​

WebChat (macOS app)

The macOS menu bar app embeds the WebChat UI as a native SwiftUI view. It connects to the Gateway and defaults to the **main session** for the selected agent (with a session switcher for other sessions).

  * **Local mode** : connects directly to the local Gateway WebSocket.
  * **Remote mode** : forwards the Gateway control port over SSH and uses that tunnel as the data plane.


## 

​

Launch & debugging

  * Manual: Lobster menu → “Open Chat”.
  * Auto‑open for testing:

Copy
[code]dist/OpenClaw.app/Contents/MacOS/OpenClaw --webchat
        
[/code]

  * Logs: `./scripts/clawlog.sh` (subsystem `ai.openclaw`, category `WebChatSwiftUI`).


## 

​

How it is wired

  * Data plane: Gateway WS methods `chat.history`, `chat.send`, `chat.abort`, `chat.inject` and events `chat`, `agent`, `presence`, `tick`, `health`.
  * Session: defaults to the primary session (`main`, or `global` when scope is global). The UI can switch between sessions.
  * Onboarding uses a dedicated session to keep first‑run setup separate.


## 

​

Security surface

  * Remote mode forwards only the Gateway WebSocket control port over SSH.


## 

​

Known limitations

  * The UI is optimized for chat sessions (not a full browser sandbox).


[Voice Overlay](</platforms/mac/voice-overlay>)[Canvas](</platforms/mac/canvas>)

⌘I