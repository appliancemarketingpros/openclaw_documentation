---
title: Plugin Zalo الشخصي
source_url: https://docs.openclaw.ai/ar/plugins/zalouser
scraped_at: 2026-05-25
---

دعم Zalo Personal لـ OpenClaw عبر Plugin، باستخدام `zca-js` الأصلي لأتمتة حساب مستخدم Zalo عادي.

## التسمية

معرّف القناة هو `zalouser` لتوضيح أن هذا يؤتمت **حساب مستخدم Zalo شخصيًا** (غير رسمي). نُبقي `zalo` محجوزًا لتكامل محتمل مستقبلًا مع واجهة Zalo API الرسمية.

## أين يعمل

يعمل هذا Plugin **داخل عملية Gateway**.

إذا كنت تستخدم Gateway بعيدًا، فثبّته/اضبطه على **الجهاز الذي يشغّل Gateway** ، ثم أعد تشغيل Gateway.

لا يلزم وجود ملف CLI تنفيذي خارجي لـ `zca`/`openzca`.

## التثبيت

### الخيار أ: التثبيت من npm

bashCopy code
[code]
    openclaw plugins install @openclaw/zalouser
[/code]

استخدم الحزمة المجردة لمتابعة وسم الإصدار الرسمي الحالي. ثبّت إصدارًا دقيقًا فقط عندما تحتاج إلى تثبيت قابل لإعادة الإنتاج.

أعد تشغيل Gateway بعد ذلك.

### الخيار ب: التثبيت من مجلد محلي (للتطوير)

bashCopy code
[code]
    PLUGIN_SRC=./path/to/local/zalouser-pluginopenclaw plugins install "$PLUGIN_SRC"cd "$PLUGIN_SRC" && pnpm install
[/code]

أعد تشغيل Gateway بعد ذلك.

## الإعدادات

توجد إعدادات القناة ضمن `channels.zalouser` (وليس `plugins.entries.*`):

json5Copy code
[code]
    {  channels: {    zalouser: {      enabled: true,      dmPolicy: "pairing",    },  },}
[/code]

## CLI

bashCopy code
[code]
    openclaw channels login --channel zalouseropenclaw channels logout --channel zalouseropenclaw channels status --probeopenclaw message send --channel zalouser --target <threadId> --message "Hello from OpenClaw"openclaw directory peers list --channel zalouser --query "name"
[/code]

## أداة الوكيل

اسم الأداة: `zalouser`

الإجراءات: `send`، `image`، `link`، `friends`، `groups`، `me`، `status`

تدعم إجراءات رسائل القناة أيضًا `react` لتفاعلات الرسائل.

## ذو صلة

  * [بناء Plugins](</ar/plugins/building-plugins>)
  * [ClawHub](</ar/clawhub>)


Was this useful?YesNo