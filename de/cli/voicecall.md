---
title: Sprachanruf
source_url: https://docs.openclaw.ai/de/cli/voicecall
scraped_at: 2026-05-25
---

# `openclaw voicecall`

`voicecall` ist ein von einem Plugin bereitgestellter Befehl. Er erscheint nur, wenn das Voice-Call-Plugin installiert und aktiviert ist.

Wenn der Gateway ausgeführt wird, werden Betriebsbefehle (`call`, `start`, `continue`, `speak`, `dtmf`, `end`, `status`) an die Voice-Call-Runtime dieses Gateway weitergeleitet. Wenn kein Gateway erreichbar ist, greifen sie auf eine eigenständige CLI-Runtime zurück.

## Unterbefehle

bashCopy code
[code]
    openclaw voicecall setup    [--json]openclaw voicecall smoke    [-t <phone>] [--message <text>] [--mode <m>] [--yes] [--json]openclaw voicecall call     -m <text> [-t <phone>] [--mode <m>]openclaw voicecall start    --to <phone> [--message <text>] [--mode <m>]openclaw voicecall continue --call-id <id> --message <text>openclaw voicecall speak    --call-id <id> --message <text>openclaw voicecall dtmf     --call-id <id> --digits <digits>openclaw voicecall end      --call-id <id>openclaw voicecall status   [--call-id <id>] [--json]openclaw voicecall tail     [--file <path>] [--since <n>] [--poll <ms>]openclaw voicecall latency  [--file <path>] [--last <n>]openclaw voicecall expose   [--mode <m>] [--path <p>] [--port <port>] [--serve-path <p>]
[/code]

Unterbefehl | Beschreibung  
---|---  
`setup` | Zeigt Bereitschaftsprüfungen für Provider und Webhook an.  
`smoke` | Führt Bereitschaftsprüfungen aus; startet einen Live-Testanruf nur mit `--yes`.  
`call` | Startet einen ausgehenden Sprachanruf.  
`start` | Alias für `call`, wobei `--to` erforderlich und `--message` optional ist.  
`continue` | Spricht eine Nachricht und wartet auf die nächste Antwort.  
`speak` | Spricht eine Nachricht, ohne auf eine Antwort zu warten.  
`dtmf` | Sendet DTMF-Ziffern an einen aktiven Anruf.  
`end` | Beendet einen aktiven Anruf.  
`status` | Prüft aktive Anrufe (oder einen per `--call-id`).  
`tail` | Verfolgt `calls.jsonl` fortlaufend (nützlich bei Provider-Tests).  
`latency` | Fasst Turn-Latenzmetriken aus `calls.jsonl` zusammen.  
`expose` | Schaltet Tailscale Serve/Funnel für den Webhook-Endpunkt um.  
  
## Einrichtung und Smoke-Test

### `setup`

Gibt standardmäßig menschenlesbare Bereitschaftsprüfungen aus. Übergeben Sie `--json` für Skripte.

bashCopy code
[code]
    openclaw voicecall setupopenclaw voicecall setup --json
[/code]

### `smoke`

Führt dieselben Bereitschaftsprüfungen aus. Es wird kein echter Telefonanruf gestartet, außer `--to` und `--yes` sind beide vorhanden.

Flag | Standardwert | Beschreibung  
---|---|---  
`-t, --to <phone>` | (keiner) | Telefonnummer für einen Live-Smoke-Test.  
`--message <text>` | `OpenClaw voice call smoke test.` | Nachricht, die während des Smoke-Anrufs gesprochen wird.  
`--mode <mode>` | `notify` | Anrufmodus: `notify` oder `conversation`.  
`--yes` | `false` | Startet den ausgehenden Live-Anruf wirklich.  
`--json` | `false` | Gibt maschinenlesbares JSON aus.  
bashCopy code
[code]
    openclaw voicecall smokeopenclaw voicecall smoke --to "+15555550123"        # dry runopenclaw voicecall smoke --to "+15555550123" --yes  # live notify call
[/code]

## Anruflebenszyklus

### `call`

Startet einen ausgehenden Sprachanruf.

Flag | Erforderlich | Standardwert | Beschreibung  
---|---|---|---  
`-m, --message <text>` | ja | (keiner) | Nachricht, die gesprochen wird, wenn der Anruf verbunden ist.  
`-t, --to <phone>` | nein | config `toNumber` | Telefonnummer im E.164-Format, die angerufen werden soll.  
`--mode <mode>` | nein | `conversation` | Anrufmodus: `notify` (nach der Nachricht auflegen) oder `conversation` (offen bleiben).  
bashCopy code
[code]
    openclaw voicecall call --to "+15555550123" --message "Hello"openclaw voicecall call -m "Heads up" --mode notify
