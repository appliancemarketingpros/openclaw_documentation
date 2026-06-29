---
title: قراردادهای جای‌نگهدار محرمانه
source_url: https://docs.openclaw.ai/fa/reference/secret-placeholder-conventions
scraped_at: 2026-06-29
---

Get started

# قراردادهای جای‌نگهدار رازها

از جای‌نگهدارهایی استفاده کنید که برای انسان خوانا باشند اما شبیه رازهای واقعی به نظر نرسند.

## سبک پیشنهادی

  * مقادیر توصیفی مانند `example-openai-key-not-real` یا `example-discord-bot-token` را ترجیح دهید.
  * برای قطعه‌کدهای shell، `${OPENAI_API_KEY}` را به رشته‌های درون‌خطی شبیه token ترجیح دهید.
  * مثال‌ها را آشکارا ساختگی و محدود به هدف نگه دارید (provider، channel، نوع auth).


## از این الگوها در مستندات پرهیز کنید

  * متن لفظی سربرگ یا پابرگ کلید خصوصی PEM.
  * پیشوندهایی که شبیه اعتبارنامه‌های زنده هستند، برای مثال `sk-...`، `xoxb-...`، `AKIA...`.
  * tokenهای bearer واقع‌نما که از لاگ‌های runtime کپی شده‌اند.


## مثال

bashCopy code
[code]
    # خوبexport OPENAI_API_KEY="example-openai-key-not-real" # بهتر (وقتی مستند درباره اتصال env است)export OPENAI_API_KEY="${OPENAI_API_KEY}"
[/code]

Was this useful?YesNo

Open issue