---
title: Заплановані завдання
source_url: https://docs.openclaw.ai/uk/automation/cron-jobs
scraped_at: 2026-05-25
---

Cron — це вбудований планувальник Gateway. Він зберігає завдання, пробуджує агента в потрібний час і може доставляти вивід назад у канал чату або кінцеву точку webhook.

## Швидкий старт

* ### Додайте одноразове нагадування

bashCopy code
[code]
    openclaw cron add \  --name "Reminder" \  --at "2026-02-01T16:00:00Z" \  --session main \  --system-event "Reminder: check the cron docs draft" \  --wake now \  --delete-after-run
[/code]

* ### Перевірте свої завдання

bashCopy code
[code]
    openclaw cron listopenclaw cron get <job-id>openclaw cron show <job-id>
[/code]

* ### Перегляньте історію запусків

bashCopy code
[code]
    openclaw cron runs --id <job-id>
[/code]

## Як працює cron

  * Cron працює **всередині процесу Gateway** (не всередині моделі).
  * Визначення завдань зберігаються в `~/.openclaw/cron/jobs.json`, тому перезапуски не втрачають розклади.
  * Стан виконання під час роботи зберігається поруч у `~/.openclaw/cron/jobs-state.json`. Якщо ви відстежуєте визначення cron у git, відстежуйте `jobs.json` і додайте `jobs-state.json` до gitignore.
  * Після розділення старіші версії OpenClaw можуть читати `jobs.json`, але можуть сприймати завдання як нові, оскільки поля runtime тепер зберігаються в `jobs-state.json`.
  * Коли `jobs.json` редагують під час роботи Gateway або коли його зупинено, OpenClaw порівнює змінені поля розкладу з метаданими pending runtime slot і очищає застарілі значення `nextRunAtMs`. Перезаписи, що змінюють лише форматування або порядок ключів, зберігають pending slot.
  * Усі виконання cron створюють записи [фонового завдання](</uk/automation/tasks>).
  * Під час запуску Gateway прострочені ізольовані завдання agent-turn переплановуються за межі вікна підключення каналу, а не відтворюються негайно, тому запуск Discord/Telegram і налаштування native-command залишаються чутливими після перезапусків.
  * Одноразові завдання (`--at`) типово автоматично видаляються після успішного виконання.
  * Ізольовані запуски cron за принципом best-effort закривають відстежувані вкладки/процеси браузера для своєї сесії `cron:<jobId>` після завершення запуску, щоб від’єднана автоматизація браузера не залишала осиротілі процеси.
  * Ізольовані запуски cron, які отримують вузький дозвіл cron self-cleanup grant, усе ще можуть читати статус планувальника, self-filtered список свого поточного завдання та історію запусків цього завдання, щоб перевірки статусу/Heartbeat могли переглядати власний розклад без ширшого доступу до мутацій cron.
  * Ізольовані запуски cron також захищаються від застарілих відповідей-підтверджень. Якщо перший результат — це лише проміжне оновлення статусу (`on it`, `pulling everything together` і подібні підказки), і жоден дочірній subagent run більше не відповідає за фінальну відповідь, OpenClaw один раз повторно запитує фактичний результат перед доставкою.
  * Ізольовані запуски cron надають перевагу структурованим метаданим execution-denial із вбудованого запуску, а потім повертаються до відомих маркерів фінального підсумку/виводу, як-от `SYSTEM_RUN_DENIED` і `INVALID_REQUEST`, тому заблокована команда не звітується як успішний запуск.
  * Ізольовані запуски cron також розглядають помилки агента на рівні запуску як помилки завдання, навіть коли payload відповіді не створено, тому збої моделі/провайдера збільшують лічильники помилок і запускають сповіщення про збій замість того, щоб позначати завдання як успішне.
  * Коли ізольоване завдання agent-turn досягає `timeoutSeconds`, cron перериває базовий запуск агента й надає йому коротке вікно очищення. Якщо запуск не завершує draining, очищення під керуванням Gateway примусово очищає право власності цієї сесії на запуск перед тим, як cron запише тайм-аут, щоб робота чату в черзі не залишилася за застарілою processing session.
  * Якщо ізольований agent-turn зависає до старту runner або до першого виклику моделі, cron записує фазово-специфічний тайм-аут, як-от `setup timed out before runner start` або `stalled before first model call (last phase: context-engine)`. Ці watchdogs покривають вбудованих провайдерів і CLI-backed провайдерів до фактичного запуску їхнього зовнішнього CLI-процесу та обмежуються незалежно від довгих значень `timeoutSeconds`, щоб збої cold-start/auth/context проявлялися швидко, а не чекали повного бюджету завдання.


