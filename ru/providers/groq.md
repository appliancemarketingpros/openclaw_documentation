---
title: Groq
source_url: https://docs.openclaw.ai/ru/providers/groq
scraped_at: 2026-06-29
---

ModelsProviders

[Groq](<https://groq.com>) обеспечивает сверхбыстрый инференс на моделях с открытыми весами (Llama, Gemma, Kimi, Qwen, GPT OSS и других) с использованием специализированного оборудования LPU. Plugin Groq регистрирует как совместимый с OpenAI провайдер чата, так и провайдер понимания аудиомедиа.

Свойство | Значение  
---|---  
Идентификатор провайдера | `groq`  
Plugin | официальный внешний пакет  
Переменная окружения авторизации | `GROQ_API_KEY`  
API | совместимый с OpenAI (`openai-completions`)  
Базовый URL | `https://api.groq.com/openai/v1`  
Транскрибация аудио | `whisper-large-v3-turbo` (по умолчанию)  
Рекомендуемая модель чата по умолчанию | `groq/llama-3.3-70b-versatile`  
  
## Установите Plugin

Установите официальный Plugin, затем перезапустите Gateway:

bashCopy code
[code]
    openclaw plugins install @openclaw/groq-provideropenclaw gateway restart
[/code]

## Начало работы

* ### Получите ключ API

Создайте ключ API на [console.groq.com/keys](<https://console.groq.com/keys>).

* ### Задайте ключ API

bashCopy code
[code]
    export GROQ_API_KEY=gsk_...
[/code]

* ### Задайте модель по умолчанию

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "groq/llama-3.3-70b-versatile" },    },  },}
[/code]

* ### Проверьте доступность каталога

bashCopy code
[code]
    openclaw models list --provider groq
[/code]

### Пример файла конфигурации

json5Copy code
[code]
    {  env: { GROQ_API_KEY: "gsk_..." },  agents: {    defaults: {      model: { primary: "groq/llama-3.3-70b-versatile" },    },  },}
[/code]

## Встроенный каталог

OpenClaw поставляется с каталогом Groq на основе манифеста, включающим записи как с рассуждением, так и без него. Выполните `openclaw models list --provider groq`, чтобы увидеть статические строки для установленной версии, или проверьте [console.groq.com/docs/models](<https://console.groq.com/docs/models>), чтобы получить авторитетный список Groq.

Ссылка на модель | Название | Рассуждение | Ввод | Контекст  
---|---|---|---|---  
`groq/llama-3.3-70b-versatile` | Llama 3.3 70B Versatile | нет | текст | 131,072  
`groq/llama-3.1-8b-instant` | Llama 3.1 8B Instant | нет | текст | 131,072  
`groq/meta-llama/llama-4-scout-17b-16e-instruct` | Llama 4 Scout 17B | нет | текст + изображение | 131,072  
`groq/openai/gpt-oss-120b` | GPT OSS 120B | да | текст | 131,072  
`groq/openai/gpt-oss-20b` | GPT OSS 20B | да | текст | 131,072  
`groq/openai/gpt-oss-safeguard-20b` | Safety GPT OSS 20B | да | текст | 131,072  
`groq/qwen/qwen3-32b` | Qwen3 32B | да | текст | 131,072  
`groq/groq/compound` | Compound | да | текст | 131,072  
`groq/groq/compound-mini` | Compound Mini | да | текст | 131,072  
  
## Модели рассуждения

OpenClaw сопоставляет свои общие уровни `/think` со специфичными для моделей Groq значениями `reasoning_effort`:

  * Для `qwen/qwen3-32b` отключенное мышление отправляет `none`, а включенное мышление отправляет `default`.
  * Для моделей рассуждения Groq GPT OSS (`openai/gpt-oss-*`) OpenClaw отправляет `low`, `medium` или `high` на основе уровня `/think`. При отключенном мышлении `reasoning_effort` не отправляется, потому что эти модели не поддерживают отключенное значение.
  * DeepSeek R1 Distill, Qwen QwQ и Compound используют нативную поверхность рассуждения Groq; `/think` управляет видимостью, но модель всегда рассуждает.


См. [Режимы мышления](</ru/tools/thinking>), чтобы узнать об общих уровнях `/think` и о том, как OpenClaw переводит их для каждого провайдера.

## Транскрибация аудио

Plugin Groq также регистрирует **провайдер понимания аудиомедиа** , чтобы голосовые сообщения можно было транскрибировать через общую поверхность `tools.media.audio`.

Свойство | Значение  
---|---  
Общий путь конфигурации | `tools.media.audio`  
Базовый URL по умолчанию | `https://api.groq.com/openai/v1`  
Модель по умолчанию | `whisper-large-v3-turbo`  
Автоматический приоритет | 20  
Конечная точка API | совместимая с OpenAI `/audio/transcriptions`  
  
Чтобы сделать Groq аудиобэкендом по умолчанию:

json5Copy code
[code]
    {  tools: {    media: {      audio: {        models: [{ provider: "groq" }],      },    },  },}
[/code]

Доступность окружения для демона

Если Gateway работает как управляемая служба (launchd, systemd, Docker), `GROQ_API_KEY` должен быть виден этому процессу, а не только вашей интерактивной оболочке.

Пользовательские идентификаторы моделей Groq

OpenClaw принимает любой идентификатор модели Groq во время выполнения. Используйте точный идентификатор, показанный Groq, и добавьте к нему префикс `groq/`. Статический каталог покрывает распространенные случаи; идентификаторы вне каталога переходят к шаблону по умолчанию, совместимому с OpenAI.

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "groq/<your-model-id>" },    },  },}
[/code]

## Связанные материалы

[**Провайдеры моделей** Выбор провайдеров, ссылок на модели и поведения при отказе. ](</ru/concepts/model-providers>) [**Режимы мышления** Уровни усилия рассуждения и взаимодействие с политикой провайдера. ](</ru/tools/thinking>) [**Справочник по конфигурации** Полная схема конфигурации, включая настройки провайдеров и аудио. ](</ru/gateway/configuration-reference>) [**Groq Console** Панель Groq, документация API и цены. ](<https://console.groq.com>)

Was this useful?YesNo

Open issue