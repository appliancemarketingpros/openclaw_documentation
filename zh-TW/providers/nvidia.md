---
title: NVIDIA
source_url: https://docs.openclaw.ai/zh-TW/providers/nvidia
scraped_at: 2026-05-25
---

NVIDIA 在 `https://integrate.api.nvidia.com/v1` 提供 OpenAI 相容 API，可免費使用 開放模型。請使用來自 [build.nvidia.com](<https://build.nvidia.com/settings/api-keys>) 的 API 金鑰進行驗證。

## 開始使用

* ### Get your API key

在 [build.nvidia.com](<https://build.nvidia.com/settings/api-keys>) 建立 API 金鑰。

* ### Export the key and run onboarding

bashCopy code
[code]
    export NVIDIA_API_KEY="nvapi-..."openclaw onboard --auth-choice nvidia-api-key
[/code]

* ### Set an NVIDIA model

bashCopy code
[code]
    openclaw models set nvidia/nvidia/nemotron-3-super-120b-a12b
[/code]

對於非互動式設定，你也可以直接傳入金鑰：

bashCopy code
[code]
    openclaw onboard --auth-choice nvidia-api-key --nvidia-api-key "nvapi-..."
[/code]

## 設定範例

json5Copy code
[code]
    {  env: { NVIDIA_API_KEY: "nvapi-..." },  models: {    providers: {      nvidia: {        baseUrl: "https://integrate.api.nvidia.com/v1",        api: "openai-completions",      },    },  },  agents: {    defaults: {      model: { primary: "nvidia/nvidia/nemotron-3-super-120b-a12b" },    },  },}
[/code]

## 內建型錄

模型參照 | 名稱 | Context | 最大輸出  
---|---|---|---  
`nvidia/nvidia/nemotron-3-super-120b-a12b` | NVIDIA Nemotron 3 Super 120B | 262,144 | 8,192  
`nvidia/moonshotai/kimi-k2.5` | Kimi K2.5 | 262,144 | 8,192  
`nvidia/minimaxai/minimax-m2.5` | Minimax M2.5 | 196,608 | 8,192  
`nvidia/z-ai/glm5` | GLM 5 | 202,752 | 8,192  
  
## 進階設定

Auto-enable behavior

當設定 `NVIDIA_API_KEY` 環境變數時，提供者會自動啟用。 除了金鑰之外，不需要明確的提供者設定。

Catalog and pricing

隨附的型錄是靜態的。由於 NVIDIA 目前為列出的模型提供免費 API 存取，原始碼中的費用預設為 `0`。

OpenAI-compatible endpoint

NVIDIA 使用標準的 `/v1` completions 端點。任何 OpenAI 相容工具 都應該可以搭配 NVIDIA 基底 URL 直接運作。

Slow custom provider responses

有些由 NVIDIA 託管的自訂模型，可能會比預設模型閒置監看器更久才發出第一個回應區塊。 對於自訂 NVIDIA 提供者項目，請提高提供者逾時時間，而不是提高整個 agent 執行階段逾時時間：

json5Copy code
[code]
    {  models: {    providers: {      "custom-integrate-api-nvidia-com": {        baseUrl: "https://integrate.api.nvidia.com/v1",        api: "openai-completions",        apiKey: "NVIDIA_API_KEY",        timeoutSeconds: 300,      },    },  },  agents: {    defaults: {      models: {        "custom-integrate-api-nvidia-com/meta/llama-3.1-70b-instruct": {          params: { thinking: "off" },        },      },    },  },}
[/code]

## 相關

[**Model selection** 選擇提供者、模型參照和容錯移轉行為。 ](</zh-TW/concepts/model-providers>) [**Configuration reference** agents、模型和提供者的完整設定參考。 ](</zh-TW/gateway/configuration-reference>)

Was this useful?YesNo