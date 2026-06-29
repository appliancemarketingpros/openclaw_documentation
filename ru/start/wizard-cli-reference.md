---
title: Справочник по настройке CLI
source_url: https://docs.openclaw.ai/ru/start/wizard-cli-reference
scraped_at: 2026-06-29
---

Get startedGuides

Эта страница является полным справочником по `openclaw onboard`. Краткое руководство см. в разделе [Онбординг (CLI)](</ru/start/wizard>).

## Что делает мастер

Локальный режим (по умолчанию) проводит вас через:

  * Настройку модели и аутентификации (OAuth для подписки OpenAI Code, CLI или API-ключ Anthropic Claude, а также варианты MiniMax, GLM, Ollama, Moonshot, StepFun и AI Gateway)
  * Расположение рабочей области и файлы начальной настройки
  * Настройки Gateway (порт, привязка, аутентификация, Tailscale)
  * Каналы и провайдеры (Telegram, WhatsApp, Discord, Google Chat, Mattermost, Signal, iMessage и другие встроенные Plugin каналов)
  * Установку демона (LaunchAgent, пользовательский юнит systemd или нативная запланированная задача Windows с резервным вариантом через папку Startup)
  * Проверку работоспособности
  * Настройку Skills


Удаленный режим настраивает этот компьютер для подключения к Gateway в другом месте. Он не устанавливает и не изменяет ничего на удаленном хосте.

## Подробности локального процесса

* ### Обнаружение существующей конфигурации

  * Если `~/.openclaw/openclaw.json` существует, выберите Keep, Modify или Reset.
  * Повторный запуск мастера ничего не удаляет, если вы явно не выберете Reset (или не передадите `--reset`).
  * CLI `--reset` по умолчанию использует `config+creds+sessions`; используйте `--reset-scope full`, чтобы также удалить рабочую область.
  * Если конфигурация недействительна или содержит устаревшие ключи, мастер останавливается и просит запустить `openclaw doctor` перед продолжением.
  * Reset использует `trash` и предлагает области: 
    * Только конфигурация
    * Конфигурация + учетные данные + сессии
    * Полный сброс (также удаляет рабочую область)


* ### Модель и аутентификация

  * Полная матрица вариантов находится в разделе Варианты аутентификации и моделей.


* ### Рабочая область

  * По умолчанию `~/.openclaw/workspace` (настраивается).
  * Создает начальные файлы рабочей области, необходимые для ритуала начальной загрузки при первом запуске.
  * Структура рабочей области: [Рабочая область агента](</ru/concepts/agent-workspace>).


* ### Gateway

  * Запрашивает порт, привязку, режим аутентификации и публикацию через Tailscale.
  * Рекомендуется: оставьте аутентификацию по токену включенной даже для loopback, чтобы локальные WS-клиенты должны были проходить аутентификацию.
  * В режиме токена интерактивная настройка предлагает: 
    * **Сгенерировать/сохранить токен в открытом виде** (по умолчанию)
    * **Использовать SecretRef** (по выбору)
  * В режиме пароля интерактивная настройка также поддерживает хранение в открытом виде или SecretRef.
  * Неинтерактивный путь SecretRef для токена: `--gateway-token-ref-env &lt;ENV_VAR&gt;`. 
    * Требует непустую переменную окружения в окружении процесса онбординга.
    * Не может сочетаться с `--gateway-token`.
  * Отключайте аутентификацию только если полностью доверяете каждому локальному процессу.
  * Привязки не к loopback по-прежнему требуют аутентификации.


* ### Каналы

  * [WhatsApp](</ru/channels/whatsapp>): необязательный вход по QR-коду
  * [Telegram](</ru/channels/telegram>): токен бота
  * [Discord](</ru/channels/discord>): токен бота
  * [Google Chat](</ru/channels/googlechat>): JSON сервисного аккаунта + аудитория Webhook
  * [Mattermost](</ru/channels/mattermost>): токен бота + базовый URL
  * [Signal](</ru/channels/signal>): необязательная установка `signal-cli` \+ конфигурация аккаунта
  * [iMessage](</ru/channels/imessage>): путь к CLI `imsg` \+ доступ к БД Messages; используйте SSH-обертку, когда Gateway работает не на Mac
  * Безопасность DM: по умолчанию используется сопряжение. Первый DM отправляет код; подтвердите через `openclaw pairing approve <channel> <code>` или используйте списки разрешенных.


