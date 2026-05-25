---
title: Espacio de trabajo del agente
source_url: https://docs.openclaw.ai/es/concepts/agent-workspace
scraped_at: 2026-05-25
---

El espacio de trabajo es el hogar del agente. Es el único directorio de trabajo usado para las herramientas de archivos y para el contexto del espacio de trabajo. Mantenlo privado y trátalo como memoria.

Esto está separado de `~/.openclaw/`, que almacena configuración, credenciales y sesiones.

## Ubicación predeterminada

  * Predeterminado: `~/.openclaw/workspace`
  * Si `OPENCLAW_PROFILE` está definido y no es `"default"`, el valor predeterminado pasa a ser `~/.openclaw/workspace-<profile>`.
  * Sobrescríbelo en `~/.openclaw/openclaw.json`:

json5Copy code
[code]
    {  agents: {    defaults: {      workspace: "~/.openclaw/workspace",    },  },}
[/code]

`openclaw onboard`, `openclaw configure` u `openclaw setup` crearán el espacio de trabajo y sembrarán los archivos de arranque si faltan.

Si ya gestionas tú mismo los archivos del espacio de trabajo, puedes deshabilitar la creación de archivos de arranque:

json5Copy code
[code]
    { agents: { defaults: { skipBootstrap: true } } }
[/code]

## Carpetas adicionales del espacio de trabajo

Las instalaciones antiguas pueden haber creado `~/openclaw`. Mantener varios directorios de espacio de trabajo puede causar deriva confusa de autenticación o estado, porque solo un espacio de trabajo está activo a la vez.

## Mapa de archivos del espacio de trabajo

Estos son los archivos estándar que OpenClaw espera dentro del espacio de trabajo:

AGENTS.md - instrucciones operativas

Instrucciones operativas para el agente y cómo debe usar la memoria. Se cargan al inicio de cada sesión. Buen lugar para reglas, prioridades y detalles de "cómo comportarse".

SOUL.md - personalidad y tono

Personalidad, tono y límites. Se carga en cada sesión. Guía: [guía de personalidad de SOUL.md](</es/concepts/soul>).

USER.md - quién es el usuario

Quién es el usuario y cómo dirigirse a él. Se carga en cada sesión.

IDENTITY.md - nombre, estilo, emoji

El nombre, el estilo y el emoji del agente. Se crea/actualiza durante el ritual de arranque.

TOOLS.md - convenciones de herramientas locales

Notas sobre tus herramientas locales y convenciones. No controla la disponibilidad de herramientas; es solo orientación.

HEARTBEAT.md - lista de comprobación de heartbeat

Lista de comprobación diminuta opcional para ejecuciones de heartbeat. Mantenla corta para evitar consumo de tokens.

BOOT.md - lista de comprobación de inicio

Lista de comprobación de inicio opcional que se ejecuta automáticamente al reiniciar el Gateway (cuando los [hooks internos](</es/automation/hooks>) están habilitados). Mantenla corta; usa la herramienta de mensajes para envíos salientes.

BOOTSTRAP.md - ritual de primera ejecución

Ritual único de primera ejecución. Solo se crea para un espacio de trabajo totalmente nuevo. Elimínalo después de completar el ritual.

memory/YYYY-MM-DD.md - registro diario de memoria

Registro diario de memoria (un archivo por día). Se recomienda leer hoy + ayer al iniciar la sesión.

MEMORY.md - memoria a largo plazo curada (opcional)

Memoria a largo plazo curada: hechos duraderos, preferencias, decisiones y resúmenes breves. Mantén los registros detallados en `memory/YYYY-MM-DD.md` para que las herramientas de memoria puedan recuperarlos bajo demanda sin inyectarlos en cada prompt. Carga `MEMORY.md` solo en la sesión principal y privada (no en contextos compartidos/grupales). Consulta [Memoria](</es/concepts/memory>) para ver el flujo de trabajo y el vaciado automático de memoria.

skills/ - skills del espacio de trabajo (opcional)

Skills específicas del espacio de trabajo. Ubicación de Skills de mayor precedencia para ese espacio de trabajo. Sobrescribe las Skills de agente de proyecto, Skills de agente personales, Skills gestionadas, Skills incluidas y `skills.load.extraDirs` cuando los nombres colisionan.

canvas/ - archivos de Canvas UI (opcional)

Archivos de Canvas UI para visualizaciones de nodos (por ejemplo, `canvas/index.html`).

