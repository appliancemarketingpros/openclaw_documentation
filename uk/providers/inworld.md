---
title: Inworld
source_url: https://docs.openclaw.ai/uk/providers/inworld
scraped_at: 2026-05-25
---

Inworld — це провайдер потокового перетворення тексту на мовлення (TTS). В OpenClaw він синтезує аудіо вихідних відповідей (MP3 за замовчуванням, OGG_OPUS для голосових нотаток) і PCM-аудіо для телефонних каналів, таких як Голосовий виклик.

OpenClaw надсилає запити до потокової кінцевої точки TTS Inworld, об’єднує повернуті фрагменти аудіо base64 в один буфер і передає результат до стандартного конвеєра аудіо відповідей.

Властивість | Значення  
---|---  
Ідентифікатор провайдера | `inworld`  
Plugin | вбудований, `enabledByDefault: true`  
Контракт | `speechProviders` (лише TTS)  
Змінна середовища автентифікації | `INWORLD_API_KEY` (HTTP Basic, облікові дані панелі у Base64)  
Базова URL-адреса | `https://api.inworld.ai`  
Голос за замовчуванням | `Sarah`  
Модель за замовчуванням | `inworld-tts-1.5-max`  
Вивід | MP3 (за замовчуванням), OGG_OPUS (голосові нотатки), PCM 22050 Гц (телефонія)  
Вебсайт | [inworld.ai](<https://inworld.ai>)  
Документація | [docs.inworld.ai/tts/tts](<https://docs.inworld.ai/tts/tts>)  
  
## Початок роботи

* ### Налаштуйте свій API-ключ

Скопіюйте облікові дані з панелі Inworld (Workspace > API Keys) і задайте їх як змінну середовища. Значення надсилається дослівно як облікові дані HTTP Basic, тому не кодуйте його в Base64 повторно і не перетворюйте на bearer-токен.

CodeCopy code
[code]
    INWORLD_API_KEY=<base64-credential-from-dashboard>
[/code]

* ### Виберіть Inworld у messages.tts

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "inworld",      providers: {        inworld: {          voiceId: "Sarah",          modelId: "inworld-tts-1.5-max",        },      },    },  },}
[/code]

* ### Надішліть повідомлення

Надішліть відповідь через будь-який підключений канал. OpenClaw синтезує аудіо за допомогою Inworld і доставляє його як MP3 (або OGG_OPUS, коли канал очікує голосову нотатку).

## Параметри конфігурації

Параметр | Шлях | Опис  
---|---|---  
`apiKey` | `messages.tts.providers.inworld.apiKey` | Облікові дані панелі у Base64. Резервно використовує `INWORLD_API_KEY`.  
`baseUrl` | `messages.tts.providers.inworld.baseUrl` | Перевизначає базову URL-адресу API Inworld (за замовчуванням `https://api.inworld.ai`).  
`voiceId` | `messages.tts.providers.inworld.voiceId` | Ідентифікатор голосу (за замовчуванням `Sarah`).  
`modelId` | `messages.tts.providers.inworld.modelId` | Ідентифікатор моделі TTS (за замовчуванням `inworld-tts-1.5-max`).  
`temperature` | `messages.tts.providers.inworld.temperature` | Температура вибірки `0..2` (необов’язково).  
  
## Примітки

Автентифікація

Inworld використовує автентифікацію HTTP Basic з одним рядком облікових даних, закодованим у Base64. Скопіюйте його дослівно з панелі Inworld. Провайдер надсилає його як `Authorization: Basic <apiKey>` без додаткового кодування, тому не кодуйте його в Base64 самостійно і не передавайте токен у bearer-стилі. Див. [примітки щодо автентифікації TTS](</uk/tools/tts#inworld-primary>) з таким самим застереженням.

Моделі

Підтримувані ідентифікатори моделей: `inworld-tts-1.5-max` (за замовчуванням), `inworld-tts-1.5-mini`, `inworld-tts-1-max`, `inworld-tts-1`.

Аудіовиходи

Відповіді за замовчуванням використовують MP3. Коли ціль каналу — `voice-note`, OpenClaw просить Inworld надати `OGG_OPUS`, щоб аудіо відтворювалося як нативна голосова бульбашка. Телефонний синтез використовує сирий `PCM` із частотою 22050 Гц для передавання в телефонний міст.

Користувацькі кінцеві точки

Перевизначте хост API за допомогою `messages.tts.providers.inworld.baseUrl`. Завершальні скісні риски вилучаються перед надсиланням запитів.

## Пов’язане

[**Перетворення тексту на мовлення** Огляд TTS, провайдери та конфігурація `messages.tts`. ](</uk/tools/tts>) [**Конфігурація** Повна довідка з конфігурації, включно з налаштуваннями `messages.tts`. ](</uk/gateway/configuration>) [**Провайдери** Усі вбудовані провайдери OpenClaw. ](</uk/providers>) [**Усунення несправностей** Поширені проблеми та кроки налагодження. ](</uk/help/troubleshooting>)

Was this useful?YesNo