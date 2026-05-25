---
title: Kilo Gateway
source_url: https://docs.openclaw.ai/zh-TW/providers/kilocode
scraped_at: 2026-05-25
---

Kilo Gateway 提供一個**統一 API** ，可透過單一端點與 API 金鑰，將請求路由到多個模型。它相容於 OpenAI，因此大多數 OpenAI SDK 只要切換 base URL 即可運作。

屬性 | 值  
---|---  
提供者 | `kilocode`  
驗證 | `KILOCODE_API_KEY`  
API | 相容於 OpenAI  
Base URL | `https://api.kilo.ai/api/gateway/`  
  
## 開始使用

* ### 建立帳戶

前往 [app.kilo.ai](<https://app.kilo.ai>)，登入或建立帳戶，然後導覽至 API Keys 並產生新的金鑰。

* ### 執行 onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice kilocode-api-key
[/code]

或直接設定環境變數：

bashCopy code
[code]
    export KILOCODE_API_KEY="<your-kilocode-api-key>" # pragma: allowlist secret
[/code]

* ### 確認模型可用

bashCopy code
[code]
    openclaw models list --provider kilocode
[/code]

## 預設模型

預設模型是 `kilocode/kilo/auto`，這是由提供者擁有並由 Kilo Gateway 管理的智慧路由模型。

## 內建目錄

OpenClaw 會在啟動時從 Kilo Gateway 動態探索可用模型。使用 `/models kilocode` 查看你的帳戶可用的完整模型清單。

Gateway 上可用的任何模型都可以搭配 `kilocode/` 前綴使用：

模型 ref | 備註  
---|---  
`kilocode/kilo/auto` | 預設 — 智慧路由  
`kilocode/anthropic/claude-sonnet-4` | 透過 Kilo 使用 Anthropic  
`kilocode/openai/gpt-5.5` | 透過 Kilo 使用 OpenAI  
`kilocode/google/gemini-3.1-pro-preview` | 透過 Kilo 使用 Google  
...以及更多 | 使用 `/models kilocode` 列出全部  
  
## 設定範例

json5Copy code
[code]
    {  env: { KILOCODE_API_KEY: "<your-kilocode-api-key>" }, // pragma: allowlist secret  agents: {    defaults: {      model: { primary: "kilocode/kilo/auto" },    },  },}
[/code]

傳輸與相容性

Kilo Gateway 在原始碼中記錄為相容於 OpenRouter，因此它會維持在 proxy 風格的 OpenAI 相容路徑，而不是使用原生 OpenAI 請求塑形。

  * Gemini 支援的 Kilo refs 會維持在 proxy-Gemini 路徑，因此 OpenClaw 會在該處保留 Gemini thought-signature 清理，而不啟用原生 Gemini replay 驗證或 bootstrap 重寫。
  * Kilo Gateway 會在底層使用帶有你的 API 金鑰的 Bearer token。

串流包裝器與 reasoning

Kilo 的共用串流包裝器會加入提供者應用程式標頭，並為支援的具體模型 refs 正規化 proxy reasoning payloads。

疑難排解

  * 如果啟動時模型探索失敗，OpenClaw 會 fallback 到包含 `kilocode/kilo/auto` 的隨附靜態目錄。
  * 確認你的 API 金鑰有效，且你的 Kilo 帳戶已啟用所需模型。
  * 當 Gateway 以 daemon 形式執行時，請確保 `KILOCODE_API_KEY` 可供該程序使用（例如在 `~/.openclaw/.env` 中，或透過 `env.shellEnv`）。


## 相關

[**模型選擇** 選擇提供者、模型 refs，以及 failover 行為。 ](</zh-TW/concepts/model-providers>) [**設定參考** 完整 OpenClaw 設定參考。 ](</zh-TW/gateway/configuration-reference>) [**Kilo Gateway** Kilo Gateway 儀表板、API 金鑰和帳戶管理。 ](<https://app.kilo.ai>)

Was this useful?YesNo