---
title: Inferenz-CLI
source_url: https://docs.openclaw.ai/de/cli/infer
scraped_at: 2026-05-25
---

`openclaw infer` ist die kanonische Headless-Oberfläche für Provider-gestützte Inferenz-Workflows.

Es stellt absichtlich Capability-Familien bereit, nicht rohe Gateway-RPC-Namen und nicht rohe Agent-Tool-IDs.

## infer in einen Skill umwandeln

Kopieren Sie dies und fügen Sie es in einen Agenten ein:

textCopy code
[code]
    Read https://docs.openclaw.ai/cli/infer, then create a skill that routes my common workflows to `openclaw infer`.Focus on model runs, image generation, video generation, audio transcription, TTS, web search, and embeddings.
[/code]

Ein guter infer-basierter Skill sollte:

  * häufige Benutzerabsichten dem richtigen infer-Unterbefehl zuordnen
  * einige kanonische infer-Beispiele für die abgedeckten Workflows enthalten
  * in Beispielen und Vorschlägen `openclaw infer ...` bevorzugen
  * vermeiden, die gesamte infer-Oberfläche im Skill-Text erneut zu dokumentieren


Typische Abdeckung eines infer-fokussierten Skill:

  * `openclaw infer model run`
  * `openclaw infer image generate`
  * `openclaw infer audio transcribe`
  * `openclaw infer tts convert`
  * `openclaw infer web search`
  * `openclaw infer embedding create`


## Warum infer verwenden

`openclaw infer` bietet eine konsistente CLI für Provider-gestützte Inferenzaufgaben innerhalb von OpenClaw.

Vorteile:

  * Verwenden Sie die bereits in OpenClaw konfigurierten Provider und Modelle, anstatt einmalige Wrapper für jedes Backend einzurichten.
  * Halten Sie Workflows für Modell, Bild, Audiotranskription, TTS, Video, Web und Embedding unter einem Befehlsbaum.
  * Verwenden Sie eine stabile `--json`-Ausgabeform für Skripte, Automatisierung und Agent-gesteuerte Workflows.
  * Bevorzugen Sie eine OpenClaw-Erstanbieteroberfläche, wenn die Aufgabe im Kern „Inferenz ausführen“ lautet.
  * Verwenden Sie für die meisten infer-Befehle den normalen lokalen Pfad, ohne den Gateway zu benötigen.


Für End-to-End-Provider-Prüfungen sollten Sie `openclaw infer ...` bevorzugen, sobald Low-Level-Provider-Tests grün sind. Es prüft die ausgelieferte CLI, das Laden der Konfiguration, die Auflösung des Standard-Agenten, die Aktivierung gebündelter Plugins und die gemeinsame Capability-Laufzeit, bevor die Provider-Anfrage gestellt wird.

## Befehlsbaum

textCopy code
[code]
     openclaw infer  list  inspect   model    run    list    inspect    providers    auth login    auth logout    auth status   image    generate    edit    describe    describe-many    providers   audio    transcribe    providers   tts    convert    voices    providers    status    enable    disable    set-provider   video    generate    describe    providers   web    search    fetch    providers   embedding    create    providers
[/code]

## Häufige Aufgaben

Diese Tabelle ordnet häufige Inferenzaufgaben dem entsprechenden infer-Befehl zu.

Aufgabe | Befehl | Hinweise  
---|---|---  
Einen Text-/Modell-Prompt ausführen | `openclaw infer model run --prompt "..." --json` | Verwendet standardmäßig den normalen lokalen Pfad  
Einen Modell-Prompt mit Bildern ausführen | `openclaw infer model run --prompt "Describe this" --file ./image.png --model provider/model` | Wiederholen Sie `--file` für mehrere Bildeingaben  
Ein Bild generieren | `openclaw infer image generate --prompt "..." --json` | Verwenden Sie `image edit`, wenn Sie mit einer vorhandenen Datei beginnen  
Eine Bilddatei beschreiben | `openclaw infer image describe --file ./image.png --prompt "..." --json` | `--model` muss ein bildfähiges `<provider/model>` sein  
Audio transkribieren | `openclaw infer audio transcribe --file ./memo.m4a --json` | `--model` muss `<provider/model>` sein  
Sprache synthetisieren | `openclaw infer tts convert --text "..." --output ./speech.mp3 --json` | `tts status` ist Gateway-orientiert  
Ein Video generieren | `openclaw infer video generate --prompt "..." --json` | Unterstützt Provider-Hinweise wie `--resolution`  
Eine Videodatei beschreiben | `openclaw infer video describe --file ./clip.mp4 --json` | `--model` muss `<provider/model>` sein  
Das Web durchsuchen | `openclaw infer web search --query "..." --json` |   
Eine Webseite abrufen | `openclaw infer web fetch --url https://example.com --json` |   
Embeddings erstellen | `openclaw infer embedding create --text "..." --json` |   
  
