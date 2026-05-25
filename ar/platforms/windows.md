---
title: Windows
source_url: https://docs.openclaw.ai/ar/platforms/windows
scraped_at: 2026-05-25
---

يدعم OpenClaw كلاً من **Windows الأصلي** و **WSL2**. يُعد WSL2 المسار الأكثر استقرارًا والموصى به للتجربة الكاملة — حيث تعمل CLI وGateway والأدوات داخل Linux بتوافق كامل. يعمل Windows الأصلي لاستخدام CLI وGateway الأساسي، مع بعض التنبيهات المذكورة أدناه.

تطبيقات Windows الأصلية المرافقة مخطط لها.

## WSL2 (موصى به)

  * [بدء الاستخدام](</ar/start/getting-started>) (استخدمه داخل WSL)
  * [التثبيت والتحديثات](</ar/install/updating>)
  * دليل WSL2 الرسمي (Microsoft): <https://learn.microsoft.com/windows/wsl/install>


## حالة Windows الأصلي

تتحسن مسارات CLI على Windows الأصلي، لكن WSL2 لا يزال المسار الموصى به.

ما يعمل جيدًا على Windows الأصلي اليوم:

  * مثبّت الموقع عبر `install.ps1`
  * استخدام CLI المحلي مثل `openclaw --version` و`openclaw doctor` و`openclaw plugins list --json`
  * اختبارات دخان الوكيل/المزوّد المحلي المضمّن مثل:

powershellCopy code
[code]
    openclaw agent --local --agent main --thinking low -m "Reply with exactly WINDOWS-HATCH-OK."
[/code]

التنبيهات الحالية:

  * ما زال `openclaw onboard --non-interactive` يتوقع Gateway محليًا يمكن الوصول إليه ما لم تمرر `--skip-health`
  * يحاول `openclaw onboard --non-interactive --install-daemon` و`openclaw gateway install` استخدام مهام Windows المجدولة أولًا
  * إذا رُفض إنشاء المهمة المجدولة، يرجع OpenClaw إلى عنصر تسجيل دخول في مجلد بدء التشغيل لكل مستخدم ويبدأ Gateway فورًا
  * إذا تعطّل `schtasks` نفسه أو توقف عن الاستجابة، فإن OpenClaw يجهض ذلك المسار بسرعة الآن ويرجع إلى المسار البديل بدلًا من التعليق إلى الأبد
  * لا تزال المهام المجدولة مفضلة عند توفرها لأنها توفر حالة إشراف أفضل


إذا كنت تريد CLI الأصلي فقط، من دون تثبيت خدمة Gateway، فاستخدم أحد هذين الأمرين:

powershellCopy code
[code]
    openclaw onboard --non-interactive --skip-healthopenclaw gateway run
[/code]

إذا كنت تريد فعلًا بدء تشغيل مُدارًا على Windows الأصلي:

powershellCopy code
[code]
    openclaw gateway installopenclaw gateway status --json
[/code]

إذا حُظر إنشاء المهمة المجدولة، فسيظل وضع الخدمة البديل يبدأ تلقائيًا بعد تسجيل الدخول من خلال مجلد بدء التشغيل للمستخدم الحالي.

## Gateway

  * [دليل تشغيل Gateway](</ar/gateway>)
  * [التكوين](</ar/gateway/configuration>)


## تثبيت خدمة Gateway (CLI)

داخل WSL2:

CodeCopy code
[code]
    openclaw onboard --install-daemon
[/code]

أو:

CodeCopy code
[code]
    openclaw gateway install
[/code]

أو:

CodeCopy code
[code]
    openclaw configure
[/code]

اختر **خدمة Gateway** عند المطالبة.

الإصلاح/الترحيل:

CodeCopy code
[code]
    openclaw doctor
[/code]

## بدء Gateway تلقائيًا قبل تسجيل الدخول إلى Windows

للإعدادات بلا واجهة، تأكد من تشغيل سلسلة الإقلاع كاملة حتى عندما لا يسجل أحد الدخول إلى Windows.

### 1) إبقاء خدمات المستخدم قيد التشغيل من دون تسجيل دخول

داخل WSL:

bashCopy code
[code]
    sudo loginctl enable-linger "$(whoami)"
[/code]

### 2) تثبيت خدمة مستخدم Gateway الخاصة بـOpenClaw

داخل WSL:

bashCopy code
[code]
    openclaw gateway install
[/code]

### 3) بدء WSL تلقائيًا عند إقلاع Windows

في PowerShell كمسؤول:

powershellCopy code
[code]
    schtasks /create /tn "WSL Boot" /tr "wsl.exe -d Ubuntu --exec /bin/true" /sc onstart /ru SYSTEM
[/code]

استبدل `Ubuntu` باسم التوزيعة لديك من:

powershellCopy code
[code]
    wsl --list --verbose
[/code]

### التحقق من سلسلة بدء التشغيل

بعد إعادة التشغيل (قبل تسجيل الدخول إلى Windows)، تحقق من WSL:

bashCopy code
[code]
    systemctl --user is-enabled openclaw-gateway.servicesystemctl --user status openclaw-gateway.service --no-pager
[/code]

## متقدم: كشف خدمات WSL عبر الشبكة المحلية LAN (portproxy)

لدى WSL شبكته الافتراضية الخاصة. إذا احتاج جهاز آخر إلى الوصول إلى خدمة تعمل **داخل WSL** (SSH، أو خادم TTS محلي، أو Gateway)، فيجب عليك تمرير منفذ Windows إلى عنوان IP الحالي الخاص بـWSL. يتغير عنوان IP الخاص بـWSL بعد عمليات إعادة التشغيل، لذلك قد تحتاج إلى تحديث قاعدة التمرير.

