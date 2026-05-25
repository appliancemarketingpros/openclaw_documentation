---
title: StepFun
source_url: https://docs.openclaw.ai/uk/providers/stepfun
scraped_at: 2026-05-25
---

OpenClaw містить вбудований Plugin провайдера StepFun із двома ідентифікаторами провайдера:

  * `stepfun` для стандартного endpoint
  * `stepfun-plan` для endpoint Step Plan


## Огляд регіонів і endpoint

Endpoint | China (`.com`) | Global (`.ai`)  
---|---|---  
Standard | `https://api.stepfun.com/v1` | `https://api.stepfun.ai/v1`  
Step Plan | `https://api.stepfun.com/step_plan/v1` | `https://api.stepfun.ai/step_plan/v1`  
  
Змінна середовища для автентифікації: `STEPFUN_API_KEY`

## Вбудований каталог

Standard (`stepfun`):

Посилання на модель | Контекст | Макс. вивід | Примітки  
---|---|---|---  
`stepfun/step-3.5-flash` | 262,144 | 65,536 | Стандартна модель за замовчуванням  
  
Step Plan (`stepfun-plan`):

Посилання на модель | Контекст | Макс. вивід | Примітки  
---|---|---|---  
`stepfun-plan/step-3.5-flash` | 262,144 | 65,536 | Модель Step Plan за замовчуванням  
`stepfun-plan/step-3.5-flash-2603` | 262,144 | 65,536 | Додаткова модель Step Plan  
  
## Початок роботи

Виберіть поверхню провайдера й виконайте кроки налаштування.

### Standard

**Найкраще для:** загального використання через стандартний endpoint StepFun.

* ### Choose your endpoint region

Вибір автентифікації | Endpoint | Регіон  
---|---|---  
`stepfun-standard-api-key-intl` | `https://api.stepfun.ai/v1` | Міжнародний  
`stepfun-standard-api-key-cn` | `https://api.stepfun.com/v1` | China  
* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-standard-api-key-intl
[/code]

Або для endpoint China:

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

### Посилання на моделі

  * Модель за замовчуванням: `stepfun/step-3.5-flash`


### Step Plan

**Найкраще для:** endpoint міркування Step Plan.

* ### Choose your endpoint region

Вибір автентифікації | Endpoint | Регіон  
---|---|---  
`stepfun-plan-api-key-intl` | `https://api.stepfun.ai/step_plan/v1` | Міжнародний  
`stepfun-plan-api-key-cn` | `https://api.stepfun.com/step_plan/v1` | China  
* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-plan-api-key-intl
[/code]

Або для endpoint China:

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

### Посилання на моделі

  * Модель за замовчуванням: `stepfun-plan/step-3.5-flash`
  * Альтернативна модель: `stepfun-plan/step-3.5-flash-2603`


## Розширена конфігурація

Full config: Standard provider json5Copy code
[code]
    {  env: { STEPFUN_API_KEY: "your-key" },  agents: { defaults: { model: { primary: "stepfun/step-3.5-flash" } } },  models: {    mode: "merge",    providers: {      stepfun: {        baseUrl: "https://api.stepfun.ai/v1",        api: "openai-completions",        apiKey: "${STEPFUN_API_KEY}",        models: [          {            id: "step-3.5-flash",            name: "Step 3.5 Flash",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 65536,          },        ],      },    },  },}
[/code]

Full config: Step Plan provider json5Copy code
[code]
    {  env: { STEPFUN_API_KEY: "your-key" },  agents: { defaults: { model: { primary: "stepfun-plan/step-3.5-flash" } } },  models: {    mode: "merge",    providers: {      "stepfun-plan": {        baseUrl: "https://api.stepfun.ai/step_plan/v1",        api: "openai-completions",        apiKey: "${STEPFUN_API_KEY}",        models: [          {            id: "step-3.5-flash",            name: "Step 3.5 Flash",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 65536,          },          {            id: "step-3.5-flash-2603",            name: "Step 3.5 Flash 2603",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 65536,          },        ],      },    },  },}
[/code]

Notes

  * Провайдер постачається разом з OpenClaw, тому окремий крок установлення Plugin не потрібен.
  * `step-3.5-flash-2603` зараз доступна лише в `stepfun-plan`.
  * Єдиний потік автентифікації записує профілі, що відповідають регіону, для `stepfun` і `stepfun-plan`, тому обидві поверхні можна виявити разом.
  * Використовуйте `openclaw models list` і `openclaw models set <provider/model>`, щоб переглядати або перемикати моделі.


## Пов’язане

[**Model selection** Огляд усіх провайдерів, посилань на моделі та поведінки failover. ](</uk/concepts/model-providers>) [**Configuration reference** Повна схема конфігурації для провайдерів, моделей і plugins. ](</uk/gateway/configuration-reference>) [**Model selection** Як вибирати й налаштовувати моделі. ](</uk/concepts/models>) [**StepFun Platform** Керування ключами API StepFun і документація. ](<https://platform.stepfun.com>)

Was this useful?YesNo