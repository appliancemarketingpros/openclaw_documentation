---
title: Zustand
source_url: https://docs.openclaw.ai/de/cli/health
scraped_at: 2026-05-25
---

# `openclaw health`

Ruft den Health-Status vom laufenden Gateway ab.

## Optionen

Flag | Standardwert | Beschreibung  
---|---|---  
`--json` | `false` | Gibt maschinenlesbares JSON statt Text aus.  
`--timeout <ms>` | `10000` | Verbindungs-Timeout in Millisekunden.  
`--verbose` | `false` | Ausführliche Protokollierung. Erzwingt eine Live-Prüfung und erweitert die Ausgabe pro Agent.  
`--debug` | `false` | Alias für `--verbose`.  
  
Beispiele:

bashCopy code
[code]
    openclaw healthopenclaw health --jsonopenclaw health --timeout 2500openclaw health --verboseopenclaw health --debug
[/code]

Hinweise:

  * Standardmäßig fragt `openclaw health` das laufende Gateway nach seinem Health-Snapshot. Wenn das Gateway bereits einen frischen zwischengespeicherten Snapshot hat, kann es diese zwischengespeicherte Nutzlast zurückgeben und im Hintergrund aktualisieren.
  * `--verbose` erzwingt eine Live-Prüfung, gibt Verbindungsdetails des Gateway aus und erweitert die menschenlesbare Ausgabe über alle konfigurierten Konten und Agenten hinweg.
  * Die Ausgabe enthält Session Stores pro Agent, wenn mehrere Agenten konfiguriert sind.


## Verwandt

  * [CLI-Referenz](</de/cli>)
  * [Gateway-Health](</de/gateway/health>)


Was this useful?YesNo