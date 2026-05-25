---
title: apply_patch 工具
source_url: https://docs.openclaw.ai/zh-CN/tools/apply-patch
scraped_at: 2026-05-25
---

使用结构化补丁格式应用文件更改。它很适合多文件或多 hunk 编辑，在这些场景中单个 `edit` 调用会比较脆弱。

该工具接受单个 `input` 字符串，其中包装一个或多个文件操作：

CodeCopy code
[code]
    *** Begin Patch*** Add File: path/to/file.txt+line 1+line 2*** Update File: src/app.ts@@-old line+new line*** Delete File: obsolete.txt*** End Patch
[/code]

## 参数

  * `input`（必需）：完整补丁内容，包括 `*** Begin Patch` 和 `*** End Patch`。


## 说明

  * 补丁路径支持相对路径（从工作区目录开始）和绝对路径。
  * `tools.exec.applyPatch.workspaceOnly` 默认值为 `true`（限制在工作区内）。仅当你有意让 `apply_patch` 在工作区目录外写入/删除时，才将它设为 `false`。
  * 在 `*** Update File:` hunk 中使用 `*** Move to:` 来重命名文件。
  * `*** End of File` 在需要时标记仅 EOF 插入。
  * 默认可用于 OpenAI 和 OpenAI Codex 模型。设置 `tools.exec.applyPatch.enabled: false` 可禁用它。
  * 可选择通过 `tools.exec.applyPatch.allowModels` 按模型设置门控。
  * 配置仅位于 `tools.exec` 下。


## 示例

jsonCopy code
[code]
    {  "tool": "apply_patch",  "input": "*** Begin Patch\n*** Update File: src/index.ts\n@@\n-const foo = 1\n+const foo = 2\n*** End Patch"}
[/code]

## 相关

[**Diffs** 用于变更呈现的只读 diff 查看器。 ](</zh-CN/tools/diffs>) [**Exec tool** 来自智能体的 shell 命令执行。 ](</zh-CN/tools/exec>) [**Code execution** 使用 xAI 的沙箱隔离远程 Python 分析。 ](</zh-CN/tools/code-execution>)

Was this useful?YesNo