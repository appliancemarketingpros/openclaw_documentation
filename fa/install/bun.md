---
title: Bun (آزمایشی)
source_url: https://docs.openclaw.ai/fa/install/bun
scraped_at: 2026-05-25
---

Bun یک زمان اجرای محلی اختیاری برای اجرای مستقیم TypeScript است (`bun run ...`، `bun --watch ...`). مدیر بستهٔ پیش‌فرض همچنان `pnpm` است، که کاملاً پشتیبانی می‌شود و ابزارهای مستندات از آن استفاده می‌کنند. Bun نمی‌تواند از `pnpm-lock.yaml` استفاده کند و آن را نادیده می‌گیرد.

## نصب

* ### نصب وابستگی‌ها

shCopy code
[code]
    bun install
[/code]

`bun.lock` / `bun.lockb` در gitignore هستند، بنابراین تغییری در repo ایجاد نمی‌شود. برای رد کردن کامل نوشتن lockfile:

shCopy code
[code]
    bun install --no-save
[/code]

* ### ساخت و آزمون

shCopy code
[code]
    bun run buildbun run vitest run
[/code]

## اسکریپت‌های چرخهٔ حیات

Bun اسکریپت‌های چرخهٔ حیات وابستگی‌ها را مسدود می‌کند مگر اینکه صریحاً قابل اعتماد اعلام شوند. برای این repo، اسکریپت‌هایی که معمولاً مسدود می‌شوند لازم نیستند:

  * `baileys` `preinstall` \-- بررسی می‌کند که نسخهٔ اصلی Node >= 20 باشد (OpenClaw به‌صورت پیش‌فرض از Node 24 استفاده می‌کند و همچنان از Node 22 LTS، در حال حاضر `22.16+`، پشتیبانی می‌کند)
  * `protobufjs` `postinstall` \-- هشدارهایی دربارهٔ طرح‌های نسخه‌گذاری ناسازگار صادر می‌کند (بدون artifactهای ساخت)


اگر با مشکلی در زمان اجرا روبه‌رو شدید که به این اسکریپت‌ها نیاز دارد، آن‌ها را صریحاً قابل اعتماد اعلام کنید:

shCopy code
[code]
    bun pm trust baileys protobufjs
[/code]

## نکات احتیاطی

برخی اسکریپت‌ها هنوز pnpm را به‌صورت hardcode دارند (برای مثال `docs:build`، `ui:*`، `protocol:check`). فعلاً آن‌ها را از طریق pnpm اجرا کنید.

## مرتبط

  * [نمای کلی نصب](</fa/install>)
  * [Node.js](</fa/install/node>)
  * [به‌روزرسانی](</fa/install/updating>)


Was this useful?YesNo