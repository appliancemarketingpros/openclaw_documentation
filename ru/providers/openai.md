---
title: OpenAI
source_url: https://docs.openclaw.ai/ru/providers/openai
scraped_at: 2026-06-29
---

ModelsProviders

OpenAI предоставляет API для разработчиков для моделей GPT, а Codex также доступен как агент для программирования в рамках плана ChatGPT через клиенты Codex от OpenAI. OpenClaw использует один идентификатор провайдера, `openai`, для обеих форм аутентификации.

OpenClaw использует `openai/*` как канонический маршрут моделей OpenAI. Встроенные ходы агента на моделях OpenAI по умолчанию выполняются через нативную среду выполнения Codex app-server; прямая аутентификация по API-ключу OpenAI остается доступной для неагентских поверхностей OpenAI, таких как изображения, эмбеддинги, речь и realtime.

  * **Модели агентов** \- модели `openai/*` через среду выполнения Codex; войдите с аутентификацией Codex для использования подписки ChatGPT/Codex или настройте Codex-совместимый резервный API-ключ OpenAI, когда вы намеренно хотите аутентификацию по API-ключу.
  * **Неагентские API OpenAI** \- прямой доступ к OpenAI Platform с оплатой по использованию через `OPENAI_API_KEY` или онбординг API-ключа OpenAI.
  * **Устаревшая конфигурация** \- устаревшие ссылки на модели Codex исправляются `openclaw doctor --fix` на `openai/*` плюс среду выполнения Codex.


OpenAI явно поддерживает использование OAuth подписки во внешних инструментах и рабочих процессах, таких как OpenClaw.

Провайдер, модель, среда выполнения и канал - отдельные уровни. Если эти метки начинают смешиваться, прочитайте [Среды выполнения агентов](</ru/concepts/agent-runtimes>) перед изменением конфигурации.

## Быстрый выбор

Цель | Использовать | Примечания  
---|---|---  
Подписка ChatGPT/Codex с нативной средой выполнения Codex | `openai/gpt-5.5` | Настройка агента OpenAI по умолчанию. Войдите с аутентификацией Codex.  
Прямая тарификация по API-ключу для моделей агентов | `openai/gpt-5.5` плюс Codex-совместимый профиль API-ключа | Используйте `auth.order.openai`, чтобы разместить резерв после аутентификации подписки.  
Прямая тарификация по API-ключу через явный OpenClaw | `openai/gpt-5.5` плюс среда выполнения провайдера/модели `openclaw` | Выберите обычный профиль API-ключа `openai`.  
Последний API-псевдоним ChatGPT Instant | `openai/chat-latest` | Только прямой API-ключ. Перемещаемый псевдоним для экспериментов, не значение по умолчанию.  
Аутентификация подписки ChatGPT/Codex через OpenClaw | `openai/gpt-5.5` плюс среда выполнения провайдера/модели `openclaw` | Выберите OAuth-профиль `openai` для маршрута совместимости.  
Генерация или редактирование изображений | `openai/gpt-image-2` | Работает либо с `OPENAI_API_KEY`, либо с OpenAI Codex OAuth.  
Изображения с прозрачным фоном | `openai/gpt-image-1.5` | Используйте `outputFormat=png` или `webp` и `openai.background=transparent`.  
  
## Карта имен

Названия похожи, но не взаимозаменяемы:

Видимое имя | Уровень | Значение  
---|---|---  
`openai` | Префикс провайдера | Канонический маршрут моделей OpenAI; ходы агента используют среду выполнения Codex.  
устаревший префикс OpenAI Codex | Устаревший префикс | Старое пространство имен моделей/профилей. `openclaw doctor --fix` мигрирует его на `openai`.  
`codex` Plugin | Plugin | Встроенный Plugin OpenClaw, предоставляющий нативную среду выполнения Codex app-server и элементы управления чатом `/codex`.  
provider/model `agentRuntime.id: codex` | Среда выполнения агента | Принудительно включает нативный harness Codex app-server для совпадающих встроенных ходов.  
`/codex ...` | Набор команд чата | Привязывать/управлять потоками Codex app-server из разговора.  
`runtime: "acp", agentId: "codex"` | Маршрут сеанса ACP | Явный резервный путь, запускающий Codex через ACP/acpx.  
  
Это означает, что конфигурация может намеренно содержать ссылки на модели `openai/*`, тогда как профили аутентификации указывают либо на учетные данные API-ключа, либо на OAuth ChatGPT/Codex. Используйте `auth.order.openai` для конфигурации; `openclaw doctor --fix` переписывает устаревшие ссылки на модели Codex, устаревшие идентификаторы профилей аутентификации Codex и устаревший порядок аутентификации Codex на канонический маршрут OpenAI.

## Покрытие возможностей OpenClaw

