---
title: Tencent Cloud (TokenHub)
source_url: https://docs.openclaw.ai/ar/providers/tencent
scraped_at: 2026-05-25
---

Tencent Cloud يأتي بوصفه Plugin موفّرًا مضمّنًا في OpenClaw. يوفّر الوصول إلى معاينة Tencent Hy3 عبر نقطة نهاية TokenHub (`tencent-tokenhub`) باستخدام API متوافقة مع OpenAI.

الخاصية | القيمة  
---|---  
معرّف الموفّر | `tencent-tokenhub`  
Plugin | مضمّن، `enabledByDefault: true`  
متغيّر بيئة المصادقة | `TOKENHUB_API_KEY`  
علم الإعداد الأولي | `--auth-choice tokenhub-api-key`  
علم CLI المباشر | `--tokenhub-api-key <key>`  
API | متوافقة مع OpenAI (`openai-completions`)  
عنوان URL الأساسي الافتراضي | `https://tokenhub.tencentmaas.com/v1`  
عنوان URL الأساسي العام | `https://tokenhub-intl.tencentmaas.com/v1` (تجاوز)  
النموذج الافتراضي | `tencent-tokenhub/hy3-preview`  
  
## البدء السريع

* ### أنشئ مفتاح API في TokenHub

أنشئ مفتاح API في Tencent Cloud TokenHub. إذا اخترت نطاق وصول محدودًا للمفتاح، فأدرج **معاينة Hy3** ضمن النماذج المسموح بها.

* ### شغّل الإعداد الأولي

OnboardingCopy code
[code]
    openclaw onboard --auth-choice tokenhub-api-key
[/code]

Direct flagCopy code
[code]
    openclaw onboard --non-interactive \--auth-choice tokenhub-api-key \--tokenhub-api-key "$TOKENHUB_API_KEY"
[/code]

Env onlyCopy code
[code]
    export TOKENHUB_API_KEY=...
[/code]

* ### تحقّق من النموذج

bashCopy code
[code]
    openclaw models list --provider tencent-tokenhub
[/code]

## إعداد غير تفاعلي

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice tokenhub-api-key \  --tokenhub-api-key "$TOKENHUB_API_KEY" \  --skip-health \  --accept-risk
[/code]

## الكتالوج المضمّن

مرجع النموذج | الاسم | الإدخال | السياق | الحد الأقصى للإخراج | ملاحظات  
---|---|---|---|---|---  
`tencent-tokenhub/hy3-preview` | معاينة Hy3 (TokenHub) | نص | 256,000 | 64,000 | افتراضي؛ مفعّل للاستدلال  
  
معاينة Hy3 هي نموذج اللغة الكبير MoE من Tencent Hunyuan للاستدلال، واتباع التعليمات ذات السياق الطويل، والبرمجة، وسير عمل الوكلاء. تستخدم أمثلة Tencent المتوافقة مع OpenAI القيمة `hy3-preview` كمعرّف النموذج وتدعم استدعاء الأدوات القياسي عبر إكمالات المحادثة بالإضافة إلى `reasoning_effort`.

## تسعير متدرّج

يأتي الكتالوج المضمّن مع بيانات تكلفة وصفية متدرّجة تتوسّع بحسب طول نافذة الإدخال، لذلك تُملأ تقديرات التكلفة من دون تجاوزات يدوية.

نطاق رموز الإدخال | معدل الإدخال | معدل الإخراج | قراءة ذاكرة التخزين المؤقت  
---|---|---|---  
0 - 16,000 | 0.176 | 0.587 | 0.059  
16,000 - 32,000 | 0.235 | 0.939 | 0.088  
32,000+ | 0.293 | 1.173 | 0.117  
  
المعدلات لكل مليون رمز بالدولار الأمريكي كما تعلنها Tencent. لا تتجاوز التسعير ضمن `models.providers.tencent-tokenhub` إلا عندما تحتاج إلى سطح مختلف.

## التكوين المتقدم

تجاوز نقطة النهاية

يستخدم OpenClaw افتراضيًا نقطة نهاية Tencent Cloud: `https://tokenhub.tencentmaas.com/v1`. توثّق Tencent أيضًا نقطة نهاية دولية لـ TokenHub:

bashCopy code
[code]
    openclaw config set models.providers.tencent-tokenhub.baseUrl "https://tokenhub-intl.tencentmaas.com/v1"
[/code]

لا تتجاوز نقطة النهاية إلا عندما يتطلب حسابك أو منطقتك في TokenHub ذلك.

توفر البيئة للبرنامج الخفي

إذا كان Gateway يعمل كخدمة مُدارة (launchd أو systemd أو Docker)، فيجب أن يكون `TOKENHUB_API_KEY` مرئيًا لتلك العملية. عيّنه في `~/.openclaw/.env` أو عبر `env.shellEnv` حتى تتمكن بيئات launchd أو systemd أو Docker exec من قراءته.

## ذو صلة

[**موفّرو النماذج** اختيار الموفّرين ومراجع النماذج وسلوك تجاوز الفشل. ](</ar/concepts/model-providers>) [**مرجع التكوين** مخطط التكوين الكامل، بما في ذلك إعدادات الموفّر. ](</ar/gateway/configuration>) [**Tencent TokenHub** صفحة منتج TokenHub من Tencent Cloud. ](<https://cloud.tencent.com/product/tokenhub>) [**بطاقة نموذج معاينة Hy3** تفاصيل ومعايير أداء معاينة Tencent Hunyuan Hy3. ](<https://huggingface.co/tencent/Hy3-preview>)

Was this useful?YesNo