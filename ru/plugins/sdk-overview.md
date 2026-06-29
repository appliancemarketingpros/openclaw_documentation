---
title: Обзор Plugin SDK
source_url: https://docs.openclaw.ai/ru/plugins/sdk-overview
scraped_at: 2026-06-29
---

ReferencePlugin SDK reference

Plugin SDK — это типизированный контракт между плагинами и core. Эта страница — справочник по тому, **что импортировать** и **что можно регистрировать**.

## Соглашение об импорте

Всегда импортируйте из конкретного подпути:

typescriptCopy code
[code]
      
[/code]

Каждый подпуть — это небольшой самодостаточный модуль. Это ускоряет запуск и предотвращает проблемы с циклическими зависимостями. Для entry/build-хелперов, специфичных для каналов, предпочитайте `openclaw/plugin-sdk/channel-core`; оставляйте `openclaw/plugin-sdk/core` для более широкой зонтичной поверхности и общих хелперов, таких как `buildChannelConfigSchema`.

Для конфигурации канала публикуйте принадлежащую каналу JSON Schema через `openclaw.plugin.json#channelConfigs`. Подпуть `plugin-sdk/channel-config-schema` предназначен для общих примитивов схемы и универсального builder. Встроенные плагины OpenClaw используют `plugin-sdk/bundled-channel-config-schema` для сохраненных схем встроенных каналов. Устаревшие экспорты совместимости остаются в `plugin-sdk/channel-config-schema-legacy`; ни один подпуть встроенных схем не является шаблоном для новых плагинов.

## Справочник подпутей

Plugin SDK предоставляется как набор узких подпутей, сгруппированных по областям (entry плагина, канал, провайдер, аутентификация, runtime, capability, память и зарезервированные хелперы встроенных плагинов). Полный каталог — сгруппированный и со ссылками — см. в [подпутях Plugin SDK](</ru/plugins/sdk-subpaths>).

Инвентарь entrypoint компилятора находится в `scripts/lib/plugin-sdk-entrypoints.json`; экспорты пакета генерируются из публичного подмножества после вычитания repo-local тестовых/внутренних подпутей, перечисленных в `scripts/lib/plugin-sdk-private-local-only-subpaths.json`. Запустите `pnpm plugin-sdk:surface`, чтобы проверить количество публичных экспортов. Устаревшие публичные подпути, которые достаточно стары и не используются production-кодом встроенных расширений, отслеживаются в `scripts/lib/plugin-sdk-deprecated-public-subpaths.json`; широкие устаревшие re-export barrel-файлы отслеживаются в `scripts/lib/plugin-sdk-deprecated-barrel-subpaths.json`.

## API регистрации

Callback `register(api)` получает объект `OpenClawPluginApi` со следующими методами:

### Регистрация capability

Метод | Что регистрирует  
---|---  
`api.registerProvider(...)` | Текстовый inference (LLM)  
`api.registerAgentHarness(...)` | Экспериментальный низкоуровневый исполнитель агента  
`api.registerCliBackend(...)` | Локальный CLI-бэкенд inference  
`api.registerChannel(...)` | Канал обмена сообщениями  
`api.registerEmbeddingProvider(...)` | Переиспользуемый провайдер векторных embeddings  
`api.registerSpeechProvider(...)` | Синтез text-to-speech / STT  
`api.registerRealtimeTranscriptionProvider(...)` | Потоковая realtime-транскрипция  
`api.registerRealtimeVoiceProvider(...)` | Duplex realtime-голосовые сессии  
`api.registerMediaUnderstandingProvider(...)` | Анализ изображений/аудио/видео  
`api.registerImageGenerationProvider(...)` | Генерация изображений  
`api.registerMusicGenerationProvider(...)` | Генерация музыки  
`api.registerVideoGenerationProvider(...)` | Генерация видео  
`api.registerWebFetchProvider(...)` | Провайдер web fetch / scrape  
`api.registerWebSearchProvider(...)` | Web search  
  