Возможность OpenAI | Поверхность OpenClaw | Статус  
---|---|---  
Чат / Responses | провайдер моделей `openai/<model>` | Да  
Модели подписки Codex | `openai/<model>` с OpenAI OAuth | Да  
Устаревшие ссылки на модели Codex | устаревшие ссылки на модели Codex или `codex-cli/<model>` | Исправляются doctor на `openai/<model>`  
Harness Codex app-server | `openai/<model>` с пропущенной средой выполнения или provider/model `agentRuntime.id: codex` | Да  
Серверный веб-поиск | Нативный инструмент OpenAI Responses | Да, когда веб-поиск включен и провайдер не закреплен  
Изображения | `image_generate` | Да  
Видео | `video_generate` | Да  
Text-to-speech | `messages.tts.provider: "openai"` / `tts` | Да  
Пакетное speech-to-text | `tools.media.audio` / понимание медиа | Да  
Потоковое speech-to-text | Voice Call `streaming.provider: "openai"` | Да  
Realtime-голос | Voice Call `realtime.provider: "openai"` / Control UI Talk `talk.realtime.provider: "openai"` | Да (требуются кредиты OpenAI Platform, а не подписка Codex/ChatGPT)  
Эмбеддинги | провайдер эмбеддингов памяти | Да  
  
## Эмбеддинги памяти

OpenClaw может использовать OpenAI или OpenAI-совместимую конечную точку эмбеддингов для индексации `memory_search` и эмбеддингов запросов:

json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        provider: "openai",        model: "text-embedding-3-small",      },    },  },}
[/code]

