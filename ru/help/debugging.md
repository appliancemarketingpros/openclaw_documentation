---
title: Отладка
source_url: https://docs.openclaw.ai/ru/help/debugging
scraped_at: 2026-06-29
---

HelpStart here

Вспомогательные средства отладки для потокового вывода, особенно когда провайдер смешивает reasoning с обычным текстом.

## Отладочные переопределения runtime

Используйте `/debug` в чате, чтобы задать переопределения конфигурации **только для runtime** (в памяти, не на диске). `/debug` по умолчанию отключен; включите его с помощью `commands.debug: true`. Это удобно, когда нужно переключать редкие настройки без редактирования `openclaw.json`.

Примеры:

CodeCopy code
[code]
    /debug show/debug set messages.responsePrefix="[openclaw]"/debug unset messages.responsePrefix/debug reset
[/code]

`/debug reset` очищает все переопределения и возвращает конфигурацию с диска.

## Вывод трассировки сессии

Используйте `/trace`, когда хотите видеть принадлежащие Plugin строки трассировки/отладки в одной сессии без включения полного подробного режима.

Примеры:

textCopy code
[code]
    /trace/trace on/trace off
[/code]

Используйте `/trace` для диагностики Plugin, например отладочных сводок Active Memory. Продолжайте использовать `/verbose` для обычного подробного вывода статуса/инструментов, а `/debug` — для переопределений конфигурации только для runtime.

## Трассировка жизненного цикла Plugin

Используйте `OPENCLAW_PLUGIN_LIFECYCLE_TRACE=1`, когда команды жизненного цикла Plugin кажутся медленными и вам нужна встроенная разбивка по фазам для метаданных Plugin, обнаружения, реестра, runtime-зеркала, изменения конфигурации и обновления. Трассировка включается явно и пишет в stderr, поэтому JSON-вывод команды остается пригодным для разбора.

Пример:

bashCopy code
[code]
    OPENCLAW_PLUGIN_LIFECYCLE_TRACE=1 openclaw plugins install tokenjuice --force
[/code]

Пример вывода:

textCopy code
[code]
    [plugins:lifecycle] phase="config read" ms=6.83 status=ok command="install"[plugins:lifecycle] phase="slot selection" ms=94.31 status=ok command="install" pluginId="tokenjuice"[plugins:lifecycle] phase="registry refresh" ms=51.56 status=ok command="install" reason="source-changed"
[/code]

Используйте это для исследования жизненного цикла Plugin, прежде чем обращаться к CPU-профилировщику. Если команда запускается из исходного checkout, предпочтительно измерять собранный runtime с `node dist/entry.js ...` после `pnpm build`; `pnpm openclaw ...` также измеряет накладные расходы source-runner.

## Профилирование запуска CLI и команд

Используйте включенный в репозиторий бенчмарк запуска, когда команда кажется медленной:

bashCopy code
[code]
    pnpm test:startup:bench:smokepnpm tsx scripts/bench-cli-startup.ts --preset real --case status --runs 3pnpm tsx scripts/bench-cli-startup.ts --preset real --cpu-prof-dir .artifacts/cli-cpu
[/code]

Для разового профилирования через обычный source runner задайте `OPENCLAW_RUN_NODE_CPU_PROF_DIR`:

bashCopy code
[code]
    OPENCLAW_RUN_NODE_CPU_PROF_DIR=.artifacts/cli-cpu pnpm openclaw status
[/code]

Source runner добавляет флаги CPU-профиля Node и записывает `.cpuprofile` для команды. Используйте это перед добавлением временной инструментализации в код команды.

Для зависаний при запуске, похожих на синхронную работу файловой системы или загрузчика модулей, добавьте флаг трассировки синхронного I/O Node через source runner:

bashCopy code
[code]
    OPENCLAW_TRACE_SYNC_IO=1 pnpm openclaw gateway --force
[/code]

