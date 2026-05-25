---
title: Xiaomi MiMo
source_url: https://docs.openclaw.ai/uk/providers/xiaomi
scraped_at: 2026-05-25
---

Xiaomi MiMo — це API-платформа для моделей **MiMo**. OpenClaw містить вбудований Plugin `xiaomi`, який реєструє як OpenAI-сумісного постачальника чату, так і постачальника мовлення (TTS) для того самого `XIAOMI_API_KEY`.

Властивість | Значення  
---|---  
ID постачальника | `xiaomi`  
Plugin | вбудований, `enabledByDefault: true`  
Змінна env для auth | `XIAOMI_API_KEY`  
Прапорець onboarding | `--auth-choice xiaomi-api-key`  
Прямий прапорець CLI | `--xiaomi-api-key <key>`  
Контракти | завершення чату + `speechProviders`  
API | OpenAI-сумісний (`openai-completions`)  
Базова URL-адреса | `https://api.xiaomimimo.com/v1`  
Модель за замовчуванням | `xiaomi/mimo-v2-flash`  
TTS за замовчуванням | `mimo-v2.5-tts`, голос `mimo_default`  
  
## Початок роботи

* ### Отримайте API-ключ

Створіть API-ключ у [консолі Xiaomi MiMo](<https://platform.xiaomimimo.com/#/console/api-keys>).

* ### Запустіть onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice xiaomi-api-key
[/code]

Або передайте ключ напряму:

bashCopy code
[code]
    openclaw onboard --auth-choice xiaomi-api-key --xiaomi-api-key "$XIAOMI_API_KEY"
[/code]

* ### Перевірте, що модель доступна

bashCopy code
[code]
    openclaw models list --provider xiaomi
[/code]

## Вбудований каталог

Посилання на модель | Вхідні дані | Контекст | Макс. вихід | Міркування | Примітки  
---|---|---|---|---|---  
`xiaomi/mimo-v2-flash` | текст | 262,144 | 8,192 | Ні | Модель за замовчуванням  
`xiaomi/mimo-v2-pro` | текст | 1,048,576 | 32,000 | Так | Великий контекст  
`xiaomi/mimo-v2-omni` | текст, зображення | 262,144 | 32,000 | Так | Мультимодальна  
  
## Перетворення тексту на мовлення

Вбудований Plugin `xiaomi` також реєструє Xiaomi MiMo як постачальника мовлення для `messages.tts`. Він викликає TTS-контракт Xiaomi для завершень чату з текстом як повідомленням `assistant` і необов’язковими вказівками стилю як повідомленням `user`.

Властивість | Значення  
---|---  
ID TTS | `xiaomi` (псевдонім `mimo`)  
Auth | `XIAOMI_API_KEY`  
API | `POST /v1/chat/completions` з `audio`  
За замовчуванням | `mimo-v2.5-tts`, голос `mimo_default`  
Вихід | MP3 за замовчуванням; WAV, якщо налаштовано  
json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "xiaomi",      providers: {        xiaomi: {          apiKey: "xiaomi_api_key",          model: "mimo-v2.5-tts",          voice: "mimo_default",          format: "mp3",          style: "Bright, natural, conversational tone.",        },      },    },  },}
[/code]

Підтримувані вбудовані голоси включають `mimo_default`, `default_zh`, `default_en`, `Mia`, `Chloe`, `Milo` і `Dean`. `mimo-v2-tts` підтримується для старіших облікових записів MiMo TTS; за замовчуванням використовується поточна модель MiMo-V2.5 TTS. Для цільових голосових нотаток, як-от Feishu і Telegram, OpenClaw транскодує вихід Xiaomi у 48 кГц Opus за допомогою `ffmpeg` перед доставленням.

## Приклад конфігурації

json5Copy code
[code]
    {  env: { XIAOMI_API_KEY: "your-key" },  agents: { defaults: { model: { primary: "xiaomi/mimo-v2-flash" } } },  models: {    mode: "merge",    providers: {      xiaomi: {        baseUrl: "https://api.xiaomimimo.com/v1",        api: "openai-completions",        apiKey: "XIAOMI_API_KEY",        models: [          {            id: "mimo-v2-flash",            name: "Xiaomi MiMo V2 Flash",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 8192,          },          {            id: "mimo-v2-pro",            name: "Xiaomi MiMo V2 Pro",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 1048576,            maxTokens: 32000,          },          {            id: "mimo-v2-omni",            name: "Xiaomi MiMo V2 Omni",            reasoning: true,            input: ["text", "image"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 32000,          },        ],      },    },  },}
[/code]

Поведінка автоін’єкції

Постачальник `xiaomi` впроваджується автоматично, коли `XIAOMI_API_KEY` встановлено у вашому середовищі або існує auth-профіль. Вам не потрібно налаштовувати постачальника вручну, якщо ви не хочете перевизначити метадані моделі або базову URL-адресу.

Відомості про моделі

  * **mimo-v2-flash** — легка й швидка, ідеальна для текстових завдань загального призначення. Без підтримки міркування.
  * **mimo-v2-pro** — підтримує міркування з контекстним вікном на 1 млн токенів для робочих навантажень із довгими документами.
  * **mimo-v2-omni** — мультимодальна модель із підтримкою міркування, яка приймає як текстові, так і графічні вхідні дані.

Усунення несправностей

  * Якщо моделі не з’являються, переконайтеся, що `XIAOMI_API_KEY` встановлено й він дійсний.
  * Коли Gateway працює як daemon, переконайтеся, що ключ доступний цьому процесу (наприклад, у `~/.openclaw/.env` або через `env.shellEnv`).


## Пов’язане

[**Вибір моделі** Вибір постачальників, посилань на моделі та поведінки failover. ](</uk/concepts/model-providers>) [**Довідник конфігурації** Повний довідник конфігурації OpenClaw. ](</uk/gateway/configuration-reference>) [**Консоль Xiaomi MiMo** Панель керування Xiaomi MiMo та керування API-ключами. ](<https://platform.xiaomimimo.com>)

Was this useful?YesNo