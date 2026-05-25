---
title: الموافقات
source_url: https://docs.openclaw.ai/ar/cli/approvals
scraped_at: 2026-05-25
---

# `openclaw approvals`

إدارة موافقات exec الخاصة بـ **المضيف المحلي** أو **مضيف Gateway** أو **مضيف Node**. افتراضيًا، تستهدف الأوامر ملف الموافقات المحلي على القرص. استخدم `--gateway` للاستهداف على Gateway، أو `--node` لاستهداف Node معيّن.

الاسم البديل: `openclaw exec-approvals`

ذو صلة:

  * موافقات exec: [موافقات exec](</ar/tools/exec-approvals>)
  * Nodes: [Nodes](</ar/nodes>)


## `openclaw exec-policy`

`openclaw exec-policy` هو أمر الراحة المحلي للحفاظ على توافق تهيئة `tools.exec.*` المطلوبة وملف الموافقات الخاص بالمضيف المحلي في خطوة واحدة.

استخدمه عندما تريد:

  * فحص السياسة المحلية المطلوبة، وملف موافقات المضيف، والدمج الفعّال
  * تطبيق إعداد محلي مسبق مثل YOLO أو deny-all
  * مزامنة `tools.exec.*` المحلي و`~/.openclaw/exec-approvals.json` المحلي


أمثلة:

bashCopy code
[code]
    openclaw exec-policy showopenclaw exec-policy show --json openclaw exec-policy preset yoloopenclaw exec-policy preset cautious --json openclaw exec-policy set --host gateway --security full --ask off --ask-fallback full
[/code]

أوضاع الإخراج:

  * بدون `--json`: يطبع عرض الجدول المقروء للبشر
  * مع `--json`: يطبع إخراجًا منظمًا قابلًا للقراءة الآلية


النطاق الحالي:

  * `exec-policy` **محلي فقط**
  * يحدّث ملف التهيئة المحلي وملف الموافقات المحلي معًا
  * لا يدفع السياسة إلى مضيف Gateway أو مضيف Node
  * يتم رفض `--host node` في هذا الأمر لأن موافقات exec الخاصة بـ Node تُجلَب من Node وقت التشغيل ويجب إدارتها عبر أوامر الموافقات الموجهة إلى Node بدلًا من ذلك
  * يعلّم `openclaw exec-policy show` نطاقات `host=node` على أنها مُدارة من Node وقت التشغيل بدلًا من اشتقاق سياسة فعّالة من ملف الموافقات المحلي


إذا كنت بحاجة إلى تعديل موافقات مضيفات بعيدة مباشرةً، فاستمر في استخدام `openclaw approvals set --gateway` أو `openclaw approvals set --node <id|name|ip>`.

## أوامر شائعة

bashCopy code
[code]
    openclaw approvals getopenclaw approvals get --node <id|name|ip>openclaw approvals get --gateway
[/code]

يعرض `openclaw approvals get` الآن سياسة exec الفعّالة للأهداف المحلية وأهداف Gateway وNode:

  * سياسة `tools.exec` المطلوبة
  * سياسة ملف موافقات المضيف
  * النتيجة الفعّالة بعد تطبيق قواعد الأسبقية


الأسبقية مقصودة:

  * ملف موافقات المضيف هو مصدر الحقيقة القابل للإنفاذ
  * يمكن لسياسة `tools.exec` المطلوبة أن تضيق النية أو توسعها، لكن النتيجة الفعّالة تظل مشتقة من قواعد المضيف
  * يجمع `--node` بين ملف موافقات مضيف Node وسياسة `tools.exec` الخاصة بـ Gateway، لأن كلاهما لا يزال يُطبَّق وقت التشغيل
  * إذا لم تكن تهيئة Gateway متاحة، يعود CLI إلى لقطة موافقات Node ويشير إلى أنه لم يمكن حساب سياسة وقت التشغيل النهائية


## استبدال الموافقات من ملف

bashCopy code
[code]
    openclaw approvals set --file ./exec-approvals.jsonopenclaw approvals set --stdin <<'EOF'{ version: 1, defaults: { security: "full", ask: "off" } }EOFopenclaw approvals set --node <id|name|ip> --file ./exec-approvals.jsonopenclaw approvals set --gateway --file ./exec-approvals.json
