---
title: Completion
source_url: https://docs.openclaw.ai/de/cli/completion
scraped_at: 2026-05-25
---

# `openclaw completion`

Generieren Sie Shell-Completion-Skripte und installieren Sie sie optional in Ihr Shell-Profil.

## Verwendung

bashCopy code
[code]
    openclaw completionopenclaw completion --shell zshopenclaw completion --installopenclaw completion --shell fish --installopenclaw completion --write-stateopenclaw completion --shell bash --write-state
[/code]

## Optionen

  * `-s, --shell <shell>`: Shell-Ziel (`zsh`, `bash`, `powershell`, `fish`; Standard: `zsh`)
  * `-i, --install`: Completion installieren, indem eine `source`-Zeile zu Ihrem Shell-Profil hinzugefügt wird
  * `--write-state`: Completion-Skript(e) nach `$OPENCLAW_STATE_DIR/completions` schreiben, ohne sie auf stdout auszugeben
  * `-y, --yes`: Bestätigungsabfragen für die Installation überspringen


## Hinweise

  * `--install` schreibt einen kleinen Block „OpenClaw Completion“ in Ihr Shell-Profil und verweist dabei auf das zwischengespeicherte Skript.
  * Ohne `--install` oder `--write-state` gibt der Befehl das Skript auf stdout aus.
  * Die Generierung von Completions lädt Befehlsbäume frühzeitig, damit verschachtelte Unterbefehle enthalten sind.


## Verwandt

  * [CLI-Referenz](</de/cli>)


Was this useful?YesNo