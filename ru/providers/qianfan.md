---
title: Qianfan
source_url: https://docs.openclaw.ai/ru/providers/qianfan
scraped_at: 2026-06-29
---

ModelsProviders

Qianfan — это MaaS-платформа Baidu, предоставляющая **унифицированный API** , который направляет запросы к множеству моделей за одной конечной точкой и ключом API. Она совместима с OpenAI, поэтому большинство SDK OpenAI работают после смены базового URL.

Свойство | Значение  
---|---  
Провайдер | `qianfan`  
Аутентификация | `QIANFAN_API_KEY`  
API | Совместим с OpenAI  
Базовый URL | `https://qianfan.baidubce.com/v2`  
  
## Установка plugin

Установите официальный plugin, затем перезапустите Gateway:

bashCopy code
[code]
    openclaw plugins install @openclaw/qianfan-provideropenclaw gateway restart
[/code]

## Начало работы

* ### Create a Baidu Cloud account

Зарегистрируйтесь или войдите в [консоль Qianfan](<https://console.bce.baidu.com/qianfan/ais/console/apiKey>) и убедитесь, что доступ к API Qianfan включен.

* ### Generate an API key

Создайте новое приложение или выберите существующее, затем сгенерируйте ключ API. Формат ключа: `bce-v3/ALTAK-...`.

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice qianfan-api-key
[/code]

* ### Verify the model is available

bashCopy code
[code]
    openclaw models list --provider qianfan
[/code]

## Встроенный каталог

Ссылка на модель | Ввод | Контекст | Макс. вывод | Рассуждение | Примечания  
---|---|---|---|---|---  
`qianfan/deepseek-v3.2` | текст | 98,304 | 32,768 | Да | Модель по умолчанию  
`qianfan/ernie-5.0-thinking-preview` | текст, изображение | 119,000 | 64,000 | Да | Мультимодальная  
  
## Пример конфигурации

json5Copy code
[code]
    {  env: { QIANFAN_API_KEY: "bce-v3/ALTAK-..." },  agents: {    defaults: {      model: { primary: "qianfan/deepseek-v3.2" },      models: {        "qianfan/deepseek-v3.2": { alias: "QIANFAN" },      },    },  },  models: {    providers: {      qianfan: {        baseUrl: "https://qianfan.baidubce.com/v2",        api: "openai-completions",        models: [          {            id: "deepseek-v3.2",            name: "DEEPSEEK V3.2",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 98304,            maxTokens: 32768,          },          {            id: "ernie-5.0-thinking-preview",            name: "ERNIE-5.0-Thinking-Preview",            reasoning: true,            input: ["text", "image"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 119000,            maxTokens: 64000,          },        ],      },    },  },}
[/code]

Transport and compatibility

Qianfan работает через транспортный путь, совместимый с OpenAI, а не через нативное формирование запросов OpenAI. Это означает, что стандартные возможности SDK OpenAI работают, но параметры, специфичные для провайдера, могут не передаваться.

Catalog and overrides

Статический каталог сейчас включает `deepseek-v3.2` и `ernie-5.0-thinking-preview`. Добавляйте или переопределяйте `models.providers.qianfan` только тогда, когда требуется пользовательский базовый URL или метаданные модели.

Troubleshooting

  * Убедитесь, что ваш ключ API начинается с `bce-v3/ALTAK-` и что доступ к API Qianfan включен в консоли Baidu Cloud.
  * Если модели не отображаются в списке, подтвердите, что в вашей учетной записи активирован сервис Qianfan.
  * Базовый URL по умолчанию: `https://qianfan.baidubce.com/v2`. Меняйте его только при использовании пользовательской конечной точки или прокси.


## Связанные материалы

[**Model selection** Выбор провайдеров, ссылок на модели и поведения при отказе. ](</ru/concepts/model-providers>) [**Configuration reference** Полный справочник конфигурации OpenClaw. ](</ru/gateway/configuration-reference>) [**Agent setup** Настройка значений по умолчанию для агентов и назначений моделей. ](</ru/concepts/agent>) [**Qianfan API docs** Официальная документация API Qianfan. ](<https://cloud.baidu.com/doc/qianfan-api/s/3m7of64lb>)

Was this useful?YesNo

Open issue