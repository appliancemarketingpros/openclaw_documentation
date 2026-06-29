---
title: Голосовой вызов
source_url: https://docs.openclaw.ai/ru/cli/voicecall
scraped_at: 2026-06-29
---

ReferenceCLI commands

# `openclaw voicecall`

`voicecall` — это команда, предоставляемая Plugin. Она появляется только тогда, когда Plugin голосовых вызовов установлен и включен.

Когда Gateway запущен, операционные команды (`call`, `start`, `continue`, `speak`, `dtmf`, `end`, `status`) маршрутизируются в среду выполнения голосовых вызовов этого Gateway. Если Gateway недоступен, они переключаются на автономную среду выполнения CLI.

## Подкоманды

bashCopy code
[code]
    openclaw voicecall setup    [--json]openclaw voicecall smoke    [-t <phone>] [--message <text>] [--mode <m>] [--yes] [--json]openclaw voicecall call     -m <text> [-t <phone>] [--mode <m>]openclaw voicecall start    --to <phone> [--message <text>] [--mode <m>]openclaw voicecall continue --call-id <id> --message <text>openclaw voicecall speak    --call-id <id> --message <text>openclaw voicecall dtmf     --call-id <id> --digits <digits>openclaw voicecall end      --call-id <id>openclaw voicecall status   [--call-id <id>] [--json]openclaw voicecall tail     [--file <path>] [--since <n>] [--poll <ms>]openclaw voicecall latency  [--file <path>] [--last <n>]openclaw voicecall expose   [--mode <m>] [--path <p>] [--port <port>] [--serve-path <p>]
[/code]

Подкоманда | Описание  
---|---  
`setup` | Показать проверки готовности провайдера и Webhook.  
`smoke` | Запустить проверки готовности; выполнить тестовый вызов в реальном времени только с `--yes`.  
`call` | Инициировать исходящий голосовой вызов.  
`start` | Псевдоним для `call`, где требуется `--to`, а `--message` необязателен.  
`continue` | Произнести сообщение и дождаться следующего ответа.  
`speak` | Произнести сообщение без ожидания ответа.  
`dtmf` | Отправить DTMF-цифры в активный вызов.  
`end` | Завершить активный вызов.  
`status` | Проверить активные вызовы (или один по `--call-id`).  
`tail` | Следить за `calls.jsonl` (полезно во время тестов провайдера).  
`latency` | Сводка метрик задержки хода из `calls.jsonl`.  
`expose` | Переключить Tailscale serve/funnel для конечной точки Webhook.  
  
## Настройка и smoke-тест

### `setup`

По умолчанию выводит удобочитаемые проверки готовности. Передайте `--json` для скриптов.

bashCopy code
[code]
    openclaw voicecall setupopenclaw voicecall setup --json
[/code]

### `smoke`

Запускает те же проверки готовности. Реальный телефонный вызов не будет выполнен, если одновременно не указаны `--to` и `--yes`.

Флаг | Значение по умолчанию | Описание  
---|---|---  
`-t, --to <phone>` | (нет) | Номер телефона для live smoke.  
`--message <text>` | `OpenClaw voice call smoke test.` | Сообщение, которое произносится во время smoke-вызова.  
`--mode <mode>` | `notify` | Режим вызова: `notify` или `conversation`.  
`--yes` | `false` | Фактически выполнить исходящий вызов в реальном времени.  
`--json` | `false` | Вывести машиночитаемый JSON.  
  
bashCopy code
[code]
    openclaw voicecall smokeopenclaw voicecall smoke --to "+15555550123"        # dry runopenclaw voicecall smoke --to "+15555550123" --yes  # live notify call
[/code]

## Жизненный цикл вызова

### `call`

Инициировать исходящий голосовой вызов.

Флаг | Обязательно | Значение по умолчанию | Описание  
---|---|---|---  
`-m, --message <text>` | да | (нет) | Сообщение, которое произносится при соединении вызова.  
`-t, --to <phone>` | нет | config `toNumber` | Номер телефона E.164 для вызова.  
`--mode <mode>` | нет | `conversation` | Режим вызова: `notify` (завершить после сообщения) или `conversation` (оставить открытым).  
  
