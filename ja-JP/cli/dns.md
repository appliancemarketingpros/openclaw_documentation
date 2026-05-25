---
title: DNS
source_url: https://docs.openclaw.ai/ja-JP/cli/dns
scraped_at: 2026-05-25
---

# `openclaw dns`

広域ディスカバリー用の DNS ヘルパー (Tailscale + CoreDNS)。現在は macOS + Homebrew CoreDNS に重点を置いています。

関連:

  * Gateway ディスカバリー: [ディスカバリー](</ja-JP/gateway/discovery>)
  * 広域ディスカバリー設定: [設定](</ja-JP/gateway/configuration>)


## セットアップ

bashCopy code
[code]
    openclaw dns setupopenclaw dns setup --domain openclaw.internalopenclaw dns setup --apply
[/code]

## `dns setup`

ユニキャスト DNS-SD ディスカバリー用の CoreDNS セットアップを計画または適用します。

オプション:

  * `--domain <domain>`: 広域ディスカバリードメイン (例: `openclaw.internal`)
  * `--apply`: CoreDNS 設定をインストールまたは更新し、サービスを再起動します (sudo が必要、macOS のみ)


表示内容:

  * 解決されたディスカバリードメイン
  * ゾーンファイルパス
  * 現在の tailnet IP
  * 推奨される `openclaw.json` ディスカバリー設定
  * 設定する Tailscale Split DNS のネームサーバー/ドメイン値


注記:

  * `--apply` なしでは、このコマンドは計画用ヘルパーのみとして機能し、推奨セットアップを出力します。
  * `--domain` を省略した場合、OpenClaw は設定の `discovery.wideArea.domain` を使用します。
  * `--apply` は現在 macOS のみをサポートし、Homebrew CoreDNS を前提としています。
  * `--apply` は必要に応じてゾーンファイルをブートストラップし、CoreDNS の import スタンザが存在することを確認し、`coredns` brew サービスを再起動します。


## 関連

  * [CLI リファレンス](</ja-JP/cli>)
  * [ディスカバリー](</ja-JP/gateway/discovery>)


Was this useful?YesNo