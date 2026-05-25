---
title: 記憶設定參考
source_url: https://docs.openclaw.ai/zh-TW/reference/memory-config
scraped_at: 2026-05-25
---

此頁面列出 OpenClaw 記憶搜尋的所有設定旋鈕。如需概念性概覽，請參閱：

[**記憶概覽** 記憶如何運作。 ](</zh-TW/concepts/memory>) [**內建引擎** 預設 SQLite 後端。 ](</zh-TW/concepts/memory-builtin>) [**QMD 引擎** 本機優先的 sidecar。 ](</zh-TW/concepts/memory-qmd>) [**記憶搜尋** 搜尋管線與調校。 ](</zh-TW/concepts/memory-search>) [**Active Memory** 用於互動式工作階段的記憶子代理。 ](</zh-TW/concepts/active-memory>)

除非另有註明，所有記憶搜尋設定都位於 `openclaw.json` 的 `agents.defaults.memorySearch` 下。

* * *

## Provider 選擇

鍵 | 類型 | 預設值 | 說明  
---|---|---|---  
`provider` | `string` | 自動偵測 | 嵌入轉接器 ID，例如 `bedrock`、`deepinfra`、`gemini`、`github-copilot`、`local`、`mistral`、`ollama`、`openai` 或 `voyage`；也可以是已設定的 `models.providers.<id>`，其 `api` 指向其中一個轉接器  
`model` | `string` | provider 預設值 | 嵌入模型名稱  
`fallback` | `string` | `"none"` | 主要項目失敗時使用的備援轉接器 ID  
`enabled` | `boolean` | `true` | 啟用或停用記憶搜尋  
  
### 自動偵測順序

未設定 `provider` 時，OpenClaw 會選擇第一個可用項目：

* ### local

若已設定 `memorySearch.local.modelPath` 且檔案存在，則會選取。

* ### github-copilot

若可解析 GitHub Copilot token（env var 或 auth profile），則會選取。

* ### openai

若可解析 OpenAI key，則會選取。

* ### gemini

若可解析 Gemini key，則會選取。

* ### voyage

若可解析 Voyage key，則會選取。

* ### mistral

若可解析 Mistral key，則會選取。

* ### deepinfra

若可解析 DeepInfra key，則會選取。

* ### bedrock

若 AWS SDK 憑證鏈可解析（instance role、access keys、profile、SSO、web identity 或 shared config），則會選取。

支援 `ollama`，但不會自動偵測（請明確設定）。

### 自訂 provider ID

`memorySearch.provider` 可以指向自訂 `models.providers.<id>` 項目。OpenClaw 會解析該 provider 的 `api` 擁有者以用於嵌入轉接器，同時保留自訂 provider ID 以處理端點、驗證和模型前綴。這讓多 GPU 或多主機設定可以將記憶嵌入專用於特定本機端點：

json5Copy code
[code]
    {  models: {    providers: {      "ollama-5080": {        api: "ollama",        baseUrl: "http://gpu-box.local:11435",        apiKey: "ollama-local",        models: [{ id: "qwen3-embedding:0.6b" }],      },    },  },  agents: {    defaults: {      memorySearch: {        provider: "ollama-5080",        model: "qwen3-embedding:0.6b",      },    },  },}
[/code]

### API key 解析

遠端嵌入需要 API key。Bedrock 則改用 AWS SDK 預設憑證鏈（instance roles、SSO、access keys）。

Provider | Env var | 設定鍵  
---|---|---  
Bedrock | AWS 憑證鏈 | 不需要 API key  
DeepInfra | `DEEPINFRA_API_KEY` | `models.providers.deepinfra.apiKey`  
Gemini | `GEMINI_API_KEY` | `models.providers.google.apiKey`  
GitHub Copilot | `COPILOT_GITHUB_TOKEN`, `GH_TOKEN`, `GITHUB_TOKEN` | 透過裝置登入的 auth profile  
Mistral | `MISTRAL_API_KEY` | `models.providers.mistral.apiKey`  
Ollama | `OLLAMA_API_KEY`（預留位置） | \--  
OpenAI | `OPENAI_API_KEY` | `models.providers.openai.apiKey`  
Voyage | `VOYAGE_API_KEY` | `models.providers.voyage.apiKey`  
  
* * *

## 遠端端點設定

用於自訂 OpenAI 相容端點，或覆寫 provider 預設值：

自訂 API 基礎 URL。

覆寫 API key。

額外 HTTP 標頭（與 provider 預設值合併）。

json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        provider: "openai",        model: "text-embedding-3-small",        remote: {          baseUrl: "https://api.example.com/v1/",          apiKey: "YOUR_KEY",        },      },    },  },}
[/code]

