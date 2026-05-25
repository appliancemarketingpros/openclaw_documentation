---
title: Пакети Plugin
source_url: https://docs.openclaw.ai/uk/plugins/bundles
scraped_at: 2026-05-25
---

OpenClaw може встановлювати plugins із трьох зовнішніх екосистем: **Codex** , **Claude** і **Cursor**. Вони називаються **пакетами** — наборами контенту й метаданих, які OpenClaw відображає на нативні можливості, як-от skills, hooks і MCP tools.

## Навіщо потрібні пакети

Багато корисних plugins публікуються у форматі Codex, Claude або Cursor. Замість вимагати від авторів переписувати їх як нативні OpenClaw plugins, OpenClaw виявляє ці формати й відображає їхній підтримуваний контент на нативний набір можливостей. Це означає, що ви можете встановити пакет команд Claude або пакет навичок Codex і одразу ним користуватися.

## Установлення пакета

* ### Установлення з каталогу, архіву або marketplace

bashCopy code
[code]
    # Local directoryopenclaw plugins install ./my-bundle # Archiveopenclaw plugins install ./my-bundle.tgz # Claude marketplaceopenclaw plugins marketplace list <marketplace-name>openclaw plugins install <plugin-name>@<marketplace-name>
[/code]

* ### Перевірка виявлення

bashCopy code
[code]
    openclaw plugins listopenclaw plugins inspect <id>
[/code]

Пакети відображаються як `Format: bundle` із підтипом `codex`, `claude` або `cursor`.

* ### Перезапуск і використання

bashCopy code
[code]
    openclaw gateway restart
[/code]

Відображені можливості (skills, hooks, MCP tools, стандартні налаштування LSP) доступні в наступній сесії.

## Що OpenClaw відображає з пакетів

Сьогодні не кожна функція пакета запускається в OpenClaw. Нижче наведено, що працює, а що виявляється, але ще не під’єднано.

### Підтримується зараз

Функція | Як вона відображається | Застосовується до  
---|---|---  
Контент skills | Корені skills пакета завантажуються як звичайні OpenClaw skills | Усі формати  
Команди | `commands/` і `.cursor/commands/` обробляються як корені skills | Claude, Cursor  
Пакети hooks | Макети OpenClaw-стилю `HOOK.md` \+ `handler.ts` | Codex  
MCP tools | Конфігурація MCP пакета об’єднується з вбудованими налаштуваннями Pi; завантажуються підтримувані сервери stdio та HTTP | Усі формати  
LSP-сервери | Claude `.lsp.json` і оголошені в manifest `lspServers` об’єднуються зі стандартними налаштуваннями LSP вбудованого Pi | Claude  
Налаштування | Claude `settings.json` імпортується як стандартні налаштування вбудованого Pi | Claude  
  
#### Контент skills

  * корені skills пакета завантажуються як звичайні корені OpenClaw skills
  * корені Claude `commands` обробляються як додаткові корені skills
  * корені Cursor `.cursor/commands` обробляються як додаткові корені skills


Це означає, що markdown-файли команд Claude працюють через звичайний завантажувач OpenClaw skills. Markdown-команди Cursor працюють тим самим шляхом.

#### Пакети hooks

  * корені hooks пакета працюють **лише** тоді, коли використовують звичайний макет OpenClaw hook-pack. Сьогодні це переважно випадок, сумісний із Codex: 
    * `HOOK.md`
    * `handler.ts` або `handler.js`


#### MCP для Pi

  * увімкнені пакети можуть додавати конфігурацію MCP-сервера
  * OpenClaw об’єднує конфігурацію MCP пакета з ефективними налаштуваннями вбудованого Pi як `mcpServers`
  * OpenClaw надає підтримувані MCP tools пакета під час ходів агента вбудованого Pi, запускаючи stdio-сервери або підключаючись до HTTP-серверів
  * профілі інструментів `coding` і `messaging` за замовчуванням включають MCP tools пакета; використовуйте `tools.deny: ["bundle-mcp"]`, щоб вимкнути їх для агента або gateway
  * локальні налаштування Pi проєкту все ще застосовуються після стандартних налаштувань пакета, тому налаштування робочої області можуть перевизначати записи MCP пакета за потреби
  * каталоги MCP tools пакета перед реєстрацією сортуються детерміновано, тому зміни порядку upstream `listTools()` не перетасовують блоки інструментів кешу prompt-cache


