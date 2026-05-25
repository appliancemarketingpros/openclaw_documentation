---
title: Estado
source_url: https://docs.openclaw.ai/es/cli/health
scraped_at: 2026-05-25
---

# `openclaw health`

Obtén el estado del Gateway en ejecución.

## Opciones

Opción | Predeterminado | Descripción  
---|---|---  
`--json` | `false` | Imprime JSON legible por máquina en lugar de texto.  
`--timeout <ms>` | `10000` | Tiempo de espera de conexión en milisegundos.  
`--verbose` | `false` | Registro detallado. Fuerza un sondeo en vivo y amplía la salida por agente.  
`--debug` | `false` | Alias de `--verbose`.  
  
Ejemplos:

bashCopy code
[code]
    openclaw healthopenclaw health --jsonopenclaw health --timeout 2500openclaw health --verboseopenclaw health --debug
[/code]

Notas:

  * De forma predeterminada, `openclaw health` solicita al Gateway en ejecución su instantánea de estado. Cuando el Gateway ya tiene una instantánea reciente en caché, puede devolver esa carga útil en caché y actualizarse en segundo plano.
  * `--verbose` fuerza un sondeo en vivo, imprime detalles de conexión del Gateway y amplía la salida legible por humanos para todas las cuentas y agentes configurados.
  * La salida incluye almacenes de sesión por agente cuando hay varios agentes configurados.


## Relacionado

  * [Referencia de CLI](</es/cli>)
  * [Estado del Gateway](</es/gateway/health>)


Was this useful?YesNo