---
title: API управления браузером
source_url: https://docs.openclaw.ai/ru/tools/browser-control
scraped_at: 2026-06-29
---

CapabilitiesTools

Для настройки, конфигурации и устранения неполадок см. [Browser](</ru/tools/browser>). Эта страница является справочником по локальному управляющему HTTP API, CLI `openclaw browser` и шаблонам сценариев (снимки состояния, ссылки, ожидания, отладочные потоки).

## Управляющий API (необязательно)

Только для локальных интеграций Gateway предоставляет небольшой HTTP API через loopback. Этот автономный сервер включается явно — задайте переменную окружения `OPENCLAW_EAGER_BROWSER_CONTROL_SERVER=1` в окружении сервиса gateway и перезапустите gateway, прежде чем HTTP-эндпоинты станут доступны. Без этой переменной среда выполнения управления браузером по-прежнему работает через CLI и инструменты агента, но на управляющем loopback-порту ничего не слушает.

  * Статус/запуск/остановка: `GET /`, `POST /start`, `POST /stop`
  * Вкладки: `GET /tabs`, `POST /tabs/open`, `POST /tabs/focus`, `DELETE /tabs/:targetId`
  * Снимок состояния/скриншот: `GET /snapshot`, `POST /screenshot`
  * Действия: `POST /navigate`, `POST /act`
  * Хуки: `POST /hooks/file-chooser`, `POST /hooks/dialog`
  * Загрузки: `POST /download`, `POST /wait/download`
  * Разрешения: `POST /permissions/grant`
  * Отладка: `GET /console`, `POST /pdf`
  * Отладка: `GET /errors`, `GET /requests`, `POST /trace/start`, `POST /trace/stop`, `POST /highlight`
  * Сеть: `POST /response/body`
  * Состояние: `GET /cookies`, `POST /cookies/set`, `POST /cookies/clear`
  * Состояние: `GET /storage/:kind`, `POST /storage/:kind/set`, `POST /storage/:kind/clear`
  * Настройки: `POST /set/offline`, `POST /set/headers`, `POST /set/credentials`, `POST /set/geolocation`, `POST /set/media`, `POST /set/timezone`, `POST /set/locale`, `POST /set/device`


Все эндпоинты принимают `?profile=<name>`. `POST /start?headless=true` запрашивает одноразовый headless-запуск для локальных управляемых профилей без изменения сохраненной конфигурации браузера; профили attach-only, удаленного CDP и существующего сеанса отклоняют это переопределение, потому что OpenClaw не запускает эти процессы браузера.

Для эндпоинтов вкладок `targetId` — это имя поля совместимости. Предпочитайте передавать `suggestedTargetId` из `GET /tabs` или `POST /tabs/open`; также принимаются метки и дескрипторы `tabId`, такие как `t1`. Необработанные идентификаторы целей CDP и уникальные необработанные префиксы target-id по-прежнему работают, но это нестабильные диагностические дескрипторы.

Если настроена аутентификация gateway с общим секретом, HTTP-маршруты браузера также требуют аутентификацию:

  * `Authorization: Bearer <gateway token>`
  * `x-openclaw-password: <gateway password>` или HTTP Basic auth с этим паролем


Примечания:

  * Этот автономный loopback API браузера **не** использует заголовки идентификации trusted-proxy или Tailscale Serve.
  * Если `gateway.auth.mode` имеет значение `none` или `trusted-proxy`, эти loopback-маршруты браузера не наследуют эти режимы с идентификацией; оставляйте их доступными только через loopback.


### Контракт ошибок `/act`

`POST /act` использует структурированный ответ об ошибке для валидации на уровне маршрута и сбоев политики:

jsonCopy code
[code]
    { "error": "<message>", "code": "ACT_*" }
[/code]

Текущие значения `code`:

  * `ACT_KIND_REQUIRED` (HTTP 400): `kind` отсутствует или не распознан.
  * `ACT_INVALID_REQUEST` (HTTP 400): полезная нагрузка действия не прошла нормализацию или валидацию.
  * `ACT_SELECTOR_UNSUPPORTED` (HTTP 400): `selector` использован с неподдерживаемым типом действия.
  * `ACT_EVALUATE_DISABLED` (HTTP 403): `evaluate` (или `wait --fn`) отключен конфигурацией.
  * `ACT_TARGET_ID_MISMATCH` (HTTP 403): верхнеуровневый или пакетный `targetId` конфликтует с целью запроса.
  * `ACT_EXISTING_SESSION_UNSUPPORTED` (HTTP 501): действие не поддерживается для профилей существующего сеанса.