bashCopy code
[code]
    openclaw voicecall call --to "+15555550123" --message "Hello"openclaw voicecall call -m "Heads up" --mode notify
[/code]

### `start`

Псевдоним для `call` с другой формой флагов по умолчанию.

Флаг | Обязательно | Значение по умолчанию | Описание  
---|---|---|---  
`--to <phone>` | да | (нет) | Номер телефона для вызова.  
`--message <text>` | нет | (нет) | Сообщение, которое произносится при соединении вызова.  
`--mode <mode>` | нет | `conversation` | Режим вызова: `notify` или `conversation`.  
  
### `continue`

Произнести сообщение и дождаться ответа.

Флаг | Обязательно | Описание  
---|---|---  
`--call-id <id>` | да | Идентификатор вызова.  
`--message <text>` | да | Сообщение для произнесения.  
  
### `speak`

Произнести сообщение без ожидания ответа.

Флаг | Обязательно | Описание  
---|---|---  
`--call-id <id>` | да | Идентификатор вызова.  
`--message <text>` | да | Сообщение для произнесения.  
  
### `dtmf`

Отправить DTMF-цифры в активный вызов.

Флаг | Обязательно | Описание  
---|---|---  
`--call-id <id>` | да | Идентификатор вызова.  
`--digits <digits>` | да | DTMF-цифры (например, `ww123456#` для пауз).  
  
### `end`

Завершить активный вызов.

Флаг | Обязательно | Описание  
---|---|---  
`--call-id <id>` | да | Идентификатор вызова.  
  
### `status`

Проверить активные вызовы.

Флаг | Значение по умолчанию | Описание  
---|---|---  
`--call-id <id>` | (нет) | Ограничить вывод одним вызовом.  
`--json` | `false` | Вывести машиночитаемый JSON.  
  
bashCopy code
[code]
    openclaw voicecall statusopenclaw voicecall status --jsonopenclaw voicecall status --call-id <id>
[/code]

## Журналы и метрики

### `tail`

Следить за журналом JSONL голосовых вызовов. При запуске выводит последние `--since` строк, затем передает новые строки по мере их записи.

Флаг | Значение по умолчанию | Описание  
---|---|---  
`--file <path>` | определяется из хранилища Plugin | Путь к `calls.jsonl`.  
`--since <n>` | `25` | Строки для вывода перед слежением.  
`--poll <ms>` | `250` (минимум 50) | Интервал опроса в миллисекундах.  
  
### `latency`

Сводка метрик задержки хода и ожидания прослушивания из `calls.jsonl`. Выводится JSON со сводками `recordsScanned`, `turnLatency` и `listenWait`.

Флаг | Значение по умолчанию | Описание  
---|---|---  
`--file <path>` | определяется из хранилища Plugin | Путь к `calls.jsonl`.  
`--last <n>` | `200` (минимум 1) | Количество последних записей для анализа.  
  
## Открытие Webhook

### `expose`

Включить, отключить или изменить конфигурацию Tailscale serve/funnel для голосового Webhook.

Флаг | Значение по умолчанию | Описание  
---|---|---  
`--mode <mode>` | `funnel` | `off`, `serve` (tailnet) или `funnel` (public).  
`--path <path>` | config `tailscale.path` или `--serve-path` | Путь Tailscale для открытия.  
`--port <port>` | config `serve.port` или `3334` | Локальный порт Webhook.  
`--serve-path <path>` | config `serve.path` или `/voice/webhook` | Локальный путь Webhook.  
  
bashCopy code
[code]
    openclaw voicecall expose --mode serveopenclaw voicecall expose --mode funnelopenclaw voicecall expose --mode off
[/code]

## Связанные материалы

  * [Справочник CLI](</ru/cli>)
  * [Plugin голосовых вызовов](</ru/plugins/voice-call>)


Was this useful?YesNo

Open issue