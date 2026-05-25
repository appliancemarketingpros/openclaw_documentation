---
title: CLI لبيئة العزل
source_url: https://docs.openclaw.ai/ar/cli/sandbox
scraped_at: 2026-05-25
---

إدارة أوقات تشغيل صندوق الرمل لتنفيذ الوكيل المعزول.

## نظرة عامة

يمكن لـ OpenClaw تشغيل الوكلاء في أوقات تشغيل صندوق رمل معزولة للأمان. تساعدك أوامر `sandbox` على فحص أوقات التشغيل هذه وإعادة إنشائها بعد التحديثات أو تغييرات التكوين.

يعني ذلك اليوم عادة:

  * حاويات صندوق رمل Docker
  * أوقات تشغيل صندوق رمل SSH عندما يكون `agents.defaults.sandbox.backend = "ssh"`
  * أوقات تشغيل صندوق رمل OpenShell عندما يكون `agents.defaults.sandbox.backend = "openshell"`


بالنسبة إلى `ssh` وOpenShell `remote`، تكون إعادة الإنشاء أهم مما هي عليه مع Docker:

  * مساحة العمل البعيدة تكون المصدر المعتمد بعد التهيئة الأولية
  * يحذف `openclaw sandbox recreate` مساحة العمل البعيدة المعتمدة هذه للنطاق المحدد
  * يؤدي الاستخدام التالي إلى تهيئتها مرة أخرى من مساحة العمل المحلية الحالية


## الأوامر

### `openclaw sandbox explain`

افحص وضع/نطاق/وصول مساحة عمل صندوق الرمل **الفعلي** ، وسياسة أدوات صندوق الرمل، وبوابات الرفع (مع مسارات مفاتيح التكوين للإصلاح).

bashCopy code
[code]
    openclaw sandbox explainopenclaw sandbox explain --session agent:main:mainopenclaw sandbox explain --agent workopenclaw sandbox explain --json
[/code]

### `openclaw sandbox list`

اسرد جميع أوقات تشغيل صندوق الرمل مع حالتها وتكوينها.

bashCopy code
[code]
    openclaw sandbox listopenclaw sandbox list --browser  # List only browser containersopenclaw sandbox list --json     # JSON output
[/code]

**يتضمن الإخراج:**

  * اسم وقت التشغيل وحالته
  * الخلفية (`docker`، `openshell`، إلخ.)
  * تسمية التكوين وما إذا كانت تطابق التكوين الحالي
  * العمر (الوقت منذ الإنشاء)
  * وقت الخمول (الوقت منذ آخر استخدام)
  * الجلسة/الوكيل المرتبط


### `openclaw sandbox recreate`

أزِل أوقات تشغيل صندوق الرمل لفرض إعادة إنشائها بالتكوين المحدث.

bashCopy code
[code]
    openclaw sandbox recreate --all                # Recreate all containersopenclaw sandbox recreate --session main       # Specific sessionopenclaw sandbox recreate --agent mybot        # Specific agentopenclaw sandbox recreate --browser            # Only browser containersopenclaw sandbox recreate --all --force        # Skip confirmation
[/code]

**الخيارات:**

  * `--all`: إعادة إنشاء جميع حاويات صندوق الرمل
  * `--session <key>`: إعادة إنشاء الحاوية لجلسة محددة
  * `--agent <id>`: إعادة إنشاء الحاويات لوكيل محدد
  * `--browser`: إعادة إنشاء حاويات المتصفح فقط
  * `--force`: تخطي مطالبة التأكيد


## حالات الاستخدام

### بعد تحديث صورة Docker

bashCopy code
[code]
    # Pull new imagedocker pull openclaw-sandbox:latestdocker tag openclaw-sandbox:latest openclaw-sandbox:bookworm-slim # Update config to use new image# Edit config: agents.defaults.sandbox.docker.image (or agents.list[].sandbox.docker.image) # Recreate containersopenclaw sandbox recreate --all
[/code]

### بعد تغيير تكوين صندوق الرمل

bashCopy code
[code]
    # Edit config: agents.defaults.sandbox.* (or agents.list[].sandbox.*) # Recreate to apply new configopenclaw sandbox recreate --all
[/code]

