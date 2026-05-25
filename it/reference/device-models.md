---
title: Database dei modelli dei dispositivi
source_url: https://docs.openclaw.ai/it/reference/device-models
scraped_at: 2026-05-25
---

L'app companion macOS mostra nomi leggibili dei modelli dei dispositivi Apple nell'interfaccia **Instances** mappando gli identificatori di modello Apple (ad esempio `iPad16,6`, `Mac16,6`) a nomi comprensibili.

La mappatura è inclusa come JSON sotto:

  * `apps/macos/Sources/OpenClaw/Resources/DeviceModels/`


## Sorgente dati

Attualmente includiamo come vendor la mappatura dal repository con licenza MIT:

  * `kyle-seongwoo-jun/apple-device-identifiers`


Per mantenere le build deterministiche, i file JSON sono fissati a commit upstream specifici (registrati in `apps/macos/Sources/OpenClaw/Resources/DeviceModels/NOTICE.md`).

## Aggiornamento del database

  1. Scegli i commit upstream che vuoi fissare (uno per iOS, uno per macOS).
  2. Aggiorna gli hash dei commit in `apps/macos/Sources/OpenClaw/Resources/DeviceModels/NOTICE.md`.
  3. Riscarica i file JSON, fissati a quei commit:

bashCopy code
[code]
    IOS_COMMIT="<commit sha for ios-device-identifiers.json>"MAC_COMMIT="<commit sha for mac-device-identifiers.json>" curl -fsSL "https://raw.githubusercontent.com/kyle-seongwoo-jun/apple-device-identifiers/${IOS_COMMIT}/ios-device-identifiers.json" \  -o apps/macos/Sources/OpenClaw/Resources/DeviceModels/ios-device-identifiers.json curl -fsSL "https://raw.githubusercontent.com/kyle-seongwoo-jun/apple-device-identifiers/${MAC_COMMIT}/mac-device-identifiers.json" \  -o apps/macos/Sources/OpenClaw/Resources/DeviceModels/mac-device-identifiers.json
[/code]

  4. Assicurati che `apps/macos/Sources/OpenClaw/Resources/DeviceModels/LICENSE.apple-device-identifiers.txt` corrisponda ancora all'upstream (sostituiscilo se la licenza upstream cambia).
  5. Verifica che l'app macOS venga compilata correttamente (senza avvisi):

bashCopy code
[code]
    swift build --package-path apps/macos
[/code]

## Correlati

  * [Node](</it/nodes>)
  * [Risoluzione dei problemi dei Node](</it/nodes/troubleshooting>)


Was this useful?YesNo