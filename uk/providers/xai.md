---
title: xAI
source_url: https://docs.openclaw.ai/uk/providers/xai
scraped_at: 2026-05-25
---

OpenClaw постачається з вбудованим Plugin провайдера `xai` для моделей Grok.

## Початок роботи

* ### Створіть API-ключ

Створіть API-ключ у [консолі xAI](<https://console.x.ai/>).

* ### Налаштуйте свій API-ключ

Налаштуйте `XAI_API_KEY` або виконайте:

bashCopy code
[code]
    openclaw onboard --auth-choice xai-api-key
[/code]

* ### Виберіть модель

json5Copy code
[code]
    {  agents: { defaults: { model: { primary: "xai/grok-4.3" } } },}
[/code]

## Вбудований каталог

OpenClaw одразу містить такі сімейства моделей xAI:

Сімейство | Ідентифікатори моделей  
---|---  
Grok 3 | `grok-3`, `grok-3-fast`, `grok-3-mini`, `grok-3-mini-fast`  
Grok 4.3 | `grok-4.3`  
Grok 4 | `grok-4`, `grok-4-0709`  
Grok 4 Fast | `grok-4-fast`, `grok-4-fast-non-reasoning`  
Grok 4.1 Fast | `grok-4-1-fast`, `grok-4-1-fast-non-reasoning`  
Grok 4.20 Beta | `grok-4.20-beta-latest-reasoning`, `grok-4.20-beta-latest-non-reasoning`  
Grok Code | `grok-code-fast-1`  
  
Plugin також наперед розв’язує новіші ідентифікатори `grok-4*` і `grok-code-fast*`, коли вони мають ту саму форму API.

## Покриття функцій OpenClaw

Вбудований Plugin відображає поточну публічну поверхню API xAI на спільні контракти провайдера та інструментів OpenClaw. Можливості, що не відповідають спільному контракту (наприклад потоковий TTS і голос у реальному часі), не експонуються - див. таблицю нижче.

Можливість xAI | Поверхня OpenClaw | Статус  
---|---|---  
Чат / Responses | провайдер моделей `xai/<model>` | Так  
Серверний вебпошук | провайдер `web_search` `grok` | Так  
Серверний пошук X | інструмент `x_search` | Так  
Серверне виконання коду | інструмент `code_execution` | Так  
Зображення | `image_generate` | Так  
Відео | `video_generate` | Так  
Пакетний text-to-speech | `messages.tts.provider: "xai"` / `tts` | Так  
Потоковий TTS | - | Не експонується; контракт TTS OpenClaw повертає повні аудіобуфери  
Пакетний speech-to-text | `tools.media.audio` / розуміння медіа | Так  
Потоковий speech-to-text | Voice Call `streaming.provider: "xai"` | Так  
Голос у реальному часі | - | Ще не експонується; інший контракт сеансу/WebSocket  
Файли / пакети | Лише сумісність із загальним API моделей | Не є першокласним інструментом OpenClaw  
  
### Відображення швидкого режиму

`/fast on` або `agents.defaults.models["xai/<model>"].params.fastMode: true` переписує нативні запити xAI так:

Початкова модель | Ціль швидкого режиму  
---|---  
`grok-3` | `grok-3-fast`  
`grok-3-mini` | `grok-3-mini-fast`  
`grok-4` | `grok-4-fast`  
`grok-4-0709` | `grok-4-fast`  
  
### Застарілі псевдоніми сумісності

Застарілі псевдоніми й далі нормалізуються до канонічних вбудованих ідентифікаторів:

Застарілий псевдонім | Канонічний ідентифікатор  
---|---  
`grok-4-fast-reasoning` | `grok-4-fast`  
`grok-4-1-fast-reasoning` | `grok-4-1-fast`  
`grok-4.20-reasoning` | `grok-4.20-beta-latest-reasoning`  
`grok-4.20-non-reasoning` | `grok-4.20-beta-latest-non-reasoning`  
  
## Функції

Вебпошук

Вбудований провайдер вебпошуку `grok` може використовувати `XAI_API_KEY` або ключ вебпошуку Plugin:

bashCopy code
[code]
    openclaw config set tools.web.search.provider grok
[/code]

Генерація відео

Вбудований Plugin `xai` реєструє генерацію відео через спільний інструмент `video_generate`.

  * Стандартна модель відео: `xai/grok-imagine-video`
  * Режими: текст-у-відео, зображення-у-відео, генерація за референсним зображенням, віддалене редагування відео та віддалене розширення відео
  * Співвідношення сторін: `1:1`, `16:9`, `9:16`, `4:3`, `3:4`, `3:2`, `2:3`
  * Роздільні здатності: `480P`, `720P`
  * Тривалість: 1-15 секунд для генерації/зображення-у-відео, 1-10 секунд під час використання ролей `reference_image`, 2-10 секунд для розширення
  * Генерація за референсним зображенням: задайте `imageRoles` як `reference_image` для кожного наданого зображення; xAI приймає до 7 таких зображень


Щоб використовувати xAI як стандартного провайдера відео:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "xai/grok-imagine-video",      },    },  },}
[/code]

