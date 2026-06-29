---
title: صندوق Upstash
source_url: https://docs.openclaw.ai/ar/install/upstash
scraped_at: 2026-06-29
---

InstallHosting

شغّل Gateway دائمًا من OpenClaw على Upstash Box، وهي بيئة Linux مُدارة تدعم دورة حياة الإبقاء قيد التشغيل.

استخدم نفق SSH للوصول إلى لوحة المعلومات. لا تكشف منفذ Gateway مباشرةً للإنترنت العام.

## المتطلبات الأساسية

  * حساب Upstash
  * Upstash Box مع إبقاء قيد التشغيل
  * عميل SSH على جهازك المحلي


## إنشاء Box

أنشئ Box مع إبقاء قيد التشغيل في Upstash Console. دوّن معرّف Box، مثل `right-flamingo-14486`، ومفتاح API الخاص بـ Box لديك.

تحتفظ Upstash بدليلها الحالي لإعداد OpenClaw Box على [إعداد OpenClaw](<https://upstash.com/docs/box/guides/openclaw-setup>).

## الاتصال عبر نفق SSH

مرّر منفذ لوحة معلومات OpenClaw إلى جهازك المحلي. استخدم مفتاح API الخاص بـ Box ككلمة مرور SSH عند مطالبتك بذلك:

bashCopy code
[code]
    ssh -o ServerAliveInterval=15 -o ServerAliveCountMax=3 -L 18789:127.0.0.1:18789 <box-id>@us-east-1.box.upstash.com
[/code]

تقلل خيارات الإبقاء قيد التشغيل انقطاعات النفق الخامل أثناء الإعداد الأولي.

## تثبيت OpenClaw

داخل Box:

bashCopy code
[code]
    sudo npm install -g openclaw
[/code]

## تشغيل الإعداد الأولي

bashCopy code
[code]
    openclaw onboard --install-daemon
[/code]

اتبع المطالبات. انسخ عنوان URL ورمز لوحة المعلومات عند اكتمال الإعداد الأولي.

## بدء Gateway

هيّئ Gateway لشبكة Box وابدأ تشغيله في الخلفية:

bashCopy code
[code]
    openclaw config set gateway.bind lannohup openclaw gateway > gateway.log 2>&1 &
[/code]

مع تفعيل نفق SSH، افتح عنوان URL الخاص بلوحة المعلومات محليًا:

textCopy code
[code]
    http://127.0.0.1:18789/#token=<your-token>
[/code]

## إعادة التشغيل التلقائي

عيّن هذا الأمر كسكربت تهيئة Box حتى يُعاد تشغيل Gateway عند بدء Box:

bashCopy code
[code]
    nohup openclaw gateway > gateway.log 2>&1 &
[/code]

## استكشاف الأخطاء وإصلاحها

إذا تجمّد SSH أثناء الإعداد الأولي، فأعد الاتصال باستخدام إعداد SSH نظيف وخيارات الإبقاء قيد التشغيل:

bashCopy code
[code]
    ssh -F /dev/null -o ControlMaster=no -o ServerAliveInterval=15 -o ServerAliveCountMax=3 -L 18789:127.0.0.1:18789 <box-id>@us-east-1.box.upstash.com
[/code]

يتجاوز هذا إعدادات `~/.ssh/config` المحلية القديمة ويحافظ على النفق نشطًا خلال فترات خمول الشبكة.

## ذات صلة

  * [الوصول عن بُعد](</ar/gateway/remote>)
  * [أمان Gateway](</ar/gateway/security>)
  * [تحديث OpenClaw](</ar/install/updating>)


Was this useful?YesNo

Open issue