Для OpenAI-совместимых конечных точек, которым требуются асимметричные метки эмбеддингов, задайте `queryInputType` и `documentInputType` в `memorySearch`. OpenClaw передает их как специфичные для провайдера поля запроса `input_type`: эмбеддинги запросов используют `queryInputType`; индексированные фрагменты памяти и пакетная индексация используют `documentInputType`. Полный пример см. в [справочнике по конфигурации памяти](</ru/reference/memory-config#provider-specific-config>).

## Начало работы

Выберите предпочтительный метод аутентификации и выполните шаги настройки.

### API-ключ (OpenAI Platform)

**Лучше всего для:** прямого доступа к API и тарификации по использованию.

* ### Получите свой API-ключ

Создайте или скопируйте API-ключ из [панели OpenAI Platform](<https://platform.openai.com/api-keys>).

* ### Запустите онбординг

bashCopy code
[code]
    openclaw onboard --auth-choice openai-api-key
[/code]

Или передайте ключ напрямую:

bashCopy code
[code]
    openclaw onboard --openai-api-key "$OPENAI_API_KEY"
[/code]

* ### Проверьте, что модель доступна

bashCopy code
[code]
    openclaw models list --provider openai
[/code]

### Сводка маршрутов

Ссылка на модель | Конфигурация среды выполнения | Маршрут | Аутентификация  
---|---|---|---  
`openai/gpt-5.5` | omitted / provider/model `agentRuntime.id: "codex"` | Harness Codex app-server | Codex-совместимый профиль OpenAI  
`openai/gpt-5.4-mini` | omitted / provider/model `agentRuntime.id: "codex"` | Harness Codex app-server | Codex-совместимый профиль OpenAI  
`openai/gpt-5.5` | provider/model `agentRuntime.id: "openclaw"` | Встроенная среда выполнения OpenClaw | Выбранный профиль `openai`  
  
### Пример конфигурации

json5Copy code
[code]
    {  env: { OPENAI_API_KEY: "example-openai-key-not-real" },  agents: { defaults: { model: { primary: "openai/gpt-5.5" } } },}
[/code]

Чтобы попробовать текущую модель Instant из ChatGPT через OpenAI API, задайте модель как `openai/chat-latest`:

json5Copy code
[code]
    {  env: { OPENAI_API_KEY: "example-openai-key-not-real" },  agents: { defaults: { model: { primary: "openai/chat-latest" } } },}
[/code]

`chat-latest` — плавающий псевдоним. OpenAI документирует его как последнюю модель Instant, используемую в ChatGPT, и рекомендует `gpt-5.5` для промышленного использования API, поэтому оставляйте `openai/gpt-5.5` стабильным значением по умолчанию, если только вам явно не нужно поведение этого псевдонима. Сейчас псевдоним принимает только `medium` для степени подробности текста, поэтому OpenClaw нормализует несовместимые переопределения степени подробности текста OpenAI для этой модели.

### Подписка Codex

**Лучше всего подходит для:** использования вашей подписки ChatGPT/Codex с нативным выполнением через сервер приложения Codex вместо отдельного API-ключа. Для облака Codex требуется вход в ChatGPT.

* ### Запустите OAuth Codex

bashCopy code
[code]
    openclaw onboard --auth-choice openai
[/code]

Или запустите OAuth напрямую:

bashCopy code
[code]
    openclaw models auth login --provider openai
[/code]

Для безголовых или несовместимых с callback настроек добавьте `--device-code`, чтобы войти через поток кода устройства ChatGPT вместо браузерного callback на localhost:

bashCopy code
[code]
    openclaw models auth login --provider openai --device-code
[/code]

* ### Используйте канонический маршрут модели OpenAI

bashCopy code
[code]
    openclaw config set agents.defaults.model.primary openai/gpt-5.5
[/code]

Для пути по умолчанию конфигурация runtime не требуется. Ходы агента OpenAI автоматически выбирают нативный runtime сервера приложения Codex, а OpenClaw устанавливает или восстанавливает встроенный Plugin Codex, когда выбран этот маршрут.

* ### Проверьте доступность аутентификации Codex

bashCopy code
[code]
    openclaw models list --provider openai
[/code]

После запуска Gateway отправьте `/codex status` или `/codex models` в чат, чтобы проверить нативный runtime сервера приложения.

### Сводка маршрутов

Ссылка на модель | Конфигурация runtime | Маршрут | Аутентификация  
---|---|---|---  
`openai/gpt-5.5` | опущена / provider/model `agentRuntime.id: "codex"` | Нативный harness сервера приложения Codex | Вход Codex или упорядоченный профиль аутентификации `openai`  
`openai/gpt-5.5` | provider/model `agentRuntime.id: "openclaw"` | Встроенный runtime OpenClaw с внутренним транспортом аутентификации Codex | Выбранный профиль OAuth `openai`  
устаревшая ссылка Codex GPT-5.5 | исправляется doctor | Устаревший маршрут переписывается в `openai/gpt-5.5` | Перенесенный профиль OAuth OpenAI  
`codex-cli/gpt-5.5` | исправляется doctor | Устаревший маршрут CLI переписывается в `openai/gpt-5.5` | Аутентификация сервера приложения Codex  
  
### Пример конфигурации

json5Copy code
[code]
    {  plugins: { entries: { codex: { enabled: true } } },  agents: {    defaults: {      model: { primary: "openai/gpt-5.5" },    },  },}
[/code]

При резервном API-ключе оставьте модель на `openai/gpt-5.5` и поместите порядок аутентификации в `openai`. OpenClaw сначала попробует подписку, затем API-ключ, оставаясь на harness Codex:

json5Copy code
[code]
    {  plugins: { entries: { codex: { enabled: true } } },  agents: {    defaults: {      model: { primary: "openai/gpt-5.5" },    },  },  auth: {    order: {      openai: [        "openai:user@example.com",        "openai:api-key-backup",      ],    },  },}
[/code]

### Проверка и восстановление маршрутизации OAuth Codex

Используйте эти команды, чтобы увидеть, какие модель, runtime и маршрут аутентификации использует ваш агент по умолчанию:

bashCopy code
[code]
    openclaw models statusopenclaw models auth list --provider openaiopenclaw config get agents.defaults.model --jsonopenclaw config get models.providers.openai.agentRuntime --json
[/code]

Для конкретного агента добавьте `--agent <id>`:

bashCopy code
[code]
    openclaw models status --agent <id>openclaw models auth list --agent <id> --provider openai
[/code]

Если в старой конфигурации все еще есть устаревшие ссылки Codex GPT или устаревшее закрепление сессии runtime OpenAI без явной конфигурации runtime, исправьте это:

bashCopy code
[code]
    openclaw doctor --fixopenclaw config validate
[/code]

Если `models auth list --provider openai` не показывает пригодного профиля, войдите снова:

bashCopy code
[code]
    openclaw models auth login --provider openaiopenclaw models status --probe --probe-provider openai
[/code]

Используйте `--profile-id`, когда вам нужно несколько входов OAuth Codex в одном агенте и позже нужно управлять ими через порядок аутентификации или `/model ...@<profileId>`:

bashCopy code
[code]
    openclaw models auth login --provider openai --profile-id openai:ritsukoopenclaw models auth login --provider openai --profile-id openai:lain
[/code]

`openai/*` — это маршрут модели для ходов агента OpenAI через Codex. Запустите `openclaw doctor --fix`, чтобы перенести старые устаревшие идентификаторы профилей с префиксом OpenAI Codex и записи порядка перед тем, как полагаться на упорядочивание профилей.

### Индикатор состояния

Чат `/status` показывает, какой runtime модели активен для текущей сессии. Встроенный harness сервера приложения Codex отображается как `Runtime: OpenAI Codex` для ходов модели агента OpenAI. Устаревшие закрепления сессии runtime OpenAI исправляются на Codex, если только конфигурация явно не закрепляет OpenClaw.

### Предупреждение doctor

Если устаревшие ссылки моделей Codex или устаревшие закрепления runtime OpenAI остаются в конфигурации или состоянии сессии, `openclaw doctor --fix` переписывает их в `openai/*` с runtime Codex, если OpenClaw не настроен явно.

### Лимит окна контекста

OpenClaw рассматривает метаданные модели и лимит контекста runtime как отдельные значения.

Для `openai/gpt-5.5` через каталог OAuth Codex:

  * Нативный `contextWindow`: `1000000`
  * Лимит runtime `contextTokens` по умолчанию: `272000`


Меньший лимит по умолчанию на практике дает лучшую задержку и качество. Переопределите его с помощью `contextTokens`:

json5Copy code
[code]
    {  models: {    providers: {      openai: {        models: [{ id: "gpt-5.5", contextTokens: 160000 }],      },    },  },}
[/code]

### Восстановление каталога

OpenClaw использует upstream-метаданные каталога Codex для `gpt-5.5`, когда они присутствуют. Если live-обнаружение Codex пропускает строку `gpt-5.5`, пока аккаунт аутентифицирован, OpenClaw синтезирует эту строку модели OAuth, чтобы запуски cron, подагента и настроенной модели по умолчанию не завершались ошибкой `Unknown model`.

## Нативная аутентификация сервера приложения Codex

Нативный harness сервера приложения Codex использует ссылки моделей `openai/*` плюс опущенную конфигурацию runtime или provider/model `agentRuntime.id: "codex"`, но его аутентификация по-прежнему основана на аккаунте. OpenClaw выбирает аутентификацию в таком порядке:

  1. Упорядоченные профили аутентификации OpenAI для агента, предпочтительно в `auth.order.openai`. Запустите `openclaw doctor --fix`, чтобы перенести старые устаревшие идентификаторы профилей аутентификации Codex и устаревший порядок аутентификации Codex.
  2. Существующий аккаунт сервера приложения, например локальный вход ChatGPT в Codex CLI.
  3. Только для локальных запусков stdio сервера приложения: `CODEX_API_KEY`, затем `OPENAI_API_KEY`, когда сервер приложения сообщает об отсутствии аккаунта и все еще требует аутентификацию OpenAI.


Это означает, что локальный вход с подпиской ChatGPT/Codex не заменяется только потому, что у процесса Gateway также есть `OPENAI_API_KEY` для прямых моделей OpenAI или эмбеддингов. Резервный env API-ключ используется только для локального пути stdio без аккаунта; он не отправляется в WebSocket-соединения сервера приложения. Когда выбран профиль Codex в стиле подписки, OpenClaw также не передает `CODEX_API_KEY` и `OPENAI_API_KEY` в дочерний процесс stdio сервера приложения и отправляет выбранные учетные данные через RPC входа сервера приложения. Когда этот профиль подписки заблокирован лимитом использования Codex, OpenClaw может переключиться на следующий упорядоченный профиль API-ключа `openai:*` без изменения выбранной модели или выхода из harness Codex. После времени сброса подписки профиль подписки снова становится доступным.

## Генерация изображений

Встроенный Plugin `openai` регистрирует генерацию изображений через инструмент `image_generate`. Он поддерживает как генерацию изображений по API-ключу OpenAI, так и генерацию изображений через OAuth Codex через одну и ту же ссылку модели `openai/gpt-image-2`.

Возможность | API-ключ OpenAI | OAuth Codex  
---|---|---  
Ссылка на модель | `openai/gpt-image-2` | `openai/gpt-image-2`  
Аутентификация | `OPENAI_API_KEY` | Вход OAuth OpenAI Codex  
Транспорт | OpenAI Images API | Backend Codex Responses  
Максимум изображений на запрос | 4 | 4  
Режим редактирования | Включен (до 5 референсных изображений) | Включен (до 5 референсных изображений)  
Переопределения размера | Поддерживаются, включая размеры 2K/4K | Поддерживаются, включая размеры 2K/4K  
Соотношение сторон / разрешение | Не передается в OpenAI Images API | Сопоставляется с поддерживаемым размером, когда это безопасно  
  
json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: { primary: "openai/gpt-image-2" },    },  },}
[/code]

