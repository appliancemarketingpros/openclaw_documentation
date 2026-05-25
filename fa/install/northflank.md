---
title: Northflank
source_url: https://docs.openclaw.ai/fa/install/northflank
scraped_at: 2026-05-25
---

# Northflank

OpenClaw را با یک الگوی یک‌کلیکی روی Northflank مستقر کنید و از طریق رابط کاربری کنترل وب به آن دسترسی داشته باشید. این ساده‌ترین مسیر «بدون ترمینال روی سرور» است: Northflank، Gateway را برای شما اجرا می‌کند.

## چگونه شروع کنیم

  1. برای باز کردن الگو، روی [استقرار OpenClaw](<https://northflank.com/stacks/deploy-openclaw>) کلیک کنید.
  2. اگر از قبل حساب ندارید، یک [حساب در Northflank](<https://app.northflank.com/signup>) بسازید.
  3. روی **همین حالا OpenClaw را مستقر کنید** کلیک کنید.
  4. متغیر محیطی الزامی را تنظیم کنید: `OPENCLAW_GATEWAY_TOKEN` (از یک مقدار تصادفی قوی استفاده کنید).
  5. برای ساخت و اجرای الگوی OpenClaw، روی **استقرار stack** کلیک کنید.
  6. صبر کنید تا استقرار کامل شود، سپس روی **مشاهده منابع** کلیک کنید.
  7. سرویس OpenClaw را باز کنید.
  8. URL عمومی OpenClaw را در `/openclaw` باز کنید و با استفاده از راز مشترک پیکربندی‌شده متصل شوید. این الگو به‌طور پیش‌فرض از `OPENCLAW_GATEWAY_TOKEN` استفاده می‌کند؛ اگر آن را با احراز هویت رمز عبور جایگزین کردید، به‌جای آن از همان رمز عبور استفاده کنید.


## چه چیزی دریافت می‌کنید

  * Gateway میزبانی‌شده OpenClaw + رابط کاربری کنترل
  * ذخیره‌سازی پایدار از طریق Northflank Volume (`/data`) تا `openclaw.json`، `auth-profiles.json` برای هر عامل، وضعیت کانال/ارائه‌دهنده، نشست‌ها و فضای کاری پس از استقرارهای مجدد باقی بمانند


## اتصال یک کانال

برای دستورالعمل‌های راه‌اندازی کانال، از رابط کاربری کنترل در `/openclaw` استفاده کنید یا `openclaw onboard` را از طریق SSH اجرا کنید:

  * [Telegram](</fa/channels/telegram>) (سریع‌ترین گزینه — فقط یک توکن ربات)
  * [Discord](</fa/channels/discord>)
  * [همه کانال‌ها](</fa/channels>)


## مراحل بعدی

  * راه‌اندازی کانال‌های پیام‌رسانی: [کانال‌ها](</fa/channels>)
  * پیکربندی Gateway: [پیکربندی Gateway](</fa/gateway/configuration>)
  * به‌روز نگه داشتن OpenClaw: [به‌روزرسانی](</fa/install/updating>)


Was this useful?YesNo