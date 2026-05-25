---
title: DeepInfra
source_url: https://docs.openclaw.ai/zh-TW/providers/deepinfra
scraped_at: 2026-05-25
---

DeepInfra 提供一個**統一 API** ，可將請求路由到最受歡迎的開源與前沿模型，並透過單一端點和 API 金鑰使用。它與 OpenAI 相容，因此多數 OpenAI SDK 只要切換基底 URL 即可運作。

## 取得 API 金鑰

  1. 前往 <https://deepinfra.com/>
  2. 登入或建立帳號
  3. 導覽至 Dashboard / Keys，產生新的 API 金鑰，或使用自動建立的金鑰


## CLI 設定

bashCopy code
[code]
    openclaw onboard --deepinfra-api-key <key>
[/code]

或設定環境變數：

bashCopy code
[code]
    export DEEPINFRA_API_KEY="<your-deepinfra-api-key>" # pragma: allowlist secret
[/code]

## Config 片段

json5Copy code
[code]
    {  env: { DEEPINFRA_API_KEY: "<your-deepinfra-api-key>" }, // pragma: allowlist secret  agents: {    defaults: {      model: { primary: "deepinfra/deepseek-ai/DeepSeek-V3.2" },    },  },}
[/code]

## 支援的 OpenClaw 介面

隨附的 Plugin 會註冊所有符合目前 OpenClaw 供應商合約的 DeepInfra 介面：

介面 | 預設模型 | OpenClaw 設定/工具  
---|---|---  
聊天 / 模型供應商 | `deepseek-ai/DeepSeek-V3.2` | `agents.defaults.model`  
圖片生成/編輯 | `black-forest-labs/FLUX-1-schnell` | `image_generate`, `agents.defaults.imageGenerationModel`  
媒體理解 | `moonshotai/Kimi-K2.5` for images | 傳入圖片理解  
語音轉文字 | `openai/whisper-large-v3-turbo` | 傳入音訊轉錄  
文字轉語音 | `hexgrad/Kokoro-82M` | `messages.tts.provider: "deepinfra"`  
影片生成 | `Pixverse/Pixverse-T2V` | `video_generate`, `agents.defaults.videoGenerationModel`  
記憶嵌入 | `BAAI/bge-m3` | `agents.defaults.memorySearch.provider: "deepinfra"`  
  
DeepInfra 也公開重排序、分類、物件偵測，以及其他原生模型類型。OpenClaw 目前尚未為這些類別提供一級供應商合約，因此此 Plugin 尚未註冊它們。

## 可用模型

OpenClaw 會在啟動時動態探索可用的 DeepInfra 模型。使用 `/models deepinfra` 查看完整的可用模型清單。

[DeepInfra.com](<https://deepinfra.com/>) 上任何可用模型都可以搭配 `deepinfra/` 前綴使用：

CodeCopy code
[code]
    deepinfra/MiniMaxAI/MiniMax-M2.5deepinfra/deepseek-ai/DeepSeek-V3.2deepinfra/moonshotai/Kimi-K2.5deepinfra/zai-org/GLM-5.1...and many more
[/code]

## 注意事項

  * 模型參照為 `deepinfra/<provider>/<model>`（例如 `deepinfra/Qwen/Qwen3-Max`）。
  * 預設模型：`deepinfra/deepseek-ai/DeepSeek-V3.2`
  * 基底 URL：`https://api.deepinfra.com/v1/openai`
  * 原生影片生成使用 `https://api.deepinfra.com/v1/inference/<model>`。


## 相關

  * [模型供應商](</zh-TW/concepts/model-providers>)
  * [所有供應商](</zh-TW/providers>)


Was this useful?YesNo