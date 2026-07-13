---
title: SecretRefs хранилища секретов
source_url: https://docs.openclaw.ai/ru/plugins/vault
scraped_at: 2026-07-13
---

CapabilitiesPlugin guides

# Ссылки SecretRef для Vault

Встроенный Plugin Vault позволяет OpenClaw разрешать SecretRef типа `exec` из HashiCorp Vault при запуске и перезагрузке Gateway. OpenClaw хранит ссылки на Vault в конфигурации, сохраняет разрешённые значения в находящемся в памяти снимке секретов и не записывает разрешённые ключи API обратно в `openclaw.json`.

Используйте эту возможность, если у вас уже работает Vault или вы хотите хранить ключи поставщиков моделей вне файлов конфигурации OpenClaw. Модель среды выполнения SecretRef описана в разделе [Управление секретами](</ru/gateway/secrets>).

## Перед началом работы

Вам потребуется:

  * OpenClaw с доступным встроенным Plugin `vault`
  * доступный сервер Vault
  * аутентификация Vault, позволяющая получить клиентский токен с правами чтения путей к секретам, которые должен разрешать OpenClaw
  * среда, запускающая Gateway, должна содержать `VAULT_ADDR` и один из следующих вариантов: `VAULT_TOKEN`; `OPENCLAW_VAULT_AUTH_METHOD=token_file` вместе с `VAULT_TOKEN_FILE`; настроенный вход через JWT/Kubernetes


Средство разрешения обращается к Vault по HTTP из Node. Для разрешения SecretRef в Gateway не требуется CLI Vault.

Включите встроенный Plugin перед выполнением команд `openclaw vault`:

bashCopy code
[code]
    openclaw plugins enable vault
[/code]

## Сохранение ключа поставщика в Vault

По умолчанию OpenClaw использует KV v2, смонтированный по пути `secret`, что соответствует примерам сервера разработки Vault. Для рабочего экземпляра Vault перед созданием идентификаторов SecretRef задайте в `OPENCLAW_VAULT_KV_MOUNT` фактический путь монтирования KV. При настройках OpenClaw по умолчанию этот идентификатор SecretRef:

textCopy code
[code]
    providers/openrouter/apiKey
[/code]

считывает следующее поле Vault:

textCopy code
[code]
    secret/data/providers/openrouter -> apiKey
[/code]

Один из способов создать его с помощью CLI Vault:

bashCopy code
[code]
    export OPENROUTER_API_KEY=<openrouter-api-key>vault kv put secret/providers/openrouter apiKey="$OPENROUTER_API_KEY"
[/code]

Используйте для OpenClaw клиентский токен с ограниченной областью действия, а не корневой токен. Для стандартной структуры KV v2 минимальная политика для ключей поставщиков моделей выглядит так:

hclCopy code
[code]
    path "secret/data/providers/*" {  capabilities = ["read"]}
[/code]

## Предоставление Gateway доступа к Vault

Для локального Gateway, работающего вне контейнера, экспортируйте настройки Vault в той же оболочке, из которой запускается OpenClaw. Стандартный метод аутентификации считывает клиентский токен Vault из `VAULT_TOKEN`:

bashCopy code
[code]
    export VAULT_ADDR=https://vault.example.comexport VAULT_TOKEN=<vault-client-token>
[/code]

Если Vault Agent записывает токен в выходной файл, используйте аутентификацию через файл токена:

bashCopy code
[code]
    export VAULT_ADDR=https://vault.example.comexport OPENCLAW_VAULT_AUTH_METHOD=token_fileexport VAULT_TOKEN_FILE=/vault/secrets/token
[/code]

Если сервер Vault использует сертификат частного центра сертификации, установите этот сертификат в системное хранилище доверенных сертификатов и включите использование системного хранилища в Node:

bashCopy code
[code]
    export NODE_USE_SYSTEM_CA=1
[/code]

Либо напрямую укажите пакет сертификатов PEM:

bashCopy code
[code]
    export NODE_EXTRA_CA_CERTS=/path/to/vault-ca.pem
[/code]

Эти переменные должны быть заданы при запуске OpenClaw. Plugin Vault передаёт их своему процессу разрешения.

Для неинтерактивной аутентификации JWT используйте файл JWT рабочей нагрузки и роль Vault типа `jwt`:

bashCopy code
[code]
    export VAULT_ADDR=https://vault.example.comexport OPENCLAW_VAULT_AUTH_METHOD=jwtexport OPENCLAW_VAULT_AUTH_MOUNT=jwtexport OPENCLAW_VAULT_AUTH_ROLE=openclawexport OPENCLAW_VAULT_JWT_FILE=/var/run/secrets/tokens/vault
