---
title: ClawRouter
source_url: https://docs.openclaw.ai/fa/providers/clawrouter
scraped_at: 2026-07-06
---

ModelsProviders

ClawRouter به OpenClaw یک کلید محدود به policy برای چندین ارائه‌دهندهٔ مدل بالادستی می‌دهد. Plugin همراه فقط مدل‌هایی را کشف می‌کند که برای آن کلید مجاز هستند، هر مدل را از طریق protocol اعلام‌شدهٔ خودش مسیریابی می‌کند، و بودجهٔ کلید و مصرف تجمیعی را در سطوح مصرف OpenClaw گزارش می‌دهد.

شما هر Plugin ارائه‌دهندهٔ بالادستی را روی میزبان OpenClaw نصب یا احراز هویت نمی‌کنید. اعتبارنامه‌های بالادستی و ارسال‌های اختصاصی هر ارائه‌دهنده در ClawRouter باقی می‌مانند. OpenClaw فقط به Plugin همراه `@openclaw/clawrouter` و یک اعتبارنامهٔ صادرشدهٔ ClawRouter نیاز دارد.

ویژگی | مقدار  
---|---  
ارائه‌دهنده | `clawrouter`  
بسته | `@openclaw/clawrouter`  
احراز هویت | `CLAWROUTER_API_KEY`  
URL پیش‌فرض | `https://clawrouter.openclaw.ai`  
فهرست مدل | محدود به اعتبارنامه از طریق `/v1/catalog`  
سهمیه‌ها | بودجه و مصرف ماهانه از طریق `/v1/usage`  
  
## شروع به کار

* ### دریافت یک اعتبارنامهٔ محدود

از مدیر ClawRouter خود یک اعتبارنامه بخواهید که policy آن شامل ارائه‌دهنده‌ها، مدل‌ها، و بودجهٔ ماهانه‌ای باشد که باید استفاده کنید. اعتبارنامه‌ها هنگام صدور فقط یک بار نمایش داده می‌شوند.

* ### پیکربندی OpenClaw

bashCopy code
[code]
    export CLAWROUTER_API_KEY="..."openclaw onboard --auth-choice clawrouter-api-keyopenclaw plugins enable clawrouter
[/code]

این Plugin همراه OpenClaw است. اگر پیکربندی شما `plugins.allow` را تنظیم می‌کند، پیش از فعال‌سازی، `clawrouter` را به آن فهرست اضافه کنید. برای یک استقرار سفارشی، `models.providers.clawrouter.baseUrl` را روی مبدا ClawRouter تنظیم کنید؛ مقدار پیش‌فرض `https://clawrouter.openclaw.ai` است.

* ### فهرست کردن مدل‌های اعطاشده

bashCopy code
[code]
    openclaw models list --all --provider clawrouter
[/code]

refs مدل برگشتی را دقیقا همان‌طور که نمایش داده شده‌اند استفاده کنید. آن‌ها فضای نام بالادستی را نگه می‌دارند، مانند `clawrouter/openai/...`، `clawrouter/anthropic/...`، یا `clawrouter/google/...`. اگر `agents.defaults.models` در پیکربندی شما یک allowlist است، هر ref انتخاب‌شدهٔ ClawRouter را به آن اضافه کنید.

* ### انتخاب یک مدل

bashCopy code
[code]
    openclaw models set clawrouter/<provider>/<model>
[/code]

همچنین می‌توانید یک مدل برگشتی را برای یک اجرا با `openclaw agent --model clawrouter/<provider>/<model> --message "..."` انتخاب کنید.

## کشف مدل

`GET /v1/catalog` منبع حقیقت است. OpenClaw فهرست دوم و ثابتی از مدل‌های ClawRouter منتشر نمی‌کند. مدلی که در ClawRouter پیکربندی شده باشد زمانی ظاهر می‌شود که:

  * policy اعتبارنامه ارائه‌دهندهٔ آن را اعطا کند؛
  * اتصال ارائه‌دهنده فعال و آماده باشد؛
  * مدل فهرست، یک قابلیت LLM پشتیبانی‌شده را اعلام کند؛ و
  * فهرست، contract انتقالی را در معرض بگذارد که Plugin از آن پشتیبانی می‌کند.


بنابراین افزودن مدل دیگری به یک ارائه‌دهندهٔ ClawRouter پشتیبانی‌شده به انتشار OpenClaw یا Plugin ارائه‌دهندهٔ دیگری نیاز ندارد. تازه‌سازی بعدی فهرست آن را کشف می‌کند. مدلی که به یک wire protocol جدید نیاز دارد، پیش از آن‌که OpenClaw آن را اعلام کند به پشتیبانی در Plugin ClawRouter نیاز دارد.

## Protocol و Pluginهای ارائه‌دهنده

