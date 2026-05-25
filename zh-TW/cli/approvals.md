---
title: 核准
source_url: https://docs.openclaw.ai/zh-TW/cli/approvals
scraped_at: 2026-05-25
---

# `openclaw approvals`

管理 **本機主機** 、**Gateway 主機** 或 **Node 主機** 的 exec 核准。 預設情況下，指令會以磁碟上的本機核准檔案為目標。使用 `--gateway` 以 Gateway 為目標，或使用 `--node` 以特定 Node 為目標。

別名：`openclaw exec-approvals`

相關：

  * Exec 核准：[Exec 核准](</zh-TW/tools/exec-approvals>)
  * Node：[Node](</zh-TW/nodes>)


## `openclaw exec-policy`

`openclaw exec-policy` 是一個本機便利指令，可一步保持要求的 `tools.exec.*` 設定與本機主機核准檔案一致。

在你想要執行以下操作時使用它：

  * 檢查本機要求的政策、主機核准檔案，以及有效合併結果
  * 套用本機預設集，例如 YOLO 或全部拒絕
  * 同步本機 `tools.exec.*` 與本機 `~/.openclaw/exec-approvals.json`


範例：

bashCopy code
[code]
    openclaw exec-policy showopenclaw exec-policy show --json openclaw exec-policy preset yoloopenclaw exec-policy preset cautious --json openclaw exec-policy set --host gateway --security full --ask off --ask-fallback full
[/code]

輸出模式：

  * 無 `--json`：列印人類可讀的表格檢視
  * `--json`：列印機器可讀的結構化輸出


目前範圍：

  * `exec-policy` **僅限本機**
  * 它會一起更新本機設定檔與本機核准檔案
  * 它**不會** 將政策推送到 Gateway 主機或 Node 主機
  * 此指令會拒絕 `--host node`，因為 Node exec 核准會在執行階段從 Node 擷取，而且必須改由以 Node 為目標的核准指令管理
  * `openclaw exec-policy show` 會將 `host=node` 範圍標示為執行階段由 Node 管理，而不是從本機核准檔案推導有效政策


如果你需要直接編輯遠端主機核准，請繼續使用 `openclaw approvals set --gateway` 或 `openclaw approvals set --node <id|name|ip>`。

## 常用指令

bashCopy code
[code]
    openclaw approvals getopenclaw approvals get --node <id|name|ip>openclaw approvals get --gateway
[/code]

`openclaw approvals get` 現在會顯示本機、Gateway 與 Node 目標的有效 exec 政策：

  * 要求的 `tools.exec` 政策
  * 主機核准檔案政策
  * 套用優先順序規則後的有效結果


優先順序是刻意設計的：

  * 主機核准檔案是可強制執行的事實來源
  * 要求的 `tools.exec` 政策可以縮小或擴大意圖，但有效結果仍然由主機規則推導
  * `--node` 會將 Node 主機核准檔案與 Gateway `tools.exec` 政策結合，因為兩者在執行階段仍然適用
  * 如果 Gateway 設定無法使用，CLI 會退回使用 Node 核准快照，並註明無法計算最終執行階段政策


## 從檔案取代核准

bashCopy code
[code]
    openclaw approvals set --file ./exec-approvals.jsonopenclaw approvals set --stdin <<'EOF'{ version: 1, defaults: { security: "full", ask: "off" } }EOFopenclaw approvals set --node <id|name|ip> --file ./exec-approvals.jsonopenclaw approvals set --gateway --file ./exec-approvals.json
[/code]

`set` 接受 JSON5，不只接受嚴格 JSON。請使用 `--file` 或 `--stdin` 其中之一，不要同時使用兩者。

##「永不提示」/ YOLO 範例

對於不應因 exec 核准而停止的主機，請將主機核准預設值設為 `full` \+ `off`：

bashCopy code
[code]
    openclaw approvals set --stdin <<'EOF'{  version: 1,  defaults: {    security: "full",    ask: "off",    askFallback: "full"  }}EOF
[/code]

Node 變體：

bashCopy code
[code]
    openclaw approvals set --node <id|name|ip> --stdin <<'EOF'{  version: 1,  defaults: {    security: "full",    ask: "off",    askFallback: "full"  }}EOF
[/code]

這只會變更**主機核准檔案** 。若要讓要求的 OpenClaw 政策保持一致，另請設定：

bashCopy code
[code]
    openclaw config set tools.exec.host gatewayopenclaw config set tools.exec.security fullopenclaw config set tools.exec.ask off
[/code]

此範例中為何使用 `tools.exec.host=gateway`：

  * `host=auto` 仍然表示「可用時使用沙盒，否則使用 Gateway」。
  * YOLO 關乎核准，而不是路由。
  * 如果即使已設定沙盒仍想要使用主機 exec，請使用 `gateway` 或 `/exec host=gateway` 明確指定主機選擇。


這符合目前的主機預設 YOLO 行為。如果你想要核准，請收緊它。

本機捷徑：

bashCopy code
[code]
    openclaw exec-policy preset yolo
[/code]

該本機捷徑會同時更新要求的本機 `tools.exec.*` 設定與 本機核准預設值。其意圖等同於上方的手動兩步驟 設定，但僅適用於本機。

## 允許清單輔助工具

bashCopy code
[code]
    openclaw approvals allowlist add "~/Projects/**/bin/rg"openclaw approvals allowlist add --agent main --node <id|name|ip> "/usr/bin/uptime"openclaw approvals allowlist add --agent "*" "/usr/bin/uname" openclaw approvals allowlist remove "~/Projects/**/bin/rg"
[/code]

## 常用選項

`get`、`set` 與 `allowlist add|remove` 全都支援：

  * `--node <id|name|ip>`
  * `--gateway`
  * 共用 Node RPC 選項：`--url`、`--token`、`--timeout`、`--json`


目標指定注意事項：

  * 沒有目標旗標表示使用磁碟上的本機核准檔案
  * `--gateway` 以 Gateway 主機核准檔案為目標
  * `--node` 在解析 ID、名稱、IP 或 ID 前綴後，以一個 Node 主機為目標


`allowlist add|remove` 也支援：

  * `--agent <id>`（預設為 `*`）


## 注意事項

  * `--node` 使用與 `openclaw nodes` 相同的解析器（ID、名稱、IP 或 ID 前綴）。
  * `--agent` 預設為 `"*"`，會套用至所有代理。
  * Node 主機必須通告 `system.execApprovals.get/set`（macOS app 或 headless Node 主機）。
  * 核准檔案會依每個主機儲存在 `~/.openclaw/exec-approvals.json`。


## 相關

  * [CLI 參考](</zh-TW/cli>)
  * [Exec 核准](</zh-TW/tools/exec-approvals>)


Was this useful?YesNo