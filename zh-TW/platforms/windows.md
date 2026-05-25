---
title: Windows
source_url: https://docs.openclaw.ai/zh-TW/platforms/windows
scraped_at: 2026-05-25
---

OpenClaw 同時支援 **原生 Windows** 與 **WSL2** 。WSL2 是較穩定的路徑，並建議用於完整體驗：CLI、Gateway 與工具都在 Linux 內執行，具有完整相容性。原生 Windows 可用於核心 CLI 與 Gateway 使用，但有一些注意事項如下。

原生 Windows 配套應用程式正在規劃中。

## WSL2（建議）

  * [開始使用](</zh-TW/start/getting-started>)（在 WSL 內使用）
  * [安裝與更新](</zh-TW/install/updating>)
  * 官方 WSL2 指南（Microsoft）：<https://learn.microsoft.com/windows/wsl/install>


## 原生 Windows 狀態

原生 Windows CLI 流程正在改善，但 WSL2 仍是建議路徑。

目前在原生 Windows 上運作良好的項目：

  * 透過 `install.ps1` 使用網站安裝程式
  * 本機 CLI 使用，例如 `openclaw --version`、`openclaw doctor` 與 `openclaw plugins list --json`
  * 嵌入式本機 agent/provider 冒煙測試，例如：

powershellCopy code
[code]
    openclaw agent --local --agent main --thinking low -m "Reply with exactly WINDOWS-HATCH-OK."
[/code]

目前注意事項：

  * `openclaw onboard --non-interactive` 仍預期可連線的本機 Gateway，除非你傳入 `--skip-health`
  * `openclaw onboard --non-interactive --install-daemon` 與 `openclaw gateway install` 會先嘗試 Windows 工作排程器
  * 如果建立工作排程遭拒，OpenClaw 會退回使用每位使用者的 Startup 資料夾登入項目，並立即啟動 Gateway
  * 如果 `schtasks` 本身卡住或停止回應，OpenClaw 現在會快速中止該路徑，並改為退回，而不是永久掛住
  * 可用時仍偏好使用工作排程器，因為它們提供較好的監督器狀態


如果你只想使用原生 CLI，而不安裝 Gateway 服務，請使用以下其中一種：

powershellCopy code
[code]
    openclaw onboard --non-interactive --skip-healthopenclaw gateway run
[/code]

如果你確實想在原生 Windows 上使用受管理的啟動：

powershellCopy code
[code]
    openclaw gateway installopenclaw gateway status --json
[/code]

如果建立工作排程遭封鎖，退回服務模式仍會在登入後透過目前使用者的 Startup 資料夾自動啟動。

## Gateway

  * [Gateway 操作手冊](</zh-TW/gateway>)
  * [設定](</zh-TW/gateway/configuration>)


## Gateway 服務安裝（CLI）

在 WSL2 內：

CodeCopy code
[code]
    openclaw onboard --install-daemon
[/code]

或：

CodeCopy code
[code]
    openclaw gateway install
[/code]

或：

CodeCopy code
[code]
    openclaw configure
[/code]

在提示時選取 **Gateway 服務** 。

修復/遷移：

CodeCopy code
[code]
    openclaw doctor
[/code]

## Windows 登入前自動啟動 Gateway

對於無頭設定，請確保即使沒有人登入 Windows，完整開機鏈也會執行。

### 1) 讓使用者服務在未登入時持續執行

在 WSL 內：

bashCopy code
[code]
    sudo loginctl enable-linger "$(whoami)"
[/code]

### 2) 安裝 OpenClaw Gateway 使用者服務

在 WSL 內：

bashCopy code
[code]
    openclaw gateway install
[/code]

### 3) 在 Windows 開機時自動啟動 WSL

以系統管理員身分在 PowerShell 中執行：

powershellCopy code
[code]
    schtasks /create /tn "WSL Boot" /tr "wsl.exe -d Ubuntu --exec /bin/true" /sc onstart /ru SYSTEM
[/code]

將 `Ubuntu` 替換為以下指令中的發行版名稱：

powershellCopy code
[code]
    wsl --list --verbose
[/code]

### 驗證啟動鏈

重新開機後（在 Windows 登入前），從 WSL 檢查：

bashCopy code
[code]
    systemctl --user is-enabled openclaw-gateway.servicesystemctl --user status openclaw-gateway.service --no-pager
[/code]

## 進階：透過 LAN 公開 WSL 服務（portproxy）

WSL 有自己的虛擬網路。如果另一台機器需要連到 **WSL 內** 執行的服務（SSH、本機 TTS 伺服器或 Gateway），你必須將 Windows 連接埠轉送到目前的 WSL IP。WSL IP 會在重新啟動後變更，因此你可能需要重新整理轉送規則。