`pnpm gateway:watch` по умолчанию оставляет этот флаг отключенным для отслеживаемого дочернего процесса Gateway. Задайте `OPENCLAW_TRACE_SYNC_IO=1`, когда явно хотите получить вывод трассировки синхронного I/O Node в режиме наблюдения.

## Режим наблюдения Gateway

Для быстрой итерации запустите gateway под файловым наблюдателем:

bashCopy code
[code]
    pnpm gateway:watch
[/code]

По умолчанию это запускает или перезапускает сессию tmux с именем `openclaw-gateway-watch-main` (или вариант для профиля/порта, например `openclaw-gateway-watch-dev-19001`) и автоматически подключается из интерактивных терминалов. Неинтерактивные оболочки, CI и вызовы agent exec остаются отсоединенными и вместо этого печатают инструкции для подключения. При необходимости подключитесь вручную:

bashCopy code
[code]
    tmux attach -t openclaw-gateway-watch-main
[/code]

Панель tmux запускает сырой наблюдатель:

bashCopy code
[code]
    node scripts/watch-node.mjs gateway --force
[/code]

Используйте foreground-режим, когда tmux не нужен:

bashCopy code
[code]
    pnpm gateway:watch:raw# orOPENCLAW_GATEWAY_WATCH_TMUX=0 pnpm gateway:watch
[/code]

Отключите автоподключение, сохранив управление tmux:

bashCopy code
[code]
    OPENCLAW_GATEWAY_WATCH_ATTACH=0 pnpm gateway:watch
[/code]

Профилируйте CPU-время отслеживаемого Gateway при отладке узких мест запуска/runtime:

bashCopy code
[code]
    pnpm gateway:watch --benchmark
[/code]

Обертка наблюдателя поглощает `--benchmark` перед вызовом Gateway и записывает по одному V8 `.cpuprofile` при каждом завершении дочернего процесса Gateway в `.artifacts/gateway-watch-profiles/`. Остановите или перезапустите отслеживаемый gateway, чтобы сбросить текущий профиль, затем откройте его в Chrome DevTools или Speedscope:

