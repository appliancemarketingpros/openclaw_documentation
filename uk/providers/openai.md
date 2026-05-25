---
title: OpenAI
source_url: https://docs.openclaw.ai/uk/providers/openai
scraped_at: 2026-05-25
---

OpenAI надає API для розробників для моделей GPT, а Codex також доступний як агент для програмування в межах плану ChatGPT через клієнти Codex від OpenAI. OpenClaw зберігає ці поверхні окремими, щоб конфігурація залишалася передбачуваною.

OpenClaw використовує `openai/*` як канонічний маршрут моделей OpenAI. Вбудовані ходи агента на моделях OpenAI за замовчуванням виконуються через нативне середовище виконання app-server Codex; пряма автентифікація ключем OpenAI API залишається доступною для неагентних поверхонь OpenAI, як-от зображення, embeddings, мовлення та realtime.

  * **Моделі агентів** \- моделі `openai/*` через середовище виконання Codex; увійдіть через автентифікацію Codex для використання підписки ChatGPT/Codex або налаштуйте Codex-сумісний резервний ключ OpenAI API, якщо ви навмисно хочете автентифікацію ключем API.
  * **Неагентні API OpenAI** \- прямий доступ до OpenAI Platform з оплатою за використання через `OPENAI_API_KEY` або онбординг ключа OpenAI API.
  * **Застаріла конфігурація** \- посилання на моделі `openai-codex/*` виправляються командою `openclaw doctor --fix` до `openai/*` плюс середовище виконання Codex.


OpenAI явно підтримує використання OAuth підписки в зовнішніх інструментах і робочих процесах на кшталт OpenClaw.

Провайдер, модель, середовище виконання та канал - це окремі шари. Якщо ці мітки змішуються між собою, прочитайте [Середовища виконання агентів](</uk/concepts/agent-runtimes>), перш ніж змінювати конфігурацію.

## Швидкий вибір

Мета | Використовуйте | Примітки  
---|---|---  
Підписка ChatGPT/Codex з нативним середовищем виконання Codex | `openai/gpt-5.5` | Стандартне налаштування агента OpenAI. Увійдіть через автентифікацію Codex.  
Пряма оплата ключем API для моделей агентів | `openai/gpt-5.5` плюс Codex-сумісний профіль ключа API | Використовуйте `auth.order.openai`, щоб розмістити резерв після автентифікації підписки.  
Пряма оплата ключем API через явний PI | `openai/gpt-5.5` плюс середовище виконання провайдера/моделі `pi` | Виберіть звичайний профіль ключа API `openai`.  
Найновіший API-псевдонім ChatGPT Instant | `openai/chat-latest` | Лише прямий ключ API. Рухомий псевдонім для експериментів, не стандартне значення.  
Автентифікація підписки ChatGPT/Codex через явний PI | `openai/gpt-5.5` плюс середовище виконання провайдера/моделі `pi` | Виберіть профіль автентифікації `openai-codex` для маршруту сумісності.  
Генерація або редагування зображень | `openai/gpt-image-2` | Працює як з `OPENAI_API_KEY`, так і з OpenAI Codex OAuth.  
Зображення з прозорим фоном | `openai/gpt-image-1.5` | Використовуйте `outputFormat=png` або `webp` і `openai.background=transparent`.  
  
## Мапа назв

Назви схожі, але не взаємозамінні:

Назва, яку ви бачите | Шар | Значення  
---|---|---  
`openai` | Префікс провайдера | Канонічний маршрут моделей OpenAI; ходи агента використовують середовище виконання Codex.  
`openai-codex` | Застарілий префікс автентифікації/профілю | Старіший простір імен профілю OAuth/підписки OpenAI Codex. Наявні профілі та `auth.order.openai-codex` досі працюють.  
Plugin `codex` | Plugin | Вбудований Plugin OpenClaw, що надає нативне середовище виконання app-server Codex і елементи керування чатом `/codex`.  
провайдер/модель `agentRuntime.id: codex` | Середовище виконання агента | Примусово використовує нативний harness app-server Codex для відповідних вбудованих ходів.  
`/codex ...` | Набір команд чату | Прив’язує/керує потоками app-server Codex із розмови.  
`runtime: "acp", agentId: "codex"` | Маршрут сеансу ACP | Явний резервний шлях, який запускає Codex через ACP/acpx.  
  
Це означає, що конфігурація може навмисно містити посилання на моделі `openai/*`, тоді як профілі автентифікації все ще вказують на Codex-сумісні облікові дані. Для нової конфігурації надавайте перевагу `auth.order.openai`; наявні профілі `openai-codex:*` і `auth.order.openai-codex` залишаються підтримуваними. `openclaw doctor --fix` переписує застарілі посилання на моделі `openai-codex/*` до канонічного маршруту моделей OpenAI.

