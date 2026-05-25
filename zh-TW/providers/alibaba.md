---
title: 阿里巴巴模型工作室
source_url: https://docs.openclaw.ai/zh-TW/providers/alibaba
scraped_at: 2026-05-25
---

OpenClaw 隨附一個 `alibaba` Plugin，會為 Alibaba Model Studio（DashScope 的國際名稱）上的 Wan 模型註冊影片生成提供者。此 Plugin 預設啟用；你只需要設定 API 金鑰。

屬性 | 值  
---|---  
提供者 id | `alibaba`  
Plugin | 隨附，`enabledByDefault: true`  
Auth 環境變數 | `MODELSTUDIO_API_KEY` → `DASHSCOPE_API_KEY` → `QWEN_API_KEY`（第一個符合者優先）  
Onboarding 旗標 | `--auth-choice alibaba-model-studio-api-key`  
直接 CLI 旗標 | `--alibaba-model-studio-api-key <key>`  
預設模型 | `alibaba/wan2.6-t2v`  
預設基礎 URL | `https://dashscope-intl.aliyuncs.com`  
  
## 開始使用

* ### 設定 API 金鑰

使用 onboarding 將金鑰儲存到 `alibaba` 提供者：

bashCopy code
[code]
    openclaw onboard --auth-choice alibaba-model-studio-api-key
[/code]

或在安裝/onboarding 期間直接傳入金鑰：

bashCopy code
[code]
    openclaw onboard --alibaba-model-studio-api-key <your-key>
[/code]

或在啟動 Gateway 前匯出任一受支援的環境變數：

bashCopy code
[code]
    export MODELSTUDIO_API_KEY=sk-...# or DASHSCOPE_API_KEY=...# or QWEN_API_KEY=...
[/code]

* ### 設定預設影片模型

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "alibaba/wan2.6-t2v",      },    },  },}
[/code]

* ### 確認提供者已設定

bashCopy code
[code]
    openclaw models list --provider alibaba
[/code]

清單應包含全部五個隨附的 Wan 模型。如果無法解析 `MODELSTUDIO_API_KEY`，`openclaw models status --json` 會在 `auth.unusableProfiles` 下回報缺少的認證。

## 內建 Wan 模型

模型參照 | 模式  
---|---  
`alibaba/wan2.6-t2v` | 文字轉影片（預設）  
`alibaba/wan2.6-i2v` | 圖片轉影片  
`alibaba/wan2.6-r2v` | 參照轉影片  
`alibaba/wan2.6-r2v-flash` | 參照轉影片（快速）  
`alibaba/wan2.7-r2v` | 參照轉影片  
  
## 功能與限制

隨附的提供者會對應 DashScope 的 Wan 影片 API 上限。三種模式共用相同的每次請求影片數量與時長上限；只有輸入形狀不同。

模式 | 最大輸出影片數 | 最大輸入圖片數 | 最大輸入影片數 | 最長時長 | 支援的控制項  
---|---|---|---|---|---  
文字轉影片 | 1 | n/a | n/a | 10 s | `size`, `aspectRatio`, `resolution`, `audio`, `watermark`  
圖片轉影片 | 1 | 1 | n/a | 10 s | `size`, `aspectRatio`, `resolution`, `audio`, `watermark`  
參照轉影片 | 1 | n/a | 4 | 10 s | `size`, `aspectRatio`, `resolution`, `audio`, `watermark`  
  
當請求省略 `durationSeconds` 時，提供者會傳送 DashScope 接受的預設值 **5 秒** 。在[影片生成工具](</zh-TW/tools/video-generation>)上明確設定 `durationSeconds`，可延長到最多 10 s。

## 進階設定

覆寫 DashScope 基礎 URL

提供者預設使用國際 DashScope 端點。若要指定中國區域端點，請設定：

json5Copy code
[code]
    {  models: {    providers: {      alibaba: {        baseUrl: "https://dashscope.aliyuncs.com",      },    },  },}
[/code]

提供者會在建構 AIGC 任務 URL 前移除結尾斜線。

Auth 環境優先順序

OpenClaw 會依下列順序從環境變數解析 Alibaba API 金鑰，並採用第一個非空值：

  1. `MODELSTUDIO_API_KEY`
  2. `DASHSCOPE_API_KEY`
  3. `QWEN_API_KEY`


已設定的 `auth.profiles` 項目（透過 `openclaw models auth login` 設定）會覆寫環境變數解析。請參閱[模型 FAQ 中的 Auth 設定檔](</zh-TW/help/faq-models#what-is-an-auth-profile>)，了解設定檔輪換、冷卻與覆寫機制。

與 Qwen Plugin 的關係

兩個隨附 Plugin 都會與 DashScope 通訊，並接受重疊的 API 金鑰。請使用：

  * `alibaba/wan*.*` id 來驅動本頁所記錄的專用 Wan 影片提供者。
  * `qwen/*` id 用於 Qwen 聊天、嵌入與媒體理解（請參閱 [Qwen](</zh-TW/providers/qwen>)）。


只要設定一次 `MODELSTUDIO_API_KEY`，就會驗證兩個 Plugin，因為 auth 環境變數清單刻意重疊；你不需要分別 onboarding 每個 Plugin。

## 相關

[**影片生成** 共用影片工具參數與提供者選擇。 ](</zh-TW/tools/video-generation>) [**Qwen** 在相同 DashScope auth 上設定 Qwen 聊天、嵌入與媒體理解。 ](</zh-TW/providers/qwen>) [**設定參考** Agent 預設值與模型設定。 ](</zh-TW/gateway/config-agents#agent-defaults>) [**模型 FAQ** Auth 設定檔、切換模型，以及解決「no profile」錯誤。 ](</zh-TW/help/faq-models>)

Was this useful?YesNo