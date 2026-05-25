---
title: پیکربندی
source_url: https://docs.openclaw.ai/fa/cli/configure
scraped_at: 2026-05-25
---

# `openclaw configure`

درخواست تعاملی برای تغییرات هدفمند در یک راه‌اندازی موجود: اعتبارنامه‌ها، دستگاه‌ها، پیش‌فرض‌های عامل، Gateway، کانال‌ها، Pluginها، Skills، و بررسی‌های سلامت.

از `openclaw onboard` برای مسیر کامل و راهنمای اجرای نخست، از `openclaw setup` فقط برای پیکربندی/فضای کاری پایه، و از `openclaw channels add` زمانی استفاده کنید که فقط به راه‌اندازی حساب کانال نیاز دارید.

وقتی configure از یک گزینه احراز هویت ارائه‌دهنده شروع می‌شود، انتخاب‌گرهای مدل پیش‌فرض و فهرست مجاز به‌صورت خودکار آن ارائه‌دهنده را ترجیح می‌دهند. برای ارائه‌دهندگان جفت‌شده مانند Volcengine و BytePlus، همین ترجیح با گونه‌های طرح کدنویسی آن‌ها نیز مطابقت دارد (`volcengine-plan/*`، `byteplus-plan/*`). اگر فیلتر ارائه‌دهنده ترجیحی یک فهرست خالی تولید کند، configure به‌جای نمایش یک انتخاب‌گر خالی، به کاتالوگ بدون فیلتر برمی‌گردد.

برای جست‌وجوی وب، `openclaw configure --section web` به شما امکان می‌دهد یک ارائه‌دهنده را انتخاب کنید و اعتبارنامه‌های آن را پیکربندی کنید. برخی ارائه‌دهندگان همچنین درخواست‌های پیگیری ویژه همان ارائه‌دهنده را نمایش می‌دهند:

  * **Grok** می‌تواند راه‌اندازی اختیاری `x_search` را با همان `XAI_API_KEY` پیشنهاد کند و به شما اجازه دهد یک مدل `x_search` انتخاب کنید.
  * **Kimi** می‌تواند منطقه API مربوط به Moonshot (`api.moonshot.ai` در برابر `api.moonshot.cn`) و مدل پیش‌فرض جست‌وجوی وب Kimi را بپرسد.


مرتبط:

  * مرجع پیکربندی Gateway: [پیکربندی](</fa/gateway/configuration>)
  * CLI پیکربندی: [پیکربندی](</fa/cli/config>)


## گزینه‌ها

  * `--section <section>`: فیلتر بخش قابل تکرار


بخش‌های موجود:

  * `workspace`
  * `model`
  * `web`
  * `gateway`
  * `daemon`
  * `channels`
  * `plugins`
  * `skills`
  * `health`


نکات:

  * انتخاب محل اجرای Gateway همیشه `gateway.mode` را به‌روزرسانی می‌کند. اگر فقط همین را نیاز دارید، می‌توانید بدون بخش‌های دیگر «ادامه» را انتخاب کنید.
  * پس از نوشتن پیکربندی محلی، configure وقتی مسیر راه‌اندازی انتخاب‌شده به Pluginهای قابل دانلود نیاز داشته باشد، آن‌ها را نصب می‌کند. پیکربندی Gateway راه دور بسته‌های Plugin محلی را نصب نمی‌کند.
  * سرویس‌های کانال‌محور (Slack/Discord/Matrix/Microsoft Teams) هنگام راه‌اندازی برای فهرست‌های مجاز کانال/اتاق درخواست می‌دهند. می‌توانید نام‌ها یا شناسه‌ها را وارد کنید؛ ویزارد در صورت امکان نام‌ها را به شناسه‌ها تبدیل می‌کند.
  * اگر مرحله نصب daemon را اجرا کنید، احراز هویت توکنی به یک توکن نیاز داشته باشد، و `gateway.auth.token` با SecretRef مدیریت شود، configure مقدار SecretRef را اعتبارسنجی می‌کند اما مقادیر توکن متن ساده حل‌شده را در فراداده محیط سرویس supervisor ذخیره نمی‌کند.
  * اگر احراز هویت توکنی به یک توکن نیاز داشته باشد و SecretRef توکن پیکربندی‌شده حل نشده باشد، configure نصب daemon را با راهنمایی اصلاحی قابل اقدام مسدود می‌کند.
  * اگر هم `gateway.auth.token` و هم `gateway.auth.password` پیکربندی شده باشند و `gateway.auth.mode` تنظیم نشده باشد، configure نصب daemon را تا زمانی که mode صراحتا تنظیم شود مسدود می‌کند.


## مثال‌ها

bashCopy code
[code]
    openclaw configureopenclaw configure --section webopenclaw configure --section model --section channelsopenclaw configure --section gateway --section daemon
[/code]

## مرتبط

  * [مرجع CLI](</fa/cli>)
  * [پیکربندی](</fa/gateway/configuration>)


Was this useful?YesNo