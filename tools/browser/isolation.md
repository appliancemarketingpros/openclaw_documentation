---
title: Isolation and browser selection
source_url: https://docs.openclaw.ai/tools/browser/isolation
scraped_at: 2026-09-14
---

CapabilitiesTools

## Isolation guarantees

  * **Dedicated user data dir** : never touches your personal browser profile.
  * **Dedicated ports** : avoids `9222` to prevent collisions with dev workflows.
  * **Deterministic tab control** : `tabs` returns `suggestedTargetId` first, then stable `tabId` handles such as `t1`, optional labels, and the raw `targetId`. Agents should reuse `suggestedTargetId`; raw ids remain available for debugging and compatibility.


## Browser selection

When launching locally, OpenClaw picks the first available:

  1. Chrome
  2. Brave
  3. Edge
  4. Chromium
  5. Chrome Canary


You can override with `browser.executablePath`.

Platforms:

  * macOS: checks `/Applications` and `~/Applications`.
  * Linux: checks common Chrome/Brave/Edge/Chromium locations under `/usr/bin`, `/snap/bin`, `/opt/google`, `/opt/brave.com`, `/usr/lib/chromium`, and `/usr/lib/chromium-browser`, plus Playwright-managed Chromium under `PLAYWRIGHT_BROWSERS_PATH` or `~/.cache/ms-playwright`.
  * Windows: checks common install locations.


## Control API (optional)

For scripting and debugging, the Gateway exposes a small **loopback-only HTTP control API** plus a matching `openclaw browser` CLI (snapshots, refs, wait power-ups, JSON output, debug workflows). See [Browser control API](</tools/browser-control>) for the full reference.

Was this useful?YesNo

Open issue