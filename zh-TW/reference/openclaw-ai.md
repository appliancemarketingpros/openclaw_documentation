---
title: @openclaw/ai 套件
source_url: https://docs.openclaw.ai/zh-TW/reference/openclaw-ai
scraped_at: 2026-07-06
---

ReferenceTechnical reference

`@openclaw/ai` 是 OpenClaw 模型執行層的可發布函式庫形式：供應商中立的訊息/工具/串流合約、驗證、診斷、事件串流、隔離的執行階段登錄，以及八個內建 API 系列的惰性配接器（Anthropic Messages、OpenAI Completions、OpenAI Responses、Azure OpenAI Responses、ChatGPT/Codex Responses、Google Generative AI、Google Vertex、Mistral Conversations）。

它會在每次發布時與根 `openclaw` 套件一同發布，並釘選到相同版本，且有自己的 `npm-shrinkwrap.json`，因此其遞移相依性樹會在安裝時鎖定。安裝 `openclaw` 會自動安裝相符的 `@openclaw/ai`；函式庫使用者可以直接相依於它，而不需要任何 OpenClaw 應用程式程式碼。

## 快速開始

jsCopy code
[code]
      const runtime = createLlmRuntime();registerBuiltInApiProviders(runtime.registry); const stream = runtime.streamSimple(model, { messages }, { apiKey });for await (const event of stream) {  if (event.type === "text_delta") process.stdout.write(event.delta);}const result = await stream.result();
[/code]

可執行版本位於儲存庫的 `examples/ai-chat`。

## 設計合約

  * **預設按實例限定範圍。** 匯入套件不會在全域註冊任何內容。`createApiRegistry()` / `createLlmRuntime()` 會回傳隔離的實例；`registerBuiltInApiProviders(registry)` 會選擇性地讓某個登錄使用內建傳輸。供應商 SDK 模組會在第一次使用時惰性載入。
  * **主機政策是注入的，而非內建綁定。** 請求 fetch 防護（例如 SSRF 政策）、工具結果重播文字的祕密遮蔽、OpenAI 嚴格工具預設值，以及診斷記錄，都是透過 `configureAiTransportHost` 設定的 `AiTransportHost` 連接埠。函式庫預設值是惰性的；OpenClaw 會在其串流 facade 中安裝實際實作。
  * **單一事件串流身分。** `@openclaw/ai/event-stream` 是 OpenClaw 核心、agent-core 和外部使用者共用的標準 `EventStream` 建構函式。
  * **`internal/*` 子路徑不是 API。** 它們存在於 OpenClaw 應用程式本身，不提供 semver 保證。
  * 供應商 ID、憑證、模型目錄、重試和容錯移轉仍屬於應用程式關注事項。OpenClaw 會在此套件周圍分層處理這些內容；函式庫使用者則直接提供 `Model` 物件和選項。


## 子路徑匯出

子路徑 | 內容  
---|---  
`.` | 合約、`createApiRegistry`、`createLlmRuntime`、`configureAiTransportHost`  
`./providers` | `registerBuiltInApiProviders`、`resetApiProviders`  
`./types` | 模型/訊息/工具/串流類型  
`./validation` | 工具引數驗證  
`./diagnostics` | 診斷合約  
`./event-stream` | 共用的 `EventStream` 實作  
`./internal/*` | OpenClaw 內部使用，不提供 semver 保證  
  
Was this useful?YesNo

Open issue