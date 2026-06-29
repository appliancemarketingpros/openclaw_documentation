---
title: Ollama Cloud
source_url: https://docs.openclaw.ai/ja-JP/providers/ollama-cloud
scraped_at: 2026-06-29
---

ModelsProviders

Ollama Cloud は Ollama のホスト型モデル API です。OpenClaw はローカルの Ollama サーバーをインストールしたり、ローカルの Ollama アプリをクラウドモードにサインインしたりせずに、Ollama でホストされたモデルを直接呼び出せます。プロバイダー ID `ollama-cloud` と、`ollama-cloud/kimi-k2.6` のようなモデル参照を使用します。

このページはクラウド専用ルーティング向けです。このプロバイダーは OpenAI 互換の `/v1` ルートではなく、Ollama ネイティブの `/api/chat` スタイルを使用します。OpenClaw はこれを別のプロバイダー ID として登録するため、クラウド専用の認証情報、ライブカタログ検出、モデル選択がローカルの `ollama` ホストと混在しません。

クラウド専用ルーティングが必要な場合はこのページを使用してください。ローカル Ollama、クラウドとローカルのハイブリッドルーティング、埋め込み、カスタムホストの詳細については、[Ollama](</ja-JP/providers/ollama>) を参照してください。

## セットアップ

[ollama.com/settings/keys](<https://ollama.com/settings/keys>) で Ollama Cloud API キーを作成してから、次を実行します。

bashCopy code
[code]
    openclaw onboard --auth-choice ollama-cloud
[/code]

または次を設定します。

bashCopy code
[code]
    export OLLAMA_API_KEY="<your-ollama-cloud-api-key>" # pragma: allowlist secret
[/code]

## デフォルト

  * プロバイダー: `ollama-cloud`
  * ベース URL: `https://ollama.com`
  * 環境変数: `OLLAMA_API_KEY`
  * API スタイル: Ollama ネイティブ `/api/chat`
  * サンプルモデル: `ollama-cloud/kimi-k2.6`


## Ollama Cloud を選ぶ場合

  * ローカルで `ollama serve` を実行せずに、ホスト型 Ollama モデルを使いたい。
  * OpenClaw がローカル Ollama に使用するものと同じネイティブ Ollama チャット API 形状を、`https://ollama.com` に向けて使用したい。
  * Ollama のホスト型カタログにすでにあるモデル向けに、シンプルなクラウド経路が必要。
  * ローカルモデルのプル、ローカル GPU 制御、LAN 専用推論は不要。


サインイン済み Ollama ホスト経由でローカル専用またはクラウドとローカルのルーティングを使いたい場合は、代わりに [Ollama](</ja-JP/providers/ollama>) を使用してください。`/v1/chat/completions` セマンティクスやプロバイダー固有の OpenAI スタイル機能が必要な場合は、代わりに OpenAI 互換プロバイダーを使用してください。

## モデル

OpenClaw はライブのホスト型カタログから Ollama Cloud モデルを検出します。一般的に利用可能なホスト型 ID には次のものがあります。

  * `ollama-cloud/gpt-oss:20b`
  * `ollama-cloud/kimi-k2.6`
  * `ollama-cloud/deepseek-v4-flash`
  * `ollama-cloud/minimax-m2.7`
  * `ollama-cloud/glm-5`


現在のホスト型カタログにあるモデル ID を使用します。

bashCopy code
[code]
    openclaw models list --provider ollama-cloudopenclaw models set ollama-cloud/kimi-k2.6
[/code]

モデル ID はクラウドカタログ ID であり、ローカルのプル名ではありません。あるモデル名がローカル Ollama ホストでは動作するものの、ホスト型カタログに存在しない場合は、代わりにそのローカルホストで `ollama` プロバイダーを使用してください。

## ライブテスト

Ollama Cloud API キーのスモークテストでは、Ollama ライブテストをホスト型エンドポイントに向け、現在のカタログからモデルを選択します。

bashCopy code
[code]
    export OLLAMA_API_KEY="<your-ollama-cloud-api-key>" # pragma: allowlist secret OPENCLAW_LIVE_TEST=1 \OPENCLAW_LIVE_OLLAMA=1 \OPENCLAW_LIVE_OLLAMA_BASE_URL=https://ollama.com \OPENCLAW_LIVE_OLLAMA_MODEL=kimi-k2.6 \OPENCLAW_LIVE_OLLAMA_WEB_SEARCH=1 \pnpm test:live -- extensions/ollama/ollama.live.test.ts
[/code]

クラウドスモークはテキスト、ネイティブストリーム、ウェブ検索を実行します。Ollama Cloud API キーでは `/api/embed` が許可されない場合があるため、`https://ollama.com` ではデフォルトで埋め込みをスキップします。

## トラブルシューティング

  * `Set OLLAMA_API_KEY` エラー: 実際のクラウド API キーを指定してください。ローカルの `ollama-local` マーカーは、ローカルまたはプライベートの Ollama ホスト専用です。
  * 不明なモデルのエラー: `openclaw models list --provider ollama-cloud` を実行し、ホスト型モデル ID を正確にコピーしてください。
  * カスタム Ollama ホストでのツール呼び出しまたは生 JSON の問題: OpenAI 互換の `/v1` URL を誤って使用していないか確認してください。Ollama ルートでは、`/v1` サフィックスのないネイティブのベース URL を使用する必要があります。


## 関連

  * [Ollama](</ja-JP/providers/ollama>)
  * [モデルプロバイダー](</ja-JP/concepts/model-providers>)
  * [すべてのプロバイダー](</ja-JP/providers>)


Was this useful?YesNo

Open issue