* * *

## Provider 專用設定

Gemini 鍵 | 類型 | 預設值 | 說明  
---|---|---|---  
`model` | `string` | `gemini-embedding-001` | 也支援 `gemini-embedding-2-preview`  
`outputDimensionality` | `number` | `3072` | 對 Embedding 2：768、1536 或 3072  
OpenAI 相容輸入類型

OpenAI 相容的嵌入端點可以選擇使用 provider 專用的 `input_type` 請求欄位。這對需要為查詢和文件嵌入使用不同標籤的非對稱嵌入模型很有用。

鍵 | 類型 | 預設值 | 說明  
---|---|---|---  
`inputType` | `string` | 未設定 | 查詢和文件嵌入共用的 `input_type`  
`queryInputType` | `string` | 未設定 | 查詢時的 `input_type`；覆寫 `inputType`  
`documentInputType` | `string` | 未設定 | 索引/文件的 `input_type`；覆寫 `inputType`  
json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        provider: "openai",        remote: {          baseUrl: "https://embeddings.example/v1",          apiKey: "env:EMBEDDINGS_API_KEY",        },        model: "asymmetric-embedder",        queryInputType: "query",        documentInputType: "passage",      },    },  },}
[/code]

當上游模型以不同方式處理這些標籤時，變更這些值會影響 provider 批次索引的嵌入快取識別，且之後應重新索引記憶。

Bedrock

### Bedrock 嵌入設定

Bedrock 使用 AWS SDK 預設憑證鏈，不需要 API key。如果 OpenClaw 在具有 Bedrock 啟用 instance role 的 EC2 上執行，只需設定 provider 和模型：

json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        provider: "bedrock",        model: "amazon.titan-embed-text-v2:0",      },    },  },}
[/code]

鍵 | 類型 | 預設值 | 說明  
---|---|---|---  
`model` | `string` | `amazon.titan-embed-text-v2:0` | 任何 Bedrock 嵌入模型 ID  
`outputDimensionality` | `number` | 模型預設值 | 對 Titan V2：256、512 或 1024  
  
**支援的模型** （含系列偵測和維度預設值）：

模型 ID | Provider | 預設維度 | 可設定維度  
---|---|---|---  
`amazon.titan-embed-text-v2:0` | Amazon | 1024 | 256, 512, 1024  
`amazon.titan-embed-text-v1` | Amazon | 1536 | \--  
`amazon.titan-embed-g1-text-02` | Amazon | 1536 | \--  
`amazon.titan-embed-image-v1` | Amazon | 1024 | \--  
`amazon.nova-2-multimodal-embeddings-v1:0` | Amazon | 1024 | 256, 384, 1024, 3072  
`cohere.embed-english-v3` | Cohere | 1024 | \--  
`cohere.embed-multilingual-v3` | Cohere | 1024 | \--  
`cohere.embed-v4:0` | Cohere | 1536 | 256-1536  
`twelvelabs.marengo-embed-3-0-v1:0` | TwelveLabs | 512 | \--  
`twelvelabs.marengo-embed-2-7-v1:0` | TwelveLabs | 1024 | \--  
  
具有輸送量後綴的變體（例如 `amazon.titan-embed-text-v1:2:8k`）會繼承基礎模型的設定。

**驗證：** Bedrock 驗證使用標準 AWS SDK 憑證解析順序：

  1. 環境變數（`AWS_ACCESS_KEY_ID` \+ `AWS_SECRET_ACCESS_KEY`）
  2. SSO token 快取
  3. Web identity token 憑證
  4. 共用憑證和設定檔
  5. ECS 或 EC2 metadata 憑證


區域會從 `AWS_REGION`、`AWS_DEFAULT_REGION`、`amazon-bedrock` provider `baseUrl` 解析，或預設為 `us-east-1`。

**IAM 權限：** IAM 角色或使用者需要：

jsonCopy code
[code]
    {  "Effect": "Allow",  "Action": "bedrock:InvokeModel",  "Resource": "*"}
[/code]

若採最小權限，請將 `InvokeModel` 範圍限定於特定模型：

CodeCopy code
[code]
    arn:aws:bedrock:*::foundation-model/amazon.titan-embed-text-v2:0
[/code]

