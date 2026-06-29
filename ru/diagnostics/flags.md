---
title: Флаги диагностики
source_url: https://docs.openclaw.ai/ru/diagnostics/flags
scraped_at: 2026-06-29
---

HelpDiagnostics

Флаги диагностики позволяют включать целевые отладочные журналы без включения подробного журналирования везде. Флаги включаются явно и не имеют эффекта, если подсистема их не проверяет.

## Как это работает

  * Флаги — это строки (без учета регистра).
  * Вы можете включать флаги в конфигурации или через переопределение env.
  * Поддерживаются подстановочные знаки: 
    * `telegram.*` соответствует `telegram.http`
    * `*` включает все флаги


## Включение через конфигурацию

jsonCopy code
[code]
    {  "diagnostics": {    "flags": ["telegram.http"]  }}
[/code]

Несколько флагов:

jsonCopy code
[code]
    {  "diagnostics": {    "flags": ["telegram.http", "brave.http", "gateway.*"]  }}
[/code]

Перезапустите Gateway после изменения флагов.

## Переопределение через env (одноразово)

bashCopy code
[code]
    OPENCLAW_DIAGNOSTICS=telegram.http,telegram.payload
[/code]

Отключить все флаги:

bashCopy code
[code]
    OPENCLAW_DIAGNOSTICS=0
[/code]

`OPENCLAW_DIAGNOSTICS=0` — это переопределение отключения на уровне процесса: оно отключает флаги как из env, так и из конфигурации для этого процесса.

## Флаги профилирования

Флаги профилировщика включают целевые интервалы измерения времени без повышения глобальных уровней журналирования. По умолчанию они отключены.

Включить все интервалы, ограниченные профилировщиком, для одного запуска Gateway:

bashCopy code
[code]
    OPENCLAW_DIAGNOSTICS=profiler openclaw gateway run
[/code]

Включить только интервалы профилировщика для диспетчеризации ответов:

bashCopy code
[code]
    OPENCLAW_DIAGNOSTICS=reply.profiler openclaw gateway run
[/code]

Включить только интервалы профилировщика запуска app-server Codex, инструментов и потоков:

bashCopy code
[code]
    OPENCLAW_DIAGNOSTICS=codex.profiler openclaw gateway run
[/code]

Включить флаги профилировщика из конфигурации:

jsonCopy code
[code]
    {  "diagnostics": {    "flags": ["reply.profiler", "codex.profiler"]  }}
[/code]

Перезапустите Gateway после изменения флагов конфигурации. Чтобы отключить флаг профилировщика, удалите его из `diagnostics.flags` и перезапустите. Чтобы временно отключить каждый флаг диагностики, даже если конфигурация включает флаги профилировщика, запустите процесс с:

bashCopy code
[code]
    OPENCLAW_DIAGNOSTICS=0 openclaw gateway run
[/code]

## Артефакты временной шкалы

Флаг `timeline` записывает структурированные события времени запуска и выполнения для внешних QA harnesses:

bashCopy code
[code]
    OPENCLAW_DIAGNOSTICS=timeline \OPENCLAW_DIAGNOSTICS_TIMELINE_PATH=/tmp/openclaw-timeline.jsonl \openclaw gateway run
[/code]

Вы также можете включить его в конфигурации:

jsonCopy code
[code]
    {  "diagnostics": {    "flags": ["timeline"]  }}
[/code]

Путь к файлу временной шкалы по-прежнему берется из `OPENCLAW_DIAGNOSTICS_TIMELINE_PATH`. Когда `timeline` включен только из конфигурации, самые ранние интервалы загрузки конфигурации не выводятся, потому что OpenClaw еще не прочитал конфигурацию; последующие интервалы запуска используют флаг конфигурации.

`OPENCLAW_DIAGNOSTICS=1`, `OPENCLAW_DIAGNOSTICS=all` и `OPENCLAW_DIAGNOSTICS=*` также включают временную шкалу, потому что они включают каждый флаг диагностики. Предпочитайте `timeline`, когда вам нужен только артефакт измерения времени в формате JSONL.

Записи временной шкалы используют оболочку `openclaw.diagnostics.v1`. События могут включать идентификаторы процессов, названия фаз, названия интервалов, длительности, идентификаторы Plugin, количество зависимостей, образцы задержки цикла событий, имена операций провайдеров, состояние выхода дочернего процесса и имена/сообщения ошибок запуска. Рассматривайте файлы временной шкалы как локальные диагностические артефакты; просматривайте их перед передачей за пределы вашего компьютера.

## Куда попадают журналы

Флаги выводят журналы в стандартный файл диагностического журнала. По умолчанию:

CodeCopy code
[code]
    /tmp/openclaw/openclaw-YYYY-MM-DD.log
[/code]

Если вы задали `logging.file`, используйте этот путь вместо него. Журналы имеют формат JSONL (один JSON-объект на строку). Редактирование чувствительных данных по-прежнему применяется на основе `logging.redactSensitive`.

## Извлечение журналов

Выберите последний файл журнала:

bashCopy code
[code]
    ls -t /tmp/openclaw/openclaw-*.log | head -n 1
[/code]

Отфильтровать диагностику HTTP Telegram:

bashCopy code
[code]
    rg "telegram http error" /tmp/openclaw/openclaw-*.log
[/code]

Отфильтровать диагностику HTTP Brave Search:

bashCopy code
[code]
    rg "brave http" /tmp/openclaw/openclaw-*.log
[/code]

Или отслеживайте файл во время воспроизведения:

bashCopy code
[code]
    tail -f /tmp/openclaw/openclaw-$(date +%F).log | rg "telegram http error"
[/code]

Для удаленных Gateway вы также можете использовать `openclaw logs --follow` (см. [/cli/logs](</ru/cli/logs>)).

## Примечания

  * Если `logging.level` установлен выше `warn`, эти журналы могут подавляться. Значение по умолчанию `info` подходит.
  * `brave.http` журналирует URL-адреса/параметры запросов Brave Search, статус/время ответа и события попадания/промаха/записи кэша. Он не журналирует ключи API или тела ответов, но поисковые запросы могут быть чувствительными.
  * Флаги безопасно оставлять включенными; они влияют только на объем журналов для конкретной подсистемы.
  * Используйте [/logging](</ru/logging>), чтобы изменить назначения, уровни и редактирование чувствительных данных в журналах.


## См. также

  * [Диагностика Gateway](</ru/gateway/diagnostics>)
  * [Устранение неполадок Gateway](</ru/gateway/troubleshooting>)


Was this useful?YesNo

Open issue