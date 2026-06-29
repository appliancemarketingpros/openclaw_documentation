---
title: حالت‌های مجوز
source_url: https://docs.openclaw.ai/fa/tools/permission-modes
scraped_at: 2026-06-29
---

CapabilitiesTools

حالت‌های مجوز تعیین می‌کنند یک عامل پیش از اینکه بتواند فرمان‌های میزبان را اجرا کند، فایل‌ها را بنویسد، یا از یک هارنس بک‌اند دسترسی اضافی بخواهد، چه مقدار اختیار دارد. وقتی می‌خواهید OpenClaw ابتدا از فهرست‌های مجاز استفاده کند و سپس برای موارد ناموفق به بازبینی خودکار بومی Codex یا مسیر تأیید انسانی برود، با `tools.exec.mode: "auto"` شروع کنید.

## پیش‌فرض پیشنهادی

برای عامل‌های کدنویسی که به دسترسی مفید میزبان نیاز دارند، بدون اینکه هر مورد ناموفق به درخواست انسانی تبدیل شود، از `auto` استفاده کنید:

bashCopy code
[code]
    openclaw config set tools.exec.mode autoopenclaw approvals getopenclaw gateway restart
[/code]

سپس سیاست مؤثر را بررسی کنید:

bashCopy code
[code]
    openclaw exec-policy show
[/code]

در حالت `auto`، OpenClaw تطابق‌های قطعی فهرست مجاز را مستقیماً اجرا می‌کند. موارد ناموفق تأیید ابتدا از بازبین خودکار بومی OpenClaw عبور می‌کنند و سپس در صورت نیاز به مسیر پیکربندی‌شده تأیید انسانی برمی‌گردند.

## حالت‌های اجرای میزبان OpenClaw

`tools.exec.mode` سطح سیاست نرمال‌شده برای `exec` میزبان است.

حالت | رفتار | زمان استفاده  
---|---|---  
`deny` | اجرای میزبان را مسدود کن. | هیچ فرمان میزبانی مجاز نیست.  
`allowlist` | فقط فرمان‌های موجود در فهرست مجاز را اجرا کن. | یک مجموعه فرمان شناخته‌شده و ایمن دارید.  
`ask` | تطابق‌های فهرست مجاز را اجرا کن و برای موارد ناموفق بپرس. | انسان باید فرمان‌های جدید را بازبینی کند.  
`auto` | تطابق‌های فهرست مجاز را اجرا کن، سپس از بازبینی خودکار استفاده کن. | نشست‌های کدنویسی به دسترسی عملی و کنترل‌شده نیاز دارند.  
`full` | اجرای میزبان را بدون درخواست انجام بده. | این میزبان/نشست مورد اعتماد باید دروازه‌های تأیید را رد کند.  
  
برای سیاست کامل اجرای میزبان، فایل تأییدهای محلی، طرح‌واره فهرست مجاز، باینری‌های ایمن، و رفتار ارسال، [تأییدهای Exec](</fa/tools/exec-approvals>) را ببینید.

## نگاشت Codex Guardian

برای نشست‌های بومی سرور برنامه Codex، وقتی الزامات محلی Codex اجازه بدهند، `tools.exec.mode: "auto"` به تأییدهای بازبینی‌شده توسط Codex Guardian نگاشت می‌شود. OpenClaw معمولاً این‌ها را ارسال می‌کند:

فیلد Codex | مقدار معمول  
---|---  
`approvalPolicy` | `on-request`  
`approvalsReviewer` | `auto_review`  
`sandbox` | `workspace-write`  
  
در حالت `auto`، OpenClaw بازنویسی‌های قدیمی و ناایمن Codex مانند `approvalPolicy: "never"` یا `sandbox: "danger-full-access"` را حفظ نمی‌کند. فقط زمانی از `tools.exec.mode: "full"` استفاده کنید که عمداً وضعیت بدون تأیید را می‌خواهید.

برای راه‌اندازی سرور برنامه، ترتیب احراز هویت، و جزئیات زمان اجرای بومی Codex، [هارنس Codex](</fa/plugins/codex-harness>) را ببینید.

## مجوزهای هارنس ACPX

نشست‌های ACPX غیرتعاملی هستند، بنابراین نمی‌توانند روی درخواست مجوز TTY کلیک کنند. ACPX از تنظیمات جداگانه سطح هارنس زیر `plugins.entries.acpx.config` استفاده می‌کند:

تنظیم | مقدار رایج | معنی  
---|---|---  
`permissionMode` | `approve-reads` | فقط خواندن‌ها را خودکار تأیید کن.  
`permissionMode` | `approve-all` | نوشتن‌ها و فرمان‌های shell را خودکار تأیید کن.  
`permissionMode` | `deny-all` | همه درخواست‌های مجوز را رد کن.  
`nonInteractivePermissions` | `fail` | وقتی درخواست لازم باشد، متوقف شو.  
`nonInteractivePermissions` | `deny` | درخواست را رد کن و در صورت امکان ادامه بده.  
  
مجوزهای ACPX را جدا از تأییدهای exec در OpenClaw تنظیم کنید:

bashCopy code
[code]
    openclaw config set plugins.entries.acpx.config.permissionMode approve-allopenclaw config set plugins.entries.acpx.config.nonInteractivePermissions failopenclaw gateway restart
[/code]

از `approve-all` به‌عنوان معادل اضطراری ACPX برای یک نشست هارنس بدون درخواست استفاده کنید. برای جزئیات راه‌اندازی و حالت‌های شکست، [راه‌اندازی عامل‌های ACP](</fa/tools/acp-agents-setup#permission-configuration>) را ببینید.

## انتخاب یک حالت

هدف | پیکربندی  
---|---  
فرمان‌های میزبان را کاملاً مسدود کن | `tools.exec.mode: "deny"`  
فقط اجازه بده فرمان‌های شناخته‌شده و ایمن اجرا شوند | `tools.exec.mode: "allowlist"`  
برای هر شکل فرمان جدید از انسان بپرس | `tools.exec.mode: "ask"`  
پیش از انسان‌ها از بازبینی خودکار Codex/OpenClaw استفاده کن | `tools.exec.mode: "auto"`  
تأییدهای اجرای میزبان را کاملاً رد کن | `tools.exec.mode: "full"` به‌علاوه فایل تأییدهای میزبان متناظر  
نشست‌های غیرتعاملی ACPX را قادر به نوشتن/اجرا کن | `plugins.entries.acpx.config.permissionMode: "approve-all"`  
  
اگر پس از تغییر حالت، یک فرمان همچنان درخواست می‌دهد یا شکست می‌خورد، هر دو لایه را بررسی کنید:

bashCopy code
[code]
    openclaw approvals getopenclaw exec-policy show
[/code]

اجرای میزبان از نتیجه سخت‌گیرانه‌تر بین پیکربندی OpenClaw و فایل تأییدهای محلی میزبان استفاده می‌کند. مجوزهای هارنس ACPX تأییدهای اجرای میزبان را آزادتر نمی‌کنند، و تأییدهای اجرای میزبان درخواست‌های هارنس ACPX را آزادتر نمی‌کنند.

## مرتبط

  * [تأییدهای Exec](</fa/tools/exec-approvals>)
  * [تأییدهای Exec - پیشرفته](</fa/tools/exec-approvals-advanced>)
  * [هارنس Codex](</fa/plugins/codex-harness>)
  * [راه‌اندازی عامل‌های ACP](</fa/tools/acp-agents-setup#permission-configuration>)


Was this useful?YesNo

Open issue