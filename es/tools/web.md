---
title: Búsqueda web
source_url: https://docs.openclaw.ai/es/tools/web
scraped_at: 2026-05-25
---

La herramienta `web_search` busca en la web usando tu proveedor configurado y devuelve resultados. Los resultados se almacenan en caché por consulta durante 15 minutos (configurable).

OpenClaw también incluye `x_search` para publicaciones de X (anteriormente Twitter) y `web_fetch` para obtención ligera de URL. En esta fase, `web_fetch` permanece local mientras que `web_search` y `x_search` pueden usar xAI Responses internamente.

## Inicio rápido

* ### Choose a provider

Elige un proveedor y completa cualquier configuración requerida. Algunos proveedores no requieren clave, mientras que otros usan claves de API. Consulta las páginas de proveedores a continuación para obtener detalles.

* ### Configure

bashCopy code
[code]
    openclaw configure --section web
[/code]

Esto almacena el proveedor y cualquier credencial necesaria. También puedes definir una variable de entorno (por ejemplo `BRAVE_API_KEY`) y omitir este paso para proveedores respaldados por API.

* ### Use it

El agente ahora puede llamar a `web_search`:

javascriptCopy code
[code]
    await web_search({ query: "OpenClaw plugin SDK" });
[/code]

Para publicaciones de X, usa:

javascriptCopy code
[code]
    await x_search({ query: "dinner recipes" });
[/code]

## Elegir un proveedor

[**Brave Search** Resultados estructurados con fragmentos. Admite el modo `llm-context` y filtros de país/idioma. Nivel gratuito disponible. ](</es/tools/brave-search>) [**DuckDuckGo** Alternativa sin clave. No se necesita clave de API. Integración no oficial basada en HTML. ](</es/tools/duckduckgo-search>) [**Exa** Búsqueda neuronal + por palabras clave con extracción de contenido (resaltados, texto, resúmenes). ](</es/tools/exa-search>) [**Firecrawl** Resultados estructurados. Funciona mejor junto con `firecrawl_search` y `firecrawl_scrape` para extracción profunda. ](</es/tools/firecrawl>) [**Gemini** Respuestas sintetizadas por IA con citas mediante fundamentación de Google Search. ](</es/tools/gemini-search>) [**Grok** Respuestas sintetizadas por IA con citas mediante fundamentación web de xAI. ](</es/tools/grok-search>) [**Kimi** Respuestas sintetizadas por IA con citas mediante búsqueda web de Moonshot; las alternativas de chat sin fundamentación fallan explícitamente. ](</es/tools/kimi-search>) [**MiniMax Search** Resultados estructurados mediante la API de búsqueda de MiniMax Token Plan. ](</es/tools/minimax-search>) [**Ollama Web Search** Búsqueda mediante un host local de Ollama con sesión iniciada o la API alojada de Ollama. ](</es/tools/ollama-search>) [**Perplexity** Resultados estructurados con controles de extracción de contenido y filtrado de dominios. ](</es/tools/perplexity-search>) [**SearXNG** Metabúsqueda autoalojada. No se necesita clave de API. Agrega Google, Bing, DuckDuckGo y más. ](</es/tools/searxng-search>) [**Tavily** Resultados estructurados con profundidad de búsqueda, filtrado por tema y `tavily_extract` para extracción de URL. ](</es/tools/tavily>)

### Comparación de proveedores

