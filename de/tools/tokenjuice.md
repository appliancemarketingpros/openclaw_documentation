---
title: Tokenjuice
source_url: https://docs.openclaw.ai/de/tools/tokenjuice
scraped_at: 2026-05-25
---

`tokenjuice` ist ein optionales gebündeltes Plugin, das verrauschte `exec`\- und `bash`\- Tool-Ergebnisse komprimiert, nachdem der Befehl bereits ausgeführt wurde.

Es verändert das zurückgegebene `tool_result`, nicht den Befehl selbst. Tokenjuice schreibt keine Shell-Eingaben um, führt keine Befehle erneut aus und ändert keine Exit-Codes.

Derzeit gilt dies für eingebettete PI-Ausführungen und dynamische OpenClaw-Tools im Codex- App-Server-Harness. Tokenjuice klinkt sich in OpenClaws Tool-Result-Middleware ein und kürzt die Ausgabe, bevor sie in die aktive Harness-Sitzung zurückgegeben wird.

## Plugin aktivieren

Schnellster Weg:

bashCopy code
[code]
    openclaw config set plugins.entries.tokenjuice.enabled true
[/code]

Äquivalent:

bashCopy code
[code]
    openclaw plugins enable tokenjuice
[/code]

OpenClaw liefert das Plugin bereits mit. Es gibt keinen separaten Schritt `plugins install` oder `tokenjuice install openclaw`.

Wenn Sie die Konfiguration lieber direkt bearbeiten möchten:

json5Copy code
[code]
    {  plugins: {    entries: {      tokenjuice: {        enabled: true,      },    },  },}
[/code]

## Was Tokenjuice verändert

  * Komprimiert verrauschte `exec`\- und `bash`-Ergebnisse, bevor sie in die Sitzung zurückgeführt werden.
  * Lässt die ursprüngliche Befehlsausführung unverändert.
  * Bewahrt exakte Dateiinhalts-Lesevorgänge und andere Befehle, die Tokenjuice unbearbeitet lassen soll.
  * Bleibt optional: Deaktivieren Sie das Plugin, wenn Sie überall wortgetreue Ausgabe möchten.


## Verifizieren, dass es funktioniert

  1. Aktivieren Sie das Plugin.
  2. Starten Sie eine Sitzung, die `exec` aufrufen kann.
  3. Führen Sie einen verrauschten Befehl wie `git status` aus.
  4. Prüfen Sie, dass das zurückgegebene Tool-Ergebnis kürzer und strukturierter ist als die rohe Shell-Ausgabe.


## Plugin deaktivieren

bashCopy code
[code]
    openclaw config set plugins.entries.tokenjuice.enabled false
[/code]

Oder:

bashCopy code
[code]
    openclaw plugins disable tokenjuice
[/code]

## Verwandt

  * [Exec tool](</de/tools/exec>)
  * [Thinking levels](</de/tools/thinking>)
  * [Context engine](</de/concepts/context-engine>)


Was this useful?YesNo