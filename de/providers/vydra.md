---
title: Vydra
source_url: https://docs.openclaw.ai/de/providers/vydra
scraped_at: 2026-05-25
---

Das gebündelte Vydra-Plugin fügt hinzu:

  * Bildgenerierung über `vydra/grok-imagine`
  * Videogenerierung über `vydra/veo3` und `vydra/kling`
  * Sprachsynthese über Vydras ElevenLabs-gestützte TTS-Route


OpenClaw verwendet denselben `VYDRA_API_KEY` für alle drei Funktionen.

Eigenschaft | Wert  
---|---  
Provider-ID | `vydra`  
Plugin | gebündelt, `enabledByDefault: true`  
Auth-Env-Var | `VYDRA_API_KEY`  
Onboarding-Flag | `--auth-choice vydra-api-key`  
Direkter CLI-Flag | `--vydra-api-key <key>`  
Verträge | `imageGenerationProviders`, `videoGenerationProviders`, `speechProviders`  
Basis-URL | `https://www.vydra.ai/api/v1` (verwenden Sie den Host `www`)  
  
## Einrichtung

* ### Interaktives Onboarding ausführen

bashCopy code
[code]
    openclaw onboard --auth-choice vydra-api-key
[/code]

Oder setzen Sie die Env-Var direkt:

bashCopy code
[code]
    export VYDRA_API_KEY="vydra_live_..."
[/code]

* ### Standardfunktion auswählen

Wählen Sie eine oder mehrere der folgenden Funktionen aus (Bild, Video oder Sprache) und wenden Sie die passende Konfiguration an.

## Funktionen

Bildgenerierung

Standard-Bildmodell:

  * `vydra/grok-imagine`


Legen Sie es als Standard-Bild-Provider fest:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "vydra/grok-imagine",      },    },  },}
[/code]

Die aktuelle gebündelte Unterstützung umfasst nur Text-zu-Bild. Vydras gehostete Bearbeitungsrouten erwarten Remote-Bild-URLs, und OpenClaw fügt im gebündelten Plugin noch keine Vydra-spezifische Upload-Bridge hinzu.

Videogenerierung

Registrierte Videomodelle:

  * `vydra/veo3` für Text-zu-Video
  * `vydra/kling` für Bild-zu-Video


Legen Sie Vydra als Standard-Video-Provider fest:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "vydra/veo3",      },    },  },}
[/code]

Hinweise:

  * `vydra/veo3` ist nur als Text-zu-Video gebündelt.
  * `vydra/kling` erfordert derzeit eine Remote-Bild-URL-Referenz. Lokale Datei-Uploads werden vorab abgelehnt.
  * Vydras aktuelle `kling`-HTTP-Route war bisher inkonsistent darin, ob sie `image_url` oder `video_url` erfordert; der gebündelte Provider ordnet dieselbe Remote-Bild-URL beiden Feldern zu.
  * Das gebündelte Plugin bleibt konservativ und leitet keine undokumentierten Stiloptionen wie Seitenverhältnis, Auflösung, Wasserzeichen oder generiertes Audio weiter.

Video-Live-Tests

Provider-spezifische Live-Abdeckung:

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 \OPENCLAW_LIVE_VYDRA_VIDEO=1 \pnpm test:live -- extensions/vydra/vydra.live.test.ts
[/code]

Die gebündelte Vydra-Live-Datei deckt jetzt ab:

  * `vydra/veo3` Text-zu-Video
  * `vydra/kling` Bild-zu-Video mit einer Remote-Bild-URL


Überschreiben Sie die Remote-Bild-Fixture bei Bedarf:

bashCopy code
[code]
    export OPENCLAW_LIVE_VYDRA_KLING_IMAGE_URL="https://example.com/reference.png"
[/code]

Sprachsynthese

Legen Sie Vydra als Sprach-Provider fest:

json5Copy code
[code]
    {  messages: {    tts: {      provider: "vydra",      providers: {        vydra: {          apiKey: "${VYDRA_API_KEY}",          voiceId: "21m00Tcm4TlvDq8ikWAM",        },      },    },  },}
[/code]

Standardwerte:

  * Modell: `elevenlabs/tts`
  * Voice-ID: `21m00Tcm4TlvDq8ikWAM`


Das gebündelte Plugin stellt derzeit eine bewährte Standardstimme bereit und gibt MP3-Audiodateien zurück.

## Verwandt

[**Provider-Verzeichnis** Durchsuchen Sie alle verfügbaren Provider. ](</de/providers>) [**Bildgenerierung** Gemeinsame Bild-Tool-Parameter und Provider-Auswahl. ](</de/tools/image-generation>) [**Videogenerierung** Gemeinsame Video-Tool-Parameter und Provider-Auswahl. ](</de/tools/video-generation>) [**Konfigurationsreferenz** Agent-Standardwerte und Modellkonfiguration. ](</de/gateway/config-agents#agent-defaults>)

Was this useful?YesNo