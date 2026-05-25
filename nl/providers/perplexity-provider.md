---
title: Perplexity
source_url: https://docs.openclaw.ai/nl/providers/perplexity-provider
scraped_at: 2026-05-25
---

De Perplexity Plugin biedt webzoekmogelijkheden via de Perplexity Search API of Perplexity Sonar via OpenRouter.

Eigenschap | Waarde  
---|---  
Type | Webzoekprovider (geen modelprovider)  
Auth | `PERPLEXITY_API_KEY` (direct) of `OPENROUTER_API_KEY` (via OpenRouter)  
Config-pad | `plugins.entries.perplexity.config.webSearch.apiKey`  
  
## Aan de slag

* ### Stel de API-sleutel in

Voer de interactieve configuratiestroom voor webzoeken uit:

bashCopy code
[code]
    openclaw configure --section web
[/code]

Of stel de sleutel direct in:

bashCopy code
[code]
    openclaw config set plugins.entries.perplexity.config.webSearch.apiKey "pplx-xxxxxxxxxxxx"
[/code]

* ### Begin met zoeken

De agent gebruikt Perplexity automatisch voor webzoekopdrachten zodra de sleutel is geconfigureerd. Er zijn geen extra stappen vereist.

## Zoekmodi

De Plugin selecteert automatisch het transport op basis van het API-sleutelvoorvoegsel:

### Native Perplexity API (pplx-)

Wanneer je sleutel begint met `pplx-`, gebruikt OpenClaw de native Perplexity Search API. Dit transport retourneert gestructureerde resultaten en ondersteunt domein-, taal- en datumfilters (zie de filteropties hieronder).

### OpenRouter / Sonar (sk-or-)

Wanneer je sleutel begint met `sk-or-`, routeert OpenClaw via OpenRouter met het Perplexity Sonar-model. Dit transport retourneert door AI samengestelde antwoorden met citaties.

Sleutelvoorvoegsel | Transport | Functies  
---|---|---  
`pplx-` | Native Perplexity Search API | Gestructureerde resultaten, domein-/taal-/datumfilters  
`sk-or-` | OpenRouter (Sonar) | Door AI samengestelde antwoorden met citaties  
  
## Native API-filtering

Wanneer je de native Perplexity API gebruikt, ondersteunen zoekopdrachten de volgende filters:

Filter | Beschrijving | Voorbeeld  
---|---|---  
Land | 2-letterige landcode | `us`, `de`, `jp`  
Taal | ISO 639-1-taalcode | `en`, `fr`, `zh`  
Datumbereik | Recentheidsvenster | `day`, `week`, `month`, `year`  
Domeinfilters | Allowlist of denylist (max. 20 domeinen) | `example.com`  
Contentbudget | Tokenlimieten per respons / per pagina | `max_tokens`, `max_tokens_per_page`  
  
## Geavanceerde configuratie

Omgevingsvariabele voor daemonprocessen

Als de OpenClaw Gateway als daemon draait (launchd/systemd), zorg er dan voor dat `PERPLEXITY_API_KEY` beschikbaar is voor dat proces.

OpenRouter-proxyconfiguratie

Als je Perplexity-zoekopdrachten liever via OpenRouter routeert, stel dan een `OPENROUTER_API_KEY` (voorvoegsel `sk-or-`) in in plaats van een native Perplexity-sleutel. OpenClaw detecteert het voorvoegsel en schakelt automatisch over naar het Sonar-transport.

## Gerelateerd

[**Perplexity-zoektool** Hoe de agent Perplexity-zoekopdrachten aanroept en resultaten interpreteert. ](</nl/tools/perplexity-search>) [**Configuratiereferentie** Volledige configuratiereferentie inclusief Plugin-vermeldingen. ](</nl/gateway/configuration-reference>)

Was this useful?YesNo