## Типи розкладів

Вид | Прапорець CLI | Опис  
---|---|---  
`at` | `--at` | Одноразова позначка часу (ISO 8601 або відносна, як `20m`)  
`every` | `--every` | Фіксований інтервал  
`cron` | `--cron` | 5-польовий або 6-польовий cron-вираз з необов’язковим `--tz`  
  
Позначки часу без часового поясу трактуються як UTC. Додайте `--tz America/New_York` для планування за локальним настінним часом.

Повторювані вирази на початку години автоматично розподіляються з відхиленням до 5 хвилин, щоб зменшити піки навантаження. Використовуйте `--exact`, щоб примусово задати точний час, або `--stagger 30s` для явного вікна.

### Day-of-month і day-of-week використовують логіку OR

Cron-вирази розбираються за допомогою [croner](<https://github.com/Hexagon/croner>). Коли поля day-of-month і day-of-week обидва не є wildcard, croner вважає збігом ситуацію, коли збігається **будь-яке** з полів, а не обидва. Це стандартна поведінка Vixie cron.

CodeCopy code
[code]
    # Intended: "9 AM on the 15th, only if it's a Monday"# Actual:   "9 AM on every 15th, AND 9 AM on every Monday"0 9 15 * 1
[/code]

Це спрацьовує приблизно 5–6 разів на місяць замість 0–1 разу на місяць. OpenClaw тут використовує типову OR-поведінку Croner. Щоб вимагати обидві умови, використовуйте модифікатор day-of-week `+` у Croner (`0 9 15 * +1`) або плануйте за одним полем і перевіряйте інше в prompt чи команді вашого завдання.

## Стилі виконання

Стиль | Значення `--session` | Виконується в | Найкраще для  
---|---|---|---  
Основна сесія | `main` | Наступний Heartbeat turn | Нагадування, системні події  
Ізольований | `isolated` | Виділена `cron:<jobId>` | Звіти, фонові робочі завдання  
Поточна сесія | `current` | Прив’язується під час створення | Контекстно-залежна повторювана робота  
Власна сесія | `session:custom-id` | Постійна іменована сесія | Workflows, що будуються на історії  
  
Основна сесія проти ізольованої проти власної

Завдання **основної сесії** додають системну подію в чергу та за потреби пробуджують Heartbeat (`--wake now` або `--wake next-heartbeat`). Ці системні події не продовжують свіжість daily/idle reset для цільової сесії. **Ізольовані** завдання виконують виділений agent turn зі свіжою сесією. **Власні сесії** (`session:xxx`) зберігають контекст між запусками, уможливлюючи workflows на кшталт щоденних standups, що будуються на попередніх підсумках.

Що означає 'fresh session' для ізольованих завдань

Для ізольованих завдань "fresh session" означає новий transcript/session id для кожного запуску. OpenClaw може переносити безпечні налаштування, як-от thinking/fast/verbose settings, labels і явні вибрані користувачем model/auth overrides, але не успадковує навколишній контекст розмови зі старішого рядка cron: channel/group routing, send або queue policy, elevation, origin чи ACP runtime binding. Використовуйте `current` або `session:<id>`, коли повторюване завдання має навмисно будуватися на тому самому контексті розмови.

Очищення runtime

Для ізольованих завдань teardown runtime тепер включає best-effort очищення браузера для цієї cron-сесії. Збої очищення ігноруються, щоб фактичний результат cron усе одно мав пріоритет.

Ізольовані запуски cron також звільняють будь-які bundled MCP runtime instances, створені для завдання, через спільний шлях runtime-cleanup. Це відповідає тому, як teardown виконується для MCP clients основної сесії та власної сесії, тому ізольовані cron-завдання не залишають stdio child processes або довготривалі MCP connections між запусками.

Доставка subagent і Discord

Коли ізольовані запуски cron оркеструють subagents, доставка також віддає перевагу фінальному виводу нащадка над застарілим проміжним текстом батьківського процесу. Якщо нащадки усе ще виконуються, OpenClaw пригнічує це часткове оновлення батьківського процесу замість того, щоб оголошувати його.

Для text-only цілей оголошення Discord OpenClaw надсилає канонічний фінальний текст асистента один раз замість повторного відтворення і streamed/intermediate text payloads, і фінальної відповіді. Media та structured Discord payloads усе ще доставляються як окремі payloads, щоб attachments і components не втрачалися.

### Параметри payload для ізольованих завдань

Текст prompt (обов’язковий для isolated).

Перевизначення моделі; використовує вибрану дозволену модель для завдання.

Перевизначення рівня thinking.

Пропустити ін’єкцію файлів bootstrap workspace.

Обмежити, які tools може використовувати завдання, наприклад `--tools exec,read`.

`--model` використовує вибрану дозволену модель як основну модель цього завдання. Це не те саме, що перевизначення `/model` у chat-session: налаштовані fallback chains усе ще застосовуються, коли основна модель завдання дає збій. Якщо запитана модель не дозволена або не може бути resolved, cron завершує запуск з явною validation error замість мовчазного fallback до agent/default model selection завдання.

Cron-завдання також можуть містити `fallbacks` на рівні payload. Коли цей список присутній, він замінює налаштований fallback chain для завдання. Використовуйте `fallbacks: []` у job payload/API, коли потрібен строгий запуск cron, який пробує лише вибрану модель. Якщо завдання має `--model`, але не має ні payload fallbacks, ні configured fallbacks, OpenClaw передає явне порожнє fallback override, щоб agent primary не додавався як прихована додаткова retry target.

Пріоритет вибору моделі для ізольованих завдань:

  1. Перевизначення моделі Gmail hook (коли запуск надійшов із Gmail і це перевизначення дозволене)
  2. Per-job payload `model`
  3. Збережене вибране користувачем перевизначення моделі cron-сесії
  4. Вибір agent/default model


Fast mode також відповідає resolved live selection. Якщо конфіг вибраної моделі має `params.fastMode`, isolated cron типово використовує його. Збережене перевизначення сесії `fastMode` усе ще має пріоритет над config в обох напрямках.

Якщо ізольований запуск потрапляє на live model-switch handoff, cron повторює спробу з перемкненим provider/model і зберігає цей live selection для активного запуску перед retry. Коли перемикання також містить новий auth profile, cron також зберігає це auth profile override для активного запуску. Повторні спроби обмежені: після початкової спроби плюс 2 switch retries cron перериває виконання замість нескінченного циклу.

Перш ніж ізольований запуск Cron увійде до runner агента, OpenClaw перевіряє доступні локальні кінцеві точки провайдера для налаштованих провайдерів `api: "ollama"` і `api: "openai-completions"`, у яких `baseUrl` є loopback, приватною мережею або `.local`. Якщо ця кінцева точка недоступна, запуск записується як `skipped` із чіткою помилкою провайдера/моделі замість початку виклику моделі. Результат кінцевої точки кешується на 5 хвилин, тому багато запланованих завдань, що використовують той самий недоступний локальний сервер Ollama, vLLM, SGLang або LM Studio, спільно використовують одну невелику перевірку замість створення шквалу запитів. Пропущені запуски provider-preflight не збільшують backoff помилок виконання; увімкніть `failureAlert.includeSkipped`, якщо потрібні повторні сповіщення про пропуск.

## Доставка та вивід

Режим | Що відбувається  
---|---  
`announce` | Резервно доставляє фінальний текст до цілі, якщо агент не надіслав його  
`webhook` | Надсилає POST із payload події завершення на URL  
`none` | Без резервної доставки runner  
  
Використовуйте `--announce --channel telegram --to "-1001234567890"` для доставки в канал. Для тем форуму Telegram використовуйте `-1001234567890:topic:123`; прямі RPC/config виклики також можуть передавати `delivery.threadId` як рядок або число. Цілі Slack/Discord/Mattermost мають використовувати явні префікси (`channel:<id>`, `user:<id>`). ID кімнат Matrix чутливі до регістру; використовуйте точний ID кімнати або форму `room:!room:server` з Matrix.

Коли доставка announce використовує `channel: "last"` або пропускає `channel`, ціль із префіксом провайдера, наприклад `telegram:123`, може вибрати канал до того, як Cron повернеться до історії сесії або одного налаштованого каналу. Лише префікси, оголошені завантаженим Plugin, є селекторами провайдера. Якщо `delivery.channel` задано явно, префікс цілі має називати того самого провайдера; наприклад, `channel: "whatsapp"` із `to: "telegram:123"` відхиляється замість того, щоб дозволити WhatsApp інтерпретувати Telegram ID як номер телефону. Префікси типу цілі та сервісу, як-от `channel:<id>`, `user:<id>`, `imessage:<handle>` і `sms:<number>`, залишаються синтаксисом цілей, яким володіє канал, а не селекторами провайдера.

Для ізольованих завдань доставка в чат є спільною. Якщо маршрут чату доступний, агент може використовувати інструмент `message`, навіть коли завдання використовує `--no-deliver`. Якщо агент надсилає до налаштованої/поточної цілі, OpenClaw пропускає резервний announce. Інакше `announce`, `webhook` і `none` керують лише тим, що runner робить із фінальною відповіддю після ходу агента.

Коли агент створює ізольоване нагадування з активного чату, OpenClaw зберігає збережену живу ціль доставки для резервного маршруту announce. Внутрішні ключі сесії можуть бути в нижньому регістрі; цілі доставки провайдера не реконструюються з цих ключів, коли доступний поточний контекст чату.

Неявна доставка announce використовує налаштовані allowlists каналів для валідації та перемаршрутизації застарілих цілей. Схвалення зі сховища пар DM не є одержувачами резервної автоматизації; задайте `delivery.to` або налаштуйте запис `allowFrom` каналу, коли заплановане завдання має проактивно надсилати в DM.

Сповіщення про помилки мають окремий шлях призначення:

  * `cron.failureDestination` задає глобальне значення за замовчуванням для сповіщень про помилки.
  * `job.delivery.failureDestination` перевизначає його для окремого завдання.
  * Якщо жодне не задано, а завдання вже доставляє через `announce`, сповіщення про помилки тепер повертаються до цієї основної цілі announce.
  * `delivery.failureDestination` підтримується лише для завдань `sessionTarget="isolated"`, якщо основний режим доставки не є `webhook`.
  * `failureAlert.includeSkipped: true` вмикає для завдання або глобальної політики сповіщень Cron повторні сповіщення про пропущені запуски. Пропущені запуски ведуть окремий лічильник послідовних пропусків, тому вони не впливають на backoff помилок виконання.


## Приклади CLI

### Одноразове нагадування

bashCopy code
[code]
    openclaw cron add \  --name "Calendar check" \  --at "20m" \  --session main \  --system-event "Next heartbeat: check calendar." \  --wake now
[/code]

### Повторюване ізольоване завдання

bashCopy code
[code]
    openclaw cron add \  --name "Morning brief" \  --cron "0 7 * * *" \  --tz "America/Los_Angeles" \  --session isolated \  --message "Summarize overnight updates." \  --announce \  --channel slack \  --to "channel:C1234567890"
[/code]

### Перевизначення моделі та thinking

bashCopy code
[code]
    openclaw cron add \  --name "Deep analysis" \  --cron "0 6 * * 1" \  --tz "America/Los_Angeles" \  --session isolated \  --message "Weekly deep analysis of project progress." \  --model "opus" \  --thinking high \  --announce
[/code]

## Webhook

Gateway може відкривати HTTP Webhook кінцеві точки для зовнішніх тригерів. Увімкніть у config:

json5Copy code
[code]
    {  hooks: {    enabled: true,    token: "shared-secret",    path: "/hooks",  },}
[/code]

### Автентифікація

Кожен запит має містити токен hook через заголовок:

  * `Authorization: Bearer <token>` (рекомендовано)
  * `x-openclaw-token: <token>`


Токени в рядку запиту відхиляються.

POST /hooks/wake

Додати системну подію до черги для основної сесії:

bashCopy code
[code]
    curl -X POST http://127.0.0.1:18789/hooks/wake \  -H 'Authorization: Bearer SECRET' \  -H 'Content-Type: application/json' \  -d '{"text":"New email received","mode":"now"}'
[/code]

Опис події.

`now` або `next-heartbeat`.

POST /hooks/agent

Запустити ізольований хід агента:

bashCopy code
[code]
    curl -X POST http://127.0.0.1:18789/hooks/agent \  -H 'Authorization: Bearer SECRET' \  -H 'Content-Type: application/json' \  -d '{"message":"Summarize inbox","name":"Email","model":"openai/gpt-5.4"}'
[/code]

Поля: `message` (обов’язкове), `name`, `agentId`, `wakeMode`, `deliver`, `channel`, `to`, `model`, `fallbacks`, `thinking`, `timeoutSeconds`.

OPENCLAW_DOCS_MARKER:accordionOpen:IHRpdGxlPSLQl9GW0YHRgtCw0LLQu9C10L3RliBob29rcyAoUE9TVCAvaG9va3MvPG5hbWU )"> Власні назви hook розв’язуються через `hooks.mappings` у config. Зіставлення можуть перетворювати довільні payloads на дії `wake` або `agent` за допомогою шаблонів чи перетворень коду.

