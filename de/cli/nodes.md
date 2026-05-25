---
title: Nodes
source_url: https://docs.openclaw.ai/de/cli/nodes
scraped_at: 2026-05-25
---

# `openclaw nodes`

Verwalten Sie gekoppelte Nodes (Geräte) und rufen Sie Node-Funktionen auf.

Verwandt:

  * Nodes-Übersicht: [Nodes](</de/nodes>)
  * Kamera: [Kamera-Nodes](</de/nodes/camera>)
  * Bilder: [Bild-Nodes](</de/nodes/images>)


Allgemeine Optionen:

  * `--url`, `--token`, `--timeout`, `--json`


## Häufige Befehle

bashCopy code
[code]
    openclaw nodes listopenclaw nodes list --connectedopenclaw nodes list --last-connected 24hopenclaw nodes pendingopenclaw nodes approve <requestId>openclaw nodes reject <requestId>openclaw nodes remove --node <id|name|ip>openclaw nodes rename --node <id|name|ip> --name <displayName>openclaw nodes statusopenclaw nodes status --connectedopenclaw nodes status --last-connected 24h
[/code]

`nodes list` gibt Tabellen mit ausstehenden/gekoppelten Einträgen aus. Gekoppelte Zeilen enthalten das Alter der letzten Verbindung (`Last Connect`). Verwenden Sie `--connected`, um nur aktuell verbundene Nodes anzuzeigen. Verwenden Sie `--last-connected <duration>`, um auf Nodes zu filtern, die sich innerhalb einer Dauer verbunden haben (z. B. `24h`, `7d`). Verwenden Sie `nodes remove --node <id|name|ip>`, um einen veralteten, Gateway-eigenen Node-Kopplungsdatensatz zu löschen.

Hinweis zur Genehmigung:

  * `openclaw nodes pending` benötigt nur den Pairing-Scope.
  * `gateway.nodes.pairing.autoApproveCidrs` kann den ausstehenden Schritt nur für ausdrücklich vertrauenswürdige, erstmalige Gerätekopplungen mit `role: node` überspringen. Es ist standardmäßig deaktiviert und genehmigt keine Upgrades.
  * `openclaw nodes approve <requestId>` übernimmt zusätzliche Scope-Anforderungen aus der ausstehenden Anfrage: 
    * Anfrage ohne Befehl: nur Pairing
    * Node-Befehle ohne Ausführung: Pairing + Schreibzugriff
    * `system.run` / `system.run.prepare` / `system.which`: Pairing + Admin


## Aufrufen

bashCopy code
[code]
    openclaw nodes invoke --node <id|name|ip> --command <command> --params <json>
[/code]

Aufruf-Flags:

  * `--params <json>`: JSON-Objektzeichenfolge (Standard `{}`).
  * `--invoke-timeout <ms>`: Timeout für Node-Aufrufe (Standard `15000`).
  * `--idempotency-key <key>`: optionaler Idempotenzschlüssel.
  * `system.run` und `system.run.prepare` werden hier blockiert; verwenden Sie das `exec`-Tool mit `host=node` für Shell-Ausführung.


Für Shell-Ausführung auf einer Node verwenden Sie das `exec`-Tool mit `host=node` statt `openclaw nodes run`. Die `nodes`-CLI ist jetzt auf Funktionen ausgerichtet: direkte RPC über `nodes invoke` sowie Pairing, Kamera, Bildschirm, Standort, Canvas und Benachrichtigungen. Canvas-Befehle werden durch das gebündelte experimentelle Canvas-Plugin implementiert; der Core behält einen Kompatibilitäts-Hook bei, damit sie weiterhin unter `openclaw nodes canvas` verfügbar bleiben.

## Verwandt

  * [CLI-Referenz](</de/cli>)
  * [Nodes](</de/nodes>)


Was this useful?YesNo