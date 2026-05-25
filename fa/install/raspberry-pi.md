---
title: Raspberry Pi
source_url: https://docs.openclaw.ai/fa/install/raspberry-pi
scraped_at: 2026-05-25
---

OpenClaw Gateway پایدار و همیشه‌روشن را روی Raspberry Pi اجرا کنید. از آنجا که Pi فقط Gateway است (مدل‌ها از طریق API در فضای ابری اجرا می‌شوند)، حتی یک Pi معمولی هم به‌خوبی از پس بار کاری برمی‌آید — هزینهٔ معمول سخت‌افزار **۳۵ تا ۸۰ دلار، یک‌باره** است و هزینهٔ ماهانه ندارد.

## سازگاری سخت‌افزاری

مدل Pi | RAM | کار می‌کند؟ | نکات  
---|---|---|---  
Pi 5 | 4/8 GB | بهترین | سریع‌ترین گزینه، توصیه‌شده.  
Pi 4 | 4 GB | خوب | نقطهٔ بهینه برای بیشتر کاربران.  
Pi 4 | 2 GB | قابل قبول | swap اضافه کنید.  
Pi 4 | 1 GB | محدود | با swap و پیکربندی حداقلی ممکن است.  
Pi 3B+ | 1 GB | کند | کار می‌کند اما کند است.  
Pi Zero 2 W | 512 MB | خیر | توصیه نمی‌شود.  
  
**حداقل:** ۱ GB RAM، ۱ هسته، ۵۰۰ MB فضای دیسک آزاد، سیستم‌عامل ۶۴ بیتی. **توصیه‌شده:** ۲ GB+ RAM، کارت SD با ظرفیت ۱۶ GB+ (یا USB SSD)، اترنت.

## پیش‌نیازها

  * Raspberry Pi 4 یا 5 با ۲ GB+ RAM (۴ GB توصیه می‌شود)
  * کارت MicroSD (۱۶ GB+) یا USB SSD (عملکرد بهتر)
  * منبع تغذیهٔ رسمی Pi
  * اتصال شبکه (اترنت یا WiFi)
  * Raspberry Pi OS ۶۴ بیتی (ضروری -- از نسخهٔ ۳۲ بیتی استفاده نکنید)
  * حدود ۳۰ دقیقه


## راه‌اندازی

* ### فلش کردن سیستم‌عامل

