---
title: Получение данных из интернета
source_url: https://docs.openclaw.ai/ru/tools/web-fetch
scraped_at: 2026-06-29
---

CapabilitiesTools

Инструмент `web_fetch` выполняет обычный HTTP GET и извлекает читаемое содержимое (HTML в markdown или текст). Он **не** выполняет JavaScript.

Для сайтов, сильно зависящих от JS, или страниц, защищенных входом в систему, используйте [веб-браузер](</ru/tools/browser>).

## Быстрый старт

`web_fetch` **включен по умолчанию** \-- настройка не требуется. Агент может вызвать его сразу:

javascriptCopy code
[code]
    await web_fetch({ url: "https://example.com/article" });
[/code]

## Параметры инструмента

URL для получения. Только `http(s)`.

Формат вывода после извлечения основного содержимого.

Обрезать вывод до указанного количества символов.

## Как это работает

* ### Fetch

Отправляет HTTP GET с User-Agent, похожим на Chrome, и заголовком `Accept-Language`. Блокирует частные/внутренние имена хостов и повторно проверяет перенаправления.

* ### Extract

Запускает Readability (извлечение основного содержимого) для HTML-ответа.

* ### Fallback (optional)

Если Readability не срабатывает и выбран Firecrawl, повторяет попытку через API Firecrawl в режиме обхода ботов.

* ### Cache

Результаты кэшируются на 15 минут (настраивается), чтобы сократить повторные запросы к одному и тому же URL.

## Обновления хода выполнения

`web_fetch` выводит публичную строку хода выполнения только если получение все еще ожидает завершения через пять секунд:

textCopy code
[code]
    Fetching page content...
[/code]

Быстрые попадания в кэш и быстрые сетевые ответы завершаются до срабатывания таймера, поэтому строка хода выполнения для них не показывается. Если вызов отменен, таймер очищается. Когда получение в итоге завершается, агент получает обычный результат инструмента; строка хода выполнения является только состоянием UI канала и никогда не содержит полученное содержимое страницы.

## Конфигурация

json5Copy code
[code]
    {  tools: {    web: {      fetch: {        enabled: true, // default: true        provider: "firecrawl", // optional; omit for auto-detect        maxChars: 50000, // max output chars        maxCharsCap: 50000, // hard cap for maxChars param        maxResponseBytes: 2000000, // max download size before truncation        timeoutSeconds: 30,        cacheTtlMinutes: 15,        maxRedirects: 3,        useTrustedEnvProxy: false, // let a trusted HTTP(S) env proxy resolve DNS        readability: true, // use Readability extraction        userAgent: "Mozilla/5.0 ...", // override User-Agent        ssrfPolicy: {          allowRfc2544BenchmarkRange: true, // opt-in for trusted fake-IP proxies using 198.18.0.0/15          allowIpv6UniqueLocalRange: true, // opt-in for trusted fake-IP proxies using fc00::/7        },      },    },  },}
[/code]

## Резервный вариант Firecrawl

Если извлечение Readability не срабатывает, `web_fetch` может перейти на [Firecrawl](</ru/tools/firecrawl>) для обхода ботов и более качественного извлечения:

json5Copy code
[code]
    {  tools: {    web: {      fetch: {        provider: "firecrawl", // optional; omit for auto-detect from available credentials      },    },  },  plugins: {    entries: {      firecrawl: {        enabled: true,        config: {          webFetch: {            // apiKey: "fc-...", // optional; omit for keyless starter access            baseUrl: "https://api.firecrawl.dev",            onlyMainContent: true,            maxAgeMs: 86400000, // cache duration (1 day)            timeoutSeconds: 60,          },        },      },    },  },}
[/code]

`plugins.entries.firecrawl.config.webFetch.apiKey` необязателен и поддерживает объекты SecretRef. Устаревшая конфигурация `tools.web.fetch.firecrawl.*` автоматически мигрируется командой `openclaw doctor --fix`.

Текущее поведение runtime:

  * `tools.web.fetch.provider` явно выбирает резервного поставщика получения.
  * Если `provider` опущен, OpenClaw автоматически определяет первого готового поставщика web-fetch по настроенным учетным данным. Неизолированный `web_fetch` может использовать установленные плагины, которые объявляют `contracts.webFetchProviders` и регистрируют соответствующего поставщика во время выполнения. Официальный плагин Firecrawl предоставляет этот резервный вариант.
  * Изолированные вызовы `web_fetch` допускают встроенных поставщиков, а также установленных поставщиков, чье официальное происхождение из npm или ClawHub подтверждено. На сегодня это разрешает официальный плагин Firecrawl; сторонние внешние плагины получения остаются исключенными.
  * Если Readability отключен, `web_fetch` сразу переходит к выбранному резервному поставщику. Если поставщик недоступен, он завершается закрытым отказом.


## Доверенный env-прокси

Если вашему развертыванию требуется, чтобы `web_fetch` проходил через доверенный исходящий HTTP(S)-прокси, установите `tools.web.fetch.useTrustedEnvProxy: true`.

В этом режиме OpenClaw по-прежнему применяет проверки SSRF на основе имени хоста перед отправкой запроса, но позволяет прокси разрешать DNS вместо локального DNS pinning. Включайте это только когда прокси контролируется оператором и обеспечивает исходящую политику после разрешения DNS.

## Ограничения и безопасность

  * `maxChars` ограничивается значением `tools.web.fetch.maxCharsCap`
  * Тело ответа ограничивается `maxResponseBytes` перед разбором; слишком большие ответы обрезаются с предупреждением
  * Частные/внутренние имена хостов блокируются
  * `tools.web.fetch.ssrfPolicy.allowRfc2544BenchmarkRange` и `tools.web.fetch.ssrfPolicy.allowIpv6UniqueLocalRange` являются узкими opt-in для доверенных стеков прокси с поддельными IP; оставьте их неустановленными, если ваш прокси не владеет этими синтетическими диапазонами и не обеспечивает собственную политику назначения
  * Перенаправления проверяются и ограничиваются `maxRedirects`
  * `useTrustedEnvProxy` является явным opt-in и должен включаться только для контролируемых оператором прокси, которые все равно обеспечивают исходящую политику после разрешения DNS
  * `web_fetch` работает по принципу best-effort -- некоторым сайтам нужен [веб-браузер](</ru/tools/browser>)


## Профили инструментов

Если вы используете профили инструментов или списки разрешений, добавьте `web_fetch` или `group:web`:

json5Copy code
[code]
    {  tools: {    allow: ["web_fetch"],    // or: allow: ["group:web"]  (includes web_fetch, web_search, and x_search)  },}
[/code]

## Связанные материалы

  * [Веб-поиск](</ru/tools/web>) \-- поиск в интернете через нескольких поставщиков
  * [Веб-браузер](</ru/tools/browser>) \-- полноценная автоматизация браузера для сайтов, сильно зависящих от JS
  * [Firecrawl](</ru/tools/firecrawl>) \-- инструменты поиска и скрейпинга Firecrawl


Was this useful?YesNo

Open issue