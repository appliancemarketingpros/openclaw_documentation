---
title: دليل تشغيل Mantis Slack لسطح المكتب
source_url: https://docs.openclaw.ai/ar/concepts/mantis-slack-desktop-runbook
scraped_at: 2026-05-25
---

Mantis Slack desktop QA هو مسار واجهة المستخدم الحقيقية لأخطاء فئة Slack التي تحتاج إلى سطح مكتب Linux، وإنقاذ عبر VNC، وSlack Web، وGateway حقيقي من OpenClaw، ولقطات شاشة، وفيديوهات، وتعليق أدلة على PR.

استخدمه عندما لا تستطيع اختبارات الوحدة أو مسار Slack الحي عديم الواجهة إثبات الخطأ.

## نموذج التخزين

يستخدم Mantis ثلاث طبقات تخزين مختلفة:

  * صورة المزوّد: يملكها Crabbox وتُخزَّن في حساب مزوّد السحابة. تحتوي على قدرات الجهاز مثل Chrome/Chromium، وffmpeg، وscrot، وNode/corepack/pnpm، وأدوات البناء الأصلية، ومجلدات تخزين مؤقت فارغة.
  * حالة التأجير الدافئة: تملكها جلسة المشغّل الحالية. يمكن أن تحتوي على ملف تعريف متصفح مسجّل الدخول، و`/var/cache/crabbox/pnpm`، ونسخة مصدر جاهزة أثناء بقاء التأجير حيًا.
  * آثار Mantis: تملكها عملية تشغيل OpenClaw. توجد تحت `.artifacts/qa-e2e/mantis/...`، ثم يرفعها GitHub Actions ويعلّق تطبيق Mantis GitHub App أدلة مضمنة على PR.


لا تضع أبدًا أسرارًا، أو ملفات تعريف ارتباط المتصفح، أو حالة تسجيل دخول Slack، أو نسخ المستودعات، أو `node_modules`، أو `dist/` داخل صورة مزوّد مخبوزة مسبقًا.

## إرسال GitHub

شغّل سير العمل من `main`:

bashCopy code
[code]
    gh workflow run mantis-slack-desktop-smoke.yml \  --ref main \  -f candidate_ref=<trusted-ref-or-sha> \  -f pr_number=<pr-number> \  -f scenario_id=slack-canary \  -f crabbox_provider=aws \  -f keep_vm=false \  -f hydrate_mode=source
[/code]

قيم `candidate_ref` المسموح بها ضيقة عمدًا لأن سير العمل يستخدم بيانات اعتماد حية: أصل `main` الحالي، أو وسوم الإصدار، أو رأس PR مفتوح من `openclaw/openclaw`.

يكتب سير العمل:

  * الأثر المرفوع: `mantis-slack-desktop-smoke-<run-id>-<attempt>`;
  * تعليق PR مضمن من تطبيق Mantis GitHub App؛
  * `slack-desktop-smoke.png`;
  * `slack-desktop-smoke.mp4`;
  * `slack-desktop-smoke-preview.gif`;
  * `slack-desktop-smoke-change.mp4`;
  * `mantis-slack-desktop-smoke-summary.json`;
  * `mantis-slack-desktop-smoke-report.md`;
  * سجلات بعيدة مثل `slack-desktop-command.log`، و`openclaw-gateway.log`، و`chrome.log`، و`ffmpeg.log`.


يُحدَّث تعليق PR في موضعه عبر العلامة المخفية `<!-- mantis-slack-desktop-smoke -->`.

## CLI المحلية

إثبات مصدر بارد:

bashCopy code
[code]
    pnpm openclaw qa mantis slack-desktop-smoke \  --provider aws \  --class standard \  --gateway-setup \  --credential-source convex \  --credential-role maintainer \  --provider-mode live-frontier \  --model openai/gpt-5.4 \  --alt-model openai/gpt-5.4 \  --scenario slack-canary \  --hydrate-mode source
[/code]

أبقِ الآلة الافتراضية لإنقاذ VNC:

bashCopy code
[code]
    pnpm openclaw qa mantis slack-desktop-smoke \  --provider aws \  --class standard \  --gateway-setup \  --scenario slack-canary \  --keep-lease
[/code]

افتح VNC:

bashCopy code
[code]
    crabbox vnc --provider aws --id <cbx_id> --open
[/code]

أعد استخدام تأجير دافئ:

bashCopy code
[code]
    pnpm openclaw qa mantis slack-desktop-smoke \  --provider aws \  --lease-id <cbx_id-or-slug> \  --gateway-setup \  --scenario slack-canary \  --hydrate-mode source
[/code]

استخدم `--hydrate-mode prehydrated` فقط عندما تكون مساحة العمل البعيدة المعاد استخدامها تحتوي مسبقًا على `node_modules` و`dist/` مبني. يفشل Mantis بإغلاق إذا كانت هذه مفقودة.

## أوضاع التهيئة

