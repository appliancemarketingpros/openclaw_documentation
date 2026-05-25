---
title: Gateway-Protokollierung
source_url: https://docs.openclaw.ai/de/gateway/logging
scraped_at: 2026-05-25
---

# Protokollierung

Eine nutzerorientierte Übersicht (CLI + Control UI + Konfiguration) finden Sie unter [/logging](</de/logging>).

OpenClaw hat zwei Log-„Oberflächen“:

  * **Konsolenausgabe** (was Sie im Terminal / Debug UI sehen).
  * **Datei-Logs** (JSON-Zeilen), die vom Gateway-Logger geschrieben werden.


Beim Start protokolliert das Gateway das aufgelöste Standard-Agentenmodell zusammen mit den Modus-Standardwerten, die neue Sitzungen beeinflussen, zum Beispiel:

textCopy code
[code]
    agent model: openai-codex/gpt-5.5 (thinking=medium, fast=on)
[/code]

`thinking` stammt aus dem Standard-Agenten, den Modellparametern oder dem globalen Agentenstandard; wenn es nicht gesetzt ist, zeigt die Startzusammenfassung `medium`. `fast` stammt aus dem Standard-Agenten oder den `fastMode`-Parametern des Modells.

## Dateibasierter Logger

  * Die standardmäßige rotierende Logdatei liegt unter `/tmp/openclaw/` (eine Datei pro Tag): `openclaw-YYYY-MM-DD.log`
    * Das Datum verwendet die lokale Zeitzone des Gateway-Hosts.
  * Aktive Logdateien rotieren bei `logging.maxFileBytes` (Standard: 100 MB), behalten bis zu fünf nummerierte Archive und schreiben anschließend in eine neue aktive Datei.
  * Pfad und Level der Logdatei können über `~/.openclaw/openclaw.json` konfiguriert werden: 
    * `logging.file`
    * `logging.level`


Das Dateiformat ist ein JSON-Objekt pro Zeile.

Talk-, Echtzeit-Sprach- und Managed-Room-Codepfade verwenden den gemeinsamen Datei-Logger für begrenzte Lebenszyklusdatensätze. Diese Datensätze sind für operatives Debugging und den OTLP-Logexport gedacht; Transkripttext, Audio-Payloads, Turn-IDs, Call-IDs und Provider-Item-IDs werden nicht in den Logdatensatz kopiert.

Der Logs-Tab der Control UI verfolgt diese Datei über das Gateway (`logs.tail`). Die CLI kann dasselbe tun:

bashCopy code
[code]
    openclaw logs --follow
[/code]

