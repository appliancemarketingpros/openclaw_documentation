---
title: جزئیات داخلی نصب‌کننده
source_url: https://docs.openclaw.ai/fa/install/installer
scraped_at: 2026-05-25
---

OpenClaw سه اسکریپت نصب را ارائه می‌کند که از `openclaw.ai` سرو می‌شوند.

اسکریپت | پلتفرم | کاری که انجام می‌دهد  
---|---|---  
`install.sh` | macOS / Linux / WSL | در صورت نیاز Node را نصب می‌کند، OpenClaw را از طریق npm (پیش‌فرض) یا git نصب می‌کند، و می‌تواند onboarding را اجرا کند.  
`install-cli.sh` | macOS / Linux / WSL | Node + OpenClaw را با حالت‌های npm یا git checkout در یک پیشوند محلی (`~/.openclaw`) نصب می‌کند. به دسترسی root نیاز ندارد.  
`install.ps1` | Windows (PowerShell) | در صورت نیاز Node را نصب می‌کند، OpenClaw را از طریق npm (پیش‌فرض) یا git نصب می‌کند، و می‌تواند onboarding را اجرا کند.  
  
## فرمان‌های سریع

### install.sh

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash
[/code]

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash -s -- --help
[/code]

### install-cli.sh

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash
[/code]

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash -s -- --help
[/code]

### install.ps1

powershellCopy code
[code]
    iwr -useb https://openclaw.ai/install.ps1 | iex
[/code]

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -Tag beta -NoOnboard -DryRun
[/code]

* * *

## [install.sh](<http://install.sh>)

### جریان ([install.sh](<http://install.sh>))

* ### Detect OS

از macOS و Linux (از جمله WSL) پشتیبانی می‌کند. اگر macOS شناسایی شود، در صورت نبود Homebrew آن را نصب می‌کند.

* ### Ensure Node.js 24 by default

نسخه Node را بررسی می‌کند و در صورت نیاز Node 24 را نصب می‌کند (Homebrew روی macOS، اسکریپت‌های راه‌اندازی NodeSource روی Linux apt/dnf/yum). OpenClaw همچنان برای سازگاری از Node 22 LTS، در حال حاضر `22.16+`، پشتیبانی می‌کند.

* ### Ensure Git

در صورت نبود Git آن را نصب می‌کند.

* ### Install OpenClaw

  * روش `npm` (پیش‌فرض): نصب سراسری npm
  * روش `git`: clone/update مخزن، نصب وابستگی‌ها با pnpm، build، سپس نصب wrapper در `~/.local/bin/openclaw`


* ### Post-install tasks

  * یک سرویس gateway بارگذاری‌شده را به‌صورت best-effort تازه‌سازی می‌کند (`openclaw gateway install --force`، سپس restart)
  * در upgradeها و نصب‌های git، `openclaw doctor --non-interactive` را اجرا می‌کند (best effort)
  * وقتی مناسب باشد onboarding را تلاش می‌کند (TTY در دسترس باشد، onboarding غیرفعال نشده باشد، و بررسی‌های bootstrap/config موفق باشند)
  * مقدار پیش‌فرض `SHARP_IGNORE_GLOBAL_LIBVIPS=1` را تنظیم می‌کند


### شناسایی checkout منبع

اگر داخل یک checkout از OpenClaw اجرا شود (`package.json` \+ `pnpm-workspace.yaml`)، اسکریپت این گزینه‌ها را پیشنهاد می‌دهد:

  * استفاده از checkout (`git`)، یا
  * استفاده از نصب سراسری (`npm`)


اگر TTY در دسترس نباشد و هیچ روش نصبی تنظیم نشده باشد، به‌طور پیش‌فرض از `npm` استفاده می‌کند و هشدار می‌دهد.

اسکریپت برای انتخاب روش نامعتبر یا مقادیر نامعتبر `--install-method` با کد `2` خارج می‌شود.

### مثال‌ها ([install.sh](<http://install.sh>))

### Default

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash
[/code]

### Skip onboarding

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash -s -- --no-onboard
[/code]

### Git install

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash -s -- --install-method git
[/code]

### GitHub main via npm

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash -s -- --version main
[/code]

### Dry run

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash -s -- --dry-run
[/code]

