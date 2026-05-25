---
title: Aygıt model veritabanı
source_url: https://docs.openclaw.ai/tr/reference/device-models
scraped_at: 2026-05-25
---

macOS yardımcı uygulaması, Apple model tanımlayıcılarını (ör. `iPad16,6`, `Mac16,6`) insan tarafından okunabilir adlara eşleyerek **Instances** UI'sında kolay okunur Apple aygıt model adlarını gösterir.

Eşleme, şu konum altında JSON olarak vendörlenir:

  * `apps/macos/Sources/OpenClaw/Resources/DeviceModels/`


## Veri kaynağı

Şu anda eşlemeyi MIT lisanslı şu depodan vendörlüyoruz:

  * `kyle-seongwoo-jun/apple-device-identifiers`


Derlemeleri deterministik tutmak için JSON dosyaları belirli upstream commit'lerine sabitlenir (`apps/macos/Sources/OpenClaw/Resources/DeviceModels/NOTICE.md` içinde kaydedilir).

## Veritabanını güncelleme

  1. Sabitlemek istediğiniz upstream commit'lerini seçin (biri iOS, biri macOS için).
  2. `apps/macos/Sources/OpenClaw/Resources/DeviceModels/NOTICE.md` içinde commit hash'lerini güncelleyin.
  3. Bu commit'lere sabitlenmiş JSON dosyalarını yeniden indirin:

bashCopy code
[code]
    IOS_COMMIT="<ios-device-identifiers.json için commit sha>"MAC_COMMIT="<mac-device-identifiers.json için commit sha>" curl -fsSL "https://raw.githubusercontent.com/kyle-seongwoo-jun/apple-device-identifiers/${IOS_COMMIT}/ios-device-identifiers.json" \  -o apps/macos/Sources/OpenClaw/Resources/DeviceModels/ios-device-identifiers.json curl -fsSL "https://raw.githubusercontent.com/kyle-seongwoo-jun/apple-device-identifiers/${MAC_COMMIT}/mac-device-identifiers.json" \  -o apps/macos/Sources/OpenClaw/Resources/DeviceModels/mac-device-identifiers.json
[/code]

  4. `apps/macos/Sources/OpenClaw/Resources/DeviceModels/LICENSE.apple-device-identifiers.txt` dosyasının hâlâ upstream ile eşleştiğinden emin olun (upstream lisansı değişirse değiştirin).
  5. macOS uygulamasının temiz şekilde derlendiğini doğrulayın (uyarı olmadan):

bashCopy code
[code]
    swift build --package-path apps/macos
[/code]

## İlgili

  * [Node'lar](</tr/nodes>)
  * [Node sorun giderme](</tr/nodes/troubleshooting>)


Was this useful?YesNo