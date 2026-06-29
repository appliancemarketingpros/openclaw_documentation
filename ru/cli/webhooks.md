---
title: Webhooks
source_url: https://docs.openclaw.ai/ru/cli/webhooks
scraped_at: 2026-06-29
---

ReferenceCLI commands

# `openclaw webhooks`

Вспомогательные средства и интеграции Webhook. Сейчас эта поверхность ограничена потоками Gmail Pub/Sub, которые интегрируются со встроенным наблюдателем `gog`.

## Подкоманды

bashCopy code
[code]
    openclaw webhooks gmail setup --account <email> [...]openclaw webhooks gmail run   [--account <email>] [...]
[/code]

Подкоманда | Описание  
---|---  
`gmail setup` | Настраивает Gmail watch, тему/подписку Pub/Sub и целевой адрес доставки OpenClaw webhook.  
`gmail run` | Запускает `gog watch serve` и цикл автоматического продления watch.  
  
## `webhooks gmail setup`

Настройте Gmail watch, Pub/Sub и доставку OpenClaw webhook.

bashCopy code
[code]
    openclaw webhooks gmail setup --account you@example.comopenclaw webhooks gmail setup --account you@example.com --project my-gcp-project --jsonopenclaw webhooks gmail setup --account you@example.com --hook-url https://gateway.example.com/hooks/gmail
[/code]

### Обязательные

Флаг | Описание  
---|---  
`--account <email>` | Аккаунт Gmail для наблюдения.  
  
### Параметры Pub/Sub

Флаг | По умолчанию | Описание  
---|---|---  
`--project <id>` | (нет) | ID проекта GCP (владелец OAuth-клиента).  
`--topic <name>` | `gog-gmail-watch` | Имя темы Pub/Sub.  
`--subscription <name>` | `gog-gmail-watch-push` | Имя подписки Pub/Sub.  
`--label <label>` | `INBOX` | Метка Gmail для наблюдения.  
`--push-endpoint <url>` | (нет) | Явная конечная точка Pub/Sub push. Переопределяет Tailscale.  
  
### Параметры доставки OpenClaw

Флаг | По умолчанию | Описание  
---|---|---  
`--hook-url <url>` | (нет) | URL OpenClaw webhook.  
`--hook-token <token>` | (нет) | Токен OpenClaw webhook.  
`--push-token <token>` | (нет) | Push-токен, передаваемый в `gog watch serve`.  
  
### Параметры `gog watch serve`

Флаг | По умолчанию | Описание  
---|---|---  
`--bind <host>` | `127.0.0.1` | Хост привязки `gog watch serve`.  
`--port <port>` | `8788` | Порт `gog watch serve`.  
`--path <path>` | `/gmail-pubsub` | Путь `gog watch serve`.  
`--include-body` | `true` | Включать фрагменты тела письма. Передайте `--no-include-body`, чтобы отключить.  
`--max-bytes <n>` | `20000` | Максимальное число байтов на фрагмент тела.  
`--renew-minutes <n>` | `720` (12 ч) | Продлевать Gmail watch каждые N минут.  
  
### Экспонирование через Tailscale

Флаг | По умолчанию | Описание  
---|---|---  
`--tailscale <mode>` | `funnel` | Экспонировать конечную точку push через tailscale: `funnel`, `serve` или `off`.  
`--tailscale-path <path>` | (нет) | Путь для tailscale serve/funnel.  
`--tailscale-target <t>` | (нет) | Цель Tailscale serve/funnel (порт, `host:port` или URL).  
  
### Вывод

Флаг | Описание  
---|---  
`--json` | Вывести машиночитаемую сводку вместо текста.  
  
## `webhooks gmail run`

Запустите `gog watch serve` и цикл автоматического продления watch на переднем плане.

bashCopy code
[code]
    openclaw webhooks gmail run --account you@example.com
[/code]

`run` принимает те же флаги `gog watch serve`, доставки OpenClaw, Pub/Sub и Tailscale, что и `setup`, за исключением:

  * `--account` является **необязательным** для `run` (используется настроенный аккаунт).
  * `run` **не** принимает `--project`, `--push-endpoint` или `--json`.
  * У флагов `run` нет встроенных значений по умолчанию; отсутствующие значения берутся из значений, записанных `setup`.


Категория | Флаги  
---|---  
Pub/Sub | `--account`, `--topic`, `--subscription`, `--label`  
Доставка OpenClaw | `--hook-url`, `--hook-token`, `--push-token`  
`gog watch serve` | `--bind`, `--port`, `--path`, `--include-body`, `--max-bytes`, `--renew-minutes`  
Tailscale | `--tailscale`, `--tailscale-path`, `--tailscale-target`  
  
## Сквозной поток

См. [интеграцию Gmail Pub/Sub](</ru/automation/cron-jobs#gmail-pubsub-integration>) для настройки проекта GCP, OAuth и стороны Gateway, которая работает вместе с этими командами CLI.

## Связанные материалы

  * [Справочник CLI](</ru/cli>)
  * [Автоматизация Webhook](</ru/automation/cron-jobs>)
  * [Gmail Pub/Sub](</ru/automation/cron-jobs#gmail-pubsub-integration>)


Was this useful?YesNo

Open issue