Flags reference پرچم | توضیح  
---|---  
`--install-method npm|git` | انتخاب روش نصب (پیش‌فرض: `npm`). نام مستعار: `--method`  
`--npm` | میان‌بر برای روش npm  
`--git` | میان‌بر برای روش git. نام مستعار: `--github`  
`--version <version|dist-tag|spec>` | نسخه npm، dist-tag، یا package spec (پیش‌فرض: `latest`)  
`--beta` | اگر beta dist-tag در دسترس باشد از آن استفاده می‌کند، در غیر این صورت به `latest` برمی‌گردد  
`--git-dir <path>` | دایرکتوری checkout (پیش‌فرض: `~/openclaw`). نام مستعار: `--dir`  
`--no-git-update` | از `git pull` برای checkout موجود صرف‌نظر می‌کند  
`--no-prompt` | promptها را غیرفعال می‌کند  
`--no-onboard` | از onboarding صرف‌نظر می‌کند  
`--onboard` | onboarding را فعال می‌کند  
`--dry-run` | اقدام‌ها را بدون اعمال تغییرات چاپ می‌کند  
`--verbose` | خروجی debug را فعال می‌کند (`set -x`، لاگ‌های سطح notice در npm)  
`--help` | نحوه استفاده را نشان می‌دهد (`-h`)  
Environment variables reference متغیر | توضیح  
---|---  
`OPENCLAW_INSTALL_METHOD=git|npm` | روش نصب  
`OPENCLAW_VERSION=latest|next|main|<semver>|<spec>` | نسخه npm، dist-tag، یا package spec  
`OPENCLAW_BETA=0|1` | در صورت در دسترس بودن از beta استفاده می‌کند  
`OPENCLAW_GIT_DIR=<path>` | دایرکتوری checkout  
`OPENCLAW_GIT_UPDATE=0|1` | به‌روزرسانی‌های git را تغییر وضعیت می‌دهد  
`OPENCLAW_NO_PROMPT=1` | promptها را غیرفعال می‌کند  
`OPENCLAW_NO_ONBOARD=1` | از onboarding صرف‌نظر می‌کند  
`OPENCLAW_DRY_RUN=1` | حالت dry run  
`OPENCLAW_VERBOSE=1` | حالت debug  
`OPENCLAW_NPM_LOGLEVEL=error|warn|notice` | سطح لاگ npm  
`SHARP_IGNORE_GLOBAL_LIBVIPS=0|1` | رفتار sharp/libvips را کنترل می‌کند (پیش‌فرض: `1`)  
  
* * *

## [install-cli.sh](<http://install-cli.sh>)

### جریان ([install-cli.sh](<http://install-cli.sh>))

* ### Install local Node runtime

یک tarball پین‌شده و پشتیبانی‌شده Node LTS را (نسخه در اسکریپت جاسازی شده و مستقل به‌روزرسانی می‌شود) در `<prefix>/tools/node-v<version>` دانلود می‌کند و SHA-256 را تأیید می‌کند.

* ### Ensure Git

اگر Git موجود نباشد، تلاش می‌کند آن را از طریق apt/dnf/yum روی Linux یا Homebrew روی macOS نصب کند.

* ### Install OpenClaw under prefix

  * روش `npm` (پیش‌فرض): زیر پیشوند با npm نصب می‌کند، سپس wrapper را در `<prefix>/bin/openclaw` می‌نویسد
  * روش `git`: یک checkout را clone/update می‌کند (پیش‌فرض `~/openclaw`) و همچنان wrapper را در `<prefix>/bin/openclaw` می‌نویسد


* ### Refresh loaded gateway service

اگر یک سرویس gateway از همان پیشوند قبلاً بارگذاری شده باشد، اسکریپت `openclaw gateway install --force`، سپس `openclaw gateway restart` را اجرا می‌کند، و سلامت gateway را به‌صورت best-effort بررسی می‌کند.

### مثال‌ها ([install-cli.sh](<http://install-cli.sh>))

### Default

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash
[/code]

### Custom prefix + version

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash -s -- --prefix /opt/openclaw --version latest
[/code]

### Git install

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash -s -- --install-method git --git-dir ~/openclaw
[/code]

### Automation JSON output

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash -s -- --json --prefix /opt/openclaw
[/code]

### Run onboarding

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash -s -- --onboard
[/code]