* ### Установка демона

  * macOS: LaunchAgent 
    * Требуется пользовательская сессия с входом в систему; для headless-сценария используйте пользовательский LaunchDaemon (не поставляется).
  * Linux и Windows через WSL2: пользовательский юнит systemd 
    * Мастер пытается выполнить `loginctl enable-linger <user>`, чтобы gateway оставался запущенным после выхода из системы.
    * Может запросить sudo (записывает в `/var/lib/systemd/linger`); сначала пробует без sudo.
  * Нативная Windows: сначала Scheduled Task 
    * Если создание задачи запрещено, OpenClaw переключается на пользовательский элемент входа в папке Startup и сразу запускает gateway.
    * Scheduled Tasks остаются предпочтительными, потому что предоставляют лучший статус супервизора.
  * Выбор runtime: Node (рекомендуется; требуется для WhatsApp и Telegram). Bun не рекомендуется.


* ### Проверка работоспособности

  * Запускает gateway (если нужно) и выполняет `openclaw health`.
  * `openclaw status --deep` добавляет к выводу статуса live-пробу работоспособности gateway, включая пробы каналов, когда они поддерживаются.


* ### Skills

  * Читает доступные Skills и проверяет требования.
  * Позволяет выбрать менеджер node: npm, pnpm или bun.
  * Устанавливает необязательные зависимости (некоторые используют Homebrew на macOS).


* ### Завершение

  * Сводка и следующие шаги, включая варианты приложений для iOS, Android и macOS.


## Подробности удаленного режима

Удаленный режим настраивает этот компьютер для подключения к Gateway в другом месте.

Что вы задаете:

  * URL удаленного gateway (`ws://...`)
  * Токен, если удаленному gateway требуется аутентификация (рекомендуется)


## Варианты аутентификации и моделей

API-ключ Anthropic

Использует `ANTHROPIC_API_KEY`, если он присутствует, или запрашивает ключ, затем сохраняет его для использования демоном.

Подписка OpenAI Code (OAuth)

Поток через браузер; вставьте `code#state`.

Устанавливает `agents.defaults.model` в `openai/gpt-5.5` через runtime Codex, когда модель не задана или уже относится к семейству OpenAI.

Подписка OpenAI Code (сопряжение устройства)

Поток сопряжения через браузер с краткоживущим кодом устройства.

Устанавливает `agents.defaults.model` в `openai/gpt-5.5` через runtime Codex, когда модель не задана или уже относится к семейству OpenAI.

API-ключ OpenAI

Использует `OPENAI_API_KEY`, если он присутствует, или запрашивает ключ, затем сохраняет учетные данные в профилях аутентификации.

Устанавливает `agents.defaults.model` в `openai/gpt-5.5`, когда модель не задана, имеет вид `openai/*` или является устаревшей ссылкой на модель Codex.

xAI (Grok) OAuth

Вход через браузер для подходящих аккаунтов SuperGrok или X Premium. Это рекомендуемый путь xAI для большинства пользователей. OpenClaw сохраняет полученный профиль аутентификации для моделей Grok, Grok `web_search`, `x_search` и `code_execution`.

Код устройства xAI (Grok)

Удобный для удаленной работы вход через браузер с коротким кодом вместо localhost callback. Используйте это из SSH, Docker или VPS-хостов.

API-ключ xAI (Grok)

Запрашивает `XAI_API_KEY` и настраивает xAI как провайдера моделей. Используйте это, когда нужен API-ключ xAI Console вместо OAuth по подписке.

OpenCode

