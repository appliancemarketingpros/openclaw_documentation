---
title: Perplexity
source_url: https://docs.openclaw.ai/fa/providers/perplexity-provider
scraped_at: 2026-05-25
---

Plugin Perplexity قابلیت‌های جست‌وجوی وب را از طریق Perplexity Search API یا Perplexity Sonar از راه OpenRouter فراهم می‌کند.

ویژگی | مقدار  
---|---  
نوع | ارائه‌دهنده جست‌وجوی وب (نه ارائه‌دهنده مدل)  
احراز هویت | `PERPLEXITY_API_KEY` (مستقیم) یا `OPENROUTER_API_KEY` (از طریق OpenRouter)  
مسیر پیکربندی | `plugins.entries.perplexity.config.webSearch.apiKey`  
  
## شروع کار

* ### تنظیم کلید API

جریان تعاملی پیکربندی جست‌وجوی وب را اجرا کنید:

bashCopy code
[code]
    openclaw configure --section web
[/code]

یا کلید را مستقیماً تنظیم کنید:

bashCopy code
[code]
    openclaw config set plugins.entries.perplexity.config.webSearch.apiKey "pplx-xxxxxxxxxxxx"
[/code]

* ### شروع جست‌وجو

پس از پیکربندی کلید، عامل به‌طور خودکار از Perplexity برای جست‌وجوهای وب استفاده می‌کند. هیچ مرحله اضافی لازم نیست.

## حالت‌های جست‌وجو

Plugin بر اساس پیشوند کلید API، مسیر انتقال را به‌طور خودکار انتخاب می‌کند:

### API بومی Perplexity (pplx-)

وقتی کلید شما با `pplx-` شروع می‌شود، OpenClaw از API بومی Perplexity Search استفاده می‌کند. این مسیر انتقال نتایج ساختاریافته برمی‌گرداند و از فیلترهای دامنه، زبان و تاریخ پشتیبانی می‌کند (گزینه‌های فیلتر کردن را در پایین ببینید).

### OpenRouter / Sonar (sk-or-)

وقتی کلید شما با `sk-or-` شروع می‌شود، OpenClaw با استفاده از مدل Perplexity Sonar از مسیر OpenRouter عبور می‌کند. این مسیر انتقال پاسخ‌های ساخته‌شده با هوش مصنوعی را همراه با ارجاع‌ها برمی‌گرداند.

پیشوند کلید | مسیر انتقال | قابلیت‌ها  
---|---|---  
`pplx-` | API بومی Perplexity Search | نتایج ساختاریافته، فیلترهای دامنه/زبان/تاریخ  
`sk-or-` | OpenRouter (Sonar) | پاسخ‌های ساخته‌شده با هوش مصنوعی همراه با ارجاع‌ها  
  
## فیلتر کردن API بومی

هنگام استفاده از API بومی Perplexity، جست‌وجوها از فیلترهای زیر پشتیبانی می‌کنند:

فیلتر | توضیح | مثال  
---|---|---  
کشور | کد دوحرفی کشور | `us`, `de`, `jp`  
زبان | کد زبان ISO 639-1 | `en`, `fr`, `zh`  
بازه تاریخ | پنجره تازگی | `day`, `week`, `month`, `year`  
فیلترهای دامنه | فهرست مجاز یا فهرست ممنوع (حداکثر ۲۰ دامنه) | `example.com`  
بودجه محتوا | محدودیت‌های توکن برای هر پاسخ / هر صفحه | `max_tokens`, `max_tokens_per_page`  
  
## پیکربندی پیشرفته

متغیر محیطی برای فرایندهای daemon

اگر OpenClaw Gateway به‌صورت daemon (launchd/systemd) اجرا می‌شود، مطمئن شوید `PERPLEXITY_API_KEY` برای آن فرایند در دسترس است.

راه‌اندازی پروکسی OpenRouter

اگر ترجیح می‌دهید جست‌وجوهای Perplexity را از طریق OpenRouter مسیریابی کنید، به‌جای کلید بومی Perplexity، یک `OPENROUTER_API_KEY` (با پیشوند `sk-or-`) تنظیم کنید. OpenClaw پیشوند را تشخیص می‌دهد و به‌طور خودکار به مسیر انتقال Sonar تغییر می‌کند.

## مرتبط

[**ابزار جست‌وجوی Perplexity** اینکه عامل چگونه جست‌وجوهای Perplexity را فراخوانی می‌کند و نتایج را تفسیر می‌کند. ](</fa/tools/perplexity-search>) [**مرجع پیکربندی** مرجع کامل پیکربندی، شامل ورودی‌های Plugin. ](</fa/gateway/configuration-reference>)

Was this useful?YesNo