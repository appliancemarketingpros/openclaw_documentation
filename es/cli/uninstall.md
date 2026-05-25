---
title: Desinstalar
source_url: https://docs.openclaw.ai/es/cli/uninstall
scraped_at: 2026-05-25
---

# `openclaw uninstall`

Desinstala el servicio de Gateway y los datos locales (la CLI permanece).

Opciones:

  * `--service`: elimina el servicio de Gateway
  * `--state`: elimina el estado y la configuración
  * `--workspace`: elimina los directorios de espacios de trabajo
  * `--app`: elimina la aplicación de macOS
  * `--all`: elimina el servicio, el estado, el espacio de trabajo y la aplicación
  * `--yes`: omite las solicitudes de confirmación
  * `--non-interactive`: desactiva las solicitudes; requiere `--yes`
  * `--dry-run`: imprime las acciones sin eliminar archivos


Ejemplos:

bashCopy code
[code]
    openclaw backup createopenclaw uninstallopenclaw uninstall --service --yes --non-interactiveopenclaw uninstall --state --workspace --yes --non-interactiveopenclaw uninstall --all --yesopenclaw uninstall --dry-run
[/code]

Notas:

  * Ejecuta primero `openclaw backup create` si quieres una instantánea restaurable antes de eliminar el estado o los espacios de trabajo.
  * `--all` es una abreviatura para eliminar conjuntamente el servicio, el estado, el espacio de trabajo y la aplicación.
  * `--non-interactive` requiere `--yes`.


## Relacionado

  * [Referencia de la CLI](</es/cli>)
  * [Desinstalar](</es/install/uninstall>)


Was this useful?YesNo