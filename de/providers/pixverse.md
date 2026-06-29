---
title: PixVerse
source_url: https://docs.openclaw.ai/de/providers/pixverse
scraped_at: 2026-06-29
---

ModelsProviders

OpenClaw stellt `pixverse` als offizielles externes Plugin für gehostete PixVerse-Videogenerierung bereit. Das Plugin registriert den Provider `pixverse` gegen den Vertrag `videoGenerationProviders`.

Eigenschaft | Wert  
---|---  
Provider-ID | `pixverse`  
Plugin-Paket | `@openclaw/pixverse-provider`  
Auth-Umgebungsvariable | `PIXVERSE_API_KEY`  
Onboarding-Flag | `--auth-choice pixverse-api-key`  
Direkter CLI-Flag | `--pixverse-api-key <key>`  
API | PixVerse Platform API v2 (`video_id`-Übermittlung plus Ergebnis-Polling)  
Standardmodell | `pixverse/v6`  
Standard-API-Region | International  
  
## Erste Schritte

* ### Installieren Sie das Plugin

bashCopy code
[code]
    openclaw plugins install clawhub:@openclaw/pixverse-provideropenclaw gateway restart
[/code]

* ### Legen Sie den API-Schlüssel fest

bashCopy code
[code]
    openclaw onboard --auth-choice pixverse-api-key
[/code]

Der Assistent fragt, ob der internationale Endpunkt (`https://app-api.pixverse.ai/openapi/v2`) oder der CN-Endpunkt (`https://app-api.pixverseai.cn/openapi/v2`) verwendet werden soll, bevor `region` und `baseUrl` in die Provider-Konfiguration geschrieben werden.

* ### Legen Sie PixVerse als Standard-Video-Provider fest

bashCopy code
[code]
    openclaw config set agents.defaults.videoGenerationModel.primary "pixverse/v6"
[/code]

* ### Generieren Sie ein Video

Bitten Sie den Agenten, ein Video zu generieren. PixVerse wird automatisch verwendet.

## Unterstützte Modi und Modelle

Der Provider stellt PixVerse-Generierungsmodelle über das gemeinsame Video-Tool von OpenClaw bereit.

Modus | Modelle | Referenzeingabe  
---|---|---  
Text-zu-Video | `v6` (Standard), `c1` | Keine  
Bild-zu-Video | `v6` (Standard), `c1` | 1 lokales oder Remote-Bild  
  
Lokale Bildreferenzen werden vor der Bild-zu-Video-Anfrage zu PixVerse hochgeladen. Remote-Bild-URLs werden über den PixVerse-Bildupload-Endpunkt als `image_url` weitergegeben.

Option | Unterstützte Werte  
---|---  
Dauer | 1-15 Sekunden  
Auflösung | `360P`, `540P`, `720P`, `1080P`  
Seitenverhältnis | `16:9`, `4:3`, `1:1`, `3:4`, `9:16`, `2:3`, `3:2`, `21:9` für Text-zu-Video  
Generiertes Audio | `audio: true`  
  
## Provider-Optionen

Der Video-Provider akzeptiert diese optionalen Provider-spezifischen Schlüssel:

Option | Typ | Wirkung  
---|---|---  
`seed` | number | Deterministischer Seed, sofern unterstützt  
`negativePrompt` / `negative_prompt` | string | Negativer Prompt  
`quality` | string | PixVerse-Qualität wie `720p`  
`motionMode` / `motion_mode` | string | Bewegungsmodus für Bild-zu-Video  
`cameraMovement` / `camera_movement` | string | PixVerse-Kamerabewegungs-Preset  
`templateId` / `template_id` | number | Aktivierte PixVerse-Template-ID  
  
## Konfiguration

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "pixverse/v6",      },    },  },}
[/code]

## Erweiterte Konfiguration

API-Region

OpenClaw verwendet standardmäßig die internationale PixVerse-API. Legen Sie `models.providers.pixverse.region` manuell fest, wenn Ihr Schlüssel zu einer bestimmten PixVerse-Plattformregion gehört, oder verwenden Sie `openclaw onboard --auth-choice pixverse-api-key`, um im Einrichtungsassistenten eine Region auszuwählen:

Regionswert | PixVerse-API-Basis-URL  
---|---  
`international` | `https://app-api.pixverse.ai/openapi/v2`  
`cn` | `https://app-api.pixverseai.cn/openapi/v2`  
  
json5Copy code
[code]
    {  models: {    providers: {      pixverse: {        region: "cn", // "international" or "cn"        baseUrl: "https://app-api.pixverseai.cn/openapi/v2",        models: [],      },    },  },}
[/code]

Benutzerdefinierte Basis-URL

Legen Sie `models.providers.pixverse.baseUrl` nur fest, wenn das Routing über einen vertrauenswürdigen kompatiblen Proxy erfolgt. `baseUrl` hat Vorrang vor `region`.

json5Copy code
[code]
    {  models: {    providers: {      pixverse: {        baseUrl: "https://app-api.pixverse.ai/openapi/v2",      },    },  },}
[/code]

Aufgaben-Polling

PixVerse gibt aus der Generierungsanfrage eine `video_id` zurück. OpenClaw pollt `/openapi/v2/video/result/{video_id}`, bis die Aufgabe erfolgreich ist, fehlschlägt oder ein Timeout erreicht.

## Verwandte Themen

[**Videogenerierung** Gemeinsame Tool-Parameter, Provider-Auswahl und asynchrones Verhalten. ](</de/tools/video-generation>) [**Konfigurationsreferenz** Agenten-Standardeinstellungen einschließlich Videogenerierungsmodell. ](</de/gateway/config-agents#agent-defaults>)

Was this useful?YesNo

Open issue