الوضع | استخدمه عندما | السلوك البعيد | المفاضلة  
---|---|---|---  
`source` | إثبات PR عادي، أجهزة باردة، CI | يشغّل `pnpm install --frozen-lockfile --prefer-offline` و`pnpm build` داخل الآلة الافتراضية | الأبطأ، وأقوى إثبات لنسخة مصدر  
`prehydrated` | حضرتَ عمدًا تأجيرًا معاد استخدامه | يتطلب وجود `node_modules` و`dist/`؛ ويتخطى التثبيت/البناء | سريع، لكنه صالح فقط للتأجيرات الدافئة التي يتحكم بها المشغّل  
  
يحضّر GitHub Actions دائمًا نسخة المرشح قبل تشغيل الآلة الافتراضية. ويُخزَّن مخزن pnpm مؤقتًا بحسب نظام التشغيل، وإصدار Node، وملف القفل. يستخدم تشغيل مصدر الآلة الافتراضية أيضًا `/var/cache/crabbox/pnpm` عند وجوده.

## تفسير التوقيت

يتضمن `mantis-slack-desktop-smoke-report.md` توقيتات المراحل:

  * `crabbox.warmup`: إقلاع مزوّد السحابة، وجاهزية سطح المكتب/المتصفح، وSSH.
  * `crabbox.inspect`: البحث عن بيانات تعريف التأجير.
  * `credentials.prepare`: الحصول على تأجير بيانات اعتماد Convex.
  * `crabbox.remote_run`: المزامنة، وتشغيل المتصفح، وتثبيت/بناء OpenClaw أو التحقق من التهيئة، وبدء Gateway، ولقطة الشاشة، والتقاط الفيديو.
  * `artifacts.copy`: النسخ عبر rsync من الآلة الافتراضية.


يمكن وسم `crabbox.remote_run` بأنه `accepted` عندما يعيد Crabbox حالة بعيدة غير صفرية بعد أن ينسخ Mantis بيانات تعريف تثبت أن Gateway الخاص بـ OpenClaw حي وأن الإعداد اكتمل. تعامل مع `accepted` كنجاح مع توضيح، وليس كسيناريو فاشل.

إذا كان التشغيل بطيئًا:

  * يهيمن warmup: اخبز مسبقًا أو رقِّ صورة مزوّد Crabbox أفضل؛
  * يهيمن remote_run في `source`: استخدم تأجيرًا دافئًا، أو حسّن إعادة استخدام مخزن pnpm، أو انقل متطلبات الجهاز المسبقة إلى صورة المزوّد؛
  * يهيمن remote_run في `prehydrated`: لم تكن مساحة العمل البعيدة جاهزة فعليًا، أو أن إعداد Gateway/المتصفح/Slack بطيء؛
  * يهيمن نسخ الآثار: افحص حجم الفيديو ومحتويات مجلد الآثار.


## قائمة تدقيق الأدلة

ينبغي أن يعرض تعليق PR الجيد:

  * معرّف السيناريو وSHA المرشح؛
  * عنوان URL لتشغيل GitHub Actions؛
  * عنوان URL للأثر؛
  * لقطة شاشة مضمنة؛
  * معاينة متحركة مضمنة عند توفرها؛
  * روابط MP4 الكامل وMP4 المقتطع؛
  * حالة النجاح/الفشل؛
  * ملخص التوقيت في التقرير المرفق.


لا تلتزم بلقطات الشاشة أو الفيديوهات داخل المستودع. احتفظ بها في آثار GitHub Actions أو تعليق PR.

## التعامل مع الفشل

إذا فشل سير العمل قبل تشغيل الآلة الافتراضية، فافحص مهمة Actions أولًا. الأسباب المعتادة هي `candidate_ref` غير موثوق، أو أسرار بيئة مفقودة، أو فشل تثبيت/بناء المرشح.

إذا فشل تشغيل الآلة الافتراضية لكن لقطات الشاشة نُسخت عائدةً، فافحص:

bashCopy code
[code]
    cat mantis-slack-desktop-smoke-report.mdcat mantis-slack-desktop-smoke-summary.jsoncat slack-desktop-command.logcat openclaw-gateway.logcat chrome.logcat ffmpeg.log
[/code]

إذا أبقى التشغيل التأجير، فافتح VNC باستخدام أمر `crabbox vnc ...` الموجود في التقرير. أوقف التأجير عند الانتهاء:

bashCopy code
[code]
    crabbox stop --provider aws <cbx_id-or-slug>
[/code]

إذا انتهت صلاحية تسجيل دخول Slack، فأصلحه في VNC على تأجير مُبقى عليه وأعد التشغيل باستخدام `--lease-id`. لا تخبز ملف تعريف المتصفح هذا داخل صورة مزوّد.

## ذات صلة

  * [نظرة عامة على QA](</ar/concepts/qa-e2e-automation>)
  * [قناة Slack](</ar/channels/slack>)
  * [الاختبار](</ar/help/testing>)


Was this useful?YesNo