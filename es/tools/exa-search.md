---
title: Búsqueda de Exa
source_url: https://docs.openclaw.ai/es/tools/exa-search
scraped_at: 2026-05-25
---

OpenClaw admite [Exa AI](<https://exa.ai/>) como proveedor de `web_search`. Exa ofrece modos de búsqueda neural, por palabras clave e híbrida con extracción de contenido integrada (resaltados, texto, resúmenes).

## Obtener una clave de API

* ### Create an account

Regístrate en [exa.ai](<https://exa.ai/>) y genera una clave de API desde tu panel.

* ### Store the key

Establece `EXA_API_KEY` en el entorno del Gateway, o configúralo mediante:

bashCopy code
[code]
    openclaw configure --section web
[/code]

## Configuración

json5Copy code
[code]
    {  plugins: {    entries: {      exa: {        config: {          webSearch: {            apiKey: "exa-...", // optional if EXA_API_KEY is set            baseUrl: "https://api.exa.ai", // optional; OpenClaw appends /search          },        },      },    },  },  tools: {    web: {      search: {        provider: "exa",      },    },  },}
[/code]

**Alternativa de entorno:** establece `EXA_API_KEY` en el entorno del Gateway. Para una instalación del gateway, colócala en `~/.openclaw/.env`.

## Anulación de URL base

Establece `plugins.entries.exa.config.webSearch.baseUrl` cuando las solicitudes de búsqueda de Exa deban pasar por un proxy compatible o un endpoint alternativo de Exa. OpenClaw normaliza los hosts sin esquema anteponiendo `https://` y añade `/search` a menos que la ruta ya termine allí. El endpoint resuelto se incluye en la clave de caché de búsqueda, por lo que los resultados de distintos endpoints de Exa no se comparten.

## Parámetros de la herramienta

Consulta de búsqueda.

Resultados que se devolverán (1–100).

Modo de búsqueda.

Filtro de tiempo.

Resultados posteriores a esta fecha (`YYYY-MM-DD`).

Resultados anteriores a esta fecha (`YYYY-MM-DD`).

Opciones de extracción de contenido (ver más abajo).

### Extracción de contenido

Exa puede devolver contenido extraído junto con los resultados de búsqueda. Pasa un objeto `contents` para activarlo:

javascriptCopy code
[code]
    await web_search({  query: "transformer architecture explained",  type: "neural",  contents: {    text: true, // full page text    highlights: { numSentences: 3 }, // key sentences    summary: true, // AI summary  },});
[/code]

Opción de contents | Tipo | Descripción  
---|---|---  
`text` | `boolean | { maxCharacters }` | Extraer texto completo de la página  
`highlights` | `boolean | { maxCharacters, query, numSentences, highlightsPerUrl }` | Extraer frases clave  
`summary` | `boolean | { query }` | Resumen generado por IA  
  
### Modos de búsqueda

Modo | Descripción  
---|---  
`auto` | Exa elige el mejor modo (predeterminado)  
`neural` | Búsqueda semántica/basada en significado  
`fast` | Búsqueda rápida por palabras clave  
`deep` | Búsqueda profunda y exhaustiva  
`deep-reasoning` | Búsqueda profunda con razonamiento  
`instant` | Resultados más rápidos  
  
## Notas

  * Si no se proporciona ninguna opción de `contents`, Exa usa de forma predeterminada `{ highlights: true }` para que los resultados incluyan extractos de frases clave
  * Los resultados conservan los campos `highlightScores` y `summary` de la respuesta de la API de Exa cuando están disponibles
  * Las descripciones de los resultados se resuelven primero a partir de los resaltados, luego del resumen y luego del texto completo — lo que esté disponible
  * `freshness` y `date_after`/`date_before` no se pueden combinar — usa un solo modo de filtro temporal
  * Se pueden devolver hasta 100 resultados por consulta (sujeto a los límites de tipo de búsqueda de Exa)
  * Los resultados se almacenan en caché durante 15 minutos de forma predeterminada (configurable mediante `cacheTtlMinutes`)
  * Exa es una integración oficial de API con respuestas JSON estructuradas


## Relacionado

  * [Resumen de Web Search](</es/tools/web>) \-- todos los proveedores y detección automática
  * [Brave Search](</es/tools/brave-search>) \-- resultados estructurados con filtros de país/idioma
  * [Perplexity Search](</es/tools/perplexity-search>) \-- resultados estructurados con filtrado de dominios


Was this useful?YesNo