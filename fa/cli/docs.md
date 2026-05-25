---
title: مستندات
source_url: https://docs.openclaw.ai/fa/cli/docs
scraped_at: 2026-05-25
---

# `openclaw docs`

نمایهٔ زندهٔ مستندات OpenClaw را از ترمینال جست‌وجو کنید. این دستور برای نقطهٔ پایانی عمومی جست‌وجوی MCP مستندات میزبانی‌شده روی Mintlify در `https://docs.openclaw.ai/mcp.SearchOpenClaw` یک فرمان پوسته اجرا می‌کند و نتایج را در ترمینال شما نمایش می‌دهد.

## کاربرد

bashCopy code
[code]
    openclaw docs                       # print docs entrypoint and example searchopenclaw docs <query...>            # search the live docs index
[/code]

آرگومان‌ها:

آرگومان | توضیح  
---|---  
`[query...]` | پرس‌وجوی جست‌وجوی آزاد. پرس‌وجوهای چندواژه‌ای با فاصله به هم پیوسته و به‌صورت یک مورد ارسال می‌شوند.  
  
## نمونه‌ها

bashCopy code
[code]
    openclaw docs browser existing-sessionopenclaw docs sandbox allowHostControlopenclaw docs gateway token secretref
[/code]

بدون پرس‌وجو، `openclaw docs` به‌جای اجرای جست‌وجو، URL نقطهٔ ورود مستندات را همراه با یک دستور جست‌وجوی نمونه چاپ می‌کند.

## نحوهٔ کار

`openclaw docs` برای فراخوانی ابزار جست‌وجوی MCP مستندات، CLI به نام `mcporter` را اجرا می‌کند، سپس بلوک‌های `Title: / Link: / Content:` را از خروجی ابزار به فهرستی از نتایج تبدیل می‌کند.

برای پیدا کردن `mcporter`، OpenClaw به‌ترتیب این موارد را بررسی می‌کند:

  1. `mcporter` در `PATH` (اگر وجود داشته باشد مستقیم استفاده می‌شود).
  2. `pnpm dlx mcporter ...` اگر `pnpm` نصب باشد.
  3. `npx -y mcporter ...` اگر `npx` نصب باشد.


اگر هیچ‌کدام در دسترس نباشند، دستور با راهنمایی برای نصب `pnpm` (`npm install -g pnpm`) ناموفق می‌شود.

فراخوانی جست‌وجو از مهلت زمانی ثابت ۳۰ ثانیه‌ای استفاده می‌کند. قطعه‌های نتیجه برای هر ورودی به حدود ۲۲۰ نویسه کوتاه می‌شوند.

## خروجی

در یک ترمینال غنی (TTY)، نتایج به‌صورت یک عنوان و سپس یک فهرست بولت‌دار نمایش داده می‌شوند. هر بولت عنوان صفحه، URL پیوندشدهٔ مستندات، و یک قطعهٔ کوتاه در خط بعدی را نشان می‌دهد. نتایج خالی، «نتیجه‌ای نیست.» را چاپ می‌کنند.

در خروجی غیرغنی (پایپ‌شده، `--no-color`، اسکریپت‌ها)، همان داده‌ها به‌صورت Markdown نمایش داده می‌شوند:

markdownCopy code
[code]
    # Docs search: <query> - [Title](https://docs.openclaw.ai/...) - snippet- [Title](https://docs.openclaw.ai/...) - snippet
[/code]

## کدهای خروج

کد | معنی  
---|---  
`0` | جست‌وجو موفق بود (از جمله پاسخ‌های بدون نتیجه).  
`1` | فراخوانی ابزار MCP ناموفق بود؛ stderr به‌صورت درون‌خطی چاپ می‌شود.  
  
## مرتبط

  * [مرجع CLI](</fa/cli>)
  * [مستندات زنده](<https://docs.openclaw.ai>)


Was this useful?YesNo