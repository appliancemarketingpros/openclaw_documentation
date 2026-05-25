---
title: Azure Speech
source_url: https://docs.openclaw.ai/de/providers/azure-speech
scraped_at: 2026-05-25
---

Azure Speech ist ein Azure AI Speech Text-to-Speech-Anbieter. In OpenClaw synthetisiert er ausgehende Antwort-Audiodaten standardmäßig als MP3, natives Ogg/Opus für Sprach- nachrichten und 8-kHz-Mulaw-Audio für Telefonie-Kanäle wie Voice Call.

OpenClaw verwendet die Azure-Speech-REST-API direkt mit SSML und sendet das anbieterdefinierte Ausgabeformat über `X-Microsoft-OutputFormat`.

Detail | Wert  
---|---  
Website | [Azure AI Speech](<https://azure.microsoft.com/products/ai-services/ai-speech>)  
Dokumentation | [Speech REST text-to-speech](<https://learn.microsoft.com/azure/ai-services/speech-service/rest-text-to-speech>)  
Authentifizierung | `AZURE_SPEECH_KEY` plus `AZURE_SPEECH_REGION`  
Standardstimme | `en-US-JennyNeural`  
Standard-Dateiausgabe | `audio-24khz-48kbitrate-mono-mp3`  
Standard-Sprachnachricht-Datei | `ogg-24khz-16bit-mono-opus`  
  
## Erste Schritte

* ### Eine Azure-Speech-Ressource erstellen

Erstellen Sie im Azure-Portal eine Speech-Ressource. Kopieren Sie **KEY 1** aus Resource Management > Keys and Endpoint und kopieren Sie den Ressourcenstandort, zum Beispiel `eastus`.

CodeCopy code
[code]
    AZURE_SPEECH_KEY=<speech-resource-key>AZURE_SPEECH_REGION=eastus
[/code]

* ### Azure Speech in messages.tts auswählen

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "azure-speech",      providers: {        "azure-speech": {          voice: "en-US-JennyNeural",          lang: "en-US",        },      },    },  },}
[/code]

* ### Eine Nachricht senden

Senden Sie eine Antwort über einen beliebigen verbundenen Kanal. OpenClaw synthetisiert das Audio mit Azure Speech und liefert MP3 für Standard-Audio oder Ogg/Opus, wenn der Kanal eine Sprachnachricht erwartet.

## Konfigurationsoptionen

Option | Pfad | Beschreibung  
---|---|---  
`apiKey` | `messages.tts.providers.azure-speech.apiKey` | Schlüssel der Azure-Speech-Ressource. Fällt auf `AZURE_SPEECH_KEY`, `AZURE_SPEECH_API_KEY` oder `SPEECH_KEY` zurück.  
`region` | `messages.tts.providers.azure-speech.region` | Region der Azure-Speech-Ressource. Fällt auf `AZURE_SPEECH_REGION` oder `SPEECH_REGION` zurück.  
`endpoint` | `messages.tts.providers.azure-speech.endpoint` | Optionales Override für Azure-Speech-Endpunkt/Basis-URL.  
`baseUrl` | `messages.tts.providers.azure-speech.baseUrl` | Optionales Override für die Azure-Speech-Basis-URL.  
`voice` | `messages.tts.providers.azure-speech.voice` | Azure-Sprach-`ShortName` (Standard `en-US-JennyNeural`).  
`lang` | `messages.tts.providers.azure-speech.lang` | SSML-Sprachcode (Standard `en-US`).  
`outputFormat` | `messages.tts.providers.azure-speech.outputFormat` | Audio-Datei-Ausgabeformat (Standard `audio-24khz-48kbitrate-mono-mp3`).  
`voiceNoteOutputFormat` | `messages.tts.providers.azure-speech.voiceNoteOutputFormat` | Ausgabeformat für Sprachnachrichten (Standard `ogg-24khz-16bit-mono-opus`).  
  
## Hinweise

Authentifizierung

Azure Speech verwendet einen Schlüssel für die Speech-Ressource, keinen Azure-OpenAI-Schlüssel. Der Schlüssel wird als `Ocp-Apim-Subscription-Key` gesendet; OpenClaw leitet `https://<region>.tts.speech.microsoft.com` aus `region` ab, sofern Sie nicht `endpoint` oder `baseUrl` angeben.

Stimmnamen

Verwenden Sie den Azure-Speech-`ShortName` der Stimme, zum Beispiel `en-US-JennyNeural`. Der gebündelte Anbieter kann Stimmen über dieselbe Speech-Ressource auflisten und filtert Stimmen heraus, die als deprecated oder retired markiert sind.

Audioausgaben

Azure akzeptiert Ausgabeformate wie `audio-24khz-48kbitrate-mono-mp3`, `ogg-24khz-16bit-mono-opus` und `riff-24khz-16bit-mono-pcm`. OpenClaw fordert für Ziele vom Typ `voice-note` Ogg/Opus an, damit Kanäle native Sprachblasen ohne zusätzliche MP3-Konvertierung senden können.

Alias

`azure` wird als Anbieter-Alias für bestehende PRs und Nutzerkonfigurationen akzeptiert, aber neue Konfigurationen sollten `azure-speech` verwenden, um Verwechslungen mit Azure- OpenAI-Modellanbietern zu vermeiden.

## Verwandte Themen

[**Text-to-Speech** TTS-Überblick, Anbieter und Konfiguration von `messages.tts`. ](</de/tools/tts>) [**Konfiguration** Vollständige Konfigurationsreferenz einschließlich der Einstellungen für `messages.tts`. ](</de/gateway/configuration>) [**Anbieter** Alle gebündelten OpenClaw-Anbieter. ](</de/providers>) [**Fehlerbehebung** Häufige Probleme und Schritte zur Fehlerdiagnose. ](</de/help/troubleshooting>)

Was this useful?YesNo