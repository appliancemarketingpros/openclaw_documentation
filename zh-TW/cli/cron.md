---
title: Cron
source_url: https://docs.openclaw.ai/zh-TW/cli/cron
scraped_at: 2026-05-25
---

# `openclaw cron`

管理 Gateway 排程器的 Cron 工作。

## 工作階段

`--session` 接受 `main`、`isolated`、`current` 或 `session:<id>`。

工作階段鍵

  * `main` 綁定到代理程式的主要工作階段。
  * `isolated` 會為每次執行建立新的逐字稿和工作階段 ID。
  * `current` 綁定到建立時的作用中工作階段。
  * `session:<id>` 固定到明確的持久工作階段鍵。

隔離工作階段語意

隔離執行會重設環境對話上下文。新執行會重設頻道與群組路由、傳送/佇列政策、提升、來源，以及 ACP 執行階段綁定。安全偏好設定和明確由使用者選取的模型或驗證覆寫可以跨執行保留。

## 傳遞

`openclaw cron list` 和 `openclaw cron show <job-id>` 會預覽解析後的傳遞路由。對於 `channel: "last"`，預覽會顯示路由是從主要工作階段或目前工作階段解析而來，或會封閉失敗。

提供者前綴目標可消除未解析公告頻道的歧義。例如，當 `delivery.channel` 省略或為 `last` 時，`to: "telegram:123"` 會選取 Telegram。只有已載入 Plugin 公告的前綴才是提供者選取器。如果 `delivery.channel` 是明確的，前綴必須符合該頻道；`channel: "whatsapp"` 搭配 `to: "telegram:123"` 會被拒絕。像 `imessage:` 和 `sms:` 這類服務前綴仍是由頻道擁有的目標語法。

### 傳遞擁有權

隔離 Cron 聊天傳遞由代理程式和執行器共同負責：

  * 當聊天路由可用時，代理程式可以使用 `message` 工具直接傳送。
  * 只有當代理程式未直接傳送到已解析目標時，`announce` 才會後援傳遞最終回覆。
  * `webhook` 會將完成的承載發布到 URL。
  * `none` 會停用執行器後援傳遞。


`--announce` 是執行器對最終回覆的後援傳遞。`--no-deliver` 會停用該後援，但當聊天路由可用時，不會移除代理程式的 `message` 工具。

從作用中聊天建立的提醒會保留即時聊天傳遞目標，用於後援公告傳遞。內部工作階段鍵可能是小寫；請勿將它們作為區分大小寫提供者 ID 的事實來源，例如 Matrix 房間 ID。

### 失敗傳遞

失敗通知依下列順序解析：

  1. 工作上的 `delivery.failureDestination`。
  2. 全域 `cron.failureDestination`。
  3. 工作的主要公告目標（未設定明確失敗目的地時）。


注意：隔離 Cron 執行會將執行層級的代理程式失敗視為工作錯誤，即使 未產生回覆承載亦然，因此模型/提供者失敗仍會增加錯誤 計數器並觸發失敗通知。

如果隔離執行在第一次模型請求前逾時，`openclaw cron show` 和 `openclaw cron runs` 會包含階段特定錯誤，例如 `setup timed out before runner start` 或 `stalled before first model call (last phase: context-engine)`。 對於 CLI 支援的提供者，前模型監視器會持續作用，直到外部 CLI 回合開始，因此工作階段查詢、掛鉤、驗證、提示詞和 CLI 設定停滯 都會回報為前模型 Cron 失敗。

## 排程

### 一次性工作

`--at <datetime>` 會排程一次性執行。沒有偏移量的日期時間會被視為 UTC，除非你也傳入 `--tz <iana>`，它會以指定時區解讀牆上時鐘時間。

### 週期性工作

週期性工作在連續錯誤後使用指數重試退避：30s、1m、5m、15m、60m。下一次成功執行後，排程會恢復正常。

略過的執行會與執行錯誤分開追蹤。它們不會影響重試退避，但 `openclaw cron edit <job-id> --failure-alert-include-skipped` 可讓失敗警示納入重複略過執行通知。

對於目標為本機已設定模型提供者的隔離工作，Cron 會在開始代理程式回合前執行輕量提供者預檢。Loopback、私人網路和 `.local` `api: "ollama"` 提供者會在 `/api/tags` 探測；本機 OpenAI 相容提供者，例如 vLLM、SGLang 和 LM Studio，會在 `/models` 探測。如果端點無法連線，執行會記錄為 `skipped`，並在之後的排程重試；符合的失效端點會快取 5 分鐘，以避免大量工作不斷敲擊同一個本機伺服器。

注意：Cron 工作定義位於 `jobs.json`，待處理執行階段狀態位於 `jobs-state.json`。如果 `jobs.json` 由外部編輯，Gateway 會重新載入變更的排程並清除過時的待處理時段；僅格式化的重寫不會清除待處理時段。

### 手動執行

`openclaw cron run` 會在手動執行排入佇列後立即返回。成功回應包含 `{ ok: true, enqueued: true, runId }`。使用 `openclaw cron runs --id <job-id>` 追蹤最終結果。

## 模型

`cron add|edit --model <ref>` 會為工作選取允許的模型。

Cron `--model` 是**工作主要模型** ，不是聊天工作階段 `/model` 覆寫。這表示：

  * 當選取的工作模型失敗時，已設定的模型後援仍會套用。
  * 若存在每工作承載 `fallbacks`，它會取代已設定的後援清單。
  * 空的每工作後援清單（工作承載/API 中的 `fallbacks: []`）會讓 Cron 執行變為嚴格模式。
  * 當工作有 `--model` 但未設定後援清單時，OpenClaw 會傳入明確的空後援覆寫，使代理程式主要模型不會被附加為隱藏重試目標。


