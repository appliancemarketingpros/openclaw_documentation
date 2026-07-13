---
title: LongCat
source_url: https://docs.openclaw.ai/ja-JP/providers/longcat
scraped_at: 2026-07-13
---

ModelsProviders

[LongCat](<https://longcat.ai>) は、コーディングおよびエージェント型ワークロード向けに構築された推論モデル LongCat-2.0 のホステッド API を提供します。OpenClaw は、LongCat の OpenAI 互換エンドポイント用の公式 `longcat` Plugin を提供します。

プロパティ | 値  
---|---  
プロバイダー | `longcat`  
認証 | `LONGCAT_API_KEY`  
API | OpenAI 互換 Chat Completions  
ベース URL | `https://api.longcat.chat/openai`  
モデル | `longcat/LongCat-2.0`  
コンテキスト | 1,048,576 トークン  
最大出力 | 131,072 トークン  
入力 | テキスト  
  
## Plugin をインストールする

公式パッケージをインストールしてから、Gateway を再起動します。

bashCopy code
[code]
    openclaw plugins install @openclaw/longcat-provideropenclaw gateway restart
[/code]

## はじめに

* ### API キーを作成する

[LongCat API プラットフォーム](<https://longcat.chat/platform/>)にサインインし、 [API Keys](<https://longcat.chat/platform/api_keys>)ページでキーを作成します。

* ### オンボーディングを実行する

bashCopy code
[code]
    openclaw onboard --auth-choice longcat-api-key
[/code]

* ### モデルを確認する

bashCopy code
[code]
    openclaw models list --provider longcat
[/code]

プライマリモデルがまだ設定されていない場合、オンボーディングによってホステッドカタログが追加され、`longcat/LongCat-2.0` が選択されます。

### 非対話型セットアップ

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice longcat-api-key \  --longcat-api-key "$LONGCAT_API_KEY"
[/code]

## 推論の動作

LongCat は、思考の有効・無効を切り替える制御を公開しています。OpenClaw は、有効な思考レベルを `thinking: { type: "enabled" }` に、`/think off` を `thinking: { type: "disabled" }` にマッピングします。LongCat は現在 `reasoning_effort` を文書化していないため、OpenClaw はこれを送信しません。

LongCat は推論を `reasoning_content` で返します。OpenClaw は、アシスタントのツール呼び出しターンを再生するときにこのフィールドを保持するため、複数ターンのエージェントセッションでもプロバイダーが想定するメッセージ形式が維持されます。

## 料金

組み込みカタログでは、LongCat の従量課金制の定価を 100 万トークンあたりの米ドル価格として使用します。キャッシュされていない入力は $0.75、キャッシュ済み入力は $0.015、出力は $2.95 です。LongCat が一時的な割引を提供する場合があります。最新の正確な情報については、[料金ページ](<https://longcat.chat/platform/docs/Pricing/LongCat-2.0.html>)および請求記録を参照してください。

## セルフホスト型 LongCat-2.0

`longcat` プロバイダーは LongCat のホステッド API を対象としています。[Hugging Face](<https://huggingface.co/meituan-longcat/LongCat-2.0>) のオープンウェイトを使用する場合は、OpenAI 互換ランタイムを通じてモデルを提供し、代わりに OpenClaw の既存の [vLLM](</ja-JP/providers/vllm>) または [SGLang](</ja-JP/providers/sglang>) プロバイダーを使用してください。

セルフホスト型プロバイダーカタログには、ランタイムの正確なモデル識別子を保持してください。ローカルデプロイを `longcat/LongCat-2.0` 経由でルーティングしないでください。

## トラブルシューティング

シェルではキーが機能するが、Gateway では機能しない

デーモン管理の Gateway プロセスは、対話型シェルのすべての変数を継承するわけではありません。`LONGCAT_API_KEY` を `~/.openclaw/.env` に配置するか、オンボーディングを通じて設定するか、承認済みのシークレット参照を使用してください。

リクエストが 402 または 429 で失敗する

`402` は、アカウントのトークンクォータが不足していることを意味します。`429` は、API キーがレート制限に達したことを意味します。[LongCat の使用状況](<https://longcat.chat/platform/usage>)を確認し、プロバイダーのバックオフ期間が経過してからレート制限されたリクエストを再試行してください。

モデルが表示されない

`openclaw plugins list` を実行して `longcat` Plugin が有効になっていることを確認し、その後 `openclaw models list --provider longcat` を実行してください。

## 関連項目

[**モデルプロバイダー** プロバイダーの設定、モデル参照、フェイルオーバーの動作。 ](</ja-JP/concepts/model-providers>) [**LongCat API ドキュメント** ホステッド API のエンドポイント、認証、制限、使用例。 ](<https://longcat.chat/platform/docs/>) [**LongCat-2.0 モデルカード** アーキテクチャ、デプロイガイダンス、モデルの詳細。 ](<https://huggingface.co/meituan-longcat/LongCat-2.0>) [**シークレット** プロバイダーの認証情報を設定に平文で埋め込まずに保存します。 ](</ja-JP/gateway/secrets>)

Was this useful?YesNo

Open issue