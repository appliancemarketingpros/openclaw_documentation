---
title: عیب‌یابی مرورگر
source_url: https://docs.openclaw.ai/fa/tools/browser-linux-troubleshooting
scraped_at: 2026-05-25
---

## مشکل: «Failed to start Chrome CDP on port 18800»

سرور کنترل مرورگر OpenClaw در اجرای Chrome/Brave/Edge/Chromium با این خطا ناموفق می‌شود:

CodeCopy code
[code]
    {"error":"Error: Failed to start Chrome CDP on port 18800 for profile \"openclaw\"."}
[/code]

### علت اصلی

در Ubuntu و بسیاری از توزیع‌های Linux، نصب پیش‌فرض Chromium یک **بسته snap** است. محدودسازی AppArmor در snap با روشی که OpenClaw فرایند مرورگر را اجرا و پایش می‌کند تداخل دارد.

فرمان `apt install chromium` یک بسته واسط نصب می‌کند که به snap هدایت می‌شود:

CodeCopy code
[code]
    Note, selecting 'chromium-browser' instead of 'chromium'chromium-browser is already the newest version (2:1snap1-0ubuntu2).
[/code]

این یک مرورگر واقعی نیست؛ فقط یک wrapper است.

خطاهای رایج دیگر هنگام اجرا در Linux:

  * `The profile appears to be in use by another Chromium process` یعنی Chrome فایل‌های قفل قدیمی `Singleton*` را در پوشه پروفایل مدیریت‌شده پیدا کرده است. OpenClaw این قفل‌ها را حذف می‌کند و وقتی قفل به فرایندی مرده یا روی میزبان متفاوت اشاره کند، یک‌بار دوباره تلاش می‌کند.
  * `Missing X server or $DISPLAY` یعنی یک مرورگر قابل مشاهده به‌صورت صریح روی میزبانی بدون نشست دسکتاپ درخواست شده است. به‌طور پیش‌فرض، پروفایل‌های مدیریت‌شده محلی اکنون در Linux وقتی هر دو `DISPLAY` و `WAYLAND_DISPLAY` تنظیم نشده باشند، به حالت headless برمی‌گردند. اگر `OPENCLAW_BROWSER_HEADLESS=0`، `browser.headless: false`، یا `browser.profiles.<name>.headless: false` را تنظیم کرده‌اید، آن override حالت headed را حذف کنید، `OPENCLAW_BROWSER_HEADLESS=1` را تنظیم کنید، `Xvfb` را شروع کنید، برای یک اجرای مدیریت‌شده تک‌باره `openclaw browser start --headless` را اجرا کنید، یا OpenClaw را در یک نشست دسکتاپ واقعی اجرا کنید.


### راه‌حل ۱: نصب Google Chrome (پیشنهادی)

بسته رسمی `.deb` مربوط به Google Chrome را نصب کنید؛ این بسته توسط snap sandbox نشده است:

bashCopy code
[code]
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.debsudo dpkg -i google-chrome-stable_current_amd64.debsudo apt --fix-broken install -y  # if there are dependency errors
[/code]

سپس پیکربندی OpenClaw خود را به‌روزرسانی کنید (`~/.openclaw/openclaw.json`):

jsonCopy code
[code]
    {  "browser": {    "enabled": true,    "executablePath": "/usr/bin/google-chrome-stable",    "headless": true,    "noSandbox": true  }}
[/code]

### راه‌حل ۲: استفاده از Snap Chromium با حالت فقط اتصال

اگر ناچارید از snap Chromium استفاده کنید، OpenClaw را طوری پیکربندی کنید که به مرورگری که دستی شروع شده است متصل شود:

  1. پیکربندی را به‌روزرسانی کنید:

jsonCopy code
[code]
    {  "browser": {    "enabled": true,    "attachOnly": true,    "headless": true,    "noSandbox": true  }}
[/code]

  2. Chromium را دستی شروع کنید:

bashCopy code
[code]
    chromium-browser --headless --no-sandbox --disable-gpu \  --remote-debugging-port=18800 \  --user-data-dir=$HOME/.openclaw/browser/openclaw/user-data \  about:blank &
[/code]

  3. در صورت تمایل، یک سرویس کاربر systemd برای شروع خودکار Chrome بسازید:

iniCopy code
[code]
    # ~/.config/systemd/user/openclaw-browser.service[Unit]Description=OpenClaw Browser (Chrome CDP)After=network.target [Service]ExecStart=/snap/bin/chromium --headless --no-sandbox --disable-gpu --remote-debugging-port=18800 --user-data-dir=%h/.openclaw/browser/openclaw/user-data about:blankRestart=on-failureRestartSec=5 [Install]WantedBy=default.target
[/code]

