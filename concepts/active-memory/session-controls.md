---
title: Session controls
source_url: https://docs.openclaw.ai/concepts/active-memory/session-controls
scraped_at: 2026-09-14
---

AgentsSessions and memory

## Session toggle

Pause or resume active memory for the current chat session without editing config:

textCopy code
[code]
    /active-memory status/active-memory off/active-memory on
[/code]

This only affects the current session; it does not change `plugins.entries.active-memory.config.enabled`, an agent's `memory.search.rememberAcrossConversations` setting, or other global configuration.

To pause/resume for all sessions instead, use the global form (requires owner or `operator.admin`):

textCopy code
[code]
    /active-memory status --global/active-memory off --global/active-memory on --global
[/code]

The global form writes `plugins.entries.active-memory.config.enabled` but leaves `plugins.entries.active-memory.enabled` on, so the command stays available to turn active memory back on later.

## How to see it

By default, active memory injects a hidden untrusted prompt prefix that is not shown in the normal reply. Turn on the session toggles that match the output you want:

textCopy code
[code]
    /verbose on/trace on
[/code]

With those on, OpenClaw appends diagnostic lines after the normal reply (as a follow-up, so channel clients do not flash a separate pre-reply bubble):

  * `/verbose on` adds a status line: `🧩 Active Memory: status=ok elapsed=842ms query=recent summary=34 chars`
  * `/trace on` adds a debug summary: `🔎 Active Memory Debug: Lemon pepper wings with blue cheese.`


Example flow:

textCopy code
[code]
    /verbose on/trace onwhat wings should i order?
[/code]

textCopy code
[code]
    ...normal assistant reply... 🧩 Active Memory: status=ok elapsed=842ms query=recent summary=34 chars🔎 Active Memory Debug: Lemon pepper wings with blue cheese.
[/code]

With `/trace raw`, the traced `Model Input (User Role)` block shows the raw hidden prefix:

textCopy code
[code]
    Context:<active_memory_plugin>...</active_memory_plugin>
[/code]

By default the blocking sub-agent's transcript is temporary and deleted after the run completes; see [Transcript persistence](</concepts/active-memory/advanced-options#transcript-persistence>) to keep it.

Was this useful?YesNo

Open issue