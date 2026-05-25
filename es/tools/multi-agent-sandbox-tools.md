---
title: Entorno aislado y herramientas multiagente
source_url: https://docs.openclaw.ai/es/tools/multi-agent-sandbox-tools
scraped_at: 2026-05-25
---

Cada agente en una configuración multiagente puede anular la política global de sandbox y herramientas. Esta página cubre la configuración por agente, las reglas de precedencia y ejemplos.

[**Aislamiento en sandbox** Backends y modos: referencia completa del sandbox. ](</es/gateway/sandboxing>) [**Sandbox frente a política de herramientas frente a elevado** Depurar "¿por qué está bloqueado esto?" ](</es/gateway/sandbox-vs-tool-policy-vs-elevated>) [**Modo elevado** Ejecución elevada para remitentes de confianza. ](</es/tools/elevated>)

* * *

## Ejemplos de configuración

Ejemplo 1: Agente personal + familiar restringido jsonCopy code
[code]
    {  "agents": {    "list": [      {        "id": "main",        "default": true,        "name": "Personal Assistant",        "workspace": "~/.openclaw/workspace",        "sandbox": { "mode": "off" }      },      {        "id": "family",        "name": "Family Bot",        "workspace": "~/.openclaw/workspace-family",        "sandbox": {          "mode": "all",          "scope": "agent"        },        "tools": {          "allow": ["read", "message"],          "deny": ["exec", "write", "edit", "apply_patch", "process", "browser"],          "message": {            "crossContext": {              "allowWithinProvider": false,              "allowAcrossProviders": false            }          }        }      }    ]  },  "bindings": [    {      "agentId": "family",      "match": {        "provider": "whatsapp",        "accountId": "*",        "peer": {          "kind": "group",          "id": "120363424282127706@g.us"        }      }    }  ]}
[/code]

**Resultado:**

  * Agente `main`: se ejecuta en el host, con acceso completo a herramientas.
  * Agente `family`: se ejecuta en Docker (un contenedor por agente), solo `read` y envíos de mensajes de la conversación actual.

Ejemplo 2: Agente de trabajo con sandbox compartido jsonCopy code
[code]
    {  "agents": {    "list": [      {        "id": "personal",        "workspace": "~/.openclaw/workspace-personal",        "sandbox": { "mode": "off" }      },      {        "id": "work",        "workspace": "~/.openclaw/workspace-work",        "sandbox": {          "mode": "all",          "scope": "shared",          "workspaceRoot": "/tmp/work-sandboxes"        },        "tools": {          "allow": ["read", "write", "apply_patch", "exec"],          "deny": ["browser", "gateway", "discord"]        }      }    ]  }}
[/code]

Ejemplo 2b: Perfil global de programación + agente solo de mensajería jsonCopy code
[code]
    {  "tools": { "profile": "coding" },  "agents": {    "list": [      {        "id": "support",        "tools": { "profile": "messaging", "allow": ["slack"] }      }    ]  }}
[/code]

**Resultado:**

  * los agentes predeterminados obtienen herramientas de programación.
  * el agente `support` es solo de mensajería (+ herramienta de Slack).

Ejemplo 3: Diferentes modos de sandbox por agente jsonCopy code
[code]
    {  "agents": {    "defaults": {      "sandbox": {        "mode": "non-main",        "scope": "session"      }    },    "list": [      {        "id": "main",        "workspace": "~/.openclaw/workspace",        "sandbox": {          "mode": "off"        }      },      {        "id": "public",        "workspace": "~/.openclaw/workspace-public",        "sandbox": {          "mode": "all",          "scope": "agent"        },        "tools": {          "allow": ["read"],          "deny": ["exec", "write", "edit", "apply_patch"]        }      }    ]  }}
[/code]

* * *

## Precedencia de configuración

Cuando existen configuraciones globales (`agents.defaults.*`) y específicas del agente (`agents.list[].*`):

### Configuración del sandbox

Las opciones específicas del agente anulan las globales:

CodeCopy code
[code]
    agents.list[].sandbox.mode > agents.defaults.sandbox.modeagents.list[].sandbox.scope > agents.defaults.sandbox.scopeagents.list[].sandbox.workspaceRoot > agents.defaults.sandbox.workspaceRootagents.list[].sandbox.workspaceAccess > agents.defaults.sandbox.workspaceAccessagents.list[].sandbox.docker.* > agents.defaults.sandbox.docker.*agents.list[].sandbox.browser.* > agents.defaults.sandbox.browser.*agents.list[].sandbox.prune.* > agents.defaults.sandbox.prune.*
[/code]

### Restricciones de herramientas

El orden de filtrado es:

* ### Perfil de herramientas

`tools.profile` o `agents.list[].tools.profile`.

* ### Perfil de herramientas del proveedor

`tools.byProvider[provider].profile` o `agents.list[].tools.byProvider[provider].profile`.

* ### Política global de herramientas

`tools.allow` / `tools.deny`.

* ### Política de herramientas del proveedor

`tools.byProvider[provider].allow/deny`.

* ### Política de herramientas específica del agente

`agents.list[].tools.allow/deny`.

* ### Política de proveedor del agente

`agents.list[].tools.byProvider[provider].allow/deny`.

* ### Política de herramientas del sandbox

`tools.sandbox.tools` o `agents.list[].tools.sandbox.tools`.

* ### Política de herramientas de subagente

`tools.subagents.tools`, si corresponde.

