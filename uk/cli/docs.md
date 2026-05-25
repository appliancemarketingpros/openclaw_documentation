---
title: Документація
source_url: https://docs.openclaw.ai/uk/cli/docs
scraped_at: 2026-05-25
---

# `openclaw docs`

Шукайте в живому індексі документації OpenClaw з термінала. Команда викликає публічну розміщену на Mintlify кінцеву точку пошуку MCP для документації за адресою `https://docs.openclaw.ai/mcp.SearchOpenClaw` і відображає результати у вашому терміналі.

## Використання

bashCopy code
[code]
    openclaw docs                       # print docs entrypoint and example searchopenclaw docs <query...>            # search the live docs index
[/code]

Аргументи:

Аргумент | Опис  
---|---  
`[query...]` | Пошуковий запит у довільній формі. Запити з кількох слів об’єднуються пробілами й надсилаються як один.  
  
## Приклади

bashCopy code
[code]
    openclaw docs browser existing-sessionopenclaw docs sandbox allowHostControlopenclaw docs gateway token secretref
[/code]

Без запиту `openclaw docs` виводить URL точки входу документації та приклад команди пошуку замість запуску пошуку.

## Як це працює

`openclaw docs` викликає CLI `mcporter`, щоб звернутися до інструмента пошуку документації MCP, а потім розбирає блоки `Title: / Link: / Content:` з виводу інструмента в список результатів.

Щоб знайти `mcporter`, OpenClaw перевіряє по черзі:

  1. `mcporter` у `PATH` (використовується напряму, якщо доступний).
  2. `pnpm dlx mcporter ...`, якщо встановлено `pnpm`.
  3. `npx -y mcporter ...`, якщо встановлено `npx`.


Якщо жоден варіант недоступний, команда завершується з помилкою та підказкою встановити `pnpm` (`npm install -g pnpm`).

Пошуковий виклик використовує фіксований тайм-аут 30 секунд. Фрагменти результатів обрізаються приблизно до 220 символів на запис.

## Вивід

У розширеному терміналі (TTY) результати відображаються як заголовок, за яким іде маркований список. Кожен пункт показує заголовок сторінки, пов’язаний URL документації і короткий фрагмент у наступному рядку. Порожні результати виводять «Немає результатів.».

У нерозширеному виводі (через канал, `--no-color`, скрипти) ті самі дані відображаються як Markdown:

markdownCopy code
[code]
    # Docs search: <query> - [Title](https://docs.openclaw.ai/...) - snippet- [Title](https://docs.openclaw.ai/...) - snippet
[/code]

## Коди виходу

Код | Значення  
---|---  
`0` | Пошук успішний (зокрема відповіді з нульовими результатами).  
`1` | Виклик інструмента MCP завершився помилкою; stderr друкується вбудовано.  
  
## Пов’язане

  * [Довідник CLI](</uk/cli>)
  * [Жива документація](<https://docs.openclaw.ai>)


Was this useful?YesNo