---
title: 建置 CLI 後端 Plugin
source_url: https://docs.openclaw.ai/zh-TW/plugins/cli-backend-plugins
scraped_at: 2026-05-25
---

CLI 後端 Plugin 可讓 OpenClaw 呼叫本機 AI CLI 作為文字推論後端。此後端會以提供者前置詞出現在模型參照中：

textCopy code
[code]
    acme-cli/acme-large
[/code]

當上游整合已經公開為本機命令、CLI 擁有本機登入狀態，或當 API 提供者無法使用時 CLI 可作為有用的備援，就使用 CLI 後端。

## Plugin 擁有的內容

CLI 後端 Plugin 有三個合約：

合約 | 檔案 | 用途  
---|---|---  
套件進入點 | `package.json` | 將 OpenClaw 指向 Plugin 執行階段模組  
Manifest 擁有權 | `openclaw.plugin.json` | 在執行階段載入前宣告後端 id  
執行階段註冊 | `index.ts` | 使用命令預設值呼叫 `api.registerCliBackend(...)`  
  
Manifest 是探索中繼資料。它不會執行 CLI，也不會註冊執行階段行為。當 Plugin 進入點呼叫 `api.registerCliBackend(...)` 時，執行階段行為才會開始。

## 最小後端 Plugin

* ### 建立套件中繼資料

package.jsonCopy code
[code]
    {  "name": "@acme/openclaw-acme-cli",  "version": "1.0.0",  "type": "module",  "openclaw": {    "extensions": ["./index.ts"],    "compat": {      "pluginApi": ">=2026.3.24-beta.2",      "minGatewayVersion": "2026.3.24-beta.2"    },    "build": {      "openclawVersion": "2026.3.24-beta.2",      "pluginSdkVersion": "2026.3.24-beta.2"    }  },  "dependencies": {    "openclaw": "^2026.3.24"  },  "devDependencies": {    "typescript": "^5.9.0"  }}
[/code]

發布的套件必須包含已建置的 JavaScript 執行階段檔案。如果你的來源進入點是 `./src/index.ts`，請新增指向已建置 JavaScript 對應檔案的 `openclaw.runtimeExtensions`。請參閱[進入點](</zh-TW/plugins/sdk-entrypoints>)。

* ### 宣告後端擁有權

openclaw.plugin.jsonCopy code
[code]
    {  "id": "acme-cli",  "name": "Acme CLI",  "description": "Run Acme's local AI CLI through OpenClaw",  "cliBackends": ["acme-cli"],  "setup": {    "cliBackends": ["acme-cli"],    "requiresRuntime": false  },  "activation": {    "onStartup": false  },  "configSchema": {    "type": "object",    "additionalProperties": false  }}
[/code]

`cliBackends` 是執行階段擁有權清單。當設定或模型選擇提到 `acme-cli/...` 時，它可讓 OpenClaw 自動載入 Plugin。

`setup.cliBackends` 是描述器優先的設定介面。當模型探索、初始設定或狀態應該在不載入 Plugin 執行階段的情況下識別後端時，請加入它。只有在這些靜態描述器已足以完成設定時，才使用 `requiresRuntime: false`。

* ### 註冊後端

index.tsCopy code
[code]
    import { definePluginEntry } from "openclaw/plugin-sdk/plugin-entry";import {  CLI_FRESH_WATCHDOG_DEFAULTS,  CLI_RESUME_WATCHDOG_DEFAULTS,  type CliBackendPlugin,} from "openclaw/plugin-sdk/cli-backend"; function buildAcmeCliBackend(): CliBackendPlugin {  return {    id: "acme-cli",    liveTest: {      defaultModelRef: "acme-cli/acme-large",      defaultImageProbe: false,      defaultMcpProbe: false,      docker: {        npmPackage: "@acme/acme-cli",        binaryName: "acme",      },    },    config: {      command: "acme",      args: ["chat", "--json"],      output: "json",      input: "stdin",      modelArg: "--model",      sessionArg: "--session",      sessionMode: "existing",      sessionIdFields: ["session_id", "conversation_id"],      systemPromptFileArg: "--system-file",      systemPromptWhen: "first",      imageArg: "--image",      imageMode: "repeat",      reliability: {        watchdog: {          fresh: { ...CLI_FRESH_WATCHDOG_DEFAULTS },          resume: { ...CLI_RESUME_WATCHDOG_DEFAULTS },        },      },      serialize: true,    },  };} export default definePluginEntry({  id: "acme-cli",  name: "Acme CLI",  description: "Run Acme's local AI CLI through OpenClaw",  register(api) {    api.registerCliBackend(buildAcmeCliBackend());  },});
[/code]

後端 id 必須與 Manifest 的 `cliBackends` 項目相符。已註冊的 `config` 只是預設值；執行階段會將 `agents.defaults.cliBackends.acme-cli` 底下的使用者設定合併覆蓋在其上。

## 設定形狀

`CliBackendConfig` 描述 OpenClaw 應如何啟動與剖析 CLI：

