---
title: Злітна смуга
source_url: https://docs.openclaw.ai/uk/providers/runway
scraped_at: 2026-05-25
---

OpenClaw постачається з вбудованим провайдером `runway` для хостингової генерації відео. Plugin увімкнено за замовчуванням, і він реєструє провайдер `runway` для контракту `videoGenerationProviders`.

Властивість | Значення  
---|---  
Ідентифікатор провайдера | `runway`  
Plugin | вбудований, `enabledByDefault: true`  
Змінні середовища автентифікації | `RUNWAYML_API_SECRET` (канонічна) або `RUNWAY_API_KEY`  
Прапорець онбордингу | `--auth-choice runway-api-key`  
Прямий прапорець CLI | `--runway-api-key <key>`  
API | генерація відео Runway на основі завдань (опитування `GET /v1/tasks/{id}`)  
Модель за замовчуванням | `runway/gen4.5`  
  
## Початок роботи

* ### Set the API key

bashCopy code
[code]
    openclaw onboard --auth-choice runway-api-key
[/code]

* ### Set Runway as the default video provider

bashCopy code
[code]
    openclaw config set agents.defaults.videoGenerationModel.primary "runway/gen4.5"
[/code]

* ### Generate a video

Попросіть агента згенерувати відео. Runway буде використано автоматично.

## Підтримувані режими та моделі

Провайдер надає сім моделей Runway, розподілених між трьома режимами. Той самий ідентифікатор моделі може обслуговувати більше ніж один режим (наприклад, `gen4.5` працює як для перетворення тексту на відео, так і для перетворення зображення на відео).

Режим | Моделі | Вхідні еталонні дані  
---|---|---  
Текст у відео | `gen4.5` (за замовчуванням), `veo3.1`, `veo3.1_fast`, `veo3` | Немає  
Зображення у відео | `gen4.5`, `gen4_turbo`, `gen3a_turbo`, `veo3.1`, `veo3.1_fast`, `veo3` | 1 локальне або віддалене зображення  
Відео у відео | `gen4_aleph` | 1 локальне або віддалене відео  
  
Локальні посилання на зображення та відео підтримуються через URI даних.

Співвідношення сторін | Дозволені значення  
---|---  
Текст у відео | `16:9`, `9:16`  
Редагування зображень і відео | `1:1`, `16:9`, `9:16`, `3:4`, `4:3`, `21:9`  
  
## Конфігурація

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "runway/gen4.5",      },    },  },}
[/code]

## Розширена конфігурація

Environment variable aliases

OpenClaw розпізнає як `RUNWAYML_API_SECRET` (канонічну), так і `RUNWAY_API_KEY`. Будь-яка з цих змінних автентифікує провайдер Runway.

Task polling

Runway використовує API на основі завдань. Після надсилання запиту на генерацію OpenClaw опитує `GET /v1/tasks/{id}`, доки відео не буде готове. Для поведінки опитування не потрібна додаткова конфігурація.

## Пов’язане

[**Video generation** Спільні параметри інструмента, вибір провайдера та асинхронна поведінка. ](</uk/tools/video-generation>) [**Configuration reference** Параметри агента за замовчуванням, зокрема модель генерації відео. ](</uk/gateway/config-agents#agent-defaults>)

Was this useful?YesNo