---
title: OpenCode
source_url: https://docs.openclaw.ai/zh-TW/providers/opencode
scraped_at: 2026-05-25
---

OpenCode 在 OpenClaw 中公開兩個託管目錄：

目錄 | 前綴 | 執行階段提供者  
---|---|---  
**Zen** | `opencode/...` | `opencode`  
**Go** | `opencode-go/...` | `opencode-go`  
  
兩個目錄都使用相同的 OpenCode API 金鑰。OpenClaw 將執行階段提供者 ID 分開保留，讓上游的逐模型路由維持正確，但入門設定和文件會將它們視為 同一個 OpenCode 設定。

## 開始使用

### Zen catalog

**最適合：** 精選的 OpenCode 多模型代理（Claude、GPT、Gemini）。

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice opencode-zen
[/code]

或直接傳入金鑰：

bashCopy code
[code]
    openclaw onboard --opencode-zen-api-key "$OPENCODE_API_KEY"
[/code]

* ### Set a Zen model as the default

bashCopy code
[code]
    openclaw config set agents.defaults.model.primary "opencode/claude-opus-4-6"
[/code]

* ### Verify models are available

bashCopy code
[code]
    openclaw models list --provider opencode
[/code]

### Go catalog

**最適合：** OpenCode 託管的 Kimi、GLM 和 MiniMax 系列。

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice opencode-go
[/code]

或直接傳入金鑰：

bashCopy code
[code]
    openclaw onboard --opencode-go-api-key "$OPENCODE_API_KEY"
[/code]

* ### Set a Go model as the default

bashCopy code
[code]
    openclaw config set agents.defaults.model.primary "opencode-go/kimi-k2.6"
[/code]

* ### Verify models are available

bashCopy code
[code]
    openclaw models list --provider opencode-go
[/code]

## 設定範例

json5Copy code
[code]
    {  env: { OPENCODE_API_KEY: "sk-..." },  agents: { defaults: { model: { primary: "opencode/claude-opus-4-6" } } },}
[/code]

## 內建目錄

### Zen

屬性 | 值  
---|---  
執行階段提供者 | `opencode`  
範例模型 | `opencode/claude-opus-4-6`, `opencode/gpt-5.5`, `opencode/gemini-3-pro`  
  
### Go

屬性 | 值  
---|---  
執行階段提供者 | `opencode-go`  
範例模型 | `opencode-go/kimi-k2.6`, `opencode-go/glm-5`, `opencode-go/minimax-m2.5`  
  
## 進階設定

API key aliases

`OPENCODE_ZEN_API_KEY` 也支援作為 `OPENCODE_API_KEY` 的別名。

Shared credentials

在設定期間輸入一組 OpenCode 金鑰，會同時儲存兩個執行階段 提供者的憑證。你不需要分別為每個目錄執行入門設定。

Billing and dashboard

你會登入 OpenCode、新增帳務詳細資料，並複製你的 API 金鑰。帳務 與目錄可用性由 OpenCode 儀表板管理。

Gemini replay behavior

Gemini 支援的 OpenCode 參照會留在 proxy-Gemini 路徑上，因此 OpenClaw 會在 那裡保留 Gemini 思考簽章清理，而不啟用原生 Gemini 重播驗證或啟動重寫。

Non-Gemini replay behavior

非 Gemini 的 OpenCode 參照會保留最小的 OpenAI 相容重播政策。

## 相關

[**Model selection** 選擇提供者、模型參照和容錯移轉行為。 ](</zh-TW/concepts/model-providers>) [**Configuration reference** 代理程式、模型和提供者的完整設定參考。 ](</zh-TW/gateway/configuration-reference>)

Was this useful?YesNo