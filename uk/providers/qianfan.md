---
title: Qianfan
source_url: https://docs.openclaw.ai/uk/providers/qianfan
scraped_at: 2026-05-25
---

Qianfan — це MaaS-платформа Baidu, що надає **уніфікований API** , який маршрутизує запити до багатьох моделей за одним endpoint і API key. Вона сумісна з OpenAI, тож більшість OpenAI SDK працюють після зміни базової URL-адреси.

Властивість | Значення  
---|---  
Провайдер | `qianfan`  
Автентифікація | `QIANFAN_API_KEY`  
API | сумісний з OpenAI  
Базова URL-адреса | `https://qianfan.baidubce.com/v2`  
  
## Початок роботи

* ### Створіть обліковий запис Baidu Cloud

Зареєструйтеся або увійдіть у [Qianfan Console](<https://console.bce.baidu.com/qianfan/ais/console/apiKey>) і переконайтеся, що у вас увімкнено доступ до Qianfan API.

* ### Згенеруйте API key

Створіть новий застосунок або виберіть наявний, а потім згенеруйте API key. Формат ключа: `bce-v3/ALTAK-...`.

* ### Запустіть onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice qianfan-api-key
[/code]

* ### Перевірте, що модель доступна

bashCopy code
[code]
    openclaw models list --provider qianfan
[/code]

## Вбудований каталог

Посилання на модель | Вхідні дані | Контекст | Макс. вихід | Міркування | Примітки  
---|---|---|---|---|---  
`qianfan/deepseek-v3.2` | текст | 98,304 | 32,768 | Так | Стандартна модель  
`qianfan/ernie-5.0-thinking-preview` | текст, зображення | 119,000 | 64,000 | Так | Мультимодальна  
  
## Приклад конфігурації

json5Copy code
[code]
    {  env: { QIANFAN_API_KEY: "bce-v3/ALTAK-..." },  agents: {    defaults: {      model: { primary: "qianfan/deepseek-v3.2" },      models: {        "qianfan/deepseek-v3.2": { alias: "QIANFAN" },      },    },  },  models: {    providers: {      qianfan: {        baseUrl: "https://qianfan.baidubce.com/v2",        api: "openai-completions",        models: [          {            id: "deepseek-v3.2",            name: "DEEPSEEK V3.2",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 98304,            maxTokens: 32768,          },          {            id: "ernie-5.0-thinking-preview",            name: "ERNIE-5.0-Thinking-Preview",            reasoning: true,            input: ["text", "image"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 119000,            maxTokens: 64000,          },        ],      },    },  },}
[/code]

Транспорт і сумісність

Qianfan працює через транспортний шлях, сумісний з OpenAI, а не через нативне формування запитів OpenAI. Це означає, що стандартні можливості OpenAI SDK працюють, але параметри, специфічні для провайдера, можуть не передаватися.

Каталог і перевизначення

Вбудований каталог наразі містить `deepseek-v3.2` і `ernie-5.0-thinking-preview`. Додавайте або перевизначайте `models.providers.qianfan` лише тоді, коли потрібна власна базова URL-адреса або metadata моделі.

Усунення несправностей

  * Переконайтеся, що ваш API key починається з `bce-v3/ALTAK-` і має ввімкнений доступ до Qianfan API у консолі Baidu Cloud.
  * Якщо моделі не відображаються в списку, підтвердьте, що для вашого облікового запису активовано сервіс Qianfan.
  * Стандартна базова URL-адреса — `https://qianfan.baidubce.com/v2`. Змінюйте її лише тоді, коли використовуєте власний endpoint або proxy.


## Пов’язане

[**Вибір моделі** Вибір провайдерів, посилань на моделі та поведінки failover. ](</uk/concepts/model-providers>) [**Довідник конфігурації** Повний довідник конфігурації OpenClaw. ](</uk/gateway/configuration-reference>) [**Налаштування agent** Налаштування стандартних параметрів agent і призначень моделей. ](</uk/concepts/agent>) [**Документація Qianfan API** Офіційна документація Qianfan API. ](<https://cloud.baidu.com/doc/qianfan-api/s/3m7of64lb>)

Was this useful?YesNo