---
title: Skills (macOS)
source_url: https://docs.openclaw.ai/es/platforms/mac/skills
scraped_at: 2026-05-25
---

La app de macOS muestra las Skills de OpenClaw a través del gateway; no analiza las Skills localmente.

## Fuente de datos

  * `skills.status` (gateway) devuelve todas las Skills más su elegibilidad y los requisitos faltantes (incluidos los bloqueos por lista de permitidos para Skills incluidas).
  * Los requisitos se derivan de `metadata.openclaw.requires` en cada `SKILL.md`.


## Acciones de instalación

  * `metadata.openclaw.install` define opciones de instalación (brew/node/go/uv).
  * La app llama a `skills.install` para ejecutar instaladores en el host del gateway.
  * Los hallazgos `critical` integrados de código peligroso bloquean `skills.install` de forma predeterminada; los hallazgos sospechosos siguen mostrando solo advertencias. La anulación de peligro existe en la solicitud del gateway, pero el flujo predeterminado de la app sigue fallando con cierre seguro.
  * Si todas las opciones de instalación son `download`, el gateway muestra todas las opciones de descarga.
  * En caso contrario, el gateway elige un instalador preferido usando las preferencias actuales de instalación y los binarios disponibles del host: primero Homebrew cuando `skills.install.preferBrew` está habilitado y existe `brew`, luego `uv`, después el gestor de node configurado en `skills.install.nodeManager`, y luego alternativas posteriores como `go` o `download`.
  * Las etiquetas de instalación de Node reflejan el gestor de node configurado, incluido `yarn`.


## Variables de entorno/claves de API

  * La app almacena las claves en `~/.openclaw/openclaw.json` bajo `skills.entries.<skillKey>`.
  * `skills.update` aplica parches a `enabled`, `apiKey` y `env`.


## Modo remoto

  * La instalación y las actualizaciones de configuración se realizan en el host del gateway (no en el Mac local).


## Relacionado

  * [Skills](</es/tools/skills>)
  * [App de macOS](</es/platforms/macos>)


Was this useful?YesNo