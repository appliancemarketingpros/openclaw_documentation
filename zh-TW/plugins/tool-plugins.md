---
title: 工具外掛
source_url: https://docs.openclaw.ai/zh-TW/plugins/tool-plugins
scraped_at: 2026-06-29
---

CapabilitiesBuilding plugins

工具外掛可在不新增通道、模型供應者、鉤子、服務或設定後端的情況下，為 OpenClaw 加入代理可呼叫的工具。當外掛擁有固定工具清單，且你希望 OpenClaw 產生資訊清單中繼資料，讓這些工具不需載入執行階段程式碼也能被探索時，請使用 `defineToolPlugin`。

建議流程如下：

  1. 使用 `openclaw plugins init` 建立套件骨架。
  2. 使用 `defineToolPlugin` 編寫工具。
  3. 建置 JavaScript。
  4. 使用 `openclaw plugins build` 產生 `openclaw.plugin.json` 和 `package.json` 中繼資料。
  5. 在發布或安裝前驗證產生的中繼資料。


對於供應者、通道、鉤子、服務或混合能力外掛，請改從[建置外掛](</zh-TW/plugins/building-plugins>)、[通道外掛](</zh-TW/plugins/sdk-channel-plugins>)或[供應者外掛](</zh-TW/plugins/sdk-provider-plugins>)開始。

## 需求

  * 節點 >= 22。
  * TypeScript ESM 套件輸出。
  * 用於設定和工具參數結構描述的 `typebox`。
  * `openclaw >=2026.5.17`，這是第一個匯出 `openclaw/plugin-sdk/tool-plugin` 的 OpenClaw 版本。
  * 可交付 `dist/`、`openclaw.plugin.json` 和 `package.json` 的套件根目錄。


產生的外掛會在執行階段匯入 `typebox`，因此請將 `typebox` 保留在 `dependencies` 中，而不只是 `devDependencies`。

## 快速開始

建立新的外掛套件：

bashCopy code
[code]
    openclaw plugins init stock-quotes --name "Stock Quotes"cd stock-quotesnpm installnpm run plugin:buildnpm run plugin:validatenpm test
[/code]

骨架會建立：

  * `src/index.ts`：包含 `echo` 工具的 `defineToolPlugin` 進入點。
  * `src/index.test.ts`：小型中繼資料測試。
  * `tsconfig.json`：輸出到 `dist/` 的 NodeNext TypeScript 設定。
  * `package.json`：指令碼、執行階段相依項，以及 `openclaw.extensions: ["./dist/index.js"]`。
  * `openclaw.plugin.json`：初始工具產生的資訊清單中繼資料。


預期驗證輸出：

textCopy code
[code]
    Plugin stock-quotes is valid.
[/code]

## 編寫工具

`defineToolPlugin` 接受外掛身分、選用設定結構描述，以及靜態工具清單。參數與設定型別會從 TypeBox 結構描述推斷。

typescriptCopy code
[code]
      export default defineToolPlugin({  id: "stock-quotes",  name: "Stock Quotes",  description: "Fetch stock quote snapshots.",  configSchema: Type.Object({    apiKey: Type.Optional(Type.String({ description: "Quote API key." })),    baseUrl: Type.Optional(Type.String({ description: "Quote API base URL." })),  }),  tools: (tool) => [    tool({      name: "stock_quote",      label: "Stock Quote",      description: "Fetch a stock quote snapshot.",      parameters: Type.Object({        symbol: Type.String({ description: "Ticker symbol, for example OPEN." }),      }),      async execute({ symbol }, config, context) {        context.signal?.throwIfAborted();        return {          symbol: symbol.toUpperCase(),          configured: Boolean(config.apiKey),          baseUrl: config.baseUrl ?? "https://api.example.com",        };      },    }),  ],});
[/code]

工具名稱是穩定的 API。請選擇唯一、小寫，且足夠具體的名稱，以避免與核心工具或其他外掛衝突。

## 選用工具與工廠工具

當使用者應在工具傳送給模型前明確將其加入允許清單時，請設定 `optional: true`：

typescriptCopy code
[code]
    tool({  name: "workflow_run",  description: "Run an external workflow.",  parameters: Type.Object({ goal: Type.String() }),  optional: true,  execute: ({ goal }) => ({ queued: true, goal }),});
[/code]

`openclaw plugins build` 會寫入相符的 `toolMetadata.<tool>.optional` 資訊清單項目，因此 OpenClaw 不需要載入外掛執行階段程式碼也能探索該工具。

