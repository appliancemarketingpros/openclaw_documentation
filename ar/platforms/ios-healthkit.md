---
title: ملخصات HealthKit
source_url: https://docs.openclaw.ai/ar/platforms/ios-healthkit
scraped_at: 2026-10-12
---

PlatformsPlatforms overview

# ملخصات HealthKit

يمكن لـ OpenClaw طلب ملخص للقراءة فقط لليوم التقويمي الحالي من عقدة iPhone متصلة. يحسب iPhone القيم المجمعة على الجهاز ويعيد فقط عدد الخطوات ومدة النوم ومتوسط معدل ضربات القلب أثناء الراحة وعدد التمارين ومدتها. لا تُدعم عينات HealthKit الفردية أو المصادر أو البيانات الوصفية أو السجلات السريرية أو استيعاب البيانات في الخلفية أو عمليات الكتابة.

هذه الميزة معطلة افتراضيًا. وهي تتطلب موافقة منفصلة على iPhone وتفويضًا على Gateway.

## المتطلبات

  * جهاز iPhone يشغّل تطبيق OpenClaw لنظام iOS وتفيد فيه HealthKit بأن البيانات الصحية متاحة.
  * عقدة iPhone متصلة ومعتمدة. راجع [إعداد تطبيق iOS](</ar/platforms/ios>).
  * إصدار حالي من Gateway يمكنه الوصول إلى عقدة iPhone.
  * بيانات صحية قابلة للقراءة لأي مقاييس تتوقع ظهورها. يمكن لـ Apple Watch إضافة بيانات إلى مخزن Health على iPhone، لكن تطبيق OpenClaw لنظام watchOS غير مطلوب لملخصات HealthKit.


## تمكين الوصول

### 1\. تفويض أمر Gateway

أضف `health.summary` إلى مصفوفة `gateway.nodes.allowCommands` الحالية في `openclaw.json`. احتفظ بأي أوامر موجودة بالفعل:

json5Copy code
[code]
    {  gateway: {    nodes: {      allowCommands: ["health.summary"],    },  },}
[/code]

