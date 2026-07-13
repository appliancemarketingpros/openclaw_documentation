---
title: SecretRef-и сховища секретів
source_url: https://docs.openclaw.ai/uk/plugins/vault
scraped_at: 2026-07-13
---

CapabilitiesPlugin guides

# SecretRef у Vault

Вбудований Plugin Vault дає змогу OpenClaw розв’язувати SecretRef типу `exec` із HashiCorp Vault під час запуску та перезавантаження Gateway. OpenClaw зберігає посилання на Vault у конфігурації, утримує розв’язані значення у знімку секретів у пам’яті та не записує розв’язані ключі API назад до `openclaw.json`.

Використовуйте це рішення, якщо ви вже використовуєте Vault або хочете зберігати ключі постачальників моделей поза файлами конфігурації OpenClaw. Опис моделі виконання SecretRef див. у розділі [Керування секретами](</uk/gateway/secrets>).

## Перед початком

Вам потрібні:

  * OpenClaw із доступним вбудованим плагіном `vault`
  * доступний сервер Vault
  * автентифікація Vault, яка може надати клієнтський токен із доступом на читання шляхів секретів, які має розв’язувати OpenClaw
  * середовище, що запускає Gateway, повинно містити `VAULT_ADDR` і один із таких варіантів: `VAULT_TOKEN`, `OPENCLAW_VAULT_AUTH_METHOD=token_file` разом із `VAULT_TOKEN_FILE` або налаштований вхід через JWT/Kubernetes


Засіб розв’язання взаємодіє з Vault через HTTP із Node. Для розв’язання SecretRef у Gateway не потрібен CLI Vault.

Увімкніть вбудований плагін перед виконанням команд `openclaw vault`:

bashCopy code
[code]
    openclaw plugins enable vault
[/code]

## Збереження ключа постачальника у Vault

За замовчуванням OpenClaw використовує KV v2, змонтований у `secret`, відповідно до прикладів сервера розробки Vault. Для робочого середовища Vault установіть `OPENCLAW_VAULT_KV_MOUNT` відповідно до фактичного шляху монтування KV перед створенням ідентифікаторів SecretRef. За стандартних налаштувань OpenClaw цей ідентифікатор SecretRef:

textCopy code
[code]
    providers/openrouter/apiKey
[/code]

читає це поле Vault:

textCopy code
[code]
    secret/data/providers/openrouter -> apiKey
[/code]

Один зі способів створити його за допомогою CLI Vault:

bashCopy code
[code]
    export OPENROUTER_API_KEY=<openrouter-api-key>vault kv put secret/providers/openrouter apiKey="$OPENROUTER_API_KEY"
[/code]

Використовуйте для OpenClaw клієнтський токен з обмеженою областю дії, а не кореневий токен. Для стандартної структури KV v2 мінімальна політика для ключів постачальників моделей має такий вигляд:

hclCopy code
[code]
    path "secret/data/providers/*" {  capabilities = ["read"]}
[/code]

## Надання Gateway доступу до Vault

Для локального Gateway без контейнеризації експортуйте налаштування Vault у тій самій оболонці, у якій запускається OpenClaw. Стандартний метод автентифікації зчитує клієнтський токен Vault із `VAULT_TOKEN`:

bashCopy code
[code]
    export VAULT_ADDR=https://vault.example.comexport VAULT_TOKEN=<vault-client-token>
[/code]

Якщо Vault Agent записує токен у вихідний файл, використовуйте автентифікацію через файл токена:

bashCopy code
[code]
    export VAULT_ADDR=https://vault.example.comexport OPENCLAW_VAULT_AUTH_METHOD=token_fileexport VAULT_TOKEN_FILE=/vault/secrets/token
[/code]

Якщо сервер Vault підписано приватним центром сертифікації, установіть цей сертифікат у сховище довіри хоста й увімкніть використання системного сховища довіри в Node:

bashCopy code
[code]
    export NODE_USE_SYSTEM_CA=1
[/code]

Або безпосередньо вкажіть набір сертифікатів PEM:

bashCopy code
[code]
    export NODE_EXTRA_CA_CERTS=/path/to/vault-ca.pem
[/code]

Ці змінні мають бути наявні під час запуску OpenClaw. Plugin Vault передає їх своєму процесу розв’язання.

Для неінтерактивної автентифікації JWT використовуйте файл JWT робочого навантаження та роль Vault типу `jwt`:

