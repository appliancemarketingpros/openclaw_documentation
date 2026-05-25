---
title: Mantis Slack 桌面端运行手册
source_url: https://docs.openclaw.ai/zh-CN/concepts/mantis-slack-desktop-runbook
scraped_at: 2026-05-25
---

Mantis Slack 桌面 QA 是 Slack 类缺陷的真实 UI 流程，适用于需要 Linux 桌面、VNC 救援、Slack Web、真实 OpenClaw Gateway 网关、截图、 视频和 PR 证据评论的场景。

当单元测试或无头 Slack 实时流程无法证明该缺陷时使用它。

## 存储模型

Mantis 使用三种不同的存储层：

  * 提供商镜像：由 Crabbox 拥有，并存储在云提供商账户中。 它包含机器能力，例如 Chrome/Chromium、ffmpeg、scrot、 Node/corepack/pnpm、原生构建工具，以及空缓存目录。
  * 热租约状态：由当前操作员会话拥有。它可以包含已登录的 浏览器配置文件、`/var/cache/crabbox/pnpm`，以及在租约存活期间准备好的源码 checkout。
  * Mantis 工件：由 OpenClaw 运行拥有。它们位于 `.artifacts/qa-e2e/mantis/...` 下，随后 GitHub Actions 会上传它们，并且 Mantis GitHub App 会在 PR 上评论内联证据。


切勿把密钥、浏览器 cookie、Slack 登录状态、仓库 checkout、 `node_modules` 或 `dist/` 放入预烘焙的提供商镜像中。

## GitHub 调度

从 `main` 运行 workflow：

bashCopy code
[code]
    gh workflow run mantis-slack-desktop-smoke.yml \  --ref main \  -f candidate_ref=<trusted-ref-or-sha> \  -f pr_number=<pr-number> \  -f scenario_id=slack-canary \  -f crabbox_provider=aws \  -f keep_vm=false \  -f hydrate_mode=source
[/code]

允许的 `candidate_ref` 值被有意限制得很窄，因为该 workflow 会使用实时凭证：当前 `main` 祖先、发布标签，或来自 `openclaw/openclaw` 的打开 PR head。

该 workflow 会写入：

  * 上传的工件：`mantis-slack-desktop-smoke-<run-id>-<attempt>`；
  * 来自 Mantis GitHub App 的内联 PR 评论；
  * `slack-desktop-smoke.png`；
  * `slack-desktop-smoke.mp4`；
  * `slack-desktop-smoke-preview.gif`；
  * `slack-desktop-smoke-change.mp4`；
  * `mantis-slack-desktop-smoke-summary.json`；
  * `mantis-slack-desktop-smoke-report.md`；
  * 远程日志，例如 `slack-desktop-command.log`、`openclaw-gateway.log`、 `chrome.log` 和 `ffmpeg.log`。


PR 评论会通过隐藏的 `<!-- mantis-slack-desktop-smoke -->` 标记原地更新。

## 本地 CLI

冷源码证明：

bashCopy code
[code]
    pnpm openclaw qa mantis slack-desktop-smoke \  --provider aws \  --class standard \  --gateway-setup \  --credential-source convex \  --credential-role maintainer \  --provider-mode live-frontier \  --model openai/gpt-5.4 \  --alt-model openai/gpt-5.4 \  --scenario slack-canary \  --hydrate-mode source
[/code]

保留 VM 以便 VNC 救援：

bashCopy code
[code]
    pnpm openclaw qa mantis slack-desktop-smoke \  --provider aws \  --class standard \  --gateway-setup \  --scenario slack-canary \  --keep-lease
[/code]

打开 VNC：

bashCopy code
[code]
    crabbox vnc --provider aws --id <cbx_id> --open
[/code]

复用热租约：

bashCopy code
[code]
    pnpm openclaw qa mantis slack-desktop-smoke \  --provider aws \  --lease-id <cbx_id-or-slug> \  --gateway-setup \  --scenario slack-canary \  --hydrate-mode source
