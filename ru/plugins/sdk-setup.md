---
title: Настройка и конфигурация Plugin
source_url: https://docs.openclaw.ai/ru/plugins/sdk-setup
scraped_at: 2026-06-29
---

ReferencePlugin SDK reference

Справочник по упаковке plugin (метаданные `package.json`), манифестам (`openclaw.plugin.json`), записям настройки и схемам конфигурации.

## Метаданные пакета

Вашему `package.json` нужно поле `openclaw`, которое сообщает системе plugin, что предоставляет ваш plugin:

### Channel plugin

jsonCopy code
[code]
    {  "name": "@myorg/openclaw-my-channel",  "version": "1.0.0",  "type": "module",  "openclaw": {    "extensions": ["./index.ts"],    "setupEntry": "./setup-entry.ts",    "channel": {      "id": "my-channel",      "label": "My Channel",      "blurb": "Short description of the channel."    }  }}
[/code]

### Provider plugin / ClawHub baseline

openclaw-clawhub-package.jsonCopy code
[code]
    {  "name": "@myorg/openclaw-my-plugin",  "version": "1.0.0",  "type": "module",  "openclaw": {    "extensions": ["./index.ts"],    "compat": {      "pluginApi": ">=2026.3.24-beta.2",      "minGatewayVersion": "2026.3.24-beta.2"    },    "build": {      "openclawVersion": "2026.3.24-beta.2",      "pluginSdkVersion": "2026.3.24-beta.2"    }  }}
[/code]

### Поля `openclaw`

Файлы точек входа (относительно корня пакета).

Легковесная точка входа только для настройки (необязательно).

Метаданные каталога канала для поверхностей настройки, выбора, быстрого старта и статуса.

Идентификаторы провайдеров, зарегистрированные этим plugin.

Подсказки установки: `npmSpec`, `localPath`, `defaultChoice`, `minHostVersion`, `expectedIntegrity`, `allowInvalidConfigRecovery`.

Флаги поведения при запуске.

### `openclaw.channel`

`openclaw.channel` — это недорогие метаданные пакета для обнаружения каналов и поверхностей настройки до загрузки runtime.

Поле | Тип | Что это означает  
---|---|---  
`id` | `string` | Канонический идентификатор канала.  
`label` | `string` | Основная метка канала.  
`selectionLabel` | `string` | Метка в выборе/настройке, когда она должна отличаться от `label`.  
`detailLabel` | `string` | Вторичная детальная метка для более содержательных каталогов каналов и поверхностей статуса.  
`docsPath` | `string` | Путь к документации для ссылок настройки и выбора.  
`docsLabel` | `string` | Переопределяющая метка для ссылок на документацию, когда она должна отличаться от идентификатора канала.  
`blurb` | `string` | Краткое описание для онбординга/каталога.  
`order` | `number` | Порядок сортировки в каталогах каналов.  
`aliases` | `string[]` | Дополнительные псевдонимы поиска для выбора канала.  
`preferOver` | `string[]` | Идентификаторы plugin/каналов с более низким приоритетом, которые этот канал должен опережать.  
`systemImage` | `string` | Необязательное имя значка/system-image для UI-каталогов каналов.  
`selectionDocsPrefix` | `string` | Префиксный текст перед ссылками на документацию в поверхностях выбора.  
`selectionDocsOmitLabel` | `boolean` | Показывать путь к документации напрямую вместо подписанной ссылки на документацию в тексте выбора.  
`selectionExtras` | `string[]` | Дополнительные короткие строки, добавляемые в текст выбора.  
`markdownCapable` | `boolean` | Помечает канал как поддерживающий Markdown для решений о форматировании исходящих сообщений.  
`exposure` | `object` | Элементы управления видимостью канала для настройки, списков настроенных каналов и поверхностей документации.  
`quickstartAllowFrom` | `boolean` | Подключить этот канал к стандартному потоку настройки быстрого старта `allowFrom`.  
`forceAccountBinding` | `boolean` | Требовать явной привязки учетной записи, даже когда существует только одна учетная запись.  
`preferSessionLookupForAnnounceTarget` | `boolean` | Предпочитать поиск сеанса при разрешении целей объявлений для этого канала.  
  
