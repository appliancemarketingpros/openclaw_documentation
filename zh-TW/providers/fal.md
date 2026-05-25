---
title: Fal
source_url: https://docs.openclaw.ai/zh-TW/providers/fal
scraped_at: 2026-05-25
---

OpenClaw 隨附內建的 `fal` provider，用於託管式圖片與影片生成。

屬性 | 值  
---|---  
Provider | `fal`  
驗證 | `FAL_KEY`（標準；`FAL_API_KEY` 也可作為備援）  
API | fal 模型端點  
  
## 開始使用

* ### 設定 API 金鑰

bashCopy code
[code]
    openclaw onboard --auth-choice fal-api-key
[/code]

* ### 設定預設圖片模型

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "fal/fal-ai/flux/dev",      },    },  },}
[/code]

## 圖片生成

內建的 `fal` 圖片生成 provider 預設為 `fal/fal-ai/flux/dev`。

功能 | 值  
---|---  
最大圖片數 | 每個請求 4 張  
編輯模式 | Flux：1 張參考圖片；GPT Image 2：10；Nano Banana 2：14  
尺寸覆寫 | 支援  
長寬比 | 支援生成與 GPT Image 2/Nano Banana 2 編輯  
解析度 | 支援  
輸出格式 | `png` 或 `jpeg`  
  
當你想要 PNG 輸出時，請使用 `outputFormat: "png"`。fal 未在 OpenClaw 中宣告 明確的透明背景控制，因此對 fal 模型而言，`background: "transparent"` 會被回報為已忽略的覆寫。

若要使用 fal 作為預設圖片 provider：

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "fal/fal-ai/flux/dev",      },    },  },}
[/code]

## 影片生成

內建的 `fal` 影片生成 provider 預設為 `fal/fal-ai/minimax/video-01-live`。

功能 | 值  
---|---  
模式 | 文字轉影片、單張圖片參考、Seedance 參考轉影片  
執行階段 | 適用於長時間執行工作的佇列式提交/狀態/結果流程  
  
可用的影片模型

**HeyGen video-agent：**

  * `fal/fal-ai/heygen/v2/video-agent`


**Seedance 2.0：**

  * `fal/bytedance/seedance-2.0/fast/text-to-video`
  * `fal/bytedance/seedance-2.0/fast/image-to-video`
  * `fal/bytedance/seedance-2.0/fast/reference-to-video`
  * `fal/bytedance/seedance-2.0/text-to-video`
  * `fal/bytedance/seedance-2.0/image-to-video`
  * `fal/bytedance/seedance-2.0/reference-to-video`

Seedance 2.0 設定範例 json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "fal/bytedance/seedance-2.0/fast/text-to-video",      },    },  },}
[/code]

Seedance 2.0 參考轉影片設定範例 json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "fal/bytedance/seedance-2.0/fast/reference-to-video",      },    },  },}
[/code]

參考轉影片可透過共用的 `video_generate` `images`、`videos` 與 `audioRefs` 參數接受最多 9 張圖片、3 支影片與 3 個音訊參考， 總參考檔案數最多為 12 個。

HeyGen video-agent 設定範例 json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "fal/fal-ai/heygen/v2/video-agent",      },    },  },}
[/code]

## 相關

[**圖片生成** 共用圖片工具參數與 provider 選擇。 ](</zh-TW/tools/image-generation>) [**影片生成** 共用影片工具參數與 provider 選擇。 ](</zh-TW/tools/video-generation>) [**設定參考** Agent 預設值，包括圖片與影片模型選擇。 ](</zh-TW/gateway/config-agents#agent-defaults>)

Was this useful?YesNo