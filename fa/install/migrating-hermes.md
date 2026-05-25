---
title: مهاجرت از Hermes
source_url: https://docs.openclaw.ai/fa/install/migrating-hermes
scraped_at: 2026-05-25
---

OpenClaw وضعیت Hermes را از طریق یک ارائه‌دهندهٔ مهاجرتِ همراه وارد می‌کند. این ارائه‌دهنده پیش از تغییر وضعیت، همه‌چیز را پیش‌نمایش می‌کند، اسرار را در برنامه‌ها و گزارش‌ها پنهان‌سازی می‌کند، و پیش از اعمال، یک پشتیبانِ تأییدشده می‌سازد.

## دو روش برای وارد کردن

### جادوگر راه‌اندازی اولیه

سریع‌ترین مسیر. جادوگر، Hermes را در `~/.hermes` تشخیص می‌دهد و پیش از اعمال، یک پیش‌نمایش نشان می‌دهد.

bashCopy code
[code]
    openclaw onboard --flow import
[/code]

یا به یک منبع مشخص اشاره کنید:

bashCopy code
[code]
    openclaw onboard --import-from hermes --import-source ~/.hermes
[/code]

### CLI

برای اجراهای اسکریپتی یا تکرارپذیر از `openclaw migrate` استفاده کنید. برای مرجع کامل، [`openclaw migrate`](</fa/cli/migrate>) را ببینید.

bashCopy code
[code]
    openclaw migrate hermes --dry-run    # preview onlyopenclaw migrate apply hermes --yes  # apply with confirmation skipped
[/code]

وقتی Hermes بیرون از `~/.hermes` قرار دارد، `--from <path>` را اضافه کنید.

## چه چیزهایی وارد می‌شود

پیکربندی مدل

  * انتخاب مدل پیش‌فرض از `config.yaml` در Hermes.
  * ارائه‌دهندگان مدل پیکربندی‌شده و نقاط پایانی سفارشیِ سازگار با OpenAI از `providers` و `custom_providers`.

سرورهای MCP

تعریف‌های سرور MCP از `mcp_servers` یا `mcp.servers`.

فایل‌های workspace

  * `SOUL.md` و `AGENTS.md` در workspace عامل OpenClaw کپی می‌شوند.
  * `memories/MEMORY.md` و `memories/USER.md` به‌جای بازنویسی، به فایل‌های حافظهٔ متناظر OpenClaw **افزوده** می‌شوند.

پیکربندی حافظه

پیش‌فرض‌های پیکربندی حافظه برای حافظهٔ فایلی OpenClaw. ارائه‌دهندگان حافظهٔ خارجی مانند Honcho به‌عنوان موارد بایگانی یا نیازمند بازبینی دستی ثبت می‌شوند تا بتوانید آن‌ها را آگاهانه منتقل کنید.

Skills

Skills دارای فایل `SKILL.md` زیر `skills/<name>/` همراه با مقدارهای پیکربندیِ مختص هر skill از `skills.config` کپی می‌شوند.

کلیدهای API (اختیاری)

برای وارد کردن کلیدهای پشتیبانی‌شدهٔ `.env`، `--include-secrets` را تنظیم کنید: `OPENAI_API_KEY`، `ANTHROPIC_API_KEY`، `OPENROUTER_API_KEY`، `GOOGLE_API_KEY`، `GEMINI_API_KEY`، `GROQ_API_KEY`، `XAI_API_KEY`، `MISTRAL_API_KEY`، `DEEPSEEK_API_KEY`. بدون این flag، اسرار هرگز کپی نمی‌شوند.

## چه چیزهایی فقط در بایگانی می‌ماند

ارائه‌دهنده این موارد را برای بازبینی دستی در دایرکتوری گزارش مهاجرت کپی می‌کند، اما آن‌ها را در پیکربندی زنده یا اعتبارنامه‌های زندهٔ OpenClaw بارگذاری **نمی‌کند** :

  * `plugins/`
  * `sessions/`
  * `logs/`
  * `cron/`
  * `mcp-tokens/`
  * `auth.json`
  * `state.db`


OpenClaw از اجرای خودکار این وضعیت یا اعتماد خودکار به آن خودداری می‌کند، زیرا قالب‌ها و فرض‌های اعتماد می‌توانند بین سیستم‌ها تغییر کنند. پس از بازبینی بایگانی، هرچه نیاز دارید را دستی منتقل کنید.

## جریان پیشنهادی

* ### پیش‌نمایش برنامه

bashCopy code
[code]
    openclaw migrate hermes --dry-run
[/code]

برنامه هر چیزی را که تغییر خواهد کرد فهرست می‌کند، از جمله تعارض‌ها، موارد ردشده، و هر مورد حساس. خروجی برنامه، کلیدهای تو در توی شبیه به secret را پنهان‌سازی می‌کند.

* ### اعمال همراه با پشتیبان