Embedding-провайдеры, зарегистрированные через `api.registerEmbeddingProvider(...)`, также должны быть перечислены в `contracts.embeddingProviders` в манифесте плагина. Это универсальная поверхность embeddings для переиспользуемой генерации векторов. Поиск в памяти может использовать эту универсальную поверхность провайдера. Более старая seam `api.registerMemoryEmbeddingProvider(...)` и `contracts.memoryEmbeddingProviders` является устаревшей совместимостью, пока существующие memory-specific провайдеры мигрируют.

Memory-specific провайдеры, которые все еще предоставляют runtime `batchEmbed(...)`, остаются на существующем per-file batching contract, если их runtime явно не задает `sourceWideBatchEmbed: true`. Этот opt-in позволяет host памяти отправлять чанки из нескольких dirty memory files и включенных источников в одном вызове `batchEmbed(...)` до batch-лимитов host. Batch-адаптеры, которые загружают JSONL-файлы запросов, должны разделять задания провайдера до достижения как лимита размера загрузки, так и лимита количества запросов. Провайдер должен вернуть один embedding на каждый входной чанк в том же порядке, что и `batch.chunks`; не указывайте флаг, если провайдер ожидает file-local batches или не может сохранить порядок входных данных в более крупном source-wide задании.

### Инструменты и команды

Используйте [`defineToolPlugin`](</ru/plugins/tool-plugins>) для простых плагинов только с инструментами и фиксированными именами инструментов. Используйте `api.registerTool(...)` напрямую для смешанных плагинов или полностью динамической регистрации инструментов.

Метод | Что регистрирует  
---|---  
`api.registerTool(tool, opts?)` | Инструмент агента (обязательный или `{ optional: true }`)  
`api.registerCommand(def)` | Пользовательская команда (обходит LLM)  
  
Команды плагинов могут задавать `agentPromptGuidance`, когда агенту нужна короткая, принадлежащая команде подсказка маршрутизации. Держите этот текст о самой команде; не добавляйте provider- или plugin-specific policy в prompt builders core.

Guidance entries могут быть legacy-строками, применяемыми ко всем prompt surfaces, или структурированными entries:

tsCopy code
[code]
    agentPromptGuidance: [  "Global command hint.",  { text: "Only show this in the main OpenClaw prompt.", surfaces: ["openclaw_main"] },];
[/code]

Структурированные `surfaces` могут включать `openclaw_main`, `codex_app_server`, `cli_backend`, `acp_backend` или `subagent`. `pi_main` остается устаревшим alias для `openclaw_main`. Опускайте `surfaces` для намеренного guidance на всех surface. Не передавайте пустой массив `surfaces`; он отклоняется, чтобы случайная потеря scope не стала глобальным prompt text.

Developer instructions нативного Codex app-server строже, чем другие prompt surfaces: только guidance, явно scoped на `codex_app_server`, продвигается в этот более приоритетный lane. Legacy string guidance и unscoped structured guidance остаются доступны для non-Codex prompt surfaces ради совместимости.

### Инфраструктура

Метод | Что регистрирует  
---|---  
`api.registerHook(events, handler, opts?)` | Event hook  
`api.registerHttpRoute(params)` | HTTP endpoint Gateway  
`api.registerGatewayMethod(name, handler)` | RPC method Gateway  
`api.registerGatewayDiscoveryService(service)` | Local Gateway discovery advertiser  
`api.registerCli(registrar, opts?)` | CLI subcommand  
`api.registerNodeCliFeature(registrar, opts?)` | CLI-функция Node в `openclaw nodes`  
`api.registerService(service)` | Фоновый сервис  
`api.registerInteractiveHandler(registration)` | Интерактивный handler  
`api.registerAgentToolResultMiddleware(...)` | Runtime middleware для результатов инструментов  
`api.registerMemoryPromptSupplement(builder)` | Additive memory-adjacent prompt section  
`api.registerMemoryCorpusSupplement(adapter)` | Additive memory search/read corpus  
  
