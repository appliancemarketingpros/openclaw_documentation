---
title: Web
source_url: https://docs.openclaw.ai/zh-CN/web
scraped_at: 2026-05-25
---

Gateway 网关会在与 Gateway 网关 WebSocket 相同的端口上提供一个小型**浏览器 Control UI** （Vite + Lit）：

  * 默认：`http://<host>:18789/`
  * 启用 `gateway.tls.enabled: true` 时：`https://<host>:18789/`
  * 可选前缀：设置 `gateway.controlUi.basePath`（例如 `/openclaw`）


功能请参见 [Control UI](</zh-CN/web/control-ui>)。本页其余部分重点介绍绑定模式、安全性和面向 Web 的界面。

## Webhook

当 `hooks.enabled=true` 时，Gateway 网关还会在同一个 HTTP 服务器上暴露一个小型 webhook 端点。 身份验证和负载请参见 [Gateway 网关配置](</zh-CN/gateway/configuration>) → `hooks`。

## 配置（默认开启）

当资源存在（`dist/control-ui`）时，Control UI **默认启用** 。 你可以通过配置控制它：

json5Copy code
[code]
    {  gateway: {    controlUi: { enabled: true, basePath: "/openclaw" }, // basePath 可选  },}
[/code]

## Tailscale 访问

### 集成 Serve（推荐）

将 Gateway 网关保持在 local loopback 上，并让 Tailscale Serve 为其做反向代理：

json5Copy code
[code]
    {  gateway: {    bind: "loopback",    tailscale: { mode: "serve" },  },}
[/code]

然后启动 gateway：

bashCopy code
[code]
    openclaw gateway
[/code]

打开：

  * `https://<magicdns>/`（或你配置的 `gateway.controlUi.basePath`）


### Tailnet 绑定 + token

json5Copy code
[code]
    {  gateway: {    bind: "tailnet",    controlUi: { enabled: true },    auth: { mode: "token", token: "your-token" },  },}
[/code]

然后启动 gateway（这个非 local loopback 示例使用共享密钥 token 身份验证）：

bashCopy code
[code]
    openclaw gateway
[/code]

打开：

  * `http://<tailscale-ip>:18789/`（或你配置的 `gateway.controlUi.basePath`）


### 公网（Funnel）

json5Copy code
[code]
    {  gateway: {    bind: "loopback",    tailscale: { mode: "funnel" },    auth: { mode: "password" }, // 或 OPENCLAW_GATEWAY_PASSWORD  },}
[/code]

## 安全说明

  * 默认情况下需要 Gateway 网关身份验证（token、password、trusted-proxy，或在启用时使用 Tailscale Serve 身份请求头）。
  * 非 local loopback 绑定仍然**需要** gateway 身份验证。实际上，这意味着使用 token/password 身份验证，或带 `gateway.auth.mode: "trusted-proxy"` 的身份感知反向代理。
  * 向导默认会创建共享密钥身份验证，并且通常会生成一个 gateway token（即使在 local loopback 上也是如此）。
  * 在共享密钥模式下，UI 会发送 `connect.params.auth.token` 或 `connect.params.auth.password`。
  * 当 `gateway.tls.enabled: true` 时，本地仪表板和 status 辅助工具会渲染 `https://` 仪表板 URL 和 `wss://` WebSocket URL。
  * 在带身份信息的模式下，例如 Tailscale Serve 或 `trusted-proxy`，WebSocket 身份验证检查则会改为从请求头中满足。
  * 对于非 local loopback 的 Control UI 部署，请显式设置 `gateway.controlUi.allowedOrigins` （完整 origin）。如果不设置，默认会拒绝 gateway 启动。
  * `gateway.controlUi.dangerouslyAllowHostHeaderOriginFallback=true` 会启用 Host 头 origin 回退模式，但这是危险的安全降级。
  * 使用 Serve 时，当 `gateway.auth.allowTailscale` 为 `true` 时， Tailscale 身份请求头可满足 Control UI/WebSocket 身份验证（无需 token/password）。 HTTP API 端点不会使用这些 Tailscale 身份请求头；它们仍遵循 gateway 的常规 HTTP 身份验证模式。设置 `gateway.auth.allowTailscale: false` 可要求显式凭证。请参见 [Tailscale](</zh-CN/gateway/tailscale>) 和 [安全](</zh-CN/gateway/security>)。这个 无 token 流程假定 gateway 主机是受信任的。
  * `gateway.tailscale.mode: "funnel"` 要求 `gateway.auth.mode: "password"`（共享密码）。


## 构建 UI

Gateway 网关会从 `dist/control-ui` 提供静态文件。使用以下命令构建它们：

bashCopy code
[code]
    pnpm ui:build
[/code]

Was this useful?YesNo