Flags reference پرچم | توضیح  
---|---  
`--prefix <path>` | پیشوند نصب (پیش‌فرض: `~/.openclaw`)  
`--install-method npm|git` | انتخاب روش نصب (پیش‌فرض: `npm`). نام مستعار: `--method`  
`--npm` | میان‌بر برای روش npm  
`--git`, `--github` | میان‌بر برای روش git  
`--git-dir <path>` | دایرکتوری git checkout (پیش‌فرض: `~/openclaw`). نام مستعار: `--dir`  
`--version <ver>` | نسخه OpenClaw یا dist-tag (پیش‌فرض: `latest`)  
`--node-version <ver>` | نسخه Node (پیش‌فرض: `22.22.0`)  
`--json` | رویدادهای NDJSON منتشر می‌کند  
`--onboard` | پس از نصب `openclaw onboard` را اجرا می‌کند  
`--no-onboard` | از onboarding صرف‌نظر می‌کند (پیش‌فرض)  
`--set-npm-prefix` | روی Linux، اگر پیشوند فعلی قابل نوشتن نباشد، پیشوند npm را به `~/.npm-global` اجبار می‌کند  
`--help` | نحوه استفاده را نشان می‌دهد (`-h`)  
Environment variables reference متغیر | توضیح  
---|---  
`OPENCLAW_PREFIX=<path>` | پیشوند نصب  
`OPENCLAW_INSTALL_METHOD=git|npm` | روش نصب  
`OPENCLAW_VERSION=<ver>` | نسخه OpenClaw یا برچسب توزیع  
`OPENCLAW_NODE_VERSION=<ver>` | نسخه Node  
`OPENCLAW_GIT_DIR=<path>` | دایرکتوری checkout مربوط به Git برای نصب‌های git  
`OPENCLAW_GIT_UPDATE=0|1` | تغییر وضعیت به‌روزرسانی‌های git برای checkoutهای موجود  
`OPENCLAW_NO_ONBOARD=1` | رد کردن راه‌اندازی اولیه  
`OPENCLAW_NPM_LOGLEVEL=error|warn|notice` | سطح لاگ npm  
`SHARP_IGNORE_GLOBAL_LIBVIPS=0|1` | کنترل رفتار sharp/libvips (پیش‌فرض: `1`)  
  
* * *

## install.ps1

### جریان (install.ps1)

* ### Ensure PowerShell + Windows environment

به PowerShell 5+ نیاز دارد.

* ### Ensure Node.js 24 by default

اگر موجود نباشد، تلاش می‌کند آن را ابتدا از طریق winget، سپس Chocolatey و بعد Scoop نصب کند. Node 22 LTS که در حال حاضر `22.16+` است، همچنان برای سازگاری پشتیبانی می‌شود.