### Host hooks для workflow-плагинов

Host hooks — это seams SDK для плагинов, которым нужно участвовать в lifecycle host, а не только добавлять провайдера, канал или инструмент. Это универсальные контракты; Plan Mode может использовать их, но так же могут approval workflows, workspace policy gates, фоновые мониторы, мастера настройки и UI companion plugins.

Метод | Контракт, за который он отвечает  
---|---  
`api.session.state.registerSessionExtension(...)` | Принадлежащее Plugin, JSON-совместимое состояние сеанса, проецируемое через сеансы Gateway  
`api.session.workflow.enqueueNextTurnInjection(...)` | Долговечный контекст с семантикой exactly-once, внедряемый в следующий ход агента для одного сеанса  
`api.registerTrustedToolPolicy(...)` | Доверенная политика инструмента до Plugin, ограниченная манифестом, которая может блокировать или переписывать параметры инструмента  
`api.registerToolMetadata(...)` | Отображаемые метаданные каталога инструментов без изменения реализации инструмента  
`api.registerCommand(...)` | Команды Plugin с ограниченной областью действия; результаты команд могут задавать `continueAgent: true`; нативные команды Discord поддерживают `descriptionLocalizations`  
`api.session.controls.registerControlUiDescriptor(...)` | Дескрипторы вкладов Control UI для поверхностей сеанса, инструмента, запуска или настроек  
`api.lifecycle.registerRuntimeLifecycle(...)` | Обратные вызовы очистки для принадлежащих Plugin runtime-ресурсов на путях сброса/удаления/перезагрузки  
`api.agent.events.registerAgentEventSubscription(...)` | Санитизированные подписки на события для состояния рабочего процесса и мониторов  
`api.runContext.setRunContext(...)` / `getRunContext(...)` / `clearRunContext(...)` | Черновое состояние Plugin для отдельного запуска, очищаемое при терминальном жизненном цикле запуска  
`api.session.workflow.registerSessionSchedulerJob(...)` | Метаданные очистки для принадлежащих Plugin заданий планировщика; не планирует работу и не создает записи задач  
`api.session.workflow.sendSessionAttachment(...)` | Только для bundled: доставка файловых вложений через хост в активный прямой исходящий маршрут сеанса  
`api.session.workflow.scheduleSessionTurn(...)` / `unscheduleSessionTurnsByTag(...)` | Только для bundled: запланированные ходы сеанса на базе Cron плюс очистка по тегам  
`api.session.controls.registerSessionAction(...)` | Типизированные действия сеанса, которые клиенты могут отправлять через Gateway  
  
Используйте сгруппированные пространства имен для нового кода Plugin:

  * `api.session.state.registerSessionExtension(...)`
  * `api.session.workflow.enqueueNextTurnInjection(...)`
  * `api.session.workflow.registerSessionSchedulerJob(...)`
  * `api.session.workflow.sendSessionAttachment(...)`
  * `api.session.workflow.scheduleSessionTurn(...)`
  * `api.session.workflow.unscheduleSessionTurnsByTag(...)`
  * `api.session.controls.registerSessionAction(...)`
  * `api.session.controls.registerControlUiDescriptor(...)`
  * `api.agent.events.registerAgentEventSubscription(...)`
  * `api.agent.events.emitAgentEvent(...)`
  * `api.runContext.setRunContext(...)` / `getRunContext(...)` / `clearRunContext(...)`
  * `api.lifecycle.registerRuntimeLifecycle(...)`


Эквивалентные плоские методы остаются доступными как устаревшие алиасы совместимости для существующих plugins. Не добавляйте новый код Plugin, который напрямую вызывает `api.registerSessionExtension`, `api.enqueueNextTurnInjection`, `api.registerControlUiDescriptor`, `api.registerRuntimeLifecycle`, `api.registerAgentEventSubscription`, `api.emitAgentEvent`, `api.setRunContext`, `api.getRunContext`, `api.clearRunContext`, `api.registerSessionSchedulerJob`, `api.registerSessionAction`, `api.sendSessionAttachment`, `api.scheduleSessionTurn` или `api.unscheduleSessionTurnsByTag`.