[/code]

Файл JWT должен содержать проецируемый токен рабочей нагрузки, например токен сервисной учётной записи Kubernetes с аудиторией, принимаемой ролью Vault. Интерактивный вход через OIDC в браузере удобен для людей, но среде выполнения Gateway требуется неинтерактивный вход через JWT или файл токена.

Для метода аутентификации Kubernetes в Vault используйте `kubernetes`. Этот вариант предназначен для Gateway, работающих как поды; по умолчанию точка монтирования — `kubernetes`, а файл JWT — стандартный путь к токену сервисной учётной записи:

bashCopy code
[code]
    export VAULT_ADDR=https://vault.example.comexport OPENCLAW_VAULT_AUTH_METHOD=kubernetesexport OPENCLAW_VAULT_AUTH_ROLE=openclaw
[/code]

Задавайте `OPENCLAW_VAULT_AUTH_MOUNT`, только если аутентификация Kubernetes смонтирована в Vault не по пути `auth/kubernetes`. Задавайте `OPENCLAW_VAULT_JWT_FILE`, только если токен сервисной учётной записи проецируется по нестандартному пути.

Необязательные настройки:

bashCopy code
[code]
    export VAULT_NAMESPACE=<namespace-name>export OPENCLAW_VAULT_KV_MOUNT=secretexport OPENCLAW_VAULT_KV_VERSION=2
[/code]

Проверьте, что доступно текущей оболочке:

bashCopy code
[code]
    openclaw vault status
[/code]

Если настроено несколько поставщиков секретов на основе Vault, выберите нужного по псевдониму:

bashCopy code
[code]
    openclaw vault status --provider-alias corp-vault
[/code]

Команда `openclaw vault status` никогда не выводит `VAULT_TOKEN`; она сообщает только о том, заданы ли токен, файл токена и файл JWT.

## Создание и применение плана SecretRef

Создайте план, сопоставляющий ключ API поставщика моделей OpenRouter с Vault:

bashCopy code
[code]
    openclaw vault setup \  --plan-out ./vault-secrets-plan.json \  --openrouter-id providers/openrouter/apiKey
[/code]

Примените и проверьте план:

bashCopy code
[code]
    openclaw secrets apply --from ./vault-secrets-plan.json --dry-run --allow-execopenclaw secrets apply --from ./vault-secrets-plan.json --allow-execopenclaw secrets audit --check --allow-execopenclaw secrets reload
[/code]

Используйте `--allow-exec`, поскольку Plugin Vault выполняет разрешение через управляемого OpenClaw поставщика SecretRef типа `exec`.

Если Gateway ещё не запущен, после применения плана запустите его обычным способом вместо выполнения `openclaw secrets reload`.

## Настройка дополнительных ключей поставщиков

Встроенные сокращённые параметры:

bashCopy code
[code]
    openclaw vault setup --openai-id providers/openai/apiKeyopenclaw vault setup --anthropic-id providers/anthropic/apiKeyopenclaw vault setup --openrouter-id providers/openrouter/apiKey
[/code]

Несколько ключей поставщиков в одном плане:

bashCopy code
[code]
    openclaw vault setup \  --plan-out ./vault-secrets-plan.json \  --openai-id providers/openai/apiKey \  --anthropic-id providers/anthropic/apiKey \  --openrouter-id providers/openrouter/apiKey
[/code]

Для встроенных поставщиков без сокращённых параметров, а также уже настроенных совместимых с OpenAI и пользовательских поставщиков моделей используйте `--provider-key`:

bashCopy code
[code]
    openclaw vault setup \  --plan-out ./vault-secrets-plan.json \  --provider-key local-openai=providers/local-openai/apiKey \  --provider-key groq=providers/groq/apiKey
[/code]

Каждый параметр `--provider-key <provider=id>` записывает SecretRef в `models.providers.<provider>.apiKey`. Для пользовательских поставщиков он не создаёт настройки `baseUrl`, `api` или `models`; сначала настройте их.

Используйте `--target <path=id>` для любого известного целевого пути SecretRef:

bashCopy code
[code]
    openclaw vault setup \  --target channels.telegram.botToken=channels/telegram/botToken \  --target models.providers.openai.headers.x-api-key=providers/openai/proxyKey \  --target auth-profiles:main:profiles.openai.key=providers/openai/apiKey
[/code]

