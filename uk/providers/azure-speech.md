---
title: Azure Speech
source_url: https://docs.openclaw.ai/uk/providers/azure-speech
scraped_at: 2026-05-25
---

Azure Speech — це провайдер перетворення тексту на мовлення Azure AI Speech. В OpenClaw він синтезує аудіо вихідних відповідей як MP3 за замовчуванням, нативний Ogg/Opus для голосових повідомлень і аудіо mulaw 8 кГц для телефонних каналів, таких як Voice Call.

OpenClaw використовує REST API Azure Speech безпосередньо з SSML і надсилає формат виводу, що належить провайдеру, через `X-Microsoft-OutputFormat`.

Деталь | Значення  
---|---  
Вебсайт | [Azure AI Speech](<https://azure.microsoft.com/products/ai-services/ai-speech>)  
Документація | [Speech REST text-to-speech](<https://learn.microsoft.com/azure/ai-services/speech-service/rest-text-to-speech>)  
Автентифікація | `AZURE_SPEECH_KEY` плюс `AZURE_SPEECH_REGION`  
Голос за замовчуванням | `en-US-JennyNeural`  
Вивід файлу за замовчуванням | `audio-24khz-48kbitrate-mono-mp3`  
Файл голосового повідомлення за замовчуванням | `ogg-24khz-16bit-mono-opus`  
  
## Початок роботи

* ### Створіть ресурс Azure Speech

У порталі Azure створіть ресурс Speech. Скопіюйте **KEY 1** з Resource Management > Keys and Endpoint, а також скопіюйте розташування ресурсу, наприклад `eastus`.

CodeCopy code
[code]
    AZURE_SPEECH_KEY=<speech-resource-key>AZURE_SPEECH_REGION=eastus
[/code]

* ### Виберіть Azure Speech у messages.tts

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "azure-speech",      providers: {        "azure-speech": {          voice: "en-US-JennyNeural",          lang: "en-US",        },      },    },  },}
[/code]

* ### Надішліть повідомлення

Надішліть відповідь через будь-який підключений канал. OpenClaw синтезує аудіо за допомогою Azure Speech і доставляє MP3 для стандартного аудіо або Ogg/Opus, коли канал очікує голосове повідомлення.

## Параметри конфігурації

Параметр | Шлях | Опис  
---|---|---  
`apiKey` | `messages.tts.providers.azure-speech.apiKey` | Ключ ресурсу Azure Speech. Використовує `AZURE_SPEECH_KEY`, `AZURE_SPEECH_API_KEY` або `SPEECH_KEY` як запасний варіант.  
`region` | `messages.tts.providers.azure-speech.region` | Регіон ресурсу Azure Speech. Використовує `AZURE_SPEECH_REGION` або `SPEECH_REGION` як запасний варіант.  
`endpoint` | `messages.tts.providers.azure-speech.endpoint` | Необов’язкове перевизначення endpoint/base URL Azure Speech.  
`baseUrl` | `messages.tts.providers.azure-speech.baseUrl` | Необов’язкове перевизначення base URL Azure Speech.  
`voice` | `messages.tts.providers.azure-speech.voice` | `ShortName` голосу Azure (за замовчуванням `en-US-JennyNeural`).  
`lang` | `messages.tts.providers.azure-speech.lang` | Код мови SSML (за замовчуванням `en-US`).  
`outputFormat` | `messages.tts.providers.azure-speech.outputFormat` | Формат виводу аудіофайлу (за замовчуванням `audio-24khz-48kbitrate-mono-mp3`).  
`voiceNoteOutputFormat` | `messages.tts.providers.azure-speech.voiceNoteOutputFormat` | Формат виводу голосового повідомлення (за замовчуванням `ogg-24khz-16bit-mono-opus`).  
  
## Примітки

Автентифікація

Azure Speech використовує ключ ресурсу Speech, а не ключ Azure OpenAI. Ключ надсилається як `Ocp-Apim-Subscription-Key`; OpenClaw виводить `https://<region>.tts.speech.microsoft.com` з `region`, якщо ви не вкажете `endpoint` або `baseUrl`.

Назви голосів

Використовуйте значення `ShortName` голосу Azure Speech, наприклад `en-US-JennyNeural`. Вбудований провайдер може перелічувати голоси через той самий ресурс Speech і відфільтровує голоси, позначені як deprecated або retired.

Аудіовиходи

Azure приймає такі формати виводу, як `audio-24khz-48kbitrate-mono-mp3`, `ogg-24khz-16bit-mono-opus` і `riff-24khz-16bit-mono-pcm`. OpenClaw запитує Ogg/Opus для цілей `voice-note`, щоб канали могли надсилати нативні голосові бульбашки без додаткового перетворення MP3.

Псевдонім

`azure` приймається як псевдонім провайдера для наявних PR і конфігурації користувачів, але в новій конфігурації слід використовувати `azure-speech`, щоб уникнути плутанини з провайдерами моделей Azure OpenAI.

## Пов’язане

[**Перетворення тексту на мовлення** Огляд TTS, провайдери та конфігурація `messages.tts`. ](</uk/tools/tts>) [**Конфігурація** Повний довідник із конфігурації, включно з параметрами `messages.tts`. ](</uk/gateway/configuration>) [**Провайдери** Усі вбудовані провайдери OpenClaw. ](</uk/providers>) [**Усунення несправностей** Поширені проблеми та кроки налагодження. ](</uk/help/troubleshooting>)

Was this useful?YesNo