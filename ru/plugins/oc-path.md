---
title: Plugin OC Path
source_url: https://docs.openclaw.ai/ru/plugins/oc-path
scraped_at: 2026-06-29
---

CapabilitiesBundled plugin guides

Встроенный Plugin `oc-path` добавляет CLI [`openclaw path`](</ru/cli/path>) для схемы адресации файлов рабочей области `oc://`. Он поставляется в репозитории OpenClaw в `extensions/oc-path/`, но включается явно — установка/сборка оставляет его бездействующим, пока вы его не включите.

Адреса `oc://` указывают на один листовой узел (или набор листовых узлов по wildcard) внутри файла рабочей области. Сегодня Plugin понимает четыре вида файлов:

  * **markdown** (`.md`, `.mdx`): frontmatter, разделы, элементы, поля
  * **jsonc** (`.jsonc`, `.json5`, `.json`): комментарии и форматирование сохраняются
  * **jsonl** (`.jsonl`, `.ndjson`): построчные записи
  * **yaml** (`.yaml`, `.yml`, `.lobster`): узлы map/sequence/scalar через API документа YAML


Self-hosters и расширения редакторов используют CLI, чтобы читать или записывать один листовой узел без прямого скриптинга через SDK; агенты и hooks рассматривают его как детерминированную основу, чтобы round-trip с точностью до байта и защита sentinel редактирования применялись единообразно для всех видов.

## Зачем включать

Включайте `oc-path`, когда хотите, чтобы скрипты, hooks или локальные агентские инструменты указывали на точную часть состояния рабочей области без изобретения парсера для каждой структуры файла. Один адрес `oc://` может обозначать ключ frontmatter в Markdown, элемент раздела, лист конфигурации JSONC, поле события JSONL или шаг workflow YAML.

Это важно для рабочих процессов maintainers, где изменение должно быть небольшим, проверяемым и повторяемым: просмотреть одно значение, найти совпадающие записи, выполнить dry-run записи, а затем применить только этот листовой узел, не трогая комментарии, окончания строк и соседнее форматирование. То, что это opt-in Plugin, дает опытным пользователям основу адресации без добавления зависимостей парсеров или поверхности CLI в core для установок, которым это никогда не нужно.

Частые причины включить его:

  * **Локальная автоматизация** : shell-скрипты могут разрешать или обновлять одно значение рабочей области с `openclaw path … --json` вместо поддержки отдельного кода парсинга Markdown, JSONC, JSONL и YAML.
  * **Правки, видимые агенту** : агент может показать dry-run diff для одного адресованного листового узла перед записью, что проще проверять, чем свободную перезапись файла.
  * **Интеграции редакторов** : редактор может сопоставить `oc://AGENTS.md/tools/gh` с точным узлом Markdown и номером строки без угадывания по тексту заголовка.
  * **Диагностика** : `emit` прогоняет файл через парсер и emitter, чтобы проверить, остается ли вид файла стабильным по байтам перед использованием автоматических правок.


Конкретные примеры:

bashCopy code
[code]
    # Is the GitHub plugin enabled in this config?openclaw path resolve 'oc://config.jsonc/plugins/github/enabled' --json # Which tool-call names appear in this session log?openclaw path find 'oc://session.jsonl/[event=tool_call]/name' --json # What bytes would this tiny config edit write?openclaw path set 'oc://config.jsonc/plugins/github/enabled' 'true' --dry-run
[/code]

Plugin намеренно не владеет семантикой более высокого уровня. Memory plugins по-прежнему владеют записями памяти, команды config по-прежнему владеют полным управлением конфигурацией, а логика LKG по-прежнему владеет восстановлением/продвижением. `oc-path` — это узкий слой адресации и файловых операций с сохранением байтов, вокруг которого такие инструменты более высокого уровня могут строиться.

## Где он работает

