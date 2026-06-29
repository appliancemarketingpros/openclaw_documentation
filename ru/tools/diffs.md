---
title: Различия
source_url: https://docs.openclaw.ai/ru/tools/diffs
scraped_at: 2026-06-29
---

CapabilitiesTools

`diffs` — необязательный инструмент Plugin с краткими встроенными системными указаниями и сопутствующим Skill, который превращает содержимое изменений в доступный только для чтения артефакт diff для агентов.

Он принимает:

  * текст `before` и `after`
  * унифицированный `patch`


Он может возвращать:

  * URL просмотрщика Gateway для представления на canvas
  * путь к отрендеренному файлу (PNG или PDF) для доставки в сообщении
  * оба результата за один вызов


Если плагин включен, он добавляет краткие указания по использованию в пространство системного промпта, а также предоставляет подробный Skill для случаев, когда агенту нужны более полные инструкции.

## Быстрый старт

* ### Установите плагин

bashCopy code
[code]
    openclaw plugins install diffs
[/code]

* ### Включите плагин

json5Copy code
[code]
    {  plugins: {    entries: {      diffs: {        enabled: true,      },    },  },}
[/code]

* ### Выберите режим

### view

Потоки с приоритетом canvas: агенты вызывают `diffs` с `mode: "view"` и открывают `details.viewerUrl` с помощью `canvas present`.

### file

Доставка файла в чате: агенты вызывают `diffs` с `mode: "file"` и отправляют `details.filePath` через `message`, используя `path` или `filePath`.

### both

Комбинированный режим: агенты вызывают `diffs` с `mode: "both"`, чтобы получить оба артефакта за один вызов.

## Отключение встроенных системных указаний

Если вы хотите оставить инструмент `diffs` включенным, но отключить его встроенные указания для системного промпта, установите `plugins.entries.diffs.hooks.allowPromptInjection` в `false`:

json5Copy code
[code]
    {  plugins: {    entries: {      diffs: {        enabled: true,        hooks: {          allowPromptInjection: false,        },      },    },  },}
[/code]

Это блокирует хук `before_prompt_build` плагина diffs, сохраняя доступными сам плагин, инструмент и сопутствующий Skill.

Если вы хотите отключить и указания, и инструмент, отключите плагин.

## Типичный рабочий процесс агента

* ### Вызов diffs

Агент вызывает инструмент `diffs` с входными данными.

* ### Чтение details

Агент читает поля `details` из ответа.

* ### Представление

Агент либо открывает `details.viewerUrl` с помощью `canvas present`, либо отправляет `details.filePath` через `message`, используя `path` или `filePath`, либо делает и то и другое.

## Примеры входных данных

### До и после

jsonCopy code
[code]
    {  "before": "# Hello\n\nOne",  "after": "# Hello\n\nTwo",  "path": "docs/example.md",  "mode": "view"}
[/code]

### Patch

jsonCopy code
[code]
    {  "patch": "diff --git a/src/example.ts b/src/example.ts\n--- a/src/example.ts\n+++ b/src/example.ts\n@@ -1 +1 @@\n-const x = 1;\n+const x = 2;\n",  "mode": "both"}
[/code]

## Справочник входных данных инструмента

Все поля необязательны, если не указано иное.

Исходный текст. Обязательно вместе с `after`, если `patch` не указан.

Обновленный текст. Обязательно вместе с `before`, если `patch` не указан.

Текст унифицированного diff. Взаимоисключается с `before` и `after`.

Отображаемое имя файла для режима до и после.

Подсказка для переопределения языка в режиме до и после. Неизвестные значения и языки вне стандартного набора просмотрщика откатываются к простому тексту, если не установлен плагин Diff Viewer Language Pack.

Переопределение заголовка просмотрщика.

Режим вывода. По умолчанию используется значение плагина `defaults.mode`. Устаревший псевдоним: `"image"` ведет себя как `"file"` и по-прежнему принимается для обратной совместимости.

Тема просмотрщика. По умолчанию используется значение плагина `defaults.theme`.

Макет diff. По умолчанию используется значение плагина `defaults.layout`.

Разворачивать неизмененные разделы, когда доступен полный контекст. Только опция отдельного вызова (не ключ по умолчанию плагина).

Формат отрендеренного файла. По умолчанию используется значение плагина `defaults.fileFormat`.

Предустановка качества для рендеринга PNG или PDF.

Переопределение масштаба устройства (`1`-`4`).

Максимальная ширина рендеринга в CSS-пикселях (`640`-`2400`).

