---
title: Довідник із конфігурації пам’яті
source_url: https://docs.openclaw.ai/uk/reference/memory-config
scraped_at: 2026-05-25
---

На цій сторінці перелічено всі параметри конфігурації для пошуку в пам’яті OpenClaw. Концептуальні огляди дивіться тут:

[**Огляд пам’яті** Як працює пам’ять. ](</uk/concepts/memory>) [**Вбудований рушій** Типовий бекенд SQLite. ](</uk/concepts/memory-builtin>) [**Рушій QMD** Локальний передусім sidecar. ](</uk/concepts/memory-qmd>) [**Пошук у пам’яті** Конвеєр пошуку та налаштування. ](</uk/concepts/memory-search>) [**Активна пам’ять** Субагент пам’яті для інтерактивних сеансів. ](</uk/concepts/active-memory>)

Усі налаштування пошуку в пам’яті розташовані в `agents.defaults.memorySearch` у `openclaw.json`, якщо не зазначено інше.

* * *

## Вибір провайдера

Ключ | Тип | Типове значення | Опис  
---|---|---|---  
`provider` | `string` | визначається автоматично | ID адаптера embedding, як-от `bedrock`, `deepinfra`, `gemini`, `github-copilot`, `local`, `mistral`, `ollama`, `openai` або `voyage`; також може бути налаштованим `models.providers.<id>`, у якому `api` вказує на один із цих адаптерів  
`model` | `string` | типове значення провайдера | Назва моделі embedding  
`fallback` | `string` | `"none"` | ID резервного адаптера, коли основний не спрацьовує  
`enabled` | `boolean` | `true` | Увімкнути або вимкнути пошук у пам’яті  
  
### Порядок автоматичного визначення

Коли `provider` не задано, OpenClaw вибирає перший доступний:

* ### local

Вибирається, якщо `memorySearch.local.modelPath` налаштовано й файл існує.

* ### github-copilot

Вибирається, якщо можна визначити токен GitHub Copilot (змінна середовища або профіль автентифікації).

* ### openai

Вибирається, якщо можна визначити ключ OpenAI.

* ### gemini

Вибирається, якщо можна визначити ключ Gemini.

* ### voyage

Вибирається, якщо можна визначити ключ Voyage.

* ### mistral

Вибирається, якщо можна визначити ключ Mistral.

* ### deepinfra

Вибирається, якщо можна визначити ключ DeepInfra.

* ### bedrock

Вибирається, якщо ланцюжок облікових даних AWS SDK успішно визначається (роль інстанса, ключі доступу, профіль, SSO, вебідентичність або спільна конфігурація).

`ollama` підтримується, але не визначається автоматично (задайте його явно).

### Власні ідентифікатори провайдерів

`memorySearch.provider` може вказувати на власний запис `models.providers.<id>`. OpenClaw визначає власника `api` цього провайдера для адаптера embedding, зберігаючи власний ідентифікатор провайдера для обробки кінцевої точки, автентифікації та префікса моделі. Це дає змогу конфігураціям із кількома GPU або кількома хостами виділити embeddings пам’яті для конкретної локальної кінцевої точки:

json5Copy code
[code]
    {  models: {    providers: {      "ollama-5080": {        api: "ollama",        baseUrl: "http://gpu-box.local:11435",        apiKey: "ollama-local",        models: [{ id: "qwen3-embedding:0.6b" }],      },    },  },  agents: {    defaults: {      memorySearch: {        provider: "ollama-5080",        model: "qwen3-embedding:0.6b",      },    },  },}
[/code]

### Визначення API-ключа

Віддалені embeddings потребують API-ключа. Bedrock натомість використовує типовий ланцюжок облікових даних AWS SDK (ролі інстансів, SSO, ключі доступу).

