---
title: Браузер
source_url: https://docs.openclaw.ai/uk/cli/browser
scraped_at: 2026-05-25
---

# `openclaw browser`

Керуйте поверхнею керування браузером OpenClaw і виконуйте дії браузера (життєвий цикл, профілі, вкладки, знімки, скриншоти, навігація, введення, емуляція стану та налагодження).

Пов’язане:

  * Інструмент Browser + API: [інструмент Browser](</uk/tools/browser>)


## Поширені прапорці

  * `--url <gatewayWsUrl>`: URL WebSocket Gateway (типово з конфігурації).
  * `--token <token>`: токен Gateway (за потреби).
  * `--timeout <ms>`: тайм-аут запиту (мс).
  * `--expect-final`: чекати на фінальну відповідь Gateway.
  * `--browser-profile <name>`: вибрати профіль браузера (типовий — із конфігурації).
  * `--json`: машиночитаний вивід (де підтримується).


## Швидкий старт (локально)

bashCopy code
[code]
    openclaw browser profilesopenclaw browser --browser-profile openclaw startopenclaw browser --browser-profile openclaw open https://example.comopenclaw browser --browser-profile openclaw snapshot
[/code]

Агенти можуть виконати ту саму перевірку готовності за допомогою `browser({ action: "doctor" })`.

## Швидке усунення несправностей

Якщо `start` завершується помилкою `not reachable after start`, спочатку усуньте проблему з готовністю CDP. Якщо `start` і `tabs` успішні, але `open` або `navigate` завершується помилкою, площина керування браузером справна, а причина збою зазвичай полягає в політиці SSRF для навігації.

Мінімальна послідовність:

bashCopy code
[code]
    openclaw browser --browser-profile openclaw doctoropenclaw browser --browser-profile openclaw startopenclaw browser --browser-profile openclaw tabsopenclaw browser --browser-profile openclaw open https://example.com
[/code]

