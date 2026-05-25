---
title: Google (Gemini)
source_url: https://docs.openclaw.ai/de/providers/google
scraped_at: 2026-05-25
---

Das Google-Plugin bietet Zugriff auf Gemini-Modelle über Google AI Studio sowie Bildgenerierung, Medienverständnis (Bild/Audio/Video), Text-to-Speech und Websuche über Gemini Grounding.

  * Provider: `google`
  * Authentifizierung: `GEMINI_API_KEY` oder `GOOGLE_API_KEY`
  * API: Google Gemini API
  * Laufzeitoption: Provider/Modell `agentRuntime.id: "google-gemini-cli"` verwendet Gemini CLI OAuth wieder, während Modellreferenzen kanonisch als `google/*` bleiben.


## Erste Schritte

Wählen Sie Ihre bevorzugte Authentifizierungsmethode und folgen Sie den Einrichtungsschritten.

### API-Schlüssel

**Am besten für:** Standardzugriff auf die Gemini API über Google AI Studio.

* ### Onboarding ausführen

bashCopy code
[code]
    openclaw onboard --auth-choice gemini-api-key
[/code]

Oder übergeben Sie den Schlüssel direkt:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice gemini-api-key \  --gemini-api-key "$GEMINI_API_KEY"
[/code]

* ### Standardmodell festlegen

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "google/gemini-3.1-pro-preview" },    },  },}
[/code]

* ### Prüfen, ob das Modell verfügbar ist

bashCopy code
[code]
    openclaw models list --provider google
[/code]

### Gemini CLI (OAuth)

**Am besten für:** Wiederverwendung einer bestehenden Gemini CLI-Anmeldung über PKCE OAuth statt eines separaten API-Schlüssels.

* ### Gemini CLI installieren

Der lokale Befehl `gemini` muss auf `PATH` verfügbar sein.

bashCopy code
[code]
    # Homebrewbrew install gemini-cli # or npmnpm install -g @google/gemini-cli
[/code]

OpenClaw unterstützt sowohl Homebrew-Installationen als auch globale npm-Installationen, einschließlich gängiger Windows/npm-Layouts.

* ### Über OAuth anmelden

bashCopy code
[code]
    openclaw models auth login --provider google-gemini-cli --set-default
[/code]

* ### Prüfen, ob das Modell verfügbar ist

bashCopy code
[code]
    openclaw models list --provider google
[/code]

  * Standardmodell: `google/gemini-3.1-pro-preview`
  * Runtime: `google-gemini-cli`
  * Alias: `gemini-cli`


Die Gemini API-Modell-ID von Gemini 3.1 Pro lautet `gemini-3.1-pro-preview`. OpenClaw akzeptiert den kürzeren Wert `google/gemini-3.1-pro` als praktischen Alias und normalisiert ihn vor Provider-Aufrufen.

**Umgebungsvariablen:**

  * `OPENCLAW_GEMINI_OAUTH_CLIENT_ID`
  * `OPENCLAW_GEMINI_OAUTH_CLIENT_SECRET`


(Oder die `GEMINI_CLI_*`-Varianten.)

`google-gemini-cli/*`-Modellreferenzen sind Legacy-Kompatibilitätsaliase. Neue Konfigurationen sollten `google/*`-Modellreferenzen plus die Runtime `google-gemini-cli` verwenden, wenn lokale Gemini CLI-Ausführung gewünscht ist.

## Fähigkeiten

Fähigkeit | Unterstützt  
---|---  
Chat-Vervollständigungen | Ja  
Bildgenerierung | Ja  
Musikgenerierung | Ja  
Text-to-Speech | Ja  
Echtzeit-Sprache | Ja (Google Live API)  
Bildverständnis | Ja  
Audiotranskription | Ja  
Videoverständnis | Ja  
Websuche (Grounding) | Ja  
Denken/Reasoning | Ja (Gemini 2.5+ / Gemini 3+)  
Gemma 4-Modelle | Ja  
  
## Websuche

Der gebündelte `gemini`-Provider für Websuche verwendet Gemini Google Search Grounding. Konfigurieren Sie einen dedizierten Suchschlüssel unter `plugins.entries.google.config.webSearch`, oder lassen Sie ihn nach `GEMINI_API_KEY` `models.providers.google.apiKey` wiederverwenden:

json5Copy code
[code]
    {  plugins: {    entries: {      google: {        config: {          webSearch: {            apiKey: "AIza...", // optional if GEMINI_API_KEY or models.providers.google.apiKey is set            baseUrl: "https://generativelanguage.googleapis.com/v1beta", // falls back to models.providers.google.baseUrl            model: "gemini-2.5-flash",          },        },      },    },  },}
[/code]

Die Priorität für Anmeldedaten ist zuerst dediziertes `webSearch.apiKey`, dann `GEMINI_API_KEY`, dann `models.providers.google.apiKey`. `webSearch.baseUrl` ist optional und existiert für Betreiber-Proxys oder kompatible Gemini API-Endpunkte; wenn es ausgelassen wird, verwendet die Gemini-Websuche `models.providers.google.baseUrl` wieder. Siehe [Gemini-Suche](</de/tools/gemini-search>) für das Provider-spezifische Toolverhalten.

## Bildgenerierung

Der gebündelte `google`-Provider für Bildgenerierung verwendet standardmäßig `google/gemini-3.1-flash-image-preview`.

  * Unterstützt auch `google/gemini-3-pro-image-preview`
  * Generieren: bis zu 4 Bilder pro Anfrage
  * Bearbeitungsmodus: aktiviert, bis zu 5 Eingabebilder
  * Geometriesteuerungen: `size`, `aspectRatio` und `resolution`


So verwenden Sie Google als Standard-Provider für Bilder:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "google/gemini-3.1-flash-image-preview",      },    },  },}
[/code]

## Videogenerierung

Das gebündelte `google`-Plugin registriert außerdem Videogenerierung über das gemeinsame Tool `video_generate`.

  * Standard-Videomodell: `google/veo-3.1-fast-generate-preview`
  * Modi: Text-zu-Video, Bild-zu-Video und Einzelvideo-Referenz-Flows
  * Unterstützt `aspectRatio` (`16:9`, `9:16`) und `resolution` (`720P`, `1080P`); Audioausgabe wird von Veo derzeit nicht unterstützt
  * Unterstützte Dauern: **4, 6 oder 8 Sekunden** (andere Werte werden auf den nächstgelegenen zulässigen Wert gesetzt)


So verwenden Sie Google als Standard-Provider für Videos:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "google/veo-3.1-fast-generate-preview",      },    },  },}
[/code]

## Musikgenerierung

Das gebündelte `google`-Plugin registriert außerdem Musikgenerierung über das gemeinsame Tool `music_generate`.

  * Standard-Musikmodell: `google/lyria-3-clip-preview`
  * Unterstützt auch `google/lyria-3-pro-preview`
  * Prompt-Steuerungen: `lyrics` und `instrumental`
  * Ausgabeformat: standardmäßig `mp3`, außerdem `wav` auf `google/lyria-3-pro-preview`
  * Referenzeingaben: bis zu 10 Bilder
  * Sitzungsbasierte Läufe werden über den gemeinsamen Aufgaben-/Status-Flow entkoppelt, einschließlich `action: "status"`


So verwenden Sie Google als Standard-Provider für Musik:

json5Copy code
[code]
    {  agents: {    defaults: {      musicGenerationModel: {        primary: "google/lyria-3-clip-preview",      },    },  },}
[/code]

## Text-to-Speech

Der gebündelte `google`-Sprach-Provider verwendet den Gemini API-TTS-Pfad mit `gemini-3.1-flash-tts-preview`.

  * Standardstimme: `Kore`
  * Authentifizierung: `messages.tts.providers.google.apiKey`, `models.providers.google.apiKey`, `GEMINI_API_KEY` oder `GOOGLE_API_KEY`
  * Ausgabe: WAV für reguläre TTS-Anhänge, Opus für Sprachnotiz-Ziele, PCM für Talk/Telefonie
  * Sprachnotiz-Ausgabe: Google PCM wird als WAV verpackt und mit `ffmpeg` in 48-kHz-Opus transkodiert


Googles Batch-Gemini-TTS-Pfad gibt generiertes Audio in der abgeschlossenen `generateContent`-Antwort zurück. Verwenden Sie für gesprochene Unterhaltungen mit geringster Latenz den Google-Echtzeit-Sprach-Provider, der auf der Gemini Live API basiert, statt Batch- TTS.

So verwenden Sie Google als Standard-TTS-Provider:

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "google",      providers: {        google: {          model: "gemini-3.1-flash-tts-preview",          voiceName: "Kore",          audioProfile: "Speak professionally with a calm tone.",        },      },    },  },}
[/code]

Gemini API TTS verwendet natürlichsprachliche Prompts zur Stilsteuerung. Setzen Sie `audioProfile`, um dem gesprochenen Text einen wiederverwendbaren Stil-Prompt voranzustellen. Setzen Sie `speakerName`, wenn Ihr Prompt-Text auf einen benannten Sprecher verweist.

Gemini API TTS akzeptiert außerdem ausdrucksstarke Audio-Tags in eckigen Klammern im Text, wie `[whispers]` oder `[laughs]`. Um Tags aus der sichtbaren Chat-Antwort herauszuhalten, sie aber an TTS zu senden, platzieren Sie sie in einem `[[tts:text]]...[[/tts:text]]`\- Block:

textCopy code
[code]
    Here is the clean reply text. [[tts:text]][whispers] Here is the spoken version.[[/tts:text]]
