---
title: Búsqueda de DuckDuckGo
source_url: https://docs.openclaw.ai/es/tools/duckduckgo-search
scraped_at: 2026-05-25
---

OpenClaw admite DuckDuckGo como proveedor `web_search` **sin clave**. No se requiere clave de API ni cuenta.

## Configuración

No se necesita clave de API: solo configura DuckDuckGo como tu proveedor:

* ### Configure

bashCopy code
[code]
    openclaw configure --section web# Select "duckduckgo" as the provider
[/code]

## Configuración

json5Copy code
[code]
    {  tools: {    web: {      search: {        provider: "duckduckgo",      },    },  },}
[/code]

Ajustes opcionales a nivel de Plugin para región y SafeSearch:

json5Copy code
[code]
    {  plugins: {    entries: {      duckduckgo: {        config: {          webSearch: {            region: "us-en", // DuckDuckGo region code            safeSearch: "moderate", // "strict", "moderate", or "off"          },        },      },    },  },}
[/code]

## Parámetros de la herramienta

Consulta de búsqueda.

Resultados que se devolverán (1-10).

Código de región de DuckDuckGo (p. ej., `us-en`, `uk-en`, `de-de`).

Nivel de SafeSearch.

La región y SafeSearch también se pueden establecer en la configuración del Plugin (ver arriba); los parámetros de la herramienta anulan los valores de configuración por consulta.

## Notas

  * **Sin clave de API** : funciona de inmediato, sin configuración
  * **Experimental** : recopila resultados de las páginas de búsqueda HTML sin JavaScript de DuckDuckGo, no de una API ni un SDK oficiales
  * **Riesgo de verificación de bots** : DuckDuckGo puede mostrar CAPTCHA o bloquear solicitudes durante un uso intensivo o automatizado
  * **Análisis de HTML** : los resultados dependen de la estructura de la página, que puede cambiar sin previo aviso
  * **Orden de detección automática** : DuckDuckGo es la primera alternativa sin clave (orden 100) en la detección automática. Los proveedores respaldados por API con claves configuradas se ejecutan primero, luego Ollama Web Search (orden 110) y después SearXNG (orden 200)
  * **SafeSearch usa moderate de forma predeterminada** cuando no está configurado


## Relacionado

  * [Descripción general de Web Search](</es/tools/web>) \-- todos los proveedores y detección automática
  * [Brave Search](</es/tools/brave-search>) \-- resultados estructurados con nivel gratuito
  * [Exa Search](</es/tools/exa-search>) \-- búsqueda neuronal con extracción de contenido


Was this useful?YesNo