---
title: Браузер
source_url: https://docs.openclaw.ai/ru/cli/browser
scraped_at: 2026-06-29
---

ReferenceCLI commands

# `openclaw browser`

Управляйте поверхностью управления браузером OpenClaw и запускайте браузерные действия (жизненный цикл, профили, вкладки, снимки, скриншоты, навигация, ввод, эмуляция состояния и отладка).

Связано:

  * Инструмент браузера + API: [Инструмент браузера](</ru/tools/browser>)


## Общие флаги

  * `--url <gatewayWsUrl>`: URL WebSocket Gateway (по умолчанию из конфигурации).
  * `--token <token>`: токен Gateway (если требуется).
  * `--timeout <ms>`: тайм-аут запроса (мс).
  * `--expect-final`: ожидать финальный ответ Gateway.
  * `--browser-profile <name>`: выбрать профиль браузера (по умолчанию из конфигурации).
  * `--json`: машиночитаемый вывод (где поддерживается).


## Быстрый старт (локально)

bashCopy code
[code]
    openclaw browser profilesopenclaw browser --browser-profile openclaw startopenclaw browser --browser-profile openclaw open https://example.comopenclaw browser --browser-profile openclaw snapshot
[/code]

Агенты могут запустить такую же проверку готовности с помощью `browser({ action: "doctor" })`.

## Быстрое устранение неполадок

Если `start` завершается ошибкой `not reachable after start`, сначала проверьте готовность CDP. Если `start` и `tabs` выполняются успешно, но `open` или `navigate` завершается ошибкой, плоскость управления браузером исправна, а сбой обычно связан с политикой SSRF для навигации.

Минимальная последовательность:

bashCopy code
[code]
    openclaw browser --browser-profile openclaw doctoropenclaw browser --browser-profile openclaw startopenclaw browser --browser-profile openclaw tabsopenclaw browser --browser-profile openclaw open https://example.com
[/code]

