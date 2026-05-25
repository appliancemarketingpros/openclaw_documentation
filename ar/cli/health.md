---
title: الصحة
source_url: https://docs.openclaw.ai/ar/cli/health
scraped_at: 2026-05-25
---

# `openclaw health`

اجلب حالة الصحة من الـ Gateway قيد التشغيل.

## الخيارات

الخيار | الافتراضي | الوصف  
---|---|---  
`--json` | `false` | اطبع JSON قابلا للقراءة آليا بدلا من النص.  
`--timeout <ms>` | `10000` | مهلة الاتصال بالمللي ثانية.  
`--verbose` | `false` | تسجيل مفصل. يفرض فحصا حيا ويوسع مخرجات كل وكيل.  
`--debug` | `false` | اسم بديل لـ `--verbose`.  
  
أمثلة:

bashCopy code
[code]
    openclaw healthopenclaw health --jsonopenclaw health --timeout 2500openclaw health --verboseopenclaw health --debug
[/code]

ملاحظات:

  * يطلب `openclaw health` الافتراضي من الـ Gateway قيد التشغيل لقطة حالة الصحة الخاصة به. عندما تكون لدى الـ Gateway بالفعل لقطة مخزنة مؤقتا وحديثة، يمكنه إرجاع تلك الحمولة المخزنة مؤقتا والتحديث في الخلفية.
  * يفرض `--verbose` فحصا حيا، ويطبع تفاصيل اتصال Gateway، ويوسع المخرجات القابلة للقراءة البشرية عبر جميع الحسابات والوكلاء المكوّنين.
  * تتضمن المخرجات مخازن جلسات لكل وكيل عند تكوين عدة وكلاء.


## ذات صلة

  * [مرجع CLI](</ar/cli>)
  * [حالة صحة Gateway](</ar/gateway/health>)


Was this useful?YesNo