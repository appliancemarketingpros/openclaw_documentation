---
title: Linux 應用程式
source_url: https://docs.openclaw.ai/zh-TW/platforms/linux
scraped_at: 2026-05-25
---

Gateway 在 Linux 上受到完整支援。**Node 是建議的執行環境** 。 不建議將 Bun 用於 Gateway（WhatsApp/Telegram 錯誤）。

原生 Linux 輔助應用程式已在規劃中。如果你想協助建置，歡迎貢獻。

## 初學者快速路徑 (VPS)

  1. 安裝 Node 24（建議；Node 22 LTS，目前為 `22.16+`，為了相容性仍可運作）
  2. `npm i -g openclaw@latest`
  3. `openclaw onboard --install-daemon`
  4. 從你的筆記型電腦執行：`ssh -N -L 18789:127.0.0.1:18789 <user>@<host>`
  5. 開啟 `http://127.0.0.1:18789/`，並使用已設定的共用密鑰進行驗證（預設為權杖；如果你設定了 `gateway.auth.mode: "password"`，則使用密碼）


完整 Linux 伺服器指南：[Linux 伺服器](</zh-TW/vps>)。逐步 VPS 範例：[exe.dev](</zh-TW/install/exe-dev>)

## 安裝

  * [開始使用](</zh-TW/start/getting-started>)
  * [安裝與更新](</zh-TW/install/updating>)
  * 選用流程：[Bun（實驗性）](</zh-TW/install/bun>)、[Nix](</zh-TW/install/nix>)、[Docker](</zh-TW/install/docker>)


## Gateway

  * [Gateway 執行手冊](</zh-TW/gateway>)
  * [設定](</zh-TW/gateway/configuration>)


## Gateway 服務安裝 (CLI)

使用下列其中一項：

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

出現提示時，選取 **Gateway 服務** 。

修復/遷移：

CodeCopy code
[code]
    openclaw doctor
[/code]

## 系統控制（systemd 使用者單元）

OpenClaw 預設會安裝 systemd **使用者** 服務。對於共用或永遠開啟的伺服器，請使用**系統** 服務。`openclaw gateway install` 和 `openclaw onboard --install-daemon` 已經會為你產生目前的標準單元；只有在你需要自訂系統/服務管理器設定時，才手動撰寫。完整服務指南位於 [Gateway 執行手冊](</zh-TW/gateway>)。

最小設定：

建立 `~/.config/systemd/user/openclaw-gateway[-<profile>].service`：

CodeCopy code
[code]
    [Unit]Description=OpenClaw Gateway (profile: <profile>, v<version>)After=network-online.targetWants=network-online.target [Service]ExecStart=/usr/local/bin/openclaw gateway --port 18789Restart=alwaysRestartSec=5TimeoutStopSec=30TimeoutStartSec=30SuccessExitStatus=0 143KillMode=control-group [Install]WantedBy=default.target
[/code]

啟用它：

CodeCopy code
[code]
    systemctl --user enable --now openclaw-gateway[-<profile>].service
[/code]

## 記憶體壓力與 OOM 終止

在 Linux 上，當主機、VM 或容器 cgroup 耗盡記憶體時，核心會選擇一個 OOM 犧牲程序。Gateway 可能是不理想的犧牲對象，因為它擁有長時間存在的工作階段和通道連線。因此 OpenClaw 會在可行時偏向先終止暫時性的子程序，而不是 Gateway。

對於符合條件的 Linux 子程序產生，OpenClaw 會透過簡短的 `/bin/sh` 包裝器啟動子程序，將子程序本身的 `oom_score_adj` 提高到 `1000`，然後 `exec` 實際命令。這是不需要特殊權限的操作，因為子程序只是在提高自己被 OOM 終止的可能性。

涵蓋的子程序表面包括：

  * 由監督器管理的命令子程序，
  * PTY shell 子程序，
  * MCP stdio 伺服器子程序，
  * 由 OpenClaw 啟動的瀏覽器/Chrome 程序。


此包裝器僅適用於 Linux，且在 `/bin/sh` 無法使用時會略過。如果子程序環境設定了 `OPENCLAW_CHILD_OOM_SCORE_ADJ=0`、`false`、 `no` 或 `off`，也會略過。

若要驗證子程序：

bashCopy code
[code]
    cat /proc/<child-pid>/oom_score_adj
[/code]

涵蓋的子程序預期值為 `1000`。Gateway 程序應保留其一般分數，通常為 `0`。

這不會取代一般的記憶體調校。如果 VPS 或容器反覆終止子程序，請提高記憶體限制、降低並行度，或新增更強的資源控制，例如 systemd `MemoryMax=` 或容器層級的記憶體限制。

## 相關

  * [安裝概覽](</zh-TW/install>)
  * [Linux 伺服器](</zh-TW/vps>)
  * [Raspberry Pi](</zh-TW/install/raspberry-pi>)


Was this useful?YesNo