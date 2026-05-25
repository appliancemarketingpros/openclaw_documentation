---
title: تعطل Node + tsx
source_url: https://docs.openclaw.ai/ar/debug/node-issue
scraped_at: 2026-05-25
---

# تعطل Node + tsx بسبب "__name is not a function"

## الملخص

يفشل تشغيل OpenClaw عبر Node باستخدام `tsx` عند بدء التشغيل مع:

CodeCopy code
[code]
    [openclaw] Failed to start CLI: TypeError: __name is not a function    at createSubsystemLogger (.../src/logging/subsystem.ts:203:25)    at .../src/agents/auth-profiles/constants.ts:25:20
[/code]

بدأ ذلك بعد تبديل سكربتات التطوير من Bun إلى `tsx` (الالتزام `2871657e`، 2026-01-06). كان مسار وقت التشغيل نفسه يعمل مع Bun.

## البيئة

  * Node: v25.x (لوحظ على v25.3.0)
  * tsx: 4.21.0
  * نظام التشغيل: macOS (من المرجح أن تتكرر المشكلة أيضًا على منصات أخرى تشغل Node 25)


## إعادة الإنتاج (Node فقط)

bashCopy code
[code]
    # in repo rootnode --versionpnpm installnode --import tsx src/entry.ts status
[/code]

## إعادة إنتاج مصغرة في المستودع

bashCopy code
[code]
    node --import tsx scripts/repro/tsx-name-repro.ts
[/code]

## فحص إصدار Node

  * Node 25.3.0: يفشل
  * Node 22.22.0 (Homebrew `node@22`): يفشل
  * Node 24: غير مثبت هنا بعد؛ يحتاج إلى التحقق


## ملاحظات / فرضية

  * يستخدم `tsx` esbuild لتحويل TS/ESM. يصدر `keepNames` في esbuild مساعد `__name` ويلف تعريفات الدوال باستخدام `__name(...)`.
  * يشير التعطل إلى أن `__name` موجود لكنه ليس دالة في وقت التشغيل، ما يعني أن المساعد مفقود أو تمت الكتابة فوقه لهذه الوحدة في مسار محمل Node 25.
  * أُبلغ عن مشكلات مشابهة في مساعد `__name` لدى مستهلكين آخرين لـ esbuild عندما يكون المساعد مفقودًا أو تمت إعادة كتابته.


## تاريخ الانحدار

  * `2871657e` (2026-01-06): تغيرت السكربتات من Bun إلى tsx لجعل Bun اختياريًا.
  * قبل ذلك (مسار Bun)، كان `openclaw status` و`gateway:watch` يعملان.


## الحلول المؤقتة

  * استخدم Bun لسكربتات التطوير (التراجع المؤقت الحالي).

  * استخدم `tsgo` لفحص الأنواع في المستودع، ثم شغل الناتج المبني:

bashCopy code
[code]pnpm tsgonode openclaw.mjs status
[/code]

  * ملاحظة تاريخية: استُخدم `tsc` هنا أثناء تصحيح مشكلة Node/tsx هذه، لكن مسارات فحص الأنواع في المستودع تستخدم الآن `tsgo`.

  * عطّل keepNames في esbuild داخل محمل TS إن أمكن (يمنع إدراج مساعد `__name`)؛ لا يوفّر tsx هذا حاليًا.

  * اختبر Node LTS (22/24) مع `tsx` لمعرفة ما إذا كانت المشكلة خاصة بـ Node 25.


## المراجع

  * <https://opennext.js.org/cloudflare/howtos/keep_names>
  * <https://esbuild.github.io/api/#keep-names>
  * <https://github.com/evanw/esbuild/issues/1031>


## الخطوات التالية

  * إعادة الإنتاج على Node 22/24 لتأكيد انحدار Node 25.
  * اختبار `tsx` nightly أو تثبيته على إصدار أقدم إذا كان هناك انحدار معروف.
  * إذا تكررت المشكلة على Node LTS، فافتح إعادة إنتاج مصغرة لدى المنبع مع تتبع مكدس `__name`.


## ذو صلة

  * [تثبيت Node.js](</ar/install/node>)
  * [استكشاف أخطاء Gateway وإصلاحها](</ar/gateway/troubleshooting>)


Was this useful?YesNo