##### Транспорти

MCP-сервери можуть використовувати транспорт stdio або HTTP:

**Stdio** запускає дочірній процес:

jsonCopy code
[code]
    {  "mcp": {    "servers": {      "my-server": {        "command": "node",        "args": ["server.js"],        "env": { "PORT": "3000" }      }    }  }}
[/code]

**HTTP** за замовчуванням підключається до запущеного MCP-сервера через `sse` або через `streamable-http`, якщо це задано:

jsonCopy code
[code]
    {  "mcp": {    "servers": {      "my-server": {        "url": "http://localhost:3100/mcp",        "transport": "streamable-http",        "headers": {          "Authorization": "Bearer ${MY_SECRET_TOKEN}"        },        "connectionTimeoutMs": 30000      }    }  }}
[/code]

  * `transport` можна встановити як `"streamable-http"` або `"sse"`; якщо пропущено, OpenClaw використовує `sse`
  * `type: "http"` — це downstream-форма, нативна для CLI; використовуйте `transport: "streamable-http"` у конфігурації OpenClaw. `openclaw mcp set` і `openclaw doctor --fix` нормалізують поширений псевдонім.
  * дозволені лише схеми URL `http:` і `https:`
  * значення `headers` підтримують інтерполяцію `${ENV_VAR}`
  * запис сервера з одночасно заданими `command` і `url` відхиляється
  * облікові дані URL (userinfo та параметри запиту) редагуються з описів tools і журналів
  * `connectionTimeoutMs` перевизначає стандартний 30-секундний тайм-аут підключення для транспортів stdio і HTTP


##### Іменування tools

OpenClaw реєструє MCP tools пакета з безпечними для провайдера іменами у формі `serverName__toolName`. Наприклад, сервер із ключем `"vigil-harbor"`, який надає інструмент `memory_search`, реєструється як `vigil-harbor__memory_search`.

  * символи поза `A-Za-z0-9_-` замінюються на `-`
  * фрагменти, які починалися б не з літери, отримують літерний префікс, тому числові ключі серверів, як-от `12306`, стають безпечними для провайдера префіксами tools
  * префікси серверів обмежено 30 символами
  * повні імена tools обмежено 64 символами
  * порожні імена серверів відступають до `mcp`
  * зіткнення санітизованих імен розрізняються числовими суфіксами
  * фінальний порядок наданих tools є детермінованим за безпечним іменем, щоб повторювані ходи Pi лишалися стабільними для кешу
  * фільтрація профілю обробляє всі tools з одного MCP-сервера пакета як належні Plugin `bundle-mcp`, тому allowlists і deny lists профілів можуть включати або окремі надані імена tools, або ключ Plugin `bundle-mcp`


#### Налаштування вбудованого Pi

  * Claude `settings.json` імпортується як стандартні налаштування вбудованого Pi, коли пакет увімкнено
  * OpenClaw санітизує ключі перевизначення shell перед їх застосуванням


Санітизовані ключі:

  * `shellPath`
  * `shellCommandPrefix`


#### LSP вбудованого Pi

  * увімкнені пакети Claude можуть додавати конфігурацію LSP-сервера
  * OpenClaw завантажує `.lsp.json` плюс будь-які оголошені в manifest шляхи `lspServers`
  * конфігурація LSP пакета об’єднується з ефективними стандартними налаштуваннями LSP вбудованого Pi
  * сьогодні запускати можна лише підтримувані LSP-сервери на основі stdio; непідтримувані транспорти все одно показуються в `openclaw plugins inspect <id>`


### Виявляється, але не виконується

Вони розпізнаються й показуються в діагностиці, але OpenClaw їх не запускає:

  * Claude `agents`, автоматизація `hooks.json`, `outputStyles`
  * Cursor `.cursor/agents`, `.cursor/hooks.json`, `.cursor/rules`
  * inline/app-метадані Codex поза звітуванням про можливості


## Формати пакетів

Пакети Codex

Маркери: `.codex-plugin/plugin.json`

Необов’язковий контент: `skills/`, `hooks/`, `.mcp.json`, `.app.json`

