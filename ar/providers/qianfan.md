---
title: Qianfan
source_url: https://docs.openclaw.ai/ar/providers/qianfan
scraped_at: 2026-05-25
---

Qianfan هي منصة MaaS من Baidu، وتوفّر **واجهة API موحّدة** توجّه الطلبات إلى العديد من النماذج خلف نقطة نهاية واحدة ومفتاح API واحد. وهي متوافقة مع OpenAI، لذا تعمل معظم SDKs الخاصة بـ OpenAI عبر تبديل عنوان URL الأساسي.

الخاصية | القيمة  
---|---  
المزوّد | `qianfan`  
المصادقة | `QIANFAN_API_KEY`  
API | متوافقة مع OpenAI  
عنوان URL الأساسي | `https://qianfan.baidubce.com/v2`  
  
## بدء الاستخدام

* ### Create a Baidu Cloud account

سجّل أو ادخل إلى [وحدة تحكم Qianfan](<https://console.bce.baidu.com/qianfan/ais/console/apiKey>) وتأكد من تمكين وصولك إلى Qianfan API.

* ### Generate an API key

أنشئ تطبيقًا جديدًا أو اختر تطبيقًا موجودًا، ثم أنشئ مفتاح API. صيغة المفتاح هي `bce-v3/ALTAK-...`.

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice qianfan-api-key
[/code]

* ### Verify the model is available

bashCopy code
[code]
    openclaw models list --provider qianfan
[/code]

## الكتالوج المضمّن

مرجع النموذج | الإدخال | السياق | الحد الأقصى للمخرجات | الاستدلال | ملاحظات  
---|---|---|---|---|---  
`qianfan/deepseek-v3.2` | نص | 98,304 | 32,768 | نعم | النموذج الافتراضي  
`qianfan/ernie-5.0-thinking-preview` | نص، صورة | 119,000 | 64,000 | نعم | متعدد الوسائط  
  
## مثال تكوين

json5Copy code
[code]
    {  env: { QIANFAN_API_KEY: "bce-v3/ALTAK-..." },  agents: {    defaults: {      model: { primary: "qianfan/deepseek-v3.2" },      models: {        "qianfan/deepseek-v3.2": { alias: "QIANFAN" },      },    },  },  models: {    providers: {      qianfan: {        baseUrl: "https://qianfan.baidubce.com/v2",        api: "openai-completions",        models: [          {            id: "deepseek-v3.2",            name: "DEEPSEEK V3.2",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 98304,            maxTokens: 32768,          },          {            id: "ernie-5.0-thinking-preview",            name: "ERNIE-5.0-Thinking-Preview",            reasoning: true,            input: ["text", "image"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 119000,            maxTokens: 64000,          },        ],      },    },  },}
[/code]

Transport and compatibility

يعمل Qianfan عبر مسار النقل المتوافق مع OpenAI، وليس عبر تشكيل طلبات OpenAI الأصلي. يعني ذلك أن ميزات SDK القياسية الخاصة بـ OpenAI تعمل، لكن قد لا يتم تمرير المعلمات الخاصة بالمزوّد.

Catalog and overrides

يتضمن الكتالوج المضمّن حاليًا `deepseek-v3.2` و`ernie-5.0-thinking-preview`. أضف أو تجاوز `models.providers.qianfan` فقط عندما تحتاج إلى عنوان URL أساسي مخصص أو بيانات وصفية للنموذج.

Troubleshooting

  * تأكد من أن مفتاح API يبدأ بـ `bce-v3/ALTAK-` وأن وصول Qianfan API مفعّل في وحدة تحكم Baidu Cloud.
  * إذا لم تكن النماذج مدرجة، فتأكد من تنشيط خدمة Qianfan في حسابك.
  * عنوان URL الأساسي الافتراضي هو `https://qianfan.baidubce.com/v2`. لا تغيّره إلا إذا كنت تستخدم نقطة نهاية مخصصة أو وكيلًا.


## ذات صلة

[**Model selection** اختيار المزوّدين ومراجع النماذج وسلوك تجاوز الفشل. ](</ar/concepts/model-providers>) [**Configuration reference** مرجع تكوين OpenClaw الكامل. ](</ar/gateway/configuration-reference>) [**Agent setup** تكوين افتراضيات الوكيل وتعيينات النماذج. ](</ar/concepts/agent>) [**Qianfan API docs** وثائق Qianfan API الرسمية. ](<https://cloud.baidu.com/doc/qianfan-api/s/3m7of64lb>)

Was this useful?YesNo