---
title: Z.AI
source_url: https://docs.openclaw.ai/ru/providers/zai
scraped_at: 2026-06-29
---

ModelsProviders

Z.AI — это API-платформа для моделей **GLM**. Она предоставляет REST API для GLM и использует ключи API для аутентификации. Создайте ключ API в консоли Z.AI. OpenClaw использует провайдера `zai` с ключом API Z.AI.

Свойство | Значение  
---|---  
Провайдер | `zai`  
Пакет | `@openclaw/zai-provider`  
Аутентификация | `ZAI_API_KEY` (устаревший псевдоним: `Z_AI_API_KEY`)  
API | Chat Completions Z.AI (аутентификация Bearer)  
  
## Модели GLM

GLM — это семейство моделей, а не отдельный провайдер. В OpenClaw модели GLM используют ссылки, такие как `zai/glm-5.2`: провайдер `zai`, идентификатор модели `glm-5.2`.

## Начало работы

Сначала установите Plugin провайдера:

bashCopy code
[code]
    openclaw plugins install @openclaw/zai-provider
[/code]

### Автоопределение конечной точки

**Лучше всего подходит для:** большинства пользователей. OpenClaw проверяет поддерживаемые конечные точки Z.AI с вашим ключом API и автоматически применяет правильный базовый URL.

* ### Запустите онбординг

bashCopy code
[code]
    openclaw onboard --auth-choice zai-api-key
[/code]

* ### Проверьте, что модель есть в списке

bashCopy code
[code]
    openclaw models list --all --provider zai
[/code]

### Явная региональная конечная точка

**Лучше всего подходит для:** пользователей, которые хотят принудительно выбрать конкретный Coding Plan или общий интерфейс API.

* ### Выберите правильный вариант онбординга

bashCopy code
[code]
    # Coding Plan Global (recommended for Coding Plan users)openclaw onboard --auth-choice zai-coding-global # Coding Plan CN (China region)openclaw onboard --auth-choice zai-coding-cn # General APIopenclaw onboard --auth-choice zai-global # General API CN (China region)openclaw onboard --auth-choice zai-cn
[/code]

* ### Проверьте, что модель есть в списке

bashCopy code
[code]
    openclaw models list --all --provider zai
[/code]

## Пример конфигурации

json5Copy code
[code]
    {  env: { ZAI_API_KEY: "sk-..." },  models: {    providers: {      zai: {        // GLM-5.2 uses the Coding Plan endpoint.        baseUrl: "https://api.z.ai/api/coding/paas/v4",      },    },  },  agents: { defaults: { model: { primary: "zai/glm-5.2" } } },}
[/code]

## Встроенный каталог

Plugin провайдера `zai` поставляет свой каталог в манифесте Plugin, поэтому список для чтения может показывать известные строки GLM без загрузки среды выполнения провайдера:

bashCopy code
[code]
    openclaw models list --all --provider zai
[/code]

Каталог на основе манифеста сейчас включает:

Ссылка модели | Примечания  
---|---  
`zai/glm-5.2` | Значение по умолчанию для Coding Plan; контекст 1M  
`zai/glm-5.1` | Значение по умолчанию для общего API  
`zai/glm-5` |   
`zai/glm-5-turbo` |   
`zai/glm-5v-turbo` |   
`zai/glm-4.7` |   
`zai/glm-4.7-flash` |   
`zai/glm-4.7-flashx` |   
`zai/glm-4.6` |   
`zai/glm-4.6v` |   
`zai/glm-4.5` |   
`zai/glm-4.5-air` |   
`zai/glm-4.5-flash` |   
`zai/glm-4.5v` |   
  
## Расширенная конфигурация

Прямое разрешение неизвестных моделей GLM-5

Неизвестные идентификаторы `glm-5*` все равно прямо разрешаются на пути провайдера путем синтеза метаданных, принадлежащих провайдеру, из шаблона `glm-4.7`, когда идентификатор соответствует текущей форме семейства GLM-5.

Потоковая передача вызовов инструментов

`tool_stream` включен по умолчанию для потоковой передачи вызовов инструментов Z.AI. Чтобы отключить его:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "zai/<model>": {          params: { tool_stream: false },        },      },    },  },}
[/code]

Мышление и сохраненное мышление

Мышление Z.AI следует элементам управления `/think` в OpenClaw. При отключенном мышлении OpenClaw отправляет `thinking: { type: "disabled" }`, чтобы избежать ответов, которые тратят бюджет вывода на `reasoning_content` до видимого текста.

Сохраненное мышление включается явно, потому что Z.AI требует повторной передачи полного исторического `reasoning_content`, что увеличивает количество токенов промпта. Включите его для каждой модели:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "zai/glm-5.2": {          params: { preserveThinking: true },        },      },    },  },}
[/code]

Когда оно включено и мышление активно, OpenClaw отправляет `thinking: { type: "enabled", clear_thinking: false }` и повторно передает предыдущий `reasoning_content` для той же совместимой с OpenAI стенограммы.

Опытные пользователи по-прежнему могут переопределить точную полезную нагрузку провайдера с помощью `params.extra_body.thinking`.

Понимание изображений

Plugin Z.AI регистрирует понимание изображений.

Свойство | Значение  
---|---  
Модель | `glm-4.6v`  
  
Понимание изображений автоматически разрешается из настроенной аутентификации Z.AI — дополнительная конфигурация не нужна.

Сведения об аутентификации

  * Z.AI использует аутентификацию Bearer с вашим ключом API.
  * Вариант онбординга `zai-api-key` автоматически определяет соответствующую конечную точку Z.AI, проверяя поддерживаемые конечные точки с вашим ключом.
  * Используйте явные региональные варианты (`zai-coding-global`, `zai-coding-cn`, `zai-global`, `zai-cn`), когда хотите принудительно выбрать конкретный интерфейс API.
  * Устаревшая переменная окружения `Z_AI_API_KEY` все еще принимается; OpenClaw копирует ее в `ZAI_API_KEY` при запуске, если `ZAI_API_KEY` не задана.


## Связанные материалы

[**Выбор модели** Выбор провайдеров, ссылок моделей и поведения при отказе. ](</ru/concepts/model-providers>) [**Справочник по конфигурации** Полная схема конфигурации OpenClaw, включая настройки провайдера и модели. ](</ru/gateway/configuration-reference>)

Was this useful?YesNo

Open issue