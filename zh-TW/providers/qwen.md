---
title: Qwen
source_url: https://docs.openclaw.ai/zh-TW/providers/qwen
scraped_at: 2026-05-25
---

OpenClaw 現在將 Qwen 視為具有標準 id `qwen` 的第一級內建 provider。內建 provider 以 Qwen Cloud / Alibaba DashScope 和 Coding Plan 端點為目標，並保留舊版 `modelstudio` id 作為相容性別名繼續運作。

  * Provider：`qwen`
  * 偏好的環境變數：`QWEN_API_KEY`
  * 為了相容性也接受：`MODELSTUDIO_API_KEY`、`DASHSCOPE_API_KEY`
  * API 風格：與 OpenAI 相容


## 開始使用

選擇你的方案類型並依照設定步驟操作。

### Coding Plan (subscription)

**最適合：** 透過 Qwen Coding Plan 取得訂閱制存取權。

* ### Get your API key

從 [home.qwencloud.com/api-keys](<https://home.qwencloud.com/api-keys>) 建立或複製 API key。

* ### Run onboarding

若使用 **Global** 端點：

bashCopy code
[code]
    openclaw onboard --auth-choice qwen-api-key
[/code]

若使用 **China** 端點：

bashCopy code
[code]
    openclaw onboard --auth-choice qwen-api-key-cn
[/code]

* ### Set a default model

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "qwen/qwen3.5-plus" },    },  },}
[/code]

* ### Verify the model is available

bashCopy code
[code]
    openclaw models list --provider qwen
[/code]

### Standard (pay-as-you-go)

**最適合：** 透過 Standard Model Studio 端點取得隨用隨付存取權，包括可能無法在 Coding Plan 使用的 `qwen3.6-plus` 等模型。

* ### Get your API key

從 [home.qwencloud.com/api-keys](<https://home.qwencloud.com/api-keys>) 建立或複製 API key。

* ### Run onboarding

若使用 **Global** 端點：

bashCopy code
[code]
    openclaw onboard --auth-choice qwen-standard-api-key
[/code]

若使用 **China** 端點：

bashCopy code
[code]
    openclaw onboard --auth-choice qwen-standard-api-key-cn
[/code]

* ### Set a default model

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "qwen/qwen3.5-plus" },    },  },}
[/code]

* ### Verify the model is available

bashCopy code
[code]
    openclaw models list --provider qwen
[/code]

## 方案類型與端點

方案 | 區域 | Auth choice | 端點  
---|---|---|---  
標準（隨用隨付） | China | `qwen-standard-api-key-cn` | `dashscope.aliyuncs.com/compatible-mode/v1`  
標準（隨用隨付） | Global | `qwen-standard-api-key` | `dashscope-intl.aliyuncs.com/compatible-mode/v1`  
Coding Plan（訂閱） | China | `qwen-api-key-cn` | `coding.dashscope.aliyuncs.com/v1`  
Coding Plan（訂閱） | Global | `qwen-api-key` | `coding-intl.dashscope.aliyuncs.com/v1`  
  
Provider 會根據你的 auth choice 自動選擇端點。標準 choice 使用 `qwen-*` 系列；`modelstudio-*` 僅保留為相容用途。 你可以在設定中使用自訂 `baseUrl` 覆寫。

## 內建型錄

OpenClaw 目前隨附此內建 Qwen 型錄。設定的型錄會感知端點： Coding Plan 設定會省略已知僅能在 Standard 端點上運作的模型。

Model ref | 輸入 | Context | 備註  
---|---|---|---  
`qwen/qwen3.5-plus` | text, image | 1,000,000 | 預設模型  
`qwen/qwen3.6-plus` | text, image | 1,000,000 | 需要此模型時，優先使用 Standard 端點  
`qwen/qwen3-max-2026-01-23` | text | 262,144 | Qwen Max 系列  
`qwen/qwen3-coder-next` | text | 262,144 | Coding  
`qwen/qwen3-coder-plus` | text | 1,000,000 | Coding  
`qwen/MiniMax-M2.5` | text | 1,000,000 | 已啟用推理  
`qwen/glm-5` | text | 202,752 | GLM  
`qwen/glm-4.7` | text | 202,752 | GLM  
`qwen/kimi-k2.5` | text, image | 262,144 | 透過 Alibaba 使用 Moonshot AI  
  
## Thinking 控制

對於已啟用推理的 Qwen Cloud 模型，內建 provider 會將 OpenClaw thinking 等級對應到 DashScope 的頂層 `enable_thinking` 請求旗標。停用 thinking 會傳送 `enable_thinking: false`；其他 thinking 等級會傳送 `enable_thinking: true`。

## 多模態附加功能

`qwen` Plugin 也在 **Standard** DashScope 端點上公開多模態能力（不是 Coding Plan 端點）：

  * 透過 `qwen-vl-max-latest` 進行**影片理解**
  * 透過 `wan2.6-t2v`（預設）、`wan2.6-i2v`、`wan2.6-r2v`、`wan2.6-r2v-flash`、`wan2.7-r2v` 進行 **Wan 影片生成**


