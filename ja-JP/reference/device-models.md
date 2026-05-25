---
title: デバイス model データベース
source_url: https://docs.openclaw.ai/ja-JP/reference/device-models
scraped_at: 2026-05-25
---

macOS コンパニオンアプリは、Apple の model identifier（例: `iPad16,6`、`Mac16,6`）を人間が読みやすい名前へマッピングすることで、**Instances** UI に分かりやすい Apple デバイス model 名を表示します。

このマッピングは JSON として次に vendor されています。

  * `apps/macos/Sources/OpenClaw/Resources/DeviceModels/`


## データソース

現在、このマッピングは MIT ライセンスの次のリポジトリから vendor しています。

  * `kyle-seongwoo-jun/apple-device-identifiers`


ビルドを決定的に保つため、JSON ファイルは特定の upstream commit に pin されています（`apps/macos/Sources/OpenClaw/Resources/DeviceModels/NOTICE.md` に記録）。

## データベースを更新する

  1. pin したい upstream commit を選びます（iOS 用 1 つ、macOS 用 1 つ）。
  2. `apps/macos/Sources/OpenClaw/Resources/DeviceModels/NOTICE.md` の commit hash を更新します。
  3. その commit に pin した JSON ファイルを再ダウンロードします。

bashCopy code
[code]
    IOS_COMMIT="<ios-device-identifiers.json 用の commit sha>"MAC_COMMIT="<mac-device-identifiers.json 用の commit sha>" curl -fsSL "https://raw.githubusercontent.com/kyle-seongwoo-jun/apple-device-identifiers/${IOS_COMMIT}/ios-device-identifiers.json" \  -o apps/macos/Sources/OpenClaw/Resources/DeviceModels/ios-device-identifiers.json curl -fsSL "https://raw.githubusercontent.com/kyle-seongwoo-jun/apple-device-identifiers/${MAC_COMMIT}/mac-device-identifiers.json" \  -o apps/macos/Sources/OpenClaw/Resources/DeviceModels/mac-device-identifiers.json
[/code]

  4. `apps/macos/Sources/OpenClaw/Resources/DeviceModels/LICENSE.apple-device-identifiers.txt` が引き続き upstream と一致していることを確認してください（upstream のライセンスが変わっていたら置き換えてください）。
  5. macOS アプリが警告なしでビルドできることを確認してください。

bashCopy code
[code]
    swift build --package-path apps/macos
[/code]

## 関連

  * [Nodes](</ja-JP/nodes>)
  * [Node troubleshooting](</ja-JP/nodes/troubleshooting>)


Was this useful?YesNo