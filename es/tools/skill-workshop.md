---
title: Taller de Skills
source_url: https://docs.openclaw.ai/es/tools/skill-workshop
scraped_at: 2026-06-29
---

CapabilitiesSkills

Taller de habilidades es la ruta gobernada de OpenClaw para crear y actualizar habilidades del espacio de trabajo.

Los agentes y operadores no escriben archivos `SKILL.md` activos directamente mediante esta ruta. Primero crean una **propuesta**. Una propuesta es un borrador pendiente que contiene el contenido de habilidad propuesto, la vinculación de destino, el estado del escáner, hashes, metadatos de archivos de soporte y metadatos de reversión. Se convierte en una habilidad activa solo cuando se aplica.

Taller de habilidades solo escribe habilidades del espacio de trabajo. No modifica habilidades incluidas, de plugin, ClawHub, raíz adicional, administradas, de agente personal ni del sistema.

## Cómo funciona

  * **Primero la propuesta:** el contenido de habilidad generado se almacena como `PROPOSAL.md`, no como `SKILL.md`.
  * **Aplicar es la única escritura activa:** crear, actualizar y revisar no cambian habilidades activas.
  * **Con alcance de espacio de trabajo:** las creaciones tienen como destino la raíz `skills/` del espacio de trabajo. Las actualizaciones solo se permiten para habilidades del espacio de trabajo editables.
  * **Sin sobrescritura:** la creación falla si la habilidad de destino ya existe.
  * **Vinculada por hash:** las propuestas de actualización se vinculan al hash actual del destino y quedan obsoletas si la habilidad activa cambia antes de aplicar.
  * **Controlada por escáner:** aplicar vuelve a ejecutar el escaneo antes de escribir.
  * **Recuperable:** aplicar escribe metadatos de reversión antes de cambiar archivos activos.
  * **Superficies coherentes:** chat, CLI y Gateway llaman todos al mismo servicio de Taller de habilidades.


## Ciclo de vida

textCopy code
[code]
    create/update -> pendingrevise        -> pendingapply         -> appliedreject        -> rejectedquarantine    -> quarantinedtarget change -> stale
[/code]

Solo las propuestas `pending` pueden revisarse, aplicarse, rechazarse o ponerse en cuarentena.

## Chat

Pide al agente la habilidad que quieres. El agente llama a `skill_workshop` y devuelve un id de propuesta.

Crear:

textCopy code
[code]
    Make a skill called morning-catchup that runs my Monday inbox routine.
[/code]

Actualizar una habilidad existente del espacio de trabajo:

textCopy code
[code]
    Update trip-planning to also check seat maps before booking.
[/code]

Iterar sobre una propuesta pendiente:

textCopy code
[code]
    Show me the morning-catchup proposal.Revise it to also flag anything marked urgent.Apply the morning-catchup proposal.
[/code]

De forma predeterminada, `apply`, `reject` y `quarantine` iniciados por el agente muestran una solicitud de aprobación antes de ejecutarse. Establece `skills.workshop.approvalPolicy` en `"auto"` para omitir la solicitud en entornos de confianza.

## CLI

Crear una nueva propuesta de habilidad:

bashCopy code
[code]
    openclaw skills workshop propose-create \  --name morning-catchup \  --description "Daily inbox catch-up: triage, archive, surface, draft, plan" \  --proposal ./PROPOSAL.md
[/code]

Crear una propuesta de actualización para una habilidad existente del espacio de trabajo:

bashCopy code
[code]
    openclaw skills workshop propose-update trip-planning --proposal ./PROPOSAL.md
[/code]

Listar e inspeccionar:

bashCopy code
[code]
    openclaw skills workshop listopenclaw skills workshop inspect <proposal-id>
[/code]

Revisar antes de la aprobación:

bashCopy code
[code]
    openclaw skills workshop revise <proposal-id> --proposal ./PROPOSAL.md
[/code]

Cerrar la propuesta:

bashCopy code
[code]
    openclaw skills workshop apply <proposal-id>openclaw skills workshop reject <proposal-id> --reason "Duplicate"openclaw skills workshop quarantine <proposal-id> --reason "Needs security review"
[/code]

## Contenido de la propuesta

Mientras está pendiente, la propuesta se almacena como `PROPOSAL.md` con frontmatter exclusivo de propuesta:

markdownCopy code
[code]
    ---name: "morning-catchup"description: "Daily inbox catch-up: triage, archive, surface, draft, plan"status: proposalversion: "v1"date: "2026-05-30T00:00:00.000Z"---
[/code]

Al aplicar, el Taller de Skills escribe el `SKILL.md` activo y elimina los campos exclusivos de la propuesta: `status`, `version` de propuesta y `date` de propuesta.

## Archivos auxiliares

Usa `--proposal-dir` cuando la skill propuesta necesite archivos junto a `PROPOSAL.md`:

bashCopy code
[code]
    openclaw skills workshop propose-create \  --name weekly-update \  --description "Friday wrap-up: stats, highlights, next week's top three" \  --proposal-dir ./weekly-update-proposal
[/code]

El directorio debe contener `PROPOSAL.md`. Los archivos auxiliares deben estar en:

  * `assets/`
  * `examples/`
  * `references/`
  * `scripts/`
  * `templates/`


