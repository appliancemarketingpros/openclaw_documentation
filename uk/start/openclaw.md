---
title: Налаштування персонального асистента
source_url: https://docs.openclaw.ai/uk/start/openclaw
scraped_at: 2026-05-25
---

OpenClaw — це self-hosted Gateway, який підключає Discord, Google Chat, iMessage, Matrix, Microsoft Teams, Signal, Slack, Telegram, WhatsApp, Zalo та інші канали до AI-агентів. У цьому посібнику описано налаштування "персонального асистента": виділений номер WhatsApp, який поводиться як ваш постійно доступний AI-асистент.

## ⚠️ Спершу безпека

Ви ставите агента в позицію, де він може:

  * виконувати команди на вашій машині (залежно від вашої політики інструментів)
  * читати/записувати файли у вашому робочому просторі
  * надсилати повідомлення назад через WhatsApp/Telegram/Discord/Mattermost та інші вбудовані канали


Почніть консервативно:

  * Завжди задавайте `channels.whatsapp.allowFrom` (ніколи не запускайте відкритим для всього світу на вашому особистому Mac).
  * Використовуйте виділений номер WhatsApp для асистента.
  * Heartbeat-и тепер за замовчуванням виконуються кожні 30 хвилин. Вимкніть їх, доки не довірятимете налаштуванню, задавши `agents.defaults.heartbeat.every: "0m"`.


## Передумови

  * OpenClaw встановлено й виконано onboarding — див. [Початок роботи](</uk/start/getting-started>), якщо ви ще цього не зробили
  * Другий номер телефону (SIM/eSIM/prepaid) для асистента


## Налаштування з двома телефонами (рекомендовано)