bashCopy code
[code]
    openclaw migrate apply hermes --yes
[/code]

OpenClaw پیش از اعمال، یک پشتیبان می‌سازد و آن را تأیید می‌کند. اگر لازم است کلیدهای API وارد شوند، `--include-secrets` را اضافه کنید.

* ### اجرای doctor

bashCopy code
[code]
    openclaw doctor
[/code]

[Doctor](</fa/gateway/doctor>) هر مهاجرت پیکربندیِ در انتظار را دوباره اعمال می‌کند و مشکلات ایجادشده هنگام وارد کردن را بررسی می‌کند.

* ### راه‌اندازی مجدد و تأیید

bashCopy code
[code]
    openclaw gateway restartopenclaw status
[/code]

تأیید کنید Gateway سالم است و مدل، حافظه و skills واردشدهٔ شما بارگذاری شده‌اند.

## مدیریت تعارض

وقتی برنامه تعارض گزارش می‌کند (یک فایل یا مقدار پیکربندی از قبل در مقصد وجود دارد)، اعمال از ادامه دادن خودداری می‌کند.

برای نصب تازهٔ OpenClaw، تعارض‌ها غیرمعمول هستند. معمولاً زمانی ظاهر می‌شوند که وارد کردن را روی راه‌اندازی‌ای دوباره اجرا می‌کنید که از قبل ویرایش‌های کاربر دارد.

اگر تعارضی در میانهٔ اعمال رخ دهد (برای مثال، یک رقابت غیرمنتظره روی فایل پیکربندی)، Hermes موارد پیکربندی وابستهٔ باقی‌مانده را به‌جای نوشتن ناقص، با دلیل `blocked by earlier apply conflict` به‌صورت `skipped` علامت‌گذاری می‌کند. گزارش مهاجرت هر مورد مسدودشده را ثبت می‌کند تا بتوانید تعارض اصلی را رفع کنید و وارد کردن را دوباره اجرا کنید.

## اسرار

اسرار به‌صورت پیش‌فرض هرگز وارد نمی‌شوند.

  * ابتدا `openclaw migrate apply hermes --yes` را اجرا کنید تا وضعیت غیرمحرمانه وارد شود.
  * اگر همچنین می‌خواهید کلیدهای پشتیبانی‌شدهٔ `.env` کپی شوند، با `--include-secrets` دوباره اجرا کنید.
  * برای اعتبارنامه‌های مدیریت‌شده با SecretRef، پس از کامل شدن وارد کردن، منبع SecretRef را پیکربندی کنید.


## خروجی JSON برای خودکارسازی

bashCopy code
[code]
    openclaw migrate hermes --dry-run --jsonopenclaw migrate apply hermes --json --yes
[/code]

با `--json` و بدون `--yes`، apply برنامه را چاپ می‌کند و وضعیت را تغییر نمی‌دهد. این امن‌ترین حالت برای CI و اسکریپت‌های مشترک است.

## عیب‌یابی

اعمال به‌دلیل تعارض‌ها خودداری می‌کند

خروجی برنامه را بررسی کنید. هر تعارض مسیر منبع و مقصد موجود را مشخص می‌کند. برای هر مورد تصمیم بگیرید که آن را رد کنید، مقصد را ویرایش کنید، یا با `--overwrite` دوباره اجرا کنید.

Hermes بیرون از ~/.hermes قرار دارد

`--from /actual/path` (CLI) یا `--import-source /actual/path` (راه‌اندازی اولیه) را پاس دهید.

راه‌اندازی اولیه از وارد کردن روی یک راه‌اندازی موجود خودداری می‌کند

وارد کردن از راه‌اندازی اولیه به یک راه‌اندازی تازه نیاز دارد. یا وضعیت را بازنشانی کنید و دوباره راه‌اندازی اولیه را انجام دهید، یا مستقیماً از `openclaw migrate apply hermes` استفاده کنید که از `--overwrite` و کنترل صریح پشتیبان پشتیبانی می‌کند.

کلیدهای API وارد نشدند

`--include-secrets` لازم است، و فقط کلیدهای فهرست‌شده در بالا شناسایی می‌شوند. متغیرهای دیگر در `.env` نادیده گرفته می‌شوند.

## مرتبط

  * [`openclaw migrate`](</fa/cli/migrate>): مرجع کامل CLI، قرارداد plugin، و شکل‌های JSON.
  * [راه‌اندازی اولیه](</fa/cli/onboard>): جریان جادوگر و flagهای غیرتعاملی.
  * [مهاجرت](</fa/install/migrating>): انتقال یک نصب OpenClaw بین ماشین‌ها.
  * [Doctor](</fa/gateway/doctor>): بررسی سلامت پس از مهاجرت.
  * [Workspace عامل](</fa/concepts/agent-workspace>): محل قرارگیری `SOUL.md`، `AGENTS.md` و فایل‌های حافظه.


Was this useful?YesNo