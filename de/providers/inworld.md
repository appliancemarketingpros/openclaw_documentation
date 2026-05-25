---
title: Inworld
source_url: https://docs.openclaw.ai/de/providers/inworld
scraped_at: 2026-05-25
---

Inworld ist ein Streaming-Text-to-Speech-Provider (TTS). In OpenClaw synthetisiert er ausgehendes Antwort-Audio (standardmäßig MP3, OGG_OPUS für Sprachnachrichten) und PCM-Audio für Telefoniekanäle wie Voice Call.

OpenClaw sendet Anfragen an den Streaming-TTS-Endpunkt von Inworld, verkettet die zurückgegebenen Base64-Audio-Chunks zu einem einzelnen Puffer und übergibt das Ergebnis an die standardmäßige Antwort-Audio-Pipeline.

Eigenschaft | Wert  
---|---  
Provider-ID | `inworld`  
Plugin | mitgeliefert, `enabledByDefault: true`  
Kontrakt | `speechProviders` (nur TTS)  
Auth-Env-Var | `INWORLD_API_KEY` (HTTP Basic, Base64-Dashboard-Zugangsdaten)  
Basis-URL | `https://api.inworld.ai`  
Standardstimme | `Sarah`  
Standardmodell | `inworld-tts-1.5-max`  
Ausgabe | MP3 (Standard), OGG_OPUS (Sprachnachrichten), PCM 22050 Hz (Telefonie)  
Website | [inworld.ai](<https://inworld.ai>)  
Dokumentation | [docs.inworld.ai/tts/tts](<https://docs.inworld.ai/tts/tts>)  
  
## Erste Schritte

* ### API-Schlüssel festlegen

Kopieren Sie die Zugangsdaten aus Ihrem Inworld-Dashboard (Workspace > API Keys) und legen Sie sie als Env-Var fest. Der Wert wird unverändert als HTTP-Basic- Zugangsdaten gesendet. Kodieren Sie ihn daher nicht erneut mit Base64 und wandeln Sie ihn nicht in ein Bearer-Token um.

CodeCopy code
[code]
    INWORLD_API_KEY=<base64-credential-from-dashboard>
[/code]

* ### Inworld in messages.tts auswählen

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "inworld",      providers: {        inworld: {          voiceId: "Sarah",          modelId: "inworld-tts-1.5-max",        },      },    },  },}
[/code]

* ### Nachricht senden

Senden Sie eine Antwort über einen beliebigen verbundenen Kanal. OpenClaw synthetisiert das Audio mit Inworld und liefert es als MP3 aus (oder als OGG_OPUS, wenn der Kanal eine Sprachnachricht erwartet).

## Konfigurationsoptionen

Option | Pfad | Beschreibung  
---|---|---  
`apiKey` | `messages.tts.providers.inworld.apiKey` | Base64-Dashboard-Zugangsdaten. Fällt auf `INWORLD_API_KEY` zurück.  
`baseUrl` | `messages.tts.providers.inworld.baseUrl` | Überschreibt die Inworld-API-Basis-URL (Standard `https://api.inworld.ai`).  
`voiceId` | `messages.tts.providers.inworld.voiceId` | Stimmkennung (Standard `Sarah`).  
`modelId` | `messages.tts.providers.inworld.modelId` | TTS-Modell-ID (Standard `inworld-tts-1.5-max`).  
`temperature` | `messages.tts.providers.inworld.temperature` | Sampling-Temperatur `0..2` (optional).  
  
## Hinweise

Authentifizierung

Inworld verwendet HTTP-Basic-Authentifizierung mit einer einzelnen Base64-kodierten Zeichenfolge für Zugangsdaten. Kopieren Sie sie unverändert aus dem Inworld-Dashboard. Der Provider sendet sie als `Authorization: Basic <apiKey>` ohne weitere Kodierung. Kodieren Sie sie daher nicht selbst mit Base64 und übergeben Sie kein Bearer-artiges Token. Siehe [TTS-Authentifizierungshinweise](</de/tools/tts#inworld-primary>) für denselben Hinweis.

Modelle

Unterstützte Modell-IDs: `inworld-tts-1.5-max` (Standard), `inworld-tts-1.5-mini`, `inworld-tts-1-max`, `inworld-tts-1`.

Audioausgaben

Antworten verwenden standardmäßig MP3. Wenn das Kanalziel `voice-note` ist, fordert OpenClaw bei Inworld `OGG_OPUS` an, damit das Audio als native Sprachblase abgespielt wird. Die Telefoniesynthese verwendet rohes `PCM` mit 22050 Hz, um die Telefonie-Bridge zu speisen.

Benutzerdefinierte Endpunkte

Überschreiben Sie den API-Host mit `messages.tts.providers.inworld.baseUrl`. Abschließende Schrägstriche werden entfernt, bevor Anfragen gesendet werden.

## Verwandte Themen

[**Text-to-Speech** TTS-Übersicht, Provider und `messages.tts`-Konfiguration. ](</de/tools/tts>) [**Konfiguration** Vollständige Konfigurationsreferenz einschließlich `messages.tts`-Einstellungen. ](</de/gateway/configuration>) [**Provider** Alle mitgelieferten OpenClaw-Provider. ](</de/providers>) [**Fehlerbehebung** Häufige Probleme und Debugging-Schritte. ](</de/help/troubleshooting>)

Was this useful?YesNo