Пример:

jsonCopy code
[code]
    {  "openclaw": {    "channel": {      "id": "my-channel",      "label": "My Channel",      "selectionLabel": "My Channel (self-hosted)",      "detailLabel": "My Channel Bot",      "docsPath": "/channels/my-channel",      "docsLabel": "my-channel",      "blurb": "Webhook-based self-hosted chat integration.",      "order": 80,      "aliases": ["mc"],      "preferOver": ["my-channel-legacy"],      "selectionDocsPrefix": "Guide:",      "selectionExtras": ["Markdown"],      "markdownCapable": true,      "exposure": {        "configured": true,        "setup": true,        "docs": true      },      "quickstartAllowFrom": true    }  }}
[/code]

`exposure` поддерживает:

  * `configured`: включать канал в поверхности списков настроенных каналов/статуса
  * `setup`: включать канал в интерактивные средства выбора настройки/конфигурации
  * `docs`: помечать канал как публичный в поверхностях документации/навигации


### `openclaw.install`

`openclaw.install` — это метаданные пакета, а не метаданные манифеста.

Поле | Тип | Что это означает  
---|---|---  
`clawhubSpec` | `string` | Каноническая спецификация ClawHub для установки/обновления и онбординг-потоков установки по требованию.  
`npmSpec` | `string` | Каноническая спецификация npm для резервных потоков установки/обновления.  
`localPath` | `string` | Локальный путь разработки или встроенной установки.  
`defaultChoice` | `"clawhub"` | `"npm"` | `"local"` | Предпочитаемый источник установки, когда доступно несколько источников.  
`minHostVersion` | `string` | Минимальная поддерживаемая версия OpenClaw в форме `>=x.y.z` или `>=x.y.z-prerelease`.  
`expectedIntegrity` | `string` | Ожидаемая строка целостности npm-дистрибутива, обычно `sha512-...`, для закрепленных установок.  
`allowInvalidConfigRecovery` | `boolean` | Позволяет потокам переустановки встроенного plugin восстанавливаться после конкретных сбоев устаревшей конфигурации.  
`requiredPlatformPackages` | `string[]` | Обязательные платформозависимые псевдонимы npm, проверяемые во время установки npm.  
  
Onboarding behavior

Интерактивный онбординг также использует `openclaw.install` для поверхностей установки по требованию. Если ваш plugin предоставляет варианты авторизации провайдера или метаданные настройки/каталога канала до загрузки runtime, онбординг может показать этот вариант, предложить установку через ClawHub, npm или локально, установить или включить plugin, а затем продолжить выбранный поток. Варианты онбординга ClawHub используют `clawhubSpec` и предпочтительны, когда они присутствуют; варианты npm требуют доверенных метаданных каталога со спецификацией реестра `npmSpec`; точные версии и `expectedIntegrity` являются необязательными закреплениями npm. Если `expectedIntegrity` присутствует, потоки установки/обновления принудительно проверяют его для npm. Держите метаданные «что показывать» в `openclaw.plugin.json`, а метаданные «как это установить» — в `package.json`.

minHostVersion enforcement

Если `minHostVersion` задан, и установка, и загрузка реестра манифестов для невстроенных plugin принудительно его проверяют. Старые хосты пропускают внешние plugin; недопустимые строки версий отклоняются. Встроенные исходные plugin считаются совместно версионированными с checkout хоста.

Pinned npm installs

Для закрепленных установок npm держите точную версию в `npmSpec` и добавьте ожидаемую целостность артефакта:

jsonCopy code
[code]
    {  "openclaw": {    "install": {      "npmSpec": "@wecom/wecom-openclaw-plugin@1.2.3",      "expectedIntegrity": "sha512-REPLACE_WITH_NPM_DIST_INTEGRITY",      "defaultChoice": "npm"    }  }}
[/code]

allowInvalidConfigRecovery scope

`allowInvalidConfigRecovery` не является общим обходом для сломанных конфигураций. Он предназначен только для узкого восстановления встроенных plugin, чтобы переустановка/настройка могла исправлять известные остатки после обновления, например отсутствующий путь встроенного plugin или устаревшую запись `channels.<id>` для того же plugin. Если конфигурация сломана по несвязанным причинам, установка по-прежнему завершается закрыто и сообщает оператору запустить `openclaw doctor --fix`.

### Отложенная полная загрузка

Plugin каналов могут включить отложенную загрузку с помощью:

jsonCopy code
[code]
    {  "openclaw": {    "extensions": ["./index.ts"],    "setupEntry": "./setup-entry.ts",    "startup": {      "deferConfiguredChannelFullLoadUntilAfterListen": true    }  }}
[/code]

Когда это включено, OpenClaw загружает только `setupEntry` на этапе запуска до начала прослушивания, даже для уже настроенных каналов. Полная точка входа загружается после того, как Gateway начинает прослушивание.

Если ваша настроечная/полная точка входа регистрирует RPC-методы Gateway, держите их на префиксе, специфичном для plugin. Зарезервированные пространства имен администрирования ядра (`config.*`, `exec.approvals.*`, `wizard.*`, `update.*`) остаются во владении ядра и всегда разрешаются в `operator.admin`.

## Манифест Plugin

Каждый нативный plugin должен поставлять `openclaw.plugin.json` в корне пакета. OpenClaw использует его для проверки конфигурации без выполнения кода plugin.

jsonCopy code
[code]
    {  "id": "my-plugin",  "name": "My Plugin",  "description": "Adds My Plugin capabilities to OpenClaw",  "configSchema": {    "type": "object",    "additionalProperties": false,    "properties": {      "webhookSecret": {        "type": "string",        "description": "Webhook verification secret"      }    }  }}
[/code]

Для plugin каналов добавьте `kind` и `channels`:

jsonCopy code
[code]
    {  "id": "my-channel",  "kind": "channel",  "channels": ["my-channel"],  "configSchema": {    "type": "object",    "additionalProperties": false,    "properties": {}  }}
[/code]

Даже plugin без конфигурации должны поставлять схему. Пустая схема допустима:

jsonCopy code
[code]
    {  "id": "my-plugin",  "configSchema": {    "type": "object",    "additionalProperties": false  }}
[/code]

См. [манифест Plugin](</ru/plugins/manifest>) для полного справочника схемы.

## Публикация в ClawHub

Для пакетов плагинов используйте команду ClawHub, предназначенную для пакетов:

bashCopy code
[code]
    clawhub package publish your-org/your-plugin --dry-runclawhub package publish your-org/your-plugin
[/code]

## Точка входа настройки

Файл `setup-entry.ts` — это облегченная альтернатива `index.ts`, которую OpenClaw загружает, когда ему нужны только поверхности настройки (первичная настройка, исправление конфигурации, проверка отключенного канала).

typescriptCopy code
[code]
    // setup-entry.ts  export default defineSetupPluginEntry(myChannelPlugin);
[/code]

Это позволяет не загружать тяжелый код времени выполнения (криптографические библиотеки, регистрации CLI, фоновые службы) во время потоков настройки.

Встроенные каналы рабочей области, которые хранят безопасные для настройки экспорты в боковых модулях, могут использовать `defineBundledChannelSetupEntry(...)` из `openclaw/plugin-sdk/channel-entry-contract` вместо `defineSetupPluginEntry(...)`. Этот встроенный контракт также поддерживает необязательный экспорт `runtime`, чтобы связывание времени выполнения на этапе настройки оставалось легким и явным.

