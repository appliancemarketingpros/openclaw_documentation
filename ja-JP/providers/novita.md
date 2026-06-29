---
title: NovitaAI
source_url: https://docs.openclaw.ai/ja-JP/providers/novita
scraped_at: 2026-06-29
---

ModelsProviders

NovitaAI は、OpenAI 互換モデル API を備えたホステッド AI インフラストラクチャプロバイダーです。OpenClaw ではバンドル済みモデルプロバイダーなので、プロバイダー ID は `novita`、認証情報は通常のモデル認証フローを通り、モデル参照は `novita/deepseek/deepseek-v3-0324` のような形式になります。

自前の推論サーバーを運用せずに、オープンウェイトモデルやサードパーティモデルのルートへホステッドアクセスしたい場合は Novita を使用します。バンドル済みカタログは、DeepSeek、Moonshot、MiniMax、GLM、Qwen など、Novita が公開するエージェントターンに実用的なチャットモデルのルートを中心にしています。

このプロバイダーは Novita の OpenAI 互換エンドポイントを使用します。OpenClaw はプロバイダー登録、認証、エイリアス、モデル参照の正規化、ベース URL の選択を処理します。ライブモデルの利用可否、アカウント権限、価格、レート制限は Novita が管理します。

## セットアップ

[novita.ai/settings/key-management](<https://novita.ai/settings/key-management>) で API キーを作成し、次を実行します。

bashCopy code
[code]
    openclaw onboard --auth-choice novita-api-key
[/code]

または、次を設定します。

bashCopy code
[code]
    export NOVITA_API_KEY="<your-novita-api-key>" # pragma: allowlist secret
[/code]

## デフォルト

  * プロバイダー: `novita`
  * エイリアス: `novita-ai`, `novitaai`
  * ベース URL: `https://api.novita.ai/openai/v1`
  * 環境変数: `NOVITA_API_KEY`
  * デフォルトモデル: `novita/deepseek/deepseek-v3-0324`


## Novita を選ぶ場合

  * OpenAI 互換 API でホステッドのオープンウェイトモデルアクセスが必要な場合。
  * 単一のプロバイダーアカウントを通じて、DeepSeek、Kimi、MiniMax、GLM、または Qwen ファミリーのルートを使いたい場合。
  * OpenRouter、GMI、DeepInfra、または直接のベンダー API とは別のホステッドフォールバック経路が必要な場合。
  * vLLM、SGLang、LM Studio、Ollama インフラストラクチャを保守するよりも、プロバイダー側のモデルホスティングを使いたい場合。


ベンダー固有のリクエストパラメーターやサポート契約が必要な場合は、直接のベンダープロバイダーを選びます。モデルを自前のハードウェア上、または自前のネットワーク境界の内側で実行する必要がある場合は、ローカルプロバイダーを選びます。

## モデル

バンドル済みカタログには、一般的に利用可能な NovitaAI ルート ID がシードされています。例:

  * `novita/moonshotai/kimi-k2.5`
  * `novita/minimax/minimax-m2.7`
  * `novita/zai-org/glm-5`
  * `novita/deepseek/deepseek-v3-0324`
  * `novita/deepseek/deepseek-r1-0528`
  * `novita/qwen/qwen3-235b-a22b-fp8`


このカタログは、OpenClaw のモデル選択の出発点です。アカウント、リージョン、または Novita の現在のカタログによって、ルートが追加、削除、または制限される場合があります。長期的なデフォルトを設定する前に、CLI からプロバイダーを確認してください。

bashCopy code
[code]
    openclaw models list --provider novita
[/code]

## トラブルシューティング

  * `401` または `403`: Novita のキー管理ページでキーを確認し、保存済みプロファイルが古い場合は `openclaw onboard --auth-choice novita-api-key` を再実行します。
  * 不明なモデルエラー: `openclaw models list --provider novita` が返す正確な `novita/<route-id>` を使用します。
  * 遅い、または失敗するルート: 別の Novita モデルルートを試すか、プロバイダー固有のばらつきを許容できるワークロードでは Novita をフォールバックプロバイダーとして設定します。


## 関連

  * [モデルプロバイダー](</ja-JP/concepts/model-providers>)
  * [すべてのプロバイダー](</ja-JP/providers>)


Was this useful?YesNo

Open issue