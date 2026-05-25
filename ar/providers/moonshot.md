---
title: Moonshot AI
source_url: https://docs.openclaw.ai/ar/providers/moonshot
scraped_at: 2026-05-25
---

توفر Moonshot واجهة Kimi API بنقاط نهاية متوافقة مع OpenAI. كوّن المزوّد واضبط النموذج الافتراضي على `moonshot/kimi-k2.6`، أو استخدم Kimi Coding مع `kimi/kimi-for-coding`.

## كتالوج النماذج المضمّن

مرجع النموذج | الاسم | الاستدلال | الإدخال | السياق | أقصى إخراج  
---|---|---|---|---|---  
`moonshot/kimi-k2.6` | Kimi K2.6 | لا | نص، صورة | 262,144 | 262,144  
`moonshot/kimi-k2.5` | Kimi K2.5 | لا | نص، صورة | 262,144 | 262,144  
`moonshot/kimi-k2-thinking` | Kimi K2 Thinking | نعم | نص | 262,144 | 262,144  
`moonshot/kimi-k2-thinking-turbo` | Kimi K2 Thinking Turbo | نعم | نص | 262,144 | 262,144  
`moonshot/kimi-k2-turbo` | Kimi K2 Turbo | لا | نص | 256,000 | 16,384  
  
تستخدم تقديرات التكلفة المضمّنة لنماذج K2 الحالية المستضافة لدى Moonshot أسعار الدفع حسب الاستخدام المنشورة من Moonshot: يبلغ سعر Kimi K2.6 مقدار $0.16/MTok عند إصابة ذاكرة التخزين المؤقت، و$0.95/MTok للإدخال، و$4.00/MTok للإخراج؛ ويبلغ سعر Kimi K2.5 مقدار $0.10/MTok عند إصابة ذاكرة التخزين المؤقت، و$0.60/MTok للإدخال، و$3.00/MTok للإخراج. تحتفظ إدخالات الكتالوج القديمة الأخرى بعناصر تكلفة صفرية نائبة ما لم تتجاوزها في الإعدادات.

## بدء الاستخدام

اختر المزوّد واتبع خطوات الإعداد.

### Moonshot API

**الأفضل لـ:** نماذج Kimi K2 عبر Moonshot Open Platform.

* ### Choose your endpoint region

خيار المصادقة | نقطة النهاية | المنطقة  
---|---|---  
`moonshot-api-key` | `https://api.moonshot.ai/v1` | دولية  
`moonshot-api-key-cn` | `https://api.moonshot.cn/v1` | الصين  
* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice moonshot-api-key
[/code]

أو لنقطة نهاية الصين:

bashCopy code
[code]
    openclaw onboard --auth-choice moonshot-api-key-cn
[/code]

* ### Set a default model

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "moonshot/kimi-k2.6" },    },  },}
[/code]

* ### Verify models are available

bashCopy code
[code]
    openclaw models list --provider moonshot
[/code]

* ### Run a live smoke test

استخدم دليل حالة معزولًا عندما تريد التحقق من الوصول إلى النموذج وتتبع التكلفة دون لمس جلساتك العادية:

bashCopy code
[code]
    OPENCLAW_CONFIG_PATH=/tmp/openclaw-kimi/openclaw.json \OPENCLAW_STATE_DIR=/tmp/openclaw-kimi \openclaw agent --local \  --session-id live-kimi-cost \  --message 'Reply exactly: KIMI_LIVE_OK' \  --thinking off \  --json
[/code]

يجب أن يبلّغ رد JSON عن `provider: "moonshot"` و `model: "kimi-k2.6"`. يخزّن إدخال سجل المساعد استخدام الرموز الموحّد بالإضافة إلى التكلفة المقدّرة ضمن `usage.cost` عندما تعيد Moonshot بيانات استخدام وصفية.

### مثال على الإعدادات

