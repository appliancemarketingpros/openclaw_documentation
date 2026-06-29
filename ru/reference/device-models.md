---
title: База данных моделей устройств
source_url: https://docs.openclaw.ai/ru/reference/device-models
scraped_at: 2026-06-29
---

ReferenceRPC and API

Сопутствующее приложение для macOS показывает понятные имена моделей устройств Apple в UI **Экземпляры** , сопоставляя идентификаторы моделей Apple (например, `iPad16,6`, `Mac16,6`) с человекочитаемыми именами.

Сопоставление поставляется как JSON в:

  * `apps/macos/Sources/OpenClaw/Resources/DeviceModels/`


## Источник данных

Сейчас мы поставляем сопоставление из репозитория под лицензией MIT:

  * `kyle-seongwoo-jun/apple-device-identifiers`


Чтобы сборки были детерминированными, JSON-файлы закреплены за конкретными вышестоящими коммитами (записаны в `apps/macos/Sources/OpenClaw/Resources/DeviceModels/NOTICE.md`).

## Обновление базы данных

  1. Выберите вышестоящие коммиты, за которыми нужно закрепиться (один для iOS, один для macOS).
  2. Обновите хэши коммитов в `apps/macos/Sources/OpenClaw/Resources/DeviceModels/NOTICE.md`.
  3. Повторно скачайте JSON-файлы, закрепленные за этими коммитами:

bashCopy code
[code]
    IOS_COMMIT="<commit sha for ios-device-identifiers.json>"MAC_COMMIT="<commit sha for mac-device-identifiers.json>" curl -fsSL "https://raw.githubusercontent.com/kyle-seongwoo-jun/apple-device-identifiers/${IOS_COMMIT}/ios-device-identifiers.json" \  -o apps/macos/Sources/OpenClaw/Resources/DeviceModels/ios-device-identifiers.json curl -fsSL "https://raw.githubusercontent.com/kyle-seongwoo-jun/apple-device-identifiers/${MAC_COMMIT}/mac-device-identifiers.json" \  -o apps/macos/Sources/OpenClaw/Resources/DeviceModels/mac-device-identifiers.json
[/code]

  4. Убедитесь, что `apps/macos/Sources/OpenClaw/Resources/DeviceModels/LICENSE.apple-device-identifiers.txt` по-прежнему соответствует вышестоящему репозиторию (замените его, если вышестоящая лицензия изменится).
  5. Проверьте, что приложение macOS собирается без ошибок (без предупреждений):

bashCopy code
[code]
    swift build --package-path apps/macos
[/code]

## Связанные материалы

  * [Nodes](</ru/nodes>)
  * [Устранение неполадок Node](</ru/nodes/troubleshooting>)


Was this useful?YesNo

Open issue