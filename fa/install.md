---
title: نصب
source_url: https://docs.openclaw.ai/fa/install
scraped_at: 2026-05-25
---

## الزامات سیستم

  * **Node 24** (توصیه‌شده) یا Node 22.16+ - اسکریپت نصب این مورد را به‌صورت خودکار مدیریت می‌کند
  * **macOS، Linux یا Windows** \- هم Windows بومی و هم WSL2 پشتیبانی می‌شوند؛ WSL2 پایدارتر است. [Windows](</fa/platforms/windows>) را ببینید.
  * `pnpm` فقط زمانی لازم است که از سورس بسازید


## توصیه‌شده: اسکریپت نصب

سریع‌ترین راه نصب. سیستم‌عامل شما را تشخیص می‌دهد، در صورت نیاز Node را نصب می‌کند، OpenClaw را نصب می‌کند و فرایند راه‌اندازی اولیه را اجرا می‌کند.

### macOS / Linux / WSL2

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash
[/code]

### Windows (PowerShell)

powershellCopy code
[code]
    iwr -useb https://openclaw.ai/install.ps1 | iex
[/code]

برای نصب بدون اجرای راه‌اندازی اولیه:

### macOS / Linux / WSL2

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash -s -- --no-onboard
[/code]

### Windows (PowerShell)

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -NoOnboard
[/code]

برای همه فلگ‌ها و گزینه‌های CI/خودکارسازی، [جزئیات داخلی نصب‌کننده](</fa/install/installer>) را ببینید.

## روش‌های جایگزین نصب

### نصب‌کننده پیشوند محلی (`install-cli.sh`)

وقتی می‌خواهید OpenClaw و Node زیر یک پیشوند محلی مانند `~/.openclaw` نگه داشته شوند، بدون وابستگی به نصب سراسری Node، از این روش استفاده کنید:

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install-cli.sh | bash
[/code]

به‌صورت پیش‌فرض از نصب‌های npm پشتیبانی می‌کند، به‌علاوه نصب‌های git-checkout را نیز در همان جریان پیشوند پشتیبانی می‌کند. مرجع کامل: [جزئیات داخلی نصب‌کننده](</fa/install/installer#install-clish>).

قبلا نصب کرده‌اید؟ با `openclaw update --channel dev` و `openclaw update --channel stable` بین نصب‌های بسته‌ای و git جابه‌جا شوید. [به‌روزرسانی](</fa/install/updating#switch-between-npm-and-git-installs>) را ببینید.

### npm، pnpm، یا bun

اگر خودتان Node را مدیریت می‌کنید:

### npm

bashCopy code
[code]
    npm install -g openclaw@latestopenclaw onboard --install-daemon
[/code]

### pnpm

bashCopy code
[code]
    pnpm add -g openclaw@latestpnpm approve-builds -gopenclaw onboard --install-daemon
[/code]

### bun

bashCopy code
[code]
    bun add -g openclaw@latestopenclaw onboard --install-daemon
[/code]

Troubleshooting: sharp build errors (npm)

اگر `sharp` به‌دلیل یک libvips نصب‌شده به‌صورت سراسری شکست خورد:

bashCopy code
[code]
    SHARP_IGNORE_GLOBAL_LIBVIPS=1 npm install -g openclaw@latest
[/code]

### از سورس

برای مشارکت‌کنندگان یا هر کسی که می‌خواهد از checkout محلی اجرا کند:

bashCopy code
[code]
    git clone https://github.com/openclaw/openclaw.gitcd openclawpnpm install && pnpm build && pnpm ui:buildpnpm link --globalopenclaw onboard --install-daemon
[/code]

یا لینک را نادیده بگیرید و از داخل مخزن از `pnpm openclaw ...` استفاده کنید. برای جریان‌های کاری کامل توسعه، [راه‌اندازی](</fa/start/setup>) را ببینید.

### نصب از GitHub main

bashCopy code
[code]
    npm install -g github:openclaw/openclaw#main
[/code]

### کانتینرها و مدیران بسته

[**Docker** استقرارهای کانتینری یا بدون رابط گرافیکی. ](</fa/install/docker>) [**Podman** جایگزین کانتینر بدون root برای Docker. ](</fa/install/podman>) [**Nix** نصب اعلانی از طریق Nix flake. ](</fa/install/nix>) [**Ansible** آماده‌سازی خودکار ناوگان. ](</fa/install/ansible>) [**Bun** استفاده فقط از CLI از طریق زمان اجرای Bun. ](</fa/install/bun>)

## بررسی نصب

bashCopy code
[code]
    openclaw --version      # confirm the CLI is availableopenclaw doctor         # check for config issuesopenclaw gateway status # verify the Gateway is running
[/code]

اگر پس از نصب راه‌اندازی مدیریت‌شده می‌خواهید:

  * macOS: ‏LaunchAgent از طریق `openclaw onboard --install-daemon` یا `openclaw gateway install`
  * Linux/WSL2: سرویس کاربری systemd از طریق همان فرمان‌ها
  * Windows بومی: ابتدا Scheduled Task، همراه با گزینه جایگزین آیتم ورود پوشه Startup برای هر کاربر اگر ساخت task رد شود


## میزبانی و استقرار

OpenClaw را روی سرور ابری یا VPS مستقر کنید:

[**VPS** [**Docker VM** [**Kubernetes** OPENCLAW_DOCS_MARKER:cardOpen:IHRpdGxlPSJGbHkuaW8iIGhyZWY9Ii9mYS9pbnN0YWxsL2ZseSI [Fly.io](<http://Fly.io>) OPENCLAW_DOCS_MARKER:cardClose: [**Hetzner** [**GCP** [**Azure** [**Railway** [**Render** [**Northflank** به‌روزرسانی، مهاجرت، یا حذف نصب [**Updating** OpenClaw را به‌روز نگه دارید. ](</fa/install/updating>) [**Migrating** به یک ماشین جدید منتقل شوید. ](</fa/install/migrating>) [**Uninstall** OpenClaw را به‌طور کامل حذف کنید. ](</fa/install/uninstall>) عیب‌یابی: `openclaw` پیدا نشد اگر نصب موفق بود اما `openclaw` در ترمینال شما پیدا نمی‌شود: bashCopy code
[code]
    node -v           # Node installed?npm prefix -g     # Where are global packages?echo "$PATH"      # Is the global bin dir in PATH?
[/code]

اگر `$(npm prefix -g)/bin` در `$PATH` شما نیست، آن را به فایل راه‌اندازی shell خود (`~/.zshrc` یا `~/.bashrc`) اضافه کنید: bashCopy code
[code]
    export PATH="$(npm prefix -g)/bin:$PATH"
[/code]

سپس یک ترمینال جدید باز کنید. برای جزئیات بیشتر، [راه‌اندازی Node](</fa/install/node>) را ببینید. ](</fa/install/northflank>) Was this useful?YesNo ](</fa/install/render>)](</fa/install/railway>)](</fa/install/azure>)](</fa/install/gcp>)](</fa/install/hetzner>)](</fa/install/kubernetes>)](</fa/install/docker-vm-runtime>)](</fa/vps>)