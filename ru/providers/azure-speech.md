---
title: Речь Azure
source_url: https://docs.openclaw.ai/ru/providers/azure-speech
scraped_at: 2026-06-29
---

ModelsProviders

Azure Speech — это провайдер преобразования текста в речь Azure AI Speech. В OpenClaw он по умолчанию синтезирует аудио исходящих ответов в MP3, нативный Ogg/Opus для голосовых сообщений и 8 kHz mulaw-аудио для телефонных каналов, таких как голосовой вызов.

OpenClaw использует Azure Speech REST API напрямую с SSML и передает формат вывода, определяемый провайдером, через `X-Microsoft-OutputFormat`.

Сведения | Значение  
---|---  
Сайт | [Azure AI Speech](<https://azure.microsoft.com/products/ai-services/ai-speech>)  
Документация | [Speech REST text-to-speech](<https://learn.microsoft.com/azure/ai-services/speech-service/rest-text-to-speech>)  
Аутентификация | `AZURE_SPEECH_KEY` плюс `AZURE_SPEECH_REGION`  
Голос по умолчанию | `en-US-JennyNeural`  
Файловый вывод по умолчанию | `audio-24khz-48kbitrate-mono-mp3`  
Файл голосового сообщения по умолчанию | `ogg-24khz-16bit-mono-opus`  
  
## Начало работы

* ### Create an Azure Speech resource

В портале Azure создайте ресурс Speech. Скопируйте **KEY 1** из «Управление ресурсами > Ключи и конечная точка», а также скопируйте расположение ресурса, например `eastus`.

CodeCopy code
[code]
    AZURE_SPEECH_KEY=<speech-resource-key>AZURE_SPEECH_REGION=eastus
[/code]

* ### Select Azure Speech in messages.tts

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "azure-speech",      providers: {        "azure-speech": {          speakerVoice: "en-US-JennyNeural",          lang: "en-US",        },      },    },  },}
[/code]

* ### Send a message

Отправьте ответ через любой подключенный канал. OpenClaw синтезирует аудио с помощью Azure Speech и доставляет MP3 для стандартного аудио либо Ogg/Opus, когда канал ожидает голосовое сообщение.

## Параметры конфигурации

Параметр | Путь | Описание  
---|---|---  
`apiKey` | `messages.tts.providers.azure-speech.apiKey` | Ключ ресурса Azure Speech. Использует `AZURE_SPEECH_KEY`, `AZURE_SPEECH_API_KEY` или `SPEECH_KEY` как запасной вариант.  
`region` | `messages.tts.providers.azure-speech.region` | Регион ресурса Azure Speech. Использует `AZURE_SPEECH_REGION` или `SPEECH_REGION` как запасной вариант.  
`endpoint` | `messages.tts.providers.azure-speech.endpoint` | Необязательное переопределение конечной точки/базового URL Azure Speech.  
`baseUrl` | `messages.tts.providers.azure-speech.baseUrl` | Необязательное переопределение базового URL Azure Speech.  
`speakerVoice` | `messages.tts.providers.azure-speech.speakerVoice` | ShortName голоса Azure (по умолчанию `en-US-JennyNeural`). Устаревший псевдоним: `voice`.  
`lang` | `messages.tts.providers.azure-speech.lang` | Код языка SSML (по умолчанию `en-US`).  
`outputFormat` | `messages.tts.providers.azure-speech.outputFormat` | Формат вывода аудиофайла (по умолчанию `audio-24khz-48kbitrate-mono-mp3`).  
`voiceNoteOutputFormat` | `messages.tts.providers.azure-speech.voiceNoteOutputFormat` | Формат вывода голосового сообщения (по умолчанию `ogg-24khz-16bit-mono-opus`).  
  
## Примечания

Authentication

Azure Speech использует ключ ресурса Speech, а не ключ Azure OpenAI. Ключ отправляется как `Ocp-Apim-Subscription-Key`; OpenClaw выводит `https://<region>.tts.speech.microsoft.com` из `region`, если вы не укажете `endpoint` или `baseUrl`.

Voice names

Используйте значение `ShortName` голоса Azure Speech, например `en-US-JennyNeural`. Встроенный провайдер может перечислять голоса через тот же ресурс Speech и отфильтровывает голоса, помеченные как устаревшие или выведенные из эксплуатации.

Audio outputs

Azure принимает форматы вывода, такие как `audio-24khz-48kbitrate-mono-mp3`, `ogg-24khz-16bit-mono-opus` и `riff-24khz-16bit-mono-pcm`. OpenClaw запрашивает Ogg/Opus для целей `voice-note`, чтобы каналы могли отправлять нативные голосовые сообщения без дополнительного преобразования MP3.

Alias

`azure` принимается как псевдоним провайдера для существующих PR и пользовательской конфигурации, но новая конфигурация должна использовать `azure-speech`, чтобы избежать путаницы с провайдерами моделей Azure OpenAI.

## Связанные материалы

[**Text-to-speech** Обзор TTS, провайдеры и конфигурация `messages.tts`. ](</ru/tools/tts>) [**Configuration** Полный справочник конфигурации, включая настройки `messages.tts`. ](</ru/gateway/configuration>) [**Providers** Все встроенные провайдеры OpenClaw. ](</ru/providers>) [**Troubleshooting** Распространенные проблемы и шаги отладки. ](</ru/help/troubleshooting>)

Was this useful?YesNo

Open issue