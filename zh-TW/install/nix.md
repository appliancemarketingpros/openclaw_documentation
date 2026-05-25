---
title: Nix
source_url: https://docs.openclaw.ai/zh-TW/install/nix
scraped_at: 2026-05-25
---

使用 **[nix-openclaw](<https://github.com/openclaw/nix-openclaw>)** 以宣告式方式安裝 OpenClaw - 第一方、功能齊備的 Home Manager 模組。

## 你會得到什麼

  * Gateway + macOS app + 工具（whisper、spotify、cameras）-- 全部固定版本
  * 可在重新開機後繼續運作的 launchd 服務
  * 具備宣告式設定的 Plugin 系統
  * 即時回復：`home-manager switch --rollback`


## 快速開始

* ### 安裝 Determinate Nix

如果尚未安裝 Nix，請依照 [Determinate Nix installer](<https://github.com/DeterminateSystems/nix-installer>) 的指示操作。

* ### 建立本機 flake

使用 nix-openclaw repo 中以 agent 優先的範本：

bashCopy code
[code]
    mkdir -p ~/code/openclaw-local# Copy templates/agent-first/flake.nix from the nix-openclaw repo
[/code]

* ### 設定密鑰

設定你的訊息機器人權杖與模型供應商 API 金鑰。放在 `~/.secrets/` 的純文字檔案即可。

* ### 填入範本預留位置並切換

bashCopy code
[code]
    home-manager switch
[/code]

* ### 驗證

確認 launchd 服務正在執行，且你的機器人會回應訊息。

完整的模組選項與範例請參閱 [nix-openclaw README](<https://github.com/openclaw/nix-openclaw>)。

## Nix 模式的執行階段行為

設定 `OPENCLAW_NIX_MODE=1` 時（使用 nix-openclaw 時會自動設定），OpenClaw 會針對 Nix 管理的安裝進入決定性模式。其他 Nix 套件也可以設定相同模式；nix-openclaw 是第一方參考實作。

你也可以手動設定：

bashCopy code
[code]
    export OPENCLAW_NIX_MODE=1
[/code]

在 macOS 上，GUI app 不會自動繼承 shell 環境變數。請改用 defaults 啟用 Nix 模式：

bashCopy code
[code]
    defaults write ai.openclaw.mac openclaw.nixMode -bool true
[/code]

### Nix 模式會改變什麼

  * 自動安裝與自我修改流程會停用
  * `openclaw.json` 會被視為不可變。啟動時衍生的預設值只保留在執行階段，setup、onboarding、會修改設定的 `openclaw update`、Plugin install/update/uninstall/enable、`doctor --fix`、`doctor --generate-gateway-token` 與 `openclaw config set` 等設定寫入器都會拒絕編輯該檔案。
  * Agents 應改為編輯 Nix 來源。對於 nix-openclaw，請使用以 agent 優先的 [快速開始](<https://github.com/openclaw/nix-openclaw#quick-start>)，並在 `programs.openclaw.config` 或 `instances.<name>.config` 底下設定 config。
  * 缺少依賴項目時會顯示 Nix 專用的修復訊息
  * UI 會顯示唯讀 Nix 模式橫幅


### Config 與狀態路徑

OpenClaw 會從 `OPENCLAW_CONFIG_PATH` 讀取 JSON5 config，並將可變資料儲存在 `OPENCLAW_STATE_DIR`。在 Nix 下執行時，請明確將這些設定為由 Nix 管理的位置，讓執行階段狀態與 config 不會進入不可變 store。

變數 | 預設值  
---|---  
`OPENCLAW_HOME` | `HOME` / `USERPROFILE` / `os.homedir()`  
`OPENCLAW_STATE_DIR` | `~/.openclaw`  
`OPENCLAW_CONFIG_PATH` | `$OPENCLAW_STATE_DIR/openclaw.json`  
  
### 服務 PATH 探索

launchd/systemd gateway 服務會自動探索 Nix-profile 二進位檔，因此 會 shell out 到 `nix` 安裝之可執行檔的 plugins 與工具，不需要 手動設定 PATH 也能運作：

  * 設定 `NIX_PROFILES` 時，每個項目都會依 由右至左的優先順序加入服務 PATH（符合 Nix shell 優先順序 - 最右側勝出）。
  * 未設定 `NIX_PROFILES` 時，會加入 `~/.nix-profile/bin` 作為備援。


這同時適用於 macOS launchd 與 Linux systemd 服務環境。

## 相關

[**nix-openclaw** 事實來源 Home Manager 模組與完整設定指南。 ](<https://github.com/openclaw/nix-openclaw>) [**設定精靈** 非 Nix CLI 設定逐步說明。 ](</zh-TW/start/wizard>) [**Docker** 作為非 Nix 替代方案的容器化設定。 ](</zh-TW/install/docker>) [**更新** 與套件一起更新由 Home Manager 管理的安裝。 ](</zh-TW/install/updating>)

Was this useful?YesNo