Другие ошибки среды выполнения могут по-прежнему возвращать `{ "error": "<message>" }` без поля `code`.

### Требование Playwright

Некоторые возможности (navigate/act/AI-снимок состояния/снимок состояния ролей, скриншоты элементов, PDF) требуют Playwright. Если Playwright не установлен, эти эндпоинты возвращают понятную ошибку 501.

Что по-прежнему работает без Playwright:

  * ARIA-снимки состояния
  * Снимки состояния доступности в стиле ролей (`--interactive`, `--compact`, `--depth`, `--efficient`), когда доступен CDP WebSocket для каждой вкладки. Это резервный вариант для инспекции и обнаружения ссылок; Playwright остается основным движком действий.
  * Скриншоты страниц для управляемого браузера `openclaw`, когда доступен CDP WebSocket для каждой вкладки
  * Скриншоты страниц для профилей `existing-session` / Chrome MCP
  * Скриншоты `existing-session` на основе ссылок (`--ref`) из вывода snapshot


Что по-прежнему требует Playwright:

  * `navigate`
  * `act`
  * AI-снимки состояния, которые зависят от собственного формата AI-снимков Playwright
  * Скриншоты элементов по CSS-селекторам (`--element`)
  * полный экспорт браузера в PDF


Скриншоты элементов также отклоняют `--full-page`; маршрут возвращает `fullPage is not supported for element screenshots`.

Если вы видите `Playwright is not available in this gateway build`, в упакованном Gateway отсутствует основная зависимость среды выполнения браузера. Переустановите или обновите OpenClaw, затем перезапустите gateway. Для Docker также установите браузерные бинарные файлы Chromium, как показано ниже.

#### Установка Playwright в Docker

Если ваш Gateway работает в Docker, избегайте `npx playwright` (конфликты переопределения npm). Для пользовательских образов встройте Chromium в образ:

bashCopy code
[code]
    OPENCLAW_INSTALL_BROWSER=1 ./scripts/docker/setup.sh
[/code]

Для существующего образа установите через встроенный CLI:

bashCopy code
[code]
    docker compose run --rm openclaw-cli \  node /app/node_modules/playwright-core/cli.js install chromium
[/code]

Чтобы сохранять загрузки браузера, задайте `PLAYWRIGHT_BROWSERS_PATH` (например, `/home/node/.cache/ms-playwright`) и убедитесь, что `/home/node` сохраняется через `OPENCLAW_HOME_VOLUME` или bind mount. OpenClaw автоматически обнаруживает сохраненный Chromium в Linux. См. [Docker](</ru/install/docker>).

## Как это работает (внутреннее)

Небольшой loopback-сервер управления принимает HTTP-запросы и подключается к браузерам на базе Chromium через CDP. Расширенные действия (click/type/snapshot/PDF) проходят через Playwright поверх CDP; когда Playwright отсутствует, доступны только операции без Playwright. Агент видит один стабильный интерфейс, пока локальные/удаленные браузеры и профили свободно меняются под ним.

## Краткий справочник CLI

Все команды принимают `--browser-profile <name>` для выбора конкретного профиля и `--json` для машиночитаемого вывода.

Основы: статус, вкладки, открыть/фокус/закрыть bashCopy code
[code]
    openclaw browser statusopenclaw browser startopenclaw browser start --headless # one-shot local managed headless launchopenclaw browser stop            # also clears emulation on attach-only/remote CDPopenclaw browser tabsopenclaw browser tab             # shortcut for current tabopenclaw browser tab newopenclaw browser tab select 2openclaw browser tab close 2openclaw browser open https://example.comopenclaw browser focus abcd1234openclaw browser close abcd1234
[/code]

Инспекция: скриншот, снимок состояния, консоль, ошибки, запросы bashCopy code
[code]
    openclaw browser screenshotopenclaw browser screenshot --full-pageopenclaw browser screenshot --ref 12        # or --ref e12openclaw browser screenshot --labelsopenclaw browser snapshotopenclaw browser snapshot --format aria --limit 200openclaw browser snapshot --interactive --compact --depth 6openclaw browser snapshot --efficientopenclaw browser snapshot --labelsopenclaw browser snapshot --urlsopenclaw browser snapshot --selector "#main" --interactiveopenclaw browser snapshot --frame "iframe#main" --interactiveopenclaw browser console --level erroropenclaw browser errors --clearopenclaw browser requests --filter api --clearopenclaw browser pdfopenclaw browser responsebody "**/api" --max-chars 5000
