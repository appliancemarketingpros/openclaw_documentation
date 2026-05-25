---
title: Aprobaciones de ejecución
source_url: https://docs.openclaw.ai/es/tools/exec-approvals
scraped_at: 2026-05-25
---

Las aprobaciones de ejecución son la **barrera de seguridad de la app complementaria / host de Node** para permitir que un agente en sandbox ejecute comandos en un host real (`gateway` o `node`). Un enclavamiento de seguridad: los comandos se permiten solo cuando la política + la lista de permitidos + la aprobación del usuario (opcional) coinciden. Las aprobaciones de ejecución se apilan **por encima de** la política de herramientas y la puerta de elevación (salvo que elevated esté configurado en `full`, lo que omite las aprobaciones).

## Inspeccionar la política efectiva

Comando | Qué muestra  
---|---  
`openclaw approvals get` / `--gateway` / `--node <id|name|ip>` | Política solicitada, fuentes de política del host y el resultado efectivo.  
`openclaw exec-policy show` | Vista combinada de la máquina local.  
`openclaw exec-policy set` / `preset` | Sincroniza la política local solicitada con el archivo local de aprobaciones del host en un solo paso.  
  
Cuando un ámbito local solicita `host=node`, `exec-policy show` informa ese ámbito como administrado por Node en tiempo de ejecución, en lugar de fingir que el archivo local de aprobaciones es la fuente de verdad.

Si la UI de la app complementaria **no está disponible** , cualquier solicitud que normalmente pediría confirmación se resuelve mediante el **ask fallback** (valor predeterminado: `deny`).

## Dónde se aplica

Las aprobaciones de ejecución se aplican localmente en el host de ejecución:

  * **Host Gateway** → proceso `openclaw` en la máquina Gateway.
  * **Host Node** → ejecutor de Node (app complementaria de macOS o host Node sin interfaz).


### Modelo de confianza

  * Los llamadores autenticados por Gateway son operadores de confianza para ese Gateway.
  * Los nodos emparejados extienden esa capacidad de operador de confianza al host Node.
  * Las aprobaciones de ejecución reducen el riesgo de ejecución accidental, pero **no** son un límite de autenticación por usuario ni una política de solo lectura del sistema de archivos.
  * Una vez aprobado, un comando puede modificar archivos según los permisos del host o del sistema de archivos del sandbox seleccionado.
  * Las ejecuciones aprobadas en host Node vinculan el contexto de ejecución canónico: cwd canónico, argv exacto, enlace de env cuando está presente y ruta de ejecutable fijada cuando corresponde.
  * Para scripts de shell e invocaciones directas de archivos de intérprete/runtime, OpenClaw también intenta vincular un operando de archivo local concreto. Si ese archivo vinculado cambia después de la aprobación pero antes de la ejecución, la ejecución se deniega en lugar de ejecutar contenido desviado.
  * La vinculación de archivos es intencionadamente de mejor esfuerzo, **no** un modelo semántico completo de cada ruta de carga de intérprete/runtime. Si el modo de aprobación no puede identificar exactamente un archivo local concreto que vincular, se niega a emitir una ejecución respaldada por aprobación en lugar de fingir cobertura completa.


### División en macOS

  * El **servicio de host Node** reenvía `system.run` a la **app de macOS** mediante IPC local.
  * La **app de macOS** aplica las aprobaciones y ejecuta el comando en contexto de UI.


## Configuración y almacenamiento

Las aprobaciones viven en un archivo JSON local en el host de ejecución:

textCopy code
[code]
    ~/.openclaw/exec-approvals.json
[/code]

Esquema de ejemplo:

jsonCopy code
[code]
    {  "version": 1,  "socket": {    "path": "~/.openclaw/exec-approvals.sock",    "token": "base64url-token"  },  "defaults": {    "security": "deny",    "ask": "on-miss",    "askFallback": "deny",    "autoAllowSkills": false  },  "agents": {    "main": {      "security": "allowlist",      "ask": "on-miss",      "askFallback": "deny",      "autoAllowSkills": true,      "allowlist": [        {          "id": "B0C8C0B3-2C2D-4F8A-9A3C-5A4B3C2D1E0F",          "pattern": "~/Projects/**/bin/rg",          "source": "allow-always",          "commandText": "rg -n TODO",          "lastUsedAt": 1737150000000,          "lastUsedCommand": "rg -n TODO",          "lastResolvedPath": "/Users/user/Projects/.../bin/rg"        }      ]    }  }}
[/code]

## Controles de política

