---
title: Агенти ACP — налаштування
source_url: https://docs.openclaw.ai/uk/tools/acp-agents-setup
scraped_at: 2026-05-25
---

Для огляду, операторського runbook і концепцій див. [ACP-агенти](</uk/tools/acp-agents>).

Наведені нижче розділи охоплюють конфігурацію acpx harness, налаштування Plugin для MCP-мостів і конфігурацію дозволів.

Використовуйте цю сторінку лише тоді, коли налаштовуєте маршрут ACP/acpx. Для нативної конфігурації runtime app-server Codex використовуйте [Codex harness](</uk/plugins/codex-harness>). Для ключів OpenAI API або конфігурації model-provider Codex OAuth використовуйте [OpenAI](</uk/providers/openai>).

Codex має два маршрути OpenClaw:

Маршрут | Конфігурація/команда | Сторінка налаштування  
---|---|---  
Нативний app-server Codex | `/codex ...`, agent refs `openai/gpt-*` | [Codex harness](</uk/plugins/codex-harness>)  
Явний адаптер Codex ACP | `/acp spawn codex`, `runtime: "acp", agentId: "codex"` | Ця сторінка  
  
Надавайте перевагу нативному маршруту, якщо вам явно не потрібна поведінка ACP/acpx.

## Підтримка acpx harness (поточна)

Поточні вбудовані псевдоніми acpx harness:

  * `claude`
  * `codex`
  * `copilot`
  * `cursor` (Cursor CLI: `cursor-agent acp`)
  * `droid`
  * `gemini`
  * `iflow`
  * `kilocode`
  * `kimi`
  * `kiro`
  * `openclaw`
  * `opencode`
  * `pi`
  * `qwen`


Коли OpenClaw використовує backend acpx, надавайте перевагу цим значенням для `agentId`, якщо ваша конфігурація acpx не визначає власні псевдоніми агентів. Якщо ваша локальна інсталяція Cursor усе ще надає ACP як `agent acp`, перевизначте команду агента `cursor` у вашій конфігурації acpx замість зміни вбудованого значення за замовчуванням.

Пряме використання acpx CLI також може націлювати довільні адаптери через `--agent <command>`, але цей необроблений аварійний обхід є функцією acpx CLI (а не звичайним шляхом OpenClaw `agentId`).

Керування моделлю залежить від можливостей адаптера. Посилання на моделі Codex ACP нормалізуються OpenClaw перед запуском. Іншим harness потрібні ACP `models` плюс підтримка `session/set_model`; якщо harness не надає ні цієї можливості ACP, ні власного прапорця моделі під час запуску, OpenClaw/acpx не може примусово вибрати модель.

## Обов’язкова конфігурація

Базова конфігурація Core ACP:

