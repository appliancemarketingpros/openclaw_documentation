---
title: Arcee AI
source_url: https://docs.openclaw.ai/ru/providers/arcee
scraped_at: 2026-06-29
---

ModelsProviders

[Arcee AI](<https://arcee.ai>) предоставляет доступ к семейству моделей Trinity на основе mixture-of-experts через OpenAI-совместимый API. Все модели Trinity лицензированы по Apache 2.0.

К моделям Arcee AI можно обращаться напрямую через платформу Arcee или через [OpenRouter](</ru/providers/openrouter>).

Свойство | Значение  
---|---  
Поставщик | `arcee`  
Аутентификация | `ARCEEAI_API_KEY` (напрямую) или `OPENROUTER_API_KEY` (через OpenRouter)  
API | OpenAI-совместимый  
Базовый URL | `https://api.arcee.ai/api/v1` (напрямую) или `https://openrouter.ai/api/v1` (OpenRouter)  
  
## Установка Plugin

Установите официальный Plugin, затем перезапустите Gateway:

bashCopy code
[code]
    openclaw plugins install @openclaw/arcee-provideropenclaw gateway restart
[/code]

## Начало работы

### Напрямую (платформа Arcee)

* ### Получите ключ API

Создайте ключ API в [Arcee AI](<https://chat.arcee.ai/>).

* ### Запустите онбординг

bashCopy code
[code]
    openclaw onboard --auth-choice arceeai-api-key
[/code]

* ### Задайте модель по умолчанию

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "arcee/trinity-large-thinking" },    },  },}
[/code]

### Через OpenRouter

* ### Получите ключ API

Создайте ключ API в [OpenRouter](<https://openrouter.ai/keys>).

* ### Запустите онбординг

bashCopy code
[code]
    openclaw onboard --auth-choice arceeai-openrouter
[/code]

* ### Задайте модель по умолчанию

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "arcee/trinity-large-thinking" },    },  },}
[/code]

Те же ссылки на модели работают как для прямой настройки, так и для настройки через OpenRouter (например, `arcee/trinity-large-thinking`).

## Неинтерактивная настройка

### Напрямую (платформа Arcee)

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice arceeai-api-key \  --arceeai-api-key "$ARCEEAI_API_KEY"
[/code]

### Через OpenRouter

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice arceeai-openrouter \  --openrouter-api-key "$OPENROUTER_API_KEY"
[/code]

## Встроенный каталог

В настоящее время OpenClaw поставляется со следующим статическим каталогом Arcee:

Ссылка на модель | Название | Ввод | Контекст | Стоимость (ввод/вывод за 1 млн) | Примечания  
---|---|---|---|---|---  
`arcee/trinity-large-thinking` | Trinity Large Thinking | text | 256K | $0.25 / $0.90 | Модель по умолчанию; reasoning включен  
`arcee/trinity-large-preview` | Trinity Large Preview | text | 128K | $0.25 / $1.00 | Универсальная; 400B параметров, 13B активных  
`arcee/trinity-mini` | Trinity Mini 26B | text | 128K | $0.045 / $0.15 | Быстрая и экономичная; вызов функций  
  
## Поддерживаемые возможности

Возможность | Поддерживается  
---|---  
Потоковая передача | Да  
Использование инструментов / вызов функций | Да (Trinity Mini, Trinity Large Preview)  
Структурированный вывод (режим JSON и схема JSON) | Да  
Расширенное мышление | Да (Trinity Large Thinking; инструменты отключены)  
  
Примечание об окружении

Если Gateway работает как демон (launchd/systemd), убедитесь, что `ARCEEAI_API_KEY` (или `OPENROUTER_API_KEY`) доступен этому процессу (например, в `~/.openclaw/.env` или через `env.shellEnv`).

Маршрутизация OpenRouter

При использовании моделей Arcee через OpenRouter применяются те же ссылки на модели `arcee/*`. OpenClaw прозрачно обрабатывает маршрутизацию на основе выбранного способа аутентификации. Подробнее о настройке, специфичной для OpenRouter, см. в [документации поставщика OpenRouter](</ru/providers/openrouter>).

## Связанные материалы

[**OpenRouter** Доступ к моделям Arcee и многим другим через один ключ API. ](</ru/providers/openrouter>) [**Выбор модели** Выбор поставщиков, ссылок на модели и поведения при отказе. ](</ru/concepts/model-providers>)

Was this useful?YesNo

Open issue