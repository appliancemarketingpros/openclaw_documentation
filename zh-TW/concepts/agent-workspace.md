---
title: 代理工作區
source_url: https://docs.openclaw.ai/zh-TW/concepts/agent-workspace
scraped_at: 2026-05-25
---

工作區是代理的家。它是檔案工具與工作區情境唯一使用的工作目錄。請保持私密，並將它視為記憶。

這與 `~/.openclaw/` 分開，後者儲存設定、憑證與工作階段。

## 預設位置

  * 預設：`~/.openclaw/workspace`
  * 如果已設定 `OPENCLAW_PROFILE` 且不是 `"default"`，預設會變成 `~/.openclaw/workspace-<profile>`。
  * 在 `~/.openclaw/openclaw.json` 中覆寫：

json5Copy code
[code]
    {  agents: {    defaults: {      workspace: "~/.openclaw/workspace",    },  },}
[/code]

如果缺少工作區與啟動檔案，`openclaw onboard`、`openclaw configure` 或 `openclaw setup` 會建立它們並植入啟動檔案。

如果你已自行管理工作區檔案，可以停用啟動檔案建立：

json5Copy code
[code]
    { agents: { defaults: { skipBootstrap: true } } }
[/code]

## 額外工作區資料夾

較舊的安裝可能建立了 `~/openclaw`。保留多個工作區目錄可能造成令人困惑的驗證或狀態漂移，因為同一時間只有一個工作區是作用中的。

## 工作區檔案對照表

以下是 OpenClaw 預期在工作區內找到的標準檔案：

AGENTS.md - 操作指示

給代理的操作指示，以及它應如何使用記憶。每個工作階段開始時載入。適合放置規則、優先順序與「如何表現」等細節。

SOUL.md - 人格與語氣

人格、語氣與邊界。每個工作階段都會載入。指南：[SOUL.md 人格指南](</zh-TW/concepts/soul>)。

USER.md - 使用者是誰

使用者是誰，以及如何稱呼他們。每個工作階段都會載入。

IDENTITY.md - 名稱、氣質、emoji

代理的名稱、氣質與 emoji。在啟動儀式期間建立/更新。

TOOLS.md - 本機工具慣例

關於你的本機工具與慣例的備註。不控制工具可用性；僅作為指引。

HEARTBEAT.md - Heartbeat 檢查清單

Heartbeat 執行用的選用小型檢查清單。保持簡短以避免消耗 token。

BOOT.md - 啟動檢查清單

在 Gateway 重新啟動時自動執行的選用啟動檢查清單（當[內部 hooks](</zh-TW/automation/hooks>) 已啟用時）。保持簡短；使用訊息工具傳送對外訊息。

BOOTSTRAP.md - 首次執行儀式

一次性的首次執行儀式。只會為全新工作區建立。儀式完成後請刪除它。

memory/YYYY-MM-DD.md - 每日記憶紀錄

每日記憶紀錄（每天一個檔案）。建議在工作階段開始時讀取今天 + 昨天。

MEMORY.md - 精選長期記憶（選用）

精選長期記憶：持久事實、偏好、決策與短摘要。將詳細紀錄保存在 `memory/YYYY-MM-DD.md`，讓記憶工具可按需擷取，而不需注入每個 prompt。只在主要的私密工作階段載入 `MEMORY.md`（不要在共享/群組情境載入）。請參閱 [Memory](</zh-TW/concepts/memory>) 了解工作流程與自動記憶 flush。

skills/ - 工作區 Skills（選用）

工作區專屬 Skills。該工作區最高優先權的 skill 位置。當名稱衝突時，會覆寫專案代理 skills、個人代理 skills、受管理 skills、內建 skills，以及 `skills.load.extraDirs`。

canvas/ - Canvas UI 檔案（選用）

用於節點顯示的 Canvas UI 檔案（例如 `canvas/index.html`）。

## 哪些內容不在工作區中