Провайдер | Змінна середовища | Ключ конфігурації  
---|---|---  
Bedrock | ланцюжок облікових даних AWS | API-ключ не потрібен  
DeepInfra | `DEEPINFRA_API_KEY` | `models.providers.deepinfra.apiKey`  
Gemini | `GEMINI_API_KEY` | `models.providers.google.apiKey`  
GitHub Copilot | `COPILOT_GITHUB_TOKEN`, `GH_TOKEN`, `GITHUB_TOKEN` | Профіль автентифікації через вхід із пристрою  
Mistral | `MISTRAL_API_KEY` | `models.providers.mistral.apiKey`  
Ollama | `OLLAMA_API_KEY` (заповнювач) | \--  
OpenAI | `OPENAI_API_KEY` | `models.providers.openai.apiKey`  
Voyage | `VOYAGE_API_KEY` | `models.providers.voyage.apiKey`  
  
* * *

## Конфігурація віддаленої кінцевої точки

Для власних OpenAI-сумісних кінцевих точок або перевизначення типових значень провайдера:

Власний базовий URL API.

Перевизначити API-ключ.

Додаткові заголовки HTTP (об’єднуються з типовими значеннями провайдера).

json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        provider: "openai",        model: "text-embedding-3-small",        remote: {          baseUrl: "https://api.example.com/v1/",          apiKey: "YOUR_KEY",        },      },    },  },}
[/code]

* * *

## Конфігурація для окремих провайдерів

Gemini Ключ | Тип | Типове значення | Опис  
---|---|---|---  
`model` | `string` | `gemini-embedding-001` | Також підтримує `gemini-embedding-2-preview`  
`outputDimensionality` | `number` | `3072` | Для Embedding 2: 768, 1536 або 3072  
OpenAI-сумісні типи введення

OpenAI-сумісні кінцеві точки embedding можуть увімкнути специфічні для провайдера поля запиту `input_type`. Це корисно для асиметричних моделей embedding, яким потрібні різні мітки для embeddings запитів і документів.

Ключ | Тип | Типове значення | Опис  
---|---|---|---  
`inputType` | `string` | не задано | Спільний `input_type` для embeddings запитів і документів  
`queryInputType` | `string` | не задано | `input_type` під час запиту; перевизначає `inputType`  
`documentInputType` | `string` | не задано | `input_type` індексу/документа; перевизначає `inputType`  
json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        provider: "openai",        remote: {          baseUrl: "https://embeddings.example/v1",          apiKey: "env:EMBEDDINGS_API_KEY",        },        model: "asymmetric-embedder",        queryInputType: "query",        documentInputType: "passage",      },    },  },}
[/code]

Зміна цих значень впливає на ідентичність кешу embedding для пакетного індексування провайдера, і після неї слід виконати переіндексування пам’яті, якщо upstream-модель обробляє мітки по-різному.

Bedrock

### Конфігурація embedding Bedrock

Bedrock використовує типовий ланцюжок облікових даних AWS SDK — API-ключі не потрібні. Якщо OpenClaw працює на EC2 з роллю інстанса з доступом до Bedrock, просто задайте провайдера й модель:

json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        provider: "bedrock",        model: "amazon.titan-embed-text-v2:0",      },    },  },}
[/code]

Ключ | Тип | Типове значення | Опис  
---|---|---|---  
`model` | `string` | `amazon.titan-embed-text-v2:0` | Будь-який ID моделі embedding Bedrock  
`outputDimensionality` | `number` | типове значення моделі | Для Titan V2: 256, 512 або 1024  
  
**Підтримувані моделі** (з визначенням сімейства та типовими розмірностями):

ID моделі | Провайдер | Типові розмірності | Налаштовувані розмірності  
---|---|---|---  
`amazon.titan-embed-text-v2:0` | Amazon | 1024 | 256, 512, 1024  
`amazon.titan-embed-text-v1` | Amazon | 1536 | \--  
`amazon.titan-embed-g1-text-02` | Amazon | 1536 | \--  
`amazon.titan-embed-image-v1` | Amazon | 1024 | \--  
`amazon.nova-2-multimodal-embeddings-v1:0` | Amazon | 1024 | 256, 384, 1024, 3072  
`cohere.embed-english-v3` | Cohere | 1024 | \--  
`cohere.embed-multilingual-v3` | Cohere | 1024 | \--  
`cohere.embed-v4:0` | Cohere | 1536 | 256-1536  
`twelvelabs.marengo-embed-3-0-v1:0` | TwelveLabs | 512 | \--  
`twelvelabs.marengo-embed-2-7-v1:0` | TwelveLabs | 1024 | \--  
  