Когда OpenClaw использует setupEntry вместо полной точки входа

  * Канал отключен, но ему нужны поверхности настройки/первичной настройки.
  * Канал включен, но не настроен.
  * Включена отложенная загрузка (`deferConfiguredChannelFullLoadUntilAfterListen`).

Что должен регистрировать setupEntry

  * Объект Plugin канала (через `defineSetupPluginEntry`).
  * Любые HTTP-маршруты, необходимые до запуска прослушивания Gateway.
  * Любые методы Gateway, необходимые во время запуска.


Эти методы Gateway для запуска все равно должны избегать зарезервированных административных пространств имен ядра, таких как `config.*` или `update.*`.

Что НЕ должен включать setupEntry

  * Регистрации CLI.
  * Фоновые службы.
  * Тяжелые импорты времени выполнения (криптография, SDK).
  * Методы Gateway, необходимые только после запуска.


### Узкие импорты помощников настройки

Для горячих путей, предназначенных только для настройки, предпочитайте узкие швы помощников настройки более широкому зонтичному модулю `plugin-sdk/setup`, когда вам нужна только часть поверхности настройки:

Путь импорта | Для чего использовать | Ключевые экспорты  
---|---|---  
`plugin-sdk/setup-runtime` | помощники времени выполнения настройки, остающиеся доступными в `setupEntry` / отложенном запуске канала | `createSetupTranslator`, `createPatchedAccountSetupAdapter`, `createEnvPatchedAccountSetupAdapter`, `createSetupInputPresenceValidator`, `noteChannelLookupFailure`, `noteChannelLookupSummary`, `promptResolvedAllowFrom`, `splitSetupEntries`, `createAllowlistSetupWizardProxy`, `createDelegatedSetupWizardProxy`  
`plugin-sdk/setup-adapter-runtime` | устаревший псевдоним совместимости; используйте `plugin-sdk/setup-runtime` | `createEnvPatchedAccountSetupAdapter`  
`plugin-sdk/setup-tools` | помощники CLI/архивов/документации для настройки/установки | `formatCliCommand`, `detectBinary`, `extractArchive`, `resolveBrewExecutable`, `formatDocsLink`, `CONFIG_DIR`  
  
Используйте более широкий шов `plugin-sdk/setup`, когда вам нужен полный общий набор инструментов настройки, включая помощники исправления конфигурации, такие как `moveSingleAccountChannelSectionToDefaultAccount(...)`.

Используйте `createSetupTranslator(...)` для фиксированного текста мастера настройки. Он следует локали мастера CLI (`OPENCLAW_LOCALE`, затем системные переменные локали) и откатывается на английский. Храните текст настройки, специфичный для плагина, в коде, принадлежащем плагину, и используйте общие ключи каталога только для общих меток настройки, текста состояния и официального текста настройки встроенных плагинов.

Адаптеры исправления настройки остаются безопасными для горячего пути при импорте. Их поиск поверхности контракта встроенного повышения однопользовательской учетной записи ленивый, поэтому импорт `plugin-sdk/setup-runtime` не загружает нетерпеливо обнаружение поверхности контракта встроенных компонентов до фактического использования адаптера.

### Повышение однопользовательской учетной записи, принадлежащее каналу

Когда канал обновляется с конфигурации верхнего уровня для одной учетной записи до `channels.<id>.accounts.*`, стандартное общее поведение перемещает повышенные значения области учетной записи в `accounts.default`.

Встроенные каналы могут сузить или переопределить это повышение через свою поверхность контракта настройки:

  * `singleAccountKeysToMove`: дополнительные ключи верхнего уровня, которые должны перейти в повышенную учетную запись
  * `namedAccountPromotionKeys`: когда именованные учетные записи уже существуют, только эти ключи переходят в повышенную учетную запись; общие ключи политики/доставки остаются в корне канала
  * `resolveSingleAccountPromotionTarget(...)`: выбор существующей учетной записи, которая получает повышенные значения


