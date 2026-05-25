---
title: استكشاف أخطاء Node وإصلاحها
source_url: https://docs.openclaw.ai/ar/nodes/troubleshooting
scraped_at: 2026-05-25
---

استخدم هذه الصفحة عندما تكون العقدة ظاهرة في الحالة لكن أدوات العقدة تفشل.

## تسلسل الأوامر

bashCopy code
[code]
    openclaw statusopenclaw gateway statusopenclaw logs --followopenclaw doctoropenclaw channels status --probe
[/code]

ثم شغّل فحوصات خاصة بالعقدة:

bashCopy code
[code]
    openclaw nodes statusopenclaw nodes describe --node <idOrNameOrIp>openclaw approvals get --node <idOrNameOrIp>
[/code]

إشارات السلامة:

  * العقدة متصلة ومقترنة للدور `node`.
  * يتضمن `nodes describe` الإمكانية التي تستدعيها.
  * تُظهر موافقات التنفيذ الوضع/قائمة السماح المتوقعة.


## متطلبات الواجهة الأمامية

`canvas.*` و`camera.*` و`screen.*` تعمل في الواجهة الأمامية فقط على عقد iOS/Android.

فحص وإصلاح سريعان:

bashCopy code
[code]
    openclaw nodes describe --node <idOrNameOrIp>openclaw nodes canvas snapshot --node <idOrNameOrIp>openclaw logs --follow
[/code]

إذا رأيت `NODE_BACKGROUND_UNAVAILABLE`، انقل تطبيق العقدة إلى الواجهة الأمامية وأعد المحاولة.

## مصفوفة الأذونات

الإمكانية | iOS | Android | تطبيق العقدة على macOS | رمز الفشل المعتاد  
---|---|---|---|---  
`camera.snap`, `camera.clip` | الكاميرا (+ الميكروفون لصوت المقطع) | الكاميرا (+ الميكروفون لصوت المقطع) | الكاميرا (+ الميكروفون لصوت المقطع) | `*_PERMISSION_REQUIRED`  
`screen.record` | تسجيل الشاشة (+ الميكروفون اختياري) | مطالبة التقاط الشاشة (+ الميكروفون اختياري) | تسجيل الشاشة | `*_PERMISSION_REQUIRED`  
`location.get` | أثناء الاستخدام أو دائمًا (يعتمد على الوضع) | موقع الواجهة الأمامية/الخلفية حسب الوضع | إذن الموقع | `LOCATION_PERMISSION_REQUIRED`  
`system.run` | غير منطبق (مسار مضيف العقدة) | غير منطبق (مسار مضيف العقدة) | موافقات التنفيذ مطلوبة | `SYSTEM_RUN_DENIED`  
  
## الاقتران مقابل الموافقات

هذه بوابات مختلفة:

  1. **اقتران الجهاز** : هل يمكن لهذه العقدة الاتصال بـ Gateway؟
  2. **سياسة أوامر عقدة Gateway** : هل معرّف أمر RPC مسموح به عبر `gateway.nodes.allowCommands` / `denyCommands` وافتراضيات المنصة؟
  3. **موافقات التنفيذ** : هل يمكن لهذه العقدة تشغيل أمر shell محدد محليًا؟


فحوصات سريعة:

bashCopy code
[code]
    openclaw devices listopenclaw nodes statusopenclaw approvals get --node <idOrNameOrIp>openclaw approvals allowlist add --node <idOrNameOrIp> "/usr/bin/uname"
[/code]

إذا كان الاقتران مفقودًا، فوافق على جهاز العقدة أولًا. إذا كان `nodes describe` يفتقد أمرًا، فتحقق من سياسة أوامر عقدة Gateway وما إذا كانت العقدة قد أعلنت هذا الأمر فعليًا عند الاتصال. إذا كان الاقتران سليمًا لكن `system.run` يفشل، فأصلح موافقات التنفيذ/قائمة السماح على تلك العقدة.

اقتران العقدة هو بوابة هوية/ثقة، وليس سطح موافقة لكل أمر. بالنسبة إلى `system.run`، تعيش سياسة كل عقدة في ملف موافقات التنفيذ الخاص بتلك العقدة (`openclaw approvals get --node ...`)، وليس في سجل اقتران Gateway.

بالنسبة إلى عمليات تشغيل `host=node` المدعومة بالموافقة، يربط Gateway أيضًا التنفيذ بـ `systemRunPlan` القانوني المُحضّر. إذا عدّل مستدعٍ لاحق الأمر/cwd أو بيانات الجلسة الوصفية قبل تمرير التشغيل الموافق عليه، يرفض Gateway التشغيل باعتباره عدم تطابق في الموافقة بدلًا من الوثوق بالحمولة المعدّلة.

## رموز أخطاء العقد الشائعة

  * `NODE_BACKGROUND_UNAVAILABLE` → التطبيق في الخلفية؛ انقله إلى الواجهة الأمامية.
  * `CAMERA_DISABLED` → مفتاح تبديل الكاميرا معطّل في إعدادات العقدة.
  * `*_PERMISSION_REQUIRED` → إذن نظام التشغيل مفقود/مرفوض.
  * `LOCATION_DISABLED` → وضع الموقع متوقف.
  * `LOCATION_PERMISSION_REQUIRED` → وضع الموقع المطلوب غير ممنوح.
  * `LOCATION_BACKGROUND_UNAVAILABLE` → التطبيق في الخلفية لكن لا يوجد إلا إذن أثناء الاستخدام.
  * `SYSTEM_RUN_DENIED: approval required` → طلب التنفيذ يحتاج إلى موافقة صريحة.
  * `SYSTEM_RUN_DENIED: allowlist miss` → الأمر محظور بسبب وضع قائمة السماح. على مضيفات عقد Windows، تُعامل صيغ مغلّف shell مثل `cmd.exe /c ...` كحالات عدم مطابقة لقائمة السماح في وضع قائمة السماح ما لم تُعتمد عبر تدفق الطلب.


## حلقة الاسترداد السريعة

bashCopy code
[code]
    openclaw nodes statusopenclaw nodes describe --node <idOrNameOrIp>openclaw approvals get --node <idOrNameOrIp>openclaw logs --follow
[/code]

إذا بقيت عالقًا:

  * أعد الموافقة على اقتران الجهاز.
  * أعد فتح تطبيق العقدة (في الواجهة الأمامية).
  * أعد منح أذونات نظام التشغيل.
  * أعد إنشاء/اضبط سياسة موافقة التنفيذ.


## ذات صلة

  * [نظرة عامة على العقد](</ar/nodes>)
  * [عقد الكاميرا](</ar/nodes/camera>)
  * [أمر الموقع](</ar/nodes/location-command>)
  * [موافقات التنفيذ](</ar/tools/exec-approvals>)
  * [اقتران Gateway](</ar/gateway/pairing>)
  * [استكشاف أخطاء Gateway وإصلاحها](</ar/gateway/troubleshooting>)
  * [استكشاف أخطاء القنوات وإصلاحها](</ar/channels/troubleshooting>)


Was this useful?YesNo