## Покриття функцій OpenClaw

Можливість OpenAI | Поверхня OpenClaw | Статус  
---|---|---  
Chat / Responses | провайдер моделі `openai/<model>` | Так  
Моделі підписки Codex | `openai/<model>` з OAuth `openai-codex` | Так  
Застарілі посилання на моделі Codex | `openai-codex/<model>` | Виправляються doctor до `openai/<model>`  
Harness app-server Codex | `openai/<model>` з пропущеним середовищем виконання або провайдером/моделлю `agentRuntime.id: codex` | Так  
Серверний вебпошук | Нативний інструмент OpenAI Responses | Так, коли вебпошук увімкнено й провайдера не закріплено  
Зображення | `image_generate` | Так  
Відео | `video_generate` | Так  
Перетворення тексту на мовлення | `messages.tts.provider: "openai"` / `tts` | Так  
Пакетне перетворення мовлення на текст | `tools.media.audio` / розуміння медіа | Так  
Потокове перетворення мовлення на текст | Voice Call `streaming.provider: "openai"` | Так  
Голос realtime | Voice Call `realtime.provider: "openai"` / Control UI Talk | Так  
Embeddings | провайдер embeddings пам’яті | Так  
  
## Embeddings пам’яті

OpenClaw може використовувати OpenAI або OpenAI-сумісну endpoint embeddings для індексування `memory_search` і embeddings запитів:

json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        provider: "openai",        model: "text-embedding-3-small",      },    },  },}
[/code]

