---
title: macOS 署名
source_url: https://docs.openclaw.ai/ja-JP/platforms/mac/signing
scraped_at: 2026-05-25
---

# mac の署名 (デバッグビルド)

このアプリは通常 [`scripts/package-mac-app.sh`](<https://github.com/openclaw/openclaw/blob/main/scripts/package-mac-app.sh>) からビルドされ、現在は次を行います。

  * 安定したデバッグ用バンドル識別子を設定します: `ai.openclaw.mac.debug`
  * そのバンドル ID で Info.plist を書き込みます (`BUNDLE_ID=...` で上書き可能)
  * [`scripts/codesign-mac-app.sh`](<https://github.com/openclaw/openclaw/blob/main/scripts/codesign-mac-app.sh>) を呼び出してメインバイナリとアプリバンドルに署名し、macOS が各リビルドを同じ署名済みバンドルとして扱い、TCC 権限 (通知、アクセシビリティ、画面収録、マイク、音声) を保持するようにします。安定した権限には、実際の署名 ID を使用してください。アドホックは明示的なオプトインであり、壊れやすいです ([macOS 権限](</ja-JP/platforms/mac/permissions>) を参照)。
  * デフォルトで `CODESIGN_TIMESTAMP=auto` を使用します。これは Developer ID 署名の信頼されたタイムスタンプを有効にします。タイムスタンプを省略するには `CODESIGN_TIMESTAMP=off` を設定します (オフラインのデバッグビルド)。
  * ビルドメタデータを Info.plist に注入します: `OpenClawBuildTimestamp` (UTC) と `OpenClawGitCommit` (短いハッシュ)。これにより About ペインでビルド、git、デバッグ/リリースチャネルを表示できます。
  * **パッケージングはデフォルトで Node 24** : スクリプトは TS ビルドと Control UI ビルドを実行します。Node 22 LTS、現在は `22.16+` も互換性のため引き続きサポートされます。
  * 環境から `SIGN_IDENTITY` を読み取ります。常に自分の証明書で署名するには、`export SIGN_IDENTITY="Apple Development: Your Name (TEAMID)"` (または Developer ID Application 証明書) をシェル rc に追加してください。アドホック署名には `ALLOW_ADHOC_SIGNING=1` または `SIGN_IDENTITY="-"` による明示的なオプトインが必要です (権限テストには推奨されません)。
  * 署名後に Team ID 監査を実行し、アプリバンドル内のいずれかの Mach-O が異なる Team ID で署名されている場合は失敗します。回避するには `SKIP_TEAM_ID_CHECK=1` を設定します。


## 使い方

bashCopy code
[code]
    # from repo rootscripts/package-mac-app.sh               # auto-selects identity; errors if none foundSIGN_IDENTITY="Developer ID Application: Your Name" scripts/package-mac-app.sh   # real certALLOW_ADHOC_SIGNING=1 scripts/package-mac-app.sh    # ad-hoc (permissions will not stick)SIGN_IDENTITY="-" scripts/package-mac-app.sh        # explicit ad-hoc (same caveat)DISABLE_LIBRARY_VALIDATION=1 scripts/package-mac-app.sh   # dev-only Sparkle Team ID mismatch workaround
[/code]

### アドホック署名に関する注意

`SIGN_IDENTITY="-"` (アドホック) で署名する場合、スクリプトは自動的に **Hardened Runtime** (`--options runtime`) を無効にします。これは、同じ Team ID を共有しない埋め込みフレームワーク (Sparkle など) をアプリが読み込もうとしたときのクラッシュを防ぐために必要です。アドホック署名は TCC 権限の永続化も壊します。復旧手順については [macOS 権限](</ja-JP/platforms/mac/permissions>) を参照してください。

## About 用ビルドメタデータ

`package-mac-app.sh` はバンドルに次を記録します。

  * `OpenClawBuildTimestamp`: パッケージ作成時の ISO8601 UTC
  * `OpenClawGitCommit`: 短い git ハッシュ (利用できない場合は `unknown`)


About タブはこれらのキーを読み取り、バージョン、ビルド日、git コミット、デバッグビルドかどうか (`#if DEBUG` 経由) を表示します。コード変更後にこれらの値を更新するには、パッケージャーを実行してください。

## 理由

TCC 権限はバンドル識別子 _および_ コード署名に紐づきます。UUID が変わる未署名のデバッグビルドにより、macOS が各リビルド後に許可を忘れる原因になっていました。バイナリに署名し (デフォルトではアドホック)、固定のバンドル ID/パス (`dist/OpenClaw.app`) を維持することで、VibeTunnel のアプローチに合わせてビルド間で許可を保持します。

## 関連

  * [macOS アプリ](</ja-JP/platforms/macos>)
  * [macOS 権限](</ja-JP/platforms/mac/permissions>)


Was this useful?YesNo