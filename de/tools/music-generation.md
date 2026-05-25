---
title: Musikgenerierung
source_url: https://docs.openclaw.ai/de/tools/music-generation
scraped_at: 2026-05-25
---

Das `music_generate`-Tool lässt den Agenten Musik oder Audio über die geteilte Musikgenerierungsfunktion mit konfigurierten Providern erstellen – derzeit Google, MiniMax und per Workflow konfiguriertes ComfyUI.

Bei sitzungsgestützten Agentenläufen startet OpenClaw die Musikgenerierung als Hintergrundaufgabe, verfolgt sie im Aufgaben-Ledger und weckt den Agenten erneut, wenn der Track bereit ist, damit der Agent den Benutzer informieren und das fertige Audio anhängen kann. In Gruppen-/Channel-Chats, die nur über Message-Tools sichtbar zustellen, übermittelt der Agent das Ergebnis über das Message-Tool. Wenn der Completion-Agent nur eine private finale Antwort schreibt, fällt OpenClaw auf einen direkten Channel-Versand mit den generierten Medien zurück. Der Completion-Wake weist den Agenten ausdrücklich darauf hin, dass normale finale Antworten in diesen Routen privat sind.

## Schnellstart

### Geteilter Provider-gestützt

* ### Authentifizierung konfigurieren

Legen Sie einen API-Schlüssel für mindestens einen Provider fest – zum Beispiel `GEMINI_API_KEY` oder `MINIMAX_API_KEY`.

* ### Standardmodell auswählen (optional)

json5Copy code
[code]
    {  agents: {    defaults: {      musicGenerationModel: {        primary: "google/lyria-3-clip-preview",      },    },  },}
[/code]

* ### Agenten fragen

_"Generate an upbeat synthpop track about a night drive through a neon city."_

Der Agent ruft `music_generate` automatisch auf. Keine Tool-Allowlist erforderlich.

Für direkte synchrone Kontexte ohne sitzungsgestützten Agentenlauf fällt das integrierte Tool weiterhin auf Inline-Generierung zurück und gibt den finalen Medienpfad im Tool-Ergebnis zurück.

### ComfyUI-Workflow

* ### Workflow konfigurieren

Konfigurieren Sie `plugins.entries.comfy.config.music` mit einem Workflow-JSON sowie Prompt-/Ausgabeknoten.

* ### Cloud-Authentifizierung (optional)

Legen Sie für Comfy Cloud `COMFY_API_KEY` oder `COMFY_CLOUD_API_KEY` fest.

* ### Tool aufrufen

textCopy code
[code]
    /tool music_generate prompt="Warm ambient synth loop with soft tape texture"
[/code]

Beispiel-Prompts:

textCopy code
[code]
    Generate a cinematic piano track with soft strings and no vocals.
[/code]

textCopy code
[code]
    Generate an energetic chiptune loop about launching a rocket at sunrise.
[/code]

## Unterstützte Provider

Provider | Standardmodell | Referenzeingaben | Unterstützte Steuerungen | Authentifizierung  
---|---|---|---|---  
ComfyUI | `workflow` | Bis zu 1 Bild | Workflow-definierte Musik oder Audio | `COMFY_API_KEY`, `COMFY_CLOUD_API_KEY`  
Google | `lyria-3-clip-preview` | Bis zu 10 Bilder | `lyrics`, `instrumental`, `format` | `GEMINI_API_KEY`, `GOOGLE_API_KEY`  
MiniMax | `music-2.6` | Keine | `lyrics`, `instrumental`, `durationSeconds`, `format=mp3` | `MINIMAX_API_KEY` oder MiniMax OAuth  
  
### Funktionsmatrix

Der explizite Modusvertrag, den `music_generate`, Contract-Tests und der geteilte Live-Sweep verwenden:

Provider | `generate` | `edit` | Bearbeitungslimit | Gemeinsame Live-Lanes  
---|---|---|---|---  
ComfyUI | ✓ | ✓ | 1 Bild | Nicht im geteilten Sweep; durch `extensions/comfy/comfy.live.test.ts` abgedeckt  
Google | ✓ | ✓ | 10 Bilder | `generate`, `edit`  
MiniMax | ✓ | — | Keine | `generate`  
  
Verwenden Sie `action: "list"`, um verfügbare geteilte Provider und Modelle zur Laufzeit zu prüfen:

textCopy code
[code]
    /tool music_generate action=list
[/code]

Verwenden Sie `action: "status"`, um die aktive sitzungsgestützte Musikaufgabe zu prüfen:

textCopy code
[code]
    /tool music_generate action=status
[/code]

Beispiel für direkte Generierung:

