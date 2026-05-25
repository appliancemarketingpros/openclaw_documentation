---
title: Zalo 個人用Plugin
source_url: https://docs.openclaw.ai/ja-JP/plugins/zalouser
scraped_at: 2026-05-25
---

OpenClaw の Zalo Personal 対応をプラグインで提供し、ネイティブの `zca-js` を使って通常の Zalo ユーザーアカウントを自動化します。

## 命名

チャネル id は `zalouser` です。これは、**個人の Zalo ユーザーアカウント** （非公式）を自動化することを明示するためです。`zalo` は将来の公式 Zalo API 統合の可能性のために予約しています。

## 実行場所

このプラグインは **Gateway プロセス内** で実行されます。

リモート Gateway を使用する場合は、**Gateway を実行しているマシン** にインストールして設定し、その後 Gateway を再起動してください。

外部の `zca`/`openzca` CLI バイナリは不要です。

## インストール

### オプション A: npm からインストール

bashCopy code
[code]
    openclaw plugins install @openclaw/zalouser
[/code]

現在の公式リリースタグに追従するには、素のパッケージを使用してください。再現可能なインストールが必要な場合のみ、正確なバージョンに固定してください。

その後、Gateway を再起動してください。

### オプション B: ローカルフォルダーからインストール（開発）

bashCopy code
[code]
    PLUGIN_SRC=./path/to/local/zalouser-pluginopenclaw plugins install "$PLUGIN_SRC"cd "$PLUGIN_SRC" && pnpm install
[/code]

その後、Gateway を再起動してください。

## 設定

チャネル設定は `channels.zalouser`（`plugins.entries.*` ではありません）配下にあります。

json5Copy code
[code]
    {  channels: {    zalouser: {      enabled: true,      dmPolicy: "pairing",    },  },}
[/code]

## CLI

bashCopy code
[code]
    openclaw channels login --channel zalouseropenclaw channels logout --channel zalouseropenclaw channels status --probeopenclaw message send --channel zalouser --target <threadId> --message "Hello from OpenClaw"openclaw directory peers list --channel zalouser --query "name"
[/code]

## エージェントツール

ツール名: `zalouser`

アクション: `send`, `image`, `link`, `friends`, `groups`, `me`, `status`

チャネルメッセージアクションは、メッセージリアクション用の `react` もサポートしています。

## 関連

  * [プラグインの構築](</ja-JP/plugins/building-plugins>)
  * [ClawHub](</ja-JP/clawhub>)


Was this useful?YesNo