Для OpenAI-сумісних endpoint, які потребують асиметричних міток embeddings, задайте `queryInputType` і `documentInputType` у `memorySearch`. OpenClaw передає їх як специфічні для провайдера поля запиту `input_type`: embeddings запитів використовують `queryInputType`; індексовані фрагменти пам’яті та пакетне індексування використовують `documentInputType`. Повний приклад див. у [довіднику конфігурації пам’яті](</uk/reference/memory-config#provider-specific-config>).

## Початок роботи

Виберіть бажаний метод автентифікації та виконайте кроки налаштування.

### Ключ API (OpenAI Platform)

**Найкраще для:** прямого доступу до API та оплати за використання.

* ### Отримайте ключ API

Створіть або скопіюйте ключ API з [панелі OpenAI Platform](<https://platform.openai.com/api-keys>).

* ### Запустіть онбординг

bashCopy code
[code]
    openclaw onboard --auth-choice openai-api-key
[/code]

Або передайте ключ напряму:

bashCopy code
[code]
    openclaw onboard --openai-api-key "$OPENAI_API_KEY"
[/code]

* ### Перевірте, що модель доступна

bashCopy code
[code]
    openclaw models list --provider openai
[/code]

### Підсумок маршруту

Посилання на модель | Конфігурація середовища виконання | Маршрут | Автентифікація  
---|---|---|---  
`openai/gpt-5.5` | пропущено / провайдер/модель `agentRuntime.id: "codex"` | Harness app-server Codex | Codex-сумісний профіль OpenAI  
`openai/gpt-5.4-mini` | пропущено / провайдер/модель `agentRuntime.id: "codex"` | Harness app-server Codex | Codex-сумісний профіль OpenAI  
`openai/gpt-5.5` | провайдер/модель `agentRuntime.id: "pi"` | Вбудоване середовище виконання PI | профіль `openai` або вибраний профіль `openai-codex`  
  
### Приклад конфігурації

json5Copy code
[code]
    {  env: { OPENAI_API_KEY: "sk-..." },  agents: { defaults: { model: { primary: "openai/gpt-5.5" } } },}
[/code]

Щоб спробувати поточну модель Instant ChatGPT з OpenAI API, задайте модель як `openai/chat-latest`:

json5Copy code
[code]
    {  env: { OPENAI_API_KEY: "sk-..." },  agents: { defaults: { model: { primary: "openai/chat-latest" } } },}
[/code]

`chat-latest` \- це рухомий псевдонім. OpenAI документує його як найновішу модель Instant, що використовується в ChatGPT, і рекомендує `gpt-5.5` для виробничого використання API, тому залишайте `openai/gpt-5.5` стабільним стандартним значенням, якщо вам явно не потрібна поведінка цього псевдоніма. Наразі псевдонім приймає лише текстову докладність `medium`, тому OpenClaw нормалізує несумісні перевизначення текстової докладності OpenAI для цієї моделі.

### Підписка Codex

**Найкраще для:** використання вашої підписки ChatGPT/Codex із нативним виконанням на app-server Codex замість окремого API-ключа. Хмара Codex вимагає входу в ChatGPT.

* ### Запустіть Codex OAuth

bashCopy code
[code]
    openclaw onboard --auth-choice openai-codex
[/code]

Або запустіть OAuth напряму:

bashCopy code
[code]
    openclaw models auth login --provider openai-codex
[/code]

Для headless або несумісних із callback налаштувань додайте `--device-code`, щоб увійти через device-code flow ChatGPT замість browser callback localhost:

bashCopy code
[code]
    openclaw models auth login --provider openai-codex --device-code
[/code]

* ### Використайте канонічний маршрут моделі OpenAI

bashCopy code
[code]
    openclaw config set agents.defaults.model.primary openai/gpt-5.5
[/code]

Для типового шляху конфігурація runtime не потрібна. Ходи агента OpenAI автоматично вибирають нативний runtime app-server Codex, а OpenClaw встановлює або відновлює вбудований plugin Codex, коли вибрано цей маршрут.

* ### Перевірте, що автентифікація Codex доступна

bashCopy code
[code]
    openclaw models list --provider openai-codex
[/code]

Після запуску gateway надішліть `/codex status` або `/codex models` у чаті, щоб перевірити нативний runtime app-server.

### Підсумок маршруту

Посилання на модель | Конфігурація runtime | Маршрут | Автентифікація  
---|---|---|---  
`openai/gpt-5.5` | пропущено / provider/model `agentRuntime.id: "codex"` | Нативний harness app-server Codex | Вхід Codex або впорядкований профіль автентифікації `openai`  
`openai/gpt-5.5` | provider/model `agentRuntime.id: "pi"` | Вбудований runtime PI з внутрішнім транспортом Codex-auth | Вибраний профіль `openai-codex`  
`openai-codex/gpt-5.5` | відновлено doctor | Застарілий маршрут, переписаний на `openai/gpt-5.5` | Наявний профіль `openai-codex`  
  
### Приклад конфігурації

json5Copy code
[code]
    {  plugins: { entries: { codex: { enabled: true } } },  agents: {    defaults: {      model: { primary: "openai/gpt-5.5" },    },  },}
[/code]

З резервним API-ключем залиште модель на `openai/gpt-5.5` і розмістіть порядок автентифікації в `openai`. OpenClaw спершу спробує підписку, потім API-ключ, залишаючись у harness Codex:

json5Copy code
[code]
    {  plugins: { entries: { codex: { enabled: true } } },  agents: {    defaults: {      model: { primary: "openai/gpt-5.5" },    },  },  auth: {    order: {      openai: [        "openai-codex:user@example.com",        "openai:api-key-backup",      ],    },  },}
[/code]

### Перевірка та відновлення маршрутизації Codex OAuth

Використайте ці команди, щоб побачити, яку модель, runtime і маршрут автентифікації використовує ваш типовий агент:

bashCopy code
[code]
    openclaw models statusopenclaw models auth list --provider openai-codexopenclaw config get agents.defaults.model --jsonopenclaw config get models.providers.openai.agentRuntime --json
[/code]

Для конкретного агента додайте `--agent <id>`:

bashCopy code
[code]
    openclaw models status --agent <id>openclaw models auth list --agent <id> --provider openai-codex
[/code]

Якщо старіша конфігурація досі має `openai-codex/gpt-*` або застаріле закріплення сесії OpenAI PI без явної конфігурації runtime, відновіть її:

bashCopy code
[code]
    openclaw doctor --fixopenclaw config validate
[/code]

Якщо `models auth list --provider openai-codex` не показує придатного профілю, увійдіть знову:

bashCopy code
[code]
    openclaw models auth login --provider openai-codexopenclaw models status --probe --probe-provider openai-codex
[/code]

`openai/*` — це маршрут моделі для ходів агента OpenAI через Codex. Ідентифікатор провайдера автентифікації/профілю `openai-codex` залишається прийнятним для наявних профілів і списків CLI.

### Індикатор стану

Чатова команда `/status` показує, який runtime моделі активний для поточної сесії. Вбудований harness app-server Codex відображається як `Runtime: OpenAI Codex` для ходів моделей агента OpenAI. Застарілі закріплення сесій PI відновлюються до Codex, якщо конфігурація явно не закріплює PI.

### Попередження doctor

Якщо маршрути `openai-codex/*` або застарілі закріплення OpenAI PI залишаються в конфігурації чи стані сесії, `openclaw doctor --fix` переписує їх на `openai/*` із runtime Codex, якщо PI не налаштовано явно.

### Обмеження контекстного вікна

OpenClaw розглядає metadata моделі та обмеження runtime context як окремі значення.

Для `openai/gpt-5.5` через каталог Codex OAuth:

  * Нативне `contextWindow`: `1000000`
  * Типове обмеження runtime `contextTokens`: `272000`


Менше типове обмеження на практиці має кращі характеристики затримки та якості. Перевизначте його за допомогою `contextTokens`:

json5Copy code
[code]
    {  models: {    providers: {      "openai-codex": {        models: [{ id: "gpt-5.5", contextTokens: 160000 }],      },    },  },}
[/code]

### Відновлення каталогу

OpenClaw використовує upstream metadata каталогу Codex для `gpt-5.5`, коли вони наявні. Якщо live discovery Codex пропускає рядок `gpt-5.5`, тоді як обліковий запис автентифіковано, OpenClaw синтезує цей рядок моделі OAuth, щоб запуски cron, sub-agent і налаштованої типової моделі не завершувалися помилкою `Unknown model`.

## Нативна автентифікація app-server Codex

Нативний harness app-server Codex використовує посилання на моделі `openai/*` плюс пропущену конфігурацію runtime або provider/model `agentRuntime.id: "codex"`, але його автентифікація все ще базується на обліковому записі. OpenClaw вибирає автентифікацію в такому порядку:

  1. Впорядковані профілі автентифікації OpenAI для агента, бажано в `auth.order.openai`. Наявні профілі `openai-codex:*` і `auth.order.openai-codex` залишаються чинними для старіших інсталяцій.
  2. Наявний обліковий запис app-server, наприклад локальний вхід Codex CLI ChatGPT.
  3. Лише для локальних запусків app-server stdio: `CODEX_API_KEY`, потім `OPENAI_API_KEY`, коли app-server повідомляє, що облікового запису немає, але все ще потребує автентифікації OpenAI.


Це означає, що локальний вхід за підпискою ChatGPT/Codex не замінюється лише тому, що процес gateway також має `OPENAI_API_KEY` для прямих моделей OpenAI або embeddings. Резервний API-ключ із env використовується лише в локальному stdio-шляху без облікового запису; він не надсилається до WebSocket-з'єднань app-server. Коли вибрано профіль Codex у стилі підписки, OpenClaw також прибирає `CODEX_API_KEY` і `OPENAI_API_KEY` із породженого дочірнього процесу stdio app-server і надсилає вибрані облікові дані через RPC входу app-server. Коли цей профіль підписки заблоковано лімітом використання Codex, OpenClaw може перейти до наступного впорядкованого профілю API-ключа `openai:*` без зміни вибраної моделі або виходу з harness Codex. Після проходження часу скидання підписки профіль підписки знову стає придатним.

## Генерація зображень

Вбудований plugin `openai` реєструє генерацію зображень через інструмент `image_generate`. Він підтримує як генерацію зображень через API-ключ OpenAI, так і генерацію зображень через Codex OAuth за допомогою того самого посилання на модель `openai/gpt-image-2`.

Можливість | API-ключ OpenAI | Codex OAuth  
---|---|---  
Посилання на модель | `openai/gpt-image-2` | `openai/gpt-image-2`  
Автентифікація | `OPENAI_API_KEY` | Вхід OpenAI Codex OAuth  
Транспорт | OpenAI Images API | backend Codex Responses  
Максимум зображень на запит | 4 | 4  
Режим редагування | Увімкнено (до 5 референсних зображень) | Увімкнено (до 5 референсних зображень)  
Перевизначення розміру | Підтримуються, зокрема розміри 2K/4K | Підтримуються, зокрема розміри 2K/4K  
Співвідношення сторін / роздільна здатність | Не пересилається до OpenAI Images API | Зіставляється з підтримуваним розміром, коли це безпечно  
json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: { primary: "openai/gpt-image-2" },    },  },}
[/code]