TTL артефакта в секундах для просмотрщика и автономных файловых выводов. Максимум 21600.

Переопределение origin URL просмотрщика. Переопределяет `viewerBaseUrl` плагина. Должен быть `http` или `https`, без query/hash.

Устаревшие псевдонимы входных данных

По-прежнему принимаются для обратной совместимости:

  * `format` -> `fileFormat`
  * `imageFormat` -> `fileFormat`
  * `imageQuality` -> `fileQuality`
  * `imageScale` -> `fileScale`
  * `imageMaxWidth` -> `fileMaxWidth`

Валидация и ограничения

  * `before` и `after`: максимум 512 KiB каждый.
  * `patch`: максимум 2 MiB.
  * `path`: максимум 2048 байт.
  * `lang`: максимум 128 байт.
  * `title`: максимум 1024 байта.
  * Ограничение сложности patch: максимум 128 файлов и 120000 строк суммарно.
  * `patch` вместе с `before` или `after` отклоняется.
  * Ограничения безопасности отрендеренного файла (применяются к PNG и PDF): 
    * `fileQuality: "standard"`: максимум 8 MP (8 000 000 отрендеренных пикселей).
    * `fileQuality: "hq"`: максимум 14 MP (14 000 000 отрендеренных пикселей).
    * `fileQuality: "print"`: максимум 24 MP (24 000 000 отрендеренных пикселей).
    * Для PDF также действует максимум 50 страниц.


## Подсветка синтаксиса

OpenClaw включает подсветку синтаксиса для распространенных языков исходного кода, конфигурации и документации:

`javascript`, `typescript`, `tsx`, `jsx`, `json`, `markdown`, `yaml`, `css`, `html`, `sh`, `python`, `go`, `rust`, `java`, `c`, `cpp`, `csharp`, `php`, `sql`, `docker`, `ruby`, `swift`, `kotlin`, `r`, `dart`, `lua`, `powershell`, `xml` и `toml`.

Распространенные псевдонимы, такие как `js`, `ts`, `bash`, `md`, `yml`, `c++`, `dockerfile`, `rb`, `kt` и `ps1`, нормализуются к этим стандартным языкам.

Установите Plugin языкового пакета просмотрщика различий, чтобы подсвечивать другие языки:

bashCopy code
[code]
    openclaw plugins install clawhub:@openclaw/diffs-language-pack
[/code]

Когда языковой пакет доступен, OpenClaw может подсвечивать гораздо больше языков. Если пакет не установлен, файлы вне списка по умолчанию все равно отображаются как читаемый простой текст. Примеры включают Astro, Vue, Svelte, MDX, GraphQL, Terraform/HCL, Nix, Clojure, Elixir, Haskell, OCaml, Scala, Zig, Solidity, Verilog/VHDL, Fortran, MATLAB, LaTeX, Mermaid, Sass/Less/SCSS, Nginx, Apache, CSV, dotenv, INI и diff-файлы.

