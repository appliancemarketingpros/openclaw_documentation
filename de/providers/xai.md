---
title: xAI
source_url: https://docs.openclaw.ai/de/providers/xai
scraped_at: 2026-05-25
---

OpenClaw liefert ein gebündeltes `xai`-Provider-Plugin für Grok-Modelle aus.

## Erste Schritte

* ### API-Schlüssel erstellen

Erstellen Sie einen API-Schlüssel in der [xAI-Konsole](<https://console.x.ai/>).

* ### Ihren API-Schlüssel festlegen

Legen Sie `XAI_API_KEY` fest, oder führen Sie aus:

bashCopy code
[code]
    openclaw onboard --auth-choice xai-api-key
[/code]

* ### Ein Modell auswählen

json5Copy code
[code]
    {  agents: { defaults: { model: { primary: "xai/grok-4.3" } } },}
[/code]

## Integrierter Katalog

OpenClaw enthält diese xAI-Modellfamilien standardmäßig:

Familie | Modell-IDs  
---|---  
Grok 3 | `grok-3`, `grok-3-fast`, `grok-3-mini`, `grok-3-mini-fast`  
Grok 4.3 | `grok-4.3`  
Grok 4 | `grok-4`, `grok-4-0709`  
Grok 4 Fast | `grok-4-fast`, `grok-4-fast-non-reasoning`  
Grok 4.1 Fast | `grok-4-1-fast`, `grok-4-1-fast-non-reasoning`  
Grok 4.20 Beta | `grok-4.20-beta-latest-reasoning`, `grok-4.20-beta-latest-non-reasoning`  
Grok Code | `grok-code-fast-1`  
  
Das Plugin löst auch neuere `grok-4*`\- und `grok-code-fast*`-IDs weiter auf, wenn sie derselben API-Struktur folgen.

## OpenClaw-Funktionsabdeckung

Das gebündelte Plugin bildet die aktuelle öffentliche API-Oberfläche von xAI auf die gemeinsamen Provider- und Tool-Verträge von OpenClaw ab. Fähigkeiten, die nicht zum gemeinsamen Vertrag passen (zum Beispiel Streaming-TTS und Echtzeit-Sprache), werden nicht bereitgestellt - siehe die Tabelle unten.

xAI-Fähigkeit | OpenClaw-Oberfläche | Status  
---|---|---  
Chat / Responses | `xai/<model>`-Modell-Provider | Ja  
Serverseitige Websuche | `web_search`-Provider `grok` | Ja  
Serverseitige X-Suche | `x_search`-Tool | Ja  
Serverseitige Codeausführung | `code_execution`-Tool | Ja  
Bilder | `image_generate` | Ja  
Videos | `video_generate` | Ja  
Batch-Text-zu-Sprache | `messages.tts.provider: "xai"` / `tts` | Ja  
Streaming-TTS | - | Nicht bereitgestellt; der TTS-Vertrag von OpenClaw gibt vollständige Audiopuffer zurück  
Batch-Sprache-zu-Text | `tools.media.audio` / Medienverständnis | Ja  
Streaming-Sprache-zu-Text | Voice Call `streaming.provider: "xai"` | Ja  
Echtzeit-Sprache | - | Noch nicht bereitgestellt; anderer Sitzungs-/WebSocket-Vertrag  
Dateien / Batches | Nur generische Modell-API-Kompatibilität | Kein erstklassiges OpenClaw-Tool  
  
### Fast-Modus-Zuordnungen

`/fast on` oder `agents.defaults.models["xai/<model>"].params.fastMode: true` schreibt native xAI-Anfragen wie folgt um:

Quellmodell | Fast-Modus-Ziel  
---|---  
`grok-3` | `grok-3-fast`  
`grok-3-mini` | `grok-3-mini-fast`  
`grok-4` | `grok-4-fast`  
`grok-4-0709` | `grok-4-fast`  
  
### Legacy-Kompatibilitätsaliase

Legacy-Aliase werden weiterhin auf die kanonischen gebündelten IDs normalisiert:

Legacy-Alias | Kanonische ID  
---|---  
`grok-4-fast-reasoning` | `grok-4-fast`  
`grok-4-1-fast-reasoning` | `grok-4-1-fast`  
`grok-4.20-reasoning` | `grok-4.20-beta-latest-reasoning`  
`grok-4.20-non-reasoning` | `grok-4.20-beta-latest-non-reasoning`  
  
## Funktionen

Websuche

Der gebündelte `grok`-Websuche-Provider kann `XAI_API_KEY` oder einen Plugin-Schlüssel für Websuche verwenden:

bashCopy code
[code]
    openclaw config set tools.web.search.provider grok
[/code]

Videogenerierung

Das gebündelte `xai`-Plugin registriert Videogenerierung über das gemeinsame `video_generate`-Tool.

  * Standard-Videomodell: `xai/grok-imagine-video`
  * Modi: Text-zu-Video, Bild-zu-Video, Referenzbildgenerierung, Remote-Video-Bearbeitung und Remote-Video-Erweiterung
  * Seitenverhältnisse: `1:1`, `16:9`, `9:16`, `4:3`, `3:4`, `3:2`, `2:3`
  * Auflösungen: `480P`, `720P`
  * Dauer: 1-15 Sekunden für Generierung/Bild-zu-Video, 1-10 Sekunden bei Verwendung von `reference_image`-Rollen, 2-10 Sekunden für Erweiterung
  * Referenzbildgenerierung: Setzen Sie `imageRoles` für jedes bereitgestellte Bild auf `reference_image`; xAI akzeptiert bis zu 7 solcher Bilder


Um xAI als Standard-Video-Provider zu verwenden:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "xai/grok-imagine-video",      },    },  },}
[/code]

