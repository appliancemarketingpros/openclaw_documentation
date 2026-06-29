---
title: Память
source_url: https://docs.openclaw.ai/ru/cli/memory
scraped_at: 2026-06-29
---

ReferenceCLI commands

# `openclaw memory`

Управляйте индексацией и поиском семантической памяти. Предоставляется встроенным Plugin `memory-core`. Команда доступна, когда `plugins.slots.memory` выбирает `memory-core` (по умолчанию); другие плагины памяти предоставляют собственные пространства имен CLI.

Связано:

  * Концепция памяти: [Память](</ru/concepts/memory>)
  * Вики памяти: [Вики памяти](</ru/plugins/memory-wiki>)
  * CLI вики: [wiki](</ru/cli/wiki>)
  * Plugins: [Plugins](</ru/tools/plugin>)


## Примеры

bashCopy code
[code]
    openclaw memory statusopenclaw memory status --deepopenclaw memory status --fixopenclaw memory index --forceopenclaw memory search "meeting notes"openclaw memory search --query "deployment" --max-results 20openclaw memory promote --limit 10 --min-score 0.75openclaw memory promote --applyopenclaw memory promote --json --min-recall-count 0 --min-unique-queries 0openclaw memory promote-explain "router vlan"openclaw memory promote-explain "router vlan" --jsonopenclaw memory rem-harnessopenclaw memory rem-harness --jsonopenclaw memory status --jsonopenclaw memory status --deep --indexopenclaw memory status --deep --index --verboseopenclaw memory status --agent mainopenclaw memory index --agent main --verbose
[/code]

## Параметры

`memory status` и `memory index`:

  * `--agent <id>`: ограничить область одним агентом. Без этого параметра эти команды выполняются для каждого настроенного агента; если список агентов не настроен, они используют агента по умолчанию.
  * `--verbose`: выводить подробные журналы во время проверок и индексации.


`memory status`:

  * `--deep`: проверить готовность локального векторного хранилища, готовность поставщика эмбеддингов и готовность семантического векторного поиска. Обычный `memory status` остается быстрым и не запускает живую генерацию эмбеддингов или обнаружение поставщика; неизвестное состояние векторного хранилища или семантического вектора означает, что оно не проверялось в этой команде. Лексический режим QMD `searchMode: "search"` пропускает семантические векторные проверки и обслуживание эмбеддингов даже с `--deep`.
  * `--index`: запустить переиндексацию, если хранилище изменено (подразумевает `--deep`).
  * `--fix`: исправить устаревшие блокировки recall и нормализовать метаданные продвижения.
  * `--json`: вывести результат в JSON.


