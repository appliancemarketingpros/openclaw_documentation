---
title: Документация
source_url: https://docs.openclaw.ai/ru/cli/docs
scraped_at: 2026-06-29
---

ReferenceCLI commands

# `openclaw docs`

Ищите в актуальном индексе документации OpenClaw из терминала. Команда вызывает размещенный в Cloudflare API поиска по документации OpenClaw и выводит результаты в вашем терминале.

## Использование

bashCopy code
[code]
    openclaw docs                       # print docs entrypoint and example searchopenclaw docs <query...>            # search the live docs index
[/code]

Аргументы:

Аргумент | Описание  
---|---  
`[query...]` | Поисковый запрос в свободной форме. Запросы из нескольких слов объединяются пробелами и отправляются как один.  
  
## Примеры

bashCopy code
[code]
    openclaw docs browser existing-sessionopenclaw docs sandbox allowHostControlopenclaw docs gateway token secretref
[/code]

Без запроса `openclaw docs` выводит URL точки входа документации и пример команды поиска вместо выполнения поиска.

## Как это работает

`openclaw docs` вызывает `https://docs.openclaw.ai/api/search` и отображает результаты JSON. Вызов поиска использует фиксированный тайм-аут 30 секунд.

## Вывод

В терминале с расширенным выводом (TTY) результаты отображаются как заголовок, за которым следует маркированный список. Каждый пункт показывает заголовок страницы, ссылку на URL документации и короткий фрагмент на следующей строке. При пустых результатах выводится «Нет результатов.».

В обычном выводе (канал, `--no-color`, скрипты) те же данные отображаются как Markdown:

markdownCopy code
[code]
    # Docs search: <query> - [Title](https://docs.openclaw.ai/...) - snippet- [Title](https://docs.openclaw.ai/...) - snippet
[/code]

## Коды выхода

Код | Значение  
---|---  
`0` | Поиск выполнен успешно (включая ответы с нулевым количеством результатов).  
`1` | Вызов размещенного API поиска по документации завершился ошибкой; stderr выводится inline.  
  
## Связанные материалы

  * [Справочник CLI](</ru/cli>)
  * [Актуальная документация](<https://docs.openclaw.ai>)


Was this useful?YesNo

Open issue