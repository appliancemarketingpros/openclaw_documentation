---
title: Anthropic
source_url: https://docs.openclaw.ai/ar/providers/anthropic
scraped_at: 2026-05-25
---

تُطوّر Anthropic عائلة نماذج **Claude**. يدعم OpenClaw مساري مصادقة:

  * **مفتاح API** — وصول مباشر إلى Anthropic API مع فوترة حسب الاستخدام (نماذج `anthropic/*`)
  * **Claude CLI** — إعادة استخدام تسجيل دخول Claude CLI موجود على المضيف نفسه


## البدء

### مفتاح API

**الأفضل لـ:** وصول API القياسي والفوترة حسب الاستخدام.

* ### احصل على مفتاح API الخاص بك

أنشئ مفتاح API في [Anthropic Console](<https://console.anthropic.com/>).

* ### شغّل الإعداد الأولي

bashCopy code
[code]
    openclaw onboard# choose: Anthropic API key
[/code]

أو مرّر المفتاح مباشرةً:

bashCopy code
[code]
    openclaw onboard --anthropic-api-key "$ANTHROPIC_API_KEY"
[/code]

* ### تحقّق من أن النموذج متاح

bashCopy code
[code]
    openclaw models list --provider anthropic
[/code]

### مثال على الإعدادات

json5Copy code
[code]
    {  env: { ANTHROPIC_API_KEY: "sk-ant-..." },  agents: { defaults: { model: { primary: "anthropic/claude-opus-4-6" } } },}
[/code]

### Claude CLI

**الأفضل لـ:** إعادة استخدام تسجيل دخول Claude CLI موجود بدون مفتاح API منفصل.

* ### تأكّد من تثبيت Claude CLI وتسجيل الدخول إليه

تحقّق باستخدام:

bashCopy code
[code]
    claude --version
[/code]

* ### شغّل الإعداد الأولي

bashCopy code
[code]
    openclaw onboard# choose: Claude CLI
[/code]

يكتشف OpenClaw بيانات اعتماد Claude CLI الموجودة ويعيد استخدامها.

* ### تحقّق من أن النموذج متاح

bashCopy code
[code]
    openclaw models list --provider anthropic
[/code]

### مثال على الإعدادات

فضّل مرجع نموذج Anthropic القياسي مع تجاوز تشغيل CLI:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "anthropic/claude-opus-4-7" },      models: {        "anthropic/claude-opus-4-7": {          agentRuntime: { id: "claude-cli" },        },      },    },  },}
[/code]

لا تزال مراجع نماذج `claude-cli/claude-opus-4-7` القديمة تعمل من أجل التوافق، لكن يجب أن تبقي الإعدادات الجديدة اختيار المزوّد/النموذج بصيغة `anthropic/*` وأن تضع خلفية التنفيذ في سياسة تشغيل المزوّد/النموذج.

## افتراضيات التفكير (Claude 4.6)

تستخدم نماذج Claude 4.6 التفكير `adaptive` افتراضياً في OpenClaw عند عدم تعيين مستوى تفكير صريح.

تجاوز ذلك لكل رسالة باستخدام `/think:<level>` أو ضمن معاملات النموذج:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "anthropic/claude-opus-4-6": {          params: { thinking: "adaptive" },        },      },    },  },}
[/code]

## تخزين المطالبات مؤقتاً

يدعم OpenClaw ميزة تخزين المطالبات مؤقتاً من Anthropic لمصادقة مفتاح API.

القيمة | مدة التخزين المؤقت | الوصف  
---|---|---  
`"short"` (افتراضي) | 5 دقائق | يُطبّق تلقائياً لمصادقة مفتاح API  
`"long"` | ساعة واحدة | تخزين مؤقت ممتد  
`"none"` | بدون تخزين مؤقت | تعطيل تخزين المطالبات مؤقتاً  
json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "anthropic/claude-opus-4-6": {          params: { cacheRetention: "long" },        },      },    },  },}
[/code]

تجاوزات التخزين المؤقت لكل وكيل

استخدم معاملات مستوى النموذج كخط أساس، ثم تجاوز وكلاء محددين عبر `agents.list[].params`:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "anthropic/claude-opus-4-6" },      models: {        "anthropic/claude-opus-4-6": {          params: { cacheRetention: "long" },        },      },    },    list: [      { id: "research", default: true },      { id: "alerts", params: { cacheRetention: "none" } },    ],  },}
[/code]

ترتيب دمج الإعدادات:

  1. `agents.defaults.models["provider/model"].params`
  2. `agents.list[].params` (المطابقة لـ `id`، وتتجاوز حسب المفتاح)


يتيح هذا لوكيل واحد الاحتفاظ بذاكرة تخزين مؤقت طويلة الأمد بينما يعطّل وكيل آخر على النموذج نفسه التخزين المؤقت لحركة المرور المتقطعة/منخفضة إعادة الاستخدام.

