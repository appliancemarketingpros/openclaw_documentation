---
title: Start- und Landebahn
source_url: https://docs.openclaw.ai/de/providers/runway
scraped_at: 2026-05-25
---

OpenClaw enthält einen gebündelten `runway`-Provider für gehostete Videogenerierung. Das Plugin ist standardmäßig aktiviert und registriert den `runway`-Provider für den `videoGenerationProviders`-Contract.

Eigenschaft | Wert  
---|---  
Provider-ID | `runway`  
Plugin | gebündelt, `enabledByDefault: true`  
Auth-Umgebungsvariablen | `RUNWAYML_API_SECRET` (kanonisch) oder `RUNWAY_API_KEY`  
Onboarding-Flag | `--auth-choice runway-api-key`  
Direktes CLI-Flag | `--runway-api-key <key>`  
API | Runway-Aufgaben-basierte Videogenerierung (`GET /v1/tasks/{id}` polling)  
Standardmodell | `runway/gen4.5`  
  
## Erste Schritte

* ### API-Schlüssel festlegen

bashCopy code
[code]
    openclaw onboard --auth-choice runway-api-key
[/code]

* ### Runway als Standard-Video-Provider festlegen

bashCopy code
[code]
    openclaw config set agents.defaults.videoGenerationModel.primary "runway/gen4.5"
[/code]

* ### Video generieren

Bitten Sie den Agenten, ein Video zu generieren. Runway wird automatisch verwendet.

## Unterstützte Modi und Modelle

Der Provider stellt sieben Runway-Modelle in drei Modi bereit. Dieselbe Modell-ID kann für mehr als einen Modus dienen (zum Beispiel funktioniert `gen4.5` sowohl für Text-zu-Video als auch für Bild-zu-Video).

Modus | Modelle | Referenzeingabe  
---|---|---  
Text-zu-Video | `gen4.5` (Standard), `veo3.1`, `veo3.1_fast`, `veo3` | Keine  
Bild-zu-Video | `gen4.5`, `gen4_turbo`, `gen3a_turbo`, `veo3.1`, `veo3.1_fast`, `veo3` | 1 lokales oder entferntes Bild  
Video-zu-Video | `gen4_aleph` | 1 lokales oder entferntes Video  
  
Lokale Bild- und Videoreferenzen werden über Data-URIs unterstützt.

Seitenverhältnisse | Zulässige Werte  
---|---  
Text-zu-Video | `16:9`, `9:16`  
Bild- und Videobearbeitungen | `1:1`, `16:9`, `9:16`, `3:4`, `4:3`, `21:9`  
  
## Konfiguration

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "runway/gen4.5",      },    },  },}
[/code]

## Erweiterte Konfiguration

Aliasse für Umgebungsvariablen

OpenClaw erkennt sowohl `RUNWAYML_API_SECRET` (kanonisch) als auch `RUNWAY_API_KEY`. Beide Variablen authentifizieren den Runway-Provider.

Aufgaben-Polling

Runway verwendet eine aufgabenbasierte API. Nach dem Senden einer Generierungsanfrage fragt OpenClaw `GET /v1/tasks/{id}` ab, bis das Video bereit ist. Für das Polling-Verhalten ist keine zusätzliche Konfiguration erforderlich.

## Verwandte Themen

[**Videogenerierung** Gemeinsame Tool-Parameter, Provider-Auswahl und asynchrones Verhalten. ](</de/tools/video-generation>) [**Konfigurationsreferenz** Standard-Agenteneinstellungen einschließlich Videogenerierungsmodell. ](</de/gateway/config-agents#agent-defaults>)

Was this useful?YesNo