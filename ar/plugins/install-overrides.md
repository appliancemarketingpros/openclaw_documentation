---
title: تجاوزات تثبيت Plugin
source_url: https://docs.openclaw.ai/ar/plugins/install-overrides
scraped_at: 2026-05-25
---

تتيح تجاوزات تثبيت Plugin للمشرفين اختبار عمليات تثبيت Plugin وقت الإعداد مقابل حزمة npm محددة أو ملف tarball محلي من npm-pack. وهي مخصصة للتحقق من E2E والحزم فقط. ينبغي للمستخدمين العاديين تثبيت Plugin باستخدام [`openclaw plugins install`](</ar/cli/plugins>).

## البيئة

تكون التجاوزات معطلة ما لم يتم تعيين كلا المتغيرين:

bashCopy code
[code]
    export OPENCLAW_ALLOW_PLUGIN_INSTALL_OVERRIDES=1export OPENCLAW_PLUGIN_INSTALL_OVERRIDES='{  "codex": "npm-pack:/tmp/openclaw-codex-2026.5.8.tgz",  "openclaw-web-search": "npm:@openclaw/web-search@2026.5.8"}'
[/code]

خريطة التجاوز هي JSON مفهرسة حسب معرّف Plugin. تدعم القيم:

  * `npm:<registry-spec>` لحزم السجل والإصدارات أو الوسوم المحددة بدقة
  * `npm-pack:<path.tgz>` لملفات tarball المحلية الناتجة عن `npm pack`


تُحل مسارات `npm-pack:` النسبية من دليل العمل الحالي.

## السلوك

عندما يطلب تدفق وقت الإعداد تثبيت Plugin يظهر معرّفه في الخريطة، يستخدم OpenClaw مصدر التجاوز بدلاً من مصدر npm من الفهرس أو المضمّن أو الافتراضي. ينطبق هذا على التهيئة الأولية والتدفقات الأخرى التي تستخدم مثبّت Plugin المشترك وقت الإعداد.

تظل التجاوزات تفرض معرّف Plugin المتوقع. يجب أن يثبّت ملف tarball المعيّن إلى `codex` Plugin يكون معرّف بيانه هو `codex`.

لا ترث التجاوزات حالة المصدر الرسمي الموثوق. حتى عندما يمثل إدخال الفهرس عادةً حزمة مملوكة لـ OpenClaw، يُعامل التجاوز كمدخل اختبار مقدم من المشغّل.

لا يمكن لملفات `.env` في مساحة العمل تمكين تجاوزات التثبيت. عيّن هذه المتغيرات في الصدفة الموثوقة أو مهمة CI أو أمر الاختبار البعيد الذي يشغّل OpenClaw.

## E2E الحزم

استخدم دليل حالة معزولاً بحيث لا تمس عمليات تثبيت الحزم وسجلات التثبيت حالة OpenClaw العادية لديك:

bashCopy code
[code]
    npm pack extensions/codex --pack-destination /tmp OPENCLAW_STATE_DIR="$(mktemp -d)" \OPENCLAW_ALLOW_PLUGIN_INSTALL_OVERRIDES=1 \OPENCLAW_PLUGIN_INSTALL_OVERRIDES='{"codex":"npm-pack:/tmp/openclaw-codex-2026.5.8.tgz"}' \pnpm openclaw onboard --mode local
[/code]

تحقق من الحزمة المثبتة ضمن دليل الحالة:

bashCopy code
[code]
    find "$OPENCLAW_STATE_DIR/npm/node_modules" -maxdepth 3 -name package.json -printgrep -R '"@openclaw/codex"' "$OPENCLAW_STATE_DIR/npm/package-lock.json"
[/code]

بالنسبة إلى E2E لمزوّد حي، حمّل مفتاح API الحقيقي من صدفة موثوقة أو سر CI قبل تشغيل أمر الاختبار. لا تطبع المفاتيح؛ أبلغ فقط عن المصدر وما إذا كان المفتاح موجوداً.

Was this useful?YesNo