Bildgenerierung

Das gebündelte `xai`-Plugin registriert Bildgenerierung über das gemeinsame `image_generate`-Tool.

  * Standard-Bildmodell: `xai/grok-imagine-image`
  * Zusätzliches Modell: `xai/grok-imagine-image-pro`
  * Modi: Text-zu-Bild und Referenzbild-Bearbeitung
  * Referenzeingaben: ein `image` oder bis zu fünf `images`
  * Seitenverhältnisse: `1:1`, `16:9`, `9:16`, `4:3`, `3:4`, `2:3`, `3:2`
  * Auflösungen: `1K`, `2K`
  * Anzahl: bis zu 4 Bilder


OpenClaw fordert von xAI `b64_json`-Bildantworten an, damit generierte Medien über den normalen Kanal-Anhangspfad gespeichert und bereitgestellt werden können. Lokale Referenzbilder werden in Daten-URLs konvertiert; remote `http(s)`-Referenzen werden durchgereicht.

Um xAI als Standard-Bild-Provider zu verwenden:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "xai/grok-imagine-image",      },    },  },}
[/code]

Text-zu-Sprache

Das gebündelte `xai`-Plugin registriert Text-zu-Sprache über die gemeinsame `tts`-Provider-Oberfläche.

  * Stimmen: `eve`, `ara`, `rex`, `sal`, `leo`, `una`
  * Standardstimme: `eve`
  * Formate: `mp3`, `wav`, `pcm`, `mulaw`, `alaw`
  * Sprache: BCP-47-Code oder `auto`
  * Geschwindigkeit: Provider-native Geschwindigkeitsüberschreibung
  * Natives Opus-Sprachnotizformat wird nicht unterstützt


Um xAI als Standard-TTS-Provider zu verwenden:

json5Copy code
[code]
    {  messages: {    tts: {      provider: "xai",      providers: {        xai: {          voiceId: "eve",        },      },    },  },}
[/code]

Sprache-zu-Text

Das gebündelte `xai`-Plugin registriert Batch-Sprache-zu-Text über die Medienverständnis-Transkriptionsoberfläche von OpenClaw.

  * Standardmodell: `grok-stt`
  * Endpunkt: xAI REST `/v1/stt`
  * Eingabepfad: Multipart-Audiodatei-Upload
  * Unterstützt von OpenClaw überall dort, wo eingehende Audiotranskription `tools.media.audio` verwendet, einschließlich Discord-Sprachkanal-Segmenten und Kanal-Audioanhängen


Um xAI für eingehende Audiotranskription zu erzwingen:

