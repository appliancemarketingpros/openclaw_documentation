---
title: Azure Speech
source_url: https://docs.openclaw.ai/pl/providers/azure-speech
scraped_at: 2026-05-25
---

Azure Speech to provider syntezy mowy Azure AI Speech. W OpenClaw syntetyzuje wychodzące audio odpowiedzi domyślnie jako MP3, natywne Ogg/Opus dla notatek głosowych oraz audio mulaw 8 kHz dla kanałów telefonicznych, takich jak Voice Call.

OpenClaw używa bezpośrednio Azure Speech REST API z SSML i wysyła należący do providera format wyjściowy przez `X-Microsoft-OutputFormat`.

Szczegół | Wartość  
---|---  
Strona internetowa | [Azure AI Speech](<https://azure.microsoft.com/products/ai-services/ai-speech>)  
Dokumentacja | [Speech REST text-to-speech](<https://learn.microsoft.com/azure/ai-services/speech-service/rest-text-to-speech>)  
Uwierzytelnianie | `AZURE_SPEECH_KEY` plus `AZURE_SPEECH_REGION`  
Domyślny głos | `en-US-JennyNeural`  
Domyślny plik wyjściowy | `audio-24khz-48kbitrate-mono-mp3`  
Domyślny plik notatki głosowej | `ogg-24khz-16bit-mono-opus`  
  
## Pierwsze kroki

* ### Utwórz zasób Azure Speech

W portalu Azure utwórz zasób Speech. Skopiuj **KEY 1** z Resource Management > Keys and Endpoint oraz skopiuj lokalizację zasobu, na przykład `eastus`.

CodeCopy code
[code]
    AZURE_SPEECH_KEY=<speech-resource-key>AZURE_SPEECH_REGION=eastus
[/code]

* ### Wybierz Azure Speech w messages.tts

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "azure-speech",      providers: {        "azure-speech": {          voice: "en-US-JennyNeural",          lang: "en-US",        },      },    },  },}
[/code]

* ### Wyślij wiadomość

Wyślij odpowiedź przez dowolny podłączony kanał. OpenClaw syntetyzuje audio za pomocą Azure Speech i dostarcza MP3 dla standardowego audio lub Ogg/Opus, gdy kanał oczekuje notatki głosowej.

## Opcje konfiguracji

Opcja | Ścieżka | Opis  
---|---|---  
`apiKey` | `messages.tts.providers.azure-speech.apiKey` | Klucz zasobu Azure Speech. Zapasowo używa `AZURE_SPEECH_KEY`, `AZURE_SPEECH_API_KEY` lub `SPEECH_KEY`.  
`region` | `messages.tts.providers.azure-speech.region` | Region zasobu Azure Speech. Zapasowo używa `AZURE_SPEECH_REGION` lub `SPEECH_REGION`.  
`endpoint` | `messages.tts.providers.azure-speech.endpoint` | Opcjonalne nadpisanie endpointu/base URL Azure Speech.  
`baseUrl` | `messages.tts.providers.azure-speech.baseUrl` | Opcjonalne nadpisanie base URL Azure Speech.  
`voice` | `messages.tts.providers.azure-speech.voice` | Azure voice `ShortName` (domyślnie `en-US-JennyNeural`).  
`lang` | `messages.tts.providers.azure-speech.lang` | Kod języka SSML (domyślnie `en-US`).  
`outputFormat` | `messages.tts.providers.azure-speech.outputFormat` | Format wyjściowy pliku audio (domyślnie `audio-24khz-48kbitrate-mono-mp3`).  
`voiceNoteOutputFormat` | `messages.tts.providers.azure-speech.voiceNoteOutputFormat` | Format wyjściowy notatki głosowej (domyślnie `ogg-24khz-16bit-mono-opus`).  
  
## Uwagi

Uwierzytelnianie

Azure Speech używa klucza zasobu Speech, a nie klucza Azure OpenAI. Klucz jest wysyłany jako `Ocp-Apim-Subscription-Key`; OpenClaw wyprowadza `https://<region>.tts.speech.microsoft.com` z `region`, chyba że podasz `endpoint` lub `baseUrl`.

Nazwy głosów

Używaj wartości `ShortName` głosu Azure Speech, na przykład `en-US-JennyNeural`. Bundlowany provider może listować głosy przez ten sam zasób Speech i filtruje głosy oznaczone jako deprecated lub retired.

Wyjścia audio

Azure akceptuje formaty wyjściowe takie jak `audio-24khz-48kbitrate-mono-mp3`, `ogg-24khz-16bit-mono-opus` i `riff-24khz-16bit-mono-pcm`. OpenClaw żąda Ogg/Opus dla celów `voice-note`, aby kanały mogły wysyłać natywne dymki głosowe bez dodatkowej konwersji MP3.

Alias

`azure` jest akceptowane jako alias providera dla istniejących PR i konfiguracji użytkowników, ale nowa konfiguracja powinna używać `azure-speech`, aby uniknąć pomyłek z providerami modeli Azure OpenAI.

## Powiązane

[**Synteza mowy** Przegląd TTS, providerzy i konfiguracja `messages.tts`. ](</pl/tools/tts>) [**Konfiguracja** Pełne odniesienie do konfiguracji, w tym ustawienia `messages.tts`. ](</pl/gateway/configuration>) [**Providerzy** Wszystkie bundlowane providery OpenClaw. ](</pl/providers>) [**Rozwiązywanie problemów** Typowe problemy i kroki debugowania. ](</pl/help/troubleshooting>)

Was this useful?YesNo