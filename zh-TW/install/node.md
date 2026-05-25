---
title: Node.js
source_url: https://docs.openclaw.ai/zh-TW/install/node
scraped_at: 2026-05-25
---

OpenClaw 需要 **Node 22.16 或更新版本** 。**Node 24 是安裝、CI 與發布工作流程的預設且建議執行環境** 。Node 22 仍透過現行 LTS 系列受到支援。[安裝程式指令碼](</zh-TW/install#alternative-install-methods>)會自動偵測並安裝 Node - 本頁適用於你想自行設定 Node，並確認所有項目都已正確串接時使用（版本、PATH、全域安裝）。

## 檢查你的版本

bashCopy code
[code]
    node -v
[/code]

如果輸出 `v24.x.x` 或更高版本，表示你使用的是建議的預設版本。如果輸出 `v22.16.x` 或更高版本，表示你使用的是受支援的 Node 22 LTS 路徑，但我們仍建議在方便時升級到 Node 24。如果尚未安裝 Node，或版本太舊，請從下方選擇一種安裝方式。

## 安裝 Node

### macOS

**Homebrew** （建議）：

bashCopy code
[code]
    brew install node
[/code]

或從 [nodejs.org](<https://nodejs.org/>) 下載 macOS 安裝程式。

### Linux

**Ubuntu / Debian：**

bashCopy code
[code]
    curl -fsSL https://deb.nodesource.com/setup_24.x | sudo -E bash -sudo apt-get install -y nodejs
[/code]

**Fedora / RHEL：**

bashCopy code
[code]
    sudo dnf install nodejs
[/code]

或使用版本管理器（見下方）。

### Windows

**winget** （建議）：

powershellCopy code
[code]
    winget install OpenJS.NodeJS.LTS
[/code]

**Chocolatey：**

powershellCopy code
[code]
    choco install nodejs-lts
[/code]

或從 [nodejs.org](<https://nodejs.org/>) 下載 Windows 安裝程式。

Using a version manager (nvm, fnm, mise, asdf)

版本管理器可讓你輕鬆切換 Node 版本。常見選項：

  * [**fnm**](<https://github.com/Schniz/fnm>) \- 快速、跨平台
  * [**nvm**](<https://github.com/nvm-sh/nvm>) \- 在 macOS/Linux 上廣泛使用
  * [**mise**](<https://mise.jdx.dev/>) \- 多語言工具（Node、Python、Ruby 等）


使用 fnm 的範例：

bashCopy code
[code]
    fnm install 24fnm use 24
[/code]

## 疑難排解

### `openclaw: command not found`

這幾乎總是表示 npm 的全域 bin 目錄不在你的 PATH 中。

* ### Find your global npm prefix

bashCopy code
[code]
    npm prefix -g
[/code]

* ### Check if it's on your PATH

bashCopy code
[code]
    echo "$PATH"
[/code]

在輸出中尋找 `<npm-prefix>/bin`（macOS/Linux）或 `<npm-prefix>`（Windows）。

* ### Add it to your shell startup file

### macOS / Linux

加入到 `~/.zshrc` 或 `~/.bashrc`：

bashCopy code
[code]
    export PATH="$(npm prefix -g)/bin:$PATH"
[/code]

然後開啟新的終端機（或在 zsh 中執行 `rehash` / 在 bash 中執行 `hash -r`）。

### Windows

透過「設定」→「系統」→「環境變數」，將 `npm prefix -g` 的輸出加入系統 PATH。

### `npm install -g` 的權限錯誤（Linux）

如果看到 `EACCES` 錯誤，請將 npm 的全域 prefix 切換到使用者可寫入的目錄：

bashCopy code
[code]
    mkdir -p "$HOME/.npm-global"npm config set prefix "$HOME/.npm-global"export PATH="$HOME/.npm-global/bin:$PATH"
[/code]

將 `export PATH=...` 這一行加入你的 `~/.bashrc` 或 `~/.zshrc`，使其永久生效。

## 相關

  * [安裝概覽](</zh-TW/install>) \- 所有安裝方式
  * [更新](</zh-TW/install/updating>) \- 讓 OpenClaw 保持最新狀態
  * [開始使用](</zh-TW/start/getting-started>) \- 安裝後的第一步


Was this useful?YesNo