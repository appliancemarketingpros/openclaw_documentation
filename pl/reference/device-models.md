---
title: Baza danych modeli urządzeń
source_url: https://docs.openclaw.ai/pl/reference/device-models
scraped_at: 2026-05-25
---

Aplikacja towarzysząca macOS wyświetla przyjazne nazwy modeli urządzeń Apple w interfejsie **Instances** , mapując identyfikatory modeli Apple (np. `iPad16,6`, `Mac16,6`) na czytelne dla użytkownika nazwy.

Mapowanie jest dostarczane jako JSON w katalogu:

  * `apps/macos/Sources/OpenClaw/Resources/DeviceModels/`


## Źródło danych

Obecnie dostarczamy mapowanie z repozytorium na licencji MIT:

  * `kyle-seongwoo-jun/apple-device-identifiers`


Aby zachować deterministyczność kompilacji, pliki JSON są przypięte do konkretnych commitów upstream (zapisanych w `apps/macos/Sources/OpenClaw/Resources/DeviceModels/NOTICE.md`).

## Aktualizowanie bazy danych

  1. Wybierz commity upstream, do których chcesz przypiąć wersje (jeden dla iOS, jeden dla macOS).
  2. Zaktualizuj hashe commitów w `apps/macos/Sources/OpenClaw/Resources/DeviceModels/NOTICE.md`.
  3. Pobierz ponownie pliki JSON, przypięte do tych commitów:

bashCopy code
[code]
    IOS_COMMIT="<commit sha for ios-device-identifiers.json>"MAC_COMMIT="<commit sha for mac-device-identifiers.json>" curl -fsSL "https://raw.githubusercontent.com/kyle-seongwoo-jun/apple-device-identifiers/${IOS_COMMIT}/ios-device-identifiers.json" \  -o apps/macos/Sources/OpenClaw/Resources/DeviceModels/ios-device-identifiers.json curl -fsSL "https://raw.githubusercontent.com/kyle-seongwoo-jun/apple-device-identifiers/${MAC_COMMIT}/mac-device-identifiers.json" \  -o apps/macos/Sources/OpenClaw/Resources/DeviceModels/mac-device-identifiers.json
[/code]

  4. Upewnij się, że `apps/macos/Sources/OpenClaw/Resources/DeviceModels/LICENSE.apple-device-identifiers.txt` nadal odpowiada wersji upstream (zastąp go, jeśli licencja upstream się zmieni).
  5. Zweryfikuj, że aplikacja macOS kompiluje się poprawnie (bez ostrzeżeń):

bashCopy code
[code]
    swift build --package-path apps/macos
[/code]

## Powiązane

  * [Nodes](</pl/nodes>)
  * [Rozwiązywanie problemów z Node](</pl/nodes/troubleshooting>)


Was this useful?YesNo