Варіанти із суфіксом пропускної здатності (наприклад, `amazon.titan-embed-text-v1:2:8k`) успадковують конфігурацію базової моделі.

**Автентифікація:** автентифікація Bedrock використовує стандартний порядок визначення облікових даних AWS SDK:

  1. Змінні середовища (`AWS_ACCESS_KEY_ID` \+ `AWS_SECRET_ACCESS_KEY`)
  2. Кеш токенів SSO
  3. Облікові дані токена вебідентичності
  4. Спільні файли облікових даних і конфігурації
  5. Облікові дані метаданих ECS або EC2


Регіон визначається з `AWS_REGION`, `AWS_DEFAULT_REGION`, `baseUrl` провайдера `amazon-bedrock` або за замовчуванням встановлюється на `us-east-1`.

**Дозволи IAM:** роль або користувач IAM потребує:

jsonCopy code
[code]
    {  "Effect": "Allow",  "Action": "bedrock:InvokeModel",  "Resource": "*"}
[/code]

Для мінімальних привілеїв обмежте `InvokeModel` конкретною моделлю:

CodeCopy code
[code]
    arn:aws:bedrock:*::foundation-model/amazon.titan-embed-text-v2:0
[/code]

Local (GGUF + node-llama-cpp) Ключ | Тип | Типово | Опис  
---|---|---|---  
`local.modelPath` | `string` | автоматично завантажується | Шлях до файлу моделі GGUF  
`local.modelCacheDir` | `string` | типове для node-llama-cpp | Каталог кешу для завантажених моделей  
`local.contextSize` | `number | "auto"` | `4096` | Розмір контекстного вікна для контексту embedding. 4096 покриває типові фрагменти (128-512 токенів), водночас обмежуючи VRAM не для ваг. Зменште до 1024-2048 на обмежених хостах. `"auto"` використовує навчений максимум моделі — не рекомендовано для моделей 8B+ (Qwen3-Embedding-8B: 40 960 токенів → ~32 ГБ VRAM проти ~8.8 ГБ за 4096).  
  
Типова модель: `embeddinggemma-300m-qat-Q8_0.gguf` (~0.6 ГБ, автоматично завантажується). Вихідні checkout-и все ще потребують схвалення нативного складання: `pnpm approve-builds`, потім `pnpm rebuild node-llama-cpp`.

Використовуйте окремий CLI, щоб перевірити той самий шлях провайдера, який використовує Gateway:

bashCopy code
[code]
    openclaw memory status --deep --agent mainopenclaw memory index --force --agent main
[/code]

Якщо `provider` має значення `auto`, `local` вибирається лише тоді, коли `local.modelPath` вказує на наявний локальний файл. Посилання на моделі `hf:` і HTTP(S) усе ще можна явно використовувати з `provider: "local"`, але вони не змушують `auto` вибрати local до того, як модель стане доступною на диску.

### Тайм-аут inline embedding

Перевизначає тайм-аут для inline embedding пакетів під час індексування пам’яті.

Якщо не задано, використовується типове значення провайдера: 600 секунд для локальних/self-hosted провайдерів, таких як `local`, `ollama` і `lmstudio`, та 120 секунд для hosted провайдерів. Збільште це значення, коли локальні CPU-bound embedding пакети справні, але повільні.

* * *

## Конфігурація гібридного пошуку

Усе в `memorySearch.query.hybrid`:

Ключ | Тип | Типово | Опис  
---|---|---|---  
`enabled` | `boolean` | `true` | Увімкнути гібридний пошук BM25 + векторний пошук  
`vectorWeight` | `number` | `0.7` | Вага для векторних оцінок (0-1)  
`textWeight` | `number` | `0.3` | Вага для оцінок BM25 (0-1)  
`candidateMultiplier` | `number` | `4` | Множник розміру пулу кандидатів  
  
### MMR (diversity)

Ключ | Тип | Типово | Опис  
---|---|---|---  
`mmr.enabled` | `boolean` | `false` | Увімкнути повторне ранжування MMR  
`mmr.lambda` | `number` | `0.7` | 0 = макс. різноманітність, 1 = макс. релевантність  
  
### Temporal decay (recency)

