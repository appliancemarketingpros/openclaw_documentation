---
title: Ganchos
source_url: https://docs.openclaw.ai/es/cli/hooks
scraped_at: 2026-05-25
---

# `openclaw hooks`

Gestiona los hooks de agentes (automatizaciones basadas en eventos para comandos como `/new`, `/reset` y el inicio del Gateway).

Ejecutar `openclaw hooks` sin subcomando equivale a `openclaw hooks list`.

Relacionado:

  * Hooks: [Hooks](</es/automation/hooks>)
  * Hooks de Plugin: [Hooks de Plugin](</es/plugins/hooks>)


## Listar todos los hooks

bashCopy code
[code]
    openclaw hooks list
[/code]

Enumera todos los hooks descubiertos desde directorios del espacio de trabajo, administrados, extra y empaquetados. El inicio del Gateway no carga controladores de hooks internos hasta que se configure al menos un hook interno.

**Opciones:**

  * `--eligible`: Muestra solo hooks elegibles (requisitos cumplidos)
  * `--json`: Genera la salida como JSON
  * `-v, --verbose`: Muestra información detallada, incluidos los requisitos faltantes


**Salida de ejemplo:**

CodeCopy code
[code]
    Hooks (4/4 ready) Ready:  🚀 boot-md ✓ - Run BOOT.md on gateway startup  📎 bootstrap-extra-files ✓ - Inject extra workspace bootstrap files during agent bootstrap  📝 command-logger ✓ - Log all command events to a centralized audit file  💾 session-memory ✓ - Save session context to memory when /new or /reset command is issued
[/code]

**Ejemplo (detallado):**

bashCopy code
[code]
    openclaw hooks list --verbose
[/code]

Muestra los requisitos faltantes para hooks no elegibles.

**Ejemplo (JSON):**

bashCopy code
[code]
    openclaw hooks list --json
[/code]

Devuelve JSON estructurado para uso programático.

## Obtener información de un hook

bashCopy code
[code]
    openclaw hooks info <name>
[/code]

Muestra información detallada sobre un hook específico.

**Argumentos:**

  * `<name>`: Nombre del hook o clave del hook (por ejemplo, `session-memory`)


**Opciones:**

  * `--json`: Genera la salida como JSON


**Ejemplo:**

bashCopy code
[code]
    openclaw hooks info session-memory
[/code]

**Salida:**

CodeCopy code
[code]
    💾 session-memory ✓ Ready Save session context to memory when /new or /reset command is issued Details:  Source: openclaw-bundled  Path: /path/to/openclaw/hooks/bundled/session-memory/HOOK.md  Handler: /path/to/openclaw/hooks/bundled/session-memory/handler.ts  Homepage: https://docs.openclaw.ai/automation/hooks#session-memory  Events: command:new, command:reset Requirements:  Config: ✓ workspace.dir
[/code]

## Comprobar la elegibilidad de los hooks

bashCopy code
[code]
    openclaw hooks check
[/code]

Muestra un resumen del estado de elegibilidad de los hooks (cuántos están listos frente a no listos).

**Opciones:**

  * `--json`: Genera la salida como JSON


**Salida de ejemplo:**

CodeCopy code
[code]
    Hooks Status Total hooks: 4Ready: 4Not ready: 0
[/code]

## Habilitar un hook

bashCopy code
[code]
    openclaw hooks enable <name>
[/code]

Habilita un hook específico agregándolo a tu configuración (`~/.openclaw/openclaw.json` de forma predeterminada).

**Nota:** Los hooks del espacio de trabajo están deshabilitados de forma predeterminada hasta que se habiliten aquí o en la configuración. Los hooks administrados por plugins muestran `plugin:<id>` en `openclaw hooks list` y no pueden habilitarse ni deshabilitarse aquí. Habilita o deshabilita el plugin en su lugar.

**Argumentos:**

  * `<name>`: Nombre del hook (por ejemplo, `session-memory`)


**Ejemplo:**

bashCopy code
[code]
    openclaw hooks enable session-memory
[/code]

**Salida:**

CodeCopy code
[code]
    ✓ Enabled hook: 💾 session-memory
[/code]

**Qué hace:**

  * Comprueba si el hook existe y es elegible
  * Actualiza `hooks.internal.entries.<name>.enabled = true` en tu configuración
  * Guarda la configuración en el disco


Si el hook proviene de `<workspace>/hooks/`, este paso de inclusión voluntaria es obligatorio antes de que el Gateway lo cargue.

**Después de habilitarlo:**

  * Reinicia el gateway para que los hooks se recarguen (reinicio de la app de la barra de menús en macOS o reinicia tu proceso de gateway en desarrollo).


## Deshabilitar un hook

bashCopy code
[code]
    openclaw hooks disable <name>
[/code]

Deshabilita un hook específico actualizando tu configuración.

**Argumentos:**

  * `<name>`: Nombre del hook (por ejemplo, `command-logger`)


**Ejemplo:**

bashCopy code
[code]
    openclaw hooks disable command-logger
[/code]

**Salida:**

CodeCopy code
[code]
    ⏸ Disabled hook: 📝 command-logger
[/code]

**Después de deshabilitarlo:**

  * Reinicia el gateway para que los hooks se recarguen


