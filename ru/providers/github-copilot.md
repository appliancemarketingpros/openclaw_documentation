---
title: GitHub Copilot
source_url: https://docs.openclaw.ai/ru/providers/github-copilot
scraped_at: 2026-06-29
---

ModelsProviders

GitHub Copilot — это AI-ассистент GitHub для написания кода. Он предоставляет доступ к моделям Copilot для вашей учетной записи и плана GitHub. OpenClaw может использовать Copilot как провайдера моделей или среду выполнения агента тремя разными способами.

## Три способа использовать Copilot в OpenClaw

### Встроенный провайдер (github-copilot)

Используйте встроенный поток входа с устройства, чтобы получить токен GitHub, а затем обменивать его на токены Copilot API при запуске OpenClaw. Это **стандартный** и самый простой путь, потому что для него не требуется VS Code.

* ### Запустите команду входа

bashCopy code
[code]
    openclaw models auth login-github-copilot
[/code]

Вам будет предложено перейти по URL и ввести одноразовый код. Держите терминал открытым до завершения.

* ### Задайте модель по умолчанию

bashCopy code
[code]
    openclaw models set github-copilot/claude-opus-4.7
[/code]

Или в конфигурации:

json5Copy code
[code]
    {  agents: {    defaults: { model: { primary: "github-copilot/claude-opus-4.7" } },  },}
[/code]

### Plugin обвязки Copilot SDK (copilot)

Установите внешний plugin `@openclaw/copilot`, если хотите, чтобы Copilot CLI и SDK от GitHub управляли низкоуровневым циклом агента для выбранных моделей `github-copilot/*`.

bashCopy code
[code]
    openclaw plugins install clawhub:@openclaw/copilot
[/code]

Затем подключите модель или провайдера к среде выполнения:

json5Copy code
[code]
    {  agents: {    defaults: {      model: "github-copilot/gpt-5.5",      models: {        "github-copilot/gpt-5.5": {          agentRuntime: { id: "copilot" },        },      },    },  },}
[/code]

Выбирайте этот вариант, если вам нужны нативные сеансы Copilot CLI, состояние потоков под управлением SDK и Compaction, управляемая Copilot, для этих ходов агента. Полный контракт среды выполнения см. в разделе [обвязка Copilot SDK](</ru/plugins/copilot>).

### Plugin Copilot Proxy (copilot-proxy)

Используйте расширение VS Code **Copilot Proxy** как локальный мост. OpenClaw обращается к конечной точке `/v1` прокси и использует список моделей, который вы там настроите.

## Необязательные флаги

Флаг | Описание  
---|---  
`--yes` | Пропустить запрос подтверждения  
`--set-default` | Также применить рекомендованную провайдером модель по умолчанию  
  
bashCopy code
[code]
    # Skip confirmationopenclaw models auth login-github-copilot --yes # Login and set the default model in one stepopenclaw models auth login --provider github-copilot --method device --set-default
[/code]

## Неинтерактивное начальное подключение

Если у вас уже есть токен доступа GitHub OAuth для Copilot, импортируйте его при headless-настройке с помощью `openclaw onboard --non-interactive`:

bashCopy code
[code]
    openclaw onboard --non-interactive --accept-risk \  --auth-choice github-copilot \  --github-copilot-token "$COPILOT_GITHUB_TOKEN" \  --skip-channels --skip-health
[/code]

Также можно опустить `--auth-choice`; передача `--github-copilot-token` автоматически определяет вариант аутентификации провайдера GitHub Copilot. Если флаг опущен, начальное подключение сначала использует `COPILOT_GITHUB_TOKEN`, затем `GH_TOKEN`, затем `GITHUB_TOKEN`. Используйте `--secret-input-mode ref` с заданной переменной `COPILOT_GITHUB_TOKEN`, чтобы сохранить подкрепленный env `tokenRef` вместо открытого текста в `auth-profiles.json`.

Требуется интерактивный TTY

Поток входа с устройства требует интерактивного TTY. Запускайте его напрямую в терминале, а не в неинтерактивном скрипте или CI-конвейере.

Доступность моделей зависит от вашего плана

