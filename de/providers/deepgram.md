---
title: Deepgram
source_url: https://docs.openclaw.ai/de/providers/deepgram
scraped_at: 2026-05-25
---

Deepgram ist eine Speech-to-Text-API. In OpenClaw wird sie für die Transkription eingehender Audio-/Sprachnachrichten über `tools.media.audio` und für Streaming-STT in Voice Call über `plugins.entries.voice-call.config.streaming` verwendet.

Für Batch-Transkription lädt OpenClaw die vollständige Audiodatei zu Deepgram hoch und fügt das Transkript in die Antwortpipeline ein (`{{Transcript}}` \+ `[Audio]`-Block). Für Streaming in Voice Call leitet OpenClaw Live-G.711- u-law-Frames über Deepgrams WebSocket-Endpunkt `listen` weiter und gibt partielle oder finale Transkripte aus, sobald Deepgram sie zurückliefert.

Detail | Wert  
---|---  
Website | [deepgram.com](<https://deepgram.com>)  
Dokumentation | [developers.deepgram.com](<https://developers.deepgram.com>)  
Authentifizierung | `DEEPGRAM_API_KEY`  
Standardmodell | `nova-3`  
  
## Erste Schritte

* ### API-Schlüssel festlegen

Fügen Sie Ihren Deepgram-API-Schlüssel zur Umgebung hinzu:

CodeCopy code
[code]
    DEEPGRAM_API_KEY=dg_...
[/code]

* ### Audioprovier aktivieren

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "deepgram", model: "nova-3" }],      },    },  },}
[/code]

* ### Sprachnachricht senden

Senden Sie eine Audionachricht über einen beliebigen verbundenen Kanal. OpenClaw transkribiert sie über Deepgram und fügt das Transkript in die Antwortpipeline ein.

## Konfigurationsoptionen

Option | Pfad | Beschreibung  
---|---|---  
`model` | `tools.media.audio.models[].model` | Deepgram-Modell-ID (Standard: `nova-3`)  
`language` | `tools.media.audio.models[].language` | Sprachhinweis (optional)  
`detect_language` | `tools.media.audio.providerOptions.deepgram.detect_language` | Spracherkennung aktivieren (optional)  
`punctuate` | `tools.media.audio.providerOptions.deepgram.punctuate` | Zeichensetzung aktivieren (optional)  
`smart_format` | `tools.media.audio.providerOptions.deepgram.smart_format` | Intelligente Formatierung aktivieren (optional)  
  
### Mit Sprachhinweis

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "deepgram", model: "nova-3", language: "en" }],      },    },  },}
[/code]

### Mit Deepgram-Optionen

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        providerOptions: {          deepgram: {            detect_language: true,            punctuate: true,            smart_format: true,          },        },        models: [{ provider: "deepgram", model: "nova-3" }],      },    },  },}
[/code]

## Streaming-STT für Voice Call

Das gebündelte `deepgram`-Plugin registriert auch einen Echtzeit-Transkriptionsprovider für das Voice Call-Plugin.

Einstellung | Konfigurationspfad | Standard  
---|---|---  
API-Schlüssel | `plugins.entries.voice-call.config.streaming.providers.deepgram.apiKey` | Fällt auf `DEEPGRAM_API_KEY` zurück  
Modell | `...deepgram.model` | `nova-3`  
Sprache | `...deepgram.language` | (nicht gesetzt)  
Kodierung | `...deepgram.encoding` | `mulaw`  
Abtastrate | `...deepgram.sampleRate` | `8000`  
Endpointing | `...deepgram.endpointingMs` | `800`  
Zwischenergebnisse | `...deepgram.interimResults` | `true`  
json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        config: {          streaming: {            enabled: true,            provider: "deepgram",            providers: {              deepgram: {                apiKey: "${DEEPGRAM_API_KEY}",                model: "nova-3",                endpointingMs: 800,                language: "en-US",              },            },          },        },      },    },  },}
[/code]

## Hinweise

Authentifizierung

Die Authentifizierung folgt der standardmäßigen Auth-Reihenfolge für Provider. `DEEPGRAM_API_KEY` ist der einfachste Weg.

Proxy und benutzerdefinierte Endpunkte

Überschreiben Sie Endpunkte oder Header mit `tools.media.audio.baseUrl` und `tools.media.audio.headers`, wenn Sie einen Proxy verwenden.

Ausgabeverhalten

Die Ausgabe folgt denselben Audioregeln wie bei anderen Providern (Größenlimits, Timeouts, Transkript-Einfügung).

## Verwandt

[**Media-Tools** Überblick über die Audio-, Bild- und Videoverarbeitungspipeline. ](</de/tools/media-overview>) [**Konfiguration** Vollständige Konfigurationsreferenz einschließlich der Einstellungen für Media-Tools. ](</de/gateway/configuration>) [**Fehlerbehebung** Häufige Probleme und Schritte zur Fehlerbehebung. ](</de/help/troubleshooting>) [**FAQ** Häufig gestellte Fragen zur Einrichtung von OpenClaw. ](</de/help/faq>)

Was this useful?YesNo