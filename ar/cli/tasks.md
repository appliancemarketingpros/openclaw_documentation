---
title: `openclaw tasks`
source_url: https://docs.openclaw.ai/ar/cli/tasks
scraped_at: 2026-05-25
---

افحص مهام الخلفية الدائمة وحالة Task Flow. دون أمر فرعي، يكون `openclaw tasks` مكافئًا لـ `openclaw tasks list`.

راجع [مهام الخلفية](</ar/automation/tasks>) لمعرفة دورة الحياة ونموذج التسليم.

## الاستخدام

bashCopy code
[code]
    openclaw tasksopenclaw tasks listopenclaw tasks list --runtime acpopenclaw tasks list --status runningopenclaw tasks show <lookup>openclaw tasks notify <lookup> state_changesopenclaw tasks cancel <lookup>openclaw tasks auditopenclaw tasks maintenanceopenclaw tasks maintenance --applyopenclaw tasks flow listopenclaw tasks flow show <lookup>openclaw tasks flow cancel <lookup>
[/code]

## خيارات الجذر

  * `--json`: إخراج JSON.
  * `--runtime <name>`: التصفية حسب النوع: `subagent` أو `acp` أو `cron` أو `cli`.
  * `--status <name>`: التصفية حسب الحالة: `queued` أو `running` أو `succeeded` أو `failed` أو `timed_out` أو `cancelled` أو `lost`.


## الأوامر الفرعية

### `list`

bashCopy code
[code]
    openclaw tasks list [--runtime <name>] [--status <name>] [--json]
[/code]

يسرد مهام الخلفية المتتبعة من الأحدث أولًا.

### `show`

bashCopy code
[code]
    openclaw tasks show <lookup> [--json]
[/code]

يعرض مهمة واحدة بحسب معرف المهمة أو معرف التشغيل أو مفتاح الجلسة.

### `notify`

bashCopy code
[code]
    openclaw tasks notify <lookup> <done_only|state_changes|silent>
[/code]

يغيّر سياسة الإشعارات لمهمة قيد التشغيل.

### `cancel`

bashCopy code
[code]
    openclaw tasks cancel <lookup>
[/code]

يلغي مهمة خلفية قيد التشغيل.

### `audit`

bashCopy code
[code]
    openclaw tasks audit [--severity <warn|error>] [--code <name>] [--limit <n>] [--json]
[/code]

يكشف سجلات المهام وTask Flow القديمة أو المفقودة أو التي فشل تسليمها أو غير المتسقة بطريقة أخرى. تُعد المهام المفقودة المحتفَظ بها حتى `cleanupAfter` تحذيرات؛ أما المهام المفقودة المنتهية الصلاحية أو غير المختومة زمنيًا فهي أخطاء.

### `maintenance`

bashCopy code
[code]
    openclaw tasks maintenance [--apply] [--json]
[/code]

يعرض معاينة أو يطبّق تسوية المهام وTask Flow، وختم التنظيف، والتقليم، وتنظيف سجل جلسات تشغيل Cron القديمة. بالنسبة إلى مهام Cron، تستخدم التسوية سجلات التشغيل/حالة المهام المستمرة قبل وسم مهمة نشطة قديمة بأنها `lost`، لذلك لا تتحول عمليات Cron المكتملة إلى أخطاء تدقيق زائفة لمجرد أن حالة تشغيل Gateway الموجودة في الذاكرة لم تعد موجودة. لا يُعد تدقيق CLI دون اتصال مصدرًا موثوقًا لمجموعة مهام Cron النشطة المحلية لعملية Gateway. تُوسم مهام CLI التي لها معرف تشغيل/معرف مصدر بأنها `lost` عندما يختفي سياق تشغيل Gateway الحي الخاص بها، حتى إذا بقي صف جلسة فرعية قديم. عند التطبيق، تقلّم الصيانة أيضًا صفوف سجل الجلسات `cron:<jobId>:run:<uuid>` الأقدم من 7 أيام مع الحفاظ على مهام Cron قيد التشغيل حاليًا وترك صفوف الجلسات غير المرتبطة بـ Cron دون تغيير.

### `flow`

bashCopy code
[code]
    openclaw tasks flow list [--status <name>] [--json]openclaw tasks flow show <lookup> [--json]openclaw tasks flow cancel <lookup>
[/code]

يفحص حالة Task Flow الدائمة ضمن سجل المهام أو يلغيها.

## ذات صلة

  * [مرجع CLI](</ar/cli>)
  * [مهام الخلفية](</ar/automation/tasks>)


Was this useful?YesNo