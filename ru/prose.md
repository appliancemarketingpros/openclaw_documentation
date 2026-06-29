---
title: OpenProse
source_url: https://docs.openclaw.ai/ru/prose
scraped_at: 2026-06-29
---

CapabilitiesSkills

OpenProse — это переносимый, ориентированный на Markdown формат рабочих процессов для оркестрации AI-сеансов. В OpenClaw он поставляется как плагин, который устанавливает набор Skills OpenProse и слеш-команду `/prose`. Программы находятся в файлах `.prose` и могут запускать несколько субагентов с явным потоком управления.

**Установка** Включите плагин OpenProse и перезапустите Gateway. **Запуск программы** Используйте `/prose run`, чтобы выполнить файл `.prose` или удаленную программу. **Написание программ** Создавайте многоагентные рабочие процессы с параллельными и последовательными шагами.

## Установка

* ### Включите плагин

Встроенные плагины по умолчанию отключены. Включите OpenProse:

bashCopy code
[code]
    openclaw plugins enable open-prose
[/code]

* ### Перезапустите Gateway

bashCopy code
[code]
    openclaw gateway restart
[/code]

* ### Проверьте

bashCopy code
[code]
    openclaw plugins list | grep prose
[/code]

Вы должны увидеть `open-prose` в статусе включенного. Команда Skills `/prose` теперь доступна в чате.

Для локального checkout: `openclaw plugins install ./path/to/local/open-prose-plugin`

## Слеш-команда

OpenProse регистрирует `/prose` как вызываемую пользователем команду Skills:

textCopy code
[code]
    /prose help/prose run <file.prose>/prose run <handle/slug>/prose run <https://example.com/file.prose>/prose compile <file.prose>/prose examples/prose update
[/code]

`/prose run <handle/slug>` разрешается в `https://p.prose.md/<handle>/<slug>`. Прямые URL загружаются как есть с помощью инструмента `web_fetch`.

Удаленные запуски верхнего уровня выполняются явно. Удаленные импорты внутри программы `.prose` являются транзитивными зависимостями кода: прежде чем OpenProse загрузит любую удаленную цель `use`, он показывает разрешенный список импортов и требует, чтобы оператор ответил точно `approve remote prose imports` для этого запуска.

## Что он может делать

  * Многоагентные исследования и синтез с явным параллелизмом.
  * Повторяемые рабочие процессы с безопасными подтверждениями (ревью кода, триаж инцидентов, контентные конвейеры).
  * Переиспользуемые программы `.prose`, которые можно запускать в поддерживаемых средах выполнения агентов.


## Пример: параллельное исследование и синтез

proseCopy code
[code]
    # Research + synthesis with two agents running in parallel. input topic: "What should we research?" agent researcher:  model: sonnet  prompt: "You research thoroughly and cite sources." agent writer:  model: opus  prompt: "You write a concise summary." parallel:  findings = session: researcher    prompt: "Research {topic}."  draft = session: writer    prompt: "Summarize {topic}." session "Merge the findings + draft into a final answer."context: { findings, draft }
[/code]

## Сопоставление со средой выполнения OpenClaw

Программы OpenProse сопоставляются с примитивами OpenClaw:

Концепция OpenProse | Инструмент OpenClaw  
---|---  
Spawn session / Task tool | `sessions_spawn`  
File read / write | `read` / `write`  
Web fetch | `web_fetch`  
  
## Расположения файлов

OpenProse хранит состояние в `.prose/` в вашем workspace:

textCopy code
[code]
    .prose/├── .env├── runs/│   └── {YYYYMMDD}-{HHMMSS}-{random}/│       ├── program.prose│       ├── state.md│       ├── bindings/│       └── agents/└── agents/
[/code]

Постоянные агенты уровня пользователя находятся в:

textCopy code
[code]
    ~/.prose/agents/
[/code]

## Бэкенды состояния

файловая система (по умолчанию)

Состояние записывается в `.prose/runs/...` в workspace. Дополнительные зависимости не требуются.

в контексте

Временное состояние хранится в окне контекста. Подходит для небольших, короткоживущих программ.

sqlite (экспериментально)

Требуется бинарный файл `sqlite3` в `PATH`.

postgres (экспериментально)

Требуются `psql` и строка подключения.

## Безопасность

Относитесь к файлам `.prose` как к коду. Проверяйте их перед запуском, включая удаленные импорты `use`. Запросы верхнего уровня `/prose run https://...` выполняются явно, но транзитивные удаленные импорты требуют подтверждения для каждого запуска перед загрузкой или выполнением. Используйте allowlist инструментов OpenClaw и шлюзы подтверждения для контроля побочных эффектов. Для детерминированных рабочих процессов с подтверждениями сравните с [Lobster](</ru/tools/lobster>).

## См. также

[**Справочник Skills** Как загружается набор Skills OpenProse и какие шлюзы применяются. ](</ru/tools/skills>) [**Субагенты** Нативный слой многоагентной координации OpenClaw. ](</ru/tools/subagents>) [**Преобразование текста в речь** Добавьте аудиовывод в свои рабочие процессы. ](</ru/tools/tts>) [**Слеш-команды** Все доступные команды чата, включая /prose. ](</ru/tools/slash-commands>)

Официальный сайт: <https://www.prose.md>

Was this useful?YesNo

Open issue