json5Copy code
[code]
    {  tools: {    media: {      audio: {        models: [          {            type: "provider",            provider: "xai",            model: "grok-stt",          },        ],      },    },  },}
[/code]

Die Sprache kann über die gemeinsame Audio-Medienkonfiguration oder pro Transkriptionsanfrage bereitgestellt werden. Prompt-Hinweise werden von der gemeinsamen OpenClaw-Oberfläche akzeptiert, aber die xAI-REST-STT-Integration leitet nur Datei, Modell und Sprache weiter, da diese sauber auf den aktuellen öffentlichen xAI-Endpunkt abbildbar sind.

Streaming-Sprache-zu-Text

Das gebündelte `xai`-Plugin registriert außerdem einen Echtzeit-Transkriptions-Provider für Live-Audio aus Sprachanrufen.

  * Endpunkt: xAI WebSocket `wss://api.x.ai/v1/stt`
  * Standardkodierung: `mulaw`
  * Standard-Abtastrate: `8000`
  * Standard-Endpointerkennung: `800ms`
  * Zwischen-Transkripte: standardmäßig aktiviert


Der Twilio-Medienstrom von Voice Call sendet G.711-µ-law-Audioframes, sodass der xAI-Provider diese Frames direkt ohne Transkodierung weiterleiten kann:

json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        config: {          streaming: {            enabled: true,            provider: "xai",            providers: {              xai: {                apiKey: "${XAI_API_KEY}",                endpointingMs: 800,                language: "en",              },            },          },        },      },    },  },}
[/code]

Provider-eigene Konfiguration befindet sich unter `plugins.entries.voice-call.config.streaming.providers.xai`. Unterstützte Schlüssel sind `apiKey`, `baseUrl`, `sampleRate`, `encoding` (`pcm`, `mulaw` oder `alaw`), `interimResults`, `endpointingMs` und `language`.

x_search-Konfiguration

Das gebündelte xAI-Plugin stellt `x_search` als OpenClaw-Tool zum Durchsuchen von X-Inhalten (ehemals Twitter) über Grok bereit.

Konfigurationspfad: `plugins.entries.xai.config.xSearch`

Schlüssel | Typ | Standardwert | Beschreibung  
---|---|---|---  
`enabled` | boolean | - | x_search aktivieren oder deaktivieren  
`model` | string | `grok-4-1-fast` | Für x_search-Anfragen verwendetes Modell  
`baseUrl` | string | - | Überschreibung der xAI Responses-Basis-URL  
`inlineCitations` | boolean | - | Inline-Zitationen in Ergebnisse aufnehmen  
`maxTurns` | number | - | Maximale Anzahl an Konversationsturns  
`timeoutSeconds` | number | - | Anfrage-Timeout in Sekunden  
`cacheTtlMinutes` | number | - | Cache-Lebensdauer in Minuten  
json5Copy code
[code]
    {  plugins: {    entries: {      xai: {        config: {          xSearch: {            enabled: true,            model: "grok-4-1-fast",            baseUrl: "https://api.x.ai/v1",            inlineCitations: true,          },        },      },    },  },}
[/code]

Konfiguration für Codeausführung

Das gebündelte xAI-Plugin stellt `code_execution` als OpenClaw-Tool für Remote-Codeausführung in der Sandbox-Umgebung von xAI bereit.

Konfigurationspfad: `plugins.entries.xai.config.codeExecution`

Schlüssel | Typ | Standardwert | Beschreibung  
---|---|---|---  
`enabled` | boolean | `true` (wenn Schlüssel verfügbar) | Codeausführung aktivieren oder deaktivieren  
`model` | string | `grok-4-1-fast` | Für Codeausführungsanfragen verwendetes Modell  
`maxTurns` | number | - | Maximale Anzahl an Konversationsturns  
`timeoutSeconds` | number | - | Anfrage-Timeout in Sekunden  
json5Copy code
[code]
    {  plugins: {    entries: {      xai: {        config: {          codeExecution: {            enabled: true,            model: "grok-4-1-fast",          },        },      },    },  },}
[/code]

