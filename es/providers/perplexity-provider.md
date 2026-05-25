---
title: Perplexity
source_url: https://docs.openclaw.ai/es/providers/perplexity-provider
scraped_at: 2026-05-25
---

El Plugin Perplexity proporciona capacidades de búsqueda web mediante la API de búsqueda de Perplexity o Perplexity Sonar a través de OpenRouter.

Propiedad | Valor  
---|---  
Tipo | Proveedor de búsqueda web (no un proveedor de modelos)  
Autenticación | `PERPLEXITY_API_KEY` (directa) o `OPENROUTER_API_KEY` (vía OpenRouter)  
Ruta de configuración | `plugins.entries.perplexity.config.webSearch.apiKey`  
  
## Primeros pasos

* ### Configurar la clave de API

Ejecuta el flujo interactivo de configuración de búsqueda web:

bashCopy code
[code]
    openclaw configure --section web
[/code]

O configura la clave directamente:

bashCopy code
[code]
    openclaw config set plugins.entries.perplexity.config.webSearch.apiKey "pplx-xxxxxxxxxxxx"
[/code]

* ### Empezar a buscar

El agente usará automáticamente Perplexity para las búsquedas web una vez que la clave esté configurada. No se requieren pasos adicionales.

## Modos de búsqueda

El Plugin selecciona automáticamente el transporte según el prefijo de la clave de API:

### API nativa de Perplexity (pplx-)

Cuando tu clave empieza por `pplx-`, OpenClaw usa la API nativa de búsqueda de Perplexity. Este transporte devuelve resultados estructurados y admite filtros de dominio, idioma y fecha (consulta las opciones de filtrado más abajo).

### OpenRouter / Sonar (sk-or-)

Cuando tu clave empieza por `sk-or-`, OpenClaw enruta a través de OpenRouter usando el modelo Perplexity Sonar. Este transporte devuelve respuestas sintetizadas por IA con citas.

Prefijo de clave | Transporte | Funciones  
---|---|---  
`pplx-` | API nativa de Perplexity Search | Resultados estructurados, filtros de dominio/idioma/fecha  
`sk-or-` | OpenRouter (Sonar) | Respuestas sintetizadas por IA con citas  
  
## Filtrado de la API nativa

Al usar la API nativa de Perplexity, las búsquedas admiten los siguientes filtros:

Filtro | Descripción | Ejemplo  
---|---|---  
País | Código de país de 2 letras | `us`, `de`, `jp`  
Idioma | Código de idioma ISO 639-1 | `en`, `fr`, `zh`  
Intervalo de fechas | Ventana de actualidad | `day`, `week`, `month`, `year`  
Filtros de dominio | Lista de permitidos o bloqueados (máx. 20 dominios) | `example.com`  
Presupuesto de contenido | Límites de tokens por respuesta / por página | `max_tokens`, `max_tokens_per_page`  
  
## Configuración avanzada

Variable de entorno para procesos daemon

Si el Gateway de OpenClaw se ejecuta como daemon (launchd/systemd), asegúrate de que `PERPLEXITY_API_KEY` esté disponible para ese proceso.

Configuración de proxy de OpenRouter

Si prefieres enrutar las búsquedas de Perplexity a través de OpenRouter, configura una `OPENROUTER_API_KEY` (prefijo `sk-or-`) en lugar de una clave nativa de Perplexity. OpenClaw detectará el prefijo y cambiará al transporte Sonar automáticamente.

## Relacionado

[**Herramienta de búsqueda de Perplexity** Cómo el agente invoca búsquedas de Perplexity e interpreta los resultados. ](</es/tools/perplexity-search>) [**Referencia de configuración** Referencia de configuración completa, incluidas las entradas de Plugin. ](</es/gateway/configuration-reference>)

Was this useful?YesNo