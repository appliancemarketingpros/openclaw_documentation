---
title: Слэш-команды
source_url: https://docs.openclaw.ai/ru/tools/slash-commands
scraped_at: 2026-06-29
---

CapabilitiesSkills

Gateway обрабатывает команды, отправленные как самостоятельные сообщения, начинающиеся с `/`. Bash-команды только для хоста используют `! <cmd>` (с `/bash <cmd>` как псевдонимом).

Когда разговор привязан к ACP-сеансу, обычный текст направляется в ACP harness. Команды управления Gateway остаются локальными: `/acp ...` всегда попадает в обработчик команд OpenClaw, а `/status` и `/unfocus` остаются локальными, когда обработка команд включена для поверхности.

## Три типа команд

**Команды** Самостоятельные сообщения `/...`, обрабатываемые Gateway. Должны быть единственным содержимым сообщения. **Директивы** `/think`, `/fast`, `/verbose`, `/trace`, `/reasoning`, `/elevated`, `/exec`, `/model`, `/queue` — удаляются из сообщения до того, как модель его увидит. Сохраняют настройки сеанса, если отправлены отдельно; действуют как встроенные подсказки, когда отправлены вместе с другим текстом. **Встроенные сокращения** `/help`, `/commands`, `/status`, `/whoami` — выполняются немедленно и удаляются до того, как модель увидит оставшийся текст. Только для авторизованных отправителей.

Подробности поведения директив

  * Директивы удаляются из сообщения до того, как модель его увидит.
  * В сообщениях **только с директивами** (сообщение состоит только из директив) они сохраняются в сеансе и отвечают подтверждением.
  * В сообщениях **обычного чата** с другим текстом они действуют как встроенные подсказки и **не** сохраняют настройки сеанса.
  * Директивы применяются только для **авторизованных отправителей**. Если задано `commands.allowFrom`, используется только этот список разрешений; иначе авторизация берется из списков разрешений/сопряжения канала плюс `commands.useAccessGroups`. У неавторизованных отправителей директивы обрабатываются как обычный текст.


## Конфигурация

json5Copy code
[code]
    {  commands: {    native: "auto",    nativeSkills: "auto",    text: true,    bash: false,    bashForegroundMs: 2000,    config: false,    mcp: false,    plugins: false,    debug: false,    restart: true,    ownerAllowFrom: ["discord:123456789012345678"],    ownerDisplay: "raw",    ownerDisplaySecret: "${OWNER_ID_HASH_SECRET}",    allowFrom: {      "*": ["user1"],      discord: ["user:123"],    },    useAccessGroups: true,  },}
[/code]

Включает разбор `/...` в сообщениях чата. На поверхностях без нативных команд (WhatsApp, WebChat, Signal, iMessage, Google Chat, Microsoft Teams), текстовые команды работают даже при значении `false`.

Регистрирует нативные команды. Auto: включено для Discord/Telegram; выключено для Slack; игнорируется для провайдеров без нативной поддержки. Переопределяется для каждого канала через `channels.<provider>.commands.native`. В Discord значение `false` пропускает регистрацию slash-команд; ранее зарегистрированные команды могут оставаться видимыми, пока не будут удалены.

Регистрирует команды Skills нативно, когда это поддерживается. Auto: включено для Discord/Telegram; выключено для Slack. Переопределяется через `channels.<provider>.commands.nativeSkills`.

Включает `! <cmd>` для запуска shell-команд хоста (псевдоним `/bash <cmd>`). Требует списков разрешений `tools.elevated`.

Сколько bash ждет перед переключением в фоновый режим (`0` переводит в фон немедленно).

Включает `/config` (читает/записывает `openclaw.json`). Только для владельца.

Включает `/mcp` (читает/записывает управляемую OpenClaw конфигурацию MCP в `mcp.servers`). Только для владельца.

Включает `/plugins` (обнаружение/статус Plugin плюс установка и включение/отключение). Запись только для владельца.

Включает `/debug` (переопределения конфигурации только на время выполнения). Только для владельца.

Включает `/restart` и действия инструментов перезапуска Gateway.

Явный список разрешенных владельцев для поверхностей команд только для владельца. Отдельно от `commands.allowFrom` и доступа через сопряжение DM.

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImNoYW5uZWxzLjxjaGFubmVs .commands.enforceOwnerForCommands" type="boolean" default="false"> Для каждого канала: требует идентичность владельца для команд только для владельца. Когда `true`, отправитель должен соответствовать `commands.ownerAllowFrom` или иметь внутреннюю область `operator.admin`. Запись wildcard в `allowFrom` **недостаточна**.

