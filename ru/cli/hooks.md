---
title: Hooks
source_url: https://docs.openclaw.ai/ru/cli/hooks
scraped_at: 2026-06-29
---

ReferenceCLI commands

# `openclaw hooks`

Управляйте хуками агента (автоматизациями по событиям для команд вроде `/new`, `/reset` и запуска Gateway).

Запуск `openclaw hooks` без подкоманды эквивалентен `openclaw hooks list`.

Связанные разделы:

  * Хуки: [Хуки](</ru/automation/hooks>)
  * Хуки Plugin: [Хуки Plugin](</ru/plugins/hooks>)


## Список всех хуков

bashCopy code
[code]
    openclaw hooks list
[/code]

Показывает все обнаруженные хуки из рабочей области, управляемых, дополнительных и встроенных каталогов. При запуске Gateway внутренние обработчики хуков не загружаются, пока не настроен хотя бы один внутренний хук.

**Параметры:**

  * `--eligible`: Показать только подходящие хуки (требования выполнены)
  * `--json`: Вывести как JSON
  * `-v, --verbose`: Показать подробную информацию, включая отсутствующие требования


**Пример вывода:**

CodeCopy code
[code]
    Hooks (4/4 ready) Ready:  🚀 boot-md ✓ - Run BOOT.md on gateway startup  📎 bootstrap-extra-files ✓ - Inject extra workspace bootstrap files during agent bootstrap  📝 command-logger ✓ - Log all command events to a centralized audit file  💾 session-memory ✓ - Save session context to memory when /new or /reset command is issued
[/code]

**Пример (подробный вывод):**

bashCopy code
[code]
    openclaw hooks list --verbose
[/code]

Показывает отсутствующие требования для неподходящих хуков.

**Пример (JSON):**

bashCopy code
[code]
    openclaw hooks list --json
[/code]

Возвращает структурированный JSON для программного использования.

## Получить информацию о хуке

bashCopy code
[code]
    openclaw hooks info <name>
[/code]

Показывает подробную информацию о конкретном хуке.

**Аргументы:**

  * `<name>`: имя хука или ключ хука (например, `session-memory`)


**Параметры:**

  * `--json`: Вывести как JSON


**Пример:**

bashCopy code
[code]
    openclaw hooks info session-memory
[/code]

**Вывод:**

CodeCopy code
[code]
    💾 session-memory ✓ Ready Save session context to memory when /new or /reset command is issued Details:  Source: openclaw-bundled  Path: /path/to/openclaw/hooks/bundled/session-memory/HOOK.md  Handler: /path/to/openclaw/hooks/bundled/session-memory/handler.ts  Homepage: https://docs.openclaw.ai/automation/hooks#session-memory  Events: command:new, command:reset Requirements:  Config: ✓ workspace.dir
[/code]

## Проверить пригодность хуков

bashCopy code
[code]
    openclaw hooks check
[/code]

Показывает сводку статуса пригодности хуков (сколько готово и сколько не готово).

**Параметры:**

  * `--json`: Вывести как JSON


**Пример вывода:**

CodeCopy code
[code]
    Hooks Status Total hooks: 4Ready: 4Not ready: 0
[/code]

## Включить хук

bashCopy code
[code]
    openclaw hooks enable <name>
[/code]

Включает конкретный хук, добавляя его в вашу конфигурацию (по умолчанию `~/.openclaw/openclaw.json`).

**Примечание:** Хуки рабочей области по умолчанию отключены, пока вы не включите их здесь или в конфигурации. Хуки, управляемые plugins, показывают `plugin:<id>` в `openclaw hooks list`, и их нельзя включить или отключить здесь. Вместо этого включите или отключите соответствующий plugin.

**Аргументы:**

  * `<name>`: имя хука (например, `session-memory`)


**Пример:**

bashCopy code
[code]
    openclaw hooks enable session-memory
[/code]

**Вывод:**

CodeCopy code
[code]
    ✓ Enabled hook: 💾 session-memory
[/code]

**Что делает команда:**

  * Проверяет, что хук существует и пригоден
  * Обновляет `hooks.internal.entries.<name>.enabled = true` в вашей конфигурации
  * Сохраняет конфигурацию на диск


Если хук получен из `<workspace>/hooks/`, этот шаг явного включения обязателен перед тем, как Gateway сможет его загрузить.

**После включения:**

  * Перезапустите gateway, чтобы хуки перезагрузились (перезапуск приложения в строке меню на macOS или перезапуск процесса gateway в разработке).


## Отключить хук

bashCopy code
[code]
    openclaw hooks disable <name>
[/code]

Отключает конкретный хук, обновляя вашу конфигурацию.

**Аргументы:**

  * `<name>`: имя хука (например, `command-logger`)


**Пример:**

bashCopy code
[code]
    openclaw hooks disable command-logger
[/code]

**Вывод:**

CodeCopy code
[code]
    ⏸ Disabled hook: 📝 command-logger
[/code]

**После отключения:**

  * Перезапустите gateway, чтобы хуки перезагрузились