`scheduleSessionTurn(...)` — это удобная обертка с областью действия сеанса над планировщиком Gateway Cron. Cron отвечает за время выполнения и создает запись фоновой задачи, когда ход запускается; Plugin SDK только ограничивает целевой сеанс, принадлежащее Plugin именование и очистку. Используйте `api.runtime.tasks.managedFlows` внутри запланированного хода, когда самой работе требуется долговечное многоэтапное состояние Task Flow.

Контракты намеренно разделяют полномочия:

  * Внешние plugins могут владеть расширениями сеанса, дескрипторами UI, командами, метаданными инструментов, внедрениями в следующий ход и обычными хуками.
  * Доверенные политики инструментов выполняются до обычных хуков `before_tool_call` и являются доверенными со стороны хоста. Bundled-политики выполняются первыми; политики установленных plugins требуют явного включения, а также их локальных идентификаторов в `contracts.trustedToolPolicies`, и выполняются следующими в порядке загрузки plugins. Идентификаторы политик ограничены регистрирующим Plugin.
  * Зарезервированное владение командами доступно только для bundled. Внешним plugins следует использовать собственные имена команд или алиасы.
  * `allowPromptInjection=false` отключает хуки, изменяющие prompt, включая `agent_turn_prepare`, `before_prompt_build`, `heartbeat_prompt_contribution`, поля prompt из устаревшего `before_agent_start` и `enqueueNextTurnInjection`.


Примеры потребителей, не относящихся к Plan:

Архетип Plugin | Используемые хуки  
---|---  
Рабочий процесс утверждения | Расширение сеанса, продолжение команды, внедрение в следующий ход, дескриптор UI  
Шлюз политики бюджета/рабочего пространства | Доверенная политика инструмента, метаданные инструмента, проекция сеанса  
Фоновый монитор жизненного цикла | Очистка жизненного цикла runtime, подписка на события агента, владение/очистка планировщика сеанса, вклад heartbeat prompt, дескриптор UI  
Мастер настройки или онбординга | Расширение сеанса, команды с ограниченной областью действия, дескриптор Control UI  
  
When to use tool-result middleware

Bundled plugins и явно включенные установленные plugins с соответствующими контрактами манифеста могут использовать `api.registerAgentToolResultMiddleware(...)`, когда им нужно переписать результат инструмента после выполнения и до того, как runtime передаст этот результат обратно модели. Это доверенная runtime-нейтральная граница для асинхронных редукторов вывода, таких как tokenjuice.

Plugins должны объявлять `contracts.agentToolResultMiddleware` для каждого целевого runtime, например `["openclaw", "codex"]`. Установленные plugins без этого контракта или без явного включения не могут регистрировать это middleware; сохраняйте обычные хуки OpenClaw Plugin для работы, которой не требуется момент обработки результата инструмента до передачи модели. Старый путь регистрации фабрики расширений только для встроенного runner удален.

### Регистрация обнаружения Gateway

`api.registerGatewayDiscoveryService(...)` позволяет Plugin объявлять активный Gateway в локальном транспорте обнаружения, таком как mDNS/Bonjour. OpenClaw вызывает сервис во время запуска Gateway, когда локальное обнаружение включено, передает текущие порты Gateway и несекретные TXT-данные подсказок, а при остановке Gateway вызывает возвращенный обработчик `stop`.

typescriptCopy code
[code]
    api.registerGatewayDiscoveryService({  id: "my-discovery",  async advertise(ctx) {    const handle = await startMyAdvertiser({      gatewayPort: ctx.gatewayPort,      tls: ctx.gatewayTlsEnabled,      displayName: ctx.machineDisplayName,    });    return { stop: () => handle.stop() };  },});
[/code]

