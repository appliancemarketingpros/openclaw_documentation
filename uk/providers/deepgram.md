---
title: Deepgram
source_url: https://docs.openclaw.ai/uk/providers/deepgram
scraped_at: 2026-05-25
---

Deepgram — це API перетворення мовлення на текст. В OpenClaw він використовується для транскрипції вхідних аудіо/голосових повідомлень через `tools.media.audio` і для потокового STT у Voice Call через `plugins.entries.voice-call.config.streaming`.

Для пакетної транскрипції OpenClaw завантажує повний аудіофайл у Deepgram і інжектує транскрипт у конвеєр відповіді (`{{Transcript}}` \+ блок `[Audio]`). Для потокового Voice Call OpenClaw пересилає live кадри G.711 u-law через WebSocket-кінцеву точку Deepgram `listen` і надсилає часткові або фінальні транскрипти в міру того, як Deepgram їх повертає.

Деталь | Значення  
---|---  
Вебсайт | [deepgram.com](<https://deepgram.com>)  
Документація | [developers.deepgram.com](<https://developers.deepgram.com>)  
Автентифікація | `DEEPGRAM_API_KEY`  
Типова модель | `nova-3`  
  
## Початок роботи

* ### Установіть свій API-ключ

Додайте свій API-ключ Deepgram до середовища:

CodeCopy code
[code]
    DEEPGRAM_API_KEY=dg_...
[/code]

* ### Увімкніть provider аудіо

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "deepgram", model: "nova-3" }],      },    },  },}
[/code]

* ### Надішліть голосове повідомлення

Надішліть аудіоповідомлення через будь-який підключений канал. OpenClaw транскрибує його через Deepgram і інжектує транскрипт у конвеєр відповіді.

## Параметри конфігурації

Параметр | Шлях | Опис  
---|---|---  
`model` | `tools.media.audio.models[].model` | id моделі Deepgram (типово: `nova-3`)  
`language` | `tools.media.audio.models[].language` | Підказка мови (необов’язково)  
`detect_language` | `tools.media.audio.providerOptions.deepgram.detect_language` | Увімкнути визначення мови (необов’язково)  
`punctuate` | `tools.media.audio.providerOptions.deepgram.punctuate` | Увімкнути пунктуацію (необов’язково)  
`smart_format` | `tools.media.audio.providerOptions.deepgram.smart_format` | Увімкнути smart formatting (необов’язково)  
  
### Із підказкою мови

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "deepgram", model: "nova-3", language: "en" }],      },    },  },}
[/code]

### З параметрами Deepgram

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        providerOptions: {          deepgram: {            detect_language: true,            punctuate: true,            smart_format: true,          },        },        models: [{ provider: "deepgram", model: "nova-3" }],      },    },  },}
[/code]

## Потоковий STT для Voice Call

Вбудований Plugin `deepgram` також реєструє provider транскрипції в реальному часі для Plugin Voice Call.

Налаштування | Шлях конфігурації | Типове значення  
---|---|---  
API-ключ | `plugins.entries.voice-call.config.streaming.providers.deepgram.apiKey` | Резервно використовує `DEEPGRAM_API_KEY`  
Модель | `...deepgram.model` | `nova-3`  
Мова | `...deepgram.language` | (не задано)  
Кодування | `...deepgram.encoding` | `mulaw`  
Частота дискретизації | `...deepgram.sampleRate` | `8000`  
Endpointing | `...deepgram.endpointingMs` | `800`  
Проміжні результати | `...deepgram.interimResults` | `true`  
json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        config: {          streaming: {            enabled: true,            provider: "deepgram",            providers: {              deepgram: {                apiKey: "${DEEPGRAM_API_KEY}",                model: "nova-3",                endpointingMs: 800,                language: "en-US",              },            },          },        },      },    },  },}
[/code]

## Примітки

Автентифікація

Автентифікація дотримується стандартного порядку автентифікації provider. `DEEPGRAM_API_KEY` — найпростіший шлях.

Проксі та власні кінцеві точки

Перевизначайте кінцеві точки або заголовки через `tools.media.audio.baseUrl` і `tools.media.audio.headers`, якщо використовуєте проксі.

Поведінка виведення

Виведення дотримується тих самих правил для аудіо, що й в інших provider (обмеження розміру, тайм-аути, інжекція транскрипту).

## Пов’язане

[**Media tools** Огляд конвеєра обробки аудіо, зображень і відео. ](</uk/tools/media-overview>) [**Конфігурація** Повний довідник конфігурації, включно з налаштуваннями media tools. ](</uk/gateway/configuration>) [**Усунення несправностей** Поширені проблеми та кроки налагодження. ](</uk/help/troubleshooting>) [**FAQ** Поширені запитання про налаштування OpenClaw. ](</uk/help/faq>)

Was this useful?YesNo