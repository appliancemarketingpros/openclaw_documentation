---
title: Fal
source_url: https://docs.openclaw.ai/ja-JP/providers/fal
scraped_at: 2026-05-25
---

OpenClaw には、ホスト型の画像および動画生成用の同梱 `fal` プロバイダーが付属しています。

プロパティ | 値  
---|---  
プロバイダー | `fal`  
認証 | `FAL_KEY`（標準。`FAL_API_KEY` もフォールバックとして機能）  
API | fal モデルエンドポイント  
  
## はじめに

* ### Set the API key

bashCopy code
[code]
    openclaw onboard --auth-choice fal-api-key
[/code]

* ### Set a default image model

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "fal/fal-ai/flux/dev",      },    },  },}
[/code]

## 画像生成

同梱の `fal` 画像生成プロバイダーのデフォルトは `fal/fal-ai/flux/dev` です。

機能 | 値  
---|---  
最大画像数 | リクエストあたり 4  
編集モード | Flux: 参照画像 1 枚、GPT Image 2: 10、Nano Banana 2: 14  
サイズ上書き | サポート  
アスペクト比 | 生成、および GPT Image 2/Nano Banana 2 編集でサポート  
解像度 | サポート  
出力形式 | `png` または `jpeg`  
  
PNG 出力が必要な場合は `outputFormat: "png"` を使用します。fal は OpenClaw で 明示的な透明背景制御を宣言していないため、fal モデルでは `background: "transparent"` は無視された上書きとして報告されます。

fal をデフォルトの画像プロバイダーとして使用するには:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "fal/fal-ai/flux/dev",      },    },  },}
[/code]

## 動画生成

同梱の `fal` 動画生成プロバイダーのデフォルトは `fal/fal-ai/minimax/video-01-live` です。

機能 | 値  
---|---  
モード | テキストから動画、単一画像参照、Seedance 参照から動画  
ランタイム | 長時間実行ジョブ向けのキューベースの送信/ステータス/結果フロー  
  
Available video models

**HeyGen video-agent:**

  * `fal/fal-ai/heygen/v2/video-agent`


**Seedance 2.0:**

  * `fal/bytedance/seedance-2.0/fast/text-to-video`
  * `fal/bytedance/seedance-2.0/fast/image-to-video`
  * `fal/bytedance/seedance-2.0/fast/reference-to-video`
  * `fal/bytedance/seedance-2.0/text-to-video`
  * `fal/bytedance/seedance-2.0/image-to-video`
  * `fal/bytedance/seedance-2.0/reference-to-video`

Seedance 2.0 config example json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "fal/bytedance/seedance-2.0/fast/text-to-video",      },    },  },}
[/code]

Seedance 2.0 reference-to-video config example json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "fal/bytedance/seedance-2.0/fast/reference-to-video",      },    },  },}
[/code]

Reference-to-video は、共有の `video_generate` の `images`、`videos`、`audioRefs` パラメーターを通じて、最大 9 個の画像、3 個の動画、3 個の音声参照を受け付け、 参照ファイルは合計で最大 12 個です。

HeyGen video-agent config example json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "fal/fal-ai/heygen/v2/video-agent",      },    },  },}
[/code]

## 関連

[**Image generation** 共有画像ツールのパラメーターとプロバイダー選択。 ](</ja-JP/tools/image-generation>) [**Video generation** 共有動画ツールのパラメーターとプロバイダー選択。 ](</ja-JP/tools/video-generation>) [**Configuration reference** 画像および動画モデルの選択を含むエージェントデフォルト。 ](</ja-JP/gateway/config-agents#agent-defaults>)

Was this useful?YesNo