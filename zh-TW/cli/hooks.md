---
title: 掛鉤
source_url: https://docs.openclaw.ai/zh-TW/cli/hooks
scraped_at: 2026-05-25
---

# `openclaw hooks`

管理代理程式掛鉤（適用於 `/new`、`/reset` 和 Gateway 啟動等命令的事件驅動自動化）。

不帶子命令執行 `openclaw hooks` 等同於 `openclaw hooks list`。

相關：

  * 掛鉤：[掛鉤](</zh-TW/automation/hooks>)
  * Plugin 掛鉤：[Plugin 掛鉤](</zh-TW/plugins/hooks>)


## 列出所有掛鉤

bashCopy code
[code]
    openclaw hooks list
[/code]

列出從工作區、受管理、額外和內建目錄中發現的所有掛鉤。 Gateway 啟動時，至少要設定一個內部掛鉤後，才會載入內部掛鉤處理常式。

**選項：**

  * `--eligible`：只顯示合格的掛鉤（已符合需求）
  * `--json`：以 JSON 輸出
  * `-v, --verbose`：顯示詳細資訊，包括缺少的需求


**範例輸出：**

CodeCopy code
[code]
    Hooks (4/4 ready) Ready:  🚀 boot-md ✓ - Run BOOT.md on gateway startup  📎 bootstrap-extra-files ✓ - Inject extra workspace bootstrap files during agent bootstrap  📝 command-logger ✓ - Log all command events to a centralized audit file  💾 session-memory ✓ - Save session context to memory when /new or /reset command is issued
[/code]

**範例（詳細）：**

bashCopy code
[code]
    openclaw hooks list --verbose
[/code]

顯示不合格掛鉤缺少的需求。

**範例（JSON）：**

bashCopy code
[code]
    openclaw hooks list --json
[/code]

傳回結構化 JSON 供程式化使用。

## 取得掛鉤資訊

bashCopy code
[code]
    openclaw hooks info <name>
[/code]

顯示特定掛鉤的詳細資訊。

**引數：**

  * `<name>`：掛鉤名稱或掛鉤鍵（例如 `session-memory`）


**選項：**

  * `--json`：以 JSON 輸出


**範例：**

bashCopy code
[code]
    openclaw hooks info session-memory
[/code]

**輸出：**

CodeCopy code
[code]
    💾 session-memory ✓ Ready Save session context to memory when /new or /reset command is issued Details:  Source: openclaw-bundled  Path: /path/to/openclaw/hooks/bundled/session-memory/HOOK.md  Handler: /path/to/openclaw/hooks/bundled/session-memory/handler.ts  Homepage: https://docs.openclaw.ai/automation/hooks#session-memory  Events: command:new, command:reset Requirements:  Config: ✓ workspace.dir
[/code]

## 檢查掛鉤合格性

bashCopy code
[code]
    openclaw hooks check
[/code]

顯示掛鉤合格狀態摘要（已就緒與未就緒的數量）。

**選項：**

  * `--json`：以 JSON 輸出


**範例輸出：**

CodeCopy code
[code]
    Hooks Status Total hooks: 4Ready: 4Not ready: 0
[/code]

## 啟用掛鉤

bashCopy code
[code]
    openclaw hooks enable <name>
[/code]

透過將特定掛鉤加入設定來啟用它（預設為 `~/.openclaw/openclaw.json`）。

**注意：** 工作區掛鉤預設停用，直到在此處或設定中啟用為止。由 plugins 管理的掛鉤會在 `openclaw hooks list` 中顯示 `plugin:<id>`，且無法在此處啟用/停用。請改為啟用/停用該 plugin。

**引數：**

  * `<name>`：掛鉤名稱（例如 `session-memory`）


**範例：**

bashCopy code
[code]
    openclaw hooks enable session-memory
[/code]

**輸出：**

CodeCopy code
[code]
    ✓ Enabled hook: 💾 session-memory
[/code]

**它會做什麼：**

  * 檢查掛鉤是否存在且合格
  * 在你的設定中更新 `hooks.internal.entries.<name>.enabled = true`
  * 將設定儲存到磁碟


如果該掛鉤來自 `<workspace>/hooks/`，Gateway 載入它之前必須先完成這個選擇加入步驟。

**啟用後：**

  * 重新啟動 Gateway，讓掛鉤重新載入（macOS 上重新啟動選單列應用程式，或在開發環境中重新啟動 Gateway 程序）。


## 停用掛鉤

bashCopy code
[code]
    openclaw hooks disable <name>
[/code]

透過更新設定來停用特定掛鉤。

**引數：**

  * `<name>`：掛鉤名稱（例如 `command-logger`）


**範例：**

bashCopy code
[code]
    openclaw hooks disable command-logger
[/code]

**輸出：**

CodeCopy code
[code]
    ⏸ Disabled hook: 📝 command-logger
[/code]

**停用後：**

  * 重新啟動 Gateway，讓掛鉤重新載入


