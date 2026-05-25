---
title: Debuggen
source_url: https://docs.openclaw.ai/de/help/debugging
scraped_at: 2026-05-25
---

Debugging-Hilfen für Streaming-Ausgabe, insbesondere wenn ein Provider Reasoning in normalen Text mischt.

## Runtime-Debug-Overrides

Verwenden Sie `/debug` im Chat, um **nur zur Laufzeit** geltende Konfigurations-Overrides festzulegen (Speicher, nicht Datenträger). `/debug` ist standardmäßig deaktiviert; aktivieren Sie es mit `commands.debug: true`. Das ist praktisch, wenn Sie seltene Einstellungen umschalten müssen, ohne `openclaw.json` zu bearbeiten.

Beispiele:

CodeCopy code
[code]
    /debug show/debug set messages.responsePrefix="[openclaw]"/debug unset messages.responsePrefix/debug reset
[/code]

`/debug reset` löscht alle Overrides und kehrt zur Konfiguration auf dem Datenträger zurück.

## Session-Trace-Ausgabe

Verwenden Sie `/trace`, wenn Sie Plugin-eigene Trace-/Debug-Zeilen in einer Session sehen möchten, ohne den vollständigen ausführlichen Modus zu aktivieren.

Beispiele:

textCopy code
[code]
    /trace/trace on/trace off
[/code]

Verwenden Sie `/trace` für Plugin-Diagnosen wie Active Memory-Debug-Zusammenfassungen. Verwenden Sie weiterhin `/verbose` für normale ausführliche Status-/Tool-Ausgabe und weiterhin `/debug` für nur zur Laufzeit geltende Konfigurations-Overrides.

## Plugin-Lifecycle-Trace

Verwenden Sie `OPENCLAW_PLUGIN_LIFECYCLE_TRACE=1`, wenn Plugin-Lifecycle-Befehle langsam wirken und Sie eine eingebaute Phasenaufschlüsselung für Plugin-Metadaten, Discovery, Registry, Runtime-Mirror, Konfigurationsmutation und Aktualisierungsarbeit benötigen. Der Trace ist opt-in und schreibt nach stderr, sodass JSON-Befehlsausgaben parsebar bleiben.

Beispiel:

bashCopy code
[code]
    OPENCLAW_PLUGIN_LIFECYCLE_TRACE=1 openclaw plugins install tokenjuice --force
[/code]

Beispielausgabe:

textCopy code
[code]
    [plugins:lifecycle] phase="config read" ms=6.83 status=ok command="install"[plugins:lifecycle] phase="slot selection" ms=94.31 status=ok command="install" pluginId="tokenjuice"[plugins:lifecycle] phase="registry refresh" ms=51.56 status=ok command="install" reason="source-changed"
[/code]

Verwenden Sie dies für Untersuchungen des Plugin-Lifecycles, bevor Sie zu einem CPU-Profiler greifen. Wenn der Befehl aus einem Source-Checkout ausgeführt wird, sollten Sie nach `pnpm build` bevorzugt die gebaute Runtime mit `node dist/entry.js ...` messen; `pnpm openclaw ...` misst auch den Overhead des Source-Runners.

## CLI-Start und Befehls-Profiling

Verwenden Sie den eingecheckten Start-Benchmark, wenn sich ein Befehl langsam anfühlt:

bashCopy code
[code]
    pnpm test:startup:bench:smokepnpm tsx scripts/bench-cli-startup.ts --preset real --case status --runs 3pnpm tsx scripts/bench-cli-startup.ts --preset real --cpu-prof-dir .artifacts/cli-cpu
[/code]

Für einmaliges Profiling über den normalen Source-Runner setzen Sie `OPENCLAW_RUN_NODE_CPU_PROF_DIR`:

bashCopy code
[code]
    OPENCLAW_RUN_NODE_CPU_PROF_DIR=.artifacts/cli-cpu pnpm openclaw status
[/code]

Der Source-Runner fügt Node-CPU-Profil-Flags hinzu und schreibt eine `.cpuprofile` für den Befehl. Verwenden Sie dies, bevor Sie temporäre Instrumentierung zum Befehls-Code hinzufügen.

Bei Start-Hängern, die nach synchronem Dateisystem- oder Module-Loader-Verhalten aussehen, fügen Sie das Sync-I/O-Trace-Flag von Node über den Source-Runner hinzu:

bashCopy code
[code]
    OPENCLAW_TRACE_SYNC_IO=1 pnpm openclaw gateway --force
[/code]

