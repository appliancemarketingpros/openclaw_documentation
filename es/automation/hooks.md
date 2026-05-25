---
title: Ganchos
source_url: https://docs.openclaw.ai/es/automation/hooks
scraped_at: 2026-05-25
---

Los hooks son pequeños scripts que se ejecutan cuando algo sucede dentro del Gateway. Se pueden descubrir desde directorios e inspeccionar con `openclaw hooks`. El Gateway carga hooks internos solo después de que habilitas los hooks o configuras al menos una entrada de hook, un paquete de hooks, un controlador heredado o un directorio adicional de hooks.

Hay dos tipos de hooks en OpenClaw:

  * **Hooks internos** (esta página): se ejecutan dentro del Gateway cuando se disparan eventos de agente, como `/new`, `/reset`, `/stop` o eventos de ciclo de vida.
  * **Webhooks** : endpoints HTTP externos que permiten que otros sistemas activen trabajo en OpenClaw. Consulta [Webhooks](</es/automation/cron-jobs#webhooks>).


Los hooks también pueden incluirse dentro de plugins. `openclaw hooks list` muestra tanto hooks independientes como hooks administrados por plugins.

## Inicio rápido

bashCopy code
[code]
    # List available hooksopenclaw hooks list # Enable a hookopenclaw hooks enable session-memory # Check hook statusopenclaw hooks check # Get detailed informationopenclaw hooks info session-memory
[/code]

## Tipos de evento

Evento | Cuándo se dispara  
---|---  
`command:new` | Se emitió el comando `/new`  
`command:reset` | Se emitió el comando `/reset`  
`command:stop` | Se emitió el comando `/stop`  
`command` | Cualquier evento de comando (listener general)  
`session:compact:before` | Antes de que Compaction resuma el historial  
`session:compact:after` | Después de que Compaction finaliza  
`session:patch` | Cuando se modifican propiedades de sesión  
`agent:bootstrap` | Antes de inyectar los archivos de bootstrap del workspace  
`gateway:startup` | Después de que los canales inician y se cargan los hooks  
`gateway:shutdown` | Cuando comienza el cierre del Gateway  
`gateway:pre-restart` | Antes de un reinicio esperado del Gateway  
`message:received` | Mensaje entrante desde cualquier canal  
`message:transcribed` | Después de que finaliza la transcripción de audio  
`message:preprocessed` | Después de que el preprocesamiento de medios y enlaces finaliza o se omite  
`message:sent` | Mensaje saliente entregado  
  
## Escritura de hooks

### Estructura del hook

Cada hook es un directorio que contiene dos archivos:

CodeCopy code
[code]
    my-hook/├── HOOK.md          # Metadata + documentation└── handler.ts       # Handler implementation
[/code]

### Formato de [HOOK.md](<http://HOOK.md>)

markdownCopy code
[code]
    ---name: my-hookdescription: "Short description of what this hook does"metadata:  { "openclaw": { "emoji": "🔗", "events": ["command:new"], "requires": { "bins": ["node"] } } }--- # My Hook Detailed documentation goes here.
[/code]

**Campos de metadatos** (`metadata.openclaw`):

Campo | Descripción  
---|---  
`emoji` | Emoji de visualización para la CLI  
`events` | Array de eventos que escuchar  
`export` | Exportación con nombre que usar (por defecto `"default"`)  
`os` | Plataformas requeridas (por ejemplo, `["darwin", "linux"]`)  
`requires` | Rutas de `bins`, `anyBins`, `env` o `config` requeridas  
`always` | Omitir comprobaciones de elegibilidad (booleano)  
`install` | Métodos de instalación  
  
### Implementación del controlador

typescriptCopy code
[code]
    const handler = async (event) => {  if (event.type !== "command" || event.action !== "new") {    return;  }   console.log(`[my-hook] New command triggered`);  // Your logic here   // Optionally send message to user  event.messages.push("Hook executed!");}; export default handler;
[/code]

Cada evento incluye: `type`, `action`, `sessionKey`, `timestamp`, `messages` (haz push para enviar al usuario) y `context` (datos específicos del evento). Los contextos de hooks de agente y de Plugin de herramientas también pueden incluir `trace`, un contexto de traza diagnóstica de solo lectura compatible con W3C que los plugins pueden pasar a logs estructurados para correlación con OTEL.

### Aspectos destacados del contexto de evento

**Eventos de comando** (`command:new`, `command:reset`): `context.sessionEntry`, `context.previousSessionEntry`, `context.commandSource`, `context.workspaceDir`, `context.cfg`.

**Eventos de mensaje** (`message:received`): `context.from`, `context.content`, `context.channelId`, `context.metadata` (datos específicos del proveedor, incluidos `senderId`, `senderName`, `guildId`). `context.content` prefiere un cuerpo de comando no vacío para mensajes similares a comandos; luego recurre al cuerpo entrante sin procesar y al cuerpo genérico; no incluye enriquecimiento exclusivo del agente, como historial de hilo o resúmenes de enlaces.

**Eventos de mensaje** (`message:sent`): `context.to`, `context.content`, `context.success`, `context.channelId`.

**Eventos de mensaje** (`message:transcribed`): `context.transcript`, `context.from`, `context.channelId`, `context.mediaPath`.

**Eventos de mensaje** (`message:preprocessed`): `context.bodyForAgent` (cuerpo enriquecido final), `context.from`, `context.channelId`.

**Eventos de bootstrap** (`agent:bootstrap`): `context.bootstrapFiles` (array mutable), `context.agentId`.

**Eventos de parche de sesión** (`session:patch`): `context.sessionEntry`, `context.patch` (solo campos modificados), `context.cfg`. Solo los clientes con privilegios pueden activar eventos de parche.

**Eventos de Compaction** : `session:compact:before` incluye `messageCount`, `tokenCount`. `session:compact:after` agrega `compactedCount`, `summaryLength`, `tokensBefore`, `tokensAfter`.

`command:stop` observa que el usuario emite `/stop`; es ciclo de vida de cancelación/comando, no una puerta de finalización del agente. Los plugins que necesitan inspeccionar una respuesta final natural y pedir al agente una pasada más deben usar el hook de Plugin tipado `before_agent_finalize` en su lugar. Consulta [Hooks de Plugin](</es/plugins/hooks>).

**Eventos de ciclo de vida del Gateway** : `gateway:shutdown` incluye `reason` y `restartExpectedMs`, y se dispara cuando comienza el cierre del Gateway. `gateway:pre-restart` incluye el mismo contexto, pero solo se dispara cuando el cierre forma parte de un reinicio esperado y se proporciona un valor finito de `restartExpectedMs`. Durante el cierre, cada espera de hook de ciclo de vida es de mejor esfuerzo y acotada, de modo que el cierre continúa si un controlador se queda bloqueado.

Entre el evento `gateway:shutdown` (o `gateway:pre-restart`) y el resto de la secuencia de cierre, el Gateway también dispara un hook de Plugin tipado `session_end` para cada sesión que seguía activa cuando el proceso se detuvo. El `reason` del evento es `shutdown` para una detención SIGTERM/SIGINT simple y `restart` cuando el cierre se programó como parte de un reinicio esperado. Este drenaje está acotado para que un controlador `session_end` lento no pueda bloquear la salida del proceso, y las sesiones que ya se han finalizado mediante reemplazo / restablecimiento / eliminación / Compaction se omiten para evitar disparos duplicados.

## Descubrimiento de hooks

Los hooks se descubren desde estos directorios, en orden de precedencia de anulación creciente:

  1. **Hooks incluidos** : enviados con OpenClaw
  2. **Hooks de Plugin** : hooks incluidos dentro de plugins instalados
  3. **Hooks administrados** : `~/.openclaw/hooks/` (instalados por el usuario, compartidos entre workspaces). Los directorios adicionales de `hooks.internal.load.extraDirs` comparten esta precedencia.
  4. **Hooks de workspace** : `<workspace>/hooks/` (por agente, deshabilitados por defecto hasta que se habilitan explícitamente)


Los hooks de workspace pueden agregar nuevos nombres de hook, pero no pueden anular hooks incluidos, administrados o proporcionados por plugins con el mismo nombre.

El Gateway omite el descubrimiento de hooks internos al iniciar hasta que los hooks internos estén configurados. Habilita un hook incluido o administrado con `openclaw hooks enable <name>`, instala un paquete de hooks o establece `hooks.internal.enabled=true` para participar. Cuando habilitas un hook con nombre, el Gateway carga solo el controlador de ese hook; `hooks.internal.enabled=true`, los directorios adicionales de hooks y los controladores heredados optan por el descubrimiento amplio.

### Paquetes de hooks

Los paquetes de hooks son paquetes npm que exportan hooks mediante `openclaw.hooks` en `package.json`. Instala con:

bashCopy code
[code]
    openclaw plugins install <path-or-spec>
[/code]

Las especificaciones de npm son solo de registro (nombre de paquete + versión exacta opcional o dist-tag). Las especificaciones Git/URL/archivo y los rangos semver se rechazan.

## Hooks incluidos

Hook | Eventos | Qué hace  
---|---|---  
session-memory | `command:new`, `command:reset` | Guarda el contexto de sesión en `<workspace>/memory/`  
bootstrap-extra-files | `agent:bootstrap` | Inyecta archivos de bootstrap adicionales desde patrones glob  
command-logger | `command` | Registra todos los comandos en `~/.openclaw/logs/commands.log`  
compaction-notifier | `session:compact:before`, `session:compact:after` | Envía avisos visibles al chat cuando la Compaction de sesión comienza/termina  
boot-md | `gateway:startup` | Ejecuta `BOOT.md` cuando se inicia el Gateway  
  
Habilita cualquier hook incluido:

bashCopy code
[code]
    openclaw hooks enable <hook-name>
[/code]

### Detalles de session-memory

Extrae los últimos 15 mensajes de usuario/asistente y los guarda en `<workspace>/memory/YYYY-MM-DD-HHMM.md` usando la fecha local del host. La captura de memoria se ejecuta en segundo plano para que los acuses de recibo de `/new` y `/reset` no se retrasen por lecturas de transcripción o generación opcional de slug. Establece `hooks.internal.entries.session-memory.llmSlug: true` para generar slugs descriptivos de nombres de archivo con el modelo configurado. Requiere que `workspace.dir` esté configurado.

### Configuración de bootstrap-extra-files

jsonCopy code
[code]
    {  "hooks": {    "internal": {      "entries": {        "bootstrap-extra-files": {          "enabled": true,          "paths": ["packages/*/AGENTS.md", "packages/*/TOOLS.md"]        }      }    }  }}
[/code]

Las rutas se resuelven relativas al workspace. Solo se cargan los basenames de bootstrap reconocidos (`AGENTS.md`, `SOUL.md`, `TOOLS.md`, `IDENTITY.md`, `USER.md`, `HEARTBEAT.md`, `BOOTSTRAP.md`, `MEMORY.md`).

### Detalles de command-logger

Registra cada comando de barra en `~/.openclaw/logs/commands.log`.

### Detalles de compaction-notifier

Envía mensajes de estado breves a la conversación actual cuando OpenClaw empieza y termina de compactar la transcripción de la sesión. Esto hace que los turnos largos sean menos confusos en superficies de chat, porque el usuario puede ver que el asistente está resumiendo el contexto y continuará después de la Compaction.

### Detalles de boot-md

Ejecuta `BOOT.md` desde el workspace activo cuando se inicia el Gateway.

## Hooks de Plugin

Los plugins pueden registrar hooks tipados mediante el Plugin SDK para una integración más profunda: interceptar llamadas de herramientas, modificar prompts, controlar el flujo de mensajes y más. Usa hooks de Plugin cuando necesites `before_tool_call`, `before_agent_reply`, `before_install` u otros hooks de ciclo de vida en proceso.

Para la referencia completa de hooks de Plugin, consulta [Hooks de Plugin](</es/plugins/hooks>).

## Configuración

jsonCopy code
[code]
    {  "hooks": {    "internal": {      "enabled": true,      "entries": {        "session-memory": { "enabled": true },        "command-logger": { "enabled": false }      }    }  }}
[/code]

Variables de entorno por hook:

jsonCopy code
[code]
    {  "hooks": {    "internal": {      "entries": {        "my-hook": {          "enabled": true,          "env": { "MY_CUSTOM_VAR": "value" }        }      }    }  }}
[/code]

Directorios adicionales de hooks:

jsonCopy code
[code]
    {  "hooks": {    "internal": {      "load": {        "extraDirs": ["/path/to/more/hooks"]      }    }  }}
[/code]

## Referencia de CLI

bashCopy code
[code]
    # List all hooks (add --eligible, --verbose, or --json)openclaw hooks list # Show detailed info about a hookopenclaw hooks info <hook-name> # Show eligibility summaryopenclaw hooks check # Enable/disableopenclaw hooks enable <hook-name>openclaw hooks disable <hook-name>
[/code]

## Mejores prácticas

  * **Mantén los handlers rápidos.** Los hooks se ejecutan durante el procesamiento de comandos. Lanza el trabajo pesado en segundo plano con `void processInBackground(event)`.
  * **Gestiona los errores con elegancia.** Envuelve las operaciones riesgosas en try/catch; no lances errores para que otros handlers puedan ejecutarse.
  * **Filtra los eventos pronto.** Devuelve inmediatamente si el tipo/acción del evento no es relevante.
  * **Usa claves de evento específicas.** Prefiere `"events": ["command:new"]` en lugar de `"events": ["command"]` para reducir la sobrecarga.


## Solución de problemas

### Hook no descubierto

bashCopy code
[code]
    # Verify directory structurels -la ~/.openclaw/hooks/my-hook/# Should show: HOOK.md, handler.ts # List all discovered hooksopenclaw hooks list
[/code]

### Hook no elegible

bashCopy code
[code]
    openclaw hooks info my-hook
[/code]

Comprueba si faltan binarios (PATH), variables de entorno, valores de configuración o compatibilidad con el sistema operativo.

### Hook no se ejecuta

  1. Verifica que el hook esté habilitado: `openclaw hooks list`
  2. Reinicia tu proceso de gateway para que los hooks se recarguen.
  3. Revisa los registros del gateway: `./scripts/clawlog.sh | grep hook`


## Relacionado

  * [Referencia de CLI: hooks](</es/cli/hooks>)
  * [Webhooks](</es/automation/cron-jobs#webhooks>)
  * [Hooks de Plugin](</es/plugins/hooks>) — hooks de ciclo de vida de Plugin en proceso
  * [Configuración](</es/gateway/configuration-reference#hooks>)


Was this useful?YesNo