---
title: 卸载
source_url: https://docs.openclaw.ai/zh-CN/install/uninstall
scraped_at: 2026-05-25
---

两种路径：

  * 如果 `openclaw` 仍已安装，使用**简易路径** 。
  * 如果 CLI 已不存在但服务仍在运行，使用**手动移除服务** 。


## 简易路径（CLI 仍已安装）

推荐：使用内置卸载程序：

bashCopy code
[code]
    openclaw uninstall
[/code]

非交互式（自动化 / npx）：

bashCopy code
[code]
    openclaw uninstall --all --yes --non-interactivenpx -y openclaw uninstall --all --yes --non-interactive
[/code]

手动步骤（结果相同）：

  1. 停止 Gateway 网关服务：

bashCopy code
[code]
    openclaw gateway stop
[/code]

  2. 卸载 Gateway 网关服务（launchd/systemd/schtasks）：

bashCopy code
[code]
    openclaw gateway uninstall
[/code]

  3. 删除状态 + 配置：

bashCopy code
[code]
    rm -rf "${OPENCLAW_STATE_DIR:-$HOME/.openclaw}"
[/code]

如果你将 `OPENCLAW_CONFIG_PATH` 设置为状态目录之外的自定义位置，也请删除该文件。

  4. 删除你的工作区（可选，会移除智能体文件）：

bashCopy code
[code]
    rm -rf ~/.openclaw/workspace
[/code]

  5. 移除 CLI 安装（选择你使用的方式）：

bashCopy code
[code]
    npm rm -g openclawpnpm remove -g openclawbun remove -g openclaw
[/code]

  6. 如果你安装了 macOS 应用：

bashCopy code
[code]
    rm -rf /Applications/OpenClaw.app
[/code]

说明：

  * 如果你使用了配置文件（`--profile` / `OPENCLAW_PROFILE`），请对每个状态目录重复步骤 3（默认值为 `~/.openclaw-<profile>`）。
  * 在远程模式下，状态目录位于**Gateway 网关主机** 上，因此也要在那里运行步骤 1-4。


## 手动移除服务（CLI 未安装）

如果 Gateway 网关服务持续运行但 `openclaw` 缺失，请使用此方法。

### macOS（launchd）

默认标签为 `ai.openclaw.gateway`（或 `ai.openclaw.<profile>`；旧版 `com.openclaw.*` 可能仍然存在）：

bashCopy code
[code]
    launchctl bootout gui/$UID/ai.openclaw.gatewayrm -f ~/Library/LaunchAgents/ai.openclaw.gateway.plist
[/code]

如果你使用了配置文件，请将标签和 plist 名称替换为 `ai.openclaw.<profile>`。如果存在任何旧版 `com.openclaw.*` plist，也请将其删除。

### Linux（systemd 用户单元）

默认单元名称为 `openclaw-gateway.service`（或 `openclaw-gateway-<profile>.service`）：

bashCopy code
[code]
    systemctl --user disable --now openclaw-gateway.servicerm -f ~/.config/systemd/user/openclaw-gateway.servicesystemctl --user daemon-reload
[/code]

### Windows（计划任务）

默认任务名称为 `OpenClaw Gateway`（或 `OpenClaw Gateway (<profile>)`）。 任务脚本位于你的状态目录下。

powershellCopy code
[code]
    schtasks /Delete /F /TN "OpenClaw Gateway"Remove-Item -Force "$env:USERPROFILE\.openclaw\gateway.cmd"
[/code]

如果你使用了配置文件，请删除匹配的任务名称和 `~\.openclaw-<profile>\gateway.cmd`。

## 正常安装 vs 源码检出

### 正常安装（[install.sh](<http://install.sh>) / npm / pnpm / bun）

如果你使用了 `https://openclaw.ai/install.sh` 或 `install.ps1`，CLI 是通过 `npm install -g openclaw@latest` 安装的。 请使用 `npm rm -g openclaw` 将其移除（如果你是通过 `pnpm` / `bun` 安装的，则使用 `pnpm remove -g` / `bun remove -g`）。

### 源码检出（git clone）

如果你是从仓库检出运行（`git clone` \+ `openclaw ...` / `bun run openclaw ...`）：

  1. 在删除仓库之前**先** 卸载 Gateway 网关服务（使用上面的简易路径或手动移除服务）。
  2. 删除仓库目录。
  3. 按上文所示移除状态 + 工作区。


## 相关

  * [安装概览](</zh-CN/install>)
  * [迁移指南](</zh-CN/install/migrating>)


Was this useful?YesNo