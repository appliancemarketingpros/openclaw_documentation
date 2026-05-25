---
title: Obtención web
source_url: https://docs.openclaw.ai/es/tools/web-fetch
scraped_at: 2026-05-25
---

La herramienta `web_fetch` realiza un HTTP GET simple y extrae contenido legible (HTML a markdown o texto). **No** ejecuta JavaScript.

Para sitios con mucho JS o páginas protegidas por inicio de sesión, usa el [Navegador web](</es/tools/browser>) en su lugar.

## Inicio rápido

`web_fetch` está **habilitada de forma predeterminada** ; no hace falta configuración. El agente puede llamarla de inmediato:

javascriptCopy code
[code]
    await web_fetch({ url: "https://example.com/article" });
[/code]

## Parámetros de la herramienta

URL que se va a obtener. Solo `http(s)`.

Formato de salida después de la extracción del contenido principal.

Trunca la salida a esta cantidad de caracteres.

## Cómo funciona

* ### Obtener

Envía un HTTP GET con un User-Agent similar al de Chrome y un encabezado `Accept-Language`. Bloquea nombres de host privados/internos y vuelve a comprobar las redirecciones.

* ### Extraer

Ejecuta Readability (extracción de contenido principal) en la respuesta HTML.

* ### Reserva (opcional)

Si Readability falla y Firecrawl está configurado, vuelve a intentarlo mediante la API de Firecrawl con modo de elusión de bots.

* ### Caché

Los resultados se almacenan en caché durante 15 minutos (configurable) para reducir las obtenciones repetidas de la misma URL.

## Configuración

json5Copy code
[code]
    {  tools: {    web: {      fetch: {        enabled: true, // default: true        provider: "firecrawl", // optional; omit for auto-detect        maxChars: 50000, // max output chars        maxCharsCap: 50000, // hard cap for maxChars param        maxResponseBytes: 2000000, // max download size before truncation        timeoutSeconds: 30,        cacheTtlMinutes: 15,        maxRedirects: 3,        useTrustedEnvProxy: false, // let a trusted HTTP(S) env proxy resolve DNS        readability: true, // use Readability extraction        userAgent: "Mozilla/5.0 ...", // override User-Agent        ssrfPolicy: {          allowRfc2544BenchmarkRange: true, // opt-in for trusted fake-IP proxies using 198.18.0.0/15          allowIpv6UniqueLocalRange: true, // opt-in for trusted fake-IP proxies using fc00::/7        },      },    },  },}
[/code]

## Reserva con Firecrawl

Si la extracción de Readability falla, `web_fetch` puede recurrir a [Firecrawl](</es/tools/firecrawl>) para elusión de bots y una mejor extracción:

json5Copy code
[code]
    {  tools: {    web: {      fetch: {        provider: "firecrawl", // optional; omit for auto-detect from available credentials      },    },  },  plugins: {    entries: {      firecrawl: {        enabled: true,        config: {          webFetch: {            apiKey: "fc-...", // optional if FIRECRAWL_API_KEY is set            baseUrl: "https://api.firecrawl.dev",            onlyMainContent: true,            maxAgeMs: 86400000, // cache duration (1 day)            timeoutSeconds: 60,          },        },      },    },  },}
[/code]

`plugins.entries.firecrawl.config.webFetch.apiKey` admite objetos SecretRef. La configuración heredada `tools.web.fetch.firecrawl.*` se migra automáticamente mediante `openclaw doctor --fix`.

Comportamiento actual en tiempo de ejecución:

  * `tools.web.fetch.provider` selecciona explícitamente el proveedor de reserva de obtención.
  * Si se omite `provider`, OpenClaw detecta automáticamente el primer proveedor de web-fetch listo a partir de las credenciales disponibles. `web_fetch` no aislado puede usar plugins instalados que declaren `contracts.webFetchProviders` y registren un proveedor coincidente en tiempo de ejecución. Hoy, el proveedor incluido es Firecrawl.
  * Las llamadas de `web_fetch` aisladas permanecen limitadas a los proveedores incluidos.
  * Si Readability está deshabilitado, `web_fetch` pasa directamente a la reserva del proveedor seleccionado. Si no hay ningún proveedor disponible, falla de forma cerrada.


## Proxy de entorno confiable

Si tu despliegue requiere que `web_fetch` pase por un proxy HTTP(S) saliente confiable, configura `tools.web.fetch.useTrustedEnvProxy: true`.

En este modo, OpenClaw sigue aplicando comprobaciones SSRF basadas en el nombre de host antes de enviar la solicitud, pero permite que el proxy resuelva DNS en lugar de hacer fijación de DNS local. Habilita esto solo cuando el proxy esté controlado por el operador y haga cumplir la política saliente después de la resolución de DNS.

## Límites y seguridad

  * `maxChars` se limita a `tools.web.fetch.maxCharsCap`
  * El cuerpo de la respuesta se limita a `maxResponseBytes` antes del análisis; las respuestas sobredimensionadas se truncan con una advertencia
  * Los nombres de host privados/internos se bloquean
  * `tools.web.fetch.ssrfPolicy.allowRfc2544BenchmarkRange` y `tools.web.fetch.ssrfPolicy.allowIpv6UniqueLocalRange` son permisos explícitos restringidos para pilas de proxy de IP falsa confiables; déjalos sin configurar salvo que tu proxy sea propietario de esos rangos sintéticos y haga cumplir su propia política de destino
  * Las redirecciones se comprueban y se limitan mediante `maxRedirects`
  * `useTrustedEnvProxy` es un permiso explícito y solo debe habilitarse para proxies controlados por el operador que sigan haciendo cumplir la política saliente después de la resolución de DNS
  * `web_fetch` funciona en modalidad de mejor esfuerzo; algunos sitios necesitan el [Navegador web](</es/tools/browser>)


## Perfiles de herramientas

Si usas perfiles de herramientas o listas de permitidos, añade `web_fetch` o `group:web`:

json5Copy code
[code]
    {  tools: {    allow: ["web_fetch"],    // or: allow: ["group:web"]  (includes web_fetch, web_search, and x_search)  },}
[/code]

## Relacionado

  * [Búsqueda web](</es/tools/web>) \-- busca en la web con varios proveedores
  * [Navegador web](</es/tools/browser>) \-- automatización completa del navegador para sitios con mucho JS
  * [Firecrawl](</es/tools/firecrawl>) \-- herramientas de búsqueda y extracción de Firecrawl


Was this useful?YesNo