### 隔離 Cron 模型優先順序

隔離 Cron 依下列順序解析作用中模型：

  1. Gmail-hook 覆寫。
  2. 每工作 `--model`。
  3. 已儲存的 Cron 工作階段模型覆寫（當使用者選取了其中一個）。
  4. 代理程式或預設模型選擇。


### 快速模式

隔離 Cron 快速模式會遵循解析後的即時模型選擇。模型設定 `params.fastMode` 預設會套用，但已儲存工作階段的 `fastMode` 覆寫仍優先於設定。

### 即時模型切換重試

如果隔離執行擲出 `LiveSessionModelSwitchError`，Cron 會在重試前，為作用中執行持久保存已切換的提供者和模型（以及存在時的已切換驗證設定檔覆寫）。外層重試迴圈限制為初始嘗試後最多兩次切換重試，之後會中止而不是無限循環。

## 執行輸出與拒絕

### 過時確認抑制

隔離 Cron 回合會抑制過時的僅確認回覆。如果第一個結果只是臨時狀態更新，且沒有後代子代理程式執行負責最終答案，Cron 會重新提示一次以取得真正結果，再進行傳遞。

### 靜默權杖抑制

如果隔離 Cron 執行只返回靜默權杖（`NO_REPLY` 或 `no_reply`），Cron 會同時抑制直接對外傳遞和後援佇列摘要路徑，因此不會將任何內容發回聊天。

### 結構化拒絕

隔離 Cron 執行會優先使用嵌入式執行中的結構化執行拒絕中繼資料，然後退回到最終輸出中的已知拒絕標記，例如 `SYSTEM_RUN_DENIED`、`INVALID_REQUEST`，以及核准綁定拒絕片語。

`cron list` 和執行歷程會顯示拒絕原因，而不是將被封鎖的命令回報為 `ok`。

## 保留

保留和修剪由設定控制：

  * `cron.sessionRetention`（預設 `24h`）會修剪已完成的隔離執行工作階段。
  * `cron.runLog.maxBytes` 和 `cron.runLog.keepLines` 會修剪 `~/.openclaw/cron/runs/<jobId>.jsonl`。


## 遷移較舊工作

## 常見編輯

更新傳遞設定而不變更訊息：

bashCopy code
[code]
    openclaw cron edit <job-id> --announce --channel telegram --to "123456789"
[/code]

停用隔離工作的傳遞：

bashCopy code
[code]
    openclaw cron edit <job-id> --no-deliver
[/code]

為隔離工作啟用輕量啟動上下文：

bashCopy code
[code]
    openclaw cron edit <job-id> --light-context
[/code]

公告到特定頻道：

bashCopy code
[code]
    openclaw cron edit <job-id> --announce --channel slack --to "channel:C1234567890"
[/code]

公告到 Telegram 論壇主題：

bashCopy code
[code]
    openclaw cron edit <job-id> --announce --channel telegram --to "-1001234567890" --thread-id 42
[/code]

建立具有輕量啟動上下文的隔離工作：

bashCopy code
[code]
    openclaw cron add \  --name "Lightweight morning brief" \  --cron "0 7 * * *" \  --session isolated \  --message "Summarize overnight updates." \  --light-context \  --no-deliver
[/code]

`--light-context` 僅套用於隔離代理程式回合工作。對於 Cron 執行，輕量模式會讓啟動上下文保持空白，而不是注入完整工作區啟動集。

## 常見管理命令

手動執行與檢查：

bashCopy code
[code]
    openclaw cron listopenclaw cron list --agent opsopenclaw cron get <job-id>openclaw cron show <job-id>openclaw cron run <job-id>openclaw cron run <job-id> --dueopenclaw cron runs --id <job-id> --limit 50
[/code]

`openclaw cron list` 預設會顯示所有符合的工作。傳入 `--agent <id>` 可只顯示有效正規化代理程式 ID 相符的工作；沒有已儲存代理程式 ID 的工作會視為已設定的預設代理程式。

`openclaw cron get <job-id>` 會直接返回已儲存的工作 JSON。當你想要包含傳遞路由預覽的人類可讀檢視時，請使用 `cron show <job-id>`。

`cron list --json` 和 `cron show <job-id> --json` 會在每個工作上包含頂層 `status` 欄位，該欄位由 `enabled`、`state.runningAtMs` 和 `state.lastRunStatus` 計算而來。值為：`disabled`、`running`、`ok`、`error`、`skipped` 或 `idle`。這會鏡像人類可讀狀態欄，讓外部工具可讀取工作狀態，而不必重新推導。

`cron runs` 項目包含傳遞診斷，包括預期 Cron 目標、已解析目標、訊息工具傳送、後援使用，以及已傳遞狀態。

代理程式與工作階段重新定向：

bashCopy code
[code]
    openclaw cron edit <job-id> --agent opsopenclaw cron edit <job-id> --clear-agentopenclaw cron edit <job-id> --session currentopenclaw cron edit <job-id> --session "session:daily-brief"
[/code]

當代理程式回合工作省略 `--agent` 時，`openclaw cron add` 會發出警告，並退回到預設代理程式（`main`）。建立時傳入 `--agent <id>` 可固定特定代理程式。

傳遞微調：

bashCopy code
[code]
    openclaw cron edit <job-id> --announce --channel slack --to "channel:C1234567890"openclaw cron edit <job-id> --best-effort-deliveropenclaw cron edit <job-id> --no-best-effort-deliveropenclaw cron edit <job-id> --no-deliver
[/code]

## 相關

  * [CLI 參考](</zh-TW/cli>)
  * [已排程任務](</zh-TW/automation/cron-jobs>)


Was this useful?YesNo