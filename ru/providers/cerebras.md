---
title: Cerebras
source_url: https://docs.openclaw.ai/ru/providers/cerebras
scraped_at: 2026-06-29
---

ModelsProviders

[Cerebras](<https://www.cerebras.ai>) предоставляет высокоскоростной, совместимый с OpenAI инференс на специализированном оборудовании для инференса. Provider Plugin Cerebras включает статический каталог из четырех моделей.

Свойство | Значение  
---|---  
ID провайдера | `cerebras`  
Plugin | официальный внешний пакет  
Переменная env для авторизации | `CEREBRAS_API_KEY`  
Флаг онбординга | `--auth-choice cerebras-api-key`  
Прямой флаг CLI | `--cerebras-api-key <key>`  
API | совместимый с OpenAI (`openai-completions`)  
Базовый URL | `https://api.cerebras.ai/v1`  
Модель по умолчанию | `cerebras/zai-glm-4.7`  
  
## Установите Plugin

Установите официальный Plugin, затем перезапустите Gateway:

bashCopy code
[code]
    openclaw plugins install @openclaw/cerebras-provideropenclaw gateway restart
[/code]

## Начало работы

* ### Get an API key

Создайте API-ключ в [Cerebras Cloud Console](<https://cloud.cerebras.ai>).

* ### Run onboarding

ОнбордингCopy code
[code]
    openclaw onboard --auth-choice cerebras-api-key
[/code]

Прямой флагCopy code
[code]
    openclaw onboard --non-interactive \--auth-choice cerebras-api-key \--cerebras-api-key "$CEREBRAS_API_KEY"
[/code]

Только envCopy code
[code]
    export CEREBRAS_API_KEY=csk-...
[/code]

* ### Verify models are available

bashCopy code
[code]
    openclaw models list --provider cerebras
[/code]

Список должен включать все четыре статические модели. Если `CEREBRAS_API_KEY` не разрешается, `openclaw models status --json` сообщает об отсутствующих учетных данных в `auth.unusableProfiles`.

## Неинтерактивная настройка

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice cerebras-api-key \  --cerebras-api-key "$CEREBRAS_API_KEY"
[/code]

## Встроенный каталог

OpenClaw поставляется со статическим каталогом Cerebras, который отражает публичную совместимую с OpenAI конечную точку. Все четыре модели используют контекст 128k и максимум 8 192 токена вывода.

Ссылка на модель | Название | Рассуждение | Примечания  
---|---|---|---  
`cerebras/zai-glm-4.7` | Z.ai GLM 4.7 | да | Модель по умолчанию; preview-модель рассуждения  
`cerebras/gpt-oss-120b` | GPT OSS 120B | да | Production-модель рассуждения  
`cerebras/qwen-3-235b-a22b-instruct-2507` | Qwen 3 235B Instruct | нет | Preview-модель без рассуждения  
`cerebras/llama3.1-8b` | Llama 3.1 8B | нет | Production-модель, ориентированная на скорость  
  
## Ручная конфигурация

Обычно Plugin означает, что вам нужен только API-ключ. Используйте явную конфигурацию `models.providers.cerebras`, если хотите переопределить метаданные модели или работать в `mode: "merge"` со статическим каталогом:

json5Copy code
[code]
    {  env: { CEREBRAS_API_KEY: "csk-..." },  agents: {    defaults: {      model: { primary: "cerebras/zai-glm-4.7" },    },  },  models: {    mode: "merge",    providers: {      cerebras: {        baseUrl: "https://api.cerebras.ai/v1",        apiKey: "${CEREBRAS_API_KEY}",        api: "openai-completions",        models: [          { id: "zai-glm-4.7", name: "Z.ai GLM 4.7" },          { id: "gpt-oss-120b", name: "GPT OSS 120B" },        ],      },    },  },}
[/code]

## Связанные материалы

[**Model providers** Выбор провайдеров, ссылок на модели и поведения failover. ](</ru/concepts/model-providers>) [**Thinking modes** Уровни усилия рассуждения для двух моделей Cerebras с поддержкой рассуждения. ](</ru/tools/thinking>) [**Configuration reference** Значения по умолчанию для агента и конфигурация моделей. ](</ru/gateway/config-agents#agent-defaults>) [**Models FAQ** Профили авторизации, переключение моделей и устранение ошибок "no profile". ](</ru/help/faq-models>)

Was this useful?YesNo

Open issue