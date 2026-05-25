---
title: Node
source_url: https://docs.openclaw.ai/zh-TW/cli/nodes
scraped_at: 2026-05-25
---

# `openclaw nodes`

管理已配對的節點（裝置），並叫用節點能力。

相關：

  * 節點總覽：[節點](</zh-TW/nodes>)
  * 相機：[相機節點](</zh-TW/nodes/camera>)
  * 圖片：[圖片節點](</zh-TW/nodes/images>)


常用選項：

  * `--url`, `--token`, `--timeout`, `--json`


## 常用指令

bashCopy code
[code]
    openclaw nodes listopenclaw nodes list --connectedopenclaw nodes list --last-connected 24hopenclaw nodes pendingopenclaw nodes approve <requestId>openclaw nodes reject <requestId>openclaw nodes remove --node <id|name|ip>openclaw nodes rename --node <id|name|ip> --name <displayName>openclaw nodes statusopenclaw nodes status --connectedopenclaw nodes status --last-connected 24h
[/code]

`nodes list` 會列印待處理/已配對表格。已配對列包含最近連線時間（上次連線）。 使用 `--connected` 只顯示目前已連線的節點。使用 `--last-connected <duration>` 篩選出在某段時間內曾連線的節點（例如 `24h`、`7d`）。 使用 `nodes remove --node <id|name|ip>` 刪除過時的 Gateway 擁有節點配對記錄。

核准注意事項：

  * `openclaw nodes pending` 只需要配對範圍。
  * `gateway.nodes.pairing.autoApproveCidrs` 只會針對明確信任、首次的 `role: node` 裝置配對略過待處理步驟。預設為關閉，且不會核准升級。
  * `openclaw nodes approve <requestId>` 會從待處理請求繼承額外範圍需求： 
    * 無指令請求：僅配對
    * 非 exec 節點指令：配對 + 寫入
    * `system.run` / `system.run.prepare` / `system.which`：配對 + admin


## 叫用

bashCopy code
[code]
    openclaw nodes invoke --node <id|name|ip> --command <command> --params <json>
[/code]

叫用旗標：

  * `--params <json>`：JSON 物件字串（預設 `{}`）。
  * `--invoke-timeout <ms>`：節點叫用逾時（預設 `15000`）。
  * `--idempotency-key <key>`：選用的冪等性金鑰。
  * `system.run` 和 `system.run.prepare` 在這裡會被封鎖；若要執行 shell，請使用 `exec` 工具搭配 `host=node`。


若要在節點上執行 shell，請使用 `exec` 工具搭配 `host=node`，而不是 `openclaw nodes run`。 `nodes` CLI 現在專注於能力：透過 `nodes invoke` 直接 RPC，外加配對、相機、螢幕、位置、Canvas 和通知。Canvas 指令由隨附的實驗性 Canvas Plugin 實作；核心保留相容性掛鉤，因此它們仍位於 `openclaw nodes canvas` 之下。

## 相關

  * [CLI 參考](</zh-TW/cli>)
  * [節點](</zh-TW/nodes>)


Was this useful?YesNo