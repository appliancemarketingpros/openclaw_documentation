---
title: 健康状态
source_url: https://docs.openclaw.ai/zh-CN/cli/health
scraped_at: 2026-05-25
---

# `openclaw health`

从正在运行的 Gateway 网关获取健康状态。

## 选项

标志 | 默认值 | 描述  
---|---|---  
`--json` | `false` | 输出机器可读的 JSON，而不是文本。  
`--timeout <ms>` | `10000` | 连接超时，单位为毫秒。  
`--verbose` | `false` | 详细日志记录。强制执行实时探测，并展开每个智能体的输出。  
`--debug` | `false` | `--verbose` 的别名。  
  
示例：

bashCopy code
[code]
    openclaw healthopenclaw health --jsonopenclaw health --timeout 2500openclaw health --verboseopenclaw health --debug
[/code]

备注：

  * 默认的 `openclaw health` 会向正在运行的 Gateway 网关请求其健康状态快照。当该 Gateway 网关已有新的缓存快照时，它可以返回该缓存负载，并在后台刷新。
  * `--verbose` 会强制执行实时探测，打印 Gateway 网关连接详情，并展开所有已配置账户和智能体的 人类可读输出。
  * 当配置了多个智能体时，输出会包含每个智能体的会话存储。


## 相关内容

  * [CLI 参考](</zh-CN/cli>)
  * [Gateway 网关健康状态](</zh-CN/gateway/health>)


Was this useful?YesNo