`gpt-image-2` используется по умолчанию как для генерации изображений по тексту OpenAI, так и для редактирования изображений. `gpt-image-1.5`, `gpt-image-1` и `gpt-image-1-mini` остаются доступными как явные переопределения модели. Используйте `openai/gpt-image-1.5` для вывода PNG/WebP с прозрачным фоном; текущий API `gpt-image-2` отклоняет `background: "transparent"`.

Для запроса с прозрачным фоном agents должны вызывать `image_generate` с `model: "openai/gpt-image-1.5"`, `outputFormat: "png"` или `"webp"` и `background: "transparent"`; более старый параметр провайдера `openai.background` по-прежнему принимается. OpenClaw также защищает публичные маршруты OAuth OpenAI и OpenAI Codex, переписывая прозрачные запросы по умолчанию `openai/gpt-image-2` на `gpt-image-1.5`; Azure и пользовательские OpenAI-совместимые конечные точки сохраняют настроенные имена развертываний/моделей.

Та же настройка доступна для headless-запусков CLI:

bashCopy code
[code]
    openclaw infer image generate \  --model openai/gpt-image-1.5 \  --output-format png \  --background transparent \  --prompt "A simple red circle sticker on a transparent background" \  --json
[/code]

Используйте те же флаги `--output-format` и `--background` с `openclaw infer image edit`, когда начинаете с входного файла. `--openai-background` остается доступным как OpenAI-специфичный псевдоним. Используйте `--quality low|medium|high|auto`, когда нужно управлять качеством и стоимостью OpenAI Images. Используйте `--openai-moderation low|auto`, чтобы передать OpenAI специфичную для провайдера подсказку модерации из `image generate` или `image edit`.