فعال‌سازی با: `systemctl --user enable --now openclaw-browser.service`

### بررسی اینکه مرورگر کار می‌کند

وضعیت را بررسی کنید:

bashCopy code
[code]
    curl -s http://127.0.0.1:18791/ | jq '{running, pid, chosenBrowser}'
[/code]

مرور را آزمایش کنید:

bashCopy code
[code]
    curl -s -X POST http://127.0.0.1:18791/startcurl -s http://127.0.0.1:18791/tabs
[/code]

### مرجع پیکربندی

گزینه | توضیح | مقدار پیش‌فرض  
---|---|---  
`browser.enabled` | فعال‌سازی کنترل مرورگر | `true`  
`browser.executablePath` | مسیر فایل اجرایی یک مرورگر مبتنی بر Chromium (Chrome/Brave/Edge/Chromium) | تشخیص خودکار (وقتی مرورگر پیش‌فرض مبتنی بر Chromium باشد، آن را ترجیح می‌دهد)  
`browser.headless` | اجرا بدون GUI | `false`  
`OPENCLAW_BROWSER_HEADLESS` | override برای هر فرایند در حالت headless مرورگر مدیریت‌شده محلی | تنظیم‌نشده  
`browser.noSandbox` | افزودن فلگ `--no-sandbox` (برای برخی راه‌اندازی‌های Linux لازم است) | `false`  
`browser.attachOnly` | مرورگر را اجرا نکن، فقط به نمونه موجود متصل شو | `false`  
`browser.cdpPort` | درگاه Chrome DevTools Protocol | `18800`  
`browser.localLaunchTimeoutMs` | مهلت تشخیص Chrome مدیریت‌شده محلی | `15000`  
`browser.localCdpReadyTimeoutMs` | مهلت آمادگی CDP پس از اجرای مرورگر مدیریت‌شده محلی | `8000`  
  
در Raspberry Pi، میزبان‌های VPS قدیمی‌تر، یا فضای ذخیره‌سازی کند، وقتی Chrome برای ارائه endpoint HTTP مربوط به CDP به زمان بیشتری نیاز دارد، `browser.localLaunchTimeoutMs` را افزایش دهید. وقتی اجرا موفق است اما `openclaw browser start` همچنان `not reachable after start` گزارش می‌دهد، `browser.localCdpReadyTimeoutMs` را افزایش دهید. مقدارها باید اعداد صحیح مثبت تا `120000` میلی‌ثانیه باشند؛ مقدارهای نامعتبر پیکربندی رد می‌شوند.

### مشکل: «No Chrome tabs found for profile="user"»

شما از یک پروفایل `existing-session` / Chrome MCP استفاده می‌کنید. OpenClaw می‌تواند Chrome محلی را ببیند، اما هیچ tab بازی برای اتصال وجود ندارد.

گزینه‌های رفع مشکل:

  1. **از مرورگر مدیریت‌شده استفاده کنید:** `openclaw browser start --browser-profile openclaw` (یا `browser.defaultProfile: "openclaw"` را تنظیم کنید).
  2. **از Chrome MCP استفاده کنید:** مطمئن شوید Chrome محلی با حداقل یک tab باز در حال اجراست، سپس با `--browser-profile user` دوباره تلاش کنید.


نکته‌ها:

  * `user` فقط مخصوص میزبان است. برای سرورهای Linux، کانتینرها، یا میزبان‌های remote، پروفایل‌های CDP را ترجیح دهید.
  * پروفایل‌های `user` / دیگر پروفایل‌های `existing-session` محدودیت‌های فعلی Chrome MCP را حفظ می‌کنند: actionهای مبتنی بر ref، hookهای آپلود تک‌فایل، بدون override برای مهلت dialog، بدون `wait --load networkidle`، و بدون `responsebody`، خروجی PDF، رهگیری دانلود، یا actionهای batch.
  * پروفایل‌های محلی `openclaw` مقدار `cdpPort`/`cdpUrl` را خودکار اختصاص می‌دهند؛ این‌ها را فقط برای CDP remote تنظیم کنید.
  * پروفایل‌های CDP remote مقدارهای `http://`، `https://`، `ws://`، و `wss://` را می‌پذیرند. برای کشف `/json/version` از HTTP(S) استفاده کنید، یا وقتی سرویس مرورگر شما یک URL مستقیم socket مربوط به DevTools می‌دهد، از WS(S) استفاده کنید.


## مرتبط

  * [مرورگر](</fa/tools/browser>)
  * [ورود به مرورگر](</fa/tools/browser-login>)
  * [عیب‌یابی Browser WSL2](</fa/tools/browser-wsl2-windows-remote-cdp-troubleshooting>)


Was this useful?YesNo