Proveedor | Estilo de resultado | Filtros | Clave de API  
---|---|---|---  
[Brave](</es/tools/brave-search>) | Fragmentos estructurados | País, idioma, tiempo, modo `llm-context` | `BRAVE_API_KEY`  
[DuckDuckGo](</es/tools/duckduckgo-search>) | Fragmentos estructurados | \-- | Ninguna (sin clave)  
[Exa](</es/tools/exa-search>) | Estructurado + extraído | Modo neuronal/por palabras clave, fecha, extracción de contenido | `EXA_API_KEY`  
[Firecrawl](</es/tools/firecrawl>) | Fragmentos estructurados | Mediante la herramienta `firecrawl_search` | `FIRECRAWL_API_KEY`  
[Gemini](</es/tools/gemini-search>) | Sintetizado por IA + citas | \-- | `GEMINI_API_KEY`  
[Grok](</es/tools/grok-search>) | Sintetizado por IA + citas | \-- | `XAI_API_KEY`  
[Kimi](</es/tools/kimi-search>) | Sintetizado por IA + citas; falla en alternativas de chat sin fundamentación | \-- | `KIMI_API_KEY` / `MOONSHOT_API_KEY`  
[MiniMax Search](</es/tools/minimax-search>) | Fragmentos estructurados | Región (`global` / `cn`) | `MINIMAX_CODE_PLAN_KEY` / `MINIMAX_CODING_API_KEY` / `MINIMAX_OAUTH_TOKEN`  
[Ollama Web Search](</es/tools/ollama-search>) | Fragmentos estructurados | \-- | Ninguna para hosts locales con sesión iniciada; `OLLAMA_API_KEY` para búsqueda directa en `https://ollama.com`  
[Perplexity](</es/tools/perplexity-search>) | Fragmentos estructurados | País, idioma, tiempo, dominios, límites de contenido | `PERPLEXITY_API_KEY` / `OPENROUTER_API_KEY`  
[SearXNG](</es/tools/searxng-search>) | Fragmentos estructurados | Categorías, idioma | Ninguna (autoalojado)  
[Tavily](</es/tools/tavily>) | Fragmentos estructurados | Mediante la herramienta `tavily_search` | `TAVILY_API_KEY`  
  
## Detección automática

## Búsqueda web nativa de OpenAI

Los modelos directos de OpenAI Responses usan automáticamente la herramienta `web_search` alojada de OpenAI cuando la búsqueda web de OpenClaw está habilitada y no hay un proveedor gestionado fijado. Este es un comportamiento propiedad del proveedor en el Plugin de OpenAI incluido y solo se aplica al tráfico nativo de la API de OpenAI, no a URL base de proxy compatibles con OpenAI ni a rutas de Azure. Define `tools.web.search.provider` en otro proveedor como `brave` para conservar la herramienta `web_search` gestionada para modelos de OpenAI, o define `tools.web.search.enabled: false` para deshabilitar tanto la búsqueda gestionada como la búsqueda nativa de OpenAI.

## Búsqueda web nativa de Codex

Los modelos compatibles con Codex pueden usar opcionalmente la herramienta `web_search` de Responses nativa del proveedor en lugar de la función `web_search` gestionada de OpenClaw.

  * Configúrala en `tools.web.search.openaiCodex`
  * Solo se activa para modelos compatibles con Codex (`openai-codex/*` o proveedores que usan `api: "openai-codex-responses"`)
  * `web_search` gestionado sigue aplicándose a modelos que no son Codex
  * `mode: "cached"` es la configuración predeterminada y recomendada
  * `tools.web.search.enabled: false` deshabilita tanto la búsqueda gestionada como la nativa

json5Copy code
[code]
    {  tools: {    web: {      search: {        enabled: true,        openaiCodex: {          enabled: true,          mode: "cached",          allowedDomains: ["example.com"],          contextSize: "high",          userLocation: {            country: "US",            city: "New York",            timezone: "America/New_York",          },        },      },    },  },}
[/code]

Si la búsqueda nativa de Codex está habilitada pero el modelo actual no es compatible con Codex, OpenClaw mantiene el comportamiento normal de `web_search` gestionado.

## Seguridad de red

Las llamadas a proveedores de `web_search` gestionado usan la ruta de fetch protegida de OpenClaw. Para hosts de API de proveedores de confianza, OpenClaw permite respuestas DNS fake-IP de Surge, Clash y sing-box en `198.18.0.0/15` y `fc00::/7` solo para ese nombre de host de proveedor. Otros destinos privados, de loopback, link-local y de metadatos permanecen bloqueados.

