---
title: گزارش‌ها
source_url: https://docs.openclaw.ai/fa/cli/logs
scraped_at: 2026-05-25
---

# `openclaw logs`

لاگ‌های فایل Gateway را از طریق RPC از انتهای فایل بخوانید (در حالت راه دور کار می‌کند).

مرتبط:

  * نمای کلی لاگ‌گیری: [لاگ‌گیری](</fa/logging>)
  * CLI مربوط به Gateway: [gateway](</fa/cli/gateway>)


## گزینه‌ها

  * `--limit <n>`: بیشترین تعداد خطوط لاگی که برگردانده می‌شود (پیش‌فرض `200`)
  * `--max-bytes <n>`: بیشترین تعداد بایت‌هایی که از فایل لاگ خوانده می‌شود (پیش‌فرض `250000`)
  * `--follow`: دنبال کردن جریان لاگ
  * `--interval <ms>`: فاصلهٔ نظرسنجی هنگام دنبال کردن (پیش‌فرض `1000`)
  * `--json`: رویدادهای JSON جداشده با خط را خروجی بده
  * `--plain`: خروجی متن ساده بدون قالب‌بندی سبک‌دهی‌شده
  * `--no-color`: غیرفعال کردن رنگ‌های ANSI
  * `--local-time`: نمایش زمان‌ها در منطقهٔ زمانی محلی شما


## گزینه‌های مشترک RPC مربوط به Gateway

`openclaw logs` همچنین فلگ‌های استاندارد کلاینت Gateway را می‌پذیرد:

  * `--url <url>`: نشانی WebSocket مربوط به Gateway
  * `--token <token>`: توکن Gateway
  * `--timeout <ms>`: مهلت زمانی بر حسب میلی‌ثانیه (پیش‌فرض `30000`)
  * `--expect-final`: وقتی فراخوانی Gateway با پشتیبانی عامل انجام می‌شود، منتظر پاسخ نهایی بمان


وقتی `--url` را پاس می‌دهید، CLI پیکربندی یا اعتبارنامه‌های محیطی را به‌طور خودکار اعمال نمی‌کند. اگر Gateway هدف به احراز هویت نیاز دارد، `--token` را صراحتاً اضافه کنید.

## نمونه‌ها

bashCopy code
[code]
    openclaw logsopenclaw logs --followopenclaw logs --follow --interval 2000openclaw logs --limit 500 --max-bytes 500000openclaw logs --jsonopenclaw logs --plainopenclaw logs --no-coloropenclaw logs --limit 500openclaw logs --local-timeopenclaw logs --follow --local-timeopenclaw logs --url ws://127.0.0.1:18789 --token "$OPENCLAW_GATEWAY_TOKEN"
[/code]

## یادداشت‌ها

  * از `--local-time` برای نمایش زمان‌ها در منطقهٔ زمانی محلی خود استفاده کنید.
  * اگر Gateway ضمنی local loopback درخواست جفت‌سازی کند، هنگام اتصال بسته شود، یا پیش از پاسخ دادن `logs.tail` مهلتش تمام شود، `openclaw logs` به‌طور خودکار به لاگ فایل Gateway پیکربندی‌شده برمی‌گردد. هدف‌های صریح `--url` از این جایگزین استفاده نمی‌کنند.
  * هنگام استفاده از `--follow`، قطع‌های گذرای gateway (بسته شدن WebSocket، پایان مهلت، قطع اتصال) باعث اتصال مجدد خودکار با پس‌روی نمایی می‌شود (تا ۸ تلاش مجدد، با سقف ۳۰ ثانیه بین تلاش‌ها). در هر تلاش مجدد، یک هشدار در stderr چاپ می‌شود و وقتی یک نظرسنجی موفق شود، اعلان `[logs] gateway reconnected` چاپ می‌شود. در حالت `--json`، هم هشدار تلاش مجدد و هم گذار اتصال مجدد به‌صورت رکوردهای `{"type":"notice"}` در stderr صادر می‌شوند. خطاهای غیرقابل‌بازیابی (شکست احراز هویت، پیکربندی نامعتبر) همچنان بلافاصله خارج می‌شوند.


## مرتبط

  * [مرجع CLI](</fa/cli>)
  * [لاگ‌گیری Gateway](</fa/gateway/logging>)


Was this useful?YesNo