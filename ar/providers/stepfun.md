---
title: StepFun
source_url: https://docs.openclaw.ai/ar/providers/stepfun
scraped_at: 2026-05-25
---

OpenClaw يتضمن Plugin موفر StepFun مضمنا مع معرفي موفر:

  * `stepfun` لنقطة النهاية القياسية
  * `stepfun-plan` لنقطة نهاية Step Plan


## نظرة عامة على المنطقة ونقطة النهاية

نقطة النهاية | الصين (`.com`) | عالمي (`.ai`)  
---|---|---  
قياسي | `https://api.stepfun.com/v1` | `https://api.stepfun.ai/v1`  
Step Plan | `https://api.stepfun.com/step_plan/v1` | `https://api.stepfun.ai/step_plan/v1`  
  
متغير بيئة المصادقة: `STEPFUN_API_KEY`

## الكتالوج المضمن

قياسي (`stepfun`):

مرجع النموذج | السياق | الحد الأقصى للإخراج | ملاحظات  
---|---|---|---  
`stepfun/step-3.5-flash` | 262,144 | 65,536 | النموذج القياسي الافتراضي  
  
Step Plan (`stepfun-plan`):

مرجع النموذج | السياق | الحد الأقصى للإخراج | ملاحظات  
---|---|---|---  
`stepfun-plan/step-3.5-flash` | 262,144 | 65,536 | نموذج Step Plan الافتراضي  
`stepfun-plan/step-3.5-flash-2603` | 262,144 | 65,536 | نموذج Step Plan إضافي  
  
## البدء

اختر سطح الموفر واتبع خطوات الإعداد.

### Standard

**الأفضل لـ:** الاستخدام العام عبر نقطة نهاية StepFun القياسية.

* ### Choose your endpoint region

خيار المصادقة | نقطة النهاية | المنطقة  
---|---|---  
`stepfun-standard-api-key-intl` | `https://api.stepfun.ai/v1` | دولية  
`stepfun-standard-api-key-cn` | `https://api.stepfun.com/v1` | الصين  
* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-standard-api-key-intl
[/code]

أو لنقطة نهاية الصين:

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-standard-api-key-cn
[/code]

* ### Non-interactive alternative

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-standard-api-key-intl \  --stepfun-api-key "$STEPFUN_API_KEY"
[/code]

* ### Verify models are available

bashCopy code
[code]
    openclaw models list --provider stepfun
[/code]

### مراجع النماذج

  * النموذج الافتراضي: `stepfun/step-3.5-flash`


### Step Plan

**الأفضل لـ:** نقطة نهاية الاستدلال Step Plan.

* ### Choose your endpoint region

خيار المصادقة | نقطة النهاية | المنطقة  
---|---|---  
`stepfun-plan-api-key-intl` | `https://api.stepfun.ai/step_plan/v1` | دولية  
`stepfun-plan-api-key-cn` | `https://api.stepfun.com/step_plan/v1` | الصين  
* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-plan-api-key-intl
[/code]

أو لنقطة نهاية الصين:

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-plan-api-key-cn
[/code]

* ### Non-interactive alternative

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-plan-api-key-intl \  --stepfun-api-key "$STEPFUN_API_KEY"
[/code]

* ### Verify models are available

bashCopy code
[code]
    openclaw models list --provider stepfun-plan
[/code]

### مراجع النماذج

  * النموذج الافتراضي: `stepfun-plan/step-3.5-flash`
  * النموذج البديل: `stepfun-plan/step-3.5-flash-2603`


## الإعدادات المتقدمة

Full config: Standard provider json5Copy code
[code]
    {  env: { STEPFUN_API_KEY: "your-key" },  agents: { defaults: { model: { primary: "stepfun/step-3.5-flash" } } },  models: {    mode: "merge",    providers: {      stepfun: {        baseUrl: "https://api.stepfun.ai/v1",        api: "openai-completions",        apiKey: "${STEPFUN_API_KEY}",        models: [          {            id: "step-3.5-flash",            name: "Step 3.5 Flash",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 65536,          },        ],      },    },  },}
[/code]

Full config: Step Plan provider json5Copy code
[code]
    {  env: { STEPFUN_API_KEY: "your-key" },  agents: { defaults: { model: { primary: "stepfun-plan/step-3.5-flash" } } },  models: {    mode: "merge",    providers: {      "stepfun-plan": {        baseUrl: "https://api.stepfun.ai/step_plan/v1",        api: "openai-completions",        apiKey: "${STEPFUN_API_KEY}",        models: [          {            id: "step-3.5-flash",            name: "Step 3.5 Flash",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 65536,          },          {            id: "step-3.5-flash-2603",            name: "Step 3.5 Flash 2603",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 65536,          },        ],      },    },  },}
[/code]

Notes

  * الموفر مضمن مع OpenClaw، لذلك لا توجد خطوة تثبيت Plugin منفصلة.
  * `step-3.5-flash-2603` متاح حاليا فقط على `stepfun-plan`.
  * يكتب مسار مصادقة واحد ملفات تعريف مطابقة للمنطقة لكل من `stepfun` و`stepfun-plan`، لذلك يمكن اكتشاف السطحين معا.
  * استخدم `openclaw models list` و`openclaw models set <provider/model>` لفحص النماذج أو تبديلها.


## ذات صلة

[**Model selection** نظرة عامة على جميع الموفرين ومراجع النماذج وسلوك تجاوز الفشل. ](</ar/concepts/model-providers>) [**Configuration reference** مخطط الإعدادات الكامل للموفرين والنماذج والـ plugins. ](</ar/gateway/configuration-reference>) [**Model selection** كيفية اختيار النماذج وإعدادها. ](</ar/concepts/models>) [**StepFun Platform** إدارة مفتاح API الخاص بـ StepFun والوثائق. ](<https://platform.stepfun.com>)

Was this useful?YesNo