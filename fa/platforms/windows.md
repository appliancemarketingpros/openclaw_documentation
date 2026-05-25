---
title: Windows
source_url: https://docs.openclaw.ai/fa/platforms/windows
scraped_at: 2026-05-25
---

OpenClaw از هر دو حالت **Windows بومی** و **WSL2** پشتیبانی می‌کند. WSL2 مسیر پایدارتر است و برای تجربه کامل توصیه می‌شود؛ CLI، Gateway و ابزارها داخل Linux با سازگاری کامل اجرا می‌شوند. Windows بومی برای استفاده اصلی از CLI و Gateway کار می‌کند، با چند نکته احتیاطی که در ادامه آمده است.

برنامه‌های همراه بومی Windows برنامه‌ریزی شده‌اند.

## WSL2 (توصیه‌شده)

  * [شروع به کار](</fa/start/getting-started>) (داخل WSL استفاده شود)
  * [نصب و به‌روزرسانی‌ها](</fa/install/updating>)
  * راهنمای رسمی WSL2 (Microsoft): <https://learn.microsoft.com/windows/wsl/install>


## وضعیت Windows بومی

جریان‌های CLI در Windows بومی در حال بهبود هستند، اما WSL2 همچنان مسیر توصیه‌شده است.

مواردی که امروز در Windows بومی خوب کار می‌کنند:

  * نصب‌کننده وب‌سایت از طریق `install.ps1`
  * استفاده محلی از CLI مانند `openclaw --version`، `openclaw doctor` و `openclaw plugins list --json`
  * دودآزمایی عامل/ارائه‌دهنده محلی تعبیه‌شده مانند:

powershellCopy code
[code]
    openclaw agent --local --agent main --thinking low -m "Reply with exactly WINDOWS-HATCH-OK."
[/code]

نکات احتیاطی فعلی:

  * `openclaw onboard --non-interactive` همچنان انتظار دارد یک gateway محلی دردسترس باشد، مگر اینکه `--skip-health` را پاس دهید
  * `openclaw onboard --non-interactive --install-daemon` و `openclaw gateway install` ابتدا Windows Scheduled Tasks را امتحان می‌کنند
  * اگر ایجاد Scheduled Task رد شود، OpenClaw به یک آیتم ورود پوشه Startup مخصوص هر کاربر برمی‌گردد و gateway را بلافاصله شروع می‌کند
  * اگر خود `schtasks` گیر کند یا پاسخ ندهد، OpenClaw اکنون آن مسیر را سریع قطع می‌کند و به‌جای معطل‌ماندن همیشگی، به مسیر جایگزین برمی‌گردد
  * Scheduled Tasks همچنان در صورت دردسترس‌بودن ترجیح داده می‌شوند، چون وضعیت ناظر بهتری ارائه می‌کنند


اگر فقط CLI بومی را می‌خواهید، بدون نصب سرویس gateway، از یکی از این‌ها استفاده کنید:

powershellCopy code
[code]
    openclaw onboard --non-interactive --skip-healthopenclaw gateway run
[/code]

اگر راه‌اندازی مدیریت‌شده را روی Windows بومی می‌خواهید:

powershellCopy code
[code]
    openclaw gateway installopenclaw gateway status --json
[/code]

اگر ایجاد Scheduled Task مسدود شده باشد، حالت سرویس جایگزین همچنان پس از ورود، از طریق پوشه Startup کاربر فعلی به‌طور خودکار شروع می‌شود.

## Gateway

  * [راهنمای عملیاتی Gateway](</fa/gateway>)
  * [پیکربندی](</fa/gateway/configuration>)


## نصب سرویس Gateway (CLI)

داخل WSL2:

CodeCopy code
[code]
    openclaw onboard --install-daemon
[/code]

یا:

CodeCopy code
[code]
    openclaw gateway install
[/code]

یا:

CodeCopy code
[code]
    openclaw configure
[/code]

