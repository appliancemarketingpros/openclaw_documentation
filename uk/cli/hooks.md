---
title: Хуки
source_url: https://docs.openclaw.ai/uk/cli/hooks
scraped_at: 2026-05-25
---

# `openclaw hooks`

Керуйте хуками агента (подієво-керованими автоматизаціями для команд на кшталт `/new`, `/reset` і запуску Gateway).

Запуск `openclaw hooks` без підкоманди еквівалентний `openclaw hooks list`.

Пов’язане:

  * Хуки: [Хуки](</uk/automation/hooks>)
  * Plugin-хуки: [Plugin-хуки](</uk/plugins/hooks>)


## Перелічити всі хуки

bashCopy code
[code]
    openclaw hooks list
[/code]

Перелічує всі виявлені хуки з робочої області, керованих, додаткових і вбудованих каталогів. Під час запуску Gateway не завантажує внутрішні обробники хуків, доки не налаштовано принаймні один внутрішній хук.

**Параметри:**

  * `--eligible`: Показати лише придатні хуки (вимоги виконано)
  * `--json`: Вивести як JSON
  * `-v, --verbose`: Показати докладну інформацію, включно з відсутніми вимогами


**Приклад виводу:**

CodeCopy code
[code]
    Hooks (4/4 ready) Ready:  🚀 boot-md ✓ - Run BOOT.md on gateway startup  📎 bootstrap-extra-files ✓ - Inject extra workspace bootstrap files during agent bootstrap  📝 command-logger ✓ - Log all command events to a centralized audit file  💾 session-memory ✓ - Save session context to memory when /new or /reset command is issued
[/code]

**Приклад (докладно):**

bashCopy code
[code]
    openclaw hooks list --verbose
[/code]

Показує відсутні вимоги для непридатних хуків.

**Приклад (JSON):**

bashCopy code
[code]
    openclaw hooks list --json
[/code]

Повертає структурований JSON для програмного використання.

## Отримати інформацію про хук

bashCopy code
[code]
    openclaw hooks info <name>
[/code]

Показує докладну інформацію про конкретний хук.

**Аргументи:**

  * `<name>`: Назва хука або ключ хука (наприклад, `session-memory`)


**Параметри:**

  * `--json`: Вивести як JSON


**Приклад:**

bashCopy code
[code]
    openclaw hooks info session-memory
[/code]

**Вивід:**

CodeCopy code
[code]
    💾 session-memory ✓ Ready Save session context to memory when /new or /reset command is issued Details:  Source: openclaw-bundled  Path: /path/to/openclaw/hooks/bundled/session-memory/HOOK.md  Handler: /path/to/openclaw/hooks/bundled/session-memory/handler.ts  Homepage: https://docs.openclaw.ai/automation/hooks#session-memory  Events: command:new, command:reset Requirements:  Config: ✓ workspace.dir
[/code]

## Перевірити придатність хуків

bashCopy code
[code]
    openclaw hooks check
[/code]

Показує зведення статусу придатності хуків (скільки готові, а скільки ні).

**Параметри:**

  * `--json`: Вивести як JSON


**Приклад виводу:**

CodeCopy code
[code]
    Hooks Status Total hooks: 4Ready: 4Not ready: 0
[/code]

## Увімкнути хук

bashCopy code
[code]
    openclaw hooks enable <name>
[/code]

Увімкніть конкретний хук, додавши його до своєї конфігурації (`~/.openclaw/openclaw.json` за замовчуванням).

**Примітка:** Хуки робочої області вимкнені за замовчуванням, доки їх не ввімкнено тут або в конфігурації. Хуки, керовані plugins, показують `plugin:<id>` у `openclaw hooks list` і не можуть бути ввімкнені або вимкнені тут. Натомість увімкніть або вимкніть Plugin.

**Аргументи:**

  * `<name>`: Назва хука (наприклад, `session-memory`)


**Приклад:**

bashCopy code
[code]
    openclaw hooks enable session-memory
[/code]

**Вивід:**

CodeCopy code
[code]
    ✓ Enabled hook: 💾 session-memory
[/code]

**Що це робить:**

  * Перевіряє, чи існує хук і чи він придатний
  * Оновлює `hooks.internal.entries.<name>.enabled = true` у вашій конфігурації
  * Зберігає конфігурацію на диск


Якщо хук походить із `<workspace>/hooks/`, цей крок явного ввімкнення потрібен до того, як Gateway завантажить його.

**Після ввімкнення:**

  * Перезапустіть Gateway, щоб хуки перезавантажилися (перезапуск застосунку в рядку меню на macOS або перезапуск процесу Gateway у dev).


## Вимкнути хук

bashCopy code
[code]
    openclaw hooks disable <name>
[/code]

Вимкніть конкретний хук, оновивши свою конфігурацію.

**Аргументи:**

  * `<name>`: Назва хука (наприклад, `command-logger`)


**Приклад:**

bashCopy code
[code]
    openclaw hooks disable command-logger
[/code]

**Вивід:**

CodeCopy code
[code]
    ⏸ Disabled hook: 📝 command-logger
[/code]

**Після вимкнення:**

  * Перезапустіть Gateway, щоб хуки перезавантажилися