本機 (GGUF + node-llama-cpp) Key | Type | Default | Description  
---|---|---|---  
`local.modelPath` | `string` | auto-downloaded | GGUF 模型檔案的路徑  
`local.modelCacheDir` | `string` | node-llama-cpp default | 已下載模型的快取目錄  
`local.contextSize` | `number | "auto"` | `4096` | 嵌入情境的情境視窗大小。4096 可涵蓋典型區塊（128–512 個 token），同時限制非權重 VRAM。受限主機可降低至 1024–2048。`"auto"` 會使用模型訓練時的最大值，不建議用於 8B+ 模型（Qwen3-Embedding-8B：40 960 個 token → 約 32 GB VRAM，相較於 4096 時約 8.8 GB）。  
  
預設模型：`embeddinggemma-300m-qat-Q8_0.gguf`（約 0.6 GB，自動下載）。原始碼簽出仍需要原生建置核准：`pnpm approve-builds`，然後執行 `pnpm rebuild node-llama-cpp`。

使用獨立 CLI 驗證 Gateway 使用的相同提供者路徑：

bashCopy code
[code]
    openclaw memory status --deep --agent mainopenclaw memory index --force --agent main
[/code]

如果 `provider` 是 `auto`，只有在 `local.modelPath` 指向現有本機檔案時才會選取 `local`。`hf:` 和 HTTP(S) 模型參照仍可搭配 `provider: "local"` 明確使用，但在模型可於磁碟上使用之前，它們不會讓 `auto` 選取本機。

### 內嵌嵌入逾時

覆寫記憶體索引期間內嵌嵌入批次的逾時。

未設定時會使用提供者預設值：對於 `local`、`ollama` 和 `lmstudio` 等本機/自託管提供者為 600 秒，對於託管提供者為 120 秒。當本機 CPU 密集的嵌入批次狀態正常但速度較慢時，請提高此值。

* * *

## 混合搜尋設定

全部位於 `memorySearch.query.hybrid` 下：

Key | Type | Default | Description  
---|---|---|---  
`enabled` | `boolean` | `true` | 啟用混合 BM25 + 向量搜尋  
`vectorWeight` | `number` | `0.7` | 向量分數的權重 (0-1)  
`textWeight` | `number` | `0.3` | BM25 分數的權重 (0-1)  
`candidateMultiplier` | `number` | `4` | 候選池大小乘數  
  
### MMR（多樣性）

Key | Type | Default | Description  
---|---|---|---  
`mmr.enabled` | `boolean` | `false` | 啟用 MMR 重新排序  
`mmr.lambda` | `number` | `0.7` | 0 = 最大多樣性，1 = 最大相關性  
  
### 時間衰減（近期性）

Key | Type | Default | Description  
---|---|---|---  
`temporalDecay.enabled` | `boolean` | `false` | 啟用近期性加權  
`temporalDecay.halfLifeDays` | `number` | `30` | 每 N 天分數減半  
  
常青檔案（`MEMORY.md`、`memory/` 中未標日期的檔案）永不衰減。

### 完整範例

json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        query: {          hybrid: {            vectorWeight: 0.7,            textWeight: 0.3,            mmr: { enabled: true, lambda: 0.7 },            temporalDecay: { enabled: true, halfLifeDays: 30 },          },        },      },    },  },}
[/code]

* * *

## 其他記憶體路徑

Key | Type | Description  
---|---|---  
`extraPaths` | `string[]` | 要索引的其他目錄或檔案  
json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        extraPaths: ["../team-docs", "/srv/shared-notes"],      },    },  },}
[/code]

路徑可以是絕對路徑或相對於工作區的路徑。目錄會以遞迴方式掃描 `.md` 檔案。符號連結處理取決於啟用中的後端：內建引擎會忽略符號連結，而 QMD 會遵循底層 QMD 掃描器行為。

對於以代理程式為範圍的跨代理程式轉錄搜尋，請使用 `agents.list[].memorySearch.qmd.extraCollections`，而不是 `memory.qmd.paths`。這些額外集合遵循相同的 `{ path, name, pattern? }` 形狀，但會依每個代理程式合併，且在路徑指向目前工作區外部時，可以保留明確的共享名稱。如果同一個解析後的路徑同時出現在 `memory.qmd.paths` 和 `memorySearch.qmd.extraCollections` 中，QMD 會保留第一個項目並略過重複項目。

* * *

## 多模態記憶體 (Gemini)

使用 Gemini Embedding 2 將圖片和音訊與 Markdown 一起索引：

Key | Type | Default | Description  
---|---|---|---  
`multimodal.enabled` | `boolean` | `false` | 啟用多模態索引  
`multimodal.modalities` | `string[]` | \-- | `["image"]`、`["audio"]` 或 `["all"]`  
`multimodal.maxFileBytes` | `number` | `10000000` | 索引的最大檔案大小  
  
