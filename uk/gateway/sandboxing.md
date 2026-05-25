---
title: Ізоляція в пісочниці
source_url: https://docs.openclaw.ai/uk/gateway/sandboxing
scraped_at: 2026-05-25
---

OpenClaw може запускати **інструменти всередині sandbox-бекендів** , щоб зменшити радіус ураження. Це **необов’язково** й керується конфігурацією (`agents.defaults.sandbox` або `agents.list[].sandbox`). Якщо sandboxing вимкнено, інструменти виконуються на хості. Gateway залишається на хості; виконання інструментів відбувається в ізольованому sandbox, коли це ввімкнено.

## Що потрапляє в sandbox

  * Виконання інструментів (`exec`, `read`, `write`, `edit`, `apply_patch`, `process` тощо).
  * Необов’язковий sandbox-браузер (`agents.defaults.sandbox.browser`).


Подробиці sandbox-браузера

  * За замовчуванням sandbox-браузер запускається автоматично (забезпечує доступність CDP), коли браузерний інструмент цього потребує. Налаштовується через `agents.defaults.sandbox.browser.autoStart` і `agents.defaults.sandbox.browser.autoStartTimeoutMs`.
  * За замовчуванням контейнери sandbox-браузера використовують окрему Docker-мережу (`openclaw-sandbox-browser`) замість глобальної мережі `bridge`. Налаштовується через `agents.defaults.sandbox.browser.network`.
  * Необов’язковий параметр `agents.defaults.sandbox.browser.cdpSourceRange` обмежує вхідний CDP-доступ на межі контейнера за допомогою CIDR allowlist (наприклад, `172.21.0.1/32`).
  * Доступ спостерігача noVNC за замовчуванням захищено паролем; OpenClaw видає короткочасну URL-адресу з токеном, яка обслуговує локальну bootstrap-сторінку й відкриває noVNC із паролем у фрагменті URL (не в журналах query/header).
  * `agents.defaults.sandbox.browser.allowHostControl` дає sandbox-сеансам змогу явно цілитися в браузер хоста.
  * Необов’язкові allowlists обмежують `target: "custom"`: `allowedControlUrls`, `allowedControlHosts`, `allowedControlPorts`.


Не потрапляє в sandbox:

  * Сам процес Gateway.
  * Будь-який інструмент, якому явно дозволено виконуватися поза sandbox (наприклад, `tools.elevated`). 
    * **Elevated exec обходить sandboxing і використовує налаштований escape-шлях (`gateway` за замовчуванням або `node`, коли ціль exec — `node`).**
    * Якщо sandboxing вимкнено, `tools.elevated` не змінює виконання (воно вже на хості). Див. [Elevated Mode](</uk/tools/elevated>).


## Режими

`agents.defaults.sandbox.mode` керує тим, **коли** використовується sandboxing:

### off

Без sandboxing.

### non-main

Sandbox лише для **не-main** сеансів (типово, якщо ви хочете, щоб звичайні чати були на хості).

`"non-main"` базується на `session.mainKey` (за замовчуванням `"main"`), а не на id агента. Сеанси груп/каналів використовують власні ключі, тому вони вважаються не-main і потраплятимуть у sandbox.

### all

Кожен сеанс виконується в sandbox.

## Область

`agents.defaults.sandbox.scope` керує тим, **скільки контейнерів** створюється:

  * `"agent"` (за замовчуванням): один контейнер на агента.
  * `"session"`: один контейнер на сеанс.
  * `"shared"`: один контейнер, спільний для всіх sandbox-сеансів.


## Бекенд

`agents.defaults.sandbox.backend` керує тим, **яке середовище виконання** надає sandbox:

  * `"docker"` (за замовчуванням, коли sandboxing увімкнено): локальне sandbox-середовище виконання на базі Docker.
  * `"ssh"`: універсальне віддалене sandbox-середовище виконання на базі SSH.
  * `"openshell"`: sandbox-середовище виконання на базі OpenShell.


SSH-специфічна конфігурація розташована в `agents.defaults.sandbox.ssh`. OpenShell-специфічна конфігурація розташована в `plugins.entries.openshell.config`.

### Вибір бекенда

