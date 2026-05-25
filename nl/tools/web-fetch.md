---
title: Web ophalen
source_url: https://docs.openclaw.ai/nl/tools/web-fetch
scraped_at: 2026-05-25
---

Het hulpprogramma `web_fetch` voert een gewone HTTP GET uit en extraheert leesbare inhoud (HTML naar markdown of tekst). Het voert **geen** JavaScript uit.

Voor JS-zware sites of pagina's achter een login gebruik je in plaats daarvan de [Webbrowser](</nl/tools/browser>).

## Snel aan de slag

`web_fetch` is **standaard ingeschakeld** \-- er is geen configuratie nodig. De agent kan het meteen aanroepen:

javascriptCopy code
[code]
    await web_fetch({ url: "https://example.com/article" });
[/code]

## Hulpprogrammaparameters

URL om op te halen. Alleen `http(s)`.

Uitvoerindeling na extractie van de hoofdinhoud.

Kort de uitvoer af tot dit aantal tekens.

## Hoe het werkt

* ### Ophalen

Verstuurt een HTTP GET met een Chrome-achtige User-Agent en `Accept-Language` header. Blokkeert prive/interne hostnamen en controleert redirects opnieuw.

* ### Extraheren

Voert Readability (extractie van hoofdinhoud) uit op de HTML-respons.

* ### Fallback (optioneel)

Als Readability mislukt en Firecrawl is geconfigureerd, wordt opnieuw geprobeerd via de Firecrawl API met modus om bots te omzeilen.

* ### Cache

Resultaten worden 15 minuten gecachet (configureerbaar) om herhaald ophalen van dezelfde URL te beperken.

## Configuratie

json5Copy code
[code]
    {  tools: {    web: {      fetch: {        enabled: true, // default: true        provider: "firecrawl", // optional; omit for auto-detect        maxChars: 50000, // max output chars        maxCharsCap: 50000, // hard cap for maxChars param        maxResponseBytes: 2000000, // max download size before truncation        timeoutSeconds: 30,        cacheTtlMinutes: 15,        maxRedirects: 3,        useTrustedEnvProxy: false, // let a trusted HTTP(S) env proxy resolve DNS        readability: true, // use Readability extraction        userAgent: "Mozilla/5.0 ...", // override User-Agent        ssrfPolicy: {          allowRfc2544BenchmarkRange: true, // opt-in for trusted fake-IP proxies using 198.18.0.0/15          allowIpv6UniqueLocalRange: true, // opt-in for trusted fake-IP proxies using fc00::/7        },      },    },  },}
[/code]

## Firecrawl-fallback

Als Readability-extractie mislukt, kan `web_fetch` terugvallen op [Firecrawl](</nl/tools/firecrawl>) voor botomzeiling en betere extractie:

json5Copy code
[code]
    {  tools: {    web: {      fetch: {        provider: "firecrawl", // optional; omit for auto-detect from available credentials      },    },  },  plugins: {    entries: {      firecrawl: {        enabled: true,        config: {          webFetch: {            apiKey: "fc-...", // optional if FIRECRAWL_API_KEY is set            baseUrl: "https://api.firecrawl.dev",            onlyMainContent: true,            maxAgeMs: 86400000, // cache duration (1 day)            timeoutSeconds: 60,          },        },      },    },  },}
[/code]

`plugins.entries.firecrawl.config.webFetch.apiKey` ondersteunt SecretRef-objecten. Verouderde configuratie voor `tools.web.fetch.firecrawl.*` wordt automatisch gemigreerd door `openclaw doctor --fix`.

Huidig runtimegedrag:

  * `tools.web.fetch.provider` selecteert expliciet de fallbackprovider voor ophalen.
  * Als `provider` is weggelaten, detecteert OpenClaw automatisch de eerste gereedstaande web-fetch- provider op basis van beschikbare referenties. Niet-gesandboxte `web_fetch` kan geinstalleerde plugins gebruiken die `contracts.webFetchProviders` declareren en tijdens runtime een overeenkomende provider registreren. Tegenwoordig is Firecrawl de meegeleverde provider.
  * Gesandboxte `web_fetch`-aanroepen blijven beperkt tot meegeleverde providers.
  * Als Readability is uitgeschakeld, springt `web_fetch` direct naar de geselecteerde providerfallback. Als er geen provider beschikbaar is, faalt het gesloten.


## Vertrouwde env-proxy

Als je deployment vereist dat `web_fetch` via een vertrouwde uitgaande HTTP(S)-proxy gaat, stel dan `tools.web.fetch.useTrustedEnvProxy: true` in.

In deze modus past OpenClaw nog steeds hostnaamgebaseerde SSRF-controles toe voordat het verzoek wordt verstuurd, maar laat het de proxy DNS oplossen in plaats van lokale DNS- pinning uit te voeren. Schakel dit alleen in wanneer de proxy door de operator wordt beheerd en uitgaand beleid afdwingt na DNS-resolutie.

## Limieten en veiligheid

  * `maxChars` wordt begrensd tot `tools.web.fetch.maxCharsCap`
  * De responsbody wordt voor het parsen begrensd op `maxResponseBytes`; te grote responsen worden afgekapt met een waarschuwing
  * Prive/interne hostnamen worden geblokkeerd
  * `tools.web.fetch.ssrfPolicy.allowRfc2544BenchmarkRange` en `tools.web.fetch.ssrfPolicy.allowIpv6UniqueLocalRange` zijn beperkte opt-ins voor vertrouwde fake-IP-proxystacks; laat ze oningesteld tenzij je proxy eigenaar is van die synthetische bereiken en zijn eigen bestemmingsbeleid afdwingt
  * Redirects worden gecontroleerd en beperkt door `maxRedirects`
  * `useTrustedEnvProxy` is een expliciete opt-in en mag alleen worden ingeschakeld voor door operators beheerde proxy's die na DNS-resolutie nog steeds uitgaand beleid afdwingen
  * `web_fetch` werkt op basis van best effort -- sommige sites hebben de [Webbrowser](</nl/tools/browser>) nodig


## Hulpprogrammaprofielen

Als je hulpprogrammaprofielen of allowlists gebruikt, voeg dan `web_fetch` of `group:web` toe:

json5Copy code
[code]
    {  tools: {    allow: ["web_fetch"],    // or: allow: ["group:web"]  (includes web_fetch, web_search, and x_search)  },}
[/code]

## Gerelateerd

  * [Webzoekfunctie](</nl/tools/web>) \-- doorzoek het web met meerdere providers
  * [Webbrowser](</nl/tools/browser>) \-- volledige browserautomatisering voor JS-zware sites
  * [Firecrawl](</nl/tools/firecrawl>) \-- zoek- en scrapehulpprogramma's van Firecrawl


Was this useful?YesNo