Bekannte Einschränkungen

  * Authentifizierung erfolgt heute nur per API-Schlüssel. Der API-Schlüssel kann in einem xAI-Auth- Profil, einer Umgebungsvariable oder der Plugin-Konfiguration gespeichert werden; es gibt in OpenClaw noch keinen xAI-OAuth- oder Device-Code-Flow.
  * `grok-4.20-multi-agent-experimental-beta-0304` wird auf dem normalen xAI-Provider-Pfad nicht unterstützt, weil es eine andere Upstream-API- Oberfläche benötigt als der standardmäßige OpenClaw-xAI-Transport.
  * xAI Realtime Voice ist noch nicht als OpenClaw-Provider registriert. Es benötigt einen anderen bidirektionalen Voice-Session-Vertrag als Batch-STT oder Streaming-Transkription.
  * xAI-Bild-`quality`, Bild-`mask` und zusätzliche nur native Seitenverhältnisse werden erst offengelegt, wenn das gemeinsame `image_generate`-Tool entsprechende providerübergreifende Steuerelemente hat.

Erweiterte Hinweise

  * OpenClaw wendet xAI-spezifische Kompatibilitätskorrekturen für Tool-Schemas und Tool-Aufrufe automatisch auf dem gemeinsamen Runner-Pfad an.
  * Native xAI-Anfragen verwenden standardmäßig `tool_stream: true`. Setzen Sie `agents.defaults.models["xai/<model>"].params.tool_stream` auf `false`, um dies zu deaktivieren.
  * Der gebündelte xAI-Wrapper entfernt nicht unterstützte Strict-Tool-Schema-Flags und Reasoning-Payload-Schlüssel, bevor native xAI-Anfragen gesendet werden.
  * `web_search`, `x_search` und `code_execution` werden als OpenClaw- Tools offengelegt. OpenClaw aktiviert das jeweils benötigte spezifische integrierte xAI-Tool innerhalb jeder Tool-Anfrage, statt alle nativen Tools an jeden Chat-Turn anzuhängen.
  * Grok `web_search` liest `plugins.entries.xai.config.webSearch.baseUrl`. `x_search` liest `plugins.entries.xai.config.xSearch.baseUrl` und fällt dann auf die Grok-Web-Search-Basis-URL zurück.
  * `x_search` und `code_execution` gehören zum gebündelten xAI-Plugin und sind nicht fest in die Core-Modelllaufzeit codiert.
  * `code_execution` ist Remote-Ausführung in der xAI-Sandbox, nicht lokales [`exec`](</de/tools/exec>).


## Live-Tests

Die xAI-Medienpfade werden durch Unit-Tests und Opt-in-Live-Suites abgedeckt. Die Live- Befehle laden Secrets aus Ihrer Login-Shell, einschließlich `~/.profile`, bevor sie `XAI_API_KEY` prüfen.

bashCopy code
[code]
    pnpm test extensions/xaiOPENCLAW_LIVE_TEST=1 OPENCLAW_LIVE_TEST_QUIET=1 pnpm test:live -- extensions/xai/xai.live.test.tsOPENCLAW_LIVE_TEST=1 OPENCLAW_LIVE_TEST_QUIET=1 OPENCLAW_LIVE_IMAGE_GENERATION_PROVIDERS=xai pnpm test:live -- test/image-generation.runtime.live.test.ts
[/code]

Die providerspezifische Live-Datei synthetisiert normales TTS, telefoniefreundliches PCM- TTS, transkribiert Audio über xAI Batch-STT, streamt dasselbe PCM über xAI Realtime-STT, generiert Text-zu-Bild-Ausgabe und bearbeitet ein Referenzbild. Die gemeinsame Image-Live-Datei verifiziert denselben xAI-Provider über OpenClaws Laufzeitauswahl, Fallback, Normalisierung und Medienanhangspfad.

## Verwandt

[**Modellauswahl** Provider, Modellreferenzen und Failover-Verhalten auswählen. ](</de/concepts/model-providers>) [**Videogenerierung** Gemeinsame Videotool-Parameter und Provider-Auswahl. ](</de/tools/video-generation>) [**Alle Provider** Die umfassendere Provider-Übersicht. ](</de/providers>) [**Fehlerbehebung** Häufige Probleme und Korrekturen. ](</de/help/troubleshooting>)

Was this useful?YesNo