Управляет тем, как идентификаторы владельцев отображаются в системном prompt.

Секрет HMAC, используемый при `commands.ownerDisplay: "hash"`.

Список разрешений по провайдерам для авторизации команд. Когда он настроен, это **единственный** источник авторизации для команд и директив. Используйте `"*"` для глобального значения по умолчанию; ключи конкретных провайдеров переопределяют его.

Применяет списки разрешений/политики для команд, когда `commands.allowFrom` не задан.

## Список команд

Команды поступают из трех источников:

  * **Встроенные команды ядра:** `src/auto-reply/commands-registry.shared.ts`
  * **Сгенерированные dock-команды:** `src/auto-reply/commands-registry.data.ts`
  * **Команды Plugin:** вызовы `registerCommand()` в Plugin


Доступность зависит от флагов конфигурации, поверхности канала и установленных/включенных plugins.

### Команды ядра

Сеансы и запуски

Команда | Описание  
---|---  
`/new [model]` | Архивировать текущий сеанс и начать новый  
`/reset [soft [message]]` | Сбросить текущий сеанс на месте. `soft` сохраняет transcript, удаляет повторно используемые идентификаторы сеансов CLI backend и повторно запускает startup  
`/name <title>` | Назвать или переименовать текущий сеанс. Опустите заголовок, чтобы увидеть текущее имя и предложение  
`/compact [instructions]` | Сжать контекст сеанса. См. [Compaction](</ru/concepts/compaction>)  
`/stop` | Прервать текущий запуск  
`/session idle <duration|off>` | Управлять истечением срока простоя привязки thread  
`/session max-age <duration|off>` | Управлять истечением максимального срока привязки thread  
`/export-session [path]` | Экспортировать текущий сеанс в HTML. Псевдоним: `/export`  
`/export-trajectory [path]` | Экспортировать пакет траектории JSONL для текущего сеанса. Псевдоним: `/trajectory`  
  
Модель и элементы управления запуском

Команда | Описание  
---|---  
`/think <level|default>` | Задать уровень мышления или очистить переопределение сеанса. Псевдонимы: `/thinking`, `/t`  
`/verbose on|off|full` | Переключить подробный вывод. Псевдоним: `/v`  
`/trace on|off` | Переключить вывод trace Plugin для текущего сеанса  
`/fast [status|auto|on|off|default]` | Показать, задать или очистить быстрый режим  
`/reasoning [on|off|stream]` | Переключить видимость рассуждений. Псевдоним: `/reason`  
`/elevated [on|off|ask|full]` | Переключить повышенный режим. Псевдоним: `/elev`  
`/exec host=<auto|sandbox|gateway|node> security=<deny|allowlist|full> ask=<off|on-miss|always> node=<id>` | Показать или задать exec по умолчанию  
`/model [name|#|status]` | Показать или задать модель  
`/models [provider] [page] [limit=<n>|all]` | Перечислить настроенных/доступных по авторизации провайдеров или модели  
`/queue <mode>` | Управлять поведением очереди активных запусков. См. [Queue](</ru/concepts/queue>) и [Управление Queue](</ru/concepts/queue-steering>)  
`/steer <message>` | Внедрить указания в активный запуск. Псевдоним: `/tell`. См. [Steer](</ru/tools/steer>)  
  
безопасность verbose / trace / fast / reasoning

  * `/verbose` предназначен для отладки — держите его **выключенным** при обычном использовании.
  * `/trace` раскрывает только принадлежащие Plugin строки trace/debug; обычная подробная болтовня остается выключенной.
  * `/fast auto|on|off` сохраняет переопределение сеанса; используйте опцию Sessions UI `inherit`, чтобы очистить его.
  * `/fast` зависит от провайдера: OpenAI/Codex сопоставляют его с `service_tier=priority`; прямые запросы Anthropic сопоставляют его с `service_tier=auto` или `standard_only`.
  * `/reasoning`, `/verbose` и `/trace` рискованны в групповых настройках — они могут раскрыть внутренние рассуждения или диагностику Plugin. Держите их выключенными в групповых чатах.

Подробности переключения модели

  * `/model` немедленно сохраняет новую модель в сеанс.
  * Если агент простаивает, следующий запуск сразу использует ее.
  * Если запуск активен, переключение помечается как ожидающее и применяется в следующей чистой точке повторной попытки.


