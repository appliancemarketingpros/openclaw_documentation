---
title: 安裝
source_url: https://docs.openclaw.ai/zh-TW/install
scraped_at: 2026-05-25
---

## 系統需求

  * **Node 24** （建議）或 Node 22.16+ - 安裝程式指令碼會自動處理這項需求
  * **macOS、Linux 或 Windows** \- 支援原生 Windows 和 WSL2；WSL2 較穩定。請參閱 [Windows](</zh-TW/platforms/windows>)。
  * 只有從原始碼建置時才需要 `pnpm`


## 建議：安裝程式指令碼

這是最快的安裝方式。它會偵測你的作業系統、在需要時安裝 Node、安裝 OpenClaw，並啟動初始設定。

### macOS / Linux / WSL2

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash
[/code]

### Windows (PowerShell)

powershellCopy code
[code]
    iwr -useb https://openclaw.ai/install.ps1 | iex
[/code]

若要安裝但不執行初始設定：

### macOS / Linux / WSL2

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash -s -- --no-onboard
[/code]

### Windows (PowerShell)

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -NoOnboard
[/code]

如需所有旗標與 CI/自動化選項，請參閱[安裝程式內部機制](</zh-TW/install/installer>)。

## 替代安裝方法

### 本機前綴安裝程式（`install-cli.sh`）

當你想將 OpenClaw 和 Node 保存在本機前綴路徑下，例如 `~/.openclaw`，且不依賴系統層級的 Node 安裝時，請使用此方法：

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install-cli.sh | bash
[/code]

它預設支援 npm 安裝，也支援在相同前綴流程下進行 git-checkout 安裝。完整參考：[安裝程式內部機制](</zh-TW/install/installer#install-clish>)。

已經安裝了嗎？可使用 `openclaw update --channel dev` 和 `openclaw update --channel stable` 在套件與 git 安裝之間切換。請參閱[更新](</zh-TW/install/updating#switch-between-npm-and-git-installs>)。

### npm、pnpm 或 bun

如果你已自行管理 Node：

### npm

bashCopy code
[code]
    npm install -g openclaw@latestopenclaw onboard --install-daemon
[/code]

### pnpm

bashCopy code
[code]
    pnpm add -g openclaw@latestpnpm approve-builds -gopenclaw onboard --install-daemon
[/code]

### bun

bashCopy code
[code]
    bun add -g openclaw@latestopenclaw onboard --install-daemon
[/code]

疑難排解：sharp 建置錯誤（npm）

如果 `sharp` 因全域安裝的 libvips 而失敗：

bashCopy code
[code]
    SHARP_IGNORE_GLOBAL_LIBVIPS=1 npm install -g openclaw@latest
[/code]

### 從原始碼安裝

適合貢獻者或想從本機 checkout 執行的人：

bashCopy code
[code]
    git clone https://github.com/openclaw/openclaw.gitcd openclawpnpm install && pnpm build && pnpm ui:buildpnpm link --globalopenclaw onboard --install-daemon
[/code]

或略過 link，直接在 repo 內使用 `pnpm openclaw ...`。完整開發工作流程請參閱[設定](</zh-TW/start/setup>)。

### 從 GitHub main 安裝

bashCopy code
[code]
    npm install -g github:openclaw/openclaw#main
[/code]

### 容器與套件管理器

[**Docker** 容器化或無介面部署。 ](</zh-TW/install/docker>) [**Podman** Docker 的無 root 容器替代方案。 ](</zh-TW/install/podman>) [**Nix** 透過 Nix flake 宣告式安裝。 ](</zh-TW/install/nix>) [**Ansible** 自動化機群佈建。 ](</zh-TW/install/ansible>) [**Bun** 透過 Bun 執行階段僅使用 CLI。 ](</zh-TW/install/bun>)

## 驗證安裝

bashCopy code
[code]
    openclaw --version      # confirm the CLI is availableopenclaw doctor         # check for config issuesopenclaw gateway status # verify the Gateway is running
[/code]

如果你想在安裝後使用受管理的啟動方式：

  * macOS：透過 `openclaw onboard --install-daemon` 或 `openclaw gateway install` 使用 LaunchAgent
  * Linux/WSL2：透過相同命令使用 systemd 使用者服務
  * 原生 Windows：優先使用 Scheduled Task；如果工作建立被拒，則 fallback 到每位使用者 Startup-folder 登入項目


## 託管與部署

將 OpenClaw 部署到雲端伺服器或 VPS：

[**VPS** [**Docker VM** [**Kubernetes** OPENCLAW_DOCS_MARKER:cardOpen:IHRpdGxlPSJGbHkuaW8iIGhyZWY9Ii96aC1UVy9pbnN0YWxsL2ZseSI [Fly.io](<http://Fly.io>) OPENCLAW_DOCS_MARKER:cardClose: [**Hetzner** [**GCP** [**Azure** [**Railway** [**Render** [**Northflank** 更新、遷移或解除安裝 [**更新** 讓 OpenClaw 保持最新。 ](</zh-TW/install/updating>) [**遷移** 移至新機器。 ](</zh-TW/install/migrating>) [**解除安裝** 完全移除 OpenClaw。 ](</zh-TW/install/uninstall>) 疑難排解：找不到 `openclaw` 如果安裝成功，但終端機找不到 `openclaw`： bashCopy code
[code]
    node -v           # Node installed?npm prefix -g     # Where are global packages?echo "$PATH"      # Is the global bin dir in PATH?
[/code]

如果 `$(npm prefix -g)/bin` 不在你的 `$PATH` 中，請將它加入你的 shell 啟動檔（`~/.zshrc` 或 `~/.bashrc`）： bashCopy code
[code]
    export PATH="$(npm prefix -g)/bin:$PATH"
[/code]

接著開啟新的終端機。更多詳細資訊請參閱 [Node 設定](</zh-TW/install/node>)。 ](</zh-TW/install/northflank>) Was this useful?YesNo ](</zh-TW/install/render>)](</zh-TW/install/railway>)](</zh-TW/install/azure>)](</zh-TW/install/gcp>)](</zh-TW/install/hetzner>)](</zh-TW/install/kubernetes>)](</zh-TW/install/docker-vm-runtime>)](</zh-TW/vps>)