---
title: Exa-zoekfunctie
source_url: https://docs.openclaw.ai/nl/tools/exa-search
scraped_at: 2026-05-25
---

OpenClaw ondersteunt [Exa AI](<https://exa.ai/>) als `web_search`-provider. Exa biedt neurale, trefwoord- en hybride zoekmodi met ingebouwde contentextractie (highlights, tekst, samenvattingen).

## Een API-sleutel verkrijgen

* ### Een account maken

Registreer je op [exa.ai](<https://exa.ai/>) en genereer een API-sleutel via je dashboard.

* ### De sleutel opslaan

Stel `EXA_API_KEY` in de Gateway-omgeving in, of configureer via:

bashCopy code
[code]
    openclaw configure --section web
[/code]

## Configuratie

json5Copy code
[code]
    {  plugins: {    entries: {      exa: {        config: {          webSearch: {            apiKey: "exa-...", // optional if EXA_API_KEY is set            baseUrl: "https://api.exa.ai", // optional; OpenClaw appends /search          },        },      },    },  },  tools: {    web: {      search: {        provider: "exa",      },    },  },}
[/code]

**Omgevingsalternatief:** stel `EXA_API_KEY` in de Gateway-omgeving in. Voor een gateway-installatie plaats je dit in `~/.openclaw/.env`.

## Base-URL overschrijven

Stel `plugins.entries.exa.config.webSearch.baseUrl` in wanneer Exa-zoekverzoeken via een compatibele proxy of alternatief Exa-eindpunt moeten lopen. OpenClaw normaliseert kale hosts door `https://` ervoor te zetten en voegt `/search` toe, tenzij het pad daar al op eindigt. Het opgeloste eindpunt wordt opgenomen in de zoekcache- sleutel, zodat resultaten van verschillende Exa-eindpunten niet worden gedeeld.

## Toolparameters

Zoekquery.

Aantal te retourneren resultaten (1-100).

Zoekmodus.

Tijdsfilter.

Resultaten na deze datum (`YYYY-MM-DD`).

Resultaten vóór deze datum (`YYYY-MM-DD`).

Opties voor contentextractie (zie hieronder).

### Contentextractie

Exa kan geëxtraheerde content naast zoekresultaten retourneren. Geef een `contents`\- object door om dit in te schakelen:

javascriptCopy code
[code]
    await web_search({  query: "transformer architecture explained",  type: "neural",  contents: {    text: true, // full page text    highlights: { numSentences: 3 }, // key sentences    summary: true, // AI summary  },});
[/code]

Contents-optie | Type | Beschrijving  
---|---|---  
`text` | `boolean | { maxCharacters }` | Volledige paginatekst extraheren  
`highlights` | `boolean | { maxCharacters, query, numSentences, highlightsPerUrl }` | Kernzinnen extraheren  
`summary` | `boolean | { query }` | Door AI gegenereerde samenvatting  
  
### Zoekmodi

Modus | Beschrijving  
---|---  
`auto` | Exa kiest de beste modus (standaard)  
`neural` | Semantisch/betekenisgebaseerd zoeken  
`fast` | Snel zoeken op trefwoorden  
`deep` | Grondig diep zoeken  
`deep-reasoning` | Diep zoeken met redeneren  
`instant` | Snelste resultaten  
  
## Opmerkingen

  * Als er geen `contents`-optie is opgegeven, gebruikt Exa standaard `{ highlights: true }` zodat resultaten fragmenten van kernzinnen bevatten
  * Resultaten behouden `highlightScores`\- en `summary`-velden uit de Exa API- respons wanneer beschikbaar
  * Resultaatbeschrijvingen worden eerst uit highlights bepaald, daarna uit de samenvatting en daarna uit de volledige tekst, afhankelijk van wat beschikbaar is
  * `freshness` en `date_after`/`date_before` kunnen niet worden gecombineerd; gebruik één tijdsfiltermodus
  * Er kunnen maximaal 100 resultaten per query worden geretourneerd (afhankelijk van Exa-zoektype- limieten)
  * Resultaten worden standaard 15 minuten gecachet (configureerbaar via `cacheTtlMinutes`)
  * Exa is een officiële API-integratie met gestructureerde JSON-responsen


## Gerelateerd

  * [Overzicht van Web Search](</nl/tools/web>) \-- alle providers en automatische detectie
  * [Brave Search](</nl/tools/brave-search>) \-- gestructureerde resultaten met filters voor land/taal
  * [Perplexity Search](</nl/tools/perplexity-search>) \-- gestructureerde resultaten met domeinfiltering


Was this useful?YesNo