## Інтеграція Gmail PubSub

Під’єднайте тригери вхідної пошти Gmail до OpenClaw через Google PubSub.

### Налаштування майстром (рекомендовано)

bashCopy code
[code]
    openclaw webhooks gmail setup --account openclaw@gmail.com
[/code]

Це записує config `hooks.gmail`, вмикає preset Gmail і використовує Tailscale Funnel для push кінцевої точки.

### Автозапуск Gateway

Коли `hooks.enabled=true` і `hooks.gmail.account` задано, Gateway запускає `gog gmail watch serve` під час завантаження та автоматично поновлює watch. Задайте `OPENCLAW_SKIP_GMAIL_WATCHER=1`, щоб відмовитися.

### Ручне одноразове налаштування

* ### Виберіть проєкт GCP

Виберіть проєкт GCP, якому належить OAuth-клієнт, що використовується `gog`:

bashCopy code
[code]
    gcloud auth logingcloud config set project <project-id>gcloud services enable gmail.googleapis.com pubsub.googleapis.com
[/code]

* ### Створіть topic і надайте Gmail push-доступ

bashCopy code
[code]
    gcloud pubsub topics create gog-gmail-watchgcloud pubsub topics add-iam-policy-binding gog-gmail-watch \  --member=serviceAccount:gmail-api-push@system.gserviceaccount.com \  --role=roles/pubsub.publisher
