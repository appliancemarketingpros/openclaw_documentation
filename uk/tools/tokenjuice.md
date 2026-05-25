---
title: Tokenjuice
source_url: https://docs.openclaw.ai/uk/tools/tokenjuice
scraped_at: 2026-05-25
---

`tokenjuice` — це необов’язковий вбудований Plugin, який виконує Compaction шумних результатів інструментів `exec` і `bash` після того, як команда вже була виконана.

Він змінює повернений `tool_result`, а не саму команду. Tokenjuice не переписує shell-ввід, не перезапускає команди й не змінює коди виходу.

Наразі це застосовується до вбудованих запусків PI та динамічних інструментів OpenClaw у harness app-server Codex. Tokenjuice підключається до middleware результатів інструментів OpenClaw і обрізає вивід перед тим, як він повертається в активний сеанс harness-а.

## Увімкнення Plugin-а

Швидкий шлях:

bashCopy code
[code]
    openclaw config set plugins.entries.tokenjuice.enabled true
[/code]

Еквівалент:

bashCopy code
[code]
    openclaw plugins enable tokenjuice
[/code]

OpenClaw уже постачається з цим Plugin-ом. Окремого кроку `plugins install` або `tokenjuice install openclaw` немає.

Якщо вам зручніше редагувати config напряму:

json5Copy code
[code]
    {  plugins: {    entries: {      tokenjuice: {        enabled: true,      },    },  },}
[/code]

## Що змінює tokenjuice

  * Виконує Compaction шумних результатів `exec` і `bash` перед тим, як вони повертаються в сеанс.
  * Залишає оригінальне виконання команди без змін.
  * Зберігає точне читання вмісту файлів та інші команди, які tokenjuice має залишати сирими.
  * Залишається opt-in: вимкніть Plugin, якщо хочете дослівний вивід усюди.


## Як перевірити, що він працює

  1. Увімкніть Plugin.
  2. Запустіть сеанс, який може викликати `exec`.
  3. Виконайте шумну команду, наприклад `git status`.
  4. Переконайтеся, що повернений результат інструмента коротший і більш структурований, ніж сирий shell-вивід.


## Вимкнення Plugin-а

bashCopy code
[code]
    openclaw config set plugins.entries.tokenjuice.enabled false
[/code]

Або:

bashCopy code
[code]
    openclaw plugins disable tokenjuice
[/code]

## Пов’язане

  * [Exec tool](</uk/tools/exec>)
  * [Thinking levels](</uk/tools/thinking>)
  * [Context engine](</uk/concepts/context-engine>)


Was this useful?YesNo