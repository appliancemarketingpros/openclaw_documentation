---
title: DNS
source_url: https://docs.openclaw.ai/fa/cli/dns
scraped_at: 2026-05-25
---

# `openclaw dns`

ابزارهای کمکی DNS برای کشف گستره‌وسیع (Tailscale + CoreDNS). در حال حاضر بر macOS + Homebrew CoreDNS متمرکز است.

مرتبط:

  * کشف Gateway: [کشف](</fa/gateway/discovery>)
  * پیکربندی کشف گستره‌وسیع: [پیکربندی](</fa/gateway/configuration>)


## راه‌اندازی

bashCopy code
[code]
    openclaw dns setupopenclaw dns setup --domain openclaw.internalopenclaw dns setup --apply
[/code]

## `dns setup`

برنامه‌ریزی یا اعمال راه‌اندازی CoreDNS برای کشف DNS-SD تک‌پخشی.

گزینه‌ها:

  * `--domain <domain>`: دامنه کشف گستره‌وسیع (برای مثال `openclaw.internal`)
  * `--apply`: نصب یا به‌روزرسانی پیکربندی CoreDNS و راه‌اندازی دوباره سرویس (به sudo نیاز دارد؛ فقط macOS)


آنچه نمایش می‌دهد:

  * دامنه کشف حل‌شده
  * مسیر فایل zone
  * IPهای tailnet فعلی
  * پیکربندی پیشنهادی کشف در `openclaw.json`
  * مقادیر نام‌سرور/دامنه Split DNS در Tailscale که باید تنظیم شوند


نکات:

  * بدون `--apply`، این دستور فقط یک ابزار کمکی برای برنامه‌ریزی است و راه‌اندازی پیشنهادی را چاپ می‌کند.
  * اگر `--domain` حذف شود، OpenClaw از `discovery.wideArea.domain` در پیکربندی استفاده می‌کند.
  * `--apply` در حال حاضر فقط از macOS پشتیبانی می‌کند و Homebrew CoreDNS را انتظار دارد.
  * `--apply` در صورت نیاز فایل zone را راه‌اندازی اولیه می‌کند، از وجود قطعه import در CoreDNS اطمینان می‌دهد و سرویس brew مربوط به `coredns` را دوباره راه‌اندازی می‌کند.


## مرتبط

  * [مرجع CLI](</fa/cli>)
  * [کشف](</fa/gateway/discovery>)


Was this useful?YesNo