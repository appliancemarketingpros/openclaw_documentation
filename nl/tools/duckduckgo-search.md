---
title: DuckDuckGo-zoekopdracht
source_url: https://docs.openclaw.ai/nl/tools/duckduckgo-search
scraped_at: 2026-05-25
---

OpenClaw ondersteunt DuckDuckGo als **sleutelloze** `web_search`-provider. Er is geen API- sleutel of account vereist.

## Installatie

Geen API-sleutel nodig - stel DuckDuckGo gewoon in als je provider:

* ### Configureren

bashCopy code
[code]
    openclaw configure --section web# Select "duckduckgo" as the provider
[/code]

## Configuratie

json5Copy code
[code]
    {  tools: {    web: {      search: {        provider: "duckduckgo",      },    },  },}
[/code]

Optionele instellingen op Plugin-niveau voor regio en SafeSearch:

json5Copy code
[code]
    {  plugins: {    entries: {      duckduckgo: {        config: {          webSearch: {            region: "us-en", // DuckDuckGo region code            safeSearch: "moderate", // "strict", "moderate", or "off"          },        },      },    },  },}
[/code]

## Toolparameters

Zoekquery.

Te retourneren resultaten (1-10).

DuckDuckGo-regiocode (bijv. `us-en`, `uk-en`, `de-de`).

SafeSearch-niveau.

Regio en SafeSearch kunnen ook worden ingesteld in de Plugin-configuratie (zie hierboven) - tool parameters overschrijven configuratiewaarden per query.

## Opmerkingen

  * **Geen API-sleutel** \- werkt direct, zonder configuratie
  * **Experimenteel** \- verzamelt resultaten uit DuckDuckGo's HTML-zoekpagina's zonder JavaScript, niet uit een officiële API of SDK
  * **Risico op bot-challenges** \- DuckDuckGo kan CAPTCHA's tonen of verzoeken blokkeren bij intensief of geautomatiseerd gebruik
  * **HTML-parsing** \- resultaten hangen af van de paginstructuur, die zonder kennisgeving kan wijzigen
  * **Volgorde voor automatische detectie** \- DuckDuckGo is de eerste sleutelloze fallback (volgorde 100) bij automatische detectie. API-gebaseerde providers met geconfigureerde sleutels worden eerst uitgevoerd, daarna Ollama Web Search (volgorde 110), daarna SearXNG (volgorde 200)
  * **SafeSearch staat standaard op moderate** wanneer dit niet is geconfigureerd


## Gerelateerd

  * [Overzicht van Web Search](</nl/tools/web>) \-- alle providers en automatische detectie
  * [Brave Search](</nl/tools/brave-search>) \-- gestructureerde resultaten met gratis laag
  * [Exa Search](</nl/tools/exa-search>) \-- neurale zoekfunctie met contentextractie


Was this useful?YesNo