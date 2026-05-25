---
title: Moonshot AI
source_url: https://docs.openclaw.ai/uk/providers/moonshot
scraped_at: 2026-05-25
---

Moonshot надає Kimi API з OpenAI-сумісними кінцевими точками. Налаштуйте провайдера й установіть стандартну модель на `moonshot/kimi-k2.6` або використовуйте Kimi Coding з `kimi/kimi-for-coding`.

## Вбудований каталог моделей

Посилання на модель | Назва | Міркування | Ввід | Контекст | Макс. вивід  
---|---|---|---|---|---  
`moonshot/kimi-k2.6` | Kimi K2.6 | Ні | text, image | 262,144 | 262,144  
`moonshot/kimi-k2.5` | Kimi K2.5 | Ні | text, image | 262,144 | 262,144  
`moonshot/kimi-k2-thinking` | Kimi K2 Thinking | Так | text | 262,144 | 262,144  
`moonshot/kimi-k2-thinking-turbo` | Kimi K2 Thinking Turbo | Так | text | 262,144 | 262,144  
`moonshot/kimi-k2-turbo` | Kimi K2 Turbo | Ні | text | 256,000 | 16,384  
  
Пакетні оцінки вартості для поточних моделей K2, розміщених у Moonshot, використовують опубліковані Moonshot тарифи оплати за використання: Kimi K2.6 коштує $0.16/MTok за cache hit, $0.95/MTok за ввід і $4.00/MTok за вивід; Kimi K2.5 коштує $0.10/MTok за cache hit, $0.60/MTok за ввід і $3.00/MTok за вивід. Інші застарілі записи каталогу зберігають заповнювачі з нульовою вартістю, якщо ви не перевизначите їх у конфігурації.

## Початок роботи

Виберіть свого провайдера та виконайте кроки налаштування.

### Moonshot API

**Найкраще для:** моделей Kimi K2 через Moonshot Open Platform.

* ### Виберіть регіон кінцевої точки

Вибір автентифікації | Кінцева точка | Регіон  
---|---|---  
`moonshot-api-key` | `https://api.moonshot.ai/v1` | Міжнародний  
`moonshot-api-key-cn` | `https://api.moonshot.cn/v1` | Китай  
* ### Запустіть онбординг

bashCopy code
[code]
    openclaw onboard --auth-choice moonshot-api-key
[/code]

Або для кінцевої точки в Китаї:

bashCopy code
[code]
    openclaw onboard --auth-choice moonshot-api-key-cn
[/code]

* ### Установіть стандартну модель

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "moonshot/kimi-k2.6" },    },  },}
[/code]

* ### Перевірте, що моделі доступні

bashCopy code
[code]
    openclaw models list --provider moonshot
[/code]

* ### Запустіть живий smoke-тест

Використовуйте ізольований каталог стану, коли хочете перевірити доступ до моделі й відстеження вартості, не торкаючись своїх звичайних сесій:

bashCopy code
[code]
    OPENCLAW_CONFIG_PATH=/tmp/openclaw-kimi/openclaw.json \OPENCLAW_STATE_DIR=/tmp/openclaw-kimi \openclaw agent --local \  --session-id live-kimi-cost \  --message 'Reply exactly: KIMI_LIVE_OK' \  --thinking off \  --json
[/code]

JSON-відповідь має повідомити `provider: "moonshot"` і `model: "kimi-k2.6"`. Запис транскрипту асистента зберігає нормалізоване використання токенів плюс оцінену вартість у `usage.cost`, коли Moonshot повертає метадані використання.

### Приклад конфігурації