[/code]

* ### Запустіть watch

bashCopy code
[code]
    gog gmail watch start \  --account openclaw@gmail.com \  --label INBOX \  --topic projects/<project-id>/topics/gog-gmail-watch
[/code]

### Перевизначення моделі Gmail

json5Copy code
[code]
    {  hooks: {    gmail: {      model: "openrouter/meta-llama/llama-3.3-70b-instruct:free",      thinking: "off",    },  },}
[/code]

## Керування завданнями

bashCopy code
[code]
    # List all jobsopenclaw cron list # Get one stored job as JSONopenclaw cron get <jobId> # Show one job, including resolved delivery routeopenclaw cron show <jobId> # Edit a jobopenclaw cron edit <jobId> --message "Updated prompt" --model "opus" # Force run a job nowopenclaw cron run <jobId> # Run only if dueopenclaw cron run <jobId> --due # View run historyopenclaw cron runs --id <jobId> --limit 50 # Delete a jobopenclaw cron remove <jobId> # Agent selection (multi-agent setups)openclaw cron add --name "Ops sweep" --cron "0 6 * * *" --session isolated --message "Check ops queue" --agent opsopenclaw cron edit <jobId> --clear-agent
[/code]

## Конфігурація

json5Copy code
[code]
    {  cron: {    enabled: true,    store: "~/.openclaw/cron/jobs.json",    maxConcurrentRuns: 1,    retry: {      maxAttempts: 3,      backoffMs: [60000, 120000, 300000],      retryOn: ["rate_limit", "overloaded", "network", "server_error"],    },    webhookToken: "replace-with-dedicated-webhook-token",    sessionRetention: "24h",    runLog: { maxBytes: "2mb", keepLines: 2000 },  },}
