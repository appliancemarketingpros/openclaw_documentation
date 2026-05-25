---
title: ComfyUI
source_url: https://docs.openclaw.ai/de/providers/comfy
scraped_at: 2026-05-25
---

OpenClaw enthält ein gebündeltes `comfy` Plugin für workflowgesteuerte ComfyUI-Ausführungen. Das Plugin ist vollständig workflowgesteuert, daher versucht OpenClaw nicht, generische Steuerelemente wie `size`, `aspectRatio`, `resolution`, `durationSeconds` oder TTS-ähnliche Optionen auf Ihren Graphen abzubilden.

Eigenschaft | Detail  
---|---  
Anbieter | `comfy`  
Modelle | `comfy/workflow`  
Gemeinsame Oberflächen | `image_generate`, `video_generate`, `music_generate`  
Authentifizierung | Keine für lokales ComfyUI; `COMFY_API_KEY` oder `COMFY_CLOUD_API_KEY` für Comfy Cloud  
API | ComfyUI `/prompt` / `/history` / `/view` und Comfy Cloud `/api/*`  
  
## Was unterstützt wird

  * Bildgenerierung aus einer Workflow-JSON
  * Bildbearbeitung mit 1 hochgeladenen Referenzbild
  * Videogenerierung aus einer Workflow-JSON
  * Videogenerierung mit 1 hochgeladenen Referenzbild
  * Musik- oder Audiogenerierung über das gemeinsame Tool `music_generate`
  * Herunterladen der Ausgabe von einem konfigurierten Node oder von allen passenden Ausgabe-Nodes


## Erste Schritte

Wählen Sie zwischen dem Ausführen von ComfyUI auf Ihrem eigenen Rechner oder der Nutzung von Comfy Cloud.

### Local

**Am besten geeignet für:** das Ausführen Ihrer eigenen ComfyUI-Instanz auf Ihrem Rechner oder im LAN.

* ### Start ComfyUI locally

Stellen Sie sicher, dass Ihre lokale ComfyUI-Instanz läuft (standardmäßig unter `http://127.0.0.1:8188`).

* ### Prepare your workflow JSON

Exportieren oder erstellen Sie eine ComfyUI-Workflow-JSON-Datei. Notieren Sie die Node-IDs für den Node zur Prompt-Eingabe und den Ausgabe-Node, aus dem OpenClaw lesen soll.

* ### Configure the provider

Setzen Sie `mode: "local"` und verweisen Sie auf Ihre Workflow-Datei. Hier ist ein minimales Bildbeispiel:

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          mode: "local",          baseUrl: "http://127.0.0.1:8188",          image: {            workflowPath: "./workflows/flux-api.json",            promptNodeId: "6",            outputNodeId: "9",          },        },      },    },  },}
[/code]

* ### Set the default model

Verweisen Sie OpenClaw für die konfigurierte Fähigkeit auf das Modell `comfy/workflow`:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "comfy/workflow",      },    },  },}
[/code]

* ### Verify

bashCopy code
[code]
    openclaw models list --provider comfy
[/code]

### Comfy Cloud

**Am besten geeignet für:** das Ausführen von Workflows in Comfy Cloud, ohne lokale GPU-Ressourcen verwalten zu müssen.

* ### Get an API key

Registrieren Sie sich unter [comfy.org](<https://comfy.org>) und generieren Sie einen API-Schlüssel in Ihrem Kontodashboard.

* ### Set the API key

Stellen Sie Ihren Schlüssel mit einer der folgenden Methoden bereit:

bashCopy code
[code]
    # Umgebungsvariable (bevorzugt)export COMFY_API_KEY="your-key" # Alternative Umgebungsvariableexport COMFY_CLOUD_API_KEY="your-key" # Oder direkt in der Konfigurationopenclaw config set plugins.entries.comfy.config.apiKey "your-key"
[/code]

* ### Prepare your workflow JSON

Exportieren oder erstellen Sie eine ComfyUI-Workflow-JSON-Datei. Notieren Sie die Node-IDs für den Node zur Prompt-Eingabe und den Ausgabe-Node.

* ### Configure the provider

Setzen Sie `mode: "cloud"` und verweisen Sie auf Ihre Workflow-Datei:

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          mode: "cloud",          image: {            workflowPath: "./workflows/flux-api.json",            promptNodeId: "6",            outputNodeId: "9",          },        },      },    },  },}
[/code]

* ### Set the default model

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "comfy/workflow",      },    },  },}
[/code]

* ### Verify

bashCopy code
[code]
    openclaw models list --provider comfy
[/code]

## Konfiguration

Comfy unterstützt gemeinsame Verbindungseinstellungen auf oberster Ebene sowie workflowbezogene Abschnitte pro Fähigkeit (`image`, `video`, `music`):

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          mode: "local",          baseUrl: "http://127.0.0.1:8188",          image: {            workflowPath: "./workflows/flux-api.json",            promptNodeId: "6",            outputNodeId: "9",          },          video: {            workflowPath: "./workflows/video-api.json",            promptNodeId: "12",            outputNodeId: "21",          },          music: {            workflowPath: "./workflows/music-api.json",            promptNodeId: "3",            outputNodeId: "18",          },        },      },    },  },}
[/code]

