---
title: 创建技能
source_url: https://docs.openclaw.ai/zh-CN/tools/creating-skills
scraped_at: 2026-05-25
---

Skills 教会智能体如何以及何时使用工具。每个技能都是一个目录， 其中包含一个带有 YAML frontmatter 和 Markdown 指令的 `SKILL.md` 文件。

有关 Skills 如何加载和优先排序，请参阅 [Skills](</zh-CN/tools/skills>)。

## 创建你的第一个技能

* ### Create the skill directory

Skills 位于你的工作区中。创建一个新文件夹：

bashCopy code
[code]
    mkdir -p ~/.openclaw/workspace/skills/hello-world
[/code]

* ### Write SKILL.md

在该目录中创建 `SKILL.md`。frontmatter 定义元数据， Markdown 正文包含给智能体的指令。

markdownCopy code
[code]
    ---name: hello-worlddescription: A simple skill that says hello.--- # Hello World Skill When the user asks for a greeting, use the `echo` tool to say"Hello from your custom skill!".
[/code]

技能 `name` 使用由小写字母、数字和连字符组成的连字符命名法。 保持文件夹名称与 frontmatter `name` 一致。

* ### Add tools (optional)

你可以在 frontmatter 中定义自定义工具 schema，或指示智能体 使用现有系统工具（例如 `exec` 或 `browser`）。Skills 也可以 随插件一起提供，并与它们所记录的工具放在一起。

* ### Load the skill

启动一个新会话，让 OpenClaw 载入该技能：

bashCopy code
[code]
    # From chat/new # Or restart the gatewayopenclaw gateway restart
[/code]

验证该技能已加载：

bashCopy code
[code]
    openclaw skills list
[/code]

* ### Test it

发送一条应该触发该技能的消息：

bashCopy code
[code]
    openclaw agent --message "give me a greeting"
[/code]

或者直接与智能体聊天并请求问候语。

## 技能元数据参考

YAML frontmatter 支持这些字段：

字段 | 必需 | 描述  
---|---|---  
`name` | 是 | 使用小写字母、数字和连字符的唯一标识符  
`description` | 是 | 显示给智能体的一行描述  
`metadata.openclaw.os` | 否 | OS 过滤器（`["darwin"]`、`["linux"]` 等）  
`metadata.openclaw.requires.bins` | 否 | PATH 上所需的二进制文件  
`metadata.openclaw.requires.config` | 否 | 所需的配置键  
  
## 最佳实践

  * **保持简洁** —— 指示模型要做_什么_，而不是如何成为 AI
  * **安全优先** —— 如果你的技能使用 `exec`，请确保提示不会允许来自不受信任输入的任意命令注入
  * **本地测试** —— 分享前使用 `openclaw agent --message "..."` 进行测试
  * **使用 ClawHub** —— 在 [ClawHub](<https://clawhub.ai>) 浏览和贡献技能


## Skills 存放位置

位置 | 优先级 | 范围  
---|---|---  
`\<workspace\>/skills/` | 最高 | 每个智能体  
`\<workspace\>/.agents/skills/` | 高 | 每个工作区智能体  
`~/.agents/skills/` | 中 | 共享智能体配置档  
`~/.openclaw/skills/` | 中 | 共享（所有智能体）  
内置（随 OpenClaw 提供） | 低 | 全局  
`skills.load.extraDirs` | 最低 | 自定义共享文件夹  
  
## 相关

  * [Skills 参考](</zh-CN/tools/skills>) —— 加载、优先级和门控规则
  * [Skills 配置](</zh-CN/tools/skills-config>) —— `skills.*` 配置 schema
  * [ClawHub](</zh-CN/clawhub>) —— 公共技能注册表
  * [构建插件](</zh-CN/plugins/building-plugins>) —— 插件可以随附 Skills


Was this useful?YesNo