Подробности см. в разделе [Plugin Diffs Language Pack](</ru/plugins/reference/diffs-language-pack>), а каталог языков и псевдонимов верхнего уровня Shiki — в [языках Shiki](<https://shiki.style/languages>).

## Контракт сведений вывода

Инструмент возвращает структурированные метаданные в `details`.

Поля просмотрщика

Общие поля для режимов, создающих просмотрщик:

  * `artifactId`
  * `viewerUrl`
  * `viewerPath`
  * `title`
  * `expiresAt`
  * `inputKind`
  * `fileCount`
  * `mode`
  * `context` (`agentId`, `sessionId`, `messageChannel`, `agentAccountId`, если доступны)

Поля файла

Поля файла при рендеринге PNG или PDF:

  * `artifactId`
  * `expiresAt`
  * `filePath`
  * `path` (то же значение, что и `filePath`, для совместимости с инструментом сообщений)
  * `fileBytes`
  * `fileFormat`
  * `fileQuality`
  * `fileScale`
  * `fileMaxWidth`

Псевдонимы совместимости

Также возвращаются для существующих вызывающих сторон:

  * `format` (то же значение, что и `fileFormat`)
  * `imagePath` (то же значение, что и `filePath`)
  * `imageBytes` (то же значение, что и `fileBytes`)
  * `imageQuality` (то же значение, что и `fileQuality`)
  * `imageScale` (то же значение, что и `fileScale`)
  * `imageMaxWidth` (то же значение, что и `fileMaxWidth`)


Сводка поведения режимов:

Режим | Что возвращается  
---|---  
`"view"` | Только поля просмотрщика.  
`"file"` | Только поля файла, без артефакта просмотрщика.  
`"both"` | Поля просмотрщика плюс поля файла. Если рендеринг файла завершается неудачей, просмотрщик все равно возвращается с псевдонимом `fileError` и `imageError`.  
  
## Свернутые неизмененные разделы

  * Средство просмотра может показывать строки вида `N unmodified lines`.
  * Элементы управления раскрытием для таких строк условны и не гарантируются для каждого вида ввода.
  * Элементы управления раскрытием появляются, когда отрисованный diff содержит данные раскрываемого контекста, что типично для ввода до и после.
  * Для многих входных данных в формате unified patch пропущенные тела контекста недоступны в разобранных hunks патча, поэтому строка может отображаться без элементов управления раскрытием. Это ожидаемое поведение.
  * `expandUnchanged` применяется только при наличии раскрываемого контекста.


## Настройки Plugin по умолчанию

Задайте настройки по умолчанию для всего plugin в `~/.openclaw/openclaw.json`:

json5Copy code
[code]
    {  plugins: {    entries: {      diffs: {        enabled: true,        config: {          defaults: {            fontFamily: "Fira Code",            fontSize: 15,            lineSpacing: 1.6,            layout: "unified",            showLineNumbers: true,            diffIndicators: "bars",            wordWrap: true,            background: true,            theme: "dark",            fileFormat: "png",            fileQuality: "standard",            fileScale: 2,            fileMaxWidth: 960,            mode: "both",            ttlSeconds: 21600,          },        },      },    },  },}
[/code]

Поддерживаемые настройки по умолчанию:

  * `fontFamily`
  * `fontSize`
  * `lineSpacing`
  * `layout`
  * `showLineNumbers`
  * `diffIndicators`
  * `wordWrap`
  * `background`
  * `theme`
  * `fileFormat`
  * `fileQuality`
  * `fileScale`
  * `fileMaxWidth`
  * `mode`
  * `ttlSeconds`


Явные параметры инструмента переопределяют эти настройки по умолчанию.

### Постоянная конфигурация URL средства просмотра

Резервное значение, принадлежащее Plugin, для возвращаемых ссылок средства просмотра, когда вызов инструмента не передает `baseUrl`. Должно быть `http` или `https`, без строки запроса/хэша.

json5Copy code
[code]
    {  plugins: {    entries: {      diffs: {        enabled: true,        config: {          viewerBaseUrl: "https://gateway.example.com/openclaw",        },      },    },  },}
[/code]

## Конфигурация безопасности

`false`: не-loopback-запросы к маршрутам средства просмотра отклоняются. `true`: удаленные средства просмотра разрешены, если токенизированный путь действителен.

json5Copy code
[code]
    {  plugins: {    entries: {      diffs: {        enabled: true,        config: {          security: {            allowRemoteViewer: false,          },        },      },    },  },}
[/code]

## Жизненный цикл и хранение артефактов

  * Артефакты хранятся во временной подпапке: `$TMPDIR/openclaw-diffs`.
  * Метаданные артефакта просмотрщика содержат: 
    * случайный ID артефакта (20 шестнадцатеричных символов)
    * случайный токен (48 шестнадцатеричных символов)
    * `createdAt` и `expiresAt`
    * сохраненный путь `viewer.html`
  * TTL артефакта по умолчанию составляет 30 минут, если не указан.
  * Максимально допустимый TTL просмотрщика составляет 6 часов.
  * Очистка запускается оппортунистически после создания артефакта.
  * Истекшие артефакты удаляются.
  * Резервная очистка удаляет устаревшие папки старше 24 часов, если метаданные отсутствуют.


## URL просмотрщика и сетевое поведение

Маршрут просмотрщика:

  * `/plugins/diffs/view/{artifactId}/{token}`


Ресурсы просмотрщика:

  * `/plugins/diffs/assets/viewer.js`
  * `/plugins/diffs/assets/viewer-runtime.js`
  * `/plugins/diffs-language-pack/assets/viewer.js`, когда diff использует язык из Diff Viewer Language Pack


Документ просмотрщика разрешает эти ресурсы относительно URL просмотрщика, поэтому необязательный префикс пути `baseUrl` также сохраняется для обоих запросов ресурсов.

Поведение построения URL:

  * Если в tool-call предоставлен `baseUrl`, он используется после строгой проверки.
  * Иначе, если настроен `viewerBaseUrl` плагина, используется он.
  * Без любого из этих переопределений URL просмотрщика по умолчанию указывает на loopback `127.0.0.1`.
  * Если режим привязки Gateway равен `custom` и задан `gateway.customBindHost`, используется этот хост.


Правила `baseUrl`:

  * Должен быть `http://` или `https://`.
  * Query и hash отклоняются.
  * Разрешены origin плюс необязательный базовый путь.


## Модель безопасности

Viewer hardening

  * По умолчанию только loopback.
  * Токенизированные пути просмотрщика со строгой проверкой ID и токена.
  * CSP ответа просмотрщика: 
    * `default-src 'none'`
    * скрипты и ресурсы только из self
    * без исходящих `connect-src`
  * Ограничение удаленных промахов при включенном удаленном доступе: 
    * 40 сбоев за 60 секунд
    * блокировка на 60 секунд (`429 Too Many Requests`)

File rendering hardening

  * Маршрутизация запросов браузера для скриншотов по умолчанию запрещающая.
  * Разрешены только локальные ресурсы просмотрщика из `http://127.0.0.1/plugins/diffs/assets/*`.
  * Внешние сетевые запросы блокируются.


## Требования браузера для файлового режима

`mode: "file"` и `mode: "both"` требуют Chromium-совместимый браузер.

Порядок разрешения:

* ### Config

`browser.executablePath` в конфигурации OpenClaw.

* ### Environment variables

  * `OPENCLAW_BROWSER_EXECUTABLE_PATH`
  * `BROWSER_EXECUTABLE_PATH`
  * `PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH`


* ### Platform fallback

Резервное обнаружение команды/пути платформы.

Распространенный текст ошибки:

  * `Diff PNG/PDF rendering requires a Chromium-compatible browser...`


Исправьте, установив Chrome, Chromium, Edge или Brave либо задав один из вариантов пути к исполняемому файлу выше.

## Устранение неполадок

Input validation errors

  * `Provide patch or both before and after text.` — укажите оба значения `before` и `after` или предоставьте `patch`.
  * `Provide either patch or before/after input, not both.` — не смешивайте режимы ввода.
  * `Invalid baseUrl: ...` — используйте origin `http(s)` с необязательным путем, без query/hash.
  * `{field} exceeds maximum size (...)` — уменьшите размер полезной нагрузки.
  * Отклонение большого patch — уменьшите количество файлов patch или общее число строк.

Viewer accessibility

  * URL просмотрщика по умолчанию разрешается в `127.0.0.1`.
  * Для сценариев удаленного доступа: 
    * задайте `viewerBaseUrl` плагина, или
    * передайте `baseUrl` для каждого вызова инструмента, или
    * используйте `gateway.bind=custom` и `gateway.customBindHost`
  * Если `gateway.trustedProxies` включает loopback для прокси на том же хосте (например, Tailscale Serve), необработанные loopback-запросы просмотрщика без перенаправленных заголовков client-IP завершаются отказом по замыслу.
  * Для такой топологии прокси: 
    * предпочитайте `mode: "file"` или `mode: "both"`, когда вам нужно только вложение, или
    * намеренно включите `security.allowRemoteViewer` и задайте `viewerBaseUrl` плагина либо передайте прокси/публичный `baseUrl`, когда нужен URL просмотрщика, которым можно поделиться
  * Включайте `security.allowRemoteViewer` только если вам намеренно нужен внешний доступ к просмотрщику.

Unmodified-lines row has no expand button

Это может происходить для ввода patch, когда patch не содержит разворачиваемого контекста. Это ожидаемо и не указывает на сбой просмотрщика.

Artifact not found

  * Срок действия артефакта истек из-за TTL.
  * Токен или путь изменился.
  * Очистка удалила устаревшие данные.


## Эксплуатационные рекомендации

  * Предпочитайте `mode: "view"` для локальных интерактивных ревью в canvas.
  * Предпочитайте `mode: "file"` для исходящих чат-каналов, которым нужно вложение.
  * Оставляйте `allowRemoteViewer` отключенным, если вашему развертыванию не требуются URL удаленного просмотрщика.
  * Задавайте явный короткий `ttlSeconds` для чувствительных diff.
  * Избегайте отправки секретов во входных данных diff, когда это не требуется.
  * Если ваш канал агрессивно сжимает изображения (например, Telegram или WhatsApp), предпочитайте вывод PDF (`fileFormat: "pdf"`).


## Связанные материалы

  * [Браузер](</ru/tools/browser>)
  * [Плагины](</ru/tools/plugin>)
  * [Обзор инструментов](</ru/tools>)


Was this useful?YesNo

Open issue