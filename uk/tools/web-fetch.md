---
title: Отримання з вебу
source_url: https://docs.openclaw.ai/uk/tools/web-fetch
scraped_at: 2026-05-25
---

Інструмент `web_fetch` виконує звичайний HTTP GET і витягує читабельний вміст (HTML у markdown або текст). Він **не** виконує JavaScript.

Для сайтів із великою кількістю JS або сторінок, захищених входом, натомість використовуйте [веббраузер](</uk/tools/browser>).

## Швидкий старт

`web_fetch` **увімкнено за замовчуванням** \-- конфігурація не потрібна. Агент може викликати його одразу:

javascriptCopy code
[code]
    await web_fetch({ url: "https://example.com/article" });
[/code]

## Параметри інструмента

URL для отримання. Лише `http(s)`.

Формат виводу після витягування основного вмісту.

Обрізати вивід до цієї кількості символів.

## Як це працює

* ### Fetch

Надсилає HTTP GET із Chrome-подібним User-Agent і заголовком `Accept-Language`. Блокує приватні/внутрішні імена хостів і повторно перевіряє перенаправлення.

* ### Extract

Запускає Readability (витягування основного вмісту) для HTML-відповіді.

* ### Fallback (optional)

Якщо Readability не спрацьовує і Firecrawl налаштовано, повторює спробу через Firecrawl API в режимі обходу бот-захисту.

* ### Cache

Результати кешуються на 15 хвилин (налаштовується), щоб зменшити повторні отримання того самого URL.

## Конфігурація

json5Copy code
[code]
    {  tools: {    web: {      fetch: {        enabled: true, // default: true        provider: "firecrawl", // optional; omit for auto-detect        maxChars: 50000, // max output chars        maxCharsCap: 50000, // hard cap for maxChars param        maxResponseBytes: 2000000, // max download size before truncation        timeoutSeconds: 30,        cacheTtlMinutes: 15,        maxRedirects: 3,        useTrustedEnvProxy: false, // let a trusted HTTP(S) env proxy resolve DNS        readability: true, // use Readability extraction        userAgent: "Mozilla/5.0 ...", // override User-Agent        ssrfPolicy: {          allowRfc2544BenchmarkRange: true, // opt-in for trusted fake-IP proxies using 198.18.0.0/15          allowIpv6UniqueLocalRange: true, // opt-in for trusted fake-IP proxies using fc00::/7        },      },    },  },}
[/code]

## Резервний варіант Firecrawl

Якщо витягування Readability не спрацьовує, `web_fetch` може перейти на [Firecrawl](</uk/tools/firecrawl>) для обходу бот-захисту та кращого витягування:

json5Copy code
[code]
    {  tools: {    web: {      fetch: {        provider: "firecrawl", // optional; omit for auto-detect from available credentials      },    },  },  plugins: {    entries: {      firecrawl: {        enabled: true,        config: {          webFetch: {            apiKey: "fc-...", // optional if FIRECRAWL_API_KEY is set            baseUrl: "https://api.firecrawl.dev",            onlyMainContent: true,            maxAgeMs: 86400000, // cache duration (1 day)            timeoutSeconds: 60,          },        },      },    },  },}
[/code]

`plugins.entries.firecrawl.config.webFetch.apiKey` підтримує об’єкти SecretRef. Застаріла конфігурація `tools.web.fetch.firecrawl.*` автоматично мігрується через `openclaw doctor --fix`.

Поточна поведінка під час виконання:

  * `tools.web.fetch.provider` явно вибирає резервного провайдера отримання.
  * Якщо `provider` пропущено, OpenClaw автоматично визначає першого готового провайдера web-fetch із доступних облікових даних. `web_fetch` без sandbox може використовувати встановлені plugins, які оголошують `contracts.webFetchProviders` і реєструють відповідного провайдера під час виконання. Наразі вбудований провайдер -- Firecrawl.
  * Виклики `web_fetch` у sandbox лишаються обмеженими вбудованими провайдерами.
  * Якщо Readability вимкнено, `web_fetch` одразу переходить до вибраного резервного провайдера. Якщо жоден провайдер недоступний, він завершується закритою відмовою.


## Довірений env-проксі

Якщо ваше розгортання вимагає, щоб `web_fetch` проходив через довірений вихідний HTTP(S)-проксі, задайте `tools.web.fetch.useTrustedEnvProxy: true`.

У цьому режимі OpenClaw все одно застосовує перевірки SSRF на основі імені хоста перед надсиланням запиту, але дозволяє проксі розв’язувати DNS замість локального DNS-пінінгу. Вмикайте це лише тоді, коли проксі контролюється оператором і застосовує вихідну політику після розв’язання DNS.

## Обмеження та безпека

  * `maxChars` обмежується до `tools.web.fetch.maxCharsCap`
  * Тіло відповіді обмежується `maxResponseBytes` перед розбором; завеликі відповіді обрізаються з попередженням
  * Приватні/внутрішні імена хостів блокуються
  * `tools.web.fetch.ssrfPolicy.allowRfc2544BenchmarkRange` і `tools.web.fetch.ssrfPolicy.allowIpv6UniqueLocalRange` \-- це вузькі opt-in для довірених стеків проксі з підробленими IP; не встановлюйте їх, якщо ваш проксі не володіє цими синтетичними діапазонами й не застосовує власну політику призначення
  * Перенаправлення перевіряються й обмежуються `maxRedirects`
  * `useTrustedEnvProxy` є явним opt-in і має вмикатися лише для контрольованих оператором проксі, які все ще застосовують вихідну політику після розв’язання DNS
  * `web_fetch` працює за принципом найкращої спроби -- для деяких сайтів потрібен [веббраузер](</uk/tools/browser>)


## Профілі інструментів

Якщо ви використовуєте профілі інструментів або allowlist-и, додайте `web_fetch` або `group:web`:

json5Copy code
[code]
    {  tools: {    allow: ["web_fetch"],    // or: allow: ["group:web"]  (includes web_fetch, web_search, and x_search)  },}
[/code]

## Пов’язане

  * [Вебпошук](</uk/tools/web>) \-- пошук в інтернеті через кількох провайдерів
  * [Веббраузер](</uk/tools/browser>) \-- повна автоматизація браузера для сайтів із великою кількістю JS
  * [Firecrawl](</uk/tools/firecrawl>) \-- інструменти пошуку та scraping Firecrawl


Was this useful?YesNo