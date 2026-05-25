---
title: إلغاء التثبيت
source_url: https://docs.openclaw.ai/ar/cli/uninstall
scraped_at: 2026-05-25
---

# `openclaw uninstall`

ألغِ تثبيت خدمة Gateway + البيانات المحلية (يبقى CLI).

الخيارات:

  * `--service`: إزالة خدمة Gateway
  * `--state`: إزالة الحالة والتهيئة
  * `--workspace`: إزالة دلائل workspace
  * `--app`: إزالة تطبيق macOS
  * `--all`: إزالة الخدمة والحالة وworkspace والتطبيق
  * `--yes`: تخطّي مطالبات التأكيد
  * `--non-interactive`: تعطيل المطالبات؛ ويتطلب `--yes`
  * `--dry-run`: طباعة الإجراءات دون إزالة الملفات


أمثلة:

bashCopy code
[code]
    openclaw backup createopenclaw uninstallopenclaw uninstall --service --yes --non-interactiveopenclaw uninstall --state --workspace --yes --non-interactiveopenclaw uninstall --all --yesopenclaw uninstall --dry-run
[/code]

ملاحظات:

  * شغّل `openclaw backup create` أولًا إذا كنت تريد لقطة قابلة للاستعادة قبل إزالة الحالة أو مساحات العمل.
  * `--all` اختصار لإزالة الخدمة والحالة وworkspace والتطبيق معًا.
  * يتطلب `--non-interactive` استخدام `--yes`.


## ذو صلة

  * [مرجع CLI](</ar/cli>)
  * [إلغاء التثبيت](</ar/install/uninstall>)


Was this useful?YesNo