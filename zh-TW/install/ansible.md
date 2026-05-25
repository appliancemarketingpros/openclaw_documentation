---
title: Ansible
source_url: https://docs.openclaw.ai/zh-TW/install/ansible
scraped_at: 2026-05-25
---

Deploy OpenClaw 至生產伺服器，使用 **[openclaw-ansible](<https://github.com/openclaw/openclaw-ansible>)** \-- 具備安全優先架構的自動化安裝程式。

## 先決條件

需求 | 詳細資訊  
---|---  
**OS** | Debian 11+ 或 Ubuntu 20.04+  
**存取權限** | Root 或 sudo 權限  
**網路** | 用於套件安裝的網際網路連線  
**Ansible** | 2.14+（由快速開始指令碼自動安裝）  
  
## 你會獲得

  * **防火牆優先的安全性** \-- UFW + Docker 隔離（僅 SSH + Tailscale 可存取）
  * **Tailscale VPN** \-- 安全遠端存取，不公開暴露服務
  * **Docker** \-- 隔離的沙箱容器、僅限 localhost 綁定
  * **縱深防禦** \-- 4 層安全架構
  * **Systemd 整合** \-- 開機自動啟動並強化安全性
  * **單一命令設定** \-- 幾分鐘內完成部署


## 快速開始

單一命令安裝：

bashCopy code
[code]
    curl -fsSL https://raw.githubusercontent.com/openclaw/openclaw-ansible/main/install.sh | bash
[/code]

## 安裝內容

Ansible playbook 會安裝並設定：

  1. **Tailscale** \-- 用於安全遠端存取的網狀 VPN
  2. **UFW 防火牆** \-- 僅開放 SSH + Tailscale 連接埠
  3. **Docker CE + Compose V2** \-- 用於預設代理沙箱後端
  4. **Node.js 24 + pnpm** \-- 執行階段相依套件（Node 22 LTS，目前為 `22.16+`，仍受支援）
  5. **OpenClaw** \-- 以主機為基礎，不容器化
  6. **Systemd 服務** \-- 自動啟動並進行安全強化


## 安裝後設定

* ### 切換到 openclaw 使用者

bashCopy code
[code]
    sudo -i -u openclaw
[/code]

* ### 執行上線精靈

安裝後指令碼會引導你設定 OpenClaw 設定。

* ### 連接訊息服務提供者

登入 WhatsApp、Telegram、Discord 或 Signal：

bashCopy code
[code]
    openclaw channels login
[/code]

* ### 驗證安裝

bashCopy code
[code]
    sudo systemctl status openclawsudo journalctl -u openclaw -f
[/code]

* ### 連接到 Tailscale

加入你的 VPN 網狀網路，以進行安全遠端存取。

### 快速命令

bashCopy code
[code]
    # Check service statussudo systemctl status openclaw # View live logssudo journalctl -u openclaw -f # Restart gatewaysudo systemctl restart openclaw # Provider login (run as openclaw user)sudo -i -u openclawopenclaw channels login
[/code]

## 安全架構

部署使用 4 層防禦模型：

  1. **防火牆 (UFW)** \-- 僅公開暴露 SSH (22) + Tailscale (41641/udp)
  2. **VPN (Tailscale)** \-- Gateway 僅可透過 VPN 網狀網路存取
  3. **Docker 隔離** \-- DOCKER-USER iptables 鏈防止外部連接埠暴露
  4. **Systemd 強化** \-- NoNewPrivileges、PrivateTmp、無特權使用者


若要驗證你的外部攻擊面：

bashCopy code
[code]
    nmap -p- YOUR_SERVER_IP
[/code]

只有連接埠 22 (SSH) 應該開放。所有其他服務（Gateway、Docker）都會被鎖定。

Docker 是為代理沙箱（隔離的工具執行）而安裝，不是用來執行 Gateway 本身。沙箱設定請參閱[多代理沙箱與工具](</zh-TW/tools/multi-agent-sandbox-tools>)。

## 手動安裝

如果你偏好手動控制自動化流程：

* ### 安裝先決條件

bashCopy code
[code]
    sudo apt update && sudo apt install -y ansible git
[/code]

* ### 複製儲存庫

bashCopy code
[code]
    git clone https://github.com/openclaw/openclaw-ansible.gitcd openclaw-ansible
[/code]

* ### 安裝 Ansible collections

bashCopy code
[code]
    ansible-galaxy collection install -r requirements.yml
[/code]

* ### 執行 playbook

bashCopy code
[code]
    ./run-playbook.sh
[/code]

或者，直接執行，然後再手動執行設定指令碼：

bashCopy code
[code]
    ansible-playbook playbook.yml --ask-become-pass# Then run: /tmp/openclaw-setup.sh
[/code]

## 更新

Ansible 安裝程式會設定 OpenClaw 以供手動更新。標準更新流程請參閱[更新](</zh-TW/install/updating>)。

若要重新執行 Ansible playbook（例如用於設定變更）：

bashCopy code
[code]
    cd openclaw-ansible./run-playbook.sh
[/code]

這是冪等的，可安全地多次執行。

## 疑難排解

防火牆封鎖我的連線

  * 先確認你可以透過 Tailscale VPN 存取
  * SSH 存取（連接埠 22）一律允許
  * Gateway 設計上僅可透過 Tailscale 存取

服務無法啟動 bashCopy code
[code]
    # Check logssudo journalctl -u openclaw -n 100 # Verify permissionssudo ls -la /opt/openclaw # Test manual startsudo -i -u openclawcd ~/openclawopenclaw gateway run
[/code]

Docker 沙箱問題 bashCopy code
[code]
    # Verify Docker is runningsudo systemctl status docker # Check sandbox imagesudo docker images | grep openclaw-sandbox # Build sandbox image if missing (requires source checkout)cd /opt/openclaw/openclawsudo -u openclaw ./scripts/sandbox-setup.sh# For npm installs without a source checkout, see# https://docs.openclaw.ai/gateway/sandboxing#images-and-setup
[/code]

提供者登入失敗

請確認你正以 `openclaw` 使用者身分執行：

bashCopy code
[code]
    sudo -i -u openclawopenclaw channels login
[/code]

## 進階設定

如需詳細的安全架構與疑難排解，請參閱 openclaw-ansible 儲存庫：

  * [安全架構](<https://github.com/openclaw/openclaw-ansible/blob/main/docs/security.md>)
  * [技術詳細資訊](<https://github.com/openclaw/openclaw-ansible/blob/main/docs/architecture.md>)
  * [疑難排解指南](<https://github.com/openclaw/openclaw-ansible/blob/main/docs/troubleshooting.md>)


## 相關

  * [openclaw-ansible](<https://github.com/openclaw/openclaw-ansible>) \-- 完整部署指南
  * [Docker](</zh-TW/install/docker>) \-- 容器化 Gateway 設定
  * [沙箱](</zh-TW/gateway/sandboxing>) \-- 代理沙箱設定
  * [多代理沙箱與工具](</zh-TW/tools/multi-agent-sandbox-tools>) \-- 逐代理隔離


Was this useful?YesNo