Plugin работает **внутри процесса CLI`openclaw`** на хосте, где вы вызываете команду. Ему не нужен запущенный Gateway, и он не открывает сетевые сокеты — каждый глагол является чистым преобразованием файла, на который вы указываете.

Метаданные Plugin находятся в `extensions/oc-path/openclaw.plugin.json`:

jsonCopy code
[code]
    {  "id": "oc-path",  "name": "OC Path",  "activation": {    "onStartup": false,    "onCommands": ["path"]  },  "commandAliases": [{ "name": "path", "kind": "cli" }]}
[/code]

`onStartup: false` не допускает Plugin в горячий путь Gateway. `onCommands: ["path"]` сообщает CLI, что Plugin нужно лениво загрузить при первом запуске `openclaw path …`, поэтому установки, которые никогда не используют этот глагол, не платят никакой цены.

## Включение

bashCopy code
[code]
    openclaw plugins enable oc-path
[/code]

Перезапустите Gateway (если вы его запускаете), чтобы snapshot манифеста получил новое состояние. Простые вызовы `openclaw path` начинают работать сразу на том же хосте — CLI загружает Plugin по требованию.

Отключение:

bashCopy code
[code]
    openclaw plugins disable oc-path
[/code]

## Зависимости

Все зависимости парсеров локальны для Plugin — включение `oc-path` не добавляет новые пакеты в runtime core:

Зависимость | Назначение  
---|---  
`commander` | Связка подкоманд для `resolve`, `find`, `set`, `validate`, `emit`.  
`jsonc-parser` | Парсинг JSONC + правки листовых узлов с сохранением комментариев и trailing commas.  
`markdown-it` | Токенизация Markdown для модели section / item / field.  
`yaml` | Парсинг / emit / правка `Document` YAML с сохранением комментариев и flow style.  
  
JSONL остается реализованным вручную — построчный парсинг проще любой зависимости, а построчный парсинг JSONC уже проходит через `jsonc-parser`.

## Что он предоставляет

Поверхность | Предоставляется  
---|---  
CLI `openclaw path` | `extensions/oc-path/cli-registration.ts`  
Парсер / formatter `oc://` | `extensions/oc-path/src/oc-path/oc-path.ts`  
Парсинг / emit / правка по видам | `extensions/oc-path/src/oc-path/{md,jsonc,jsonl,yaml}`  
Универсальные resolve / find / set | `extensions/oc-path/src/oc-path/{resolve,find,edit}.ts`  
Защита redaction-sentinel | `extensions/oc-path/src/oc-path/sentinel.ts`  
  
CLI сегодня является единственной публичной поверхностью. Глаголы основы приватны для Plugin; потребители используют CLI (или создают собственный Plugin на базе SDK).

## Связь с другими plugins

  * **`memory-*`** : записи памяти проходят через memory plugins, а не через `oc-path`. `oc-path` — универсальная файловая основа; memory plugins накладывают сверху собственную семантику.
  * **LKG** : `path` не знает о восстановлении Last-Known-Good конфигурации. Если файл отслеживается LKG, следующий вызов `observe` решает, продвигать или восстанавливать; `set --batch` для атомарного multi-set через жизненный цикл promote/recover LKG планируется вместе с основой LKG-recovery.


## Безопасность

`set` записывает сырые байты через путь emit основы, который автоматически применяет защиту redaction-sentinel. Листовой узел, содержащий `__OPENCLAW_REDACTED__` (буквально или как подстроку), отклоняется во время записи с `OC_EMIT_SENTINEL`. CLI также очищает буквальный sentinel из любого человеко-читаемого или JSON-вывода, который печатает, заменяя его на `[REDACTED]`, чтобы terminal captures и pipelines никогда не утекали маркер.

## См. также

  * [Справочник CLI `openclaw path`](</ru/cli/path>)
  * [Управление plugins](</ru/plugins/manage-plugins>)
  * [Создание plugins](</ru/plugins/building-plugins>)


Was this useful?YesNo

Open issue