支援的格式：`.jpg`、`.jpeg`、`.png`、`.webp`、`.gif`、`.heic`、`.heif`（圖片）；`.mp3`、`.wav`、`.ogg`、`.opus`、`.m4a`、`.aac`、`.flac`（音訊）。

* * *

## 嵌入快取

Key | Type | Default | Description  
---|---|---|---  
`cache.enabled` | `boolean` | `false` | 在 SQLite 中快取區塊嵌入  
`cache.maxEntries` | `number` | `50000` | 快取嵌入數量上限  
  
在重新索引或逐字稿更新期間，避免重新嵌入未變更的文字。

* * *

## 批次索引

Key | Type | Default | Description  
---|---|---|---  
`remote.nonBatchConcurrency` | `number` | `4` | 平行內嵌嵌入  
`remote.batch.enabled` | `boolean` | `false` | 啟用批次嵌入 API  
`remote.batch.concurrency` | `number` | `2` | 平行批次工作  
`remote.batch.wait` | `boolean` | `true` | 等待批次完成  
`remote.batch.pollIntervalMs` | `number` | \-- | 輪詢間隔  
`remote.batch.timeoutMinutes` | `number` | \-- | 批次逾時  
  
適用於 `openai`、`gemini` 和 `voyage`。對於大型回填，OpenAI 批次通常最快且成本最低。

`remote.nonBatchConcurrency` 控制本機／自託管供應商，以及未啟用供應商批次 API 時的託管供應商所使用的內嵌嵌入呼叫。Ollama 的非批次索引預設為 `1`，以避免讓較小的本機主機負載過高；在較大的機器上可設定較高的值。

這與 `sync.embeddingBatchTimeoutSeconds` 分開，後者控制內嵌嵌入呼叫的逾時。

* * *

## 工作階段記憶搜尋（實驗性）

索引工作階段逐字稿，並透過 `memory_search` 呈現：

Key | Type | Default | Description  
---|---|---|---  
`experimental.sessionMemory` | `boolean` | `false` | 啟用工作階段索引  
`sources` | `string[]` | `["memory"]` | 新增 `"sessions"` 以包含逐字稿  
`sync.sessions.deltaBytes` | `number` | `100000` | 重新索引的位元組閾值  
`sync.sessions.deltaMessages` | `number` | `50` | 重新索引的訊息閾值  
  
* * *

## SQLite 向量加速（sqlite-vec）

Key | Type | Default | Description  
---|---|---|---  
`store.vector.enabled` | `boolean` | `true` | 使用 sqlite-vec 進行向量查詢  
`store.vector.extensionPath` | `string` | bundled | 覆寫 sqlite-vec 路徑  
  
當 sqlite-vec 無法使用時，OpenClaw 會自動退回至程序內餘弦相似度。

* * *

## 索引儲存

Key | Type | Default | Description  
---|---|---|---  
`store.path` | `string` | `~/.openclaw/memory/{agentId}.sqlite` | 索引位置（支援 `{agentId}` 權杖）  
`store.fts.tokenizer` | `string` | `unicode61` | FTS5 tokenizer（`unicode61` 或 `trigram`）  
  
* * *

## QMD 後端設定

設定 `memory.backend = "qmd"` 以啟用。所有 QMD 設定都位於 `memory.qmd` 下：

Key | Type | Default | Description  
---|---|---|---  
`command` | `string` | `qmd` | QMD 可執行檔路徑；當服務 `PATH` 與你的 shell 不同時，請設定絕對路徑  
`searchMode` | `string` | `search` | 搜尋命令：`search`、`vsearch`、`query`  
`includeDefaultMemory` | `boolean` | `true` | 自動索引 `MEMORY.md` \+ `memory/**/*.md`  
`paths[]` | `array` | \-- | 額外路徑：`{ name, path, pattern? }`  
`sessions.enabled` | `boolean` | `false` | 索引工作階段逐字稿  
`sessions.retentionDays` | `number` | \-- | 逐字稿保留期限  
`sessions.exportDir` | `string` | \-- | 匯出目錄  
  
`searchMode: "search"` 是僅詞彙/BM25 模式。OpenClaw 不會為該模式執行語意向量就緒探測或 QMD embedding 維護，包括在 `memory status --deep` 期間；`vsearch` 與 `query` 仍然需要 QMD 向量就緒狀態與 embeddings。

OpenClaw 偏好目前的 QMD collection 與 MCP query 形狀，但會在需要時嘗試相容的 collection pattern flags 與較舊的 MCP tool 名稱，以維持較舊 QMD 版本可用。當 QMD 宣告支援多個 collection filters 時，同來源 collections 會以單一 QMD process 搜尋；較舊的 QMD builds 則保留逐 collection 的相容路徑。同來源表示 durable memory collections 會被分組在一起，而 session transcript collections 仍保留為獨立群組，讓 source diversification 仍同時具備兩種輸入。

