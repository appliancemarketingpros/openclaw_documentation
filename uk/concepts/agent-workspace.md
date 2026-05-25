---
title: Робочий простір агента
source_url: https://docs.openclaw.ai/uk/concepts/agent-workspace
scraped_at: 2026-05-25
---

The workspace — це домівка агента. Це єдиний робочий каталог, який використовується для файлових інструментів і контексту workspace. Зберігайте його приватним і розглядайте як пам’ять.

Це окремо від `~/.openclaw/`, де зберігаються конфігурація, облікові дані та сесії.

## Типове розташування

  * Типово: `~/.openclaw/workspace`
  * Якщо `OPENCLAW_PROFILE` задано і він не `"default"`, типовим стає `~/.openclaw/workspace-<profile>`.
  * Перевизначення в `~/.openclaw/openclaw.json`:

json5Copy code
[code]
    {  agents: {    defaults: {      workspace: "~/.openclaw/workspace",    },  },}
[/code]

`openclaw onboard`, `openclaw configure` або `openclaw setup` створять workspace і заповнять початкові файли, якщо їх немає.

Якщо ви вже самостійно керуєте файлами workspace, можна вимкнути створення початкових файлів:

json5Copy code
[code]
    { agents: { defaults: { skipBootstrap: true } } }
[/code]

## Додаткові папки workspace

Старіші встановлення могли створити `~/openclaw`. Наявність кількох каталогів workspace може спричиняти плутанину з автентифікацією або розбіжність стану, оскільки одночасно активний лише один workspace.

## Мапа файлів workspace

Це стандартні файли, які OpenClaw очікує всередині workspace:

AGENTS.md - робочі інструкції

Робочі інструкції для агента й те, як він має використовувати пам’ять. Завантажується на початку кожної сесії. Добре місце для правил, пріоритетів і деталей про те, «як поводитися».

SOUL.md - персона й тон

Персона, тон і межі. Завантажується в кожній сесії. Посібник: [посібник з особистості SOUL.md](</uk/concepts/soul>).

USER.md - хто такий користувач

Хто такий користувач і як до нього звертатися. Завантажується в кожній сесії.

IDENTITY.md - ім’я, вайб, емодзі

Ім’я агента, вайб і емодзі. Створюється/оновлюється під час bootstrap-ритуалу.

TOOLS.md - локальні домовленості щодо інструментів

Нотатки про ваші локальні інструменти й домовленості. Не керує доступністю інструментів; це лише настанови.

HEARTBEAT.md - контрольний список heartbeat

Необов’язковий маленький контрольний список для запусків heartbeat. Тримайте його коротким, щоб уникнути витрат токенів.

BOOT.md - контрольний список запуску

Необов’язковий контрольний список запуску, який автоматично виконується під час перезапуску Gateway (коли ввімкнено [внутрішні hooks](</uk/automation/hooks>)). Тримайте його коротким; використовуйте message tool для вихідних надсилань.

BOOTSTRAP.md - ритуал першого запуску

Одноразовий ритуал першого запуску. Створюється лише для абсолютно нового workspace. Видаліть його після завершення ритуалу.

memory/YYYY-MM-DD.md - щоденний журнал пам’яті

Щоденний журнал пам’яті (один файл на день). Рекомендовано читати сьогоднішній + вчорашній на початку сесії.

MEMORY.md - кураторована довготривала пам’ять (необов’язково)

Кураторована довготривала пам’ять: сталі факти, уподобання, рішення й короткі підсумки. Тримайте докладні журнали в `memory/YYYY-MM-DD.md`, щоб інструменти пам’яті могли отримувати їх на вимогу без вставляння в кожен prompt. Завантажуйте `MEMORY.md` лише в основній приватній сесії (не в shared/group-контекстах). Див. [Memory](</uk/concepts/memory>) щодо workflow та автоматичного скидання пам’яті.

skills/ - Skills workspace (необов’язково)

Skills, специфічні для workspace. Розташування Skills з найвищим пріоритетом для цього workspace. Перевизначає Skills агента проєкту, особисті Skills агента, керовані Skills, вбудовані Skills і `skills.load.extraDirs`, коли назви збігаються.

canvas/ - файли Canvas UI (необов’язково)

Файли Canvas UI для відображень вузлів (наприклад, `canvas/index.html`).

## Чого НЕ має бути у workspace