Пакети Codex найкраще пасують OpenClaw, коли використовують корені skills і каталоги hook-pack у стилі OpenClaw (`HOOK.md` \+ `handler.ts`).

Пакети Claude

Два режими виявлення:

  * **На основі manifest:** `.claude-plugin/plugin.json`
  * **Без manifest:** стандартний макет Claude (`skills/`, `commands/`, `agents/`, `hooks/`, `.mcp.json`, `.lsp.json`, `settings.json`)


Специфічна для Claude поведінка:

  * `commands/` обробляється як контент skills
  * `settings.json` імпортується в налаштування вбудованого Pi (ключі перевизначення shell санітизуються)
  * `.mcp.json` надає підтримувані stdio tools вбудованому Pi
  * `.lsp.json` плюс оголошені в manifest шляхи `lspServers` завантажуються у стандартні налаштування LSP вбудованого Pi
  * `hooks/hooks.json` виявляється, але не виконується
  * користувацькі шляхи компонентів у manifest є додатковими (вони розширюють стандартні, а не замінюють їх)

Пакети Cursor

Маркери: `.cursor-plugin/plugin.json`

Необов’язковий контент: `skills/`, `.cursor/commands/`, `.cursor/agents/`, `.cursor/rules/`, `.cursor/hooks.json`, `.mcp.json`

  * `.cursor/commands/` обробляється як контент skills
  * `.cursor/rules/`, `.cursor/agents/` і `.cursor/hooks.json` лише виявляються


## Пріоритет виявлення

OpenClaw спочатку перевіряє нативний формат Plugin:

  1. `openclaw.plugin.json` або чинний `package.json` з `openclaw.extensions` — обробляється як **нативний Plugin**
  2. Маркери пакета (`.codex-plugin/`, `.claude-plugin/` або стандартний макет Claude/Cursor) — обробляється як **пакет**


Якщо каталог містить обидва варіанти, OpenClaw використовує нативний шлях. Це запобігає частковому встановленню двоформатних пакетів як пакетів.

## Runtime-залежності та очищення

  * Сумісні пакети сторонніх розробників не отримують startup-виправлення `npm install`. Їх слід установлювати через `openclaw plugins install` і постачати все необхідне в установленому каталозі Plugin.
  * Plugins у пакетах, які належать OpenClaw, або постачаються полегшено в core, або завантажуються через інсталятор plugins. Під час запуску Gateway для них ніколи не запускається package manager.
  * `openclaw doctor --fix` видаляє застарілі staged-каталоги залежностей і може відновлювати завантажувані plugins, яких бракує в локальному індексі plugins, коли конфігурація посилається на них.


## Безпека

Пакети мають вужчу межу довіри, ніж нативні plugins:

  * OpenClaw **не** завантажує довільні runtime-модулі пакета в процес
  * Шляхи Skills і hook-pack мають залишатися всередині кореня Plugin (із перевіркою межі)
  * Файли налаштувань читаються з тими самими перевірками межі
  * Підтримувані stdio MCP-сервери можуть запускатися як subprocesses


Це робить пакети безпечнішими за замовчуванням, але все одно слід розглядати сторонні пакети як довірений контент для функцій, які вони надають.

## Усунення неполадок

Пакет виявлено, але можливості не запускаються

Запустіть `openclaw plugins inspect <id>`. Якщо можливість наведена в списку, але позначена як не під’єднана, це обмеження продукту — не зламане встановлення.

Файли команд Claude не з’являються

Переконайтеся, що пакет увімкнено, а markdown-файли розташовані всередині виявленого кореня `commands/` або `skills/`.

Налаштування Claude не застосовуються

Підтримуються лише налаштування вбудованого Pi з `settings.json`. OpenClaw не обробляє налаштування пакета як сирі config patches.

Hooks Claude не виконуються

`hooks/hooks.json` лише виявляється. Якщо вам потрібні hooks, які можна запускати, використовуйте макет OpenClaw hook-pack або постачайте нативний Plugin.

## Пов’язане

  * [Установлення та налаштування Plugins](</uk/tools/plugin>)
  * [Створення Plugins](</uk/plugins/building-plugins>) — створення нативного Plugin
  * [Manifest Plugin](</uk/plugins/manifest>) — схема нативного manifest


Was this useful?YesNo