Для установок ChatGPT/Codex OAuth сохраняйте ту же ссылку `openai/gpt-image-2`. Когда настроен OAuth-профиль `openai`, OpenClaw разрешает сохраненный OAuth-токен доступа и отправляет запросы изображений через backend Codex Responses. Он не пытается сначала использовать `OPENAI_API_KEY` и не выполняет тихий откат к API-ключу для этого запроса. Настройте `models.providers.openai` явно с API-ключом, пользовательским базовым URL или конечной точкой Azure, когда нужен прямой маршрут OpenAI Images API. Если эта пользовательская конечная точка изображений находится в доверенной LAN/частной адресации, также задайте `browser.ssrfPolicy.dangerouslyAllowPrivateNetwork: true`; OpenClaw оставляет частные/внутренние OpenAI-совместимые конечные точки изображений заблокированными, если это явное согласие не присутствует.

Сгенерировать:

CodeCopy code
[code]
    /tool image_generate model=openai/gpt-image-2 prompt="A polished launch poster for OpenClaw on macOS" size=3840x2160 count=1
[/code]

Сгенерировать прозрачный PNG:

CodeCopy code
[code]
    /tool image_generate model=openai/gpt-image-1.5 prompt="A simple red circle sticker on a transparent background" outputFormat=png background=transparent
[/code]

Редактировать:

CodeCopy code
[code]
    /tool image_generate model=openai/gpt-image-2 prompt="Preserve the object shape, change the material to translucent glass" image=/path/to/reference.png size=1024x1536
[/code]

## Генерация видео

Встроенный Plugin `openai` регистрирует генерацию видео через инструмент `video_generate`.

Возможность | Значение  
---|---  
Модель по умолчанию | `openai/sora-2`  
Режимы | Текст-в-видео, изображение-в-видео, редактирование одного видео  
Входные референсы | 1 изображение или 1 видео  
Переопределения размера | Поддерживаются для текста-в-видео и изображения-в-видео  
Другие переопределения | `aspectRatio`, `resolution`, `audio`, `watermark` игнорируются с предупреждением инструмента  
  
Запросы OpenAI изображение-в-видео используют `POST /v1/videos` с изображением `input_reference`. Редактирование одного видео использует `POST /v1/videos/edits` с загруженным видео в поле `video`.

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: { primary: "openai/sora-2" },    },  },}
[/code]

## Вклад в промпт GPT-5

OpenClaw добавляет общий вклад в промпт GPT-5 для запусков семейства GPT-5 на поверхностях промптов, собранных OpenClaw. Он применяется по id модели, поэтому маршруты OpenClaw/провайдеров, такие как устаревшие ссылки до исправления (устаревшая ссылка Codex GPT-5.5), `openrouter/openai/gpt-5.5`, `opencode/gpt-5.5` и другие совместимые ссылки GPT-5 получают тот же overlay. Более старые модели GPT-4.x не получают его.

Встроенный нативный harness Codex не получает этот GPT-5 overlay OpenClaw через developer instructions сервера приложения Codex. Нативный Codex сохраняет принадлежащее Codex поведение base, model и project-doc, а OpenClaw отключает встроенную personality Codex для нативных threads, чтобы файлы personality рабочей области agent оставались авторитетными. OpenClaw добавляет только runtime-контекст, такой как доставка канала, динамические инструменты OpenClaw, делегирование ACP, контекст рабочей области и OpenClaw Skills.

Вклад GPT-5 добавляет помеченный контракт поведения для сохранения persona, безопасности выполнения, дисциплины инструментов, формы вывода, проверок завершения и верификации на соответствующих промптах, собранных OpenClaw. Поведение ответов, специфичное для каналов, и silent-message остается в общем системном промпте OpenClaw и политике исходящей доставки. Дружественный слой стиля взаимодействия отделен и настраивается.

Значение | Эффект  
---|---  
`"friendly"` (по умолчанию) | Включить дружественный слой стиля взаимодействия  
`"on"` | Псевдоним для `"friendly"`  
`"off"` | Отключить только дружественный слой стиля  
  
### Конфиг

json5Copy code
[code]
    {  agents: {    defaults: {      promptOverlays: {        gpt5: { personality: "friendly" },      },    },  },}
[/code]

### CLI

bashCopy code
[code]
    openclaw config set agents.defaults.promptOverlays.gpt5.personality off
[/code]

## Голос и речь

Синтез речи (TTS)

Встроенный Plugin `openai` регистрирует синтез речи для поверхности `messages.tts`.

