---
title: system
source_url: https://docs.openclaw.ai/cli/system
scraped_at: 2026-03-20
---

[OpenClaw home page](</>)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

⌘K

Search...

Navigation

Agents and sessions

system

# 

​

`openclaw system`

System-level helpers for the Gateway: enqueue system events, control heartbeats, and view presence.

## 

​

Common commands

Copy
[code]
    openclaw system event --text "Check for urgent follow-ups" --mode now
    openclaw system heartbeat enable
    openclaw system heartbeat last
    openclaw system presence
    
[/code]

## 

​

`system event`

Enqueue a system event on the **main** session. The next heartbeat will inject it as a `System:` line in the prompt. Use `--mode now` to trigger the heartbeat immediately; `next-heartbeat` waits for the next scheduled tick. Flags:

  * `--text <text>`: required system event text.
  * `--mode <mode>`: `now` or `next-heartbeat` (default).
  * `--json`: machine-readable output.


## 

​

`system heartbeat last|enable|disable`

Heartbeat controls:

  * `last`: show the last heartbeat event.
  * `enable`: turn heartbeats back on (use this if they were disabled).
  * `disable`: pause heartbeats.

Flags:

  * `--json`: machine-readable output.


## 

​

`system presence`

List the current system presence entries the Gateway knows about (nodes, instances, and similar status lines). Flags:

  * `--json`: machine-readable output.


## 

​

Notes

  * Requires a running Gateway reachable by your current config (local or remote).
  * System events are ephemeral and not persisted across restarts.


[sessions](</cli/sessions>)[channels](</cli/channels>)

⌘I