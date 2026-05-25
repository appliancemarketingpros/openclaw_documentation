---
title: 网页获取
source_url: https://docs.openclaw.ai/zh-CN/tools/web-fetch
scraped_at: 2026-05-25
---

`web_fetch` 工具会执行普通的 HTTP GET，并提取可读内容 （HTML 转为 Markdown 或文本）。它**不会** 执行 JavaScript。

对于大量依赖 JS 的站点或受登录保护的页面，请改用 [Web Browser](</zh-CN/tools/browser>)。

## 快速开始

`web_fetch` **默认启用** ，无需配置。智能体可以立即调用它：

javascriptCopy code
[code]
    await web_fetch({ url: "https://example.com/article" });
[/code]

## 工具参数

要获取的 URL。仅支持 `http(s)`。

主内容提取后的输出格式。

将输出截断到这么多字符。

## 工作原理

* ### Fetch

使用类似 Chrome 的 User-Agent 和 `Accept-Language` 标头发送 HTTP GET。阻止私有/内部主机名，并重新检查重定向。

* ### Extract

对 HTML 响应运行 Readability（主内容提取）。

* ### Fallback (optional)

如果 Readability 失败且已配置 Firecrawl，则通过 Firecrawl API 使用绕过机器人检测模式重试。

* ### Cache

结果会缓存 15 分钟（可配置），以减少对同一 URL 的重复 获取。

## 配置

json5Copy code
[code]
    {  tools: {    web: {      fetch: {        enabled: true, // default: true        provider: "firecrawl", // optional; omit for auto-detect        maxChars: 50000, // max output chars        maxCharsCap: 50000, // hard cap for maxChars param        maxResponseBytes: 2000000, // max download size before truncation        timeoutSeconds: 30,        cacheTtlMinutes: 15,        maxRedirects: 3,        useTrustedEnvProxy: false, // let a trusted HTTP(S) env proxy resolve DNS        readability: true, // use Readability extraction        userAgent: "Mozilla/5.0 ...", // override User-Agent        ssrfPolicy: {          allowRfc2544BenchmarkRange: true, // opt-in for trusted fake-IP proxies using 198.18.0.0/15          allowIpv6UniqueLocalRange: true, // opt-in for trusted fake-IP proxies using fc00::/7        },      },    },  },}
[/code]

## Firecrawl 兜底

如果 Readability 提取失败，`web_fetch` 可以回退到 [Firecrawl](</zh-CN/tools/firecrawl>)，用于绕过机器人检测并获得更好的提取效果：

json5Copy code
[code]
    {  tools: {    web: {      fetch: {        provider: "firecrawl", // optional; omit for auto-detect from available credentials      },    },  },  plugins: {    entries: {      firecrawl: {        enabled: true,        config: {          webFetch: {            apiKey: "fc-...", // optional if FIRECRAWL_API_KEY is set            baseUrl: "https://api.firecrawl.dev",            onlyMainContent: true,            maxAgeMs: 86400000, // cache duration (1 day)            timeoutSeconds: 60,          },        },      },    },  },}
[/code]

`plugins.entries.firecrawl.config.webFetch.apiKey` 支持 SecretRef 对象。 旧版 `tools.web.fetch.firecrawl.*` 配置会由 `openclaw doctor --fix` 自动迁移。

当前运行时行为：

  * `tools.web.fetch.provider` 会显式选择获取兜底提供商。
  * 如果省略 `provider`，OpenClaw 会根据可用凭证自动检测第一个就绪的 web-fetch 提供商。非沙箱隔离的 `web_fetch` 可以使用已安装的插件，这些插件声明 `contracts.webFetchProviders` 并在运行时注册匹配的提供商。目前内置提供商是 Firecrawl。
  * 沙箱隔离的 `web_fetch` 调用仍仅限于内置提供商。
  * 如果禁用 Readability，`web_fetch` 会直接跳到所选的 提供商兜底。如果没有可用提供商，它会默认拒绝并失败。


## 受信任的环境代理

如果你的部署要求 `web_fetch` 通过受信任的出站 HTTP(S) 代理，请设置 `tools.web.fetch.useTrustedEnvProxy: true`。

在此模式下，OpenClaw 仍会在发送请求前应用基于主机名的 SSRF 检查， 但会让代理解析 DNS，而不是执行本地 DNS 固定。仅当该代理由操作员控制， 并且在 DNS 解析后仍强制执行出站策略时，才启用此项。

## 限制和安全性

  * `maxChars` 会被限制在 `tools.web.fetch.maxCharsCap` 以内
  * 响应正文在解析前会被限制为 `maxResponseBytes`；超大的 响应会被截断并带有警告
  * 私有/内部主机名会被阻止
  * `tools.web.fetch.ssrfPolicy.allowRfc2544BenchmarkRange` 和 `tools.web.fetch.ssrfPolicy.allowIpv6UniqueLocalRange` 是针对 受信任假 IP 代理栈的窄范围选择启用项；除非你的代理拥有 这些合成地址范围并强制执行自己的目标策略，否则请保持未设置
  * 重定向会被检查，并受 `maxRedirects` 限制
  * `useTrustedEnvProxy` 是显式选择启用项，并且只应为 由操作员控制、在 DNS 解析后仍强制执行出站策略的代理启用
  * `web_fetch` 是尽力而为的工具，有些站点需要使用 [Web Browser](</zh-CN/tools/browser>)


## 工具配置文件

如果你使用工具配置文件或允许列表，请添加 `web_fetch` 或 `group:web`：

json5Copy code
[code]
    {  tools: {    allow: ["web_fetch"],    // or: allow: ["group:web"]  (includes web_fetch, web_search, and x_search)  },}
[/code]

## 相关内容

  * [Web Search](</zh-CN/tools/web>) \-- 使用多个提供商搜索 Web
  * [Web Browser](</zh-CN/tools/browser>) \-- 面向大量依赖 JS 的站点的完整浏览器自动化
  * [Firecrawl](</zh-CN/tools/firecrawl>) \-- Firecrawl 搜索和抓取工具


Was this useful?YesNo