Настройка | Путь конфига | По умолчанию  
---|---|---  
Модель | `messages.tts.providers.openai.model` | `gpt-4o-mini-tts`  
Голос | `messages.tts.providers.openai.speakerVoice` | `coral`  
Скорость | `messages.tts.providers.openai.speed` | (не задано)  
Инструкции | `messages.tts.providers.openai.instructions` | (не задано, только `gpt-4o-mini-tts`)  
Формат | `messages.tts.providers.openai.responseFormat` | `opus` для голосовых заметок, `mp3` для файлов  
API-ключ | `messages.tts.providers.openai.apiKey` | Откатывается к `OPENAI_API_KEY`  
Базовый URL | `messages.tts.providers.openai.baseUrl` | `https://api.openai.com/v1`  
Дополнительное тело | `messages.tts.providers.openai.extraBody` / `extra_body` | (не задано)  
  
Доступные модели: `gpt-4o-mini-tts`, `tts-1`, `tts-1-hd`. Доступные голоса: `alloy`, `ash`, `ballad`, `cedar`, `coral`, `echo`, `fable`, `juniper`, `marin`, `onyx`, `nova`, `sage`, `shimmer`, `verse`.

`extraBody` объединяется с JSON запроса `/audio/speech` после сгенерированных OpenClaw полей, поэтому используйте его для OpenAI-совместимых конечных точек, которым требуются дополнительные ключи, такие как `lang`. Prototype-ключи игнорируются.

json5Copy code
[code]
    {  messages: {    tts: {      providers: {        openai: { model: "gpt-4o-mini-tts", speakerVoice: "coral" },      },    },  },}
[/code]

Речь-в-текст

Встроенный Plugin `openai` регистрирует пакетное распознавание речь-в-текст через поверхность транскрипции media-understanding OpenClaw.

  * Модель по умолчанию: `gpt-4o-transcribe`
  * Конечная точка: OpenAI REST `/v1/audio/transcriptions`
  * Путь ввода: загрузка multipart-аудиофайла
  * Поддерживается OpenClaw везде, где входящая аудиотранскрипция использует `tools.media.audio`, включая сегменты голосовых каналов Discord и аудиовложения каналов


Чтобы принудительно использовать OpenAI для входящей аудиотранскрипции:

json5Copy code
[code]
    {  tools: {    media: {      audio: {        models: [          {            type: "provider",            provider: "openai",            model: "gpt-4o-transcribe",          },        ],      },    },  },}
[/code]

Подсказки языка и промпта пересылаются в OpenAI, когда они предоставлены общей конфигурацией audio media или запросом транскрипции для конкретного вызова.

Realtime-транскрипция

Встроенный Plugin `openai` регистрирует realtime-транскрипцию для Plugin Voice Call.

Настройка | Путь конфига | По умолчанию  
---|---|---  
Модель | `plugins.entries.voice-call.config.streaming.providers.openai.model` | `gpt-4o-transcribe`  
Язык | `...openai.language` | (не задано)  
Промпт | `...openai.prompt` | (не задано)  
Длительность тишины | `...openai.silenceDurationMs` | `800`  
Порог VAD | `...openai.vadThreshold` | `0.5`  
Аутентификация | `...openai.apiKey`, `OPENAI_API_KEY` или OAuth `openai` | API-ключи подключаются напрямую; OAuth выпускает клиентский секрет Realtime-транскрипции  
  
Realtime voice

Встроенный Plugin `openai` регистрирует realtime voice для Plugin Voice Call.

Настройка | Путь конфига | По умолчанию  
---|---|---  
Модель | `plugins.entries.voice-call.config.realtime.providers.openai.model` | `gpt-realtime-2`  
Голос | `...openai.voice` | `alloy`  
Температура (мост развертывания Azure) | `...openai.temperature` | `0.8`  
Порог VAD | `...openai.vadThreshold` | `0.5`  
Длительность тишины | `...openai.silenceDurationMs` | `500`  
Prefix padding | `...openai.prefixPaddingMs` | `300`  
Reasoning effort | `...openai.reasoningEffort` | (не задано)  
Аутентификация | API-key auth profile `openai`, `...openai.apiKey` или `OPENAI_API_KEY` | Требуется API-ключ OpenAI Platform; OpenAI OAuth не настраивает Realtime voice  
  
Доступные встроенные Realtime-голоса для `gpt-realtime-2`: `alloy`, `ash`, `ballad`, `coral`, `echo`, `sage`, `shimmer`, `verse`, `marin`, `cedar`. OpenAI рекомендует `marin` и `cedar` для лучшего качества Realtime. Это отдельный набор от голосов Text-to-speech выше; не предполагайте, что TTS-голос, такой как `fable`, `nova` или `onyx`, действителен для Realtime-сессий.

## Конечные точки Azure OpenAI

Встроенный провайдер `openai` может обращаться к ресурсу Azure OpenAI для генерации изображений через переопределение базового URL. На пути генерации изображений OpenClaw обнаруживает имена хостов Azure в `models.providers.openai.baseUrl` и автоматически переключается на формат запросов Azure.