這些位於 `~/.openclaw/` 下，不應提交到工作區 repo：

  * `~/.openclaw/openclaw.json`（設定）
  * `~/.openclaw/agents/<agentId>/agent/auth-profiles.json`（模型驗證設定檔：OAuth + API keys）
  * `~/.openclaw/agents/<agentId>/agent/codex-home/`（每個代理的 Codex runtime 帳號、設定、skills、plugins 與原生 thread 狀態）
  * `~/.openclaw/credentials/`（頻道/提供者狀態，以及舊版 OAuth 匯入資料）
  * `~/.openclaw/agents/<agentId>/sessions/`（工作階段逐字稿 + metadata）
  * `~/.openclaw/skills/`（受管理 skills）


如果你需要遷移工作階段或設定，請分開複製，並讓它們保持在版本控制之外。

## Git 備份（建議，私密）

將工作區視為私密記憶。把它放在**私密** git repo 中，讓它可備份且可復原。

在 Gateway 執行所在的機器上執行以下步驟（也就是工作區所在的位置）。

* ### 初始化 repo

如果已安裝 git，全新工作區會自動初始化。如果此工作區尚不是 repo，請執行：

bashCopy code
[code]
    cd ~/.openclaw/workspacegit initgit add AGENTS.md SOUL.md TOOLS.md IDENTITY.md USER.md HEARTBEAT.md memory/git commit -m "Add agent workspace"
[/code]

* ### 新增私密 remote

### GitHub web UI

  1. 在 GitHub 上建立新的**私密** 儲存庫。
  2. 不要使用 README 初始化（避免 merge conflicts）。
  3. 複製 HTTPS remote URL。
  4. 新增 remote 並推送：

bashCopy code
[code]
    git branch -M maingit remote add origin <https-url>git push -u origin main
[/code]

### GitHub CLI (gh)

bashCopy code
[code]
    gh auth logingh repo create openclaw-workspace --private --source . --remote origin --push
[/code]

### GitLab web UI

  1. 在 GitLab 上建立新的**私密** 儲存庫。
  2. 不要使用 README 初始化（避免 merge conflicts）。
  3. 複製 HTTPS remote URL。
  4. 新增 remote 並推送：

bashCopy code
[code]
    git branch -M maingit remote add origin <https-url>git push -u origin main
[/code]

* ### 持續更新

bashCopy code
[code]
    git statusgit add .git commit -m "Update memory"git push
[/code]

## 不要提交秘密

建議的 `.gitignore` 起始內容：

gitignoreCopy code
[code]
    .DS_Store.env**/*.key**/*.pem**/secrets*
[/code]

## 將工作區移到新機器

* ### Clone repo

將 repo clone 到想要的路徑（預設 `~/.openclaw/workspace`）。

* ### 更新設定

在 `~/.openclaw/openclaw.json` 中將 `agents.defaults.workspace` 設為該路徑。

* ### 植入缺少的檔案

執行 `openclaw setup --workspace <path>` 以植入任何缺少的檔案。

* ### 複製工作階段（選用）

如果你需要工作階段，請從舊機器分開複製 `~/.openclaw/agents/<agentId>/sessions/`。

## 進階備註

  * 多代理路由可為每個代理使用不同工作區。請參閱 [Channel routing](</zh-TW/channels/channel-routing>) 了解路由設定。
  * 如果已啟用 `agents.defaults.sandbox`，非主要工作階段可使用 `agents.defaults.sandbox.workspaceRoot` 下的個別工作階段沙盒工作區。


## 相關

  * [Heartbeat](</zh-TW/gateway/heartbeat>) \- [HEARTBEAT.md](<http://HEARTBEAT.md>) 工作區檔案
  * [Sandboxing](</zh-TW/gateway/sandboxing>) \- 沙盒環境中的工作區存取
  * [Session](</zh-TW/concepts/session>) \- 工作階段儲存路徑
  * [Standing orders](</zh-TW/automation/standing-orders>) \- 工作區檔案中的持久指示


Was this useful?YesNo