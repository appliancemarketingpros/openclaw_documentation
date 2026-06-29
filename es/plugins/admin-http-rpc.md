---
title: Plugin RPC HTTP de administración
source_url: https://docs.openclaw.ai/es/plugins/admin-http-rpc
scraped_at: 2026-06-29
---

CapabilitiesBundled plugin guides

El plugin incluido `admin-http-rpc` expone métodos seleccionados del plano de control del Gateway mediante HTTP para automatización de hosts de confianza que no puede usar el cliente RPC WebSocket normal del Gateway.

El plugin se incluye con OpenClaw, pero está desactivado de forma predeterminada. Cuando está desactivado, la ruta no se registra. Cuando está activado, añade:

  * `POST /api/v1/admin/rpc`
  * el mismo listener que el Gateway: `http://<gateway-host>:<port>/api/v1/admin/rpc`


Actívalo solo para herramientas privadas del host, automatización de tailnet o un ingreso interno de confianza. No expongas esta ruta directamente a la internet pública.

## Antes de activarlo

Admin HTTP RPC es una superficie completa del plano de control del operador. Cualquier llamador que pase la autenticación HTTP del Gateway puede invocar los métodos permitidos en esta página.

Úsalo cuando todo esto sea cierto:

  * El llamador es de confianza para operar el Gateway.
  * El llamador no puede usar el cliente RPC WebSocket.
  * La ruta solo es accesible en loopback, una tailnet o un ingreso privado autenticado.
  * Has revisado los métodos permitidos y coinciden con la automatización que planeas ejecutar.


Usa la ruta RPC WebSocket para clientes de OpenClaw y herramientas interactivas que puedan mantener abierta una conexión WebSocket del Gateway.

## Activar

Activa el plugin incluido:

### CLI

bashCopy code
[code]
    openclaw plugins enable admin-http-rpcopenclaw gateway restart
[/code]

### Config

json5Copy code
[code]
    {  plugins: {    entries: {      "admin-http-rpc": { enabled: true },    },  },}
[/code]

La ruta se registra durante el inicio del plugin. Reinicia el Gateway después de cambiar la configuración del plugin.

Desactívalo cuando ya no necesites la superficie HTTP:

bashCopy code
[code]
    openclaw plugins disable admin-http-rpcopenclaw gateway restart
[/code]

## Verificar la ruta

Usa `health` como la solicitud segura más pequeña:

bashCopy code
[code]
    curl -sS http://<gateway-host>:<port>/api/v1/admin/rpc \  -H 'Authorization: Bearer <gateway-token>' \  -H 'Content-Type: application/json' \  -d '{"method":"health","params":{}}'
[/code]

Una respuesta correcta tiene `ok: true`:

jsonCopy code
[code]
    {  "id": "generated-request-id",  "ok": true,  "payload": {    "status": "ok"  }}
[/code]

Cuando el plugin está desactivado, la ruta devuelve `404` porque no está registrada.

## Autenticación

La ruta del plugin usa la autenticación HTTP del Gateway.

Rutas de autenticación comunes:

  * autenticación con secreto compartido (`gateway.auth.mode="token"` o `"password"`): `Authorization: Bearer <token-or-password>`
  * autenticación HTTP con identidad de confianza (`gateway.auth.mode="trusted-proxy"`): enruta a través del proxy configurado con conocimiento de identidad y deja que inyecte los encabezados de identidad requeridos
  * autenticación abierta de ingreso privado (`gateway.auth.mode="none"`): no se requiere encabezado de autenticación


## Modelo de seguridad

Trata este plugin como una superficie completa de operador del Gateway.

  * Activar el plugin ofrece intencionalmente acceso a los métodos RPC de administración permitidos en `/api/v1/admin/rpc`.
  * El plugin declara el contrato de manifiesto reservado `contracts.gatewayMethodDispatch: ["authenticated-request"]` para que su ruta HTTP autenticada por el Gateway pueda despachar métodos del plano de control en el proceso.
  * La autenticación bearer con secreto compartido demuestra la posesión del secreto del operador del gateway.
  * Para autenticación `token` y `password`, se ignoran encabezados `x-openclaw-scopes` más restringidos y se restauran los valores predeterminados normales de operador completo.
  * Los modos HTTP con identidad de confianza respetan `x-openclaw-scopes` cuando está presente.
  * `gateway.auth.mode="none"` significa que esta ruta no está autenticada si el plugin está activado. Úsalo solo detrás de un ingreso privado en el que confíes plenamente.
  * Las solicitudes se despachan a través de los mismos manejadores de métodos del Gateway y comprobaciones de alcance que RPC WebSocket después de que pasa la autenticación de la ruta del plugin.
  * Mantén esta ruta en loopback, tailnet o un ingreso privado de confianza. No la expongas directamente a la internet pública.
  * Los contratos de manifiesto de plugin no son un sandbox. Evitan el uso accidental de helpers reservados del SDK; los plugins de confianza aun así se ejecutan en el proceso del Gateway.


