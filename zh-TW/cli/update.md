---
title: 更新
source_url: https://docs.openclaw.ai/zh-TW/cli/update
scraped_at: 2026-05-25
---

# `openclaw update`

安全地更新 OpenClaw，並在 stable/beta/dev 通道之間切換。

如果你是透過 **npm/pnpm/bun** 安裝（全域安裝，沒有 git 中繼資料）， 更新會透過 [Updating](</zh-TW/install/updating>) 中的套件管理器流程進行。

## 使用方式

bashCopy code
[code]
    openclaw updateopenclaw update statusopenclaw update wizardopenclaw update --channel betaopenclaw update --channel devopenclaw update --tag betaopenclaw update --tag mainopenclaw update --dry-runopenclaw update --no-restartopenclaw update --yesopenclaw update --jsonopenclaw --update
[/code]

## 選項

  * `--no-restart`：成功更新後略過重新啟動 Gateway 服務。會重新啟動 Gateway 的套件管理器更新，會先確認重新啟動的服務回報預期的更新後版本，命令才會成功。
  * `--channel <stable|beta|dev>`：設定更新通道（git + npm；會保存到設定中）。
  * `--tag <dist-tag|version|spec>`：僅針對這次更新覆寫套件目標。對於套件安裝，`main` 會對應到 `github:openclaw/openclaw#main`。
  * `--dry-run`：預覽規劃中的更新動作（通道/標籤/目標/重新啟動流程），不寫入設定、不安裝、不同步 plugins，也不重新啟動。
  * `--json`：列印機器可讀的 `UpdateRunResult` JSON，包括 核心更新成功後，損毀或無法卸載的受管理 plugins 需要 修復時的 `postUpdate.plugins.warnings`；Plugin 沒有 beta 發行版時的 beta 通道 Plugin 後援細節； 以及更新後 Plugin 同步期間偵測到 npm Plugin 成品漂移時的 `postUpdate.plugins.integrityDrifts`。
  * `--timeout <seconds>`：每個步驟的逾時時間（預設為 1800s）。
  * `--yes`：略過確認提示（例如降級確認）。


`openclaw update` 沒有 `--verbose` 旗標。使用 `--dry-run` 預覽 規劃中的通道/標籤/安裝/重新啟動動作，使用 `--json` 取得機器可讀的 結果；當你只需要通道與可用性細節時，使用 `openclaw update status --json`。 如果你正在偵錯更新前後的 Gateway 記錄， 主控台詳細程度和檔案記錄層級是分開的：Gateway `--verbose` 會影響 終端機/WebSocket 輸出，而檔案記錄需要在設定中使用 `logging.level: "debug"` 或 `"trace"`。請參閱 [Gateway 記錄](</zh-TW/gateway/logging>)。

## `update status`

顯示作用中的更新通道 + git 標籤/分支/SHA（適用於原始碼 checkout），以及更新可用性。

bashCopy code
[code]
    openclaw update statusopenclaw update status --jsonopenclaw update status --timeout 10
[/code]

選項：

  * `--json`：列印機器可讀的狀態 JSON。
  * `--timeout <seconds>`：檢查逾時時間（預設為 3s）。


## `update wizard`

互動式流程，用來選擇更新通道，並確認更新後是否要重新啟動 Gateway （預設會重新啟動）。如果你選擇 `dev` 但沒有 git checkout，它會 提議建立一個。

選項：

  * `--timeout <seconds>`：每個更新步驟的逾時時間（預設 `1800`）


## 它會做什麼

當你明確切換通道（`--channel ...`）時，OpenClaw 也會保持 安裝方式一致：

  * `dev` → 確保存在 git checkout（預設：`~/openclaw`，可用 `OPENCLAW_GIT_DIR` 覆寫）， 更新它，並從該 checkout 安裝全域 CLI。
  * `stable` → 使用 `latest` 從 npm 安裝。
  * `beta` → 優先使用 npm dist-tag `beta`，但當 beta 缺失或比目前 stable 發行版更舊時，會後援到 `latest`。


Gateway 核心自動更新器（透過設定啟用時）會在即時 Gateway 請求處理器 之外啟動 CLI 更新路徑。控制平面 `update.run` 套件管理器 更新會在套件替換後強制執行非延後、無冷卻時間的更新重新啟動， 因為舊的 Gateway 程序可能仍有指向 新套件已移除檔案的記憶體中區塊。

