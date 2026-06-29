---
title: Тестирование Plugin
source_url: https://docs.openclaw.ai/ru/plugins/sdk-testing
scraped_at: 2026-06-29
---

ReferencePlugin SDK reference

Справочник по тестовым утилитам, шаблонам и проверкам линтера для Plugin OpenClaw.

## Тестовые утилиты

Эти подпути тестовых помощников являются локальными для репозитория исходными точками входа для собственных тестов встроенных Plugin OpenClaw. Они не являются экспортами пакета для сторонних Plugin и могут импортировать Vitest или другие тестовые зависимости, используемые только в репозитории.

**Импорт мока API Plugin:** `openclaw/plugin-sdk/plugin-test-api`

**Импорт контракта среды выполнения агента:** `openclaw/plugin-sdk/agent-runtime-test-contracts`

**Импорт контракта канала:** `openclaw/plugin-sdk/channel-contract-testing`

**Импорт тестового помощника канала:** `openclaw/plugin-sdk/channel-test-helpers`

**Импорт теста цели канала:** `openclaw/plugin-sdk/channel-target-testing`

**Импорт контракта Plugin:** `openclaw/plugin-sdk/plugin-test-contracts`

**Импорт теста среды выполнения Plugin:** `openclaw/plugin-sdk/plugin-test-runtime`

**Импорт контракта провайдера:** `openclaw/plugin-sdk/provider-test-contracts`

**Импорт HTTP-мока провайдера:** `openclaw/plugin-sdk/provider-http-test-mocks`

**Импорт тестов среды/сети:** `openclaw/plugin-sdk/test-env`

**Импорт универсальной фикстуры:** `openclaw/plugin-sdk/test-fixtures`

**Импорт мока встроенного модуля Node:** `openclaw/plugin-sdk/test-node-mocks`

Внутри репозитория OpenClaw для новых тестов встроенных Plugin предпочитайте узконаправленные подпути ниже. Широкий barrel-экспорт `openclaw/plugin-sdk/testing` предназначен только для устаревшей совместимости. Ограничения репозитория отклоняют новые реальные импорты из `plugin-sdk/testing` и `plugin-sdk/test-utils`; эти имена остаются только как устаревшие поверхности совместимости для тестов записей совместимости.

typescriptCopy code
[code]
       shouldAckReaction,  removeAckReactionAfterReply,} from "openclaw/plugin-sdk/channel-feedback";             bundledPluginRoot,  createCliRuntimeCapture,  typedCases,} from "openclaw/plugin-sdk/test-fixtures"; 
[/code]

### Доступные экспорты