當工具在建立前需要執行階段工具情境時，請使用 `factory`。工廠會讓中繼資料保持靜態，同時允許工具針對特定執行選擇退出、檢查沙箱狀態，或繫結執行階段輔助工具。

typescriptCopy code
[code]
    tool({  name: "local_workflow",  description: "Run a local workflow outside sandboxed sessions.",  parameters: Type.Object({ goal: Type.String() }),  optional: true,  factory({ api, toolContext }) {    if (toolContext.sandboxed) {      return null;    }    return createLocalWorkflowTool(api);  },});
[/code]

工廠仍適用於固定工具名稱。當外掛會動態計算工具名稱，或將工具與鉤子、服務、供應者、命令或其他執行階段介面結合時，請直接使用 `definePluginEntry`。

## 回傳值

`defineToolPlugin` 會將純回傳值包裝成 OpenClaw 工具結果格式：

  * 當模型應看到該確切文字時，回傳字串。
  * 當你希望模型看到格式化 JSON，且 OpenClaw 將原始值保留在 `details` 中時，回傳 JSON 相容值。

typescriptCopy code
[code]
    tool({  name: "echo_text",  description: "Echo input text.",  parameters: Type.Object({    input: Type.String(),  }),  execute: ({ input }) => input,});
[/code]

typescriptCopy code
[code]
    tool({  name: "echo_json",  description: "Echo input as structured JSON.",  parameters: Type.Object({    input: Type.String(),  }),  execute: ({ input }) => ({ input, length: input.length }),});
[/code]

當你需要回傳自訂 `AgentToolResult`，或重用現有的 `api.registerTool` 實作時，請使用工廠工具。當你需要完全動態的工具或混合外掛能力時，請使用 `definePluginEntry`，而不是 `defineToolPlugin`。

## 設定

`configSchema` 是選用的。如果省略它，OpenClaw 會使用嚴格的空物件結構描述，且產生的資訊清單仍會包含 `configSchema`。

typescriptCopy code
[code]
    export default defineToolPlugin({  id: "no-config-tools",  name: "No Config Tools",  description: "Adds tools that do not need configuration.",  tools: () => [],});
[/code]

當你包含 `configSchema` 時，第二個 `execute` 引數會依結構描述取得型別：

typescriptCopy code
[code]
    const configSchema = Type.Object({  apiKey: Type.String(),}); export default defineToolPlugin({  id: "configured-tools",  name: "Configured Tools",  description: "Adds configured tools.",  configSchema,  tools: (tool) => [    tool({      name: "configured_ping",      description: "Check whether configuration is available.",      parameters: Type.Object({}),      execute: (_params, config) => ({ hasKey: config.apiKey.length > 0 }),    }),  ],});
[/code]

OpenClaw 會從閘道設定中的外掛項目讀取外掛設定。請勿在原始碼或文件範例中硬編碼祕密。請依外掛的安全模型使用設定、環境變數或 SecretRefs。

## 產生的中繼資料

OpenClaw 會從冷中繼資料探索已安裝外掛。它必須能在匯入外掛執行階段程式碼前讀取外掛資訊清單。因此，`defineToolPlugin` 會公開靜態中繼資料，而 `openclaw plugins build` 會將該中繼資料寫入套件。

在變更外掛 ID、名稱、描述、設定結構描述、啟用方式或工具名稱後，請執行產生器：

bashCopy code
[code]
    npm run buildopenclaw plugins build --entry ./dist/index.js
[/code]

對於單工具外掛，產生的資訊清單如下：

jsonCopy code
[code]
    {  "id": "stock-quotes",  "name": "Stock Quotes",  "description": "Fetch stock quote snapshots.",  "version": "0.1.0",  "configSchema": {    "type": "object",    "additionalProperties": false,    "properties": {}  },  "activation": {    "onStartup": true  },  "contracts": {    "tools": ["stock_quote"]  }}
[/code]

`contracts.tools` 是重要的探索合約。它會告訴 OpenClaw 每個工具由哪個外掛擁有，而不必載入每個已安裝外掛的執行階段。如果資訊清單過期，工具可能會從探索中遺失，或註冊錯誤可能會歸咎於錯誤的外掛。

## 套件中繼資料

對於簡單的工具外掛工作流程，`openclaw plugins build` 會將 `package.json` 對齊所選的單一執行階段進入點：

jsonCopy code
[code]
    {  "type": "module",  "files": ["dist", "openclaw.plugin.json", "README.md"],  "dependencies": {    "typebox": "^1.1.38"  },  "peerDependencies": {    "openclaw": ">=2026.5.17"  },  "openclaw": {    "extensions": ["./dist/index.js"]  }}