`gpt-image-2` є типовим для генерації зображень із тексту OpenAI та редагування зображень. `gpt-image-1.5`, `gpt-image-1` і `gpt-image-1-mini` залишаються придатними як явні перевизначення моделі. Використовуйте `openai/gpt-image-1.5` для виводу PNG/WebP із прозорим фоном; поточний API `gpt-image-2` відхиляє `background: "transparent"`.

Для запиту з прозорим фоном агенти мають викликати `image_generate` з `model: "openai/gpt-image-1.5"`, `outputFormat: "png"` або `"webp"` і `background: "transparent"`; старіший параметр провайдера `openai.background` все ще приймається. OpenClaw також захищає публічні маршрути OpenAI та OpenAI Codex OAuth, переписуючи типові прозорі запити `openai/gpt-image-2` на `gpt-image-1.5`; Azure і власні OpenAI-сумісні endpoints зберігають свої налаштовані deployment/model names.

Те саме налаштування доступне для headless запусків CLI:

bashCopy code
[code]
    openclaw infer image generate \  --model openai/gpt-image-1.5 \  --output-format png \  --background transparent \  --prompt "A simple red circle sticker on a transparent background" \  --json
[/code]

Використовуйте ті самі прапорці `--output-format` і `--background` з `openclaw infer image edit`, коли починаєте з вхідного файлу. `--openai-background` залишається доступним як специфічний для OpenAI alias.