Ключ | Тип | Типово | Опис  
---|---|---|---  
`temporalDecay.enabled` | `boolean` | `false` | Увімкнути підсилення за свіжістю  
`temporalDecay.halfLifeDays` | `number` | `30` | Оцінка зменшується вдвічі кожні N днів  
  
Evergreen-файли (`MEMORY.md`, файли без дат у `memory/`) ніколи не піддаються згасанню.

### Повний приклад

json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        query: {          hybrid: {            vectorWeight: 0.7,            textWeight: 0.3,            mmr: { enabled: true, lambda: 0.7 },            temporalDecay: { enabled: true, halfLifeDays: 30 },          },        },      },    },  },}
[/code]

* * *

## Додаткові шляхи пам’яті

Ключ | Тип | Опис  
---|---|---  
`extraPaths` | `string[]` | Додаткові каталоги або файли для індексування  
json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        extraPaths: ["../team-docs", "/srv/shared-notes"],      },    },  },}
[/code]

Шляхи можуть бути абсолютними або відносними до workspace. Каталоги рекурсивно скануються на файли `.md`. Обробка symlink залежить від активного backend: вбудований рушій ігнорує symlink, тоді як QMD дотримується поведінки базового сканера QMD.

Для agent-scoped пошуку транскриптів між агентами використовуйте `agents.list[].memorySearch.qmd.extraCollections` замість `memory.qmd.paths`. Ці додаткові колекції мають таку саму форму `{ path, name, pattern? }`, але об’єднуються для кожного агента й можуть зберігати явні спільні назви, коли шлях вказує за межі поточного workspace. Якщо той самий resolved path з’являється і в `memory.qmd.paths`, і в `memorySearch.qmd.extraCollections`, QMD зберігає перший запис і пропускає дублікат.

* * *

## Мультимодальна пам’ять (Gemini)

Індексуйте зображення й аудіо разом із Markdown за допомогою Gemini Embedding 2:

Ключ | Тип | Типово | Опис  
---|---|---|---  
`multimodal.enabled` | `boolean` | `false` | Увімкнути мультимодальне індексування  
`multimodal.modalities` | `string[]` | \-- | `["image"]`, `["audio"]` або `["all"]`  
`multimodal.maxFileBytes` | `number` | `10000000` | Максимальний розмір файлу для індексування  
  
Підтримувані формати: `.jpg`, `.jpeg`, `.png`, `.webp`, `.gif`, `.heic`, `.heif` (зображення); `.mp3`, `.wav`, `.ogg`, `.opus`, `.m4a`, `.aac`, `.flac` (аудіо).

* * *

## Кеш embedding

Ключ | Тип | За замовчуванням | Опис  
---|---|---|---  
`cache.enabled` | `boolean` | `false` | Кешувати embedding фрагментів у SQLite  
`cache.maxEntries` | `number` | `50000` | Максимальна кількість кешованих embedding  
  
Запобігає повторному embedding незміненого тексту під час повторного індексування або оновлень транскриптів.

* * *

## Пакетне індексування

Ключ | Тип | За замовчуванням | Опис  
---|---|---|---  
`remote.nonBatchConcurrency` | `number` | `4` | Паралельні inline embedding  
`remote.batch.enabled` | `boolean` | `false` | Увімкнути API пакетного embedding  
`remote.batch.concurrency` | `number` | `2` | Паралельні пакетні завдання  
`remote.batch.wait` | `boolean` | `true` | Чекати завершення пакета  
`remote.batch.pollIntervalMs` | `number` | \-- | Інтервал опитування  
`remote.batch.timeoutMinutes` | `number` | \-- | Тайм-аут пакета  
  
Доступно для `openai`, `gemini` і `voyage`. Пакетний режим OpenAI зазвичай найшвидший і найдешевший для великих ретроспективних заповнень.

`remote.nonBatchConcurrency` керує inline-викликами embedding, які використовуються локальними/self-hosted провайдерами та hosted провайдерами, коли пакетні API провайдера не активні. Для непакетного індексування Ollama за замовчуванням використовує `1`, щоб не перевантажувати менші локальні хости; задайте більше значення на потужніших машинах.