對於套件管理器安裝，`openclaw update` 會先解析目標套件 版本，再呼叫套件管理器。npm 全域安裝會使用分段式 安裝：OpenClaw 會把新套件安裝到暫時的 npm prefix，確認 那裡打包的 `dist` 清單，然後把乾淨的套件樹替換到 真正的全域 prefix。如果驗證失敗，更新後的 doctor、Plugin 同步和 重新啟動工作不會從可疑的樹執行。即使已安裝版本 已經符合目標，命令也會重新整理全域套件安裝， 然後執行 Plugin 同步、核心命令補全重新整理，以及重新啟動工作。這 會讓打包的 sidecar 和通道擁有的 Plugin 記錄與 已安裝的 OpenClaw 建置保持一致，同時把完整的 Plugin 命令補全重建留給 明確的 `openclaw completion --write-state` 執行。

當本機受管理的 Gateway 服務已安裝且啟用重新啟動時， 套件管理器更新會先停止執行中的服務，再替換套件 樹，然後從更新後的安裝重新整理服務中繼資料，重新啟動 服務，並確認重新啟動的 Gateway 回報預期版本後 才回報成功。在 macOS 上，更新後檢查也會確認 LaunchAgent 已針對作用中的設定檔載入/執行，且設定的 loopback 埠 健康。如果 plist 已安裝但 launchd 未監督它，OpenClaw 會自動重新 bootstrap LaunchAgent，然後重新執行 健康狀態/版本/通道就緒檢查。全新的 bootstrap 會直接載入 RunAtLoad 工作，因此更新復原不會立即對新產生的 Gateway 執行 `kickstart -k`。如果 Gateway 仍未變健康，命令會以 非零狀態結束，並列印重新啟動記錄路徑，以及明確的重新啟動、重新安裝和 套件回復指示。使用 `--no-restart` 時， 仍會執行套件替換，但受管理服務不會被停止或 重新啟動，因此執行中的 Gateway 可能會持續使用舊程式碼，直到你 手動重新啟動它。

## Git checkout 流程

### 通道選擇

  * `stable`：checkout 最新的非 beta 標籤，然後建置並執行 doctor。
  * `beta`：優先使用最新的 `-beta` 標籤，但當 beta 缺失或較舊時，會後援到最新的 stable 標籤。
  * `dev`：checkout `main`，然後 fetch 並 rebase。


### 更新步驟

* ### 確認乾淨的 worktree

要求沒有未提交的變更。

* ### 切換通道

切換到選定的通道（標籤或分支）。

* ### Fetch upstream

僅限 Dev。

* ### 預檢建置（僅限 dev）

在暫時 worktree 中執行 TypeScript 建置。如果 tip 失敗，會往回最多 10 個 commit，尋找最新可建置的 commit。設定 `OPENCLAW_UPDATE_PREFLIGHT_LINT=1` 也會在此預檢期間執行 lint；lint 會以受限的序列模式執行，因為使用者的更新主機通常比 CI runner 更小。

* ### Rebase

Rebase 到選定的 commit（僅限 dev）。

* ### 安裝相依性

使用 repo 套件管理器。對於 pnpm checkout，更新器會依需求 bootstrap `pnpm`（先透過 `corepack`，再後援到暫時的 `npm install pnpm@11`），而不是在 pnpm workspace 內執行 `npm run build`。

* ### 建置 Control UI

建置 Gateway 和 Control UI。

* ### 執行 doctor

`openclaw doctor` 會作為最後的安全更新檢查執行。

* ### 同步 plugins

將 plugins 同步到作用中的通道。Dev 使用內建 plugins；stable 和 beta 使用 npm。更新受追蹤的 Plugin 安裝。

在 beta 更新通道上，遵循預設/latest 線的受追蹤 npm 與 ClawHub Plugin 安裝 會先嘗試 Plugin `@beta` 發行版。如果 Plugin 沒有 beta 發行版，OpenClaw 會後援到記錄的預設/latest spec，並將 該情況回報為警告。對於 npm plugins，當 beta 套件存在但安裝驗證失敗時，OpenClaw 也會後援。這些 Plugin 後援警告 不會讓核心更新失敗。精確版本和明確標籤不會 被改寫。

## `--update` 簡寫

`openclaw --update` 會改寫為 `openclaw update`（適用於 shell 和啟動器腳本）。

## 相關

  * `openclaw doctor`（在 git checkout 上會提議先執行 update）
  * [開發通道](</zh-TW/install/development-channels>)
  * [Updating](</zh-TW/install/updating>)
  * [CLI 參考](</zh-TW/cli>)


Was this useful?YesNo