Обнаружение и статус

Команда | Описание  
---|---  
`/help` | Показать краткую справку  
`/commands` | Показать сгенерированный каталог команд  
`/tools [compact|verbose]` | Показать, что текущий агент может использовать прямо сейчас  
`/status` | Показать статус выполнения/среды выполнения, время работы Gateway и системы, состояние Plugin, а также использование/квоту провайдера  
`/status plugins` | Показать подробное состояние Plugin: ошибки загрузки, карантины, сбои каналов, проблемы зависимостей, уведомления о совместимости  
`/goal [status|start|pause|resume|complete|block|clear] ...` | Управлять постоянной [целью](</ru/tools/goal>) текущего сеанса  
`/diagnostics [note]` | Поток отчета в поддержку только для владельца. Каждый раз запрашивает одобрение exec  
`/crestodian <request>` | Запустить помощник настройки и ремонта Crestodian из DM владельца  
`/tasks` | Перечислить активные/недавние фоновые задачи для текущего сеанса  
`/context [list|detail|map|json]` | Объяснить, как собирается контекст  
`/whoami` | Показать ваш идентификатор отправителя. Псевдоним: `/id`  
`/usage off|tokens|full|reset|cost` | Управлять футером использования для каждого ответа (`reset`/`inherit`/`clear`/`default` очищает переопределение сеанса для повторного наследования настроенного значения по умолчанию) или вывести локальную сводку затрат  
  
Skills, списки разрешений, одобрения

Команда | Описание  
---|---  
`/skill <name> [input]` | Запустить skill по имени  
`/allowlist [list|add|remove] ...` | Управлять записями списка разрешений. Только текст  
`/approve <id> <decision>` | Разрешить запросы одобрения exec или Plugin  
`/btw <question>` | Задать побочный вопрос без изменения контекста сеанса. Псевдоним: `/side`. См. [BTW](</ru/tools/btw>)  
  
Субагенты и ACP

Команда | Описание  
---|---  
`/subagents list|log|info` | Проверить запуски субагентов для текущей сессии  
`/acp spawn|cancel|steer|close|sessions|status|set-mode|set|cwd|permissions|timeout|model|reset-options|doctor|install|help` | Управлять сессиями ACP и параметрами среды выполнения  
`/focus <target>` | Привязать текущую ветку Discord или тему Telegram к цели сессии  
`/unfocus` | Удалить текущую привязку ветки  
`/agents` | Показать агентов, привязанных к ветке, для текущей сессии  
  
Запись только для владельца и администрирование

Команда | Требуется | Описание  
---|---|---  
`/config show|get|set|unset` | `commands.config: true` | Читать или записывать `openclaw.json`. Только для владельца  
`/mcp show|get|set|unset` | `commands.mcp: true` | Читать или записывать конфигурацию MCP-сервера, управляемую OpenClaw. Только для владельца  
`/plugins list|inspect|show|get|install|enable|disable` | `commands.plugins: true` | Проверять или изменять состояние Plugin. Запись только для владельца. Псевдоним: `/plugin`  
`/debug show|set|unset|reset` | `commands.debug: true` | Переопределения конфигурации только для среды выполнения. Только для владельца  
`/restart` | `commands.restart: true` (по умолчанию) | Перезапустить OpenClaw  
`/send on|off|inherit` | владелец | Задать политику отправки  
  
Голос, TTS, управление каналом

Команда | Описание  
---|---  
`/tts on|off|status|chat|latest|provider|limit|summary|audio|help` | Управлять TTS. См. [TTS](</ru/tools/tts>)  
`/activation mention|always` | Задать режим активации группы  
`/bash <command>` | Выполнить команду оболочки хоста. Псевдоним: `! <command>`. Требуется `commands.bash: true`  
`!poll [sessionId]` | Проверить фоновую задачу bash  
`!stop [sessionId]` | Остановить фоновую задачу bash  
  
### Команды Dock

Команды Dock переключают маршрут ответа активной сессии на другой связанный канал. См. [Стыковка каналов](</ru/concepts/channel-docking>) для настройки и устранения неполадок.

Сгенерировано из Plugin каналов с поддержкой нативных команд:

  * `/dock-discord` (псевдоним: `/dock_discord`)
  * `/dock-mattermost` (псевдоним: `/dock_mattermost`)
  * `/dock-slack` (псевдоним: `/dock_slack`)
  * `/dock-telegram` (псевдоним: `/dock_telegram`)


