---
title: Конфігурація
source_url: https://docs.openclaw.ai/uk/cli/config
scraped_at: 2026-05-25
---

Допоміжні команди конфігурації для неінтерактивних змін у `openclaw.json`: отримуйте/задавайте/застосовуйте патчі/скасовуйте/переглядайте файл/схему/перевіряйте значення за шляхом і виводьте активний файл конфігурації. Запустіть без підкоманди, щоб відкрити майстер налаштування (те саме, що `openclaw configure`).

## Кореневі параметри

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ii0tc2VjdGlvbiA8c2VjdGlvbg " type="string"> Повторюваний фільтр розділів керованого налаштування, коли ви запускаєте `openclaw config` без підкоманди.

Підтримувані керовані розділи: `workspace`, `model`, `web`, `gateway`, `daemon`, `channels`, `plugins`, `skills`, `health`.

## Приклади

bashCopy code
[code]
    openclaw config fileopenclaw config --section modelopenclaw config --section gateway --section daemonopenclaw config schemaopenclaw config get browser.executablePathopenclaw config set browser.executablePath "/usr/bin/google-chrome"openclaw config set browser.profiles.work.executablePath "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"openclaw config set agents.defaults.heartbeat.every "2h"openclaw config set agents.list[0].tools.exec.node "node-id-or-name"openclaw config set agents.defaults.models '{"openai/gpt-5.4":{}}' --strict-json --mergeopenclaw config set channels.discord.token --ref-provider default --ref-source env --ref-id DISCORD_BOT_TOKENopenclaw config set secrets.providers.vaultfile --provider-source file --provider-path /etc/openclaw/secrets.json --provider-mode jsonopenclaw config patch --file ./openclaw.patch.json5 --dry-runopenclaw config unset plugins.entries.brave.config.webSearch.apiKeyopenclaw config set channels.discord.token --ref-provider default --ref-source env --ref-id DISCORD_BOT_TOKEN --dry-runopenclaw config validateopenclaw config validate --json
[/code]

### `config schema`

Виводить згенеровану схему JSON для `openclaw.json` у stdout як JSON.

Що вона містить

  * Поточну кореневу схему конфігурації, а також кореневе рядкове поле `$schema` для редакторських інструментів.
  * Метадані документації полів `title` і `description`, які використовує Control UI.
  * Вкладені об'єкти, вузли wildcard (`*`) і елементів масиву (`[]`) успадковують ті самі метадані `title` / `description`, коли існує відповідна документація поля.
  * Гілки `anyOf` / `oneOf` / `allOf` також успадковують ті самі метадані документації, коли існує відповідна документація поля.
  * Наскільки можливо актуальні метадані схем Plugin + каналу, коли можна завантажити runtime-маніфести.
  * Чисту резервну схему навіть тоді, коли поточна конфігурація недійсна.

Пов'язаний runtime RPC

`config.schema.lookup` повертає один нормалізований шлях конфігурації з неглибоким вузлом схеми (`title`, `description`, `type`, `enum`, `const`, поширені межі), зіставленими метаданими підказок UI і короткими описами безпосередніх дочірніх елементів. Використовуйте його для деталізації, обмеженої шляхом, у Control UI або власних клієнтах.

bashCopy code
[code]
    openclaw config schema
[/code]

Передайте результат у файл, коли хочете переглянути або перевірити його іншими інструментами:

bashCopy code
[code]
    openclaw config schema > openclaw.schema.json
[/code]

### Шляхи

Шляхи використовують крапкову або дужкову нотацію:

bashCopy code
[code]
    openclaw config get agents.defaults.workspaceopenclaw config get agents.list[0].id
[/code]

Використовуйте індекс списку агентів, щоб указати конкретного агента:

bashCopy code
[code]
    openclaw config get agents.listopenclaw config set agents.list[1].tools.exec.node "node-id-or-name"
[/code]

## Значення

Значення за можливості розбираються як JSON5; інакше вони обробляються як рядки. Використовуйте `--strict-json`, щоб вимагати розбору JSON5. `--json` залишається підтримуваним як застарілий псевдонім.

bashCopy code
[code]
    openclaw config set agents.defaults.heartbeat.every "0m"openclaw config set gateway.port 19001 --strict-jsonopenclaw config set channels.whatsapp.groups '["*"]' --strict-json
[/code]

`config get <path> --json` виводить сире значення як JSON замість тексту, відформатованого для термінала.

Використовуйте `--merge`, коли додаєте записи до цих мап:

bashCopy code
[code]
    openclaw config set agents.defaults.models '{"openai/gpt-5.4":{}}' --strict-json --mergeopenclaw config set models.providers.ollama.models '[{"id":"llama3.2","name":"Llama 3.2"}]' --strict-json --merge
