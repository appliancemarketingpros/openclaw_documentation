---
title: Gradium
source_url: https://docs.openclaw.ai/ru/providers/gradium
scraped_at: 2026-06-29
---

ModelsProviders

[Gradium](<https://gradium.ai>) — провайдер преобразования текста в речь для OpenClaw. Plugin может создавать обычные аудиоответы (WAV), совместимый с голосовыми заметками вывод Opus и 8 кГц u-law-аудио для телефонных поверхностей.

Свойство | Значение  
---|---  
ID провайдера | `gradium`  
Аутентификация | `GRADIUM_API_KEY` или config `apiKey`  
Базовый URL | `https://api.gradium.ai` (по умолчанию)  
Голос по умолчанию | `Emma` (`YTpq7expH9539ERJ`)  
  
## Установка plugin

Установите официальный plugin, затем перезапустите Gateway:

bashCopy code
[code]
    openclaw plugins install @openclaw/gradium-speechopenclaw gateway restart
[/code]

## Настройка

Создайте API-ключ Gradium, затем передайте его в OpenClaw через переменную окружения или ключ конфигурации.

### Переменная окружения

bashCopy code
[code]
    export GRADIUM_API_KEY="gsk_..."
[/code]

### Ключ конфигурации

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "gradium",      providers: {        gradium: {          apiKey: "${GRADIUM_API_KEY}",        },      },    },  },}
[/code]

Plugin сначала проверяет разрешенный `apiKey`, а затем откатывается к переменной окружения `GRADIUM_API_KEY`.

## Конфигурация

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "gradium",      providers: {        gradium: {          speakerVoiceId: "YTpq7expH9539ERJ",          // apiKey: "${GRADIUM_API_KEY}",          // baseUrl: "https://api.gradium.ai",        },      },    },  },}
[/code]

Ключ | Тип | Описание  
---|---|---  
`messages.tts.providers.gradium.apiKey` | string | Разрешенный API-ключ. Поддерживает `${ENV}` и ссылки на секреты.  
`messages.tts.providers.gradium.baseUrl` | string | Переопределяет origin API. Завершающие косые черты удаляются. По умолчанию `https://api.gradium.ai`.  
`messages.tts.providers.gradium.speakerVoiceId` | string | ID голоса по умолчанию, используемый при отсутствии переопределения директивой.  
  
Формат выходного аудио автоматически выбирается средой выполнения на основе целевой поверхности и не настраивается из `openclaw.json`. См. Вывод ниже.

## Голоса

Имя | ID голоса  
---|---  
Emma | `YTpq7expH9539ERJ`  
Kent | `LFZvm12tW_z0xfGo`  
Tiffany | `Eu9iL_CYe8N-Gkx_`  
Christina | `2H4HY2CBNyJHBCrP`  
Sydney | `jtEKaLYNn6iif5PR`  
John | `KWJiFWu2O9nMPYcR`  
Arthur | `3jUdJyOi9pgbxBTK`  
  
Голос по умолчанию: Emma.

### Переопределение голоса для сообщения

Когда активная политика речи разрешает переопределения голоса, можно переключать голоса прямо в тексте с помощью токена директивы. Используйте `speakerVoiceId` для нативных ID голосов провайдера.

textCopy code
[code]
    /voice:LFZvm12tW_z0xfGo/voice_id:LFZvm12tW_z0xfGo/voiceid:LFZvm12tW_z0xfGo/gradium_voice:LFZvm12tW_z0xfGo/gradiumvoice:LFZvm12tW_z0xfGo
[/code]

Если политика речи отключает переопределения голоса, директива потребляется, но игнорируется.

## Вывод

Среда выполнения выбирает формат вывода на основе целевой поверхности. Сейчас провайдер не синтезирует другие форматы.

Цель | Формат | Расширение файла | Частота дискретизации | Флаг совместимости с голосом  
---|---|---|---|---  
Стандартное аудио | `wav` | `.wav` | provider | нет  
Голосовая заметка | `opus` | `.opus` | provider | да  
Телефония | `ulaw_8000` | n/a | 8 кГц | n/a  
  
## Порядок автовыбора

Среди настроенных TTS-провайдеров порядок автовыбора Gradium — `30`. См. [Преобразование текста в речь](</ru/tools/tts>), чтобы узнать, как OpenClaw выбирает активного провайдера, когда `messages.tts.provider` не закреплен.

## Связанные материалы

  * [Преобразование текста в речь](</ru/tools/tts>)
  * [Обзор медиа](</ru/tools/media-overview>)


Was this useful?YesNo

Open issue