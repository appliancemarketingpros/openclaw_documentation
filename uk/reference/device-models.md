---
title: база даних моделей пристроїв
source_url: https://docs.openclaw.ai/uk/reference/device-models
scraped_at: 2026-05-25
---

Супутній застосунок macOS показує дружні назви моделей пристроїв Apple в UI **Instances** , зіставляючи ідентифікатори моделей Apple (наприклад, `iPad16,6`, `Mac16,6`) з людиночитаними назвами.

Зіставлення вендориться як JSON у:

  * `apps/macos/Sources/OpenClaw/Resources/DeviceModels/`


## Джерело даних

Наразі ми вендоримо зіставлення з репозиторію під ліцензією MIT:

  * `kyle-seongwoo-jun/apple-device-identifiers`


Щоб забезпечити детермінованість збірок, JSON-файли прив’язані до конкретних комітів upstream (записаних у `apps/macos/Sources/OpenClaw/Resources/DeviceModels/NOTICE.md`).

## Оновлення бази даних

  1. Виберіть коміти upstream, до яких хочете прив’язатися (один для iOS, один для macOS).
  2. Оновіть hash комітів у `apps/macos/Sources/OpenClaw/Resources/DeviceModels/NOTICE.md`.
  3. Повторно завантажте JSON-файли, прив’язані до цих комітів:

bashCopy code
[code]
    IOS_COMMIT="<commit sha for ios-device-identifiers.json>"MAC_COMMIT="<commit sha for mac-device-identifiers.json>" curl -fsSL "https://raw.githubusercontent.com/kyle-seongwoo-jun/apple-device-identifiers/${IOS_COMMIT}/ios-device-identifiers.json" \  -o apps/macos/Sources/OpenClaw/Resources/DeviceModels/ios-device-identifiers.json curl -fsSL "https://raw.githubusercontent.com/kyle-seongwoo-jun/apple-device-identifiers/${MAC_COMMIT}/mac-device-identifiers.json" \  -o apps/macos/Sources/OpenClaw/Resources/DeviceModels/mac-device-identifiers.json
[/code]

  4. Переконайтеся, що `apps/macos/Sources/OpenClaw/Resources/DeviceModels/LICENSE.apple-device-identifiers.txt` усе ще відповідає upstream (замініть його, якщо upstream-ліцензія зміниться).
  5. Перевірте, що застосунок macOS збирається без попереджень:

bashCopy code
[code]
    swift build --package-path apps/macos
[/code]

## Пов’язане

  * [Nodes](</uk/nodes>)
  * [Усунення проблем Node](</uk/nodes/troubleshooting>)


Was this useful?YesNo