Используйте Azure OpenAI, когда:

  * У вас уже есть подписка, квота или корпоративное соглашение Azure OpenAI
  * Вам нужны региональное размещение данных или средства контроля соответствия, которые предоставляет Azure
  * Вы хотите удерживать трафик внутри существующего тенанта Azure


### Конфигурация

Для генерации изображений Azure через встроенный провайдер `openai` укажите в `models.providers.openai.baseUrl` ваш ресурс Azure и задайте `apiKey` как ключ Azure OpenAI (а не ключ OpenAI Platform):

json5Copy code
[code]
    {  models: {    providers: {      openai: {        baseUrl: "https://<your-resource>.openai.azure.com",        apiKey: "<azure-openai-api-key>",      },    },  },}
[/code]

OpenClaw распознает эти суффиксы хостов Azure для маршрута генерации изображений Azure:

  * `*.openai.azure.com`
  * `*.services.ai.azure.com`
  * `*.cognitiveservices.azure.com`


Для запросов генерации изображений на распознанном хосте Azure OpenClaw:

  * Отправляет заголовок `api-key` вместо `Authorization: Bearer`
  * Использует пути в области deployment (`/openai/deployments/{deployment}/...`)
  * Добавляет `?api-version=...` к каждому запросу
  * Использует стандартный тайм-аут запроса 600 с для вызовов генерации изображений Azure. Значения `timeoutMs` для отдельных вызовов по-прежнему переопределяют это значение по умолчанию.


Другие базовые URL (публичный OpenAI, OpenAI-совместимые прокси) сохраняют стандартный формат запросов изображений OpenAI.

### Версия API

Задайте `AZURE_OPENAI_API_VERSION`, чтобы закрепить конкретную preview- или GA-версию Azure для пути генерации изображений Azure:

bashCopy code
[code]
    export AZURE_OPENAI_API_VERSION="2024-12-01-preview"
[/code]

По умолчанию используется `2024-12-01-preview`, если переменная не задана.

### Имена моделей — это имена deployment

Azure OpenAI привязывает модели к deployment. Для запросов генерации изображений Azure, маршрутизируемых через встроенный провайдер `openai`, поле `model` в OpenClaw должно быть **именем deployment Azure** , которое вы настроили на портале Azure, а не публичным идентификатором модели OpenAI.

Если вы создаете deployment с именем `gpt-image-2-prod`, который обслуживает `gpt-image-2`:

CodeCopy code
[code]
    /tool image_generate model=openai/gpt-image-2-prod prompt="A clean poster" size=1024x1024 count=1
[/code]

То же правило имени deployment применяется к вызовам генерации изображений, маршрутизируемым через встроенный провайдер `openai`.

### Региональная доступность

Генерация изображений Azure сейчас доступна только в части регионов (например, `eastus2`, `swedencentral`, `polandcentral`, `westus3`, `uaenorth`). Перед созданием deployment проверьте актуальный список регионов Microsoft и подтвердите, что конкретная модель доступна в вашем регионе.

### Различия параметров

Azure OpenAI и публичный OpenAI не всегда принимают одинаковые параметры изображений. Azure может отклонять параметры, которые разрешает публичный OpenAI (например, некоторые значения `background` в `gpt-image-2`), или предоставлять их только в конкретных версиях модели. Эти различия исходят от Azure и базовой модели, а не от OpenClaw. Если запрос Azure завершается ошибкой валидации, проверьте набор параметров, поддерживаемый вашим конкретным deployment и версией API, на портале Azure.

## Расширенная конфигурация

Транспорт (WebSocket и SSE)

OpenClaw для `openai/*` сначала использует WebSocket с резервным переходом на SSE (`"auto"`).

В режиме `"auto"` OpenClaw:

  * Повторяет один ранний сбой WebSocket перед переходом на SSE
  * После сбоя помечает WebSocket как деградировавший примерно на 60 секунд и использует SSE во время охлаждения
  * Прикрепляет стабильные заголовки идентичности сеанса и хода для повторов и переподключений
  * Нормализует счетчики использования (`input_tokens` / `prompt_tokens`) между вариантами транспорта


Значение | Поведение  
---|---  
`"auto"` (по умолчанию) | Сначала WebSocket, резервный переход на SSE  
`"sse"` | Принудительно только SSE  
`"websocket"` | Принудительно только WebSocket  
  
json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "openai/gpt-5.5": {          params: { transport: "auto" },        },      },    },  },}
[/code]

