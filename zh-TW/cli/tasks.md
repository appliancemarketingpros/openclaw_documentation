---
title: `openclaw tasks`
source_url: https://docs.openclaw.ai/zh-TW/cli/tasks
scraped_at: 2026-05-25
---

檢查持久性背景任務與 Task Flow 狀態。沒有子命令時，`openclaw tasks` 等同於 `openclaw tasks list`。

請參閱 [背景任務](</zh-TW/automation/tasks>) 了解生命週期與傳遞模型。

## 使用方式

bashCopy code
[code]
    openclaw tasksopenclaw tasks listopenclaw tasks list --runtime acpopenclaw tasks list --status runningopenclaw tasks show <lookup>openclaw tasks notify <lookup> state_changesopenclaw tasks cancel <lookup>openclaw tasks auditopenclaw tasks maintenanceopenclaw tasks maintenance --applyopenclaw tasks flow listopenclaw tasks flow show <lookup>openclaw tasks flow cancel <lookup>
[/code]

## 根選項

  * `--json`: 輸出 JSON。
  * `--runtime <name>`: 依類型篩選：`subagent`、`acp`、`cron` 或 `cli`。
  * `--status <name>`: 依狀態篩選：`queued`、`running`、`succeeded`、`failed`、`timed_out`、`cancelled` 或 `lost`。


## 子命令

### `list`

bashCopy code
[code]
    openclaw tasks list [--runtime <name>] [--status <name>] [--json]
[/code]

列出追蹤中的背景任務，最新的在前。

### `show`

bashCopy code
[code]
    openclaw tasks show <lookup> [--json]
[/code]

依任務 ID、執行 ID 或工作階段金鑰顯示單一任務。

### `notify`

bashCopy code
[code]
    openclaw tasks notify <lookup> <done_only|state_changes|silent>
[/code]

變更執行中任務的通知政策。

### `cancel`

bashCopy code
[code]
    openclaw tasks cancel <lookup>
[/code]

取消執行中的背景任務。

### `audit`

bashCopy code
[code]
    openclaw tasks audit [--severity <warn|error>] [--code <name>] [--limit <n>] [--json]
[/code]

顯示過期、遺失、傳遞失敗，或其他不一致的任務與 Task Flow 記錄。保留到 `cleanupAfter` 的遺失任務為警告；已過期或未蓋章的遺失任務為錯誤。

### `maintenance`

bashCopy code
[code]
    openclaw tasks maintenance [--apply] [--json]
[/code]

預覽或套用任務與 Task Flow 協調、清理蓋章、修剪， 以及過期的 Cron 執行工作階段登錄清理。 對於 Cron 任務，協調會先使用持久化的執行記錄/工作狀態，然後才將 舊的作用中任務標記為 `lost`，因此已完成的 Cron 執行不會只因記憶體中的 Gateway 執行階段狀態消失 就變成錯誤的稽核錯誤。離線 CLI 稽核對 Gateway 的程序本機 Cron 作用中工作集合 不具權威性。具有執行 ID/來源 ID 的 CLI 任務會在其即時 Gateway 執行內容 消失時標記為 `lost`，即使仍有舊的子工作階段資料列存在。 套用後，維護也會修剪早於 7 天的 `cron:<jobId>:run:<uuid>` 工作階段登錄 資料列，同時保留目前執行中的 Cron 工作，並讓 非 Cron 工作階段資料列保持不變。

### `flow`

bashCopy code
[code]
    openclaw tasks flow list [--status <name>] [--json]openclaw tasks flow show <lookup> [--json]openclaw tasks flow cancel <lookup>
[/code]

檢查或取消任務分類帳下的持久性 Task Flow 狀態。

## 相關

  * [CLI 參考](</zh-TW/cli>)
  * [背景任務](</zh-TW/automation/tasks>)


Was this useful?YesNo