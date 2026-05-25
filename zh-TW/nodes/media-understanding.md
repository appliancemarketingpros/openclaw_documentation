---
title: 媒體理解
source_url: https://docs.openclaw.ai/zh-TW/nodes/media-understanding
scraped_at: 2026-05-25
---

OpenClaw 可以在回覆流程執行前**摘要傳入媒體** （圖片/音訊/影片）。它會在本機工具或供應商金鑰可用時自動偵測，且可停用或自訂。如果理解功能關閉，模型仍會照常接收原始檔案/URL。

供應商特定的媒體行為由供應商 Plugin 註冊，而 OpenClaw 核心則負責共用的 `tools.media` 設定、備援順序，以及回覆流程整合。

## 目標

  * 選用：將傳入媒體預先消化成短文字，以加快路由並改善命令解析。
  * 保留原始媒體傳送給模型（永遠）。
  * 支援**供應商 API** 和 **CLI 備援** 。
  * 允許多個模型並依序備援（錯誤/大小/逾時）。


## 高階行為

* ### 收集附件

收集傳入附件（`MediaPaths`、`MediaUrls`、`MediaTypes`）。

* ### 依能力選取

針對每個已啟用的能力（圖片/音訊/影片），依政策選取附件（預設：**第一個** ）。

* ### 選擇模型

選擇第一個符合資格的模型項目（大小 + 能力 + 驗證）。

* ### 失敗時備援

如果模型失敗或媒體過大，**退回下一個項目** 。

* ### 套用成功區塊

成功時：

  * `Body` 會變成 `[Image]`、`[Audio]` 或 `[Video]` 區塊。
  * 音訊會設定 `{{Transcript}}`；命令解析會在有字幕文字時使用字幕，否則使用逐字稿。
  * 字幕會以區塊內的 `User text:` 保留。


如果理解失敗或已停用，**回覆流程會繼續** 使用原始本文 + 附件。

## 設定概覽

`tools.media` 支援**共用模型** 加上各能力覆寫：

頂層鍵

  * `tools.media.models`：共用模型清單（使用 `capabilities` 來控管）。
  * `tools.media.image` / `tools.media.audio` / `tools.media.video`： 
    * 預設值（`prompt`、`maxChars`、`maxBytes`、`timeoutSeconds`、`language`）
    * 供應商覆寫（`baseUrl`、`headers`、`providerOptions`）
    * 透過 `tools.media.audio.providerOptions.deepgram` 設定 Deepgram 音訊選項
    * 音訊逐字稿回顯控制（`echoTranscript`，預設 `false`；`echoFormat`）
    * 選用的**各能力`models` 清單**（優先於共用模型）
    * `attachments` 政策（`mode`、`maxAttachments`、`prefer`）
    * `scope`（依頻道/chatType/session key 選用控管）
  * `tools.media.concurrency`：最大並行能力執行數（預設 **2** ）。


json5Copy code
[code]
    {  tools: {    media: {      models: [        /* shared list */      ],      image: {        /* optional overrides */      },      audio: {        /* optional overrides */        echoTranscript: true,        echoFormat: '📝 "{transcript}"',      },      video: {        /* optional overrides */      },    },  },}
[/code]

### 模型項目

每個 `models[]` 項目都可以是**供應商** 或 **CLI** ：

### 供應商項目