## 注意事項

  * `openclaw hooks list --json`、`info --json` 和 `check --json` 會將結構化 JSON 直接寫入 stdout。
  * Plugin 管理的掛鉤無法在此處啟用或停用；請改為啟用或停用擁有該掛鉤的 plugin。


## 安裝掛鉤套件

bashCopy code
[code]
    openclaw plugins install <package>        # npm by defaultopenclaw plugins install npm:<package>    # npm onlyopenclaw plugins install <package> --pin  # pin versionopenclaw plugins install <path>           # local path
[/code]

透過統一的 plugins 安裝器安裝掛鉤套件。

`openclaw hooks install` 仍可作為相容性別名運作，但它會列印棄用警告，並轉送到 `openclaw plugins install`。

Npm 規格**僅限 registry** （套件名稱 + 選用的**確切版本** 或 **dist-tag** ）。Git/URL/file 規格和 semver 範圍會被拒絕。為了安全，即使你的 shell 有全域 npm 安裝設定，依賴項安裝仍會以 `--ignore-scripts` 在專案本機執行。

裸規格和 `@latest` 會留在穩定軌道。如果 npm 將其中任一解析為預覽版本，OpenClaw 會停止並要求你使用 `@beta`/`@rc` 之類的預覽標籤或確切預覽版本明確選擇加入。

**它會做什麼：**

  * 將掛鉤套件複製到 `~/.openclaw/hooks/<id>`
  * 在 `hooks.internal.entries.*` 中啟用已安裝的掛鉤
  * 將安裝記錄在 `hooks.internal.installs` 下


**選項：**

  * `-l, --link`：連結本機目錄而不是複製（將其加入 `hooks.internal.load.extraDirs`）
  * `--pin`：將 npm 安裝記錄為 `hooks.internal.installs` 中精確解析的 `name@version`


**支援的封存檔：** `.zip`、`.tgz`、`.tar.gz`、`.tar`

**範例：**

bashCopy code
[code]
    # Local directoryopenclaw plugins install ./my-hook-pack # Local archiveopenclaw plugins install ./my-hook-pack.zip # NPM packageopenclaw plugins install @openclaw/my-hook-pack # Link a local directory without copyingopenclaw plugins install -l ./my-hook-pack
[/code]

已連結的掛鉤套件會被視為來自操作員設定目錄的受管理掛鉤，而不是工作區掛鉤。

## 更新掛鉤套件

bashCopy code
[code]
    openclaw plugins update <id>openclaw plugins update --all
[/code]

透過統一的 plugins 更新器更新已追蹤、以 npm 為基礎的掛鉤套件。

`openclaw hooks update` 仍可作為相容性別名運作，但它會列印棄用警告，並轉送到 `openclaw plugins update`。

**選項：**

  * `--all`：更新所有已追蹤的掛鉤套件
  * `--dry-run`：顯示將變更的內容而不寫入


當已儲存的完整性雜湊存在且擷取到的成品雜湊發生變更時，OpenClaw 會列印警告並要求確認後才繼續。請使用全域 `--yes` 在 CI/非互動式執行中略過提示。

## 內建掛鉤

### session-memory

當你發出 `/new` 或 `/reset` 時，將工作階段內容儲存到記憶體。

**啟用：**

bashCopy code
[code]
    openclaw hooks enable session-memory
[/code]

**輸出：** 預設為 `~/.openclaw/workspace/memory/YYYY-MM-DD-HHMM.md`。設定 `hooks.internal.entries.session-memory.llmSlug: true` 可使用模型產生的檔名 slug。

**參閱：** [session-memory 文件](</zh-TW/automation/hooks#session-memory>)

### bootstrap-extra-files

在 `agent:bootstrap` 期間注入額外的 bootstrap 檔案（例如 monorepo 本機的 `AGENTS.md` / `TOOLS.md`）。

**啟用：**

bashCopy code
[code]
    openclaw hooks enable bootstrap-extra-files
[/code]

**參閱：** [bootstrap-extra-files 文件](</zh-TW/automation/hooks#bootstrap-extra-files>)

### command-logger

將所有命令事件記錄到集中式稽核檔案。

**啟用：**

bashCopy code
[code]
    openclaw hooks enable command-logger
[/code]

**輸出：** `~/.openclaw/logs/commands.log`

**檢視記錄：**

bashCopy code
[code]
    # Recent commandstail -n 20 ~/.openclaw/logs/commands.log # Pretty-printcat ~/.openclaw/logs/commands.log | jq . # Filter by actiongrep '"action":"new"' ~/.openclaw/logs/commands.log | jq .
[/code]

**參閱：** [command-logger 文件](</zh-TW/automation/hooks#command-logger>)

### boot-md

在 Gateway 啟動時執行 `BOOT.md`（在頻道啟動後）。

**事件** ：`gateway:startup`

**啟用** ：

bashCopy code
[code]
    openclaw hooks enable boot-md
[/code]

**參閱：** [boot-md 文件](</zh-TW/automation/hooks#boot-md>)

## 相關

  * [CLI 參考](</zh-TW/cli>)
  * [自動化掛鉤](</zh-TW/automation/hooks>)


Was this useful?YesNo