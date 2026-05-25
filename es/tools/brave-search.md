---
title: Búsqueda de Brave
source_url: https://docs.openclaw.ai/es/tools/brave-search
scraped_at: 2026-05-25
---

OpenClaw admite Brave Search API como proveedor `web_search`.

## Obtener una clave de API

  1. Crea una cuenta de Brave Search API en <https://brave.com/search/api/>
  2. En el panel, elige el plan **Search** y genera una clave de API.
  3. Guarda la clave en la configuración o define `BRAVE_API_KEY` en el entorno del Gateway.


## Ejemplo de configuración

json5Copy code
[code]
    {  plugins: {    entries: {      brave: {        config: {          webSearch: {            apiKey: "BRAVE_API_KEY_HERE",            mode: "web", // or "llm-context"            baseUrl: "https://api.search.brave.com", // optional proxy/base URL override          },        },      },    },  },  tools: {    web: {      search: {        provider: "brave",        maxResults: 5,        timeoutSeconds: 30,      },    },  },}
[/code]

La configuración de búsqueda de Brave específica del proveedor ahora se encuentra en `plugins.entries.brave.config.webSearch.*`. El `tools.web.search.apiKey` heredado todavía se carga mediante la capa de compatibilidad, pero ya no es la ruta de configuración canónica.

`webSearch.mode` controla el transporte de Brave:

  * `web` (predeterminado): búsqueda web normal de Brave con títulos, URL y fragmentos
  * `llm-context`: API Brave LLM Context con fragmentos de texto preextraídos y fuentes para fundamentación


`webSearch.baseUrl` puede dirigir las solicitudes de Brave a un proxy o gateway confiable compatible con Brave. OpenClaw agrega `/res/v1/web/search` o `/res/v1/llm/context` a la URL base configurada y mantiene la URL base en la clave de caché. Los endpoints públicos deben usar `https://`; `http://` solo se acepta para hosts proxy de loopback confiables o de red privada.

## Parámetros de la herramienta

Consulta de búsqueda.

Número de resultados que se devolverán (1–10).

Código de país ISO de 2 letras (por ejemplo, `US`, `DE`).

Código de idioma ISO 639-1 para los resultados de búsqueda (por ejemplo, `en`, `de`, `fr`).

Código de idioma de búsqueda de Brave (por ejemplo, `en`, `en-gb`, `zh-hans`).

Código de idioma ISO para elementos de la interfaz de usuario.

Filtro de tiempo: `day` son 24 horas.

Solo resultados publicados después de esta fecha (`YYYY-MM-DD`).

Solo resultados publicados antes de esta fecha (`YYYY-MM-DD`).

**Ejemplos:**

javascriptCopy code
[code]
    // Country and language-specific searchawait web_search({  query: "renewable energy",  country: "DE",  language: "de",}); // Recent results (past week)await web_search({  query: "AI news",  freshness: "week",}); // Date range searchawait web_search({  query: "AI developments",  date_after: "2024-01-01",  date_before: "2024-06-30",});
[/code]

## Notas

  * OpenClaw usa el plan **Search** de Brave. Si tienes una suscripción heredada (por ejemplo, el plan Free original con 2000 consultas/mes), sigue siendo válida, pero no incluye funciones más recientes como LLM Context ni límites de frecuencia más altos.
  * Cada plan de Brave incluye **$5/mes en crédito gratuito** (renovable). El plan Search cuesta $5 por cada 1000 solicitudes, por lo que el crédito cubre 1000 consultas/mes. Define tu límite de uso en el panel de Brave para evitar cargos inesperados. Consulta el [portal de API de Brave](<https://brave.com/search/api/>) para ver los planes actuales.
  * El plan Search incluye el endpoint LLM Context y derechos de inferencia de IA. Almacenar resultados para entrenar o ajustar modelos requiere un plan con derechos explícitos de almacenamiento. Consulta los [Términos de servicio](<https://api-dashboard.search.brave.com/terms-of-service>) de Brave.
  * El modo `llm-context` devuelve entradas de fuentes fundamentadas en lugar de la forma normal de fragmento de búsqueda web.
  * El modo `llm-context` admite `freshness` y rangos acotados de `date_after` \+ `date_before`. No admite `ui_lang`; `date_before` sin `date_after` se rechaza porque Brave exige que los rangos personalizados de freshness incluyan tanto fecha de inicio como de finalización.
  * `ui_lang` debe incluir una subetiqueta de región como `en-US`.
  * Los resultados se almacenan en caché durante 15 minutos de forma predeterminada (configurable mediante `cacheTtlMinutes`).
  * Los valores personalizados de `webSearch.baseUrl` se incluyen en la identidad de caché de Brave, por lo que las respuestas específicas del proxy no colisionan.
  * Activa la marca de diagnóstico `brave.http` para registrar URL/parámetros de consulta de solicitudes de Brave, estado/tiempos de respuesta y eventos de acierto/fallo/escritura de caché de búsqueda durante la resolución de problemas. La marca nunca registra la clave de API ni los cuerpos de respuesta, pero las consultas de búsqueda pueden ser confidenciales.


## Relacionado

  * [Descripción general de Web Search](</es/tools/web>) \-- todos los proveedores y detección automática
  * [Perplexity Search](</es/tools/perplexity-search>) \-- resultados estructurados con filtrado de dominios
  * [Exa Search](</es/tools/exa-search>) \-- búsqueda neuronal con extracción de contenido


Was this useful?YesNo