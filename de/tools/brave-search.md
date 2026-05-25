---
title: Brave-Suche
source_url: https://docs.openclaw.ai/de/tools/brave-search
scraped_at: 2026-05-25
---

OpenClaw unterstützt die Brave Search API als `web_search`-Provider.

## API-Schlüssel abrufen

  1. Erstellen Sie ein Brave Search API-Konto unter <https://brave.com/search/api/>
  2. Wählen Sie im Dashboard den **Search** -Plan aus und generieren Sie einen API-Schlüssel.
  3. Speichern Sie den Schlüssel in der Konfiguration oder setzen Sie `BRAVE_API_KEY` in der Gateway-Umgebung.


## Konfigurationsbeispiel

json5Copy code
[code]
    {  plugins: {    entries: {      brave: {        config: {          webSearch: {            apiKey: "BRAVE_API_KEY_HERE",            mode: "web", // or "llm-context"            baseUrl: "https://api.search.brave.com", // optional proxy/base URL override          },        },      },    },  },  tools: {    web: {      search: {        provider: "brave",        maxResults: 5,        timeoutSeconds: 30,      },    },  },}
[/code]

Brave-spezifische Sucheinstellungen des Providers befinden sich jetzt unter `plugins.entries.brave.config.webSearch.*`. Das veraltete `tools.web.search.apiKey` wird weiterhin über den Kompatibilitäts-Shim geladen, ist aber nicht mehr der kanonische Konfigurationspfad.

`webSearch.mode` steuert den Brave-Transport:

  * `web` (Standard): normale Brave-Websuche mit Titeln, URLs und Snippets
  * `llm-context`: Brave LLM Context API mit vorab extrahierten Textabschnitten und Quellen für Grounding


`webSearch.baseUrl` kann Brave-Anfragen an einen vertrauenswürdigen Brave-kompatiblen Proxy oder ein Gateway leiten. OpenClaw hängt `/res/v1/web/search` oder `/res/v1/llm/context` an die konfigurierte Basis-URL an und behält die Basis-URL im Cache-Schlüssel bei. Öffentliche Endpunkte müssen `https://` verwenden; `http://` wird nur für vertrauenswürdige Loopback- oder Private-Network-Proxy-Hosts akzeptiert.

## Tool-Parameter

Suchanfrage.

Anzahl der zurückzugebenden Ergebnisse (1–10).

2-stelliger ISO-Ländercode (z. B. `US`, `DE`).

ISO-639-1-Sprachcode für Suchergebnisse (z. B. `en`, `de`, `fr`).

Brave-Suchsprachcode (z. B. `en`, `en-gb`, `zh-hans`).

ISO-Sprachcode für UI-Elemente.

Zeitfilter — `day` entspricht 24 Stunden.

Nur Ergebnisse, die nach diesem Datum veröffentlicht wurden (`YYYY-MM-DD`).

Nur Ergebnisse, die vor diesem Datum veröffentlicht wurden (`YYYY-MM-DD`).

**Beispiele:**

javascriptCopy code
[code]
    // Country and language-specific searchawait web_search({  query: "renewable energy",  country: "DE",  language: "de",}); // Recent results (past week)await web_search({  query: "AI news",  freshness: "week",}); // Date range searchawait web_search({  query: "AI developments",  date_after: "2024-01-01",  date_before: "2024-06-30",});
[/code]

## Hinweise

  * OpenClaw verwendet den Brave-**Search** -Plan. Wenn Sie ein älteres Abonnement haben (z. B. den ursprünglichen kostenlosen Plan mit 2.000 Abfragen/Monat), bleibt es gültig, enthält aber keine neueren Funktionen wie LLM Context oder höhere Ratenlimits.
  * Jeder Brave-Plan enthält **$5/Monat kostenloses Guthaben** (erneuernd). Der Search-Plan kostet $5 pro 1.000 Anfragen, sodass das Guthaben 1.000 Abfragen/Monat abdeckt. Legen Sie im Brave-Dashboard Ihr Nutzungslimit fest, um unerwartete Kosten zu vermeiden. Aktuelle Pläne finden Sie im [Brave API-Portal](<https://brave.com/search/api/>).
  * Der Search-Plan enthält den LLM Context-Endpunkt und Rechte für KI-Inferenz. Das Speichern von Ergebnissen zum Trainieren oder Optimieren von Modellen erfordert einen Plan mit ausdrücklichen Speicherrechten. Siehe die Brave-[Nutzungsbedingungen](<https://api-dashboard.search.brave.com/terms-of-service>).
  * Der Modus `llm-context` gibt geerdete Quelleneinträge statt der normalen Snippet-Struktur der Websuche zurück.
  * Der Modus `llm-context` unterstützt `freshness` und begrenzte Bereiche mit `date_after` \+ `date_before`. Er unterstützt `ui_lang` nicht; `date_before` ohne `date_after` wird abgelehnt, da Brave für benutzerdefinierte Freshness-Bereiche sowohl Start- als auch Enddatum verlangt.
  * `ui_lang` muss ein Regions-Subtag wie `en-US` enthalten.
  * Ergebnisse werden standardmäßig 15 Minuten lang zwischengespeichert (konfigurierbar über `cacheTtlMinutes`).
  * Benutzerdefinierte `webSearch.baseUrl`-Werte werden in die Brave-Cache-Identität einbezogen, sodass proxy-spezifische Antworten nicht kollidieren.
  * Aktivieren Sie das Diagnose-Flag `brave.http`, um bei der Fehlerbehebung Brave-Anfrage-URLs/Abfrageparameter, Antwortstatus/-Timing sowie Treffer/Fehlschläge/Schreibereignisse des Such-Caches zu protokollieren. Das Flag protokolliert niemals den API-Schlüssel oder Antwortkörper, Suchanfragen können jedoch sensibel sein.


## Verwandte Themen

  * [Web Search-Übersicht](</de/tools/web>) \-- alle Provider und automatische Erkennung
  * [Perplexity Search](</de/tools/perplexity-search>) \-- strukturierte Ergebnisse mit Domain-Filterung
  * [Exa Search](</de/tools/exa-search>) \-- neuronale Suche mit Inhaltsextraktion


Was this useful?YesNo