## Qué NO está en el espacio de trabajo

Estos viven bajo `~/.openclaw/` y NO deben confirmarse en el repo del espacio de trabajo:

  * `~/.openclaw/openclaw.json` (configuración)
  * `~/.openclaw/agents/<agentId>/agent/auth-profiles.json` (perfiles de autenticación de modelos: OAuth + claves de API)
  * `~/.openclaw/agents/<agentId>/agent/codex-home/` (cuenta de runtime de Codex por agente, configuración, Skills, plugins y estado nativo de hilos)
  * `~/.openclaw/credentials/` (estado de canal/proveedor más datos de importación OAuth heredados)
  * `~/.openclaw/agents/<agentId>/sessions/` (transcripciones de sesiones + metadatos)
  * `~/.openclaw/skills/` (Skills gestionadas)


Si necesitas migrar sesiones o configuración, cópialas por separado y mantenlas fuera del control de versiones.

## Copia de seguridad con git (recomendada, privada)

Trata el espacio de trabajo como memoria privada. Colócalo en un repo git **privado** para que tenga copia de seguridad y sea recuperable.

Ejecuta estos pasos en la máquina donde se ejecuta el Gateway (ahí es donde vive el espacio de trabajo).

* ### Inicializar el repo

Si git está instalado, los espacios de trabajo totalmente nuevos se inicializan automáticamente. Si este espacio de trabajo aún no es un repo, ejecuta:

bashCopy code
[code]
    cd ~/.openclaw/workspacegit initgit add AGENTS.md SOUL.md TOOLS.md IDENTITY.md USER.md HEARTBEAT.md memory/git commit -m "Add agent workspace"
[/code]

* ### Añadir un remoto privado

### Interfaz web de GitHub

  1. Crea un nuevo repositorio **privado** en GitHub.
  2. No lo inicialices con un README (evita conflictos de merge).
  3. Copia la URL remota HTTPS.
  4. Añade el remoto y haz push:

bashCopy code
[code]
    git branch -M maingit remote add origin <https-url>git push -u origin main
[/code]

### GitHub CLI (gh)

bashCopy code
[code]
    gh auth logingh repo create openclaw-workspace --private --source . --remote origin --push
[/code]

### Interfaz web de GitLab

  1. Crea un nuevo repositorio **privado** en GitLab.
  2. No lo inicialices con un README (evita conflictos de merge).
  3. Copia la URL remota HTTPS.
  4. Añade el remoto y haz push:

bashCopy code
[code]
    git branch -M maingit remote add origin <https-url>git push -u origin main
[/code]

* ### Actualizaciones continuas

bashCopy code
[code]
    git statusgit add .git commit -m "Update memory"git push
[/code]

## No confirmes secretos

Plantilla inicial sugerida de `.gitignore`:

gitignoreCopy code
[code]
    .DS_Store.env**/*.key**/*.pem**/secrets*
[/code]

## Mover el espacio de trabajo a una máquina nueva

* ### Clonar el repo

Clona el repo en la ruta deseada (predeterminada `~/.openclaw/workspace`).

* ### Actualizar la configuración

Establece `agents.defaults.workspace` en esa ruta en `~/.openclaw/openclaw.json`.

* ### Sembrar archivos faltantes

Ejecuta `openclaw setup --workspace <path>` para sembrar cualquier archivo faltante.

* ### Copiar sesiones (opcional)

Si necesitas sesiones, copia `~/.openclaw/agents/<agentId>/sessions/` desde la máquina antigua por separado.

## Notas avanzadas

  * El enrutamiento multiagente puede usar espacios de trabajo diferentes por agente. Consulta [enrutamiento de canales](</es/channels/channel-routing>) para la configuración de enrutamiento.
  * Si `agents.defaults.sandbox` está habilitado, las sesiones no principales pueden usar espacios de trabajo de sandbox por sesión bajo `agents.defaults.sandbox.workspaceRoot`.


## Relacionado

  * [Heartbeat](</es/gateway/heartbeat>) \- archivo de espacio de trabajo [HEARTBEAT.md](<http://HEARTBEAT.md>)
  * [Sandboxing](</es/gateway/sandboxing>) \- acceso al espacio de trabajo en entornos con sandboxing
  * [Sesión](</es/concepts/session>) \- rutas de almacenamiento de sesiones
  * [Órdenes permanentes](</es/automation/standing-orders>) \- instrucciones persistentes en archivos del espacio de trabajo


Was this useful?YesNo