Доступность моделей Copilot зависит от вашего плана GitHub. Если модель отклоняется, попробуйте другой ID (например, `github-copilot/gpt-5.5`). Актуальный список моделей см. в разделе GitHub [поддерживаемые модели для каждого плана Copilot](<https://docs.github.com/en/copilot/reference/ai-models/supported-models#supported-ai-models-per-copilot-plan>).

Живое обновление каталога из Copilot API

После того как путь аутентификации через вход с устройства (или env-переменную) получит токен GitHub, OpenClaw по требованию обновляет каталог моделей из `${baseUrl}/models` (той же конечной точки, которую использует VS Code Copilot), чтобы среда выполнения отслеживала права доступа для конкретной учетной записи и точные контекстные окна без изменений манифеста. Новые опубликованные модели Copilot становятся видимыми без обновления OpenClaw, а контекстные окна отражают реальные ограничения каждой модели (например, 400 тыс. для серии gpt-5.x, 1 млн для внутренних вариантов `claude-opus-*-1m`).

Встроенный статический каталог остается видимым резервным вариантом, когда обнаружение отключено, у пользователя нет профиля аутентификации GitHub, обмен токена завершается ошибкой или HTTPS-вызов `/models` завершается ошибкой. Чтобы отказаться от этого и полностью полагаться на статический каталог манифеста (офлайн-сценарии / изолированные среды):

json5Copy code
[code]
    {  plugins: {    entries: {      "github-copilot": {        config: { discovery: { enabled: false } },      },    },  },}
[/code]

Выбор транспорта

ID моделей Claude автоматически используют транспорт Anthropic Messages. Модели GPT, o-series и Gemini продолжают использовать транспорт OpenAI Responses. OpenClaw выбирает правильный транспорт на основе ссылки на модель.

Совместимость запросов

OpenClaw отправляет заголовки запросов в стиле Copilot IDE через транспорты Copilot, включая ходы со встроенной Compaction, результатами инструментов и последующими запросами по изображениям. Он не включает продолжение Responses на уровне провайдера для Copilot, если это поведение не было проверено с API Copilot.

Порядок разрешения переменных окружения

OpenClaw разрешает аутентификацию Copilot из переменных окружения в следующем порядке приоритета:

Приоритет | Переменная | Примечания  
---|---|---  
1 | `COPILOT_GITHUB_TOKEN` | Наивысший приоритет, специфично для Copilot  
2 | `GH_TOKEN` | Токен GitHub CLI (резервный вариант)  
3 | `GITHUB_TOKEN` | Стандартный токен GitHub (самый низкий)  
  
Когда задано несколько переменных, OpenClaw использует переменную с наивысшим приоритетом. Поток входа с устройства (`openclaw models auth login-github-copilot`) сохраняет свой токен в хранилище профилей аутентификации и имеет приоритет над всеми переменными окружения.

Хранение токенов

Вход сохраняет токен GitHub в хранилище профилей аутентификации и обменивает его на токен Copilot API при запуске OpenClaw. Вам не нужно управлять токеном вручную.

## Эмбеддинги для поиска в памяти

GitHub Copilot также может служить провайдером эмбеддингов для [поиска в памяти](</ru/concepts/memory-search>). Если у вас есть подписка Copilot и вы вошли в систему, OpenClaw может использовать его для эмбеддингов без отдельного ключа API.

### Конфигурация

Явно задайте `memorySearch.provider`, чтобы использовать эмбеддинги GitHub Copilot. Если доступен токен GitHub, OpenClaw обнаруживает доступные модели эмбеддингов через Copilot API и автоматически выбирает лучшую.

json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        provider: "github-copilot",        // Optional: override the auto-discovered model        model: "text-embedding-3-small",      },    },  },}
[/code]

### Как это работает

  1. OpenClaw разрешает ваш токен GitHub (из env-переменных или профиля аутентификации).
  2. Обменивает его на краткоживущий токен Copilot API.
  3. Запрашивает конечную точку Copilot `/models`, чтобы обнаружить доступные модели эмбеддингов.
  4. Выбирает лучшую модель (предпочитает `text-embedding-3-small`).
  5. Отправляет запросы эмбеддингов в конечную точку Copilot `/embeddings`.


Доступность моделей зависит от вашего плана GitHub. Если модели эмбеддингов недоступны, OpenClaw пропускает Copilot и пробует следующего провайдера.

## Связанные материалы

[**Выбор модели** Выбор провайдеров, ссылок на модели и поведения при отказе. ](</ru/concepts/model-providers>) [**OAuth и аутентификация** Сведения об аутентификации и правила повторного использования учетных данных. ](</ru/gateway/authentication>)

Was this useful?YesNo

Open issue