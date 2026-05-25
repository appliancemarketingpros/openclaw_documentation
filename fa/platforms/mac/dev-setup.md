---
title: راه‌اندازی محیط توسعه macOS
source_url: https://docs.openclaw.ai/fa/platforms/mac/dev-setup
scraped_at: 2026-05-25
---

# راه‌اندازی توسعه‌دهنده macOS

برنامه macOS مربوط به OpenClaw را از منبع بسازید و اجرا کنید.

## پیش‌نیازها

پیش از ساخت برنامه، مطمئن شوید موارد زیر را نصب کرده‌اید:

  1. **Xcode 26.2+** : برای توسعه Swift لازم است.
  2. **Node.js 24 و pnpm** : برای Gateway، CLI و اسکریپت‌های بسته‌بندی توصیه می‌شود. Node 22 LTS، در حال حاضر `22.16+`، همچنان برای سازگاری پشتیبانی می‌شود.


## 1\. نصب وابستگی‌ها

وابستگی‌های سراسر پروژه را نصب کنید:

bashCopy code
[code]
    pnpm install
[/code]

## 2\. ساخت و بسته‌بندی برنامه

برای ساخت برنامه macOS و بسته‌بندی آن در `dist/OpenClaw.app`، اجرا کنید:

bashCopy code
[code]
    ./scripts/package-mac-app.sh
[/code]

اگر گواهی Apple Developer ID ندارید، اسکریپت به‌طور خودکار از **امضای ad-hoc** (`-`) استفاده می‌کند.

برای حالت‌های اجرای توسعه، پرچم‌های امضا و عیب‌یابی Team ID، README برنامه macOS را ببینید: <https://github.com/openclaw/openclaw/blob/main/apps/macos/README.md>

> **نکته** : برنامه‌های امضاشده به‌صورت ad-hoc ممکن است اعلان‌های امنیتی ایجاد کنند. اگر برنامه بلافاصله با "Abort trap 6" خراب شد، بخش عیب‌یابی را ببینید.

## 3\. نصب CLI

برنامه macOS برای مدیریت کارهای پس‌زمینه انتظار دارد CLI سراسری `openclaw` نصب باشد.

**برای نصب آن (توصیه‌شده):**

  1. برنامه OpenClaw را باز کنید.
  2. به زبانه تنظیمات **General** بروید.
  3. روی **"Install CLI"** کلیک کنید.


همچنین می‌توانید آن را به‌صورت دستی نصب کنید:

bashCopy code
[code]
    npm install -g openclaw@<version>
[/code]

`pnpm add -g openclaw@<version>` و `bun add -g openclaw@<version>` نیز کار می‌کنند. برای زمان اجرای Gateway، Node همچنان مسیر توصیه‌شده است.

## عیب‌یابی

### ساخت ناموفق است: ناهماهنگی زنجیره‌ابزار یا SDK

ساخت برنامه macOS به آخرین SDK macOS و زنجیره‌ابزار Swift 6.2 نیاز دارد.

**وابستگی‌های سیستم (الزامی):**

  * **آخرین نسخه macOS موجود در Software Update** (موردنیاز SDKهای Xcode 26.2)
  * **Xcode 26.2** (زنجیره‌ابزار Swift 6.2)


**بررسی‌ها:**

bashCopy code
[code]
    xcodebuild -versionxcrun swift --version
[/code]

اگر نسخه‌ها مطابقت ندارند، macOS/Xcode را به‌روزرسانی کنید و ساخت را دوباره اجرا کنید.

### برنامه هنگام اعطای مجوز خراب می‌شود

اگر هنگام تلاش برای اجازه دادن به دسترسی **Speech Recognition** یا **Microphone** برنامه خراب می‌شود، ممکن است به‌دلیل خرابی کش TCC یا ناهماهنگی امضا باشد.

**رفع مشکل:**

  1. مجوزهای TCC را بازنشانی کنید:

bashCopy code
[code]tccutil reset All ai.openclaw.mac.debug
[/code]

  2. اگر این کار ناموفق بود، `BUNDLE_ID` را موقتاً در [`scripts/package-mac-app.sh`](<https://github.com/openclaw/openclaw/blob/main/scripts/package-mac-app.sh>) تغییر دهید تا macOS را مجبور کنید از یک «لوح پاک» شروع کند.


### Gateway به‌طور نامحدود روی "Starting..." می‌ماند

اگر وضعیت Gateway روی "Starting..." باقی می‌ماند، بررسی کنید آیا یک فرایند زامبی پورت را نگه داشته است یا نه:

bashCopy code
[code]
    openclaw gateway statusopenclaw gateway stop # If you're not using a LaunchAgent (dev mode / manual runs), find the listener:lsof -nP -iTCP:18789 -sTCP:LISTEN
[/code]

اگر یک اجرای دستی پورت را نگه داشته است، آن فرایند را متوقف کنید (Ctrl+C). به‌عنوان آخرین راهکار، PID پیدا شده در بالا را بکشید.

## مرتبط

  * [برنامه macOS](</fa/platforms/macos>)
  * [نمای کلی نصب](</fa/install>)


Was this useful?YesNo