---
title: Tokenjuice
source_url: https://docs.openclaw.ai/ru/tools/tokenjuice
scraped_at: 2026-06-29
---

CapabilitiesTools

`tokenjuice` — это необязательный внешний Plugin, который сжимает зашумленные результаты инструментов `exec` и `bash` после того, как команда уже выполнена.

Он изменяет возвращаемый `tool_result`, а не саму команду. Tokenjuice не переписывает ввод оболочки, не запускает команды повторно и не изменяет коды выхода.

Сегодня это применяется к встроенным запускам OpenClaw и динамическим инструментам OpenClaw в Codex app-server harness. Tokenjuice подключается к middleware результатов инструментов OpenClaw и обрезает вывод перед тем, как он возвращается в активную сессию harness.

## Включить Plugin

Установите один раз:

bashCopy code
[code]
    openclaw plugins install clawhub:@openclaw/tokenjuice
[/code]

Затем включите его:

bashCopy code
[code]
    openclaw config set plugins.entries.tokenjuice.enabled true
[/code]

Эквивалент:

bashCopy code
[code]
    openclaw plugins enable tokenjuice
[/code]

Если вы предпочитаете редактировать конфигурацию напрямую:

json5Copy code
[code]
    {  plugins: {    entries: {      tokenjuice: {        enabled: true,      },    },  },}
[/code]

## Что изменяет tokenjuice

  * Сжимает зашумленные результаты `exec` и `bash` перед их передачей обратно в сессию.
  * Оставляет исходное выполнение команды без изменений.
  * Сохраняет точные чтения содержимого файлов и другие команды, которые tokenjuice должен оставлять в исходном виде.
  * Остается явным выбором: отключите Plugin, если хотите получать дословный вывод везде.


## Проверить, что он работает

  1. Включите Plugin.
  2. Запустите сессию, которая может вызывать `exec`.
  3. Выполните зашумленную команду, например `git status`.
  4. Проверьте, что возвращенный результат инструмента короче и структурированнее, чем необработанный вывод оболочки.


## Отключить Plugin

bashCopy code
[code]
    openclaw config set plugins.entries.tokenjuice.enabled false
[/code]

Или:

bashCopy code
[code]
    openclaw plugins disable tokenjuice
[/code]

## Связанное

  * [Инструмент Exec](</ru/tools/exec>)
  * [Уровни размышления](</ru/tools/thinking>)
  * [Движок контекста](</ru/concepts/context-engine>)


Was this useful?YesNo

Open issue