| Docker | SSH | OpenShell  
---|---|---|---  
**Де виконується** | Локальний контейнер | Будь-який хост із доступом SSH | Sandbox, керований OpenShell  
**Налаштування** | `scripts/sandbox-setup.sh` | SSH-ключ + цільовий хост | Увімкнений OpenShell plugin  
**Модель робочої області** | Bind-mount або копіювання | Віддалена канонічна (одноразове початкове заповнення) | `mirror` або `remote`  
**Керування мережею** | `docker.network` (за замовчуванням: none) | Залежить від віддаленого хоста | Залежить від OpenShell  
**Sandbox браузера** | Підтримується | Не підтримується | Ще не підтримується  
**Bind mounts** | `docker.binds` | N/A | N/A  
**Найкраще для** | Локальної розробки, повної ізоляції | Перенесення навантаження на віддалену машину | Керованих віддалених sandbox із необов’язковою двосторонньою синхронізацією  
  
### Бекенд Docker

Sandboxing вимкнено за замовчуванням. Якщо ви вмикаєте sandboxing і не вибираєте бекенд, OpenClaw використовує бекенд Docker. Він виконує інструменти й sandbox-браузери локально через сокет демона Docker (`/var/run/docker.sock`). Ізоляція sandbox-контейнера визначається просторами імен Docker.

Щоб надати GPU хоста Docker-sandbox, задайте `agents.defaults.sandbox.docker.gpus` або перевизначення для окремого агента `agents.list[].sandbox.docker.gpus`. Значення передається до прапорця Docker `--gpus` як окремий аргумент, наприклад `"all"` або `"device=GPU-uuid"`, і потребує сумісного середовища виконання хоста, такого як NVIDIA Container Toolkit.

### Бекенд SSH

Використовуйте `backend: "ssh"`, коли хочете, щоб OpenClaw запускав `exec`, файлові інструменти й читання медіа в sandbox на довільній машині з доступом SSH.