Целевые пути без префикса применяются к `openclaw.json`. Для существующих целей в `auth-profiles.json` используйте `auth-profiles:<agentId>:<path>`. Целевой путь должен быть зарегистрированной целью SecretRef в OpenClaw. Команда настройки не создаёт произвольные именованные секреты в OpenClaw; хранилищем секретов остаётся Vault, а OpenClaw сохраняет SecretRef только в поддерживаемых полях конфигурации.

## Формат идентификатора SecretRef

Идентификаторы SecretRef для Vault используют следующее соглашение:

textCopy code
[code]
    <vault-secret-path>/<field>
[/code]

Примеры:

Идентификатор SecretRef | Стандартное чтение из KV v2 в Vault | Возвращаемое поле  
---|---|---  
`providers/openrouter/apiKey` | `secret/data/providers/openrouter` | `apiKey`  
`providers/openai/apiKey` | `secret/data/providers/openai` | `apiKey`  
`teams/agent-prod/openrouter` | `secret/data/teams/agent-prod` | `openrouter`  
  
Возвращаемое поле Vault должно быть строкой.

Для KV v1 задайте:

bashCopy code
[code]
    export OPENCLAW_VAULT_KV_VERSION=1
[/code]

После этого `providers/openrouter/apiKey` считывается так:

textCopy code
[code]
    secret/providers/openrouter -> apiKey
[/code]

## Что хранит OpenClaw

При применении плана настройки Vault сохраняется управляемый Plugin поставщик:

jsonCopy code
[code]
    {  "source": "exec",  "pluginIntegration": {    "pluginId": "vault",    "integrationId": "vault"  }}
[/code]

Поля учётных данных ссылаются на этого поставщика:

jsonCopy code
[code]
    { "source": "exec", "provider": "vault", "id": "providers/openrouter/apiKey" }
[/code]

Разрешённое значение существует только в активном снимке секретов среды выполнения.

## Контейнеры и управляемые развёртывания

Gateway в контейнерах по-прежнему используют тот же Plugin и конфигурацию SecretRef. Контейнер должен получать:

  * `VAULT_ADDR`
  * один источник аутентификации: 
    * `VAULT_TOKEN`
    * `OPENCLAW_VAULT_AUTH_METHOD=token_file` вместе с `VAULT_TOKEN_FILE`
    * `OPENCLAW_VAULT_AUTH_METHOD=jwt` вместе с `OPENCLAW_VAULT_AUTH_MOUNT`, `OPENCLAW_VAULT_AUTH_ROLE` и `OPENCLAW_VAULT_JWT_FILE`
    * `OPENCLAW_VAULT_AUTH_METHOD=kubernetes` вместе с `OPENCLAW_VAULT_AUTH_ROLE`; при необходимости можно переопределить `OPENCLAW_VAULT_AUTH_MOUNT` или `OPENCLAW_VAULT_JWT_FILE`
  * необязательные `VAULT_NAMESPACE`, `OPENCLAW_VAULT_KV_MOUNT` и `OPENCLAW_VAULT_KV_VERSION`


При использовании Kubernetes отдавайте предпочтение `OPENCLAW_VAULT_AUTH_METHOD=kubernetes`, если в Vault для кластера настроена аутентификация Kubernetes. Используйте `OPENCLAW_VAULT_AUTH_METHOD=jwt`, только если Vault настроен для обработки кластера как универсального издателя JWT/OIDC. Оба варианта предпочтительнее долгоживущего токена Vault в секрете Kubernetes. В развёртываниях с боковым контейнером Vault Agent или инжектором вместо этого можно использовать `token_file`.

В многопользовательских конфигурациях Vault сохраняйте маршрутизацию арендаторов в политиках Vault и конфигурации развёртывания. OpenClaw не требует фиксированной точки монтирования, роли или пути: каждая среда Gateway может задавать собственные `OPENCLAW_VAULT_KV_MOUNT`, `OPENCLAW_VAULT_AUTH_ROLE` и идентификаторы SecretRef. Если один общий Gateway должен одновременно разрешать секреты разных пользователей Vault, используйте настроенных вручную поставщиков `exec`, оборачивающих разные среды аутентификации, либо распределите арендаторов по средам Gateway с отдельными переменными окружения Vault.

## Связанные материалы

  * [Управление секретами](</ru/gateway/secrets>)
  * [`openclaw secrets`](</ru/cli/secrets>)
  * [Перечень плагинов](</ru/plugins/plugin-inventory>)


Was this useful?YesNo

Open issue