* ### Install OpenClaw

  * روش `npm` (پیش‌فرض): نصب سراسری npm با استفاده از `-Tag` انتخاب‌شده، از یک دایرکتوری موقت قابل‌نوشتن نصب‌کننده اجرا می‌شود تا shellهایی که در پوشه‌های محافظت‌شده مانند `C:\` باز شده‌اند همچنان کار کنند
  * روش `git`: clone/update کردن repo، نصب/ساخت با pnpm، و نصب wrapper در `%USERPROFILE%\.local\bin\openclaw.cmd`


* ### Post-install tasks

  * در صورت امکان، دایرکتوری bin لازم را به PATH کاربر اضافه می‌کند
  * سرویس Gateway بارگذاری‌شده را به‌صورت best-effort تازه‌سازی می‌کند (`openclaw gateway install --force`، سپس restart)
  * در upgradeها و نصب‌های git، `openclaw doctor --non-interactive` را اجرا می‌کند (best effort)


* ### Handle failures

نصب‌های `iwr ... | iex` و scriptblock یک خطای خاتمه‌دهنده گزارش می‌کنند، بدون اینکه نشست فعلی PowerShell را ببندند. نصب‌های مستقیم `powershell -File` / `pwsh -File` همچنان برای خودکارسازی با کد غیرصفر خارج می‌شوند.

### نمونه‌ها (install.ps1)

### Default

powershellCopy code
[code]
    iwr -useb https://openclaw.ai/install.ps1 | iex
[/code]

### Git install

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -InstallMethod git
[/code]

### GitHub main via npm

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -Tag main
[/code]

### Custom git directory

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -InstallMethod git -GitDir "C:\openclaw"
[/code]

### Dry run

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -DryRun
[/code]

### Debug trace

powershellCopy code
[code]
    # install.ps1 has no dedicated -Verbose flag yet.Set-PSDebug -Trace 1& ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -NoOnboardSet-PSDebug -Trace 0
[/code]

Flags reference پرچم | توضیح  
---|---  
`-InstallMethod npm|git` | روش نصب (پیش‌فرض: `npm`)  
`-Tag <tag|version|spec>` | برچسب توزیع npm، نسخه، یا مشخصات بسته (پیش‌فرض: `latest`)  
`-GitDir <path>` | دایرکتوری checkout (پیش‌فرض: `%USERPROFILE%\openclaw`)  
`-NoOnboard` | رد کردن راه‌اندازی اولیه  
`-NoGitUpdate` | رد کردن `git pull`  
`-DryRun` | فقط چاپ کنش‌ها  
Environment variables reference متغیر | توضیح  
---|---  
`OPENCLAW_INSTALL_METHOD=git|npm` | روش نصب  
`OPENCLAW_GIT_DIR=<path>` | دایرکتوری checkout  
`OPENCLAW_NO_ONBOARD=1` | رد کردن راه‌اندازی اولیه  
`OPENCLAW_GIT_UPDATE=0` | غیرفعال کردن git pull  
`OPENCLAW_DRY_RUN=1` | حالت اجرای آزمایشی  
  
* * *

## CI و خودکارسازی

برای اجراهای قابل‌پیش‌بینی از پرچم‌ها/متغیرهای محیطی غیرتعاملی استفاده کنید.

### install.sh (non-interactive npm)

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash -s -- --no-prompt --no-onboard
[/code]

### install.sh (non-interactive git)

bashCopy code
[code]
    OPENCLAW_INSTALL_METHOD=git OPENCLAW_NO_PROMPT=1 \  curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash
[/code]

### install-cli.sh (JSON)

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash -s -- --json --prefix /opt/openclaw
[/code]

### install.ps1 (skip onboarding)

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -NoOnboard
[/code]

* * *

## عیب‌یابی

Why is Git required?

Git برای روش نصب `git` لازم است. برای نصب‌های `npm` نیز Git همچنان بررسی/نصب می‌شود تا وقتی وابستگی‌ها از URLهای git استفاده می‌کنند، از خطاهای `spawn git ENOENT` جلوگیری شود.

Why does npm hit EACCES on Linux?

برخی تنظیمات Linux پیشوند سراسری npm را به مسیرهای متعلق به root اشاره می‌دهند. `install.sh` می‌تواند پیشوند را به `~/.npm-global` تغییر دهد و exportهای PATH را به فایل‌های rc مربوط به shell اضافه کند (وقتی آن فایل‌ها وجود داشته باشند).

sharp/libvips issues

اسکریپت‌ها به‌صورت پیش‌فرض `SHARP_IGNORE_GLOBAL_LIBVIPS=1` را تنظیم می‌کنند تا از build شدن sharp در برابر libvips سیستم جلوگیری شود. برای override کردن:

bashCopy code
[code]
    SHARP_IGNORE_GLOBAL_LIBVIPS=0 curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash
[/code]

Windows: "npm error spawn git / ENOENT"

Git for Windows را نصب کنید، PowerShell را دوباره باز کنید، نصب‌کننده را دوباره اجرا کنید.

Windows: "openclaw is not recognized"

`npm config get prefix` را اجرا کنید و آن دایرکتوری را به PATH کاربر خود اضافه کنید (در Windows پسوند `\bin` لازم نیست)، سپس PowerShell را دوباره باز کنید.

Windows: how to get verbose installer output

`install.ps1` در حال حاضر switch مربوط به `-Verbose` را ارائه نمی‌کند. برای تشخیص‌های سطح اسکریپت از tracing در PowerShell استفاده کنید:

powershellCopy code
[code]
    Set-PSDebug -Trace 1& ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -NoOnboardSet-PSDebug -Trace 0
[/code]

openclaw not found after install

معمولاً مشکل PATH است. [عیب‌یابی Node.js](</fa/install/node#troubleshooting>) را ببینید.

## مرتبط

  * [نمای کلی نصب](</fa/install>)
  * [به‌روزرسانی](</fa/install/updating>)
  * [حذف نصب](</fa/install/uninstall>)


Was this useful?YesNo