## Notas

  * `openclaw hooks list --json`, `info --json` y `check --json` escriben JSON estructurado directamente en stdout.
  * Los hooks administrados por plugins no pueden habilitarse ni deshabilitarse aquí; habilita o deshabilita el plugin propietario en su lugar.


## Instalar paquetes de hooks

bashCopy code
[code]
    openclaw plugins install <package>        # npm by defaultopenclaw plugins install npm:<package>    # npm onlyopenclaw plugins install <package> --pin  # pin versionopenclaw plugins install <path>           # local path
[/code]

Instala paquetes de hooks mediante el instalador unificado de plugins.

`openclaw hooks install` sigue funcionando como alias de compatibilidad, pero imprime una advertencia de obsolescencia y reenvía a `openclaw plugins install`.

Las especificaciones de npm son **solo de registro** (nombre de paquete + **versión exacta** opcional o **dist-tag**). Las especificaciones Git/URL/archivo y los rangos semver se rechazan. Las instalaciones de dependencias se ejecutan localmente al proyecto con `--ignore-scripts` por seguridad, incluso cuando tu shell tiene configuraciones globales de instalación de npm.

Las especificaciones simples y `@latest` permanecen en la rama estable. Si npm resuelve cualquiera de ellas a una versión preliminar, OpenClaw se detiene y te pide que aceptes explícitamente con una etiqueta de versión preliminar como `@beta`/`@rc` o una versión preliminar exacta.

**Qué hace:**

  * Copia el paquete de hooks en `~/.openclaw/hooks/<id>`
  * Habilita los hooks instalados en `hooks.internal.entries.*`
  * Registra la instalación en `hooks.internal.installs`


**Opciones:**

  * `-l, --link`: Enlaza un directorio local en lugar de copiarlo (lo agrega a `hooks.internal.load.extraDirs`)
  * `--pin`: Registra las instalaciones de npm como `name@version` resuelto exacto en `hooks.internal.installs`


**Archivos compatibles:** `.zip`, `.tgz`, `.tar.gz`, `.tar`

**Ejemplos:**

bashCopy code
[code]
    # Local directoryopenclaw plugins install ./my-hook-pack # Local archiveopenclaw plugins install ./my-hook-pack.zip # NPM packageopenclaw plugins install @openclaw/my-hook-pack # Link a local directory without copyingopenclaw plugins install -l ./my-hook-pack
[/code]

Los paquetes de hooks enlazados se tratan como hooks administrados desde un directorio configurado por el operador, no como hooks del espacio de trabajo.

## Actualizar paquetes de hooks

bashCopy code
[code]
    openclaw plugins update <id>openclaw plugins update --all
[/code]

Actualiza los paquetes de hooks basados en npm con seguimiento mediante el actualizador unificado de plugins.

`openclaw hooks update` sigue funcionando como alias de compatibilidad, pero imprime una advertencia de obsolescencia y reenvía a `openclaw plugins update`.

**Opciones:**

  * `--all`: Actualiza todos los paquetes de hooks con seguimiento
  * `--dry-run`: Muestra qué cambiaría sin escribir


Cuando existe un hash de integridad almacenado y el hash del artefacto obtenido cambia, OpenClaw imprime una advertencia y solicita confirmación antes de continuar. Usa `--yes` global para omitir los avisos en CI/ejecuciones no interactivas.

## Hooks empaquetados

### session-memory

Guarda el contexto de sesión en memoria cuando emites `/new` o `/reset`.

**Habilitar:**

bashCopy code
[code]
    openclaw hooks enable session-memory
[/code]

**Salida:** `~/.openclaw/workspace/memory/YYYY-MM-DD-HHMM.md` de forma predeterminada. Define `hooks.internal.entries.session-memory.llmSlug: true` para slugs de nombres de archivo generados por el modelo.

**Ver:** [documentación de session-memory](</es/automation/hooks#session-memory>)

### bootstrap-extra-files

Inyecta archivos de arranque adicionales (por ejemplo, `AGENTS.md` / `TOOLS.md` locales al monorepo) durante `agent:bootstrap`.

**Habilitar:**

bashCopy code
[code]
    openclaw hooks enable bootstrap-extra-files
[/code]

**Ver:** [documentación de bootstrap-extra-files](</es/automation/hooks#bootstrap-extra-files>)

### command-logger

Registra todos los eventos de comandos en un archivo de auditoría centralizado.

**Habilitar:**

bashCopy code
[code]
    openclaw hooks enable command-logger
[/code]

**Salida:** `~/.openclaw/logs/commands.log`

**Ver registros:**

bashCopy code
[code]
    # Recent commandstail -n 20 ~/.openclaw/logs/commands.log # Pretty-printcat ~/.openclaw/logs/commands.log | jq . # Filter by actiongrep '"action":"new"' ~/.openclaw/logs/commands.log | jq .
[/code]

**Ver:** [documentación de command-logger](</es/automation/hooks#command-logger>)

### boot-md

Ejecuta `BOOT.md` cuando se inicia el gateway (después de que se inicien los canales).

**Eventos** : `gateway:startup`

**Habilitar** :

bashCopy code
[code]
    openclaw hooks enable boot-md
[/code]

**Ver:** [documentación de boot-md](</es/automation/hooks#boot-md>)

## Relacionado

  * [referencia de la CLI](</es/cli>)
  * [Hooks de automatización](</es/automation/hooks>)


Was this useful?YesNo