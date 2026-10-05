---
title: Gateway runbook
source_url: https://docs.openclaw.ai/gateway
scraped_at: 2026-10-05
---

**Note**

Gateway config reload watches the active config file path (resolved from profile/state defaults, or `OPENCLAW_CONFIG_PATH` when set). Default mode is `gateway.reload.mode="hybrid"`. After the first successful load, the running process serves the active in-memory config snapshot; a successful reload swaps that snapshot atomically.