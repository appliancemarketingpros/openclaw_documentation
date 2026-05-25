---
title: Cloudflare AI Gateway
source_url: https://docs.openclaw.ai/ja-JP/providers/cloudflare-ai-gateway
scraped_at: 2026-05-25
---

Cloudflare AI Gateway はプロバイダー API の前段に配置され、分析、キャッシュ、制御を追加できます。Anthropic の場合、OpenClaw は Gateway エンドポイント経由で Anthropic Messages API を使用します。

プロパティ | 値  
---|---  
プロバイダー | `cloudflare-ai-gateway`  
ベース URL | `https://gateway.ai.cloudflare.com/v1/<account_id>/<gateway_id>/anthropic`  
デフォルトモデル | `cloudflare-ai-gateway/claude-sonnet-4-6`  
APIキー | `CLOUDFLARE_AI_GATEWAY_API_KEY`（Gateway 経由のリクエストに使用するプロバイダー APIキー）  
  
Anthropic Messages モデルで thinking が有効な場合、OpenClaw は Cloudflare AI Gateway 経由でペイロードを送信する前に、末尾の assistant prefill ターンを取り除きます。Anthropic は extended thinking でのレスポンスの prefilling を拒否しますが、通常の thinking なしの prefill は引き続き利用できます。

## はじめに

* ### プロバイダー APIキーと Gateway 詳細を設定する

オンボーディングを実行し、Cloudflare AI Gateway の認証オプションを選択します。

bashCopy code
[code]
    openclaw onboard --auth-choice cloudflare-ai-gateway-api-key
[/code]

これにより、アカウント ID、Gateway ID、APIキーの入力が求められます。

* ### デフォルトモデルを設定する

OpenClaw 設定にモデルを追加します。

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "cloudflare-ai-gateway/claude-sonnet-4-6" },    },  },}
[/code]

* ### モデルが利用可能であることを確認する

bashCopy code
[code]
    openclaw models list --provider cloudflare-ai-gateway
[/code]

## 非対話型の例

スクリプトや CI のセットアップでは、すべての値をコマンドラインで渡します。

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice cloudflare-ai-gateway-api-key \  --cloudflare-ai-gateway-account-id "your-account-id" \  --cloudflare-ai-gateway-gateway-id "your-gateway-id" \  --cloudflare-ai-gateway-api-key "$CLOUDFLARE_AI_GATEWAY_API_KEY"
[/code]

## 高度な設定

認証付き Gateway

Cloudflare で Gateway 認証を有効にした場合は、`cf-aig-authorization` ヘッダーを追加します。これはプロバイダー APIキー**に加えて** 必要です。

json5Copy code
[code]
    {  models: {    providers: {      "cloudflare-ai-gateway": {        headers: {          "cf-aig-authorization": "Bearer <cloudflare-ai-gateway-token>",        },      },    },  },}
[/code]

環境に関する注意

Gateway がデーモン（launchd/systemd）として実行されている場合は、`CLOUDFLARE_AI_GATEWAY_API_KEY` がそのプロセスで利用できるようにしてください。

## 関連

[**モデル選択** プロバイダー、モデル参照、フェイルオーバー動作の選択。 ](</ja-JP/concepts/model-providers>) [**トラブルシューティング** 一般的なトラブルシューティングと FAQ。 ](</ja-JP/help/troubleshooting>)

Was this useful?YesNo