يُصنَّف `health.summary` على أنه شديد الحساسية من ناحية الخصوصية، ولا تسمح به إعدادات منصة iOS الافتراضية مطلقًا. يتجاوز أي إدخال في `gateway.nodes.denyCommands` إدخال السماح. راجع [سياسة أوامر Node](</ar/nodes#command-policy>).

### 2\. تمكين المشاركة على iPhone

في تطبيق iOS:

  1. افتح **Settings - > Permissions -> Privacy & Access -> Health Summaries**.
  2. اضغط على **Enable & Share Summaries**.
  3. اقرأ بيان الإفصاح، ثم اختر فئات Health التي يُسمح لـ OpenClaw بقراءتها في ورقة أذونات Apple.


يسجل مفتاح التبديل اختيارك الصريح لمشاركة البيانات مع OpenClaw. ولا يعني ذلك أن Apple منحت الإذن لكل فئة مطلوبة.

يضيف تمكين ملخصات Health الأمر `health.summary` إلى سطح الأوامر المعلن للعقدة. اعتمد تحديث إقران العقدة الناتج:

bashCopy code
[code]
    openclaw nodes pendingopenclaw nodes approve <requestId>
[/code]

ثم تحقق من أن جهاز iPhone المتصل يعرض أمر `health.summary` فعليًا:

bashCopy code
[code]
    openclaw nodes describe --node "<iPhone name>"
[/code]

## طلب ملخص اليوم

لا يُدعم سوى `today`. ويغطي الفترة من منتصف الليل بالتوقيت المحلي حتى وقت الطلب، باستخدام التقويم والمنطقة الزمنية الحاليين على iPhone.

bashCopy code
[code]
    openclaw nodes invoke \  --node "<iPhone name>" \  --command health.summary \  --params '{"period":"today"}' \  --json
[/code]

يمكن للوكلاء استدعاء الأمر نفسه باستخدام أداة `nodes`:

jsonCopy code
[code]
    {  "action": "invoke",  "node": "<iPhone name>",  "invokeCommand": "health.summary",  "invokeParamsJson": "{\"period\":\"today\"}"}
[/code]

تتضمن حمولة الملخص ما يلي:

الحقل | المعنى  
---|---  
`period` | دائمًا `today`  
`startISO` | بداية اليوم بالتوقيت المحلي، مشفرة كلحظة زمنية بتنسيق ISO  
`endISO` | وقت الطلب، مشفر كلحظة زمنية بتنسيق ISO  
`timeZoneIdentifier` | معرّف المنطقة الزمنية لـ iPhone  
`stepCount` | إجمالي الخطوات مقربًا  
`sleepDurationMinutes` | مدة النوم بعد إزالة التكرار، ومقتصرة على اليوم  
`restingHeartRateBpm` | متوسط معدل ضربات القلب أثناء الراحة  
`workoutCount` | التمارين التي بدأت اليوم  
`workoutDurationMinutes` | المدة الإجمالية لتلك التمارين  
  
حقول المقاييس اختيارية وتُحذف عندما لا تعيد HealthKit أي قيمة قابلة للقراءة. تُدمج مراحل النوم والمصادر المتداخلة قبل حساب المدة، بحيث لا تُحتسب الدقيقة نفسها مرتين.

## سلوك الخصوصية

  * تُجرى عملية التجميع على iPhone. ولا تغادر العينات الأولية الجهاز.
  * تغادر القيم المجمعة المطلوبة iPhone عبر Gateway الخاص بك. عندما يطلبها وكيل، تصل القيم المجمعة إلى مزود الذكاء الاصطناعي المضبوط وقد تبقى في سجل المحادثة. ويعيدها استدعاء CLI المباشر إلى مشغّل CLI.
  * يطلب OpenClaw صلاحية القراءة فقط. ولا يمكنه إضافة بيانات Health أو تعديلها.
  * لا يقرأ OpenClaw بيانات HealthKit إلا عند استدعاء `health.summary`. ولا يحدث استيعاب للبيانات الصحية في الخلفية.
  * لا تكشف HealthKit عمدًا ما إذا كانت صلاحية القراءة قد رُفضت. وقد يعني غياب أحد المقاييس رفض الوصول أو عدم وجود عينات مطابقة أو عدم توفر نوع البيانات. ولا يستطيع OpenClaw التمييز بين هذه الحالات.
  * الملخص مخصص لسياق الصحة الشخصية واللياقة البدنية، وليس للتشخيص أو المشورة الطبية.


لإيقاف المشاركة، ارجع إلى **Health Summaries** واضغط على **Disable**. عندئذٍ يزيل iPhone إمكانية Health والأمر `health.summary` من سطح العقدة. ويمكنك أيضًا إزالة `health.summary` من `gateway.nodes.allowCommands` لإغلاق بوابة الوصول من جانب Gateway.

## استكشاف الأخطاء وإصلاحها

### الأمر غير معلن من جانب العقدة

تأكد من تمكين ملخصات Health في تطبيق iOS ومن اتصال iPhone. شغّل `openclaw nodes pending` واعتمد أي تحديث للإمكانات، ثم افحص `openclaw nodes describe --node "<iPhone name>"` مرة أخرى.

### يتطلب الأمر اشتراكًا صريحًا

أضف `health.summary` إلى `gateway.nodes.allowCommands`. وتحقق أيضًا من أن `gateway.nodes.denyCommands` لا يحتوي عليه؛ فقائمة الرفض لها الأولوية.

### `HEALTH_ACCESS_DISABLED`

مفتاح المشاركة في التطبيق معطل. فعّل **Health Summaries** ضمن **Privacy & Access** على iPhone.

### ينجح الملخص لكن بعض المقاييس مفقودة

افتح تطبيق Health من Apple وتأكد من وجود بيانات لليوم. راجع وصول OpenClaw في إعدادات Health من Apple، لكن لا تعتبر النتيجة الفارغة دليلًا على رفض الوصول، إذ تخفي HealthKit هذا التمييز عمدًا.

### تفشل النطاقات الأقدم

لا يقبل الأمر سوى `{"period":"today"}`. ولا تُدعم الملخصات متعددة الأيام أو التاريخية.

## ذو صلة

  * [تطبيق iOS](</ar/platforms/ios>)
  * [العقد](</ar/nodes>)
  * [مرجع إعداد Gateway](</ar/gateway/configuration-reference#gateway>)
  * [تدقيق الأمان](</ar/gateway/security>)


Was this useful?YesNo

Open issue