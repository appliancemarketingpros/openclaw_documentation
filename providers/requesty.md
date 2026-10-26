---
title: Requesty
source_url: https://docs.openclaw.ai/providers/requesty
scraped_at: 2026-10-26
---

Discovery lists Requesty's managed policies, which route a bare model name to the best available hosting provider under your organization's routing and compliance settings. To pin a specific host instead (`vertex/claude-sonnet-4-6`, `bedrock/claude-sonnet-4-6`), add that id under `models.providers.requesty.models` in your config; OpenClaw publishes authored rows alongside the discovered policies.