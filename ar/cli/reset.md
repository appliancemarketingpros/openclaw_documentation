---
title: إعادة التعيين
source_url: https://docs.openclaw.ai/ar/cli/reset
scraped_at: 2026-05-25
---

# `openclaw reset`

أعد تعيين الإعدادات/الحالة المحلية (مع الإبقاء على CLI مثبتًا).

الخيارات:

  * `--scope <scope>`: ‏`config` أو `config+creds+sessions` أو `full`
  * `--yes`: تخطي مطالبات التأكيد
  * `--non-interactive`: تعطيل المطالبات؛ ويتطلب `--scope` و`--yes`
  * `--dry-run`: طباعة الإجراءات دون إزالة الملفات


أمثلة:

bashCopy code
[code]
    openclaw backup createopenclaw resetopenclaw reset --dry-runopenclaw reset --scope config --yes --non-interactiveopenclaw reset --scope config+creds+sessions --yes --non-interactiveopenclaw reset --scope full --yes --non-interactive
[/code]

ملاحظات:

  * شغّل `openclaw backup create` أولًا إذا كنت تريد لقطة قابلة للاستعادة قبل إزالة الحالة المحلية.
  * إذا حذفت `--scope`، يستخدم `openclaw reset` مطالبة تفاعلية لاختيار ما يجب إزالته.
  * يكون `--non-interactive` صالحًا فقط عندما يتم ضبط كل من `--scope` و`--yes`.


## ذو صلة

  * [مرجع CLI](</ar/cli>)


Was this useful?YesNo