json5Copy code
[code]
    {  type: "provider", // default if omitted  provider: "openai",  model: "gpt-5.5",  prompt: "Describe the image in <= 500 chars.",  maxChars: 500,  maxBytes: 10485760,  timeoutSeconds: 60,  capabilities: ["image"], // optional, used for multi-modal entries  profile: "vision-profile",  preferredProfile: "vision-fallback",}
[/code]

### CLI 項目

json5Copy code
[code]
    {  type: "cli",  command: "gemini",  args: [    "-m",    "gemini-3-flash",    "--allowed-tools",    "read_file",    "Read the media at {{MediaPath}} and describe it in <= {{MaxChars}} characters.",  ],  maxChars: 500,  maxBytes: 52428800,  timeoutSeconds: 120,  capabilities: ["video", "image"],}
[/code]

CLI 範本也可以使用：

  * `{{MediaDir}}`（包含媒體檔案的目錄）
  * `{{OutputDir}}`（為此執行建立的暫存目錄）
  * `{{OutputBase}}`（暫存檔案基底路徑，無副檔名）


## 預設值與限制

建議預設值：

  * `maxChars`：圖片/影片為 **500** （簡短、便於命令使用）
  * `maxChars`：音訊為**未設定** （完整逐字稿，除非你設定限制）
  * `maxBytes`： 
    * 圖片：**10MB**
    * 音訊：**20MB**
    * 影片：**50MB**


規則

  * 如果媒體超過 `maxBytes`，該模型會被略過，並**嘗試下一個模型** 。
  * 小於 **1024 bytes** 的音訊檔案會被視為空白/損毀，並在供應商/CLI 轉錄前略過；傳入回覆情境會收到確定性的佔位逐字稿，讓代理知道該語音記事太小。
  * 如果模型回傳超過 `maxChars`，輸出會被截短。
  * `prompt` 預設為簡單的 "Describe the {media}." 加上 `maxChars` 指引（僅圖片/影片）。
  * 如果作用中的主要圖片模型已原生支援視覺，OpenClaw 會略過 `[Image]` 摘要區塊，改為將原始圖片傳入模型。
  * 如果 Gateway/WebChat 主要模型僅支援文字，圖片附件會保留為已卸載的 `media://inbound/*` 參照，讓圖片/PDF 工具或已設定的圖片模型仍可檢查，而不會遺失附件。
  * 明確的 `openclaw infer image describe --model <provider/model>` 請求不同：它們會直接執行該具圖片能力的供應商/模型，包括 `ollama/qwen2.5vl:7b` 等 Ollama 參照。
  * 如果 `<capability>.enabled: true` 但未設定任何模型，OpenClaw 會在作用中回覆模型的供應商支援該能力時嘗試使用它。


### 自動偵測媒體理解（預設）

如果 `tools.media.<capability>.enabled` **未** 設定為 `false`，且你尚未設定模型，OpenClaw 會依下列順序自動偵測，並**在第一個可用選項停止** ：

* ### 作用中回覆模型

當作用中回覆模型的供應商支援該能力時使用它。

* ### agents.defaults.imageModel

`agents.defaults.imageModel` 主要/備援參照（僅圖片）。 優先使用 `provider/model` 參照。裸參照只會在已設定的具圖片能力供應商模型項目中相符且唯一時補上限定。

* ### 本機 CLI（僅音訊）

本機 CLI（若已安裝）：

  * `sherpa-onnx-offline`（需要包含 encoder/decoder/joiner/tokens 的 `SHERPA_ONNX_MODEL_DIR`）
  * `whisper-cli`（`whisper-cpp`；使用 `WHISPER_CPP_MODEL` 或內建 tiny 模型）
  * `whisper`（Python CLI；會自動下載模型）


* ### Gemini CLI

使用 `read_many_files` 的 `gemini`。

* ### 供應商驗證

  * 支援該能力的已設定 `models.providers.*` 項目，會在內建備援順序前嘗試。
  * 只有圖片設定、且具有圖片能力模型的供應商，即使不是內建供應商 Plugin，也會自動註冊用於媒體理解。
  * Ollama 圖片理解在明確選取時可用，例如透過 `agents.defaults.imageModel` 或 `openclaw infer image describe --model ollama/<vision-model>`。


內建備援順序：

  * 音訊：OpenAI → Groq → xAI → Deepgram → OpenRouter → Google → SenseAudio → ElevenLabs → Mistral
  * 圖片：OpenAI → Anthropic → Google → MiniMax → MiniMax Portal → [Z.AI](<http://Z.AI>)
  * 影片：Google → Qwen → Moonshot


若要停用自動偵測，請設定：

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: false,      },    },  },}
[/code]