Экспорт | Назначение  
---|---  
`createTestPluginApi` | Создает минимальный mock API Plugin для модульных тестов прямой регистрации. Импорт из `plugin-sdk/plugin-test-api`  
`AUTH_PROFILE_RUNTIME_CONTRACT` | Общая фикстура контракта auth-profile для адаптеров среды выполнения нативного агента. Импорт из `plugin-sdk/agent-runtime-test-contracts`  
`DELIVERY_NO_REPLY_RUNTIME_CONTRACT` | Общая фикстура контракта подавления доставки для адаптеров среды выполнения нативного агента. Импорт из `plugin-sdk/agent-runtime-test-contracts`  
`OUTCOME_FALLBACK_RUNTIME_CONTRACT` | Общая фикстура контракта классификации fallback для адаптеров среды выполнения нативного агента. Импорт из `plugin-sdk/agent-runtime-test-contracts`  
`createParameterFreeTool` | Создает фикстуры схемы динамического инструмента для тестов контракта нативной среды выполнения. Импорт из `plugin-sdk/agent-runtime-test-contracts`  
`expectChannelInboundContextContract` | Проверяет форму входящего контекста канала. Импорт из `plugin-sdk/channel-contract-testing`  
`installChannelOutboundPayloadContractSuite` | Устанавливает набор случаев контракта исходящей полезной нагрузки канала. Импорт из `plugin-sdk/channel-contract-testing`  
`createStartAccountContext` | Создает контексты жизненного цикла учетной записи канала. Импорт из `plugin-sdk/channel-test-helpers`  
`installChannelActionsContractSuite` | Устанавливает типовые случаи контракта действий сообщений канала. Импорт из `plugin-sdk/channel-test-helpers`  
`installChannelSetupContractSuite` | Устанавливает типовые случаи контракта настройки канала. Импорт из `plugin-sdk/channel-test-helpers`  
`installChannelStatusContractSuite` | Устанавливает типовые случаи контракта статуса канала. Импорт из `plugin-sdk/channel-test-helpers`  
`expectDirectoryIds` | Проверяет идентификаторы каталога каналов из функции списка каталогов. Импорт из `plugin-sdk/channel-test-helpers`  
`assertBundledChannelEntries` | Проверяет, что точки входа встроенных каналов предоставляют ожидаемый публичный контракт. Импорт из `plugin-sdk/channel-test-helpers`  
`formatEnvelopeTimestamp` | Форматирует детерминированные временные метки конвертов. Импорт из `plugin-sdk/channel-test-helpers`  
`expectPairingReplyText` | Проверяет текст ответа сопряжения канала и извлекает его код. Импорт из `plugin-sdk/channel-test-helpers`  
`describePluginRegistrationContract` | Устанавливает проверки контракта регистрации Plugin. Импорт из `plugin-sdk/plugin-test-contracts`  
`registerSingleProviderPlugin` | Регистрирует один Plugin провайдера в smoke-тестах загрузчика. Импорт из `plugin-sdk/plugin-test-runtime`  
`registerProviderPlugin` | Захватывает все виды провайдеров из одного Plugin. Импорт из `plugin-sdk/plugin-test-runtime`  
`registerProviderPlugins` | Захватывает регистрации провайдеров из нескольких Plugin. Импорт из `plugin-sdk/plugin-test-runtime`  
`requireRegisteredProvider` | Проверяет, что коллекция провайдеров содержит идентификатор. Импорт из `plugin-sdk/plugin-test-runtime`  
`createRuntimeEnv` | Создает mock-окружение среды выполнения CLI/Plugin. Импорт из `plugin-sdk/plugin-test-runtime`  
`createPluginRuntimeMock` | Создает mock-поверхность среды выполнения Plugin. Импорт из `plugin-sdk/plugin-test-runtime`  
`createPluginSetupWizardStatus` | Создает вспомогательные объекты статуса настройки для Plugin каналов. Импорт из `plugin-sdk/plugin-test-runtime`  
`describeOpenAIProviderRuntimeContract` | Устанавливает проверки контракта среды выполнения семейства провайдеров. Импорт из `plugin-sdk/provider-test-contracts`  
`expectPassthroughReplayPolicy` | Проверяет, что политики повтора провайдера пропускают инструменты и метаданные, принадлежащие провайдеру. Импорт из `plugin-sdk/provider-test-contracts`  
`runRealtimeSttLiveTest` | Запускает live-тест realtime STT-провайдера с общими аудиофикстурами. Импорт из `plugin-sdk/provider-test-contracts`  
`normalizeTranscriptForMatch` | Нормализует вывод live-транскрипта перед нечеткими проверками. Импорт из `plugin-sdk/provider-test-contracts`  
`expectExplicitVideoGenerationCapabilities` | Проверяет, что видеопровайдеры объявляют явные возможности режима генерации. Импорт из `plugin-sdk/provider-test-contracts`  
`expectExplicitMusicGenerationCapabilities` | Проверяет, что музыкальные провайдеры объявляют явные возможности генерации/редактирования. Импорт из `plugin-sdk/provider-test-contracts`  
`mockSuccessfulDashscopeVideoTask` | Устанавливает успешный ответ видеозадачи, совместимый с DashScope. Импорт из `plugin-sdk/provider-test-contracts`  
`getProviderHttpMocks` | Получает доступ к opt-in HTTP/auth mock Vitest для провайдеров. Импорт из `plugin-sdk/provider-http-test-mocks`  
`installProviderHttpMockCleanup` | Сбрасывает HTTP/auth mock провайдеров после каждого теста. Импорт из `plugin-sdk/provider-http-test-mocks`  
`installCommonResolveTargetErrorCases` | Общие тестовые случаи для обработки ошибок разрешения цели. Импорт из `plugin-sdk/channel-target-testing`  
`shouldAckReaction` | Проверяет, должен ли канал добавить ack-реакцию. Импорт из `plugin-sdk/channel-feedback`  
`removeAckReactionAfterReply` | Удаляет ack-реакцию после доставки ответа. Импорт из `plugin-sdk/channel-feedback`  
`createTestRegistry` | Создает фикстуру реестра Plugin канала. Импорт из `plugin-sdk/plugin-test-runtime` или `plugin-sdk/channel-test-helpers`  
`createEmptyPluginRegistry` | Создает фикстуру пустого реестра Plugin. Импорт из `plugin-sdk/plugin-test-runtime` или `plugin-sdk/channel-test-helpers`  
`setActivePluginRegistry` | Устанавливает фикстуру реестра для тестов среды выполнения Plugin. Импорт из `plugin-sdk/plugin-test-runtime` или `plugin-sdk/channel-test-helpers`  
`createRequestCaptureJsonFetch` | Захватывает JSON-запросы fetch в тестах вспомогательных средств для медиа. Импорт из `plugin-sdk/test-env`  
`withServer` | Запускает тесты с одноразовым локальным HTTP-сервером. Импорт из `plugin-sdk/test-env`  
`createMockIncomingRequest` | Создает минимальный объект входящего HTTP-запроса. Импорт из `plugin-sdk/test-env`  
`withFetchPreconnect` | Запускает тесты fetch с установленными хуками preconnect. Импорт из `plugin-sdk/test-env`  
`withEnv` / `withEnvAsync` | Временно изменяет переменные окружения. Импорт из `plugin-sdk/test-env`  
`createTempHomeEnv` / `withTempHome` / `withTempDir` | Создает изолированные тестовые фикстуры файловой системы. Импорт из `plugin-sdk/test-env`  
`createMockServerResponse` | Создает минимальный mock ответа HTTP-сервера. Импорт из `plugin-sdk/test-env`  
`createCliRuntimeCapture` | Захватывает вывод среды выполнения CLI в тестах. Импорт из `plugin-sdk/test-fixtures`  
`importFreshModule` | Импортирует ESM-модуль со свежим query-токеном для обхода кэша модулей. Импорт из `plugin-sdk/test-fixtures`  
`bundledPluginRoot` / `bundledPluginFile` | Разрешает пути к фикстурам исходников или dist встроенного Plugin. Импорт из `plugin-sdk/test-fixtures`  
`mockNodeBuiltinModule` | Устанавливает узкие mock Vitest для встроенных модулей Node. Импорт из `plugin-sdk/test-node-mocks`  
`createSandboxTestContext` | Создает контексты тестирования sandbox. Импорт из `plugin-sdk/test-fixtures`  
`writeSkill` | Записывает фикстуры Skills. Импорт из `plugin-sdk/test-fixtures`  
`makeAgentAssistantMessage` | Создает фикстуры сообщений транскрипта агента. Импорт из `plugin-sdk/test-fixtures`  
`peekSystemEvents` / `resetSystemEventsForTest` | Проверяет и сбрасывает фикстуры системных событий. Импорт из `plugin-sdk/test-fixtures`  
`sanitizeTerminalText` | Очищает вывод терминала для проверок. Импорт из `plugin-sdk/test-fixtures`  
`countLines` / `hasBalancedFences` | Проверяет форму вывода разбиения на фрагменты. Импорт из `plugin-sdk/test-fixtures`  
`runProviderCatalog` | Выполняет хук каталога провайдера с тестовыми зависимостями  
`resolveProviderWizardOptions` | Разрешает варианты мастера настройки провайдера в контрактных тестах  
`resolveProviderModelPickerEntries` | Разрешает элементы выбора модели провайдера в контрактных тестах  
`buildProviderPluginMethodChoice` | Создает идентификаторы вариантов мастера провайдера для проверок  
`setProviderWizardProvidersResolverForTest` | Внедрить провайдеры мастера настройки провайдера для изолированных тестов  
`createProviderUsageFetch` | Создать фикстуры fetch для использования провайдера  
`useFrozenTime` / `useRealTime` | Заморозить и восстановить таймеры для тестов, чувствительных ко времени. Импортируйте из `plugin-sdk/test-env`  
`createTestWizardPrompter` | Создать имитированный prompter мастера настройки  
`createRuntimeTaskFlow` | Создать изолированное состояние потока задач runtime  
`typedCases` | Сохранить литеральные типы для табличных тестов. Импортируйте из `plugin-sdk/test-fixtures`  
  
