---
title: Міграція з Claude
source_url: https://docs.openclaw.ai/uk/install/migrating-claude
scraped_at: 2026-05-25
---

OpenClaw імпортує локальний стан Claude через вбудований провайдер міграції Claude. Провайдер попередньо показує кожен елемент перед зміною стану, редагує секрети в планах і звітах та створює перевірену резервну копію перед застосуванням.

## Два способи імпорту

### Майстер онбордингу

Майстер пропонує Claude, коли виявляє локальний стан Claude.

bashCopy code
[code]
    openclaw onboard --flow import
[/code]

Або вкажіть конкретне джерело:

bashCopy code
[code]
    openclaw onboard --import-from claude --import-source ~/.claude
[/code]

### CLI

Використовуйте `openclaw migrate` для скриптованих або повторюваних запусків. Повну довідку див. у [`openclaw migrate`](</uk/cli/migrate>).

bashCopy code
[code]
    openclaw migrate claude --dry-runopenclaw migrate apply claude --yes
[/code]

Додайте `--from <path>`, щоб імпортувати конкретний домашній каталог Claude Code або корінь проєкту.

## Що імпортується

Інструкції та пам’ять

  * Вміст проєктних `CLAUDE.md` і `.claude/CLAUDE.md` копіюється або додається до `AGENTS.md` у робочому просторі агента OpenClaw.
  * Вміст користувацького `~/.claude/CLAUDE.md` додається до `USER.md` у робочому просторі.

MCP-сервери

Визначення MCP-серверів імпортуються з проєктного `.mcp.json`, Claude Code `~/.claude.json` і Claude Desktop `claude_desktop_config.json`, якщо вони наявні.

Skills і команди

  * Claude Skills із файлом `SKILL.md` копіюються до каталогу Skills робочого простору OpenClaw.
  * Markdown-файли команд Claude у `.claude/commands/` або `~/.claude/commands/` перетворюються на OpenClaw Skills із `disable-model-invocation: true`.


## Що залишається лише в архіві

Провайдер копіює це до звіту міграції для ручного перегляду, але **не** завантажує в активну конфігурацію OpenClaw:

  * Хуки Claude
  * Дозволи Claude і широкі списки дозволених інструментів
  * Стандартні значення середовища Claude
  * `CLAUDE.local.md`
  * `.claude/rules/`
  * Субагенти Claude у `.claude/agents/` або `~/.claude/agents/`
  * Каталоги кешів, планів та історії проєктів Claude Code
  * Розширення Claude Desktop і облікові дані, збережені ОС


OpenClaw відмовляється автоматично виконувати хуки, довіряти спискам дозволів або декодувати непрозорий стан облікових даних OAuth і Desktop. Перенесіть потрібне вручну після перегляду архіву.

## Вибір джерела

Без `--from` OpenClaw перевіряє типовий домашній каталог Claude Code у `~/.claude`, вибраний файл стану Claude Code `~/.claude.json` і конфігурацію MCP Claude Desktop на macOS.

Коли `--from` вказує на корінь проєкту, OpenClaw імпортує лише файли Claude цього проєкту, як-от `CLAUDE.md`, `.claude/settings.json`, `.claude/commands/`, `.claude/skills/` і `.mcp.json`. Під час імпорту з кореня проєкту він не читає ваш глобальний домашній каталог Claude.

## Рекомендований процес

* ### Попередньо перегляньте план

bashCopy code
[code]
    openclaw migrate claude --dry-run
[/code]

У плані перелічено все, що буде змінено, зокрема конфлікти, пропущені елементи та чутливі значення, відредаговані з вкладених полів MCP `env` або `headers`.

* ### Застосуйте з резервною копією

bashCopy code
[code]
    openclaw migrate apply claude --yes
[/code]

OpenClaw створює та перевіряє резервну копію перед застосуванням.

* ### Запустіть doctor

bashCopy code
[code]
    openclaw doctor
[/code]

[Doctor](</uk/gateway/doctor>) перевіряє проблеми конфігурації або стану після імпорту.

* ### Перезапустіть і перевірте

bashCopy code
[code]
    openclaw gateway restartopenclaw status
[/code]

Переконайтеся, що Gateway справний, а імпортовані інструкції, MCP-сервери та Skills завантажено.

## Обробка конфліктів

Застосування відмовляється продовжувати, коли план повідомляє про конфлікти (файл або значення конфігурації вже існує в цільовому місці).

Для свіжого встановлення OpenClaw конфлікти незвичні. Вони зазвичай з’являються, коли ви повторно запускаєте імпорт у налаштуванні, яке вже має користувацькі зміни.

## Вивід JSON для автоматизації

bashCopy code
[code]
    openclaw migrate claude --dry-run --jsonopenclaw migrate apply claude --json --yes
[/code]

З `--json` і без `--yes` застосування друкує план і не змінює стан. Це найбезпечніший режим для CI і спільних скриптів.

## Усунення несправностей

Стан Claude розміщений поза ~/.claude

Передайте `--from /actual/path` (CLI) або `--import-source /actual/path` (онбординг).

Онбординг відмовляється імпортувати в наявне налаштування

Імпорт під час онбордингу потребує свіжого налаштування. Або скиньте стан і повторіть онбординг, або скористайтеся `openclaw migrate apply claude` напряму, що підтримує `--overwrite` і явне керування резервними копіями.

MCP-сервери з Claude Desktop не імпортувалися

Claude Desktop читає `claude_desktop_config.json` зі шляху, специфічного для платформи. Вкажіть `--from` на каталог цього файла, якщо OpenClaw не виявив його автоматично.

Команди Claude стали Skills із вимкненим викликом моделі

Це очікувана поведінка. Команди Claude запускає користувач, тому OpenClaw імпортує їх як Skills із `disable-model-invocation: true`. Відредагуйте frontmatter кожного Skill, якщо хочете, щоб агент викликав їх автоматично.

## Пов’язане

  * [`openclaw migrate`](</uk/cli/migrate>): повна довідка CLI, контракт Plugin і форми JSON.
  * [Посібник із міграції](</uk/install/migrating>): усі шляхи міграції.
  * [Міграція з Hermes](</uk/install/migrating-hermes>): інший шлях міжсистемного імпорту.
  * [Онбординг](</uk/cli/onboard>): процес майстра й неінтерактивні прапорці.
  * [Doctor](</uk/gateway/doctor>): перевірка справності після міграції.
  * [Робочий простір агента](</uk/concepts/agent-workspace>): де розміщено `AGENTS.md`, `USER.md` і Skills.


Was this useful?YesNo