Подробные инструкции: [Устранение неполадок браузера](</ru/tools/browser#cdp-startup-failure-vs-navigation-ssrf-block>)

## Жизненный цикл

bashCopy code
[code]
    openclaw browser statusopenclaw browser doctoropenclaw browser doctor --deepopenclaw browser startopenclaw browser start --headlessopenclaw browser stopopenclaw browser --browser-profile openclaw reset-profile
[/code]

Примечания:

  * `doctor --deep` добавляет живую пробу снимка. Это полезно, когда базовая готовность CDP в порядке, но нужно доказательство, что текущую вкладку можно проверить.
  * Для `attachOnly` и удаленных профилей CDP `openclaw browser stop` закрывает активный сеанс управления и очищает временные переопределения эмуляции, даже если OpenClaw не запускал процесс браузера самостоятельно.
  * Для локальных управляемых профилей `openclaw browser stop` останавливает созданный процесс браузера.
  * `openclaw browser start --headless` применяется только к этому запросу запуска и только когда OpenClaw запускает локальный управляемый браузер. Он не переписывает `browser.headless` или конфигурацию профиля и ничего не делает для уже запущенного браузера.
  * На хостах Linux без `DISPLAY` или `WAYLAND_DISPLAY` локальные управляемые профили автоматически запускаются в headless-режиме, если только `OPENCLAW_BROWSER_HEADLESS=0`, `browser.headless=false` или `browser.profiles.<name>.headless=false` явно не запрашивает видимый браузер.


## Если команда отсутствует

Если `openclaw browser` является неизвестной командой, проверьте `plugins.allow` в `~/.openclaw/openclaw.json`.

Когда `plugins.allow` присутствует, явно укажите встроенный Plugin браузера, если в конфигурации уже нет корневого блока `browser`:

json5Copy code
[code]
    {  plugins: {    allow: ["telegram", "browser"],  },}
[/code]

Явный корневой блок `browser`, например `browser.enabled=true` или `browser.profiles.<name>`, также активирует встроенный Plugin браузера при ограничительном списке разрешенных Plugins.

Связано: [Инструмент браузера](</ru/tools/browser#missing-browser-command-or-tool>)

## Профили

Профили — это именованные конфигурации маршрутизации браузера. На практике:

  * `openclaw`: запускает выделенный экземпляр Chrome, управляемый OpenClaw, или подключается к нему (изолированный каталог пользовательских данных).
  * `user`: управляет существующим сеансом Chrome с выполненным входом через Chrome DevTools MCP.
  * пользовательские профили CDP: указывают на локальную или удаленную конечную точку CDP.

bashCopy code
[code]
    openclaw browser profilesopenclaw browser create-profile --name work --color "#FF5A36"openclaw browser create-profile --name chrome-live --driver existing-sessionopenclaw browser create-profile --name remote --cdp-url https://browser-host.example.comopenclaw browser delete-profile --name work
[/code]

Использовать конкретный профиль:

bashCopy code
[code]
    openclaw browser --browser-profile work tabs
[/code]

## Вкладки

bashCopy code
[code]
    openclaw browser tabsopenclaw browser tab new --label docsopenclaw browser tab label t1 docsopenclaw browser tab select 2openclaw browser tab close 2openclaw browser open https://docs.openclaw.ai --label docsopenclaw browser focus docsopenclaw browser close t1
[/code]

`tabs` сначала возвращает `suggestedTargetId`, затем стабильный `tabId`, например `t1`, необязательную метку и необработанный `targetId`. Агенты должны передавать `suggestedTargetId` обратно в `focus`, `close`, снимки и действия. Метку можно назначить с помощью `open --label`, `tab new --label` или `tab label`; принимаются метки, идентификаторы вкладок, необработанные идентификаторы целей и уникальные префиксы идентификаторов целей. Поле запроса по-прежнему называется `targetId` для совместимости, но оно принимает эти ссылки на вкладки. Рассматривайте необработанные идентификаторы целей как диагностические дескрипторы, а не как долговременную память агента. Когда Chromium заменяет базовую необработанную цель во время навигации или отправки формы, OpenClaw сохраняет стабильный `tabId`/метку за заменяющей вкладкой, если может доказать соответствие. Необработанные идентификаторы целей остаются изменчивыми; предпочитайте `suggestedTargetId`.

## Снимок / скриншот / действия

Снимок:

bashCopy code
[code]
    openclaw browser snapshotopenclaw browser snapshot --urls
[/code]

Скриншот:

bashCopy code
[code]
    openclaw browser screenshotopenclaw browser screenshot --full-pageopenclaw browser screenshot --ref e12openclaw browser screenshot --labels
[/code]

Примечания:

  * `--full-page` предназначен только для снимков страниц; его нельзя сочетать с `--ref` или `--element`.
  * Профили `existing-session` / `user` поддерживают скриншоты страниц и скриншоты `--ref` из вывода снимка, но не CSS-скриншоты `--element`.
  * `--labels` накладывает текущие ссылки снимка на скриншот. В профилях на базе Playwright это работает с `--full-page` (наложение меток на всю страницу), `--ref` (наложение меток на вырезанный элемент по ARIA-ссылке) и `--element` (наложение меток на вырезанный элемент по CSS-селектору); в режимах вырезания элемента метки проецируются относительно элемента. Ответ также включает массив `annotations` с рамкой каждого ref. Каждый элемент содержит `ref`, `number`, `role`, необязательное `name` и `box: {x, y, width, height}`; координаты указаны в пространстве захваченного изображения (viewport / fullpage / относительно элемента). Поле опускается, когда оно пустое. Профили `existing-session` отображают наложение chrome-mcp на скриншотах страниц, но не используют вспомогательный механизм проекции Playwright и не включают `annotations`; CSS-скриншоты `--element` там не поддерживаются. Без Playwright или chrome-mcp скриншоты с метками недоступны. Предыдущие выпуски игнорировали `--full-page`, `--ref` и `--element` на скриншотах Playwright с метками и всегда возвращали захват viewport; теперь скриншоты с метками учитывают эти области.
  * `snapshot --urls` добавляет найденные назначения ссылок к AI-снимкам, чтобы агенты могли выбирать прямые цели навигации, а не угадывать только по тексту ссылок.


Навигация/щелчок/ввод (автоматизация UI на основе ref):

bashCopy code
[code]
    openclaw browser navigate https://example.comopenclaw browser click <ref>openclaw browser click-coords 120 340openclaw browser type <ref> "hello"openclaw browser press Enteropenclaw browser hover <ref>openclaw browser scrollintoview <ref>openclaw browser drag <startRef> <endRef>openclaw browser select <ref> OptionA OptionBopenclaw browser fill --fields '[{"ref":"1","value":"Ada"}]'openclaw browser wait --text "Done"openclaw browser evaluate --fn '(el) => el.textContent' --ref <ref>openclaw browser evaluate --fn 'const title = document.title; return title;'openclaw browser evaluate --timeout-ms 30000 --fn 'async () => { await window.ready; return true; }'
[/code]

`evaluate --fn` принимает исходный код функции, выражение или тело оператора. Тела операторов оборачиваются как асинхронные функции, поэтому используйте `return` для значения, которое хотите получить обратно. Используйте `evaluate --timeout-ms <ms>`, когда функция на стороне страницы может требовать больше времени, чем стандартный тайм-аут evaluate.

Ответы действий возвращают текущий необработанный `targetId` после замены страницы, вызванной действием, когда OpenClaw может доказать заменяющую вкладку. Скрипты все равно должны сохранять и передавать `suggestedTargetId`/метки для долговременных рабочих процессов.

Помощники файлов и диалогов:

bashCopy code
[code]
    openclaw browser upload /tmp/openclaw/uploads/file.pdf --ref <ref>openclaw browser upload media://inbound/file.pdf --ref <ref>openclaw browser waitfordownloadopenclaw browser download <ref> report.pdfopenclaw browser dialog --acceptopenclaw browser dialog --dismiss --dialog-id d1
[/code]

Управляемые профили Chrome сохраняют обычные загрузки, запущенные щелчком, в каталог загрузок OpenClaw (`/tmp/openclaw/downloads` по умолчанию или настроенный временный корень). Используйте `waitfordownload` или `download`, когда агенту нужно дождаться конкретного файла и вернуть его путь; эти явные ожидатели владеют следующей загрузкой. Загрузки файлов принимают файлы из временного корня загрузок OpenClaw и управляемые OpenClaw входящие медиа, включая ссылки `media://inbound/<id>` и относительные к sandbox `media/inbound/<id>`. Вложенные ссылки media, обход путей и произвольные локальные пути по-прежнему отклоняются. Когда действие открывает модальный диалог, ответ действия возвращает `blockedByDialog` с `browserState.dialogs.pending`; передайте `--dialog-id`, чтобы ответить на него напрямую. Диалоги, обработанные вне OpenClaw, появляются в `browserState.dialogs.recent`.

## Состояние и хранилище

Viewport + эмуляция:

bashCopy code
[code]
    openclaw browser resize 1280 720openclaw browser set viewport 1280 720openclaw browser set offline onopenclaw browser set media darkopenclaw browser set timezone Europe/Londonopenclaw browser set locale en-GBopenclaw browser set geo 51.5074 -0.1278 --accuracy 25openclaw browser set device "iPhone 14"openclaw browser set headers '{"x-test":"1"}'openclaw browser set credentials myuser mypass
[/code]

Cookie + хранилище:

bashCopy code
[code]
    openclaw browser cookiesopenclaw browser cookies set session abc123 --url https://example.comopenclaw browser cookies clearopenclaw browser storage local getopenclaw browser storage local set token abc123openclaw browser storage session clear
[/code]

## Отладка

bashCopy code
[code]
    openclaw browser console --level erroropenclaw browser pdfopenclaw browser responsebody "**/api"openclaw browser highlight <ref>openclaw browser errors --clearopenclaw browser requests --filter apiopenclaw browser trace startopenclaw browser trace stop --out trace.zip
[/code]

## Существующий Chrome через MCP

Используйте встроенный профиль `user` или создайте собственный профиль `existing-session`:

bashCopy code
[code]
    openclaw browser --browser-profile user tabsopenclaw browser create-profile --name chrome-live --driver existing-sessionopenclaw browser create-profile --name brave-live --driver existing-session --user-data-dir "~/Library/Application Support/BraveSoftware/Brave-Browser"openclaw browser create-profile --name chrome-port --driver existing-session --cdp-url http://127.0.0.1:9222openclaw browser --browser-profile chrome-live tabs
[/code]

Путь existing-session по умолчанию — автоматическое подключение Chrome MCP только на хосте. Если браузер уже запущен с конечной точкой DevTools, передайте `--cdp-url`, чтобы Chrome MCP подключился к этой конечной точке вместо этого. Для Docker, Browserless или других удаленных настроек, где семантика Chrome MCP не нужна, используйте профиль CDP.

Текущие ограничения existing-session:

  * действия на основе снимков используют refs, а не CSS-селекторы
  * `browser.actionTimeoutMs` задает по умолчанию для поддерживаемых запросов `act` значение 60000 мс, когда вызывающие стороны не указывают `timeoutMs`; `timeoutMs` для отдельного вызова по-прежнему имеет приоритет.
  * `click` выполняет только щелчок левой кнопкой
  * `type` не поддерживает `slowly=true`
  * `press` не поддерживает `delayMs`
  * `hover`, `scrollintoview`, `drag`, `select`, `fill` и `evaluate` отклоняют переопределения тайм-аута для отдельного вызова
  * `select` поддерживает только одно значение
  * `wait --load networkidle` не поддерживается для профилей существующих сеансов (работает с управляемыми и raw/remote CDP)
  * загрузка файлов требует `--ref` / `--input-ref`, не поддерживает CSS `--element` и сейчас поддерживает только один файл за раз
  * хуки диалогов не поддерживают `--timeout`
  * снимки экрана поддерживают захват страницы и `--ref`, но не CSS `--element`
  * `responsebody`, перехват загрузок, экспорт PDF и пакетные действия по-прежнему требуют управляемый браузер или профиль raw CDP


## Удаленное управление браузером (прокси хоста узла)

Если Gateway работает на другой машине, чем браузер, запустите **хост узла** на машине с Chrome/Brave/Edge/Chromium. Gateway будет проксировать действия браузера на этот узел (отдельный сервер управления браузером не требуется).

Используйте `gateway.nodes.browser.mode`, чтобы управлять автоматической маршрутизацией, и `gateway.nodes.browser.node`, чтобы закрепить конкретный узел, если подключено несколько.

Безопасность + удаленная настройка: [Инструмент браузера](</ru/tools/browser>), [Удаленный доступ](</ru/gateway/remote>), [Tailscale](</ru/gateway/tailscale>), [Безопасность](</ru/gateway/security>)

## См. также

  * [Справочник CLI](</ru/cli>)
  * [Браузер](</ru/tools/browser>)


Was this useful?YesNo

Open issue