Plugins обнаружения Gateway не должны считать объявляемые TXT-значения секретами или аутентификацией. Обнаружение — это подсказка для маршрутизации; доверие по-прежнему принадлежит аутентификации Gateway и TLS pinning.

### Метаданные регистрации CLI

`api.registerCli(registrar, opts?)` принимает два вида метаданных команд:

  * `commands`: явные имена команд, принадлежащие регистратору
  * `descriptors`: дескрипторы команд времени разбора, используемые для справки CLI, маршрутизации и ленивой регистрации CLI Plugin
  * `parentPath`: необязательный путь родительской команды для вложенных групп команд, например `["nodes"]`


Для функций paired-node предпочитайте `api.registerNodeCliFeature(registrar, opts?)`. Это небольшая обертка вокруг `api.registerCli(..., { parentPath: ["nodes"] })`, которая делает команды вроде `openclaw nodes canvas` явными node-функциями, принадлежащими Plugin.

Если вы хотите, чтобы команда Plugin оставалась лениво загружаемой в обычном корневом пути CLI, предоставьте `descriptors`, которые покрывают каждый корневой top-level command, раскрываемый этим регистратором.

typescriptCopy code
[code]
    api.registerCli(  async ({ program }) => {    const { registerMatrixCli } = await import("./src/cli.js");    registerMatrixCli({ program });  },  {    descriptors: [      {        name: "matrix",        description: "Manage Matrix accounts, verification, devices, and profile state",        hasSubcommands: true,      },    ],  },);
[/code]

Вложенные команды получают разрешенную родительскую команду как `program`:

typescriptCopy code
[code]
    api.registerCli(  async ({ program }) => {    const { registerNodesCanvasCommands } = await import("./src/cli.js");    registerNodesCanvasCommands(program);  },  {    parentPath: ["nodes"],    descriptors: [      {        name: "canvas",        description: "Capture or render canvas content from a paired node",        hasSubcommands: true,      },    ],  },);
[/code]

Используйте `commands` отдельно только тогда, когда вам не нужна ленивая корневая регистрация CLI. Этот энергичный путь совместимости остается поддерживаемым, но он не устанавливает placeholders на базе дескрипторов для ленивой загрузки во время разбора.

### Регистрация backend CLI

`api.registerCliBackend(...)` позволяет Plugin владеть конфигурацией по умолчанию для локального AI CLI backend, такого как `claude-cli` или `my-cli`.

  * `id` backend становится префиксом provider в ссылках на модели вроде `my-cli/gpt-5`.
  * `config` backend использует ту же форму, что и `agents.defaults.cliBackends.<id>`.
  * Пользовательская конфигурация по-прежнему имеет приоритет. OpenClaw объединяет `agents.defaults.cliBackends.<id>` поверх значения по умолчанию от Plugin перед запуском CLI.
  * Используйте `normalizeConfig`, когда backend нужны переписывания совместимости после слияния (например, нормализация старых форм флагов).
  * Используйте `resolveExecutionArgs` для переписывания argv в области запроса, относящегося к диалекту CLI, например для сопоставления уровней thinking OpenClaw с нативным флагом effort. Хук получает `ctx.executionMode`; используйте `"side-question"`, чтобы добавить backend-native флаги изоляции для эфемерных вызовов `/btw`. Если эти флаги надежно отключают нативные инструменты для CLI, который иначе всегда их включает, также объявите `sideQuestionToolMode: "disabled"`.


Полное руководство по созданию см. в [plugins backend CLI](</ru/plugins/cli-backend-plugins>).

### Эксклюзивные слоты

Метод | Что он регистрирует  
---|---  
`api.registerContextEngine(id, factory)` | Движок контекста (один активен в каждый момент времени). Обратные вызовы жизненного цикла получают `runtimeSettings`, когда хост может предоставить диагностику модели/провайдера/режима; более старые строгие движки повторно вызываются без этого ключа.  
`api.registerMemoryCapability(capability)` | Унифицированная возможность памяти  
`api.registerMemoryPromptSection(builder)` | Построитель секции памяти в промпте  
`api.registerMemoryFlushPlan(resolver)` | Резолвер плана сброса памяти  
`api.registerMemoryRuntime(runtime)` | Адаптер среды выполнения памяти  
  
