---
title: Fal
source_url: https://docs.openclaw.ai/de/providers/fal
scraped_at: 2026-05-25
---

OpenClaw liefert einen gebündelten `fal`-Provider für gehostete Bild- und Videogenerierung aus.

Eigenschaft | Wert  
---|---  
Provider | `fal`  
Authentifizierung | `FAL_KEY` (kanonisch; `FAL_API_KEY` funktioniert auch als Fallback)  
API | fal-Modellendpunkte  
  
## Erste Schritte

* ### API-Schlüssel festlegen

bashCopy code
[code]
    openclaw onboard --auth-choice fal-api-key
[/code]

* ### Standard-Bildmodell festlegen

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "fal/fal-ai/flux/dev",      },    },  },}
[/code]

## Bildgenerierung

Der gebündelte `fal`-Provider für Bildgenerierung verwendet standardmäßig `fal/fal-ai/flux/dev`.

Fähigkeit | Wert  
---|---  
Maximale Bilder | 4 pro Anfrage  
Bearbeitungsmodus | Flux: 1 Referenzbild; GPT Image 2: 10; Nano Banana 2: 14  
Größenüberschreibungen | Unterstützt  
Seitenverhältnis | Unterstützt für Generierung und Bearbeitung mit GPT Image 2/Nano Banana 2  
Auflösung | Unterstützt  
Ausgabeformat | `png` oder `jpeg`  
  
Verwenden Sie `outputFormat: "png"`, wenn Sie eine PNG-Ausgabe möchten. fal deklariert in OpenClaw keine explizite Steuerung für transparente Hintergründe, daher wird `background: "transparent"` für fal-Modelle als ignorierte Überschreibung gemeldet.

So verwenden Sie fal als Standard-Bild-Provider:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "fal/fal-ai/flux/dev",      },    },  },}
[/code]

## Videogenerierung

Der gebündelte `fal`-Provider für Videogenerierung verwendet standardmäßig `fal/fal-ai/minimax/video-01-live`.

Fähigkeit | Wert  
---|---  
Modi | Text-zu-Video, Einzelbildreferenz, Seedance-Referenz-zu-Video  
Laufzeit | Warteschlangenbasierter Ablauf für Submit/Status/Ergebnis bei lang laufenden Jobs  
  
Verfügbare Videomodelle

**HeyGen video-agent:**

  * `fal/fal-ai/heygen/v2/video-agent`


**Seedance 2.0:**

  * `fal/bytedance/seedance-2.0/fast/text-to-video`
  * `fal/bytedance/seedance-2.0/fast/image-to-video`
  * `fal/bytedance/seedance-2.0/fast/reference-to-video`
  * `fal/bytedance/seedance-2.0/text-to-video`
  * `fal/bytedance/seedance-2.0/image-to-video`
  * `fal/bytedance/seedance-2.0/reference-to-video`

Seedance 2.0-Konfigurationsbeispiel json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "fal/bytedance/seedance-2.0/fast/text-to-video",      },    },  },}
[/code]

Seedance 2.0-Konfigurationsbeispiel für Referenz-zu-Video json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "fal/bytedance/seedance-2.0/fast/reference-to-video",      },    },  },}
[/code]

Referenz-zu-Video akzeptiert bis zu 9 Bilder, 3 Videos und 3 Audioreferenzen über die gemeinsamen Parameter `images`, `videos` und `audioRefs` von `video_generate`, mit maximal 12 Referenzdateien insgesamt.

HeyGen video-agent-Konfigurationsbeispiel json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "fal/fal-ai/heygen/v2/video-agent",      },    },  },}
[/code]

## Verwandte Themen

[**Bildgenerierung** Gemeinsame Bild-Tool-Parameter und Provider-Auswahl. ](</de/tools/image-generation>) [**Videogenerierung** Gemeinsame Video-Tool-Parameter und Provider-Auswahl. ](</de/tools/video-generation>) [**Konfigurationsreferenz** Agent-Standardwerte einschließlich Auswahl von Bild- und Videomodellen. ](</de/gateway/config-agents#agent-defaults>)

Was this useful?YesNo