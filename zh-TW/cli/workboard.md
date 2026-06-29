---
title: Workboard 命令列介面
source_url: https://docs.openclaw.ai/zh-TW/cli/workboard
scraped_at: 2026-06-29
---

ReferenceCLI commands

`openclaw workboard` 是內建 [Workboard 外掛](</zh-TW/plugins/workboard>)的終端介面。它讓操作者列出卡片、建立 卡片、檢視單一卡片，並要求執行中的閘道將已就緒的工作分派到 子代理工作執行。

使用命令前請先啟用外掛：

bashCopy code
[code]
    openclaw plugins enable workboardopenclaw gateway restart
[/code]

## 使用方式

bashCopy code
[code]
    openclaw workboard list [--board <id>] [--status <status>] [--include-archived] [--json]openclaw workboard create <title...> [--notes <text>] [--status <status>] [--priority <priority>] [--agent <id>] [--board <id>] [--labels <items>] [--json]openclaw workboard show <id> [--json]openclaw workboard dispatch [--url <url>] [--token <token>] [--timeout <ms>] [--json]
[/code]

此命令會讀寫與儀表板和 Workboard 代理工具使用的同一個外掛所屬 SQLite 資料庫。當命令接受卡片 id 時，卡片 id 可以傳入完整 id，或傳入不會造成歧義的 前綴。

## `list`

bashCopy code
[code]
    openclaw workboard listopenclaw workboard list --board default --status readyopenclaw workboard list --json
[/code]

文字輸出很精簡：

textCopy code
[code]
    7f4a2c10  ready     high    default agent-a  Fix stale worker heartbeat
[/code]

欄位依序為 id 前綴、狀態、優先順序、看板 id、選用代理 id，以及標題。

旗標：

旗標 | 用途  
---|---  
`--board <id>` | 將結果限制在單一看板命名空間  
`--status <status>` | 將結果限制在單一 Workboard 狀態  
`--include-archived` | 在精簡文字輸出中包含已封存卡片  
`--json` | 以機器 JSON 列印完整卡片清單  
  
精簡文字輸出預設會隱藏已封存卡片，讓命令列介面與 `/workboard list` 命令一致。傳入 `--include-archived` 可顯示它們。JSON 輸出 會保留完整卡片清單，包括已封存卡片，以支援既有自動化。

## `create`

bashCopy code
[code]
    openclaw workboard create "Fix stale worker heartbeat" --priority high --labels bug,workboardopenclaw workboard create "Write Workboard docs" --status ready --agent docs-agent --board docs --notes "Cover CLI, slash command, dispatch, and SQLite state."
[/code]

旗標：

旗標 | 用途  
---|---  
`--notes <text>` | 初始卡片備註  
`--status <status>` | 初始狀態，預設為 `todo`  
`--priority <priority>` | 優先順序，預設為 `normal`  
`--agent <id>` | 將卡片指派給代理或擁有者 id  
`--board <id>` | 將卡片儲存在看板命名空間  
`--labels <items>` | 逗號分隔的標籤  
`--json` | 以機器 JSON 列印已建立的卡片  
  
`create` 會直接寫入 Workboard SQLite 狀態。卡片會立即顯示在控制介面的 Workboard 分頁中，也會立即提供給 Workboard 工具使用。

## `show`

bashCopy code
[code]
    openclaw workboard show 7f4a2c10openclaw workboard show 7f4a2c10 --json
[/code]

文字輸出會列印精簡卡片列與備註。JSON 輸出會回傳完整卡片記錄，包括執行中繼資料、 嘗試次數、留言、連結、證明、成品、工作者日誌、協定狀態、診斷資訊，以及自動化 中繼資料。

## `dispatch`

bashCopy code
[code]
    openclaw workboard dispatchopenclaw workboard dispatch --jsonopenclaw workboard dispatch --url http://127.0.0.1:18789 --token "$OPENCLAW_GATEWAY_TOKEN"
[/code]

`dispatch` 會先呼叫執行中閘道的 RPC 方法 `workboard.cards.dispatch`。該路徑使用與儀表板分派動作相同的子代理執行階段， 因此已就緒卡片會變成帶有任務追蹤的工作者執行，並連結工作階段金鑰。已指派代理的 卡片會使用代理範圍的子代理工作階段金鑰；未指派卡片會保留未限定範圍的子代理金鑰， 以保留閘道設定的預設代理。

