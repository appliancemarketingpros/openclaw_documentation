---
title: التثبيت
source_url: https://docs.openclaw.ai/ar/install
scraped_at: 2026-05-25
---

## متطلبات النظام

  * **Node 24** (موصى به) أو Node 22.16+ - يتولى نص التثبيت البرمجي ذلك تلقائيا
  * **macOS أو Linux أو Windows** \- يدعم كل من Windows الأصلي و WSL2؛ و WSL2 أكثر استقرارا. راجع [Windows](</ar/platforms/windows>).
  * لا تحتاج إلى `pnpm` إلا إذا كنت تبني من المصدر


## موصى به: نص التثبيت البرمجي

أسرع طريقة للتثبيت. يكتشف نظام التشغيل لديك، ويثبت Node عند الحاجة، ويثبت OpenClaw، ويشغل الإعداد الأولي.

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

للتثبيت من دون تشغيل الإعداد الأولي:

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

لجميع العلامات وخيارات CI/الأتمتة، راجع [تفاصيل المثبت الداخلية](</ar/install/installer>).

## طرق التثبيت البديلة

### مثبت البادئة المحلية (`install-cli.sh`)

استخدم هذا عندما تريد إبقاء OpenClaw و Node ضمن بادئة محلية مثل `~/.openclaw`، من دون الاعتماد على تثبيت Node على مستوى النظام:

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install-cli.sh | bash
[/code]

يدعم تثبيتات npm افتراضيا، إضافة إلى تثبيتات السحب من git ضمن تدفق البادئة نفسه. المرجع الكامل: [تفاصيل المثبت الداخلية](</ar/install/installer#install-clish>).

مثبت بالفعل؟ بدّل بين تثبيتات الحزمة و git باستخدام `openclaw update --channel dev` و `openclaw update --channel stable`. راجع [التحديث](</ar/install/updating#switch-between-npm-and-git-installs>).

### npm أو pnpm أو bun

إذا كنت تدير Node بنفسك بالفعل:

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

إذا فشل `sharp` بسبب libvips مثبت عالميا:

bashCopy code
[code]
    SHARP_IGNORE_GLOBAL_LIBVIPS=1 npm install -g openclaw@latest
[/code]

### من المصدر

للمساهمين أو أي شخص يريد التشغيل من نسخة محلية:

bashCopy code
[code]
    git clone https://github.com/openclaw/openclaw.gitcd openclawpnpm install && pnpm build && pnpm ui:buildpnpm link --globalopenclaw onboard --install-daemon
[/code]

أو تجاوز الربط واستخدم `pnpm openclaw ...` من داخل المستودع. راجع [الإعداد](</ar/start/setup>) لتدفقات عمل التطوير الكاملة.

### التثبيت من GitHub main

bashCopy code
[code]
    npm install -g github:openclaw/openclaw#main
[/code]

### الحاويات ومديرو الحزم

[**Docker** عمليات نشر ضمن حاويات أو بلا واجهة رسومية. ](</ar/install/docker>) [**Podman** بديل حاويات بلا صلاحيات جذرية لـ Docker. ](</ar/install/podman>) [**Nix** تثبيت تصريحي عبر Nix flake. ](</ar/install/nix>) [**Ansible** توفير آلي لأسطول الأجهزة. ](</ar/install/ansible>) [**Bun** استخدام CLI فقط عبر وقت تشغيل Bun. ](</ar/install/bun>)

## التحقق من التثبيت

bashCopy code
[code]
    openclaw --version      # confirm the CLI is availableopenclaw doctor         # check for config issuesopenclaw gateway status # verify the Gateway is running
[/code]

إذا كنت تريد بدءا مداريا بعد التثبيت:

  * macOS: LaunchAgent عبر `openclaw onboard --install-daemon` أو `openclaw gateway install`
  * Linux/WSL2: خدمة systemd للمستخدم عبر الأوامر نفسها
  * Windows الأصلي: Scheduled Task أولا، مع عنصر تسجيل دخول في مجلد Startup لكل مستخدم كخيار احتياطي إذا رفض إنشاء المهمة


## الاستضافة والنشر

انشر OpenClaw على خادم سحابي أو VPS:

[**VPS** [**Docker VM** [**Kubernetes** OPENCLAW_DOCS_MARKER:cardOpen:IHRpdGxlPSJGbHkuaW8iIGhyZWY9Ii9hci9pbnN0YWxsL2ZseSI [Fly.io](<http://Fly.io>) OPENCLAW_DOCS_MARKER:cardClose: [**Hetzner** [**GCP** [**Azure** [**Railway** [**Render** [**Northflank** التحديث أو الترحيل أو إلغاء التثبيت [**Updating** حافظ على OpenClaw محدثا. ](</ar/install/updating>) [**Migrating** الانتقال إلى جهاز جديد. ](</ar/install/migrating>) [**Uninstall** أزل OpenClaw بالكامل. ](</ar/install/uninstall>) استكشاف الأخطاء وإصلاحها: لم يتم العثور على `openclaw` إذا نجح التثبيت لكن لم يتم العثور على `openclaw` في الطرفية لديك: bashCopy code
[code]
    node -v           # Node installed?npm prefix -g     # Where are global packages?echo "$PATH"      # Is the global bin dir in PATH?
[/code]

إذا لم يكن `$(npm prefix -g)/bin` ضمن `$PATH` لديك، فأضفه إلى ملف بدء تشغيل الصدفة (`~/.zshrc` أو `~/.bashrc`): bashCopy code
[code]
    export PATH="$(npm prefix -g)/bin:$PATH"
[/code]

ثم افتح طرفية جديدة. راجع [إعداد Node](</ar/install/node>) لمزيد من التفاصيل. ](</ar/install/northflank>) Was this useful?YesNo ](</ar/install/render>)](</ar/install/railway>)](</ar/install/azure>)](</ar/install/gcp>)](</ar/install/hetzner>)](</ar/install/kubernetes>)](</ar/install/docker-vm-runtime>)](</ar/vps>)