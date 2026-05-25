---
title: Tavily
source_url: https://docs.openclaw.ai/es/tools/tavily
scraped_at: 2026-05-25
---

[Tavily](<https://tavily.com>) es una API de búsqueda diseñada para aplicaciones de IA. OpenClaw la expone de dos formas:

  * como proveedor `web_search` para la herramienta de búsqueda genérica
  * como herramientas explícitas del Plugin: `tavily_search` y `tavily_extract`


Tavily devuelve resultados estructurados optimizados para el consumo por LLM, con profundidad de búsqueda configurable, filtrado por tema, filtros de dominio, resúmenes de respuestas generados por IA y extracción de contenido desde URL (incluidas páginas renderizadas con JavaScript).

Propiedad | Valor  
---|---  
ID del Plugin | `tavily`  
Autenticación | `TAVILY_API_KEY` o config `apiKey`  
URL base | `https://api.tavily.com` (predeterminada)  
Herramientas incluidas | `tavily_search`, `tavily_extract`  
  
## Primeros pasos

* ### Obtén una clave de API

Crea una cuenta de Tavily en [tavily.com](<https://tavily.com>) y luego genera una clave de API en el panel.

* ### Configura el Plugin y el proveedor

json5Copy code
[code]
    {  plugins: {    entries: {      tavily: {        enabled: true,        config: {          webSearch: {            apiKey: "tvly-...", // optional if TAVILY_API_KEY is set            baseUrl: "https://api.tavily.com",          },        },      },    },  },  tools: {    web: {      search: {        provider: "tavily",      },    },  },}
[/code]

* ### Verifica que la búsqueda se ejecute

Activa una `web_search` desde cualquier agente, o llama directamente a `tavily_search`.

## Referencia de herramientas

### `tavily_search`

Usa esto cuando quieras controles de búsqueda específicos de Tavily en lugar de `web_search` genérico.

Parámetro | Tipo | Restricciones / predeterminado | Descripción  
---|---|---|---  
`query` | cadena | obligatorio | Cadena de consulta de búsqueda. Mantenla por debajo de 400 caracteres.  
`search_depth` | enum | `basic` (predeterminado), `advanced` | `advanced` es más lento, pero tiene mayor relevancia.  
`topic` | enum | `general` (predeterminado), `news`, `finance` | Filtra por familia temática.  
`max_results` | entero | 1-20 | Número de resultados.  
`include_answer` | booleano | predeterminado `false` | Incluye un resumen de respuesta generado por IA de Tavily.  
`time_range` | enum | `day`, `week`, `month`, `year` | Filtra resultados por actualidad.  
`include_domains` | array de cadenas | (ninguno) | Incluye solo resultados de estos dominios.  
`exclude_domains` | array de cadenas | (ninguno) | Excluye resultados de estos dominios.  
  
Compensación de profundidad de búsqueda:

Profundidad | Velocidad | Relevancia | Ideal para  
---|---|---|---  
`basic` | Más rápida | Alta | Consultas de propósito general (predeterminado).  
`advanced` | Más lenta | Máxima | Investigación precisa y verificación de hechos.  
  
### `tavily_extract`

Usa esto para extraer contenido limpio de una o más URL. Maneja páginas renderizadas con JavaScript y admite fragmentación enfocada en consultas para extracción dirigida.

Parámetro | Tipo | Restricciones / predeterminado | Descripción  
---|---|---|---  
`urls` | array de cadenas | obligatorio, 1-20 | URL de las que extraer contenido.  
`query` | cadena | (opcional) | Reordena los fragmentos extraídos por relevancia para esta consulta.  
`extract_depth` | enum | `basic` (predeterminado), `advanced` | Usa `advanced` para páginas con mucho JS, SPA o tablas dinámicas.  
`chunks_per_source` | entero | 1-5; **requiere`query`** | Fragmentos devueltos por URL. Da error si se establece sin `query`.  
`include_images` | booleano | predeterminado `false` | Incluye URL de imágenes en los resultados.  
  
Compensación de profundidad de extracción:

Profundidad | Cuándo usarla  
---|---  
`basic` | Páginas simples. Prueba esto primero.  
`advanced` | SPA renderizadas con JS, contenido dinámico, tablas.  
  
## Elegir la herramienta adecuada

Necesidad | Herramienta  
---|---  
Búsqueda web rápida, sin opciones especiales | `web_search`  
Búsqueda con profundidad, tema y respuestas de IA | `tavily_search`  
Extraer contenido de URL específicas | `tavily_extract`  
  
## Configuración avanzada

Orden de resolución de la clave de API

El cliente de Tavily busca su clave de API en este orden:

  1. `plugins.entries.tavily.config.webSearch.apiKey` (resuelta mediante SecretRefs).
  2. `TAVILY_API_KEY` desde el entorno del Gateway.


`tavily_extract` genera un error de configuración si no está presente ninguna de las dos.

URL base personalizada

Sobrescribe `plugins.entries.tavily.config.webSearch.baseUrl` si expones Tavily mediante un proxy. El valor predeterminado es `https://api.tavily.com`.

`chunks_per_source` requiere `query`

`tavily_extract` rechaza llamadas que pasen `chunks_per_source` sin una `query`. Tavily clasifica los fragmentos por relevancia respecto de la consulta, por lo que el parámetro no tiene sentido sin una.

## Relacionado

[**Descripción general de Web Search** Todos los proveedores y reglas de detección automática. ](</es/tools/web>) [**Firecrawl** Búsqueda más scraping con extracción de contenido. ](</es/tools/firecrawl>) [**Exa Search** Búsqueda neuronal con extracción de contenido. ](</es/tools/exa-search>) [**Configuración** Esquema de configuración completo para entradas de Plugin y enrutamiento de herramientas. ](</es/gateway/configuration>)

Was this useful?YesNo