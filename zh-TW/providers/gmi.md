---
title: GMI Cloud
source_url: https://docs.openclaw.ai/zh-TW/providers/gmi
scraped_at: 2026-06-29
---

ModelsProviders

GMI Cloud 是一個託管推論平台，支援前沿與開放權重模型，並提供 OpenAI 相容的 API。OpenClaw 中，它是官方外部供應商外掛，這表示你只需安裝一次，使用供應商 ID `gmi` 選取它，透過一般模型驗證儲存憑證，並使用像 `gmi/google/gemini-3.1-flash-lite` 這樣的模型參照。

當你想用一組 API 金鑰存取多個託管模型家族時，請使用 GMI，包括 GMI 型錄公開的 Google、Anthropic、OpenAI、DeepSeek、Moonshot 和 Z.AI 路由。它適合作為模型備援的次要供應商、用於比較不同供應商的託管路由，或在 GMI 比你的主要供應商更早提供某個模型時使用。

此供應商使用 OpenAI 相容的聊天語意。OpenClaw 擁有供應商 ID、驗證設定檔、別名、模型型錄種子和基底 URL；GMI 擁有即時模型可用性、計費、速率限制，以及任何供應商端路由政策。

## 設定

安裝外掛、重新啟動閘道，然後在 GMI Cloud 建立 API 金鑰：

bashCopy code
[code]
    openclaw plugins install @openclaw/gmi-provideropenclaw gateway restart
[/code]

然後執行：

bashCopy code
[code]
    openclaw onboard --auth-choice gmi-api-key
[/code]

或設定：

bashCopy code
[code]
    export GMI_API_KEY="<your-gmi-api-key>" # pragma: allowlist secret
[/code]

## 預設值

  * 供應商：`gmi`
  * 別名：`gmi-cloud`、`gmicloud`
  * 基底 URL：`https://api.gmi-serving.com/v1`
  * 環境變數：`GMI_API_KEY`
  * 預設模型：`gmi/google/gemini-3.1-flash-lite`


## 何時選擇 GMI

  * 你想要託管的 OpenAI 相容端點，而不是本機模型伺服器。
  * 你想透過一個供應商帳戶試用多個商用與開放權重模型家族。
  * 你想要一個備援供應商，其上游路由不同於 OpenRouter、DeepInfra、Together 或直接的供應商 API。
  * 你需要 GMI 特定的模型 ID、定價或帳戶控制。


當你需要 GMI 未透過其 OpenAI 相容路由公開的供應商原生功能時，請改選直接的供應商供應者。當資料在地性或本機 GPU 控制比託管便利性更重要時，請選擇 Ollama、LM Studio、vLLM 或 SGLang 等本機供應商。

## 模型

外掛型錄會預先加入常見可用的 GMI Cloud 路由 ID，包括：

  * `gmi/zai-org/GLM-5.1-FP8`
  * `gmi/deepseek-ai/DeepSeek-V3.2`
  * `gmi/moonshotai/Kimi-K2.5`
  * `gmi/google/gemini-3.1-flash-lite`
  * `gmi/anthropic/claude-sonnet-4.6`
  * `gmi/openai/gpt-5.4`


此型錄是種子，不保證每個帳戶在任何時候都能呼叫每個模型。使用 OpenClaw 的模型列出命令，查看已設定供應商在你的環境中回報的內容：

bashCopy code
[code]
    openclaw models list --provider gmi
[/code]

## 疑難排解

  * `401` 或 `403`：檢查執行 OpenClaw 的程序是否已設定 `GMI_API_KEY`，或重新執行入門設定，將金鑰儲存在供應商驗證設定檔中。
  * 未知模型錯誤：確認該模型存在於你的 GMI 帳戶中，並使用 `openclaw models list --provider gmi` 顯示的完整 `gmi/<route-id>` 參照。
  * 間歇性供應商錯誤：嘗試不同的 GMI 路由，或將 GMI 設定為備援，而不是唯一的主要模型供應商。


## 相關

  * [模型供應商](</zh-TW/concepts/model-providers>)
  * [所有供應商](</zh-TW/providers>)


Was this useful?YesNo

Open issue