---
title: `openclaw commitments`
source_url: https://docs.openclaw.ai/ar/cli/commitments
scraped_at: 2026-05-25
---

اعرض وأدر التزامات المتابعة المستنتجة.

الالتزامات هي ذكريات متابعة اختيارية وقصيرة الأجل تُنشأ من سياق المحادثة. راجع [الالتزامات المستنتجة](</ar/concepts/commitments>) للاطلاع على الدليل المفاهيمي.

من دون أمر فرعي، يعرض `openclaw commitments` الالتزامات المعلّقة.

## الاستخدام

bashCopy code
[code]
    openclaw commitments [--all] [--agent <id>] [--status <status>] [--json]openclaw commitments list [--all] [--agent <id>] [--status <status>] [--json]openclaw commitments dismiss <id...> [--json]
[/code]

## الخيارات

  * `--all`: اعرض كل الحالات بدلاً من الالتزامات المعلّقة فقط.
  * `--agent <id>`: صفِّ النتائج إلى معرّف وكيل واحد.
  * `--status <status>`: صفِّ حسب الحالة. القيم: `pending`، و`sent`، و`dismissed`، و`snoozed`، أو `expired`.
  * `--json`: أخرج JSON قابلاً للقراءة آلياً.


## أمثلة

اعرض الالتزامات المعلّقة:

bashCopy code
[code]
    openclaw commitments
[/code]

اعرض كل التزام مخزّن:

bashCopy code
[code]
    openclaw commitments --all
[/code]

صفِّ إلى وكيل واحد:

bashCopy code
[code]
    openclaw commitments --agent main
[/code]

اعثر على الالتزامات المؤجلة:

bashCopy code
[code]
    openclaw commitments --status snoozed
[/code]

استبعد التزاماً واحداً أو أكثر:

bashCopy code
[code]
    openclaw commitments dismiss cm_abc123 cm_def456
[/code]

صدّر كـ JSON:

bashCopy code
[code]
    openclaw commitments --all --json
[/code]

## الإخراج

يتضمن الإخراج النصي:

  * معرّف الالتزام
  * الحالة
  * النوع
  * أقرب وقت استحقاق
  * النطاق
  * نص تسجيل الوصول المقترح


يتضمن إخراج JSON أيضاً مسار مخزن الالتزامات والسجلات المخزّنة الكاملة.

## ذو صلة

  * [الالتزامات المستنتجة](</ar/concepts/commitments>)
  * [نظرة عامة على الذاكرة](</ar/concepts/memory>)
  * [Heartbeat](</ar/gateway/heartbeat>)
  * [المهام المجدولة](</ar/automation/cron-jobs>)


Was this useful?YesNo