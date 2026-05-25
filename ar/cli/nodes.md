---
title: العُقد
source_url: https://docs.openclaw.ai/ar/cli/nodes
scraped_at: 2026-05-25
---

# `openclaw nodes`

إدارة العُقد (الأجهزة) المقترنة واستدعاء قدرات العقدة.

ذات صلة:

  * نظرة عامة على العُقد: [العُقد](</ar/nodes>)
  * الكاميرا: [عُقد الكاميرا](</ar/nodes/camera>)
  * الصور: [عُقد الصور](</ar/nodes/images>)


الخيارات الشائعة:

  * `--url`, `--token`, `--timeout`, `--json`


## الأوامر الشائعة

bashCopy code
[code]
    openclaw nodes listopenclaw nodes list --connectedopenclaw nodes list --last-connected 24hopenclaw nodes pendingopenclaw nodes approve <requestId>openclaw nodes reject <requestId>openclaw nodes remove --node <id|name|ip>openclaw nodes rename --node <id|name|ip> --name <displayName>openclaw nodes statusopenclaw nodes status --connectedopenclaw nodes status --last-connected 24h
[/code]

يطبع `nodes list` جداول الطلبات المعلّقة/المقترنة. تتضمن الصفوف المقترنة عمر أحدث اتصال (آخر اتصال). استخدم `--connected` لعرض العُقد المتصلة حاليًا فقط. استخدم `--last-connected <duration>` من أجل التصفية إلى العُقد التي اتصلت ضمن مدة محددة (مثل `24h`، `7d`). استخدم `nodes remove --node <id|name|ip>` لحذف سجل اقتران عقدة قديم مملوك لـ Gateway.

ملاحظة الموافقة:

  * لا يحتاج `openclaw nodes pending` إلا إلى نطاق الاقتران.
  * يمكن لـ `gateway.nodes.pairing.autoApproveCidrs` تخطي خطوة التعليق فقط لاقتران جهاز `role: node` موثوق به صراحة لأول مرة. يكون متوقفًا افتراضيًا ولا يوافق على الترقيات.
  * يرث `openclaw nodes approve <requestId>` متطلبات نطاق إضافية من الطلب المعلّق: 
    * طلب بلا أمر: الاقتران فقط
    * أوامر عقدة غير تنفيذية: الاقتران + الكتابة
    * `system.run` / `system.run.prepare` / `system.which`: الاقتران + الإدارة


## الاستدعاء

bashCopy code
[code]
    openclaw nodes invoke --node <id|name|ip> --command <command> --params <json>
[/code]

علامات الاستدعاء:

  * `--params <json>`: سلسلة كائن JSON (الافتراضي `{}`).
  * `--invoke-timeout <ms>`: مهلة استدعاء العقدة (الافتراضي `15000`).
  * `--idempotency-key <key>`: مفتاح اختيارى لضمان عدم تكرار التنفيذ.
  * يتم حظر `system.run` و`system.run.prepare` هنا؛ استخدم أداة `exec` مع `host=node` لتنفيذ أوامر الصدفة.


لتنفيذ أوامر الصدفة على عقدة، استخدم أداة `exec` مع `host=node` بدلًا من `openclaw nodes run`. أصبح CLI الخاص بـ `nodes` يركز الآن على القدرات: RPC مباشر عبر `nodes invoke`، إلى جانب الاقتران، والكاميرا، والشاشة، والموقع، وCanvas، والإشعارات. تُنفَّذ أوامر Canvas بواسطة Plugin التجريبي المضمن لـ Canvas؛ ويحافظ النواة على خطاف توافق بحيث تبقى ضمن `openclaw nodes canvas`.

## ذات صلة

  * [مرجع CLI](</ar/cli>)
  * [العُقد](</ar/nodes>)


Was this useful?YesNo