[/code]

Действия: navigate, click, type, drag, wait, evaluate bashCopy code
[code]
    openclaw browser navigate https://example.comopenclaw browser resize 1280 720openclaw browser click 12 --double           # or e12 for role refsopenclaw browser click-coords 120 340        # viewport coordinatesopenclaw browser type 23 "hello" --submitopenclaw browser press Enteropenclaw browser hover 44openclaw browser scrollintoview e12openclaw browser drag 10 11openclaw browser select 9 OptionA OptionBopenclaw browser download e12 report.pdfopenclaw browser waitfordownload report.pdfopenclaw browser upload /tmp/openclaw/uploads/file.pdfopenclaw browser upload media://inbound/file.pdfopenclaw browser fill --fields '[{"ref":"1","type":"text","value":"Ada"}]'openclaw browser dialog --acceptopenclaw browser dialog --dismiss --dialog-id d1openclaw browser wait --text "Done"openclaw browser wait "#main" --url "**/dash" --load networkidle --fn "window.ready===true"openclaw browser evaluate --fn '(el) => el.textContent' --ref 7openclaw browser evaluate --fn 'const title = document.title; return title;'openclaw browser evaluate --timeout-ms 30000 --fn 'async () => { await window.ready; return true; }'openclaw browser highlight e12openclaw browser trace startopenclaw browser trace stop
[/code]

Состояние: cookies, storage, offline, headers, geo, device bashCopy code
[code]
    openclaw browser cookiesopenclaw browser cookies set session abc123 --url "https://example.com"openclaw browser cookies clearopenclaw browser storage local getopenclaw browser storage local set theme darkopenclaw browser storage session clearopenclaw browser set offline onopenclaw browser set headers --headers-json '{"X-Debug":"1"}'openclaw browser set credentials user pass            # --clear to removeopenclaw browser set geo 37.7749 -122.4194 --origin "https://example.com"openclaw browser set media darkopenclaw browser set timezone America/New_Yorkopenclaw browser set locale en-USopenclaw browser set device "iPhone 14"
[/code]

Примечания:

  * `upload` и `dialog` — это вызовы **взведения** ; запускайте их перед click/press, который вызывает выбор файла/диалог. Если действие открывает модальное окно, ответ действия включает `blockedByDialog` и `browserState.dialogs.pending`; передайте этот `dialogId`, чтобы ответить напрямую. Диалоги, обработанные вне OpenClaw, отображаются в `browserState.dialogs.recent`.
  * `click`/`type`/и т. д. требуют `ref` из `snapshot` (числовой `12`, ролевая ссылка `e12` или действенная ARIA-ссылка `ax12`). CSS-селекторы намеренно не поддерживаются для действий. Используйте `click-coords`, когда видимая позиция в viewport — единственная надежная цель.
  * Пути загрузок и трассировок ограничены временными корнями OpenClaw: `/tmp/openclaw{,/downloads}` (резервный вариант: `${os.tmpdir()}/openclaw/...`).
  * `upload` принимает файлы из временного корня загрузок OpenClaw и входящие медиа, управляемые OpenClaw. Управляемые входящие медиа можно указывать как `media://inbound/<id>`, относительный к песочнице путь `media/inbound/<id>` или разрешенный путь внутри управляемого каталога входящих медиа. Вложенные media refs, обход каталогов, symlinks, hardlinks и произвольные локальные пути по-прежнему отклоняются.
  * `upload` также может напрямую задавать файловые input через `--input-ref` или `--element`.


Стабильные идентификаторы и метки вкладок сохраняются при замене необработанной цели Chromium, когда OpenClaw может доказать замену вкладки, например по тому же URL или когда одна старая вкладка становится одной новой вкладкой после отправки формы. Необработанные target ids по-прежнему нестабильны; в сценариях предпочитайте `suggestedTargetId` из `tabs`.