Це розташовано в `~/.openclaw/` і НЕ має комітитися в репозиторій workspace:

  * `~/.openclaw/openclaw.json` (конфігурація)
  * `~/.openclaw/agents/<agentId>/agent/auth-profiles.json` (профілі автентифікації моделей: OAuth + API keys)
  * `~/.openclaw/agents/<agentId>/agent/codex-home/` (окремий для агента обліковий запис runtime Codex, конфігурація, Skills, plugins і нативний стан thread)
  * `~/.openclaw/credentials/` (стан channel/provider плюс застарілі дані імпорту OAuth)
  * `~/.openclaw/agents/<agentId>/sessions/` (транскрипти сесій + метадані)
  * `~/.openclaw/skills/` (керовані Skills)


Якщо потрібно перенести сесії або конфігурацію, скопіюйте їх окремо й не додавайте до контролю версій.

## Git-резервна копія (рекомендовано, приватно)

Розглядайте workspace як приватну пам’ять. Помістіть його в **приватний** git-репозиторій, щоб він мав резервну копію й міг бути відновлений.

Виконайте ці кроки на машині, де працює Gateway (саме там розташований workspace).

* ### Ініціалізуйте репозиторій

Якщо git встановлено, абсолютно нові workspace ініціалізуються автоматично. Якщо цей workspace ще не є репозиторієм, виконайте:

bashCopy code
[code]
    cd ~/.openclaw/workspacegit initgit add AGENTS.md SOUL.md TOOLS.md IDENTITY.md USER.md HEARTBEAT.md memory/git commit -m "Add agent workspace"
[/code]

* ### Додайте приватний remote

### Вебінтерфейс GitHub

  1. Створіть новий **приватний** репозиторій на GitHub.
  2. Не ініціалізуйте з README (це уникає merge conflicts).
  3. Скопіюйте HTTPS remote URL.
  4. Додайте remote і виконайте push:

bashCopy code
[code]
    git branch -M maingit remote add origin <https-url>git push -u origin main
[/code]

### GitHub CLI (gh)

bashCopy code
[code]
    gh auth logingh repo create openclaw-workspace --private --source . --remote origin --push
[/code]

### Вебінтерфейс GitLab

  1. Створіть новий **приватний** репозиторій на GitLab.
  2. Не ініціалізуйте з README (це уникає merge conflicts).
  3. Скопіюйте HTTPS remote URL.
  4. Додайте remote і виконайте push:

bashCopy code
[code]
    git branch -M maingit remote add origin <https-url>git push -u origin main
[/code]

* ### Поточні оновлення

bashCopy code
[code]
    git statusgit add .git commit -m "Update memory"git push
[/code]

## Не комітьте секрети

Рекомендований початковий `.gitignore`:

gitignoreCopy code
[code]
    .DS_Store.env**/*.key**/*.pem**/secrets*
[/code]

## Перенесення workspace на нову машину

* ### Клонуйте репозиторій

Клонуйте репозиторій у потрібний шлях (типово `~/.openclaw/workspace`).

* ### Оновіть конфігурацію

Встановіть `agents.defaults.workspace` на цей шлях у `~/.openclaw/openclaw.json`.

* ### Заповніть відсутні файли

Виконайте `openclaw setup --workspace <path>`, щоб додати будь-які відсутні файли.

* ### Скопіюйте сесії (необов’язково)

Якщо вам потрібні сесії, окремо скопіюйте `~/.openclaw/agents/<agentId>/sessions/` зі старої машини.

## Розширені нотатки

  * Multi-agent routing може використовувати різні workspaces для кожного агента. Див. [Channel routing](</uk/channels/channel-routing>) щодо конфігурації routing.
  * Якщо `agents.defaults.sandbox` увімкнено, non-main сесії можуть використовувати per-session sandbox workspaces під `agents.defaults.sandbox.workspaceRoot`.


## Пов’язане

  * [Heartbeat](</uk/gateway/heartbeat>) \- файл workspace [HEARTBEAT.md](<http://HEARTBEAT.md>)
  * [Sandboxing](</uk/gateway/sandboxing>) \- доступ до workspace у sandboxed середовищах
  * [Session](</uk/concepts/session>) \- шляхи зберігання сесій
  * [Standing orders](</uk/automation/standing-orders>) \- постійні інструкції у файлах workspace


Was this useful?YesNo