`pnpm gateway:watch` lässt dieses Flag standardmäßig für das überwachte Gateway-Kind deaktiviert. Setzen Sie `OPENCLAW_TRACE_SYNC_IO=1`, wenn Sie im Watch-Modus ausdrücklich Node-Sync-I/O-Trace-Ausgabe möchten.

## Gateway-Watch-Modus

Für schnelle Iteration führen Sie den Gateway unter dem Datei-Watcher aus:

bashCopy code
[code]
    pnpm gateway:watch
[/code]

Standardmäßig startet oder startet dies eine tmux-Session namens `openclaw-gateway-watch-main` neu (oder eine profil-/portspezifische Variante wie `openclaw-gateway-watch-dev-19001`) und verbindet interaktive Terminals automatisch. Nicht interaktive Shells, CI und Agent-Exec-Aufrufe bleiben getrennt und geben stattdessen Anweisungen zum Verbinden aus. Verbinden Sie sich bei Bedarf manuell:

bashCopy code
[code]
    tmux attach -t openclaw-gateway-watch-main
[/code]

Der tmux-Bereich führt den rohen Watcher aus:

bashCopy code
[code]
    node scripts/watch-node.mjs gateway --force
[/code]

Verwenden Sie den Vordergrundmodus, wenn tmux nicht gewünscht ist:

bashCopy code
[code]
    pnpm gateway:watch:raw# orOPENCLAW_GATEWAY_WATCH_TMUX=0 pnpm gateway:watch
[/code]

Deaktivieren Sie das automatische Verbinden, behalten Sie aber die tmux-Verwaltung bei:

bashCopy code
[code]
    OPENCLAW_GATEWAY_WATCH_ATTACH=0 pnpm gateway:watch
[/code]

Profilieren Sie die CPU-Zeit des überwachten Gateway, wenn Sie Start-/Runtime-Hotspots debuggen:

bashCopy code
[code]
    pnpm gateway:watch --benchmark
[/code]

Der Watch-Wrapper verarbeitet `--benchmark`, bevor er den Gateway aufruft, und schreibt pro Beenden eines Gateway-Kindprozesses eine V8-`.cpuprofile` unter `.artifacts/gateway-watch-profiles/`. Stoppen oder starten Sie den überwachten Gateway neu, um das aktuelle Profil zu flushen, und öffnen Sie es dann mit Chrome DevTools oder Speedscope:

