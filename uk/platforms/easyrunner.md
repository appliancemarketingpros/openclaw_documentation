---
title: EasyRunner
source_url: https://docs.openclaw.ai/uk/platforms/easyrunner
scraped_at: 2026-06-29
---

PlatformsPlatforms overview

EasyRunner може розміщувати OpenClaw Gateway як невеликий контейнеризований застосунок за своїм проксі Caddy. Цей посібник передбачає наявність хоста EasyRunner, який запускає сумісні з Podman застосунки Compose і надає HTTPS через Caddy.

## Перш ніж почати

  * Сервер EasyRunner із доменом, спрямованим на нього.
  * Зібраний або опублікований контейнерний образ OpenClaw.
  * Постійний том конфігурації для `/home/node/.openclaw`.
  * Постійний том робочого простору для `/workspace`.
  * Надійний токен або пароль Gateway.


За можливості залишайте автентифікацію пристрою ввімкненою. Якщо ваше розгортання зворотного проксі не може коректно передавати ідентичність пристрою, спершу виправте налаштування довіреного проксі; використовуйте небезпечні обходи автентифікації лише для повністю приватної мережі під контролем оператора.

## Застосунок Compose

Створіть застосунок EasyRunner із файлом Compose такого вигляду:

yamlCopy code
[code]
    services:  openclaw:    image: ghcr.io/openclaw/openclaw:latest    restart: unless-stopped    environment:      OPENCLAW_GATEWAY_TOKEN: ${OPENCLAW_GATEWAY_TOKEN}      OPENCLAW_HOME: /home/node      OPENCLAW_STATE_DIR: /home/node/.openclaw      OPENCLAW_CONFIG_PATH: /home/node/.openclaw/openclaw.json      OPENCLAW_WORKSPACE_DIR: /workspace    volumes:      - openclaw-config:/home/node/.openclaw      - openclaw-workspace:/workspace    labels:      caddy: openclaw.example.com      caddy.reverse_proxy: "{{upstreams 1455}}"    command: ["openclaw", "gateway", "--bind", "lan", "--port", "1455"] volumes:  openclaw-config:  openclaw-workspace:
[/code]

Замініть `openclaw.example.com` на ім’я хоста вашого Gateway. Зберігайте `OPENCLAW_GATEWAY_TOKEN` у менеджері секретів/змінних середовища EasyRunner, а не комітьте його у визначення застосунку.

## Налаштування OpenClaw

У постійному томі конфігурації залишайте Gateway доступним лише через проксі та вимагайте автентифікацію:

json5Copy code
[code]
    {  gateway: {    bind: "lan",    port: 1455,    auth: {      token: "${OPENCLAW_GATEWAY_TOKEN}",    },  },}
[/code]

Якщо Caddy завершує TLS для Gateway, налаштуйте параметри довіреного проксі для точного шляху проксі, а не вимикайте перевірки автентифікації глобально. Див. [автентифікацію довіреного проксі](</uk/gateway/trusted-proxy-auth>).

## Перевірка

З вашої робочої станції:

bashCopy code
[code]
    openclaw gateway probe --url https://openclaw.example.com --token <token>openclaw gateway status --url https://openclaw.example.com --token <token>
[/code]

З хоста EasyRunner перевірте журнали застосунку на наявність Gateway, що слухає, і відсутність помилок запуску SecretRef, Plugin або автентифікації каналу.

## Оновлення та резервні копії

  * Отримайте або зберіть новий образ OpenClaw, а потім повторно розгорніть застосунок EasyRunner.
  * Створіть резервну копію тому `openclaw-config` перед оновленнями.
  * Створіть резервну копію `openclaw-workspace`, якщо агенти записують туди довговічні дані проєкту.
  * Запустіть `openclaw doctor` після великих оновлень, щоб виявити міграції конфігурації та попередження сервісів.


## Усунення несправностей

  * `gateway probe` не може підключитися: переконайтеся, що ім’я хоста Caddy вказує на застосунок і що контейнер слухає на `0.0.0.0:1455`.
  * Автентифікація не проходить: одночасно змініть токен у секретах EasyRunner і в команді локального клієнта.
  * Після відновлення файли належать root: виправте змонтовані томи, щоб користувач контейнера міг записувати в `/home/node/.openclaw` і `/workspace`.
  * Plugin-и браузера або каналів не працюють: перевірте, чи доступні всередині контейнера потрібні зовнішні двійкові файли, вихід у мережу та змонтовані облікові дані.


Was this useful?YesNo

Open issue