---
title: Cohere
source_url: https://docs.openclaw.ai/ru/providers/cohere
scraped_at: 2026-06-29
---

ModelsProviders

[Cohere](<https://cohere.com>) предоставляет OpenAI-совместимый инференс через свой Compatibility API. OpenClaw поставляет провайдер Cohere во время перехода к внешнему пакету, а также публикует его как официальный внешний Plugin с каталогом моделей Command A.

Свойство | Значение  
---|---  
Идентификатор провайдера | `cohere`  
Plugin | встроен на время перехода; официальный внешний пакет  
Переменная окружения для аутентификации | `COHERE_API_KEY`  
Флаг онбординга | `--auth-choice cohere-api-key`  
Прямой флаг CLI | `--cohere-api-key <key>`  
API | OpenAI-совместимый (`openai-completions`)  
Базовый URL | `https://api.cohere.ai/compatibility/v1`  
Модель по умолчанию | `cohere/command-a-03-2025`  
  
## Начало работы

  1. Cohere включен в текущие пакеты OpenClaw. Если он недоступен, установите внешний пакет и перезапустите Gateway:

bashCopy code
[code]
    openclaw plugins install @openclaw/cohere-provideropenclaw gateway restart
[/code]

  2. Создайте ключ API Cohere.
  3. Запустите онбординг:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --auth-choice cohere-api-key \  --cohere-api-key "$COHERE_API_KEY"
[/code]

  4. Убедитесь, что каталог доступен:

bashCopy code
[code]
    openclaw models list --provider cohere
[/code]

Модель по умолчанию задается только если основная модель еще не настроена.

## Настройка только через окружение

Сделайте `COHERE_API_KEY` доступной для процесса Gateway, затем выберите модель Cohere:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "cohere/command-a-03-2025" },    },  },}
[/code]

## См. также

  * [Провайдеры моделей](</ru/concepts/model-providers>)
  * [CLI моделей](</ru/cli/models>)
  * [Каталог провайдеров](</ru/providers>)


Was this useful?YesNo

Open issue