bashCopy code
[code]
    npx speedscope .artifacts/gateway-watch-profiles/*.cpuprofile
[/code]

Используйте `--benchmark-dir <path>`, когда хотите хранить профили в другом месте. Используйте `--benchmark-no-force`, когда хотите, чтобы бенчмаркируемый дочерний процесс пропускал очистку порта по умолчанию через `--force` и быстро завершался с ошибкой, если порт Gateway уже используется. Режим бенчмарка по умолчанию подавляет шум трассировки sync-I/O. Задайте `OPENCLAW_TRACE_SYNC_IO=1` вместе с `--benchmark`, когда явно хотите получить и CPU-профили, и трассировки стеков sync-I/O Node. В режиме бенчмарка эти блоки трассировки записываются в `gateway-watch-output.log` в каталоге бенчмарка и отфильтровываются из панели терминала; обычные логи Gateway остаются видимыми.

Обертка tmux передает в панель обычные несекретные селекторы runtime, такие как `OPENCLAW_PROFILE`, `OPENCLAW_CONFIG_PATH`, `OPENCLAW_STATE_DIR`, `OPENCLAW_GATEWAY_PORT` и `OPENCLAW_SKIP_CHANNELS`. Храните учетные данные провайдеров в обычном профиле/конфигурации или используйте сырой foreground-режим для разовых эфемерных секретов. Если отслеживаемый Gateway завершается во время запуска, наблюдатель один раз запускает `openclaw doctor --fix --non-interactive` и перезапускает дочерний процесс Gateway. Используйте `OPENCLAW_GATEWAY_WATCH_AUTO_DOCTOR=0`, когда хотите увидеть исходный сбой запуска без dev-only прохода восстановления. Управляемая панель tmux также по умолчанию использует цветные логи Gateway для читаемости; задайте `FORCE_COLOR=0` при запуске `pnpm gateway:watch`, чтобы отключить ANSI-вывод.

Наблюдатель перезапускается при изменениях файлов, влияющих на сборку, в `src/`, исходных файлов расширений, метаданных `package.json` и `openclaw.plugin.json` расширений, `tsconfig.json`, `package.json` и `tsdown.config.ts`. Изменения метаданных расширений перезапускают gateway без принудительной пересборки `tsdown`; изменения исходников и конфигурации все еще сначала пересобирают `dist`.

Добавьте любые флаги CLI gateway после `gateway:watch`, и они будут передаваться при каждом перезапуске. Повторный запуск той же команды наблюдения пересоздает именованную панель tmux, а сырой наблюдатель все равно сохраняет блокировку единственного наблюдателя, поэтому дублирующиеся родительские процессы наблюдателя заменяются, а не накапливаются.

## Dev-профиль + dev-gateway (--dev)

Используйте dev-профиль, чтобы изолировать состояние и поднять безопасную одноразовую настройку для отладки. Есть **два** флага `--dev`:

  * **Глобальный`--dev` (профиль):** изолирует состояние в `~/.openclaw-dev` и по умолчанию задает порт gateway `19001` (производные порты сдвигаются вместе с ним).
  * **`gateway --dev`: сообщает Gateway, что нужно автоматически создать конфигурацию по умолчанию + workspace** при их отсутствии (и пропустить BOOTSTRAP.md).


Рекомендуемый поток (dev-профиль + dev-bootstrap):

bashCopy code
[code]
    pnpm gateway:devOPENCLAW_PROFILE=dev openclaw tui
[/code]

Если у вас еще нет глобальной установки, запускайте CLI через `pnpm openclaw ...`.

Что это делает:

  1. **Изоляция профиля** (глобальный `--dev`)

     * `OPENCLAW_PROFILE=dev`
     * `OPENCLAW_STATE_DIR=~/.openclaw-dev`
     * `OPENCLAW_CONFIG_PATH=~/.openclaw-dev/openclaw.json`
     * `OPENCLAW_GATEWAY_PORT=19001` (browser/canvas сдвигаются соответственно)
  2. **Dev-bootstrap** (`gateway --dev`)

     * Записывает минимальную конфигурацию, если ее нет (`gateway.mode=local`, привязка к loopback).
     * Задает `agent.workspace` как dev-workspace.
     * Задает `agent.skipBootstrap=true` (без BOOTSTRAP.md).
     * Создает начальные файлы workspace, если их нет: `AGENTS.md`, `SOUL.md`, `TOOLS.md`, `IDENTITY.md`, `USER.md`, `HEARTBEAT.md`.
     * Идентичность по умолчанию: **C3-PO** (протокольный дроид).
     * Пропускает провайдеры каналов в dev-режиме (`OPENCLAW_SKIP_CHANNELS=1`).


Поток сброса (чистый старт):

bashCopy code
[code]
    pnpm gateway:dev:reset
[/code]

`--reset` стирает конфигурацию, учетные данные, сессии и dev-workspace (используя `trash`, а не `rm`), затем заново создает dev-настройку по умолчанию.

## Логирование сырого потока (OpenClaw)

OpenClaw может логировать **сырой поток ассистента** до любой фильтрации/форматирования. Это лучший способ увидеть, приходит ли reasoning как обычные текстовые дельты (или как отдельные блоки thinking).

Включите это через CLI:

bashCopy code
[code]
    pnpm gateway:watch --raw-stream
[/code]

Необязательное переопределение пути:

bashCopy code
[code]
    pnpm gateway:watch --raw-stream --raw-stream-path ~/.openclaw/logs/raw-stream.jsonl
[/code]

Эквивалентные env vars:

bashCopy code
[code]
    OPENCLAW_RAW_STREAM=1OPENCLAW_RAW_STREAM_PATH=~/.openclaw/logs/raw-stream.jsonl
[/code]

Файл по умолчанию:

`~/.openclaw/logs/raw-stream.jsonl`

## Логирование сырых OpenAI-совместимых фрагментов

Чтобы захватывать **сырые OpenAI-совместимые фрагменты** до их разбора на блоки, включите transport-логгер:

bashCopy code
[code]
    OPENCLAW_RAW_STREAM=1
[/code]

Необязательный путь:

bashCopy code
[code]
    OPENCLAW_RAW_STREAM_PATH=~/.openclaw/logs/raw-openai-completions.jsonl
[/code]

Файл по умолчанию:

`~/.openclaw/logs/raw-openai-completions.jsonl`

## Примечания по безопасности

  * Логи сырого потока могут включать полные промпты, вывод инструментов и пользовательские данные.
  * Храните логи локально и удаляйте их после отладки.
  * Если вы делитесь логами, сначала удалите секреты и PII.


## Отладка в VSCode

Source maps необходимы для включения отладки в IDE на основе VSCode, потому что многие сгенерированные файлы получают хешированные имена как часть процесса сборки. Включенные конфигурации `launch.json` нацелены на сервис Gateway, но их можно быстро адаптировать для других целей:

  1. **Пересобрать и отладить Gateway** \- отлаживает сервис Gateway после создания новой сборки
  2. **Отладить Gateway** \- отлаживает сервис Gateway уже существующей сборки


### Настройка

Конфигурация **Пересобрать и отладить Gateway** по умолчанию поставляется со всем необходимым: она автоматически удалит папку `/dist` и пересоберет проект с включенной отладкой:

  1. Откройте панель **Run and Debug** из Activity Bar или нажмите `Ctrl`+`Shift`+`D`
  2. В IDE убедитесь, что в выпадающем списке конфигураций выбрано **Пересобрать и отладить Gateway** , затем нажмите кнопку **Start Debugging**


Альтернативно, если вы предпочитаете вручную управлять процессами сборки и отладки:

  1. Откройте терминал и включите source maps: 
     * **Linux/macOS** : `export OUTPUT_SOURCE_MAPS=1`
     * **Windows (PowerShell)** : `$env:OUTPUT_SOURCE_MAPS="1"`
     * **Windows (CMD)** : `set OUTPUT_SOURCE_MAPS=1`
  2. В том же терминале пересоберите проект: `pnpm clean:dist && pnpm build`
  3. В IDE выберите вариант **Отладить Gateway** в выпадающем списке конфигураций **Run and Debug** , затем нажмите кнопку **Start Debugging**


Теперь вы можете ставить точки останова в исходных файлах TypeScript (каталог `src/`), и отладчик будет корректно сопоставлять точки останова со скомпилированным JavaScript через source maps. Вы сможете просматривать переменные, выполнять код пошагово и изучать стеки вызовов как ожидается.

### Примечания

  * При использовании варианта **"Пересобрать и отладить Gateway"** каждый запуск отладчика будет полностью удалять папку `/dist` и выполнять полный `pnpm build` с включенными source maps перед запуском Gateway
  * При использовании варианта **"Отладить Gateway"** отладочные сессии можно запускать и останавливать в любое время без влияния на папку `/dist`, но для включения отладки и управления циклом сборки нужно использовать отдельный процесс терминала
  * Измените настройки `launch.json` для `args`, чтобы отлаживать другие разделы проекта
  * Если вам нужно использовать собранный OpenClaw CLI для других задач (например, `dashboard --no-open`, если ваша отладочная сессия создает новый auth token), вы можете выполнить его в другом терминале как `node ./openclaw.mjs` или создать shell alias вроде `alias openclaw-build="node $(pwd)/openclaw.mjs"`


## Связанные материалы

  * [Устранение неполадок](</ru/help/troubleshooting>)
  * [FAQ](</ru/help/faq>)


Was this useful?YesNo

Open issue