json5Copy code
[code]
    {  acp: {    enabled: true,    // Optional. Default is true; set false to pause ACP dispatch while keeping /acp controls.    dispatch: { enabled: true },    backend: "acpx",    defaultAgent: "codex",    allowedAgents: [      "claude",      "codex",      "copilot",      "cursor",      "droid",      "gemini",      "iflow",      "kilocode",      "kimi",      "kiro",      "openclaw",      "opencode",      "pi",      "qwen",    ],    maxConcurrentSessions: 8,    stream: {      coalesceIdleMs: 300,      maxChunkChars: 1200,    },    runtime: {      ttlMinutes: 120,    },  },}
[/code]

Конфігурація прив’язки потоків залежить від адаптера каналу. Приклад для Discord:

json5Copy code
[code]
    {  session: {    threadBindings: {      enabled: true,      idleHours: 24,      maxAgeHours: 0,    },  },  channels: {    discord: {      threadBindings: {        enabled: true,        spawnSessions: true,      },    },  },}
[/code]

Якщо породження ACP з прив’язкою до потоку не працює, спочатку перевірте прапорець можливості адаптера:

  * Discord: `channels.discord.threadBindings.spawnSessions=true`


Прив’язки поточної розмови не потребують створення дочірнього потоку. Вони потребують активного контексту розмови й адаптера каналу, який надає прив’язки розмов ACP.

Див. [Довідник конфігурації](</uk/gateway/configuration-reference>).

## Налаштування Plugin для backend acpx

Пакетні інсталяції використовують офіційний runtime Plugin `@openclaw/acpx` для ACP. Установіть і ввімкніть його перед використанням сесій ACP harness:

bashCopy code
[code]
    openclaw plugins install @openclaw/acpxopenclaw config set plugins.entries.acpx.enabled true
[/code]

Вихідні checkout також можуть використовувати локальний workspace Plugin після `pnpm install`.

Почніть з:

textCopy code
[code]
    /acp doctor
[/code]

Якщо ви вимкнули `acpx`, заборонили його через `plugins.allow` / `plugins.deny` або хочете повернутися до пакетного Plugin, використовуйте явний шлях пакета:

bashCopy code
[code]
    openclaw plugins install @openclaw/acpxopenclaw config set plugins.entries.acpx.enabled true
[/code]

Локальна workspace-інсталяція під час розробки:

bashCopy code
[code]
    openclaw plugins install ./path/to/local/acpx-plugin
[/code]

Потім перевірте справність backend:

textCopy code
[code]
    /acp doctor
[/code]

### Конфігурація команди та версії acpx

За замовчуванням Plugin `acpx` перевіряє вбудований backend ACP під час запуску Gateway і чекає на цю перевірку перед сигналом готовності gateway `ready`. Установіть `OPENCLAW_ACPX_RUNTIME_STARTUP_PROBE=0`, щоб пропустити перевірку під час запуску й натомість зареєструвати backend ліниво. Запустіть `/acp doctor` для явної перевірки на вимогу.

Перевизначте команду або версію в конфігурації Plugin:

jsonCopy code
[code]
    {  "plugins": {    "entries": {      "acpx": {        "enabled": true,        "config": {          "command": "../acpx/dist/cli.js",          "expectedVersion": "any"        }      }    }  }}
[/code]

  * `command` приймає абсолютний шлях, відносний шлях (розв’язується від workspace OpenClaw) або назву команди.
  * `expectedVersion: "any"` вимикає суворе зіставлення версії.
  * Власні шляхи `command` вимикають локальне для Plugin автоматичне встановлення.


Перевизначте команду окремого агента ACP зі структурованими аргументами, коли шлях або значення прапорця має залишатися одним argv-токеном:

jsonCopy code
[code]
    {  "plugins": {    "entries": {      "acpx": {        "enabled": true,        "config": {          "agents": {            "claude": {              "command": "node",              "args": ["/path/to/custom adapter.mjs", "--verbose"]            }          }        }      }    }  }}
[/code]

  * `agents.<id>.command` — це виконуваний файл або наявний рядок команди для цього агента ACP.
  * `agents.<id>.args` необов’язковий. Кожен елемент масиву shell-quoted перед тим, як OpenClaw передає його через поточний реєстр рядків команд acpx.


Див. [Plugins](</uk/tools/plugin>).

### Автоматичне встановлення залежностей

Коли ви встановлюєте OpenClaw глобально через `npm install -g openclaw`, runtime-залежності acpx (платформозалежні binaries) встановлюються автоматично через postinstall hook. Якщо автоматичне встановлення не вдається, gateway усе одно запускається нормально й повідомляє про відсутню залежність через `openclaw acp doctor`.

### MCP-міст для інструментів Plugin

За замовчуванням сесії ACPX **не** надають зареєстровані Plugin інструменти OpenClaw для ACP harness.

Якщо ви хочете, щоб агенти ACP, такі як Codex або Claude Code, викликали встановлені інструменти Plugin OpenClaw, як-от memory recall/store, увімкніть спеціальний міст:

bashCopy code
[code]
    openclaw config set plugins.entries.acpx.config.pluginToolsMcpBridge true
[/code]

Що це робить:

  * Вставляє вбудований MCP server з назвою `openclaw-plugin-tools` у bootstrap сесії ACPX.
  * Надає інструменти Plugin, уже зареєстровані встановленими й увімкненими Plugin OpenClaw.
  * Залишає цю функцію явною та вимкненою за замовчуванням.


Примітки щодо безпеки й довіри:

  * Це розширює поверхню інструментів ACP harness.
  * Агенти ACP отримують доступ лише до інструментів Plugin, які вже активні в gateway.
  * Розглядайте це як таку саму межу довіри, як дозвіл цим Plugin виконуватися в самому OpenClaw.
  * Перегляньте встановлені Plugin перед увімкненням.


Власні `mcpServers` продовжують працювати, як і раніше. Вбудований міст plugin-tools є додатковою зручною опцією, а не заміною загальної конфігурації MCP server.

### MCP-міст для інструментів OpenClaw

За замовчуванням сесії ACPX також **не** надають вбудовані інструменти OpenClaw через MCP. Увімкніть окремий міст core-tools, коли агенту ACP потрібні вибрані вбудовані інструменти, такі як `cron`:

bashCopy code
[code]
    openclaw config set plugins.entries.acpx.config.openClawToolsMcpBridge true
[/code]

Що це робить:

  * Вставляє вбудований MCP server з назвою `openclaw-tools` у bootstrap сесії ACPX.
  * Надає вибрані вбудовані інструменти OpenClaw. Початковий server надає `cron`.
  * Залишає надання core-tool явним і вимкненим за замовчуванням.


### Конфігурація runtime timeout

Plugin `acpx` за замовчуванням встановлює timeout 120 секунд для вбудованих runtime turns. Це дає повільнішим harness, таким як Gemini CLI, достатньо часу для завершення запуску та ініціалізації ACP. Перевизначте це, якщо вашому host потрібен інший runtime limit:

bashCopy code
[code]
    openclaw config set plugins.entries.acpx.config.timeoutSeconds 180
[/code]

Перезапустіть gateway після зміни цього значення.

### Конфігурація агента health probe

Коли `/acp doctor` або перевірка під час запуску перевіряє backend, bundled Plugin `acpx` перевіряє одного harness agent. Якщо встановлено `acp.allowedAgents`, за замовчуванням використовується перший дозволений агент; інакше — `codex`. Якщо вашому deployment потрібен інший агент ACP для health checks, задайте агента перевірки явно:

bashCopy code
[code]
    openclaw config set plugins.entries.acpx.config.probeAgent claude
[/code]

Перезапустіть gateway після зміни цього значення.

## Конфігурація дозволів

Сесії ACP виконуються неінтерактивно — немає TTY для схвалення або відхилення запитів дозволу на file-write і shell-exec. Plugin acpx надає два ключі конфігурації, які керують обробкою дозволів:

Ці дозволи ACPX harness окремі від exec approvals OpenClaw і окремі від vendor bypass flags CLI-backend, таких як Claude CLI `--permission-mode bypassPermissions`. ACPX `approve-all` — це break-glass-перемикач рівня harness для сесій ACP.

### `permissionMode`

Керує тим, які операції harness agent може виконувати без запиту.

Значення | Поведінка  
---|---  
`approve-all` | Автоматично схвалювати всі записи файлів і shell-команди.  
`approve-reads` | Автоматично схвалювати лише читання; записи й exec потребують запитів.  
`deny-all` | Відхиляти всі запити дозволів.  
  
### `nonInteractivePermissions`

Керує тим, що відбувається, коли мав би відобразитися запит дозволу, але інтерактивний TTY недоступний (що завжди так для сесій ACP).

Значення | Поведінка  
---|---  
`fail` | Перервати сесію з `AcpRuntimeError`. **(за замовчуванням)**  
`deny` | Тихо відхилити дозвіл і продовжити (плавна деградація).  
  
### Конфігурація

Задайте через конфігурацію Plugin:

bashCopy code
[code]
    openclaw config set plugins.entries.acpx.config.permissionMode approve-allopenclaw config set plugins.entries.acpx.config.nonInteractivePermissions fail
[/code]

Перезапустіть gateway після зміни цих значень.

## Пов’язане

  * [ACP-агенти](</uk/tools/acp-agents>) — огляд, операторський runbook, концепції
  * [Sub-agents](</uk/tools/subagents>)
  * [Multi-agent routing](</uk/concepts/multi-agent>)


Was this useful?YesNo