## Примечания

  * `openclaw hooks list --json`, `info --json` и `check --json` записывают структурированный JSON напрямую в stdout.
  * Хуки, управляемые Plugin, нельзя включить или отключить здесь; вместо этого включите или отключите владеющий plugin.


## Установить пакеты хуков

bashCopy code
[code]
    openclaw plugins install <package>        # npm by defaultopenclaw plugins install npm:<package>    # npm onlyopenclaw plugins install <package> --pin  # pin versionopenclaw plugins install <path>           # local path
[/code]

Устанавливает пакеты хуков через единый установщик plugins.

`openclaw hooks install` по-прежнему работает как псевдоним совместимости, но выводит предупреждение об устаревании и перенаправляет на `openclaw plugins install`.

Спецификации npm работают **только через реестр** (имя пакета + необязательная **точная версия** или **dist-tag**). Спецификации Git/URL/file и диапазоны semver отклоняются. Установка зависимостей выполняется локально для проекта с `--ignore-scripts` ради безопасности, даже если в вашей оболочке заданы глобальные настройки установки npm.

Базовые спецификации и `@latest` остаются на стабильной ветке. Если npm разрешает любую из них в предварительную версию, OpenClaw останавливается и просит явно согласиться через тег предварительной версии, например `@beta`/`@rc`, или точную предварительную версию.

**Что делает команда:**

  * Копирует пакет хуков в `~/.openclaw/hooks/<id>`
  * Включает установленные хуки в `hooks.internal.entries.*`
  * Записывает установку в `hooks.internal.installs`


**Параметры:**

  * `-l, --link`: Связать локальный каталог вместо копирования (добавляет его в `hooks.internal.load.extraDirs`)
  * `--pin`: Записывать установки npm как точно разрешенные `name@version` в `hooks.internal.installs`


**Поддерживаемые архивы:** `.zip`, `.tgz`, `.tar.gz`, `.tar`

**Примеры:**

bashCopy code
[code]
    # Local directoryopenclaw plugins install ./my-hook-pack # Local archiveopenclaw plugins install ./my-hook-pack.zip # NPM packageopenclaw plugins install @openclaw/my-hook-pack # Link a local directory without copyingopenclaw plugins install -l ./my-hook-pack
[/code]

Связанные пакеты хуков считаются управляемыми хуками из каталога, настроенного оператором, а не хуками рабочей области.

## Обновить пакеты хуков

bashCopy code
[code]
    openclaw plugins update <id>openclaw plugins update --all
[/code]

Обновляет отслеживаемые пакеты хуков на основе npm через единый обновлятор plugins.

`openclaw hooks update` по-прежнему работает как псевдоним совместимости, но выводит предупреждение об устаревании и перенаправляет на `openclaw plugins update`.

**Параметры:**

  * `--all`: Обновить все отслеживаемые пакеты хуков
  * `--dry-run`: Показать, что изменилось бы, без записи


Когда сохраненный хеш целостности существует и хеш полученного артефакта меняется, OpenClaw выводит предупреждение и запрашивает подтверждение перед продолжением. Используйте глобальный `--yes`, чтобы пропустить запросы в CI или неинтерактивных запусках.

## Встроенные хуки

### session-memory

Сохраняет контекст сессии в память, когда вы выполняете `/new` или `/reset`.

**Включить:**

bashCopy code
[code]
    openclaw hooks enable session-memory
[/code]

**Вывод:** по умолчанию `~/.openclaw/workspace/memory/YYYY-MM-DD-HHMM.md`. Задайте `hooks.internal.entries.session-memory.llmSlug: true` для слагов имен файлов, сгенерированных моделью.

**См.:** [документацию session-memory](</ru/automation/hooks#session-memory>)

### bootstrap-extra-files

Внедряет дополнительные bootstrap-файлы (например, локальные для монорепозитория `AGENTS.md` / `TOOLS.md`) во время `agent:bootstrap`.

**Включить:**

bashCopy code
[code]
    openclaw hooks enable bootstrap-extra-files
[/code]

**См.:** [документацию bootstrap-extra-files](</ru/automation/hooks#bootstrap-extra-files>)

### command-logger

Записывает все события команд в централизованный файл аудита.

**Включить:**

bashCopy code
[code]
    openclaw hooks enable command-logger
[/code]

**Вывод:** `~/.openclaw/logs/commands.log`

**Просмотреть логи:**

bashCopy code
[code]
    # Recent commandstail -n 20 ~/.openclaw/logs/commands.log # Pretty-printcat ~/.openclaw/logs/commands.log | jq . # Filter by actiongrep '"action":"new"' ~/.openclaw/logs/commands.log | jq .
[/code]

**См.:** [документацию command-logger](</ru/automation/hooks#command-logger>)

### boot-md

Запускает `BOOT.md` при запуске gateway (после запуска каналов).

**События** : `gateway:startup`

**Включить** :

bashCopy code
[code]
    openclaw hooks enable boot-md
[/code]

**См.:** [документацию boot-md](</ru/automation/hooks#boot-md>)

## Связанные разделы

  * [Справочник CLI](</ru/cli>)
  * [Хуки автоматизации](</ru/automation/hooks>)


Was this useful?YesNo

Open issue