Вам потрібно ось це:
[code] 
    flowchart TB
        A["<b>Your Phone (personal)
    </b>
    Your WhatsApp
    +1-555-YOU"] -- message --> B["<b>Second Phone (assistant)
    </b>
    Assistant WA
    +1-555-ASSIST"]
        B -- linked via QR --> C["<b>Your Mac (openclaw)
    </b>
    AI agent"]
[/code]

Якщо ви підключите свій особистий WhatsApp до OpenClaw, кожне повідомлення до вас стане "вхідними даними агента". Це рідко саме те, що вам потрібно.

## Швидкий старт за 5 хвилин

  1. Спарте WhatsApp Web (показує QR; проскануйте його телефоном асистента):

bashCopy code
[code]
    openclaw channels login
[/code]

  2. Запустіть Gateway (залиште його працювати):

bashCopy code
[code]
    openclaw gateway --port 18789
[/code]

  3. Додайте мінімальну конфігурацію в `~/.openclaw/openclaw.json`:

json5Copy code
[code]
    {  gateway: { mode: "local" },  channels: { whatsapp: { allowFrom: ["+15555550123"] } },}
[/code]

Тепер напишіть на номер асистента з вашого allowlisted телефону.

Коли onboarding завершиться, OpenClaw автоматично відкриє dashboard і виведе чисте посилання (без токена). Якщо dashboard попросить автентифікацію, вставте налаштований спільний секрет у налаштування Control UI. Onboarding за замовчуванням використовує токен (`gateway.auth.token`), але парольна автентифікація теж працює, якщо ви перемкнули `gateway.auth.mode` на `password`. Щоб відкрити пізніше: `openclaw dashboard`.

## Дайте агенту робочий простір (AGENTS)

OpenClaw читає операційні інструкції та "пам’ять" зі свого каталогу робочого простору.

За замовчуванням OpenClaw використовує `~/.openclaw/workspace` як робочий простір агента і створить його (а також стартові `AGENTS.md`, `SOUL.md`, `TOOLS.md`, `IDENTITY.md`, `USER.md`, `HEARTBEAT.md`) автоматично під час налаштування/першого запуску агента. `BOOTSTRAP.md` створюється лише тоді, коли робочий простір абсолютно новий (він не має з’являтися знову після видалення). `MEMORY.md` необов’язковий (не створюється автоматично); якщо він наявний, його завантажують для звичайних сесій. У сесії subagent додаються лише `AGENTS.md` і `TOOLS.md`.

bashCopy code
[code]
    openclaw setup
[/code]

Повна структура робочого простору + посібник із резервного копіювання: [Робочий простір агента](</uk/concepts/agent-workspace>) Робочий процес пам’яті: [Пам’ять](</uk/concepts/memory>)

Необов’язково: виберіть інший робочий простір через `agents.defaults.workspace` (підтримує `~`).

json5Copy code
[code]
    {  agents: {    defaults: {      workspace: "~/.openclaw/workspace",    },  },}
[/code]

Якщо ви вже постачаєте власні файли робочого простору з репозиторію, можна повністю вимкнути створення bootstrap-файлів:

json5Copy code
[code]
    {  agents: {    defaults: {      skipBootstrap: true,    },  },}
[/code]

## Конфігурація, яка перетворює це на "асистента"

OpenClaw за замовчуванням має хороше налаштування асистента, але зазвичай варто налаштувати:

  * persona/інструкції в [`SOUL.md`](</uk/concepts/soul>)
  * стандартні параметри мислення (за потреби)
  * Heartbeat-и (коли ви вже довірятимете цьому)


Приклад:

json5Copy code
[code]
    {  logging: { level: "info" },  agents: {    defaults: {      model: { primary: "anthropic/claude-opus-4-6" },      workspace: "~/.openclaw/workspace",      thinkingDefault: "high",      timeoutSeconds: 1800,      // Start with 0; enable later.      heartbeat: { every: "0m" },    },    list: [      {        id: "main",        default: true,        groupChat: {          mentionPatterns: ["@openclaw", "openclaw"],        },      },    ],  },  channels: {    whatsapp: {      allowFrom: ["+15555550123"],      groups: {        "*": { requireMention: true },      },    },  },  session: {    scope: "per-sender",    resetTriggers: ["/new", "/reset"],    reset: {      mode: "daily",      atHour: 4,      idleMinutes: 10080,    },  },}
[/code]

## Сесії та пам’ять

  * Файли сесій: `~/.openclaw/agents/<agentId>/sessions/{{SessionId}}.jsonl`
  * Метадані сесій (використання токенів, останній маршрут тощо): `~/.openclaw/agents/<agentId>/sessions/sessions.json` (застаріле: `~/.openclaw/sessions/sessions.json`)
  * `/new` або `/reset` починає нову сесію для цього чату (налаштовується через `resetTriggers`). Якщо надіслано окремо, OpenClaw підтверджує скидання без виклику моделі.
  * `/compact [instructions]` ущільнює контекст сесії та повідомляє залишковий бюджет контексту.


## Heartbeat-и (проактивний режим)

За замовчуванням OpenClaw запускає Heartbeat кожні 30 хвилин із prompt: `Read HEARTBEAT.md if it exists (workspace context). Follow it strictly. Do not infer or repeat old tasks from prior chats. If nothing needs attention, reply HEARTBEAT_OK.` Задайте `agents.defaults.heartbeat.every: "0m"`, щоб вимкнути.

  * Якщо `HEARTBEAT.md` існує, але фактично порожній (лише порожні рядки та markdown-заголовки на кшталт `# Heading`), OpenClaw пропускає запуск Heartbeat, щоб заощадити API-виклики.
  * Якщо файл відсутній, Heartbeat все одно запускається, а модель вирішує, що робити.
  * Якщо агент відповідає `HEARTBEAT_OK` (необов’язково з коротким доповненням; див. `agents.defaults.heartbeat.ackMaxChars`), OpenClaw пригнічує вихідну доставку для цього Heartbeat.
  * За замовчуванням доставка Heartbeat до DM-подібних цілей `user:<id>` дозволена. Задайте `agents.defaults.heartbeat.directPolicy: "block"`, щоб пригнітити доставку до прямих цілей, залишивши запуски Heartbeat активними.
  * Heartbeat-и виконують повні ходи агента — коротші інтервали витрачають більше токенів.

json5Copy code
[code]
    {  agents: {    defaults: {      heartbeat: { every: "30m" },    },  },}
[/code]

## Медіа на вхід і вихід

Вхідні вкладення (зображення/аудіо/документи) можна передавати вашій команді через шаблони:

  * `{{MediaPath}}` (шлях до локального тимчасового файлу)
  * `{{MediaUrl}}` (псевдо-URL)
  * `{{Transcript}}` (якщо транскрипцію аудіо ввімкнено)


Вихідні вкладення від агента: додайте `MEDIA:<path-or-url>` в окремому рядку (без пробілів). Приклад:

CodeCopy code
[code]
    Here's the screenshot.MEDIA:https://example.com/screenshot.png
[/code]

OpenClaw витягує їх і надсилає як медіа разом із текстом.

Поведінка локальних шляхів дотримується тієї самої моделі довіри для читання файлів, що й агент:

  * Якщо `tools.fs.workspaceOnly` має значення `true`, вихідні локальні шляхи `MEDIA:` залишаються обмеженими тимчасовим коренем OpenClaw, медіакешем, шляхами робочого простору агента та файлами, згенерованими в sandbox.
  * Якщо `tools.fs.workspaceOnly` має значення `false`, вихідні `MEDIA:` можуть використовувати локальні файли хоста, які агенту вже дозволено читати.
  * Локальні шляхи можуть бути абсолютними, відносними до робочого простору або відносними до home із `~/`.
  * Надсилання локальних файлів хоста все одно дозволяє лише медіа та безпечні типи документів (зображення, аудіо, відео, PDF і документи Office). Звичайний текст і файли, схожі на секрети, не вважаються медіа, які можна надсилати.


Це означає, що згенеровані зображення/файли поза робочим простором тепер можна надсилати, коли ваша fs-політика вже дозволяє їх читання, без повторного відкриття довільної ексфільтрації текстових вкладень хоста.

## Операційний чекліст

bashCopy code
[code]
    openclaw status          # local status (creds, sessions, queued events)openclaw status --all    # full diagnosis (read-only, pasteable)openclaw status --deep   # asks the gateway for a live health probe with channel probes when supportedopenclaw health --json   # gateway health snapshot (WS; default can return a fresh cached snapshot)
[/code]

Логи зберігаються в `/tmp/openclaw/` (за замовчуванням: `openclaw-YYYY-MM-DD.log`).

## Наступні кроки

  * WebChat: [WebChat](</uk/web/webchat>)
  * Операції Gateway: [Runbook Gateway](</uk/gateway>)
  * Cron + пробудження: [Cron jobs](</uk/automation/cron-jobs>)
  * Компаньйон у рядку меню macOS: [застосунок OpenClaw для macOS](</uk/platforms/macos>)
  * Застосунок iOS node: [застосунок iOS](</uk/platforms/ios>)
  * Застосунок Android node: [застосунок Android](</uk/platforms/android>)
  * Статус Windows: [Windows (WSL2)](</uk/platforms/windows>)
  * Статус Linux: [застосунок Linux](</uk/platforms/linux>)
  * Безпека: [Безпека](</uk/gateway/security>)


## Пов’язане

  * [Початок роботи](</uk/start/getting-started>)
  * [Налаштування](</uk/start/setup>)
  * [Огляд каналів](</uk/channels>)


Was this useful?YesNo