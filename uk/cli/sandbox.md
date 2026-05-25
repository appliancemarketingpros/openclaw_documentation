---
title: CLI пісочниці
source_url: https://docs.openclaw.ai/uk/cli/sandbox
scraped_at: 2026-05-25
---

Керуйте середовищами виконання sandbox для ізольованого виконання агентів.

## Огляд

OpenClaw може запускати агентів в ізольованих середовищах виконання sandbox для безпеки. Команди `sandbox` допомагають перевіряти та перестворювати ці середовища після оновлень або змін конфігурації.

Сьогодні це зазвичай означає:

  * Контейнери Docker sandbox
  * Середовища виконання SSH sandbox, коли `agents.defaults.sandbox.backend = "ssh"`
  * Середовища виконання OpenShell sandbox, коли `agents.defaults.sandbox.backend = "openshell"`


Для `ssh` і OpenShell `remote` перестворення важливіше, ніж для Docker:

  * віддалений робочий простір є канонічним після початкового наповнення
  * `openclaw sandbox recreate` видаляє цей канонічний віддалений робочий простір для вибраної області
  * наступне використання знову наповнює його з поточного локального робочого простору


## Команди

### `openclaw sandbox explain`

Перевірте **ефективні** режим/область/доступ до робочого простору sandbox, політику інструментів sandbox і gates для підвищених прав (із шляхами ключів конфігурації для виправлення).

bashCopy code
[code]
    openclaw sandbox explainopenclaw sandbox explain --session agent:main:mainopenclaw sandbox explain --agent workopenclaw sandbox explain --json
[/code]

### `openclaw sandbox list`

Перелічує всі середовища виконання sandbox з їхнім станом і конфігурацією.

bashCopy code
[code]
    openclaw sandbox listopenclaw sandbox list --browser  # List only browser containersopenclaw sandbox list --json     # JSON output
[/code]

**Вивід містить:**

  * Назву середовища виконання та стан
  * Backend (`docker`, `openshell` тощо)
  * Мітку конфігурації та чи відповідає вона поточній конфігурації
  * Вік (час від створення)
  * Час простою (час від останнього використання)
  * Пов’язану сесію/агента


### `openclaw sandbox recreate`

Видаліть середовища виконання sandbox, щоб примусово перестворити їх з оновленою конфігурацією.

bashCopy code
[code]
    openclaw sandbox recreate --all                # Recreate all containersopenclaw sandbox recreate --session main       # Specific sessionopenclaw sandbox recreate --agent mybot        # Specific agentopenclaw sandbox recreate --browser            # Only browser containersopenclaw sandbox recreate --all --force        # Skip confirmation
[/code]

**Параметри:**

  * `--all`: перестворити всі контейнери sandbox
  * `--session <key>`: перестворити контейнер для певної сесії
  * `--agent <id>`: перестворити контейнери для певного агента
  * `--browser`: перестворити лише браузерні контейнери
  * `--force`: пропустити запит підтвердження


## Варіанти використання

### Після оновлення образу Docker

bashCopy code
[code]
    # Pull new imagedocker pull openclaw-sandbox:latestdocker tag openclaw-sandbox:latest openclaw-sandbox:bookworm-slim # Update config to use new image# Edit config: agents.defaults.sandbox.docker.image (or agents.list[].sandbox.docker.image) # Recreate containersopenclaw sandbox recreate --all
[/code]

### Після зміни конфігурації sandbox

bashCopy code
[code]
    # Edit config: agents.defaults.sandbox.* (or agents.list[].sandbox.*) # Recreate to apply new configopenclaw sandbox recreate --all
[/code]

### Після зміни цілі SSH або матеріалів автентифікації SSH

bashCopy code
[code]
    # Edit config:# - agents.defaults.sandbox.backend# - agents.defaults.sandbox.ssh.target# - agents.defaults.sandbox.ssh.workspaceRoot# - agents.defaults.sandbox.ssh.identityFile / certificateFile / knownHostsFile# - agents.defaults.sandbox.ssh.identityData / certificateData / knownHostsData openclaw sandbox recreate --all
[/code]

Для основного backend `ssh` перестворення видаляє корінь віддаленого робочого простору для кожної області на цілі SSH. Наступний запуск знову наповнює його з локального робочого простору.

### Після зміни джерела, політики або режиму OpenShell

bashCopy code
[code]
    # Edit config:# - agents.defaults.sandbox.backend# - plugins.entries.openshell.config.from# - plugins.entries.openshell.config.mode# - plugins.entries.openshell.config.policy openclaw sandbox recreate --all
[/code]

Для режиму OpenShell `remote` перестворення видаляє канонічний віддалений робочий простір для цієї області. Наступний запуск знову наповнює його з локального робочого простору.

### Після зміни setupCommand

bashCopy code
[code]
    openclaw sandbox recreate --all# or just one agent:openclaw sandbox recreate --agent family
[/code]

### Лише для певного агента

bashCopy code
[code]
    # Update only one agent's containersopenclaw sandbox recreate --agent alfred
[/code]

## Навіщо це потрібно

Коли ви оновлюєте конфігурацію sandbox:

  * Наявні середовища виконання продовжують працювати зі старими налаштуваннями.
  * Середовища виконання очищаються лише після 24 годин неактивності.
  * Агенти, які використовуються регулярно, утримують старі середовища виконання живими безстроково.


Використовуйте `openclaw sandbox recreate`, щоб примусово видалити старі середовища виконання. Вони автоматично перестворюються з поточними налаштуваннями, коли знову знадобляться.

## Міграція реєстру

OpenClaw зберігає метадані середовища виконання sandbox як один JSON-фрагмент на кожен запис контейнера/браузера в каталозі стану sandbox. Старі встановлення все ще можуть мати монолітні застарілі файли:

  * `~/.openclaw/sandbox/containers.json`
  * `~/.openclaw/sandbox/browsers.json`


Звичайні читання середовища виконання sandbox не перезаписують ці файли. Запустіть `openclaw doctor --fix`, щоб перенести чинні застарілі записи до каталогів фрагментованого реєстру. Нечинні застарілі файли ізолюються, щоб один поганий старий реєстр не міг приховати поточні записи середовища виконання.

## Конфігурація

Налаштування sandbox містяться в `~/.openclaw/openclaw.json` під `agents.defaults.sandbox` (перевизначення для окремих агентів розміщуються в `agents.list[].sandbox`):

jsoncCopy code
[code]
    {  "agents": {    "defaults": {      "sandbox": {        "mode": "all", // off, non-main, all        "backend": "docker", // docker, ssh, openshell        "scope": "agent", // session, agent, shared        "docker": {          "image": "openclaw-sandbox:bookworm-slim",          "containerPrefix": "openclaw-sbx-",          // ... more Docker options        },        "prune": {          "idleHours": 24, // Auto-prune after 24h idle          "maxAgeDays": 7, // Auto-prune after 7 days        },      },    },  },}
[/code]

## Пов’язане

  * [Довідник CLI](</uk/cli>)
  * [Sandboxing](</uk/gateway/sandboxing>)
  * [Робочий простір агента](</uk/concepts/agent-workspace>)
  * [Doctor](</uk/gateway/doctor>): перевіряє налаштування sandbox.


Was this useful?YesNo