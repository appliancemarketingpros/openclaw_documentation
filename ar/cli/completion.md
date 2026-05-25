---
title: الإكمال
source_url: https://docs.openclaw.ai/ar/cli/completion
scraped_at: 2026-05-25
---

# `openclaw completion`

إنشاء سكربتات إكمال shell واختيارياً تثبيتها في ملف تعريف shell الخاص بك.

## الاستخدام

bashCopy code
[code]
    openclaw completionopenclaw completion --shell zshopenclaw completion --installopenclaw completion --shell fish --installopenclaw completion --write-stateopenclaw completion --shell bash --write-state
[/code]

## الخيارات

  * `-s, --shell <shell>`: هدف shell (`zsh` أو `bash` أو `powershell` أو `fish`؛ الافتراضي: `zsh`)
  * `-i, --install`: تثبيت الإكمال بإضافة سطر source إلى ملف تعريف shell الخاص بك
  * `--write-state`: كتابة سكربت/سكربتات الإكمال إلى `$OPENCLAW_STATE_DIR/completions` من دون الطباعة إلى stdout
  * `-y, --yes`: تخطي مطالبات تأكيد التثبيت


## ملاحظات

  * يكتب `--install` كتلة صغيرة باسم "OpenClaw Completion" في ملف تعريف shell الخاص بك ويوجهها إلى السكربت المخزن مؤقتًا.
  * من دون `--install` أو `--write-state`، يطبع الأمر السكربت إلى stdout.
  * يقوم إنشاء الإكمال بتحميل أشجار الأوامر بشكل مسبق حتى يتم تضمين الأوامر الفرعية المتداخلة.


## ذو صلة

  * [مرجع CLI](</ar/cli>)


Was this useful?YesNo