---
title: التدفقات (إعادة توجيه)
source_url: https://docs.openclaw.ai/ar/cli/flows
scraped_at: 2026-05-25
---

# `openclaw tasks flow`

لا يوجد أمر `openclaw flows` على المستوى الأعلى. يوجد فحص TaskFlow الدائم ضمن `openclaw tasks flow`.

## الأوامر الفرعية

bashCopy code
[code]
    openclaw tasks flow list   [--json] [--status <name>]openclaw tasks flow show   <lookup> [--json]openclaw tasks flow cancel <lookup>
[/code]

الأمر الفرعي | الوصف | الوسيطات / الخيارات  
---|---|---  
`list` | يسرد TaskFlows المتتبعة. | مخرجات `--json` قابلة للقراءة آليًا؛ مرشح `--status <name>` (انظر قيم الحالة أدناه).  
`show` | يعرض TaskFlow واحدًا. | `<lookup>` معرّف التدفق أو مفتاح المالك؛ مخرجات `--json` قابلة للقراءة آليًا.  
`cancel` | يلغي TaskFlow قيد التشغيل. | `<lookup>` معرّف التدفق أو مفتاح المالك.  
  
يقبل `<lookup>` إما معرّف تدفق (تعيده `list` / `show`) أو مفتاح مالك التدفق (المعرّف الثابت الذي يستخدمه النظام الفرعي المالك لتتبع التدفق).

### قيم مرشح الحالة

يقبل `--status` في `list` إحدى القيم التالية:

`queued`, `running`, `waiting`, `blocked`, `succeeded`, `failed`, `cancelled`, `lost`

## أمثلة

bashCopy code
[code]
    openclaw tasks flow listopenclaw tasks flow list --status runningopenclaw tasks flow list --jsonopenclaw tasks flow show flow_abc123openclaw tasks flow show flow_abc123 --jsonopenclaw tasks flow cancel flow_abc123
[/code]

للاطلاع على مفاهيم TaskFlow الكاملة والتأليف، راجع [TaskFlow](</ar/automation/taskflow>). ولأمر `tasks` الأصل، راجع [مرجع CLI للمهام](</ar/cli/tasks>).

## ذو صلة

  * [مرجع CLI](</ar/cli>)
  * [الأتمتة](</ar/automation>)
  * [TaskFlow](</ar/automation/taskflow>)


Was this useful?YesNo