[/code]

يقبل `set` تنسيق JSON5، وليس JSON الصارم فقط. استخدم إما `--file` أو `--stdin`، وليس كليهما.

## مثال "عدم السؤال مطلقًا" / YOLO

بالنسبة إلى مضيف يجب ألا يتوقف أبدًا عند موافقات exec، اضبط القيم الافتراضية لموافقات المضيف إلى `full` \+ `off`:

bashCopy code
[code]
    openclaw approvals set --stdin <<'EOF'{  version: 1,  defaults: {    security: "full",    ask: "off",    askFallback: "full"  }}EOF
[/code]

صيغة Node:

bashCopy code
[code]
    openclaw approvals set --node <id|name|ip> --stdin <<'EOF'{  version: 1,  defaults: {    security: "full",    ask: "off",    askFallback: "full"  }}EOF
[/code]

يغيّر هذا **ملف موافقات المضيف** فقط. ولإبقاء سياسة OpenClaw المطلوبة متوافقة، اضبط أيضًا:

bashCopy code
[code]
    openclaw config set tools.exec.host gatewayopenclaw config set tools.exec.security fullopenclaw config set tools.exec.ask off
[/code]

لماذا `tools.exec.host=gateway` في هذا المثال:

  * ما زال `host=auto` يعني "sandbox عند توفره، وإلا فـ Gateway".
  * يتعلق YOLO بالموافقات، وليس بالتوجيه.
  * إذا كنت تريد exec على المضيف حتى عند تهيئة sandbox، فاجعل اختيار المضيف صريحًا باستخدام `gateway` أو `/exec host=gateway`.


وهذا يطابق سلوك YOLO الحالي الافتراضي للمضيف. شدّده إذا كنت تريد موافقات.

اختصار محلي:

bashCopy code
[code]
    openclaw exec-policy preset yolo
[/code]

يحدّث هذا الاختصار المحلي كلًا من تهيئة `tools.exec.*` المحلية المطلوبة والقيم الافتراضية للموافقات المحلية معًا. وهو مكافئ من حيث النية للإعداد اليدوي ذي الخطوتين أعلاه، لكنه مخصص للجهاز المحلي فقط.

## مساعدات قائمة السماح

bashCopy code
[code]
    openclaw approvals allowlist add "~/Projects/**/bin/rg"openclaw approvals allowlist add --agent main --node <id|name|ip> "/usr/bin/uptime"openclaw approvals allowlist add --agent "*" "/usr/bin/uname" openclaw approvals allowlist remove "~/Projects/**/bin/rg"
[/code]

## خيارات شائعة

تدعم الأوامر `get` و`set` و`allowlist add|remove` جميعها:

  * `--node <id|name|ip>`
  * `--gateway`
  * خيارات RPC المشتركة الخاصة بـ Node: `--url`, `--token`, `--timeout`, `--json`


ملاحظات الاستهداف:

  * عدم استخدام أي علامات استهداف يعني ملف الموافقات المحلي على القرص
  * يستهدف `--gateway` ملف موافقات مضيف Gateway
  * يستهدف `--node` مضيف Node واحدًا بعد resolve المعرّف أو الاسم أو IP أو بادئة المعرّف


كما يدعم `allowlist add|remove` أيضًا:

  * `--agent <id>` (الافتراضي `*`)


## ملاحظات

  * يستخدم `--node` نفس المحلِّل الذي يستخدمه `openclaw nodes` ‏(المعرّف أو الاسم أو ip أو بادئة المعرّف).
  * القيمة الافتراضية لـ `--agent` هي `"*"`, وهذا ينطبق على جميع الوكلاء.
  * يجب أن يعلن مضيف Node عن `system.execApprovals.get/set` ‏(تطبيق macOS أو مضيف Node دون واجهة).
  * تُخزَّن ملفات الموافقات لكل مضيف في `~/.openclaw/exec-approvals.json`.


## ذو صلة

  * [مرجع CLI](</ar/cli>)
  * [موافقات exec](</ar/tools/exec-approvals>)


Was this useful?YesNo