Це окремо від `sync.embeddingBatchTimeoutSeconds`, який керує тайм-аутом для inline-викликів embedding.

* * *

## Пошук у пам’яті сеансів (експериментально)

Індексуйте транскрипти сеансів і надавайте їх через `memory_search`:

Ключ | Тип | За замовчуванням | Опис  
---|---|---|---  
`experimental.sessionMemory` | `boolean` | `false` | Увімкнути індексування сеансів  
`sources` | `string[]` | `["memory"]` | Додайте `"sessions"`, щоб включити транскрипти  
`sync.sessions.deltaBytes` | `number` | `100000` | Пороговий обсяг байтів для повторного індексування  
`sync.sessions.deltaMessages` | `number` | `50` | Порогова кількість повідомлень для повторного індексування  
  
* * *

## Векторне прискорення SQLite (sqlite-vec)

Ключ | Тип | За замовчуванням | Опис  
---|---|---|---  
`store.vector.enabled` | `boolean` | `true` | Використовувати sqlite-vec для векторних запитів  
`store.vector.extensionPath` | `string` | bundled | Перевизначити шлях sqlite-vec  
  
Коли sqlite-vec недоступний, OpenClaw автоматично повертається до косинусної подібності в межах процесу.

* * *

## Сховище індексу

Ключ | Тип | За замовчуванням | Опис  
---|---|---|---  
`store.path` | `string` | `~/.openclaw/memory/{agentId}.sqlite` | Розташування індексу (підтримує токен `{agentId}`)  
`store.fts.tokenizer` | `string` | `unicode61` | Токенізатор FTS5 (`unicode61` або `trigram`)  
  
* * *

## Конфігурація backend QMD

Задайте `memory.backend = "qmd"`, щоб увімкнути. Усі налаштування QMD розташовані в `memory.qmd`:

Ключ | Тип | За замовчуванням | Опис  
---|---|---|---  
`command` | `string` | `qmd` | Шлях до виконуваного файлу QMD; задайте абсолютний шлях, коли `PATH` сервісу відрізняється від вашої оболонки  
`searchMode` | `string` | `search` | Команда пошуку: `search`, `vsearch`, `query`  
`includeDefaultMemory` | `boolean` | `true` | Автоматично індексувати `MEMORY.md` \+ `memory/**/*.md`  
`paths[]` | `array` | \-- | Додаткові шляхи: `{ name, path, pattern? }`  
`sessions.enabled` | `boolean` | `false` | Індексувати транскрипти сеансів  
`sessions.retentionDays` | `number` | \-- | Термін зберігання транскриптів  
`sessions.exportDir` | `string` | \-- | Каталог експорту  
  
`searchMode: "search"` є лише лексичним/BM25. OpenClaw не запускає перевірки готовності семантичних векторів або обслуговування QMD-вбудовувань для цього режиму, зокрема під час `memory status --deep`; `vsearch` і `query` і далі потребують готовності QMD-векторів і вбудовувань.

OpenClaw віддає перевагу поточним колекціям QMD і формам запитів MCP, але зберігає сумісність зі старішими випусками QMD, за потреби пробуючи сумісні прапорці шаблонів колекцій і старіші назви інструментів MCP. Коли QMD оголошує підтримку кількох фільтрів колекцій, колекції з одного джерела шукаються одним процесом QMD; старіші збірки QMD зберігають шлях сумісності для кожної колекції. Одне джерело означає, що колекції сталої пам’яті групуються разом, тоді як колекції транскриптів сесій залишаються окремою групою, щоб диверсифікація джерел і далі мала обидва входи.

