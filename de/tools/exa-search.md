---
title: Exa-Suche
source_url: https://docs.openclaw.ai/de/tools/exa-search
scraped_at: 2026-05-25
---

OpenClaw unterstützt [Exa AI](<https://exa.ai/>) als `web_search`-Provider. Exa bietet neuronale, schlüsselwortbasierte und hybride Suchmodi mit integrierter Inhaltsextraktion (Hervorhebungen, Text, Zusammenfassungen).

## API-Schlüssel erhalten

* ### Create an account

Registrieren Sie sich unter [exa.ai](<https://exa.ai/>) und generieren Sie einen API-Schlüssel in Ihrem Dashboard.

* ### Store the key

Legen Sie `EXA_API_KEY` in der Gateway-Umgebung fest, oder konfigurieren Sie ihn über:

bashCopy code
[code]
    openclaw configure --section web
[/code]

## Konfiguration

json5Copy code
[code]
    {  plugins: {    entries: {      exa: {        config: {          webSearch: {            apiKey: "exa-...", // optional if EXA_API_KEY is set            baseUrl: "https://api.exa.ai", // optional; OpenClaw appends /search          },        },      },    },  },  tools: {    web: {      search: {        provider: "exa",      },    },  },}
[/code]

**Alternative per Umgebung:** Legen Sie `EXA_API_KEY` in der Gateway-Umgebung fest. Bei einer Gateway-Installation tragen Sie ihn in `~/.openclaw/.env` ein.

## Basis-URL überschreiben

Legen Sie `plugins.entries.exa.config.webSearch.baseUrl` fest, wenn Exa-Suchanfragen über einen kompatiblen Proxy oder einen alternativen Exa-Endpunkt laufen sollen. OpenClaw normalisiert reine Hosts, indem `https://` vorangestellt wird, und hängt `/search` an, sofern der Pfad nicht bereits dort endet. Der aufgelöste Endpunkt wird in den Such-Cache-Schlüssel aufgenommen, sodass Ergebnisse von verschiedenen Exa-Endpunkten nicht gemeinsam genutzt werden.

## Tool-Parameter

Suchanfrage.

Zurückzugebende Ergebnisse (1–100).

Suchmodus.

Zeitfilter.

Ergebnisse nach diesem Datum (`YYYY-MM-DD`).

Ergebnisse vor diesem Datum (`YYYY-MM-DD`).

Optionen zur Inhaltsextraktion (siehe unten).

### Inhaltsextraktion

Exa kann extrahierte Inhalte zusammen mit Suchergebnissen zurückgeben. Übergeben Sie ein `contents`-Objekt, um dies zu aktivieren:

javascriptCopy code
[code]
    await web_search({  query: "transformer architecture explained",  type: "neural",  contents: {    text: true, // full page text    highlights: { numSentences: 3 }, // key sentences    summary: true, // AI summary  },});
[/code]

contents-Option | Typ | Beschreibung  
---|---|---  
`text` | `boolean | { maxCharacters }` | Vollständigen Seitentext extrahieren  
`highlights` | `boolean | { maxCharacters, query, numSentences, highlightsPerUrl }` | Schlüsselsätze extrahieren  
`summary` | `boolean | { query }` | KI-generierte Zusammenfassung  
  
### Suchmodi

Modus | Beschreibung  
---|---  
`auto` | Exa wählt den besten Modus aus (Standard)  
`neural` | Semantische/bedeutungsbasierte Suche  
`fast` | Schnelle Schlüsselwortsuche  
`deep` | Gründliche Tiefensuche  
`deep-reasoning` | Tiefensuche mit Reasoning  
`instant` | Schnellste Ergebnisse  
  
## Hinweise

  * Wenn keine `contents`-Option angegeben wird, verwendet Exa standardmäßig `{ highlights: true }`, sodass Ergebnisse Auszüge aus Schlüsselsätzen enthalten
  * Ergebnisse behalten `highlightScores`\- und `summary`-Felder aus der Exa API- Antwort bei, sofern verfügbar
  * Ergebnisbeschreibungen werden zuerst aus Hervorhebungen, dann aus der Zusammenfassung und danach aus dem vollständigen Text ermittelt, je nachdem, was verfügbar ist
  * `freshness` und `date_after`/`date_before` können nicht kombiniert werden; verwenden Sie einen Zeitfiltermodus
  * Pro Anfrage können bis zu 100 Ergebnisse zurückgegeben werden (abhängig von den Limits des Exa-Suchtyps)
  * Ergebnisse werden standardmäßig 15 Minuten zwischengespeichert (konfigurierbar über `cacheTtlMinutes`)
  * Exa ist eine offizielle API-Integration mit strukturierten JSON-Antworten


## Siehe auch

  * [Websuche-Übersicht](</de/tools/web>) \-- alle Provider und automatische Erkennung
  * [Brave Search](</de/tools/brave-search>) \-- strukturierte Ergebnisse mit Länder-/Sprachfiltern
  * [Perplexity Search](</de/tools/perplexity-search>) \-- strukturierte Ergebnisse mit Domain-Filterung


Was this useful?YesNo