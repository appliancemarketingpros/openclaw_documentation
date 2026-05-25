---
title: الخطافات
source_url: https://docs.openclaw.ai/ar/cli/hooks
scraped_at: 2026-05-25
---

# `openclaw hooks`

إدارة خطافات الوكيل (أتمتات مدفوعة بالأحداث لأوامر مثل `/new` و`/reset` وبدء تشغيل Gateway).

تشغيل `openclaw hooks` بلا أمر فرعي يعادل `openclaw hooks list`.

ذات صلة:

  * الخطافات: [الخطافات](</ar/automation/hooks>)
  * خطافات Plugin: [خطافات Plugin](</ar/plugins/hooks>)


## سرد كل الخطافات

bashCopy code
[code]
    openclaw hooks list
[/code]

يسرد كل الخطافات المكتشفة من أدلة مساحة العمل، والمدارة، والإضافية، والمضمنة. لا يحمّل بدء تشغيل Gateway معالجات الخطافات الداخلية حتى يتم تكوين خطاف داخلي واحد على الأقل.

**الخيارات:**

  * `--eligible`: إظهار الخطافات المؤهلة فقط (المتطلبات مستوفاة)
  * `--json`: الإخراج بصيغة JSON
  * `-v, --verbose`: إظهار معلومات تفصيلية تشمل المتطلبات المفقودة


**مثال على الإخراج:**

CodeCopy code
[code]
    Hooks (4/4 ready) Ready:  🚀 boot-md ✓ - Run BOOT.md on gateway startup  📎 bootstrap-extra-files ✓ - Inject extra workspace bootstrap files during agent bootstrap  📝 command-logger ✓ - Log all command events to a centralized audit file  💾 session-memory ✓ - Save session context to memory when /new or /reset command is issued
[/code]

**مثال (تفصيلي):**

bashCopy code
[code]
    openclaw hooks list --verbose
[/code]

يعرض المتطلبات المفقودة للخطافات غير المؤهلة.

**مثال (JSON):**

bashCopy code
[code]
    openclaw hooks list --json
[/code]

يعيد JSON منظماً للاستخدام البرمجي.

## الحصول على معلومات الخطاف

bashCopy code
[code]
    openclaw hooks info <name>
[/code]

يعرض معلومات تفصيلية عن خطاف محدد.

**الوسائط:**

  * `<name>`: اسم الخطاف أو مفتاح الخطاف (مثل `session-memory`)


**الخيارات:**

  * `--json`: الإخراج بصيغة JSON


**مثال:**

bashCopy code
[code]
    openclaw hooks info session-memory
[/code]

**الإخراج:**

CodeCopy code
[code]
    💾 session-memory ✓ Ready Save session context to memory when /new or /reset command is issued Details:  Source: openclaw-bundled  Path: /path/to/openclaw/hooks/bundled/session-memory/HOOK.md  Handler: /path/to/openclaw/hooks/bundled/session-memory/handler.ts  Homepage: https://docs.openclaw.ai/automation/hooks#session-memory  Events: command:new, command:reset Requirements:  Config: ✓ workspace.dir
[/code]

## التحقق من أهلية الخطافات

bashCopy code
[code]
    openclaw hooks check
[/code]

يعرض ملخصاً لحالة أهلية الخطافات (كم عدد الجاهزة مقابل غير الجاهزة).

**الخيارات:**

  * `--json`: الإخراج بصيغة JSON


**مثال على الإخراج:**

CodeCopy code
[code]
    Hooks Status Total hooks: 4Ready: 4Not ready: 0
[/code]

## تمكين خطاف

bashCopy code
[code]
    openclaw hooks enable <name>
[/code]

يمكّن خطافاً محدداً عبر إضافته إلى تكوينك (`~/.openclaw/openclaw.json` افتراضياً).

**ملاحظة:** خطافات مساحة العمل معطلة افتراضياً حتى يتم تمكينها هنا أو في التكوين. الخطافات المُدارة بواسطة Plugin تعرض `plugin:<id>` في `openclaw hooks list` ولا يمكن تمكينها/تعطيلها هنا. مكّن/عطّل Plugin بدلاً من ذلك.

**الوسائط:**

  * `<name>`: اسم الخطاف (مثل `session-memory`)


**مثال:**

bashCopy code
[code]
    openclaw hooks enable session-memory
[/code]

**الإخراج:**

CodeCopy code
[code]
    ✓ Enabled hook: 💾 session-memory
[/code]

**ما الذي يفعله:**

  * يتحقق مما إذا كان الخطاف موجوداً ومؤهلاً
  * يحدّث `hooks.internal.entries.<name>.enabled = true` في تكوينك
  * يحفظ التكوين إلى القرص


إذا كان الخطاف قادماً من `<workspace>/hooks/`، فهذه الخطوة الاختيارية مطلوبة قبل أن يحمّله Gateway.

**بعد التمكين:**

  * أعد تشغيل Gateway حتى تُعاد تحميل الخطافات (إعادة تشغيل تطبيق شريط القوائم على macOS، أو إعادة تشغيل عملية Gateway في التطوير).


## تعطيل خطاف

bashCopy code
[code]
    openclaw hooks disable <name>
[/code]

يعطّل خطافاً محدداً عبر تحديث تكوينك.

**الوسائط:**

  * `<name>`: اسم الخطاف (مثل `command-logger`)


**مثال:**

bashCopy code
[code]
    openclaw hooks disable command-logger
[/code]

**الإخراج:**

CodeCopy code
[code]
    ⏸ Disabled hook: 📝 command-logger
[/code]

**بعد التعطيل:**

  * أعد تشغيل Gateway حتى تُعاد تحميل الخطافات