Для інсталяцій Codex OAuth залишайте те саме посилання `openai/gpt-image-2`. Коли налаштовано OAuth-профіль `openai-codex`, OpenClaw розв'язує цей збережений access token OAuth і надсилає запити зображень через backend Codex Responses. Він не пробує спершу `OPENAI_API_KEY` і не переходить мовчки на API-ключ для цього запиту. Налаштуйте `models.providers.openai` явно з API-ключем, власним base URL або Azure endpoint, коли потрібен прямий маршрут OpenAI Images API. Якщо цей власний image endpoint перебуває в довіреній LAN/приватній адресі, також установіть `browser.ssrfPolicy.dangerouslyAllowPrivateNetwork: true`; OpenClaw залишає приватні/внутрішні OpenAI-сумісні image endpoints заблокованими, якщо ця opt-in опція відсутня.

Згенерувати:

CodeCopy code
[code]
    /tool image_generate model=openai/gpt-image-2 prompt="A polished launch poster for OpenClaw on macOS" size=3840x2160 count=1
[/code]

Згенерувати прозорий PNG:

CodeCopy code
[code]
    /tool image_generate model=openai/gpt-image-1.5 prompt="A simple red circle sticker on a transparent background" outputFormat=png background=transparent
[/code]

Редагувати:

CodeCopy code
[code]
    /tool image_generate model=openai/gpt-image-2 prompt="Preserve the object shape, change the material to translucent glass" image=/path/to/reference.png size=1024x1536
[/code]

## Генерація відео

Вбудований Plugin `openai` реєструє генерацію відео через інструмент `video_generate`.

Можливість | Значення  
---|---  
Модель за замовчуванням | `openai/sora-2`  
Режими | Текст-у-відео, зображення-у-відео, редагування одного відео  
Референсні вхідні дані | 1 зображення або 1 відео  
Перевизначення розміру | Підтримується  
Інші перевизначення | `aspectRatio`, `resolution`, `audio`, `watermark` ігноруються з попередженням інструмента  
json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: { primary: "openai/sora-2" },    },  },}
[/code]

## Внесок промпта GPT-5

OpenClaw додає спільний внесок промпта GPT-5 для запусків сімейства GPT-5 у різних постачальників. Він застосовується за ідентифікатором моделі, тому `openai/gpt-5.5`, застарілі refs до repair, як-от `openai-codex/gpt-5.5`, `openrouter/openai/gpt-5.5`, `opencode/gpt-5.5`, та інші сумісні refs GPT-5 отримують той самий overlay. Старіші моделі GPT-4.x не отримують його.

Вбудований нативний harness Codex використовує ту саму поведінку GPT-5 і overlay heartbeat через інструкції розробника app-server Codex, тому сеанси `openai/gpt-5.x`, спрямовані через Codex, зберігають ті самі настанови щодо доведення дій до кінця та проактивного heartbeat, хоча рештою промпта harness володіє Codex.

Внесок GPT-5 додає тегований контракт поведінки для сталості persona, безпеки виконання, дисципліни інструментів, форми виводу, перевірок завершення та верифікації. Поведінка відповідей для конкретних каналів і тихих повідомлень лишається у спільному системному промпті OpenClaw та політиці вихідної доставки. Настанови GPT-5 завжди ввімкнені для відповідних моделей. Дружній шар стилю взаємодії є окремим і налаштовуваним.

Значення | Ефект  
---|---  
`"friendly"` (за замовчуванням) | Увімкнути дружній шар стилю взаємодії  
`"on"` | Псевдонім для `"friendly"`  
`"off"` | Вимкнути лише дружній шар стилю  
  
### Конфігурація

json5Copy code
[code]
    {  agents: {    defaults: {      promptOverlays: {        gpt5: { personality: "friendly" },      },    },  },}
[/code]

### CLI

bashCopy code
[code]
    openclaw config set agents.defaults.promptOverlays.gpt5.personality off
[/code]

## Голос і мовлення

Синтез мовлення (TTS)

Вбудований Plugin `openai` реєструє синтез мовлення для поверхні `messages.tts`.

Налаштування | Шлях конфігурації | За замовчуванням  
---|---|---  
Модель | `messages.tts.providers.openai.model` | `gpt-4o-mini-tts`  
Голос | `messages.tts.providers.openai.voice` | `coral`  
Швидкість | `messages.tts.providers.openai.speed` | (не задано)  
Інструкції | `messages.tts.providers.openai.instructions` | (не задано, лише `gpt-4o-mini-tts`)  
Формат | `messages.tts.providers.openai.responseFormat` | `opus` для голосових нотаток, `mp3` для файлів  
API-ключ | `messages.tts.providers.openai.apiKey` | Повертається до `OPENAI_API_KEY`  
Базова URL-адреса | `messages.tts.providers.openai.baseUrl` | `https://api.openai.com/v1`  
Додаткове тіло | `messages.tts.providers.openai.extraBody` / `extra_body` | (не задано)  
  