json5Copy code
[code]
    {  env: { MOONSHOT_API_KEY: "sk-..." },  agents: {    defaults: {      model: { primary: "moonshot/kimi-k2.6" },      models: {        // moonshot-kimi-k2-aliases:start        "moonshot/kimi-k2.6": { alias: "Kimi K2.6" },        "moonshot/kimi-k2.5": { alias: "Kimi K2.5" },        "moonshot/kimi-k2-thinking": { alias: "Kimi K2 Thinking" },        "moonshot/kimi-k2-thinking-turbo": { alias: "Kimi K2 Thinking Turbo" },        "moonshot/kimi-k2-turbo": { alias: "Kimi K2 Turbo" },        // moonshot-kimi-k2-aliases:end      },    },  },  models: {    mode: "merge",    providers: {      moonshot: {        baseUrl: "https://api.moonshot.ai/v1",        apiKey: "${MOONSHOT_API_KEY}",        api: "openai-completions",        models: [          // moonshot-kimi-k2-models:start          {            id: "kimi-k2.6",            name: "Kimi K2.6",            reasoning: false,            input: ["text", "image"],            cost: { input: 0.95, output: 4, cacheRead: 0.16, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 262144,          },          {            id: "kimi-k2.5",            name: "Kimi K2.5",            reasoning: false,            input: ["text", "image"],            cost: { input: 0.6, output: 3, cacheRead: 0.1, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 262144,          },          {            id: "kimi-k2-thinking",            name: "Kimi K2 Thinking",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 262144,          },          {            id: "kimi-k2-thinking-turbo",            name: "Kimi K2 Thinking Turbo",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 262144,          },          {            id: "kimi-k2-turbo",            name: "Kimi K2 Turbo",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 256000,            maxTokens: 16384,          },          // moonshot-kimi-k2-models:end        ],      },    },  },}
[/code]

### Kimi Coding

**Найкраще для:** задач, орієнтованих на код, через кінцеву точку Kimi Coding.

* ### Запустіть онбординг

bashCopy code
[code]
    openclaw onboard --auth-choice kimi-code-api-key
[/code]

* ### Установіть стандартну модель

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "kimi/kimi-for-coding" },    },  },}
[/code]

* ### Перевірте, що модель доступна

bashCopy code
[code]
    openclaw models list --provider kimi
[/code]

### Приклад конфігурації

json5Copy code
[code]
    {  env: { KIMI_API_KEY: "sk-..." },  agents: {    defaults: {      model: { primary: "kimi/kimi-for-coding" },      models: {        "kimi/kimi-for-coding": { alias: "Kimi" },      },    },  },}
[/code]

## Вебпошук Kimi

OpenClaw також постачає **Kimi** як провайдера `web_search` на основі вебпошуку Moonshot.

* ### Запустіть інтерактивне налаштування вебпошуку

bashCopy code
[code]
    openclaw configure --section web
[/code]

Виберіть **Kimi** у розділі вебпошуку, щоб зберегти `plugins.entries.moonshot.config.webSearch.*`.

* ### Налаштуйте регіон і модель вебпошуку

Інтерактивне налаштування запитує:

Налаштування | Варіанти  
---|---  
Регіон API | `https://api.moonshot.ai/v1` (міжнародний) або `https://api.moonshot.cn/v1` (Китай)  
Модель вебпошуку | За замовчуванням `kimi-k2.6`  
  
Конфігурація міститься в `plugins.entries.moonshot.config.webSearch`:

