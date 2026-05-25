---
title: NVIDIA
source_url: https://docs.openclaw.ai/ja-JP/providers/nvidia
scraped_at: 2026-05-25
---

NVIDIA は、オープンモデルを無料で利用できる OpenAI 互換 API を `https://integrate.api.nvidia.com/v1` で提供しています。[build.nvidia.com](<https://build.nvidia.com/settings/api-keys>) の API キーで認証します。

## はじめに

* ### API キーを取得する

[build.nvidia.com](<https://build.nvidia.com/settings/api-keys>) で API キーを作成します。

* ### キーをエクスポートしてオンボーディングを実行する

bashCopy code
[code]
    export NVIDIA_API_KEY="nvapi-..."openclaw onboard --auth-choice nvidia-api-key
[/code]

* ### NVIDIA モデルを設定する

bashCopy code
[code]
    openclaw models set nvidia/nvidia/nemotron-3-super-120b-a12b
[/code]

非対話型セットアップでは、キーを直接渡すこともできます。

bashCopy code
[code]
    openclaw onboard --auth-choice nvidia-api-key --nvidia-api-key "nvapi-..."
[/code]

## 設定例

json5Copy code
[code]
    {  env: { NVIDIA_API_KEY: "nvapi-..." },  models: {    providers: {      nvidia: {        baseUrl: "https://integrate.api.nvidia.com/v1",        api: "openai-completions",      },    },  },  agents: {    defaults: {      model: { primary: "nvidia/nvidia/nemotron-3-super-120b-a12b" },    },  },}
[/code]

## 組み込みカタログ

モデル参照 | 名前 | コンテキスト | 最大出力  
---|---|---|---  
`nvidia/nvidia/nemotron-3-super-120b-a12b` | NVIDIA Nemotron 3 Super 120B | 262,144 | 8,192  
`nvidia/moonshotai/kimi-k2.5` | Kimi K2.5 | 262,144 | 8,192  
`nvidia/minimaxai/minimax-m2.5` | Minimax M2.5 | 196,608 | 8,192  
`nvidia/z-ai/glm5` | GLM 5 | 202,752 | 8,192  
  
## 高度な設定

自動有効化の動作

`NVIDIA_API_KEY` 環境変数が設定されている場合、プロバイダーは自動的に有効になります。 キー以外に明示的なプロバイダー設定は不要です。

カタログと料金

同梱カタログは静的です。NVIDIA は現在、掲載モデルの API アクセスを無料で提供しているため、ソース内のコストはデフォルトで `0` です。

OpenAI 互換エンドポイント

NVIDIA は標準の `/v1` completions エンドポイントを使用します。OpenAI 互換のツールは、NVIDIA のベース URL でそのまま動作するはずです。

カスタムプロバイダーの応答が遅い場合

NVIDIA がホストする一部のカスタムモデルは、最初の応答チャンクを送出するまでに、デフォルトのモデルアイドル監視時間より長くかかる場合があります。カスタム NVIDIA プロバイダーエントリでは、エージェント全体のランタイムタイムアウトを引き上げるのではなく、プロバイダーのタイムアウトを引き上げてください。

json5Copy code
[code]
    {  models: {    providers: {      "custom-integrate-api-nvidia-com": {        baseUrl: "https://integrate.api.nvidia.com/v1",        api: "openai-completions",        apiKey: "NVIDIA_API_KEY",        timeoutSeconds: 300,      },    },  },  agents: {    defaults: {      models: {        "custom-integrate-api-nvidia-com/meta/llama-3.1-70b-instruct": {          params: { thinking: "off" },        },      },    },  },}
[/code]

## 関連

[**モデル選択** プロバイダー、モデル参照、フェイルオーバー動作の選択。 ](</ja-JP/concepts/model-providers>) [**設定リファレンス** エージェント、モデル、プロバイダーの完全な設定リファレンス。 ](</ja-JP/gateway/configuration-reference>)

Was this useful?YesNo