Esta concesión automática no se aplica a URL arbitrarias de `web_fetch`. Para `web_fetch`, habilita `tools.web.fetch.ssrfPolicy.allowRfc2544BenchmarkRange` y `tools.web.fetch.ssrfPolicy.allowIpv6UniqueLocalRange` explícitamente solo cuando tu proxy de confianza sea propietario de esos rangos sintéticos.

## Configurar la búsqueda web

Las listas de proveedores en la documentación y los flujos de configuración están en orden alfabético. La detección automática mantiene un orden de precedencia separado.

Si no se define ningún `provider`, OpenClaw comprueba los proveedores en este orden y usa el primero que esté listo:

Primero los proveedores respaldados por API:

  1. **Brave** \-- `BRAVE_API_KEY` o `plugins.entries.brave.config.webSearch.apiKey` (orden 10)
  2. **MiniMax Search** \-- `MINIMAX_CODE_PLAN_KEY` / `MINIMAX_CODING_API_KEY` / `MINIMAX_OAUTH_TOKEN` / `MINIMAX_API_KEY` o `plugins.entries.minimax.config.webSearch.apiKey` (orden 15)
  3. **Gemini** \-- `plugins.entries.google.config.webSearch.apiKey`, `GEMINI_API_KEY` o `models.providers.google.apiKey` (orden 20)
  4. **Grok** \-- `XAI_API_KEY` o `plugins.entries.xai.config.webSearch.apiKey` (orden 30)
  5. **Kimi** \-- `KIMI_API_KEY` / `MOONSHOT_API_KEY` o `plugins.entries.moonshot.config.webSearch.apiKey` (orden 40)
  6. **Perplexity** \-- `PERPLEXITY_API_KEY` / `OPENROUTER_API_KEY` o `plugins.entries.perplexity.config.webSearch.apiKey` (orden 50)
  7. **Firecrawl** \-- `FIRECRAWL_API_KEY` o `plugins.entries.firecrawl.config.webSearch.apiKey` (orden 60)
  8. **Exa** \-- `EXA_API_KEY` o `plugins.entries.exa.config.webSearch.apiKey`; `plugins.entries.exa.config.webSearch.baseUrl` opcional anula el endpoint de Exa (orden 65)
  9. **Tavily** \-- `TAVILY_API_KEY` o `plugins.entries.tavily.config.webSearch.apiKey` (orden 70)


Alternativas sin clave después de eso:

  10. **DuckDuckGo** \-- alternativa HTML sin clave, sin cuenta ni clave de API (orden 100)
  11. **Ollama Web Search** \-- alternativa sin clave mediante tu host local de Ollama configurado cuando está accesible y con sesión iniciada con `ollama signin`; puede reutilizar la autenticación bearer del proveedor de Ollama cuando el host la necesita, y puede llamar a la búsqueda directa en `https://ollama.com` cuando se configura con `OLLAMA_API_KEY` (orden 110)
  12. **SearXNG** \-- `SEARXNG_BASE_URL` o `plugins.entries.searxng.config.webSearch.baseUrl` (orden 200)


Si no se detecta ningún proveedor, vuelve a Brave (recibirás un error de clave faltante que te pedirá configurar una).

## Configuración

