---
title: اتصال CLI
source_url: https://docs.openclaw.ai/fa/cli/attach
scraped_at: 2026-07-06
---

ReferenceCLI commands

`openclaw attach`، Claude Code را با یک پیکربندی موقت و سخت‌گیرانه MCP راه‌اندازی می‌کند که به یک نشست Gateway متصل است.

shCopy code
[code]
    openclaw attachopenclaw attach --session agent:main:telegram:123 --ttl 600000openclaw attach --print-config
[/code]

گزینه‌ها:

  * `--session <key>` مجوز را به یک نشست Gateway متصل می‌کند. پیش‌فرض، نشست اصلی است.
  * `--ttl <ms>` یک TTL مثبت برای مجوز، بر حسب میلی‌ثانیه، درخواست می‌کند. Gateway سقف خودش را اعمال می‌کند.
  * `--bin <path>` باینری Claude Code را انتخاب می‌کند. پیش‌فرض `claude` است.
  * `--print-config` فایل موقت `.mcp.json` را می‌نویسد، فرمان راه‌اندازی و env را چاپ می‌کند، و مجوز را تا پایان TTL فعال نگه می‌دارد.


توکن Bearer از طریق متغیرهای محیطی ارسال می‌شود، نه argv. OpenClaw Claude Code را با `--strict-mcp-config --mcp-config <path>` راه‌اندازی می‌کند تا سرورهای محیطی Claude MCP به نشست متصل‌شده نپیوندند. راه‌اندازی‌های عادی، هنگام خروج فرایند Claude Code، مجوز را لغو می‌کنند.

همچنین ببینید: [CLI Gateway](</fa/cli/gateway>)، [CLI MCP](</fa/cli/mcp>)، و [CLI ACP](</fa/cli/acp>).

Was this useful?YesNo

Open issue