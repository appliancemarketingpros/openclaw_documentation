---
title: ComfyUI
source_url: https://docs.openclaw.ai/zh-TW/providers/comfy
scraped_at: 2026-05-25
---

OpenClaw 內建隨附 `comfy` Plugin，用於以工作流程驅動的 ComfyUI 執行。此 Plugin 完全以工作流程驅動，因此 OpenClaw 不會嘗試將通用的 `size`、`aspectRatio`、`resolution`、`durationSeconds` 或 TTS 風格控制項對應到你的圖形。

屬性 | 詳細資訊  
---|---  
提供者 | `comfy`  
模型 | `comfy/workflow`  
共用介面 | `image_generate`, `video_generate`, `music_generate`  
驗證 | 本機 ComfyUI 不需要；Comfy Cloud 使用 `COMFY_API_KEY` 或 `COMFY_CLOUD_API_KEY`  
API | ComfyUI `/prompt` / `/history` / `/view` 和 Comfy Cloud `/api/*`  
  
## 支援內容

  * 從工作流程 JSON 產生圖片
  * 使用 1 張已上傳參考圖片編輯圖片
  * 從工作流程 JSON 產生影片
  * 使用 1 張已上傳參考圖片產生影片
  * 透過共用的 `music_generate` 工具產生音樂或音訊
  * 從已設定的節點或所有相符的輸出節點下載輸出


## 開始使用

選擇在自己的機器上執行 ComfyUI，或使用 Comfy Cloud。

### 本機

**最適合：** 在你的機器或 LAN 上執行自己的 ComfyUI 執行個體。

* ### 在本機啟動 ComfyUI

確認你的本機 ComfyUI 執行個體正在執行（預設為 `http://127.0.0.1:8188`）。

* ### 準備你的工作流程 JSON

匯出或建立 ComfyUI 工作流程 JSON 檔案。記下提示輸入節點和你希望 OpenClaw 讀取的輸出節點的節點 ID。

* ### 設定提供者

設定 `mode: "local"` 並指向你的工作流程檔案。以下是最小圖片範例：

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          mode: "local",          baseUrl: "http://127.0.0.1:8188",          image: {            workflowPath: "./workflows/flux-api.json",            promptNodeId: "6",            outputNodeId: "9",          },        },      },    },  },}
[/code]

* ### 設定預設模型

將 OpenClaw 指向你已設定能力的 `comfy/workflow` 模型：

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "comfy/workflow",      },    },  },}
[/code]

* ### 驗證

bashCopy code
[code]
    openclaw models list --provider comfy
[/code]

### Comfy Cloud

**最適合：** 不管理本機 GPU 資源，直接在 Comfy Cloud 上執行工作流程。

* ### 取得 API 金鑰

在 [comfy.org](<https://comfy.org>) 註冊，並從你的帳戶儀表板產生 API 金鑰。

* ### 設定 API 金鑰

透過以下其中一種方法提供你的金鑰：

bashCopy code
[code]
    # Environment variable (preferred)export COMFY_API_KEY="your-key" # Alternative environment variableexport COMFY_CLOUD_API_KEY="your-key" # Or inline in configopenclaw config set plugins.entries.comfy.config.apiKey "your-key"
[/code]

* ### 準備你的工作流程 JSON

匯出或建立 ComfyUI 工作流程 JSON 檔案。記下提示輸入節點和輸出節點的節點 ID。

* ### 設定提供者

設定 `mode: "cloud"` 並指向你的工作流程檔案：

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          mode: "cloud",          image: {            workflowPath: "./workflows/flux-api.json",            promptNodeId: "6",            outputNodeId: "9",          },        },      },    },  },}
[/code]

* ### 設定預設模型

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "comfy/workflow",      },    },  },}
[/code]

* ### 驗證

bashCopy code
[code]
    openclaw models list --provider comfy
[/code]

## 設定

Comfy 支援共用頂層連線設定，以及依能力區分的工作流程區段（`image`、`video`、`music`）：

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          mode: "local",          baseUrl: "http://127.0.0.1:8188",          image: {            workflowPath: "./workflows/flux-api.json",            promptNodeId: "6",            outputNodeId: "9",          },          video: {            workflowPath: "./workflows/video-api.json",            promptNodeId: "12",            outputNodeId: "21",          },          music: {            workflowPath: "./workflows/music-api.json",            promptNodeId: "3",            outputNodeId: "18",          },        },      },    },  },}
[/code]

