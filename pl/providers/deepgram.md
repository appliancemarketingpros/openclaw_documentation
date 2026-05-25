---
title: Deepgram
source_url: https://docs.openclaw.ai/pl/providers/deepgram
scraped_at: 2026-05-25
---

Deepgram to API speech-to-text. W OpenClaw jest używane do transkrypcji przychodzącego audio/notatek głosowych przez `tools.media.audio` oraz do strumieniowego STT Voice Call przez `plugins.entries.voice-call.config.streaming`.

W przypadku transkrypcji wsadowej OpenClaw przesyła cały plik audio do Deepgram i wstrzykuje transkrypt do potoku odpowiedzi (`{{Transcript}}` \+ blok `[Audio]`). W przypadku strumieniowego Voice Call OpenClaw przekazuje na żywo ramki G.711 u-law przez endpoint WebSocket `listen` Deepgram i emituje transkrypty częściowe albo końcowe, gdy Deepgram je zwraca.

Szczegół | Wartość  
---|---  
Strona WWW | [deepgram.com](<https://deepgram.com>)  
Dokumentacja | [developers.deepgram.com](<https://developers.deepgram.com>)  
Uwierzytelnianie | `DEEPGRAM_API_KEY`  
Model domyślny | `nova-3`  
  
## Pierwsze kroki

* ### Ustaw klucz API

Dodaj klucz API Deepgram do środowiska:

CodeCopy code
[code]
    DEEPGRAM_API_KEY=dg_...
[/code]

* ### Włącz providera audio

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "deepgram", model: "nova-3" }],      },    },  },}
[/code]

* ### Wyślij notatkę głosową

Wyślij wiadomość audio przez dowolny połączony kanał. OpenClaw transkrybuje ją przez Deepgram i wstrzykuje transkrypt do potoku odpowiedzi.

## Opcje konfiguracji

Opcja | Ścieżka | Opis  
---|---|---  
`model` | `tools.media.audio.models[].model` | Identyfikator modelu Deepgram (domyślnie: `nova-3`)  
`language` | `tools.media.audio.models[].language` | Wskazówka języka (opcjonalnie)  
`detect_language` | `tools.media.audio.providerOptions.deepgram.detect_language` | Włącz wykrywanie języka (opcjonalnie)  
`punctuate` | `tools.media.audio.providerOptions.deepgram.punctuate` | Włącz interpunkcję (opcjonalnie)  
`smart_format` | `tools.media.audio.providerOptions.deepgram.smart_format` | Włącz inteligentne formatowanie (opcjonalnie)  
  
### Ze wskazówką języka

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "deepgram", model: "nova-3", language: "en" }],      },    },  },}
[/code]

### Z opcjami Deepgram

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        providerOptions: {          deepgram: {            detect_language: true,            punctuate: true,            smart_format: true,          },        },        models: [{ provider: "deepgram", model: "nova-3" }],      },    },  },}
[/code]

## Strumieniowe STT Voice Call

Dołączony Plugin `deepgram` rejestruje również providera transkrypcji w czasie rzeczywistym dla Plugin Voice Call.

Ustawienie | Ścieżka konfiguracji | Domyślnie  
---|---|---  
Klucz API | `plugins.entries.voice-call.config.streaming.providers.deepgram.apiKey` | Fallback do `DEEPGRAM_API_KEY`  
Model | `...deepgram.model` | `nova-3`  
Język | `...deepgram.language` | (nieustawione)  
Kodowanie | `...deepgram.encoding` | `mulaw`  
Częstotliwość próbkowania | `...deepgram.sampleRate` | `8000`  
Endpointing | `...deepgram.endpointingMs` | `800`  
Wyniki pośrednie | `...deepgram.interimResults` | `true`  
json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        config: {          streaming: {            enabled: true,            provider: "deepgram",            providers: {              deepgram: {                apiKey: "${DEEPGRAM_API_KEY}",                model: "nova-3",                endpointingMs: 800,                language: "en-US",              },            },          },        },      },    },  },}
[/code]

## Uwagi

Uwierzytelnianie

Uwierzytelnianie przebiega według standardowej kolejności uwierzytelniania providera. `DEEPGRAM_API_KEY` to najprostsza ścieżka.

Proxy i własne endpointy

Nadpisz endpointy lub nagłówki przez `tools.media.audio.baseUrl` i `tools.media.audio.headers`, gdy używasz proxy.

Zachowanie wyjścia

Wyjście podlega tym samym zasadom audio co u innych providerów (limity rozmiaru, timeouty, wstrzykiwanie transkryptu).

## Powiązane

[**Narzędzia multimedialne** Przegląd potoku przetwarzania audio, obrazów i wideo. ](</pl/tools/media-overview>) [**Konfiguracja** Pełna dokumentacja konfiguracji, w tym ustawienia narzędzi multimedialnych. ](</pl/gateway/configuration>) [**Rozwiązywanie problemów** Typowe problemy i kroki debugowania. ](</pl/help/troubleshooting>) [**FAQ** Najczęściej zadawane pytania dotyczące konfiguracji OpenClaw. ](</pl/help/faq>)

Was this useful?YesNo