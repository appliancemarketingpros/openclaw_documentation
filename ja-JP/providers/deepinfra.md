---
title: DeepInfra
source_url: https://docs.openclaw.ai/ja-JP/providers/deepinfra
scraped_at: 2026-05-25
---

DeepInfra は、単一のエンドポイントと API キーの背後で、最も人気のあるオープンソースモデルと最先端モデルにリクエストをルーティングする **統合 API** を提供します。OpenAI 互換なので、ほとんどの OpenAI SDK はベース URL を切り替えるだけで動作します。

## API キーの取得

  1. <https://deepinfra.com/> にアクセスする
  2. サインインするかアカウントを作成する
  3. Dashboard / Keys に移動し、新しい API キーを生成するか、自動作成されたものを使用する


## CLI セットアップ

bashCopy code
[code]
    openclaw onboard --deepinfra-api-key <key>
[/code]

または環境変数を設定します。

bashCopy code
[code]
    export DEEPINFRA_API_KEY="<your-deepinfra-api-key>" # pragma: allowlist secret
[/code]

## 設定スニペット

json5Copy code
[code]
    {  env: { DEEPINFRA_API_KEY: "<your-deepinfra-api-key>" }, // pragma: allowlist secret  agents: {    defaults: {      model: { primary: "deepinfra/deepseek-ai/DeepSeek-V3.2" },    },  },}
[/code]

## サポートされている OpenClaw サーフェス

バンドルされた Plugin は、現在の OpenClaw プロバイダー契約に一致するすべての DeepInfra サーフェスを登録します。

サーフェス | デフォルトモデル | OpenClaw 設定/ツール  
---|---|---  
チャット / モデルプロバイダー | `deepseek-ai/DeepSeek-V3.2` | `agents.defaults.model`  
画像生成/編集 | `black-forest-labs/FLUX-1-schnell` | `image_generate`, `agents.defaults.imageGenerationModel`  
メディア理解 | 画像用 `moonshotai/Kimi-K2.5` | 受信画像の理解  
音声テキスト変換 | `openai/whisper-large-v3-turbo` | 受信音声の文字起こし  
テキスト音声変換 | `hexgrad/Kokoro-82M` | `messages.tts.provider: "deepinfra"`  
動画生成 | `Pixverse/Pixverse-T2V` | `video_generate`, `agents.defaults.videoGenerationModel`  
メモリエンベディング | `BAAI/bge-m3` | `agents.defaults.memorySearch.provider: "deepinfra"`  
  
DeepInfra は、リランキング、分類、物体検出、その他のネイティブモデルタイプも公開しています。OpenClaw には現在、これらのカテゴリに対する第一級のプロバイダー契約がないため、この Plugin はまだそれらを登録していません。

## 利用可能なモデル

OpenClaw は起動時に利用可能な DeepInfra モデルを動的に検出します。利用可能なモデルの完全な一覧を表示するには、`/models deepinfra` を使用します。

[DeepInfra.com](<https://deepinfra.com/>) で利用可能な任意のモデルは、`deepinfra/` プレフィックス付きで使用できます。

CodeCopy code
[code]
    deepinfra/MiniMaxAI/MiniMax-M2.5deepinfra/deepseek-ai/DeepSeek-V3.2deepinfra/moonshotai/Kimi-K2.5deepinfra/zai-org/GLM-5.1...and many more
[/code]

## 注記

  * モデル参照は `deepinfra/<provider>/<model>` です（例: `deepinfra/Qwen/Qwen3-Max`）。
  * デフォルトモデル: `deepinfra/deepseek-ai/DeepSeek-V3.2`
  * ベース URL: `https://api.deepinfra.com/v1/openai`
  * ネイティブ動画生成は `https://api.deepinfra.com/v1/inference/<model>` を使用します。


## 関連

  * [モデルプロバイダー](</ja-JP/concepts/model-providers>)
  * [すべてのプロバイダー](</ja-JP/providers>)


Was this useful?YesNo