Для команд Dock требуется `session.identityLinks`. Исходный отправитель и целевой peer должны находиться в одной группе идентичности.

### Команды встроенных Plugin

Команда | Описание  
---|---  
`/dreaming [on|off|status|help]` | Включить или отключить Dreaming памяти. См. [Dreaming](</ru/concepts/dreaming>)  
`/pair [qr|status|pending|approve|cleanup|notify]` | Управлять сопряжением устройств. См. [Сопряжение](</ru/channels/pairing>)  
`/phone status|arm ...|disarm` | Временно активировать высокорисковые команды телефонного узла  
`/voice status|list|set <voiceId>` | Управлять конфигурацией голоса Talk. Нативное имя Discord: `/talkvoice`  
`/card ...` | Отправлять пресеты rich card LINE. См. [LINE](</ru/channels/line>)  
`/codex status|models|threads|resume|compact|review|diagnostics|account|mcp|skills` | Управлять harness сервера приложения Codex. См. [Codex harness](</ru/plugins/codex-harness>)  
  
Только QQBot: `/bot-ping`, `/bot-version`, `/bot-help`, `/bot-upgrade`, `/bot-logs`

### Команды Skills

Skills, вызываемые пользователем, доступны как slash-команды:

  * `/skill <name> [input]` всегда работает как универсальная точка входа.
  * Skills могут регистрироваться как прямые команды (например, `/prose` для OpenProse).
  * Регистрация нативных команд Skills управляется `commands.nativeSkills` и `channels.<provider>.commands.nativeSkills`.
  * Имена нормализуются до `a-z0-9_` (максимум 32 символа); при конфликтах добавляются числовые суффиксы.


Диспетчеризация команд Skill

По умолчанию команды Skill маршрутизируются в модель как обычный запрос.

Skills могут объявить `command-dispatch: tool`, чтобы маршрутизироваться напрямую в инструмент (детерминированно, без участия модели). Пример: `/prose` (Plugin OpenProse) — см. [OpenProse](</ru/prose>).

Аргументы нативных команд

Discord использует автодополнение для динамических параметров и кнопочные меню, когда обязательные аргументы опущены. Telegram и Slack показывают кнопочное меню для команд с вариантами выбора. Динамические варианты разрешаются относительно модели целевой сессии, поэтому специфичные для модели параметры, такие как уровни `/think`, учитывают переопределение `/model` сессии.

## `/tools` — что агент может использовать сейчас

`/tools` отвечает на вопрос среды выполнения: **что этот агент может использовать прямо сейчас в этом разговоре** — а не показывает статический каталог конфигурации.

textCopy code
[code]
    /tools         # compact view/tools verbose # with short descriptions
[/code]

Результаты имеют область действия сессии. Изменение агента, канала, ветки, авторизации отправителя или модели может изменить вывод. Для редактирования профиля и переопределений используйте панель Tools в Control UI или поверхности конфигурации.

## `/model` — выбор модели

textCopy code
[code]
    /model             # show model picker/model list        # same/model 3           # select by number from picker/model openai/gpt-5.4/model opus@anthropic:default/model default     # clear the session model selection/model status      # detailed view with endpoint and API mode
[/code]

В Discord `/model` и `/models` открывают интерактивный выбор с выпадающими списками провайдеров и моделей. Выбор учитывает `agents.defaults.models`, включая записи `provider/*`.

## `/config` — запись конфигурации на диск

textCopy code
[code]
    /config show/config show messages.responsePrefix/config get messages.responsePrefix/config set messages.responsePrefix="[openclaw]"/config unset messages.responsePrefix
[/code]

Конфигурация проверяется перед записью. Недопустимые изменения отклоняются. Обновления `/config` сохраняются после перезапусков.

## `/mcp` — конфигурация MCP-сервера

textCopy code
[code]
    /mcp show/mcp show context7/mcp set context7={"command":"uvx","args":["context7-mcp"]}/mcp unset context7
[/code]

`/mcp` хранит конфигурацию в конфигурации OpenClaw, а не во встроенных настройках проекта агента.

## `/debug` — переопределения только для среды выполнения

textCopy code
[code]
    /debug show/debug set messages.responsePrefix="[openclaw]"/debug set channels.whatsapp.allowFrom=["+1555","+4477"]/debug unset messages.responsePrefix/debug reset
[/code]

## `/plugins` — управление Plugin

