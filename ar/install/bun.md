---
title: Bun (تجريبي)
source_url: https://docs.openclaw.ai/ar/install/bun
scraped_at: 2026-05-25
---

Bun هو وقت تشغيل محلي اختياري لتشغيل TypeScript مباشرةً (`bun run ...`، `bun --watch ...`). يظل مدير الحزم الافتراضي هو `pnpm`، وهو مدعوم بالكامل وتستخدمه أدوات التوثيق. لا يستطيع Bun استخدام `pnpm-lock.yaml` وسيتجاهله.

## التثبيت

* ### Install dependencies

shCopy code
[code]
    bun install
[/code]

يتم تجاهل `bun.lock` / `bun.lockb` في git، لذلك لا يحدث تغيير زائد في المستودع. لتجاوز كتابة ملف القفل بالكامل:

shCopy code
[code]
    bun install --no-save
[/code]

* ### Build and test

shCopy code
[code]
    bun run buildbun run vitest run
[/code]

## نصوص دورة الحياة

يحظر Bun نصوص دورة حياة التبعيات ما لم تكن موثوقة صراحةً. في هذا المستودع، لا تكون النصوص المحظورة عادةً مطلوبة:

  * `baileys` `preinstall` \-- يتحقق من أن الإصدار الرئيسي من Node هو >= 20 (يعتمد OpenClaw افتراضيًا على Node 24 ولا يزال يدعم Node 22 LTS، حاليًا `22.16+`)
  * `protobufjs` `postinstall` \-- يصدر تحذيرات حول مخططات إصدارات غير متوافقة (لا توجد مصنوعات بناء)


إذا واجهت مشكلة وقت تشغيل تتطلب هذه النصوص، فاجعلها موثوقة صراحةً:

shCopy code
[code]
    bun pm trust baileys protobufjs
[/code]

## تنبيهات

لا تزال بعض النصوص ترمز pnpm بشكل ثابت (على سبيل المثال `docs:build` و`ui:*` و`protocol:check`). شغّلها عبر pnpm في الوقت الحالي.

## ذو صلة

  * [نظرة عامة على التثبيت](</ar/install>)
  * [Node.js](</ar/install/node>)
  * [التحديث](</ar/install/updating>)


Was this useful?YesNo