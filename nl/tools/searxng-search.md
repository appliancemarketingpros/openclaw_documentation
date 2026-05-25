---
title: SearXNG-zoekopdracht
source_url: https://docs.openclaw.ai/nl/tools/searxng-search
scraped_at: 2026-05-25
---

OpenClaw ondersteunt [SearXNG](<https://docs.searxng.org/>) als **zelf-gehoste, sleutelvrije** `web_search`-provider. SearXNG is een open-source meta-zoekmachine die resultaten van Google, Bing, DuckDuckGo en andere bronnen samenvoegt.

Voordelen:

  * **Gratis en onbeperkt** \-- geen API-sleutel of commercieel abonnement vereist
  * **Privacy / air-gap** \-- zoekopdrachten verlaten je netwerk nooit
  * **Werkt overal** \-- geen regiobeperkingen op commerciële zoek-API's


## Installatie

* ### Run a SearXNG instance

bashCopy code
[code]
    docker run -d -p 8888:8080 searxng/searxng
[/code]

Of gebruik een bestaande SearXNG-deployment waartoe je toegang hebt. Zie de [SearXNG-documentatie](<https://docs.searxng.org/>) voor productie-installatie.

* ### Configure

bashCopy code
[code]
    openclaw configure --section web# Select "searxng" as the provider
[/code]

Of stel de env var in en laat automatische detectie die vinden:

bashCopy code
[code]
    export SEARXNG_BASE_URL="http://localhost:8888"
[/code]

## Configuratie

json5Copy code
[code]
    {  tools: {    web: {      search: {        provider: "searxng",      },    },  },}
[/code]

Instellingen op Plugin-niveau voor de SearXNG-instantie:

json5Copy code
[code]
    {  plugins: {    entries: {      searxng: {        config: {          webSearch: {            baseUrl: "http://localhost:8888",            categories: "general,news", // optional            language: "en", // optional          },        },      },    },  },}
[/code]

Het veld `baseUrl` accepteert ook SecretRef-objecten.

Transportregels:

  * `https://` werkt voor openbare of private SearXNG-hosts
  * `http://` wordt alleen geaccepteerd voor vertrouwde private-network- of loopback-hosts
  * openbare SearXNG-hosts moeten `https://` gebruiken
  * private/interne hosts gebruiken de zelf-gehoste netwerkbeveiliging; openbare `https://`\- hosts blijven op de strikte webzoekbeveiliging en kunnen niet doorverwijzen naar private adressen


## Omgevingsvariabele

Stel `SEARXNG_BASE_URL` in als alternatief voor configuratie:

bashCopy code
[code]
    export SEARXNG_BASE_URL="http://localhost:8888"
[/code]

Wanneer `SEARXNG_BASE_URL` is ingesteld en er geen expliciete provider is geconfigureerd, kiest automatische detectie SearXNG automatisch (met de laagste prioriteit -- elke API-ondersteunde provider met een sleutel wint eerst).

## Referentie voor Plugin-configuratie

Veld | Beschrijving  
---|---  
`baseUrl` | Basis-URL van je SearXNG-instantie (vereist)  
`categories` | Door komma's gescheiden categorieen zoals `general`, `news` of `science`  
`language` | Taalcode voor resultaten zoals `en`, `de` of `fr`  
  
## Opmerkingen

  * **JSON-API** \-- gebruikt het native `format=json`-endpoint van SearXNG, geen HTML-scraping
  * **URL's van afbeeldingsresultaten** \-- resultaten uit afbeeldingscategorieen bevatten `img_src` wanneer SearXNG een directe afbeeldings-URL retourneert
  * **Geen API-sleutel** \-- werkt direct met elke SearXNG-instantie
  * **Validatie van basis-URL** \-- `baseUrl` moet een geldige `http://`\- of `https://`\- URL zijn; openbare hosts moeten `https://` gebruiken
  * **Netwerkbeveiliging** \-- private/interne SearXNG-endpoints kiezen expliciet voor toegang tot private netwerken; openbare `https://` SearXNG-endpoints behouden strikte SSRF- bescherming
  * **Volgorde van automatische detectie** \-- SearXNG wordt als laatste gecontroleerd (volgorde 200) in automatische detectie. API-ondersteunde providers met geconfigureerde sleutels draaien eerst, daarna DuckDuckGo (volgorde 100), daarna Ollama Web Search (volgorde 110)
  * **Zelf-gehost** \-- jij beheert de instantie, zoekopdrachten en upstream-zoekmachines
  * **Categorieen** gebruiken standaard `general` wanneer ze niet zijn geconfigureerd
  * **Categoriefallback** \-- als een categorieaanvraag anders dan `general` slaagt maar nul resultaten retourneert, probeert OpenClaw dezelfde zoekopdracht nog eenmaal met `general` voordat een lege resultatenset wordt geretourneerd


## Gerelateerd

  * [Overzicht van Web Search](</nl/tools/web>) \-- alle providers en automatische detectie
  * [DuckDuckGo Search](</nl/tools/duckduckgo-search>) \-- nog een sleutelvrije fallback
  * [Brave Search](</nl/tools/brave-search>) \-- gestructureerde resultaten met gratis laag


Was this useful?YesNo