json5Copy code
[code]
    {  env: { MOONSHOT_API_KEY: "sk-..." },  agents: {    defaults: {      model: { primary: "moonshot/kimi-k2.6" },      models: {        // moonshot-kimi-k2-aliases:start        "moonshot/kimi-k2.6": { alias: "Kimi K2.6" },        "moonshot/kimi-k2.5": { alias: "Kimi K2.5" },        "moonshot/kimi-k2-thinking": { alias: "Kimi K2 Thinking" },        "moonshot/kimi-k2-thinking-turbo": { alias: "Kimi K2 Thinking Turbo" },        "moonshot/kimi-k2-turbo": { alias: "Kimi K2 Turbo" },        // moonshot-kimi-k2-aliases:end      },    },  },  models: {    mode: "merge",    providers: {      moonshot: {        baseUrl: "https://api.moonshot.ai/v1",        apiKey: "${MOONSHOT_API_KEY}",        api: "openai-completions",        models: [          // moonshot-kimi-k2-models:start          {            id: "kimi-k2.6",            name: "Kimi K2.6",            reasoning: false,            input: ["text", "image"],            cost: { input: 0.95, output: 4, cacheRead: 0.16, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 262144,          },          {            id: "kimi-k2.5",            name: "Kimi K2.5",            reasoning: false,            input: ["text", "image"],            cost: { input: 0.6, output: 3, cacheRead: 0.1, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 262144,          },          {            id: "kimi-k2-thinking",            name: "Kimi K2 Thinking",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 262144,          },          {            id: "kimi-k2-thinking-turbo",            name: "Kimi K2 Thinking Turbo",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 262144,          },          {            id: "kimi-k2-turbo",            name: "Kimi K2 Turbo",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 256000,            maxTokens: 16384,          },          // moonshot-kimi-k2-models:end        ],      },    },  },}
[/code]

### Kimi Coding

**الأفضل لـ:** المهام المركّزة على الشيفرة عبر نقطة نهاية Kimi Coding.

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice kimi-code-api-key
[/code]

* ### Set a default model

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "kimi/kimi-for-coding" },    },  },}
[/code]

* ### Verify the model is available

bashCopy code
[code]
    openclaw models list --provider kimi
[/code]

### مثال على الإعدادات

json5Copy code
[code]
    {  env: { KIMI_API_KEY: "sk-..." },  agents: {    defaults: {      model: { primary: "kimi/kimi-for-coding" },      models: {        "kimi/kimi-for-coding": { alias: "Kimi" },      },    },  },}
[/code]

## بحث Kimi على الويب

يشحن OpenClaw أيضًا **Kimi** بوصفه مزوّد `web_search`، مدعومًا ببحث الويب من Moonshot.

* ### شغّل إعداد بحث الويب التفاعلي

bashCopy code
[code]
    openclaw configure --section web
[/code]

اختر **Kimi** في قسم بحث الويب لتخزين `plugins.entries.moonshot.config.webSearch.*`.

* ### كوّن منطقة بحث الويب والنموذج

يطلب الإعداد التفاعلي ما يلي:

الإعداد | الخيارات  
---|---  
منطقة API | `https://api.moonshot.ai/v1` (دولي) أو `https://api.moonshot.cn/v1` (الصين)  
نموذج بحث الويب | يكون افتراضيًا `kimi-k2.6`  
  
يوجد التكوين تحت `plugins.entries.moonshot.config.webSearch`:

json5Copy code
[code]
    {  plugins: {    entries: {      moonshot: {        config: {          webSearch: {            apiKey: "sk-...", // or use KIMI_API_KEY / MOONSHOT_API_KEY            baseUrl: "https://api.moonshot.ai/v1",            model: "kimi-k2.6",          },        },      },    },  },  tools: {    web: {      search: {        provider: "kimi",      },    },  },}
[/code]

## التكوين المتقدم

وضع التفكير الأصلي

يدعم Moonshot Kimi التفكير الأصلي الثنائي:

  * `thinking: { type: "enabled" }`
  * `thinking: { type: "disabled" }`


كوّنه لكل نموذج عبر `agents.defaults.models.<provider/model>.params`:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "moonshot/kimi-k2.6": {          params: {            thinking: { type: "disabled" },          },        },      },    },  },}
[/code]

يعيّن OpenClaw أيضًا مستويات `/think` وقت التشغيل لـ Moonshot:

مستوى `/think` | سلوك Moonshot  
---|---  
`/think off` | `thinking.type=disabled`  
أي مستوى غير off | `thinking.type=enabled`  
  
يقبل Kimi K2.6 أيضًا حقل `thinking.keep` اختياريًا يتحكم في الاحتفاظ متعدد الأدوار بـ `reasoning_content`. اضبطه على `"all"` للاحتفاظ بالاستدلال الكامل عبر الأدوار؛ احذفه (أو اتركه `null`) لاستخدام استراتيجية الخادم الافتراضية. يمرّر OpenClaw فقط `thinking.keep` لـ `moonshot/kimi-k2.6` ويزيله من النماذج الأخرى.

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "moonshot/kimi-k2.6": {          params: {            thinking: { type: "enabled", keep: "all" },          },        },      },    },  },}
[/code]

