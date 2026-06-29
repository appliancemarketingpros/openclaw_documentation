---
title: CLI песочницы
source_url: https://docs.openclaw.ai/ru/cli/sandbox
scraped_at: 2026-06-29
---

ReferenceCLI commands

Управляйте sandbox-средами выполнения для изолированного выполнения агентов.

## Обзор

OpenClaw может запускать агентов в изолированных sandbox-средах выполнения для безопасности. Команды `sandbox` помогают проверять и пересоздавать эти среды выполнения после обновлений или изменений конфигурации.

Сегодня это обычно означает:

  * Docker sandbox-контейнеры
  * SSH sandbox-среды выполнения, когда `agents.defaults.sandbox.backend = "ssh"`
  * OpenShell sandbox-среды выполнения, когда `agents.defaults.sandbox.backend = "openshell"`


Для `ssh` и OpenShell `remote` пересоздание важнее, чем для Docker:

  * удаленное рабочее пространство является каноническим после начального заполнения
  * `openclaw sandbox recreate` удаляет это каноническое удаленное рабочее пространство для выбранной области
  * при следующем использовании оно снова заполняется из текущего локального рабочего пространства


## Команды

### `openclaw sandbox explain`

Проверьте **эффективные** режим/область/доступ к рабочему пространству sandbox, политику sandbox-инструментов и привилегированные шлюзы (с путями к ключам конфигурации для исправления).

bashCopy code
[code]
    openclaw sandbox explainopenclaw sandbox explain --session agent:main:mainopenclaw sandbox explain --agent workopenclaw sandbox explain --json
[/code]

### `openclaw sandbox list`

Выведите все sandbox-среды выполнения с их статусом и конфигурацией.

bashCopy code
[code]
    openclaw sandbox listopenclaw sandbox list --browser  # List only browser containersopenclaw sandbox list --json     # JSON output
[/code]

**Вывод включает:**

  * Имя и статус среды выполнения
  * Бэкенд (`docker`, `openshell` и т. д.)
  * Метку конфигурации и совпадает ли она с текущей конфигурацией
  * Возраст (время с момента создания)
  * Время простоя (время с последнего использования)
  * Связанный сеанс/агент


### `openclaw sandbox recreate`

Удалите sandbox-среды выполнения, чтобы принудительно пересоздать их с обновленной конфигурацией.

bashCopy code
[code]
    openclaw sandbox recreate --all                # Recreate all containersopenclaw sandbox recreate --session main       # Specific sessionopenclaw sandbox recreate --agent mybot        # Specific agentopenclaw sandbox recreate --browser            # Only browser containersopenclaw sandbox recreate --all --force        # Skip confirmation
[/code]

**Параметры:**

  * `--all`: пересоздать все sandbox-контейнеры
  * `--session <key>`: пересоздать контейнер для определенного сеанса
  * `--agent <id>`: пересоздать контейнеры для определенного агента
  * `--browser`: пересоздать только браузерные контейнеры
  * `--force`: пропустить запрос подтверждения


## Сценарии использования

### После обновления образа Docker

bashCopy code
[code]
    # Pull new imagedocker pull openclaw-sandbox:latestdocker tag openclaw-sandbox:latest openclaw-sandbox:bookworm-slim # Update config to use new image# Edit config: agents.defaults.sandbox.docker.image (or agents.list[].sandbox.docker.image) # Recreate containersopenclaw sandbox recreate --all
[/code]

### После изменения конфигурации sandbox

bashCopy code
[code]
    # Edit config: agents.defaults.sandbox.* (or agents.list[].sandbox.*) # Recreate to apply new configopenclaw sandbox recreate --all
[/code]

### После изменения SSH-цели или материала SSH-аутентификации

bashCopy code
[code]
    # Edit config:# - agents.defaults.sandbox.backend# - agents.defaults.sandbox.ssh.target# - agents.defaults.sandbox.ssh.workspaceRoot# - agents.defaults.sandbox.ssh.identityFile / certificateFile / knownHostsFile# - agents.defaults.sandbox.ssh.identityData / certificateData / knownHostsData openclaw sandbox recreate --all
[/code]

Для основного бэкенда `ssh` пересоздание удаляет корень удаленного рабочего пространства для каждой области на SSH-цели. Следующий запуск снова заполняет его из локального рабочего пространства.

### После изменения источника, политики или режима OpenShell

bashCopy code
[code]
    # Edit config:# - agents.defaults.sandbox.backend# - plugins.entries.openshell.config.from# - plugins.entries.openshell.config.mode# - plugins.entries.openshell.config.policy openclaw sandbox recreate --all
[/code]

Для режима OpenShell `remote` пересоздание удаляет каноническое удаленное рабочее пространство для этой области. Следующий запуск снова заполняет его из локального рабочего пространства.

### После изменения setupCommand

bashCopy code
[code]
    openclaw sandbox recreate --all# or just one agent:openclaw sandbox recreate --agent family
[/code]

### Только для определенного агента

bashCopy code
[code]
    # Update only one agent's containersopenclaw sandbox recreate --agent alfred
[/code]

## Зачем это нужно

Когда вы обновляете конфигурацию sandbox:

  * Существующие среды выполнения продолжают работать со старыми настройками.
  * Среды выполнения удаляются только после 24 часов неактивности.
  * Регулярно используемые агенты сохраняют старые среды выполнения активными на неопределенный срок.


Используйте `openclaw sandbox recreate`, чтобы принудительно удалить старые среды выполнения. Они автоматически пересоздаются с текущими настройками, когда снова понадобятся.

## Миграция реестра

OpenClaw хранит метаданные sandbox-сред выполнения в общей базе данных состояния SQLite. В старых установках все еще могут быть устаревшие файлы реестра sandbox:

  * `~/.openclaw/sandbox/containers.json`
  * `~/.openclaw/sandbox/browsers.json`


В некоторых обновлениях также может быть по одному JSON-фрагменту на контейнер/браузер в `~/.openclaw/sandbox/containers/` или `~/.openclaw/sandbox/browsers/`. Обычные операции чтения sandbox-сред выполнения не перезаписывают эти устаревшие источники. Запустите `openclaw doctor --fix`, чтобы перенести допустимые устаревшие записи в SQLite. Недопустимые устаревшие файлы помещаются в карантин, чтобы один поврежденный старый реестр не мог скрыть текущие записи сред выполнения.

## Конфигурация

Настройки sandbox находятся в `~/.openclaw/openclaw.json` в `agents.defaults.sandbox` (переопределения для отдельных агентов указываются в `agents.list[].sandbox`):

jsoncCopy code
[code]
    {  "agents": {    "defaults": {      "sandbox": {        "mode": "all", // off, non-main, all        "backend": "docker", // docker, ssh, openshell        "scope": "agent", // session, agent, shared        "docker": {          "image": "openclaw-sandbox:bookworm-slim",          "containerPrefix": "openclaw-sbx-",          // ... more Docker options        },        "prune": {          "idleHours": 24, // Auto-prune after 24h idle          "maxAgeDays": 7, // Auto-prune after 7 days        },      },    },  },}
[/code]

## См. также

  * [Справочник CLI](</ru/cli>)
  * [Sandboxing](</ru/gateway/sandboxing>)
  * [Рабочее пространство агента](</ru/concepts/agent-workspace>)
  * [Doctor](</ru/gateway/doctor>): проверяет настройку sandbox.


Was this useful?YesNo

Open issue