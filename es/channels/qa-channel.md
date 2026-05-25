---
title: Canal de QA
source_url: https://docs.openclaw.ai/es/channels/qa-channel
scraped_at: 2026-05-25
---

`qa-channel` es un transporte de mensajes sintético incluido para QA automatizada de OpenClaw. No es un canal de producción: existe para ejercitar el mismo límite de Plugin de canal que usan los transportes reales, manteniendo el estado determinista y totalmente inspeccionable.

## Qué hace

  * Gramática de destino de clase Slack: 
    * `dm:<user>`
    * `channel:<room>`
    * `group:<room>`
    * `thread:<room>/<thread>`
  * Las conversaciones compartidas `channel:` y `group:` se exponen a los agentes como turnos de sala de grupo/canal, por lo que ejercitan la misma política de respuesta visible y enrutamiento de herramientas de mensajes que usan Discord, Slack, Telegram y transportes similares.
  * Bus sintético respaldado por HTTP para inyectar mensajes entrantes, capturar transcripciones salientes, crear hilos, reacciones, ediciones, eliminaciones y acciones de búsqueda/lectura.
  * Ejecutor de autocomprobación del lado del host que escribe un informe Markdown en `.artifacts/qa-e2e/`.


## Configuración

jsonCopy code
[code]
    {  "channels": {    "qa-channel": {      "baseUrl": "http://127.0.0.1:43123",      "botUserId": "openclaw",      "botDisplayName": "OpenClaw QA",      "allowFrom": ["*"],      "pollTimeoutMs": 1000    }  }}
[/code]

Claves de cuenta:

  * `enabled`: conmutador principal para esta cuenta.
  * `name`: etiqueta de visualización opcional.
  * `baseUrl`: URL del bus sintético.
  * `botUserId`: id de usuario de bot estilo Matrix usado en la gramática de destino.
  * `botDisplayName`: nombre de visualización para mensajes salientes.
  * `pollTimeoutMs`: ventana de espera de long-poll. Entero entre 100 y 30000.
  * `allowFrom`: lista de remitentes permitidos (ids de usuario o `"*"`). Los mensajes directos y la política de grupos permitidos usan estos ids de remitente sintéticos.
  * `groupPolicy`: política de sala compartida: `"open"` (predeterminado), `"allowlist"` o `"disabled"`.
  * `groupAllowFrom`: lista opcional de remitentes permitidos en salas compartidas. Cuando se omite bajo `"allowlist"`, QA Channel recurre a `allowFrom`.
  * `groups.<room>.requireMention`: exige una mención al bot antes de responder en una sala de grupo/canal específica. `groups."*"` establece el valor predeterminado.
  * `defaultTo`: destino alternativo cuando no se proporciona ninguno.
  * `actions.messages` / `actions.reactions` / `actions.search` / `actions.threads`: control de acceso a herramientas por acción.


Claves multicuenta en el nivel superior:

  * `accounts`: registro de sobrescrituras nombradas por cuenta, indexadas por id de cuenta.
  * `defaultAccount`: id de cuenta preferido cuando hay varias configuradas.


## Ejecutores

Autocomprobación del lado del host (escribe un informe Markdown en `.artifacts/qa-e2e/`):

bashCopy code
[code]
    pnpm qa:e2e
[/code]

Esto se enruta a través de `qa-lab`, inicia el bus de QA dentro del repositorio, arranca la porción de runtime incluida de `qa-channel` y ejecuta una autocomprobación determinista.

Suite completa de escenarios respaldada por el repositorio:

bashCopy code
[code]
    pnpm openclaw qa suite
[/code]

Ejecuta escenarios en paralelo contra el carril del Gateway de QA. Consulta la [descripción general de QA](</es/concepts/qa-e2e-automation>) para escenarios, perfiles y modos de proveedor.

Sitio de QA respaldado por Docker (Gateway + interfaz de depuración de QA Lab en una sola pila):

bashCopy code
[code]
    pnpm qa:lab:up
[/code]

Compila el sitio de QA, inicia la pila de Gateway respaldado por Docker + QA Lab e imprime la URL de QA Lab. Desde allí puedes elegir escenarios, seleccionar el carril del modelo, lanzar ejecuciones individuales y ver los resultados en vivo. El depurador de QA Lab es independiente del paquete de Control UI incluido.

## Relacionado

  * [Descripción general de QA](</es/concepts/qa-e2e-automation>): pila general, adaptadores de transporte, creación de escenarios
  * [QA de Matrix](</es/concepts/qa-matrix>): ejemplo de ejecutor de transporte en vivo que controla un canal real
  * [Emparejamiento](</es/channels/pairing>)
  * [Grupos](</es/channels/groups>)
  * [Descripción general de canales](</es/channels>)


Was this useful?YesNo