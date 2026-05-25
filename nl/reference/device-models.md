---
title: Database met apparaatmodellen
source_url: https://docs.openclaw.ai/nl/reference/device-models
scraped_at: 2026-05-25
---

De begeleidende macOS-app toont gebruiksvriendelijke Apple-apparaatmodelnamen in de **Instanties** -UI door Apple-model-ID's (bijv. `iPad16,6`, `Mac16,6`) toe te wijzen aan voor mensen leesbare namen.

De toewijzing is als JSON meegeleverd onder:

  * `apps/macos/Sources/OpenClaw/Resources/DeviceModels/`


## Gegevensbron

We leveren de toewijzing momenteel mee uit de repository met MIT-licentie:

  * `kyle-seongwoo-jun/apple-device-identifiers`


Om builds deterministisch te houden, zijn de JSON-bestanden vastgezet op specifieke broncommits (vastgelegd in `apps/macos/Sources/OpenClaw/Resources/DeviceModels/NOTICE.md`).

## De database bijwerken

  1. Kies de broncommits waarop je wilt vastzetten (een voor iOS, een voor macOS).
  2. Werk de commit-hashes bij in `apps/macos/Sources/OpenClaw/Resources/DeviceModels/NOTICE.md`.
  3. Download de JSON-bestanden opnieuw, vastgezet op die commits:

bashCopy code
[code]
    IOS_COMMIT="<commit sha for ios-device-identifiers.json>"MAC_COMMIT="<commit sha for mac-device-identifiers.json>" curl -fsSL "https://raw.githubusercontent.com/kyle-seongwoo-jun/apple-device-identifiers/${IOS_COMMIT}/ios-device-identifiers.json" \  -o apps/macos/Sources/OpenClaw/Resources/DeviceModels/ios-device-identifiers.json curl -fsSL "https://raw.githubusercontent.com/kyle-seongwoo-jun/apple-device-identifiers/${MAC_COMMIT}/mac-device-identifiers.json" \  -o apps/macos/Sources/OpenClaw/Resources/DeviceModels/mac-device-identifiers.json
[/code]

  4. Zorg ervoor dat `apps/macos/Sources/OpenClaw/Resources/DeviceModels/LICENSE.apple-device-identifiers.txt` nog steeds overeenkomt met de bronrepository (vervang het als de licentie van de bronrepository verandert).
  5. Controleer of de macOS-app zonder problemen bouwt (geen waarschuwingen):

bashCopy code
[code]
    swift build --package-path apps/macos
[/code]

## Gerelateerd

  * [Nodes](</nl/nodes>)
  * [Node-probleemoplossing](</nl/nodes/troubleshooting>)


Was this useful?YesNo