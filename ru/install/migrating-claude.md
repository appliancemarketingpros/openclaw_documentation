---
title: Миграция с Claude
source_url: https://docs.openclaw.ai/ru/install/migrating-claude
scraped_at: 2026-06-29
---

InstallMaintenance

OpenClaw импортирует локальное состояние Claude через встроенный поставщик миграции Claude. Поставщик предварительно показывает каждый элемент перед изменением состояния, скрывает секреты в планах и отчетах и создает проверенную резервную копию перед применением.

## Два способа импорта

### Мастер онбординга

Мастер предлагает Claude, когда обнаруживает локальное состояние Claude.

bashCopy code
[code]
    openclaw onboard --flow import
[/code]

Или укажите конкретный источник:

bashCopy code
[code]
    openclaw onboard --import-from claude --import-source ~/.claude
[/code]

### CLI

Используйте `openclaw migrate` для сценарных или повторяемых запусков. Полную справку см. в [`openclaw migrate`](</ru/cli/migrate>).

bashCopy code
[code]
    openclaw migrate claude --dry-runopenclaw migrate apply claude --yes
[/code]

Добавьте `--from <path>`, чтобы импортировать конкретный домашний каталог Claude Code или корень проекта.

## Что импортируется

Инструкции и память

  * Содержимое проектных `CLAUDE.md` и `.claude/CLAUDE.md` копируется или добавляется в `AGENTS.md` рабочей области агента OpenClaw.
  * Содержимое пользовательского `~/.claude/CLAUDE.md` добавляется в `USER.md` рабочей области.

Серверы MCP

Определения серверов MCP импортируются из проектного `.mcp.json`, Claude Code `~/.claude.json` и Claude Desktop `claude_desktop_config.json`, если они существуют.

Skills и команды

  * Skills Claude с файлом `SKILL.md` копируются в каталог Skills рабочей области OpenClaw.
  * Markdown-файлы команд Claude в `.claude/commands/` или `~/.claude/commands/` преобразуются в Skills OpenClaw с `disable-model-invocation: true`.


## Что остается только в архиве

Поставщик копирует это в отчет о миграции для ручной проверки, но **не** загружает в активную конфигурацию OpenClaw:

  * хуки Claude
  * разрешения Claude и широкие списки разрешенных инструментов
  * значения среды по умолчанию Claude
  * `CLAUDE.local.md`
  * `.claude/rules/`
  * субагенты Claude в `.claude/agents/` или `~/.claude/agents/`
  * кэши, планы и каталоги истории проектов Claude Code
  * расширения Claude Desktop и учетные данные, сохраненные ОС


OpenClaw отказывается автоматически выполнять хуки, доверять спискам разрешений или декодировать непрозрачное состояние учетных данных OAuth и Desktop. Перенесите нужное вручную после просмотра архива.

## Выбор источника

Без `--from` OpenClaw проверяет домашний каталог Claude Code по умолчанию в `~/.claude`, выборочный файл состояния Claude Code `~/.claude.json` и конфигурацию MCP Claude Desktop на macOS.

Когда `--from` указывает на корень проекта, OpenClaw импортирует только файлы Claude этого проекта, такие как `CLAUDE.md`, `.claude/settings.json`, `.claude/commands/`, `.claude/skills/` и `.mcp.json`. Во время импорта из корня проекта он не читает ваш глобальный домашний каталог Claude.

## Рекомендуемый процесс

* ### Предварительно просмотрите план

bashCopy code
[code]
    openclaw migrate claude --dry-run
[/code]

В плане перечисляется все, что изменится, включая конфликты, пропущенные элементы и чувствительные значения, скрытые во вложенных полях MCP `env` или `headers`.

* ### Примените с резервной копией

bashCopy code
[code]
    openclaw migrate apply claude --yes
[/code]

OpenClaw создает и проверяет резервную копию перед применением.

* ### Запустите doctor

bashCopy code
[code]
    openclaw doctor
[/code]

[Doctor](</ru/gateway/doctor>) проверяет наличие проблем с конфигурацией или состоянием после импорта.

* ### Перезапустите и проверьте

bashCopy code
[code]
    openclaw gateway restartopenclaw status
[/code]

Убедитесь, что Gateway исправен, а импортированные инструкции, серверы MCP и Skills загружены.

## Обработка конфликтов

Применение отказывается продолжать работу, когда план сообщает о конфликтах (файл или значение конфигурации уже существует в целевом расположении).

Для новой установки OpenClaw конфликты необычны. Обычно они появляются, когда вы повторно запускаете импорт в настройке, где уже есть пользовательские правки.

## Вывод JSON для автоматизации

bashCopy code
[code]
    openclaw migrate claude --dry-run --jsonopenclaw migrate apply claude --json --yes
[/code]

С `--json` и без `--yes` применение печатает план и не изменяет состояние. Это самый безопасный режим для CI и общих скриптов.

## Устранение неполадок

Состояние Claude находится вне ~/.claude

Передайте `--from /actual/path` (CLI) или `--import-source /actual/path` (онбординг).

Онбординг отказывается импортировать в существующую настройку

Импорт при онбординге требует новой настройки. Либо сбросьте состояние и пройдите онбординг заново, либо используйте `openclaw migrate apply claude` напрямую; он поддерживает `--overwrite` и явное управление резервными копиями.

Серверы MCP из Claude Desktop не импортировались

Claude Desktop читает `claude_desktop_config.json` из пути, зависящего от платформы. Укажите `--from` на каталог этого файла, если OpenClaw не обнаружил его автоматически.

Команды Claude стали Skills с отключенным вызовом модели

Так задумано. Команды Claude запускаются пользователем, поэтому OpenClaw импортирует их как Skills с `disable-model-invocation: true`. Отредактируйте frontmatter каждого Skill, если хотите, чтобы агент вызывал их автоматически.

## См. также

  * [`openclaw migrate`](</ru/cli/migrate>): полная справка CLI, контракт Plugin и формы JSON.
  * [Руководство по миграции](</ru/install/migrating>): все пути миграции.
  * [Миграция с Hermes](</ru/install/migrating-hermes>): другой путь межсистемного импорта.
  * [Онбординг](</ru/cli/onboard>): поток мастера и флаги для неинтерактивного режима.
  * [Doctor](</ru/gateway/doctor>): проверка работоспособности после миграции.
  * [Рабочая область агента](</ru/concepts/agent-workspace>): где находятся `AGENTS.md`, `USER.md` и Skills.


Was this useful?YesNo

Open issue