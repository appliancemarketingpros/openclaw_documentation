---
title: Firecrawl
source_url: https://docs.openclaw.ai/es/tools/firecrawl
scraped_at: 2026-05-25
---

OpenClaw puede usar **Firecrawl** de tres maneras:

  * como proveedor de `web_search`
  * como herramientas explícitas de Plugin: `firecrawl_search` y `firecrawl_scrape`
  * como extractor de respaldo para `web_fetch`


Es un servicio alojado de extracción/búsqueda que admite evasión de bots y almacenamiento en caché, lo que ayuda con sitios con mucho JS o páginas que bloquean las recuperaciones HTTP simples.

## Obtener una clave de API

  1. Crea una cuenta de Firecrawl y genera una clave de API.
  2. Guárdala en la configuración o define `FIRECRAWL_API_KEY` en el entorno del Gateway.


## Configurar la búsqueda con Firecrawl

json5Copy code
[code]
    {  tools: {    web: {      search: {        provider: "firecrawl",      },    },  },  plugins: {    entries: {      firecrawl: {        enabled: true,        config: {          webSearch: {            apiKey: "FIRECRAWL_API_KEY_HERE",            baseUrl: "https://api.firecrawl.dev",          },        },      },    },  },}
[/code]

Notas:

  * Elegir Firecrawl durante la incorporación o con `openclaw configure --section web` habilita automáticamente el Plugin de Firecrawl incluido.
  * `web_search` con Firecrawl admite `query` y `count`.
  * Para controles específicos de Firecrawl como `sources`, `categories` o extracción de resultados, usa `firecrawl_search`.
  * `baseUrl` usa de forma predeterminada el Firecrawl alojado en `https://api.firecrawl.dev`. Las sustituciones autoalojadas solo se permiten para endpoints privados/internos; HTTP se acepta solo para esos destinos privados.
  * `FIRECRAWL_BASE_URL` es el respaldo compartido de entorno para las URL base de búsqueda y extracción de Firecrawl.


## Configurar la extracción de Firecrawl + respaldo de web_fetch

json5Copy code
[code]
    {  plugins: {    entries: {      firecrawl: {        enabled: true,        config: {          webFetch: {            apiKey: "FIRECRAWL_API_KEY_HERE",            baseUrl: "https://api.firecrawl.dev",            onlyMainContent: true,            maxAgeMs: 172800000,            timeoutSeconds: 60,          },        },      },    },  },}
[/code]

Notas:

  * Los intentos de respaldo de Firecrawl se ejecutan solo cuando hay una clave de API disponible (`plugins.entries.firecrawl.config.webFetch.apiKey` o `FIRECRAWL_API_KEY`).
  * `maxAgeMs` controla qué tan antiguos pueden ser los resultados almacenados en caché (ms). El valor predeterminado es 2 días.
  * La configuración heredada `tools.web.fetch.firecrawl.*` se migra automáticamente con `openclaw doctor --fix`.
  * Las sustituciones de URL base/extracción de Firecrawl siguen la misma regla alojado/privado que la búsqueda: el tráfico alojado público usa `https://api.firecrawl.dev`; las sustituciones autoalojadas deben resolverse a endpoints privados/internos.
  * `firecrawl_scrape` rechaza URL de destino obviamente privadas, de loopback, de metadatos y que no sean HTTP(S) antes de reenviarlas a Firecrawl, de acuerdo con el contrato de seguridad de destino de `web_fetch` para llamadas explícitas de extracción de Firecrawl.


`firecrawl_scrape` reutiliza la misma configuración `plugins.entries.firecrawl.config.webFetch.*` y las mismas variables de entorno.

### Firecrawl autoalojado

Define `plugins.entries.firecrawl.config.webSearch.baseUrl`, `plugins.entries.firecrawl.config.webFetch.baseUrl` o `FIRECRAWL_BASE_URL` cuando ejecutes Firecrawl por tu cuenta. OpenClaw acepta `http://` solo para destinos de loopback, red privada, `.local`, `.internal` o `.localhost`. Los hosts personalizados públicos se rechazan para que las claves de API de Firecrawl no se envíen por accidente a endpoints arbitrarios.

## Herramientas del Plugin de Firecrawl

### `firecrawl_search`

Usa esto cuando quieras controles de búsqueda específicos de Firecrawl en lugar del `web_search` genérico.

Parámetros principales:

  * `query`
  * `count`
  * `sources`
  * `categories`
  * `scrapeResults`
  * `timeoutSeconds`


### `firecrawl_scrape`

Usa esto para páginas con mucho JS o protegidas contra bots donde el `web_fetch` simple es débil.

Parámetros principales:

  * `url`
  * `extractMode`
  * `maxChars`
  * `onlyMainContent`
  * `maxAgeMs`
  * `proxy`
  * `storeInCache`
  * `timeoutSeconds`


## Sigilo / evasión de bots

Firecrawl expone un parámetro de **modo proxy** para la evasión de bots (`basic`, `stealth` o `auto`). OpenClaw siempre usa `proxy: "auto"` más `storeInCache: true` para las solicitudes de Firecrawl. Si se omite proxy, Firecrawl usa `auto` de forma predeterminada. `auto` reintenta con proxies sigilosos si falla un intento básico, lo que puede consumir más créditos que la extracción solo básica.

## Cómo `web_fetch` usa Firecrawl

Orden de extracción de `web_fetch`:

  1. Readability (local)
  2. Firecrawl (si se selecciona o se detecta automáticamente como respaldo activo de web-fetch)
  3. Limpieza básica de HTML (último respaldo)


El control de selección es `tools.web.fetch.provider`. Si lo omites, OpenClaw detecta automáticamente el primer proveedor de web-fetch listo a partir de las credenciales disponibles. Actualmente, el proveedor incluido es Firecrawl.

## Relacionado

  * [Resumen de Web Search](</es/tools/web>) \-- todos los proveedores y la detección automática
  * [Web Fetch](</es/tools/web-fetch>) \-- herramienta web_fetch con respaldo de Firecrawl
  * [Tavily](</es/tools/tavily>) \-- herramientas de búsqueda + extracción


Was this useful?YesNo