Доступні моделі: `gpt-4o-mini-tts`, `tts-1`, `tts-1-hd`. Доступні голоси: `alloy`, `ash`, `ballad`, `cedar`, `coral`, `echo`, `fable`, `juniper`, `marin`, `onyx`, `nova`, `sage`, `shimmer`, `verse`.

`extraBody` об'єднується з JSON запиту `/audio/speech` після згенерованих OpenClaw полів, тож використовуйте його для OpenAI-сумісних endpoint, які потребують додаткових ключів, як-от `lang`. Ключі прототипу ігноруються.

json5Copy code
[code]
    {  messages: {    tts: {      providers: {        openai: { model: "gpt-4o-mini-tts", voice: "coral" },      },    },  },}
[/code]

Перетворення мовлення на текст

Вбудований Plugin `openai` реєструє пакетне перетворення мовлення на текст через поверхню транскрибування media-understanding OpenClaw.

  * Модель за замовчуванням: `gpt-4o-transcribe`
  * Endpoint: OpenAI REST `/v1/audio/transcriptions`
  * Шлях вхідних даних: завантаження аудіофайлу multipart
  * Підтримується OpenClaw усюди, де транскрибування вхідного аудіо використовує `tools.media.audio`, зокрема сегменти голосових каналів Discord і аудіовкладення каналів


Щоб примусово використовувати OpenAI для транскрибування вхідного аудіо:

json5Copy code
[code]
    {  tools: {    media: {      audio: {        models: [          {            type: "provider",            provider: "openai",            model: "gpt-4o-transcribe",          },        ],      },    },  },}
[/code]

Підказки щодо мови та промпта передаються до OpenAI, коли їх надано через спільну конфігурацію аудіомедіа або запит транскрибування для окремого виклику.

Транскрипція в реальному часі

Вбудований Plugin `openai` реєструє транскрипцію в реальному часі для Plugin Voice Call.

Налаштування | Шлях конфігурації | Типове значення  
---|---|---  
Модель | `plugins.entries.voice-call.config.streaming.providers.openai.model` | `gpt-4o-transcribe`  
Мова | `...openai.language` | (не встановлено)  
Prompt | `...openai.prompt` | (не встановлено)  
Тривалість тиші | `...openai.silenceDurationMs` | `800`  
Поріг VAD | `...openai.vadThreshold` | `0.5`  
Автентифікація | `...openai.apiKey`, `OPENAI_API_KEY`, або OAuth `openai-codex` | API-ключі підключаються напряму; OAuth створює клієнтський секрет Realtime transcription  
Голос у реальному часі

Вбудований Plugin `openai` реєструє голос у реальному часі для Plugin Voice Call.

Налаштування | Шлях конфігурації | Типове значення  
---|---|---  
Модель | `plugins.entries.voice-call.config.realtime.providers.openai.model` | `gpt-realtime-2`  
Голос | `...openai.voice` | `alloy`  
Температура (міст розгортання Azure) | `...openai.temperature` | `0.8`  
Поріг VAD | `...openai.vadThreshold` | `0.5`  
Тривалість тиші | `...openai.silenceDurationMs` | `500`  
Префіксне доповнення | `...openai.prefixPaddingMs` | `300`  
Зусилля reasoning | `...openai.reasoningEffort` | (не встановлено)  
Автентифікація | `...openai.apiKey`, `OPENAI_API_KEY`, або OAuth `openai-codex` | Browser Talk і не-Azure backend-мости можуть використовувати Codex OAuth  
  
Доступні вбудовані Realtime-голоси для `gpt-realtime-2`: `alloy`, `ash`, `ballad`, `coral`, `echo`, `sage`, `shimmer`, `verse`, `marin`, `cedar`. OpenAI рекомендує `marin` і `cedar` для найкращої якості Realtime. Це окремий набір від голосів Text-to-speech вище; не припускайте, що TTS голос, як-от `fable`, `nova` або `onyx`, дійсний для Realtime-сесій.

## Кінцеві точки Azure OpenAI

Вбудований провайдер `openai` може спрямовувати генерацію зображень до ресурсу Azure OpenAI через перевизначення базової URL-адреси. На шляху генерації зображень OpenClaw виявляє імена хостів Azure у `models.providers.openai.baseUrl` і автоматично перемикається на форму запиту Azure.

