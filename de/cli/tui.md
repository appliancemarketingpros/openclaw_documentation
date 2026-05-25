---
title: TUI
source_url: https://docs.openclaw.ai/de/cli/tui
scraped_at: 2026-05-25
---

# `openclaw tui`

Öffnen Sie die mit dem Gateway verbundene Terminal-UI, oder führen Sie sie im lokalen eingebetteten Modus aus.

Siehe auch:

  * TUI-Leitfaden: [TUI](</de/web/tui>)


## Optionen

Flag | Standardwert | Beschreibung  
---|---|---  
`--local` | `false` | Gegen die lokale eingebettete Agent-Runtime statt gegen ein Gateway ausführen.  
`--url <url>` | `gateway.remote.url` aus der Konfiguration | Gateway-WebSocket-URL.  
`--token <token>` | (keiner) | Gateway-Token, falls erforderlich.  
`--password <pass>` | (keines) | Gateway-Passwort, falls erforderlich.  
`--session <key>` | `main` (oder `global`, wenn der Scope global ist) | Sitzungsschlüssel. Innerhalb eines Agent-Arbeitsbereichs wird dieser Agent automatisch ausgewählt, sofern kein Präfix angegeben ist.  
`--deliver` | `false` | Assistant-Antworten über konfigurierte Kanäle zustellen.  
`--thinking <level>` | (Modellstandardwert) | Überschreibung des Thinking-Levels.  
`--message <text>` | (keine) | Nach dem Verbinden eine anfängliche Nachricht senden.  
`--timeout-ms <ms>` | `agents.defaults.timeoutSeconds` | Agent-Timeout. Ungültige Werte protokollieren eine Warnung und werden ignoriert.  
`--history-limit <n>` | `200` | Verlaufseinträge, die beim Anhängen geladen werden.  
  
Aliasse: `openclaw chat` und `openclaw terminal` rufen denselben Befehl mit impliziertem `--local` auf.

Hinweise:

  * `chat` und `terminal` sind Aliasse für `openclaw tui --local`.
  * `--local` kann nicht mit `--url`, `--token` oder `--password` kombiniert werden.
  * `tui` löst konfigurierte Gateway-Auth-SecretRefs für Token-/Passwort-Auth nach Möglichkeit auf (`env`-/`file`-/`exec`-Provider).
  * Wenn TUI aus einem konfigurierten Agent-Arbeitsbereichsverzeichnis gestartet wird, wählt es diesen Agent automatisch als Standard für den Sitzungsschlüssel aus (sofern `--session` nicht explizit `agent:<id>:...` ist).
  * Der lokale Modus verwendet die eingebettete Agent-Runtime direkt. Die meisten lokalen Tools funktionieren, aber reine Gateway-Funktionen sind nicht verfügbar.
  * Der lokale Modus fügt `/auth [provider]` innerhalb der TUI-Befehlsoberfläche hinzu.
  * Plugin-Genehmigungs-Gates gelten weiterhin im lokalen Modus. Tools, die eine Genehmigung erfordern, fragen im Terminal nach einer Entscheidung; nichts wird stillschweigend automatisch genehmigt, nur weil das Gateway nicht beteiligt ist.


## Beispiele

bashCopy code
[code]
    openclaw chatopenclaw tui --localopenclaw tuiopenclaw tui --url ws://127.0.0.1:18789 --token <token>openclaw tui --session main --deliveropenclaw chat --message "Compare my config to the docs and tell me what to fix"# when run inside an agent workspace, infers that agent automaticallyopenclaw tui --session bugfix
[/code]

## Reparaturschleife für die Konfiguration

Verwenden Sie den lokalen Modus, wenn die aktuelle Konfiguration bereits validiert und Sie möchten, dass der eingebettete Agent sie prüft, mit der Dokumentation vergleicht und Ihnen hilft, sie aus demselben Terminal heraus zu reparieren:

Wenn `openclaw config validate` bereits fehlschlägt, verwenden Sie zuerst `openclaw configure` oder `openclaw doctor --fix`. `openclaw chat` umgeht den Schutz vor ungültiger Konfiguration nicht.

bashCopy code
[code]
    openclaw chat
[/code]

Dann innerhalb der TUI:

textCopy code
[code]
    !openclaw config file!openclaw docs gateway auth token secretref!openclaw config validate!openclaw doctor
[/code]

Wenden Sie gezielte Korrekturen mit `openclaw config set` oder `openclaw configure` an, und führen Sie anschließend `openclaw config validate` erneut aus. Siehe [TUI](</de/web/tui>) und [Konfiguration](</de/cli/config>).

## Siehe auch

  * [CLI-Referenz](</de/cli>)
  * [TUI](</de/web/tui>)


Was this useful?YesNo