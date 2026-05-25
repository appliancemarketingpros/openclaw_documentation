---
title: جریان‌ها (تغییرمسیر)
source_url: https://docs.openclaw.ai/fa/cli/flows
scraped_at: 2026-05-25
---

# `openclaw tasks flow`

هیچ فرمان سطح‌بالای `openclaw flows` وجود ندارد. بازرسی پایدار TaskFlow زیر `openclaw tasks flow` قرار دارد.

## زیرفرمان‌ها

bashCopy code
[code]
    openclaw tasks flow list   [--json] [--status <name>]openclaw tasks flow show   <lookup> [--json]openclaw tasks flow cancel <lookup>
[/code]

زیرفرمان | توضیح | آرگومان‌ها / گزینه‌ها  
---|---|---  
`list` | TaskFlowهای ردیابی‌شده را فهرست می‌کند. | `--json` خروجی قابل‌خواندن توسط ماشین؛ `--status <name>` فیلتر (مقادیر وضعیت را در پایین ببینید).  
`show` | یک TaskFlow را نشان می‌دهد. | `<lookup>` شناسهٔ جریان یا کلید مالک؛ `--json` خروجی قابل‌خواندن توسط ماشین.  
`cancel` | یک TaskFlow در حال اجرا را لغو می‌کند. | `<lookup>` شناسهٔ جریان یا کلید مالک.  
  
`<lookup>` یا یک شناسهٔ جریان را می‌پذیرد (که توسط `list` / `show` برگردانده می‌شود) یا کلید مالک جریان را (شناسهٔ پایداری که زیرسامانهٔ مالک برای ردیابی جریان استفاده می‌کند).

### مقادیر فیلتر وضعیت

`--status` روی `list` یکی از این موارد را می‌پذیرد:

`queued`, `running`, `waiting`, `blocked`, `succeeded`, `failed`, `cancelled`, `lost`

## مثال‌ها

bashCopy code
[code]
    openclaw tasks flow listopenclaw tasks flow list --status runningopenclaw tasks flow list --jsonopenclaw tasks flow show flow_abc123openclaw tasks flow show flow_abc123 --jsonopenclaw tasks flow cancel flow_abc123
[/code]

برای مفاهیم کامل TaskFlow و شیوهٔ نگارش، [TaskFlow](</fa/automation/taskflow>) را ببینید. برای فرمان والد `tasks`، [مرجع CLI مربوط به tasks](</fa/cli/tasks>) را ببینید.

## مرتبط

  * [مرجع CLI](</fa/cli>)
  * [خودکارسازی](</fa/automation>)
  * [TaskFlow](</fa/automation/taskflow>)


Was this useful?YesNo