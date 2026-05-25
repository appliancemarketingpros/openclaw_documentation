---
title: Dirigir
source_url: https://docs.openclaw.ai/es/tools/steer
scraped_at: 2026-05-25
---

`/steer` envía indicaciones a una ejecución ya activa. Es para momentos de "ajustar esta ejecución mientras todavía está trabajando", no para iniciar un turno nuevo.

## Sesión actual

Usa `/steer` de nivel superior para apuntar a la ejecución activa de la sesión actual:

textCopy code
[code]
    /steer prefer the smaller patch and keep the tests focused/tell summarize before making the next tool call
[/code]

Comportamiento:

  * Apunta solo a la ejecución activa de la sesión actual.
  * Funciona independientemente del modo `/queue` de la sesión.
  * No inicia una nueva ejecución cuando la sesión está inactiva.
  * Responde con una advertencia cuando no hay ninguna ejecución activa que orientar.
  * Usa la ruta de orientación del entorno de ejecución activo, por lo que el modelo ve las indicaciones en el siguiente límite compatible del entorno de ejecución.


## Orientación frente a cola

`/queue steer` cambia cómo se comportan los mensajes entrantes normales cuando llegan mientras una ejecución está activa. `/steer <message>` es un comando explícito que intenta inyectar el mensaje de ese comando en la ejecución activa en el siguiente límite compatible del entorno de ejecución, independientemente de la configuración `/queue` almacenada.

Uso:

  * `/steer <message>` cuando quieres guiar la ejecución activa ahora mismo.
  * `/queue steer` cuando quieres que los mensajes normales futuros orienten las ejecuciones activas de forma predeterminada.
  * `/queue collect` o `/queue followup` cuando los mensajes nuevos deben esperar a un turno posterior en lugar de orientar la ejecución activa.


Para los modos de cola y el comportamiento de reserva, consulta [Cola de comandos](</es/concepts/queue>) y [Cola de orientación](</es/concepts/queue-steering>).

## Subagentes

Usa `/subagents steer` cuando el destino sea una ejecución secundaria:

textCopy code
[code]
    /subagents steer 2 focus only on the API surface
[/code]

`/steer` de nivel superior no selecciona un subagente por id ni por índice de lista. Siempre apunta a la ejecución activa de la sesión actual. Consulta [Subagentes](</es/tools/subagents>) para los ids, las etiquetas y los comandos de control de subagentes.

## Sesiones ACP

Usa `/acp steer` cuando el destino sea una sesión de arnés ACP:

textCopy code
[code]
    /acp steer --session agent:main:acp:codex tighten the repro
[/code]

Consulta [Agentes ACP](</es/tools/acp-agents>) para la selección de sesiones ACP y el comportamiento del entorno de ejecución.

## Relacionado

  * [Comandos slash](</es/tools/slash-commands>)
  * [Cola de comandos](</es/concepts/queue>)
  * [Cola de orientación](</es/concepts/queue-steering>)
  * [Subagentes](</es/tools/subagents>)


Was this useful?YesNo