### `exec.security`

  * `deny` \- bloquea todas las solicitudes de ejecución en host.
  * `allowlist` \- permite solo comandos en la lista de permitidos.
  * `full` \- permite todo (equivalente a elevated).


### `exec.ask`

  * `off` \- nunca solicita confirmación.
  * `on-miss` \- solicita confirmación solo cuando la lista de permitidos no coincide.
  * `always` \- solicita confirmación en cada comando. La confianza duradera `allow-always` **no** suprime las solicitudes cuando el modo ask efectivo es `always`.


### `askFallback`

Resolución cuando se requiere una solicitud de confirmación pero no hay ninguna UI accesible.

  * `deny` \- bloquea.
  * `allowlist` \- permite solo si la lista de permitidos coincide.
  * `full` \- permite.


### `tools.exec.strictInlineEval`

Cuando es `true`, OpenClaw trata las formas de evaluación de código en línea como solo aprobables aunque el binario del intérprete esté en la lista de permitidos. Defensa en profundidad para cargadores de intérprete que no se asignan limpiamente a un único operando de archivo estable.

Ejemplos que captura el modo estricto:

  * `python -c`
  * `node -e`, `node --eval`, `node -p`
  * `ruby -e`
  * `perl -e`, `perl -E`
  * `php -r`
  * `lua -e`
  * `osascript -e`


En modo estricto, estos comandos siguen necesitando aprobación explícita, y `allow-always` no conserva automáticamente nuevas entradas de lista de permitidos para ellos.

### `tools.exec.commandHighlighting`

Controla solo la presentación en las solicitudes de aprobación de ejecución. Cuando está habilitado, OpenClaw puede adjuntar intervalos de comando derivados del analizador para que las solicitudes de aprobación Web puedan resaltar tokens de comando. Configúralo en `true` para habilitar el resaltado de texto de comandos.

Esta configuración **no** cambia `security`, `ask`, la coincidencia de la lista de permitidos, el comportamiento estricto de inline-eval, el reenvío de aprobaciones ni la ejecución de comandos. Puede configurarse globalmente en `tools.exec.commandHighlighting` o por agente en `agents.list[].tools.exec.commandHighlighting`.

## Modo YOLO (sin aprobación)

Si quieres que la ejecución en host se ejecute sin solicitudes de aprobación, debes abrir **ambas** capas de política: la política de ejecución solicitada en la configuración de OpenClaw (`tools.exec.*`) **y** la política local de aprobaciones del host en `~/.openclaw/exec-approvals.json`.

YOLO es el comportamiento predeterminado del host salvo que lo restrinjas explícitamente:

Capa | Configuración YOLO  
---|---  
`tools.exec.security` | `full` en `gateway`/`node`  
`tools.exec.ask` | `off`  
Host `askFallback` | `full`  
  
Los proveedores respaldados por CLI que exponen su propio modo de permisos no interactivo pueden seguir esta política. Claude CLI añade `--permission-mode bypassPermissions` cuando la política de ejecución solicitada por OpenClaw es YOLO. Anula ese comportamiento de backend con argumentos explícitos de Claude en `agents.defaults.cliBackends.claude-cli.args` / `resumeArgs` \- por ejemplo `--permission-mode default`, `acceptEdits` o `bypassPermissions`.

Si quieres una configuración más conservadora, vuelve a restringir cualquiera de las capas a `allowlist` / `on-miss` o `deny`.

### Configuración persistente de "nunca solicitar" en host Gateway

* ### Configura la política solicitada de configuración

bashCopy code
[code]
    openclaw config set tools.exec.host gatewayopenclaw config set tools.exec.security fullopenclaw config set tools.exec.ask offopenclaw gateway restart
[/code]

* ### Haz coincidir el archivo de aprobaciones del host

bashCopy code
[code]
    openclaw approvals set --stdin <<'EOF'{  version: 1,  defaults: {    security: "full",    ask: "off",    askFallback: "full"  }}EOF
[/code]

### Atajo local

bashCopy code
[code]
    openclaw exec-policy preset yolo
[/code]

Ese atajo local actualiza ambos:

  * `tools.exec.host/security/ask` local.
  * Valores predeterminados locales de `~/.openclaw/exec-approvals.json`.


Es intencionadamente solo local. Para cambiar aprobaciones de host Gateway o host Node de forma remota, usa `openclaw approvals set --gateway` o `openclaw approvals set --node <id|name|ip>`.

### Host Node

Para un host Node, aplica el mismo archivo de aprobaciones en ese Node:

bashCopy code
[code]
    openclaw approvals set --node <id|name|ip> --stdin <<'EOF'{  version: 1,  defaults: {    security: "full",    ask: "off",    askFallback: "full"  }}EOF
[/code]

### Atajo solo de sesión

  * `/exec security=full ask=off` cambia solo la sesión actual.
  * `/elevated full` es un atajo de emergencia que también omite las aprobaciones de ejecución para esa sesión.


Si el archivo de aprobaciones del host sigue siendo más estricto que la configuración, la política más estricta del host sigue ganando.

## Lista de permitidos (por agente)

Las listas de permitidos son **por agente**. Si existen varios agentes, cambia qué agente estás editando en la app de macOS. Los patrones son coincidencias glob.

Los patrones pueden ser globs de ruta de binario resuelta o globs de nombre de comando simple. Los nombres simples coinciden solo con comandos invocados mediante `PATH`, por lo que `rg` puede coincidir con `/opt/homebrew/bin/rg` cuando el comando es `rg`, pero **no** con `./rg` ni `/tmp/rg`. Usa un glob de ruta cuando quieras confiar en una ubicación de binario específica.

Las entradas heredadas `agents.default` se migran a `agents.main` al cargar. Las cadenas de shell como `echo ok && pwd` siguen necesitando que cada segmento de nivel superior satisfaga las reglas de la lista de permitidos.

Ejemplos:

  * `rg`
  * `~/Projects/**/bin/peekaboo`
  * `~/.local/bin/*`
  * `/opt/homebrew/bin/rg`


### Restringir argumentos con argPattern

Añade `argPattern` cuando una entrada de lista de permitidos deba coincidir con un binario y una forma específica de argumentos. OpenClaw evalúa la expresión regular contra los argumentos de comando analizados, excluido el token ejecutable (`argv[0]`). Para entradas escritas a mano, los argumentos se unen con un solo espacio, así que ancla el patrón cuando necesites una coincidencia exacta.

jsonCopy code
[code]
    {  "version": 1,  "agents": {    "main": {      "allowlist": [        {          "pattern": "python3",          "argPattern": "^safe\\.py$"        }      ]    }  }}
[/code]

Esa entrada permite `python3 safe.py`; `python3 other.py` no coincide con la lista de permitidos. Si también está presente una entrada solo de ruta para el mismo binario, los argumentos sin coincidencia todavía pueden recurrir a esa entrada solo de ruta. Omite la entrada solo de ruta cuando el objetivo sea restringir el binario a los argumentos declarados.

Las entradas guardadas por flujos de aprobación pueden usar un formato de separador interno para la coincidencia exacta de argv. Prefiere la UI o el flujo de aprobación para regenerar esas entradas en lugar de editar manualmente el valor codificado. Si OpenClaw no puede analizar argv para un segmento de comando, las entradas con `argPattern` no coinciden.

Cada entrada de la lista de permitidos admite:

Campo | Significado  
---|---  
`pattern` | Glob de ruta binaria resuelta o glob de nombre de comando simple  
`argPattern` | Regex argv opcional; las entradas omitidas son solo de ruta  
`id` | UUID estable usado para la identidad de la UI  
`source` | Origen de la entrada, como `allow-always`  
`commandText` | Texto del comando capturado cuando un flujo de aprobación creó la entrada  
`lastUsedAt` | Marca de tiempo de último uso  
`lastUsedCommand` | Último comando que coincidió  
`lastResolvedPath` | Última ruta binaria resuelta  
  
## Autoaprobar CLI de Skills

Cuando **Autoaprobar CLI de Skills** está habilitado, los ejecutables referenciados por Skills conocidos se tratan como permitidos en nodos (nodo macOS o host de nodo sin interfaz). Esto usa `skills.bins` sobre el RPC del Gateway para obtener la lista de binarios de Skills. Deshabilita esto si quieres listas de permitidos manuales estrictas.

## Binarios seguros y reenvío de aprobaciones

Para binarios seguros (la ruta rápida solo por stdin), los detalles de vinculación de intérpretes y cómo reenviar solicitudes de aprobación a Slack/Discord/Telegram (o ejecutarlas como clientes de aprobación nativos), consulta [Aprobaciones de ejecución: avanzado](</es/tools/exec-approvals-advanced>).

## Edición en la UI de control

