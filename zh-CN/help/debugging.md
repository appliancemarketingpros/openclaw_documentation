---
title: 调试
source_url: https://docs.openclaw.ai/zh-CN/help/debugging
scraped_at: 2026-05-25
---

用于调试流式输出的辅助工具，尤其适用于提供商将 reasoning 混入普通文本的情况。

## 运行时调试覆盖

在聊天中使用 `/debug` 设置**仅运行时** 配置覆盖（内存中，不写入磁盘）。 `/debug` 默认禁用；通过 `commands.debug: true` 启用。 当你需要切换较冷门的设置而不编辑 `openclaw.json` 时，这很方便。

示例：

CodeCopy code
[code]
    /debug show/debug set messages.responsePrefix="[openclaw]"/debug unset messages.responsePrefix/debug reset
[/code]

`/debug reset` 会清除所有覆盖，并恢复到磁盘上的配置。

## 会话 trace 输出

当你想在一个会话中查看插件拥有的 trace/debug 行， 但不启用完整 verbose 模式时，使用 `/trace`。

示例：

textCopy code
[code]
    /trace/trace on/trace off
[/code]

将 `/trace` 用于插件诊断，例如 Active Memory 调试摘要。 继续使用 `/verbose` 查看正常的 verbose 状态/工具输出，并继续使用 `/debug` 设置仅运行时配置覆盖。

## 插件生命周期 trace

当插件生命周期命令感觉很慢，并且你需要内置的阶段拆解来分析插件元数据、设备发现、注册表、 运行时镜像、配置变更和刷新工作时，使用 `OPENCLAW_PLUGIN_LIFECYCLE_TRACE=1`。 该 trace 需要显式启用并写入 stderr，因此 JSON 命令输出仍然可解析。

示例：

bashCopy code
[code]
    OPENCLAW_PLUGIN_LIFECYCLE_TRACE=1 openclaw plugins install tokenjuice --force
[/code]

示例输出：

textCopy code
[code]
    [plugins:lifecycle] phase="config read" ms=6.83 status=ok command="install"[plugins:lifecycle] phase="slot selection" ms=94.31 status=ok command="install" pluginId="tokenjuice"[plugins:lifecycle] phase="registry refresh" ms=51.56 status=ok command="install" reason="source-changed"
[/code]

在使用 CPU profiler 之前，先用它调查插件生命周期。 如果命令从源码 checkout 运行，优先在 `pnpm build` 后用 `node dist/entry.js ...` 测量已构建的运行时；`pnpm openclaw ...` 也会计入源码运行器开销。

## CLI 启动和命令性能分析

当某个命令感觉很慢时，使用仓库中提供的启动基准测试：

bashCopy code
[code]
    pnpm test:startup:bench:smokepnpm tsx scripts/bench-cli-startup.ts --preset real --case status --runs 3pnpm tsx scripts/bench-cli-startup.ts --preset real --cpu-prof-dir .artifacts/cli-cpu
[/code]

如果要通过正常源码运行器进行一次性性能分析，请设置 `OPENCLAW_RUN_NODE_CPU_PROF_DIR`：

bashCopy code
[code]
    OPENCLAW_RUN_NODE_CPU_PROF_DIR=.artifacts/cli-cpu pnpm openclaw status
[/code]

源码运行器会添加 Node CPU profile 标志，并为该命令写入一个 `.cpuprofile`。 在向命令代码添加临时插桩之前，先使用这种方式。

对于看起来像同步文件系统或模块加载器工作导致的启动卡顿， 通过源码运行器添加 Node 的同步 I/O trace 标志：

bashCopy code
[code]
    OPENCLAW_TRACE_SYNC_IO=1 pnpm openclaw gateway --force
[/code]

`pnpm gateway:watch` 默认会为被监视的 Gateway 网关子进程禁用此标志。 当你明确希望在 watch 模式下看到 Node 同步 I/O trace 输出时， 设置 `OPENCLAW_TRACE_SYNC_IO=1`。

## Gateway 网关 watch 模式

为了快速迭代，请在文件 watcher 下运行 gateway：

bashCopy code
[code]
    pnpm gateway:watch
[/code]

默认情况下，这会启动或重启名为 `openclaw-gateway-watch-main` 的 tmux 会话（或特定 profile/端口的变体，例如 `openclaw-gateway-watch-dev-19001`），并从交互式终端自动附加。 非交互式 shell、CI 和智能体 exec 调用会保持分离状态，并打印附加说明。 需要时手动附加：

bashCopy code
[code]
    tmux attach -t openclaw-gateway-watch-main
[/code]

tmux pane 会运行原始 watcher：

bashCopy code
[code]
    node scripts/watch-node.mjs gateway --force
[/code]

不需要 tmux 时使用前台模式：

bashCopy code
[code]
    pnpm gateway:watch:raw# orOPENCLAW_GATEWAY_WATCH_TMUX=0 pnpm gateway:watch
[/code]