bashCopy code
[code]
    npx speedscope .artifacts/gateway-watch-profiles/*.cpuprofile
[/code]

Verwenden Sie `--benchmark-dir <path>`, wenn Sie Profile an einem anderen Ort möchten. Verwenden Sie `--benchmark-no-force`, wenn das benchmarkte Kind die standardmäßige `--force`-Portbereinigung überspringen und schnell fehlschlagen soll, falls der Gateway-Port bereits belegt ist. Der Benchmark-Modus unterdrückt Sync-I/O-Trace-Spam standardmäßig. Setzen Sie `OPENCLAW_TRACE_SYNC_IO=1` mit `--benchmark`, wenn Sie ausdrücklich sowohl CPU-Profile als auch Node-Sync-I/O-Stack-Traces möchten. Im Benchmark-Modus werden diese Trace-Blöcke unter dem Benchmark-Verzeichnis nach `gateway-watch-output.log` geschrieben und aus dem Terminalbereich herausgefiltert; normale Gateway-Logs bleiben sichtbar.

Der tmux-Wrapper übernimmt gängige nicht geheime Runtime-Selektoren wie `OPENCLAW_PROFILE`, `OPENCLAW_CONFIG_PATH`, `OPENCLAW_STATE_DIR`, `OPENCLAW_GATEWAY_PORT` und `OPENCLAW_SKIP_CHANNELS` in den Bereich. Legen Sie Provider-Zugangsdaten in Ihrem normalen Profil/Ihrer normalen Konfiguration ab, oder verwenden Sie den rohen Vordergrundmodus für einmalige flüchtige Secrets. Wenn der überwachte Gateway während des Starts beendet wird, führt der Watcher einmal `openclaw doctor --fix --non-interactive` aus und startet das Gateway-Kind neu. Verwenden Sie `OPENCLAW_GATEWAY_WATCH_AUTO_DOCTOR=0`, wenn Sie den ursprünglichen Startfehler ohne den nur für die Entwicklung vorgesehenen Reparaturdurchlauf möchten. Der verwaltete tmux-Bereich verwendet außerdem standardmäßig farbige Gateway-Logs für bessere Lesbarkeit; setzen Sie `FORCE_COLOR=0`, wenn Sie `pnpm gateway:watch` starten, um ANSI-Ausgabe zu deaktivieren.

Der Watcher startet bei buildrelevanten Dateien unter `src/`, Plugin-Quelldateien, Plugin-`package.json`\- und `openclaw.plugin.json`-Metadaten, `tsconfig.json`, `package.json` und `tsdown.config.ts` neu. Änderungen an Plugin-Metadaten starten den Gateway neu, ohne einen `tsdown`-Rebuild zu erzwingen; Quell- und Konfigurationsänderungen bauen weiterhin zuerst `dist` neu.

Fügen Sie Gateway-CLI-Flags nach `gateway:watch` hinzu; sie werden bei jedem Neustart durchgereicht. Das erneute Ausführen desselben Watch-Befehls startet den benannten tmux-Bereich neu, und der rohe Watcher behält weiterhin seine Single-Watcher-Sperre bei, sodass doppelte Watcher-Eltern ersetzt werden, statt sich anzuhäufen.

## Dev-Profil + Dev-Gateway (`--dev`)

Verwenden Sie das Dev-Profil, um Zustand zu isolieren und eine sichere, wegwerfbare Einrichtung zum Debuggen zu starten. Es gibt **zwei** `--dev`-Flags:

  * **Globales`--dev` (Profil):** isoliert den Zustand unter `~/.openclaw-dev` und setzt den Gateway-Port standardmäßig auf `19001` (abgeleitete Ports verschieben sich entsprechend).
  * **`gateway --dev`: weist den Gateway an, bei Bedarf eine Standardkonfiguration + einen Workspace automatisch zu erstellen** (und [BOOTSTRAP.md](<http://BOOTSTRAP.md>) zu überspringen).


Empfohlener Ablauf (Dev-Profil + Dev-Bootstrap):

bashCopy code
[code]
    pnpm gateway:devOPENCLAW_PROFILE=dev openclaw tui
[/code]

Wenn Sie noch keine globale Installation haben, führen Sie die CLI über `pnpm openclaw ...` aus.

Was dies bewirkt:

  1. **Profilisolation** (globales `--dev`)

     * `OPENCLAW_PROFILE=dev`
     * `OPENCLAW_STATE_DIR=~/.openclaw-dev`
     * `OPENCLAW_CONFIG_PATH=~/.openclaw-dev/openclaw.json`
     * `OPENCLAW_GATEWAY_PORT=19001` (Browser/Canvas verschieben sich entsprechend)
  2. **Dev-Bootstrap** (`gateway --dev`)

     * Schreibt eine minimale Konfiguration, falls sie fehlt (`gateway.mode=local`, bindet Loopback).
     * Setzt `agent.workspace` auf den Dev-Workspace.
     * Setzt `agent.skipBootstrap=true` (kein [BOOTSTRAP.md](<http://BOOTSTRAP.md>)).
     * Legt die Workspace-Dateien an, falls sie fehlen: `AGENTS.md`, `SOUL.md`, `TOOLS.md`, `IDENTITY.md`, `USER.md`, `HEARTBEAT.md`.
     * Standardidentität: **C3-PO** (Protokolldroide).
     * Überspringt Channel-Provider im Dev-Modus (`OPENCLAW_SKIP_CHANNELS=1`).


Reset-Ablauf (frischer Start):

bashCopy code
[code]
    pnpm gateway:dev:reset
[/code]

`--reset` löscht Konfiguration, Zugangsdaten, Sessions und den Dev-Workspace (mit `trash`, nicht `rm`) und erstellt anschließend die Standard-Dev-Einrichtung neu.

## Rohstream-Protokollierung (OpenClaw)

OpenClaw kann den **rohen Assistenten-Stream** vor jeder Filterung/Formatierung protokollieren. Dies ist der beste Weg, um zu sehen, ob Reasoning als Plain-Text-Deltas ankommt (oder als separate Thinking-Blöcke).

Aktivieren Sie dies über die CLI:

bashCopy code
[code]
    pnpm gateway:watch --raw-stream
[/code]

Optionaler Pfad-Override:

bashCopy code
[code]
    pnpm gateway:watch --raw-stream --raw-stream-path ~/.openclaw/logs/raw-stream.jsonl
[/code]

Äquivalente Env-Vars:

bashCopy code
[code]
    OPENCLAW_RAW_STREAM=1OPENCLAW_RAW_STREAM_PATH=~/.openclaw/logs/raw-stream.jsonl
[/code]

Standarddatei:

`~/.openclaw/logs/raw-stream.jsonl`

## Raw-Chunk-Protokollierung (pi-mono)

Um **rohe OpenAI-kompatible Chunks** zu erfassen, bevor sie in Blöcke geparst werden, stellt pi-mono einen separaten Logger bereit:

bashCopy code
[code]
    PI_RAW_STREAM=1
[/code]

Optionaler Pfad:

bashCopy code
[code]
    PI_RAW_STREAM_PATH=~/.pi-mono/logs/raw-openai-completions.jsonl
[/code]

Standarddatei:

`~/.pi-mono/logs/raw-openai-completions.jsonl`

> Hinweis: Dies wird nur von Prozessen ausgegeben, die den `openai-completions`-Provider von pi-mono verwenden.

## Sicherheitshinweise

  * Rohstream-Logs können vollständige Prompts, Tool-Ausgabe und Benutzerdaten enthalten.
  * Bewahren Sie Logs lokal auf und löschen Sie sie nach dem Debuggen.
  * Wenn Sie Logs teilen, entfernen Sie zuerst Secrets und personenbezogene Daten.


## Debugging in VSCode

Source Maps sind erforderlich, um Debugging in VSCode-basierten IDEs zu ermöglichen, weil viele der generierten Dateien im Rahmen des Build-Prozesses gehashte Namen erhalten. Die enthaltenen `launch.json`-Konfigurationen zielen auf den Gateway-Dienst, können aber schnell für andere Zwecke angepasst werden:

  1. **Gateway neu bauen und debuggen** \- Debuggt den Gateway-Dienst nach dem Erstellen eines neuen Builds
  2. **Gateway debuggen** \- Debuggt den Gateway-Dienst eines bereits vorhandenen Builds


### Einrichtung

Die Standardkonfiguration **Gateway neu bauen und debuggen** ist sofort einsatzbereit; sie löscht automatisch den Ordner `/dist` und baut das Projekt mit aktiviertem Debugging neu:

  1. Öffnen Sie das Panel **Run and Debug** aus der Activity Bar oder drücken Sie `Ctrl`+`Shift`+`D`
  2. Stellen Sie in der IDE sicher, dass **Gateway neu bauen und debuggen** im Konfigurations-Dropdown ausgewählt ist, und drücken Sie dann die Schaltfläche **Start Debugging**


Alternativ, wenn Sie Build- und Debug-Prozesse lieber manuell verwalten:

  1. Öffnen Sie ein Terminal und aktivieren Sie Source Maps: 
     * **Linux/macOS** : `export OUTPUT_SOURCE_MAPS=1`
     * **Windows (PowerShell)** : `$env:OUTPUT_SOURCE_MAPS="1"`
     * **Windows (CMD)** : `set OUTPUT_SOURCE_MAPS=1`
  2. Bauen Sie das Projekt im selben Terminal neu: `pnpm clean:dist && pnpm build`
  3. Wählen Sie in der IDE die Option **Gateway debuggen** im Konfigurations-Dropdown **Run and Debug** aus und drücken Sie dann die Schaltfläche **Start Debugging**


Sie können nun Breakpoints in Ihren TypeScript-Quelldateien (Verzeichnis `src/`) setzen, und der Debugger ordnet Breakpoints über Source Maps korrekt dem kompilierten JavaScript zu. Sie können Variablen inspizieren, Code schrittweise ausführen und Call Stacks wie erwartet untersuchen.

### Hinweise

  * Wenn Sie die Option **"Gateway neu bauen und debuggen"** verwenden, wird bei jedem Start des Debuggers der Ordner `/dist` vollständig gelöscht und vor dem Start des Gateway ein vollständiger `pnpm build` mit aktivierten Source Maps ausgeführt
  * Wenn Sie die Option **"Gateway debuggen"** verwenden, können Debug-Sessions jederzeit gestartet und gestoppt werden, ohne den Ordner `/dist` zu beeinflussen, aber Sie müssen einen separaten Terminalprozess verwenden, um sowohl Debugging zu aktivieren als auch den Build-Zyklus zu verwalten
  * Ändern Sie die `launch.json`-Einstellungen für `args`, um andere Bereiche des Projekts zu debuggen
  * Wenn Sie die gebaute OpenClaw-CLI für andere Aufgaben verwenden müssen (z. B. `dashboard --no-open`, falls Ihre Debug-Session ein neues Auth-Token erzeugt), können Sie sie in einem anderen Terminal als `node ./openclaw.mjs` ausführen oder einen Shell-Alias wie `alias openclaw-build="node $(pwd)/openclaw.mjs"` erstellen


## Verwandte Themen

  * [Fehlerbehebung](</de/help/troubleshooting>)
  * [FAQ](</de/help/faq>)


Was this useful?YesNo