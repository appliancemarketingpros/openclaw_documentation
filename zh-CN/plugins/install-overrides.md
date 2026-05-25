---
title: 插件安装覆盖项
source_url: https://docs.openclaw.ai/zh-CN/plugins/install-overrides
scraped_at: 2026-05-25
---

插件安装覆盖允许维护者针对特定 npm 软件包或本地 `npm-pack` tar 包测试设置期间的插件安装。它们仅用于 E2E 和软件包验证。普通用户应使用 [`openclaw plugins install`](</zh-CN/cli/plugins>) 安装插件。

## 环境

除非同时设置这两个变量，否则覆盖会被禁用：

bashCopy code
[code]
    export OPENCLAW_ALLOW_PLUGIN_INSTALL_OVERRIDES=1export OPENCLAW_PLUGIN_INSTALL_OVERRIDES='{  "codex": "npm-pack:/tmp/openclaw-codex-2026.5.8.tgz",  "openclaw-web-search": "npm:@openclaw/web-search@2026.5.8"}'
[/code]

覆盖映射是以插件 id 为键的 JSON。值支持：

  * `npm:<registry-spec>`，用于注册表软件包以及精确版本或标签
  * `npm-pack:<path.tgz>`，用于由 `npm pack` 生成的本地 tar 包


相对 `npm-pack:` 路径会从当前工作目录解析。

## 行为

当设置期间的流程请求安装某个插件，且该插件的 id 出现在映射中时，OpenClaw 会使用覆盖来源，而不是目录、内置或默认的 npm 来源。这适用于新手引导以及其他使用共享设置期间插件安装器的流程。

覆盖仍会强制检查预期的插件 id。映射到 `codex` 的 tar 包必须安装清单 id 为 `codex` 的插件。

覆盖不会继承官方可信来源状态。即使目录条目通常代表 OpenClaw 拥有的软件包，覆盖也会被视为操作者提供的测试输入。

工作区 `.env` 文件无法启用安装覆盖。请在启动 OpenClaw 的可信 shell、CI 作业或远程测试命令中设置这些变量。

## 包 E2E

使用隔离的状态目录，避免软件包安装和安装记录触碰你的正常 OpenClaw 状态：

bashCopy code
[code]
    npm pack extensions/codex --pack-destination /tmp OPENCLAW_STATE_DIR="$(mktemp -d)" \OPENCLAW_ALLOW_PLUGIN_INSTALL_OVERRIDES=1 \OPENCLAW_PLUGIN_INSTALL_OVERRIDES='{"codex":"npm-pack:/tmp/openclaw-codex-2026.5.8.tgz"}' \pnpm openclaw onboard --mode local
[/code]

验证状态目录下已安装的软件包：

bashCopy code
[code]
    find "$OPENCLAW_STATE_DIR/npm/node_modules" -maxdepth 3 -name package.json -printgrep -R '"@openclaw/codex"' "$OPENCLAW_STATE_DIR/npm/package-lock.json"
[/code]

对于实时提供商 E2E，在启动测试命令之前，从可信 shell 或 CI 密钥中加载真实 API key。不要打印密钥；只报告来源以及密钥是否存在。

Was this useful?YesNo