Связанная документация OpenAI:

  * [Realtime API with WebSocket](<https://platform.openai.com/docs/guides/realtime-websocket>)
  * [Streaming API responses (SSE)](<https://platform.openai.com/docs/guides/streaming-responses>)

Быстрый режим

OpenClaw предоставляет общий переключатель быстрого режима для `openai/*`:

  * **Chat/UI:** `/fast status|auto|on|off`
  * **Конфигурация:** `agents.defaults.models["<provider>/<model>"].params.fastMode`


Когда он включен, OpenClaw сопоставляет быстрый режим с приоритетной обработкой OpenAI (`service_tier = "priority"`). Существующие значения `service_tier` сохраняются, а быстрый режим не переписывает `reasoning` или `text.verbosity`. `fastMode: "auto"` запускает новые вызовы модели в быстром режиме до автоматического порога, а последующие вызовы retry, fallback, tool-result или continuation запускает без быстрого режима. Порог по умолчанию — 60 секунд; чтобы изменить его, задайте `params.fastAutoOnSeconds` для активной модели.

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "openai/gpt-5.5": { params: { fastMode: "auto", fastAutoOnSeconds: 30 } },      },    },  },}
[/code]

Приоритетная обработка (service_tier)

API OpenAI предоставляет приоритетную обработку через `service_tier`. Задайте ее в OpenClaw для каждой модели:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "openai/gpt-5.5": { params: { serviceTier: "priority" } },      },    },  },}
[/code]

Поддерживаемые значения: `auto`, `default`, `flex`, `priority`.

Server-side compaction (Responses API)

Для прямых моделей OpenAI Responses (`openai/*` на `api.openai.com`) обертка потока OpenClaw в Plugin OpenAI автоматически включает серверную Compaction:

  * Принудительно задает `store: true` (если совместимость модели не задает `supportsStore: false`)
  * Внедряет `context_management: [{ type: "compaction", compact_threshold: ... }]`
  * Значение `compact_threshold` по умолчанию: 70% от `contextWindow` (или `80000`, если оно недоступно)


Это применяется к встроенному runtime-пути OpenClaw и к хукам провайдера OpenAI, используемым встроенными запусками. Нативный app-server harness Codex управляет собственным контекстом через Codex и настраивается маршрутом агента OpenAI по умолчанию или runtime-политикой провайдера/модели.

### Включить явно

Полезно для совместимых конечных точек, таких как Azure OpenAI Responses:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "azure-openai-responses/gpt-5.5": {          params: { responsesServerCompaction: true },        },      },    },  },}
[/code]

### Пользовательский порог

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "openai/gpt-5.5": {          params: {            responsesServerCompaction: true,            responsesCompactThreshold: 120000,          },        },      },    },  },}
[/code]

### Отключить

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "openai/gpt-5.5": {          params: { responsesServerCompaction: false },        },      },    },  },}
[/code]

Строгий агентный режим GPT

Для запусков семейства GPT-5 на `openai/*` OpenClaw может использовать более строгий встроенный контракт выполнения:

json5Copy code
[code]
    {  agents: {    defaults: {      embeddedAgent: { executionContract: "strict-agentic" },    },  },}
[/code]

С `strict-agentic` OpenClaw:

  * Автоматически включает `update_plan` для существенной работы
  * Повторяет структурно пустые или состоящие только из reasoning ходы с continuation видимого ответа
  * Использует явные события плана harness, когда выбранный harness их предоставляет


OpenClaw не классифицирует прозу ассистента, чтобы решить, является ли ход планом, обновлением прогресса или финальным ответом.

Нативные и OpenAI-совместимые маршруты

OpenClaw обрабатывает прямые конечные точки OpenAI, Codex и Azure OpenAI иначе, чем универсальные OpenAI-совместимые прокси `/v1`:

**Нативные маршруты** (`openai/*`, Azure OpenAI):

  * Сохраняют `reasoning: { effort: "none" }` только для моделей, которые поддерживают effort OpenAI `none`
  * Опускают отключенный reasoning для моделей или прокси, которые отклоняют `reasoning.effort: "none"`
  * По умолчанию переводят схемы инструментов в строгий режим
  * Прикрепляют скрытые заголовки атрибуции только на проверенных нативных хостах
  * Сохраняют форматирование запросов, специфичное для OpenAI (`service_tier`, `store`, reasoning-compat, подсказки prompt-cache)


**Прокси-/совместимые маршруты:**

  * Используют менее строгое совместимое поведение
  * Удаляют `store` Completions из неродных payload `openai-completions`
  * Принимают сквозной JSON для расширенных `params.extra_body`/`params.extraBody` для OpenAI-совместимых прокси Completions
  * Принимают `params.chat_template_kwargs` для OpenAI-совместимых прокси Completions, таких как vLLM
  * Не требуют строгих схем инструментов или заголовков только для родного транспорта


Azure OpenAI использует родной транспорт и совместимое поведение, но не получает скрытые заголовки атрибуции.

## Связанные материалы

[**Model selection** Выбор провайдеров, ссылок на модели и поведения при переключении при сбое. ](</ru/concepts/model-providers>) [**Image generation** Общие параметры инструмента изображений и выбор провайдера. ](</ru/tools/image-generation>) [**Video generation** Общие параметры инструмента видео и выбор провайдера. ](</ru/tools/video-generation>) [**OAuth and auth** Сведения об auth и правила повторного использования учетных данных. ](</ru/gateway/authentication>)

Was this useful?YesNo

Open issue