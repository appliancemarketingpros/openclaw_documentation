---
title: Node.js
source_url: https://docs.openclaw.ai/fa/install/node
scraped_at: 2026-05-25
---

OpenClaw به **Node 22.16 یا جدیدتر** نیاز دارد. **Node 24 محیط اجرای پیش‌فرض و پیشنهادی** برای نصب‌ها، CI و گردش‌کارهای انتشار است. Node 22 همچنان از طریق خط LTS فعال پشتیبانی می‌شود. [اسکریپت نصب‌کننده](</fa/install#alternative-install-methods>) به‌صورت خودکار Node را شناسایی و نصب می‌کند - این صفحه برای زمانی است که می‌خواهید خودتان Node را راه‌اندازی کنید و مطمئن شوید همه‌چیز درست متصل شده است (نسخه‌ها، PATH، نصب‌های سراسری).

## نسخه خود را بررسی کنید

bashCopy code
[code]
    node -v
[/code]

اگر این دستور `v24.x.x` یا بالاتر چاپ کرد، روی پیش‌فرض پیشنهادی هستید. اگر `v22.16.x` یا بالاتر چاپ کرد، روی مسیر پشتیبانی‌شده Node 22 LTS هستید، اما همچنان پیشنهاد می‌کنیم در زمان مناسب به Node 24 ارتقا دهید. اگر Node نصب نیست یا نسخه آن بیش از حد قدیمی است، یکی از روش‌های نصب زیر را انتخاب کنید.

## نصب Node

### macOS

**Homebrew** (پیشنهادی):

bashCopy code
[code]
    brew install node
[/code]

یا نصب‌کننده macOS را از [nodejs.org](<https://nodejs.org/>) دانلود کنید.

### Linux

**Ubuntu / Debian:**

bashCopy code
[code]
    curl -fsSL https://deb.nodesource.com/setup_24.x | sudo -E bash -sudo apt-get install -y nodejs
[/code]

**Fedora / RHEL:**

bashCopy code
[code]
    sudo dnf install nodejs
[/code]

یا از یک مدیر نسخه استفاده کنید (پایین را ببینید).

### Windows

**winget** (پیشنهادی):

powershellCopy code
[code]
    winget install OpenJS.NodeJS.LTS
[/code]

**Chocolatey:**

powershellCopy code
[code]
    choco install nodejs-lts
[/code]

یا نصب‌کننده Windows را از [nodejs.org](<https://nodejs.org/>) دانلود کنید.

Using a version manager (nvm, fnm, mise, asdf)

مدیران نسخه به شما امکان می‌دهند به‌سادگی بین نسخه‌های Node جابه‌جا شوید. گزینه‌های محبوب:

  * [**fnm**](<https://github.com/Schniz/fnm>) \- سریع، چندسکویی
  * [**nvm**](<https://github.com/nvm-sh/nvm>) \- پرکاربرد در macOS/Linux
  * [**mise**](<https://mise.jdx.dev/>) \- چندزبانه (Node، Python، Ruby و غیره)


نمونه با fnm:

bashCopy code
[code]
    fnm install 24fnm use 24
[/code]

## عیب‌یابی

### `openclaw: command not found`

این تقریباً همیشه یعنی دایرکتوری bin سراسری npm در PATH شما نیست.

* ### Find your global npm prefix

bashCopy code
[code]
    npm prefix -g
[/code]

* ### Check if it's on your PATH

bashCopy code
[code]
    echo "$PATH"
[/code]

در خروجی به‌دنبال `<npm-prefix>/bin` (macOS/Linux) یا `<npm-prefix>` (Windows) بگردید.

* ### Add it to your shell startup file

### macOS / Linux

به `~/.zshrc` یا `~/.bashrc` اضافه کنید:

bashCopy code
[code]
    export PATH="$(npm prefix -g)/bin:$PATH"
[/code]

سپس یک ترمینال جدید باز کنید (یا در zsh دستور `rehash` / در bash دستور `hash -r` را اجرا کنید).

### Windows

خروجی `npm prefix -g` را از طریق Settings → System → Environment Variables به PATH سیستم خود اضافه کنید.

### خطاهای مجوز در `npm install -g` (Linux)

اگر خطاهای `EACCES` می‌بینید، prefix سراسری npm را به دایرکتوری‌ای تغییر دهید که کاربر بتواند در آن بنویسد:

bashCopy code
[code]
    mkdir -p "$HOME/.npm-global"npm config set prefix "$HOME/.npm-global"export PATH="$HOME/.npm-global/bin:$PATH"
[/code]

خط `export PATH=...` را به `~/.bashrc` یا `~/.zshrc` خود اضافه کنید تا دائمی شود.

## مرتبط

  * [نمای کلی نصب](</fa/install>) \- همه روش‌های نصب
  * [به‌روزرسانی](</fa/install/updating>) \- به‌روز نگه داشتن OpenClaw
  * [شروع به کار](</fa/start/getting-started>) \- گام‌های نخست پس از نصب


Was this useful?YesNo