Reglas de precedencia

  * Cada nivel puede restringir más las herramientas, pero no puede volver a conceder herramientas denegadas en niveles anteriores.
  * Si `agents.list[].tools.sandbox.tools` está definido, reemplaza `tools.sandbox.tools` para ese agente.
  * Si `agents.list[].tools.profile` está definido, anula `tools.profile` para ese agente.
  * Las claves de herramientas de proveedor aceptan `provider` (por ejemplo, `google-antigravity`) o `provider/model` (por ejemplo, `openai/gpt-5.4`).

Comportamiento de listas de permitidos vacías

Si cualquier lista de permitidos explícita en esa cadena deja la ejecución sin herramientas invocables, OpenClaw se detiene antes de enviar el prompt al modelo. Esto es intencional: un agente configurado con una herramienta faltante como `agents.list[].tools.allow: ["query_db"]` debe fallar de forma evidente hasta que se habilite el plugin que registra `query_db`, no continuar como agente solo de texto.

Las políticas de herramientas admiten abreviaturas `group:*` que se expanden a varias herramientas. Consulta [Grupos de herramientas](</es/gateway/sandbox-vs-tool-policy-vs-elevated#tool-groups-shorthands>) para ver la lista completa.

Las anulaciones elevadas por agente (`agents.list[].tools.elevated`) pueden restringir aún más la ejecución elevada para agentes específicos. Consulta [Modo elevado](</es/tools/elevated>) para obtener más detalles.

* * *

## Migración desde un agente único

### Antes (agente único)

jsonCopy code
[code]
    {  "agents": {    "defaults": {      "workspace": "~/.openclaw/workspace",      "sandbox": {        "mode": "non-main"      }    }  },  "tools": {    "sandbox": {      "tools": {        "allow": ["read", "write", "apply_patch", "exec"],        "deny": []      }    }  }}
[/code]

### Después (multiagente)

jsonCopy code
[code]
    {  "agents": {    "list": [      {        "id": "main",        "default": true,        "workspace": "~/.openclaw/workspace",        "sandbox": { "mode": "off" }      }    ]  }}
[/code]

* * *

## Ejemplos de restricción de herramientas

### Agente de solo lectura

jsonCopy code
[code]
    {  "tools": {    "allow": ["read"],    "deny": ["exec", "write", "edit", "apply_patch", "process"]  }}
[/code]

### Ejecución de shell con herramientas del sistema de archivos deshabilitadas

jsonCopy code
[code]
    {  "tools": {    "allow": ["read", "exec", "process"],    "deny": ["write", "edit", "apply_patch", "browser", "gateway"]  }}
[/code]

### Solo comunicación

jsonCopy code
[code]
    {  "tools": {    "sessions": { "visibility": "tree" },    "allow": ["sessions_list", "sessions_send", "sessions_history", "session_status"],    "deny": ["exec", "write", "edit", "apply_patch", "read", "browser"]  }}
[/code]

`sessions_history` en este perfil sigue devolviendo una vista de recuerdo acotada y saneada, en lugar de un volcado sin procesar de la transcripción. El recuerdo del asistente elimina etiquetas de pensamiento, estructura auxiliar `<relevant-memories>`, cargas XML de llamadas a herramientas en texto plano (incluidos `<tool_call>...</tool_call>`, `<function_call>...</function_call>`, `<tool_calls>...</tool_calls>`, `<function_calls>...</function_calls>` y bloques truncados de llamadas a herramientas), estructura auxiliar degradada de llamadas a herramientas, tokens de control del modelo filtrados en ASCII/ancho completo y XML de llamadas a herramientas de MiniMax malformado antes de la redacción/truncamiento.

* * *

## Error común: "non-main"

* * *

## Pruebas

Después de configurar el sandbox y las herramientas multiagente:

* ### Comprobar la resolución de agentes

bashCopy code
[code]
    openclaw agents list --bindings
[/code]

* ### Verificar los contenedores de sandbox

bashCopy code
[code]
    docker ps --filter "name=openclaw-sbx-"
[/code]

* ### Probar las restricciones de herramientas

  * Envíe un mensaje que requiera herramientas restringidas.
  * Verifique que el agente no pueda usar herramientas denegadas.


* ### Supervisar registros

bashCopy code
[code]
    tail -f "${OPENCLAW_STATE_DIR:-$HOME/.openclaw}/logs/gateway.log" | grep -E "routing|sandbox|tools"
[/code]

* * *

## Solución de problemas

El agente no está en sandbox a pesar de `mode: 'all'`

  * Compruebe si hay un `agents.defaults.sandbox.mode` global que lo sobrescriba.
  * La configuración específica del agente tiene prioridad, así que establezca `agents.list[].sandbox.mode: "all"`.

Las herramientas siguen disponibles a pesar de la lista de denegación

  * Compruebe el orden de filtrado de herramientas: global → agente → sandbox → subagente.
  * Cada nivel solo puede restringir más, no volver a conceder.
  * Verifique con los registros: `[tools] filtering tools for agent:${agentId}`.

El contenedor no está aislado por agente

  * Establezca `scope: "agent"` en la configuración de sandbox específica del agente.
  * El valor predeterminado es `"session"`, que crea un contenedor por sesión.


* * *

## Relacionado

  * [Modo elevado](</es/tools/elevated>)
  * [Enrutamiento multiagente](</es/concepts/multi-agent>)
  * [Configuración de sandbox](</es/gateway/config-agents#agentsdefaultssandbox>)
  * [Sandbox frente a política de herramientas frente a elevado](</es/gateway/sandbox-vs-tool-policy-vs-elevated>) — depuración de "¿por qué está bloqueado esto?"
  * [Aislamiento en sandbox](</es/gateway/sandboxing>) — referencia completa del sandbox (modos, ámbitos, backends, imágenes)
  * [Gestión de sesiones](</es/concepts/session>)


Was this useful?YesNo