Краткий обзор флагов снимков состояния:

  * `--format ai` (по умолчанию с Playwright): AI-снимок с числовыми ref-идентификаторами (`aria-ref="<n>"`).
  * `--format aria`: дерево доступности с ref-идентификаторами `axN`. Когда Playwright доступен, OpenClaw связывает ref-идентификаторы с backend DOM id на живой странице, чтобы последующие действия могли их использовать; иначе считайте вывод предназначенным только для инспекции.
  * `--efficient` (или `--mode efficient`): компактный пресет снимка ролей. Установите `browser.snapshotDefaults.mode: "efficient"`, чтобы сделать его значением по умолчанию (см. [конфигурацию Gateway](</ru/gateway/configuration-reference#browser>)).
  * `--interactive`, `--compact`, `--depth`, `--selector` принудительно используют снимок ролей с ref-идентификаторами вида `ref=e12`. `--frame "<iframe>"` ограничивает снимки ролей iframe.
  * С Playwright `--labels` добавляет снимок экрана с наложенными ref-метками (печатает `MEDIA:<path>`) плюс массив `annotations` с ограничивающей рамкой каждого ref-идентификатора. Для `screenshot` метки на базе Playwright работают с `--full-page`, `--ref` и `--element`; для `snapshot` сопровождающий снимок экрана остается только в пределах viewport. Профили existing-session/chrome-mcp отображают наложенные метки на снимках страниц, но не возвращают `annotations` и не используют вспомогательную проекцию Playwright для full-page/ref/element. Без Playwright или chrome-mcp снимки экрана с метками недоступны.
  * `--urls` добавляет обнаруженные назначения ссылок к AI-снимкам.


## Снимки и ref-идентификаторы

OpenClaw поддерживает два стиля "снимков":

  * **AI-снимок (числовые ref-идентификаторы)** : `openclaw browser snapshot` (по умолчанию; `--format ai`)

    * Вывод: текстовый снимок, включающий числовые ref-идентификаторы.
    * Действия: `openclaw browser click 12`, `openclaw browser type 23 "hello"`.
    * Внутри ref-идентификатор разрешается через `aria-ref` Playwright.
  * **Снимок ролей (role refs вроде`e12`)**: `openclaw browser snapshot --interactive` (или `--compact`, `--depth`, `--selector`, `--frame`)

    * Вывод: список/дерево на основе ролей с `[ref=e12]` (и необязательным `[nth=1]`).
    * Действия: `openclaw browser click e12`, `openclaw browser highlight e12`.
    * Внутри ref-идентификатор разрешается через `getByRole(...)` (плюс `nth()` для дубликатов).
    * Добавьте `--labels`, чтобы включить снимок экрана с наложенными метками `e12`. В профилях на базе Playwright это также возвращает метаданные ограничивающих рамок для каждого ref-идентификатора (`annotations[]`).
    * Добавьте `--urls`, когда текст ссылки неоднозначен и агенту нужны конкретные цели навигации.
  * **ARIA-снимок (ARIA refs вроде`ax12`)**: `openclaw browser snapshot --format aria`

    * Вывод: дерево доступности в виде структурированных узлов.
    * Действия: `openclaw browser click ax12` работает, когда путь снимка может связать ref-идентификатор через Playwright и Chrome backend DOM ids.
  * Если Playwright недоступен, ARIA-снимки все равно могут быть полезны для инспекции, но ref-идентификаторы могут быть недоступны для действий. Повторно снимите страницу с `--format ai` или `--interactive`, когда нужны ref-идентификаторы для действий.

  * Docker-доказательство для резервного пути raw-CDP: `pnpm test:docker:browser-cdp-snapshot` запускает Chromium с CDP, выполняет `browser doctor --deep` и проверяет, что снимки ролей включают URL ссылок, кликабельные элементы, повышенные из курсора, и метаданные iframe.


Поведение ref-идентификаторов:

  * Ref-идентификаторы **не стабильны между навигациями** ; если что-то не удалось, повторно выполните `snapshot` и используйте свежий ref-идентификатор.
  * `/act` возвращает текущий сырой `targetId` после замены, вызванной действием, когда может доказать вкладку-замену. Продолжайте использовать стабильные id/метки вкладок для последующих команд.
  * Если снимок ролей был сделан с `--frame`, ref-идентификаторы ролей ограничены этим iframe до следующего снимка ролей.
  * Неизвестные или устаревшие ref-идентификаторы `axN` быстро завершаются ошибкой вместо перехода к селектору `aria-ref` Playwright. Когда это происходит, выполните свежий снимок той же вкладки.


## Расширенные ожидания

Можно ждать не только время/текст:

  * Ожидать URL (globs поддерживаются Playwright): 
    * `openclaw browser wait --url "**/dash"`
  * Ожидать состояние загрузки: 
    * `openclaw browser wait --load networkidle`
    * Поддерживается в управляемых профилях `openclaw` и raw/remote CDP. Профили `user` и `existing-session` отклоняют `networkidle`; используйте там ожидания по `--url`, `--text`, селектору или `--fn`.
  * Ожидать JS-предикат: 
    * `openclaw browser wait --fn "window.ready===true"`
  * Ожидать, пока селектор станет видимым: 
    * `openclaw browser wait "#main"`


Их можно комбинировать:

bashCopy code
[code]
    openclaw browser wait "#main" \  --url "**/dash" \  --load networkidle \  --fn "window.ready===true" \  --timeout-ms 15000
[/code]

## Рабочие процессы отладки

Когда действие завершается ошибкой (например, "not visible", "strict mode violation", "covered"):

  1. `openclaw browser snapshot --interactive`
  2. Используйте `click <ref>` / `type <ref>` (предпочитайте ref-идентификаторы ролей в интерактивном режиме)
  3. Если ошибка сохраняется: `openclaw browser highlight <ref>`, чтобы увидеть, на что нацелен Playwright
  4. Если страница ведет себя странно: 
     * `openclaw browser errors --clear`
     * `openclaw browser requests --filter api --clear`
  5. Для глубокой отладки: запишите трассировку: 
     * `openclaw browser trace start`
     * воспроизведите проблему
     * `openclaw browser trace stop` (печатает `TRACE:<path>`)


## JSON-вывод

`--json` предназначен для скриптов и структурированных инструментов.

Примеры:

bashCopy code
[code]
    openclaw browser status --jsonopenclaw browser snapshot --interactive --jsonopenclaw browser requests --filter api --jsonopenclaw browser cookies --json
[/code]

Снимки ролей в JSON включают `refs` и небольшой блок `stats` (lines/chars/refs/interactive), чтобы инструменты могли оценивать размер и плотность полезной нагрузки.

## Настройки состояния и окружения

Они полезны для рабочих процессов вида "заставить сайт вести себя как X":

  * Cookies: `cookies`, `cookies set`, `cookies clear`
  * Хранилище: `storage local|session get|set|clear`
  * Offline: `set offline on|off`
  * Заголовки: `set headers --headers-json '{"X-Debug":"1"}'` (устаревший `set headers --json '{"X-Debug":"1"}'` остается поддерживаемым)
  * HTTP basic auth: `set credentials user pass` (или `--clear`)
  * Геолокация: `set geo <lat> <lon> --origin "https://example.com"` (или `--clear`)
  * Media: `set media dark|light|no-preference|none`
  * Часовой пояс / локаль: `set timezone ...`, `set locale ...`
  * Устройство / viewport: 
    * `set device "iPhone 14"` (пресеты устройств Playwright)
    * `set viewport 1280 720`


## Безопасность и конфиденциальность

  * Профиль браузера openclaw может содержать авторизованные сессии; считайте его чувствительным.
  * `browser act kind=evaluate` / `openclaw browser evaluate` и `wait --fn` выполняют произвольный JavaScript в контексте страницы. Prompt injection может направлять это поведение. Отключите его с помощью `browser.evaluateEnabled=false`, если он вам не нужен.
  * `openclaw browser evaluate --fn` принимает исходный код функции, выражение или тело инструкции. Тела инструкций оборачиваются как async-функции, поэтому используйте `return` для значения, которое нужно вернуть. Используйте `--timeout-ms <ms>`, когда функция на стороне страницы может требовать больше времени, чем стандартный тайм-аут evaluate.
  * Для заметок о входе и антибот-защите (X/Twitter и т. д.) см. [Вход в браузер + публикация в X/Twitter](</ru/tools/browser-login>).
  * Держите Gateway/Node-хост приватным (loopback или только tailnet).
  * Удаленные CDP endpoints имеют широкие возможности; туннелируйте и защищайте их.


Пример strict-mode (по умолчанию блокировать частные/внутренние назначения):

json5Copy code
[code]
    {  browser: {    ssrfPolicy: {      dangerouslyAllowPrivateNetwork: false,      hostnameAllowlist: ["*.example.com", "example.com"],      allowedHostnames: ["localhost"], // optional exact allow    },  },}
[/code]

## Связанные материалы

  * [Браузер](</ru/tools/browser>) \- обзор, конфигурация, профили, безопасность
  * [Вход в браузер](</ru/tools/browser-login>) \- вход на сайты
  * [Устранение неполадок браузера в Linux](</ru/tools/browser-linux-troubleshooting>)
  * [Устранение неполадок браузера в WSL2](</ru/tools/browser-wsl2-windows-remote-cdp-troubleshooting>)


Was this useful?YesNo

Open issue