هنگام درخواست، **سرویس Gateway** را انتخاب کنید.

ترمیم/مهاجرت:

CodeCopy code
[code]
    openclaw doctor
[/code]

## شروع خودکار Gateway پیش از ورود به Windows

برای راه‌اندازی‌های headless، مطمئن شوید زنجیره کامل بوت حتی وقتی کسی وارد Windows نمی‌شود اجرا می‌شود.

### 1) اجرای سرویس‌های کاربر بدون ورود را فعال نگه دارید

داخل WSL:

bashCopy code
[code]
    sudo loginctl enable-linger "$(whoami)"
[/code]

### 2) سرویس کاربری gateway در OpenClaw را نصب کنید

داخل WSL:

bashCopy code
[code]
    openclaw gateway install
[/code]

### 3) WSL را هنگام بوت Windows به‌طور خودکار شروع کنید

در PowerShell با دسترسی Administrator:

powershellCopy code
[code]
    schtasks /create /tn "WSL Boot" /tr "wsl.exe -d Ubuntu --exec /bin/true" /sc onstart /ru SYSTEM
[/code]

`Ubuntu` را با نام توزیع خود از خروجی زیر جایگزین کنید:

powershellCopy code
[code]
    wsl --list --verbose
[/code]

### راستی‌آزمایی زنجیره راه‌اندازی

پس از راه‌اندازی مجدد (پیش از ورود به Windows)، از داخل WSL بررسی کنید:

bashCopy code
[code]
    systemctl --user is-enabled openclaw-gateway.servicesystemctl --user status openclaw-gateway.service --no-pager
[/code]

## پیشرفته: ارائه سرویس‌های WSL روی LAN (portproxy)

WSL شبکه مجازی خودش را دارد. اگر ماشین دیگری باید به سرویسی که **داخل WSL** اجرا می‌شود دسترسی داشته باشد (SSH، یک سرور TTS محلی، یا Gateway)، باید یک پورت Windows را به IP فعلی WSL فوروارد کنید. IP مربوط به WSL پس از راه‌اندازی مجدد تغییر می‌کند، بنابراین ممکن است لازم باشد قانون فوروارد را تازه‌سازی کنید.

مثال (PowerShell **با دسترسی Administrator**):

powershellCopy code
[code]
    $Distro = "Ubuntu-24.04"$ListenPort = 2222$TargetPort = 22 $WslIp = (wsl -d $Distro -- hostname -I).Trim().Split(" ")[0]if (-not $WslIp) { throw "WSL IP not found." } netsh interface portproxy add v4tov4 listenaddress=0.0.0.0 listenport=$ListenPort `  connectaddress=$WslIp connectport=$TargetPort
[/code]

اجازه عبور پورت از Windows Firewall را بدهید (یک‌باره):

powershellCopy code
[code]
    New-NetFirewallRule -DisplayName "WSL SSH $ListenPort" -Direction Inbound `  -Protocol TCP -LocalPort $ListenPort -Action Allow
[/code]

پس از راه‌اندازی مجدد WSL، portproxy را تازه‌سازی کنید:

powershellCopy code
[code]
    netsh interface portproxy delete v4tov4 listenport=$ListenPort listenaddress=0.0.0.0 | Out-Nullnetsh interface portproxy add v4tov4 listenport=$ListenPort listenaddress=0.0.0.0 `  connectaddress=$WslIp connectport=$TargetPort | Out-Null
[/code]

نکات:

  * SSH از ماشین دیگر، **IP میزبان Windows** را هدف می‌گیرد (مثال: `ssh user@windows-host -p 2222`).
  * گره‌های ریموت باید به یک URL مربوط به Gateway که **قابل دسترسی** است اشاره کنند (نه `127.0.0.1`)؛ برای تایید از `openclaw status --all` استفاده کنید.
  * برای دسترسی LAN از `listenaddress=0.0.0.0` استفاده کنید؛ `127.0.0.1` آن را فقط محلی نگه می‌دارد.
  * اگر می‌خواهید این کار خودکار باشد، یک Scheduled Task ثبت کنید تا مرحله تازه‌سازی را هنگام ورود اجرا کند.


## نصب گام‌به‌گام WSL2

### 1) نصب WSL2 + Ubuntu

PowerShell را باز کنید (Admin):

powershellCopy code
[code]
    wsl --install# Or pick a distro explicitly:wsl --list --onlinewsl --install -d Ubuntu-24.04
[/code]

اگر Windows درخواست کرد، راه‌اندازی مجدد کنید.

### 2) فعال‌کردن systemd (برای نصب gateway لازم است)

در ترمینال WSL خود:

bashCopy code
[code]
    sudo tee /etc/wsl.conf >/dev/null <<'EOF'[boot]systemd=trueEOF
[/code]

سپس از PowerShell:

powershellCopy code
[code]
    wsl --shutdown
[/code]

Ubuntu را دوباره باز کنید، سپس بررسی کنید:

bashCopy code
[code]
    systemctl --user status
[/code]

### 3) نصب OpenClaw (داخل WSL)

برای راه‌اندازی عادی بار اول داخل WSL، جریان شروع به کار Linux را دنبال کنید:

bashCopy code
[code]
    git clone https://github.com/openclaw/openclaw.gitcd openclawpnpm installpnpm buildpnpm ui:buildpnpm openclaw onboard --install-daemon
[/code]

اگر به‌جای onboarding بار اول، از سورس توسعه می‌دهید، از حلقه توسعه سورس در [راه‌اندازی](</fa/start/setup>) استفاده کنید:

bashCopy code
[code]
    pnpm install# First run only (or after resetting local OpenClaw config/workspace)pnpm openclaw setuppnpm gateway:watch
[/code]

راهنمای کامل: [شروع به کار](</fa/start/getting-started>)

## برنامه همراه Windows

هنوز برنامه همراه Windows نداریم. اگر می‌خواهید در تحقق آن کمک کنید، مشارکت‌ها پذیرفته می‌شوند.

## اتصال Git و GitHub (مشارکت‌کنندگان)

بعضی شبکه‌ها HTTPS به GitHub را مسدود یا محدود می‌کنند. اگر `git clone` با timeout یا بازنشانی اتصال شکست خورد، شبکه‌ای دیگر، VPN، یا یک پراکسی HTTP/HTTPS ارائه‌شده توسط سازمانتان را امتحان کنید.

اگر `gh auth login` هنگام جریان دستگاه مرورگر شکست خورد (برای مثال timeout هنگام دسترسی به `github.com:443`)، به‌جای آن با یک personal access token احراز هویت کنید:

  1. یک token با حداقل scope مربوط به `repo` (PAT کلاسیک) یا دسترسی fine-grained معادل بسازید.
  2. در PowerShell برای نشست فعلی:

powershellCopy code
[code]
    $env:GH_TOKEN="<your-token>"gh auth statusgh auth setup-git
[/code]

  3. اگر `gh auth status` درباره نبودن `read:org` هشدار داد، token بسازید که شامل آن scope باشد و متغیر را دوباره اختصاص دهید:

powershellCopy code
[code]
    $env:GH_TOKEN="<your-token-with-repo-and-read:org>"gh auth status
[/code]

`gh auth refresh -s read:org` فقط زمانی اعمال می‌شود که از طریق `gh auth login` احراز هویت کرده باشید و اعتبارنامه‌های ذخیره‌شده برای تازه‌سازی داشته باشید (نه هنگام استفاده از `GH_TOKEN`).

هرگز tokenها را commit نکنید یا آن‌ها را در issueها یا pull requestها نچسبانید.

## مرتبط

  * [نمای کلی نصب](</fa/install>)
  * [پلتفرم‌ها](</fa/platforms>)


Was this useful?YesNo