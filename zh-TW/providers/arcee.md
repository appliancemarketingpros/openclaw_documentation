---
title: Arcee AI
source_url: https://docs.openclaw.ai/zh-TW/providers/arcee
scraped_at: 2026-05-25
---

[Arcee AI](<https://arcee.ai>) 透過與 OpenAI 相容的 API，提供 Trinity 系列 mixture-of-experts 模型的存取。所有 Trinity 模型皆採 Apache 2.0 授權。

Arcee AI 模型可透過 Arcee 平台直接存取，或透過 [OpenRouter](</zh-TW/providers/openrouter>) 存取。

屬性 | 值  
---|---  
Provider | `arcee`  
Auth | `ARCEEAI_API_KEY`（直接）或 `OPENROUTER_API_KEY`（透過 OpenRouter）  
API | 與 OpenAI 相容  
Base URL | `https://api.arcee.ai/api/v1`（直接）或 `https://openrouter.ai/api/v1`（OpenRouter）  
  
## 開始使用

### 直接（Arcee 平台）

* ### 取得 API 金鑰

在 [Arcee AI](<https://chat.arcee.ai/>) 建立 API 金鑰。

* ### 執行 onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice arceeai-api-key
[/code]

* ### 設定預設模型

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "arcee/trinity-large-thinking" },    },  },}
[/code]

### 透過 OpenRouter

* ### 取得 API 金鑰

在 [OpenRouter](<https://openrouter.ai/keys>) 建立 API 金鑰。

* ### 執行 onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice arceeai-openrouter
[/code]

* ### 設定預設模型

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "arcee/trinity-large-thinking" },    },  },}
[/code]

相同的模型 ref 適用於直接與 OpenRouter 設定（例如 `arcee/trinity-large-thinking`）。

## 非互動式設定

### 直接（Arcee 平台）

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice arceeai-api-key \  --arceeai-api-key "$ARCEEAI_API_KEY"
[/code]

### 透過 OpenRouter

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice arceeai-openrouter \  --openrouter-api-key "$OPENROUTER_API_KEY"
[/code]

## 內建目錄

OpenClaw 目前隨附此 Arcee 目錄：

模型 ref | 名稱 | 輸入 | 上下文 | 成本（每 100 萬輸入/輸出） | 備註  
---|---|---|---|---|---  
`arcee/trinity-large-thinking` | Trinity Large Thinking | text | 256K | $0.25 / $0.90 | 預設模型；已啟用推理  
`arcee/trinity-large-preview` | Trinity Large Preview | text | 128K | $0.25 / $1.00 | 通用；400B 參數，13B active  
`arcee/trinity-mini` | Trinity Mini 26B | text | 128K | $0.045 / $0.15 | 快速且符合成本效益；函式呼叫  
  
## 支援的功能

功能 | 支援  
---|---  
串流 | 是  
工具使用 / 函式呼叫 | 是（Trinity Mini、Trinity Large Preview）  
結構化輸出（JSON 模式與 JSON schema） | 是  
擴展思考 | 是（Trinity Large Thinking；工具已停用）  
  
環境注意事項

如果 Gateway 以 daemon（launchd/systemd）形式執行，請確認 `ARCEEAI_API_KEY` （或 `OPENROUTER_API_KEY`）可供該程序使用（例如，在 `~/.openclaw/.env` 中，或透過 `env.shellEnv`）。

OpenRouter 路由

透過 OpenRouter 使用 Arcee 模型時，適用相同的 `arcee/*` 模型 ref。 OpenClaw 會根據你的驗證選擇透明處理路由。請參閱 [OpenRouter provider 文件](</zh-TW/providers/openrouter>)，了解 OpenRouter 專屬 設定詳細資訊。

## 相關

[**OpenRouter** 使用單一 API 金鑰存取 Arcee 模型與許多其他模型。 ](</zh-TW/providers/openrouter>) [**模型選擇** 選擇 providers、模型 refs 與容錯移轉行為。 ](</zh-TW/concepts/model-providers>)

Was this useful?YesNo