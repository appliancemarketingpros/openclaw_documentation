---
title: شروع به کار
source_url: https://docs.openclaw.ai/fa/start/getting-started
scraped_at: 2026-05-25
---

OpenClaw را نصب کنید، راه‌اندازی اولیه را اجرا کنید و با دستیار هوش مصنوعی خود گفت‌وگو کنید؛ همه در حدود ۵ دقیقه. در پایان، یک Gateway در حال اجرا، احراز هویت پیکربندی‌شده و یک نشست گفت‌وگوی فعال خواهید داشت.

## آنچه نیاز دارید

  * **Node.js** — Node 24 توصیه می‌شود (Node 22.16+ نیز پشتیبانی می‌شود)
  * **یک کلید API** از یک ارائه‌دهنده مدل (Anthropic، OpenAI، Google و غیره) — راه‌اندازی اولیه از شما آن را می‌خواهد


## راه‌اندازی سریع

* ### نصب OpenClaw

### macOS / Linux

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash
[/code]

![فرایند اسکریپت نصب](/assets/install-script.svg)

### Windows (PowerShell)

powershellCopy code
[code]
    iwr -useb https://openclaw.ai/install.ps1 | iex
[/code]

* ### اجرای راه‌اندازی اولیه

bashCopy code
[code]
    openclaw onboard --install-daemon
[/code]

این راهنما شما را در انتخاب یک ارائه‌دهنده مدل، تنظیم کلید API، و پیکربندی Gateway همراهی می‌کند. حدود ۲ دقیقه طول می‌کشد.

برای مرجع کامل، [راه‌اندازی اولیه (CLI)](</fa/start/wizard>) را ببینید.

* ### بررسی کنید Gateway در حال اجرا است

bashCopy code
[code]
    openclaw gateway status
[/code]

باید ببینید که Gateway روی درگاه 18789 گوش می‌دهد.

* ### باز کردن داشبورد

bashCopy code
[code]
    openclaw dashboard
[/code]

این کار Control UI را در مرورگر شما باز می‌کند. اگر بارگذاری شود، همه چیز کار می‌کند.

* ### ارسال اولین پیام

در گفت‌وگوی Control UI یک پیام بنویسید و باید یک پاسخ هوش مصنوعی دریافت کنید.

می‌خواهید به‌جای آن از گوشی خود گفت‌وگو کنید؟ سریع‌ترین کانال برای راه‌اندازی [Telegram](</fa/channels/telegram>) است (فقط یک توکن بات). برای همه گزینه‌ها، [کانال‌ها](</fa/channels>) را ببینید.

پیشرفته: اتصال یک ساخت سفارشی Control UI

اگر یک ساخت داشبورد بومی‌سازی‌شده یا سفارشی نگه‌داری می‌کنید، `gateway.controlUi.root` را به پوشه‌ای اشاره دهید که دارایی‌های ایستای ساخته‌شده و `index.html` شما را در خود دارد.

bashCopy code
[code]
    mkdir -p "$HOME/.openclaw/control-ui-custom"# Copy your built static files into that directory.
[/code]

سپس تنظیم کنید:

jsonCopy code
[code]
    {"gateway": {  "controlUi": {    "enabled": true,    "root": "$HOME/.openclaw/control-ui-custom"  }}}
[/code]

Gateway را دوباره راه‌اندازی کنید و داشبورد را دوباره باز کنید:

bashCopy code
[code]
    openclaw gateway restartopenclaw dashboard
[/code]

## گام بعدی

[**اتصال یک کانال** Discord، Feishu، iMessage، Matrix، Microsoft Teams، Signal، Slack، Telegram، WhatsApp، Zalo و موارد بیشتر. ](</fa/channels>) [**جفت‌سازی و ایمنی** کنترل کنید چه کسی می‌تواند به عامل شما پیام بدهد. ](</fa/channels/pairing>) [**پیکربندی Gateway** مدل‌ها، ابزارها، sandbox، و تنظیمات پیشرفته. ](</fa/gateway/configuration>) [**مرور ابزارها** مرورگر، exec، جست‌وجوی وب، Skills، و pluginها. ](</fa/tools>)

پیشرفته: متغیرهای محیطی

اگر OpenClaw را به‌عنوان یک حساب سرویس اجرا می‌کنید یا مسیرهای سفارشی می‌خواهید:

  * `OPENCLAW_HOME` — پوشه خانگی برای رفع مسیرهای داخلی
  * `OPENCLAW_STATE_DIR` — بازنویسی پوشه وضعیت
  * `OPENCLAW_CONFIG_PATH` — بازنویسی مسیر فایل پیکربندی


مرجع کامل: [متغیرهای محیطی](</fa/help/environment>).

## مرتبط

  * [نمای کلی نصب](</fa/install>)
  * [نمای کلی کانال‌ها](</fa/channels>)
  * [راه‌اندازی](</fa/start/setup>)


Was this useful?YesNo