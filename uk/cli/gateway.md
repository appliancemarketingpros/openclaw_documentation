---
title: Gateway
source_url: https://docs.openclaw.ai/uk/cli/gateway
scraped_at: 2026-05-25
---

Gateway — це WebSocket-сервер OpenClaw (канали, вузли, сесії, hooks). Підкоманди на цій сторінці розміщені під `openclaw gateway …`.

[**Bonjour discovery** Налаштування локального mDNS + широкозонного DNS-SD. ](</uk/gateway/bonjour>) [**Discovery overview** Як OpenClaw оголошує та знаходить gateways. ](</uk/gateway/discovery>) [**Configuration** Ключі конфігурації gateway верхнього рівня. ](</uk/gateway/configuration>)

## Запуск Gateway

Запустіть локальний процес Gateway:

bashCopy code
[code]
    openclaw gateway
[/code]

Псевдонім для запуску на передньому плані:

bashCopy code
[code]
    openclaw gateway run
[/code]

Startup behavior

  * За замовчуванням Gateway відмовляється запускатися, якщо в `~/.openclaw/openclaw.json` не задано `gateway.mode=local`. Використовуйте `--allow-unconfigured` для ad-hoc/dev запусків.
  * Очікується, що `openclaw onboard --mode local` і `openclaw setup` записують `gateway.mode=local`. Якщо файл існує, але `gateway.mode` відсутній, вважайте це зламаною або перезаписаною конфігурацією та відновіть її, замість неявно припускати локальний режим.
  * Якщо файл існує, а `gateway.mode` відсутній, Gateway трактує це як підозріле пошкодження конфігурації та відмовляється "вгадувати local" за вас.
  * Прив’язування поза межами loopback без автентифікації заблоковано (захисне обмеження).
  * `SIGUSR1` запускає перезапуск у процесі, коли це дозволено (`commands.restart` увімкнено за замовчуванням; задайте `commands.restart: false`, щоб заблокувати ручний перезапуск, при цьому застосування/оновлення gateway tool/config залишаються дозволеними).
  * Обробники `SIGINT`/`SIGTERM` зупиняють процес gateway, але не відновлюють жоден користувацький стан термінала. Якщо ви обгортаєте CLI за допомогою TUI або введення в raw-mode, відновіть термінал перед виходом.


### Параметри

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ii0tcG9ydCA8cG9ydA " type="number"> Порт WebSocket (значення за замовчуванням береться з конфігурації/env; зазвичай `18789`).

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ii0tdG9rZW4gPHRva2Vu " type="string"> Перевизначення токена (також задає `OPENCLAW_GATEWAY_TOKEN` для процесу).

Скинути конфігурацію Tailscale serve/funnel під час завершення роботи.

Дозволити запуск gateway без `gateway.mode=local` у конфігурації. Обходить захист запуску лише для ad-hoc/dev початкового налаштування; не записує й не відновлює файл конфігурації.