## Схема конфигурации

Конфигурация Plugin проверяется по JSON Schema в вашем манифесте. Пользователи настраивают плагины через:

json5Copy code
[code]
    {  plugins: {    entries: {      "my-plugin": {        config: {          webhookSecret: "abc123",        },      },    },  },}
[/code]

Ваш плагин получает эту конфигурацию как `api.pluginConfig` во время регистрации.

Для конфигурации, специфичной для канала, используйте вместо этого раздел конфигурации канала:

json5Copy code
[code]
    {  channels: {    "my-channel": {      token: "bot-token",      allowFrom: ["user1", "user2"],    },  },}
[/code]

### Создание схем конфигурации канала

Используйте `buildChannelConfigSchema`, чтобы преобразовать схему Zod в обертку `ChannelConfigSchema`, используемую артефактами конфигурации, принадлежащими плагину:

typescriptCopy code
[code]
      const accountSchema = z.object({  token: z.string().optional(),  allowFrom: z.array(z.string()).optional(),  accounts: z.object({}).catchall(z.any()).optional(),  defaultAccount: z.string().optional(),}); const configSchema = buildChannelConfigSchema(accountSchema);
[/code]

Если вы уже описываете контракт как JSON Schema или TypeBox, используйте прямой помощник, чтобы OpenClaw мог пропустить преобразование Zod в JSON Schema на путях метаданных:

typescriptCopy code
[code]
      const configSchema = buildJsonChannelConfigSchema(  Type.Object({    token: Type.Optional(Type.String()),    allowFrom: Type.Optional(Type.Array(Type.String())),  }),);
[/code]

Для сторонних плагинов контракт холодного пути по-прежнему находится в манифесте Plugin: отразите сгенерированную JSON Schema в `openclaw.plugin.json#channelConfigs`, чтобы схема конфигурации, настройка и поверхности UI могли проверять `channels.<id>` без загрузки кода времени выполнения.

## Мастера настройки

Плагины каналов могут предоставлять интерактивные мастера настройки для `openclaw onboard`. Мастер — это объект `ChannelSetupWizard` в `ChannelPlugin`:

typescriptCopy code
[code]
     const setupWizard: ChannelSetupWizard = {  channel: "my-channel",  status: {    configuredLabel: "Connected",    unconfiguredLabel: "Not configured",    resolveConfigured: ({ cfg }) => Boolean((cfg.channels as any)?.["my-channel"]?.token),  },  credentials: [    {      inputKey: "token",      providerHint: "my-channel",      credentialLabel: "Bot token",      preferredEnvVar: "MY_CHANNEL_BOT_TOKEN",      envPrompt: "Use MY_CHANNEL_BOT_TOKEN from environment?",      keepPrompt: "Keep current token?",      inputPrompt: "Enter your bot token:",      inspect: ({ cfg, accountId }) => {        const token = (cfg.channels as any)?.["my-channel"]?.token;        return {          accountConfigured: Boolean(token),          hasConfiguredValue: Boolean(token),        };      },    },  ],};
[/code]

Тип `ChannelSetupWizard` поддерживает `credentials`, `textInputs`, `dmPolicy`, `allowFrom`, `groupAccess`, `prepare`, `finalize` и многое другое. Полные примеры см. в пакетах встроенных плагинов (например, в плагине Discord `src/channel.setup.ts`).

Общие запросы allowFrom

Для запросов списка разрешенных DM, которым нужен только стандартный поток `note -> prompt -> parse -> merge -> patch`, предпочитайте общие помощники настройки из `openclaw/plugin-sdk/setup`: `createPromptParsedAllowFromForAccount(...)`, `createTopLevelChannelParsedAllowFromPrompt(...)` и `createNestedChannelParsedAllowFromPrompt(...)`.

Стандартное состояние настройки канала

