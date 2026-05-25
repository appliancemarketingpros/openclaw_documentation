---
title: ダッシュボード
source_url: https://docs.openclaw.ai/ja-JP/cli/dashboard
scraped_at: 2026-05-25
---

# `openclaw dashboard`

現在の認証を使用して Control UI を開きます。

bashCopy code
[code]
    openclaw dashboardopenclaw dashboard --no-open
[/code]

注記:

  * `dashboard` は、可能な場合に設定済みの `gateway.auth.token` SecretRefs を解決します。
  * `dashboard` は `gateway.tls.enabled` に従います。TLS が有効な Gateway は `https://` Control UI URL を表示/開き、`wss://` 経由で接続します。
  * トークン認証されたダッシュボード URL のクリップボード/ブラウザー配信に失敗した場合、 `dashboard` は安全な手動認証ヒントをログに記録し、トークン値を出力せずに `OPENCLAW_GATEWAY_TOKEN`、`gateway.auth.token`、フラグメントキー `token` を示します。
  * SecretRef で管理されたトークン（解決済みまたは未解決）の場合、`dashboard` はターミナル出力、クリップボード履歴、ブラウザー起動引数で外部シークレットを公開しないように、トークン化されていない URL を表示/コピー/開きます。
  * `gateway.auth.token` が SecretRef で管理されているものの、このコマンドパスで未解決の場合、コマンドは無効なトークンプレースホルダーを埋め込む代わりに、トークン化されていない URL と明示的な修復手順を表示します。


## 関連

  * [CLI リファレンス](</ja-JP/cli>)
  * [ダッシュボード](</ja-JP/web/dashboard>)


Was this useful?YesNo