### Устаревшие адаптеры эмбеддингов памяти

Метод | Что он регистрирует  
---|---  
`api.registerMemoryEmbeddingProvider(adapter)` | Адаптер эмбеддингов памяти для активного Plugin  
  
  * `registerMemoryCapability` — предпочтительный эксклюзивный API Plugin памяти.
  * `registerMemoryCapability` также может предоставлять `publicArtifacts.listArtifacts(...)`, чтобы сопутствующие Plugin могли потреблять экспортированные артефакты памяти через `openclaw/plugin-sdk/memory-host-core`, не обращаясь к приватной структуре конкретного Plugin памяти.
  * `registerMemoryPromptSection`, `registerMemoryFlushPlan` и `registerMemoryRuntime` — эксклюзивные API Plugin памяти с поддержкой устаревшей совместимости.
  * `MemoryFlushPlan.model` может закрепить ход сброса за точной ссылкой `provider/model`, например `ollama/qwen3:8b`, без наследования активной цепочки fallback.
  * `registerMemoryEmbeddingProvider` устарел. Новым провайдерам эмбеддингов следует использовать `api.registerEmbeddingProvider(...)` и `contracts.embeddingProviders`.
  * Существующие провайдеры, специфичные для памяти, продолжают работать в течение окна миграции, но инспекция Plugin сообщает об этом как о долге совместимости для невстроенных Plugin.


### События и жизненный цикл

Метод | Что он делает  
---|---  
`api.on(hookName, handler, opts?)` | Типизированный хук жизненного цикла  
`api.onConversationBindingResolved(handler)` | Обратный вызов привязки разговора  
  
См. [хуки Plugin](</ru/plugins/hooks>) с примерами, распространенными именами хуков и семантикой защитных условий.

### Семантика решений хуков

`before_install` — это хук жизненного цикла среды выполнения Plugin, а не поверхность политики установки оператора. Используйте `security.installPolicy`, когда решение разрешить/заблокировать должно охватывать пути установки или обновления через CLI и Gateway.

  * `before_tool_call`: возврат `{ block: true }` является терминальным. Как только любой обработчик устанавливает его, обработчики с более низким приоритетом пропускаются.
  * `before_tool_call`: возврат `{ block: false }` трактуется как отсутствие решения (то же, что и пропуск `block`), а не как переопределение.
  * `before_install`: возврат `{ block: true }` является терминальным. Как только любой обработчик устанавливает его, обработчики с более низким приоритетом пропускаются.
  * `before_install`: возврат `{ block: false }` трактуется как отсутствие решения (то же, что и пропуск `block`), а не как переопределение.
  * `reply_dispatch`: возврат `{ handled: true, ... }` является терминальным. Как только любой обработчик берет отправку на себя, обработчики с более низким приоритетом и стандартный путь отправки в модель пропускаются.
  * `message_sending`: возврат `{ cancel: true }` является терминальным. Как только любой обработчик устанавливает его, обработчики с более низким приоритетом пропускаются.
  * `message_sending`: возврат `{ cancel: false }` трактуется как отсутствие решения (то же, что и пропуск `cancel`), а не как переопределение.
  * `message_received`: используйте типизированное поле `threadId`, когда нужна маршрутизация входящих потоков/тем. Оставляйте `metadata` для дополнительных данных, специфичных для канала.
  * `message_sending`: используйте типизированные поля маршрутизации `replyToId` / `threadId` перед переходом к специфичным для канала `metadata`.
  * `gateway_start`: используйте `ctx.config`, `ctx.workspaceDir` и `ctx.getCron?.()` для состояния запуска, принадлежащего Gateway, вместо опоры на внутренние хуки `gateway:startup`.
  * `cron_changed`: наблюдайте за изменениями жизненного цикла Cron, принадлежащего Gateway. Используйте `event.job?.state?.nextRunAtMs` и `ctx.getCron?.()` при синхронизации внешних планировщиков пробуждения, и оставляйте OpenClaw источником истины для проверок наступления срока и выполнения.