## Verhalten

  * `openclaw infer ...` ist die primäre CLI-Oberfläche für diese Workflows.
  * Verwenden Sie `--json`, wenn die Ausgabe von einem anderen Befehl oder Skript verarbeitet wird.
  * Verwenden Sie `--provider` oder `--model provider/model`, wenn ein bestimmtes Backend erforderlich ist.
  * Verwenden Sie `model run --thinking <level>`, um eine einmalige Thinking-/Reasoning-Stufe (`off`, `minimal`, `low`, `medium`, `high`, `adaptive`, `xhigh` oder `max`) zu übergeben und den Lauf dabei roh zu halten.
  * Für `image describe`, `audio transcribe` und `video describe` muss `--model` die Form `<provider/model>` verwenden.
  * Für `image describe` führt ein explizites `--model` dieses Provider/Modell direkt aus. Das Modell muss im Modellkatalog oder in der Provider-Konfiguration bildfähig sein. `codex/<model>` führt einen begrenzten Bildverständnis-Turn des Codex-App-Servers aus; `openai-codex/<model>` verwendet den OAuth-Provider-Pfad von OpenAI Codex.
  * Zustandslose Ausführungsbefehle verwenden standardmäßig lokal.
  * Gateway-verwaltete Zustandsbefehle verwenden standardmäßig den Gateway.
  * Der normale lokale Pfad erfordert nicht, dass der Gateway läuft.
  * Lokales `model run` ist eine schlanke einmalige Provider-Completion. Es löst das konfigurierte Agentenmodell und die Authentifizierung auf, startet aber keinen Chat-Agent-Turn, lädt keine Tools und öffnet keine gebündelten MCP-Server.
  * `model run --file` akzeptiert Bilddateien, erkennt deren MIME-Typ und sendet sie mit dem angegebenen Prompt an das ausgewählte Modell. Wiederholen Sie `--file` für mehrere Bilder.
  * `model run --file` lehnt Nicht-Bildeingaben ab. Verwenden Sie `infer audio transcribe` für Audiodateien und `infer video describe` für Videodateien.
  * `model run --gateway` prüft Gateway-Routing, gespeicherte Authentifizierung, Provider-Auswahl und die eingebettete Laufzeit, läuft aber weiterhin als roher Modell-Probe: Es sendet den angegebenen Prompt und etwaige Bildanhänge ohne vorheriges Sitzungstranskript, Bootstrap-/AGENTS-Kontext, Context-Engine-Zusammenstellung, Tools oder gebündelte MCP-Server.
  * `model run --gateway --model <provider/model>` erfordert vertrauenswürdige Operator-Gateway-Anmeldedaten, da die Anfrage den Gateway auffordert, einen einmaligen Provider/Modell-Override auszuführen.
  * Lokales `model run --thinking` verwendet den schlanken Provider-Completion-Pfad; Provider-spezifische Stufen wie `adaptive` und `max` werden der nächstliegenden portablen Simple-Completion-Stufe zugeordnet.


## Modell

Verwenden Sie `model` für Provider-gestützte Textinferenz und Modell-/Provider-Inspektion.

bashCopy code
[code]
    openclaw infer model run --prompt "Reply with exactly: smoke-ok" --jsonopenclaw infer model run --prompt "Summarize this changelog entry" --model openai/gpt-5.4 --jsonopenclaw infer model run --prompt "Describe this image in one sentence" --file ./photo.jpg --model google/gemini-2.5-flash --jsonopenclaw infer model run --prompt "Use more reasoning here" --thinking high --jsonopenclaw infer model providers --jsonopenclaw infer model inspect --name gpt-5.5 --json
