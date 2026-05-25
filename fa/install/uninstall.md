---
title: حذف نصب
source_url: https://docs.openclaw.ai/fa/install/uninstall
scraped_at: 2026-05-25
---

دو مسیر:

  * **مسیر آسان** اگر `openclaw` هنوز نصب است.
  * **حذف دستی سرویس** اگر CLI حذف شده اما سرویس هنوز در حال اجراست.


## مسیر آسان (CLI هنوز نصب است)

توصیه‌شده: از حذف‌کنندهٔ نصب داخلی استفاده کنید:

bashCopy code
[code]
    openclaw uninstall
[/code]

غیرتعاملی (خودکارسازی / npx):

bashCopy code
[code]
    openclaw uninstall --all --yes --non-interactivenpx -y openclaw uninstall --all --yes --non-interactive
[/code]

مراحل دستی (با همان نتیجه):

  1. سرویس Gateway را متوقف کنید:

bashCopy code
[code]
    openclaw gateway stop
[/code]

  2. سرویس Gateway را حذف نصب کنید (launchd/systemd/schtasks):

bashCopy code
[code]
    openclaw gateway uninstall
[/code]

  3. وضعیت + پیکربندی را حذف کنید:

bashCopy code
[code]
    rm -rf "${OPENCLAW_STATE_DIR:-$HOME/.openclaw}"
[/code]

اگر `OPENCLAW_CONFIG_PATH` را روی مکانی سفارشی خارج از دایرکتوری وضعیت تنظیم کرده‌اید، آن فایل را هم حذف کنید.

  4. فضای کاری خود را حذف کنید (اختیاری، فایل‌های عامل را حذف می‌کند):

bashCopy code
[code]
    rm -rf ~/.openclaw/workspace
[/code]

  5. نصب CLI را حذف کنید (موردی را که استفاده کرده‌اید انتخاب کنید):

bashCopy code
[code]
    npm rm -g openclawpnpm remove -g openclawbun remove -g openclaw
[/code]

  6. اگر برنامهٔ macOS را نصب کرده‌اید:

bashCopy code
[code]
    rm -rf /Applications/OpenClaw.app
[/code]

نکته‌ها:

  * اگر از پروفایل‌ها (`--profile` / `OPENCLAW_PROFILE`) استفاده کرده‌اید، مرحلهٔ 3 را برای هر دایرکتوری وضعیت تکرار کنید (پیش‌فرض‌ها `~/.openclaw-<profile>` هستند).
  * در حالت راه دور، دایرکتوری وضعیت روی **میزبان Gateway** قرار دارد، بنابراین مراحل 1 تا 4 را آنجا هم اجرا کنید.


## حذف دستی سرویس (CLI نصب نیست)

اگر سرویس Gateway همچنان در حال اجراست اما `openclaw` وجود ندارد، از این روش استفاده کنید.

### macOS (launchd)

برچسب پیش‌فرض `ai.openclaw.gateway` است (یا `ai.openclaw.<profile>`؛ قالب قدیمی `com.openclaw.*` ممکن است هنوز وجود داشته باشد):

bashCopy code
[code]
    launchctl bootout gui/$UID/ai.openclaw.gatewayrm -f ~/Library/LaunchAgents/ai.openclaw.gateway.plist
[/code]

اگر از پروفایل استفاده کرده‌اید، برچسب و نام plist را با `ai.openclaw.<profile>` جایگزین کنید. اگر plistهای قدیمی `com.openclaw.*` وجود دارند، آن‌ها را هم حذف کنید.

### Linux (واحد کاربری systemd)

نام واحد پیش‌فرض `openclaw-gateway.service` است (یا `openclaw-gateway-<profile>.service`):

bashCopy code
[code]
    systemctl --user disable --now openclaw-gateway.servicerm -f ~/.config/systemd/user/openclaw-gateway.servicesystemctl --user daemon-reload
[/code]

### Windows (کار زمان‌بندی‌شده)

نام کار پیش‌فرض `OpenClaw Gateway` است (یا `OpenClaw Gateway (<profile>)`). اسکریپت کار زیر دایرکتوری وضعیت شما قرار دارد.

powershellCopy code
[code]
    schtasks /Delete /F /TN "OpenClaw Gateway"Remove-Item -Force "$env:USERPROFILE\.openclaw\gateway.cmd"
[/code]

اگر از پروفایل استفاده کرده‌اید، نام کار متناظر و `~\.openclaw-<profile>\gateway.cmd` را حذف کنید.

## نصب عادی در برابر checkout از منبع

### نصب عادی ([install.sh](<http://install.sh>) / npm / pnpm / bun)

اگر از `https://openclaw.ai/install.sh` یا `install.ps1` استفاده کرده‌اید، CLI با `npm install -g openclaw@latest` نصب شده است. آن را با `npm rm -g openclaw` حذف کنید (یا اگر با آن روش نصب کرده‌اید، با `pnpm remove -g` / `bun remove -g`).

### checkout از منبع (git clone)

اگر از یک checkout مخزن اجرا می‌کنید (`git clone` \+ `openclaw ...` / `bun run openclaw ...`):

  1. سرویس Gateway را **پیش از** حذف مخزن، حذف نصب کنید (از مسیر آسان بالا یا حذف دستی سرویس استفاده کنید).
  2. دایرکتوری مخزن را حذف کنید.
  3. وضعیت + فضای کاری را همان‌طور که در بالا نشان داده شد حذف کنید.


## مرتبط

  * [نمای کلی نصب](</fa/install>)
  * [راهنمای مهاجرت](</fa/install/migrating>)


Was this useful?YesNo