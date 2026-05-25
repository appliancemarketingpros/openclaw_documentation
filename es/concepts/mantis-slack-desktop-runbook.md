---
title: Guía operativa de Mantis Slack para escritorio
source_url: https://docs.openclaw.ai/es/concepts/mantis-slack-desktop-runbook
scraped_at: 2026-05-25
---

Mantis Slack desktop QA es el carril de interfaz real para errores de clase Slack que necesitan un escritorio Linux, rescate por VNC, Slack Web, un Gateway real de OpenClaw, capturas de pantalla, videos y un comentario de evidencia en el PR.

Úsalo cuando las pruebas unitarias o el carril live de Slack sin interfaz gráfica no puedan demostrar el error.

## Modelo de almacenamiento

Mantis usa tres capas de almacenamiento diferentes:

  * Imagen del proveedor: propiedad de Crabbox y almacenada en la cuenta del proveedor de nube. Contiene capacidades de máquina como Chrome/Chromium, ffmpeg, scrot, Node/corepack/pnpm, herramientas de compilación nativas y directorios de caché vacíos.
  * Estado de lease caliente: propiedad de la sesión actual del operador. Puede contener un perfil de navegador con sesión iniciada, `/var/cache/crabbox/pnpm` y un checkout de código fuente preparado mientras el lease esté activo.
  * Artefactos de Mantis: propiedad de la ejecución de OpenClaw. Viven bajo `.artifacts/qa-e2e/mantis/...`; luego GitHub Actions los sube y la Mantis GitHub App comenta evidencia inline en el PR.


Nunca coloques secretos, cookies del navegador, estado de inicio de sesión de Slack, checkouts de repositorio, `node_modules` ni `dist/` en una imagen prebakeada del proveedor.

## Dispatch de GitHub

Ejecuta el workflow desde `main`:

bashCopy code
[code]
    gh workflow run mantis-slack-desktop-smoke.yml \  --ref main \  -f candidate_ref=<trusted-ref-or-sha> \  -f pr_number=<pr-number> \  -f scenario_id=slack-canary \  -f crabbox_provider=aws \  -f keep_vm=false \  -f hydrate_mode=source
[/code]

Los valores permitidos de `candidate_ref` son intencionalmente limitados porque el workflow usa credenciales live: la ascendencia actual de `main`, etiquetas de release o la cabeza de un PR abierto desde `openclaw/openclaw`.

El workflow escribe:

  * artefacto subido: `mantis-slack-desktop-smoke-<run-id>-<attempt>`;
  * comentario inline en el PR desde la Mantis GitHub App;
  * `slack-desktop-smoke.png`;
  * `slack-desktop-smoke.mp4`;
  * `slack-desktop-smoke-preview.gif`;
  * `slack-desktop-smoke-change.mp4`;
  * `mantis-slack-desktop-smoke-summary.json`;
  * `mantis-slack-desktop-smoke-report.md`;
  * logs remotos como `slack-desktop-command.log`, `openclaw-gateway.log`, `chrome.log` y `ffmpeg.log`.


El comentario del PR se actualiza en el mismo lugar mediante el marcador oculto `<!-- mantis-slack-desktop-smoke -->`.

## CLI local

Prueba de código fuente en frío:

bashCopy code
[code]
    pnpm openclaw qa mantis slack-desktop-smoke \  --provider aws \  --class standard \  --gateway-setup \  --credential-source convex \  --credential-role maintainer \  --provider-mode live-frontier \  --model openai/gpt-5.4 \  --alt-model openai/gpt-5.4 \  --scenario slack-canary \  --hydrate-mode source
[/code]

Mantén la VM para rescate por VNC:

bashCopy code
[code]
    pnpm openclaw qa mantis slack-desktop-smoke \  --provider aws \  --class standard \  --gateway-setup \  --scenario slack-canary \  --keep-lease
[/code]

Abre VNC:

bashCopy code
[code]
    crabbox vnc --provider aws --id <cbx_id> --open
[/code]

Reutiliza un lease caliente:

bashCopy code
[code]
    pnpm openclaw qa mantis slack-desktop-smoke \  --provider aws \  --lease-id <cbx_id-or-slug> \  --gateway-setup \  --scenario slack-canary \  --hydrate-mode source
[/code]