[/code]

Verwenden Sie vollständige `<provider/model>`-Referenzen, um einen bestimmten Provider per Smoke-Test zu prüfen, ohne den Gateway zu starten oder die vollständige Agent-Tool-Oberfläche zu laden:

bashCopy code
[code]
    openclaw infer model run --local --model anthropic/claude-sonnet-4-6 --prompt "Reply with exactly: pong" --jsonopenclaw infer model run --local --model cerebras/zai-glm-4.7 --prompt "Reply with exactly: pong" --jsonopenclaw infer model run --local --model google/gemini-2.5-flash --prompt "Reply with exactly: pong" --jsonopenclaw infer model run --local --model groq/llama-3.1-8b-instant --prompt "Reply with exactly: pong" --jsonopenclaw infer model run --local --model mistral/mistral-medium-3-5 --prompt "Reply with exactly: pong" --jsonopenclaw infer model run --local --model mistral/mistral-small-latest --prompt "Reply with exactly: pong" --jsonopenclaw infer model run --local --model openai/gpt-4.1 --prompt "Reply with exactly: pong" --jsonopenclaw infer model run --local --model ollama/qwen2.5vl:7b --prompt "Describe this image." --file ./photo.jpg --json
[/code]

Hinweise:

  * Lokales `model run` ist der engste CLI-Smoke-Test für Provider-/Modell-/Authentifizierungszustand, da es für Nicht-Codex-Provider nur den angegebenen Prompt an das ausgewählte Modell sendet.
  * Lokales `model run --model <provider/model>` kann exakte gebündelte statische Katalogzeilen aus `models list --all` verwenden, bevor dieser Provider in die Konfiguration geschrieben wurde. Provider-Authentifizierung ist weiterhin erforderlich; fehlende Anmeldedaten schlagen als Authentifizierungsfehler fehl, nicht als `Unknown model`.
  * Lassen Sie bei Reasoning-Probes für Mistral Medium 3.5 die Temperatur ungesetzt bzw. auf dem Standardwert. Mistral lehnt `reasoning_effort="high"` plus `temperature: 0` ab; verwenden Sie `mistral/mistral-medium-3-5` mit Standardtemperatur oder einem Reasoning-Modus-Wert ungleich null, etwa `0.7`.
  * Lokale `openai-codex/*`-Probes sind die enge Ausnahme: OpenClaw fügt eine minimale Systemanweisung hinzu, damit der Codex-Responses-Transport sein erforderliches `instructions`-Feld befüllen kann, ohne vollständigen Agentenkontext, Tools, Memory oder Sitzungstranskript hinzuzufügen.
  * Lokales `model run --file` behält diesen schlanken Pfad bei und hängt Bildinhalte direkt an die einzelne Benutzernachricht an. Gängige Bilddateien wie PNG, JPEG und WebP funktionieren, wenn ihr MIME-Typ als `image/*` erkannt wird; nicht unterstützte oder nicht erkannte Dateien schlagen fehl, bevor der Provider aufgerufen wird.
  * `model run --file` ist am besten geeignet, wenn Sie das ausgewählte multimodale Textmodell direkt testen möchten. Verwenden Sie `infer image describe`, wenn Sie OpenClaws Provider-Auswahl für Bildverständnis und das Standardrouting für Bildmodelle nutzen möchten.
  * Das ausgewählte Modell muss Bildeingaben unterstützen; reine Textmodelle können die Anfrage auf Provider-Ebene ablehnen.
  * `model run --prompt` muss Text enthalten, der nicht nur aus Leerraum besteht; leere Prompts werden abgelehnt, bevor lokale Provider oder der Gateway aufgerufen werden.
  * Lokales `model run` beendet sich mit einem Exitcode ungleich null, wenn der Provider keine Textausgabe zurückgibt, sodass nicht erreichbare lokale Provider und leere Completions nicht wie erfolgreiche Probes aussehen.
  * Verwenden Sie `model run --gateway`, wenn Sie Gateway-Routing, Agent-Laufzeit-Setup oder Gateway-verwalteten Provider-Zustand testen müssen, während die Modelleingabe roh bleibt. Verwenden Sie `openclaw agent` oder Chat-Oberflächen, wenn Sie den vollständigen Agentenkontext, Tools, Memory und Sitzungstranskript benötigen.
  * `model auth login`, `model auth logout` und `model auth status` verwalten den gespeicherten Provider-Authentifizierungszustand.


