---
title: Detección de bucles de herramientas
source_url: https://docs.openclaw.ai/es/tools/loop-detection
scraped_at: 2026-05-25
---

OpenClaw tiene dos mecanismos de protección cooperativos para patrones repetitivos de llamadas a herramientas:

  1. **Detección de bucles** (`tools.loopDetection.enabled`) — deshabilitada de forma predeterminada. Observa el historial móvil de llamadas a herramientas en busca de patrones repetidos y reintentos de herramientas desconocidas.
  2. **Protección posterior a la Compaction** (`tools.loopDetection.postCompactionGuard`) — habilitada de forma predeterminada salvo que `tools.loopDetection.enabled` sea explícitamente `false`. Se activa después de cada reintento de Compaction y aborta la ejecución cuando el agente emite la misma terna `(tool, args, result)` dentro de la ventana.


Ambos se configuran bajo el mismo bloque `tools.loopDetection`, pero la protección posterior a la Compaction se ejecuta siempre que el interruptor principal no esté explícitamente desactivado. Define `tools.loopDetection.enabled: false` para silenciar ambas superficies.

## Por qué existe esto

  * Detectar secuencias repetitivas que no avanzan.
  * Detectar bucles de alta frecuencia sin resultados (misma herramienta, mismas entradas, errores repetidos).
  * Detectar patrones específicos de llamadas repetidas para herramientas de sondeo conocidas.
  * Evitar que ciclos de desbordamiento de contexto, luego Compaction y luego el mismo bucle se ejecuten indefinidamente.


## Bloque de configuración

Valores predeterminados globales, con todos los campos documentados mostrados:

json5Copy code
[code]
    {  tools: {    loopDetection: {      enabled: false, // master switch for the rolling-history detectors      historySize: 30,      warningThreshold: 10,      criticalThreshold: 20,      unknownToolThreshold: 10,      globalCircuitBreakerThreshold: 30,      detectors: {        genericRepeat: true,        knownPollNoProgress: true,        pingPong: true,      },      postCompactionGuard: {        windowSize: 3, // armed after compaction-retry; runs unless enabled is explicitly false      },    },  },}
[/code]

Anulación por agente (opcional):

json5Copy code
[code]
    {  agents: {    list: [      {        id: "safe-runner",        tools: {          loopDetection: {            enabled: true,            warningThreshold: 8,            criticalThreshold: 16,          },        },      },    ],  },}
[/code]

### Comportamiento de los campos

Campo | Predeterminado | Efecto  
---|---|---  
`enabled` | `false` | Interruptor principal para los detectores de historial móvil. Definirlo como `false` también deshabilita la protección posterior a la Compaction.  
`historySize` | `30` | Número de llamadas a herramientas recientes conservadas para análisis.  
`warningThreshold` | `10` | Umbral antes de que un patrón se clasifique solo como advertencia.  
`criticalThreshold` | `20` | Umbral para bloquear patrones repetitivos de bucle sin progreso.  
`unknownToolThreshold` | `10` | Bloquea llamadas repetidas a la misma herramienta no disponible después de esta cantidad de fallos.  
`globalCircuitBreakerThreshold` | `30` | Umbral global de interruptor por falta de progreso en todos los detectores.  
`detectors.genericRepeat` | `true` | Advierte sobre patrones repetidos de misma herramienta + mismos parámetros y bloquea cuando las mismas llamadas también devuelven resultados idénticos.  
`detectors.knownPollNoProgress` | `true` | Detecta patrones conocidos similares a sondeo sin cambio de estado.  
`detectors.pingPong` | `true` | Detecta patrones alternos de ida y vuelta.  
`postCompactionGuard.windowSize` | `3` | Número de llamadas a herramientas posteriores a la Compaction durante las cuales la protección permanece activada y conteo de ternas idénticas que aborta la ejecución.  
  
Para `exec`, las comprobaciones de falta de progreso comparan resultados estables de comandos e ignoran metadatos volátiles de ejecución como duración, PID, ID de sesión y directorio de trabajo. Cuando hay un ID de ejecución disponible, el historial reciente de llamadas a herramientas se evalúa solo dentro de esa ejecución para que los ciclos programados de Heartbeat y las ejecuciones nuevas no hereden conteos de bucles obsoletos de ejecuciones anteriores.

## Configuración recomendada

  * Para modelos más pequeños, define `enabled: true` y deja los umbrales en sus valores predeterminados. Los modelos insignia rara vez necesitan detección de historial móvil y pueden dejar el interruptor principal en `false` mientras siguen beneficiándose de la protección posterior a la Compaction.
  * Mantén los umbrales ordenados como `warningThreshold < criticalThreshold < globalCircuitBreakerThreshold`.
  * Si ocurren falsos positivos: 
    * Aumenta `warningThreshold` y/o `criticalThreshold`.
    * Opcionalmente aumenta `globalCircuitBreakerThreshold`.
    * Deshabilita solo el detector específico que cause problemas (`detectors.<name>: false`).
    * Reduce `historySize` para un contexto histórico menos estricto.
  * Para deshabilitar todo (incluida la protección posterior a la Compaction), define explícitamente `tools.loopDetection.enabled: false`.


## Protección posterior a la Compaction

Cuando el ejecutor completa un reintento de Compaction después de un desbordamiento de contexto, activa una protección de ventana corta que observa las siguientes llamadas a herramientas. Si el agente emite la misma terna `(toolName, argsHash, resultHash)` varias veces dentro de la ventana, la protección concluye que la Compaction no rompió el bucle y aborta la ejecución con un error `compaction_loop_persisted`.

La protección está controlada por la bandera principal `tools.loopDetection.enabled` con un matiz: permanece **habilitada cuando la bandera no está definida o es`true`** y solo se desactiva cuando la bandera es explícitamente `false`. Esto es intencional. La protección existe para escapar de bucles de Compaction que de otro modo consumirían tokens sin límite, así que un usuario sin configuración sigue recibiendo la protección.

json5Copy code
[code]
    {  tools: {    loopDetection: {      // master switch; set false to disable the guard along with the rolling detectors      enabled: true,      postCompactionGuard: {        windowSize: 3, // default      },    },  },}
[/code]

  * Un `windowSize` menor es más estricto (menos intentos antes de abortar).
  * Un `windowSize` mayor le da al agente más intentos de recuperación.
  * La protección nunca aborta cuando los resultados cambian, solo cuando los resultados son idénticos byte por byte en toda la ventana.
  * Es intencionalmente estrecha: se activa solo inmediatamente después de un reintento de Compaction.


## Registros y comportamiento esperado

Cuando se detecta un bucle, OpenClaw informa un evento de bucle y atenúa o bloquea el siguiente ciclo de herramientas según la gravedad. Esto protege a los usuarios del gasto descontrolado de tokens y de bloqueos, al tiempo que preserva el acceso normal a las herramientas.

  * Las advertencias aparecen primero.
  * La supresión sigue cuando los patrones persisten más allá del umbral de advertencia.
  * Los umbrales críticos bloquean el siguiente ciclo de herramientas y muestran un motivo claro de detección de bucle en el registro de ejecución.
  * La protección posterior a la Compaction emite errores `compaction_loop_persisted` con el nombre de la herramienta infractora y el conteo de llamadas idénticas.


## Relacionado

[**Aprobaciones de exec** Política de permitir/denegar para ejecución de shell. ](</es/tools/exec-approvals>) [**Niveles de pensamiento** Niveles de esfuerzo de razonamiento e interacción con la política del proveedor. ](</es/tools/thinking>) [**Subagentes** Generación de agentes aislados para limitar comportamientos descontrolados. ](</es/tools/subagents>) [**Referencia de configuración** Esquema completo de `tools.loopDetection` y semántica de combinación. ](</es/gateway/configuration-reference>)

Was this useful?YesNo