Використовуйте Azure OpenAI, коли:

  * У вас уже є підписка Azure OpenAI, квота або корпоративна угода
  * Вам потрібні регіональне розміщення даних або засоби контролю відповідності, які надає Azure
  * Ви хочете залишити трафік усередині наявного клієнтського середовища Azure


### Конфігурація

Для генерації зображень Azure через вбудований провайдер `openai` вкажіть `models.providers.openai.baseUrl` на ваш ресурс Azure і встановіть `apiKey` як ключ Azure OpenAI (не ключ OpenAI Platform):

json5Copy code
[code]
    {  models: {    providers: {      openai: {        baseUrl: "https://<your-resource>.openai.azure.com",        apiKey: "<azure-openai-api-key>",      },    },  },}
[/code]

OpenClaw розпізнає ці суфікси хостів Azure для маршруту генерації зображень Azure:

  * `*.openai.azure.com`
  * `*.services.ai.azure.com`
  * `*.cognitiveservices.azure.com`


Для запитів генерації зображень на розпізнаному хості Azure OpenClaw:

  * Надсилає заголовок `api-key` замість `Authorization: Bearer`
  * Використовує шляхи з областю розгортання (`/openai/deployments/{deployment}/...`)
  * Додає `?api-version=...` до кожного запиту
  * Використовує типовий тайм-аут запиту 600 с для викликів генерації зображень Azure. Значення `timeoutMs` для окремих викликів усе ще перевизначають це типове значення.


Інші базові URL-адреси (публічний OpenAI, OpenAI-сумісні проксі) зберігають стандартну форму запиту зображень OpenAI.

### Версія API

Установіть `AZURE_OPENAI_API_VERSION`, щоб зафіксувати конкретну preview- або GA-версію Azure для шляху генерації зображень Azure:

bashCopy code
[code]
    export AZURE_OPENAI_API_VERSION="2024-12-01-preview"
[/code]

Типове значення — `2024-12-01-preview`, коли змінну не встановлено.

### Назви моделей є назвами розгортань

Azure OpenAI прив’язує моделі до розгортань. Для запитів генерації зображень Azure, маршрутизованих через вбудований провайдер `openai`, поле `model` в OpenClaw має бути **назвою розгортання Azure** , яку ви налаштували на порталі Azure, а не публічним ідентифікатором моделі OpenAI.

Якщо ви створите розгортання з назвою `gpt-image-2-prod`, яке обслуговує `gpt-image-2`:

CodeCopy code
[code]
    /tool image_generate model=openai/gpt-image-2-prod prompt="A clean poster" size=1024x1024 count=1
[/code]

Те саме правило щодо назви розгортання застосовується до викликів генерації зображень, маршрутизованих через вбудований провайдер `openai`.

### Регіональна доступність

Генерація зображень Azure наразі доступна лише в підмножині регіонів (наприклад, `eastus2`, `swedencentral`, `polandcentral`, `westus3`, `uaenorth`). Перевірте поточний список регіонів Microsoft перед створенням розгортання та підтвердьте, що конкретна модель доступна у вашому регіоні.

### Відмінності параметрів

Azure OpenAI і публічний OpenAI не завжди приймають однакові параметри зображень. Azure може відхиляти параметри, які дозволяє публічний OpenAI (наприклад, певні значення `background` для `gpt-image-2`), або надавати їх лише для конкретних версій моделей. Ці відмінності походять від Azure і базової моделі, а не від OpenClaw. Якщо запит Azure завершується помилкою валідації, перевірте набір параметрів, підтримуваний вашим конкретним розгортанням і версією API на порталі Azure.

## Розширена конфігурація

Transport (WebSocket vs SSE)

OpenClaw спершу використовує WebSocket із запасним переходом на SSE (`"auto"`) для `openai/*`.

У режимі `"auto"` OpenClaw:

  * Повторює одну ранню помилку WebSocket перед переходом на SSE
  * Після помилки позначає WebSocket як деградований приблизно на 60 секунд і використовує SSE під час охолодження
  * Додає стабільні заголовки ідентичності сеансу й ходу для повторів і повторних підключень
  * Нормалізує лічильники використання (`input_tokens` / `prompt_tokens`) між варіантами транспорту

Значення | Поведінка  
---|---  
`"auto"` (типово) | Спершу WebSocket, запасний перехід на SSE  
`"sse"` | Примусово лише SSE  
`"websocket"` | Примусово лише WebSocket  
json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "openai/gpt-5.5": {          params: { transport: "auto" },        },      },    },  },}
[/code]

