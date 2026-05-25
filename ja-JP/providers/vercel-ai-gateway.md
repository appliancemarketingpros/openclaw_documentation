---
title: Vercel AI Gateway
source_url: https://docs.openclaw.ai/ja-JP/providers/vercel-ai-gateway
scraped_at: 2026-05-25
---

The [Vercel AI Gateway](<https://vercel.com/ai-gateway>) は、単一のエンドポイントを通じて数百のモデルにアクセスするための統一 API を提供します。

プロパティ | 値  
---|---  
プロバイダー | `vercel-ai-gateway`  
認証 | `AI_GATEWAY_API_KEY`  
API | Anthropic Messages 互換  
モデルカタログ | `/v1/models` で自動検出  
  
## はじめに

* ### API キーを設定する

オンボーディングを実行し、AI Gateway 認証オプションを選択します。

bashCopy code
[code]
    openclaw onboard --auth-choice ai-gateway-api-key
[/code]

* ### デフォルトモデルを設定する

OpenClaw 設定にモデルを追加します。

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "vercel-ai-gateway/anthropic/claude-opus-4.6" },    },  },}
[/code]

* ### モデルが利用可能であることを確認する

bashCopy code
[code]
    openclaw models list --provider vercel-ai-gateway
[/code]

## 非対話型の例

スクリプト化されたセットアップや CI セットアップでは、すべての値をコマンドラインで渡します。

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice ai-gateway-api-key \  --ai-gateway-api-key "$AI_GATEWAY_API_KEY"
[/code]

## モデル ID の省略形

OpenClaw は Vercel Claude の省略形モデル参照を受け入れ、実行時に正規化します。

省略形入力 | 正規化されたモデル参照  
---|---  
`vercel-ai-gateway/claude-opus-4.6` | `vercel-ai-gateway/anthropic/claude-opus-4.6`  
`vercel-ai-gateway/opus-4.6` | `vercel-ai-gateway/anthropic/claude-opus-4-6`  
  
## 高度な設定

デーモンプロセス用の環境変数

OpenClaw Gateway がデーモン（launchd/systemd）として実行される場合は、`AI_GATEWAY_API_KEY` がそのプロセスで利用可能であることを確認してください。

プロバイダーのルーティング

Vercel AI Gateway は、モデル参照のプレフィックスに基づいてリクエストを上流プロバイダーへルーティングします。たとえば、`vercel-ai-gateway/anthropic/claude-opus-4.6` は Anthropic 経由でルーティングされ、`vercel-ai-gateway/openai/gpt-5.5` は OpenAI 経由で、`vercel-ai-gateway/moonshotai/kimi-k2.6` は MoonshotAI 経由でルーティングされます。単一の `AI_GATEWAY_API_KEY` が、すべての上流プロバイダーの認証を処理します。

思考レベル

`/think` オプションは、OpenClaw が上流プロバイダーの契約を把握している場合、信頼された上流モデルプレフィックスに従います。`vercel-ai-gateway/anthropic/...` は、Claude 4.6 モデル向けの適応的なデフォルトを含む Claude 思考プロファイルを使用します。`vercel-ai-gateway/openai/gpt-5.4`、`gpt-5.5`、および Codex スタイルの参照は、直接の OpenAI/OpenAI Codex プロバイダーと同様に `/think xhigh` を公開します。その他の名前空間付き参照は、カタログメタデータで追加が宣言されていない限り、通常の推論レベルを維持します。

## 関連

[**モデル選択** プロバイダー、モデル参照、フェイルオーバー動作の選択。 ](</ja-JP/concepts/model-providers>) [**トラブルシューティング** 一般的なトラブルシューティングと FAQ。 ](</ja-JP/help/troubleshooting>)

Was this useful?YesNo