نیازی نیست Plugin احراز هویت هر شرکت بالادستی را نصب کنید. ClawRouter مالک اعتبارنامه‌های بالادستی است؛ فهرست آن به OpenClaw می‌گوید از کدام انتقال استفاده کند. این Plugin از موارد زیر پشتیبانی می‌کند:

مسیر فهرست | انتقال OpenClaw  
---|---  
چت سازگار با OpenAI | `openai-completions`  
Responses سازگار با OpenAI | `openai-responses`  
Messages بومی Anthropic | `anthropic-messages`  
جریان‌دهی بومی Google Gemini | `google-generative-ai`  
  
این Plugin همچنین policyهای بازپخش و tool-schema منطبق را برای آن خانواده‌ها اعمال می‌کند. ردیف‌های فهرست که از قالب request/stream دیگری استفاده می‌کنند، عمدا به‌عنوان مدل‌های متنی OpenClaw اعلام نمی‌شوند. به‌جای ارسال payload ناسازگار، آن ارائه‌دهنده‌ها را در ClawRouter به یکی از contractهای پشتیبانی‌شده عادی‌سازی کنید.

## سهمیه‌ها و مصرف

پاسخ `/v1/usage` در ClawRouter سطوح معمول مصرف ارائه‌دهنده در OpenClaw را تغذیه می‌کند. `/status` و وضعیت‌های مرتبط dashboard، زمانی که کلید محدودیت دارد، پنجرهٔ بودجهٔ ماهانه را به‌همراه مجموع request، token و هزینه نشان می‌دهند. کلیدهای بدون اندازه‌گیری همچنان مصرف تجمیعی را بدون پنجرهٔ درصدی نشان می‌دهند.

جست‌وجوی سهمیه از همان کلید محدودشده‌ای استفاده می‌کند که برای کشف مدل به کار می‌رود. شکست در جست‌وجوی سهمیه اجرای مدل را مسدود نمی‌کند.

نمای زنده را با این دستور بررسی کنید:

bashCopy code
[code]
    openclaw status --usageopenclaw models status
[/code]

همان نمای ارائه‌دهنده برای `/status` در chat و UI مصرف OpenClaw در دسترس است. بودجه در سطح policy است، بنابراین requestهایی که توسط client دیگری با همان policy ClawRouter انجام می‌شوند می‌توانند درصد باقی‌مانده را تغییر دهند.

## عیب‌یابی

نشانه | بررسی  
---|---  
هیچ مدل ClawRouter وجود ندارد | تایید کنید Plugin فعال است و توسط `plugins.allow` مجاز شده، سپس بررسی کنید که اعتبارنامه فعال است و دست‌کم یک ارائه‌دهندهٔ آماده را اعطا می‌کند.  
یک مدل ClawRouter پیکربندی‌شده وجود ندارد | قابلیت و قالب مسیر آن را در `/v1/catalog` بررسی کنید. contractهای انتقال پشتیبانی‌نشده عمدا فیلتر می‌شوند.  
`Unknown model: clawrouter/...` | زمانی که آن map پیکربندی به‌عنوان allowlist استفاده می‌شود، ref دقیق فهرست را به `agents.defaults.models` اضافه کنید.  
`401` یا `403` از فهرست یا مصرف | اعتبارنامهٔ ClawRouter را دوباره صادر یا دوباره محدود کنید؛ OpenClaw به کلیدهای ارائه‌دهندهٔ بالادستی fallback نمی‌کند.  
فراخوانی مدل پس از کشف شکست می‌خورد | اتصال ارائه‌دهنده و سلامت بالادستی را در ClawRouter بررسی کنید، سپس پس از بازیابی وضعیت آمادگی آن دوباره تلاش کنید.  
مصرف مجموع دارد اما درصد ندارد | policy بدون اندازه‌گیری است؛ برای نمایش پنجرهٔ درصدی، یک بودجهٔ ماهانه در ClawRouter اضافه کنید.  
  
## رفتار امنیتی

  * کشف فهرست به کلید proxy پیکربندی‌شده محدود است و برای هر کلید cache می‌شود.
  * کلید proxy فقط هنگام ارسال request پیوست می‌شود؛ در metadata مدل ذخیره نمی‌شود.
  * شناسه‌های مدل بومی Anthropic و Gemini فقط هنگام ارسال به شناسه‌های بالادستی خود بازنویسی می‌شوند.
  * ردیف‌های فهرست پشتیبانی‌نشده یا اعطاشده‌نشده به‌صورت fail closed عمل می‌کنند و قابل انتخاب نیستند.


## مرتبط

[**ارائه‌دهنده‌های مدل** پیکربندی ارائه‌دهنده و انتخاب مدل. ](</fa/concepts/model-providers>) [**ردیابی مصرف** سطوح مصرف و وضعیت OpenClaw. ](</fa/concepts/usage-tracking>)

Was this useful?YesNo

Open issue