[/code]

### `start`

Alias für `call` mit einer anderen Standard-Flag-Form.

Flag | Erforderlich | Standardwert | Beschreibung  
---|---|---|---  
`--to <phone>` | ja | (keiner) | Telefonnummer, die angerufen werden soll.  
`--message <text>` | nein | (keiner) | Nachricht, die gesprochen wird, wenn der Anruf verbunden ist.  
`--mode <mode>` | nein | `conversation` | Anrufmodus: `notify` oder `conversation`.  
  
### `continue`

Spricht eine Nachricht und wartet auf eine Antwort.

Flag | Erforderlich | Beschreibung  
---|---|---  
`--call-id <id>` | ja | Anruf-ID.  
`--message <text>` | ja | Nachricht, die gesprochen wird.  
  
### `speak`

Spricht eine Nachricht, ohne auf eine Antwort zu warten.

Flag | Erforderlich | Beschreibung  
---|---|---  
`--call-id <id>` | ja | Anruf-ID.  
`--message <text>` | ja | Nachricht, die gesprochen wird.  
  
### `dtmf`

Sendet DTMF-Ziffern an einen aktiven Anruf.

Flag | Erforderlich | Beschreibung  
---|---|---  
`--call-id <id>` | ja | Anruf-ID.  
`--digits <digits>` | ja | DTMF-Ziffern (z. B. `ww123456#` für Wartezeiten).  
  
### `end`

Beendet einen aktiven Anruf.

Flag | Erforderlich | Beschreibung  
---|---|---  
`--call-id <id>` | ja | Anruf-ID.  
  
### `status`

Prüft aktive Anrufe.

Flag | Standardwert | Beschreibung  
---|---|---  
`--call-id <id>` | (keiner) | Beschränkt die Ausgabe auf einen Anruf.  
`--json` | `false` | Gibt maschinenlesbares JSON aus.  
bashCopy code
[code]
    openclaw voicecall statusopenclaw voicecall status --jsonopenclaw voicecall status --call-id <id>
[/code]

## Protokolle und Metriken

### `tail`

Verfolgt das JSONL-Protokoll für Sprachanrufe fortlaufend. Gibt beim Start die letzten `--since` Zeilen aus und streamt danach neue Zeilen, sobald sie geschrieben werden.

Flag | Standardwert | Beschreibung  
---|---|---  
`--file <path>` | aus dem Plugin-Store aufgelöst | Pfad zu `calls.jsonl`.  
`--since <n>` | `25` | Zeilen, die vor dem fortlaufenden Verfolgen ausgegeben werden.  
`--poll <ms>` | `250` (Minimum 50) | Abfrageintervall in Millisekunden.  
  
### `latency`

Fasst Turn-Latenz- und Listen-Wait-Metriken aus `calls.jsonl` zusammen. Die Ausgabe ist JSON mit Zusammenfassungen für `recordsScanned`, `turnLatency` und `listenWait`.

Flag | Standardwert | Beschreibung  
---|---|---  
`--file <path>` | aus dem Plugin-Store aufgelöst | Pfad zu `calls.jsonl`.  
`--last <n>` | `200` (Minimum 1) | Anzahl der zuletzt zu analysierenden Datensätze.  
  
## Webhooks veröffentlichen

### `expose`

Aktiviert, deaktiviert oder ändert die Tailscale Serve/Funnel-Konfiguration für den Voice-Webhook.

Flag | Standardwert | Beschreibung  
---|---|---  
`--mode <mode>` | `funnel` | `off`, `serve` (Tailnet) oder `funnel` (öffentlich).  
`--path <path>` | config `tailscale.path` oder `--serve-path` | Freizugebender Tailscale-Pfad.  
`--port <port>` | config `serve.port` oder `3334` | Lokaler Webhook-Port.  
`--serve-path <path>` | config `serve.path` oder `/voice/webhook` | Lokaler Webhook-Pfad.  
bashCopy code
[code]
    openclaw voicecall expose --mode serveopenclaw voicecall expose --mode funnelopenclaw voicecall expose --mode off
[/code]

## Verwandte Themen

  * [CLI-Referenz](</de/cli>)
  * [Voice-Call-Plugin](</de/plugins/voice-call>)


Was this useful?YesNo