textCopy code
[code]
    /tool music_generate prompt="Dreamy lo-fi hip hop with vinyl texture and gentle rain" instrumental=true
[/code]

## Tool-Parameter

Prompt für die Musikgenerierung. Erforderlich für `action: "generate"`.

`"status"` gibt die aktuelle Sitzungsaufgabe zurück; `"list"` prüft Provider.

Provider-/Modell-Override (z. B. `google/lyria-3-pro-preview`, `comfy/workflow`).

Optionaler Liedtext, wenn der Provider explizite Liedtexteingabe unterstützt.

Fordert eine rein instrumentale Ausgabe an, wenn der Provider dies unterstützt.

Einzelner Referenzbildpfad oder URL.

Mehrere Referenzbilder (bis zu 10 bei unterstützenden Providern).

Zieldauer in Sekunden, wenn der Provider Dauerhinweise unterstützt.

Hinweis zum Ausgabeformat, wenn der Provider dies unterstützt.

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InRpbWVvdXRNcyIgdHlwZT0ibnVtYmVyIg Optionales Zeitlimit für Provider-Anfragen in Millisekunden. Wenn es weggelassen wird, verwendet OpenClaw `agents.defaults.musicGenerationModel.timeoutMs`, sofern konfiguriert. Werte unter 10000ms werden auf 10000ms angehoben und im Tool-Ergebnis gemeldet. OPENCLAW_DOCS_MARKER:paramClose:

## Asynchrones Verhalten

Sitzungsgestützte Musikgenerierung läuft als Hintergrundaufgabe:

  * **Hintergrundaufgabe:** `music_generate` erstellt eine Hintergrundaufgabe, gibt sofort eine Started-/Task-Antwort zurück und postet den fertigen Track später in einer nachfolgenden Agentennachricht.
  * **Duplikatvermeidung:** Solange eine Aufgabe `queued` oder `running` ist, geben spätere `music_generate`-Aufrufe in derselben Sitzung den Aufgabenstatus zurück, statt eine weitere Generierung zu starten. Verwenden Sie `action: "status"` für eine explizite Prüfung.
  * **Statusabfrage:** `openclaw tasks list` oder `openclaw tasks show <taskId>` prüft wartende, laufende und terminale Status.
  * **Completion-Wake:** OpenClaw injiziert ein internes Completion-Ereignis zurück in dieselbe Sitzung, damit das Modell selbst die für Benutzer sichtbare Folgenachricht schreiben kann.
  * **Prompt-Hinweis:** Spätere Benutzer-/manuelle Turns in derselben Sitzung erhalten einen kleinen Laufzeithinweis, wenn bereits eine Musikaufgabe läuft, damit das Modell `music_generate` nicht blind erneut aufruft.
  * **Fallback ohne Sitzung:** Direkte/lokale Kontexte ohne echte Agentensitzung laufen inline und geben das finale Audioergebnis im selben Turn zurück.


### Aufgabenlebenszyklus

Status | Bedeutung  
---|---  
`queued` | Aufgabe erstellt, wartet darauf, dass der Provider sie akzeptiert.  
`running` | Provider verarbeitet sie (typisch 30 Sekunden bis 3 Minuten, je nach Provider und Dauer).  
`succeeded` | Track bereit; der Agent wird geweckt und postet ihn in die Unterhaltung.  
`failed` | Provider-Fehler oder Zeitüberschreitung; der Agent wird mit Fehlerdetails geweckt.  
  
Status über die CLI prüfen:

bashCopy code
[code]
    openclaw tasks listopenclaw tasks show <taskId>openclaw tasks cancel <taskId>
[/code]

## Konfiguration

### Modellauswahl

json5Copy code
[code]
    {  agents: {    defaults: {      musicGenerationModel: {        primary: "google/lyria-3-clip-preview",        fallbacks: ["minimax/music-2.6"],      },    },  },}
[/code]

### Reihenfolge der Providerauswahl

OpenClaw versucht Provider in dieser Reihenfolge:

  1. `model`-Parameter aus dem Tool-Aufruf (wenn der Agent einen angibt).
  2. `musicGenerationModel.primary` aus der Konfiguration.
  3. `musicGenerationModel.fallbacks` der Reihe nach.
  4. Automatische Erkennung nur mit authentifizierungsgestützten Provider-Standards: 
     * aktueller Standard-Provider zuerst;
     * übrige registrierte Musikgenerierungs-Provider in Provider-ID-Reihenfolge.


Wenn ein Provider fehlschlägt, wird der nächste Kandidat automatisch versucht. Wenn alle fehlschlagen, enthält der Fehler Details zu jedem Versuch.

