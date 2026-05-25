---
title: Nix
source_url: https://docs.openclaw.ai/zh-CN/install/nix
scraped_at: 2026-05-25
---

声明式安装 OpenClaw：使用 **[nix-openclaw](<https://github.com/openclaw/nix-openclaw>)** ，这是第一方、功能齐备的 Home Manager 模块。

## 你将获得什么

  * Gateway 网关 + macOS 应用 + 工具（whisper、spotify、cameras）-- 全部固定版本
  * 重启后仍会保留的 launchd 服务
  * 带声明式配置的插件系统
  * 即时回滚：`home-manager switch --rollback`


## 快速开始

* ### 安装 Determinate Nix

如果尚未安装 Nix，请按照 [Determinate Nix 安装器](<https://github.com/DeterminateSystems/nix-installer>)说明操作。

* ### 创建本地 flake

使用 nix-openclaw 仓库中的 agent 优先模板：

bashCopy code
[code]
    mkdir -p ~/code/openclaw-local# Copy templates/agent-first/flake.nix from the nix-openclaw repo
[/code]

* ### 配置密钥

设置你的消息传递 bot 令牌和模型提供商 API key。放在 `~/.secrets/` 下的纯文件即可。

* ### 填写模板占位符并切换

bashCopy code
[code]
    home-manager switch
[/code]

* ### 验证

确认 launchd 服务正在运行，并且你的 bot 会响应消息。

请参阅 [nix-openclaw README](<https://github.com/openclaw/nix-openclaw>)，了解完整的模块选项和示例。

## Nix 模式运行时行为

设置 `OPENCLAW_NIX_MODE=1` 时（使用 nix-openclaw 会自动设置），OpenClaw 会进入用于 Nix 托管安装的确定性模式。其他 Nix 包也可以设置同一模式；nix-openclaw 是第一方参考实现。

你也可以手动设置：

bashCopy code
[code]
    export OPENCLAW_NIX_MODE=1
[/code]

在 macOS 上，GUI 应用不会自动继承 shell 环境变量。请改用 defaults 启用 Nix 模式：

bashCopy code
[code]
    defaults write ai.openclaw.mac openclaw.nixMode -bool true
[/code]

### Nix 模式会改变什么

  * 自动安装和自我变更流程会被禁用
  * `openclaw.json` 会被视为不可变。启动时派生的默认值只保留在运行时，并且设置、新手引导、会修改配置的 `openclaw update`、插件安装/更新/卸载/启用、`doctor --fix`、`doctor --generate-gateway-token` 和 `openclaw config set` 等配置写入器都会拒绝编辑该文件。
  * Agent 应改为编辑 Nix 源。对于 nix-openclaw，请使用 agent 优先的[快速开始](<https://github.com/openclaw/nix-openclaw#quick-start>)，并在 `programs.openclaw.config` 或 `instances.<name>.config` 下设置配置。
  * 缺失依赖会显示 Nix 专用的修复消息
  * UI 会显示只读 Nix 模式横幅


### 配置和状态路径

OpenClaw 从 `OPENCLAW_CONFIG_PATH` 读取 JSON5 配置，并将可变数据存储在 `OPENCLAW_STATE_DIR` 中。在 Nix 下运行时，请将这些路径显式设置为 Nix 托管位置，确保运行时状态和配置不会进入不可变 store。

变量 | 默认值  
---|---  
`OPENCLAW_HOME` | `HOME` / `USERPROFILE` / `os.homedir()`  
`OPENCLAW_STATE_DIR` | `~/.openclaw`  
`OPENCLAW_CONFIG_PATH` | `$OPENCLAW_STATE_DIR/openclaw.json`  
  
### 服务 PATH 发现

launchd/systemd Gateway 网关服务会自动发现 Nix profile 二进制文件，因此 通过 shell 调用 `nix` 安装可执行文件的插件和工具无需 手动设置 PATH 即可工作：

  * 设置 `NIX_PROFILES` 时，每个条目都会按 从右到左的优先级加入服务 PATH（与 Nix shell 优先级一致 -- 最右侧获胜）。
  * 未设置 `NIX_PROFILES` 时，会将 `~/.nix-profile/bin` 作为回退加入。


这同时适用于 macOS launchd 和 Linux systemd 服务环境。

## 相关

[**nix-openclaw** 权威 Home Manager 模块和完整设置指南。 ](<https://github.com/openclaw/nix-openclaw>) [**设置向导** 非 Nix CLI 设置演练。 ](</zh-CN/start/wizard>) [**Docker** 作为非 Nix 替代方案的容器化设置。 ](</zh-CN/install/docker>) [**更新** 随包一起更新由 Home Manager 管理的安装。 ](</zh-CN/install/updating>)

Was this useful?YesNo