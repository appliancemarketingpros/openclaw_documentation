---
title: Preguntar al usuario
source_url: https://docs.openclaw.ai/es/tools/ask-user
scraped_at: 2026-07-20
---

CapabilitiesTools

`ask_user` permite al agente formular al humano de una a tres preguntas estructuradas y esperar las respuestas. Está destinada a decisiones que realmente corresponden al usuario, no a confirmaciones rutinarias ni a información que el agente pueda deducir de la solicitud, el código o un valor predeterminado razonable.

La herramienta solo está disponible en la sesión principal. Los subagentes y otras ejecuciones no principales no la reciben.

## Responder una pregunta

Se puede responder desde cualquier superficie de conversación compatible:

  * La interfaz de control web acopla un panel de preguntas directamente encima del cuadro de redacción. En las solicitudes con varias preguntas, el panel muestra una pregunta a la vez y avanza mediante un breve indicador de pasos. Tras resolverse, el panel se cierra y el chat conserva únicamente un resumen compacto de las respuestas.
  * Telegram, Discord y Slack muestran botones nativos para una solicitud de una sola pregunta y una sola opción.
  * Una respuesta de texto sin formato funciona en cualquier canal. Se puede responder con un número, la etiqueta de una opción o una respuesta propia.


OpenClaw siempre habilita una respuesta de texto libre **Other**. El agente no debe añadir una opción `Other` a la lista de opciones creada.

## Comportamiento de la plataforma

Las respuestas funcionan en todas las superficies de conversación compatibles. La interfaz de control web utiliza un indicador de pasos acoplado que sustituye el cuadro de redacción mientras está expandido; al contraerlo, se restaura el cuadro de redacción completo debajo de una barra de preguntas estrecha. iOS, macOS y Android muestran tarjetas en línea; las preguntas múltiples permanecen apiladas como patrón intencional adaptado a interfaces táctiles. Todas las plataformas conservan el resumen de preguntas y respuestas en la cronología del chat activo sin eliminación programada, y **Skip** está disponible en todas ellas.

Las solicitudes que no pueden utilizar botones nativos, incluidas las de varias preguntas y selección múltiple, se convierten en texto legible en los canales. La interfaz de control conserva el indicador de pasos estructurado completo.

## Tiempo de espera y ausencia de respuesta

El tiempo de espera predeterminado es de 900 segundos. `timeoutSeconds` se limita al intervalo de 30 a 3600 segundos.

Si la pregunta caduca o se cancela antes de que llegue una respuesta, la herramienta devuelve `status: "no_answer"`. A continuación, el agente continúa según su mejor criterio. Una ejecución del agente interrumpida cancela su pregunta pendiente del Gateway.

## Esquema de la herramienta

tsCopy code
[code]
    {  questions: Array<{    id: string; // clave de respuesta única en snake_case    header: string; // etiqueta breve; se trunca a 12 caracteres    question: string; // una frase    options: Array<{      label: string;      description?: string;    }>; // 2-4 opciones    multiSelect?: boolean;  }>; // 1-3 preguntas  timeoutSeconds?: number; // entero; valor predeterminado 900, limitado a 30-3600}
[/code]

Con `multiSelect: true`, el usuario puede elegir más de una opción. Los valores de las respuestas se devuelven como un arreglo para cada pregunta.

Ejemplo de resultado respondido:

jsonCopy code
[code]
    {  "status": "answered",  "answers": {    "answers": {      "deploy_target": {        "answers": ["Staging (Recommended)"]      }    }  }}
[/code]

## Orientación para el modelo

El contrato dirigido al modelo indica al agente que debe:

  * preguntar solo cuando esté bloqueado por una decisión que realmente corresponda al usuario;
  * preferir una sola pregunta y no formular más de tres;
  * colocar primero la opción recomendada y añadir `(Recommended)` al final de su etiqueta;
  * omitir una opción `Other` creada porque el texto libre se añade automáticamente;
  * continuar según su mejor criterio después de `no_answer`.


El agente no debe utilizar `ask_user` para preguntar si puede continuar ni para confirmar su propio plan.

Was this useful?YesNo

Open issue