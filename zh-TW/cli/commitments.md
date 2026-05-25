---
title: `openclaw commitments`
source_url: https://docs.openclaw.ai/zh-TW/cli/commitments
scraped_at: 2026-05-25
---

列出並管理推斷出的後續承諾。

承諾是選用、短期存在的後續記憶，從對話情境建立。概念指南請參閱[推斷承諾](</zh-TW/concepts/commitments>)。

未指定子命令時，`openclaw commitments` 會列出待處理的承諾。

## 用法

bashCopy code
[code]
    openclaw commitments [--all] [--agent <id>] [--status <status>] [--json]openclaw commitments list [--all] [--agent <id>] [--status <status>] [--json]openclaw commitments dismiss <id...> [--json]
[/code]

## 選項

  * `--all`：顯示所有狀態，而不只顯示待處理的承諾。
  * `--agent <id>`：篩選至一個代理程式 ID。
  * `--status <status>`：依狀態篩選。值：`pending`、`sent`、 `dismissed`、`snoozed` 或 `expired`。
  * `--json`：輸出機器可讀的 JSON。


## 範例

列出待處理的承諾：

bashCopy code
[code]
    openclaw commitments
[/code]

列出每個已儲存的承諾：

bashCopy code
[code]
    openclaw commitments --all
[/code]

篩選至一個代理程式：

bashCopy code
[code]
    openclaw commitments --agent main
[/code]

尋找已延後的承諾：

bashCopy code
[code]
    openclaw commitments --status snoozed
[/code]

關閉一或多個承諾：

bashCopy code
[code]
    openclaw commitments dismiss cm_abc123 cm_def456
[/code]

匯出為 JSON：

bashCopy code
[code]
    openclaw commitments --all --json
[/code]

## 輸出

文字輸出包含：

  * 承諾 ID
  * 狀態
  * 種類
  * 最早到期時間
  * 範圍
  * 建議的確認文字


JSON 輸出也包含承諾儲存區路徑和完整的已儲存記錄。

## 相關

  * [推斷承諾](</zh-TW/concepts/commitments>)
  * [記憶概觀](</zh-TW/concepts/memory>)
  * [Heartbeat](</zh-TW/gateway/heartbeat>)
  * [排程工作](</zh-TW/automation/cron-jobs>)


Was this useful?YesNo