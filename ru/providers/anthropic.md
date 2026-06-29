---
title: Anthropic
source_url: https://docs.openclaw.ai/ru/providers/anthropic
scraped_at: 2026-06-29
---

ModelsProviders

Anthropic разрабатывает семейство моделей **Claude**. OpenClaw поддерживает два способа аутентификации:

  * **Ключ API** — прямой доступ к Anthropic API с оплатой по фактическому использованию (модели `anthropic/*`)
  * **Claude CLI** — повторное использование существующего входа Claude Code на том же хосте


## Начало работы

### Ключ API

**Лучше всего подходит для:** стандартного доступа к API и оплаты по фактическому использованию.

* ### Получите ключ API

Создайте ключ API в [Anthropic Console](<https://console.anthropic.com/>).

* ### Запустите онбординг

bashCopy code
[code]
    openclaw onboard# choose: Anthropic API key
[/code]

Или передайте ключ напрямую:

bashCopy code
[code]
    openclaw onboard --anthropic-api-key "$ANTHROPIC_API_KEY"
[/code]

* ### Проверьте, что модель доступна

bashCopy code
[code]
    openclaw models list --provider anthropic
[/code]

### Пример конфигурации

json5Copy code
[code]
    {  env: { ANTHROPIC_API_KEY: "example-anthropic-key-not-real" },  agents: { defaults: { model: { primary: "anthropic/claude-opus-4-8" } } },}
[/code]

### Claude CLI

**Лучше всего подходит для:** повторного использования существующего входа Claude CLI без отдельного ключа API.

* ### Убедитесь, что Claude CLI установлен и вход выполнен

Проверьте с помощью:

bashCopy code
[code]
    claude --version
[/code]

* ### Запустите онбординг

bashCopy code
[code]
    openclaw onboard# choose: Claude CLI
[/code]

OpenClaw обнаруживает и повторно использует существующие учетные данные Claude CLI.

* ### Проверьте, что модель доступна

bashCopy code
[code]
    openclaw models list --provider anthropic
[/code]

### Пример конфигурации

Предпочитайте каноническую ссылку на модель Anthropic плюс переопределение среды выполнения CLI:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "anthropic/claude-opus-4-8" },      models: {        "anthropic/claude-opus-4-8": {          agentRuntime: { id: "claude-cli" },        },      },    },  },}
[/code]

Устаревшие ссылки на модели `claude-cli/claude-opus-4-7` по-прежнему работают для совместимости, но новая конфигурация должна сохранять выбор провайдера/модели как `anthropic/*` и помещать бэкенд выполнения в политику среды выполнения провайдера/модели.

### Тарификация и `claude -p`

OpenClaw использует неинтерактивный путь `claude -p` Claude Code для запусков Claude CLI. Anthropic сейчас рассматривает этот путь как использование Agent SDK/программный режим:

  * Обновление поддержки Anthropic от 15 июня 2026 года приостановило ранее объявленный отдельный план кредитов Agent SDK.
  * Сейчас Claude Agent SDK по подписному плану, `claude -p` и использование сторонними приложениями по-прежнему расходуют лимиты использования подписки, в которую выполнен вход.
  * Ранее объявленный ежемесячный кредит Agent SDK недоступен, пока Anthropic пересматривает этот план.
  * Входы через Console/ключ API используют оплату API по фактическому использованию и не получают кредит Agent SDK подписки.


См. [статью о плане Agent SDK](<https://support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan>) Anthropic для уведомления о паузе, а также статьи о планах Claude Code для поведения подписок [Pro/Max](<https://support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-or-max-plan>) и [Team/Enterprise](<https://support.claude.com/en/articles/11845131-use-claude-code-with-your-team-or-enterprise-plan>).

Anthropic может менять тарификацию Claude Code и поведение лимитов скорости без релиза OpenClaw. Проверяйте `claude auth status`, `/status` и связанные документы Anthropic, когда важна предсказуемость расходов.

## Значения по умолчанию для рассуждения (Claude Fable 5, 4.8 и 4.6)

`anthropic/claude-fable-5` всегда использует адаптивное рассуждение и по умолчанию задает `high` усилие. Поскольку Anthropic не разрешает отключать рассуждение для этой модели, `/think off` и `/think minimal` используют `low` усилие. OpenClaw также опускает пользовательские значения температуры для запросов Fable 5.

Claude Opus 4.8 по умолчанию в OpenClaw оставляет рассуждение выключенным. Когда вы явно включаете адаптивное рассуждение с помощью `/think high|xhigh|max`, OpenClaw отправляет значения усилия Anthropic для Opus 4.8; модели Claude 4.6 по умолчанию используют `adaptive`.

Переопределяйте для отдельного сообщения с помощью `/think:<level>` или в параметрах модели:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "anthropic/claude-opus-4-8": {          params: { thinking: "high" },        },      },    },  },}
[/code]

## Кэширование промптов

OpenClaw поддерживает функцию кэширования промптов Anthropic для аутентификации по ключу API.

Значение | Длительность кэша | Описание  
---|---|---  
`"short"` (по умолчанию) | 5 минут | Автоматически применяется для аутентификации по ключу API  
`"long"` | 1 час | Расширенный кэш  
`"none"` | Без кэширования | Отключить кэширование промптов  
  
