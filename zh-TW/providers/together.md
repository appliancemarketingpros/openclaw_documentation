---
title: Together AI
source_url: https://docs.openclaw.ai/zh-TW/providers/together
scraped_at: 2026-05-25
---

[Together AI](<https://together.ai>) 透過統一的 API 提供對 Llama、DeepSeek、Kimi 等領先開放原始碼模型的存取。

屬性 | 值  
---|---  
提供者 | `together`  
驗證 | `TOGETHER_API_KEY`  
API | OpenAI 相容  
基底 URL | `https://api.together.xyz/v1`  
  
## 開始使用

* ### Get an API key

在 [api.together.ai/settings/api-keys](<https://api.together.ai/settings/api-keys>) 建立 API 金鑰。

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice together-api-key
[/code]

* ### Set a default model

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "together/moonshotai/Kimi-K2.5" },    },  },}
[/code]

### 非互動式範例

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice together-api-key \  --together-api-key "$TOGETHER_API_KEY"
[/code]

## 內建型錄

OpenClaw 隨附此 Together 型錄：

模型參照 | 名稱 | 輸入 | 上下文 | 備註  
---|---|---|---|---  
`together/moonshotai/Kimi-K2.5` | Kimi K2.5 | 文字、圖片 | 262,144 | 預設模型；已啟用推理  
`together/zai-org/GLM-4.7` | GLM 4.7 Fp8 | 文字 | 202,752 | 通用文字模型  
`together/meta-llama/Llama-3.3-70B-Instruct-Turbo` | Llama 3.3 70B Instruct Turbo | 文字 | 131,072 | 快速指令模型  
`together/meta-llama/Llama-4-Scout-17B-16E-Instruct` | Llama 4 Scout 17B 16E Instruct | 文字、圖片 | 10,000,000 | 多模態  
`together/meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8` | Llama 4 Maverick 17B 128E Instruct FP8 | 文字、圖片 | 20,000,000 | 多模態  
`together/deepseek-ai/DeepSeek-V3.1` | DeepSeek V3.1 | 文字 | 131,072 | 通用文字模型  
`together/deepseek-ai/DeepSeek-R1` | DeepSeek R1 | 文字 | 131,072 | 推理模型  
`together/moonshotai/Kimi-K2-Instruct-0905` | Kimi K2-Instruct 0905 | 文字 | 262,144 | 次要 Kimi 文字模型  
  
## 影片生成

隨附的 `together` Plugin 也透過共用的 `video_generate` 工具註冊影片生成。

屬性 | 值  
---|---  
預設影片模型 | `together/Wan-AI/Wan2.2-T2V-A14B`  
模式 | 文字轉影片、單一圖片參照  
支援的參數 | `aspectRatio`, `resolution`  
  
若要將 Together 作為預設影片提供者：

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "together/Wan-AI/Wan2.2-T2V-A14B",      },    },  },}
[/code]

Environment note

如果 Gateway 以常駐程式（launchd/systemd）執行，請確保 `TOGETHER_API_KEY` 可供該程序使用（例如，在 `~/.openclaw/.env` 中或透過 `env.shellEnv`）。

Troubleshooting

  * 驗證你的金鑰可用：`openclaw models list --provider together`
  * 如果模型沒有出現，請確認 API 金鑰已在 Gateway 程序的正確環境中設定。
  * 模型參照使用 `together/<model-id>` 形式。


## 相關

[**Model selection** 提供者規則、模型參照和容錯移轉行為。 ](</zh-TW/concepts/model-providers>) [**Video generation** 共用影片生成工具參數和提供者選擇。 ](</zh-TW/tools/video-generation>) [**Configuration reference** 完整設定結構描述，包含提供者設定。 ](</zh-TW/gateway/configuration-reference>) [**Together AI** Together AI 儀表板、API 文件和定價。 ](<https://together.ai>)

Was this useful?YesNo