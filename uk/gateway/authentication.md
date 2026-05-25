---
title: Автентифікація
source_url: https://docs.openclaw.ai/uk/gateway/authentication
scraped_at: 2026-05-25
---

OpenClaw підтримує OAuth і API-ключі для постачальників моделей. Для постійно ввімкнених хостів Gateway API-ключі зазвичай є найпередбачуванішим варіантом. Потоки підписки/OAuth також підтримуються, коли вони відповідають моделі облікового запису вашого постачальника.

Див. [/concepts/oauth](</uk/concepts/oauth>), щоб ознайомитися з повним потоком OAuth і схемою зберігання. Для автентифікації на основі SecretRef (постачальники `env`/`file`/`exec`) див. [Керування секретами](</uk/gateway/secrets>). Правила відповідності облікових даних і кодів причин, які використовує `models status --probe`, див. у [Семантиці облікових даних автентифікації](</uk/auth-credential-semantics>).

## Рекомендоване налаштування (API-ключ, будь-який постачальник)

Якщо ви запускаєте довготривалий Gateway, почніть з API-ключа для вибраного постачальника. Зокрема для Anthropic автентифікація за API-ключем усе ще є найпередбачуванішим серверним налаштуванням, але OpenClaw також підтримує повторне використання локального входу Claude CLI.

  1. Створіть API-ключ у консолі свого постачальника.
  2. Розмістіть його на **хості Gateway** (машині, де виконується `openclaw gateway`).

bashCopy code
[code]
    export &lt;PROVIDER&gt;_API_KEY="..."openclaw models status
[/code]

  3. Якщо Gateway працює під systemd/launchd, краще розмістити ключ у `~/.openclaw/.env`, щоб демон міг його прочитати:

bashCopy code
[code]
    cat >> ~/.openclaw/.env <<'EOF'&lt;PROVIDER&gt;_API_KEY=...EOF
[/code]

Потім перезапустіть демон (або перезапустіть процес Gateway) і перевірте ще раз:

bashCopy code
[code]
    openclaw models statusopenclaw doctor
[/code]

Якщо ви не хочете самостійно керувати змінними середовища, онбординг може зберігати API-ключі для використання демоном: `openclaw onboard`.

Докладніше про успадкування середовища (`env.shellEnv`, `~/.openclaw/.env`, systemd/launchd) див. у [Довідці](</uk/help>).

## Anthropic: сумісність Claude CLI і токенів

Автентифікація setup-token Anthropic досі доступна в OpenClaw як підтримуваний шлях токена. Співробітники Anthropic відтоді повідомили нам, що використання Claude CLI у стилі OpenClaw знову дозволене, тому OpenClaw вважає повторне використання Claude CLI і використання `claude -p` санкціонованими для цієї інтеграції, якщо Anthropic не опублікує нову політику. Коли повторне використання Claude CLI доступне на хості, тепер це рекомендований шлях.

Для довготривалих хостів Gateway API-ключ Anthropic усе ще є найпередбачуванішим налаштуванням. Якщо ви хочете повторно використати наявний вхід Claude на тому самому хості, використайте шлях Anthropic Claude CLI в онбордингу/конфігурації.

Рекомендоване налаштування хоста для повторного використання Claude CLI:

bashCopy code
[code]
    # Run on the gateway hostclaude auth loginclaude auth status --textopenclaw models auth login --provider anthropic --method cli --set-default
[/code]

Це двокрокове налаштування:

  1. Увійдіть у сам Claude Code до Anthropic на хості Gateway.
  2. Повідомте OpenClaw, щоб він перемкнув вибір моделей Anthropic на локальний бекенд `claude-cli` і зберіг відповідний профіль автентифікації OpenClaw.


Якщо `claude` відсутній у `PATH`, спочатку встановіть Claude Code або задайте `agents.defaults.cliBackends.claude-cli.command` як реальний шлях до виконуваного файла.

Ручне введення токена (будь-який постачальник; записує `auth-profiles.json` і оновлює конфігурацію):

bashCopy code
[code]
    openclaw models auth paste-token --provider openrouter
[/code]

`auth-profiles.json` зберігає лише облікові дані. Канонічна форма така:

jsonCopy code
[code]
    {  "version": 1,  "profiles": {    "openrouter:default": {      "type": "api_key",      "provider": "openrouter",      "key": "OPENROUTER_API_KEY"    }  }}
[/code]

OpenClaw під час виконання очікує канонічну форму `version` \+ `profiles`. Якщо в старішій інсталяції досі є плаский файл, наприклад `{ "openrouter": { "apiKey": "..." } }`, виконайте `openclaw doctor --fix`, щоб переписати його як профіль API-ключа `openrouter:default`; doctor збереже копію `.legacy-flat.*.bak` поруч з оригіналом. Деталі кінцевої точки, як-от `baseUrl`, `api`, ідентифікатори моделей, заголовки й тайм-аути, мають бути в `models.providers.<id>` у `openclaw.json` або `models.json`, а не в `auth-profiles.json`.

Зовнішні маршрути автентифікації, як-от Bedrock `auth: "aws-sdk"`, також не є обліковими даними. Якщо вам потрібен іменований маршрут Bedrock, розмістіть `auth.profiles.<id>.mode: "aws-sdk"` в `openclaw.json`; не записуйте `type: "aws-sdk"` у `auth-profiles.json`. `openclaw doctor --fix` переносить застарілі маркери AWS SDK зі сховища облікових даних у метадані конфігурації.