bashCopy code
[code]
    export VAULT_ADDR=https://vault.example.comexport OPENCLAW_VAULT_AUTH_METHOD=jwtexport OPENCLAW_VAULT_AUTH_MOUNT=jwtexport OPENCLAW_VAULT_AUTH_ROLE=openclawexport OPENCLAW_VAULT_JWT_FILE=/var/run/secrets/tokens/vault
[/code]

Файл JWT має містити проєктований токен робочого навантаження, наприклад токен облікового запису служби Kubernetes з аудиторією, яку приймає роль Vault. Інтерактивний вхід OIDC через браузер корисний для людей, але середовищу виконання Gateway потрібен неінтерактивний вхід JWT або файл токена.

Для методу автентифікації Kubernetes у Vault використовуйте `kubernetes`. Він призначений для Gateway, що працюють як поди; стандартна точка монтування — `kubernetes`, а стандартний файл JWT — це типовий шлях токена облікового запису служби:

bashCopy code
[code]
    export VAULT_ADDR=https://vault.example.comexport OPENCLAW_VAULT_AUTH_METHOD=kubernetesexport OPENCLAW_VAULT_AUTH_ROLE=openclaw
[/code]

Установлюйте `OPENCLAW_VAULT_AUTH_MOUNT`, лише якщо автентифікацію Kubernetes у Vault змонтовано не в `auth/kubernetes`. Установлюйте `OPENCLAW_VAULT_JWT_FILE`, лише якщо токен облікового запису служби проєктується за нестандартним шляхом.

Необов’язкові налаштування:

bashCopy code
[code]
    export VAULT_NAMESPACE=<namespace-name>export OPENCLAW_VAULT_KV_MOUNT=secretexport OPENCLAW_VAULT_KV_VERSION=2
[/code]

Перевірте, що доступно поточній оболонці:

bashCopy code
[code]
    openclaw vault status
[/code]

Якщо налаштовано кілька постачальників секретів на основі Vault, виберіть одного за псевдонімом:

bashCopy code
[code]
    openclaw vault status --provider-alias corp-vault
[/code]

`openclaw vault status` ніколи не виводить `VAULT_TOKEN`; команда повідомляє лише про те, чи задано токен, файл токена та файл JWT.

## Створення та застосування плану SecretRef

Створіть план, який зіставляє ключ API постачальника моделей OpenRouter із Vault:

bashCopy code
[code]
    openclaw vault setup \  --plan-out ./vault-secrets-plan.json \  --openrouter-id providers/openrouter/apiKey
[/code]

Застосуйте та перевірте план:

bashCopy code
[code]
    openclaw secrets apply --from ./vault-secrets-plan.json --dry-run --allow-execopenclaw secrets apply --from ./vault-secrets-plan.json --allow-execopenclaw secrets audit --check --allow-execopenclaw secrets reload
[/code]

Використовуйте `--allow-exec`, оскільки Plugin Vault виконує розв’язання через керованого OpenClaw постачальника SecretRef типу `exec`.

Якщо Gateway ще не запущено, після застосування плану запустіть його звичайним способом замість виконання `openclaw secrets reload`.

## Налаштування додаткових ключів постачальників

Вбудовані скорочення:

bashCopy code
[code]
    openclaw vault setup --openai-id providers/openai/apiKeyopenclaw vault setup --anthropic-id providers/anthropic/apiKeyopenclaw vault setup --openrouter-id providers/openrouter/apiKey
[/code]

Кілька ключів постачальників в одному плані:

bashCopy code
[code]
    openclaw vault setup \  --plan-out ./vault-secrets-plan.json \  --openai-id providers/openai/apiKey \  --anthropic-id providers/anthropic/apiKey \  --openrouter-id providers/openrouter/apiKey
[/code]

Для вбудованих постачальників без скорочень або вже налаштованих сумісних з OpenAI та спеціалізованих постачальників моделей використовуйте `--provider-key`:

bashCopy code
[code]
    openclaw vault setup \  --plan-out ./vault-secrets-plan.json \  --provider-key local-openai=providers/local-openai/apiKey \  --provider-key groq=providers/groq/apiKey
[/code]

Кожен параметр `--provider-key <provider=id>` записує SecretRef до `models.providers.<provider>.apiKey`. Для спеціалізованих постачальників він не створює налаштування `baseUrl`, `api` або `models`; спочатку налаштуйте їх.

Використовуйте `--target <path=id>` для будь-якого відомого цільового шляху SecretRef:

bashCopy code
[code]
    openclaw vault setup \  --target channels.telegram.botToken=channels/telegram/botToken \  --target models.providers.openai.headers.x-api-key=providers/openai/proxyKey \  --target auth-profiles:main:profiles.openai.key=providers/openai/apiKey
[/code]