json5Copy code
[code]
    {  plugins: {    entries: {      moonshot: {        config: {          webSearch: {            apiKey: "sk-...", // or use KIMI_API_KEY / MOONSHOT_API_KEY            baseUrl: "https://api.moonshot.ai/v1",            model: "kimi-k2.6",          },        },      },    },  },  tools: {    web: {      search: {        provider: "kimi",      },    },  },}
[/code]

## Розширена конфігурація

Нативний режим міркування

Moonshot Kimi підтримує бінарне нативне міркування:

  * `thinking: { type: "enabled" }`
  * `thinking: { type: "disabled" }`


Налаштуйте його для кожної моделі через `agents.defaults.models.<provider/model>.params`:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "moonshot/kimi-k2.6": {          params: {            thinking: { type: "disabled" },          },        },      },    },  },}
[/code]

OpenClaw також зіставляє рівні `/think` під час виконання для Moonshot:

Рівень `/think` | Поведінка Moonshot  
---|---  
`/think off` | `thinking.type=disabled`  
Будь-який рівень не off | `thinking.type=enabled`  
  
Kimi K2.6 також приймає необов’язкове поле `thinking.keep`, яке керує багатокроковим збереженням `reasoning_content`. Установіть його на `"all"`, щоб зберігати повне міркування між ходами; пропустіть його (або залиште `null`), щоб використовувати серверну стратегію за замовчуванням. OpenClaw передає `thinking.keep` лише для `moonshot/kimi-k2.6` і вилучає його з інших моделей.

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "moonshot/kimi-k2.6": {          params: {            thinking: { type: "enabled", keep: "all" },          },        },      },    },  },}
[/code]

Санітизація ID виклику інструмента

Moonshot Kimi обслуговує ID tool_call у форматі `functions.<name>:<index>`. OpenClaw зберігає їх без змін, щоб багатокрокові виклики інструментів продовжували працювати.

Щоб примусово ввімкнути сувору санітизацію для власного OpenAI-сумісного провайдера, установіть `sanitizeToolCallIds: true`:

json5Copy code
[code]
    {  models: {    providers: {      "my-kimi-proxy": {        api: "openai-completions",        sanitizeToolCallIds: true,      },    },  },}
[/code]

Сумісність використання під час стримінгу

Нативні кінцеві точки Moonshot (`https://api.moonshot.ai/v1` і `https://api.moonshot.cn/v1`) оголошують сумісність використання під час стримінгу на спільному транспорті `openai-completions`. OpenClaw визначає це за можливостями кінцевої точки, тому сумісні власні ID провайдерів, що спрямовані на ті самі нативні хости Moonshot, успадковують таку саму поведінку використання під час стримінгу.

З пакетною ціною K2.6 стримінгове використання, яке включає токени вводу, виводу та cache-read, також перетворюється на локально оцінену вартість у USD для `/status`, `/usage full`, `/usage cost` і обліку сесій на основі транскриптів.

Довідник кінцевих точок і посилань на моделі Провайдер | Префікс посилання на модель | Кінцева точка | Змінна середовища автентифікації  
---|---|---|---  
Moonshot | `moonshot/` | `https://api.moonshot.ai/v1` | `MOONSHOT_API_KEY`  
Moonshot CN | `moonshot/` | `https://api.moonshot.cn/v1` | `MOONSHOT_API_KEY`  
Kimi Coding | `kimi/` | Кінцева точка Kimi Coding | `KIMI_API_KEY`  
Вебпошук | N/A | Та сама, що й регіон Moonshot API | `KIMI_API_KEY` або `MOONSHOT_API_KEY`  
  
  * Вебпошук Kimi використовує `KIMI_API_KEY` або `MOONSHOT_API_KEY` і за замовчуванням застосовує `https://api.moonshot.ai/v1` з моделлю `kimi-k2.6`.
  * За потреби перевизначте ціни й метадані контексту в `models.providers`.
  * Якщо Moonshot публікує інші обмеження контексту для моделі, відповідно налаштуйте `contextWindow`.


## Пов’язане

[**Вибір моделі** Вибір провайдерів, посилань на моделі та поведінки відмовостійкого перемикання. ](</uk/concepts/model-providers>) [**Вебпошук** Налаштування провайдерів вебпошуку, зокрема Kimi. ](</uk/tools/web>) [**Довідник конфігурації** Повна схема конфігурації для провайдерів, моделей і plugins. ](</uk/gateway/configuration-reference>) [**Moonshot Open Platform** Керування ключами Moonshot API та документація. ](<https://platform.moonshot.ai>)

Was this useful?YesNo