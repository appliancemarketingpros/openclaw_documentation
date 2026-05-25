---
title: Diagnose-Flags
source_url: https://docs.openclaw.ai/de/diagnostics/flags
scraped_at: 2026-05-25
---

Diagnose-Flags ermöglichen es Ihnen, gezielte Debug-Logs zu aktivieren, ohne überall ausführliches Logging einzuschalten. Flags sind Opt-in und haben keine Wirkung, sofern ein Subsystem sie nicht prüft.

## Funktionsweise

  * Flags sind Zeichenfolgen (Groß-/Kleinschreibung wird ignoriert).
  * Sie können Flags in der Konfiguration oder über einen Env-Override aktivieren.
  * Platzhalter werden unterstützt: 
    * `telegram.*` entspricht `telegram.http`
    * `*` aktiviert alle Flags


## Über die Konfiguration aktivieren

jsonCopy code
[code]
    {  "diagnostics": {    "flags": ["telegram.http"]  }}
[/code]

Mehrere Flags:

jsonCopy code
[code]
    {  "diagnostics": {    "flags": ["telegram.http", "brave.http", "gateway.*"]  }}
[/code]

Starten Sie das Gateway neu, nachdem Sie Flags geändert haben.

## Env-Override (einmalig)

bashCopy code
[code]
    OPENCLAW_DIAGNOSTICS=telegram.http,telegram.payload
[/code]

Alle Flags deaktivieren:

bashCopy code
[code]
    OPENCLAW_DIAGNOSTICS=0
[/code]

## Timeline-Artefakte

Das Flag `timeline` schreibt strukturierte Zeitereignisse für Start und Laufzeit für externe QA-Harnesses:

bashCopy code
[code]
    OPENCLAW_DIAGNOSTICS=timeline \OPENCLAW_DIAGNOSTICS_TIMELINE_PATH=/tmp/openclaw-timeline.jsonl \openclaw gateway run
[/code]

Sie können es auch in der Konfiguration aktivieren:

jsonCopy code
[code]
    {  "diagnostics": {    "flags": ["timeline"]  }}
[/code]

Der Dateipfad für die Timeline stammt weiterhin aus `OPENCLAW_DIAGNOSTICS_TIMELINE_PATH`. Wenn `timeline` nur über die Konfiguration aktiviert ist, werden die frühesten Spans zum Laden der Konfiguration nicht ausgegeben, da OpenClaw die Konfiguration noch nicht gelesen hat; nachfolgende Start-Spans verwenden das Konfigurations-Flag.

`OPENCLAW_DIAGNOSTICS=1`, `OPENCLAW_DIAGNOSTICS=all` und `OPENCLAW_DIAGNOSTICS=*` aktivieren ebenfalls die Timeline, da sie jedes Diagnose-Flag aktivieren. Verwenden Sie bevorzugt `timeline`, wenn Sie nur das JSONL-Zeitmessungsartefakt möchten.

Timeline-Datensätze verwenden den Umschlag `openclaw.diagnostics.v1`. Ereignisse können Prozess-IDs, Phasennamen, Span-Namen, Dauern, Plugin-IDs, Abhängigkeitsanzahlen, Event-Loop-Verzögerungsstichproben, Namen von Provider-Operationen, den Exit-Zustand von Kindprozessen und Namen/Meldungen von Startfehlern enthalten. Behandeln Sie Timeline-Dateien als lokale Diagnoseartefakte; prüfen Sie sie, bevor Sie sie außerhalb Ihres Computers weitergeben.

## Speicherort der Logs

Flags geben Logs in die standardmäßige Diagnose-Logdatei aus. Standardmäßig:

CodeCopy code
[code]
    /tmp/openclaw/openclaw-YYYY-MM-DD.log
[/code]

Wenn Sie `logging.file` festlegen, verwenden Sie stattdessen diesen Pfad. Logs sind JSONL (ein JSON-Objekt pro Zeile). Die Schwärzung gilt weiterhin basierend auf `logging.redactSensitive`.

## Logs extrahieren

Wählen Sie die neueste Logdatei aus:

bashCopy code
[code]
    ls -t /tmp/openclaw/openclaw-*.log | head -n 1
[/code]

Nach Telegram-HTTP-Diagnosen filtern:

bashCopy code
[code]
    rg "telegram http error" /tmp/openclaw/openclaw-*.log
[/code]

Nach Brave Search-HTTP-Diagnosen filtern:

bashCopy code
[code]
    rg "brave http" /tmp/openclaw/openclaw-*.log
[/code]

Oder beim Reproduzieren per Tail mitlesen:

bashCopy code
[code]
    tail -f /tmp/openclaw/openclaw-$(date +%F).log | rg "telegram http error"
[/code]

Für Remote-Gateways können Sie auch `openclaw logs --follow` verwenden (siehe [/cli/logs](</de/cli/logs>)).

## Hinweise

  * Wenn `logging.level` höher als `warn` gesetzt ist, können diese Logs unterdrückt werden. Der Standardwert `info` ist ausreichend.
  * `brave.http` protokolliert Brave Search-Anfrage-URLs/Query-Parameter, Antwortstatus/-Timing sowie Cache-Hit/Miss/Write-Ereignisse. Es protokolliert keine API-Schlüssel oder Antworttexte, Suchanfragen können jedoch sensibel sein.
  * Flags können aktiviert bleiben; sie wirken sich nur auf das Logvolumen des jeweiligen Subsystems aus.
  * Verwenden Sie [/logging](</de/logging>), um Logziele, Level und Schwärzung zu ändern.


## Verwandte Themen

  * [Gateway-Diagnose](</de/gateway/diagnostics>)
  * [Gateway-Fehlerbehebung](</de/gateway/troubleshooting>)


Was this useful?YesNo