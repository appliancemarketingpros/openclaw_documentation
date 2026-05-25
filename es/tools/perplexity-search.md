---
title: Búsqueda de Perplexity
source_url: https://docs.openclaw.ai/es/tools/perplexity-search
scraped_at: 2026-05-25
---

OpenClaw admite Perplexity Search API como proveedor de `web_search`. Devuelve resultados estructurados con los campos `title`, `url` y `snippet`.

Por compatibilidad, OpenClaw también admite configuraciones heredadas de Perplexity Sonar/OpenRouter. Si usas `OPENROUTER_API_KEY`, una clave `sk-or-...` en `plugins.entries.perplexity.config.webSearch.apiKey`, o defines `plugins.entries.perplexity.config.webSearch.baseUrl` / `model`, el proveedor cambia a la ruta de chat completions y devuelve respuestas sintetizadas por IA con citas en lugar de resultados estructurados de Search API.

## Obtener una clave de API de Perplexity

  1. Crea una cuenta de Perplexity en [perplexity.ai/settings/api](<https://www.perplexity.ai/settings/api>)
  2. Genera una clave de API en el panel
  3. Guarda la clave en la configuración o define `PERPLEXITY_API_KEY` en el entorno del Gateway.


## Compatibilidad con OpenRouter

Si ya estabas usando OpenRouter para Perplexity Sonar, conserva `provider: "perplexity"` y define `OPENROUTER_API_KEY` en el entorno del Gateway, o guarda una clave `sk-or-...` en `plugins.entries.perplexity.config.webSearch.apiKey`.

Controles opcionales de compatibilidad:

  * `plugins.entries.perplexity.config.webSearch.baseUrl`
  * `plugins.entries.perplexity.config.webSearch.model`


## Ejemplos de configuración

### Perplexity Search API nativa

json5Copy code
[code]
    {  plugins: {    entries: {      perplexity: {        config: {          webSearch: {            apiKey: "pplx-...",          },        },      },    },  },  tools: {    web: {      search: {        provider: "perplexity",      },    },  },}
[/code]

### Compatibilidad con OpenRouter / Sonar

json5Copy code
[code]
    {  plugins: {    entries: {      perplexity: {        config: {          webSearch: {            apiKey: "<openrouter-api-key>",            baseUrl: "https://openrouter.ai/api/v1",            model: "perplexity/sonar-pro",          },        },      },    },  },  tools: {    web: {      search: {        provider: "perplexity",      },    },  },}
[/code]

## Dónde definir la clave

**Mediante configuración:** ejecuta `openclaw configure --section web`. Guarda la clave en `~/.openclaw/openclaw.json` dentro de `plugins.entries.perplexity.config.webSearch.apiKey`. Ese campo también acepta objetos SecretRef.

**Mediante entorno:** define `PERPLEXITY_API_KEY` o `OPENROUTER_API_KEY` en el entorno del proceso del Gateway. Para una instalación de gateway, colócalo en `~/.openclaw/.env` (o en el entorno de tu servicio). Consulta [variables de entorno](</es/help/faq#env-vars-and-env-loading>).

Si `provider: "perplexity"` está configurado y el SecretRef de la clave de Perplexity no se resuelve y no hay alternativa en el entorno, el inicio o la recarga falla rápidamente.

## Parámetros de la herramienta

Estos parámetros se aplican a la ruta nativa de Perplexity Search API.

Consulta de búsqueda.

Número de resultados que devolver (1-10).

Código de país ISO de 2 letras (p. ej., `US`, `DE`).

Código de idioma ISO 639-1 (p. ej., `en`, `de`, `fr`).

Filtro de tiempo: `day` equivale a 24 horas.

Solo resultados publicados después de esta fecha (`YYYY-MM-DD`).

Solo resultados publicados antes de esta fecha (`YYYY-MM-DD`).

Array de dominios permitidos o denegados (máx. 20).

Presupuesto total de contenido (máx. 1000000).

Límite de tokens por página.

Para la ruta de compatibilidad heredada de Sonar/OpenRouter:

  * se aceptan `query`, `count` y `freshness`
  * `count` allí es solo para compatibilidad; la respuesta sigue siendo una única respuesta sintetizada con citas, en lugar de una lista de N resultados
  * los filtros exclusivos de Search API como `country`, `language`, `date_after`, `date_before`, `domain_filter`, `max_tokens` y `max_tokens_per_page` devuelven errores explícitos


**Ejemplos:**

javascriptCopy code
[code]
    // Country and language-specific searchawait web_search({  query: "renewable energy",  country: "DE",  language: "de",}); // Recent results (past week)await web_search({  query: "AI news",  freshness: "week",}); // Date range searchawait web_search({  query: "AI developments",  date_after: "2024-01-01",  date_before: "2024-06-30",}); // Domain filtering (allowlist)await web_search({  query: "climate research",  domain_filter: ["nature.com", "science.org", ".edu"],}); // Domain filtering (denylist - prefix with -)await web_search({  query: "product reviews",  domain_filter: ["-reddit.com", "-pinterest.com"],}); // More content extractionawait web_search({  query: "detailed AI research",  max_tokens: 50000,  max_tokens_per_page: 4096,});
[/code]

### Reglas de filtro de dominios

  * Máximo de 20 dominios por filtro
  * No se pueden mezclar listas de permitidos y listas de denegados en la misma solicitud
  * Usa el prefijo `-` para las entradas de lista de denegados (p. ej., `["-reddit.com"]`)


## Notas

  * Perplexity Search API devuelve resultados estructurados de búsqueda web (`title`, `url`, `snippet`)
  * OpenRouter o `plugins.entries.perplexity.config.webSearch.baseUrl` / `model` explícitos vuelven a cambiar Perplexity a chat completions de Sonar por compatibilidad
  * La compatibilidad con Sonar/OpenRouter devuelve una respuesta sintetizada con citas, no filas de resultados estructurados
  * Los resultados se almacenan en caché durante 15 minutos de forma predeterminada (configurable mediante `cacheTtlMinutes`)


## Relacionado

[**Web search overview** Todos los proveedores y reglas de detección automática. ](</es/tools/web>) [**Brave search** Resultados estructurados con filtros de país e idioma. ](</es/tools/brave-search>) [**Exa search** Búsqueda neuronal con extracción de contenido. ](</es/tools/exa-search>) [**Perplexity Search API docs** Guía de inicio rápido y referencia oficiales de Perplexity Search API. ](<https://docs.perplexity.ai/docs/search/quickstart>)

Was this useful?YesNo