Usa gateways separados cuando los llamadores crucen límites de confianza.

## Solicitud

httpCopy code
[code]
    POST /api/v1/admin/rpcAuthorization: Bearer <gateway-token>Content-Type: application/json
[/code]

jsonCopy code
[code]
    {  "id": "optional-request-id",  "method": "health",  "params": {}}
[/code]

Campos:

  * `id` (cadena, opcional): se copia en la respuesta. Se genera un UUID cuando se omite.
  * `method` (cadena, obligatorio): nombre de método permitido del Gateway.
  * `params` (cualquiera, opcional): parámetros específicos del método.


El tamaño máximo predeterminado del cuerpo de la solicitud es 1 MB.

## Respuesta

Las respuestas correctas usan la forma RPC del Gateway:

jsonCopy code
[code]
    {  "id": "optional-request-id",  "ok": true,  "payload": {}}
[/code]

Los errores de método del Gateway usan:

jsonCopy code
[code]
    {  "id": "optional-request-id",  "ok": false,  "error": {    "code": "INVALID_REQUEST",    "message": "bad params"  }}
[/code]

El estado HTTP sigue el error del Gateway cuando es posible. Por ejemplo, `INVALID_REQUEST` devuelve `400` y `UNAVAILABLE` devuelve `503`.

## Métodos permitidos

  * descubrimiento: `commands.list` Devuelve los nombres de métodos HTTP RPC permitidos por este plugin.
  * gateway: `health`, `status`, `logs.tail`, `usage.status`, `usage.cost`, `gateway.restart.request`
  * config: `config.get`, `config.schema`, `config.schema.lookup`, `config.set`, `config.patch`, `config.apply`
  * canales: `channels.status`, `channels.start`, `channels.stop`, `channels.logout`
  * web: `web.login.start`, `web.login.wait`
  * modelos: `models.list`, `models.authStatus`
  * agentes: `agents.list`, `agents.create`, `agents.update`, `agents.delete`
  * aprobaciones: `exec.approvals.get`, `exec.approvals.set`, `exec.approvals.node.get`, `exec.approvals.node.set`
  * cron: `cron.status`, `cron.list`, `cron.get`, `cron.runs`, `cron.add`, `cron.update`, `cron.remove`, `cron.run`
  * dispositivos: `device.pair.list`, `device.pair.approve`, `device.pair.reject`, `device.pair.remove`
  * nodos: `node.list`, `node.describe`, `node.pair.list`, `node.pair.approve`, `node.pair.reject`, `node.pair.remove`, `node.rename`
  * tareas: `tasks.list`, `tasks.get`, `tasks.cancel`
  * diagnósticos: `doctor.memory.status`, `update.status`


Otros métodos del Gateway se bloquean hasta que se añadan intencionalmente.

## Comparación con WebSocket

La ruta RPC WebSocket normal del Gateway sigue siendo la API de plano de control preferida para los clientes de OpenClaw. Usa admin HTTP RPC solo para herramientas de host que necesitan una superficie HTTP de solicitud/respuesta.

Los clientes WebSocket con token compartido sin una identidad de dispositivo de confianza no pueden autodeclarar alcances de administrador durante la conexión. Admin HTTP RPC sigue deliberadamente el modelo de operador HTTP de confianza existente: cuando el plugin está activado, la autenticación bearer con secreto compartido se trata como acceso de operador completo para esta superficie de administración.

## Solución de problemas

`404 Not Found`

: El plugin está desactivado, el Gateway no se ha reiniciado desde que se activó o la solicitud va a un proceso de Gateway diferente.

`401 Unauthorized`

: La solicitud no satisfizo la autenticación HTTP del Gateway. Comprueba el token bearer o los encabezados de identidad del proxy de confianza.

`400 INVALID_REQUEST`

: El cuerpo de la solicitud no es JSON válido, falta el campo `method` o el método no está en la lista de permitidos del plugin.

`503 UNAVAILABLE`

: El manejador de métodos del Gateway no está disponible. Revisa los registros del Gateway y vuelve a intentarlo después de que el Gateway termine de iniciarse.

## Relacionado

  * [Alcances de operador](</es/gateway/operator-scopes>)
  * [Seguridad del Gateway](</es/gateway/security>)
  * [Acceso remoto](</es/gateway/remote>)
  * [Manifiesto de plugin](</es/plugins/manifest#contracts>)
  * [Subrutas del SDK](</es/plugins/sdk-subpaths>)


Was this useful?YesNo

Open issue