---
title: Base de données des modèles d’appareils
source_url: https://docs.openclaw.ai/fr/reference/device-models
scraped_at: 2026-05-25
---

L’application compagnon macOS affiche des noms de modèles d’appareils Apple conviviaux dans l’interface utilisateur **Instances** en faisant correspondre les identifiants de modèle Apple (par ex. `iPad16,6`, `Mac16,6`) à des noms lisibles par l’humain.

Le mappage est intégré sous forme de JSON dans :

  * `apps/macos/Sources/OpenClaw/Resources/DeviceModels/`


## Source de données

Nous intégrons actuellement le mappage depuis le dépôt sous licence MIT suivant :

  * `kyle-seongwoo-jun/apple-device-identifiers`


Pour garantir des builds déterministes, les fichiers JSON sont épinglés à des commits upstream spécifiques (enregistrés dans `apps/macos/Sources/OpenClaw/Resources/DeviceModels/NOTICE.md`).

## Mise à jour de la base de données

  1. Choisissez les commits upstream que vous souhaitez épingler (un pour iOS, un pour macOS).
  2. Mettez à jour les hachages de commit dans `apps/macos/Sources/OpenClaw/Resources/DeviceModels/NOTICE.md`.
  3. Téléchargez à nouveau les fichiers JSON, épinglés à ces commits :

bashCopy code
[code]
    IOS_COMMIT="<sha de commit pour ios-device-identifiers.json>"MAC_COMMIT="<sha de commit pour mac-device-identifiers.json>" curl -fsSL "https://raw.githubusercontent.com/kyle-seongwoo-jun/apple-device-identifiers/${IOS_COMMIT}/ios-device-identifiers.json" \  -o apps/macos/Sources/OpenClaw/Resources/DeviceModels/ios-device-identifiers.json curl -fsSL "https://raw.githubusercontent.com/kyle-seongwoo-jun/apple-device-identifiers/${MAC_COMMIT}/mac-device-identifiers.json" \  -o apps/macos/Sources/OpenClaw/Resources/DeviceModels/mac-device-identifiers.json
[/code]

  4. Assurez-vous que `apps/macos/Sources/OpenClaw/Resources/DeviceModels/LICENSE.apple-device-identifiers.txt` correspond toujours à la version upstream (remplacez-le si la licence upstream change).
  5. Vérifiez que l’application macOS se compile correctement (sans avertissements) :

bashCopy code
[code]
    swift build --package-path apps/macos
[/code]

## Lié

  * [Nœuds](</fr/nodes>)
  * [Dépannage des nœuds](</fr/nodes/troubleshooting>)


Was this useful?YesNo