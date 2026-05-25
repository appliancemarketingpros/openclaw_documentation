---
title: نظام أسماء النطاقات
source_url: https://docs.openclaw.ai/ar/cli/dns
scraped_at: 2026-05-25
---

# `openclaw dns`

مساعدات DNS للاكتشاف واسع النطاق (Tailscale + CoreDNS). تركز حاليًا على macOS + Homebrew CoreDNS.

ذات صلة:

  * اكتشاف Gateway: [الاكتشاف](</ar/gateway/discovery>)
  * تهيئة الاكتشاف واسع النطاق: [التهيئة](</ar/gateway/configuration>)


## الإعداد

bashCopy code
[code]
    openclaw dns setupopenclaw dns setup --domain openclaw.internalopenclaw dns setup --apply
[/code]

## `dns setup`

خطّط أو طبّق إعداد CoreDNS لاكتشاف DNS-SD أحادي البث.

الخيارات:

  * `--domain <domain>`: نطاق الاكتشاف واسع النطاق (على سبيل المثال `openclaw.internal`)
  * `--apply`: تثبيت تهيئة CoreDNS أو تحديثها وإعادة تشغيل الخدمة (يتطلب sudo؛ macOS فقط)


ما يعرضه:

  * نطاق الاكتشاف المحلول
  * مسار ملف المنطقة
  * عناوين IP الحالية لشبكة tailnet
  * تهيئة اكتشاف `openclaw.json` الموصى بها
  * قيم خادم الأسماء/النطاق لـ Tailscale Split DNS المطلوب ضبطها


ملاحظات:

  * بدون `--apply`، يكون الأمر مساعدًا للتخطيط فقط ويطبع الإعداد الموصى به.
  * إذا حُذف `--domain`، يستخدم OpenClaw قيمة `discovery.wideArea.domain` من التهيئة.
  * يدعم `--apply` حاليًا macOS فقط ويتوقع Homebrew CoreDNS.
  * يقوم `--apply` بتمهيد ملف المنطقة عند الحاجة، ويتأكد من وجود مقطع استيراد CoreDNS، ويعيد تشغيل خدمة brew الخاصة بـ `coredns`.


## ذات صلة

  * [مرجع CLI](</ar/cli>)
  * [الاكتشاف](</ar/gateway/discovery>)


Was this useful?YesNo