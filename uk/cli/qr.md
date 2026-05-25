---
title: QR
source_url: https://docs.openclaw.ai/uk/cli/qr
scraped_at: 2026-05-25
---

# `openclaw qr`

Згенеруйте QR для сполучення мобільного пристрою та код налаштування з поточної конфігурації Gateway.

## Використання

bashCopy code
[code]
    openclaw qropenclaw qr --setup-code-onlyopenclaw qr --jsonopenclaw qr --remoteopenclaw qr --url wss://gateway.example/ws
[/code]

## Параметри

  * `--remote`: віддати перевагу `gateway.remote.url`; якщо його не задано, `gateway.tailscale.mode=serve|funnel` усе ще може надати віддалену публічну URL-адресу
  * `--url <url>`: перевизначити URL-адресу gateway, що використовується в payload
  * `--public-url <url>`: перевизначити публічну URL-адресу, що використовується в payload
  * `--token <token>`: перевизначити, за яким токеном gateway проходить автентифікацію bootstrap-потік
  * `--password <password>`: перевизначити, за яким паролем gateway проходить автентифікацію bootstrap-потік
  * `--setup-code-only`: вивести лише код налаштування
  * `--no-ascii`: пропустити ASCII-відображення QR
  * `--json`: вивести JSON (`setupCode`, `gatewayUrl`, `auth`, `urlSource`)


## Примітки

  * `--token` і `--password` взаємовиключні.
  * Сам код налаштування тепер містить непрозорий короткочасний `bootstrapToken`, а не спільний токен/пароль gateway.
  * У вбудованому bootstrap-потоці для вузла/оператора основний токен вузла все ще потрапляє з `scopes: []`.
  * Якщо bootstrap-передача також видає токен оператора, він залишається обмеженим allowlist для bootstrap: `operator.approvals`, `operator.read`, `operator.talk.secrets`, `operator.write`.
  * Перевірки scope для bootstrap мають префікс ролі. Цей allowlist оператора задовольняє лише запити оператора; ролям, що не є операторами, усе ще потрібні scope під власним префіксом ролі.
  * Сполучення мобільного пристрою завершується закритою відмовою для URL-адрес gateway `ws://` через Tailscale/публічні маршрути. Приватні LAN-адреси та хости Bonjour `.local` залишаються підтримуваними через `ws://`, але мобільні маршрути Tailscale/публічні маршрути мають використовувати Tailscale Serve/Funnel або URL-адресу gateway `wss://`.
  * З `--remote` OpenClaw вимагає або `gateway.remote.url`, або `gateway.tailscale.mode=serve|funnel`.
  * З `--remote`, якщо фактично активні віддалені облікові дані налаштовано як SecretRefs і ви не передаєте `--token` або `--password`, команда розв’язує їх з активного знімка gateway. Якщо gateway недоступний, команда швидко завершується з помилкою.
  * Без `--remote` локальні SecretRefs автентифікації gateway розв’язуються, коли не передано CLI-перевизначення автентифікації: 
    * `gateway.auth.token` розв’язується, коли автентифікація токеном може перемогти (явний `gateway.auth.mode="token"` або виведений режим, у якому жодне джерело пароля не перемагає).
    * `gateway.auth.password` розв’язується, коли автентифікація паролем може перемогти (явний `gateway.auth.mode="password"` або виведений режим без переможного токена з auth/env).
  * Якщо налаштовано і `gateway.auth.token`, і `gateway.auth.password` (включно з SecretRefs), а `gateway.auth.mode` не задано, розв’язання коду налаштування завершується помилкою, доки режим не буде задано явно.
  * Примітка щодо розбіжності версій Gateway: цей шлях команди вимагає gateway, який підтримує `secrets.resolve`; старіші gateway повертають помилку невідомого методу.
  * Після сканування підтвердьте сполучення пристрою за допомогою: 
    * `openclaw devices list`
    * `openclaw devices approve <requestId>`


## Пов’язане

  * [Довідник CLI](</uk/cli>)
  * [Сполучення](</uk/cli/pairing>)


Was this useful?YesNo