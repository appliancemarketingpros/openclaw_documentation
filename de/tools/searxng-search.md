---
title: SearXNG-Suche
source_url: https://docs.openclaw.ai/de/tools/searxng-search
scraped_at: 2026-05-25
---

OpenClaw unterstützt [SearXNG](<https://docs.searxng.org/>) als **selbst gehosteten, schlüsselfreien** `web_search`-Provider. SearXNG ist eine quelloffene Metasuchmaschine, die Ergebnisse von Google, Bing, DuckDuckGo und anderen Quellen aggregiert.

Vorteile:

  * **Kostenlos und unbegrenzt** \-- kein API-Schlüssel und kein kommerzielles Abonnement erforderlich
  * **Datenschutz / Air-Gap** \-- Abfragen verlassen niemals Ihr Netzwerk
  * **Funktioniert überall** \-- keine Regionsbeschränkungen für kommerzielle Such-APIs


## Einrichtung

* ### Eine SearXNG-Instanz ausführen

bashCopy code
[code]
    docker run -d -p 8888:8080 searxng/searxng
[/code]

Oder verwenden Sie eine vorhandene SearXNG-Bereitstellung, auf die Sie Zugriff haben. Weitere Informationen zur Produktionseinrichtung finden Sie in der [SearXNG-Dokumentation](<https://docs.searxng.org/>).

* ### Konfigurieren

bashCopy code
[code]
    openclaw configure --section web# Select "searxng" as the provider
[/code]

Oder legen Sie die Umgebungsvariable fest und lassen Sie sie von der automatischen Erkennung finden:

bashCopy code
[code]
    export SEARXNG_BASE_URL="http://localhost:8888"
[/code]

## Konfiguration

json5Copy code
[code]
    {  tools: {    web: {      search: {        provider: "searxng",      },    },  },}
[/code]

Plugin-Einstellungen für die SearXNG-Instanz:

json5Copy code
[code]
    {  plugins: {    entries: {      searxng: {        config: {          webSearch: {            baseUrl: "http://localhost:8888",            categories: "general,news", // optional            language: "en", // optional          },        },      },    },  },}
[/code]

Das Feld `baseUrl` akzeptiert auch SecretRef-Objekte.

Transportregeln:

  * `https://` funktioniert für öffentliche oder private SearXNG-Hosts
  * `http://` wird nur für vertrauenswürdige private Netzwerk- oder loopback-Hosts akzeptiert
  * öffentliche SearXNG-Hosts müssen `https://` verwenden
  * private/interne Hosts verwenden den selbst gehosteten Netzwerkschutz; öffentliche `https://`-Hosts bleiben beim strikten Websuch-Schutz und können nicht auf private Adressen umleiten


## Umgebungsvariable

Legen Sie `SEARXNG_BASE_URL` als Alternative zur Konfiguration fest:

bashCopy code
[code]
    export SEARXNG_BASE_URL="http://localhost:8888"
[/code]

Wenn `SEARXNG_BASE_URL` gesetzt ist und kein expliziter Provider konfiguriert wurde, wählt die automatische Erkennung SearXNG automatisch aus (mit der niedrigsten Priorität -- jeder API-gestützte Provider mit einem Schlüssel gewinnt zuerst).

## Plugin-Konfigurationsreferenz

Feld | Beschreibung  
---|---  
`baseUrl` | Basis-URL Ihrer SearXNG-Instanz (erforderlich)  
`categories` | Kommagetrennte Kategorien wie `general`, `news` oder `science`  
`language` | Sprachcode für Ergebnisse wie `en`, `de` oder `fr`  
  
## Hinweise

  * **JSON-API** \-- verwendet SearXNGs nativen `format=json`-Endpunkt, kein HTML-Scraping
  * **URLs für Bildergebnisse** \-- Ergebnisse der Bildkategorie enthalten `img_src`, wenn SearXNG eine direkte Bild-URL zurückgibt
  * **Kein API-Schlüssel** \-- funktioniert sofort mit jeder SearXNG-Instanz
  * **Validierung der Basis-URL** \-- `baseUrl` muss eine gültige `http://`\- oder `https://`-URL sein; öffentliche Hosts müssen `https://` verwenden
  * **Netzwerkschutz** \-- private/interne SearXNG-Endpunkte entscheiden sich für den Zugriff auf private Netzwerke; öffentliche `https://`-SearXNG-Endpunkte behalten den strikten SSRF-Schutz bei
  * **Reihenfolge der automatischen Erkennung** \-- SearXNG wird bei der automatischen Erkennung zuletzt geprüft (Reihenfolge 200). API-gestützte Provider mit konfigurierten Schlüsseln laufen zuerst, dann DuckDuckGo (Reihenfolge 100), dann Ollama Web Search (Reihenfolge 110)
  * **Selbst gehostet** \-- Sie kontrollieren die Instanz, Abfragen und vorgelagerten Suchmaschinen
  * **Kategorien** sind standardmäßig `general`, wenn sie nicht konfiguriert sind
  * **Kategorie-Fallback** \-- wenn eine Anfrage für eine nicht-`general`-Kategorie erfolgreich ist, aber keine Ergebnisse zurückgibt, wiederholt OpenClaw dieselbe Abfrage einmal mit `general`, bevor ein leeres Ergebnisset zurückgegeben wird


## Verwandte Themen

  * [Websuche-Übersicht](</de/tools/web>) \-- alle Provider und automatische Erkennung
  * [DuckDuckGo-Suche](</de/tools/duckduckgo-search>) \-- ein weiterer schlüsselfreier Fallback
  * [Brave Search](</de/tools/brave-search>) \-- strukturierte Ergebnisse mit kostenloser Stufe


Was this useful?YesNo