---
title: Ansible
source_url: https://docs.openclaw.ai/zh-CN/install/ansible
scraped_at: 2026-05-25
---

使用 **[openclaw-ansible](<https://github.com/openclaw/openclaw-ansible>)** 将 OpenClaw 部署到生产服务器，这是一个采用安全优先架构的自动化安装器。

## 前提条件

要求 | 详细信息  
---|---  
**OS** | Debian 11+ 或 Ubuntu 20.04+  
**访问权限** | Root 或 sudo 权限  
**网络** | 用于安装软件包的互联网连接  
**Ansible** | 2.14+（由快速开始脚本自动安装）  
  
## 你会获得什么

  * **防火墙优先的安全性** \-- UFW + Docker 隔离（仅 SSH + Tailscale 可访问）
  * **Tailscale VPN** \-- 无需公开暴露服务即可安全远程访问
  * **Docker** \-- 隔离的沙箱容器，仅 localhost 绑定
  * **纵深防御** \-- 4 层安全架构
  * **Systemd 集成** \-- 启动时自动启动并加固
  * **一条命令完成设置** \-- 数分钟内完成部署


## 快速开始

一条命令安装：

bashCopy code
[code]
    curl -fsSL https://raw.githubusercontent.com/openclaw/openclaw-ansible/main/install.sh | bash
[/code]

## 会安装什么

Ansible playbook 会安装并配置：

  1. **Tailscale** \-- 用于安全远程访问的 mesh VPN
  2. **UFW 防火墙** \-- 仅开放 SSH + Tailscale 端口
  3. **Docker CE + Compose V2** \-- 用于默认的智能体沙箱后端
  4. **Node.js 24 + pnpm** \-- 运行时依赖（Node 22 LTS，目前为 `22.16+`，仍受支持）
  5. **OpenClaw** \-- 基于主机运行，不容器化
  6. **Systemd 服务** \-- 通过安全加固实现自动启动


## 安装后设置

* ### 切换到 openclaw 用户

bashCopy code
[code]
    sudo -i -u openclaw
[/code]

* ### 运行新手引导向导

安装后脚本会引导你配置 OpenClaw 设置。

* ### 连接消息提供商

登录 WhatsApp、Telegram、Discord 或 Signal：

bashCopy code
[code]
    openclaw channels login
[/code]

* ### 验证安装

bashCopy code
[code]
    sudo systemctl status openclawsudo journalctl -u openclaw -f
[/code]

* ### 连接到 Tailscale

加入你的 VPN mesh 以进行安全远程访问。

### 快捷命令

bashCopy code
[code]
    # Check service statussudo systemctl status openclaw # View live logssudo journalctl -u openclaw -f # Restart gatewaysudo systemctl restart openclaw # Provider login (run as openclaw user)sudo -i -u openclawopenclaw channels login
[/code]

## 安全架构

该部署使用 4 层防御模型：

  1. **防火墙 (UFW)** \-- 仅公开暴露 SSH (22) + Tailscale (41641/udp)
  2. **VPN (Tailscale)** \-- Gateway 网关只能通过 VPN mesh 访问
  3. **Docker 隔离** \-- DOCKER-USER iptables 链防止外部端口暴露
  4. **Systemd 加固** \-- NoNewPrivileges、PrivateTmp、非特权用户


验证你的外部攻击面：

bashCopy code
[code]
    nmap -p- YOUR_SERVER_IP
[/code]

只有端口 22 (SSH) 应该处于开放状态。所有其他服务（Gateway 网关、Docker）都会被锁定。

Docker 是为智能体沙箱（隔离的工具执行）而安装的，不用于运行 Gateway 网关本身。沙箱配置请参阅 [Multi-Agent Sandbox and Tools](</zh-CN/tools/multi-agent-sandbox-tools>)。

## 手动安装

如果你希望手动控制自动化流程：

* ### 安装前提条件

bashCopy code
[code]
    sudo apt update && sudo apt install -y ansible git
[/code]

* ### 克隆仓库

bashCopy code
[code]
    git clone https://github.com/openclaw/openclaw-ansible.gitcd openclaw-ansible
[/code]

* ### 安装 Ansible collections

bashCopy code
[code]
    ansible-galaxy collection install -r requirements.yml
[/code]

* ### 运行 playbook

bashCopy code
[code]
    ./run-playbook.sh
[/code]

或者，直接运行，然后在之后手动执行设置脚本：

bashCopy code
[code]
    ansible-playbook playbook.yml --ask-become-pass# Then run: /tmp/openclaw-setup.sh
[/code]

## 更新

Ansible 安装器会设置 OpenClaw 以便手动更新。标准更新流程请参阅 [Updating](</zh-CN/install/updating>)。

重新运行 Ansible playbook（例如用于配置变更）：

bashCopy code
[code]
    cd openclaw-ansible./run-playbook.sh
[/code]

它是幂等的，可以安全地多次运行。

## 故障排除

防火墙阻止我的连接

  * 确保你可以先通过 Tailscale VPN 访问
  * SSH 访问（端口 22）始终允许
  * Gateway 网关按设计只能通过 Tailscale 访问

服务无法启动 bashCopy code
[code]
    # Check logssudo journalctl -u openclaw -n 100 # Verify permissionssudo ls -la /opt/openclaw # Test manual startsudo -i -u openclawcd ~/openclawopenclaw gateway run
[/code]

Docker 沙箱问题 bashCopy code
[code]
    # Verify Docker is runningsudo systemctl status docker # Check sandbox imagesudo docker images | grep openclaw-sandbox # Build sandbox image if missing (requires source checkout)cd /opt/openclaw/openclawsudo -u openclaw ./scripts/sandbox-setup.sh# For npm installs without a source checkout, see# https://docs.openclaw.ai/gateway/sandboxing#images-and-setup
[/code]

提供商登录失败

确保你正以 `openclaw` 用户运行：

bashCopy code
[code]
    sudo -i -u openclawopenclaw channels login
[/code]

## 高级配置

有关详细的安全架构和故障排除，请参阅 openclaw-ansible 仓库：

  * [安全架构](<https://github.com/openclaw/openclaw-ansible/blob/main/docs/security.md>)
  * [技术细节](<https://github.com/openclaw/openclaw-ansible/blob/main/docs/architecture.md>)
  * [故障排除指南](<https://github.com/openclaw/openclaw-ansible/blob/main/docs/troubleshooting.md>)


## 相关内容

  * [openclaw-ansible](<https://github.com/openclaw/openclaw-ansible>) \-- 完整部署指南
  * [Docker](</zh-CN/install/docker>) \-- 容器化 Gateway 网关设置
  * [沙箱隔离](</zh-CN/gateway/sandboxing>) \-- 智能体沙箱配置
  * [Multi-Agent Sandbox and Tools](</zh-CN/tools/multi-agent-sandbox-tools>) \-- 每个智能体的隔离


Was this useful?YesNo