مثال (PowerShell **كمسؤول**):

powershellCopy code
[code]
    $Distro = "Ubuntu-24.04"$ListenPort = 2222$TargetPort = 22 $WslIp = (wsl -d $Distro -- hostname -I).Trim().Split(" ")[0]if (-not $WslIp) { throw "WSL IP not found." } netsh interface portproxy add v4tov4 listenaddress=0.0.0.0 listenport=$ListenPort `  connectaddress=$WslIp connectport=$TargetPort
[/code]

اسمح للمنفذ عبر جدار حماية Windows (مرة واحدة):

powershellCopy code
[code]
    New-NetFirewallRule -DisplayName "WSL SSH $ListenPort" -Direction Inbound `  -Protocol TCP -LocalPort $ListenPort -Action Allow
[/code]

حدّث portproxy بعد إعادة تشغيل WSL:

powershellCopy code
[code]
    netsh interface portproxy delete v4tov4 listenport=$ListenPort listenaddress=0.0.0.0 | Out-Nullnetsh interface portproxy add v4tov4 listenport=$ListenPort listenaddress=0.0.0.0 `  connectaddress=$WslIp connectport=$TargetPort | Out-Null
[/code]

ملاحظات:

  * يستهدف SSH من جهاز آخر **عنوان IP لمضيف Windows** (مثال: `ssh user@windows-host -p 2222`).
  * يجب أن تشير العقد البعيدة إلى عنوان URL لـGateway **يمكن الوصول إليه** (وليس `127.0.0.1`)؛ استخدم `openclaw status --all` للتأكيد.
  * استخدم `listenaddress=0.0.0.0` للوصول عبر LAN؛ أما `127.0.0.1` فيبقيه محليًا فقط.
  * إذا كنت تريد جعل هذا تلقائيًا، فسجّل مهمة مجدولة لتشغيل خطوة التحديث عند تسجيل الدخول.


## تثبيت WSL2 خطوة بخطوة

### 1) تثبيت WSL2 + Ubuntu

افتح PowerShell (مسؤول):

powershellCopy code
[code]
    wsl --install# Or pick a distro explicitly:wsl --list --onlinewsl --install -d Ubuntu-24.04
[/code]

أعد التشغيل إذا طلب Windows ذلك.

### 2) تمكين systemd (مطلوب لتثبيت Gateway)

في طرفية WSL لديك:

bashCopy code
[code]
    sudo tee /etc/wsl.conf >/dev/null <<'EOF'[boot]systemd=trueEOF
[/code]

ثم من PowerShell:

powershellCopy code
[code]
    wsl --shutdown
[/code]

أعد فتح Ubuntu، ثم تحقق:

bashCopy code
[code]
    systemctl --user status
[/code]

### 3) تثبيت OpenClaw (داخل WSL)

لإعداد عادي لأول مرة داخل WSL، اتبع مسار بدء الاستخدام الخاص بـLinux:

bashCopy code
[code]
    git clone https://github.com/openclaw/openclaw.gitcd openclawpnpm installpnpm buildpnpm ui:buildpnpm openclaw onboard --install-daemon
[/code]

إذا كنت تطوّر من المصدر بدلًا من إجراء تهيئة أولية لأول مرة، فاستخدم حلقة تطوير المصدر من [الإعداد](</ar/start/setup>):

bashCopy code
[code]
    pnpm install# First run only (or after resetting local OpenClaw config/workspace)pnpm openclaw setuppnpm gateway:watch
[/code]

الدليل الكامل: [بدء الاستخدام](</ar/start/getting-started>)

## تطبيق Windows المرافق

ليس لدينا تطبيق Windows مرافق بعد. نرحب بالمساهمات إذا كنت تريد المساعدة في تحقيق ذلك.

## اتصال Git وGitHub (للمساهمين)

تحظر بعض الشبكات HTTPS إلى GitHub أو تخنقه. إذا فشل `git clone` بسبب انتهاء المهلة أو إعادة تعيين الاتصال، فجرّب شبكة أخرى، أو VPN، أو وكيل HTTP/HTTPS توفره مؤسستك.

إذا فشل `gh auth login` أثناء مسار جهاز المتصفح (على سبيل المثال انتهاء مهلة الوصول إلى `github.com:443`)، فصادق باستخدام رمز وصول شخصي بدلًا من ذلك:

  1. أنشئ رمزًا بنطاق `repo` على الأقل (PAT كلاسيكي) أو وصولًا دقيق الصلاحيات مكافئًا.
  2. في PowerShell للجلسة الحالية:

powershellCopy code
[code]
    $env:GH_TOKEN="<your-token>"gh auth statusgh auth setup-git
[/code]

  3. إذا حذّر `gh auth status` من فقدان `read:org`، فأصدر رمزًا يتضمن ذلك النطاق وأعد تعيين المتغير:

powershellCopy code
[code]
    $env:GH_TOKEN="<your-token-with-repo-and-read:org>"gh auth status
[/code]

ينطبق `gh auth refresh -s read:org` فقط عندما تكون قد صادقت عبر `gh auth login` ولديك بيانات اعتماد مخزنة لتحديثها (وليس عند استخدام `GH_TOKEN`).

لا تلتزم بالرموز مطلقًا ولا تلصقها في القضايا أو طلبات السحب.

## ذات صلة

  * [نظرة عامة على التثبيت](</ar/install>)
  * [المنصات](</ar/platforms>)


Was this useful?YesNo