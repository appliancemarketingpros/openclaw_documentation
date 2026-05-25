---
title: Стан
source_url: https://docs.openclaw.ai/uk/cli/health
scraped_at: 2026-05-25
---

# `openclaw health`

Отримати стан запущеного Gateway.

## Опції

Прапорець | Типово | Опис  
---|---|---  
`--json` | `false` | Вивести машинно-читаний JSON замість тексту.  
`--timeout <ms>` | `10000` | Тайм-аут з'єднання в мілісекундах.  
`--verbose` | `false` | Докладне журналювання. Примусово виконує живу перевірку й розгортає вивід для кожного агента.  
`--debug` | `false` | Псевдонім для `--verbose`.  
  
Приклади:

bashCopy code
[code]
    openclaw healthopenclaw health --jsonopenclaw health --timeout 2500openclaw health --verboseopenclaw health --debug
[/code]

Примітки:

  * Типовий `openclaw health` запитує у запущеного Gateway його знімок стану. Коли Gateway уже має свіжий кешований знімок, він може повернути це кешоване корисне навантаження та оновитися у фоновому режимі.
  * `--verbose` примусово виконує живу перевірку, друкує відомості про з'єднання Gateway і розгортає людиночитний вивід для всіх налаштованих облікових записів і агентів.
  * Вивід містить сховища сеансів для кожного агента, коли налаштовано кілька агентів.


## Пов'язане

  * [Довідник CLI](</uk/cli>)
  * [Стан Gateway](</uk/gateway/health>)


Was this useful?YesNo