Usa `--hydrate-mode prehydrated` solo cuando el workspace remoto reutilizado ya tenga `node_modules` y un `dist/` compilado. Mantis falla de forma cerrada si faltan.

## Modos de hidratación

Modo | Úsalo cuando | Comportamiento remoto | Compensación  
---|---|---|---  
`source` | Prueba normal de PR, máquinas frías, CI | Ejecuta `pnpm install --frozen-lockfile --prefer-offline` y `pnpm build` dentro de la VM | El más lento, la prueba más sólida de checkout de código fuente  
`prehydrated` | Preparaste intencionalmente un lease reutilizado | Requiere `node_modules` y `dist/` existentes; omite install/build | Rápido, pero solo válido para leases calientes controlados por el operador  
  
GitHub Actions siempre prepara el checkout candidato antes de la ejecución de la VM. Su almacén de pnpm se cachea por sistema operativo, versión de Node y lockfile. La ejecución de código fuente en la VM también usa `/var/cache/crabbox/pnpm` cuando está presente.

## Interpretación de tiempos

`mantis-slack-desktop-smoke-report.md` incluye tiempos por fase:

  * `crabbox.warmup`: arranque del proveedor de nube, disponibilidad de escritorio/navegador y SSH.
  * `crabbox.inspect`: búsqueda de metadatos del lease.
  * `credentials.prepare`: adquisición del lease de credenciales de Convex.
  * `crabbox.remote_run`: sincronización, inicio del navegador, instalación/compilación de OpenClaw o validación de hidratación, inicio del Gateway, captura de pantalla y captura de video.
  * `artifacts.copy`: rsync de vuelta desde la VM.


`crabbox.remote_run` puede marcarse como `accepted` cuando Crabbox devuelve un estado remoto distinto de cero después de que Mantis haya copiado metadatos que prueban que el Gateway de OpenClaw está activo y que la configuración se completó. Trata `accepted` como aprobado con explicación, no como un escenario fallido.

Si la ejecución es lenta:

  * predomina warmup: prebakea o promueve una mejor imagen de proveedor de Crabbox;
  * predomina remote_run en `source`: usa un lease caliente, mejora la reutilización del almacén de pnpm o mueve los prerrequisitos de máquina a la imagen del proveedor;
  * predomina remote_run en `prehydrated`: el workspace remoto en realidad no estaba listo, o la configuración del Gateway/navegador/Slack es lenta;
  * predomina la copia de artefactos: inspecciona el tamaño del video y el contenido del directorio de artefactos.


## Lista de verificación de evidencia

Un buen comentario de PR debería mostrar:

  * id de escenario y SHA candidato;
  * URL de ejecución de GitHub Actions;
  * URL del artefacto;
  * captura de pantalla inline;
  * vista previa animada inline cuando esté disponible;
  * enlaces al MP4 completo y al MP4 recortado;
  * estado aprobado/fallido;
  * resumen de tiempos en el reporte adjunto.


No confirmes capturas de pantalla ni videos en el repositorio. Mantenlos en artefactos de GitHub Actions o en el comentario del PR.

## Manejo de fallos

Si el workflow falla antes de la ejecución de la VM, inspecciona primero el job de Actions. Las causas típicas son un `candidate_ref` no confiable, secretos de entorno faltantes o fallo de instalación/compilación del candidato.

Si la ejecución de la VM falla pero las capturas de pantalla se copiaron de vuelta, inspecciona:

bashCopy code
[code]
    cat mantis-slack-desktop-smoke-report.mdcat mantis-slack-desktop-smoke-summary.jsoncat slack-desktop-command.logcat openclaw-gateway.logcat chrome.logcat ffmpeg.log
[/code]

Si la ejecución mantuvo el lease, abre VNC con el comando `crabbox vnc ...` del reporte. Detén el lease cuando termines:

bashCopy code
[code]
    crabbox stop --provider aws <cbx_id-or-slug>
[/code]

Si el inicio de sesión de Slack expiró, repáralo en VNC en un lease conservado y vuelve a ejecutar con `--lease-id`. No bakees ese perfil de navegador en una imagen de proveedor.

## Relacionado

  * [Resumen de QA](</es/concepts/qa-e2e-automation>)
  * [Canal Slack](</es/channels/slack>)
  * [Pruebas](</es/help/testing>)


Was this useful?YesNo