---
title: Volcengine (Doubao)
source_url: https://docs.openclaw.ai/uk/providers/volcengine
scraped_at: 2026-05-25
---

Постачальник Volcengine надає доступ до моделей Doubao і сторонніх моделей, розміщених на Volcano Engine, з окремими кінцевими точками для загальних і пов’язаних із кодуванням навантажень. Той самий вбудований Plugin також може зареєструвати Volcengine Speech як постачальника TTS.

Деталь | Значення  
---|---  
Постачальники | `volcengine` (загальний + TTS) + `volcengine-plan` (кодування)  
Автентифікація моделі | `VOLCANO_ENGINE_API_KEY`  
Автентифікація TTS | `VOLCENGINE_TTS_API_KEY` or `BYTEPLUS_SEED_SPEECH_API_KEY`  
API | OpenAI-сумісні моделі, BytePlus Seed Speech TTS  
  
## Початок роботи

* ### Установіть ключ API

Запустіть інтерактивне онбординг-налаштування:

bashCopy code
[code]
    openclaw onboard --auth-choice volcengine-api-key
[/code]

Це реєструє як загального (`volcengine`), так і постачальника для кодування (`volcengine-plan`) за одним ключем API.

* ### Установіть модель за замовчуванням

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "volcengine-plan/ark-code-latest" },    },  },}
[/code]

* ### Переконайтеся, що модель доступна

bashCopy code
[code]
    openclaw models list --provider volcengineopenclaw models list --provider volcengine-plan
[/code]

## Постачальники та кінцеві точки

Постачальник | Кінцева точка | Випадок використання  
---|---|---  
`volcengine` | `ark.cn-beijing.volces.com/api/v3` | Загальні моделі  
`volcengine-plan` | `ark.cn-beijing.volces.com/api/coding/v3` | Моделі для кодування  
  
## Вбудований каталог

### Загальні (volcengine)

Model ref | Назва | Вхід | Контекст  
---|---|---|---  
`volcengine/doubao-seed-1-8-251228` | Doubao Seed 1.8 | text, image | 256,000  
`volcengine/doubao-seed-code-preview-251028` | doubao-seed-code-preview-251028 | text, image | 256,000  
`volcengine/kimi-k2-5-260127` | Kimi K2.5 | text, image | 256,000  
`volcengine/glm-4-7-251222` | GLM 4.7 | text, image | 200,000  
`volcengine/deepseek-v3-2-251201` | DeepSeek V3.2 | text, image | 128,000  
  
### Кодування (volcengine-plan)

Model ref | Назва | Вхід | Контекст  
---|---|---|---  
`volcengine-plan/ark-code-latest` | Ark Coding Plan | text | 256,000  
`volcengine-plan/doubao-seed-code` | Doubao Seed Code | text | 256,000  
`volcengine-plan/glm-4.7` | GLM 4.7 Coding | text | 200,000  
`volcengine-plan/kimi-k2-thinking` | Kimi K2 Thinking | text | 256,000  
`volcengine-plan/kimi-k2.5` | Kimi K2.5 Coding | text | 256,000  
`volcengine-plan/doubao-seed-code-preview-251028` | Doubao Seed Code Preview | text | 256,000  
  
## Перетворення тексту на мовлення

Volcengine TTS використовує HTTP API BytePlus Seed Speech і налаштовується окремо від OpenAI-сумісного ключа API моделі Doubao. У консолі BytePlus відкрийте Seed Speech > Settings > API Keys і скопіюйте ключ API, а потім задайте:

bashCopy code
[code]
    export VOLCENGINE_TTS_API_KEY="byteplus_seed_speech_api_key"export VOLCENGINE_TTS_RESOURCE_ID="seed-tts-1.0"
[/code]

Потім увімкніть його в `openclaw.json`:

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "volcengine",      providers: {        volcengine: {          apiKey: "byteplus_seed_speech_api_key",          voice: "en_female_anna_mars_bigtts",          speedRatio: 1.0,        },      },    },  },}
[/code]

Для цілей голосових нотаток OpenClaw запитує у Volcengine рідний для постачальника формат `ogg_opus`. Для звичайних аудіовкладень він запитує `mp3`. Псевдоніми постачальника `bytedance` і `doubao` також вказують на того самого постачальника мовлення.

Ресурсний ідентифікатор за замовчуванням — `seed-tts-1.0`, тому що саме його BytePlus надає новоствореним ключам API Seed Speech у проєкті за замовчуванням. Якщо ваш проєкт має entitlement на TTS 2.0, установіть `VOLCENGINE_TTS_RESOURCE_ID=seed-tts-2.0`.

Застаріла автентифікація AppID/токеном і далі підтримується для старих застосунків Speech Console:

bashCopy code
[code]
    export VOLCENGINE_TTS_APPID="speech_app_id"export VOLCENGINE_TTS_TOKEN="speech_access_token"export VOLCENGINE_TTS_CLUSTER="volcano_tts"
[/code]

## Розширене налаштування

Модель за замовчуванням після онбординг-налаштування

`openclaw onboard --auth-choice volcengine-api-key` наразі встановлює `volcengine-plan/ark-code-latest` як модель за замовчуванням, одночасно реєструючи загальний каталог `volcengine`.

Поведінка резервного варіанта для вибору моделі

Під час онбординг-налаштування/налаштування вибору моделі варіант автентифікації Volcengine надає перевагу рядкам `volcengine/*` і `volcengine-plan/*`. Якщо ці моделі ще не завантажені, OpenClaw повертається до нефільтрованого каталогу замість показу порожнього засобу вибору в межах постачальника.

Змінні середовища для процесів демона

Якщо Gateway працює як демон (launchd/systemd), переконайтеся, що змінні середовища для моделі й TTS, такі як `VOLCANO_ENGINE_API_KEY`, `VOLCENGINE_TTS_API_KEY`, `BYTEPLUS_SEED_SPEECH_API_KEY`, `VOLCENGINE_TTS_APPID` і `VOLCENGINE_TTS_TOKEN`, доступні цьому процесу (наприклад, у `~/.openclaw/.env` або через `env.shellEnv`).

## Пов’язане

[**Вибір моделі** Вибір постачальників, посилань на моделі та поведінки резервного перемикання. ](</uk/concepts/model-providers>) [**Конфігурація** Повний довідник із конфігурації для агентів, моделей і постачальників. ](</uk/gateway/configuration>) [**Усунення несправностей** Поширені проблеми та кроки налагодження. ](</uk/help/troubleshooting>) [**FAQ** Поширені запитання щодо налаштування OpenClaw. ](</uk/help/faq>)

Was this useful?YesNo