Детальні вказівки: [усунення несправностей Browser](</uk/tools/browser#cdp-startup-failure-vs-navigation-ssrf-block>)

## Життєвий цикл

bashCopy code
[code]
    openclaw browser statusopenclaw browser doctoropenclaw browser doctor --deepopenclaw browser startopenclaw browser start --headlessopenclaw browser stopopenclaw browser --browser-profile openclaw reset-profile
[/code]

Примітки:

  * `doctor --deep` додає перевірку живого знімка. Це корисно, коли базова готовність CDP позначена як справна, але вам потрібне підтвердження, що поточну вкладку можна інспектувати.
  * Для профілів `attachOnly` і віддалених профілів CDP команда `openclaw browser stop` закриває активну сесію керування та скидає тимчасові перевизначення емуляції, навіть якщо OpenClaw не запускав процес браузера самостійно.
  * Для локальних керованих профілів `openclaw browser stop` зупиняє запущений процес браузера.
  * `openclaw browser start --headless` застосовується лише до цього запиту запуску й лише тоді, коли OpenClaw запускає локальний керований браузер. Це не переписує `browser.headless` або конфігурацію профілю й не має ефекту для браузера, який уже працює.
  * На Linux-хостах без `DISPLAY` або `WAYLAND_DISPLAY` локальні керовані профілі автоматично працюють у режимі headless, якщо лише `OPENCLAW_BROWSER_HEADLESS=0`, `browser.headless=false` або `browser.profiles.<name>.headless=false` явно не вимагає видимого браузера.


## Якщо команда відсутня

Якщо `openclaw browser` є невідомою командою, перевірте `plugins.allow` у `~/.openclaw/openclaw.json`.

Коли `plugins.allow` присутній, явно перелічіть вбудований плагін браузера, якщо лише конфігурація вже не містить кореневий блок `browser`:

json5Copy code
[code]
    {  plugins: {    allow: ["telegram", "browser"],  },}
[/code]

Явний кореневий блок `browser`, наприклад `browser.enabled=true` або `browser.profiles.<name>`, також активує вбудований плагін браузера за обмежувального allowlist плагінів.

Пов’язане: [інструмент Browser](</uk/tools/browser#missing-browser-command-or-tool>)

## Профілі

Профілі — це іменовані конфігурації маршрутизації браузера. На практиці:

  * `openclaw`: запускає або під’єднується до окремого екземпляра Chrome, керованого OpenClaw (ізольований каталог даних користувача).
  * `user`: керує вашою наявною сесією Chrome із виконаним входом через Chrome DevTools MCP.
  * спеціальні профілі CDP: вказують на локальну або віддалену кінцеву точку CDP.

bashCopy code
[code]
    openclaw browser profilesopenclaw browser create-profile --name work --color "#FF5A36"openclaw browser create-profile --name chrome-live --driver existing-sessionopenclaw browser create-profile --name remote --cdp-url https://browser-host.example.comopenclaw browser delete-profile --name work
[/code]

Використати конкретний профіль:

bashCopy code
[code]
    openclaw browser --browser-profile work tabs
[/code]

## Вкладки

bashCopy code
[code]
    openclaw browser tabsopenclaw browser tab new --label docsopenclaw browser tab label t1 docsopenclaw browser tab select 2openclaw browser tab close 2openclaw browser open https://docs.openclaw.ai --label docsopenclaw browser focus docsopenclaw browser close t1
[/code]

`tabs` спочатку повертає `suggestedTargetId`, потім стабільний `tabId`, наприклад `t1`, необов’язкову мітку та сирий `targetId`. Агенти мають передавати `suggestedTargetId` назад у `focus`, `close`, знімки та дії. Ви можете призначити мітку за допомогою `open --label`, `tab new --label` або `tab label`; мітки, ідентифікатори вкладок, сирі ідентифікатори цілей і унікальні префікси target-id — усе це приймається. Коли Chromium замінює базову сиру ціль під час навігації або надсилання форми, OpenClaw зберігає стабільний `tabId`/мітку прив’язаними до вкладки-замінника, коли може довести збіг. Сирі ідентифікатори цілей залишаються нестабільними; віддавайте перевагу `suggestedTargetId`.

## Знімок / скриншот / дії

Знімок:

bashCopy code
[code]
    openclaw browser snapshotopenclaw browser snapshot --urls
[/code]

Скриншот:

bashCopy code
[code]
    openclaw browser screenshotopenclaw browser screenshot --full-pageopenclaw browser screenshot --ref e12openclaw browser screenshot --labels
[/code]

Примітки:

  * `--full-page` призначений лише для захоплення сторінок; його не можна поєднувати з `--ref` або `--element`.
  * Профілі `existing-session` / `user` підтримують скриншоти сторінок і скриншоти `--ref` з виводу знімка, але не скриншоти CSS `--element`.
  * `--labels` накладає поточні посилання знімка на скриншот.
  * `snapshot --urls` додає виявлені адреси посилань до AI-знімків, щоб агенти могли вибирати прямі цілі навігації замість того, щоб вгадувати лише за текстом посилання.


Navigate/click/type (автоматизація UI на основі ref):

bashCopy code
[code]
    openclaw browser navigate https://example.comopenclaw browser click <ref>openclaw browser click-coords 120 340openclaw browser type <ref> "hello"openclaw browser press Enteropenclaw browser hover <ref>openclaw browser scrollintoview <ref>openclaw browser drag <startRef> <endRef>openclaw browser select <ref> OptionA OptionBopenclaw browser fill --fields '[{"ref":"1","value":"Ada"}]'openclaw browser wait --text "Done"openclaw browser evaluate --fn '(el) => el.textContent' --ref <ref>
[/code]

Відповіді дій повертають поточний сирий `targetId` після заміни сторінки, спричиненої дією, коли OpenClaw може довести вкладку-замінник. Скрипти все одно мають зберігати й передавати `suggestedTargetId`/мітки для довготривалих робочих процесів.

Допоміжні команди для файлів і діалогів:

bashCopy code
[code]
    openclaw browser upload /tmp/openclaw/uploads/file.pdf --ref <ref>openclaw browser waitfordownloadopenclaw browser download <ref> report.pdfopenclaw browser dialog --accept
[/code]

Керовані профілі Chrome зберігають звичайні завантаження, ініційовані кліком, до каталогу завантажень OpenClaw (типово `/tmp/openclaw/downloads` або налаштований тимчасовий корінь). Використовуйте `waitfordownload` або `download`, коли агенту потрібно дочекатися певного файлу та повернути його шлях; ці явні очікувачі беруть на себе наступне завантаження.

## Стан і сховище

Viewport + емуляція:

bashCopy code
[code]
    openclaw browser resize 1280 720openclaw browser set viewport 1280 720openclaw browser set offline onopenclaw browser set media darkopenclaw browser set timezone Europe/Londonopenclaw browser set locale en-GBopenclaw browser set geo 51.5074 -0.1278 --accuracy 25openclaw browser set device "iPhone 14"openclaw browser set headers '{"x-test":"1"}'openclaw browser set credentials myuser mypass
[/code]

Cookies + сховище:

bashCopy code
[code]
    openclaw browser cookiesopenclaw browser cookies set session abc123 --url https://example.comopenclaw browser cookies clearopenclaw browser storage local getopenclaw browser storage local set token abc123openclaw browser storage session clear
[/code]

## Налагодження

bashCopy code
[code]
    openclaw browser console --level erroropenclaw browser pdfopenclaw browser responsebody "**/api"openclaw browser highlight <ref>openclaw browser errors --clearopenclaw browser requests --filter apiopenclaw browser trace startopenclaw browser trace stop --out trace.zip
[/code]

## Наявний Chrome через MCP

Використовуйте вбудований профіль `user` або створіть власний профіль `existing-session`:

bashCopy code
[code]
    openclaw browser --browser-profile user tabsopenclaw browser create-profile --name chrome-live --driver existing-sessionopenclaw browser create-profile --name brave-live --driver existing-session --user-data-dir "~/Library/Application Support/BraveSoftware/Brave-Browser"openclaw browser --browser-profile chrome-live tabs
[/code]

Цей шлях працює лише на хості. Для Docker, headless-серверів, Browserless або інших віддалених конфігурацій використовуйте профіль CDP.

Поточні обмеження existing-session:

  * дії на основі знімків використовують ref, а не CSS-селектори
  * `browser.actionTimeoutMs` встановлює для підтримуваних запитів `act` типове значення 60000 мс, коли виклики не передають `timeoutMs`; значення `timeoutMs` для конкретного виклику все одно має пріоритет.
  * `click` підтримує лише клік лівою кнопкою
  * `type` не підтримує `slowly=true`
  * `press` не підтримує `delayMs`
  * `hover`, `scrollintoview`, `drag`, `select`, `fill` і `evaluate` відхиляють перевизначення тайм-ауту для окремого виклику
  * `select` підтримує лише одне значення
  * `wait --load networkidle` не підтримується
  * завантаження файлів вимагає `--ref` / `--input-ref`, не підтримує CSS `--element` і наразі підтримує по одному файлу за раз
  * хуки діалогів не підтримують `--timeout`
  * скриншоти підтримують захоплення сторінок і `--ref`, але не CSS `--element`
  * `responsebody`, перехоплення завантажень, експорт PDF і пакетні дії все ще вимагають керованого браузера або сирого профілю CDP


## Віддалене керування браузером (проксі вузла-хоста)

Якщо Gateway працює на іншій машині, ніж браузер, запустіть **вузол-хост** на машині, де є Chrome/Brave/Edge/Chromium. Gateway проксуватиме дії браузера до цього вузла (окремий сервер керування браузером не потрібен).

Використовуйте `gateway.nodes.browser.mode`, щоб керувати автомаршрутизацією, і `gateway.nodes.browser.node`, щоб закріпити конкретний вузол, якщо під’єднано кілька вузлів.

Безпека й віддалене налаштування: [інструмент Browser](</uk/tools/browser>), [віддалений доступ](</uk/gateway/remote>), [Tailscale](</uk/gateway/tailscale>), [безпека](</uk/gateway/security>)

## Пов’язане

  * [Довідник CLI](</uk/cli>)
  * [Browser](</uk/tools/browser>)


Was this useful?YesNo