更新排程 Key | Type | Default | Description  
---|---|---|---  
`update.interval` | `string` | `5m` | 重新整理間隔  
`update.debounceMs` | `number` | `15000` | 對檔案變更進行 debounce  
`update.onBoot` | `boolean` | `true` | 在長駐 QMD manager 開啟時重新整理；也會控管 opt-in startup refresh  
`update.startup` | `string` | `off` | 選用的 gateway 啟動時重新整理：`off`、`idle` 或 `immediate`  
`update.startupDelayMs` | `number` | `120000` | `startup: "idle"` 重新整理執行前的延遲  
`update.waitForBootSync` | `boolean` | `false` | 阻擋 manager 開啟，直到其初始重新整理完成  
`update.embedInterval` | `string` | \-- | 獨立的 embed 節奏  
`update.commandTimeoutMs` | `number` | \-- | QMD commands 的逾時  
`update.updateTimeoutMs` | `number` | \-- | QMD update operations 的逾時  
`update.embedTimeoutMs` | `number` | \-- | QMD embed operations 的逾時  
限制 Key | Type | Default | Description  
---|---|---|---  
`limits.maxResults` | `number` | `6` | 搜尋結果數上限  
`limits.maxSnippetChars` | `number` | \-- | 限制 snippet 長度  
`limits.maxInjectedChars` | `number` | \-- | 限制注入字元總數  
`limits.timeoutMs` | `number` | `4000` | 搜尋逾時  
範圍

控制哪些 sessions 可以接收 QMD 搜尋結果。Schema 與 [`session.sendPolicy`](</zh-TW/gateway/config-agents#session>) 相同：

json5Copy code
[code]
    {  memory: {    qmd: {      scope: {        default: "deny",        rules: [{ action: "allow", match: { chatType: "direct" } }],      },    },  },}
[/code]

隨附的預設值允許 direct 與 channel sessions，同時仍拒絕 groups。

預設為僅限 DM。`match.keyPrefix` 會比對正規化後的 session key；`match.rawKeyPrefix` 會比對包含 `agent:<id>:` 的原始 key。

引用

`memory.citations` 適用於所有 backends：

Value | Behavior  
---|---  
`auto` (default) | 在 snippets 中包含 `Source: <path#line>` footer  
`on` | 一律包含 footer  
`off` | 省略 footer（path 仍會在內部傳給 agent）  
  
QMD boot refreshes 會在 Gateway 啟動期間使用一次性的 subprocess path。當 memory search 被開啟供互動使用時，長駐 QMD manager 仍負責一般 file watcher 與 interval timers。

### 完整 QMD 範例

json5Copy code
[code]
    {  memory: {    backend: "qmd",    citations: "auto",    qmd: {      includeDefaultMemory: true,      update: { interval: "5m", debounceMs: 15000 },      limits: { maxResults: 6, timeoutMs: 4000 },      scope: {        default: "deny",        rules: [{ action: "allow", match: { chatType: "direct" } }],      },      paths: [{ name: "docs", path: "~/notes", pattern: "**/*.md" }],    },  },}
[/code]

* * *

## Dreaming

Dreaming 設定於 `plugins.entries.memory-core.config.dreaming` 之下，而不是 `agents.defaults.memorySearch` 之下。

Dreaming 會作為單一排程 sweep 執行，並使用內部 light/deep/REM phases 作為 implementation detail。

如需概念行為與 slash commands，請參閱 [Dreaming](</zh-TW/concepts/dreaming>)。

### 使用者設定

Key | Type | Default | Description  
---|---|---|---  
`enabled` | `boolean` | `false` | 完整啟用或停用 dreaming  
`frequency` | `string` | `0 3 * * *` | 完整 dreaming sweep 的選用 cron 節奏  
`model` | `string` | default model | 選用的 Dream Diary subagent model override  
  
### 範例

json5Copy code
[code]
    {  plugins: {    entries: {      "memory-core": {        subagent: {          allowModelOverride: true,          allowedModels: ["anthropic/claude-sonnet-4-6"],        },        config: {          dreaming: {            enabled: true,            frequency: "0 3 * * *",            model: "anthropic/claude-sonnet-4-6",          },        },      },    },  },}
[/code]

## 相關

  * [設定參考](</zh-TW/gateway/configuration-reference>)
  * [Memory 概覽](</zh-TW/concepts/memory>)
  * [Memory search](</zh-TW/concepts/memory-search>)


Was this useful?YesNo