Цільові шляхи без префікса застосовуються до `openclaw.json`. Для наявних цільових шляхів у `auth-profiles.json` використовуйте `auth-profiles:<agentId>:<path>`. Цільовий шлях має бути зареєстрованим у OpenClaw цільовим шляхом SecretRef. Команда налаштування не створює довільні іменовані секрети в OpenClaw; Vault залишається сховищем секретів, а OpenClaw зберігає SecretRef лише в підтримуваних полях конфігурації.

## Формат ідентифікатора SecretRef

Ідентифікатори SecretRef у Vault використовують таку угоду:

textCopy code
[code]
    <vault-secret-path>/<field>
[/code]

Приклади:

Ідентифікатор SecretRef | Стандартне читання Vault KV v2 | Повернуте поле  
---|---|---  
`providers/openrouter/apiKey` | `secret/data/providers/openrouter` | `apiKey`  
`providers/openai/apiKey` | `secret/data/providers/openai` | `apiKey`  
`teams/agent-prod/openrouter` | `secret/data/teams/agent-prod` | `openrouter`  
  
Поле, повернуте Vault, має бути рядком.

Для KV v1 установіть:

bashCopy code
[code]
    export OPENCLAW_VAULT_KV_VERSION=1
[/code]

Тоді `providers/openrouter/apiKey` читає:

textCopy code
[code]
    secret/providers/openrouter -> apiKey
[/code]

## Що зберігає OpenClaw

Застосування плану налаштування Vault зберігає керованого плагіном постачальника:

jsonCopy code
[code]
    {  "source": "exec",  "pluginIntegration": {    "pluginId": "vault",    "integrationId": "vault"  }}
[/code]

Поля облікових даних посилаються на цього постачальника:

jsonCopy code
[code]
    { "source": "exec", "provider": "vault", "id": "providers/openrouter/apiKey" }
[/code]

Розв’язане значення міститься лише в активному знімку секретів середовища виконання.

## Контейнери та керовані розгортання

Контейнеризовані Gateway використовують той самий Plugin і ту саму конфігурацію SecretRef. Контейнер повинен отримати:

  * `VAULT_ADDR`
  * одне джерело автентифікації: 
    * `VAULT_TOKEN`
    * `OPENCLAW_VAULT_AUTH_METHOD=token_file` разом із `VAULT_TOKEN_FILE`
    * `OPENCLAW_VAULT_AUTH_METHOD=jwt` разом із `OPENCLAW_VAULT_AUTH_MOUNT`, `OPENCLAW_VAULT_AUTH_ROLE` і `OPENCLAW_VAULT_JWT_FILE`
    * `OPENCLAW_VAULT_AUTH_METHOD=kubernetes` разом із `OPENCLAW_VAULT_AUTH_ROLE`; за потреби можна перевизначити `OPENCLAW_VAULT_AUTH_MOUNT` або `OPENCLAW_VAULT_JWT_FILE`
  * необов’язкові `VAULT_NAMESPACE`, `OPENCLAW_VAULT_KV_MOUNT` і `OPENCLAW_VAULT_KV_VERSION`


Під час використання Kubernetes віддавайте перевагу `OPENCLAW_VAULT_AUTH_METHOD=kubernetes`, якщо у Vault для кластера налаштовано автентифікацію Kubernetes. Використовуйте `OPENCLAW_VAULT_AUTH_METHOD=jwt`, лише якщо Vault налаштовано розглядати кластер як універсального видавця JWT/OIDC. Обидва варіанти кращі за довготривалий токен Vault у секреті Kubernetes. Розгортання із допоміжним контейнером або інжектором Vault Agent натомість можуть використовувати `token_file`.

Для багатокористувацьких конфігурацій Vault зберігайте маршрутизацію орендарів у політиках Vault і конфігурації розгортання. OpenClaw не вимагає фіксованої точки монтування, ролі чи шляху: кожне середовище Gateway може задавати власні `OPENCLAW_VAULT_KV_MOUNT`, `OPENCLAW_VAULT_AUTH_ROLE` та ідентифікатори SecretRef. Якщо один спільний Gateway має одночасно розв’язувати секрети різних користувачів Vault, використовуйте налаштованих вручну постачальників `exec`, які обгортають окремі середовища автентифікації, або розділіть орендарів між середовищами Gateway з окремими змінними середовища Vault.

## Пов’язані матеріали

  * [Керування секретами](</uk/gateway/secrets>)
  * [`openclaw secrets`](</uk/cli/secrets>)
  * [Перелік плагінів](</uk/plugins/plugin-inventory>)


Was this useful?YesNo

Open issue