### Поля объекта API

Поле | Тип | Описание  
---|---|---  
`api.id` | `string` | Идентификатор Plugin  
`api.name` | `string` | Отображаемое имя  
`api.version` | `string?` | Версия Plugin (необязательно)  
`api.description` | `string?` | Описание Plugin (необязательно)  
`api.source` | `string` | Путь к источнику Plugin  
`api.rootDir` | `string?` | Корневой каталог Plugin (необязательно)  
`api.config` | `OpenClawConfig` | Текущий снимок конфигурации (активный снимок среды выполнения в памяти, когда доступен)  
`api.pluginConfig` | `Record<string, unknown>` | Конфигурация, специфичная для Plugin, из `plugins.entries.<id>.config`  
`api.runtime` | `PluginRuntime` | [Вспомогательные средства среды выполнения](</ru/plugins/sdk-runtime>)  
`api.logger` | `PluginLogger` | Логгер с областью действия (`debug`, `info`, `warn`, `error`)  
`api.registrationMode` | `PluginRegistrationMode` | Текущий режим загрузки; `"setup-runtime"` — облегченный предварительный период запуска/настройки до полной точки входа  
`api.resolvePath(input)` | `(string) => string` | Разрешить путь относительно корня Plugin  
  
## Соглашение о внутренних модулях

Внутри своего Plugin используйте локальные barrel-файлы для внутренних импортов:

CodeCopy code
[code]
    my-plugin/  api.ts            # Public exports for external consumers  runtime-api.ts    # Internal-only runtime exports  index.ts          # Plugin entry point  setup-entry.ts    # Lightweight setup-only entry (optional)
[/code]

Публичные поверхности встроенного Plugin, загружаемого через фасад (`api.ts`, `runtime-api.ts`, `index.ts`, `setup-entry.ts` и похожие публичные файлы входа), предпочитают активный снимок конфигурации среды выполнения, когда OpenClaw уже запущен. Если снимка среды выполнения еще нет, они используют разрешенный файл конфигурации на диске. Фасады упакованных встроенных Plugin следует загружать через фасадные загрузчики Plugin OpenClaw; прямые импорты из `dist/extensions/...` обходят манифест и проверки runtime sidecar, которые упакованные установки используют для кода, принадлежащего Plugin.

Provider Plugin могут предоставлять узкий локальный для Plugin barrel контракта, когда вспомогательная функция намеренно специфична для провайдера и пока не относится к универсальному подпути SDK. Встроенные примеры:

  * **Anthropic** : публичный шов `api.ts` / `contract-api.ts` для вспомогательных средств Claude beta-header и потока `service_tier`.
  * **`@openclaw/openai-provider`** : `api.ts` экспортирует построители провайдера, вспомогательные средства модели по умолчанию и построители realtime-провайдера.
  * **`@openclaw/openrouter-provider`** : `api.ts` экспортирует построитель провайдера плюс вспомогательные средства онбординга/конфигурации.


## Связанные материалы

[**Точки входа** Параметры `definePluginEntry` и `defineChannelPluginEntry`. ](</ru/plugins/sdk-entrypoints>) [**Вспомогательные средства среды выполнения** Полный справочник пространства имен `api.runtime`. ](</ru/plugins/sdk-runtime>) [**Настройка и конфигурация** Упаковка, манифесты и схемы конфигурации. ](</ru/plugins/sdk-setup>) [**Тестирование** Тестовые утилиты и правила lint. ](</ru/plugins/sdk-testing>) [**Миграция SDK** Миграция с устаревших поверхностей. ](</ru/plugins/sdk-migration>) [**Внутреннее устройство Plugin** Глубокая архитектура и модель возможностей. ](</ru/plugins/architecture>)

Was this useful?YesNo

Open issue