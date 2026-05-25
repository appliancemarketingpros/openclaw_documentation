---
title: 配置
source_url: https://docs.openclaw.ai/zh-CN/cli/configure
scraped_at: 2026-05-25
---

# `openclaw configure`

用于对现有设置进行定向更改的交互式提示：凭证、设备、智能体默认值、Gateway 网关、渠道、插件、Skills 和健康检查。

使用 `openclaw onboard` 完成完整的首次运行引导流程，使用 `openclaw setup` 仅设置基线配置/工作区，只需要设置渠道账号时使用 `openclaw channels add`。

当 configure 从提供商认证选择启动时，默认模型和允许列表选择器会自动优先使用该提供商。对于 Volcengine 和 BytePlus 等成对提供商，相同的偏好也会匹配它们的编码计划变体（`volcengine-plan/*`、`byteplus-plan/*`）。如果首选提供商筛选器会生成空列表，configure 会回退到未筛选的目录，而不是显示空白选择器。

对于 Web 搜索，`openclaw configure --section web` 可让你选择提供商 并配置其凭证。某些提供商还会显示特定于提供商的 后续提示：

  * **Grok** 可以使用相同的 `XAI_API_KEY` 提供可选的 `x_search` 设置，并 让你选择一个 `x_search` 模型。
  * **Kimi** 可以询问 Moonshot API 区域（`api.moonshot.ai` 与 `api.moonshot.cn`）以及默认 Kimi Web 搜索模型。


相关：

  * Gateway 网关配置参考：[配置](</zh-CN/gateway/configuration>)
  * 配置 CLI：[配置](</zh-CN/cli/config>)


## 选项

  * `--section <section>`：可重复的部分筛选器


可用部分：

  * `workspace`
  * `model`
  * `web`
  * `gateway`
  * `daemon`
  * `channels`
  * `plugins`
  * `skills`
  * `health`


注意事项：

  * 选择 Gateway 网关运行位置总是会更新 `gateway.mode`。如果这就是你需要的全部内容，可以在不选择其他部分的情况下选择“继续”。
  * 写入本地配置后，如果所选设置路径需要可下载插件，configure 会安装所选插件。远程 Gateway 网关配置不会安装本地插件包。
  * 面向渠道的服务（Slack/Discord/Matrix/Microsoft Teams）会在设置期间提示输入渠道/房间允许列表。你可以输入名称或 ID；向导会在可能的情况下将名称解析为 ID。
  * 如果你运行 daemon 安装步骤，令牌认证需要令牌，并且 `gateway.auth.token` 由 SecretRef 管理，configure 会验证 SecretRef，但不会将解析后的明文令牌值持久化到 supervisor 服务环境元数据中。
  * 如果令牌认证需要令牌，而配置的令牌 SecretRef 未解析，configure 会阻止 daemon 安装，并给出可执行的修复指导。
  * 如果同时配置了 `gateway.auth.token` 和 `gateway.auth.password`，且 `gateway.auth.mode` 未设置，configure 会阻止 daemon 安装，直到显式设置模式。


## 示例

bashCopy code
[code]
    openclaw configureopenclaw configure --section webopenclaw configure --section model --section channelsopenclaw configure --section gateway --section daemon
[/code]

## 相关

  * [CLI 参考](</zh-CN/cli>)
  * [配置](</zh-CN/gateway/configuration>)


Was this useful?YesNo