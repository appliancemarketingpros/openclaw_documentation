---
title: Gradium
source_url: https://docs.openclaw.ai/uk/providers/gradium
scraped_at: 2026-05-25
---

[Gradium](<https://gradium.ai>) — це вбудований постачальник перетворення тексту на мовлення для OpenClaw. Plugin може створювати звичайні аудіовідповіді (WAV), сумісний із голосовими нотатками вивід Opus і 8 кГц u-law аудіо для телефонних поверхонь.

Властивість | Значення  
---|---  
Ідентифікатор постачальника | `gradium`  
Автентифікація | `GRADIUM_API_KEY` або config `apiKey`  
Базова URL-адреса | `https://api.gradium.ai` (за замовчуванням)  
Голос за замовчуванням | `Emma` (`YTpq7expH9539ERJ`)  
  
## Налаштування

Створіть ключ Gradium API, а потім надайте його OpenClaw через змінну середовища або ключ конфігурації.

### Env var

bashCopy code
[code]
    export GRADIUM_API_KEY="gsk_..."
[/code]

### Config key

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "gradium",      providers: {        gradium: {          apiKey: "${GRADIUM_API_KEY}",        },      },    },  },}
[/code]

Plugin спочатку перевіряє вирішений `apiKey` і в разі відсутності використовує змінну середовища `GRADIUM_API_KEY`.

## Конфігурація

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "gradium",      providers: {        gradium: {          voiceId: "YTpq7expH9539ERJ",          // apiKey: "${GRADIUM_API_KEY}",          // baseUrl: "https://api.gradium.ai",        },      },    },  },}
[/code]

Ключ | Тип | Опис  
---|---|---  
`messages.tts.providers.gradium.apiKey` | string | Вирішений ключ API. Підтримує `${ENV}` і посилання на секрети.  
`messages.tts.providers.gradium.baseUrl` | string | Перевизначає джерело API. Кінцеві скісні риски видаляються. За замовчуванням `https://api.gradium.ai`.  
`messages.tts.providers.gradium.voiceId` | string | Ідентифікатор голосу за замовчуванням, який використовується, коли немає перевизначення директивою.  
  
Формат вихідного аудіо автоматично вибирається runtime на основі цільової поверхні й не налаштовується з `openclaw.json`. Див. Вивід нижче.

## Голоси

Назва | Ідентифікатор голосу  
---|---  
Emma | `YTpq7expH9539ERJ`  
Kent | `LFZvm12tW_z0xfGo`  
Tiffany | `Eu9iL_CYe8N-Gkx_`  
Christina | `2H4HY2CBNyJHBCrP`  
Sydney | `jtEKaLYNn6iif5PR`  
John | `KWJiFWu2O9nMPYcR`  
Arthur | `3jUdJyOi9pgbxBTK`  
  
Голос за замовчуванням: Emma.

### Перевизначення голосу для окремого повідомлення

Коли активна політика мовлення дозволяє перевизначення голосу, ви можете перемикати голоси безпосередньо в тексті за допомогою токена директиви. Усі ці варіанти вирішуються в одне й те саме перевизначення `voiceId`:

textCopy code
[code]
    /voice:LFZvm12tW_z0xfGo/voice_id:LFZvm12tW_z0xfGo/voiceid:LFZvm12tW_z0xfGo/gradium_voice:LFZvm12tW_z0xfGo/gradiumvoice:LFZvm12tW_z0xfGo
[/code]

Якщо політика мовлення вимикає перевизначення голосу, директива споживається, але ігнорується.

## Вивід

Runtime вибирає формат виводу з цільової поверхні. Наразі постачальник не синтезує інші формати.

Ціль | Формат | Розширення файлу | Частота дискретизації | Прапорець сумісності з голосом  
---|---|---|---|---  
Стандартне аудіо | `wav` | `.wav` | постачальник | ні  
Голосова нотатка | `opus` | `.opus` | постачальник | так  
Телефонія | `ulaw_8000` | n/a | 8 кГц | n/a  
  
## Порядок автоматичного вибору

Серед налаштованих постачальників TTS порядок автоматичного вибору Gradium дорівнює `30`. Див. [Перетворення тексту на мовлення](</uk/tools/tts>), щоб дізнатися, як OpenClaw вибирає активного постачальника, коли `messages.tts.provider` не закріплено.

## Пов’язане

  * [Перетворення тексту на мовлення](</uk/tools/tts>)
  * [Огляд медіа](</uk/tools/media-overview>)


Was this useful?YesNo