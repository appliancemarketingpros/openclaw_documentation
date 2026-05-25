---
title: Actualizar
source_url: https://docs.openclaw.ai/es/cli/update
scraped_at: 2026-05-25
---

# `openclaw update`

Actualiza OpenClaw de forma segura y cambia entre los canales stable/beta/dev.

Si instalaste mediante **npm/pnpm/bun** (instalación global, sin metadatos de git), las actualizaciones se realizan mediante el flujo del gestor de paquetes en [Actualización](</es/install/updating>).

## Uso

bashCopy code
[code]
    openclaw updateopenclaw update statusopenclaw update wizardopenclaw update --channel betaopenclaw update --channel devopenclaw update --tag betaopenclaw update --tag mainopenclaw update --dry-runopenclaw update --no-restartopenclaw update --yesopenclaw update --jsonopenclaw --update
[/code]

## Opciones

  * `--no-restart`: omite reiniciar el servicio Gateway después de una actualización correcta. Las actualizaciones del gestor de paquetes que sí reinician el Gateway verifican que el servicio reiniciado informe la versión actualizada esperada antes de que el comando se complete correctamente.
  * `--channel <stable|beta|dev>`: establece el canal de actualización (git + npm; se conserva en la configuración).
  * `--tag <dist-tag|version|spec>`: anula el paquete objetivo solo para esta actualización. Para instalaciones de paquetes, `main` se asigna a `github:openclaw/openclaw#main`.
  * `--dry-run`: previsualiza las acciones de actualización planificadas (flujo de canal/etiqueta/objetivo/reinicio) sin escribir la configuración, instalar, sincronizar plugins ni reiniciar.
  * `--json`: imprime JSON `UpdateRunResult` legible por máquinas, incluido `postUpdate.plugins.warnings` cuando plugins administrados dañados o que no se pueden cargar necesitan reparación después de que la actualización del núcleo se completa correctamente, detalles de reserva de plugins del canal beta cuando un plugin no tiene versión beta, y `postUpdate.plugins.integrityDrifts` cuando se detecta deriva de artefactos de plugins de npm durante la sincronización de plugins posterior a la actualización.
  * `--timeout <seconds>`: tiempo de espera por paso (el valor predeterminado es 1800s).
  * `--yes`: omite las solicitudes de confirmación (por ejemplo, la confirmación de degradación de versión).


`openclaw update` no tiene una marca `--verbose`. Usa `--dry-run` para previsualizar las acciones planificadas de canal/etiqueta/instalación/reinicio, `--json` para obtener resultados legibles por máquinas, y `openclaw update status --json` cuando solo necesitas detalles del canal y de disponibilidad. Si estás depurando registros del Gateway durante una actualización, la verbosidad de consola y el nivel de registro de archivo son independientes: `--verbose` del Gateway afecta la salida de terminal/WebSocket, mientras que los registros de archivo requieren `logging.level: "debug"` o `"trace"` en la configuración. Consulta [registro del Gateway](</es/gateway/logging>).

## `update status`

Muestra el canal de actualización activo + etiqueta/rama/SHA de git (para checkouts de código fuente), además de la disponibilidad de actualizaciones.

bashCopy code
[code]
    openclaw update statusopenclaw update status --jsonopenclaw update status --timeout 10
[/code]

Opciones:

  * `--json`: imprime JSON de estado legible por máquinas.
  * `--timeout <seconds>`: tiempo de espera para las comprobaciones (el valor predeterminado es 3s).


## `update wizard`

Flujo interactivo para elegir un canal de actualización y confirmar si se debe reiniciar el Gateway después de actualizar (el valor predeterminado es reiniciar). Si seleccionas `dev` sin un checkout de git, ofrece crear uno.

Opciones:

  * `--timeout <seconds>`: tiempo de espera para cada paso de actualización (valor predeterminado `1800`)


## Qué hace

Cuando cambias de canal explícitamente (`--channel ...`), OpenClaw también mantiene alineado el método de instalación:

  * `dev` → garantiza un checkout de git (valor predeterminado: `~/openclaw`, se puede anular con `OPENCLAW_GIT_DIR`), lo actualiza e instala la CLI global desde ese checkout.
  * `stable` → instala desde npm usando `latest`.
  * `beta` → prefiere la dist-tag `beta` de npm, pero vuelve a `latest` cuando beta falta o es anterior a la versión estable actual.


El actualizador automático del núcleo del Gateway (cuando está habilitado mediante configuración) lanza la ruta de actualización de la CLI fuera del controlador de solicitudes del Gateway en vivo. Las actualizaciones de gestor de paquetes `update.run` del plano de control fuerzan un reinicio de actualización no diferido y sin periodo de enfriamiento después del intercambio del paquete, porque el proceso antiguo del Gateway aún puede tener fragmentos en memoria que apuntan a archivos eliminados por el paquete nuevo.

