---
title: Database model perangkat
source_url: https://docs.openclaw.ai/id/reference/device-models
scraped_at: 2026-05-25
---

Aplikasi pendamping macOS menampilkan nama model perangkat Apple yang mudah dikenali di UI **Instances** dengan memetakan identifier model Apple (misalnya `iPad16,6`, `Mac16,6`) ke nama yang dapat dibaca manusia.

Pemetaan tersebut divendor sebagai JSON di bawah:

  * `apps/macos/Sources/OpenClaw/Resources/DeviceModels/`


## Sumber data

Saat ini kami memvendor pemetaan dari repositori berlisensi MIT:

  * `kyle-seongwoo-jun/apple-device-identifiers`


Agar build tetap deterministik, file JSON dipin ke commit upstream tertentu (dicatat di `apps/macos/Sources/OpenClaw/Resources/DeviceModels/NOTICE.md`).

## Memperbarui database

  1. Pilih commit upstream yang ingin Anda pin (satu untuk iOS, satu untuk macOS).
  2. Perbarui hash commit di `apps/macos/Sources/OpenClaw/Resources/DeviceModels/NOTICE.md`.
  3. Unduh ulang file JSON, dipin ke commit tersebut:

bashCopy code
[code]
    IOS_COMMIT="<commit sha untuk ios-device-identifiers.json>"MAC_COMMIT="<commit sha untuk mac-device-identifiers.json>" curl -fsSL "https://raw.githubusercontent.com/kyle-seongwoo-jun/apple-device-identifiers/${IOS_COMMIT}/ios-device-identifiers.json" \  -o apps/macos/Sources/OpenClaw/Resources/DeviceModels/ios-device-identifiers.json curl -fsSL "https://raw.githubusercontent.com/kyle-seongwoo-jun/apple-device-identifiers/${MAC_COMMIT}/mac-device-identifiers.json" \  -o apps/macos/Sources/OpenClaw/Resources/DeviceModels/mac-device-identifiers.json
[/code]

  4. Pastikan `apps/macos/Sources/OpenClaw/Resources/DeviceModels/LICENSE.apple-device-identifiers.txt` masih cocok dengan upstream (ganti jika lisensi upstream berubah).
  5. Verifikasi bahwa aplikasi macOS berhasil dibangun dengan bersih (tanpa peringatan):

bashCopy code
[code]
    swift build --package-path apps/macos
[/code]

## Terkait

  * [Node](</id/nodes>)
  * [Pemecahan masalah Node](</id/nodes/troubleshooting>)


Was this useful?YesNo