Розклад оновлень Ключ | Тип | Типово | Опис  
---|---|---|---  
`update.interval` | `string` | `5m` | Інтервал оновлення  
`update.debounceMs` | `number` | `15000` | Усунення брязкоту змін файлів  
`update.onBoot` | `boolean` | `true` | Оновлювати, коли відкривається довгоживучий менеджер QMD; також обмежує добровільне стартове оновлення  
`update.startup` | `string` | `off` | Необов’язкове оновлення під час запуску gateway: `off`, `idle` або `immediate`  
`update.startupDelayMs` | `number` | `120000` | Затримка перед виконанням оновлення `startup: "idle"`  
`update.waitForBootSync` | `boolean` | `false` | Блокувати відкриття менеджера, доки не завершиться його початкове оновлення  
`update.embedInterval` | `string` | \-- | Окрема періодичність вбудовування  
`update.commandTimeoutMs` | `number` | \-- | Тайм-аут для команд QMD  
`update.updateTimeoutMs` | `number` | \-- | Тайм-аут для операцій оновлення QMD  
`update.embedTimeoutMs` | `number` | \-- | Тайм-аут для операцій вбудовування QMD  
Обмеження Ключ | Тип | Типово | Опис  
---|---|---|---  
`limits.maxResults` | `number` | `6` | Максимальна кількість результатів пошуку  
`limits.maxSnippetChars` | `number` | \-- | Обмежити довжину фрагмента  
`limits.maxInjectedChars` | `number` | \-- | Обмежити загальну кількість вставлених символів  
`limits.timeoutMs` | `number` | `4000` | Тайм-аут пошуку  
Область дії

Керує тим, які сесії можуть отримувати результати пошуку QMD. Та сама схема, що й [`session.sendPolicy`](</uk/gateway/config-agents#session>):

json5Copy code
[code]
    {  memory: {    qmd: {      scope: {        default: "deny",        rules: [{ action: "allow", match: { chatType: "direct" } }],      },    },  },}
[/code]

Типове значення, що постачається, дозволяє прямі сесії та сесії каналів, але й далі забороняє групи.

Типово дозволено лише DM. `match.keyPrefix` зіставляє нормалізований ключ сесії; `match.rawKeyPrefix` зіставляє сирий ключ, включно з `agent:<id>:`.

Цитування

`memory.citations` застосовується до всіх бекендів:

Значення | Поведінка  
---|---  
`auto` (типово) | Додавати нижній колонтитул `Source: <path#line>` у фрагменти  
`on` | Завжди додавати нижній колонтитул  
`off` | Не додавати нижній колонтитул (шлях усе одно передається агенту внутрішньо)  
  
Оновлення QMD під час завантаження використовують одноразовий шлях підпроцесу під час запуску gateway. Довгоживучий менеджер QMD і далі володіє звичайним спостерігачем за файлами та таймерами інтервалів, коли пошук у пам’яті відкрито для інтерактивного використання.

### Повний приклад QMD

json5Copy code
[code]
    {  memory: {    backend: "qmd",    citations: "auto",    qmd: {      includeDefaultMemory: true,      update: { interval: "5m", debounceMs: 15000 },      limits: { maxResults: 6, timeoutMs: 4000 },      scope: {        default: "deny",        rules: [{ action: "allow", match: { chatType: "direct" } }],      },      paths: [{ name: "docs", path: "~/notes", pattern: "**/*.md" }],    },  },}
[/code]

* * *

## Dreaming

Dreaming налаштовується в `plugins.entries.memory-core.config.dreaming`, а не в `agents.defaults.memorySearch`.

Dreaming виконується як одне заплановане сканування та використовує внутрішні фази light/deep/REM як деталь реалізації.

Концептуальну поведінку та slash-команди див. у [Dreaming](</uk/concepts/dreaming>).

### Налаштування користувача

Ключ | Тип | Типово | Опис  
---|---|---|---  
`enabled` | `boolean` | `false` | Повністю увімкнути або вимкнути dreaming  
`frequency` | `string` | `0 3 * * *` | Необов’язкова cron-періодичність для повного сканування dreaming  
`model` | `string` | типова модель | Необов’язкове перевизначення моделі субагента Dream Diary  
  
### Приклад

json5Copy code
[code]
    {  plugins: {    entries: {      "memory-core": {        subagent: {          allowModelOverride: true,          allowedModels: ["anthropic/claude-sonnet-4-6"],        },        config: {          dreaming: {            enabled: true,            frequency: "0 3 * * *",            model: "anthropic/claude-sonnet-4-6",          },        },      },    },  },}
[/code]

## Пов’язане

  * [Довідник конфігурації](</uk/gateway/configuration-reference>)
  * [Огляд пам’яті](</uk/concepts/memory>)
  * [Пошук у пам’яті](</uk/concepts/memory-search>)


Was this useful?YesNo