範例（PowerShell **以系統管理員身分** ）：

powershellCopy code
[code]
    $Distro = "Ubuntu-24.04"$ListenPort = 2222$TargetPort = 22 $WslIp = (wsl -d $Distro -- hostname -I).Trim().Split(" ")[0]if (-not $WslIp) { throw "WSL IP not found." } netsh interface portproxy add v4tov4 listenaddress=0.0.0.0 listenport=$ListenPort `  connectaddress=$WslIp connectport=$TargetPort
[/code]

允許連接埠通過 Windows 防火牆（一次性）：

powershellCopy code
[code]
    New-NetFirewallRule -DisplayName "WSL SSH $ListenPort" -Direction Inbound `  -Protocol TCP -LocalPort $ListenPort -Action Allow
[/code]

在 WSL 重新啟動後重新整理 portproxy：

powershellCopy code
[code]
    netsh interface portproxy delete v4tov4 listenport=$ListenPort listenaddress=0.0.0.0 | Out-Nullnetsh interface portproxy add v4tov4 listenport=$ListenPort listenaddress=0.0.0.0 `  connectaddress=$WslIp connectport=$TargetPort | Out-Null
[/code]

備註：

  * 從另一台機器進行 SSH 時，目標是 **Windows 主機 IP** （範例：`ssh user@windows-host -p 2222`）。
  * 遠端節點必須指向 **可連線** 的 Gateway URL（不是 `127.0.0.1`）；使用 `openclaw status --all` 確認。
  * 使用 `listenaddress=0.0.0.0` 供 LAN 存取；`127.0.0.1` 會讓它僅限本機。
  * 如果你希望自動執行，請註冊一個工作排程，在登入時執行重新整理步驟。


## WSL2 逐步安裝

### 1) 安裝 WSL2 + Ubuntu

開啟 PowerShell（系統管理員）：

powershellCopy code
[code]
    wsl --install# Or pick a distro explicitly:wsl --list --onlinewsl --install -d Ubuntu-24.04
[/code]

如果 Windows 要求，請重新開機。

### 2) 啟用 systemd（Gateway 安裝所需）

在你的 WSL 終端機中：

bashCopy code
[code]
    sudo tee /etc/wsl.conf >/dev/null <<'EOF'[boot]systemd=trueEOF
[/code]

然後從 PowerShell：

powershellCopy code
[code]
    wsl --shutdown
[/code]

重新開啟 Ubuntu，然後驗證：

bashCopy code
[code]
    systemctl --user status
[/code]

### 3) 安裝 OpenClaw（在 WSL 內）

若是在 WSL 內進行一般首次設定，請遵循 Linux 開始使用流程：

bashCopy code
[code]
    git clone https://github.com/openclaw/openclaw.gitcd openclawpnpm installpnpm buildpnpm ui:buildpnpm openclaw onboard --install-daemon
[/code]

如果你是從原始碼開發，而不是進行首次導覽設定，請使用 [設定](</zh-TW/start/setup>) 中的原始碼開發迴圈：

bashCopy code
[code]
    pnpm install# First run only (or after resetting local OpenClaw config/workspace)pnpm openclaw setuppnpm gateway:watch
[/code]

完整指南：[開始使用](</zh-TW/start/getting-started>)

## Windows 配套應用程式

我們尚未有 Windows 配套應用程式。如果你想協助實現，歡迎貢獻。

## Git 與 GitHub 連線（貢獻者）

某些網路會封鎖或限速到 GitHub 的 HTTPS。如果 `git clone` 因逾時或連線重設而失敗，請嘗試其他網路、VPN，或你的組織提供的 HTTP/HTTPS Proxy。

如果 `gh auth login` 在瀏覽器裝置流程期間失敗（例如連線到 `github.com:443` 逾時），請改用個人存取權杖進行驗證：

  1. 建立至少具有 `repo` 範圍（classic PAT）或等效細粒度存取權的權杖。
  2. 在目前工作階段的 PowerShell 中：

powershellCopy code
[code]
    $env:GH_TOKEN="<your-token>"gh auth statusgh auth setup-git
[/code]

  3. 如果 `gh auth status` 警告缺少 `read:org`，請建立包含該範圍的權杖，並重新指派變數：

powershellCopy code
[code]
    $env:GH_TOKEN="<your-token-with-repo-and-read:org>"gh auth status
[/code]

`gh auth refresh -s read:org` 只適用於你透過 `gh auth login` 驗證，且已儲存可重新整理的憑證時（不適用於使用 `GH_TOKEN` 時）。

切勿提交權杖，或將其貼到 issue 或 pull request 中。

## 相關

  * [安裝總覽](</zh-TW/install>)
  * [平台](</zh-TW/platforms>)


Was this useful?YesNo