json5Copy code
[code]
    {  tools: {    web: {      search: {        enabled: true, // default: true        provider: "brave", // or omit for auto-detection        maxResults: 5,        timeoutSeconds: 30,        cacheTtlMinutes: 15,      },    },  },}
[/code]

La configuración específica del proveedor (claves de API, URL base, modos) vive bajo `plugins.entries.<plugin>.config.webSearch.*`. Gemini también puede reutilizar `models.providers.google.apiKey` y `models.providers.google.baseUrl` como alternativas de menor prioridad después de su configuración dedicada de búsqueda web y `GEMINI_API_KEY`. Consulta las páginas de proveedores para ver ejemplos.

`tools.web.search.provider` se valida contra los identificadores de proveedores de búsqueda web declarados por los manifiestos de plugins incluidos e instalados. Un error tipográfico como `"brvae"` hace fallar la validación de la configuración en lugar de recurrir silenciosamente a la detección automática. Si un proveedor configurado solo tiene evidencia obsoleta del plugin, como un bloque `plugins.entries.<plugin>` sobrante después de desinstalar un plugin de terceros, OpenClaw mantiene un inicio resistente e informa una advertencia para que puedas reinstalar el plugin o ejecutar `openclaw doctor --fix` para limpiar la configuración obsoleta.

La selección del proveedor alternativo de `web_fetch` es independiente:

  * elígelo con `tools.web.fetch.provider`
  * o omite ese campo y deja que OpenClaw detecte automáticamente el primer proveedor de web-fetch listo a partir de las credenciales disponibles
  * `web_fetch` sin sandbox puede usar proveedores de plugins instalados que declaren `contracts.webFetchProviders`; las recuperaciones con sandbox siguen siendo solo las incluidas
  * hoy el proveedor web-fetch incluido es Firecrawl, configurado bajo `plugins.entries.firecrawl.config.webFetch.*`


Cuando eliges **Kimi** durante `openclaw onboard` o `openclaw configure --section web`, OpenClaw también puede pedir:

  * la región de la API de Moonshot (`https://api.moonshot.ai/v1` o `https://api.moonshot.cn/v1`)
  * el modelo predeterminado de búsqueda web de Kimi (predeterminado: `kimi-k2.6`)


Para `x_search`, configura `plugins.entries.xai.config.xSearch.*`. Usa el mismo perfil de autenticación de xAI que el chat, o la credencial `XAI_API_KEY` / de búsqueda web del plugin usada por la búsqueda web de Grok. La configuración heredada `tools.web.x_search.*` se migra automáticamente mediante `openclaw doctor --fix`. Cuando eliges Grok durante `openclaw onboard` o `openclaw configure --section web`, OpenClaw también puede ofrecer una configuración opcional de `x_search` con la misma clave. Este es un paso de seguimiento independiente dentro de la ruta de Grok, no una opción independiente de proveedor de búsqueda web de nivel superior. Si eliges otro proveedor, OpenClaw no muestra el aviso de `x_search`.

### Almacenamiento de claves de API

### Archivo de configuración

Ejecuta `openclaw configure --section web` o establece la clave directamente:

json5Copy code
[code]
    {  plugins: {    entries: {      brave: {        config: {          webSearch: {            apiKey: "YOUR_KEY", // pragma: allowlist secret          },        },      },    },  },}
[/code]

### Variable de entorno

Establece la variable de entorno del proveedor en el entorno del proceso del Gateway:

bashCopy code
[code]
    export BRAVE_API_KEY="YOUR_KEY"
[/code]

Para una instalación de gateway, ponla en `~/.openclaw/.env`. Consulta [Variables de entorno](</es/help/faq#env-vars-and-env-loading>).

## Parámetros de la herramienta

Parámetro | Descripción  
---|---  
`query` | Consulta de búsqueda (obligatorio)  
`count` | Resultados que se devolverán (1-10, predeterminado: 5)  
`country` | Código de país ISO de 2 letras (p. ej., "US", "DE")  
`language` | Código de idioma ISO 639-1 (p. ej., "en", "de")  
`search_lang` | Código de idioma de búsqueda (solo Brave)  
`freshness` | Filtro de tiempo: `day`, `week`, `month` o `year`  
`date_after` | Resultados posteriores a esta fecha (YYYY-MM-DD)  
`date_before` | Resultados anteriores a esta fecha (YYYY-MM-DD)  
`ui_lang` | Código de idioma de la interfaz (solo Brave)  
`domain_filter` | Matriz de lista permitida/denegada de dominios (solo Perplexity)  
`max_tokens` | Presupuesto total de contenido, predeterminado 25000 (solo Perplexity)  
`max_tokens_per_page` | Límite de tokens por página, predeterminado 2048 (solo Perplexity)  
  
## x_search

`x_search` consulta publicaciones de X (anteriormente Twitter) usando xAI y devuelve respuestas sintetizadas por IA con citas. Acepta consultas en lenguaje natural y filtros estructurados opcionales. OpenClaw solo habilita la herramienta integrada `x_search` de xAI en la solicitud que sirve esta llamada de herramienta.

### Configuración de x_search

json5Copy code
[code]
    {  plugins: {    entries: {      xai: {        config: {          xSearch: {            enabled: true,            model: "grok-4-1-fast-non-reasoning",            baseUrl: "https://api.x.ai/v1", // optional, overrides webSearch.baseUrl            inlineCitations: false,            maxTurns: 2,            timeoutSeconds: 30,            cacheTtlMinutes: 15,          },          webSearch: {            apiKey: "xai-...", // optional if an xAI auth profile or XAI_API_KEY is set            baseUrl: "https://api.x.ai/v1", // optional shared xAI Responses base URL          },        },      },    },  },}
[/code]

`x_search` publica en `<baseUrl>/responses` cuando `plugins.entries.xai.config.xSearch.baseUrl` está definido. Si se omite ese campo, recurre a `plugins.entries.xai.config.webSearch.baseUrl`, luego al `tools.web.search.grok.baseUrl` heredado y finalmente al endpoint público de xAI.

### Parámetros de x_search

Parámetro | Descripción  
---|---  
`query` | Consulta de búsqueda (obligatorio)  
`allowed_x_handles` | Restringir resultados a identificadores concretos de X  
`excluded_x_handles` | Excluir identificadores concretos de X  
`from_date` | Incluir solo publicaciones en esta fecha o después (YYYY-MM-DD)  
`to_date` | Incluir solo publicaciones en esta fecha o antes (YYYY-MM-DD)  
`enable_image_understanding` | Permitir que xAI inspeccione imágenes adjuntas a publicaciones coincidentes  
`enable_video_understanding` | Permitir que xAI inspeccione videos adjuntos a publicaciones coincidentes  
  
### Ejemplo de x_search

javascriptCopy code
[code]
    await x_search({  query: "dinner recipes",  allowed_x_handles: ["nytfood"],  from_date: "2026-03-01",});
[/code]

javascriptCopy code
[code]
    // Per-post stats: use the exact status URL or status ID when possibleawait x_search({  query: "https://x.com/huntharo/status/1905678901234567890",});
[/code]

## Ejemplos

javascriptCopy code
[code]
    // Basic searchawait web_search({ query: "OpenClaw plugin SDK" }); // German-specific searchawait web_search({ query: "TV online schauen", country: "DE", language: "de" }); // Recent results (past week)await web_search({ query: "AI developments", freshness: "week" }); // Date rangeawait web_search({  query: "climate research",  date_after: "2024-01-01",  date_before: "2024-06-30",}); // Domain filtering (Perplexity only)await web_search({  query: "product reviews",  domain_filter: ["-reddit.com", "-pinterest.com"],});
[/code]

## Perfiles de herramientas

Si usas perfiles de herramientas o listas de permitidos, agrega `web_search`, `x_search` o `group:web`:

json5Copy code
[code]
    {  tools: {    allow: ["web_search", "x_search"],    // or: allow: ["group:web"]  (includes web_search, x_search, and web_fetch)  },}
[/code]

## Relacionado

  * [Web Fetch](</es/tools/web-fetch>) \-- obtiene una URL y extrae contenido legible
  * [Web Browser](</es/tools/browser>) \-- automatización completa del navegador para sitios con mucho JS
  * [Grok Search](</es/tools/grok-search>) \-- Grok como proveedor de `web_search`
  * [Ollama Web Search](</es/tools/ollama-search>) \-- búsqueda web sin clave a través de tu host de Ollama


Was this useful?YesNo