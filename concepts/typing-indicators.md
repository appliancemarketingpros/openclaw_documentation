---
title: Typing Indicators
source_url: https://docs.openclaw.ai/concepts/typing-indicators
scraped_at: 2026-03-20
---

[OpenClaw home page](</>)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

⌘K

Search...

Navigation

Concept internals

Typing Indicators

# 

​

Typing indicators

Typing indicators are sent to the chat channel while a run is active. Use `agents.defaults.typingMode` to control **when** typing starts and `typingIntervalSeconds` to control **how often** it refreshes.

## 

​

Defaults

When `agents.defaults.typingMode` is **unset** , OpenClaw keeps the legacy behavior:

  * **Direct chats** : typing starts immediately once the model loop begins.
  * **Group chats with a mention** : typing starts immediately.
  * **Group chats without a mention** : typing starts only when message text begins streaming.
  * **Heartbeat runs** : typing is disabled.


## 

​

Modes

Set `agents.defaults.typingMode` to one of:

  * `never` — no typing indicator, ever.
  * `instant` — start typing **as soon as the model loop begins** , even if the run later returns only the silent reply token.
  * `thinking` — start typing on the **first reasoning delta** (requires `reasoningLevel: "stream"` for the run).
  * `message` — start typing on the **first non-silent text delta** (ignores the `NO_REPLY` silent token).

Order of “how early it fires”: `never` → `message` → `thinking` → `instant`

## 

​

Configuration

Copy
[code]
    {
      agent: {
        typingMode: "thinking",
        typingIntervalSeconds: 6,
      },
    }
    
[/code]

You can override mode or cadence per session:

Copy
[code]
    {
      session: {
        typingMode: "message",
        typingIntervalSeconds: 4,
      },
    }
    
[/code]

## 

​

Notes

  * `message` mode won’t show typing for silent-only replies (e.g. the `NO_REPLY` token used to suppress output).
  * `thinking` only fires if the run streams reasoning (`reasoningLevel: "stream"`). If the model doesn’t emit reasoning deltas, typing won’t start.
  * Heartbeats never show typing, regardless of mode.
  * `typingIntervalSeconds` controls the **refresh cadence** , not the start time. The default is 6 seconds.


[Markdown Formatting](</concepts/markdown-formatting>)[Usage Tracking](</concepts/usage-tracking>)

⌘I