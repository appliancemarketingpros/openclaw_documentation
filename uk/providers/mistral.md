---
title: Mistral
source_url: https://docs.openclaw.ai/uk/providers/mistral
scraped_at: 2026-05-25
---

OpenClaw містить вбудований плагін Mistral, який реєструє чотири контракти: chat completions, розуміння медіа (пакетна транскрипція Voxtral), realtime STT для Voice Call (Voxtral Realtime) і вбудовування пам’яті (`mistral-embed`).

Властивість | Значення  
---|---  
ID провайдера | `mistral`  
Plugin | вбудований, `enabledByDefault: true`  
Змінна env для auth | `MISTRAL_API_KEY`  
Прапорець onboarding | `--auth-choice mistral-api-key`  
Прямий прапорець CLI | `--mistral-api-key <key>`  
API | сумісний з OpenAI (`openai-completions`)  
Базовий URL | `https://api.mistral.ai/v1`  
Модель за замовчуванням | `mistral/mistral-large-latest`  
Модель embedding | `mistral-embed`  
Пакетний Voxtral | `voxtral-mini-latest` (транскрипція аудіо)  
Voxtral realtime | `voxtral-mini-transcribe-realtime-2602`  
  
## Початок роботи

* ### Отримайте свій API-ключ

Створіть API-ключ у [Mistral Console](<https://console.mistral.ai/>).

* ### Запустіть onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice mistral-api-key
[/code]

Або передайте ключ напряму:

bashCopy code
[code]
    openclaw onboard --mistral-api-key "$MISTRAL_API_KEY"
[/code]

* ### Встановіть модель за замовчуванням

json5Copy code
[code]
    {  env: { MISTRAL_API_KEY: "sk-..." },  agents: { defaults: { model: { primary: "mistral/mistral-large-latest" } } },}
[/code]

* ### Перевірте, що модель доступна

bashCopy code
[code]
    openclaw models list --provider mistral
[/code]

## Вбудований каталог LLM

[Mistral Medium 3.5](<https://docs.mistral.ai/models/model-cards/mistral-medium-3-5-26-04>) є поточною змішаною моделлю Medium у вбудованому каталозі: 128B щільних ваг, текстовий і графічний ввід, контекст 256K, виклики функцій, структурований вивід, програмування та настроюване reasoning через Chat Completions API. Використовуйте `mistral/mistral-medium-3-5`, коли потрібна новіша уніфікована agentic/coding-модель Mistral замість стандартної `mistral/mistral-large-latest`.

OpenClaw наразі постачає цей вбудований каталог Mistral:

Посилання на модель | Ввід | Контекст | Макс. вивід | Примітки  
---|---|---|---|---  
`mistral/mistral-large-latest` | текст, зображення | 262,144 | 16,384 | Модель за замовчуванням  
`mistral/mistral-medium-2508` | текст, зображення | 262,144 | 8,192 | Mistral Medium 3.1  
`mistral/mistral-medium-3-5` | текст, зображення | 262,144 | 8,192 | Mistral Medium 3.5; настроюване reasoning  
`mistral/mistral-small-latest` | текст, зображення | 128,000 | 16,384 | Mistral Small 4; настроюване reasoning через API `reasoning_effort`  
`mistral/pixtral-large-latest` | текст, зображення | 128,000 | 32,768 | Pixtral  
`mistral/codestral-latest` | текст | 256,000 | 4,096 | Програмування  
`mistral/devstral-medium-latest` | текст | 262,144 | 32,768 | Devstral 2  
`mistral/magistral-small` | текст | 128,000 | 40,000 | З увімкненим reasoning  
  
Після onboarding виконайте smoke-test Medium 3.5 без запуску Gateway:

bashCopy code
[code]
    openclaw infer model run --local \  --model mistral/mistral-medium-3-5 \  --prompt "Reply with exactly: mistral-ok" \  --json
[/code]

Щоб переглянути рядок вбудованого каталогу перед зміною конфігурації:

bashCopy code
[code]
    openclaw models list --all --provider mistral --plain
[/code]

## Транскрипція аудіо (Voxtral)

Використовуйте Voxtral для пакетної транскрипції аудіо через pipeline розуміння медіа.

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "mistral", model: "voxtral-mini-latest" }],      },    },  },}
[/code]

## Потоковий STT для Voice Call

Вбудований плагін `mistral` реєструє Voxtral Realtime як провайдера потокового STT для Voice Call.

Налаштування | Шлях конфігурації | За замовчуванням  
---|---|---  
API-ключ | `plugins.entries.voice-call.config.streaming.providers.mistral.apiKey` | Повертається до `MISTRAL_API_KEY`  
Модель | `...mistral.model` | `voxtral-mini-transcribe-realtime-2602`  
Кодування | `...mistral.encoding` | `pcm_mulaw`  
Частота дискретизації | `...mistral.sampleRate` | `8000`  
Цільова затримка | `...mistral.targetStreamingDelayMs` | `800`  
json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        config: {          streaming: {            enabled: true,            provider: "mistral",            providers: {              mistral: {                apiKey: "${MISTRAL_API_KEY}",                targetStreamingDelayMs: 800,              },            },          },        },      },    },  },}
[/code]

## Розширена конфігурація

Настроюване reasoning

`mistral/mistral-small-latest` (Mistral Small 4) і `mistral/mistral-medium-3-5` підтримують [настроюване reasoning](<https://docs.mistral.ai/studio-api/conversations/reasoning/adjustable>) у Chat Completions API через `reasoning_effort` (`none` мінімізує додаткове мислення у виводі; `high` показує повні трасування мислення перед фінальною відповіддю). Mistral рекомендує `reasoning_effort="high"` для agentic і code-сценаріїв Medium 3.5.

OpenClaw зіставляє рівень **thinking** сесії з API Mistral:

Рівень thinking в OpenClaw | Mistral `reasoning_effort`  
---|---  
**off** / **minimal** | `none`  
**low** / **medium** / **high** / **xhigh** / **adaptive** / **max** | `high`  
  
Приклад конфігурації, scoped до моделі, для reasoning Medium 3.5:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "mistral/mistral-medium-3-5" },      models: {        "mistral/mistral-medium-3-5": {          params: { thinking: "high" },        },      },    },  },}
[/code]

Вбудовування пам’яті

Mistral може обслуговувати вбудовування пам’яті через `/v1/embeddings` (модель за замовчуванням: `mistral-embed`).

json5Copy code
[code]
    {  memorySearch: { provider: "mistral" },}
[/code]

Auth і базовий URL

  * Auth Mistral використовує `MISTRAL_API_KEY` (заголовок Bearer).
  * Базовий URL провайдера за замовчуванням — `https://api.mistral.ai/v1`, він приймає стандартну форму запиту chat-completions, сумісну з OpenAI.
  * Модель onboarding за замовчуванням — `mistral/mistral-large-latest`.
  * Перевизначайте базовий URL у `models.providers.mistral.baseUrl` лише тоді, коли Mistral явно публікує потрібний вам регіональний endpoint.


## Пов’язане

[**Вибір моделі** Вибір провайдерів, посилань на моделі та поведінки failover. ](</uk/concepts/model-providers>) [**Розуміння медіа** Налаштування транскрипції аудіо та вибір провайдера. ](</uk/nodes/media-understanding>)

Was this useful?YesNo