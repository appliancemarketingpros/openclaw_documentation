---
title: Vydra
source_url: https://docs.openclaw.ai/uk/providers/vydra
scraped_at: 2026-05-25
---

Комплектний Vydra Plugin додає:

  * Генерацію зображень через `vydra/grok-imagine`
  * Генерацію відео через `vydra/veo3` і `vydra/kling`
  * Синтез мовлення через TTS-маршрут Vydra на базі ElevenLabs


OpenClaw використовує той самий `VYDRA_API_KEY` для всіх трьох можливостей.

Властивість | Значення  
---|---  
Ідентифікатор провайдера | `vydra`  
Plugin | комплектний, `enabledByDefault: true`  
Змінна env для автентифікації | `VYDRA_API_KEY`  
Прапорець онбордингу | `--auth-choice vydra-api-key`  
Прямий прапорець CLI | `--vydra-api-key <key>`  
Контракти | `imageGenerationProviders`, `videoGenerationProviders`, `speechProviders`  
Базова URL-адреса | `https://www.vydra.ai/api/v1` (використовуйте хост `www`)  
  
## Налаштування

* ### Запустіть інтерактивний онбординг

bashCopy code
[code]
    openclaw onboard --auth-choice vydra-api-key
[/code]

Або задайте змінну env напряму:

bashCopy code
[code]
    export VYDRA_API_KEY="vydra_live_..."
[/code]

* ### Виберіть можливість за замовчуванням

Виберіть одну або кілька можливостей нижче (зображення, відео або мовлення) і застосуйте відповідну конфігурацію.

## Можливості

Генерація зображень

Модель зображень за замовчуванням:

  * `vydra/grok-imagine`


Задайте її як провайдера зображень за замовчуванням:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "vydra/grok-imagine",      },    },  },}
[/code]

Поточна комплектна підтримка охоплює лише перетворення тексту на зображення. Розміщені у Vydra маршрути редагування очікують віддалені URL-адреси зображень, а OpenClaw поки не додає специфічний для Vydra міст завантаження в комплектному Plugin.

Генерація відео

Зареєстровані відеомоделі:

  * `vydra/veo3` для перетворення тексту на відео
  * `vydra/kling` для перетворення зображення на відео


Задайте Vydra як провайдера відео за замовчуванням:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "vydra/veo3",      },    },  },}
[/code]

Примітки:

  * `vydra/veo3` комплектується лише для перетворення тексту на відео.
  * `vydra/kling` наразі потребує посилання на віддалену URL-адресу зображення. Завантаження локальних файлів відхиляються одразу.
  * Поточний HTTP-маршрут `kling` у Vydra був непослідовним щодо того, чи потребує він `image_url`, чи `video_url`; комплектний провайдер відображає ту саму віддалену URL-адресу зображення в обидва поля.
  * Комплектний Plugin залишається консервативним і не передає недокументовані параметри стилю, як-от співвідношення сторін, роздільну здатність, водяний знак або згенероване аудіо.

Live-тести відео

Специфічне для провайдера live-покриття:

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 \OPENCLAW_LIVE_VYDRA_VIDEO=1 \pnpm test:live -- extensions/vydra/vydra.live.test.ts
[/code]

Комплектний live-файл Vydra тепер охоплює:

  * перетворення тексту на відео `vydra/veo3`
  * перетворення зображення на відео `vydra/kling` з використанням віддаленої URL-адреси зображення


За потреби перевизначте віддалену фікстуру зображення:

bashCopy code
[code]
    export OPENCLAW_LIVE_VYDRA_KLING_IMAGE_URL="https://example.com/reference.png"
[/code]

Синтез мовлення

Задайте Vydra як провайдера мовлення:

json5Copy code
[code]
    {  messages: {    tts: {      provider: "vydra",      providers: {        vydra: {          apiKey: "${VYDRA_API_KEY}",          voiceId: "21m00Tcm4TlvDq8ikWAM",        },      },    },  },}
[/code]

Значення за замовчуванням:

  * Модель: `elevenlabs/tts`
  * Ідентифікатор голосу: `21m00Tcm4TlvDq8ikWAM`


Комплектний Plugin наразі надає один перевірений голос за замовчуванням і повертає аудіофайли MP3.

## Пов’язане

[**Каталог провайдерів** Перегляньте всі доступні провайдери. ](</uk/providers>) [**Генерація зображень** Спільні параметри інструмента для зображень і вибір провайдера. ](</uk/tools/image-generation>) [**Генерація відео** Спільні параметри інструмента для відео і вибір провайдера. ](</uk/tools/video-generation>) [**Довідник конфігурації** Значення агентів за замовчуванням і конфігурація моделей. ](</uk/gateway/config-agents#agent-defaults>)

Was this useful?YesNo