**Ausführlichkeit vs. Log-Level**

  * **Datei-Logs** werden ausschließlich durch `logging.level` gesteuert.
  * `--verbose` wirkt sich nur auf die **Ausführlichkeit der Konsole** (und den WS-Logstil) aus; es erhöht **nicht** das Log-Level der Datei.
  * Um nur bei ausführlicher Ausgabe sichtbare Details in Datei-Logs zu erfassen, setzen Sie `logging.level` auf `debug` oder `trace`.
  * Trace-Logging enthält außerdem diagnostische Timing-Zusammenfassungen für ausgewählte Hot Paths, etwa die Vorbereitung von Plugin-Tool-Factories. Siehe [/tools/plugin#slow-plugin-tool-setup](</de/tools/plugin#slow-plugin-tool-setup>).


## Konsolenerfassung

Die CLI erfasst `console.log/info/warn/error/debug/trace` und schreibt sie in Datei-Logs, während sie weiterhin auf stdout/stderr ausgegeben werden.

Sie können die Ausführlichkeit der Konsole unabhängig einstellen über:

  * `logging.consoleLevel` (Standard `info`)
  * `logging.consoleStyle` (`pretty` | `compact` | `json`)


## Schwärzung

OpenClaw kann sensible Token maskieren, bevor Log- oder Transkriptausgaben den Prozess verlassen. Diese Protokollierungs-Schwärzungsrichtlinie wird auf Konsolen-, Datei-Log-, OTLP- Logdatensatz- und Sitzungstranskript-Textsenken angewendet, sodass passende geheime Werte maskiert werden, bevor JSONL-Zeilen oder Nachrichten auf die Festplatte geschrieben werden.

  * `logging.redactSensitive`: `off` | `tools` (Standard: `tools`)
  * `logging.redactPatterns`: Array von Regex-Strings (überschreibt Standardwerte) 
    * Verwenden Sie rohe Regex-Strings (automatisch `gi`) oder `/pattern/flags`, wenn Sie eigene Flags benötigen.
    * Treffer werden maskiert, indem die ersten 6 + letzten 4 Zeichen beibehalten werden (Länge >= 18), andernfalls `***`.
    * Standardwerte decken gängige Schlüsselzuweisungen, CLI-Flags, JSON-Felder, Bearer-Header, PEM-Blöcke, verbreitete Token-Präfixe und Feldnamen für Zahlungsdaten wie Kartennummer, CVC/CVV, gemeinsames Zahlungstoken und Zahlungsnachweis ab.


Einige Sicherheitsgrenzen schwärzen immer, unabhängig von `logging.redactSensitive`. Dazu gehören Tool-Call-Ereignisse der Control UI, `sessions_history`-Tool-Ausgaben, Diagnose-Supportexporte, Provider-Fehlerbeobachtungen, die Anzeige von Exec-Freigabebefehlen und Gateway-WebSocket-Protokoll-Logs. Diese Oberflächen können weiterhin `logging.redactPatterns` als zusätzliche Muster verwenden, aber `redactSensitive: "off"` führt nicht dazu, dass sie rohe Secrets ausgeben.

## Gateway-WebSocket-Logs

Das Gateway gibt WebSocket-Protokoll-Logs in zwei Modi aus:

  * **Normalmodus (kein`--verbose`)**: Nur „interessante“ RPC-Ergebnisse werden ausgegeben: 
    * Fehler (`ok=false`)
    * langsame Aufrufe (Standardschwelle: `>= 50ms`)
    * Parse-Fehler
  * **Ausführlicher Modus (`--verbose`)**: Gibt den gesamten WS-Anfrage-/Antwortverkehr aus.


### WS-Logstil

`openclaw gateway` unterstützt einen stilbezogenen Schalter pro Gateway:

  * `--ws-log auto` (Standard): Normalmodus ist optimiert; ausführlicher Modus verwendet kompakte Ausgabe
  * `--ws-log compact`: kompakte Ausgabe (gepaarte Anfrage/Antwort), wenn ausführlich
  * `--ws-log full`: vollständige Ausgabe pro Frame, wenn ausführlich
  * `--compact`: Alias für `--ws-log compact`


Beispiele:

bashCopy code
[code]
    # optimiert (nur Fehler/langsam)openclaw gateway # gesamten WS-Verkehr anzeigen (gepaart)openclaw gateway --verbose --ws-log compact # gesamten WS-Verkehr anzeigen (vollständige Metadaten)openclaw gateway --verbose --ws-log full
[/code]

## Konsolenformatierung (Subsystem-Logging)

Der Konsolen-Formatter ist **TTY-bewusst** und gibt konsistente, präfixierte Zeilen aus. Subsystem-Logger halten die Ausgabe gruppiert und gut erfassbar.

Verhalten:

  * **Subsystem-Präfixe** in jeder Zeile (z. B. `[gateway]`, `[canvas]`, `[tailscale]`)
  * **Subsystem-Farben** (stabil pro Subsystem) plus Level-Einfärbung
  * **Farbe, wenn die Ausgabe ein TTY ist oder die Umgebung wie ein funktionsreiches Terminal aussieht** (`TERM`/`COLORTERM`/`TERM_PROGRAM`), berücksichtigt `NO_COLOR`
  * **Verkürzte Subsystem-Präfixe** : entfernt führendes `gateway/` \+ `channels/`, behält die letzten 2 Segmente (z. B. `whatsapp/outbound`)
  * **Sub-Logger nach Subsystem** (automatisches Präfix + strukturiertes Feld `{ subsystem }`)
  * **`logRaw()`** für QR-/UX-Ausgabe (kein Präfix, keine Formatierung)
  * **Konsolenstile** (z. B. `pretty | compact | json`)
  * **Konsolen-Log-Level** getrennt vom Datei-Log-Level (Datei behält vollständige Details, wenn `logging.level` auf `debug`/`trace` gesetzt ist)
  * **WhatsApp-Nachrichtentexte** werden auf `debug` protokolliert (verwenden Sie `--verbose`, um sie zu sehen)


So bleiben bestehende Datei-Logs stabil, während interaktive Ausgaben gut erfassbar werden.

## Verwandte Themen

  * [Protokollierung](</de/logging>)
  * [OpenTelemetry-Export](</de/gateway/opentelemetry>)
  * [Diagnoseexport](</de/gateway/diagnostics>)


Was this useful?YesNo