---
title: 入门指南
source_url: https://docs.openclaw.ai/zh-CN/start/getting-started
scraped_at: 2026-05-25
---

安装 OpenClaw，运行新手引导，并与你的 AI 助手聊天，全程大约 5 分钟。完成后，你将拥有一个正在运行的 Gateway 网关、已配置的凭证， 以及一个可用的聊天会话。

## 你需要准备

  * **Node.js** — 推荐 Node 24（也支持 Node 22.16+）
  * 来自模型提供商的 **API key** （Anthropic、OpenAI、Google 等）— 新手引导会提示你输入


## 快速设置

* ### 安装 OpenClaw

### macOS / Linux

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash
[/code]

![安装脚本流程](/assets/install-script.svg)

### Windows (PowerShell)

powershellCopy code
[code]
    iwr -useb https://openclaw.ai/install.ps1 | iex
[/code]

* ### 运行新手引导

bashCopy code
[code]
    openclaw onboard --install-daemon
[/code]

向导会引导你选择模型提供商、设置 API key， 并配置 Gateway 网关。大约需要 2 分钟。

完整参考见 [新手引导（CLI）](</zh-CN/start/wizard>)。

* ### 验证 Gateway 网关正在运行

bashCopy code
[code]
    openclaw gateway status
[/code]

你应该会看到 Gateway 网关正在监听端口 18789。

* ### 打开仪表板

bashCopy code
[code]
    openclaw dashboard
[/code]

这会在你的浏览器中打开 Control UI。如果它能加载，说明一切正常。

* ### 发送你的第一条消息

在 Control UI 聊天中输入一条消息，你应该会收到 AI 回复。

想改用手机聊天？最快可设置的渠道是 [Telegram](</zh-CN/channels/telegram>)（只需要一个 bot token）。所有选项见 [渠道](</zh-CN/channels>)。

高级：挂载自定义 Control UI 构建

如果你维护本地化或自定义的仪表板构建，请将 `gateway.controlUi.root` 指向一个包含已构建静态 资源和 `index.html` 的目录。

bashCopy code
[code]
    mkdir -p "$HOME/.openclaw/control-ui-custom"# Copy your built static files into that directory.
[/code]

然后设置：

jsonCopy code
[code]
    {"gateway": {  "controlUi": {    "enabled": true,    "root": "$HOME/.openclaw/control-ui-custom"  }}}
[/code]

重启 Gateway 网关并重新打开仪表板：

bashCopy code
[code]
    openclaw gateway restartopenclaw dashboard
[/code]

## 下一步

[**连接渠道** Discord、Feishu、iMessage、Matrix、Microsoft Teams、Signal、Slack、Telegram、WhatsApp、Zalo 等。 ](</zh-CN/channels>) [**配对和安全** 控制谁可以给你的智能体发消息。 ](</zh-CN/channels/pairing>) [**配置 Gateway 网关** 模型、工具、沙箱和高级设置。 ](</zh-CN/gateway/configuration>) [**浏览工具** 浏览器、exec、Web 搜索、skills 和插件。 ](</zh-CN/tools>)

高级：环境变量

如果你将 OpenClaw 作为服务账号运行，或想使用自定义路径：

  * `OPENCLAW_HOME` — 用于内部路径解析的主目录
  * `OPENCLAW_STATE_DIR` — 覆盖状态目录
  * `OPENCLAW_CONFIG_PATH` — 覆盖配置文件路径


完整参考：[环境变量](</zh-CN/help/environment>)。

## 相关内容

  * [安装概览](</zh-CN/install>)
  * [渠道概览](</zh-CN/channels>)
  * [设置](</zh-CN/start/setup>)


Was this useful?YesNo