## Примітки

  * `openclaw hooks list --json`, `info --json` і `check --json` записують структурований JSON безпосередньо в stdout.
  * Хуки, керовані Plugin, не можна ввімкнути або вимкнути тут; натомість увімкніть або вимкніть Plugin-власник.


## Установити пакети хуків

bashCopy code
[code]
    openclaw plugins install <package>        # npm by defaultopenclaw plugins install npm:<package>    # npm onlyopenclaw plugins install <package> --pin  # pin versionopenclaw plugins install <path>           # local path
[/code]

Установлюйте пакети хуків через уніфікований інсталятор plugins.

`openclaw hooks install` все ще працює як псевдонім сумісності, але друкує попередження про застарівання та переспрямовує до `openclaw plugins install`.

Специфікації npm є **лише registry** (назва пакета + необов’язкова **точна версія** або **dist-tag**). Специфікації Git/URL/файлів і діапазони semver відхиляються. Установлення залежностей виконується локально для проєкту з `--ignore-scripts` для безпеки, навіть якщо ваша оболонка має глобальні налаштування npm install.

Голі специфікації та `@latest` залишаються на стабільній гілці. Якщо npm розв’язує будь-яку з них у попередній випуск, OpenClaw зупиняється і просить вас явно погодитися за допомогою тега попереднього випуску, такого як `@beta`/`@rc`, або точної версії попереднього випуску.

**Що це робить:**

  * Копіює пакет хуків у `~/.openclaw/hooks/<id>`
  * Увімкнює встановлені хуки в `hooks.internal.entries.*`
  * Записує встановлення в `hooks.internal.installs`


**Параметри:**

  * `-l, --link`: Пов’язати локальний каталог замість копіювання (додає його до `hooks.internal.load.extraDirs`)
  * `--pin`: Записувати встановлення npm як точно розв’язане `name@version` у `hooks.internal.installs`


**Підтримувані архіви:** `.zip`, `.tgz`, `.tar.gz`, `.tar`

**Приклади:**

bashCopy code
[code]
    # Local directoryopenclaw plugins install ./my-hook-pack # Local archiveopenclaw plugins install ./my-hook-pack.zip # NPM packageopenclaw plugins install @openclaw/my-hook-pack # Link a local directory without copyingopenclaw plugins install -l ./my-hook-pack
[/code]

Пов’язані пакети хуків обробляються як керовані хуки з каталогу, налаштованого оператором, а не як хуки робочої області.

## Оновити пакети хуків

bashCopy code
[code]
    openclaw plugins update <id>openclaw plugins update --all
[/code]

Оновлюйте відстежувані пакети хуків на основі npm через уніфікований засіб оновлення plugins.

`openclaw hooks update` все ще працює як псевдонім сумісності, але друкує попередження про застарівання та переспрямовує до `openclaw plugins update`.

**Параметри:**

  * `--all`: Оновити всі відстежувані пакети хуків
  * `--dry-run`: Показати, що зміниться, без запису


Коли збережений хеш цілісності існує, а хеш отриманого артефакту змінюється, OpenClaw друкує попередження та просить підтвердження перед продовженням. Використовуйте глобальний `--yes`, щоб обійти запити в CI/неінтерактивних запусках.

## Вбудовані хуки

### session-memory

Зберігає контекст сеансу в пам’ять, коли ви виконуєте `/new` або `/reset`.

**Увімкнення:**

bashCopy code
[code]
    openclaw hooks enable session-memory
[/code]

**Вивід:** `~/.openclaw/workspace/memory/YYYY-MM-DD-HHMM.md` за замовчуванням. Установіть `hooks.internal.entries.session-memory.llmSlug: true` для згенерованих моделлю слагів імен файлів.

**Див.:** [документацію session-memory](</uk/automation/hooks#session-memory>)

### bootstrap-extra-files

Вставляє додаткові bootstrap-файли (наприклад, локальні для монорепозиторію `AGENTS.md` / `TOOLS.md`) під час `agent:bootstrap`.

**Увімкнення:**

bashCopy code
[code]
    openclaw hooks enable bootstrap-extra-files
[/code]

**Див.:** [документацію bootstrap-extra-files](</uk/automation/hooks#bootstrap-extra-files>)

### command-logger

Записує всі події команд до централізованого файлу аудиту.

**Увімкнення:**

bashCopy code
[code]
    openclaw hooks enable command-logger
[/code]

**Вивід:** `~/.openclaw/logs/commands.log`

**Перегляд журналів:**

bashCopy code
[code]
    # Recent commandstail -n 20 ~/.openclaw/logs/commands.log # Pretty-printcat ~/.openclaw/logs/commands.log | jq . # Filter by actiongrep '"action":"new"' ~/.openclaw/logs/commands.log | jq .
[/code]

**Див.:** [документацію command-logger](</uk/automation/hooks#command-logger>)

### boot-md

Запускає `BOOT.md`, коли Gateway запускається (після запуску каналів).

**Події** : `gateway:startup`

**Увімкнення** :

bashCopy code
[code]
    openclaw hooks enable boot-md
[/code]

**Див.:** [документацію boot-md](</uk/automation/hooks#boot-md>)

## Пов’язане

  * [Довідник CLI](</uk/cli>)
  * [Хуки автоматизації](</uk/automation/hooks>)


Was this useful?YesNo