### 代理環境支援（供應商模型）

啟用以供應商為基礎的**音訊** 和**影片** 媒體理解時，OpenClaw 會在供應商 HTTP 呼叫中遵循標準外送代理環境變數：

  * `HTTPS_PROXY`
  * `HTTP_PROXY`
  * `ALL_PROXY`
  * `https_proxy`
  * `http_proxy`
  * `all_proxy`


如果未設定任何代理環境變數，媒體理解會使用直接外連。如果代理值格式錯誤，OpenClaw 會記錄警告並退回直接擷取。

## 能力（選用）

如果你設定 `capabilities`，該項目只會針對那些媒體類型執行。對於共用清單，OpenClaw 可推斷預設值：

  * `openai`、`anthropic`、`minimax`：**圖片**
  * `minimax-portal`：**圖片**
  * `moonshot`：**圖片 + 影片**
  * `openrouter`：**圖片 + 音訊**
  * `google`（Gemini API）：**圖片 + 音訊 + 影片**
  * `qwen`：**圖片 + 影片**
  * `mistral`：**音訊**
  * `zai`：**圖片**
  * `groq`：**音訊**
  * `xai`：**音訊**
  * `deepgram`：**音訊**
  * 任何包含具圖片能力模型的 `models.providers.<id>.models[]` 目錄：**圖片**


對於 CLI 項目，請**明確設定`capabilities`** 以避免意外相符。如果省略 `capabilities`，該項目會適用於它所在的清單。

## 供應商支援矩陣（OpenClaw 整合）

能力 | 供應商整合 | 備註  
---|---|---  
圖片 | OpenAI, OpenAI Codex OAuth, Codex app-server, OpenRouter, Anthropic, Google, MiniMax, Moonshot, Qwen, [Z.AI](<http://Z.AI>), config providers | 供應商 Plugin 會註冊圖片支援；`openai-codex/*` 使用 OAuth 供應商管線；`codex/*` 使用有界的 Codex app-server 回合；MiniMax 和 MiniMax OAuth 都使用 `MiniMax-VL-01`；具圖片能力的設定供應商會自動註冊。  
音訊 | OpenAI, Groq, xAI, Deepgram, OpenRouter, Google, SenseAudio, ElevenLabs, Mistral | 供應商轉錄（Whisper/Groq/xAI/Deepgram/OpenRouter STT/Gemini/SenseAudio/Scribe/Voxtral）。  
影片 | Google, Qwen, Moonshot | 透過供應商 Plugin 進行供應商影片理解；Qwen 影片理解使用 Standard DashScope 端點。  
  
## 模型選擇指引

  * 當品質與安全性重要時，優先為每個媒體能力使用可用的最強最新世代模型。
  * 對於處理不受信任輸入的工具啟用代理，避免使用較舊/較弱的媒體模型。
  * 每個能力至少保留一個備援以提高可用性（品質模型 + 較快/較便宜模型）。
  * 當供應商 API 無法使用時，CLI 備援（`whisper-cli`、`whisper`、`gemini`）很有用。
  * `parakeet-mlx` 備註：搭配 `--output-dir` 時，若輸出格式為 `txt`（或未指定），OpenClaw 會讀取 `<output-dir>/<media-basename>.txt`；非 `txt` 格式則退回 stdout。


## 附件政策

各能力的 `attachments` 控制要處理哪些附件：

要處理第一個選取的附件，或全部附件。

限制處理的數量。

候選附件之間的選取偏好。

當 `mode: "all"` 時，輸出會標示為 `[Image 1/2]`、`[Audio 2/2]` 等。

檔案附件擷取行為

  * 擷取出的檔案文字會先包裝為**不受信任的外部內容** ，再附加到媒體提示中。
  * 注入的區塊會使用明確的邊界標記，例如 `<<&lt;EXTERNAL_UNTRUSTED_CONTENT id=&quot;...&quot;&gt;>>` / `<<&lt;END_EXTERNAL_UNTRUSTED_CONTENT id=&quot;...&quot;&gt;>>`，並包含 `Source: External` 中繼資料行。
  * 這個附件擷取路徑會刻意省略較長的 `SECURITY NOTICE:` 橫幅，以避免讓媒體提示過度膨脹；邊界標記和中繼資料仍會保留。
  * 如果檔案沒有可擷取的文字，OpenClaw 會注入 `[No extractable text]`。
  * 如果 PDF 在此路徑中改用算繪後的頁面影像，媒體提示會保留佔位符 `[PDF content rendered to images; images not forwarded to model]`，因為這個附件擷取步驟會轉送文字區塊，而不是算繪後的 PDF 影像。


## 設定範例

### 共用模型 + 覆寫

json5Copy code
[code]
    {  tools: {    media: {      models: [        { provider: "openai", model: "gpt-5.5", capabilities: ["image"] },        {          provider: "google",          model: "gemini-3-flash-preview",          capabilities: ["image", "audio", "video"],        },        {          type: "cli",          command: "gemini",          args: [            "-m",            "gemini-3-flash",            "--allowed-tools",            "read_file",            "Read the media at {{MediaPath}} and describe it in <= {{MaxChars}} characters.",          ],          capabilities: ["image", "video"],        },      ],      audio: {        attachments: { mode: "all", maxAttachments: 2 },      },      video: {        maxChars: 500,      },    },  },}
[/code]

### 僅音訊 + 影片

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [          { provider: "openai", model: "gpt-4o-mini-transcribe" },          {            type: "cli",            command: "whisper",            args: ["--model", "base", "{{MediaPath}}"],          },        ],      },      video: {        enabled: true,        maxChars: 500,        models: [          { provider: "google", model: "gemini-3-flash-preview" },          {            type: "cli",            command: "gemini",            args: [              "-m",              "gemini-3-flash",              "--allowed-tools",              "read_file",              "Read the media at {{MediaPath}} and describe it in <= {{MaxChars}} characters.",            ],          },        ],      },    },  },}
[/code]

