---
title: Tokenjuice
source_url: https://docs.openclaw.ai/ar/tools/tokenjuice
scraped_at: 2026-05-25
---

`tokenjuice` هو Plugin مضمّن اختياري يقوم بضغط نتائج أداتي `exec` و`bash` الصاخبة بعد أن يكون الأمر قد نُفِّذ بالفعل.

وهو يغيّر `tool_result` المعاد، وليس الأمر نفسه. ولا يقوم Tokenjuice بإعادة كتابة مدخلات shell، أو إعادة تشغيل الأوامر، أو تغيير رموز الخروج.

واليوم ينطبق هذا على تشغيلات PI المضمّنة وأدوات OpenClaw الديناميكية في حزام Codex app-server. ويتصل Tokenjuice بوسيط نتائج الأدوات في OpenClaw ويقوم بتقليم المخرجات قبل أن تعود إلى جلسة الحزام النشطة.

## فعّل Plugin

المسار السريع:

bashCopy code
[code]
    openclaw config set plugins.entries.tokenjuice.enabled true
[/code]

والمكافئ له:

bashCopy code
[code]
    openclaw plugins enable tokenjuice
[/code]

يشحن OpenClaw هذا Plugin بالفعل. ولا توجد خطوة منفصلة من نوع `plugins install` أو `tokenjuice install openclaw`.

إذا كنت تفضّل تعديل الإعدادات مباشرة:

json5Copy code
[code]
    {  plugins: {    entries: {      tokenjuice: {        enabled: true,      },    },  },}
[/code]

## ما الذي يغيّره tokenjuice

  * يضغط نتائج `exec` و`bash` الصاخبة قبل إعادتها إلى الجلسة.
  * يبقي تنفيذ الأمر الأصلي من دون تغيير.
  * يحافظ على قراءات محتوى الملفات الدقيقة والأوامر الأخرى التي ينبغي أن يتركها tokenjuice خامًا.
  * يظل خيار اشتراك صريح: عطّل Plugin إذا كنت تريد مخرجات حرفية في كل مكان.


## تحقق من أنه يعمل

  1. فعّل Plugin.
  2. ابدأ جلسة يمكنها استدعاء `exec`.
  3. شغّل أمرًا صاخبًا مثل `git status`.
  4. تحقق من أن نتيجة الأداة المعادة أقصر وأكثر تنظيمًا من مخرجات shell الخام.


## عطّل Plugin

bashCopy code
[code]
    openclaw config set plugins.entries.tokenjuice.enabled false
[/code]

أو:

bashCopy code
[code]
    openclaw plugins disable tokenjuice
[/code]

## ذو صلة

  * [أداة Exec](</ar/tools/exec>)
  * [مستويات التفكير](</ar/tools/thinking>)
  * [محرك السياق](</ar/concepts/context-engine>)


Was this useful?YesNo