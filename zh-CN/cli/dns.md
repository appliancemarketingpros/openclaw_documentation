---
title: DNS
source_url: https://docs.openclaw.ai/zh-CN/cli/dns
scraped_at: 2026-05-25
---

# `openclaw dns`

用于广域设备发现（Tailscale + CoreDNS）的 DNS 辅助工具。目前专注于 macOS + Homebrew CoreDNS。

相关内容：

  * Gateway 网关设备发现：[设备发现](</zh-CN/gateway/discovery>)
  * 广域设备发现配置：[配置](</zh-CN/gateway/configuration>)


## 设置

bashCopy code
[code]
    openclaw dns setupopenclaw dns setup --domain openclaw.internalopenclaw dns setup --apply
[/code]

## `dns setup`

规划或应用用于单播 DNS-SD 设备发现的 CoreDNS 设置。

选项：

  * `--domain <domain>`：广域设备发现域名（例如 `openclaw.internal`）
  * `--apply`：安装或更新 CoreDNS 配置并重启服务（需要 sudo；仅限 macOS）


它会显示：

  * 解析后的设备发现域名
  * 区域文件路径
  * 当前 tailnet IP
  * 推荐的 `openclaw.json` 设备发现配置
  * 需要设置的 Tailscale Split DNS 名称服务器/域名值


注意事项：

  * 不带 `--apply` 时，该命令仅作为规划辅助工具，并会打印推荐设置。
  * 如果省略 `--domain`，OpenClaw 会使用配置中的 `discovery.wideArea.domain`。
  * `--apply` 目前仅支持 macOS，并要求使用 Homebrew CoreDNS。
  * `--apply` 会在需要时初始化区域文件，确保 CoreDNS import stanza 存在，并重启 `coredns` brew 服务。


## 相关内容

  * [CLI 参考](</zh-CN/cli>)
  * [设备发现](</zh-CN/gateway/discovery>)


Was this useful?YesNo