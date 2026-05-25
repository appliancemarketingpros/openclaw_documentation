---
title: حافظهٔ Honcho
source_url: https://docs.openclaw.ai/fa/concepts/memory-honcho
scraped_at: 2026-05-25
---

[Honcho](<https://honcho.dev>) حافظه بومیِ هوش مصنوعی را به OpenClaw اضافه می‌کند. این ابزار مکالمه‌ها را در یک سرویس اختصاصی ماندگار می‌کند و به‌مرور زمان مدل‌های کاربر و agent را می‌سازد، تا agent شما زمینه بین‌نشستی‌ای داشته باشد که فراتر از فایل‌های Markdown در workspace است.

## چه چیزهایی فراهم می‌کند

  * **حافظه بین‌نشستی** \-- مکالمه‌ها پس از هر نوبت ماندگار می‌شوند، بنابراین زمینه در بازنشانی نشست‌ها، Compaction، و جابه‌جایی کانال‌ها حفظ می‌شود.
  * **مدل‌سازی کاربر** \-- Honcho برای هر کاربر یک پروفایل نگه می‌دارد (ترجیحات، facts، سبک ارتباطی) و همین‌طور برای agent (شخصیت، رفتارهای آموخته‌شده).
  * **جست‌وجوی معنایی** \-- جست‌وجو روی مشاهدات مکالمه‌های گذشته، نه فقط نشست فعلی.
  * **آگاهی چند-agentی** \-- agentهای والد به‌طور خودکار sub-agentهای ایجادشده را ردیابی می‌کنند، و والدها به‌عنوان ناظر به نشست‌های فرزند اضافه می‌شوند.


## ابزارهای موجود

Honcho ابزارهایی را ثبت می‌کند که agent می‌تواند در طول مکالمه از آن‌ها استفاده کند:

**بازیابی داده (سریع، بدون فراخوانی LLM):**

ابزار | کاری که انجام می‌دهد  
---|---  
`honcho_context` | بازنمایی کامل کاربر در نشست‌ها  
`honcho_search_conclusions` | جست‌وجوی معنایی روی نتیجه‌گیری‌های ذخیره‌شده  
`honcho_search_messages` | یافتن پیام‌ها در نشست‌ها (فیلتر بر اساس فرستنده، تاریخ)  
`honcho_session` | تاریخچه و خلاصه نشست فعلی  
  
**پرسش و پاسخ (با توان LLM):**

ابزار | کاری که انجام می‌دهد  
---|---  
`honcho_ask` | پرسش درباره کاربر. `depth='quick'` برای facts، و `'thorough'` برای synthesis  
  
## شروع به کار

Plugin را نصب کنید و راه‌اندازی را اجرا کنید:

bashCopy code
[code]
    openclaw plugins install @honcho-ai/openclaw-honchoopenclaw honcho setupopenclaw gateway --force
[/code]

دستور setup اطلاعات API شما را می‌پرسد، پیکربندی را می‌نویسد، و به‌صورت اختیاری فایل‌های حافظه موجود در workspace را مهاجرت می‌دهد.

## پیکربندی

تنظیمات زیر `plugins.entries["openclaw-honcho"].config` قرار دارند:

json5Copy code
[code]
    {  plugins: {    entries: {      "openclaw-honcho": {        config: {          apiKey: "your-api-key", // omit for self-hosted          workspaceId: "openclaw", // memory isolation          baseUrl: "https://api.honcho.dev",        },      },    },  },}
[/code]

برای نمونه‌های خودمیزبان، `baseUrl` را به سرور محلی خود اشاره دهید (برای مثال `http://localhost:8000`) و کلید API را حذف کنید.

## مهاجرت حافظه موجود

اگر فایل‌های حافظه موجود در workspace دارید (`USER.md`، `MEMORY.md`، `IDENTITY.md`، `memory/`، `canvas/`)، `openclaw honcho setup` آن‌ها را شناسایی می‌کند و پیشنهاد مهاجرت می‌دهد.

## سازوکار آن

پس از هر نوبت هوش مصنوعی، مکالمه در Honcho ماندگار می‌شود. پیام‌های کاربر و agent هر دو مشاهده می‌شوند، و به Honcho اجازه می‌دهند مدل‌های خود را به‌مرور زمان بسازد و پالایش کند.

در طول مکالمه، ابزارهای Honcho در مرحله `before_prompt_build` از سرویس پرس‌وجو می‌کنند و زمینه مرتبط را پیش از آن‌که مدل prompt را ببیند تزریق می‌کنند. این کار مرزهای دقیق نوبت‌ها و یادآوری مرتبط را تضمین می‌کند.

## Honcho در برابر حافظه داخلی

| داخلی / QMD | Honcho  
---|---|---  
**ذخیره‌سازی** | فایل‌های Markdown در workspace | سرویس اختصاصی (محلی یا میزبانی‌شده)  
**بین‌نشستی** | از طریق فایل‌های حافظه | خودکار، داخلی  
**مدل‌سازی کاربر** | دستی (نوشتن در [MEMORY.md](<http://MEMORY.md>)) | پروفایل‌های خودکار  
**جست‌وجو** | برداری + کلیدواژه (ترکیبی) | معنایی روی مشاهدات  
**چند-agentی** | ردیابی نمی‌شود | آگاهی والد/فرزند  
**وابستگی‌ها** | هیچ‌کدام (داخلی) یا باینری QMD | نصب Plugin  
  
Honcho و سامانه حافظه داخلی می‌توانند با هم کار کنند. وقتی QMD پیکربندی شده باشد، ابزارهای بیشتری برای جست‌وجوی فایل‌های Markdown محلی در کنار حافظه بین‌نشستی Honcho در دسترس قرار می‌گیرند.

## دستورهای CLI

bashCopy code
[code]
    openclaw honcho setup                        # Configure API key and migrate filesopenclaw honcho status                       # Check connection statusopenclaw honcho ask <question>               # Query Honcho about the useropenclaw honcho search <query> [-k N] [-d D] # Semantic search over memory
[/code]

## مطالعه بیشتر

  * [کد منبع Plugin](<https://github.com/plastic-labs/openclaw-honcho>)
  * [مستندات Honcho](<https://docs.honcho.dev>)
  * [راهنمای یکپارچه‌سازی Honcho با OpenClaw](<https://docs.honcho.dev/v3/guides/integrations/openclaw>)
  * [حافظه](</fa/concepts/memory>) \-- نمای کلی حافظه OpenClaw
  * [موتورهای زمینه](</fa/concepts/context-engine>) \-- سازوکار موتورهای زمینه Plugin


## مرتبط

  * [نمای کلی حافظه](</fa/concepts/memory>)
  * [موتور حافظه داخلی](</fa/concepts/memory-builtin>)
  * [موتور حافظه QMD](</fa/concepts/memory-qmd>)


Was this useful?YesNo