Пов’язана документація OpenAI:

  * [Realtime API з WebSocket](<https://platform.openai.com/docs/guides/realtime-websocket>)
  * [Потокові відповіді API (SSE)](<https://platform.openai.com/docs/guides/streaming-responses>)

Fast mode

OpenClaw надає спільний перемикач fast-mode для `openai/*`:

  * **Chat/UI:** `/fast status|on|off`
  * **Конфігурація:** `agents.defaults.models["<provider>/<model>"].params.fastMode`


Коли його ввімкнено, OpenClaw зіставляє fast mode з пріоритетною обробкою OpenAI (`service_tier = "priority"`). Наявні значення `service_tier` зберігаються, і fast mode не переписує `reasoning` або `text.verbosity`.

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "openai/gpt-5.5": { params: { fastMode: true } },      },    },  },}
[/code]

Пріоритетна обробка (service_tier)

API OpenAI надає пріоритетну обробку через `service_tier`. Задайте її для кожної моделі в OpenClaw:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "openai/gpt-5.5": { params: { serviceTier: "priority" } },      },    },  },}
[/code]

Підтримувані значення: `auto`, `default`, `flex`, `priority`.

Server-side compaction (Responses API)

Для прямих моделей OpenAI Responses (`openai/*` на `api.openai.com`) stream-обгортка Pi-harness Plugin OpenAI автоматично вмикає server-side compaction:

  * Примусово задає `store: true` (якщо compat моделі не задає `supportsStore: false`)
  * Впроваджує `context_management: [{ type: "compaction", compact_threshold: ... }]`
  * Типове значення `compact_threshold`: 70% від `contextWindow` (або `80000`, коли недоступно)


Це застосовується до вбудованого шляху Pi harness і до хуків провайдера OpenAI, які використовуються вбудованими запусками. Нативний harness app-server Codex керує власним контекстом через Codex і налаштовується типовим маршрутом агента OpenAI або runtime-політикою провайдера/моделі.

### Увімкнути явно

Корисно для сумісних кінцевих точок, таких як Azure OpenAI Responses:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "azure-openai-responses/gpt-5.5": {          params: { responsesServerCompaction: true },        },      },    },  },}
[/code]

### Власний поріг

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "openai/gpt-5.5": {          params: {            responsesServerCompaction: true,            responsesCompactThreshold: 120000,          },        },      },    },  },}
[/code]

### Вимкнути

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "openai/gpt-5.5": {          params: { responsesServerCompaction: false },        },      },    },  },}
[/code]

Режим strict-agentic GPT

Для запусків сімейства GPT-5 на `openai/*` OpenClaw може використовувати суворіший контракт вбудованого виконання:

json5Copy code
[code]
    {  agents: {    defaults: {      embeddedPi: { executionContract: "strict-agentic" },    },  },}
[/code]

З `strict-agentic` OpenClaw:

  * Більше не вважає хід лише з планом успішним прогресом, коли доступна дія інструмента
  * Повторює хід із підказкою діяти зараз
  * Автоматично вмикає `update_plan` для суттєвої роботи
  * Показує явний заблокований стан, якщо модель продовжує планувати без дії

Нативні маршрути проти OpenAI-сумісних маршрутів

OpenClaw обробляє прямі кінцеві точки OpenAI, Codex і Azure OpenAI інакше, ніж загальні OpenAI-сумісні проксі `/v1`:

**Нативні маршрути** (`openai/*`, Azure OpenAI):

  * Зберігають `reasoning: { effort: "none" }` лише для моделей, які підтримують OpenAI `none` effort
  * Пропускають вимкнений reasoning для моделей або проксі, що відхиляють `reasoning.effort: "none"`
  * За замовчуванням використовують строгий режим для схем інструментів
  * Додають приховані заголовки атрибуції лише на перевірених нативних хостах
  * Зберігають формування запитів, специфічне для OpenAI (`service_tier`, `store`, reasoning-compat, підказки prompt-cache)


**Проксі/сумісні маршрути:**

  * Використовують м’якшу compat-поведінку
  * Вилучають Completions `store` з ненативних payload `openai-completions`
  * Приймають наскрізний JSON `params.extra_body`/`params.extraBody` для OpenAI-сумісних проксі Completions
  * Приймають `params.chat_template_kwargs` для OpenAI-сумісних проксі Completions, таких як vLLM
  * Не примушують строгі схеми інструментів або лише нативні заголовки


Azure OpenAI використовує нативний транспорт і compat-поведінку, але не отримує приховані заголовки атрибуції.

## Пов’язане

[**Вибір моделі** Вибір провайдерів, посилань на моделі та поведінки failover. ](</uk/concepts/model-providers>) [**Генерація зображень** Спільні параметри інструмента зображень і вибір провайдера. ](</uk/tools/image-generation>) [**Генерація відео** Спільні параметри інструмента відео та вибір провайдера. ](</uk/tools/video-generation>) [**OAuth і auth** Подробиці auth і правила повторного використання облікових даних. ](</uk/gateway/authentication>)

Was this useful?YesNo