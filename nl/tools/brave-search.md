---
title: Brave zoeken
source_url: https://docs.openclaw.ai/nl/tools/brave-search
scraped_at: 2026-05-25
---

OpenClaw ondersteunt de Brave Search API als `web_search`-provider.

## Een API-sleutel verkrijgen

  1. Maak een Brave Search API-account aan op <https://brave.com/search/api/>
  2. Kies in het dashboard het **Search** -abonnement en genereer een API-sleutel.
  3. Sla de sleutel op in de configuratie of stel `BRAVE_API_KEY` in de Gateway-omgeving in.


## Configuratievoorbeeld

json5Copy code
[code]
    {  plugins: {    entries: {      brave: {        config: {          webSearch: {            apiKey: "BRAVE_API_KEY_HERE",            mode: "web", // or "llm-context"            baseUrl: "https://api.search.brave.com", // optional proxy/base URL override          },        },      },    },  },  tools: {    web: {      search: {        provider: "brave",        maxResults: 5,        timeoutSeconds: 30,      },    },  },}
[/code]

Providerspecifieke Brave-zoekinstellingen staan nu onder `plugins.entries.brave.config.webSearch.*`. De verouderde `tools.web.search.apiKey` wordt nog steeds geladen via de compatibiliteitsshim, maar is niet langer het canonieke configuratiepad.

`webSearch.mode` bepaalt de Brave-transportlaag:

  * `web` (standaard): normale Brave-webzoekfunctie met titels, URL's en snippets
  * `llm-context`: Brave LLM Context API met vooraf geëxtraheerde tekstfragmenten en bronnen voor grounding


`webSearch.baseUrl` kan Brave-verzoeken naar een vertrouwde Brave-compatibele proxy of Gateway laten wijzen. OpenClaw voegt `/res/v1/web/search` of `/res/v1/llm/context` toe aan de geconfigureerde basis-URL en houdt de basis-URL in de cachesleutel. Publieke endpoints moeten `https://` gebruiken; `http://` wordt alleen geaccepteerd voor vertrouwde loopback- of privénetwerk-proxyhosts.

## Toolparameters

Zoekquery.

Aantal resultaten om terug te geven (1–10).

2-letterige ISO-landcode (bijv. `US`, `DE`).

ISO 639-1-taalcode voor zoekresultaten (bijv. `en`, `de`, `fr`).

Brave-zoektaalcode (bijv. `en`, `en-gb`, `zh-hans`).

ISO-taalcode voor UI-elementen.

Tijdfilter — `day` is 24 uur.

Alleen resultaten die na deze datum zijn gepubliceerd (`YYYY-MM-DD`).

Alleen resultaten die vóór deze datum zijn gepubliceerd (`YYYY-MM-DD`).

**Voorbeelden:**

javascriptCopy code
[code]
    // Country and language-specific searchawait web_search({  query: "renewable energy",  country: "DE",  language: "de",}); // Recent results (past week)await web_search({  query: "AI news",  freshness: "week",}); // Date range searchawait web_search({  query: "AI developments",  date_after: "2024-01-01",  date_before: "2024-06-30",});
[/code]

## Opmerkingen

  * OpenClaw gebruikt het Brave **Search** -abonnement. Als je een verouderd abonnement hebt (bijv. het oorspronkelijke Free-abonnement met 2.000 query's/maand), blijft dit geldig, maar het bevat geen nieuwere functies zoals LLM Context of hogere limieten.
  * Elk Brave-abonnement bevat **$5/maand aan gratis tegoed** (vernieuwend). Het Search-abonnement kost $5 per 1.000 verzoeken, dus het tegoed dekt 1.000 query's/maand. Stel je gebruikslimiet in het Brave-dashboard in om onverwachte kosten te voorkomen. Zie de [Brave API-portal](<https://brave.com/search/api/>) voor actuele abonnementen.
  * Het Search-abonnement bevat het LLM Context-endpoint en AI-inferentierechten. Resultaten opslaan om modellen te trainen of af te stemmen vereist een abonnement met expliciete opslagrechten. Zie de Brave [Servicevoorwaarden](<https://api-dashboard.search.brave.com/terms-of-service>).
  * De `llm-context`-modus retourneert gegronde bronitems in plaats van de normale snippetstructuur voor webzoekresultaten.
  * De `llm-context`-modus ondersteunt `freshness` en begrensde `date_after` \+ `date_before`-bereiken. Deze ondersteunt geen `ui_lang`; `date_before` zonder `date_after` wordt geweigerd omdat Brave vereist dat aangepaste versheidsbereiken zowel een begin- als einddatum bevatten.
  * `ui_lang` moet een regiosubtag bevatten, zoals `en-US`.
  * Resultaten worden standaard 15 minuten gecachet (configureerbaar via `cacheTtlMinutes`).
  * Aangepaste `webSearch.baseUrl`-waarden worden opgenomen in de Brave-cache-identiteit, zodat proxyspecifieke antwoorden niet botsen.
  * Schakel de diagnostische vlag `brave.http` in om Brave-verzoek-URL's/queryparameters, responsstatus/timing en zoekcache-hit/miss/write-gebeurtenissen te loggen tijdens probleemoplossing. De vlag logt nooit de API-sleutel of responsbody's, maar zoekquery's kunnen gevoelig zijn.


## Gerelateerd

  * [Overzicht van Web Search](</nl/tools/web>) \-- alle providers en automatische detectie
  * [Perplexity Search](</nl/tools/perplexity-search>) \-- gestructureerde resultaten met domeinfiltering
  * [Exa Search](</nl/tools/exa-search>) \-- neurale zoekfunctie met inhoudsextractie


Was this useful?YesNo