---
title: Plugin ناظر Codex
source_url: https://docs.openclaw.ai/fa/plugins/reference/codex-supervisor
scraped_at: 2026-06-29
---

Get started

# Plugin سرپرست Codex

نشست‌های app-server Codex را از OpenClaw نظارت کنید.

## توزیع

  * بسته: `@openclaw/codex-supervisor`
  * مسیر نصب: در OpenClaw گنجانده شده است


## سطح

contracts: tools

## فهرست نشست‌ها

`codex_sessions_list` به طور پیش‌فرض فقط نشست‌های بارگذاری‌شده Codex را نشان می‌دهد. `include_stored` را تنظیم کنید تا تاریخچه ذخیره‌شده هم شامل شود؛ Plugin از مسیر فهرست‌گیری فقط state-DB در app-server Codex استفاده می‌کند و به طور پیش‌فرض نتایج ذخیره‌شده را به 200 محدود می‌کند. `max_stored_sessions` را ارسال کنید تا این سقف را کاهش یا افزایش دهید، حداکثر تا 1000.

Was this useful?YesNo

Open issue