### بعد تغيير هدف SSH أو مواد مصادقة SSH

bashCopy code
[code]
    # Edit config:# - agents.defaults.sandbox.backend# - agents.defaults.sandbox.ssh.target# - agents.defaults.sandbox.ssh.workspaceRoot# - agents.defaults.sandbox.ssh.identityFile / certificateFile / knownHostsFile# - agents.defaults.sandbox.ssh.identityData / certificateData / knownHostsData openclaw sandbox recreate --all
[/code]

بالنسبة إلى خلفية `ssh` الأساسية، تحذف إعادة الإنشاء جذر مساحة العمل البعيدة لكل نطاق على هدف SSH. يعيد التشغيل التالي تهيئتها من مساحة العمل المحلية.

### بعد تغيير مصدر OpenShell أو سياسته أو وضعه

bashCopy code
[code]
    # Edit config:# - agents.defaults.sandbox.backend# - plugins.entries.openshell.config.from# - plugins.entries.openshell.config.mode# - plugins.entries.openshell.config.policy openclaw sandbox recreate --all
[/code]

بالنسبة إلى وضع OpenShell `remote`، تحذف إعادة الإنشاء مساحة العمل البعيدة المعتمدة لذلك النطاق. يعيد التشغيل التالي تهيئتها من مساحة العمل المحلية.

### بعد تغيير setupCommand

bashCopy code
[code]
    openclaw sandbox recreate --all# or just one agent:openclaw sandbox recreate --agent family
[/code]

### لوكيل محدد فقط

bashCopy code
[code]
    # Update only one agent's containersopenclaw sandbox recreate --agent alfred
[/code]

## سبب الحاجة إلى ذلك

عند تحديث تكوين صندوق الرمل:

  * تستمر أوقات التشغيل الموجودة في العمل بالإعدادات القديمة.
  * لا تُزال أوقات التشغيل إلا بعد 24 ساعة من عدم النشاط.
  * الوكلاء المستخدمون بانتظام يُبقون أوقات التشغيل القديمة نشطة إلى أجل غير مسمى.


استخدم `openclaw sandbox recreate` لفرض إزالة أوقات التشغيل القديمة. تُعاد إنشاؤها تلقائيًا بالإعدادات الحالية عند الحاجة إليها لاحقًا.

## ترحيل السجل

يخزن OpenClaw بيانات تعريف وقت تشغيل صندوق الرمل كجزء JSON واحد لكل إدخال حاوية/متصفح ضمن دليل حالة صندوق الرمل. قد تظل التثبيتات الأقدم تحتوي على ملفات قديمة موحدة:

  * `~/.openclaw/sandbox/containers.json`
  * `~/.openclaw/sandbox/browsers.json`


لا تعيد قراءات وقت تشغيل صندوق الرمل العادية كتابة هذه الملفات. شغّل `openclaw doctor --fix` لترحيل الإدخالات القديمة الصالحة إلى دلائل السجل المجزأ. تُعزل الملفات القديمة غير الصالحة حتى لا يتمكن سجل قديم تالف واحد من إخفاء إدخالات وقت التشغيل الحالية.

## التكوين

توجد إعدادات صندوق الرمل في `~/.openclaw/openclaw.json` ضمن `agents.defaults.sandbox` (توضع التجاوزات لكل وكيل في `agents.list[].sandbox`):

jsoncCopy code
[code]
    {  "agents": {    "defaults": {      "sandbox": {        "mode": "all", // off, non-main, all        "backend": "docker", // docker, ssh, openshell        "scope": "agent", // session, agent, shared        "docker": {          "image": "openclaw-sandbox:bookworm-slim",          "containerPrefix": "openclaw-sbx-",          // ... more Docker options        },        "prune": {          "idleHours": 24, // Auto-prune after 24h idle          "maxAgeDays": 7, // Auto-prune after 7 days        },      },    },  },}
[/code]

## ذات صلة

  * [مرجع CLI](</ar/cli>)
  * [استخدام صندوق الرمل](</ar/gateway/sandboxing>)
  * [مساحة عمل الوكيل](</ar/concepts/agent-workspace>)
  * [Doctor](</ar/gateway/doctor>): يفحص إعداد صندوق الرمل.


Was this useful?YesNo