El Taller de Skills escanea, genera hashes y almacena los archivos auxiliares con la propuesta. Se escriben junto al `SKILL.md` activo solo al aplicar.

Las rutas de archivos auxiliares rechazadas incluyen rutas absolutas, segmentos ocultos de ruta, recorrido de rutas, rutas superpuestas, archivos ejecutables de directorios de propuesta, texto que no sea UTF-8, bytes nulos y archivos fuera de las carpetas auxiliares estándar.

## Herramienta de agente

El modelo usa `skill_workshop`:

textCopy code
[code]
    action: create | update | revise | list | inspect | apply | reject | quarantine
[/code]

Los agentes deben usar `skill_workshop` para el trabajo de Skills generadas. No deben crear ni cambiar archivos de propuesta mediante `write`, `edit`, `exec`, comandos de shell ni operaciones directas del sistema de archivos.

## Aprobación y autonomía

json5Copy code
[code]
    {  skills: {    workshop: {      autonomous: {        enabled: false,      },      allowSymlinkTargetWrites: false,      approvalPolicy: "pending",      maxPending: 50,      maxSkillBytes: 40000,    },  },}
[/code]

  * `autonomous.enabled`: permite que OpenClaw cree propuestas pendientes a partir de señales duraderas de conversación después de turnos correctos. Valor predeterminado: `false`.
  * `allowSymlinkTargetWrites`: permite que apply escriba a través de enlaces simbólicos de Skills del workspace cuyo destino real esté listado en `skills.load.allowSymlinkTargets`. Valor predeterminado: `false`.
  * `approvalPolicy: "pending"`: requiere una solicitud de aprobación antes de `apply`, `reject` o `quarantine` iniciados por el agente.
  * `approvalPolicy: "auto"`: omite esa solicitud de aprobación. El agente aún debe llamar a la acción.
  * `maxPending`: limita las propuestas pendientes y en cuarentena por workspace.
  * `maxSkillBytes`: limita el tamaño del cuerpo de la propuesta. Valor predeterminado: `40000`.


Las descripciones de propuestas siempre tienen un límite de 160 bytes.

## Métodos de Gateway

textCopy code
[code]
    skills.proposals.listskills.proposals.inspectskills.proposals.createskills.proposals.updateskills.proposals.reviseskills.proposals.applyskills.proposals.rejectskills.proposals.quarantine
[/code]

Los métodos de solo lectura requieren `operator.read`. Los métodos que modifican requieren `operator.admin`.

## Almacenamiento

textCopy code
[code]
    &lt;OPENCLAW_STATE_DIR&gt;/skill-workshop/  proposals.json  proposals/<proposal-id>/    proposal.json    PROPOSAL.md    rollback.json    assets/    examples/    references/    scripts/    templates/
[/code]

Directorio de estado predeterminado: `~/.openclaw`.

  * `proposal.json`: registro canónico de la propuesta.
  * `proposals.json`: índice de listado rápido, reconstruible desde las carpetas de propuestas.
  * `PROPOSAL.md`: propuesta de skill pendiente.
  * `rollback.json`: metadatos de recuperación escritos antes de aplicar cambios a archivos activos.


## Límites

  * Descripción: 160 bytes.
  * Cuerpo de la propuesta: `skills.workshop.maxSkillBytes` (valor predeterminado 40,000).
  * Archivos auxiliares: 64 por propuesta.
  * Tamaño de archivo auxiliar: 256 KB cada uno, 2 MB en total.
  * Propuestas pendientes y en cuarentena: `skills.workshop.maxPending` por workspace (valor predeterminado 50).


## Solución de problemas

Problema | Resolución  
---|---  
`Skill proposal description is too large` | Acorta `description` a 160 bytes o menos.  
`Skill proposal content is too large` | Acorta el cuerpo de la propuesta o aumenta `skills.workshop.maxSkillBytes`.  
`Target skill changed after proposal creation` | Revisa la propuesta contra el destino actual, o crea una propuesta nueva.  
`Proposal scan failed` | Inspecciona los hallazgos del escáner y luego revisa o pon en cuarentena la propuesta.  
`untrusted symlink target` | Configura `skills.load.allowSymlinkTargets` y habilita `skills.workshop.allowSymlinkTargetWrites` solo para raíces de Skills compartidas intencionales.  
`Support file paths must be under one of...` | Mueve los archivos auxiliares a `assets/`, `examples/`, `references/`, `scripts/` o `templates/`.  
La propuesta no aparece en la lista | Comprueba el workspace `--agent` seleccionado y `OPENCLAW_STATE_DIR`.  
El agente no puede llamar a `skill_workshop` | Comprueba la política de herramientas activa y el modo de ejecución. `coding` incluye la herramienta; las políticas restrictivas de `tools.allow` deben listarla explícitamente, y las ejecuciones en sandbox deben usar una sesión normal de agente del lado del host o la CLI.  
  
## Relacionado

  * [Skills](</es/tools/skills>) para el orden de carga, la precedencia y la visibilidad
  * [Crear Skills](</es/tools/creating-skills>) para los conceptos básicos de `SKILL.md` escritos a mano
  * [Configuración de Skills](</es/tools/skills-config>) para el esquema completo de `skills.workshop`
  * [CLI de Skills](</es/cli/skills>) para comandos `openclaw skills`


Was this useful?YesNo

Open issue