json5Copy code
[code]
    {  agents: {    defaults: {      sandbox: {        mode: "all",        backend: "ssh",        scope: "session",        workspaceAccess: "rw",        ssh: {          target: "user@gateway-host:22",          workspaceRoot: "/tmp/openclaw-sandboxes",          strictHostKeyChecking: true,          updateHostKeys: true,          identityFile: "~/.ssh/id_ed25519",          certificateFile: "~/.ssh/id_ed25519-cert.pub",          knownHostsFile: "~/.ssh/known_hosts",          // Or use SecretRefs / inline contents instead of local files:          // identityData: { source: "env", provider: "default", id: "SSH_IDENTITY" },          // certificateData: { source: "env", provider: "default", id: "SSH_CERTIFICATE" },          // knownHostsData: { source: "env", provider: "default", id: "SSH_KNOWN_HOSTS" },        },      },    },  },}
[/code]

Як це працює

  * OpenClaw створює віддалений корінь для кожної області в `sandbox.ssh.workspaceRoot`.
  * Під час першого використання після створення або повторного створення OpenClaw один раз заповнює цю віддалену робочу область із локальної робочої області.
  * Після цього `exec`, `read`, `write`, `edit`, `apply_patch`, читання медіа з промптів і staging вхідних медіа виконуються безпосередньо щодо віддаленої робочої області через SSH.
  * OpenClaw не синхронізує віддалені зміни назад у локальну робочу область автоматично.

Матеріали автентифікації

  * `identityFile`, `certificateFile`, `knownHostsFile`: використовуйте наявні локальні файли й передавайте їх через конфігурацію OpenSSH.
  * `identityData`, `certificateData`, `knownHostsData`: використовуйте inline-рядки або SecretRefs. OpenClaw розв’язує їх через звичайний snapshot середовища виконання секретів, записує їх у тимчасові файли з `0600` і видаляє їх після завершення SSH-сеансу.
  * Якщо для того самого елемента задано і `*File`, і `*Data`, у цьому SSH-сеансі перемагає `*Data`.

Наслідки віддаленої канонічності

Це **віддалена канонічна** модель. Віддалена SSH-робоча область стає реальним станом sandbox після початкового заповнення.

  * Локальні на хості зміни, зроблені поза OpenClaw після етапу заповнення, не видимі віддалено, доки ви не створите sandbox повторно.
  * `openclaw sandbox recreate` видаляє віддалений корінь для цієї області й під час наступного використання знову заповнює його з локального.
  * Sandboxing браузера не підтримується в бекенді SSH.
  * Налаштування `sandbox.docker.*` не застосовуються до бекенда SSH.


### Бекенд OpenShell

Використовуйте `backend: "openshell"`, коли хочете, щоб OpenClaw запускав інструменти в sandbox у віддаленому середовищі, керованому OpenShell. Повний посібник із налаштування, довідку з конфігурації та порівняння режимів робочої області див. на окремій [сторінці OpenShell](</uk/gateway/openshell>).

OpenShell повторно використовує той самий основний SSH-транспорт і віддалений міст файлової системи, що й універсальний бекенд SSH, і додає специфічний для OpenShell життєвий цикл (`sandbox create/get/delete`, `sandbox ssh-config`) плюс необов’язковий режим робочої області `mirror`.

json5Copy code
[code]
    {  agents: {    defaults: {      sandbox: {        mode: "all",        backend: "openshell",        scope: "session",        workspaceAccess: "rw",      },    },  },  plugins: {    entries: {      openshell: {        enabled: true,        config: {          from: "openclaw",          mode: "remote", // mirror | remote          remoteWorkspaceDir: "/sandbox",          remoteAgentWorkspaceDir: "/agent",        },      },    },  },}
[/code]

Режими OpenShell:

  * `mirror` (за замовчуванням): локальна робоча область залишається канонічною. OpenClaw синхронізує локальні файли в OpenShell перед exec і синхронізує віддалену робочу область назад після exec.
  * `remote`: робоча область OpenShell є канонічною після створення sandbox. OpenClaw один раз заповнює віддалену робочу область із локальної робочої області, після чого файлові інструменти й exec виконуються безпосередньо щодо віддаленого sandbox без синхронізації змін назад.


Подробиці віддаленого транспорту

  * OpenClaw просить OpenShell надати SSH-конфігурацію для конкретного sandbox через `openshell sandbox ssh-config <name>`.
  * Core записує цю SSH-конфігурацію в тимчасовий файл, відкриває SSH-сеанс і повторно використовує той самий віддалений міст файлової системи, що й `backend: "ssh"`.
  * У режимі `mirror` відрізняється лише життєвий цикл: синхронізація з локального в віддалене перед exec, потім синхронізація назад після exec.

Поточні обмеження OpenShell

  * sandbox-браузер ще не підтримується
  * `sandbox.docker.binds` не підтримується в бекенді OpenShell
  * Специфічні для Docker runtime-параметри в `sandbox.docker.*` і далі застосовуються лише до бекенда Docker


#### Режими робочої області

OpenShell має дві моделі робочої області. Це частина, яка на практиці має найбільше значення.

### mirror (локальна канонічна)

Використовуйте `plugins.entries.openshell.config.mode: "mirror"`, коли хочете, щоб **локальна робоча область залишалася канонічною**.

Поведінка:

  * Перед `exec` OpenClaw синхронізує локальну робочу область із пісочницею OpenShell.
  * Після `exec` OpenClaw синхронізує віддалену робочу область назад у локальну робочу область.
  * Файлові інструменти й надалі працюють через міст пісочниці, але локальна робоча область залишається джерелом істини між ходами.


Використовуйте це, коли:

  * ви редагуєте файли локально поза OpenClaw і хочете, щоб ці зміни автоматично з’являлися в пісочниці
  * ви хочете, щоб пісочниця OpenShell поводилася максимально подібно до бекенду Docker
  * ви хочете, щоб робоча область хоста відображала записи пісочниці після кожного ходу exec


Компроміс: додаткова вартість синхронізації до й після exec.

### remote (OpenShell canonical)

Використовуйте `plugins.entries.openshell.config.mode: "remote"`, коли хочете, щоб **робоча область OpenShell стала канонічною**.

Поведінка:

  * Коли пісочницю створюють уперше, OpenClaw один раз заповнює віддалену робочу область із локальної робочої області.
  * Після цього `exec`, `read`, `write`, `edit` і `apply_patch` працюють безпосередньо з віддаленою робочою областю OpenShell.
  * OpenClaw **не** синхронізує віддалені зміни назад у локальну робочу область після exec.
  * Читання медіа під час підготовки запиту й надалі працює, бо файлові та медіаінструменти читають через міст пісочниці, а не припускають наявність локального шляху хоста.
  * Транспортом є SSH у пісочницю OpenShell, повернуту `openshell sandbox ssh-config`.


Важливі наслідки:

  * Якщо після кроку початкового заповнення ви редагуєте файли на хості поза OpenClaw, віддалена пісочниця **не** побачить ці зміни автоматично.
  * Якщо пісочницю створити повторно, віддалена робоча область знову заповнюється з локальної робочої області.
  * Із `scope: "agent"` або `scope: "shared"` ця віддалена робоча область спільно використовується в тій самій області дії.


Використовуйте це, коли:

  * пісочниця має переважно існувати на віддаленому боці OpenShell
  * ви хочете зменшити накладні витрати синхронізації на кожен хід
  * ви не хочете, щоб локальні редагування на хості непомітно перезаписували стан віддаленої пісочниці


Виберіть `mirror`, якщо вважаєте пісочницю тимчасовим середовищем виконання. Виберіть `remote`, якщо вважаєте пісочницю справжньою робочою областю.

#### Життєвий цикл OpenShell

Пісочниці OpenShell і надалі керуються через звичайний життєвий цикл пісочниці:

  * `openclaw sandbox list` показує середовища виконання OpenShell, а також середовища виконання Docker
  * `openclaw sandbox recreate` видаляє поточне середовище виконання й дає OpenClaw створити його повторно під час наступного використання
  * логіка очищення також враховує бекенд


Для режиму `remote` повторне створення особливо важливе:

  * повторне створення видаляє канонічну віддалену робочу область для цієї області дії
  * наступне використання заповнює нову віддалену робочу область із локальної робочої області


Для режиму `mirror` повторне створення переважно скидає віддалене середовище виконання, бо локальна робоча область усе одно залишається канонічною.

## Доступ до робочої області

`agents.defaults.sandbox.workspaceAccess` керує тим, **що може бачити пісочниця** :

### none (default)

Інструменти бачать робочу область пісочниці в `~/.openclaw/sandboxes`.

### ro

Монтує робочу область агента лише для читання в `/agent` (вимикає `write`/`edit`/`apply_patch`).

### rw

Монтує робочу область агента для читання/запису в `/workspace`.

З бекендом OpenShell:

  * режим `mirror` і надалі використовує локальну робочу область як канонічне джерело між ходами exec
  * режим `remote` використовує віддалену робочу область OpenShell як канонічне джерело після початкового заповнення
  * `workspaceAccess: "ro"` і `"none"` і надалі однаково обмежують поведінку запису


Вхідні медіа копіюються в активну робочу область пісочниці (`media/inbound/*`).

## Власні bind-монтування

`agents.defaults.sandbox.docker.binds` монтує додаткові каталоги хоста в контейнер. Формат: `host:container:mode` (наприклад, `"/home/user/source:/source:rw"`).

Глобальні та поагентні bind-монтування **об’єднуються** (а не замінюються). За `scope: "shared"` поагентні bind-монтування ігноруються.

`agents.defaults.sandbox.browser.binds` монтує додаткові каталоги хоста лише в контейнер **браузера пісочниці**.

  * Коли задано (зокрема `[]`), це замінює `agents.defaults.sandbox.docker.binds` для контейнера браузера.
  * Коли пропущено, контейнер браузера повертається до `agents.defaults.sandbox.docker.binds` (зворотна сумісність).


Приклад (джерело лише для читання + додатковий каталог даних):

json5Copy code
[code]
    {  agents: {    defaults: {      sandbox: {        docker: {          binds: ["/home/user/source:/source:ro", "/var/data/myapp:/data:ro"],        },      },    },    list: [      {        id: "build",        sandbox: {          docker: {            binds: ["/mnt/cache:/cache:rw"],          },        },      },    ],  },}
[/code]

## Образи та налаштування

Стандартний образ Docker: `openclaw-sandbox:bookworm-slim`

* ### Build the default image

З вихідного checkout:

bashCopy code
[code]
    scripts/sandbox-setup.sh
[/code]

З установлення npm (вихідний checkout не потрібен):

bashCopy code
[code]
    docker build -t openclaw-sandbox:bookworm-slim - <<'DOCKERFILE'FROM debian:bookworm-slimENV DEBIAN_FRONTEND=noninteractiveRUN apt-get update && apt-get install -y --no-install-recommends \  bash ca-certificates curl git jq python3 ripgrep \  && rm -rf /var/lib/apt/lists/*RUN useradd --create-home --shell /bin/bash sandboxUSER sandboxWORKDIR /home/sandboxCMD ["sleep", "infinity"]DOCKERFILE
[/code]

Стандартний образ **не** містить Node. Якщо Skills потрібен Node (або інші середовища виконання), або вбудуйте власний образ, або встановіть через `sandbox.docker.setupCommand` (потрібні мережевий вихід + записуваний root + користувач root).

OpenClaw не підставляє мовчки звичайний `debian:bookworm-slim`, коли `openclaw-sandbox:bookworm-slim` відсутній. Запуски пісочниці, які націлені на стандартний образ, швидко завершуються з інструкцією зі збирання, доки ви його не зберете, бо вбудований образ містить `python3` для допоміжних засобів запису/редагування в пісочниці.

* ### Optional: build the common image

Для функціональнішого образу пісочниці зі звичними інструментами (наприклад, `curl`, `jq`, `nodejs`, `python3`, `git`):

З вихідного checkout:

bashCopy code
[code]
    scripts/sandbox-common-setup.sh
[/code]

З установлення npm спочатку зберіть стандартний образ (див. вище), потім зберіть common-образ поверх нього, використовуючи [`scripts/docker/sandbox/Dockerfile.common`](<https://github.com/openclaw/openclaw/blob/main/scripts/docker/sandbox/Dockerfile.common>) з репозиторію.

Потім установіть `agents.defaults.sandbox.docker.image` у `openclaw-sandbox-common:bookworm-slim`.

* ### Optional: build the sandbox browser image

З вихідного checkout:

bashCopy code
[code]
    scripts/sandbox-browser-setup.sh
[/code]

З установлення npm зберіть, використовуючи [`scripts/docker/sandbox/Dockerfile.browser`](<https://github.com/openclaw/openclaw/blob/main/scripts/docker/sandbox/Dockerfile.browser>) з репозиторію.

За замовчуванням контейнери пісочниці Docker запускаються **без мережі**. Перевизначте це за допомогою `agents.defaults.sandbox.docker.network`.

Sandbox browser Chromium defaults

Вбудований образ браузера пісочниці також застосовує консервативні стандартні параметри запуску Chromium для контейнеризованих навантажень. Поточні стандартні параметри контейнера включають:

  * `--remote-debugging-address=127.0.0.1`
  * `--remote-debugging-port=<derived from OPENCLAW_BROWSER_CDP_PORT>`
  * `--user-data-dir=${HOME}/.chrome`
  * `--no-first-run`
  * `--no-default-browser-check`
  * `--disable-3d-apis`
  * `--disable-gpu`
  * `--disable-dev-shm-usage`
  * `--disable-background-networking`
  * `--disable-extensions`
  * `--disable-features=TranslateUI`
  * `--disable-breakpad`
  * `--disable-crash-reporter`
  * `--disable-software-rasterizer`
  * `--no-zygote`
  * `--metrics-recording-only`
  * `--renderer-process-limit=2`
  * `--no-sandbox`, коли ввімкнено `noSandbox`.
  * Три прапорці посилення графіки (`--disable-3d-apis`, `--disable-software-rasterizer`, `--disable-gpu`) є необов’язковими й корисні, коли контейнери не мають підтримки GPU. Установіть `OPENCLAW_BROWSER_DISABLE_GRAPHICS_FLAGS=0`, якщо вашому навантаженню потрібні WebGL або інші 3D/браузерні можливості.
  * `--disable-extensions` увімкнено за замовчуванням, і його можна вимкнути за допомогою `OPENCLAW_BROWSER_DISABLE_EXTENSIONS=0` для потоків, що залежать від розширень.
  * `--renderer-process-limit=2` керується `OPENCLAW_BROWSER_RENDERER_PROCESS_LIMIT=&lt;N&gt;`, де `0` зберігає стандартне значення Chromium.


Якщо вам потрібен інший профіль середовища виконання, використовуйте власний образ браузера й надайте власний entrypoint. Для локальних (неконтейнерних) профілів Chromium використовуйте `browser.extraArgs`, щоб додати додаткові прапорці запуску.

Network security defaults

  * `network: "host"` заблоковано.
  * `network: "container:<id>"` заблоковано за замовчуванням (ризик обходу через приєднання до namespace).
  * Аварійне перевизначення: `agents.defaults.sandbox.docker.dangerouslyAllowContainerNamespaceJoin: true`.


Установлення Docker і контейнеризований Gateway описані тут: [Docker](</uk/install/docker>)

Для розгортань Docker Gateway `scripts/docker/setup.sh` може ініціалізувати конфігурацію пісочниці. Установіть `OPENCLAW_SANDBOX=1` (або `true`/`yes`/`on`), щоб увімкнути цей шлях. Ви можете перевизначити розташування сокета за допомогою `OPENCLAW_DOCKER_SOCKET`. Повне налаштування й довідка щодо змінних середовища: [Docker](</uk/install/docker#agent-sandbox>).

## setupCommand (одноразове налаштування контейнера)

`setupCommand` запускається **один раз** після створення контейнера пісочниці (не під час кожного запуску). Він виконується всередині контейнера через `sh -lc`.

Шляхи:

  * Глобально: `agents.defaults.sandbox.docker.setupCommand`
  * Поагентно: `agents.list[].sandbox.docker.setupCommand`


Поширені помилки

  * Типове значення `docker.network` — `"none"` (без вихідного мережевого трафіку), тому встановлення пакетів завершиться помилкою.
  * `docker.network: "container:<id>"` потребує `dangerouslyAllowContainerNamespaceJoin: true` і призначений лише для аварійних випадків.
  * `readOnlyRoot: true` забороняє запис; установіть `readOnlyRoot: false` або зберіть власний образ.
  * Для встановлення пакетів `user` має бути root (пропустіть `user` або встановіть `user: "0:0"`).
  * Виконання в пісочниці **не** успадковує `process.env` хоста. Використовуйте `agents.defaults.sandbox.docker.env` (або власний образ) для ключів API Skills.


## Політика інструментів і аварійні механізми обходу

Політики дозволу/заборони інструментів усе ще застосовуються перед правилами пісочниці. Якщо інструмент заборонено глобально або для окремого агента, ізоляція в пісочниці не повертає його.

`tools.elevated` — це явний аварійний механізм обходу, який запускає `exec` поза пісочницею (`gateway` за замовчуванням або `node`, коли ціль виконання — `node`). Директиви `/exec` застосовуються лише для авторизованих відправників і зберігаються для кожного сеансу; щоб жорстко вимкнути `exec`, скористайтеся забороною в політиці інструментів (див. [Пісочниця, політика інструментів і Elevated](</uk/gateway/sandbox-vs-tool-policy-vs-elevated>)).

Налагодження:

  * Використовуйте `openclaw sandbox explain`, щоб перевірити ефективний режим пісочниці, політику інструментів і ключі конфігурації для виправлення.
  * Див. [Пісочниця, політика інструментів і Elevated](</uk/gateway/sandbox-vs-tool-policy-vs-elevated>), щоб зрозуміти ментальну модель «чому це заблоковано?».


Тримайте все заблокованим.

## Багатоагентні перевизначення

Кожен агент може перевизначати пісочницю й інструменти: `agents.list[].sandbox` і `agents.list[].tools` (а також `agents.list[].tools.sandbox.tools` для політики інструментів пісочниці). Див. [Багатоагентна пісочниця та інструменти](</uk/tools/multi-agent-sandbox-tools>), щоб дізнатися про пріоритетність.

## Мінімальний приклад увімкнення

json5Copy code
[code]
    {  agents: {    defaults: {      sandbox: {        mode: "non-main",        scope: "session",        workspaceAccess: "none",      },    },  },}
[/code]

## Пов’язане

  * [Багатоагентна пісочниця та інструменти](</uk/tools/multi-agent-sandbox-tools>) — перевизначення для окремих агентів і пріоритетність
  * [OpenShell](</uk/gateway/openshell>) — налаштування керованого бекенда пісочниці, режими робочого простору та довідник конфігурації
  * [Конфігурація пісочниці](</uk/gateway/config-agents#agentsdefaultssandbox>)
  * [Пісочниця, політика інструментів і Elevated](</uk/gateway/sandbox-vs-tool-policy-vs-elevated>) — налагодження «чому це заблоковано?»
  * [Безпека](</uk/gateway/security>)


Was this useful?YesNo