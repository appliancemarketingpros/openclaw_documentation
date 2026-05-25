---
title: Política de reintentos
source_url: https://docs.openclaw.ai/es/concepts/retry
scraped_at: 2026-05-25
---

## Objetivos

  * Reintentar por solicitud HTTP, no por flujo de varios pasos.
  * Conservar el orden reintentando solo el paso actual.
  * Evitar duplicar operaciones no idempotentes.


## Valores predeterminados

  * Intentos: 3
  * Límite máximo de demora: 30000 ms
  * Jitter: 0.1 (10 por ciento)
  * Valores predeterminados del proveedor: 
    * Demora mínima de Telegram: 400 ms
    * Demora mínima de Discord: 500 ms


## Comportamiento

### Proveedores de modelos

  * OpenClaw permite que los SDK de proveedores gestionen los reintentos cortos normales.
  * Para SDK basados en Stainless, como Anthropic y OpenAI, las respuestas reintentables (`408`, `409`, `429` y `5xx`) pueden incluir `retry-after-ms` o `retry-after`. Cuando esa espera supera los 60 segundos, OpenClaw inyecta `x-should-retry: false` para que el SDK exponga el error inmediatamente y la conmutación por error de modelos pueda rotar a otro perfil de autenticación o modelo alternativo.
  * Sobrescribe el límite con `OPENCLAW_SDK_RETRY_MAX_WAIT_SECONDS=<seconds>`. Establécelo en `0`, `false`, `off`, `none` o `disabled` para permitir que los SDK respeten internamente las esperas largas de `Retry-After`.


### Discord

  * Reintenta ante errores de límite de frecuencia (HTTP 429), tiempos de espera de solicitud, respuestas HTTP 5xx y fallos transitorios de transporte, como fallos de búsqueda DNS, reinicios de conexión, cierres de socket y fallos de fetch.
  * Usa `retry_after` de Discord cuando está disponible; de lo contrario, usa retroceso exponencial.


### Telegram

  * Reintenta ante errores transitorios (429, tiempo de espera, conexión/reinicio/cierre, temporalmente no disponible).
  * Usa `retry_after` cuando está disponible; de lo contrario, usa retroceso exponencial.
  * Los errores de análisis de Markdown no se reintentan; recurren a texto sin formato.


## Configuración

Establece la política de reintentos por proveedor en `~/.openclaw/openclaw.json`:

json5Copy code
[code]
    {  channels: {    telegram: {      retry: {        attempts: 3,        minDelayMs: 400,        maxDelayMs: 30000,        jitter: 0.1,      },    },    discord: {      retry: {        attempts: 3,        minDelayMs: 500,        maxDelayMs: 30000,        jitter: 0.1,      },    },  },}
[/code]

## Notas

  * Los reintentos se aplican por solicitud (envío de mensaje, carga de medios, reacción, encuesta, sticker).
  * Los flujos compuestos no reintentan los pasos completados.


## Relacionado

  * [Conmutación por error de modelos](</es/concepts/model-failover>)
  * [Cola de comandos](</es/concepts/queue>)


Was this useful?YesNo