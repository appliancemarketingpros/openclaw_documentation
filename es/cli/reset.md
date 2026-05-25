---
title: Restablecer
source_url: https://docs.openclaw.ai/es/cli/reset
scraped_at: 2026-05-25
---

# `openclaw reset`

Restablece la configuración/estado local (mantiene la CLI instalada).

Opciones:

  * `--scope <scope>`: `config`, `config+creds+sessions` o `full`
  * `--yes`: omite las solicitudes de confirmación
  * `--non-interactive`: desactiva las solicitudes; requiere `--scope` y `--yes`
  * `--dry-run`: muestra las acciones sin eliminar archivos


Ejemplos:

bashCopy code
[code]
    openclaw backup createopenclaw resetopenclaw reset --dry-runopenclaw reset --scope config --yes --non-interactiveopenclaw reset --scope config+creds+sessions --yes --non-interactiveopenclaw reset --scope full --yes --non-interactive
[/code]

Notas:

  * Ejecuta primero `openclaw backup create` si quieres una instantánea restaurable antes de eliminar el estado local.
  * Si omites `--scope`, `openclaw reset` usa una solicitud interactiva para elegir qué eliminar.
  * `--non-interactive` solo es válido cuando están establecidos tanto `--scope` como `--yes`.


## Relacionado

  * [Referencia de la CLI](</es/cli>)


Was this useful?YesNo