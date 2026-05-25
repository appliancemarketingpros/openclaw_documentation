---
title: Reset
source_url: https://docs.openclaw.ai/de/cli/reset
scraped_at: 2026-05-25
---

# `openclaw reset`

Lokale Konfiguration/Status zurücksetzen (die CLI bleibt installiert).

Optionen:

  * `--scope <scope>`: `config`, `config+creds+sessions` oder `full`
  * `--yes`: Bestätigungsabfragen überspringen
  * `--non-interactive`: Eingabeaufforderungen deaktivieren; erfordert `--scope` und `--yes`
  * `--dry-run`: Aktionen ausgeben, ohne Dateien zu entfernen


Beispiele:

bashCopy code
[code]
    openclaw backup createopenclaw resetopenclaw reset --dry-runopenclaw reset --scope config --yes --non-interactiveopenclaw reset --scope config+creds+sessions --yes --non-interactiveopenclaw reset --scope full --yes --non-interactive
[/code]

Hinweise:

  * Führen Sie zuerst `openclaw backup create` aus, wenn Sie vor dem Entfernen des lokalen Status einen wiederherstellbaren Snapshot möchten.
  * Wenn Sie `--scope` weglassen, verwendet `openclaw reset` eine interaktive Eingabeaufforderung, um auszuwählen, was entfernt werden soll.
  * `--non-interactive` ist nur gültig, wenn sowohl `--scope` als auch `--yes` gesetzt sind.


## Verwandt

  * [CLI-Referenz](</de/cli>)


Was this useful?YesNo