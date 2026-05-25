---
title: تطبيق Linux
source_url: https://docs.openclaw.ai/ar/platforms/linux
scraped_at: 2026-05-25
---

Gateway مدعوم بالكامل على Linux. **Node هو بيئة التشغيل الموصى بها**. لا يوصى باستخدام Bun مع Gateway (بسبب أخطاء WhatsApp/Telegram).

تطبيقات Linux المرافقة الأصلية مخطط لها. المساهمات مرحب بها إذا كنت تريد المساعدة في بناء أحدها.

## المسار السريع للمبتدئين (VPS)

  1. ثبّت Node 24 (موصى به؛ Node 22 LTS، حاليًا `22.16+`، ما زال يعمل للتوافق)
  2. `npm i -g openclaw@latest`
  3. `openclaw onboard --install-daemon`
  4. من حاسوبك المحمول: `ssh -N -L 18789:127.0.0.1:18789 <user>@<host>`
  5. افتح `http://127.0.0.1:18789/` وصادِق باستخدام السر المشترك المكوّن (رمز افتراضيًا؛ أو كلمة مرور إذا ضبطت `gateway.auth.mode: "password"`)


دليل خادم Linux الكامل: [خادم Linux](</ar/vps>). مثال VPS خطوة بخطوة: [exe.dev](</ar/install/exe-dev>)

## التثبيت

  * [البدء](</ar/start/getting-started>)
  * [التثبيت والتحديثات](</ar/install/updating>)
  * مسارات اختيارية: [Bun (تجريبي)](</ar/install/bun>)، [Nix](</ar/install/nix>)، [Docker](</ar/install/docker>)


## Gateway

  * [دليل تشغيل Gateway](</ar/gateway>)
  * [التكوين](</ar/gateway/configuration>)


## تثبيت خدمة Gateway (CLI)

استخدم أحد هذه الخيارات:

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

حدّد **خدمة Gateway** عندما يُطلب منك ذلك.

الإصلاح/الترحيل:

CodeCopy code
[code]
    openclaw doctor
[/code]

## التحكم في النظام (وحدة مستخدم systemd)

يثبّت OpenClaw خدمة systemd خاصة بـ**المستخدم** افتراضيًا. استخدم خدمة **نظام** للخوادم المشتركة أو الدائمة التشغيل. يقوم `openclaw gateway install` و `openclaw onboard --install-daemon` بالفعل بإنشاء الوحدة القياسية الحالية لك؛ اكتب واحدة يدويًا فقط عندما تحتاج إلى إعداد نظام/مدير خدمات مخصص. توجد إرشادات الخدمة الكاملة في [دليل تشغيل Gateway](</ar/gateway>).

إعداد بسيط:

أنشئ `~/.config/systemd/user/openclaw-gateway[-<profile>].service`:

CodeCopy code
[code]
    [Unit]Description=OpenClaw Gateway (profile: <profile>, v<version>)After=network-online.targetWants=network-online.target [Service]ExecStart=/usr/local/bin/openclaw gateway --port 18789Restart=alwaysRestartSec=5TimeoutStopSec=30TimeoutStartSec=30SuccessExitStatus=0 143KillMode=control-group [Install]WantedBy=default.target
[/code]

فعّلها:

CodeCopy code
[code]
    systemctl --user enable --now openclaw-gateway[-<profile>].service
[/code]

## ضغط الذاكرة وعمليات القتل بسبب OOM

على Linux، تختار النواة ضحية OOM عندما تنفد الذاكرة من مضيف أو VM أو cgroup داخل حاوية. قد يكون Gateway ضحية سيئة لأنه يملك جلسات طويلة العمر واتصالات قنوات. لذلك يجعل OpenClaw احتمالية قتل العمليات الفرعية المؤقتة أعلى من Gateway عندما يكون ذلك ممكنًا.

بالنسبة إلى عمليات Linux الفرعية المؤهلة، يبدأ OpenClaw العملية الفرعية عبر غلاف قصير من `/bin/sh` يرفع قيمة `oom_score_adj` الخاصة بالعملية الفرعية إلى `1000`، ثم ينفّذ الأمر الحقيقي باستخدام `exec`. هذه عملية لا تتطلب امتيازات لأن العملية الفرعية تزيد فقط احتمالية قتلها هي نفسها بسبب OOM.

تشمل أسطح العمليات الفرعية المشمولة:

  * العمليات الفرعية للأوامر المُدارة عبر المشرف،
  * العمليات الفرعية لصدفة PTY،
  * العمليات الفرعية لخوادم MCP عبر stdio،
  * عمليات المتصفح/Chrome التي يشغّلها OpenClaw.


الغلاف خاص بـ Linux فقط ويُتخطى عندما لا يكون `/bin/sh` متاحًا. ويُتخطى أيضًا إذا ضبطت بيئة العملية الفرعية `OPENCLAW_CHILD_OOM_SCORE_ADJ=0` أو `false` أو `no` أو `off`.

للتحقق من عملية فرعية:

bashCopy code
[code]
    cat /proc/<child-pid>/oom_score_adj
[/code]

القيمة المتوقعة للعمليات الفرعية المشمولة هي `1000`. يجب أن يحتفظ إجراء Gateway بدرجته العادية، والتي تكون عادةً `0`.

هذا لا يستبدل الضبط الطبيعي للذاكرة. إذا كان VPS أو الحاوية يقتل العمليات الفرعية بشكل متكرر، فارفع حد الذاكرة، أو قلّل التزامن، أو أضف عناصر تحكم أقوى في الموارد مثل `MemoryMax=` في systemd أو حدود الذاكرة على مستوى الحاوية.

## ذات صلة

  * [نظرة عامة على التثبيت](</ar/install>)
  * [خادم Linux](</ar/vps>)
  * [Raspberry Pi](</ar/install/raspberry-pi>)


Was this useful?YesNo