textCopy code
[code]
    /plugins/plugins list/plugin show context7/plugins enable context7/plugins disable context7/plugins install ./path/to/plugin
[/code]

`/plugins enable|disable` обновляет конфигурацию Plugin и выполняет hot-reload среды выполнения Plugin Gateway для новых ходов агента. `/plugins install` автоматически перезапускает управляемые Gateways, потому что исходные модули Plugin изменились.

## `/trace` — вывод трассировки Plugin

textCopy code
[code]
    /trace          # show current trace state/trace on/trace off
[/code]

`/trace` показывает строки трассировки/отладки Plugin в области действия сессии без полного verbose режима. Он не заменяет `/debug` (переопределения среды выполнения) или `/verbose` (обычный вывод инструмента).

## `/btw` — побочные вопросы

`/btw` — это быстрый побочный вопрос о контексте текущей сессии. Псевдоним: `/side`.

textCopy code
[code]
    /btw what are we doing right now?/side what changed while the main run continued?
[/code]

В отличие от обычного сообщения:

  * Использует текущую сессию как фоновый контекст.
  * В сессиях Codex harness запускается как эфемерная побочная ветка Codex.
  * **Не** изменяет будущий контекст сессии.
  * Не записывается в историю transcript.


См. [Побочные вопросы BTW](</ru/tools/btw>) для полного поведения.

## Примечания о поверхностях

Область действия сессии по поверхности

  * **Текстовые команды:** выполняются в обычной чат-сессии (личные сообщения используют общий `main`, группы имеют собственную сессию).
  * **Нативные команды Discord:** `agent:<agentId>:discord:slash:<userId>`
  * **Нативные команды Slack:** `agent:<agentId>:slack:slash:<userId>` (префикс настраивается через `channels.slack.slashCommand.sessionPrefix`)
  * **Нативные команды Telegram:** `telegram:slash:<userId>` (нацеливаются на чат-сессию через `CommandTargetSessionKey`)
  * **`/stop`** нацеливается на активную чат-сессию, чтобы прервать текущий запуск.

Особенности Slack

`channels.slack.slashCommand` поддерживает одну команду в стиле `/openclaw`. При `commands.native: true` создайте одну slash-команду Slack для каждой встроенной команды. Зарегистрируйте `/agentstatus` (не `/status`), потому что Slack резервирует `/status`. Текстовая `/status` по-прежнему работает в сообщениях Slack.

Быстрый путь и встроенные сокращения

  * Сообщения только с командами от отправителей из allowlist обрабатываются немедленно (в обход очереди и модели).
  * Встроенные сокращения (`/help`, `/commands`, `/status`, `/whoami`) также работают внутри обычных сообщений и удаляются до того, как модель увидит оставшийся текст.
  * Неавторизованные сообщения только с командами молча игнорируются; встроенные токены `/...` рассматриваются как обычный текст.

Примечания к аргументам

  * Команды принимают необязательный `:` между командой и аргументами (`/think: high`, `/send: on`).
  * `/new <model>` принимает псевдоним модели, `provider/model` или имя провайдера (нечеткое совпадение); если совпадения нет, текст рассматривается как тело сообщения.
  * `/allowlist add|remove` требует `commands.config: true` и учитывает `configWrites` канала.


## Использование и статус провайдера

  * **Использование/квота провайдера** (например, "Claude 80% left") отображается в `/status` для провайдера текущей модели, когда включено отслеживание использования.
  * **Строки токенов/кэша** в `/status` могут fallback к последней записи использования transcript, когда live-снимок сессии разрежен.
  * **Execution и среда выполнения:** `/status` сообщает `Execution` для эффективного пути sandbox и `Runtime` для того, кто запускает сессию: `OpenClaw Default`, `OpenAI Codex`, backend CLI или backend ACP.
  * **Токены/стоимость на ответ:** управляется `/usage off|tokens|full`.
  * `/model status` относится к моделям/аутентификации/endpoint, а не к использованию.


## Связанные разделы

[**Skills** Как slash-команды Skills регистрируются и ограничиваются. ](</ru/tools/skills>) [**Создание Skills** Создайте Skill, который регистрирует собственную slash-команду. ](</ru/tools/creating-skills>) [**BTW** Побочные вопросы без изменения контекста сессии. ](</ru/tools/btw>) [**Steer** Направляйте агента в середине запуска с помощью `/steer`. ](</ru/tools/steer>)

Was this useful?YesNo

Open issue