---
title: Ollama-webzoekfunctie
source_url: https://docs.openclaw.ai/nl/tools/ollama-search
scraped_at: 2026-05-25
---

OpenClaw ondersteunt **Ollama Web Search** als een meegeleverde `web_search`-provider. Deze gebruikt de webzoek-API van Ollama en retourneert gestructureerde resultaten met titels, URL's en fragmenten.

Voor lokale of zelf gehoste Ollama heeft deze configuratie standaard geen API-sleutel nodig. Wel vereist dit:

  * een Ollama-host die bereikbaar is vanuit OpenClaw
  * `ollama signin`


Voor direct gehost zoeken stelt u de basis-URL van de Ollama-provider in op `https://ollama.com` en geeft u een echte `OLLAMA_API_KEY` op.

## Configuratie

* ### Start Ollama

Zorg dat Ollama is geinstalleerd en actief is.

* ### Sign in

Voer uit:

bashCopy code
[code]
    ollama signin
[/code]

* ### Choose Ollama Web Search

Voer uit:

bashCopy code
[code]
    openclaw configure --section web
[/code]

Selecteer vervolgens **Ollama Web Search** als provider.

Als u Ollama al voor modellen gebruikt, hergebruikt Ollama Web Search dezelfde geconfigureerde host.

## Configuratie

json5Copy code
[code]
    {  tools: {    web: {      search: {        provider: "ollama",      },    },  },}
[/code]

Optionele override voor de Ollama-host:

json5Copy code
[code]
    {  plugins: {    entries: {      ollama: {        config: {          webSearch: {            baseUrl: "http://ollama-host:11434",          },        },      },    },  },}
[/code]

Als u Ollama al als modelprovider configureert, kan de webzoek-provider in plaats daarvan die host hergebruiken:

json5Copy code
[code]
    {  models: {    providers: {      ollama: {        baseUrl: "http://ollama-host:11434",      },    },  },}
[/code]

De Ollama-modelprovider gebruikt `baseUrl` als canonieke sleutel. De webzoek-provider respecteert ook `baseURL` op `models.providers.ollama` voor compatibiliteit met configuratievoorbeelden in OpenAI SDK-stijl.

Als er geen expliciete Ollama-basis-URL is ingesteld, gebruikt OpenClaw `http://127.0.0.1:11434`.

Als uw Ollama-host bearer-authenticatie verwacht, hergebruikt OpenClaw `models.providers.ollama.apiKey` (of de overeenkomende door env ondersteunde provider-authenticatie) voor verzoeken naar die geconfigureerde host.

Direct gehoste Ollama Web Search:

json5Copy code
[code]
    {  models: {    providers: {      ollama: {        baseUrl: "https://ollama.com",        apiKey: "OLLAMA_API_KEY",      },    },  },  tools: {    web: {      search: {        provider: "ollama",      },    },  },}
[/code]

## Opmerkingen

  * Voor deze provider is geen webzoek-specifiek API-sleutelveld vereist.
  * Als de Ollama-host met authenticatie is beveiligd, hergebruikt OpenClaw de normale API-sleutel van de Ollama-provider wanneer die aanwezig is.
  * Als `baseUrl` `https://ollama.com` is, roept OpenClaw `https://ollama.com/api/web_search` rechtstreeks aan en verzendt het de geconfigureerde Ollama-API-sleutel als bearer-authenticatie.
  * Als de geconfigureerde host geen webzoekfunctie beschikbaar stelt en `OLLAMA_API_KEY` is ingesteld, kan OpenClaw terugvallen op `https://ollama.com/api/web_search` zonder die env-sleutel naar de lokale host te verzenden.
  * OpenClaw waarschuwt tijdens de configuratie als Ollama niet bereikbaar is of niet is aangemeld, maar blokkeert de selectie niet.
  * Automatische detectie tijdens runtime kan terugvallen op Ollama Web Search wanneer er geen geconfigureerde provider met referenties en hogere prioriteit is.
  * Lokale Ollama-daemonhosts gebruiken het lokale proxy-eindpunt `/api/experimental/web_search`, dat ondertekent en doorstuurt naar Ollama Cloud.
  * `https://ollama.com`-hosts gebruiken het openbare gehoste eindpunt `/api/web_search` rechtstreeks met bearer-API-sleutelauthenticatie.


## Gerelateerd

  * [Overzicht van webzoekfunctie](</nl/tools/web>) \-- alle providers en automatische detectie
  * [Ollama](</nl/providers/ollama>) \-- configuratie van Ollama-modellen en cloud-/lokale modi


Was this useful?YesNo