Створити dev-конфігурацію + робочий простір, якщо їх немає (пропускає [BOOTSTRAP.md](<http://BOOTSTRAP.md>)).

Скинути dev-конфігурацію + облікові дані + сесії + робочий простір (потребує `--dev`).

Завершити будь-який наявний слухач на вибраному порту перед запуском.

Детальні журнали.

Показувати в консолі лише журнали бекенду CLI (і ввімкнути stdout/stderr).

Псевдонім для `--ws-log compact`.

Записувати raw model stream події до jsonl.

## Перезапуск Gateway

bashCopy code
[code]
    openclaw gateway restartopenclaw gateway restart --safeopenclaw gateway restart --safe --skip-deferralopenclaw gateway restart --force
[/code]

`openclaw gateway restart --safe` просить запущений Gateway виконати попередню перевірку активної роботи OpenClaw перед перезапуском. Якщо активні операції в черзі, доставка відповідей, вбудовані запуски або task runs, Gateway повідомляє про блокувальники, об’єднує дублікати запитів безпечного перезапуску й перезапускається після завершення активної роботи. Звичайний `restart` зберігає наявну поведінку service-manager для сумісності. Використовуйте `--force` лише тоді, коли явно потрібен шлях негайного перевизначення.

`openclaw gateway restart --safe --skip-deferral` виконує той самий скоординований перезапуск з урахуванням OpenClaw, що й `--safe`, але обходить gate відкладення активної роботи, тому Gateway надсилає перезапуск негайно, навіть коли повідомлено про блокувальники. Використовуйте це як аварійний вихід оператора, коли відкладення зафіксоване завислим task run і сам `--safe` чекав би нескінченно. `--skip-deferral` потребує `--safe`.

### Профілювання запуску

  * Задайте `OPENCLAW_GATEWAY_STARTUP_TRACE=1`, щоб журналювати таймінги фаз під час запуску Gateway, включно із затримкою `eventLoopMax` для кожної фази та таймінгами lookup-table Plugin для installed-index, manifest registry, startup planning і owner-map.
  * Задайте `OPENCLAW_DIAGNOSTICS=timeline` з `OPENCLAW_DIAGNOSTICS_TIMELINE_PATH=<path>`, щоб записати best-effort JSONL timeline діагностики запуску для зовнішніх QA harnesses. Також можна ввімкнути прапорець через `diagnostics.flags: ["timeline"]` у конфігурації; шлях усе одно надається через env. Додайте `OPENCLAW_DIAGNOSTICS_EVENT_LOOP=1`, щоб включити вибірки event-loop.
  * Запустіть `pnpm test:startup:gateway -- --runs 5 --warmup 1`, щоб виміряти продуктивність запуску Gateway. Benchmark записує перший вивід процесу, `/healthz`, `/readyz`, таймінги startup trace, затримку event-loop і подробиці таймінгів lookup-table Plugin.


## Запит до запущеного Gateway

Усі команди запитів використовують WebSocket RPC.

### Output modes

  * За замовчуванням: зручно для читання людиною (кольорово в TTY).
  * `--json`: машиночитний JSON (без стилізації/spinner).
  * `--no-color` (або `NO_COLOR=1`): вимкнути ANSI, зберігши людський layout.


### Shared options

  * `--url <url>`: WebSocket URL Gateway.
  * `--token <token>`: токен Gateway.
  * `--password <password>`: пароль Gateway.
  * `--timeout <ms>`: тайм-аут/бюджет (залежить від команди).
  * `--expect-final`: чекати на "final" відповідь (виклики агента).


### `gateway health`

bashCopy code
[code]
    openclaw gateway health --url ws://127.0.0.1:18789
[/code]

HTTP endpoint `/healthz` — це liveness probe: він повертає відповідь, щойно сервер може відповідати через HTTP. HTTP endpoint `/readyz` суворіший і залишається червоним, доки startup plugin sidecars, канали або налаштовані hooks ще стабілізуються. Локальні або автентифіковані докладні відповіді readiness містять діагностичний блок `eventLoop` із затримкою event-loop, використанням event-loop, співвідношенням ядер CPU та прапорцем `degraded`.

### `gateway usage-cost`

Отримати зведення usage-cost із журналів сесій.

bashCopy code
[code]
    openclaw gateway usage-costopenclaw gateway usage-cost --days 7openclaw gateway usage-cost --json
[/code]

### `gateway stability`

Отримати recent diagnostic stability recorder із запущеного Gateway.

bashCopy code
[code]
    openclaw gateway stabilityopenclaw gateway stability --type payload.largeopenclaw gateway stability --bundle latestopenclaw gateway stability --bundle latest --exportopenclaw gateway stability --json
[/code]

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ii0tbGltaXQgPGxpbWl0 " type="number" default="25"> Максимальна кількість нещодавніх подій для включення (макс. `1000`).

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ii0tdHlwZSA8dHlwZQ " type="string"> Фільтрувати за типом діагностичної події, наприклад `payload.large` або `diagnostic.memory.pressure`.

Читати збережений stability bundle замість виклику запущеного Gateway. Використовуйте `--bundle latest` (або просто `--bundle`) для найновішого bundle у каталозі стану, або передайте шлях до bundle JSON напряму.

Записати придатний для поширення zip із support diagnostics замість друку деталей stability.

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ii0tb3V0cHV0IDxwYXRo " type="string"> Шлях виводу для `--export`.

Privacy and bundle behavior

  * Записи зберігають операційні метадані: назви подій, лічильники, розміри в байтах, показники пам’яті, стан черг/сесій, назви каналів/Plugin і відредаговані зведення сесій. Вони не зберігають текст чатів, тіла webhook, виводи tool, raw тіла запитів або відповідей, токени, cookies, секретні значення, hostnames або raw session ids. Задайте `diagnostics.enabled: false`, щоб повністю вимкнути recorder.
  * Під час fatal Gateway exits, shutdown timeouts і restart startup failures OpenClaw записує той самий diagnostic snapshot до `~/.openclaw/logs/stability/openclaw-stability-*.json`, коли recorder має події. Перегляньте найновіший bundle через `openclaw gateway stability --bundle latest`; `--limit`, `--type` і `--since-seq` також застосовуються до виводу bundle.


### `gateway diagnostics export`

Записує локальний diagnostics zip, призначений для прикріплення до bug reports. Модель приватності та вміст bundle див. у [Diagnostics Export](</uk/gateway/diagnostics>).

bashCopy code
[code]
    openclaw gateway diagnostics exportopenclaw gateway diagnostics export --output openclaw-diagnostics.zipopenclaw gateway diagnostics export --json
[/code]

Пропустити пошук збереженого stability bundle.

Надрукувати записаний шлях, розмір і manifest як JSON.

Експорт містить manifest, Markdown-зведення, форму конфігурації, очищені деталі конфігурації, очищені зведення журналів, очищені знімки status/health Gateway і найновіший stability bundle, коли він існує.

Його призначено для поширення. Він зберігає операційні деталі, які допомагають налагодженню, як-от безпечні поля журналів OpenClaw, назви підсистем, status codes, тривалості, налаштовані режими, порти, plugin ids, provider ids, несекретні налаштування функцій і відредаговані operational log messages. Він пропускає або редагує текст чатів, тіла webhook, виводи tool, облікові дані, cookies, ідентифікатори облікових записів/повідомлень, текст prompt/instruction, hostnames і секретні значення. Коли повідомлення у стилі LogTape схоже на текст user/chat/tool payload, експорт зберігає лише факт, що повідомлення було пропущено, плюс його кількість байтів.

### `gateway status`

`gateway status` показує службу Gateway (launchd/systemd/schtasks) плюс необов’язкову перевірку connectivity/auth capability.

bashCopy code
[code]
    openclaw gateway statusopenclaw gateway status --jsonopenclaw gateway status --require-rpc
[/code]

Пропустити зондування з’єднання (перегляд лише сервісу).

Також сканувати сервіси системного рівня.

Підвищити стандартне зондування з’єднання до зондування читання й завершитися з ненульовим кодом, якщо це зондування читання не вдається. Не можна поєднувати з `--no-probe`.

Status semantics

  * `gateway status` залишається доступною для діагностики, навіть коли локальна конфігурація CLI відсутня або недійсна.
  * Типова `gateway status` підтверджує стан сервісу, підключення WebSocket і можливість автентифікації, видиму під час рукостискання. Вона не підтверджує операції читання/запису/адміністрування.
  * Діагностичні зондування не змінюють стан для першої автентифікації пристрою: вони повторно використовують наявний кешований токен пристрою, якщо він існує, але не створюють нову ідентичність пристрою CLI або запис сполучення пристрою лише для читання лише для перевірки стану.
  * `gateway status` за можливості розв’язує налаштовані SecretRefs автентифікації для автентифікації зондування.
  * Якщо потрібний SecretRef автентифікації не розв’язано в цьому шляху команди, `gateway status --json` повідомляє `rpc.authWarning`, коли з’єднання/автентифікація зондування не вдається; явно передайте `--token`/`--password` або спочатку розв’яжіть джерело секрету.
  * Якщо зондування успішне, попередження про нерозв’язані посилання автентифікації пригнічуються, щоб уникнути хибних спрацювань.
  * Використовуйте `--require-rpc` у скриптах і автоматизації, коли сервісу, що прослуховує, недостатньо і також потрібна справність RPC-викликів з областю читання.
  * `--deep` додає найкраще можливе сканування додаткових інсталяцій launchd/systemd/schtasks. Коли виявлено кілька сервісів, схожих на Gateway, вивід для людини друкує підказки з очищення та попереджає, що більшості налаштувань слід запускати один Gateway на машину.
  * `--deep` також повідомляє про нещодавню передачу перезапуску супервізора Gateway, коли процес сервісу коректно завершився для перезапуску зовнішнім супервізором.
  * `--deep` виконує перевірку конфігурації в режимі з урахуванням plugin (`pluginValidation: "full"`) і показує попередження налаштованого маніфесту plugin (наприклад, відсутні метадані конфігурації каналу), щоб smoke-перевірки інсталяції та оновлення їх виявляли. Типова `gateway status` зберігає швидкий шлях лише для читання, який пропускає перевірку plugin.
  * Вивід для людини містить розв’язаний шлях до файлового журналу, а також знімок шляхів/дійсності конфігурації CLI порівняно із сервісом, щоб допомогти діагностувати дрейф профілю або каталогу стану.

Linux systemd auth-drift checks

  * В інсталяціях Linux systemd перевірки дрейфу автентифікації сервісу читають значення `Environment=` і `EnvironmentFile=` з unit (зокрема `%h`, шляхи в лапках, кілька файлів і необов’язкові файли з `-`).
  * Перевірки дрейфу розв’язують SecretRefs `gateway.auth.token` за допомогою об’єднаного runtime-середовища (спочатку середовище команди сервісу, потім резервно середовище процесу).
  * Якщо автентифікація токеном фактично не активна (явний `gateway.auth.mode` зі значенням `password`/`none`/`trusted-proxy`, або режим не задано, пароль може мати перевагу й жоден кандидат токена не може мати переваги), перевірки дрейфу токена пропускають розв’язання токена конфігурації.


### `gateway probe`

`gateway probe` — це команда «налагодити все». Вона завжди зондує:

  * ваш налаштований віддалений gateway (якщо задано), і
  * localhost (loopback) **навіть якщо віддалений gateway налаштовано**.


Якщо передати `--url`, ця явна ціль додається перед обома. Вивід для людини позначає цілі так:

  * `URL (explicit)`
  * `Remote (configured)` або `Remote (configured, inactive)`
  * `Local loopback`

bashCopy code
[code]
    openclaw gateway probeopenclaw gateway probe --json
[/code]

Interpretation

  * `Reachable: yes` означає, що принаймні одна ціль прийняла підключення WebSocket.
  * `Capability: read-only|write-capable|admin-capable|pairing-pending|connect-only` повідомляє, що зондування змогло підтвердити щодо автентифікації. Це окремо від доступності.
  * `Read probe: ok` означає, що детальні RPC-виклики з областю читання (`health`/`status`/`system-presence`/`config.get`) також успішні.
  * `Read probe: limited - missing scope: operator.read` означає, що підключення успішне, але RPC з областю читання обмежене. Це повідомляється як **погіршена** доступність, а не повний збій.
  * `Read probe: failed` після `Connect: ok` означає, що Gateway прийняв підключення WebSocket, але подальша діагностика читання перевищила тайм-аут або не вдалася. Це також **погіршена** доступність, а не недоступний Gateway.
  * Як і `gateway status`, зондування повторно використовує наявну кешовану автентифікацію пристрою, але не створює першої ідентичності пристрою або стану сполучення.
  * Код виходу ненульовий лише тоді, коли жодна зондувана ціль недоступна.

JSON output

Верхній рівень:

  * `ok`: принаймні одна ціль доступна.
  * `degraded`: принаймні одна ціль прийняла підключення, але не завершила повну детальну RPC-діагностику.
  * `capability`: найкраща можливість, побачена серед доступних цілей (`read_only`, `write_capable`, `admin_capable`, `pairing_pending`, `connected_no_operator_scope` або `unknown`).
  * `primaryTargetId`: найкраща ціль, яку слід вважати активним переможцем у такому порядку: явний URL, SSH-тунель, налаштований віддалений, потім local loopback.
  * `warnings[]`: записи попереджень у режимі найкращого зусилля з `code`, `message` і необов’язковими `targetIds`.
  * `network`: підказки URL local loopback/tailnet, виведені з поточної конфігурації та мережі хоста.
  * `discovery.timeoutMs` і `discovery.count`: фактичний бюджет виявлення/кількість результатів, використані для цього проходу зондування.


Для кожної цілі (`targets[].connect`):

  * `ok`: доступність після підключення + класифікація погіршення.
  * `rpcOk`: повний успіх детального RPC.
  * `scopeLimited`: детальний RPC не вдався через відсутню область оператора.


Для кожної цілі (`targets[].auth`):

  * `role`: роль автентифікації, повідомлена в `hello-ok`, коли доступна.
  * `scopes`: надані області, повідомлені в `hello-ok`, коли доступні.
  * `capability`: показана класифікація можливості автентифікації для цієї цілі.

Common warning codes

  * `ssh_tunnel_failed`: налаштування SSH-тунелю не вдалося; команда повернулася до прямих зондувань.
  * `multiple_gateways`: доступною була більш ніж одна ціль; це незвично, якщо ви навмисно не запускаєте ізольовані профілі, наприклад рятувального бота.
  * `auth_secretref_unresolved`: налаштований SecretRef автентифікації не вдалося розв’язати для невдалої цілі.
  * `probe_scope_limited`: підключення WebSocket успішне, але зондування читання було обмежене через відсутній `operator.read`.


#### Віддалено через SSH (паритет із Mac-застосунком)

Режим macOS-застосунку "Remote over SSH" використовує локальне перенаправлення порту, щоб віддалений gateway (який може бути прив’язаний лише до loopback) став доступним за адресою `ws://127.0.0.1:<port>`.

Еквівалент CLI:

bashCopy code
[code]
    openclaw gateway probe --ssh user@gateway-host
[/code]

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ii0tc3NoIDx0YXJnZXQ " type="string"> `user@host` або `user@host:port` (типовий порт — `22`).

Вибрати перший виявлений хост gateway як SSH-ціль із розв’язаного endpoint виявлення (`local.` плюс налаштований домен глобальної мережі, якщо є). Підказки лише TXT ігноруються.

Конфігурація (необов’язково, використовується як типові значення):

  * `gateway.remote.sshTarget`
  * `gateway.remote.sshIdentity`


### `gateway call <method>`

Низькорівневий помічник RPC.

bashCopy code
[code]
    openclaw gateway call statusopenclaw gateway call logs.tail --params '{"sinceMs": 60000}'
[/code]

Переважно для RPC у стилі агентів, які транслюють проміжні події перед фінальним payload.

Машинозчитуваний JSON-вивід.

## Керування сервісом Gateway

bashCopy code
[code]
    openclaw gateway installopenclaw gateway startopenclaw gateway stopopenclaw gateway restartopenclaw gateway uninstall
[/code]

### Інсталяція з обгорткою

Використовуйте `--wrapper`, коли керований сервіс має запускатися через інший виконуваний файл, наприклад shim менеджера секретів або помічник запуску від імені іншого користувача. Обгортка отримує звичайні аргументи Gateway і відповідає за те, щоб зрештою виконати `openclaw` або Node з цими аргументами.

bashCopy code
[code]
    cat > ~/.local/bin/openclaw-doppler <<'EOF'#!/usr/bin/env bashset -euo pipefailexec doppler run --project my-project --config production -- openclaw "$@"EOFchmod +x ~/.local/bin/openclaw-doppler openclaw gateway install --wrapper ~/.local/bin/openclaw-doppler --forceopenclaw gateway restart
[/code]

Також можна задати обгортку через середовище. `gateway install` перевіряє, що шлях є виконуваним файлом, записує обгортку в `ProgramArguments` сервісу та зберігає `OPENCLAW_WRAPPER` у середовищі сервісу для подальших примусових перевстановлень, оновлень і виправлень doctor.

bashCopy code
[code]
    OPENCLAW_WRAPPER="$HOME/.local/bin/openclaw-doppler" openclaw gateway install --forceopenclaw doctor
[/code]

Щоб видалити збережену обгортку, очистьте `OPENCLAW_WRAPPER` під час перевстановлення:

bashCopy code
[code]
    OPENCLAW_WRAPPER= openclaw gateway install --forceopenclaw gateway restart
[/code]

Command options

  * `gateway status`: `--url`, `--token`, `--password`, `--timeout`, `--no-probe`, `--require-rpc`, `--deep`, `--json`
  * `gateway install`: `--port`, `--runtime <node|bun>`, `--token`, `--wrapper <path>`, `--force`, `--json`
  * `gateway restart`: `--safe`, `--skip-deferral`, `--force`, `--wait <duration>`, `--json`
  * `gateway uninstall|start`: `--json`
  * `gateway stop`: `--disable`, `--json`

Поведінка життєвого циклу

  * Використовуйте `gateway restart`, щоб перезапустити керований сервіс. Не поєднуйте `gateway stop` і `gateway start` як заміну перезапуску.
  * У macOS `gateway stop` за замовчуванням використовує `launchctl bootout`, що видаляє LaunchAgent з поточного сеансу завантаження без постійного вимкнення — автоматичне відновлення KeepAlive залишається активним для майбутніх збоїв, а `gateway start` повторно вмикається чисто без ручного `launchctl enable`. Передайте `--disable`, щоб постійно приглушити KeepAlive і RunAtLoad, аби Gateway не запускався повторно до наступного явного `gateway start`; використовуйте це, коли ручна зупинка має пережити перезавантаження або перезапуски системи.
  * `gateway restart --safe` просить запущений Gateway попередньо перевірити активну роботу OpenClaw і відкласти перезапуск, доки доставлення відповідей, вбудовані запуски та запуски завдань не завершаться. `--safe` не можна поєднувати з `--force` або `--wait`.
  * `gateway restart --wait 30s` перевизначає налаштований бюджет очікування завершення перед перезапуском для цього перезапуску. Числа без одиниць вимірюються в мілісекундах; приймаються одиниці на кшталт `s`, `m` і `h`. `--wait 0` чекає необмежено.
  * `gateway restart --safe --skip-deferral` виконує безпечний перезапуск з урахуванням OpenClaw, але обходить шлюз відкладання, тому Gateway негайно видає перезапуск, навіть коли повідомлено про блокувальники. Це аварійний вихід для оператора у випадку завислих відкладань запусків завдань; потребує `--safe`.
  * `gateway restart --force` пропускає очікування завершення активної роботи та перезапускає негайно. Використовуйте це, коли оператор уже перевірив перелічені блокувальники завдань і хоче негайно повернути gateway до роботи.
  * Команди життєвого циклу приймають `--json` для скриптів.

Автентифікація та SecretRefs під час установлення

  * Коли автентифікація за токеном потребує токена, а `gateway.auth.token` керується через SecretRef, `gateway install` перевіряє, що SecretRef можна розв’язати, але не зберігає розв’язаний токен у метаданих середовища сервісу.
  * Якщо автентифікація за токеном потребує токена, а налаштований SecretRef токена не розв’язується, установлення завершується закритою відмовою замість збереження резервного відкритого тексту.
  * Для автентифікації паролем у `gateway run` надавайте перевагу `OPENCLAW_GATEWAY_PASSWORD`, `--password-file` або `gateway.auth.password` на основі SecretRef замість вбудованого `--password`.
  * У виведеному режимі автентифікації лише оболонковий `OPENCLAW_GATEWAY_PASSWORD` не послаблює вимоги до токена під час установлення; використовуйте тривалу конфігурацію (`gateway.auth.password` або конфігураційний `env`) під час установлення керованого сервісу.
  * Якщо налаштовано і `gateway.auth.token`, і `gateway.auth.password`, а `gateway.auth.mode` не задано, установлення блокується, доки режим не буде задано явно.


## Виявлення gateway (Bonjour)

`gateway discover` сканує маяки Gateway (`_openclaw-gw._tcp`).

  * Багатоадресний DNS-SD: `local.`
  * Одноадресний DNS-SD (Wide-Area Bonjour): виберіть домен (приклад: `openclaw.internal.`) і налаштуйте split DNS + DNS-сервер; див. [Bonjour](</uk/gateway/bonjour>).


Лише gateway з увімкненим виявленням Bonjour (за замовчуванням) оголошують маяк.

Записи широкозонного виявлення можуть містити ці підказки TXT:

  * `role` (підказка ролі gateway)
  * `transport` (підказка транспорту, напр. `gateway`)
  * `gatewayPort` (порт WebSocket, зазвичай `18789`)
  * `sshPort` (лише режим повного виявлення; клієнти за замовчуванням використовують цілі SSH `22`, коли він відсутній)
  * `tailnetDns` (ім’я хоста MagicDNS, коли доступне)
  * `gatewayTls` / `gatewayTlsSha256` (TLS увімкнено + відбиток сертифіката)
  * `cliPath` (лише режим повного виявлення)


### `gateway discover`

bashCopy code
[code]
    openclaw gateway discover
[/code]

Машиночитаний вивід (також вимикає стилізацію/індикатор виконання).

Приклади:

bashCopy code
[code]
    openclaw gateway discover --timeout 4000openclaw gateway discover --json | jq '.beacons[].wsUrl'
[/code]

## Пов’язане

  * [Довідник CLI](</uk/cli>)
  * [Регламент Gateway](</uk/gateway>)


Was this useful?YesNo