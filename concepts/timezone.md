---
title: Timezones
source_url: https://docs.openclaw.ai/concepts/timezone
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

Timezones

# 

​

Timezones

OpenClaw standardizes timestamps so the model sees a **single reference time**.

## 

​

Message envelopes (local by default)

Inbound messages are wrapped in an envelope like:

Copy
[code]
    [Provider ... 2026-01-05 16:26 PST] message text
    
[/code]

The timestamp in the envelope is **host-local by default** , with minutes precision. You can override this with:

Copy
[code]
    {
      agents: {
        defaults: {
          envelopeTimezone: "local", // "utc" | "local" | "user" | IANA timezone
          envelopeTimestamp: "on", // "on" | "off"
          envelopeElapsed: "on", // "on" | "off"
        },
      },
    }
    
[/code]

  * `envelopeTimezone: "utc"` uses UTC.
  * `envelopeTimezone: "user"` uses `agents.defaults.userTimezone` (falls back to host timezone).
  * Use an explicit IANA timezone (e.g., `"Europe/Vienna"`) for a fixed offset.
  * `envelopeTimestamp: "off"` removes absolute timestamps from envelope headers.
  * `envelopeElapsed: "off"` removes elapsed time suffixes (the `+2m` style).


### 

​

Examples

**Local (default):**

Copy
[code]
    [Signal Alice +1555 2026-01-18 00:19 PST] hello
    
[/code]

**Fixed timezone:**

Copy
[code]
    [Signal Alice +1555 2026-01-18 06:19 GMT+1] hello
    
[/code]

**Elapsed time:**

Copy
[code]
    [Signal Alice +1555 +2m 2026-01-18T05:19Z] follow-up
    
[/code]

## 

​

Tool payloads (raw provider data + normalized fields)

Tool calls (`channels.discord.readMessages`, `channels.slack.readMessages`, etc.) return **raw provider timestamps**. We also attach normalized fields for consistency:

  * `timestampMs` (UTC epoch milliseconds)
  * `timestampUtc` (ISO 8601 UTC string)

Raw provider fields are preserved.

## 

​

User timezone for the system prompt

Set `agents.defaults.userTimezone` to tell the model the user’s local time zone. If it is unset, OpenClaw resolves the **host timezone at runtime** (no config write).

Copy
[code]
    {
      agents: { defaults: { userTimezone: "America/Chicago" } },
    }
    
[/code]

The system prompt includes:

  * `Current Date & Time` section with local time and timezone
  * `Time format: 12-hour` or `24-hour`

You can control the prompt format with `agents.defaults.timeFormat` (`auto` | `12` | `24`). See [Date & Time](</date-time>) for the full behavior and examples.

[Usage Tracking](</concepts/usage-tracking>)[Credits](</reference/credits>)

⌘I