## Bild

Verwenden Sie `image` für Generierung, Bearbeitung und Beschreibung.

bashCopy code
[code]
    openclaw infer image generate --prompt "friendly lobster illustration" --jsonopenclaw infer image generate --prompt "cinematic product photo of headphones" --jsonopenclaw infer image generate --model openai/gpt-image-1.5 --output-format png --background transparent --prompt "simple red circle sticker on a transparent background" --jsonopenclaw infer image generate --prompt "slow image backend" --timeout-ms 180000 --jsonopenclaw infer image edit --file ./logo.png --model openai/gpt-image-1.5 --output-format png --background transparent --prompt "keep the logo, remove the background" --jsonopenclaw infer image edit --file ./poster.png --prompt "make this a vertical story ad" --size 2160x3840 --aspect-ratio 9:16 --resolution 4K --jsonopenclaw infer image describe --file ./photo.jpg --jsonopenclaw infer image describe --file ./receipt.jpg --prompt "Extract the merchant, date, and total" --jsonopenclaw infer image describe-many --file ./before.png --file ./after.png --prompt "Compare the screenshots and list visible UI changes" --jsonopenclaw infer image describe --file ./ui-screenshot.png --model openai/gpt-4.1-mini --jsonopenclaw infer image describe --file ./photo.jpg --model ollama/qwen2.5vl:7b --prompt "Describe the image in one sentence" --timeout-ms 300000 --json
[/code]

Hinweise:

  * Verwenden Sie `image edit`, wenn Sie mit vorhandenen Eingabedateien beginnen.

  * Verwenden Sie `--size`, `--aspect-ratio` oder `--resolution` mit `image edit` für Provider/Modelle, die Geometriehinweise bei Bearbeitungen von Referenzbildern unterstützen.

  * Verwenden Sie `--output-format png --background transparent` mit `--model openai/gpt-image-1.5` für OpenAI-PNG-Ausgaben mit transparentem Hintergrund; `--openai-background` bleibt als OpenAI-spezifischer Alias verfügbar. Provider, die keine Hintergrundunterstützung deklarieren, melden den Hinweis als ignorierte Überschreibung.

  * Verwenden Sie `image providers --json`, um zu prüfen, welche gebündelten Bild-Provider auffindbar, konfiguriert und ausgewählt sind und welche Generierungs-/Bearbeitungsfunktionen jeder Provider bereitstellt.

  * Verwenden Sie `image generate --model <provider/model> --json` als engsten Live- CLI-Smoke-Test für Änderungen an der Bildgenerierung. Beispiel:

bashCopy code
[code]openclaw infer image providers --jsonopenclaw infer image generate \  --model google/gemini-3.1-flash-image-preview \  --prompt "Minimal flat test image: one blue square on a white background, no text." \  --output ./openclaw-infer-image-smoke.png \  --json
[/code]

