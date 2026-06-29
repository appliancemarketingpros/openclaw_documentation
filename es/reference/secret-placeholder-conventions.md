---
title: Convenciones de marcadores de posición de secretos
source_url: https://docs.openclaw.ai/es/reference/secret-placeholder-conventions
scraped_at: 2026-06-29
---

Get started

# Convenciones para marcadores de posición de secretos

Usa marcadores de posición que sean legibles para humanos, pero que no se parezcan a secretos reales.

## Estilo recomendado

  * Prefiere valores descriptivos como `example-openai-key-not-real` o `example-discord-bot-token`.
  * Para fragmentos de shell, prefiere `${OPENAI_API_KEY}` en lugar de cadenas en línea que parezcan tokens.
  * Mantén los ejemplos claramente falsos y acotados a su propósito (proveedor, canal, tipo de autenticación).


## Evita estos patrones en la documentación

  * Texto literal de encabezado o pie de clave privada PEM.
  * Prefijos que se parezcan a credenciales activas, por ejemplo `sk-...`, `xoxb-...`, `AKIA...`.
  * Tokens bearer de aspecto realista copiados de registros de runtime.


## Ejemplo

bashCopy code
[code]
    # Goodexport OPENAI_API_KEY="example-openai-key-not-real" # Better (when the doc is about env wiring)export OPENAI_API_KEY="${OPENAI_API_KEY}"
[/code]

Was this useful?YesNo

Open issue