欄位 | 用法  
---|---  
`command` | 二進位名稱或絕對命令路徑  
`args` | 全新執行的基礎 argv  
`resumeArgs` | 已恢復工作階段的替代 argv；支援 `{sessionId}`  
`output` / `resumeOutput` | 剖析器：`json`、`jsonl` 或 `text`  
`input` | 提示傳輸：`arg` 或 `stdin`  
`modelArg` | 模型 id 前使用的旗標  
`modelAliases` | 將 OpenClaw 模型 id 對應到 CLI 原生 id  
`sessionArg` / `sessionArgs` | 如何傳遞工作階段 id  
`sessionMode` | `always`、`existing` 或 `none`  
`sessionIdFields` | OpenClaw 從 CLI 輸出讀取的 JSON 欄位  
`systemPromptArg` / `systemPromptFileArg` | 系統提示傳輸  
`systemPromptWhen` | `first`、`always` 或 `never`  
`imageArg` / `imageMode` | 圖片路徑支援  
`serialize` | 保持同一後端的執行順序  
`reliability.watchdog` | 無輸出逾時調校  
  
偏好使用符合 CLI 的最小靜態設定。只有在行為確實屬於該後端時，才加入 Plugin 回呼。

## 進階後端 Hook

`CliBackendPlugin` 也可以定義：

Hook | 用法  
---|---  
`normalizeConfig(config, context)` | 合併後重寫舊版使用者設定  
`resolveExecutionArgs(ctx)` | 加入請求範圍的旗標，例如思考強度  
`prepareExecution(ctx)` | 啟動前建立臨時驗證或設定橋接  
`transformSystemPrompt(ctx)` | 套用最後的 CLI 專屬系統提示轉換  
`textTransforms` | 雙向提示與輸出替換  
`defaultAuthProfileId` | 偏好特定的 OpenClaw 驗證設定檔  
`authEpochMode` | 決定驗證變更如何使已儲存的 CLI 工作階段失效  
`nativeToolMode` | 宣告 CLI 是否有永遠啟用的原生工具  
`bundleMcp` / `bundleMcpMode` | 選擇加入 OpenClaw 的 loopback MCP 工具橋接  
  
讓這些 Hook 由提供者擁有。當後端 Hook 能表達該行為時，不要把 CLI 專屬分支加入核心。

## MCP 工具橋接

CLI 後端預設不會接收 OpenClaw 工具。如果 CLI 可以使用 MCP 設定，請明確選擇加入：

typescriptCopy code
[code]
    return {  id: "acme-cli",  bundleMcp: true,  bundleMcpMode: "codex-config-overrides",  config: {    command: "acme",    args: ["chat", "--json"],    output: "json",  },};
[/code]

支援的橋接模式如下：

模式 | 用法  
---|---  
`claude-config-file` | 接受 MCP 設定檔的 CLI  
`codex-config-overrides` | 接受 argv 上設定覆蓋的 CLI  
`gemini-system-settings` | 從系統設定目錄讀取 MCP 設定的 CLI  
  
只有在 CLI 確實能使用橋接時才啟用。如果 CLI 有無法停用的內建工具層，請設定 `nativeToolMode: "always-on"`，讓 OpenClaw 在呼叫端要求沒有原生工具時能封閉式失敗。

## 使用者設定

使用者可以覆蓋任何後端預設值：

json5Copy code
[code]
    {  agents: {    defaults: {      cliBackends: {        "acme-cli": {          command: "/opt/acme/bin/acme",          args: ["chat", "--json", "--profile", "work"],          modelAliases: {            large: "acme-large-2026",          },        },      },      model: {        primary: "openai/gpt-5.5",        fallbacks: ["acme-cli/large"],      },    },  },}
[/code]

記錄使用者可能需要的最小覆蓋。通常只有在二進位檔位於 `PATH` 之外時，才需要 `command`。

## 驗證

對於內建 Plugin，請針對建構器與設定註冊新增聚焦測試，然後執行該 Plugin 的目標測試路徑：

bashCopy code
[code]
    pnpm test extensions/acme-cli
[/code]

對於本機或已安裝的 Plugin，請驗證探索以及一次真實模型執行：

bashCopy code
[code]
    openclaw plugins inspect acme-cli --runtime --jsonopenclaw agent --message "reply exactly: backend ok" --model acme-cli/acme-large
[/code]

如果後端支援圖片或 MCP，請新增能用真實 CLI 證明這些路徑的 live smoke。不要只依賴靜態檢查來驗證提示、圖片、MCP 或工作階段恢復行為。

## 檢查清單

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s `package.json` 對發布套件包含 `openclaw.extensions` 和已建置的執行階段進入點 OPENCLAW_DOCS_MARKER:calloutClose:

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s `openclaw.plugin.json` 宣告 `cliBackends` 和有意設定的 `activation.onStartup` OPENCLAW_DOCS_MARKER:calloutClose:

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s 當設定或模型探索應在冷啟動時看到後端，存在 `setup.cliBackends` OPENCLAW_DOCS_MARKER:calloutClose:

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s `api.registerCliBackend(...)` 使用與 Manifest 相同的後端 id OPENCLAW_DOCS_MARKER:calloutClose:

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s `agents.defaults.cliBackends.<id>` 底下的使用者覆蓋仍然優先 OPENCLAW_DOCS_MARKER:calloutClose:

Was this useful?YesNo