Die JSON-Antwort meldet `ok`, `provider`, `model`, `attempts` und geschriebene Ausgabepfade. Wenn `--output` gesetzt ist, kann die finale Erweiterung dem vom Provider zurückgegebenen MIME-Typ folgen.

  * Verwenden Sie für `image describe` und `image describe-many` `--prompt`, um dem Vision-Modell eine aufgabenspezifische Anweisung wie OCR, Vergleich, UI-Prüfung oder knappe Bildbeschreibung zu geben.

  * Verwenden Sie `--timeout-ms` bei langsamen lokalen Vision-Modellen oder Kaltstarts von Ollama.

  * Für `image describe` muss `--model` ein bildfähiges `<provider/model>` sein.

  * Für lokale Ollama-Vision-Modelle laden Sie zuerst das Modell herunter und setzen `OLLAMA_API_KEY` auf einen beliebigen Platzhalterwert, zum Beispiel `ollama-local`. Siehe [Ollama](</de/providers/ollama#vision-and-image-description>).


## Audio

Verwenden Sie `audio` für Dateitranskription.

bashCopy code
[code]
    openclaw infer audio transcribe --file ./memo.m4a --jsonopenclaw infer audio transcribe --file ./team-sync.m4a --language en --prompt "Focus on names and action items" --jsonopenclaw infer audio transcribe --file ./memo.m4a --model openai/whisper-1 --json
[/code]

Hinweise:

  * `audio transcribe` ist für Dateitranskription gedacht, nicht für die Verwaltung von Echtzeitsitzungen.
  * `--model` muss `<provider/model>` sein.


## TTS

Verwenden Sie `tts` für Sprachsynthese und den TTS-Provider-Status.

bashCopy code
[code]
    openclaw infer tts convert --text "hello from openclaw" --output ./hello.mp3 --jsonopenclaw infer tts convert --text "Your build is complete" --output ./build-complete.mp3 --jsonopenclaw infer tts providers --jsonopenclaw infer tts status --json
[/code]

Hinweise:

  * `tts status` verwendet standardmäßig den Gateway, weil der Befehl den vom Gateway verwalteten TTS-Status widerspiegelt.
  * Verwenden Sie `tts providers`, `tts voices` und `tts set-provider`, um TTS-Verhalten zu prüfen und zu konfigurieren.


## Video

Verwenden Sie `video` für Generierung und Beschreibung.

bashCopy code
[code]
    openclaw infer video generate --prompt "cinematic sunset over the ocean" --jsonopenclaw infer video generate --prompt "slow drone shot over a forest lake" --resolution 768P --duration 6 --jsonopenclaw infer video describe --file ./clip.mp4 --jsonopenclaw infer video describe --file ./clip.mp4 --model openai/gpt-4.1-mini --json
[/code]

Hinweise:

  * `video generate` akzeptiert `--size`, `--aspect-ratio`, `--resolution`, `--duration`, `--audio`, `--watermark` und `--timeout-ms` und leitet sie an die Laufzeit für Videogenerierung weiter.
  * `--model` muss für `video describe` `<provider/model>` sein.


## Web

Verwenden Sie `web` für Such- und Abrufworkflows.

bashCopy code
[code]
    openclaw infer web search --query "OpenClaw docs" --jsonopenclaw infer web search --query "OpenClaw infer web providers" --jsonopenclaw infer web fetch --url https://docs.openclaw.ai/cli/infer --jsonopenclaw infer web providers --json
[/code]

Hinweise:

  * Verwenden Sie `web providers`, um verfügbare, konfigurierte und ausgewählte Provider zu prüfen.


## Embedding

Verwenden Sie `embedding` für Vektorerstellung und Prüfung von Embedding-Providern.

bashCopy code
[code]
    openclaw infer embedding create --text "friendly lobster" --jsonopenclaw infer embedding create --text "customer support ticket: delayed shipment" --model openai/text-embedding-3-large --jsonopenclaw infer embedding providers --json
[/code]

## JSON-Ausgabe

Infer-Befehle normalisieren JSON-Ausgaben unter einer gemeinsamen Hülle:

jsonCopy code
[code]
    {  "ok": true,  "capability": "image.generate",  "transport": "local",  "provider": "openai",  "model": "gpt-image-2",  "attempts": [],  "outputs": []}
[/code]

Felder auf oberster Ebene sind stabil:

  * `ok`
  * `capability`
  * `transport`
  * `provider`
  * `model`
  * `attempts`
  * `outputs`
  * `error`


Für Befehle mit generierten Medien enthält `outputs` Dateien, die von OpenClaw geschrieben wurden. Verwenden Sie `path`, `mimeType`, `size` und alle medienspezifischen Abmessungen in diesem Array für Automatisierung, statt menschenlesbare Standardausgabe zu parsen.

## Häufige Fallstricke

bashCopy code
[code]
    # Badopenclaw infer media image generate --prompt "friendly lobster" # Goodopenclaw infer image generate --prompt "friendly lobster"
[/code]

bashCopy code
[code]
    # Badopenclaw infer audio transcribe --file ./memo.m4a --model whisper-1 --json # Goodopenclaw infer audio transcribe --file ./memo.m4a --model openai/whisper-1 --json
[/code]

## Hinweise

  * `openclaw capability ...` ist ein Alias für `openclaw infer ...`.


## Verwandte Themen

  * [CLI-Referenz](</de/cli>)
  * [Modelle](</de/concepts/models>)


Was this useful?YesNo