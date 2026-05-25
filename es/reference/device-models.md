---
title: Base de datos de modelos de dispositivos
source_url: https://docs.openclaw.ai/es/reference/device-models
scraped_at: 2026-05-25
---

La app complementaria de macOS muestra nombres legibles de modelos de dispositivos Apple en la interfaz de **Instances** al mapear identificadores de modelo de Apple (por ejemplo, `iPad16,6`, `Mac16,6`) a nombres legibles para las personas.

La asignación se incorpora como JSON en:

  * `apps/macos/Sources/OpenClaw/Resources/DeviceModels/`


## Fuente de datos

Actualmente incorporamos la asignación desde el repositorio con licencia MIT:

  * `kyle-seongwoo-jun/apple-device-identifiers`


Para mantener compilaciones deterministas, los archivos JSON están fijados a commits específicos de upstream (registrados en `apps/macos/Sources/OpenClaw/Resources/DeviceModels/NOTICE.md`).

## Actualizar la base de datos

  1. Elige los commits de upstream que quieras fijar (uno para iOS y otro para macOS).
  2. Actualiza los hashes de commit en `apps/macos/Sources/OpenClaw/Resources/DeviceModels/NOTICE.md`.
  3. Vuelve a descargar los archivos JSON, fijados a esos commits:

bashCopy code
[code]
    IOS_COMMIT="<commit sha for ios-device-identifiers.json>"MAC_COMMIT="<commit sha for mac-device-identifiers.json>" curl -fsSL "https://raw.githubusercontent.com/kyle-seongwoo-jun/apple-device-identifiers/${IOS_COMMIT}/ios-device-identifiers.json" \  -o apps/macos/Sources/OpenClaw/Resources/DeviceModels/ios-device-identifiers.json curl -fsSL "https://raw.githubusercontent.com/kyle-seongwoo-jun/apple-device-identifiers/${MAC_COMMIT}/mac-device-identifiers.json" \  -o apps/macos/Sources/OpenClaw/Resources/DeviceModels/mac-device-identifiers.json
[/code]

  4. Asegúrate de que `apps/macos/Sources/OpenClaw/Resources/DeviceModels/LICENSE.apple-device-identifiers.txt` siga coincidiendo con upstream (reemplázalo si cambia la licencia de upstream).
  5. Verifica que la app de macOS compile correctamente (sin advertencias):

bashCopy code
[code]
    swift build --package-path apps/macos
[/code]

## Relacionado

  * [Nodes](</es/nodes>)
  * [Solución de problemas de Node](</es/nodes/troubleshooting>)


Was this useful?YesNo