[/code]

## Echtzeit-Sprache

Das gebündelte `google`-Plugin registriert einen Echtzeit-Sprach-Provider, der auf der Gemini Live API für Backend-Audio-Bridges wie Voice Call und Google Meet basiert.

Einstellung | Konfigurationspfad | Standard  
---|---|---  
Modell | `plugins.entries.voice-call.config.realtime.providers.google.model` | `gemini-2.5-flash-native-audio-preview-12-2025`  
Stimme | `...google.voice` | `Kore`  
Temperatur | `...google.temperature` | (nicht gesetzt)  
VAD-Startempfindlichkeit | `...google.startSensitivity` | (nicht gesetzt)  
VAD-Endempfindlichkeit | `...google.endSensitivity` | (nicht gesetzt)  
Stilledauer | `...google.silenceDurationMs` | (nicht gesetzt)  
Aktivitätsbehandlung | `...google.activityHandling` | Google-Standard, `start-of-activity-interrupts`  
Turn-Abdeckung | `...google.turnCoverage` | Google-Standard, `only-activity`  
Automatische VAD deaktivieren | `...google.automaticActivityDetectionDisabled` | `false`  
Sitzungsfortsetzung | `...google.sessionResumption` | `true`  
Kontextkomprimierung | `...google.contextWindowCompression` | `true`  
API-Schlüssel | `...google.apiKey` | Fällt auf `models.providers.google.apiKey`, `GEMINI_API_KEY` oder `GOOGLE_API_KEY` zurück  
  
Beispiel für die Realtime-Konfiguration von Voice Call:

json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        enabled: true,        config: {          realtime: {            enabled: true,            provider: "google",            providers: {              google: {                model: "gemini-2.5-flash-native-audio-preview-12-2025",                voice: "Kore",                activityHandling: "start-of-activity-interrupts",                turnCoverage: "only-activity",              },            },          },        },      },    },  },}
[/code]

Für die Live-Verifikation durch Maintainer führen Sie `OPENAI_API_KEY=... GEMINI_API_KEY=... node --import tsx scripts/dev/realtime-talk-live-smoke.ts` aus. Der Smoke-Test deckt auch OpenAI-Backend-/WebRTC-Pfade ab; der Google-Abschnitt erstellt dieselbe eingeschränkte Live-API-Token-Form, die von Control UI Talk verwendet wird, öffnet den Browser- WebSocket-Endpunkt, sendet die anfängliche Setup-Nutzlast und wartet auf `setupComplete`.

## Erweiterte Konfiguration

Direkte Wiederverwendung des Gemini-Cache

Für direkte Gemini-API-Läufe (`api: "google-generative-ai"`) leitet OpenClaw ein konfiguriertes `cachedContent`-Handle an Gemini-Anfragen weiter.

  * Konfigurieren Sie Parameter pro Modell oder global entweder mit `cachedContent` oder dem alten `cached_content`
  * Wenn beide vorhanden sind, hat `cachedContent` Vorrang
  * Beispielwert: `cachedContents/prebuilt-context`
  * Die Gemini-Cache-Hit-Nutzung wird aus dem Upstream-`cachedContentTokenCount` in OpenClaw `cacheRead` normalisiert

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "google/gemini-2.5-pro": {          params: {            cachedContent: "cachedContents/prebuilt-context",          },        },      },    },  },}
[/code]

Nutzungshinweise für Gemini CLI JSON

Bei Verwendung des OAuth-Providers `google-gemini-cli` normalisiert OpenClaw die CLI-JSON-Ausgabe wie folgt:

  * Antworttext stammt aus dem CLI-JSON-Feld `response`.
  * Die Nutzung fällt auf `stats` zurück, wenn die CLI `usage` leer lässt.
  * `stats.cached` wird in OpenClaw `cacheRead` normalisiert.
  * Wenn `stats.input` fehlt, leitet OpenClaw Eingabe-Token aus `stats.input_tokens - stats.cached` ab.

Umgebungs- und Daemon-Einrichtung

Wenn der Gateway als Daemon ausgeführt wird (launchd/systemd), stellen Sie sicher, dass `GEMINI_API_KEY` für diesen Prozess verfügbar ist (zum Beispiel in `~/.openclaw/.env` oder über `env.shellEnv`).

## Verwandte Themen

[**Modellauswahl** Provider, Modellreferenzen und Failover-Verhalten auswählen. ](</de/concepts/model-providers>) [**Bildgenerierung** Gemeinsame Bild-Tool-Parameter und Provider-Auswahl. ](</de/tools/image-generation>) [**Videogenerierung** Gemeinsame Video-Tool-Parameter und Provider-Auswahl. ](</de/tools/video-generation>) [**Musikgenerierung** Gemeinsame Musik-Tool-Parameter und Provider-Auswahl. ](</de/tools/music-generation>)

Was this useful?YesNo