[/code]

`maxConcurrentRuns` обмежує як заплановану диспетчеризацію Cron, так і виконання ізольованих ходів агента. Ізольовані агентські ходи Cron внутрішньо використовують виділену lane виконання черги `cron-nested`, тому збільшення цього значення дає незалежним LLM-запускам Cron просуватися паралельно, а не лише запускати їхні зовнішні wrappers Cron. Спільна lane `nested`, що не належить Cron, цим налаштуванням не розширюється.

Sidecar стану runtime виводиться з `cron.store`: сховище `.json`, як-от `~/clawd/cron/jobs.json`, використовує `~/clawd/cron/jobs-state.json`, тоді як шлях сховища без суфікса `.json` додає `-state.json`.

Якщо ви редагуєте `jobs.json` вручну, не додавайте `jobs-state.json` до source control. OpenClaw використовує цей sidecar для pending slots, active markers, метаданих останнього запуску та ідентичності розкладу, яка повідомляє scheduler, коли зовнішньо відредагованому завданню потрібен свіжий `nextRunAtMs`.

Вимкнути Cron: `cron.enabled: false` або `OPENCLAW_SKIP_CRON=1`.

Поведінка повторних спроб

**Одноразова повторна спроба** : тимчасові помилки (rate limit, перевантаження, мережа, помилка сервера) повторюються до 3 разів з експоненційним backoff. Постійні помилки вимикають негайно.