Если `memory status` показывает `Dreaming status: blocked`, управляемый cron Dreaming включен, но heartbeat, который его запускает, не срабатывает для агента по умолчанию. См. [Dreaming никогда не запускается](</ru/concepts/dreaming#dreaming-never-runs-status-shows-blocked>) для двух распространенных причин.

`memory index`:

  * `--force`: принудительно выполнить полную переиндексацию.


`memory search`:

  * Ввод запроса: передайте либо позиционный `[query]`, либо `--query <text>`.
  * Если указаны оба, приоритет имеет `--query`.
  * Если не указан ни один, команда завершается с ошибкой.
  * `--agent <id>`: ограничить область одним агентом (по умолчанию: агент по умолчанию).
  * `--max-results <n>`: ограничить количество возвращаемых результатов.
  * `--min-score <n>`: отфильтровать совпадения с низкой оценкой.
  * `--json`: вывести результаты в JSON.


`memory promote`:

Предварительно просматривайте и применяйте продвижения краткосрочной памяти.

bashCopy code
[code]
    openclaw memory promote [--apply] [--limit <n>] [--include-promoted]
[/code]

  * `--apply` \-- записать продвижения в `MEMORY.md` (по умолчанию: только предварительный просмотр).
  * `--limit <n>` \-- ограничить количество показываемых кандидатов.
  * `--include-promoted` \-- включить записи, уже продвинутые в предыдущих циклах.


Полный список параметров:

  * Ранжирует краткосрочных кандидатов из `memory/YYYY-MM-DD.md` с использованием взвешенных сигналов продвижения (`frequency`, `relevance`, `query diversity`, `recency`, `consolidation`, `conceptual richness`).
  * Использует краткосрочные сигналы как из recall памяти, так и из проходов ежедневного приема данных, а также сигналы усиления фаз light/REM.
  * Когда Dreaming включен, `memory-core` автоматически управляет одним заданием cron, которое выполняет полный проход (`light -> REM -> deep`) в фоне (ручной `openclaw cron add` не требуется).
  * `--agent <id>`: ограничить область одним агентом (по умолчанию: агент по умолчанию).
  * `--limit <n>`: максимальное количество кандидатов для возврата/применения.
  * `--min-score <n>`: минимальная взвешенная оценка продвижения.
  * `--min-recall-count <n>`: минимальное количество recall, требуемое для кандидата.
  * `--min-unique-queries <n>`: минимальное количество различных запросов, требуемое для кандидата.
  * `--apply`: добавить выбранных кандидатов в `MEMORY.md` и пометить их как продвинутые.
  * `--include-promoted`: включить в вывод уже продвинутых кандидатов.
  * `--json`: вывести результат в JSON.


`memory promote-explain`:

Объяснить конкретного кандидата на продвижение и разбивку его оценки.

bashCopy code
[code]
    openclaw memory promote-explain <selector> [--agent <id>] [--include-promoted] [--json]
[/code]

  * `<selector>`: ключ кандидата, фрагмент пути или фрагмент сниппета для поиска.
  * `--agent <id>`: ограничить область одним агентом (по умолчанию: агент по умолчанию).
  * `--include-promoted`: включить уже продвинутых кандидатов.
  * `--json`: вывести результат в JSON.


`memory rem-harness`:

Предварительно просмотреть REM-рефлексии, кандидатные истины и результат глубокого продвижения без записи чего-либо.

bashCopy code
[code]
    openclaw memory rem-harness [--agent <id>] [--include-promoted] [--json]
[/code]

  * `--agent <id>`: ограничить область одним агентом (по умолчанию: агент по умолчанию).
  * `--include-promoted`: включить уже продвинутых глубоких кандидатов.
  * `--json`: вывести результат в JSON.


## Dreaming

Dreaming — это фоновая система консолидации памяти с тремя совместными фазами: **light** (сортировка/подготовка краткосрочного материала), **deep** (продвижение устойчивых фактов в `MEMORY.md`) и **REM** (рефлексия и выявление тем).

  * Включите с помощью `plugins.entries.memory-core.config.dreaming.enabled: true`.
  * Переключайте из чата с помощью `/dreaming on|off` (или проверяйте с помощью `/dreaming status`).
  * Dreaming выполняется по одному управляемому расписанию прохода (`dreaming.frequency`) и запускает фазы по порядку: light, REM, deep.
  * Только фаза deep записывает устойчивую память в `MEMORY.md`.
  * Читаемый человеком вывод фаз и записи дневника записываются в `DREAMS.md` (или существующий `dreams.md`), с необязательными отчетами по фазам в `memory/dreaming/<phase>/YYYY-MM-DD.md`.
  * Ранжирование использует взвешенные сигналы: частоту recall, релевантность извлечения, разнообразие запросов, временную недавность, междневную консолидацию и производное концептуальное богатство.
  * Продвижение заново читает живую ежедневную заметку перед записью в `MEMORY.md`, поэтому отредактированные или удаленные краткосрочные сниппеты не продвигаются из устаревших снимков recall-хранилища.
  * Запланированные и ручные запуски `memory promote` используют одни и те же значения фазы deep по умолчанию, если вы не передаете переопределения порогов CLI.
  * Автоматические запуски распределяются по настроенным рабочим пространствам памяти.


Расписание по умолчанию:

  * **Частота прохода** : `dreaming.frequency = 0 3 * * *`
  * **Пороги deep** : `minScore=0.8`, `minRecallCount=3`, `minUniqueQueries=3`, `recencyHalfLifeDays=14`, `maxAgeDays=30`


Пример:

jsonCopy code
[code]
    {  "plugins": {    "entries": {      "memory-core": {        "config": {          "dreaming": {            "enabled": true          }        }      }    }  }}
[/code]

Примечания:

  * `memory index --verbose` выводит сведения по фазам (поставщик, модель, источники, активность пакетов).
  * `memory status` включает любые дополнительные пути, настроенные через `memorySearch.extraPaths`.
  * Если фактически активные поля ключей удаленного API памяти настроены как SecretRefs, команда разрешает эти значения из активного снимка Gateway. Если Gateway недоступен, команда быстро завершается с ошибкой.
  * Примечание о несовпадении версий Gateway: этот путь команды требует Gateway с поддержкой `secrets.resolve`; более старые Gateway возвращают ошибку неизвестного метода.
  * Настраивайте частоту запланированного прохода с помощью `dreaming.frequency`. Политика продвижения deep в остальном является внутренней, кроме `dreaming.phases.deep.maxPromotedSnippetTokens`, который ограничивает длину продвигаемого сниппета, сохраняя видимой его provenance. Используйте флаги CLI в `memory promote`, когда нужны разовые ручные переопределения порогов.
  * `memory rem-harness --path <file-or-dir> --grounded` предварительно показывает grounded `What Happened`, `Reflections` и `Possible Lasting Updates` из исторических ежедневных заметок без записи чего-либо.
  * `memory rem-backfill --path <file-or-dir>` записывает обратимые grounded-записи дневника в `DREAMS.md` для просмотра в UI.
  * `memory rem-backfill --path <file-or-dir> --stage-short-term` также помещает grounded устойчивых кандидатов в живое краткосрочное хранилище продвижения, чтобы обычная фаза deep могла их ранжировать.
  * `memory rem-backfill --rollback` удаляет ранее записанные grounded-записи дневника, а `memory rem-backfill --rollback-short-term` удаляет ранее подготовленных grounded краткосрочных кандидатов.
  * См. [Dreaming](</ru/concepts/dreaming>) для полных описаний фаз и справочника по конфигурации.


## Связано

  * [Справочник CLI](</ru/cli>)
  * [Обзор памяти](</ru/concepts/memory>)


Was this useful?YesNo

Open issue