保留 tmux 管理但禁用自动附加：

bashCopy code
[code]
    OPENCLAW_GATEWAY_WATCH_ATTACH=0 pnpm gateway:watch
[/code]

调试启动/运行时热点时，对被监视的 Gateway 网关 CPU 时间进行分析：

bashCopy code
[code]
    pnpm gateway:watch --benchmark
[/code]

watch 包装器会在调用 Gateway 网关前消费 `--benchmark`，并在 `.artifacts/gateway-watch-profiles/` 下为每次 Gateway 网关子进程退出写入一个 V8 `.cpuprofile`。停止或重启被监视的 gateway 以刷新当前 profile， 然后用 Chrome DevTools 或 Speedscope 打开：

bashCopy code
[code]
    npx speedscope .artifacts/gateway-watch-profiles/*.cpuprofile
[/code]

当你希望将 profile 写到其他位置时，使用 `--benchmark-dir <path>`。 当你希望被基准测试的子进程跳过默认的 `--force` 端口清理，并在 Gateway 网关端口已被占用时快速失败，使用 `--benchmark-no-force`。 基准模式默认会抑制同步 I/O trace 噪声。当你明确希望同时获得 CPU profile 和 Node 同步 I/O stack trace 时，配合 `--benchmark` 设置 `OPENCLAW_TRACE_SYNC_IO=1`。在基准模式下，这些 trace 块会写入基准目录下的 `gateway-watch-output.log`，并从终端 pane 中过滤；正常的 Gateway 网关日志仍然可见。

tmux 包装器会将常见的非秘密运行时选择器带入 pane，例如 `OPENCLAW_PROFILE`、`OPENCLAW_CONFIG_PATH`、`OPENCLAW_STATE_DIR`、 `OPENCLAW_GATEWAY_PORT` 和 `OPENCLAW_SKIP_CHANNELS`。将 提供商凭据放在你的正常 profile/config 中，或使用原始前台模式处理一次性临时秘密。 如果被监视的 Gateway 网关在启动期间退出，watcher 会运行一次 `openclaw doctor --fix --non-interactive`，然后重启 Gateway 网关子进程。 当你希望看到原始启动失败而不执行仅开发用修复流程时，使用 `OPENCLAW_GATEWAY_WATCH_AUTO_DOCTOR=0`。 托管的 tmux pane 也默认使用彩色 Gateway 网关日志以提高可读性； 启动 `pnpm gateway:watch` 时设置 `FORCE_COLOR=0` 可禁用 ANSI 输出。

watcher 会在 `src/` 下与构建相关的文件、插件源码文件、插件 `package.json` 和 `openclaw.plugin.json` 元数据、`tsconfig.json`、`package.json` 以及 `tsdown.config.ts` 发生变化时重启。插件元数据变化会在不强制执行 `tsdown` 重建的情况下重启 gateway；源码和配置变化仍会先重建 `dist`。

在 `gateway:watch` 后添加任何 gateway CLI 标志，它们都会在每次重启时透传。 重新运行同一个 watch 命令会重新生成具名 tmux pane，并且原始 watcher 仍会保持其 single-watcher 锁，因此重复的 watcher 父进程会被替换，而不是不断堆积。

## 开发 profile + 开发 gateway（--dev）

使用开发 profile 隔离状态，并启动一个安全、可丢弃的设置用于调试。 这里有**两个** `--dev` 标志：

  * **全局`--dev`（profile）：** 将状态隔离在 `~/.openclaw-dev` 下，并 将 gateway 端口默认设为 `19001`（派生端口会随之偏移）。
  * **`gateway --dev`：告诉 Gateway 网关在缺失时自动创建默认配置 + 工作区**（并跳过 [BOOTSTRAP.md](<http://BOOTSTRAP.md>)）。


推荐流程（开发 profile + 开发 bootstrap）：

bashCopy code
[code]
    pnpm gateway:devOPENCLAW_PROFILE=dev openclaw tui
[/code]

如果你还没有全局安装，请通过 `pnpm openclaw ...` 运行 CLI。

它会执行以下操作：

  1. **Profile 隔离** （全局 `--dev`）

     * `OPENCLAW_PROFILE=dev`
     * `OPENCLAW_STATE_DIR=~/.openclaw-dev`
     * `OPENCLAW_CONFIG_PATH=~/.openclaw-dev/openclaw.json`
     * `OPENCLAW_GATEWAY_PORT=19001`（browser/canvas 会相应偏移）
  2. **开发 bootstrap** （`gateway --dev`）

     * 缺失时写入最小配置（`gateway.mode=local`，绑定 loopback）。
     * 将 `agent.workspace` 设置为开发工作区。
     * 设置 `agent.skipBootstrap=true`（无 [BOOTSTRAP.md](<http://BOOTSTRAP.md>)）。
     * 如果缺失，则初始化工作区文件： `AGENTS.md`、`SOUL.md`、`TOOLS.md`、`IDENTITY.md`、`USER.md`、`HEARTBEAT.md`。
     * 默认身份：**C3-PO** （协议机器人）。
     * 在开发模式下跳过渠道提供商（`OPENCLAW_SKIP_CHANNELS=1`）。


重置流程（全新开始）：

bashCopy code
[code]
    pnpm gateway:dev:reset
[/code]

`--reset` 会清除配置、凭据、会话和开发工作区（使用 `trash`，不是 `rm`），然后重新创建默认开发设置。

## 原始流日志（OpenClaw）

OpenClaw 可以在任何过滤/格式化之前记录**原始 assistant 流** 。 这是查看 reasoning 是作为普通文本 delta 到达 （还是作为单独的 thinking 块到达）的最佳方式。

通过 CLI 启用：

bashCopy code
[code]
    pnpm gateway:watch --raw-stream
[/code]

可选路径覆盖：

bashCopy code
[code]
    pnpm gateway:watch --raw-stream --raw-stream-path ~/.openclaw/logs/raw-stream.jsonl
[/code]

等效环境变量：

bashCopy code
[code]
    OPENCLAW_RAW_STREAM=1OPENCLAW_RAW_STREAM_PATH=~/.openclaw/logs/raw-stream.jsonl
[/code]

默认文件：

`~/.openclaw/logs/raw-stream.jsonl`

## 原始 chunk 日志（pi-mono）

为了在它们被解析为块之前捕获**原始 OpenAI 兼容 chunk** ， pi-mono 暴露了一个单独的 logger：

bashCopy code
[code]
    PI_RAW_STREAM=1
[/code]

可选路径：

bashCopy code
[code]
    PI_RAW_STREAM_PATH=~/.pi-mono/logs/raw-openai-completions.jsonl
[/code]

默认文件：

`~/.pi-mono/logs/raw-openai-completions.jsonl`

> 注意：这只会由使用 pi-mono 的 `openai-completions` 提供商的进程发出。

## 安全注意事项

  * 原始流日志可能包含完整 prompt、工具输出和用户数据。
  * 将日志保留在本地，并在调试后删除。
  * 如果你共享日志，请先清除秘密和 PII。


## 在 VSCode 中调试

基于 VSCode 的 IDE 需要 source maps 才能启用调试，因为许多生成文件会在构建过程中带有哈希名称。随附的 `launch.json` 配置面向 Gateway 网关服务，但可以快速调整用于其他目的：

  1. **重建并调试 Gateway 网关** \- 创建新构建后调试 Gateway 网关服务
  2. **调试 Gateway 网关** \- 调试已有构建中的 Gateway 网关服务


### 设置

默认的 **重建并调试 Gateway 网关** 配置开箱即用，它会自动删除 `/dist` 文件夹，并在启用调试的情况下重建项目：

  1. 从 Activity Bar 打开 **Run and Debug** 面板，或按 `Ctrl`+`Shift`+`D`
  2. 在 IDE 中，确保配置下拉菜单中选择了 **重建并调试 Gateway 网关** ，然后按下 **Start Debugging** 按钮


或者，如果你更喜欢手动管理构建和调试流程：

  1. 打开终端并启用 source maps： 
     * **Linux/macOS** ：`export OUTPUT_SOURCE_MAPS=1`
     * **Windows (PowerShell)** ：`$env:OUTPUT_SOURCE_MAPS="1"`
     * **Windows (CMD)** ：`set OUTPUT_SOURCE_MAPS=1`
  2. 在同一终端中重建项目：`pnpm clean:dist && pnpm build`
  3. 在 IDE 中，在 **Run and Debug** 配置下拉菜单中选择 **调试 Gateway 网关** 选项，然后按下 **Start Debugging** 按钮


现在你可以在 TypeScript 源文件（`src/` 目录）中设置断点，调试器会通过 source maps 将断点正确映射到已编译的 JavaScript。你将能够按预期检查变量、单步执行代码并查看调用栈。

### 说明

  * 如果使用 **"重建并调试 Gateway 网关"** 选项，每次启动调试器时，它都会完全删除 `/dist` 文件夹，并在启动 Gateway 网关前运行一次启用 source maps 的完整 `pnpm build`
  * 如果使用 **"调试 Gateway 网关"** 选项，调试会话可以随时启动和停止，而不会影响 `/dist` 文件夹，但你必须使用单独的终端进程来同时启用调试并管理构建周期
  * 修改 `launch.json` 中的 `args` 设置，以调试项目的其他部分
  * 如果你需要将已构建的 OpenClaw CLI 用于其他任务（例如当你的调试会话生成新的 auth token 时使用 `dashboard --no-open`），可以在另一个终端中以 `node ./openclaw.mjs` 执行它，或创建类似 `alias openclaw-build="node $(pwd)/openclaw.mjs"` 的 shell alias


## 相关

  * [故障排除](</zh-CN/help/troubleshooting>)
  * [常见问题](</zh-CN/help/faq>)


Was this useful?YesNo