Usa la tarjeta **UI de control → Nodos → Aprobaciones de ejecución** para editar valores predeterminados, sobrescrituras por agente y listas de permitidos. Elige un ámbito (Predeterminados o un agente), ajusta la política, agrega/elimina patrones de lista de permitidos y luego **Guardar**. La UI muestra metadatos de último uso por patrón para que puedas mantener la lista ordenada.

El selector de destino elige **Gateway** (aprobaciones locales) o un **Nodo**. Los nodos deben anunciar `system.execApprovals.get/set` (app de macOS o host de nodo sin interfaz). Si un nodo aún no anuncia aprobaciones de ejecución, edita directamente su `~/.openclaw/exec-approvals.json` local.

CLI: `openclaw approvals` admite la edición de gateway o nodo; consulta [CLI de aprobaciones](</es/cli/approvals>).

## Flujo de aprobación

Cuando se requiere una solicitud, el gateway transmite `exec.approval.requested` a los clientes operadores. La UI de control y la app de macOS la resuelven mediante `exec.approval.resolve`, luego el gateway reenvía la solicitud aprobada al host del nodo.

Para `host=node`, las solicitudes de aprobación incluyen una carga útil canónica `systemRunPlan`. El gateway usa ese plan como el contexto autorizado de comando/cwd/sesión al reenviar solicitudes `system.run` aprobadas.

Esto importa para la latencia de aprobación asíncrona:

  * La ruta de ejecución del nodo prepara un plan canónico por adelantado.
  * El registro de aprobación almacena ese plan y sus metadatos de vinculación.
  * Una vez aprobado, la llamada `system.run` reenviada final reutiliza el plan almacenado en lugar de confiar en ediciones posteriores del llamador.
  * Si el llamador cambia `command`, `rawCommand`, `cwd`, `agentId` o `sessionKey` después de que se creó la solicitud de aprobación, el gateway rechaza la ejecución reenviada como una discrepancia de aprobación.


## Eventos del sistema

El ciclo de vida de la ejecución se expone como mensajes del sistema:

  * `Exec running` (solo si el comando supera el umbral de aviso de ejecución).
  * `Exec finished`.
  * `Exec denied`.


Estos se publican en la sesión del agente después de que el nodo informa el evento. Las aprobaciones de ejecución alojadas en Gateway emiten los mismos eventos de ciclo de vida cuando el comando finaliza (y, opcionalmente, cuando se ejecuta más tiempo que el umbral). Las ejecuciones protegidas por aprobación reutilizan el id de aprobación como `runId` en estos mensajes para facilitar la correlación.

## Comportamiento de aprobaciones denegadas

Cuando se deniega una aprobación de ejecución asíncrona, OpenClaw impide que el agente reutilice la salida de cualquier ejecución anterior del mismo comando en la sesión. El motivo de denegación se pasa con una guía explícita de que no hay salida de comando disponible, lo que impide que el agente afirme que hay salida nueva o repita el comando denegado con resultados obsoletos de una ejecución correcta anterior.

## Implicaciones

  * **`full`** es potente; prefiere listas de permitidos cuando sea posible.
  * **`ask`** te mantiene al tanto y aun así permite aprobaciones rápidas.
  * Las listas de permitidos por agente evitan que las aprobaciones de un agente se filtren a otros.
  * Las aprobaciones solo se aplican a solicitudes de ejecución del host de **remitentes autorizados**. Los remitentes no autorizados no pueden emitir `/exec`.
  * `/exec security=full` es una comodidad a nivel de sesión para operadores autorizados y omite las aprobaciones por diseño. Para bloquear de forma estricta la ejecución en el host, configura la seguridad de aprobaciones como `deny` o deniega la herramienta `exec` mediante la política de herramientas.


## Relacionado

[**Aprobaciones de ejecución: avanzado** Binarios seguros, vinculación de intérpretes y reenvío de aprobaciones al chat. ](</es/tools/exec-approvals-advanced>) [**Herramienta de ejecución** Herramienta de ejecución de comandos de shell. ](</es/tools/exec>) [**Modo elevado** Ruta de emergencia que también omite aprobaciones. ](</es/tools/elevated>) [**Aislamiento** Modos de aislamiento y acceso al espacio de trabajo. ](</es/gateway/sandboxing>) [**Seguridad** Modelo de seguridad y endurecimiento. ](</es/gateway/security>) [**Aislamiento vs política de herramientas vs elevado** Cuándo recurrir a cada control. ](</es/gateway/sandbox-vs-tool-policy-vs-elevated>) [**Skills** Comportamiento de autoaprobación respaldado por Skills. ](</es/tools/skills>)

Was this useful?YesNo