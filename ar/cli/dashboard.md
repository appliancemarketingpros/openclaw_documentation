---
title: لوحة المعلومات
source_url: https://docs.openclaw.ai/ar/cli/dashboard
scraped_at: 2026-05-25
---

# `openclaw dashboard`

افتح واجهة التحكم باستخدام مصادقتك الحالية.

bashCopy code
[code]
    openclaw dashboardopenclaw dashboard --no-open
[/code]

ملاحظات:

  * يحل `dashboard` مراجع SecretRefs الخاصة بـ `gateway.auth.token` المهيأة عندما يكون ذلك ممكنًا.
  * يتبع `dashboard` إعداد `gateway.tls.enabled`: تطبع/تفتح بوابات Gateway المفعّل فيها TLS عناوين URL لواجهة التحكم بصيغة `https://` وتتصل عبر `wss://`.
  * إذا فشل التسليم إلى الحافظة/المتصفح لعنوان URL للوحة تحكم مصادَق عليه برمز مميز، يسجل `dashboard` تلميحًا آمنًا للمصادقة اليدوية يذكر `OPENCLAW_GATEWAY_TOKEN`، و`gateway.auth.token`، ومفتاح الجزء `token` من دون طباعة قيمة الرمز المميز.
  * بالنسبة إلى الرموز المميزة المُدارة بواسطة SecretRef (سواء جرى حلها أم لا)، يطبع/ينسخ/يفتح `dashboard` عنوان URL غير متضمن لرمز مميز لتجنب كشف الأسرار الخارجية في مخرجات الطرفية، أو سجل الحافظة، أو وسائط تشغيل المتصفح.
  * إذا كان `gateway.auth.token` مُدارًا بواسطة SecretRef لكن لم يُحل في مسار هذا الأمر، يطبع الأمر عنوان URL غير متضمن لرمز مميز وإرشادات إصلاح صريحة بدلًا من تضمين عنصر نائب لرمز مميز غير صالح.


## ذو صلة

  * [مرجع CLI](</ar/cli>)
  * [لوحة التحكم](</ar/web/dashboard>)


Was this useful?YesNo