[/code]

對已安裝套件，請使用已建置的 JavaScript，例如 `./dist/index.js`。原始碼進入點在工作區開發中很有用，但已發布套件不應依賴 TypeScript 執行階段載入。

## 在 CI 中驗證

使用 `plugins build --check`，在產生的中繼資料過期時讓 CI 失敗，而不重寫檔案：

bashCopy code
[code]
    npm run buildopenclaw plugins build --entry ./dist/index.js --checkopenclaw plugins validate --entry ./dist/index.jsnpm test
[/code]

`plugins validate` 會檢查：

  * `openclaw.plugin.json` 存在並通過一般資訊清單載入器。
  * 目前進入點匯出 `defineToolPlugin` 中繼資料。
  * 產生的資訊清單欄位符合進入點中繼資料。
  * `contracts.tools` 符合宣告的工具名稱。
  * `package.json` 將 `openclaw.extensions` 指向所選的執行階段進入點。


## 在本機安裝並檢查

從另一個 OpenClaw checkout 或已安裝的命令列介面，安裝套件路徑：

bashCopy code
[code]
    openclaw plugins install ./stock-quotesopenclaw plugins inspect stock-quotes --runtime
[/code]

對於封裝冒煙測試，請先打包再安裝 tarball：

bashCopy code
[code]
    npm packopenclaw plugins install npm-pack:./openclaw-plugin-stock-quotes-0.1.0.tgzopenclaw plugins inspect stock-quotes --runtime --json
[/code]

安裝後，啟動或重新啟動閘道，並請代理使用該工具。如果你正在偵錯工具可見性，請先檢查外掛執行階段與有效工具目錄，再變更程式碼。

## 發布

當套件就緒時，透過 ClawHub 發布：

bashCopy code
[code]
    clawhub package publish your-org/stock-quotes --dry-runclawhub package publish your-org/stock-quotes
[/code]

使用明確的 ClawHub 定位器安裝：

bashCopy code
[code]
    openclaw plugins install clawhub:your-org/stock-quotes
[/code]

在發布切換期間，仍支援裸 npm 套件規格，但 ClawHub 是 OpenClaw 外掛偏好的探索與發佈介面。

## 疑難排解

### `plugin entry not found: ./dist/index.js`

所選進入點檔案不存在。請執行 `npm run build`，然後重新執行 `openclaw plugins build --entry ./dist/index.js` 或 `openclaw plugins validate --entry ./dist/index.js`。

### `plugin entry does not expose defineToolPlugin metadata`

進入點未匯出由 `defineToolPlugin` 建立的值。請檢查模組預設匯出是否為 `defineToolPlugin(...)` 結果，或使用 `--entry` 傳入正確進入點。

### `openclaw.plugin.json generated metadata is stale`

資訊清單不再符合進入點中繼資料。請執行：

bashCopy code
[code]
    npm run buildopenclaw plugins build --entry ./dist/index.js
[/code]

提交 `openclaw.plugin.json` 和 `package.json` 兩者的變更。

### `package.json openclaw.extensions must include ./dist/index.js`

套件中繼資料指向不同的執行階段進入點。請執行 `openclaw plugins build --entry ./dist/index.js`，讓產生器將套件中繼資料與你打算交付的進入點對齊。

### `Cannot find package 'typebox'`

已建置的外掛會在執行階段匯入 `typebox`。請將 `typebox` 保留在 `dependencies` 中，重新安裝套件相依項、重新建置，並重新執行驗證。

### 安裝後工具未出現

請依序檢查：

  1. `openclaw plugins inspect <plugin-id> --runtime`
  2. `openclaw plugins validate --root <plugin-root> --entry ./dist/index.js`
  3. `openclaw.plugin.json` 具有包含預期工具名稱的 `contracts.tools`。
  4. `package.json` 具有 `openclaw.extensions: ["./dist/index.js"]`。
  5. 安裝外掛後，閘道已重新啟動或重新載入。


## 另請參閱

  * [建置外掛](</zh-TW/plugins/building-plugins>)
  * [外掛進入點](</zh-TW/plugins/sdk-entrypoints>)
  * [外掛 SDK 子路徑](</zh-TW/plugins/sdk-subpaths>)
  * [外掛資訊清單](</zh-TW/plugins/manifest>)
  * [外掛命令列介面](</zh-TW/cli/plugins>)
  * [ClawHub 發布](</zh-TW/clawhub/publishing>)


Was this useful?YesNo

Open issue