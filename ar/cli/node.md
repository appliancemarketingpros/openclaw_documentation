---
title: Node
source_url: https://docs.openclaw.ai/ar/cli/node
scraped_at: 2026-05-25
---

# `openclaw node`

شغّل **مضيف Node بلا واجهة رسومية** يتصل بـ WebSocket الخاص بـ Gateway ويعرض `system.run` / `system.which` على هذا الجهاز.

## لماذا تستخدم مضيف Node؟

استخدم مضيف Node عندما تريد من الوكلاء **تشغيل أوامر على أجهزة أخرى** في شبكتك من دون تثبيت تطبيق macOS مرافق كامل هناك.

حالات الاستخدام الشائعة:

  * تشغيل الأوامر على أجهزة Linux/Windows بعيدة (خوادم البناء، أجهزة المختبر، NAS).
  * إبقاء التنفيذ **داخل sandbox** على Gateway، مع تفويض التشغيلات المعتمدة إلى مضيفين آخرين.
  * توفير هدف تنفيذ خفيف وبلا واجهة رسومية للأتمتة أو عُقد CI.


يبقى التنفيذ محميًا بواسطة **موافقات التنفيذ** وقوائم السماح لكل وكيل على مضيف Node، بحيث يمكنك إبقاء الوصول إلى الأوامر محدودًا وصريحًا.

## وكيل المتصفح (بلا إعداد)

تعلن مضيفات Node تلقائيًا عن وكيل متصفح إذا لم يكن `browser.enabled` معطّلًا على Node. يتيح ذلك للوكيل استخدام أتمتة المتصفح على تلك Node من دون إعداد إضافي.

افتراضيًا، يعرض الوكيل سطح ملف تعريف المتصفح العادي في Node. إذا ضبطت `nodeHost.browserProxy.allowProfiles`، يصبح الوكيل تقييديًا: يُرفض استهداف ملفات التعريف غير الموجودة في قائمة السماح، وتُحظر مسارات إنشاء/حذف ملفات التعريف الدائمة عبر الوكيل.

عطّله على Node عند الحاجة:

json5Copy code
[code]
    {  nodeHost: {    browserProxy: {      enabled: false,    },  },}
[/code]

## التشغيل (في المقدمة)

bashCopy code
[code]
    openclaw node run --host <gateway-host> --port 18789
[/code]

الخيارات:

  * `--host <host>`: مضيف WebSocket الخاص بـ Gateway (الافتراضي: `127.0.0.1`)
  * `--port <port>`: منفذ WebSocket الخاص بـ Gateway (الافتراضي: `18789`)
  * `--tls`: استخدام TLS لاتصال Gateway
  * `--tls-fingerprint <sha256>`: بصمة شهادة TLS المتوقعة (sha256)
  * `--node-id <id>`: تجاوز معرّف Node (يمسح رمز الاقتران)
  * `--display-name <name>`: تجاوز اسم عرض Node


## مصادقة Gateway لمضيف Node

يستنتج `openclaw node run` و`openclaw node install` مصادقة Gateway من الإعدادات/البيئة (لا توجد أعلام `--token`/`--password` في أوامر Node):

  * يتم فحص `OPENCLAW_GATEWAY_TOKEN` / `OPENCLAW_GATEWAY_PASSWORD` أولًا.
  * ثم الرجوع إلى الإعداد المحلي: `gateway.auth.token` / `gateway.auth.password`.
  * في الوضع المحلي، لا يرث مضيف Node عمدًا `gateway.remote.token` / `gateway.remote.password`.
  * إذا تم تكوين `gateway.auth.token` / `gateway.auth.password` صراحةً عبر SecretRef ولم يُحل، يفشل حل مصادقة Node بشكل مغلق (من دون رجوع بعيد يخفي ذلك).
  * في `gateway.mode=remote`، تصبح حقول العميل البعيد (`gateway.remote.token` / `gateway.remote.password`) مؤهلة أيضًا وفق قواعد أولوية البعيد.
  * لا يراعي حل مصادقة مضيف Node إلا متغيرات البيئة `OPENCLAW_GATEWAY_*`.


لـ Node تتصل بـ Gateway غير local loopback عبر `ws://` على شبكة خاصة موثوقة، اضبط `OPENCLAW_ALLOW_INSECURE_PRIVATE_WS=1`. من دونه، يفشل بدء Node بشكل مغلق ويطلب منك استخدام `wss://` أو نفق SSH أو Tailscale. هذا تفعيل اختياري عبر بيئة العملية، وليس مفتاح إعداد `openclaw.json`. يحفظ `openclaw node install` هذا الخيار في خدمة Node المُدارة عندما يكون موجودًا في بيئة أمر التثبيت.

