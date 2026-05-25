---
title: Hostinger
source_url: https://docs.openclaw.ai/ja-JP/install/hostinger
scraped_at: 2026-05-25
---

[Hostinger](<https://www.hostinger.com/openclaw>) 上で、**1クリック** のマネージドデプロイ、または **VPS** インストールを使って、永続的なOpenClaw Gatewayを実行します。

## 前提条件

  * Hostingerアカウント（[signup](<https://www.hostinger.com/openclaw>)）
  * 約5〜10分


## オプションA: 1クリックOpenClaw

最も素早く始める方法です。Hostingerがインフラ、Docker、自動更新を処理します。

* ### 購入して起動する

  1. [Hostinger OpenClawページ](<https://www.hostinger.com/openclaw>) で、Managed OpenClawプランを選択し、購入手続きを完了します。


* ### メッセージングチャネルを選ぶ

接続するチャネルを1つ以上選択します:

  * **WhatsApp** \-- セットアップウィザードに表示されるQRコードをスキャンします。
  * **Telegram** \-- [BotFather](<https://t.me/BotFather>) から取得したボットトークンを貼り付けます。


* ### インストールを完了する

**Finish** をクリックしてインスタンスをデプロイします。準備ができたら、hPanel の **OpenClaw Overview** からOpenClawダッシュボードにアクセスします。

## オプションB: VPS上のOpenClaw

サーバーをより細かく制御できます。HostingerはあなたのVPS上にDocker経由でOpenClawをデプロイし、hPanel の **Docker Manager** から管理します。

* ### VPSを購入する

  1. [Hostinger OpenClawページ](<https://www.hostinger.com/openclaw>) で、OpenClaw on VPSプランを選択し、購入手続きを完了します。


* ### OpenClawを設定する

VPSのプロビジョニング後、設定項目を入力します:

  * **Gateway token** \-- 自動生成されます。後で使うので保存してください。
  * **WhatsApp number** \-- 国番号付きのあなたの番号（任意）。
  * **Telegram bot token** \-- [BotFather](<https://t.me/BotFather>) から取得（任意）。
  * **API keys** \-- 購入時にReady-to-Use AIクレジットを選択しなかった場合のみ必要です。


* ### OpenClawを起動する

**Deploy** をクリックします。起動したら、hPanel で **Open** をクリックしてOpenClawダッシュボードを開きます。

ログ、再起動、更新は、hPanel のDocker Managerインターフェースから直接管理します。更新するには、Docker Managerの **Update** を押すと最新イメージがpullされます。

## セットアップを確認する

接続したチャネルで、アシスタントに「Hi」と送ってください。OpenClawが返信し、初期設定について案内します。

## トラブルシューティング

**ダッシュボードが読み込まれない** \-- コンテナのプロビジョニング完了まで数分待ってください。hPanelのDocker Managerログを確認してください。

**Dockerコンテナが再起動を繰り返す** \-- Docker Managerログを開き、設定エラー（トークン不足、無効なAPIキー）がないか確認してください。

**Telegramボットが応答しない** \-- 接続を完了するため、Telegramからペアリングコードメッセージを、OpenClawチャット内に直接メッセージとして送ってください。

## 次のステップ

  * [Channels](</ja-JP/channels>) \-- Telegram、WhatsApp、Discord などを接続する
  * [Gateway設定](</ja-JP/gateway/configuration>) \-- すべての設定オプション


## 関連

  * [インストール概要](</ja-JP/install>)
  * [VPSホスティング](</ja-JP/vps>)
  * [DigitalOcean](</ja-JP/install/digitalocean>)


Was this useful?YesNo