[/code]

仅当复用的远程工作区已经有 `node_modules` 和已构建的 `dist/` 时，才使用 `--hydrate-mode prehydrated`。如果缺少这些内容，Mantis 会失败关闭。

## Hydrate 模式

模式 | 使用时机 | 远程行为 | 权衡  
---|---|---|---  
`source` | 正常 PR 证明、冷机器、CI | 在 VM 内运行 `pnpm install --frozen-lockfile --prefer-offline` 和 `pnpm build` | 最慢，但源码 checkout 证明最强  
`prehydrated` | 你有意准备了一个复用租约 | 要求已有 `node_modules` 和 `dist/`；跳过安装/构建 | 很快，但只对操作员控制的热租约有效  
  
GitHub Actions 始终会在 VM 运行前准备候选 checkout。其 pnpm store 会按 OS、Node 版本和 lockfile 缓存。VM 源码运行在存在时也会 使用 `/var/cache/crabbox/pnpm`。

## 时序解读

`mantis-slack-desktop-smoke-report.md` 包含阶段耗时：

  * `crabbox.warmup`：云提供商启动、桌面/浏览器就绪，以及 SSH。
  * `crabbox.inspect`：租约元数据查询。
  * `credentials.prepare`：获取 Convex 凭证租约。
  * `crabbox.remote_run`：同步、浏览器启动、OpenClaw 安装/构建或 hydrate 校验、Gateway 网关启动、截图和视频捕获。
  * `artifacts.copy`：从 VM 通过 rsync 复制回来。


当 Crabbox 返回非零远程状态，但 Mantis 已复制元数据证明 OpenClaw Gateway 网关 存活且设置已完成时，`crabbox.remote_run` 可以标记为 `accepted`。 将 `accepted` 视为带解释的通过，而不是失败场景。

如果运行很慢：

  * warmup 占主导：预烘焙或升级到更好的 Crabbox 提供商镜像；
  * `source` 中 remote_run 占主导：使用热租约、改进 pnpm store 复用， 或把机器前置条件移入提供商镜像；
  * `prehydrated` 中 remote_run 占主导：远程工作区实际上未就绪， 或 Gateway 网关/浏览器/Slack 设置很慢；
  * artifact copy 占主导：检查视频大小和工件目录内容。


## 证据清单

好的 PR 评论应显示：

  * 场景 ID 和候选 SHA；
  * GitHub Actions 运行 URL；
  * 工件 URL；
  * 内联截图；
  * 可用时的内联动画预览；
  * 完整 MP4 和裁剪后 MP4 链接；
  * 通过/失败状态；
  * 附加报告中的耗时摘要。


不要把截图或视频提交到仓库。将它们保存在 GitHub Actions 工件或 PR 评论中。

## 失败处理

如果 workflow 在 VM 运行前失败，先检查 Actions job。典型原因包括 不受信任的 `candidate_ref`、缺少环境密钥，或候选安装/构建失败。

如果 VM 运行失败但截图已复制回来，请检查：

bashCopy code
[code]
    cat mantis-slack-desktop-smoke-report.mdcat mantis-slack-desktop-smoke-summary.jsoncat slack-desktop-command.logcat openclaw-gateway.logcat chrome.logcat ffmpeg.log
[/code]

如果运行保留了租约，请使用报告中的 `crabbox vnc ...` 命令打开 VNC。 完成后停止租约：

bashCopy code
[code]
    crabbox stop --provider aws <cbx_id-or-slug>
[/code]

如果 Slack 登录已过期，请在保留租约上的 VNC 中修复它，并使用 `--lease-id` 重新运行。不要把该浏览器配置文件烘焙进提供商镜像。

## 相关

  * [QA overview](</zh-CN/concepts/qa-e2e-automation>)
  * [Slack 渠道](</zh-CN/channels/slack>)
  * [测试](</zh-CN/help/testing>)


Was this useful?YesNo