Para instalaciones con gestor de paquetes, `openclaw update` resuelve la versión del paquete objetivo antes de invocar el gestor de paquetes. Las instalaciones globales de npm usan una instalación por etapas: OpenClaw instala el paquete nuevo en un prefijo npm temporal, verifica allí el inventario `dist` empaquetado y luego intercambia ese árbol de paquete limpio en el prefijo global real. Si la verificación falla, el doctor posterior a la actualización, la sincronización de plugins y el trabajo de reinicio no se ejecutan desde el árbol sospechoso. Incluso cuando la versión instalada ya coincide con el objetivo, el comando actualiza la instalación global del paquete, luego ejecuta la sincronización de plugins, una actualización de finalización de comandos del núcleo y el trabajo de reinicio. Esto mantiene los sidecars empaquetados y los registros de plugins propiedad del canal alineados con la compilación de OpenClaw instalada, mientras deja las reconstrucciones completas de finalización de comandos de plugins para ejecuciones explícitas de `openclaw completion --write-state`.

Cuando hay instalado un servicio Gateway administrado local y el reinicio está habilitado, las actualizaciones del gestor de paquetes detienen el servicio en ejecución antes de reemplazar el árbol del paquete, luego actualizan los metadatos del servicio desde la instalación actualizada, reinician el servicio y verifican que el Gateway reiniciado informe la versión esperada antes de informar éxito. En macOS, la comprobación posterior a la actualización también verifica que el LaunchAgent esté cargado/en ejecución para el perfil activo y que el puerto de loopback configurado esté en buen estado. Si el plist está instalado pero launchd no lo está supervisando, OpenClaw vuelve a arrancar el LaunchAgent automáticamente y luego vuelve a ejecutar las comprobaciones de salud/versión/preparación del canal. Un arranque nuevo carga directamente el trabajo RunAtLoad, por lo que la recuperación de actualización no ejecuta inmediatamente `kickstart -k` en el Gateway recién iniciado. Si el Gateway aún no se vuelve saludable, el comando sale con valor distinto de cero e imprime la ruta del registro de reinicio más instrucciones explícitas de reinicio, reinstalación y reversión del paquete. Con `--no-restart`, el reemplazo del paquete sigue ejecutándose, pero el servicio administrado no se detiene ni se reinicia, por lo que el Gateway en ejecución puede conservar código antiguo hasta que lo reinicies manualmente.

## Flujo de checkout de git

### Selección de canal

  * `stable`: hace checkout de la etiqueta no beta más reciente, luego compila y ejecuta doctor.
  * `beta`: prefiere la etiqueta `-beta` más reciente, pero vuelve a la etiqueta estable más reciente cuando beta falta o es anterior.
  * `dev`: hace checkout de `main`, luego obtiene cambios y hace rebase.


### Pasos de actualización

* ### Verify clean worktree

Requiere que no haya cambios sin confirmar.

* ### Switch channel

Cambia al canal seleccionado (etiqueta o rama).

* ### Fetch upstream

Solo dev.

* ### Preflight build (dev only)

Ejecuta la compilación de TypeScript en un worktree temporal. Si la punta falla, retrocede hasta 10 commits para encontrar el commit más reciente que se pueda compilar. Establece `OPENCLAW_UPDATE_PREFLIGHT_LINT=1` para ejecutar también lint durante esta comprobación previa; lint se ejecuta en modo serial restringido porque los hosts de actualización de usuarios suelen ser más pequeños que los runners de CI.

* ### Rebase

Hace rebase sobre el commit seleccionado (solo dev).

* ### Install dependencies

Usa el gestor de paquetes del repositorio. Para checkouts de pnpm, el actualizador prepara `pnpm` bajo demanda (primero mediante `corepack`, luego con una reserva temporal `npm install pnpm@11`) en lugar de ejecutar `npm run build` dentro de un workspace pnpm.

* ### Build Control UI

Compila el gateway y la Control UI.

* ### Run doctor

`openclaw doctor` se ejecuta como la comprobación final de actualización segura.

* ### Sync plugins

Sincroniza plugins con el canal activo. Dev usa plugins incluidos; stable y beta usan npm. Actualiza las instalaciones de plugins rastreadas.

En el canal de actualización beta, las instalaciones rastreadas de plugins npm y ClawHub que siguen la línea predeterminada/latest prueban primero una versión `@beta` del plugin. Si el plugin no tiene versión beta, OpenClaw vuelve a la especificación default/latest registrada e informa eso como una advertencia. Para plugins npm, OpenClaw también recurre a la reserva cuando el paquete beta existe pero falla la validación de instalación. Estas advertencias de reserva de plugins no hacen que la actualización del núcleo falle. Las versiones exactas y las etiquetas explícitas no se reescriben.

## Atajo `--update`

`openclaw --update` se reescribe como `openclaw update` (útil para shells y scripts de lanzadores).

## Relacionado

  * `openclaw doctor` (ofrece ejecutar update primero en checkouts de git)
  * [Canales de desarrollo](</es/install/development-channels>)
  * [Actualización](</es/install/updating>)
  * [Referencia de la CLI](</es/cli>)


Was this useful?YesNo