---
title: StepFun
source_url: https://docs.openclaw.ai/ru/providers/stepfun
scraped_at: 2026-06-29
---

ModelsProviders

Plugin провайдера StepFun поддерживает два идентификатора провайдера:

  * `stepfun` для стандартного эндпоинта
  * `stepfun-plan` для эндпоинта Step Plan


## Установка Plugin

Установите официальный Plugin, затем перезапустите Gateway:

bashCopy code
[code]
    openclaw plugins install @openclaw/stepfun-provideropenclaw gateway restart
[/code]

## Обзор регионов и эндпоинтов

Эндпоинт | Китай (`.com`) | Глобальный (`.ai`)  
---|---|---  
Стандартный | `https://api.stepfun.com/v1` | `https://api.stepfun.ai/v1`  
Step Plan | `https://api.stepfun.com/step_plan/v1` | `https://api.stepfun.ai/step_plan/v1`  
  
Переменная окружения для аутентификации: `STEPFUN_API_KEY`

## Встроенный каталог

Стандартный (`stepfun`):

Ссылка на модель | Контекст | Макс. вывод | Примечания  
---|---|---|---  
`stepfun/step-3.5-flash` | 262,144 | 65,536 | Стандартная модель по умолчанию  
  
Step Plan (`stepfun-plan`):

Ссылка на модель | Контекст | Макс. вывод | Примечания  
---|---|---|---  
`stepfun-plan/step-3.5-flash` | 262,144 | 65,536 | Модель Step Plan по умолчанию  
`stepfun-plan/step-3.5-flash-2603` | 262,144 | 65,536 | Дополнительная модель Step Plan  
  
## Начало работы

Выберите поверхность провайдера и выполните шаги настройки.

### Стандартный

**Лучше всего подходит для:** универсального использования через стандартный эндпоинт StepFun.

* ### Выберите регион эндпоинта

Вариант аутентификации | Эндпоинт | Регион  
---|---|---  
`stepfun-standard-api-key-intl` | `https://api.stepfun.ai/v1` | Международный  
`stepfun-standard-api-key-cn` | `https://api.stepfun.com/v1` | Китай  
  
* ### Запустите первичную настройку

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-standard-api-key-intl
[/code]

Или для эндпоинта в Китае:

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-standard-api-key-cn
[/code]

* ### Неинтерактивная альтернатива

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-standard-api-key-intl \  --stepfun-api-key "$STEPFUN_API_KEY"
[/code]

* ### Проверьте, что модели доступны

bashCopy code
[code]
    openclaw models list --provider stepfun
[/code]

### Ссылки на модели

  * Модель по умолчанию: `stepfun/step-3.5-flash`


### Step Plan

**Лучше всего подходит для:** эндпоинта рассуждений Step Plan.

* ### Выберите регион эндпоинта

Вариант аутентификации | Эндпоинт | Регион  
---|---|---  
`stepfun-plan-api-key-intl` | `https://api.stepfun.ai/step_plan/v1` | Международный  
`stepfun-plan-api-key-cn` | `https://api.stepfun.com/step_plan/v1` | Китай  
  
* ### Запустите первичную настройку

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-plan-api-key-intl
[/code]

Или для эндпоинта в Китае:

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-plan-api-key-cn
[/code]

* ### Неинтерактивная альтернатива

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-plan-api-key-intl \  --stepfun-api-key "$STEPFUN_API_KEY"
[/code]

* ### Проверьте, что модели доступны

bashCopy code
[code]
    openclaw models list --provider stepfun-plan
[/code]

### Ссылки на модели

  * Модель по умолчанию: `stepfun-plan/step-3.5-flash`
  * Альтернативная модель: `stepfun-plan/step-3.5-flash-2603`


## Расширенная конфигурация

Полная конфигурация: стандартный провайдер json5Copy code
[code]
    {  env: { STEPFUN_API_KEY: "your-key" },  agents: { defaults: { model: { primary: "stepfun/step-3.5-flash" } } },  models: {    mode: "merge",    providers: {      stepfun: {        baseUrl: "https://api.stepfun.ai/v1",        api: "openai-completions",        apiKey: "${STEPFUN_API_KEY}",        models: [          {            id: "step-3.5-flash",            name: "Step 3.5 Flash",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 65536,          },        ],      },    },  },}
[/code]

Полная конфигурация: провайдер Step Plan json5Copy code
[code]
    {  env: { STEPFUN_API_KEY: "your-key" },  agents: { defaults: { model: { primary: "stepfun-plan/step-3.5-flash" } } },  models: {    mode: "merge",    providers: {      "stepfun-plan": {        baseUrl: "https://api.stepfun.ai/step_plan/v1",        api: "openai-completions",        apiKey: "${STEPFUN_API_KEY}",        models: [          {            id: "step-3.5-flash",            name: "Step 3.5 Flash",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 65536,          },          {            id: "step-3.5-flash-2603",            name: "Step 3.5 Flash 2603",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 65536,          },        ],      },    },  },}
[/code]

Примечания

  * Провайдер является официальным внешним пакетом; установите его перед настройкой.
  * `step-3.5-flash-2603` сейчас доступна только в `stepfun-plan`.
  * Единый поток аутентификации записывает профили, соответствующие региону, как для `stepfun`, так и для `stepfun-plan`, поэтому обе поверхности можно обнаружить вместе.
  * Используйте `openclaw models list` и `openclaw models set <provider/model>`, чтобы просмотреть или переключить модели.


## Связанные разделы

[**Выбор модели** Обзор всех провайдеров, ссылок на модели и поведения при отказе. ](</ru/concepts/model-providers>) [**Справочник по конфигурации** Полная схема конфигурации для провайдеров, моделей и plugins. ](</ru/gateway/configuration-reference>) [**Выбор модели** Как выбирать и настраивать модели. ](</ru/concepts/models>) [**Платформа StepFun** Управление ключами API StepFun и документация. ](<https://platform.stepfun.com>)

Was this useful?YesNo

Open issue