---
title: 文档
source_url: https://docs.openclaw.ai/zh-CN/cli/docs
scraped_at: 2026-05-25
---

# `openclaw docs`

从终端搜索实时 OpenClaw 文档索引。该命令会调用公开的 Mintlify 托管文档 MCP 搜索端点 `https://docs.openclaw.ai/mcp.SearchOpenClaw`，并在你的终端中呈现结果。

## 用法

bashCopy code
[code]
    openclaw docs                       # print docs entrypoint and example searchopenclaw docs <query...>            # search the live docs index
[/code]

参数：

参数 | 描述  
---|---  
`[query...]` | 自由格式搜索查询。多词查询会用空格连接，并作为一个查询发送。  
  
## 示例

bashCopy code
[code]
    openclaw docs browser existing-sessionopenclaw docs sandbox allowHostControlopenclaw docs gateway token secretref
[/code]

没有查询时，`openclaw docs` 会打印文档入口 URL 和一个示例搜索命令，而不是运行搜索。

## 工作原理

`openclaw docs` 会调用 `mcporter` CLI 来调用文档搜索 MCP 工具，然后将工具输出中的 `Title: / Link: / Content:` 块解析为结果列表。

为解析 `mcporter`，OpenClaw 会按顺序检查：

  1. `PATH` 上的 `mcporter`（如果存在则直接使用）。
  2. 如果已安装 `pnpm`，则使用 `pnpm dlx mcporter ...`。
  3. 如果已安装 `npx`，则使用 `npx -y mcporter ...`。


如果都不可用，该命令会失败，并提示安装 `pnpm`（`npm install -g pnpm`）。

搜索调用使用固定的 30 秒超时。结果摘要会被截断为每条约 220 个字符。

## 输出

在富文本（TTY）终端中，结果会呈现为一个标题，后跟项目符号列表。每个项目符号会显示页面标题、链接的文档 URL，以及下一行的简短摘要。空结果会打印 “No results.”。

在非富文本输出中（管道、`--no-color`、脚本），相同数据会呈现为 Markdown：

markdownCopy code
[code]
    # Docs search: <query> - [Title](https://docs.openclaw.ai/...) - snippet- [Title](https://docs.openclaw.ai/...) - snippet
[/code]

## 退出代码

代码 | 含义  
---|---  
`0` | 搜索成功（包括零结果响应）。  
`1` | MCP 工具调用失败；stderr 会内联打印。  
  
## 相关内容

  * [CLI 参考](</zh-CN/cli>)
  * [实时文档](<https://docs.openclaw.ai>)


Was this useful?YesNo