### Gemeinsame Schlüssel

Schlüssel | Typ | Beschreibung  
---|---|---  
`mode` | `"local"` oder `"cloud"` | Verbindungsmodus.  
`baseUrl` | string | Standard ist `http://127.0.0.1:8188` für lokal oder `https://cloud.comfy.org` für Cloud.  
`apiKey` | string | Optionaler Inline-Schlüssel als Alternative zu den Umgebungsvariablen `COMFY_API_KEY` / `COMFY_CLOUD_API_KEY`.  
`allowPrivateNetwork` | boolean | Erlaubt eine private/LAN-`baseUrl` im Cloud-Modus.  
  
### Schlüssel pro Fähigkeit

Diese Schlüssel gelten innerhalb der Abschnitte `image`, `video` oder `music`:

Schlüssel | Erforderlich | Standard | Beschreibung  
---|---|---|---  
`workflow` oder `workflowPath` | Ja | \-- | Pfad zur ComfyUI-Workflow-JSON-Datei.  
`promptNodeId` | Ja | \-- | Node-ID, die den Text-Prompt empfängt.  
`promptInputName` | Nein | `"text"` | Eingabename auf dem Prompt-Node.  
`outputNodeId` | Nein | \-- | Node-ID, aus der die Ausgabe gelesen wird. Wenn weggelassen, werden alle passenden Ausgabe-Nodes verwendet.  
`pollIntervalMs` | Nein | \-- | Abfrageintervall in Millisekunden für den Abschluss des Jobs.  
`timeoutMs` | Nein | \-- | Timeout in Millisekunden für die Workflow-Ausführung.  
  
Die Abschnitte `image` und `video` unterstützen außerdem:

Schlüssel | Erforderlich | Standard | Beschreibung  
---|---|---|---  
`inputImageNodeId` | Ja (beim Übergeben eines Referenzbilds) | \-- | Node-ID, die das hochgeladene Referenzbild empfängt.  
`inputImageInputName` | Nein | `"image"` | Eingabename auf dem Bild-Node.  
  
## Workflow-Details

Image workflows

Setzen Sie das Standardmodell für Bilder auf `comfy/workflow`:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "comfy/workflow",      },    },  },}
[/code]

**Beispiel für die Bearbeitung mit Referenzbild:**

Um die Bildbearbeitung mit einem hochgeladenen Referenzbild zu aktivieren, fügen Sie `inputImageNodeId` zu Ihrer Bildkonfiguration hinzu:

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          image: {            workflowPath: "./workflows/edit-api.json",            promptNodeId: "6",            inputImageNodeId: "7",            inputImageInputName: "image",            outputNodeId: "9",          },        },      },    },  },}
[/code]

Video workflows

Setzen Sie das Standardmodell für Videos auf `comfy/workflow`:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "comfy/workflow",      },    },  },}
[/code]

Comfy-Video-Workflows unterstützen Text-zu-Video und Bild-zu-Video über den konfigurierten Graphen.

Music workflows

Das gebündelte Plugin registriert einen Anbieter für Musikgenerierung für workflowdefinierte Audio- oder Musikausgaben, bereitgestellt über das gemeinsame Tool `music_generate`:

textCopy code
[code]
    /tool music_generate prompt="Warm ambient synth loop with soft tape texture"
[/code]

Verwenden Sie den Konfigurationsabschnitt `music`, um auf Ihre Audio-Workflow-JSON und den Ausgabe-Node zu verweisen.

Backward compatibility

Die bestehende Bildkonfiguration auf oberster Ebene (ohne den verschachtelten Abschnitt `image`) funktioniert weiterhin:

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          workflowPath: "./workflows/flux-api.json",          promptNodeId: "6",          outputNodeId: "9",        },      },    },  },}
[/code]

OpenClaw behandelt diese ältere Form als Konfiguration für den Bild-Workflow. Sie müssen nicht sofort migrieren, aber die verschachtelten Abschnitte `image` / `video` / `music` werden für neue Setups empfohlen.

Live tests

Es gibt eine opt-in Live-Abdeckung für das gebündelte Plugin:

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 COMFY_LIVE_TEST=1 pnpm test:live -- extensions/comfy/comfy.live.test.ts
[/code]

Der Live-Test überspringt einzelne Fälle für Bild, Video oder Musik, sofern der passende Comfy-Workflow-Abschnitt nicht konfiguriert ist.

## Verwandt

[**Bildgenerierung** Konfiguration und Verwendung des Tools für die Bildgenerierung. ](</de/tools/image-generation>) [**Videogenerierung** Konfiguration und Verwendung des Tools für die Videogenerierung. ](</de/tools/video-generation>) [**Musikgenerierung** Einrichtung des Tools für Musik- und Audiogenerierung. ](</de/tools/music-generation>) [**Anbieterverzeichnis** Überblick über alle Anbieter und Modellreferenzen. ](</de/providers>) [**Konfigurationsreferenz** Vollständige Konfigurationsreferenz einschließlich der Standardwerte für Agents. ](</de/gateway/config-agents#agent-defaults>)

Was this useful?YesNo