---
title: WhatsApp Plugin
source_url: https://docs.openclaw.ai/ja-JP/plugins/reference/whatsapp
scraped_at: 2026-05-25
---

# WhatsApp Plugin

OpenClaw メッセージを送受信するための WhatsApp チャネルサーフェスを追加します。

## 配布

  * パッケージ: `@openclaw/whatsapp`
  * インストール経路: npm; ClawHub


## サーフェス

channels: whatsapp

## Windows インストール時の注意

Windows では、WhatsApp Plugin は npm install 中に `PATH` 上の Git を必要とします。これは、その Baileys/libsignal 依存関係の 1 つが git URL から取得されるためです。Git for Windows をインストールし、シェルを再起動してからインストールを再実行します。

powershellCopy code
[code]
    winget install --id Git.Git -e
[/code]

Portable Git も、その `bin` ディレクトリが `PATH` 上にあれば動作します。

## 関連ドキュメント

  * [whatsapp](</ja-JP/channels/whatsapp>)


Was this useful?YesNo