### 共用鍵

鍵 | 類型 | 說明  
---|---|---  
`mode` | `"local"` 或 `"cloud"` | 連線模式。  
`baseUrl` | 字串 | 本機預設為 `http://127.0.0.1:8188`，雲端預設為 `https://cloud.comfy.org`。  
`apiKey` | 字串 | 選用的行內金鑰，可替代 `COMFY_API_KEY` / `COMFY_CLOUD_API_KEY` 環境變數。  
`allowPrivateNetwork` | 布林值 | 允許在雲端模式中使用私人/LAN `baseUrl`。  
  
### 各能力鍵

這些鍵適用於 `image`、`video` 或 `music` 區段內：

鍵 | 必填 | 預設 | 說明  
---|---|---|---  
`workflow` 或 `workflowPath` | 是 | \-- | ComfyUI 工作流程 JSON 檔案的路徑。  
`promptNodeId` | 是 | \-- | 接收文字提示的節點 ID。  
`promptInputName` | 否 | `"text"` | 提示節點上的輸入名稱。  
`outputNodeId` | 否 | \-- | 要讀取輸出的節點 ID。若省略，會使用所有相符的輸出節點。  
`pollIntervalMs` | 否 | \-- | 作業完成的輪詢間隔，單位為毫秒。  
`timeoutMs` | 否 | \-- | 工作流程執行的逾時時間，單位為毫秒。  
  
`image` 和 `video` 區段也支援：

鍵 | 必填 | 預設 | 說明  
---|---|---|---  
`inputImageNodeId` | 是（傳入參考圖片時） | \-- | 接收已上傳參考圖片的節點 ID。  
`inputImageInputName` | 否 | `"image"` | 圖片節點上的輸入名稱。  
  
## 工作流程詳細資訊

圖片工作流程

將預設圖片模型設定為 `comfy/workflow`：

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "comfy/workflow",      },    },  },}
[/code]

**參考圖片編輯範例：**

若要啟用使用已上傳參考圖片的圖片編輯，請將 `inputImageNodeId` 加入你的圖片設定：

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          image: {            workflowPath: "./workflows/edit-api.json",            promptNodeId: "6",            inputImageNodeId: "7",            inputImageInputName: "image",            outputNodeId: "9",          },        },      },    },  },}
[/code]

影片工作流程

將預設影片模型設定為 `comfy/workflow`：

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "comfy/workflow",      },    },  },}
[/code]

Comfy 影片工作流程透過已設定的圖形支援文字轉影片和圖片轉影片。

音樂工作流程

內建 Plugin 會為工作流程定義的音訊或音樂輸出註冊音樂產生提供者，並透過共用的 `music_generate` 工具公開：

textCopy code
[code]
    /tool music_generate prompt="Warm ambient synth loop with soft tape texture"
[/code]

使用 `music` 設定區段指向你的音訊工作流程 JSON 和輸出節點。

向後相容性

現有的頂層圖片設定（沒有巢狀 `image` 區段）仍可使用：

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          workflowPath: "./workflows/flux-api.json",          promptNodeId: "6",          outputNodeId: "9",        },      },    },  },}
[/code]

OpenClaw 會將該舊版形狀視為圖片工作流程設定。你不需要立即遷移，但建議新設定使用巢狀 `image` / `video` / `music` 區段。

即時測試

內建 Plugin 有選擇加入的即時覆蓋範圍：

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 COMFY_LIVE_TEST=1 pnpm test:live -- extensions/comfy/comfy.live.test.ts
[/code]

除非已設定相符的 Comfy 工作流程區段，否則即時測試會略過個別圖片、影片或音樂案例。

## 相關內容

[**圖像生成** 圖像生成工具設定與用法。 ](</zh-TW/tools/image-generation>) [**影片生成** 影片生成工具設定與用法。 ](</zh-TW/tools/video-generation>) [**音樂生成** 音樂與音訊生成工具設定。 ](</zh-TW/tools/music-generation>) [**提供者目錄** 所有提供者與模型參照的概覽。 ](</zh-TW/providers>) [**設定參考** 完整設定參考，包含代理預設值。 ](</zh-TW/gateway/config-agents#agent-defaults>)

Was this useful?YesNo