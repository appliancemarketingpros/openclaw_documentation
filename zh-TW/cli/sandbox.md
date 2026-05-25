---
title: 沙盒 CLI
source_url: https://docs.openclaw.ai/zh-TW/cli/sandbox
scraped_at: 2026-05-25
---

管理用於隔離代理執行的沙盒執行階段。

## 概觀

OpenClaw 可以在隔離的沙盒執行階段中執行代理以提升安全性。`sandbox` 指令可協助你在更新或設定變更後，檢查並重新建立這些執行階段。

目前這通常表示：

  * Docker 沙盒容器
  * 當 `agents.defaults.sandbox.backend = "ssh"` 時的 SSH 沙盒執行階段
  * 當 `agents.defaults.sandbox.backend = "openshell"` 時的 OpenShell 沙盒執行階段


對於 `ssh` 和 OpenShell `remote`，重新建立比 Docker 更重要：

  * 初始種子建立後，遠端工作區就是權威來源
  * `openclaw sandbox recreate` 會刪除所選範圍的權威遠端工作區
  * 下次使用時會再次從目前的本機工作區建立種子


## 指令

### `openclaw sandbox explain`

檢查**有效的** 沙盒模式/範圍/工作區存取權、沙盒工具政策，以及提升權限閘門（含修正用設定鍵路徑）。

bashCopy code
[code]
    openclaw sandbox explainopenclaw sandbox explain --session agent:main:mainopenclaw sandbox explain --agent workopenclaw sandbox explain --json
[/code]

### `openclaw sandbox list`

列出所有沙盒執行階段及其狀態與設定。

bashCopy code
[code]
    openclaw sandbox listopenclaw sandbox list --browser  # List only browser containersopenclaw sandbox list --json     # JSON output
[/code]

**輸出包含：**

  * 執行階段名稱與狀態
  * 後端（`docker`、`openshell` 等）
  * 設定標籤，以及它是否符合目前設定
  * 存在時間（自建立以來的時間）
  * 閒置時間（自上次使用以來的時間）
  * 關聯的工作階段/代理


### `openclaw sandbox recreate`

移除沙盒執行階段，以強制使用更新後的設定重新建立。

bashCopy code
[code]
    openclaw sandbox recreate --all                # Recreate all containersopenclaw sandbox recreate --session main       # Specific sessionopenclaw sandbox recreate --agent mybot        # Specific agentopenclaw sandbox recreate --browser            # Only browser containersopenclaw sandbox recreate --all --force        # Skip confirmation
[/code]

**選項：**

  * `--all`：重新建立所有沙盒容器
  * `--session <key>`：重新建立特定工作階段的容器
  * `--agent <id>`：重新建立特定代理的容器
  * `--browser`：只重新建立瀏覽器容器
  * `--force`：略過確認提示


## 使用案例

### 更新 Docker 映像後

bashCopy code
[code]
    # Pull new imagedocker pull openclaw-sandbox:latestdocker tag openclaw-sandbox:latest openclaw-sandbox:bookworm-slim # Update config to use new image# Edit config: agents.defaults.sandbox.docker.image (or agents.list[].sandbox.docker.image) # Recreate containersopenclaw sandbox recreate --all
[/code]

### 變更沙盒設定後

bashCopy code
[code]
    # Edit config: agents.defaults.sandbox.* (or agents.list[].sandbox.*) # Recreate to apply new configopenclaw sandbox recreate --all
[/code]

### 變更 SSH 目標或 SSH 驗證材料後

bashCopy code
[code]
    # Edit config:# - agents.defaults.sandbox.backend# - agents.defaults.sandbox.ssh.target# - agents.defaults.sandbox.ssh.workspaceRoot# - agents.defaults.sandbox.ssh.identityFile / certificateFile / knownHostsFile# - agents.defaults.sandbox.ssh.identityData / certificateData / knownHostsData openclaw sandbox recreate --all
[/code]

對於核心 `ssh` 後端，重新建立會刪除 SSH 目標上每個範圍的遠端工作區根目錄。下次執行時會再次從本機工作區建立種子。

### 變更 OpenShell 來源、政策或模式後

bashCopy code
[code]
    # Edit config:# - agents.defaults.sandbox.backend# - plugins.entries.openshell.config.from# - plugins.entries.openshell.config.mode# - plugins.entries.openshell.config.policy openclaw sandbox recreate --all
[/code]

對於 OpenShell `remote` 模式，重新建立會刪除該範圍的權威遠端工作區。下次執行時會再次從本機工作區建立種子。

### 變更 setupCommand 後

bashCopy code
[code]
    openclaw sandbox recreate --all# or just one agent:openclaw sandbox recreate --agent family
[/code]

### 只針對特定代理

bashCopy code
[code]
    # Update only one agent's containersopenclaw sandbox recreate --agent alfred
[/code]

## 為什麼需要這麼做

當你更新沙盒設定時：

  * 現有執行階段會繼續使用舊設定執行。
  * 執行階段只會在閒置 24 小時後被清除。
  * 經常使用的代理會讓舊執行階段無限期保持存活。


使用 `openclaw sandbox recreate` 強制移除舊執行階段。它們會在下次需要時以目前設定自動重新建立。

## 登錄遷移

OpenClaw 會在沙盒狀態目錄下，以每個容器/瀏覽器項目一個 JSON 分片的形式儲存沙盒執行階段中繼資料。較舊的安裝可能仍有整體式舊版檔案：

  * `~/.openclaw/sandbox/containers.json`
  * `~/.openclaw/sandbox/browsers.json`


一般沙盒執行階段讀取不會重新寫入那些檔案。執行 `openclaw doctor --fix`，將有效的舊版項目遷移到分片式登錄目錄中。無效的舊版檔案會被隔離，避免單一損壞的舊登錄隱藏目前的執行階段項目。

## 設定

沙盒設定位於 `~/.openclaw/openclaw.json` 的 `agents.defaults.sandbox` 下（每個代理的覆寫設定放在 `agents.list[].sandbox`）：

jsoncCopy code
[code]
    {  "agents": {    "defaults": {      "sandbox": {        "mode": "all", // off, non-main, all        "backend": "docker", // docker, ssh, openshell        "scope": "agent", // session, agent, shared        "docker": {          "image": "openclaw-sandbox:bookworm-slim",          "containerPrefix": "openclaw-sbx-",          // ... more Docker options        },        "prune": {          "idleHours": 24, // Auto-prune after 24h idle          "maxAgeDays": 7, // Auto-prune after 7 days        },      },    },  },}
[/code]

## 相關

  * [CLI 參考](</zh-TW/cli>)
  * [沙盒化](</zh-TW/gateway/sandboxing>)
  * [代理工作區](</zh-TW/concepts/agent-workspace>)
  * [Doctor](</zh-TW/gateway/doctor>)：檢查沙盒設定。


Was this useful?YesNo