ملاحظات Bedrock Claude

  * تقبل نماذج Anthropic Claude على Bedrock (`amazon-bedrock/*anthropic.claude*`) تمرير `cacheRetention` عند تكوينها.
  * تُجبَر نماذج Bedrock غير التابعة لـ Anthropic على `cacheRetention: "none"` وقت التشغيل.
  * كما تضع الافتراضيات الذكية لمفتاح API القيمة `cacheRetention: "short"` لمراجع Claude-on-Bedrock عندما لا تكون هناك قيمة صريحة معيّنة.


## الإعدادات المتقدمة

الوضع السريع

يدعم مفتاح التبديل المشترك `/fast` في OpenClaw حركة Anthropic المباشرة (مفتاح API وOAuth إلى `api.anthropic.com`).

الأمر | يُطابَق مع  
---|---  
`/fast on` | `service_tier: "auto"`  
`/fast off` | `service_tier: "standard_only"`  
json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "anthropic/claude-sonnet-4-6": {          params: { fastMode: true },        },      },    },  },}
[/code]

فهم الوسائط (الصور وPDF)

يسجّل Plugin Anthropic المضمّن فهم الصور وPDF. يحلّ OpenClaw إمكانات الوسائط تلقائياً من مصادقة Anthropic المكوّنة — لا حاجة إلى إعدادات إضافية.

الخاصية | القيمة  
---|---  
النموذج الافتراضي | `claude-opus-4-7`  
الإدخال المدعوم | الصور، مستندات PDF  
  
عند إرفاق صورة أو PDF بمحادثة، يوجّهها OpenClaw تلقائياً عبر مزوّد فهم وسائط Anthropic.

نافذة سياق 1M (تجريبية)

نافذة السياق 1M من Anthropic محكومة ببوابة تجريبية. فعّلها لكل نموذج:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "anthropic/claude-opus-4-6": {          params: { context1m: true },        },      },    },  },}
[/code]

يطابق OpenClaw هذا مع `anthropic-beta: context-1m-2025-08-07` في الطلبات.

ينطبق `params.context1m: true` أيضاً على خلفية Claude CLI (`claude-cli/*`) لنماذج Opus وSonnet المؤهلة، مما يوسّع نافذة سياق التشغيل لتلك جلسات CLI لتطابق سلوك API المباشر.

سياق 1M في Claude Opus 4.7

يملك `anthropic/claude-opus-4.7` ومتغيره `claude-cli` نافذة سياق 1M افتراضياً — لا حاجة إلى `params.context1m: true`.

## استكشاف الأخطاء وإصلاحها

أخطاء 401 / الرمز أصبح غير صالح فجأة

تنتهي صلاحية مصادقة رمز Anthropic ويمكن إبطالها. للإعدادات الجديدة، استخدم مفتاح Anthropic API بدلاً من ذلك.

لم يتم العثور على مفتاح API للمزوّد "anthropic"

مصادقة Anthropic هي **لكل وكيل** — لا ترث الوكلاء الجدد مفاتيح الوكيل الرئيسي. أعد تشغيل الإعداد الأولي لذلك الوكيل (أو كوّن مفتاح API على مضيف Gateway)، ثم تحقّق باستخدام `openclaw models status`.

لم يتم العثور على بيانات اعتماد للملف الشخصي "anthropic:default"

شغّل `openclaw models status` لمعرفة ملف المصادقة الشخصي النشط. أعد تشغيل الإعداد الأولي، أو كوّن مفتاح API لمسار ذلك الملف الشخصي.

لا يوجد ملف مصادقة شخصي متاح (الكل في فترة تهدئة)

افحص `openclaw models status --json` بحثاً عن `auth.unusableProfiles`. يمكن أن تكون فترات تهدئة حدود المعدل في Anthropic مقيّدة بنموذج معيّن، لذلك قد يظل نموذج Anthropic شقيق قابلاً للاستخدام. أضف ملف Anthropic شخصياً آخر أو انتظر انتهاء فترة التهدئة.

## ذات صلة

[**اختيار النموذج** اختيار المزوّدين، ومراجع النماذج، وسلوك تجاوز الفشل. ](</ar/concepts/model-providers>) [**خلفيات CLI** إعداد خلفية Claude CLI وتفاصيل التشغيل. ](</ar/gateway/cli-backends>) [**تخزين المطالبات مؤقتاً** كيفية عمل تخزين المطالبات مؤقتاً عبر المزوّدين. ](</ar/reference/prompt-caching>) [**OAuth والمصادقة** تفاصيل المصادقة وقواعد إعادة استخدام بيانات الاعتماد. ](</ar/gateway/authentication>)

Was this useful?YesNo