---
title: Modo elevado
source_url: https://docs.openclaw.ai/es/tools/elevated
scraped_at: 2026-05-25
---

Cuando un agente se ejecuta dentro de un sandbox, sus comandos `exec` quedan confinados al entorno del sandbox. El **modo elevado** permite que el agente salga y ejecute comandos fuera del sandbox en su lugar, con puertas de aprobación configurables.

## Directivas

Controla el modo elevado por sesión con comandos de barra:

Directiva | Qué hace  
---|---  
`/elevated on` | Ejecuta fuera del sandbox en la ruta del host configurada, mantiene las aprobaciones  
`/elevated ask` | Igual que `on` (alias)  
`/elevated full` | Ejecuta fuera del sandbox en la ruta del host configurada y omite las aprobaciones  
`/elevated off` | Vuelve a la ejecución confinada al sandbox  
  
También disponible como `/elev on|off|ask|full`.

Envía `/elevated` sin argumento para ver el nivel actual.

## Cómo funciona

* ### Check availability

Elevated debe estar habilitado en la configuración y el remitente debe estar en la lista de permitidos:

json5Copy code
[code]
    {  tools: {    elevated: {      enabled: true,      allowFrom: {        discord: ["user-id-123"],        whatsapp: ["+15555550123"],      },    },  },}
[/code]

* ### Set the level

Envía un mensaje que contenga solo la directiva para establecer el valor predeterminado de la sesión:

CodeCopy code
[code]
    /elevated full
[/code]

O úsala en línea (se aplica solo a ese mensaje):

CodeCopy code
[code]
    /elevated on run the deployment script
[/code]

* ### Commands run outside the sandbox

Con elevated activo, las llamadas `exec` salen del sandbox. El host efectivo es `gateway` de forma predeterminada, o `node` cuando el destino exec configurado/de sesión es `node`. En modo `full`, se omiten las aprobaciones de exec. En modo `on`/`ask`, las reglas de aprobación configuradas siguen aplicándose.

## Orden de resolución

  1. **Directiva en línea** en el mensaje (se aplica solo a ese mensaje)
  2. **Anulación de sesión** (establecida al enviar un mensaje que contiene solo la directiva)
  3. **Valor predeterminado global** (`agents.defaults.elevatedDefault` en la configuración)


## Disponibilidad y listas de permitidos

  * **Puerta global** : `tools.elevated.enabled` (debe ser `true`)
  * **Lista de permitidos de remitentes** : `tools.elevated.allowFrom` con listas por canal
  * **Puerta por agente** : `agents.list[].tools.elevated.enabled` (solo puede restringir más)
  * **Lista de permitidos por agente** : `agents.list[].tools.elevated.allowFrom` (el remitente debe coincidir tanto con la global como con la del agente)
  * **Reserva de Discord** : si se omite `tools.elevated.allowFrom.discord`, se usa `channels.discord.allowFrom` como reserva
  * **Todas las puertas deben pasar** ; de lo contrario, elevated se trata como no disponible


Formatos de entradas de la lista de permitidos:

Prefijo | Coincide con  
---|---  
(ninguno) | ID del remitente, E.164 o campo From  
`name:` | Nombre visible del remitente  
`username:` | Nombre de usuario del remitente  
`tag:` | Etiqueta del remitente  
`id:`, `from:`, `e164:` | Selección explícita de identidad  
  
## Lo que elevated no controla

  * **Política de herramientas** : si `exec` es denegado por la política de herramientas, elevated no puede anularlo.
  * **Política de selección de host** : elevated no convierte `auto` en una anulación libre entre hosts. Usa las reglas del destino exec configurado/de sesión, eligiendo `node` solo cuando el destino ya es `node`.
  * **Separado de`/exec`**: la directiva `/exec` ajusta los valores predeterminados de exec por sesión para remitentes autorizados y no requiere modo elevado.


## Relacionado

[**Exec tool** Ejecución de comandos de shell desde el agente. ](</es/tools/exec>) [**Exec approvals** Sistema de aprobación y lista de permitidos para `exec`. ](</es/tools/exec-approvals>) [**Sandboxing** Configuración de sandbox a nivel de Gateway. ](</es/gateway/sandboxing>) [**Sandbox vs Tool Policy vs Elevated** Cómo se componen las tres puertas durante una llamada de herramienta. ](</es/gateway/sandbox-vs-tool-policy-vs-elevated>)

Was this useful?YesNo