## الخدمة (في الخلفية)

ثبّت مضيف Node بلا واجهة رسومية كخدمة مستخدم.

bashCopy code
[code]
    openclaw node install --host <gateway-host> --port 18789
[/code]

الخيارات:

  * `--host <host>`: مضيف WebSocket الخاص بـ Gateway (الافتراضي: `127.0.0.1`)
  * `--port <port>`: منفذ WebSocket الخاص بـ Gateway (الافتراضي: `18789`)
  * `--tls`: استخدام TLS لاتصال Gateway
  * `--tls-fingerprint <sha256>`: بصمة شهادة TLS المتوقعة (sha256)
  * `--node-id <id>`: تجاوز معرّف Node (يمسح رمز الاقتران)
  * `--display-name <name>`: تجاوز اسم عرض Node
  * `--runtime <runtime>`: وقت تشغيل الخدمة (`node` أو `bun`)
  * `--force`: إعادة التثبيت/الكتابة فوق الموجود إذا كان مثبتًا بالفعل


إدارة الخدمة:

bashCopy code
[code]
    openclaw node statusopenclaw node startopenclaw node stopopenclaw node restartopenclaw node uninstall
[/code]

استخدم `openclaw node run` لمضيف Node يعمل في المقدمة (بلا خدمة).

تقبل أوامر الخدمة `--json` لإخراج قابل للقراءة آليًا.

يعيد مضيف Node محاولة إعادة تشغيل Gateway وإغلاقات الشبكة داخل العملية. إذا أبلغ Gateway عن إيقاف مؤقت نهائي لمصادقة الرمز/كلمة المرور/التمهيد، يسجّل مضيف Node تفاصيل الإغلاق ويخرج برمز غير صفري كي يتمكن launchd/systemd من إعادة تشغيله بإعدادات وبيانات اعتماد حديثة. تبقى حالات الإيقاف المؤقت التي تتطلب الاقتران في مسار المقدمة حتى يمكن اعتماد الطلب المعلّق.

## الاقتران

ينشئ الاتصال الأول طلب اقتران جهاز معلّقًا (`role: node`) على Gateway. اعتمده عبر:

bashCopy code
[code]
    openclaw devices listopenclaw devices approve <requestId>
[/code]

في شبكات Node ذات التحكم الصارم، يمكن لمشغّل Gateway تفعيل اعتماد اقتران Node للمرة الأولى تلقائيًا من CIDR موثوقة بشكل صريح:

json5Copy code
[code]
    {  gateway: {    nodes: {      pairing: {        autoApproveCidrs: ["192.168.1.0/24"],      },    },  },}
[/code]

هذا معطّل افتراضيًا. لا ينطبق إلا على اقتران `role: node` جديد بلا نطاقات مطلوبة. لا يزال عملاء المشغّل/المتصفح، وواجهة Control UI، وWebChat، وترقيات الدور أو النطاق أو البيانات الوصفية أو المفتاح العام تتطلب اعتمادًا يدويًا.

إذا أعادت Node محاولة الاقتران مع تفاصيل مصادقة متغيرة (الدور/النطاقات/المفتاح العام)، يُستبدل الطلب المعلّق السابق ويُنشأ `requestId` جديد. شغّل `openclaw devices list` مرة أخرى قبل الاعتماد.

يخزن مضيف Node معرّف Node والرمز واسم العرض ومعلومات اتصال Gateway في `~/.openclaw/node.json`.

## موافقات التنفيذ

يخضع `system.run` لموافقات التنفيذ المحلية:

  * `~/.openclaw/exec-approvals.json`
  * [موافقات التنفيذ](</ar/tools/exec-approvals>)
  * `openclaw approvals --node <id|name|ip>` (تحرير من Gateway)


بالنسبة إلى تنفيذ Node غير المتزامن المعتمد، يُحضّر OpenClaw خطة `systemRunPlan` قياسية قبل عرض طلب الموافقة. ويعيد تمرير `system.run` المعتمد لاحقًا استخدام تلك الخطة المخزّنة، لذلك تُرفض التعديلات على حقول الأمر/cwd/الجلسة بعد إنشاء طلب الموافقة بدلًا من تغيير ما تنفذه Node.

## ذو صلة

  * [مرجع CLI](</ar/cli>)
  * [Nodes](</ar/nodes>)


Was this useful?YesNo