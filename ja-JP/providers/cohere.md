---
title: Cohere
source_url: https://docs.openclaw.ai/ja-JP/providers/cohere
scraped_at: 2026-06-29
---

ModelsProviders

[Cohere](<https://cohere.com>) は、Compatibility API を通じて OpenAI 互換の推論を提供します。OpenClaw は外部化移行中に Cohere プロバイダーを同梱し、Command A モデルカタログを備えた公式の外部 Plugin としても公開しています。

プロパティ | 値  
---|---  
プロバイダー ID | `cohere`  
Plugin | 移行中は同梱、公式の外部パッケージ  
認証 env var | `COHERE_API_KEY`  
オンボーディングフラグ | `--auth-choice cohere-api-key`  
直接 CLI フラグ | `--cohere-api-key <key>`  
API | OpenAI 互換 (`openai-completions`)  
ベース URL | `https://api.cohere.ai/compatibility/v1`  
デフォルトモデル | `cohere/command-a-03-2025`  
  
## はじめる

  1. Cohere は現在の OpenClaw パッケージに含まれています。利用できない場合は、外部パッケージをインストールして Gateway を再起動します。

bashCopy code
[code]
    openclaw plugins install @openclaw/cohere-provideropenclaw gateway restart
[/code]

  2. Cohere API キーを作成します。
  3. オンボーディングを実行します。

bashCopy code
[code]
    openclaw onboard --non-interactive \  --auth-choice cohere-api-key \  --cohere-api-key "$COHERE_API_KEY"
[/code]

  4. カタログが利用可能であることを確認します。

bashCopy code
[code]
    openclaw models list --provider cohere
[/code]

デフォルトモデルは、プライマリモデルがまだ設定されていない場合にのみ設定されます。

## 環境変数のみのセットアップ

`COHERE_API_KEY` を Gateway プロセスで利用可能にしてから、Cohere モデルを選択します。

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "cohere/command-a-03-2025" },    },  },}
[/code]

## 関連

  * [モデルプロバイダー](</ja-JP/concepts/model-providers>)
  * [モデル CLI](</ja-JP/cli/models>)
  * [プロバイダーディレクトリ](</ja-JP/providers>)


Was this useful?YesNo

Open issue