---
title: 遷移指南
source_url: https://docs.openclaw.ai/zh-TW/install/migrating
scraped_at: 2026-05-25
---

OpenClaw 支援三種遷移路徑：從另一個代理系統匯入、將現有安裝移至新機器，以及就地升級 Plugin。

## 從另一個代理系統匯入

使用內建的遷移提供者，將指令、MCP 伺服器、Skills、模型設定，以及（選擇性）API 金鑰帶入 OpenClaw。計畫會在任何變更前預覽，報告中的秘密會經過遮蔽，而套用作業會有已驗證的備份作為保障。

[**從 Claude 遷移** 匯入 Claude Code 和 Claude Desktop 狀態，包括 `CLAUDE.md`、MCP 伺服器、Skills，以及專案命令。 ](</zh-TW/install/migrating-claude>) [**從 Hermes 遷移** 匯入 Hermes 設定、提供者、MCP 伺服器、記憶體、Skills，以及支援的 `.env` 金鑰。 ](</zh-TW/install/migrating-hermes>)

CLI 進入點是 [`openclaw migrate`](</zh-TW/cli/migrate>)。初始設定在偵測到已知來源時，也可以提供遷移（`openclaw onboard --flow import`）。

## 將 OpenClaw 移至新機器

複製**狀態目錄** （預設為 `~/.openclaw/`）和你的**工作區** ，以保留：

  * **設定** — `openclaw.json` 和所有 Gateway 設定。
  * **驗證** — 每個代理的 `auth-profiles.json`（API 金鑰加上 OAuth），以及 `credentials/` 底下的任何通道或提供者狀態。
  * **工作階段** — 對話歷史和代理狀態。
  * **通道狀態** — WhatsApp 登入、Telegram 工作階段，以及類似狀態。
  * **工作區檔案** — `MEMORY.md`、`USER.md`、Skills，以及提示。


### 遷移步驟

* ### 停止 Gateway 並備份

在**舊** 機器上，停止 Gateway，避免檔案在複製過程中變更，然後封存：

bashCopy code
[code]
    openclaw gateway stopcd ~tar -czf openclaw-state.tgz .openclaw
[/code]

如果你使用多個設定檔（例如 `~/.openclaw-work`），請分別封存每一個。

* ### 在新機器上安裝 OpenClaw

在新機器上[安裝](</zh-TW/install>) CLI（如有需要，也安裝 Node）。即使初始設定建立了新的 `~/.openclaw/` 也沒關係。你接下來會覆寫它。

* ### 複製狀態目錄和工作區

透過 `scp`、`rsync -a` 或外接硬碟傳輸封存檔，然後解壓縮：

bashCopy code
[code]
    cd ~tar -xzf openclaw-state.tgz
[/code]

確認已包含隱藏目錄，且檔案擁有權符合將執行 Gateway 的使用者。

* ### 執行 doctor 並驗證

在新機器上，執行 [Doctor](</zh-TW/gateway/doctor>) 以套用設定遷移並修復服務：

bashCopy code
[code]
    openclaw doctoropenclaw gateway restartopenclaw status
[/code]

如果 Telegram 或 Discord 使用預設 env 後援（`TELEGRAM_BOT_TOKEN` 或 `DISCORD_BOT_TOKEN`），請確認遷移後狀態目錄的 `.env` 包含這些金鑰，且不要列印秘密值：

bashCopy code
[code]
    awk -F= '/^(TELEGRAM_BOT_TOKEN|DISCORD_BOT_TOKEN)=/ { print $1 "=present" }' ~/.openclaw/.env
[/code]

當已啟用的預設 Telegram 或 Discord 帳號沒有設定 token，且相符的環境變數無法提供給 doctor 程序時，`openclaw doctor` 也會發出警告。

### 常見問題

設定檔或狀態目錄不相符

如果舊 Gateway 使用了 `--profile` 或 `OPENCLAW_STATE_DIR`，而新的沒有，通道會顯示為已登出，工作階段也會是空的。使用你遷移的**相同** 設定檔或狀態目錄啟動 Gateway，然後重新執行 `openclaw doctor`。

只複製 openclaw.json

只有設定檔是不夠的。模型驗證設定檔位於 `agents/<agentId>/agent/auth-profiles.json` 底下，而通道和提供者狀態位於 `credentials/` 底下。請一律遷移**整個** 狀態目錄。

權限和擁有權

如果你以 root 複製或切換了使用者，Gateway 可能無法讀取認證。請確保狀態目錄和工作區由執行 Gateway 的使用者擁有。

遠端模式

如果你的 UI 指向**遠端** Gateway，工作階段和工作區由遠端主機擁有。請遷移 Gateway 主機本身，而不是你的本機筆記型電腦。請參閱 [FAQ](</zh-TW/help/faq#where-things-live-on-disk>)。

備份中的秘密

狀態目錄包含驗證設定檔、通道認證和其他提供者狀態。請加密儲存備份，避免使用不安全的傳輸通道；如果懷疑外洩，請輪替金鑰。

### 驗證清單

在新機器上確認：

  * [ ] `openclaw status` 顯示 Gateway 正在執行。
  * [ ] 通道仍保持連線（不需要重新配對）。
  * [ ] 儀表板可開啟並顯示既有工作階段。
  * [ ] 工作區檔案（記憶體、設定）存在。


## 就地升級 Plugin

就地 Plugin 升級會保留相同的 Plugin id 和設定金鑰，但可能會將磁碟上的狀態移至目前版面配置。Plugin 專屬升級指南會與其通道並列：

  * [Matrix 遷移](</zh-TW/channels/matrix-migration>)：加密狀態復原限制、自動快照行為，以及手動復原命令。


## 相關

  * [`openclaw migrate`](</zh-TW/cli/migrate>)：跨系統匯入的 CLI 參考。
  * [安裝概覽](</zh-TW/install>)：所有安裝方法。
  * [Doctor](</zh-TW/gateway/doctor>)：遷移後健康檢查。
  * [解除安裝](</zh-TW/install/uninstall>)：乾淨移除 OpenClaw。


Was this useful?YesNo