از **Raspberry Pi OS Lite (64-bit)** استفاده کنید -- برای یک سرور headless نیازی به محیط دسکتاپ نیست.

  1. [Raspberry Pi Imager](<https://www.raspberrypi.com/software/>) را دانلود کنید.
  2. سیستم‌عامل را انتخاب کنید: **Raspberry Pi OS Lite (64-bit)**.
  3. در پنجرهٔ تنظیمات، از پیش پیکربندی کنید: 
     * Hostname: `gateway-host`
     * SSH را فعال کنید
     * نام کاربری و گذرواژه را تنظیم کنید
     * WiFi را پیکربندی کنید (اگر از اترنت استفاده نمی‌کنید)
  4. روی کارت SD یا درایو USB فلش کنید، آن را وارد کنید و Pi را بوت کنید.


* ### اتصال از طریق SSH

bashCopy code
[code]
    ssh user@gateway-host
[/code]

* ### به‌روزرسانی سیستم

bashCopy code
[code]
    sudo apt update && sudo apt upgrade -ysudo apt install -y git curl build-essential # Set timezone (important for cron and reminders)sudo timedatectl set-timezone America/Chicago
[/code]

* ### نصب Node.js 24

bashCopy code
[code]
    curl -fsSL https://deb.nodesource.com/setup_24.x | sudo -E bash -sudo apt install -y nodejsnode --version
[/code]

* ### افزودن swap (مهم برای ۲ GB یا کمتر)

bashCopy code
[code]
    sudo fallocate -l 2G /swapfilesudo chmod 600 /swapfilesudo mkswap /swapfilesudo swapon /swapfileecho '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab # Reduce swappiness for low-RAM devicesecho 'vm.swappiness=10' | sudo tee -a /etc/sysctl.confsudo sysctl -p
[/code]

* ### نصب OpenClaw

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash
[/code]

* ### اجرای راه‌اندازی اولیه

bashCopy code
[code]
    openclaw onboard --install-daemon
[/code]

جادوگر را دنبال کنید. برای دستگاه‌های headless، کلیدهای API به OAuth ترجیح داده می‌شوند. Telegram ساده‌ترین کانال برای شروع است.

* ### اعتبارسنجی

bashCopy code
[code]
    openclaw statussystemctl --user status openclaw-gateway.servicejournalctl --user -u openclaw-gateway.service -f
[/code]

* ### دسترسی به Control UI

در رایانهٔ خود، یک URL داشبورد از Pi بگیرید:

bashCopy code
[code]
    ssh user@gateway-host 'openclaw dashboard --no-open'
[/code]

سپس در یک ترمینال دیگر یک تونل SSH بسازید:

bashCopy code
[code]
    ssh -N -L 18789:127.0.0.1:18789 user@gateway-host
[/code]

URL چاپ‌شده را در مرورگر محلی خود باز کنید. برای دسترسی راه دور همیشه‌روشن، [یکپارچه‌سازی Tailscale](</fa/gateway/tailscale>) را ببینید.

## نکات عملکردی

**از USB SSD استفاده کنید** \-- کارت‌های SD کند هستند و فرسوده می‌شوند. USB SSD عملکرد را به‌شکل چشمگیری بهتر می‌کند. [راهنمای بوت USB در Pi](<https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#usb-mass-storage-boot>) را ببینید.

**کش کامپایل ماژول را فعال کنید** \-- فراخوانی‌های تکراری CLI را روی میزبان‌های Pi کم‌مصرف سریع‌تر می‌کند:

bashCopy code
[code]
    grep -q 'NODE_COMPILE_CACHE=/var/tmp/openclaw-compile-cache' ~/.bashrc || cat >> ~/.bashrc <<'EOF' # pragma: allowlist secretexport NODE_COMPILE_CACHE=/var/tmp/openclaw-compile-cachemkdir -p /var/tmp/openclaw-compile-cacheexport OPENCLAW_NO_RESPAWN=1EOFsource ~/.bashrc
[/code]

**مصرف حافظه را کاهش دهید** \-- برای راه‌اندازی‌های headless، حافظهٔ GPU را آزاد کنید و سرویس‌های استفاده‌نشده را غیرفعال کنید:

bashCopy code
[code]
    echo 'gpu_mem=16' | sudo tee -a /boot/config.txtsudo systemctl disable bluetooth
[/code]

**drop-in مربوط به systemd برای راه‌اندازی مجدد پایدار** \-- اگر این Pi عمدتاً OpenClaw را اجرا می‌کند، یک drop-in برای سرویس اضافه کنید:

bashCopy code
[code]
    systemctl --user edit openclaw-gateway.service
[/code]

iniCopy code
[code]
    [Service]Environment=OPENCLAW_NO_RESPAWN=1Environment=NODE_COMPILE_CACHE=/var/tmp/openclaw-compile-cacheRestart=alwaysRestartSec=2TimeoutStartSec=90
[/code]

سپس `systemctl --user daemon-reload && systemctl --user restart openclaw-gateway.service` را اجرا کنید. روی یک Pi headless، همچنین lingering را یک‌بار فعال کنید تا سرویس کاربر پس از خروج از سیستم هم باقی بماند: `sudo loginctl enable-linger "$(whoami)"`.

## راه‌اندازی مدل توصیه‌شده

از آنجا که Pi فقط Gateway را اجرا می‌کند، از مدل‌های API میزبانی‌شده در فضای ابری استفاده کنید:

jsonCopy code
[code]
    {  "agents": {    "defaults": {      "model": {        "primary": "anthropic/claude-sonnet-4-6",        "fallbacks": ["openai/gpt-5.4-mini"]      }    }  }}
[/code]

LLMهای محلی را روی Pi اجرا نکنید — حتی مدل‌های کوچک هم بیش از حد کند هستند که مفید باشند. بگذارید Claude یا GPT کار مدل را انجام دهد.

## نکات باینری ARM

بیشتر قابلیت‌های OpenClaw روی ARM64 بدون تغییر کار می‌کنند (Node.js، Telegram، WhatsApp/Baileys، Chromium). باینری‌هایی که گاهی بیلد ARM ندارند معمولاً ابزارهای CLI اختیاری Go/Rust هستند که توسط Skills ارائه می‌شوند. پیش از بازگشت به ساخت از سورس، صفحهٔ انتشار باینریِ گم‌شده را برای آرتیفکت‌های `linux-arm64` / `aarch64` بررسی کنید.

## پایداری و پشتیبان‌گیری

وضعیت OpenClaw زیر این مسیرها قرار دارد:

  * `~/.openclaw/` — `openclaw.json`، `auth-profiles.json` برای هر عامل، وضعیت کانال/ارائه‌دهنده، نشست‌ها.
  * `~/.openclaw/workspace/` — فضای کاری عامل ([SOUL.md](<http://SOUL.md>)، حافظه، آرتیفکت‌ها).


این‌ها پس از راه‌اندازی مجدد باقی می‌مانند. با دستور زیر یک snapshot قابل‌حمل بگیرید:

bashCopy code
[code]
    openclaw backup create
[/code]

اگر این موارد را روی SSD نگه دارید، هم عملکرد و هم دوام نسبت به کارت SD بهتر می‌شود.

## عیب‌یابی

**کمبود حافظه** \-- با `free -h` بررسی کنید که swap فعال است. سرویس‌های استفاده‌نشده را غیرفعال کنید (`sudo systemctl disable cups bluetooth avahi-daemon`). فقط از مدل‌های مبتنی بر API استفاده کنید.

**عملکرد کند** \-- به‌جای کارت SD از USB SSD استفاده کنید. با `vcgencmd get_throttled` throttling پردازنده را بررسی کنید (باید `0x0` برگرداند).

**سرویس شروع نمی‌شود** \-- لاگ‌ها را با `journalctl --user -u openclaw-gateway.service --no-pager -n 100` بررسی کنید و `openclaw doctor --non-interactive` را اجرا کنید. اگر این یک Pi headless است، همچنین بررسی کنید lingering فعال باشد: `sudo loginctl enable-linger "$(whoami)"`.

**مشکلات باینری ARM** \-- اگر یک skill با خطای "exec format error" شکست خورد، بررسی کنید آیا باینری بیلد ARM64 دارد یا نه. معماری را با `uname -m` بررسی کنید (باید `aarch64` نشان دهد).

**قطع شدن WiFi** \-- مدیریت مصرف برق WiFi را غیرفعال کنید: `sudo iwconfig wlan0 power off`.

## گام‌های بعدی

  * [کانال‌ها](</fa/channels>) \-- Telegram، WhatsApp، Discord و موارد بیشتر را متصل کنید
  * [پیکربندی Gateway](</fa/gateway/configuration>) \-- همهٔ گزینه‌های پیکربندی
  * [به‌روزرسانی](</fa/install/updating>) \-- OpenClaw را به‌روز نگه دارید


## مرتبط

  * [نمای کلی نصب](</fa/install>)
  * [سرور Linux](</fa/vps>)
  * [پلتفرم‌ها](</fa/platforms>)


Was this useful?YesNo