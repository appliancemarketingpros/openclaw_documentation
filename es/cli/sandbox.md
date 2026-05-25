---
title: CLI del entorno aislado
source_url: https://docs.openclaw.ai/es/cli/sandbox
scraped_at: 2026-05-25
---

Administra runtimes sandbox para la ejecución aislada de agentes.

## Resumen

OpenClaw puede ejecutar agentes en runtimes sandbox aislados por seguridad. Los comandos `sandbox` te ayudan a inspeccionar y recrear esos runtimes después de actualizaciones o cambios de configuración.

Hoy eso normalmente significa:

  * Contenedores sandbox de Docker
  * Runtimes sandbox SSH cuando `agents.defaults.sandbox.backend = "ssh"`
  * Runtimes sandbox de OpenShell cuando `agents.defaults.sandbox.backend = "openshell"`


Para `ssh` y OpenShell `remote`, recrear importa más que con Docker:

  * el espacio de trabajo remoto es canónico después de la inicialización inicial
  * `openclaw sandbox recreate` elimina ese espacio de trabajo remoto canónico para el ámbito seleccionado
  * el siguiente uso lo inicializa de nuevo desde el espacio de trabajo local actual


## Comandos

### `openclaw sandbox explain`

Inspecciona el modo/ámbito/acceso al espacio de trabajo sandbox **efectivo** , la política de herramientas sandbox y las puertas de elevación (con rutas de claves de configuración para corregirlo).

bashCopy code
[code]
    openclaw sandbox explainopenclaw sandbox explain --session agent:main:mainopenclaw sandbox explain --agent workopenclaw sandbox explain --json
[/code]

### `openclaw sandbox list`

Lista todos los runtimes sandbox con su estado y configuración.

bashCopy code
[code]
    openclaw sandbox listopenclaw sandbox list --browser  # List only browser containersopenclaw sandbox list --json     # JSON output
[/code]

**La salida incluye:**

  * Nombre y estado del runtime
  * Backend (`docker`, `openshell`, etc.)
  * Etiqueta de configuración y si coincide con la configuración actual
  * Antigüedad (tiempo desde la creación)
  * Tiempo inactivo (tiempo desde el último uso)
  * Sesión/agente asociado


### `openclaw sandbox recreate`

Elimina runtimes sandbox para forzar su recreación con la configuración actualizada.

bashCopy code
[code]
    openclaw sandbox recreate --all                # Recreate all containersopenclaw sandbox recreate --session main       # Specific sessionopenclaw sandbox recreate --agent mybot        # Specific agentopenclaw sandbox recreate --browser            # Only browser containersopenclaw sandbox recreate --all --force        # Skip confirmation
[/code]

**Opciones:**

  * `--all`: Recrea todos los contenedores sandbox
  * `--session <key>`: Recrea el contenedor para una sesión específica
  * `--agent <id>`: Recrea los contenedores para un agente específico
  * `--browser`: Recrea solo los contenedores de navegador
  * `--force`: Omite la solicitud de confirmación


## Casos de uso

### Después de actualizar una imagen de Docker

bashCopy code
[code]
    # Pull new imagedocker pull openclaw-sandbox:latestdocker tag openclaw-sandbox:latest openclaw-sandbox:bookworm-slim # Update config to use new image# Edit config: agents.defaults.sandbox.docker.image (or agents.list[].sandbox.docker.image) # Recreate containersopenclaw sandbox recreate --all
[/code]

### Después de cambiar la configuración del sandbox

bashCopy code
[code]
    # Edit config: agents.defaults.sandbox.* (or agents.list[].sandbox.*) # Recreate to apply new configopenclaw sandbox recreate --all
[/code]

### Después de cambiar el destino SSH o el material de autenticación SSH

bashCopy code
[code]
    # Edit config:# - agents.defaults.sandbox.backend# - agents.defaults.sandbox.ssh.target# - agents.defaults.sandbox.ssh.workspaceRoot# - agents.defaults.sandbox.ssh.identityFile / certificateFile / knownHostsFile# - agents.defaults.sandbox.ssh.identityData / certificateData / knownHostsData openclaw sandbox recreate --all
[/code]

Para el backend `ssh` principal, recrear elimina la raíz del espacio de trabajo remoto por ámbito en el destino SSH. La siguiente ejecución la inicializa de nuevo desde el espacio de trabajo local.

### Después de cambiar la fuente, la política o el modo de OpenShell

bashCopy code
[code]
    # Edit config:# - agents.defaults.sandbox.backend# - plugins.entries.openshell.config.from# - plugins.entries.openshell.config.mode# - plugins.entries.openshell.config.policy openclaw sandbox recreate --all
[/code]

Para el modo OpenShell `remote`, recrear elimina el espacio de trabajo remoto canónico para ese ámbito. La siguiente ejecución lo inicializa de nuevo desde el espacio de trabajo local.

### Después de cambiar setupCommand

bashCopy code
[code]
    openclaw sandbox recreate --all# or just one agent:openclaw sandbox recreate --agent family
[/code]

### Solo para un agente específico

bashCopy code
[code]
    # Update only one agent's containersopenclaw sandbox recreate --agent alfred
[/code]

## Por qué esto es necesario

Cuando actualizas la configuración del sandbox:

  * Los runtimes existentes siguen ejecutándose con la configuración anterior.
  * Los runtimes solo se eliminan después de 24 h de inactividad.
  * Los agentes usados regularmente mantienen vivos los runtimes antiguos indefinidamente.


Usa `openclaw sandbox recreate` para forzar la eliminación de runtimes antiguos. Se recrean automáticamente con la configuración actual cuando vuelven a necesitarse.

## Migración del registro

OpenClaw almacena los metadatos de runtime sandbox como un fragmento JSON por entrada de contenedor/navegador bajo el directorio de estado del sandbox. Las instalaciones antiguas aún pueden tener archivos heredados monolíticos:

  * `~/.openclaw/sandbox/containers.json`
  * `~/.openclaw/sandbox/browsers.json`


Las lecturas normales de runtime sandbox no reescriben esos archivos. Ejecuta `openclaw doctor --fix` para migrar las entradas heredadas válidas a los directorios del registro fragmentado. Los archivos heredados no válidos se ponen en cuarentena para que un registro antiguo defectuoso no pueda ocultar entradas de runtime actuales.

## Configuración

La configuración del sandbox vive en `~/.openclaw/openclaw.json` bajo `agents.defaults.sandbox` (las sobrescrituras por agente van en `agents.list[].sandbox`):

jsoncCopy code
[code]
    {  "agents": {    "defaults": {      "sandbox": {        "mode": "all", // off, non-main, all        "backend": "docker", // docker, ssh, openshell        "scope": "agent", // session, agent, shared        "docker": {          "image": "openclaw-sandbox:bookworm-slim",          "containerPrefix": "openclaw-sbx-",          // ... more Docker options        },        "prune": {          "idleHours": 24, // Auto-prune after 24h idle          "maxAgeDays": 7, // Auto-prune after 7 days        },      },    },  },}
[/code]

## Relacionado

  * [Referencia de CLI](</es/cli>)
  * [Aislamiento en sandbox](</es/gateway/sandboxing>)
  * [Espacio de trabajo del agente](</es/concepts/agent-workspace>)
  * [Doctor](</es/gateway/doctor>): comprueba la configuración del sandbox.


Was this useful?YesNo