Наборы контрактных тестов встроенных Plugin также используют тестовые подпути SDK для вспомогательных средств реестра, манифеста, публичных артефактов и runtime-фикстур, предназначенных только для тестов. Наборы только для ядра, которые зависят от встроенного инвентаря OpenClaw, остаются в `src/plugins/contracts`. Размещайте новые тесты расширений в документированном узконаправленном подпути SDK, таком как `plugin-sdk/plugin-test-api`, `plugin-sdk/channel-contract-testing`, `plugin-sdk/agent-runtime-test-contracts`, `plugin-sdk/channel-test-helpers`, `plugin-sdk/plugin-test-contracts`, `plugin-sdk/plugin-test-runtime`, `plugin-sdk/provider-test-contracts`, `plugin-sdk/provider-http-test-mocks`, `plugin-sdk/test-env` или `plugin-sdk/test-fixtures`, вместо прямого импорта широкого совместимого barrel `plugin-sdk/testing`, файлов репозитория `src/**` или мостов репозитория `test/helpers/*`.

### Типы

Узконаправленные тестовые подпути также повторно экспортируют типы, полезные в тестовых файлах:

typescriptCopy code
[code]
       ChannelAccountSnapshot,  ChannelGatewayContext,} from "openclaw/plugin-sdk/channel-contract";  
