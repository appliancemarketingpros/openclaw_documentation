---
title: DigitalOcean
source_url: https://docs.openclaw.ai/zh-TW/install/digitalocean
scraped_at: 2026-05-25
---

在 DigitalOcean Droplet 上執行持久的 OpenClaw Gateway（1 GB Basic 方案約 $6/月）。

DigitalOcean 是最簡單的付費 VPS 路徑。如果你偏好更便宜或免費的選項：

  * [Hetzner](</zh-TW/install/hetzner>) — €3.79/月，每美元可取得更多核心/RAM。
  * [Oracle Cloud](</zh-TW/install/oracle>) — Always Free ARM（最高 4 OCPU、24 GB RAM），但註冊可能有些不穩定，且僅限 ARM。


## 先決條件

  * DigitalOcean 帳戶（[註冊](<https://cloud.digitalocean.com/registrations/new>)）
  * SSH 金鑰組（或願意使用密碼驗證）
  * 約 20 分鐘


## 設定

* ### 建立 Droplet

  1. 登入 [DigitalOcean](<https://cloud.digitalocean.com/>)。
  2. 點擊 **Create > Droplets**。
  3. 選擇： 
     * **區域：** 離你最近的位置
     * **映像：** Ubuntu 24.04 LTS
     * **大小：** Basic、Regular、1 vCPU / 1 GB RAM / 25 GB SSD
     * **驗證：** SSH 金鑰（建議）或密碼
  4. 點擊 **Create Droplet** 並記下 IP 位址。


* ### 連線並安裝

bashCopy code
[code]
    ssh root@YOUR_DROPLET_IP apt update && apt upgrade -y # Install Node.js 24curl -fsSL https://deb.nodesource.com/setup_24.x | bash -apt install -y nodejs # Install OpenClawcurl -fsSL https://openclaw.ai/install.sh | bash # Create the non-root user that will own OpenClaw state and services.adduser openclawusermod -aG sudo openclawloginctl enable-linger openclaw su - openclawopenclaw --version
[/code]

只使用 root shell 進行系統啟動設定。請以非 root 的 `openclaw` 使用者執行 OpenClaw 命令，讓狀態位於 `/home/openclaw/.openclaw/` 下，且 Gateway 會安裝為該使用者的 systemd 服務。

* ### 執行引導設定

bashCopy code
[code]
    openclaw onboard --install-daemon
[/code]

精靈會引導你完成模型驗證、通道設定、gateway 權杖產生，以及 daemon 安裝（systemd）。

* ### 新增 swap（建議用於 1 GB Droplet）

bashCopy code
[code]
    fallocate -l 2G /swapfilechmod 600 /swapfilemkswap /swapfileswapon /swapfileecho '/swapfile none swap sw 0 0' >> /etc/fstab
[/code]

* ### 驗證 Gateway

bashCopy code
[code]
    openclaw statussystemctl --user status openclaw-gateway.servicejournalctl --user -u openclaw-gateway.service -f
[/code]

* ### 存取 Control UI

Gateway 預設繫結至本機回環。請選擇下列其中一個選項。

**選項 A：SSH tunnel（最簡單）**

bashCopy code
[code]
    # From your local machinessh -L 18789:localhost:18789 root@YOUR_DROPLET_IP
[/code]

然後開啟 `http://localhost:18789`。

**選項 B：Tailscale Serve**

bashCopy code
[code]
    curl -fsSL https://tailscale.com/install.sh | sudo shsudo tailscale upopenclaw config set gateway.tailscale.mode serveopenclaw gateway restart
[/code]

然後從 tailnet 上的任何裝置開啟 `https://<magicdns>/`。

Tailscale Serve 會透過 tailnet 身分標頭驗證 Control UI 和 WebSocket 流量，這假設 Gateway 主機本身是受信任的。無論如何，HTTP API 端點都會遵循 Gateway 的一般驗證模式（權杖/密碼）。若要在 Serve 上要求明確的共享秘密憑證，請設定 `gateway.auth.allowTailscale: false`，並使用 `gateway.auth.mode: "token"` 或 `"password"`。

**選項 C：Tailnet 繫結（不使用 Serve）**

bashCopy code
[code]
    openclaw config set gateway.bind tailnetopenclaw gateway restart
[/code]

然後開啟 `http://<tailscale-ip>:18789`（需要權杖）。

## 持久性與備份

OpenClaw 狀態位於：

  * `~/.openclaw/` — `openclaw.json`、每個 agent 的 `auth-profiles.json`、通道/provider 狀態，以及工作階段資料。
  * `~/.openclaw/workspace/` — agent workspace（[SOUL.md](<http://SOUL.md>)、記憶、成品）。


這些資料會在 Droplet 重新開機後保留下來。若要建立可攜式快照：

bashCopy code
[code]
    openclaw backup create
[/code]

DigitalOcean snapshots 會備份整個 Droplet；`openclaw backup create` 則可在不同主機之間攜帶。

## 1 GB RAM 提示

$6 的 Droplet 只有 1 GB RAM。若要保持順暢：

  * 確認上方的 swap 步驟已寫入 `/etc/fstab`，以便重新開機後仍會保留。
  * 偏好使用 API 型模型（Claude、GPT），而不是本機模型 — 本機 LLM 推論無法放進 1 GB。
  * 如果大型提示導致 OOM，請將 `agents.defaults.model.primary` 設為較小的模型。
  * 使用 `free -h` 和 `htop` 監控。


## 疑難排解

**Gateway 無法啟動** \-- 執行 `openclaw doctor --non-interactive`，並使用 `journalctl --user -u openclaw-gateway.service -n 50` 檢查日誌。

**連接埠已被使用** \-- 執行 `lsof -i :18789` 找出程序，然後停止它。

**記憶體不足** \-- 使用 `free -h` 確認 swap 已啟用。如果仍遇到 OOM，請使用 API 型模型（Claude、GPT）而不是本機模型，或升級到 2 GB Droplet。

## 後續步驟

  * [通道](</zh-TW/channels>) \-- 連接 Telegram、WhatsApp、Discord 等更多服務
  * [Gateway configuration](</zh-TW/gateway/configuration>) \-- 所有設定選項
  * [更新](</zh-TW/install/updating>) \-- 讓 OpenClaw 保持最新


## 相關

  * [安裝概覽](</zh-TW/install>)
  * [Fly.io](</zh-TW/install/fly>)
  * [Hetzner](</zh-TW/install/hetzner>)
  * [VPS hosting](</zh-TW/vps>)


Was this useful?YesNo