Запрашивает `OPENCODE_API_KEY` (или `OPENCODE_ZEN_API_KEY`) и позволяет выбрать каталог Zen или Go. URL настройки: [opencode.ai/auth](<https://opencode.ai/auth>).

API-ключ (общий)

Сохраняет ключ для вас.

Vercel AI Gateway

Запрашивает `AI_GATEWAY_API_KEY`. Подробнее: [Vercel AI Gateway](</ru/providers/vercel-ai-gateway>).

Cloudflare AI Gateway

Запрашивает ID аккаунта, ID gateway и `CLOUDFLARE_AI_GATEWAY_API_KEY`. Подробнее: [Cloudflare AI Gateway](</ru/providers/cloudflare-ai-gateway>).

MiniMax

Конфигурация записывается автоматически. Размещенное значение по умолчанию — `MiniMax-M3`; настройка по API-ключу использует `minimax/...`, а настройка OAuth использует `minimax-portal/...`. Подробнее: [MiniMax](</ru/providers/minimax>).

StepFun

Конфигурация записывается автоматически для стандартного StepFun или Step Plan на китайских или глобальных endpoint. Standard сейчас включает `step-3.5-flash`, а Step Plan также включает `step-3.5-flash-2603`. Подробнее: [StepFun](</ru/providers/stepfun>).

Synthetic (совместимый с Anthropic)

Запрашивает `SYNTHETIC_API_KEY`. Подробнее: [Synthetic](</ru/providers/synthetic>).

Ollama (облачные и локальные открытые модели)

Сначала запрашивает `Cloud + Local`, `Cloud only` или `Local only`. `Cloud only` использует `OLLAMA_API_KEY` с `https://ollama.com`. Режимы с хостом запрашивают базовый URL (по умолчанию `http://127.0.0.1:11434`), обнаруживают доступные модели и предлагают значения по умолчанию. `Cloud + Local` также проверяет, выполнен ли вход на этом хосте Ollama для облачного доступа. Подробнее: [Ollama](</ru/providers/ollama>).

Moonshot и Kimi Coding

Конфигурации Moonshot (Kimi K2) и Kimi Coding записываются автоматически. Подробнее: [Moonshot AI (Kimi + Kimi Coding)](</ru/providers/moonshot>).

Пользовательский провайдер

Работает с endpoint, совместимыми с OpenAI и Anthropic.

Интерактивный онбординг поддерживает те же варианты хранения API-ключа, что и другие потоки API-ключей провайдеров:

  * **Вставить API-ключ сейчас** (открытый текст)
  * **Использовать ссылку на секрет** (ссылка env или настроенная ссылка провайдера, с предварительной валидацией)


Неинтерактивные флаги:

  * `--auth-choice custom-api-key`
  * `--custom-base-url`
  * `--custom-model-id`
  * `--custom-api-key` (необязательно; откатывается к `CUSTOM_API_KEY`)
  * `--custom-provider-id` (необязательно)
  * `--custom-compatibility <openai|openai-responses|anthropic>` (необязательно; по умолчанию `openai`)
  * `--custom-image-input` / `--custom-text-input` (необязательно; переопределяет выведенную возможность ввода модели)

Пропустить

Оставляет аутентификацию ненастроенной.

Поведение модели:

  * Выберите модель по умолчанию из обнаруженных вариантов или введите провайдера и модель вручную.
  * Онбординг пользовательского провайдера выводит поддержку изображений для распространенных ID моделей и спрашивает только тогда, когда имя модели неизвестно.
  * Когда онбординг начинается с выбора аутентификации провайдера, средство выбора модели автоматически предпочитает этого провайдера. Для Volcengine и BytePlus то же предпочтение также соответствует их вариантам coding-plan (`volcengine-plan/*`, `byteplus-plan/*`).
  * Если этот фильтр предпочитаемого провайдера оказался бы пустым, средство выбора откатывается к полному каталогу вместо показа отсутствия моделей.
  * Мастер выполняет проверку модели и предупреждает, если настроенная модель неизвестна или для нее отсутствует аутентификация.


Пути учетных данных и профилей:

  * Профили аутентификации (API-ключи + OAuth): `~/.openclaw/agents/<agentId>/agent/auth-profiles.json`
  * Импорт устаревшего OAuth: `~/.openclaw/credentials/oauth.json`


Режим хранения учетных данных:

  * Поведение onboarding по умолчанию сохраняет ключи API как plaintext-значения в auth profiles.
  * `--secret-input-mode ref` включает режим ссылок вместо хранения plaintext-ключей. В интерактивной настройке можно выбрать один из вариантов: 
    * ссылка на переменную окружения (например, `keyRef: { source: "env", provider: "default", id: "OPENAI_API_KEY" }`)
    * ссылка на настроенный provider (`file` или `exec`) с alias provider + id
  * Интерактивный режим ссылок выполняет быструю предварительную проверку перед сохранением. 
    * Ссылки env: проверяет имя переменной + непустое значение в текущем окружении onboarding.
    * Ссылки provider: проверяет конфигурацию provider и разрешает запрошенный id.
    * Если предварительная проверка не проходит, onboarding показывает ошибку и позволяет повторить попытку.
  * В неинтерактивном режиме `--secret-input-mode ref` поддерживается только через env. 
    * Задайте env var provider в окружении процесса onboarding.
    * Inline-флаги ключей (например, `--openai-api-key`) требуют, чтобы эта env var была задана; иначе onboarding быстро завершается с ошибкой.
    * Для пользовательских providers неинтерактивный режим `ref` сохраняет `models.providers.<id>.apiKey` как `{ source: "env", provider: "default", id: "CUSTOM_API_KEY" }`.
    * В таком случае пользовательского provider `--custom-api-key` требует, чтобы `CUSTOM_API_KEY` была задана; иначе onboarding быстро завершается с ошибкой.
  * Учетные данные auth для Gateway поддерживают выбор plaintext и SecretRef в интерактивной настройке: 
    * Режим токена: **Сгенерировать/сохранить plaintext-токен** (по умолчанию) или **Использовать SecretRef**.
    * Режим пароля: plaintext или SecretRef.
  * Неинтерактивный путь SecretRef для токена: `--gateway-token-ref-env &lt;ENV_VAR&gt;`.
  * Существующие настройки plaintext продолжают работать без изменений.


## Выводы и внутреннее устройство

Типичные поля в `~/.openclaw/openclaw.json`:

  * `agents.defaults.workspace`
  * `agents.defaults.skipBootstrap`, когда передан `--skip-bootstrap`
  * `agents.defaults.model` / `models.providers` (если выбран Minimax)
  * `tools.profile` (локальный onboarding по умолчанию использует `"coding"`, если значение не задано; существующие явно заданные значения сохраняются)
  * `gateway.*` (режим, привязка, auth, tailscale)
  * `session.dmScope` (локальный onboarding по умолчанию задает `per-channel-peer`, если значение не задано; существующие явно заданные значения сохраняются)
  * `channels.telegram.botToken`, `channels.discord.token`, `channels.matrix.*`, `channels.signal.*`, `channels.imessage.*`
  * Списки разрешенных каналов (Slack, Discord, Matrix, Microsoft Teams), когда вы соглашаетесь во время подсказок (имена по возможности разрешаются в ID)
  * `skills.install.nodeManager`
    * Флаг `setup --node-manager` принимает `npm`, `pnpm` или `bun`.
    * Ручная конфигурация все еще может позже задать `skills.install.nodeManager: "yarn"`.
  * `wizard.lastRunAt`
  * `wizard.lastRunVersion`
  * `wizard.lastRunCommit`
  * `wizard.lastRunCommand`
  * `wizard.lastRunMode`


`openclaw agents add` записывает `agents.list[]` и необязательные `bindings`.

Учетные данные WhatsApp помещаются в `~/.openclaw/credentials/whatsapp/<accountId>/`. Сессии хранятся в `~/.openclaw/agents/<agentId>/sessions/`.

RPC мастера Gateway:

  * `wizard.start`
  * `wizard.next`
  * `wizard.cancel`
  * `wizard.status`


Клиенты (приложение macOS и Control UI) могут отображать шаги без повторной реализации логики onboarding.

Поведение настройки Signal:

  * Загружает соответствующий asset релиза
  * Сохраняет его в `~/.openclaw/tools/signal-cli/<version>/`
  * Записывает `channels.signal.cliPath` в конфигурацию
  * JVM-сборки требуют Java 21
  * Native-сборки используются, когда доступны
  * Windows использует WSL2 и следует Linux-процессу signal-cli внутри WSL


## Связанные документы

  * Центр onboarding: [Onboarding (CLI)](</ru/start/wizard>)
  * Автоматизация и скрипты: [Автоматизация CLI](</ru/start/wizard-cli-automation>)
  * Справочник команд: [`openclaw onboard`](</ru/cli/onboard>)


Was this useful?YesNo

Open issue