## ملاحظات

  * تكتب `openclaw hooks list --json` و`info --json` و`check --json` بيانات JSON منظّمة مباشرة إلى stdout.
  * لا يمكن تمكين أو تعطيل الخطافات المُدارة بواسطة Plugin هنا؛ مكّن أو عطّل Plugin المالك بدلاً من ذلك.


## تثبيت حزم الخطافات

bashCopy code
[code]
    openclaw plugins install <package>        # npm by defaultopenclaw plugins install npm:<package>    # npm onlyopenclaw plugins install <package> --pin  # pin versionopenclaw plugins install <path>           # local path
[/code]

ثبّت حزم الخطافات عبر مثبّت plugins الموحد.

لا يزال `openclaw hooks install` يعمل كاسم بديل للتوافق، لكنه يطبع تحذير إهمال ويمرر إلى `openclaw plugins install`.

مواصفات npm **خاصة بالسجل فقط** (اسم الحزمة + **إصدار دقيق** اختياري أو **dist-tag**). تُرفض مواصفات Git/URL/file ونطاقات semver. تعمل عمليات تثبيت الاعتماديات محلياً ضمن المشروع مع `--ignore-scripts` للأمان، حتى عندما تحتوي الصدفة لديك على إعدادات تثبيت npm عمومية.

تبقى المواصفات المجردة و`@latest` على مسار stable. إذا حل npm أياً من هذين إلى إصدار تمهيدي، يتوقف OpenClaw ويطلب منك الاشتراك صراحة باستخدام وسم إصدار تمهيدي مثل `@beta`/`@rc` أو إصدار تمهيدي دقيق.

**ما الذي يفعله:**

  * ينسخ حزمة الخطافات إلى `~/.openclaw/hooks/<id>`
  * يمكّن الخطافات المثبتة في `hooks.internal.entries.*`
  * يسجل التثبيت ضمن `hooks.internal.installs`


**الخيارات:**

  * `-l, --link`: ربط دليل محلي بدلاً من نسخه (يضيفه إلى `hooks.internal.load.extraDirs`)
  * `--pin`: تسجيل تثبيتات npm بصيغة `name@version` المحلولة بدقة في `hooks.internal.installs`


**الأرشيفات المدعومة:** `.zip` و`.tgz` و`.tar.gz` و`.tar`

**أمثلة:**

bashCopy code
[code]
    # Local directoryopenclaw plugins install ./my-hook-pack # Local archiveopenclaw plugins install ./my-hook-pack.zip # NPM packageopenclaw plugins install @openclaw/my-hook-pack # Link a local directory without copyingopenclaw plugins install -l ./my-hook-pack
[/code]

تُعامل حزم الخطافات المرتبطة كخطافات مُدارة من دليل مكوّن بواسطة المشغّل، وليس كخطافات مساحة عمل.

## تحديث حزم الخطافات

bashCopy code
[code]
    openclaw plugins update <id>openclaw plugins update --all
[/code]

حدّث حزم الخطافات المستندة إلى npm والمتتبعة عبر محدّث plugins الموحد.

لا يزال `openclaw hooks update` يعمل كاسم بديل للتوافق، لكنه يطبع تحذير إهمال ويمرر إلى `openclaw plugins update`.

**الخيارات:**

  * `--all`: تحديث كل حزم الخطافات المتتبعة
  * `--dry-run`: إظهار ما سيتغير دون كتابة


عندما توجد تجزئة سلامة مخزنة وتتغير تجزئة الأثر الذي تم جلبه، يطبع OpenClaw تحذيراً ويطلب التأكيد قبل المتابعة. استخدم `--yes` العام لتجاوز المطالبات في CI/التشغيل غير التفاعلي.

## الخطافات المضمنة

### session-memory

يحفظ سياق الجلسة في الذاكرة عند إصدار `/new` أو `/reset`.

**التمكين:**

bashCopy code
[code]
    openclaw hooks enable session-memory
[/code]

**الإخراج:** `~/.openclaw/workspace/memory/YYYY-MM-DD-HHMM.md` افتراضياً. عيّن `hooks.internal.entries.session-memory.llmSlug: true` لاستخدام شرائح أسماء ملفات مولدة بواسطة النموذج.

**انظر:** [توثيق session-memory](</ar/automation/hooks#session-memory>)

### bootstrap-extra-files

يحقن ملفات bootstrap إضافية (على سبيل المثال `AGENTS.md` / `TOOLS.md` المحلية لمستودع monorepo) أثناء `agent:bootstrap`.

**التمكين:**

bashCopy code
[code]
    openclaw hooks enable bootstrap-extra-files
[/code]

**انظر:** [توثيق bootstrap-extra-files](</ar/automation/hooks#bootstrap-extra-files>)

### command-logger

يسجل كل أحداث الأوامر في ملف تدقيق مركزي.

**التمكين:**

bashCopy code
[code]
    openclaw hooks enable command-logger
[/code]

**الإخراج:** `~/.openclaw/logs/commands.log`

**عرض السجلات:**

bashCopy code
[code]
    # Recent commandstail -n 20 ~/.openclaw/logs/commands.log # Pretty-printcat ~/.openclaw/logs/commands.log | jq . # Filter by actiongrep '"action":"new"' ~/.openclaw/logs/commands.log | jq .
[/code]

**انظر:** [توثيق command-logger](</ar/automation/hooks#command-logger>)

### boot-md

يشغّل `BOOT.md` عند بدء Gateway (بعد بدء القنوات).

**الأحداث** : `gateway:startup`

**التمكين** :

bashCopy code
[code]
    openclaw hooks enable boot-md
[/code]

**انظر:** [توثيق boot-md](</ar/automation/hooks#boot-md>)

## ذات صلة

  * [مرجع CLI](</ar/cli>)
  * [خطافات الأتمتة](</ar/automation/hooks>)


Was this useful?YesNo