[/code]

Використовуйте `--replace` лише тоді, коли навмисно хочете, щоб надане значення стало повним цільовим значенням.

## Режими `config set`

`openclaw config set` підтримує чотири стилі призначення:

### Режим значення

bashCopy code
[code]
    openclaw config set <path> <value>
[/code]

### Режим конструктора SecretRef

bashCopy code
[code]
    openclaw config set channels.discord.token \  --ref-provider default \  --ref-source env \  --ref-id DISCORD_BOT_TOKEN
[/code]

### Режим конструктора провайдера

Режим конструктора провайдера застосовується лише до шляхів `secrets.providers.<alias>`:

bashCopy code
[code]
    openclaw config set secrets.providers.vault \  --provider-source exec \  --provider-command /usr/local/bin/openclaw-vault \  --provider-arg read \  --provider-arg openai/api-key \  --provider-timeout-ms 5000
[/code]

### Пакетний режим

bashCopy code
[code]
    openclaw config set --batch-json '[  {    "path": "secrets.providers.default",    "provider": { "source": "env" }  },  {    "path": "channels.discord.token",    "ref": { "source": "env", "provider": "default", "id": "DISCORD_BOT_TOKEN" }  }]'
[/code]

bashCopy code
[code]
    openclaw config set --batch-file ./config-set.batch.json --dry-run
[/code]

Пакетний розбір завжди використовує пакетне корисне навантаження (`--batch-json`/`--batch-file`) як джерело істини. `--strict-json` / `--json` не змінюють поведінку пакетного розбору.

## `config patch`

Використовуйте `config patch`, коли хочете вставити або передати через pipe патч у формі конфігурації замість виконання багатьох команд `config set` на основі шляхів. Вхідні дані є об'єктом JSON5. Об'єкти об'єднуються рекурсивно, масиви та скалярні значення замінюють цільове значення, а `null` видаляє цільовий шлях.

bashCopy code
[code]
    openclaw config patch --file ./openclaw.patch.json5 --dry-runopenclaw config patch --file ./openclaw.patch.json5
[/code]

Ви також можете передати патч через stdin, що корисно для сценаріїв віддаленого налаштування:

bashCopy code
[code]
    ssh openclaw-host 'openclaw config patch --stdin --dry-run' < ./openclaw.patch.json5ssh openclaw-host 'openclaw config patch --stdin' < ./openclaw.patch.json5
[/code]

Приклад патча:

json5Copy code
[code]
    {  channels: {    slack: {      enabled: true,      mode: "socket",      botToken: { source: "env", provider: "default", id: "SLACK_BOT_TOKEN" },      appToken: { source: "env", provider: "default", id: "SLACK_APP_TOKEN" },      groupPolicy: "open",      requireMention: false,    },    discord: {      enabled: true,      token: { source: "env", provider: "default", id: "DISCORD_BOT_TOKEN" },      dmPolicy: "disabled",      dm: { enabled: false },      groupPolicy: "allowlist",    },  },  agents: {    defaults: {      model: { primary: "openai/gpt-5.5" },      models: {        "openai/gpt-5.5": { params: { fastMode: true } },      },    },  },}
[/code]

Використовуйте `--replace-path <path>`, коли один об'єкт або масив має стати точно наданим значенням замість рекурсивного патчування:

bashCopy code
[code]
    openclaw config patch --file ./discord.patch.json5 --replace-path 'channels.discord.guilds["123"].channels'
[/code]

`--dry-run` запускає перевірки схеми та розв'язуваності SecretRef без запису. Exec-backed SecretRefs типово пропускаються під час сухого запуску; додайте `--allow-exec`, коли навмисно хочете, щоб сухий запуск виконував команди провайдера.

Режим шляху/значення JSON залишається підтримуваним як для SecretRef, так і для провайдерів:

bashCopy code
[code]
    openclaw config set channels.discord.token \  '{"source":"env","provider":"default","id":"DISCORD_BOT_TOKEN"}' \  --strict-json openclaw config set secrets.providers.vaultfile \  '{"source":"file","path":"/etc/openclaw/secrets.json","mode":"json"}' \  --strict-json
[/code]

## Прапорці конструктора провайдера

Цілі конструктора провайдера мають використовувати `secrets.providers.<alias>` як шлях.

Спільні прапорці

  * `--provider-source <env|file|exec>`
  * `--provider-timeout-ms <ms>` (`file`, `exec`)

Провайдер env (--provider-source env)

  * `--provider-allowlist &lt;ENV_VAR&gt;` (повторюваний)

