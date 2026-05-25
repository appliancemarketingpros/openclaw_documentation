---
title: داشبورد
source_url: https://docs.openclaw.ai/fa/cli/dashboard
scraped_at: 2026-05-25
---

# `openclaw dashboard`

رابط کاربری کنترل را با استفاده از احراز هویت فعلی خود باز کنید.

bashCopy code
[code]
    openclaw dashboardopenclaw dashboard --no-open
[/code]

یادداشت‌ها:

  * `dashboard` در صورت امکان SecretRefهای پیکربندی‌شده‌ی `gateway.auth.token` را resolve می‌کند.
  * `dashboard` از `gateway.tls.enabled` پیروی می‌کند: Gatewayهای دارای TLS فعال، URLهای رابط کاربری کنترل را با `https://` چاپ/باز می‌کنند و از طریق `wss://` متصل می‌شوند.
  * اگر تحویل از طریق کلیپ‌بورد/مرورگر برای URL داشبوردِ احراز هویت‌شده با توکن ناموفق باشد، `dashboard` یک راهنمای امن برای احراز هویت دستی ثبت می‌کند که از `OPENCLAW_GATEWAY_TOKEN`، `gateway.auth.token`، و کلید fragment یعنی `token` نام می‌برد، بدون آنکه مقدار توکن را چاپ کند.
  * برای توکن‌های مدیریت‌شده با SecretRef (resolve‌شده یا resolveنشده)، `dashboard` یک URL بدون توکن را چاپ/کپی/باز می‌کند تا از افشای اسرار خارجی در خروجی ترمینال، تاریخچه کلیپ‌بورد، یا آرگومان‌های اجرای مرورگر جلوگیری شود.
  * اگر `gateway.auth.token` با SecretRef مدیریت می‌شود اما در این مسیر فرمان resolve نشده باشد، فرمان به‌جای جاسازی یک placeholder نامعتبر برای توکن، یک URL بدون توکن و راهنمای اصلاح صریح چاپ می‌کند.


## مرتبط

  * [مرجع CLI](</fa/cli>)
  * [داشبورد](</fa/web/dashboard>)


Was this useful?YesNo