**Повторна спроба для повторюваних завдань** : експоненційний backoff (від 30 с до 60 хв) між повторними спробами. Backoff скидається після наступного успішного запуску.

Обслуговування

`cron.sessionRetention` (за замовчуванням `24h`) очищає ізольовані записи сеансів запуску. `cron.runLog.maxBytes` / `cron.runLog.keepLines` автоматично очищають файли журналів запуску.

## Усунення несправностей

### Послідовність команд

bashCopy code
[code]
    openclaw statusopenclaw gateway statusopenclaw cron statusopenclaw cron listopenclaw cron runs --id <jobId> --limit 20openclaw system heartbeat lastopenclaw logs --followopenclaw doctor
[/code]

Cron не запускається

  * Перевірте `cron.enabled` і змінну середовища `OPENCLAW_SKIP_CRON`.
  * Переконайтеся, що Gateway працює безперервно.
  * Для розкладів `cron` перевірте часовий пояс (`--tz`) порівняно з часовим поясом хоста.
  * `reason: not-due` у виводі запуску означає, що ручний запуск було перевірено через `openclaw cron run <jobId> --due`, і час виконання завдання ще не настав.

Cron спрацював, але доставлення немає

  * Режим доставлення `none` означає, що резервне надсилання runner не очікується. Агент усе ще може надсилати напряму за допомогою інструмента `message`, коли доступний маршрут чату.
  * Відсутня або недійсна ціль доставлення (`channel`/`to`) означає, що вихідне надсилання було пропущено.
  * Для Matrix скопійовані або застарілі завдання з ідентифікаторами кімнат `delivery.to`, перетвореними на нижній регістр, можуть не спрацювати, оскільки ідентифікатори кімнат Matrix чутливі до регістру. Змініть завдання на точне значення `!room:server` або `room:!room:server` з Matrix.
  * Помилки автентифікації каналу (`unauthorized`, `Forbidden`) означають, що доставлення було заблоковано обліковими даними.
  * Якщо ізольований запуск повертає лише тихий токен (`NO_REPLY` / `no_reply`), OpenClaw пригнічує пряме вихідне доставлення, а також резервний шлях підсумку в черзі, тому нічого не публікується назад у чат.
  * Якщо агент має сам надіслати повідомлення користувачу, перевірте, що завдання має придатний маршрут (`channel: "last"` із попереднім чатом або явний канал/ціль).

Cron або Heartbeat, схоже, перешкоджає переходу /new-style

  * Актуальність щоденного та неактивного скидання не базується на `updatedAt`; див. [Керування сеансами](</uk/concepts/session#session-lifecycle>).
  * Пробудження Cron, запуски Heartbeat, сповіщення exec і службове ведення Gateway можуть оновлювати рядок сеансу для маршрутизації/статусу, але вони не продовжують `sessionStartedAt` або `lastInteractionAt`.
  * Для застарілих рядків, створених до появи цих полів, OpenClaw може відновити `sessionStartedAt` із заголовка сеансу transcript JSONL, якщо файл усе ще доступний. Застарілі неактивні рядки без `lastInteractionAt` використовують цей відновлений час початку як базову точку неактивності.

Нюанси часових поясів

  * Cron без `--tz` використовує часовий пояс хоста Gateway.
  * Розклади `at` без часового поясу вважаються UTC.
  * Heartbeat `activeHours` використовує налаштоване визначення часового поясу.


## Пов’язане

  * [Автоматизація](</uk/automation>) — усі механізми автоматизації одним поглядом
  * [Фонові завдання](</uk/automation/tasks>) — журнал завдань для виконань cron
  * [Heartbeat](</uk/gateway/heartbeat>) — періодичні кроки головного сеансу
  * [Часовий пояс](</uk/concepts/timezone>) — налаштування часового поясу


Was this useful?YesNo