[/code]

## Разрешение тестовой цели

Используйте `installCommonResolveTargetErrorCases`, чтобы добавить стандартные случаи ошибок для разрешения цели канала:

typescriptCopy code
[code]
      describe("my-channel target resolution", () => {  installCommonResolveTargetErrorCases({    resolveTarget: ({ to, mode, allowFrom }) => {      // Your channel's target resolution logic      return myChannelResolveTarget({ to, mode, allowFrom });    },    implicitAllowFrom: ["user1", "user2"],  });   // Add channel-specific test cases  it("should resolve @username targets", () => {    // ...  });});
[/code]

## Шаблоны тестирования

### Тестирование контрактов регистрации

Модульные тесты, которые передают вручную написанный мок `api` в `register(api)`, не проверяют шлюзы приемки загрузчика OpenClaw. Добавьте хотя бы один smoke-тест на основе загрузчика для каждой поверхности регистрации, от которой зависит ваш Plugin, особенно для хуков и эксклюзивных возможностей, таких как память.

Реальный загрузчик завершает регистрацию Plugin с ошибкой, когда отсутствуют обязательные метаданные или Plugin вызывает API возможности, которой он не владеет. Например, `api.registerHook(...)` требует имя хука, а `api.registerMemoryCapability(...)` требует, чтобы манифест Plugin или экспортированная точка входа объявляли `kind: "memory"`.

### Тестирование доступа к конфигурации среды выполнения

Предпочитайте общий мок среды выполнения Plugin из `openclaw/plugin-sdk/plugin-test-runtime`. Его устаревшие моки `runtime.config.loadConfig()` и `runtime.config.writeConfigFile(...)` по умолчанию выбрасывают ошибку, чтобы тесты выявляли новое использование API совместимости. Переопределяйте эти моки только тогда, когда тест явно покрывает устаревшее поведение совместимости.

### Модульное тестирование канального Plugin

typescriptCopy code
[code]
     describe("my-channel plugin", () => {  it("should resolve account from config", () => {    const cfg = {      channels: {        "my-channel": {          token: "test-token",          allowFrom: ["user1"],        },      },    };     const account = myPlugin.setup.resolveAccount(cfg, undefined);    expect(account.token).toBe("test-token");  });   it("should inspect account without materializing secrets", () => {    const cfg = {      channels: {        "my-channel": { token: "test-token" },      },    };     const inspection = myPlugin.setup.inspectAccount(cfg, undefined);    expect(inspection.configured).toBe(true);    expect(inspection.tokenStatus).toBe("available");    // No token value exposed    expect(inspection).not.toHaveProperty("token");  });});
[/code]

### Модульное тестирование провайдерского Plugin

typescriptCopy code
[code]
     describe("my-provider plugin", () => {  it("should resolve dynamic models", () => {    const model = myProvider.resolveDynamicModel({      modelId: "custom-model-v2",      // ... context    });     expect(model.id).toBe("custom-model-v2");    expect(model.provider).toBe("my-provider");    expect(model.api).toBe("openai-completions");  });   it("should return catalog when API key is available", async () => {    const result = await myProvider.catalog.run({      resolveProviderApiKey: () => ({ apiKey: "test-key" }),      // ... context    });     expect(result?.provider?.models).toHaveLength(2);  });});
[/code]

### Мокирование среды выполнения Plugin

Для кода, который использует `createPluginRuntimeStore`, мокируйте среду выполнения в тестах:

typescriptCopy code
[code]
      const store = createPluginRuntimeStore&lt;PluginRuntime&gt;({  pluginId: "test-plugin",  errorMessage: "test runtime not set",}); // In test setupconst mockRuntime = {  agent: {    resolveAgentDir: vi.fn().mockReturnValue("/tmp/agent"),    // ... other mocks  },  config: {    current: vi.fn(() => ({}) as const),    mutateConfigFile: vi.fn(),    replaceConfigFile: vi.fn(),  },  // ... other namespaces} as unknown as PluginRuntime; store.setRuntime(mockRuntime); // After testsstore.clearRuntime();
[/code]

### Тестирование с заглушками на уровне экземпляра

Предпочитайте заглушки на уровне экземпляра вместо изменения прототипа:

typescriptCopy code
[code]
    // Preferred: per-instance stubconst client = new MyChannelClient();client.sendMessage = vi.fn().mockResolvedValue({ id: "msg-1" }); // Avoid: prototype mutation// MyChannelClient.prototype.sendMessage = vi.fn();
[/code]

## Контрактные тесты (Plugin внутри репозитория)

Встроенные Plugin имеют контрактные тесты, которые проверяют владение регистрацией:

bashCopy code
[code]
    pnpm test -- src/plugins/contracts/
[/code]

Эти тесты проверяют:

  * Какие Plugin регистрируют каких провайдеров
  * Какие Plugin регистрируют каких речевых провайдеров
  * Корректность формы регистрации
  * Соответствие контракту среды выполнения


### Запуск ограниченных по области тестов

Для конкретного Plugin:

bashCopy code
[code]
    pnpm test -- <bundled-plugin-root>/my-channel/
[/code]

Только для контрактных тестов:

bashCopy code
[code]
    pnpm test -- src/plugins/contracts/shape.contract.test.tspnpm test -- src/plugins/contracts/auth-choice.contract.test.tspnpm test -- src/plugins/contracts/runtime-seams.contract.test.ts
[/code]

## Проверка lint (Plugin внутри репозитория)

Для Plugin внутри репозитория `pnpm check` применяет три правила:

  1. **Без монолитных корневых импортов** \-- корневой barrel `openclaw/plugin-sdk` отклоняется
  2. **Без прямых импортов`src/`** \-- Plugin не могут напрямую импортировать `../../src/`
  3. **Без самоимпортов** \-- Plugin не могут импортировать собственный подпуть `plugin-sdk/<name>`


Внешние Plugin не подпадают под эти правила lint, но рекомендуется следовать тем же шаблонам.

## Конфигурация тестов

OpenClaw использует Vitest с порогами покрытия V8. Для тестов Plugin:

bashCopy code
[code]
    # Run all testspnpm test # Run specific plugin testspnpm test -- <bundled-plugin-root>/my-channel/src/channel.test.ts # Run with a specific test name filterpnpm test -- <bundled-plugin-root>/my-channel/ -t "resolves account" # Run with coveragepnpm test:coverage
[/code]

Если локальные запуски вызывают нехватку памяти:

bashCopy code
[code]
    OPENCLAW_VITEST_MAX_WORKERS=1 pnpm test
[/code]

## Связанные материалы

  * [Обзор SDK](</ru/plugins/sdk-overview>) \-- соглашения об импорте
  * [Канальные Plugin SDK](</ru/plugins/sdk-channel-plugins>) \-- интерфейс канального Plugin
  * [Провайдерские Plugin SDK](</ru/plugins/sdk-provider-plugins>) \-- хуки провайдерского Plugin
  * [Создание Plugin](</ru/plugins/building-plugins>) \-- руководство по началу работы


Was this useful?YesNo

Open issue