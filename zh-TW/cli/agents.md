---
title: 代理
source_url: https://docs.openclaw.ai/zh-TW/cli/agents
scraped_at: 2026-05-25
---

# `openclaw agents`

管理隔離的代理（工作區 + 驗證 + 路由）。

相關：

  * [多代理路由](</zh-TW/concepts/multi-agent>)
  * [代理工作區](</zh-TW/concepts/agent-workspace>)
  * [Skills 設定](</zh-TW/tools/skills-config>)：Skills 可見性設定。


## 範例

bashCopy code
[code]
    openclaw agents listopenclaw agents list --bindingsopenclaw agents add work --workspace ~/.openclaw/workspace-workopenclaw agents add ops --workspace ~/.openclaw/workspace-ops --bind telegram:ops --non-interactiveopenclaw agents bindingsopenclaw agents bind --agent work --bind telegram:opsopenclaw agents unbind --agent work --bind telegram:opsopenclaw agents set-identity --workspace ~/.openclaw/workspace --from-identityopenclaw agents set-identity --agent main --avatar avatars/openclaw.pngopenclaw agents delete work
[/code]

## 路由繫結

使用路由繫結，將傳入的頻道流量固定到特定代理。

如果你也想讓每個代理有不同的可見 Skills，請在 `openclaw.json` 中設定 `agents.defaults.skills` 和 `agents.list[].skills`。請參閱 [Skills 設定](</zh-TW/tools/skills-config>)與[設定參考](</zh-TW/gateway/config-agents#agents-defaults-skills>)。

列出繫結：

bashCopy code
[code]
    openclaw agents bindingsopenclaw agents bindings --agent workopenclaw agents bindings --json
[/code]

新增繫結：

bashCopy code
[code]
    openclaw agents bind --agent work --bind telegram:ops --bind discord:guild-a
[/code]

如果省略 `accountId`（`--bind <channel>`），OpenClaw 會在可用時從頻道預設值和 Plugin 設定 Hook 解析它。

如果對 `bind` 或 `unbind` 省略 `--agent`，OpenClaw 會以目前的預設代理作為目標。

### 繫結範圍行為

  * 不含 `accountId` 的繫結只會比對頻道預設帳號。
  * `accountId: "*"` 是整個頻道的備援（所有帳號），且比明確帳號繫結更不具體。
  * 如果同一個代理已經有一個不含 `accountId` 的相符頻道繫結，而你稍後用明確或已解析的 `accountId` 進行繫結，OpenClaw 會就地升級該既有繫結，而不是新增重複項目。


範例：

bashCopy code
[code]
    # 初始的僅頻道繫結openclaw agents bind --agent work --bind telegram # 稍後升級為帳號範圍繫結openclaw agents bind --agent work --bind telegram:ops
[/code]

升級後，該繫結的路由範圍會限定為 `telegram:ops`。如果也想要預設帳號路由，請明確新增它（例如 `--bind telegram:default`）。

移除繫結：

bashCopy code
[code]
    openclaw agents unbind --agent work --bind telegram:opsopenclaw agents unbind --agent work --all
[/code]

`unbind` 接受 `--all` 或一個以上的 `--bind` 值，但不能同時使用兩者。

## 命令介面

### `agents`

執行不帶子命令的 `openclaw agents` 等同於 `openclaw agents list`。

### `agents list`

選項：

  * `--json`
  * `--bindings`：包含完整路由規則，而不只是每個代理的計數/摘要


### `agents add [name]`

選項：

  * `--workspace <dir>`
  * `--model <id>`
  * `--agent-dir <dir>`
  * `--bind <channel[:accountId]>`（可重複）
  * `--non-interactive`
  * `--json`


注意事項：

  * 傳入任何明確的新增旗標，會將命令切換到非互動式路徑。
  * 非互動模式需要代理名稱和 `--workspace`。
  * `main` 為保留字，不能用作新的代理 ID。
  * 在互動模式中，驗證植入只會複製可攜式靜態設定檔 （預設為 `api_key` 和靜態 `token`）。OAuth 重新整理權杖設定檔仍然 只能透過從實際 `main` 代理儲存區讀取繼承來使用。 如果設定的預設代理不是 `main`，請針對新代理另外登入 OAuth 設定檔。


### `agents bindings`

選項：

  * `--agent <id>`
  * `--json`


### `agents bind`

選項：

  * `--agent <id>`（預設為目前的預設代理）
  * `--bind <channel[:accountId]>`（可重複）
  * `--json`


### `agents unbind`

選項：

  * `--agent <id>`（預設為目前的預設代理）
  * `--bind <channel[:accountId]>`（可重複）
  * `--all`
  * `--json`


### `agents delete <id>`

選項：

  * `--force`
  * `--json`


注意事項：

  * `main` 不能刪除。
  * 若未使用 `--force`，需要互動式確認。
  * 工作區、代理狀態和工作階段轉錄目錄會移到垃圾桶，而不是硬刪除。
  * 當 Gateway 可連線時，刪除會透過 Gateway 傳送，讓設定和工作階段儲存區清理與執行階段流量共用同一個寫入者。如果無法連線到 Gateway，CLI 會退回離線本機路徑。
  * 如果另一個代理的工作區是相同路徑、位於此工作區內，或包含此工作區， 則會保留該工作區，而 `--json` 會回報 `workspaceRetained`、 `workspaceRetainedReason` 和 `workspaceSharedWith`。


## 身分檔案

每個代理工作區都可以在工作區根目錄包含 `IDENTITY.md`：

  * 範例路徑：`~/.openclaw/workspace/IDENTITY.md`
  * `set-identity --from-identity` 會從工作區根目錄讀取（或從明確的 `--identity-file` 讀取）


頭像路徑會相對於工作區根目錄解析。

## 設定身分

`set-identity` 會將欄位寫入 `agents.list[].identity`：

  * `name`
  * `theme`
  * `emoji`
  * `avatar`（工作區相對路徑、http(s) URL，或資料 URI）


選項：

  * `--agent <id>`
  * `--workspace <dir>`
  * `--identity-file <path>`
  * `--from-identity`
  * `--name <name>`
  * `--theme <theme>`
  * `--emoji <emoji>`
  * `--avatar <value>`
  * `--json`


注意事項：

  * 可以使用 `--agent` 或 `--workspace` 來選取目標代理。
  * 如果你依賴 `--workspace`，且多個代理共用該工作區，命令會失敗並要求你傳入 `--agent`。
  * 如果未提供明確的身分欄位，命令會從 `IDENTITY.md` 讀取身分資料。


從 `IDENTITY.md` 載入：

bashCopy code
[code]
    openclaw agents set-identity --workspace ~/.openclaw/workspace --from-identity
[/code]

明確覆寫欄位：

bashCopy code
[code]
    openclaw agents set-identity --agent main --name "OpenClaw" --emoji "🦞" --avatar avatars/openclaw.png
[/code]

設定範例：

json5Copy code
[code]
    {  agents: {    list: [      {        id: "main",        identity: {          name: "OpenClaw",          theme: "space lobster",          emoji: "🦞",          avatar: "avatars/openclaw.png",        },      },    ],  },}
[/code]

## 相關

  * [CLI 參考](</zh-TW/cli>)
  * [多代理路由](</zh-TW/concepts/multi-agent>)
  * [代理工作區](</zh-TW/concepts/agent-workspace>)


Was this useful?YesNo