تنقية معرّفات استدعاء الأدوات

يقدّم Moonshot Kimi معرّفات tool_call بالشكل `functions.<name>:<index>`. يحافظ OpenClaw عليها دون تغيير لكي تستمر استدعاءات الأدوات متعددة الأدوار في العمل.

لفرض تنقية صارمة على مزوّد مخصص متوافق مع OpenAI، اضبط `sanitizeToolCallIds: true`:

json5Copy code
[code]
    {  models: {    providers: {      "my-kimi-proxy": {        api: "openai-completions",        sanitizeToolCallIds: true,      },    },  },}
[/code]

توافق استخدام البث

تعلن نقاط نهاية Moonshot الأصلية (`https://api.moonshot.ai/v1` و `https://api.moonshot.cn/v1`) عن توافق استخدام البث على نقل `openai-completions` المشترك. يعتمد OpenClaw في ذلك على إمكانات نقطة النهاية، لذا ترث معرّفات المزوّدين المخصصة المتوافقة التي تستهدف مضيفي Moonshot الأصليين أنفسهم سلوك استخدام البث نفسه.

مع تسعير K2.6 المضمّن، يُحوَّل الاستخدام المتدفق الذي يتضمن رموز الإدخال والإخراج ورموز قراءة ذاكرة التخزين المؤقت أيضًا إلى تكلفة محلية تقديرية بالدولار الأمريكي من أجل `/status` و`/usage full` و`/usage cost` ومحاسبة الجلسات المدعومة بالنصوص المسجلة.

مرجع نقطة النهاية ومرجع النموذج المزوّد | بادئة مرجع النموذج | نقطة النهاية | متغيّر بيئة المصادقة  
---|---|---|---  
Moonshot | `moonshot/` | `https://api.moonshot.ai/v1` | `MOONSHOT_API_KEY`  
Moonshot CN | `moonshot/` | `https://api.moonshot.cn/v1` | `MOONSHOT_API_KEY`  
Kimi Coding | `kimi/` | نقطة نهاية Kimi Coding | `KIMI_API_KEY`  
بحث الويب | غير منطبق | مثل منطقة Moonshot API نفسها | `KIMI_API_KEY` أو `MOONSHOT_API_KEY`  
  
  * يستخدم بحث الويب في Kimi `KIMI_API_KEY` أو `MOONSHOT_API_KEY`، ويستخدم افتراضيًا `https://api.moonshot.ai/v1` مع النموذج `kimi-k2.6`.
  * تجاوز بيانات التسعير وبيانات تعريف السياق في `models.providers` إذا لزم الأمر.
  * إذا نشرت Moonshot حدود سياق مختلفة لنموذج ما، فاضبط `contextWindow` وفقًا لذلك.


## ذو صلة

[**اختيار النموذج** اختيار المزوّدين ومراجع النماذج وسلوك تجاوز الفشل. ](</ar/concepts/model-providers>) [**بحث الويب** تكوين مزوّدي بحث الويب، بما في ذلك Kimi. ](</ar/tools/web>) [**مرجع التكوين** مخطط التكوين الكامل للمزوّدين والنماذج والـ plugins. ](</ar/gateway/configuration-reference>) [**Moonshot Open Platform** إدارة مفتاح Moonshot API ووثائقه. ](<https://platform.moonshot.ai>)

Was this useful?YesNo