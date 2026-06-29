---
title: Панель управления
source_url: https://docs.openclaw.ai/ru/cli/dashboard
scraped_at: 2026-06-29
---

ReferenceCLI commands

# `openclaw dashboard`

Откройте пользовательский интерфейс управления с текущей аутентификацией.

bashCopy code
[code]
    openclaw dashboardopenclaw dashboard --no-open
[/code]

Примечания:

  * `dashboard` по возможности разрешает настроенные SecretRefs `gateway.auth.token`.
  * `dashboard` следует `gateway.tls.enabled`: Gateway с включенным TLS выводят/открывают URL пользовательского интерфейса управления с `https://` и подключаются через `wss://`.
  * Если доставка URL панели управления с аутентификацией по токену через буфер обмена/браузер не удалась, `dashboard` записывает безопасную подсказку для ручной аутентификации, называя `OPENCLAW_GATEWAY_TOKEN`, `gateway.auth.token` и ключ фрагмента `token`, не выводя значение токена.
  * Для токенов, управляемых SecretRef (разрешенных или неразрешенных), `dashboard` выводит/копирует/открывает URL без токена, чтобы не раскрывать внешние секреты в выводе терминала, истории буфера обмена или аргументах запуска браузера.
  * Если `gateway.auth.token` управляется SecretRef, но не разрешен в этом пути команды, команда выводит URL без токена и явные инструкции по устранению проблемы вместо встраивания недействительного плейсхолдера токена.


## Связанные материалы

  * [Справочник CLI](</ru/cli>)
  * [Панель управления](</ru/web/dashboard>)


Was this useful?YesNo

Open issue