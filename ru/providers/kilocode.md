---
title: Kilo Gateway
source_url: https://docs.openclaw.ai/ru/providers/kilocode
scraped_at: 2026-06-29
---

ModelsProviders

Kilo Gateway предоставляет **единый API** , который маршрутизирует запросы ко многим моделям через одну конечную точку и API-ключ. Он совместим с OpenAI, поэтому большинство OpenAI SDK работают после смены базового URL.

Свойство | Значение  
---|---  
Провайдер | `kilocode`  
Авторизация | `KILOCODE_API_KEY`  
API | Совместимый с OpenAI  
Базовый URL | `https://api.kilo.ai/api/gateway/`  
  
## Установка Plugin

Установите официальный Plugin, затем перезапустите Gateway:

bashCopy code
[code]
    openclaw plugins install @openclaw/kilocode-provideropenclaw gateway restart
[/code]

## Начало работы

* ### Создайте учетную запись

Перейдите на [app.kilo.ai](<https://app.kilo.ai>), войдите или создайте учетную запись, затем откройте API Keys и сгенерируйте новый ключ.

* ### Запустите онбординг

bashCopy code
[code]
    openclaw onboard --auth-choice kilocode-api-key
[/code]

Или задайте переменную окружения напрямую:

bashCopy code
[code]
    export KILOCODE_API_KEY="<your-kilocode-api-key>" # pragma: allowlist secret
[/code]

* ### Проверьте, что модель доступна

bashCopy code
[code]
    openclaw models list --provider kilocode
[/code]

## Модель по умолчанию

Модель по умолчанию — `kilocode/kilo/auto`, принадлежащая провайдеру модель интеллектуальной маршрутизации, управляемая Kilo Gateway.

## Встроенный каталог

OpenClaw динамически обнаруживает доступные модели из Kilo Gateway при запуске. Используйте `/models kilocode`, чтобы увидеть полный список моделей, доступных для вашей учетной записи.

Любую модель, доступную в Gateway, можно использовать с префиксом `kilocode/`:

Ссылка на модель | Примечания  
---|---  
`kilocode/kilo/auto` | По умолчанию — интеллектуальная маршрутизация  
`kilocode/anthropic/claude-sonnet-4` | Anthropic через Kilo  
`kilocode/openai/gpt-5.5` | OpenAI через Kilo  
`kilocode/google/gemini-3.1-pro-preview` | Google через Kilo  
...и многие другие | Используйте `/models kilocode`, чтобы вывести все  
  
## Пример конфигурации

json5Copy code
[code]
    {  env: { KILOCODE_API_KEY: "<your-kilocode-api-key>" }, // pragma: allowlist secret  agents: {    defaults: {      model: { primary: "kilocode/kilo/auto" },    },  },}
[/code]

Транспорт и совместимость

Kilo Gateway задокументирован в исходном коде как совместимый с OpenRouter, поэтому он остается на прокси-пути, совместимом с OpenAI, а не использует нативное формирование запросов OpenAI.

  * Ссылки Kilo на базе Gemini остаются на прокси-пути Gemini, поэтому OpenClaw сохраняет там очистку thought-signature Gemini без включения нативной проверки воспроизведения Gemini или перезаписей начальной загрузки.
  * Kilo Gateway использует токен Bearer с вашим API-ключом внутри.

Обертка потока и reasoning

Общая обертка потока Kilo добавляет заголовок приложения провайдера и нормализует прокси-полезные нагрузки reasoning для поддерживаемых конкретных ссылок на модели.

Устранение неполадок

  * Если обнаружение моделей при запуске не удается, OpenClaw возвращается к статическому каталогу, содержащему `kilocode/kilo/auto`.
  * Убедитесь, что ваш API-ключ действителен и что в вашей учетной записи Kilo включены нужные модели.
  * Когда Gateway работает как daemon, убедитесь, что `KILOCODE_API_KEY` доступен этому процессу (например, в `~/.openclaw/.env` или через `env.shellEnv`).


## Связанные материалы

[**Выбор модели** Выбор провайдеров, ссылок на модели и поведения failover. ](</ru/concepts/model-providers>) [**Справочник по конфигурации** Полный справочник по конфигурации OpenClaw. ](</ru/gateway/configuration-reference>) [**Kilo Gateway** Панель управления Kilo Gateway, API-ключи и управление учетной записью. ](<https://app.kilo.ai>)

Was this useful?YesNo

Open issue