Файловий провайдер (--provider-source file)

  * `--provider-path <path>` (обов'язковий)
  * `--provider-mode <singleValue|json>`
  * `--provider-max-bytes <bytes>`
  * `--provider-allow-insecure-path`

Exec-провайдер (--provider-source exec)

  * `--provider-command <path>` (обов'язковий)
  * `--provider-arg <arg>` (повторюваний)
  * `--provider-no-output-timeout-ms <ms>`
  * `--provider-max-output-bytes <bytes>`
  * `--provider-json-only`
  * `--provider-env &lt;KEY=VALUE&gt;` (повторюваний)
  * `--provider-pass-env &lt;ENV_VAR&gt;` (повторюваний)
  * `--provider-trusted-dir <path>` (повторюваний)
  * `--provider-allow-insecure-path`
  * `--provider-allow-symlink-command`


Приклад посиленого exec-провайдера:

bashCopy code
[code]
    openclaw config set secrets.providers.vault \  --provider-source exec \  --provider-command /usr/local/bin/openclaw-vault \  --provider-arg read \  --provider-arg openai/api-key \  --provider-json-only \  --provider-pass-env VAULT_TOKEN \  --provider-trusted-dir /usr/local/bin \  --provider-timeout-ms 5000
[/code]

## Сухий запуск

Використовуйте `--dry-run`, щоб перевірити зміни без запису в `openclaw.json`.

bashCopy code
[code]
    openclaw config set channels.discord.token \  --ref-provider default \  --ref-source env \  --ref-id DISCORD_BOT_TOKEN \  --dry-run openclaw config set channels.discord.token \  --ref-provider default \  --ref-source env \  --ref-id DISCORD_BOT_TOKEN \  --dry-run \  --json openclaw config set channels.discord.token \  --ref-provider vault \  --ref-source exec \  --ref-id discord/token \  --dry-run \  --allow-exec
[/code]

Поведінка сухого запуску

  * Режим конструктора: запускає перевірки розв'язуваності SecretRef для змінених refs/провайдерів.
  * Режим JSON (`--strict-json`, `--json` або пакетний режим): запускає перевірку схеми плюс перевірки розв'язуваності SecretRef.
  * Перевірка політик також виконується для відомих непідтримуваних цільових поверхонь SecretRef.
  * Перевірки політик оцінюють повну конфігурацію після зміни, тому записи батьківських об'єктів (наприклад, задавання `hooks` як об'єкта) не можуть обійти перевірку непідтримуваних поверхонь.
  * Перевірки exec SecretRef типово пропускаються під час сухого запуску, щоб уникнути побічних ефектів команд.
  * Використовуйте `--allow-exec` з `--dry-run`, щоб явно ввімкнути перевірки exec SecretRef (це може виконувати команди провайдера).
  * `--allow-exec` працює лише для сухого запуску й видає помилку, якщо використовується без `--dry-run`.

Поля --dry-run --json

`--dry-run --json` виводить машинозчитуваний звіт:

  * `ok`: чи пройшов пробний запуск
  * `operations`: кількість оцінених призначень
  * `checks`: чи виконувалися перевірки схеми/можливості розв’язання
  * `checks.resolvabilityComplete`: чи перевірки можливості розв’язання виконалися до завершення (false, коли exec-посилання пропущено)
  * `refsChecked`: кількість посилань, фактично розв’язаних під час пробного запуску
  * `skippedExecRefs`: кількість exec-посилань, пропущених через те, що `--allow-exec` не було встановлено
  * `errors`: структуровані помилки схеми/можливості розв’язання, коли `ok=false`


### Форма виводу JSON

json5Copy code
[code]
    {  ok: boolean,  operations: number,  configPath: string,  inputModes: ["value" | "json" | "builder", ...],  checks: {    schema: boolean,    resolvability: boolean,    resolvabilityComplete: boolean,  },  refsChecked: number,  skippedExecRefs: number,  errors?: [    {      kind: "schema" | "resolvability",      message: string,      ref?: string, // present for resolvability errors    },  ],}
[/code]

### Success example

jsonCopy code
[code]
    {  "ok": true,  "operations": 1,  "configPath": "~/.openclaw/openclaw.json",  "inputModes": ["builder"],  "checks": {    "schema": false,    "resolvability": true,    "resolvabilityComplete": true  },  "refsChecked": 1,  "skippedExecRefs": 0}
[/code]

### Failure example

jsonCopy code
[code]
    {  "ok": false,  "operations": 1,  "configPath": "~/.openclaw/openclaw.json",  "inputModes": ["builder"],  "checks": {    "schema": false,    "resolvability": true,    "resolvabilityComplete": true  },  "refsChecked": 1,  "skippedExecRefs": 0,  "errors": [    {      "kind": "resolvability",      "message": "Error: Environment variable \"MISSING_TEST_SECRET\" is not set.",      "ref": "env:default:MISSING_TEST_SECRET"    }  ]}
[/code]

If dry-run fails

  * `config schema validation failed`: форма вашої конфігурації після зміни недійсна; виправте шлях/значення або форму об’єкта provider/ref.
  * `Config policy validation failed: unsupported SecretRef usage`: поверніть ці облікові дані до введення відкритим текстом/рядком і використовуйте SecretRefs лише на підтримуваних поверхнях.
  * `SecretRef assignment(s) could not be resolved`: указаний provider/ref наразі не може бути розв’язаний (відсутня змінна середовища, недійсний файловий указівник, збій exec-провайдера або невідповідність провайдера/джерела).
  * `Dry run note: skipped <n> exec SecretRef resolvability check(s)`: пробний запуск пропустив exec-посилання; перезапустіть із `--allow-exec`, якщо вам потрібна перевірка можливості розв’язання exec.
  * Для пакетного режиму виправте помилкові записи та повторно запустіть `--dry-run` перед записом.


## Безпека запису

`openclaw config set` та інші засоби запису конфігурації, що належать OpenClaw, перевіряють повну конфігурацію після зміни, перш ніж зберегти її на диск. Якщо нове корисне навантаження не проходить перевірку схеми або виглядає як руйнівне перезаписування, активна конфігурація залишається без змін, а відхилене корисне навантаження зберігається поруч як `openclaw.json.rejected.*`.

Надавайте перевагу записам через CLI для невеликих змін:

bashCopy code
[code]
    openclaw config set gateway.reload.mode hybrid --dry-runopenclaw config set gateway.reload.mode hybridopenclaw config validate
[/code]

Якщо запис відхилено, перевірте збережене корисне навантаження та виправте повну форму конфігурації:

bashCopy code
[code]
    CONFIG="$(openclaw config file)"ls -lt "$CONFIG".rejected.* 2>/dev/null | headopenclaw config validate
[/code]

Прямі записи в редакторі все ще дозволені, але запущений Gateway вважає їх ненадійними, доки вони не пройдуть перевірку. Недійсні прямі зміни призводять до помилки запуску або пропускаються під час гарячого перезавантаження; Gateway не перезаписує `openclaw.json`. Запустіть `openclaw doctor --fix`, щоб відновити конфігурацію з префіксами/перезаписуванням або повернути останню відому справну копію. Див. [усунення несправностей Gateway](</uk/gateway/troubleshooting#gateway-rejected-invalid-config>).

Відновлення всього файла зарезервоване для ремонту через doctor. Зміни схеми Plugin або розбіжність `minHostVersion` залишаються явними, замість того щоб відкочувати непов’язані користувацькі налаштування, як-от моделі, провайдерів, профілі автентифікації, канали, експозицію gateway, інструменти, пам’ять, браузер або конфігурацію cron.

## Підкоманди

  * `config file`: вивести шлях до активного файла конфігурації (визначений із `OPENCLAW_CONFIG_PATH` або стандартного розташування). Шлях має вказувати на звичайний файл, а не на символічне посилання.


Перезапустіть gateway після змін.

## Перевірка

Перевірте поточну конфігурацію за активною схемою без запуску gateway.

bashCopy code
[code]
    openclaw config validateopenclaw config validate --json
[/code]

Після успішного проходження `openclaw config validate` ви можете використати локальний TUI, щоб вбудований агент порівняв активну конфігурацію з документацією, поки ви перевіряєте кожну зміну з того самого термінала:

bashCopy code
[code]
    openclaw chat
[/code]

Потім усередині TUI:

textCopy code
[code]
    !openclaw config file!openclaw docs gateway auth token secretref!openclaw config validate!openclaw doctor
[/code]

Типовий цикл ремонту:

* ### Compare with docs

Попросіть агента порівняти вашу поточну конфігурацію з відповідною сторінкою документації та запропонувати найменше виправлення.

* ### Apply targeted edits

Застосуйте цільові зміни за допомогою `openclaw config set` або `openclaw configure`.

* ### Re-validate

Повторно запускайте `openclaw config validate` після кожної зміни.

* ### Doctor for runtime issues

Якщо перевірка проходить, але runtime усе ще несправний, запустіть `openclaw doctor` або `openclaw doctor --fix` для допомоги з міграцією та ремонтом.

## Пов’язане

  * [Довідник CLI](</uk/cli>)
  * [Конфігурація](</uk/gateway/configuration>)


Was this useful?YesNo