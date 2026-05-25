---
title: Gerätemodelldatenbank
source_url: https://docs.openclaw.ai/de/reference/device-models
scraped_at: 2026-05-25
---

Die macOS-Companion-App zeigt in der UI **Instances** benutzerfreundliche Namen für Apple-Gerätemodelle an, indem Apple-Modellkennungen (z. B. `iPad16,6`, `Mac16,6`) menschenlesbaren Namen zugeordnet werden.

Die Zuordnung ist als JSON unter folgendem Pfad eingebunden:

  * `apps/macos/Sources/OpenClaw/Resources/DeviceModels/`


## Datenquelle

Derzeit binden wir die Zuordnung aus dem unter MIT lizenzierten Repository ein:

  * `kyle-seongwoo-jun/apple-device-identifiers`


Damit Builds deterministisch bleiben, sind die JSON-Dateien auf bestimmte Upstream-Commits festgelegt (dokumentiert in `apps/macos/Sources/OpenClaw/Resources/DeviceModels/NOTICE.md`).

## Die Datenbank aktualisieren

  1. Wählen Sie die Upstream-Commits aus, auf die Sie festlegen möchten (einen für iOS, einen für macOS).
  2. Aktualisieren Sie die Commit-Hashes in `apps/macos/Sources/OpenClaw/Resources/DeviceModels/NOTICE.md`.
  3. Laden Sie die JSON-Dateien erneut herunter, festgelegt auf diese Commits:

bashCopy code
[code]
    IOS_COMMIT="<commit sha for ios-device-identifiers.json>"MAC_COMMIT="<commit sha for mac-device-identifiers.json>" curl -fsSL "https://raw.githubusercontent.com/kyle-seongwoo-jun/apple-device-identifiers/${IOS_COMMIT}/ios-device-identifiers.json" \  -o apps/macos/Sources/OpenClaw/Resources/DeviceModels/ios-device-identifiers.json curl -fsSL "https://raw.githubusercontent.com/kyle-seongwoo-jun/apple-device-identifiers/${MAC_COMMIT}/mac-device-identifiers.json" \  -o apps/macos/Sources/OpenClaw/Resources/DeviceModels/mac-device-identifiers.json
[/code]

  4. Stellen Sie sicher, dass `apps/macos/Sources/OpenClaw/Resources/DeviceModels/LICENSE.apple-device-identifiers.txt` weiterhin mit dem Upstream übereinstimmt (ersetzen Sie die Datei, wenn sich die Upstream-Lizenz ändert).
  5. Vergewissern Sie sich, dass die macOS-App fehlerfrei erstellt wird (ohne Warnungen):

bashCopy code
[code]
    swift build --package-path apps/macos
[/code]

## Verwandt

  * [Nodes](</de/nodes>)
  * [Fehlerbehebung für Node](</de/nodes/troubleshooting>)


Was this useful?YesNo