Посилання на профілі автентифікації також підтримуються для статичних облікових даних:

  * Облікові дані `api_key` можуть використовувати `keyRef: { source, provider, id }`
  * Облікові дані `token` можуть використовувати `tokenRef: { source, provider, id }`
  * Профілі в режимі OAuth не підтримують облікові дані SecretRef; якщо `auth.profiles.<id>.mode` встановлено в `"oauth"`, вхідні `keyRef`/`tokenRef` на основі SecretRef для цього профілю відхиляються.


Перевірка, зручна для автоматизації (вихід `1`, коли прострочено/відсутнє, `2`, коли строк дії завершується):

bashCopy code
[code]
    openclaw models status --check
[/code]

Живі перевірки автентифікації:

bashCopy code
[code]
    openclaw models status --probe
[/code]

Примітки:

  * Рядки перевірки можуть надходити з профілів автентифікації, облікових даних середовища або `models.json`.
  * Якщо явний `auth.order.<provider>` пропускає збережений профіль, перевірка повідомляє `excluded_by_auth_order` для цього профілю, замість того щоб пробувати його.
  * Якщо автентифікація існує, але OpenClaw не може визначити придатного для перевірки кандидата моделі для цього постачальника, перевірка повідомляє `status: no_model`.
  * Періоди cooldown через rate-limit можуть бути прив'язані до моделі. Профіль, що перебуває в cooldown для однієї моделі, усе ще може бути придатним для спорідненої моделі в того самого постачальника.


Необов'язкові операційні скрипти (systemd/Termux) задокументовано тут: [Скрипти моніторингу автентифікації](</uk/help/scripts#auth-monitoring-scripts>)

## Примітка щодо Anthropic

Бекенд Anthropic `claude-cli` знову підтримується.

  * Співробітники Anthropic повідомили нам, що цей шлях інтеграції OpenClaw знову дозволений.
  * Тому OpenClaw вважає повторне використання Claude CLI і використання `claude -p` санкціонованими для запусків із підтримкою Anthropic, якщо Anthropic не опублікує нову політику.
  * API-ключі Anthropic залишаються найпередбачуванішим вибором для довготривалих хостів Gateway і явного контролю серверного білінгу.


## Перевірка стану автентифікації моделей

bashCopy code
[code]
    openclaw models statusopenclaw doctor
[/code]

## Поведінка ротації API-ключів (Gateway)

Деякі постачальники підтримують повторну спробу запиту з альтернативними ключами, коли API-виклик натрапляє на rate-limit постачальника.

  * Порядок пріоритету: 
    * `OPENCLAW_LIVE_&lt;PROVIDER&gt;_KEY` (одиночне перевизначення)
    * `&lt;PROVIDER&gt;_API_KEYS`
    * `&lt;PROVIDER&gt;_API_KEY`
    * `&lt;PROVIDER&gt;_API_KEY_*`
  * Постачальники Google також включають `GOOGLE_API_KEY` як додатковий fallback.
  * Той самий список ключів дедуплікується перед використанням.
  * OpenClaw повторює спробу з наступним ключем лише для помилок rate-limit (наприклад `429`, `rate_limit`, `quota`, `resource exhausted`, `Too many concurrent requests`, `ThrottlingException`, `concurrency limit reached` або `workers_ai ... quota limit exceeded`).
  * Помилки, не пов'язані з rate-limit, не повторюються з альтернативними ключами.
  * Якщо всі ключі завершуються помилкою, повертається фінальна помилка з останньої спроби.


## Керування тим, які облікові дані використовуються

### Для сеансу (команда чату)

Використовуйте `/model <alias-or-id>@<profileId>`, щоб закріпити конкретні облікові дані постачальника для поточного сеансу (приклади ідентифікаторів профілів: `anthropic:default`, `anthropic:work`).

Використовуйте `/model` (або `/model list`) для компактного вибору; використовуйте `/model status` для повного подання (кандидати + наступний профіль автентифікації, а також деталі кінцевої точки постачальника, коли налаштовано).

### Для агента (перевизначення CLI)

Установіть явне перевизначення порядку профілів автентифікації для агента (зберігається в `auth-state.json` цього агента):

bashCopy code
[code]
    openclaw models auth order get --provider anthropicopenclaw models auth order set --provider anthropic anthropic:defaultopenclaw models auth order clear --provider anthropic
[/code]

Використовуйте `--agent <id>`, щоб націлитися на конкретного агента; пропустіть його, щоб використати налаштованого агента за замовчуванням. Коли ви налагоджуєте проблеми порядку, `openclaw models status --probe` показує пропущені збережені профілі як `excluded_by_auth_order`, а не мовчки пропускає їх. Коли ви налагоджуєте проблеми cooldown, пам'ятайте, що cooldown через rate-limit може бути прив'язаний до одного ідентифікатора моделі, а не до всього профілю постачальника.

## Усунення несправностей

### "No credentials found"

Якщо профіль Anthropic відсутній, налаштуйте API-ключ Anthropic на **хості Gateway** або налаштуйте шлях setup-token Anthropic, а потім перевірте ще раз:

bashCopy code
[code]
    openclaw models status
[/code]

### Токен скоро завершиться/прострочений

Виконайте `openclaw models status`, щоб підтвердити, строк дії якого профілю завершується. Якщо профіль токена Anthropic відсутній або прострочений, оновіть це налаштування через setup-token або перейдіть на API-ключ Anthropic.

## Пов'язане

  * [Керування секретами](</uk/gateway/secrets>)
  * [Віддалений доступ](</uk/gateway/remote>)
  * [Сховище автентифікації](</uk/concepts/oauth>)


Was this useful?YesNo