Генерація зображень

Вбудований Plugin `xai` реєструє генерацію зображень через спільний інструмент `image_generate`.

  * Стандартна модель зображень: `xai/grok-imagine-image`
  * Додаткова модель: `xai/grok-imagine-image-pro`
  * Режими: текст-у-зображення та редагування за референсним зображенням
  * Референсні вхідні дані: одне `image` або до п’яти `images`
  * Співвідношення сторін: `1:1`, `16:9`, `9:16`, `4:3`, `3:4`, `2:3`, `3:2`
  * Роздільні здатності: `1K`, `2K`
  * Кількість: до 4 зображень


OpenClaw запитує в xAI відповіді зображень `b64_json`, щоб згенеровані медіа можна було зберігати й доставляти через звичайний шлях вкладень каналу. Локальні референсні зображення перетворюються на data URL; віддалені референси `http(s)` передаються напряму.

Щоб використовувати xAI як стандартного провайдера зображень:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "xai/grok-imagine-image",      },    },  },}
[/code]

Text-to-speech

Вбудований Plugin `xai` реєструє text-to-speech через спільну поверхню провайдера `tts`.

  * Голоси: `eve`, `ara`, `rex`, `sal`, `leo`, `una`
  * Стандартний голос: `eve`
  * Формати: `mp3`, `wav`, `pcm`, `mulaw`, `alaw`
  * Мова: код BCP-47 або `auto`
  * Швидкість: нативне перевизначення швидкості провайдера
  * Нативний формат голосових нотаток Opus не підтримується


Щоб використовувати xAI як стандартного провайдера TTS:

json5Copy code
[code]
    {  messages: {    tts: {      provider: "xai",      providers: {        xai: {          voiceId: "eve",        },      },    },  },}
[/code]

Speech-to-text

Вбудований Plugin `xai` реєструє пакетний speech-to-text через поверхню транскрипції розуміння медіа OpenClaw.

  * Стандартна модель: `grok-stt`
  * Endpoint: xAI REST `/v1/stt`
  * Шлях введення: завантаження multipart-аудіофайлу
  * Підтримується OpenClaw усюди, де транскрипція вхідного аудіо використовує `tools.media.audio`, включно із сегментами голосових каналів Discord і аудіовкладеннями каналів


Щоб примусово використовувати xAI для транскрипції вхідного аудіо:

json5Copy code
[code]
    {  tools: {    media: {      audio: {        models: [          {            type: "provider",            provider: "xai",            model: "grok-stt",          },        ],      },    },  },}
[/code]

Мову можна надати через спільну конфігурацію аудіомедіа або в запиті транскрипції для окремого виклику. Підказки prompt приймаються спільною поверхнею OpenClaw, але REST-інтеграція STT xAI передає лише файл, модель і мову, бо вони чітко відповідають поточному публічному endpoint xAI.

Потоковий speech-to-text

Вбудований Plugin `xai` також реєструє провайдера транскрипції в реальному часі для живого аудіо голосових викликів.

  * Endpoint: xAI WebSocket `wss://api.x.ai/v1/stt`
  * Стандартне кодування: `mulaw`
  * Стандартна частота дискретизації: `8000`
  * Стандартне визначення кінця мовлення: `800ms`
  * Проміжні транскрипти: увімкнено типово


Медіапотік Twilio у Voice Call надсилає аудіокадри G.711 µ-law, тож провайдер xAI може передавати ці кадри напряму без транскодування:

json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        config: {          streaming: {            enabled: true,            provider: "xai",            providers: {              xai: {                apiKey: "${XAI_API_KEY}",                endpointingMs: 800,                language: "en",              },            },          },        },      },    },  },}
[/code]

Конфігурація, що належить провайдеру, розміщується в `plugins.entries.voice-call.config.streaming.providers.xai`. Підтримувані ключі: `apiKey`, `baseUrl`, `sampleRate`, `encoding` (`pcm`, `mulaw` або `alaw`), `interimResults`, `endpointingMs` і `language`.

x_search configuration

Вбудований Plugin xAI надає `x_search` як інструмент OpenClaw для пошуку вмісту X (раніше Twitter) через Grok.

Шлях конфігурації: `plugins.entries.xai.config.xSearch`

Key | Type | Default | Description  
---|---|---|---  
`enabled` | boolean | - | Увімкнути або вимкнути x_search  
`model` | string | `grok-4-1-fast` | Модель, що використовується для запитів x_search  
`baseUrl` | string | - | Перевизначення базової URL-адреси xAI Responses  
`inlineCitations` | boolean | - | Додавати вбудовані цитати в результати  
`maxTurns` | number | - | Максимальна кількість ходів розмови  
`timeoutSeconds` | number | - | Час очікування запиту в секундах  
`cacheTtlMinutes` | number | - | Час життя кешу в хвилинах  
json5Copy code
[code]
    {  plugins: {    entries: {      xai: {        config: {          xSearch: {            enabled: true,            model: "grok-4-1-fast",            baseUrl: "https://api.x.ai/v1",            inlineCitations: true,          },        },      },    },  },}