若要將 Qwen 用作預設影片提供者：

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: { primary: "qwen/wan2.6-t2v" },    },  },}
[/code]

## 進階設定

Image and video understanding

內建的 Qwen Plugin 會在 **Standard** DashScope 端點（不是 Coding Plan 端點） 上註冊圖片與影片的媒體理解能力。

屬性 | 值  
---|---  
模型 | `qwen-vl-max-latest`  
支援的輸入 | 圖片、影片  
  
媒體理解會從已設定的 Qwen 驗證自動解析，無需額外設定。請確保你使用的是 Standard（隨用隨付）端點， 以支援媒體理解。

Qwen 3.6 Plus availability

`qwen3.6-plus` 可在 Standard（隨用隨付）Model Studio 端點上使用：

  * 中國：`dashscope.aliyuncs.com/compatible-mode/v1`
  * 全球：`dashscope-intl.aliyuncs.com/compatible-mode/v1`


如果 Coding Plan 端點對 `qwen3.6-plus` 傳回「不支援的模型」錯誤，請改用 Standard（隨用隨付）， 而不是 Coding Plan 端點/金鑰組。

OpenClaw 的內建 Qwen 目錄不會在 Coding Plan 端點上公開 `qwen3.6-plus`，但在 `models.providers.qwen.models` 下明確設定的 `qwen/qwen3.6-plus` 項目，會在 Coding Plan baseUrls 上受到遵循， 因此若阿里雲在你的訂閱中啟用該模型，你可以選擇加入。上游 API 仍會決定呼叫是否成功。

Capability plan

`qwen` Plugin 正被定位為完整 Qwen Cloud 介面的供應商歸屬，而不只是程式碼/文字模型。

  * **文字/聊天模型：** 目前已內建
  * **工具呼叫、結構化輸出、思考：** 繼承自 OpenAI 相容傳輸
  * **圖片生成：** 規劃在提供者 Plugin 層實作
  * **圖片/影片理解：** 目前已在 Standard 端點內建
  * **語音/音訊：** 規劃在提供者 Plugin 層實作
  * **記憶體嵌入/重新排序：** 規劃透過嵌入介面提供
  * **影片生成：** 目前已透過共用影片生成能力內建

Video generation details

對於影片生成，OpenClaw 會先將設定的 Qwen 區域對應到相符的 DashScope AIGC 主機，再提交工作：

  * 全球/國際：`https://dashscope-intl.aliyuncs.com`
  * 中國：`https://dashscope.aliyuncs.com`


這表示一般指向 Coding Plan 或 Standard Qwen 主機的 `models.providers.qwen.baseUrl`， 仍會讓影片生成使用正確的區域性 DashScope 影片端點。

目前內建的 Qwen 影片生成限制：

  * 每次請求最多 **1** 支輸出影片
  * 最多 **1** 張輸入圖片
  * 最多 **4** 支輸入影片
  * 最長 **10 秒** 時長
  * 支援 `size`、`aspectRatio`、`resolution`、`audio` 和 `watermark`
  * 參考圖片/影片模式目前需要**遠端 http(s) URL** 。本機檔案路徑會預先遭到拒絕，因為 DashScope 影片端點不接受針對這些參考上傳的本機緩衝區。

Streaming usage compatibility

原生 Model Studio 端點會在共用的 `openai-completions` 傳輸上公開串流用量相容性。OpenClaw 現在會根據端點能力判定， 因此以相同原生主機為目標的 DashScope 相容自訂提供者 ID，會繼承相同的串流用量行為， 而不需要特別使用內建的 `qwen` 提供者 ID。

原生串流用量相容性同時適用於 Coding Plan 主機與 Standard DashScope 相容主機：

  * `https://coding.dashscope.aliyuncs.com/v1`
  * `https://coding-intl.dashscope.aliyuncs.com/v1`
  * `https://dashscope.aliyuncs.com/compatible-mode/v1`
  * `https://dashscope-intl.aliyuncs.com/compatible-mode/v1`

Multimodal endpoint regions

多模態介面（影片理解與 Wan 影片生成）使用 **Standard** DashScope 端點，而不是 Coding Plan 端點：

  * 全球/國際 Standard base URL：`https://dashscope-intl.aliyuncs.com/compatible-mode/v1`
  * 中國 Standard base URL：`https://dashscope.aliyuncs.com/compatible-mode/v1`

環境與常駐程式設定

如果 Gateway 以常駐程式（launchd/systemd）執行，請確保該行程可以使用 `QWEN_API_KEY` （例如，在 `~/.openclaw/.env` 中，或透過 `env.shellEnv`）。

## 相關內容

[**模型選擇** 選擇供應商、模型參照，以及容錯移轉行為。 ](</zh-TW/concepts/model-providers>) [**影片生成** 共用的影片工具參數與供應商選擇。 ](</zh-TW/tools/video-generation>) [**Alibaba (ModelStudio)** 舊版 ModelStudio 供應商與遷移注意事項。 ](</zh-TW/providers/alibaba>) [**疑難排解** 一般疑難排解與常見問題。 ](</zh-TW/help/troubleshooting>)

Was this useful?YesNo