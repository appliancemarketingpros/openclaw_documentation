---
title: Deepgram
source_url: https://docs.openclaw.ai/ru/providers/deepgram
scraped_at: 2026-06-29
---

ModelsProviders

Deepgram — это API преобразования речи в текст. В OpenClaw он используется для транскрибации входящих аудио/голосовых заметок через `tools.media.audio` и для потокового STT голосовых вызовов через `plugins.entries.voice-call.config.streaming`.

Для пакетной транскрибации OpenClaw загружает полный аудиофайл в Deepgram и внедряет транскрипт в конвейер ответа (блок `{{Transcript}}` \+ `[Audio]`). Для потоковой передачи голосового вызова OpenClaw пересылает live-кадры G.711 u-law через WebSocket-эндпоинт Deepgram `listen` и выдает частичные или финальные транскрипты по мере их возврата Deepgram.

Сведения | Значение  
---|---  
Сайт | [deepgram.com](<https://deepgram.com>)  
Документация | [developers.deepgram.com](<https://developers.deepgram.com>)  
Аутентификация | `DEEPGRAM_API_KEY`  
Модель по умолчанию | `nova-3`  
  
## Начало работы

* ### Задайте ключ API

Добавьте ключ API Deepgram в окружение:

CodeCopy code
[code]
    DEEPGRAM_API_KEY=dg_...
[/code]

* ### Включите аудиопровайдера

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "deepgram", model: "nova-3" }],      },    },  },}
[/code]

* ### Отправьте голосовую заметку

Отправьте аудиосообщение через любой подключенный канал. OpenClaw транскрибирует его через Deepgram и внедрит транскрипт в конвейер ответа.

## Параметры конфигурации

Параметр | Путь | Описание  
---|---|---  
`model` | `tools.media.audio.models[].model` | Идентификатор модели Deepgram (по умолчанию: `nova-3`)  
`language` | `tools.media.audio.models[].language` | Подсказка языка (необязательно)  
`detect_language` | `tools.media.audio.providerOptions.deepgram.detect_language` | Включить определение языка (необязательно)  
`punctuate` | `tools.media.audio.providerOptions.deepgram.punctuate` | Включить пунктуацию (необязательно)  
`smart_format` | `tools.media.audio.providerOptions.deepgram.smart_format` | Включить интеллектуальное форматирование (необязательно)  
  
### С подсказкой языка

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "deepgram", model: "nova-3", language: "en" }],      },    },  },}
[/code]

### С параметрами Deepgram

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        providerOptions: {          deepgram: {            detect_language: true,            punctuate: true,            smart_format: true,          },        },        models: [{ provider: "deepgram", model: "nova-3" }],      },    },  },}
[/code]

## Потоковое STT для Voice Call

Встроенный Plugin `deepgram` также регистрирует поставщика транскрибации в реальном времени для Plugin Voice Call.

Настройка | Путь конфигурации | По умолчанию  
---|---|---  
Ключ API | `plugins.entries.voice-call.config.streaming.providers.deepgram.apiKey` | Использует `DEEPGRAM_API_KEY`  
Модель | `...deepgram.model` | `nova-3`  
Язык | `...deepgram.language` | (не задано)  
Кодирование | `...deepgram.encoding` | `mulaw`  
Частота дискретизации | `...deepgram.sampleRate` | `8000`  
Endpointing | `...deepgram.endpointingMs` | `800`  
Промежуточные результаты | `...deepgram.interimResults` | `true`  
  
json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        config: {          streaming: {            enabled: true,            provider: "deepgram",            providers: {              deepgram: {                apiKey: "${DEEPGRAM_API_KEY}",                model: "nova-3",                endpointingMs: 800,                language: "en-US",              },            },          },        },      },    },  },}
[/code]

## Примечания

Аутентификация

Аутентификация следует стандартному порядку авторизации поставщиков. `DEEPGRAM_API_KEY` — самый простой путь.

Прокси и пользовательские конечные точки

Переопределяйте конечные точки или заголовки с помощью `tools.media.audio.baseUrl` и `tools.media.audio.headers` при использовании прокси.

Поведение вывода

Вывод следует тем же правилам для аудио, что и у других поставщиков (ограничения размера, тайм-ауты, внедрение транскрипта).

## Связанные материалы

[**Медиаинструменты** Обзор конвейера обработки аудио, изображений и видео. ](</ru/tools/media-overview>) [**Конфигурация** Полный справочник конфигурации, включая настройки медиаинструментов. ](</ru/gateway/configuration>) [**Устранение неполадок** Распространенные проблемы и шаги отладки. ](</ru/help/troubleshooting>) [**Часто задаваемые вопросы** Часто задаваемые вопросы о настройке OpenClaw. ](</ru/help/faq>)

Was this useful?YesNo

Open issue