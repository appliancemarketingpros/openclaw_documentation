---
title: 流程（重新導向）
source_url: https://docs.openclaw.ai/zh-TW/cli/flows
scraped_at: 2026-05-25
---

# `openclaw tasks flow`

沒有頂層的 `openclaw flows` 命令。持久化 TaskFlow 檢視位於 `openclaw tasks flow` 之下。

## 子命令

bashCopy code
[code]
    openclaw tasks flow list   [--json] [--status <name>]openclaw tasks flow show   <lookup> [--json]openclaw tasks flow cancel <lookup>
[/code]

子命令 | 說明 | 引數 / 選項  
---|---|---  
`list` | 列出追蹤的 TaskFlow。 | `--json` 機器可讀輸出；`--status <name>` 篩選器（請參閱下方狀態值）。  
`show` | 顯示一個 TaskFlow。 | `<lookup>` 流程 ID 或擁有者鍵；`--json` 機器可讀輸出。  
`cancel` | 取消執行中的 TaskFlow。 | `<lookup>` 流程 ID 或擁有者鍵。  
  
`<lookup>` 接受流程 ID（由 `list` / `show` 傳回）或流程的擁有者鍵（擁有該流程的子系統用來追蹤流程的穩定識別碼）。

### 狀態篩選值

`list` 上的 `--status` 接受以下其中之一：

`queued`, `running`, `waiting`, `blocked`, `succeeded`, `failed`, `cancelled`, `lost`

## 範例

bashCopy code
[code]
    openclaw tasks flow listopenclaw tasks flow list --status runningopenclaw tasks flow list --jsonopenclaw tasks flow show flow_abc123openclaw tasks flow show flow_abc123 --jsonopenclaw tasks flow cancel flow_abc123
[/code]

如需完整的 TaskFlow 概念與撰寫方式，請參閱 [TaskFlow](</zh-TW/automation/taskflow>)。如需父層 `tasks` 命令，請參閱 [tasks CLI 參考](</zh-TW/cli/tasks>)。

## 相關

  * [CLI 參考](</zh-TW/cli>)
  * [自動化](</zh-TW/automation>)
  * [TaskFlow](</zh-TW/automation/taskflow>)


Was this useful?YesNo