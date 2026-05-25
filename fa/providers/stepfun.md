---
title: StepFun
source_url: https://docs.openclaw.ai/fa/providers/stepfun
scraped_at: 2026-05-25
---

OpenClaw شامل یک Plugin ارائه‌دهنده StepFun است که به‌صورت همراه عرضه می‌شود و دو شناسه ارائه‌دهنده دارد:

  * `stepfun` برای endpoint استاندارد
  * `stepfun-plan` برای endpoint Step Plan


## نمای کلی منطقه و endpoint

Endpoint | چین (`.com`) | جهانی (`.ai`)  
---|---|---  
Standard | `https://api.stepfun.com/v1` | `https://api.stepfun.ai/v1`  
Step Plan | `https://api.stepfun.com/step_plan/v1` | `https://api.stepfun.ai/step_plan/v1`  
  
متغیر محیطی احراز هویت: `STEPFUN_API_KEY`

## کاتالوگ داخلی

Standard (`stepfun`):

مدل ref | Context | حداکثر خروجی | یادداشت‌ها  
---|---|---|---  
`stepfun/step-3.5-flash` | 262,144 | 65,536 | مدل استاندارد پیش‌فرض  
  
Step Plan (`stepfun-plan`):

مدل ref | Context | حداکثر خروجی | یادداشت‌ها  
---|---|---|---  
`stepfun-plan/step-3.5-flash` | 262,144 | 65,536 | مدل Step Plan پیش‌فرض  
`stepfun-plan/step-3.5-flash-2603` | 262,144 | 65,536 | مدل اضافی Step Plan  
  
## شروع به کار

سطح ارائه‌دهنده خود را انتخاب کنید و مراحل راه‌اندازی را دنبال کنید.

### Standard

**بهترین گزینه برای:** استفاده عمومی از طریق endpoint استاندارد StepFun.

* ### منطقه endpoint خود را انتخاب کنید

انتخاب احراز هویت | Endpoint | منطقه  
---|---|---  
`stepfun-standard-api-key-intl` | `https://api.stepfun.ai/v1` | بین‌المللی  
`stepfun-standard-api-key-cn` | `https://api.stepfun.com/v1` | چین  
* ### onboarding را اجرا کنید

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-standard-api-key-intl
[/code]

یا برای endpoint چین:

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-standard-api-key-cn
[/code]

* ### جایگزین غیرتعاملی

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-standard-api-key-intl \  --stepfun-api-key "$STEPFUN_API_KEY"
[/code]

* ### در دسترس بودن مدل‌ها را بررسی کنید

bashCopy code
[code]
    openclaw models list --provider stepfun
[/code]

### مدل‌های ref

  * مدل پیش‌فرض: `stepfun/step-3.5-flash`


### Step Plan

**بهترین گزینه برای:** endpoint استدلال Step Plan.

* ### منطقه endpoint خود را انتخاب کنید

انتخاب احراز هویت | Endpoint | منطقه  
---|---|---  
`stepfun-plan-api-key-intl` | `https://api.stepfun.ai/step_plan/v1` | بین‌المللی  
`stepfun-plan-api-key-cn` | `https://api.stepfun.com/step_plan/v1` | چین  
* ### onboarding را اجرا کنید

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-plan-api-key-intl
[/code]

یا برای endpoint چین:

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-plan-api-key-cn
[/code]

* ### جایگزین غیرتعاملی

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-plan-api-key-intl \  --stepfun-api-key "$STEPFUN_API_KEY"
[/code]

* ### در دسترس بودن مدل‌ها را بررسی کنید

bashCopy code
[code]
    openclaw models list --provider stepfun-plan
[/code]

### مدل‌های ref

  * مدل پیش‌فرض: `stepfun-plan/step-3.5-flash`
  * مدل جایگزین: `stepfun-plan/step-3.5-flash-2603`


## پیکربندی پیشرفته

پیکربندی کامل: ارائه‌دهنده Standard json5Copy code
[code]
    {  env: { STEPFUN_API_KEY: "your-key" },  agents: { defaults: { model: { primary: "stepfun/step-3.5-flash" } } },  models: {    mode: "merge",    providers: {      stepfun: {        baseUrl: "https://api.stepfun.ai/v1",        api: "openai-completions",        apiKey: "${STEPFUN_API_KEY}",        models: [          {            id: "step-3.5-flash",            name: "Step 3.5 Flash",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 65536,          },        ],      },    },  },}
[/code]

پیکربندی کامل: ارائه‌دهنده Step Plan json5Copy code
[code]
    {  env: { STEPFUN_API_KEY: "your-key" },  agents: { defaults: { model: { primary: "stepfun-plan/step-3.5-flash" } } },  models: {    mode: "merge",    providers: {      "stepfun-plan": {        baseUrl: "https://api.stepfun.ai/step_plan/v1",        api: "openai-completions",        apiKey: "${STEPFUN_API_KEY}",        models: [          {            id: "step-3.5-flash",            name: "Step 3.5 Flash",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 65536,          },          {            id: "step-3.5-flash-2603",            name: "Step 3.5 Flash 2603",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 65536,          },        ],      },    },  },}
[/code]

یادداشت‌ها

  * این ارائه‌دهنده همراه OpenClaw عرضه می‌شود، بنابراین مرحله نصب Plugin جداگانه‌ای ندارد.
  * `step-3.5-flash-2603` در حال حاضر فقط روی `stepfun-plan` ارائه می‌شود.
  * یک جریان احراز هویت واحد، پروفایل‌های همسان با منطقه را برای هر دو `stepfun` و `stepfun-plan` می‌نویسد، بنابراین هر دو سطح می‌توانند با هم کشف شوند.
  * از `openclaw models list` و `openclaw models set <provider/model>` برای بررسی یا تغییر مدل‌ها استفاده کنید.


## مرتبط

[**انتخاب مدل** نمای کلی همه ارائه‌دهنده‌ها، مدل‌های ref، و رفتار failover. ](</fa/concepts/model-providers>) [**مرجع پیکربندی** طرح‌واره کامل پیکربندی برای ارائه‌دهنده‌ها، مدل‌ها، و Pluginها. ](</fa/gateway/configuration-reference>) [**انتخاب مدل** نحوه انتخاب و پیکربندی مدل‌ها. ](</fa/concepts/models>) [**پلتفرم StepFun** مدیریت کلید API و مستندات StepFun. ](<https://platform.stepfun.com>)

Was this useful?YesNo