[/code]

Code execution configuration

Вбудований Plugin xAI надає `code_execution` як інструмент OpenClaw для віддаленого виконання коду в пісочниці xAI.

Шлях конфігурації: `plugins.entries.xai.config.codeExecution`

Key | Type | Default | Description  
---|---|---|---  
`enabled` | boolean | `true` (якщо ключ доступний) | Увімкнути або вимкнути виконання коду  
`model` | string | `grok-4-1-fast` | Модель, що використовується для запитів виконання коду  
`maxTurns` | number | - | Максимальна кількість ходів розмови  
`timeoutSeconds` | number | - | Час очікування запиту в секундах  
json5Copy code
[code]
    {  plugins: {    entries: {      xai: {        config: {          codeExecution: {            enabled: true,            model: "grok-4-1-fast",          },        },      },    },  },}
[/code]

Known limits

  * Автентифікація сьогодні підтримує лише API-ключ. API-ключ можна зберігати в профілі автентифікації xAI, змінній середовища або конфігурації plugin; OAuth xAI або потоку device-code в OpenClaw поки немає.
  * `grok-4.20-multi-agent-experimental-beta-0304` не підтримується у звичайному шляху провайдера xAI, оскільки потребує іншої поверхні upstream API, ніж стандартний транспорт OpenClaw xAI.
  * Голос xAI Realtime ще не зареєстровано як провайдера OpenClaw. Для нього потрібен інший контракт двонапрямної голосової сесії, ніж для пакетного STT або потокового транскрибування.
  * `quality` зображення xAI, `mask` зображення та додаткові співвідношення сторін лише для нативного режиму не надаються, доки спільний інструмент `image_generate` не матиме відповідних міжпровайдерних елементів керування.

Advanced notes

  * OpenClaw автоматично застосовує специфічні для xAI виправлення сумісності схем інструментів і викликів інструментів у спільному шляху runner.
  * Нативні запити xAI за замовчуванням мають `tool_stream: true`. Установіть `agents.defaults.models["xai/<model>"].params.tool_stream` на `false`, щоб вимкнути це.
  * Вбудована обгортка xAI вилучає непідтримувані прапорці строгих схем інструментів і ключі payload reasoning перед надсиланням нативних запитів xAI.
  * `web_search`, `x_search` і `code_execution` надаються як інструменти OpenClaw. OpenClaw вмикає конкретний вбудований xAI-інструмент, потрібний у кожному запиті інструмента, замість того щоб додавати всі нативні інструменти до кожного ходу чату.
  * Grok `web_search` читає `plugins.entries.xai.config.webSearch.baseUrl`. `x_search` читає `plugins.entries.xai.config.xSearch.baseUrl`, а потім повертається до базової URL-адреси вебпошуку Grok.
  * `x_search` і `code_execution` належать вбудованому Plugin xAI, а не жорстко закодовані в core runtime моделей.
  * `code_execution` — це віддалене виконання в пісочниці xAI, а не локальний [`exec`](</uk/tools/exec>).


## Live-тестування

Медійні шляхи xAI покриті модульними тестами й live-наборами, що вмикаються явно. Live-команди завантажують секрети з вашої login shell, зокрема `~/.profile`, перед перевіркою `XAI_API_KEY`.

bashCopy code
[code]
    pnpm test extensions/xaiOPENCLAW_LIVE_TEST=1 OPENCLAW_LIVE_TEST_QUIET=1 pnpm test:live -- extensions/xai/xai.live.test.tsOPENCLAW_LIVE_TEST=1 OPENCLAW_LIVE_TEST_QUIET=1 OPENCLAW_LIVE_IMAGE_GENERATION_PROVIDERS=xai pnpm test:live -- test/image-generation.runtime.live.test.ts
[/code]

Файл live-тестів, специфічний для провайдера, синтезує звичайний TTS, зручний для телефонії PCM TTS, транскрибує аудіо через пакетний STT xAI, потоково передає той самий PCM через realtime STT xAI, генерує результат text-to-image і редагує еталонне зображення. Спільний live-файл для зображень перевіряє того самого провайдера xAI через вибір runtime OpenClaw, fallback, нормалізацію та шлях медійних вкладень.

## Пов’язане

[**Model selection** Вибір провайдерів, посилань на моделі та поведінки failover. ](</uk/concepts/model-providers>) [**Video generation** Спільні параметри відеоінструмента та вибір провайдера. ](</uk/tools/video-generation>) [**All providers** Ширший огляд провайдерів. ](</uk/providers>) [**Troubleshooting** Поширені проблеми та виправлення. ](</uk/help/troubleshooting>)

Was this useful?YesNo