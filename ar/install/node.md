---
title: Node.js
source_url: https://docs.openclaw.ai/ar/install/node
scraped_at: 2026-05-25
---

يتطلب OpenClaw **Node 22.16 أو أحدث**. **Node 24 هو وقت التشغيل الافتراضي والموصى به** للتثبيتات وCI وسير عمل الإصدارات. يظل Node 22 مدعومًا عبر خط LTS النشط. سيكتشف [نص التثبيت](</ar/install#alternative-install-methods>) Node ويثبته تلقائيًا - هذه الصفحة مخصصة للحالات التي تريد فيها إعداد Node بنفسك والتأكد من توصيل كل شيء بشكل صحيح (الإصدارات، PATH، التثبيتات العامة).

## تحقق من إصدارك

bashCopy code
[code]
    node -v
[/code]

إذا طبع هذا الأمر `v24.x.x` أو أعلى، فأنت تستخدم الإعداد الافتراضي الموصى به. إذا طبع `v22.16.x` أو أعلى، فأنت على مسار Node 22 LTS المدعوم، لكننا لا نزال نوصي بالترقية إلى Node 24 عندما يكون ذلك مناسبًا. إذا لم يكن Node مثبتًا أو كان الإصدار قديمًا جدًا، فاختر إحدى طرق التثبيت أدناه.

## تثبيت Node

### macOS

**Homebrew** (موصى به):

bashCopy code
[code]
    brew install node
[/code]

أو نزّل مثبت macOS من [nodejs.org](<https://nodejs.org/>).

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

أو استخدم مدير إصدارات (انظر أدناه).

### Windows

**winget** (موصى به):

powershellCopy code
[code]
    winget install OpenJS.NodeJS.LTS
[/code]

**Chocolatey:**

powershellCopy code
[code]
    choco install nodejs-lts
[/code]

أو نزّل مثبت Windows من [nodejs.org](<https://nodejs.org/>).

Using a version manager (nvm, fnm, mise, asdf)

تتيح لك مديرات الإصدارات التبديل بين إصدارات Node بسهولة. خيارات شائعة:

  * [**fnm**](<https://github.com/Schniz/fnm>) \- سريع ومتعدد المنصات
  * [**nvm**](<https://github.com/nvm-sh/nvm>) \- مستخدم على نطاق واسع في macOS/Linux
  * [**mise**](<https://mise.jdx.dev/>) \- متعدد اللغات (Node وPython وRuby وغيرها)


مثال باستخدام fnm:

bashCopy code
[code]
    fnm install 24fnm use 24
[/code]

## استكشاف الأخطاء وإصلاحها

### `openclaw: command not found`

يعني هذا غالبًا أن دليل bin العام الخاص بـ npm غير موجود في PATH لديك.

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

ابحث عن `<npm-prefix>/bin` (macOS/Linux) أو `<npm-prefix>` (Windows) في الناتج.

* ### Add it to your shell startup file

### macOS / Linux

أضف إلى `~/.zshrc` أو `~/.bashrc`:

bashCopy code
[code]
    export PATH="$(npm prefix -g)/bin:$PATH"
[/code]

ثم افتح طرفية جديدة (أو شغّل `rehash` في zsh / `hash -r` في bash).

### Windows

أضف ناتج `npm prefix -g` إلى PATH الخاص بالنظام عبر Settings → System → Environment Variables.

### أخطاء الأذونات في `npm install -g` (Linux)

إذا رأيت أخطاء `EACCES`، فبدّل البادئة العامة لـ npm إلى دليل يمكن للمستخدم الكتابة فيه:

bashCopy code
[code]
    mkdir -p "$HOME/.npm-global"npm config set prefix "$HOME/.npm-global"export PATH="$HOME/.npm-global/bin:$PATH"
[/code]

أضف سطر `export PATH=...` إلى `~/.bashrc` أو `~/.zshrc` لديك لجعله دائمًا.

## ذو صلة

  * [نظرة عامة على التثبيت](</ar/install>) \- جميع طرق التثبيت
  * [التحديث](</ar/install/updating>) \- إبقاء OpenClaw محدثًا
  * [بدء الاستخدام](</ar/start/getting-started>) \- الخطوات الأولى بعد التثبيت


Was this useful?YesNo