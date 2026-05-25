---
title: الوكيل
source_url: https://docs.openclaw.ai/ar/cli/proxy
scraped_at: 2026-05-25
---

# `openclaw proxy`

تحقق من توجيه الوكيل المُدار من المشغّل، أو شغّل وكيل التصحيح المحلي الصريح وافحص حركة المرور الملتقطة.

استخدم `validate` لإجراء فحص تمهيدي لوكيل توجيه أمامي مُدار من المشغّل قبل تمكين توجيه وكيل OpenClaw. الأوامر الأخرى هي أدوات تصحيح للتحقيق على مستوى النقل: يمكنها بدء وكيل محلي، وتشغيل أمر فرعي مع تمكين الالتقاط، وسرد جلسات الالتقاط، والاستعلام عن أنماط حركة المرور الشائعة، وقراءة الكتل الملتقطة، ومسح بيانات الالتقاط المحلية.

## الأوامر

bashCopy code
[code]
    openclaw proxy start [--host <host>] [--port <port>]openclaw proxy run [--host <host>] [--port <port>] -- <cmd...>openclaw proxy validate [--json] [--proxy-url <url>] [--allowed-url <url>] [--denied-url <url>] [--apns-reachable] [--apns-authority <url>] [--timeout-ms <ms>]openclaw proxy coverageopenclaw proxy sessions [--limit <count>]openclaw proxy query --preset <name> [--session <id>]openclaw proxy blob --id <blobId>openclaw proxy purge
[/code]

## التحقق

يفحص `openclaw proxy validate` عنوان URL الفعّال للوكيل المُدار من المشغّل من `--proxy-url` أو الإعدادات أو `OPENCLAW_PROXY_URL`. يبلّغ عن مشكلة في الإعدادات عندما لا يكون أي وكيل ممكّنًا ومُعدًا؛ استخدم `--proxy-url` لإجراء فحص تمهيدي لمرة واحدة قبل تغيير الإعدادات. افتراضيًا، يتحقق من نجاح وجهة عامة عبر الوكيل ومن أن الوكيل لا يمكنه الوصول إلى مؤشر اختبار loopback مؤقت. الوجهات المرفوضة المخصصة تفشل بشكل مغلق: تفشل استجابات HTTP وإخفاقات النقل الملتبسة ما لم تتمكن من التحقق من إشارة رفض خاصة بالنشر بشكل منفصل. أضف `--apns-reachable` لفتح نفق APNs HTTP/2 CONNECT عبر الوكيل أيضًا والتأكد من أن بيئة اختبار APNs تستجيب؛ يستخدم الفحص رمز موفّر غير صالح عمدًا، لذلك تُعد استجابة APNs `403 InvalidProviderToken` إشارة نجاح للوصول.

الخيارات:

  * `--json`: اطبع JSON قابلًا للقراءة آليًا.
  * `--proxy-url <url>`: تحقق من عنوان URL هذا للوكيل بدلًا من الإعدادات أو البيئة.
  * `--allowed-url <url>`: أضف وجهة يُتوقع أن تنجح عبر الوكيل. كررها لفحص وجهات متعددة.
  * `--denied-url <url>`: أضف وجهة يُتوقع أن يحظرها الوكيل. كررها لفحص وجهات متعددة.
  * `--apns-reachable`: تحقق أيضًا من إمكانية الوصول إلى APNs HTTP/2 في بيئة الاختبار عبر الوكيل.
  * `--apns-authority <url>`: سلطة APNs المراد فحصها باستخدام `--apns-reachable` (`https://api.sandbox.push.apple.com` افتراضيًا؛ الإنتاج هو `https://api.push.apple.com`).
  * `--timeout-ms <ms>`: مهلة كل طلب بالمللي ثانية.


راجع [وكيل الشبكة](</ar/security/network-proxy>) للحصول على إرشادات النشر ودلالات الرفض.

## إعدادات الاستعلام المسبقة

يقبل `openclaw proxy query --preset <name>`:

  * `double-sends`
  * `retry-storms`
  * `cache-busting`
  * `ws-duplicate-frames`
  * `missing-ack`
  * `error-bursts`


## ملاحظات

  * يستخدم `start` القيمة `127.0.0.1` افتراضيًا ما لم يتم تعيين `--host`.
  * يبدأ `run` وكيل تصحيح محليًا ثم يشغّل الأمر بعد `--`.
  * يفتح تمرير المنبع المباشر لوكيل التصحيح مقابس منبع لأغراض التشخيص. عندما يكون وضع الوكيل المُدار من OpenClaw نشطًا، يُعطّل التمرير المباشر لطلبات الوكيل وأنفاق CONNECT افتراضيًا؛ عيّن `OPENCLAW_DEBUG_PROXY_ALLOW_DIRECT_CONNECT_WITH_MANAGED_PROXY=1` فقط لتشخيصات محلية معتمدة.
  * يخرج `validate` بالرمز 1 عند فشل إعدادات الوكيل أو فحوصات الوجهة.
  * الالتقاطات هي بيانات تصحيح محلية؛ استخدم `openclaw proxy purge` عند الانتهاء.


## ذات صلة

  * [مرجع CLI](</ar/cli>)
  * [وكيل الشبكة](</ar/security/network-proxy>)
  * [مصادقة الوكيل الموثوق](</ar/gateway/trusted-proxy-auth>)


Was this useful?YesNo