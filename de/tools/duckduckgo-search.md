---
title: DuckDuckGo-Suche
source_url: https://docs.openclaw.ai/de/tools/duckduckgo-search
scraped_at: 2026-05-25
---

OpenClaw unterstützt DuckDuckGo als **schlüsselfreien** `web_search`-Provider. Es ist kein API-Schlüssel und kein Konto erforderlich.

## Einrichtung

Kein API-Schlüssel erforderlich - legen Sie DuckDuckGo einfach als Ihren Provider fest:

* ### Konfigurieren

bashCopy code
[code]
    openclaw configure --section web# Select "duckduckgo" as the provider
[/code]

## Konfiguration

json5Copy code
[code]
    {  tools: {    web: {      search: {        provider: "duckduckgo",      },    },  },}
[/code]

Optionale Einstellungen auf Plugin-Ebene für Region und SafeSearch:

json5Copy code
[code]
    {  plugins: {    entries: {      duckduckgo: {        config: {          webSearch: {            region: "us-en", // DuckDuckGo region code            safeSearch: "moderate", // "strict", "moderate", or "off"          },        },      },    },  },}
[/code]

## Tool-Parameter

Suchanfrage.

Zurückzugebende Ergebnisse (1-10).

DuckDuckGo-Regionscode (z. B. `us-en`, `uk-en`, `de-de`).

SafeSearch-Stufe.

Region und SafeSearch können auch in der Plugin-Konfiguration festgelegt werden (siehe oben) - Tool- Parameter überschreiben Konfigurationswerte pro Abfrage.

## Hinweise

  * **Kein API-Schlüssel** \- funktioniert sofort, ohne Konfiguration
  * **Experimentell** \- sammelt Ergebnisse aus DuckDuckGos Nicht-JavaScript-HTML- Suchseiten, nicht aus einer offiziellen API oder einem SDK
  * **Bot-Challenge-Risiko** \- DuckDuckGo kann CAPTCHAs ausliefern oder Anfragen bei starker oder automatisierter Nutzung blockieren
  * **HTML-Parsing** \- Ergebnisse hängen von der Seitenstruktur ab, die sich ohne Ankündigung ändern kann
  * **Reihenfolge der automatischen Erkennung** \- DuckDuckGo ist der erste schlüsselfreie Fallback (Reihenfolge 100) in der automatischen Erkennung. API-gestützte Provider mit konfigurierten Schlüsseln werden zuerst ausgeführt, dann Ollama Web Search (Reihenfolge 110), dann SearXNG (Reihenfolge 200)
  * **SafeSearch ist standardmäßig moderat** , wenn nicht konfiguriert


## Verwandt

  * [Web Search-Übersicht](</de/tools/web>) \-- alle Provider und automatische Erkennung
  * [Brave Search](</de/tools/brave-search>) \-- strukturierte Ergebnisse mit kostenlosem Kontingent
  * [Exa Search](</de/tools/exa-search>) \-- neuronale Suche mit Inhaltsextraktion


Was this useful?YesNo