Для блоков состояния настройки канала, которые отличаются только метками, оценками и необязательными дополнительными строками, предпочитайте `createStandardChannelSetupStatus(...)` из `openclaw/plugin-sdk/setup` вместо ручного создания одного и того же объекта `status` в каждом плагине.

Необязательная поверхность настройки канала

Для необязательных поверхностей настройки, которые должны появляться только в определенных контекстах, используйте `createOptionalChannelSetupSurface` из `openclaw/plugin-sdk/channel-setup`:

typescriptCopy code
[code]
    import { createOptionalChannelSetupSurface } from "openclaw/plugin-sdk/channel-setup"; const setupSurface = createOptionalChannelSetupSurface({  channel: "my-channel",  label: "My Channel",  npmSpec: "@myorg/openclaw-my-channel",  docsPath: "/channels/my-channel",});// Returns { setupAdapter, setupWizard }
[/code]

`plugin-sdk/channel-setup` также предоставляет более низкоуровневые сборщики `createOptionalChannelSetupAdapter(...)` и `createOptionalChannelSetupWizard(...)`, когда вам нужна только одна половина этой поверхности необязательной установки.

Сгенерированные необязательные адаптер/мастер закрываются при реальных записях конфигурации. Они повторно используют одно сообщение о необходимости установки в `validateInput`, `applyAccountConfig` и `finalize`, а также добавляют ссылку на документацию, когда задан `docsPath`.

Помощники настройки на основе бинарных файлов

Для UI настройки на основе бинарных файлов предпочитайте общие делегированные помощники вместо копирования одной и той же связки бинарного файла/состояния в каждый канал:

  * `createDetectedBinaryStatus(...)` для блоков состояния, которые отличаются только метками, подсказками, оценками и обнаружением бинарного файла
  * `createCliPathTextInput(...)` для текстовых вводов на основе пути
  * `createDelegatedSetupWizardStatusResolvers(...)`, `createDelegatedPrepare(...)`, `createDelegatedFinalize(...)` и `createDelegatedResolveConfigured(...)`, когда `setupEntry` должен лениво перенаправлять к более тяжелому полному мастеру
  * `createDelegatedTextInputShouldPrompt(...)`, когда `setupEntry` должен делегировать только решение `textInputs[*].shouldPrompt`


## Публикация и установка

**Внешние plugins:** опубликуйте в [ClawHub](</ru/clawhub>), затем установите:

### npm

bashCopy code
[code]
    openclaw plugins install @myorg/openclaw-my-plugin
[/code]

Спецификации пакетов без префикса устанавливаются из npm во время перехода при запуске.

### Только ClawHub

bashCopy code
[code]
    openclaw plugins install clawhub:@myorg/openclaw-my-plugin
[/code]

### Спецификация пакета npm

Используйте npm, если пакет еще не перенесен в ClawHub или если во время миграции нужен прямой путь установки из npm:

bashCopy code
[code]
    openclaw plugins install npm:@myorg/openclaw-my-plugin
[/code]

**Plugins в репозитории:** разместите их в дереве рабочей области встроенных plugins, и они будут автоматически обнаружены во время сборки.

**Пользователи могут установить:**

bashCopy code
[code]
    openclaw plugins install <package-name>
[/code]

Метаданные встроенного пакета задаются явно, а не выводятся из собранного JavaScript при запуске gateway. Runtime-зависимости должны находиться в пакете plugin, который ими владеет; запуск упакованного OpenClaw никогда не исправляет и не зеркалирует зависимости plugin.

## См. также

  * [Создание plugins](</ru/plugins/building-plugins>) — пошаговое руководство по началу работы
  * [Манифест Plugin](</ru/plugins/manifest>) — полный справочник схемы манифеста
  * [Точки входа SDK](</ru/plugins/sdk-entrypoints>) — `definePluginEntry` и `defineChannelPluginEntry`


Was this useful?YesNo

Open issue