json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "anthropic/claude-opus-4-6": {          params: { cacheRetention: "long" },        },      },    },  },}
[/code]

Переопределения кэша для отдельных агентов

Используйте параметры уровня модели как базовую настройку, затем переопределяйте конкретных агентов через `agents.list[].params`:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "anthropic/claude-opus-4-6" },      models: {        "anthropic/claude-opus-4-6": {          params: { cacheRetention: "long" },        },      },    },    list: [      { id: "research", default: true },      { id: "alerts", params: { cacheRetention: "none" } },    ],  },}
[/code]

Порядок слияния конфигурации:

  1. `agents.defaults.models["provider/model"].params`
  2. `agents.list[].params` (соответствует `id`, переопределяет по ключу)


Это позволяет одному агенту сохранять долгоживущий кэш, пока другой агент на той же модели отключает кэширование для всплескового трафика или трафика с низким повторным использованием.

Заметки о Bedrock Claude

  * Модели Anthropic Claude на Bedrock (`amazon-bedrock/*anthropic.claude*`) принимают сквозную передачу `cacheRetention`, когда она настроена.
  * Для моделей Bedrock, не относящихся к Anthropic, во время выполнения принудительно задается `cacheRetention: "none"`.
  * Умные значения по умолчанию для ключа API также задают `cacheRetention: "short"` для ссылок Claude-on-Bedrock, когда явное значение не установлено.


## Расширенная конфигурация

Быстрый режим

Общий переключатель `/fast` в OpenClaw поддерживает прямой трафик Anthropic (ключ API и OAuth к `api.anthropic.com`).

Команда | Сопоставляется с  
---|---  
`/fast on` | `service_tier: "auto"`  
`/fast off` | `service_tier: "standard_only"`  
  
json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "anthropic/claude-sonnet-4-6": {          params: { fastMode: true },        },      },    },  },}
[/code]

Понимание медиа (изображения и PDF)

Встроенный Plugin Anthropic регистрирует понимание изображений и PDF. OpenClaw автоматически разрешает медиа-возможности из настроенной аутентификации Anthropic — дополнительная конфигурация не нужна.

Свойство | Значение  
---|---  
Модель по умолчанию | `claude-opus-4-8`  
Поддерживаемый ввод | Изображения, PDF-документы  
  
Когда изображение или PDF прикреплены к беседе, OpenClaw автоматически направляет их через провайдера понимания медиа Anthropic.

Контекстное окно 1M

Контекстное окно 1M Anthropic доступно на моделях Claude 4.x с поддержкой GA, таких как Opus 4.8, Opus 4.7, Opus 4.6 и Sonnet 4.6. OpenClaw автоматически задает для этих моделей размер 1M:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "anthropic/claude-opus-4-6": {},      },    },  },}
[/code]

Старые конфигурации могут сохранять `params.context1m: true`, но OpenClaw больше не отправляет устаревший бета-заголовок `context-1m-2025-08-07`. Старые записи конфигурации `anthropicBeta` с этим значением игнорируются при разрешении заголовков запроса, а неподдерживаемые старые модели Claude остаются на своем обычном контекстном окне.

`params.context1m: true` также применяется к бэкенду Claude CLI (`claude-cli/*`) для подходящих моделей Opus и Sonnet с поддержкой GA, сохраняя контекстное окно среды выполнения для этих CLI-сеансов в соответствии с поведением прямого API.

Контекст 1M Claude Opus 4.8

`anthropic/claude-opus-4-8` и его вариант `claude-cli` по умолчанию имеют окно контекста 1M — `params.context1m: true` не требуется.

## Устранение неполадок

Ошибки 401 / токен внезапно стал недействительным

Аутентификация токеном Anthropic истекает, и токен может быть отозван. Для новых настроек вместо этого используйте ключ API Anthropic.

Не найден ключ API для провайдера "anthropic"

Аутентификация Anthropic выполняется **для каждого агента** — новые агенты не наследуют ключи основного агента. Повторно выполните onboarding для этого агента (или настройте ключ API на хосте Gateway), затем проверьте с помощью `openclaw models status`.

Не найдены учетные данные для профиля "anthropic:default"

Запустите `openclaw models status`, чтобы увидеть, какой профиль аутентификации активен. Повторно выполните onboarding или настройте ключ API для этого пути профиля.

Нет доступного профиля аутентификации (все в периоде ожидания)

Проверьте `auth.unusableProfiles` в `openclaw models status --json`. Периоды ожидания из-за ограничения скорости Anthropic могут быть привязаны к модели, поэтому родственная модель Anthropic все еще может быть доступна. Добавьте еще один профиль Anthropic или дождитесь окончания периода ожидания.

## Связанные материалы

[**Выбор модели** Выбор провайдеров, ссылок на модели и поведения переключения при сбое. ](</ru/concepts/model-providers>) [**Бэкенды CLI** Настройка бэкенда Claude CLI и сведения о выполнении. ](</ru/gateway/cli-backends>) [**Кэширование промптов** Как кэширование промптов работает у разных провайдеров. ](</ru/reference/prompt-caching>) [**OAuth и аутентификация** Сведения об аутентификации и правила повторного использования учетных данных. ](</ru/gateway/authentication>)

Was this useful?YesNo

Open issue