### 僅影像

json5Copy code
[code]
    {  tools: {    media: {      image: {        enabled: true,        maxBytes: 10485760,        maxChars: 500,        models: [          { provider: "openai", model: "gpt-5.5" },          { provider: "anthropic", model: "claude-opus-4-6" },          {            type: "cli",            command: "gemini",            args: [              "-m",              "gemini-3-flash",              "--allowed-tools",              "read_file",              "Read the media at {{MediaPath}} and describe it in <= {{MaxChars}} characters.",            ],          },        ],      },    },  },}
[/code]

### 單一多模態項目

json5Copy code
[code]
    {  tools: {    media: {      image: {        models: [          {            provider: "google",            model: "gemini-3.1-pro-preview",            capabilities: ["image", "video", "audio"],          },        ],      },      audio: {        models: [          {            provider: "google",            model: "gemini-3.1-pro-preview",            capabilities: ["image", "video", "audio"],          },        ],      },      video: {        models: [          {            provider: "google",            model: "gemini-3.1-pro-preview",            capabilities: ["image", "video", "audio"],          },        ],      },    },  },}
[/code]

## 狀態輸出

當媒體理解執行時，`/status` 會包含一行簡短摘要：

CodeCopy code
[code]
    📎 Media: image ok (openai/gpt-5.4) · audio skipped (maxBytes)
[/code]

這會顯示各能力的結果，以及適用時所選的供應商/模型。

## 備註

  * 理解屬於**盡力而為** 。錯誤不會阻擋回覆。
  * 即使停用理解，附件仍會傳遞給模型。
  * 使用 `scope` 限制理解執行的位置（例如僅限私訊）。


## 相關

  * [設定](</zh-TW/gateway/configuration>)
  * [影像與媒體支援](</zh-TW/nodes/images>)


Was this useful?YesNo