分派迴圈：

  1. 將相依項目已就緒的子項提升為 `ready`。
  2. 封鎖已過期的宣告或逾時的工作者執行。
  3. 在已就緒卡片上記錄分派中繼資料。
  4. 選取一小批未宣告的已就緒卡片。
  5. 為分派器或已指派代理宣告每張選取的卡片。
  6. 使用受限的卡片情境與卡片宣告權杖啟動子代理工作者執行。
  7. 在卡片上儲存工作者執行 id、工作階段金鑰、閘道任務帳本回報時的任務連結、 執行狀態，以及工作者日誌。


選取策略刻意保守。一次分派預設最多啟動三個工作者，會略過已封存或已被宣告的卡片， 而且單次處理只會為每個擁有者或代理啟動一張卡片。已由執行中或審查中的工作擁有的 卡片，會留待稍後的分派處理。

如果卡片已被宣告後工作者啟動失敗，Workboard 會封鎖該卡片、清除宣告，並在卡片執行 與工作者日誌中繼資料中記錄失敗。這會讓啟動失敗保持可見，而不是靜默地把卡片退回 佇列。

如果未提供明確的閘道目標，且本機閘道無法使用或尚未公開 Workboard 分派方法，命令列介面 會退回到只針對本機 Workboard 狀態進行資料分派。純資料分派仍可提升相依項目、清理過期 宣告，並封鎖逾時執行，但不會啟動工作者。驗證、權限、驗證失敗，以及明確 `--url` 或 `--token` 目標的失敗會直接回報。

文字輸出會回報工作者啟動：

textCopy code
[code]
    dispatch complete: started=2 failures=0
[/code]

後援輸出會明確標示：

textCopy code
[code]
    gateway unavailable; data dispatch only: promoted=1 blocked=0
[/code]

JSON 輸出會包含分派結果。由閘道支援的分派可包含 `started` 和 `startFailures`；純資料後援會包含 `gatewayUnavailable: true`。卡片 JSON 輸出中的宣告權杖會被遮蔽。

在儀表板中，同一個分派結果會以簡短摘要顯示，讓操作者不必開啟卡片詳細資料，就能看到 已啟動、提升、封鎖、重新宣告或失敗的卡片數量。

## 斜線命令對等性

支援命令的通道可以使用對應的斜線命令：

textCopy code
[code]
    /workboard list/workboard show 7f4a2c10/workboard create Fix stale worker heartbeat/workboard dispatch
[/code]

斜線命令分派也使用閘道子代理執行階段，因此會遵循與儀表板和命令列介面閘道路徑相同的 宣告、工作者啟動與失敗行為。

`/workboard list` 和 `/workboard show` 是提供給已授權命令傳送者的讀取命令。 `/workboard create` 和 `/workboard dispatch` 會變更看板狀態，在聊天介面上需要擁有者身分， 或需要具備 `operator.write` 或 `operator.admin` 的閘道用戶端。

## 權限

命令列介面分派路徑會以 `operator.read` 和 `operator.write` 範圍呼叫閘道 RPC。唯讀閘道權杖可以透過讀取方法檢視 Workboard 資料， 但不能建立卡片或分派工作者。

本機 `list`、`create` 和 `show` 命令會操作目前設定檔使用的本機 OpenClaw 狀態目錄。 需要不同狀態根目錄時，請在頂層 `openclaw` 命令上使用 `--dev` 或 `--profile <name>`。

## 疑難排解

### 沒有顯示卡片

確認外掛已針對相同設定檔與狀態根目錄啟用：

bashCopy code
[code]
    openclaw plugins inspect workboard --runtime --json
[/code]

如果儀表板顯示卡片但命令列介面沒有，請檢查兩個命令是否使用相同的 `--dev` 或 `--profile` 設定。

### 分派顯示純資料

啟動或重新啟動閘道：

bashCopy code
[code]
    openclaw gateway restartopenclaw gateway status --deep
[/code]

然後重試 `openclaw workboard dispatch`。純資料後援適合本機狀態清理，但工作者執行需要 即時閘道。

### 分派沒有啟動任何項目

檢查至少有一張沒有作用中宣告的 `ready` 卡片：

bashCopy code
[code]
    openclaw workboard list --status ready
[/code]

當同一個擁有者已有執行中或審查中的工作時，卡片也可能被略過。請將已完成的工作移至 `done`，透過 Workboard 工具釋放過期宣告，或在作用中工作者完成後再次執行分派。

## 相關

  * [Workboard 外掛](</zh-TW/plugins/workboard>)
  * [命令列介面參考](</zh-TW/cli>)
  * [斜線命令](</zh-TW/tools/slash-commands>)
  * [控制介面](</zh-TW/web/control-ui>)


Was this useful?YesNo

Open issue