Legen Sie `agents.defaults.mediaGenerationAutoProviderFallback: false` fest, um nur explizite Einträge für `model`, `primary` und `fallbacks` zu verwenden.

## Provider-Hinweise

ComfyUI

Workflow-gesteuert und abhängig vom konfigurierten Graphen sowie dem Knoten-Mapping für Prompt-/Ausgabefelder. Das gebündelte `comfy`-Plugin bindet sich über die Provider-Registry für Musikgenerierung in das geteilte `music_generate`-Tool ein.

Google (Lyria 3)

Verwendet Lyria-3-Batchgenerierung. Der aktuelle gebündelte Ablauf unterstützt Prompt, optionalen Liedtext und optionale Referenzbilder.

MiniMax

Verwendet den Batch-Endpunkt `music_generation`. Unterstützt Prompt, optionalen Liedtext, Instrumentalmodus, Dauersteuerung und mp3-Ausgabe über `minimax`-API-Schlüssel-Authentifizierung oder `minimax-portal` OAuth.

## Den richtigen Pfad wählen

  * **Geteilter Provider-gestützt** , wenn Sie Modellauswahl, Provider-Failover und den integrierten asynchronen Task-/Statusablauf möchten.
  * **Plugin-Pfad (ComfyUI)** , wenn Sie einen benutzerdefinierten Workflow-Graphen oder einen Provider benötigen, der nicht Teil der geteilten gebündelten Musikfunktion ist.


Wenn Sie ComfyUI-spezifisches Verhalten debuggen, siehe [ComfyUI](</de/providers/comfy>). Wenn Sie geteiltes Provider-Verhalten debuggen, beginnen Sie mit [Google (Gemini)](</de/providers/google>) oder [MiniMax](</de/providers/minimax>).

## Provider-Funktionsmodi

Der geteilte Musikgenerierungsvertrag unterstützt explizite Modusdeklarationen:

  * `generate` für reine Prompt-Generierung.
  * `edit`, wenn die Anfrage ein oder mehrere Referenzbilder enthält.


Neue Provider-Implementierungen sollten explizite Modusblöcke bevorzugen:

typescriptCopy code
[code]
    capabilities: {  generate: {    maxTracks: 1,    supportsLyrics: true,    supportsFormat: true,  },  edit: {    enabled: true,    maxTracks: 1,    maxInputImages: 1,    supportsFormat: true,  },}
[/code]

Legacy-Flachfelder wie `maxInputImages`, `supportsLyrics` und `supportsFormat` reichen **nicht** aus, um Bearbeitungsunterstützung anzukündigen. Provider sollten `generate` und `edit` explizit deklarieren, damit Live-Tests, Contract-Tests und das geteilte `music_generate`-Tool Modusunterstützung deterministisch validieren können.

## Live-Tests

Opt-in-Live-Abdeckung für die geteilten gebündelten Provider:

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 pnpm test:live -- extensions/music-generation-providers.live.test.ts
[/code]

Repo-Wrapper:

bashCopy code
[code]
    pnpm test:live:media music
[/code]

Diese Live-Datei lädt fehlende Provider-Umgebungsvariablen aus `~/.profile`, bevorzugt standardmäßig Live-/Env-API-Schlüssel vor gespeicherten Auth-Profilen und führt sowohl `generate` als auch die deklarierte `edit`-Abdeckung aus, wenn der Provider den Edit-Modus aktiviert. Aktuelle Abdeckung:

  * `google`: `generate` plus `edit`
  * `minimax`: nur `generate`
  * `comfy`: separate Comfy-Live-Abdeckung, nicht der gemeinsame Provider-Sweep


Live-Abdeckung für den mitgelieferten ComfyUI-Musikpfad aktivieren:

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 COMFY_LIVE_TEST=1 pnpm test:live -- extensions/comfy/comfy.live.test.ts
[/code]

Die Comfy-Live-Datei deckt auch Comfy-Bild- und -Videoworkflows ab, wenn diese Abschnitte konfiguriert sind.

## Verwandt

  * [Hintergrundaufgaben](</de/automation/tasks>) — Aufgabenverfolgung für abgetrennte `music_generate`-Ausführungen
  * [ComfyUI](</de/providers/comfy>)
  * [Konfigurationsreferenz](</de/gateway/config-agents#agent-defaults>) — `musicGenerationModel`-Konfiguration
  * [Google (Gemini)](</de/providers/google>)
  * [MiniMax](</de/providers/minimax>)
  * [Modelle](</de/concepts/models>) — Modellkonfiguration und Failover
  * [Tools-Übersicht](</de/tools>)


Was this useful?YesNo