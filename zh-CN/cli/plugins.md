---
title: 插件
source_url: https://docs.openclaw.ai/zh-CN/cli/plugins
scraped_at: 2026-05-25
---

管理 Gateway 网关插件、钩子包和兼容包。

[**插件系统** 面向最终用户的插件安装、启用和故障排除指南。 ](</zh-CN/tools/plugin>) [**管理插件** 安装、列出、更新、卸载和发布的快速示例。 ](</zh-CN/plugins/manage-plugins>) [**插件包** 包兼容性模型。 ](</zh-CN/plugins/bundles>) [**插件清单** 清单字段和配置架构。 ](</zh-CN/plugins/manifest>) [**安全性** 插件安装的安全加固。 ](</zh-CN/gateway/security>)

## 命令

bashCopy code
[code]
    openclaw plugins listopenclaw plugins list --enabledopenclaw plugins list --verboseopenclaw plugins list --jsonopenclaw plugins search <query>openclaw plugins search <query> --limit 20openclaw plugins search <query> --jsonopenclaw plugins install <path-or-spec>openclaw plugins inspect <id>openclaw plugins inspect <id> --runtimeopenclaw plugins inspect <id> --jsonopenclaw plugins inspect --allopenclaw plugins info <id>openclaw plugins enable <id>openclaw plugins disable <id>openclaw plugins registryopenclaw plugins registry --refreshopenclaw plugins uninstall <id>openclaw plugins doctoropenclaw plugins update <id-or-npm-spec>openclaw plugins update --allopenclaw plugins marketplace list <marketplace>openclaw plugins marketplace list <marketplace> --json
[/code]

若要调查缓慢的安装、检查、卸载或注册表刷新，请在运行命令时设置 `OPENCLAW_PLUGIN_LIFECYCLE_TRACE=1`。跟踪会将阶段耗时写入 stderr，并保持 JSON 输出可解析。参见[调试](</zh-CN/help/debugging#plugin-lifecycle-trace>)。

### 安装

bashCopy code
[code]
    openclaw plugins search "calendar"                   # search ClawHub pluginsopenclaw plugins install <package>                      # npm by defaultopenclaw plugins install clawhub:<package>              # ClawHub onlyopenclaw plugins install npm:<package>                  # npm onlyopenclaw plugins install npm-pack:<path.tgz>            # local npm pack through npm install semanticsopenclaw plugins install git:github.com/<owner>/<repo>  # git repoopenclaw plugins install git:github.com/<owner>/<repo>@<ref>openclaw plugins install <package> --force              # overwrite existing installopenclaw plugins install <package> --pin                # pin versionopenclaw plugins install <package> --dangerously-force-unsafe-installopenclaw plugins install <path>                         # local pathopenclaw plugins install <plugin>@<marketplace>         # marketplaceopenclaw plugins install <plugin> --marketplace <name>  # marketplace (explicit)openclaw plugins install <plugin> --marketplace https://github.com/<owner>/<repo>
[/code]

测试设置期安装的维护者可以使用受保护的环境变量覆盖自动插件安装来源。参见[插件安装覆盖](</zh-CN/plugins/install-overrides>)。

`plugins search` 会查询 ClawHub 中可安装的插件包，并输出可直接安装的包名。它搜索代码插件和包插件包，而不是 Skills。ClawHub Skills 请使用 `openclaw skills search`。

配置 include 和无效配置修复

如果你的 `plugins` 部分由单文件 `$include` 支撑，`plugins install/update/enable/disable/uninstall` 会写入该被包含的文件，并保持 `openclaw.json` 不变。根 include、include 数组以及带有同级覆盖的 include 会封闭失败，而不是扁平化。有关受支持的形态，请参见[配置 include](</zh-CN/gateway/configuration>)。

如果安装期间配置无效，`plugins install` 通常会封闭失败，并提示你先运行 `openclaw doctor --fix`。在 Gateway 网关启动和热重载期间，无效插件配置会像任何其他无效配置一样封闭失败；`openclaw doctor --fix` 可以隔离该无效插件条目。唯一有文档说明的安装时例外，是针对显式选择加入 `openclaw.install.allowInvalidConfigRecovery` 的插件的窄范围内置插件恢复路径。

\--force 和重新安装与更新

`--force` 会复用现有安装目标，并就地覆盖已安装的插件或钩子包。当你有意从新的本地路径、归档、ClawHub 包或 npm 构件重新安装相同 id 时使用它。对于已跟踪的 npm 插件的常规升级，优先使用 `openclaw plugins update <id-or-npm-spec>`。

如果你对已安装插件 id 运行 `plugins install`，OpenClaw 会停止，并将你指向 `plugins update <id-or-npm-spec>` 进行正常升级；如果你确实想从其他来源覆盖当前安装，则指向 `plugins install <package> --force`。

\--pin 范围

`--pin` 仅适用于 npm 安装。它不支持 `git:` 安装；如果你想要固定来源，请使用显式 git ref，例如 `git:github.com/acme/plugin@v1.2.3`。它不支持 `--marketplace`，因为 marketplace 安装会持久化 marketplace 来源元数据，而不是 npm spec。

\--dangerously-force-unsafe-install

`--dangerously-force-unsafe-install` 是用于内置危险代码扫描器误报的应急选项。即使内置扫描器报告 `critical` 发现，它也允许继续安装，但它**不会** 绕过插件 `before_install` 钩子策略阻断，也**不会** 绕过扫描失败。

此 CLI 标志适用于插件安装/更新流程。由 Gateway 网关支撑的 skill 依赖安装使用对应的 `dangerouslyForceUnsafeInstall` 请求覆盖，而 `openclaw skills install` 仍是单独的 ClawHub skill 下载/安装流程。

如果你发布到 ClawHub 的插件被注册表扫描阻断，请使用 [ClawHub](</zh-CN/clawhub/security>) 中的发布者步骤。

钩子包和 npm spec

`plugins install` 也是安装在 `package.json` 中暴露 `openclaw.hooks` 的钩子包的入口。请使用 `openclaw hooks` 查看筛选后的钩子可见性并启用单个钩子，而不是安装包。

Npm spec **仅限注册表** （包名 + 可选的**精确版本** 或 **dist-tag** ）。Git/URL/file spec 和 semver 范围会被拒绝。为安全起见，依赖安装会使用 `--ignore-scripts` 在项目本地运行，即使你的 shell 配置了全局 npm 安装设置。托管插件 npm 根会继承 OpenClaw 包级别的 npm `overrides`，因此主机安全固定也会应用到提升的插件依赖。

当你想明确使用 npm 解析时，请使用 `npm:<package>`。裸包 spec 在启动切换期间也会直接从 npm 安装。

裸 spec 和 `@latest` 会留在稳定轨道。OpenClaw 带日期戳的修正版版本（例如 `2026.5.3-1`）在此检查中属于稳定发布。如果 npm 将其中任一解析为预发布版本，OpenClaw 会停止，并要求你使用预发布标签（例如 `@beta`/`@rc`）或精确预发布版本（例如 `@1.2.3-beta.4`）显式选择加入。

如果裸安装 spec 匹配官方插件 id（例如 `diffs`），OpenClaw 会直接安装目录条目。若要安装同名 npm 包，请使用显式带作用域 spec（例如 `@scope/diffs`）。

Git 仓库

使用 `git:<repo>` 可直接从 git 仓库安装。支持的形式包括 `git:github.com/owner/repo`、`git:owner/repo`、完整 `https://`、`ssh://`、`git://`、`file://` 以及 `git@host:owner/repo.git` 克隆 URL。添加 `@<ref>` 或 `#<ref>` 可在安装前检出分支、标签或提交。

Git 安装会克隆到临时目录，在存在所请求的 ref 时检出它，然后使用普通插件目录安装器。这意味着清单验证、危险代码扫描、包管理器安装工作和安装记录的行为都与 npm 安装相同。记录的 git 安装会包含源 URL/ref 以及解析后的提交，以便 `openclaw plugins update` 后续可以重新解析该来源。

从 git 安装后，请使用 `openclaw plugins inspect <id> --runtime --json` 验证运行时注册，例如 gateway 方法和 CLI 命令。如果插件通过 `api.registerCli` 注册了 CLI 根，请直接通过 OpenClaw 根 CLI 执行该命令，例如 `openclaw demo-plugin ping`。

归档

支持的归档：`.zip`、`.tgz`、`.tar.gz`、`.tar`。原生 OpenClaw 插件归档必须在解压后的插件根目录包含有效的 `openclaw.plugin.json`；只包含 `package.json` 的归档会在 OpenClaw 写入安装记录前被拒绝。

当文件是 npm-pack tarball，且你想测试与注册表安装相同的托管 npm 根安装路径时，请使用 `npm-pack:<path.tgz>`，包括 `package-lock.json` 验证、提升依赖扫描和 npm 安装记录。普通归档路径仍会作为本地归档安装在插件 extensions 根下。

也支持 Claude marketplace 安装。

ClawHub 安装使用显式 `clawhub:<package>` 定位符：

bashCopy code
[code]
    openclaw plugins install clawhub:openclaw-codex-app-serveropenclaw plugins install clawhub:openclaw-codex-app-server@1.2.3
[/code]

裸 npm 安全插件 spec 在启动切换期间默认从 npm 安装：

bashCopy code
[code]
    openclaw plugins install openclaw-codex-app-server
[/code]

使用 `npm:` 可明确仅使用 npm 解析：

bashCopy code
[code]
    openclaw plugins install npm:openclaw-codex-app-serveropenclaw plugins install npm:@scope/plugin-name@1.0.1
[/code]

OpenClaw 会在安装前检查声明的插件 API / 最低 Gateway 网关兼容性。当选定的 ClawHub 版本发布 ClawPack 构件时，OpenClaw 会下载带版本的 npm-pack `.tgz`，验证 ClawHub 摘要标头和构件摘要，然后通过常规归档路径安装。没有 ClawPack 元数据的较旧 ClawHub 版本仍会通过旧版包归档验证路径安装。记录的安装会保留其 ClawHub 来源元数据、构件类型、npm integrity、npm shasum、tarball 名称以及 ClawPack 摘要信息，以供后续更新使用。 未指定版本的 ClawHub 安装会保留未指定版本的记录规范，因此 `openclaw plugins update` 可以跟随更新的 ClawHub 版本；显式版本或标签选择器（例如 `clawhub:pkg@1.2.3` 和 `clawhub:pkg@beta`）会继续固定到该选择器。

#### 市场简写

当 Claude 的本地注册表缓存在 `~/.claude/plugins/known_marketplaces.json` 中存在该市场名称时，使用 `plugin@marketplace` 简写：

bashCopy code
[code]
    openclaw plugins marketplace list <marketplace-name>openclaw plugins install <plugin-name>@<marketplace-name>
[/code]

当你想显式传入市场来源时，使用 `--marketplace`：

bashCopy code
[code]
    openclaw plugins install <plugin-name> --marketplace <marketplace-name>openclaw plugins install <plugin-name> --marketplace <owner/repo>openclaw plugins install <plugin-name> --marketplace https://github.com/<owner>/<repo>openclaw plugins install <plugin-name> --marketplace ./my-marketplace
[/code]

### 市场来源

  * 来自 `~/.claude/plugins/known_marketplaces.json` 的 Claude 已知市场名称
  * 本地市场根目录或 `marketplace.json` 路径
  * GitHub 仓库简写，例如 `owner/repo`
  * GitHub 仓库 URL，例如 `https://github.com/owner/repo`
  * git URL


### 远程市场规则

对于从 GitHub 或 git 加载的远程市场，插件条目必须留在克隆的市场仓库内。OpenClaw 接受来自该仓库的相对路径来源，并拒绝远程清单中的 HTTP(S)、绝对路径、git、GitHub 以及其他非路径插件来源。

对于本地路径和归档，OpenClaw 会自动检测：

  * 原生 OpenClaw 插件（`openclaw.plugin.json`）
  * Codex 兼容包（`.codex-plugin/plugin.json`）
  * Claude 兼容包（`.claude-plugin/plugin.json` 或默认 Claude 组件布局）
  * Cursor 兼容包（`.cursor-plugin/plugin.json`）


### 列出

bashCopy code
[code]
    openclaw plugins listopenclaw plugins list --enabledopenclaw plugins list --verboseopenclaw plugins list --jsonopenclaw plugins search <query>openclaw plugins search <query> --limit 20openclaw plugins search <query> --json
[/code]

仅显示已启用的插件。

从表格视图切换到每个插件的详细行，其中包含来源/源点/版本/激活元数据。

机器可读的清单，加上注册表诊断和包依赖安装状态。

`plugins search` 是远程 ClawHub 目录查询。它不会检查本地 状态、变更配置、安装包，或加载插件运行时代码。搜索 结果包含 ClawHub 包名称、族、渠道、版本、摘要，以及 类似 `openclaw plugins install clawhub:<package>` 的安装提示。

对于打包 Docker 镜像内的内置插件工作，请将插件 源目录 bind-mount 到匹配的打包源路径之上，例如 `/app/extensions/synology-chat`。OpenClaw 会先发现该挂载的源 覆盖层，然后才是 `/app/dist/extensions/synology-chat`；普通复制的源 目录保持不生效，因此常规打包安装仍会使用编译后的 dist。

对于运行时钩子调试：

  * `openclaw plugins inspect <id> --runtime --json` 会显示模块加载检查过程中注册的钩子和诊断。运行时检查永远不会安装依赖；使用 `openclaw doctor --fix` 清理旧版依赖状态，或恢复配置引用的缺失可下载插件。
  * `openclaw gateway status --deep --require-rpc` 会确认可访问的 Gateway 网关、服务/进程提示、配置路径以及 RPC 健康状态。
  * 非内置对话钩子（`llm_input`、`llm_output`、`before_model_resolve`、`before_agent_reply`、`before_agent_run`、`before_agent_finalize`、`agent_end`）需要 `plugins.entries.<id>.hooks.allowConversationAccess=true`。


使用 `--link` 可避免复制本地目录（会添加到 `plugins.load.paths`）：

bashCopy code
[code]
    openclaw plugins install -l ./my-plugin
[/code]

### 插件索引

插件安装元数据是机器管理的状态，不是用户配置。安装和更新会把它写入活动 OpenClaw 状态目录下的 `plugins/installs.json`。其顶层 `installRecords` 映射是安装元数据的持久来源，包括损坏或缺失插件清单的记录。`plugins` 数组是由清单派生的冷注册表缓存。该文件包含不要编辑警告，并由 `openclaw plugins update`、卸载、诊断以及冷插件注册表使用。

当 OpenClaw 在配置中看到已发布的旧版 `plugins.installs` 记录时，运行时读取会将它们作为兼容性输入处理，而不会重写 `openclaw.json`。显式插件写入和 `openclaw doctor --fix` 会在允许写入配置时把这些记录移动到插件索引，并移除配置键；如果任一写入失败，配置记录会被保留，因此安装元数据不会丢失。

### 卸载

bashCopy code
[code]
    openclaw plugins uninstall <id>openclaw plugins uninstall <id> --dry-runopenclaw plugins uninstall <id> --keep-files
[/code]

`uninstall` 会从 `plugins.entries`、持久化插件索引、插件允许/拒绝列表条目，以及适用时的链接 `plugins.load.paths` 条目中移除插件记录。除非设置了 `--keep-files`，卸载还会在被跟踪的托管安装目录位于 OpenClaw 插件扩展根目录内时移除该目录。对于主动记忆插件，记忆槽位会重置为 `memory-core`。

### 更新

bashCopy code
[code]
    openclaw plugins update <id-or-npm-spec>openclaw plugins update --allopenclaw plugins update <id-or-npm-spec> --dry-runopenclaw plugins update @openclaw/voice-callopenclaw plugins update openclaw-codex-app-server --dangerously-force-unsafe-install
[/code]

更新适用于托管插件索引中跟踪的插件安装，以及 `hooks.internal.installs` 中跟踪的 hook-pack 安装。

解析插件 id 与 npm 规范

当你传入插件 id 时，OpenClaw 会复用该插件记录的安装规范。这意味着之前存储的 dist-tag（例如 `@beta`）和精确固定版本会在后续 `update <id>` 运行中继续使用。

对于 npm 安装，你也可以传入带 dist-tag 或精确版本的显式 npm 包规范。OpenClaw 会将该包名称解析回被跟踪的插件记录，更新该已安装插件，并记录新的 npm 规范以供后续基于 id 的更新使用。

传入不带版本或标签的 npm 包名称也会解析回被跟踪的插件记录。当插件已固定到精确版本，而你想把它移回注册表的默认发布线时，请使用这种方式。

Beta 渠道更新

`openclaw plugins update` 会复用被跟踪的插件规范，除非你传入新规范。`openclaw update` 还知道活动的 OpenClaw 更新渠道：在 beta 渠道上，默认线 npm 和 ClawHub 插件记录会先尝试 `@beta`，如果不存在插件 beta 版本，则回退到记录的默认/latest 规范。该回退会以警告形式报告，并且不会导致核心更新失败。精确版本和显式标签会保持固定到该选择器。

版本检查和完整性漂移

在实时 npm 更新之前，OpenClaw 会根据 npm 注册表元数据检查已安装包版本。如果已安装版本和记录的构件身份已经与解析后的目标匹配，则会跳过更新，不下载、不重新安装，也不重写 `openclaw.json`。

当存在已存储的完整性哈希且获取到的构件哈希发生变化时，OpenClaw 会将其视为 npm 构件漂移。交互式 `openclaw plugins update` 命令会打印预期和实际哈希，并在继续之前请求确认。非交互式更新辅助工具会默认失败关闭，除非调用方提供显式继续策略。

更新时的 --dangerously-force-unsafe-install

`--dangerously-force-unsafe-install` 也可用于 `plugins update`，作为插件更新期间内置危险代码扫描误报的紧急覆盖。它仍不会绕过插件 `before_install` 策略阻断或扫描失败阻断，并且只适用于插件更新，不适用于 hook-pack 更新。

### 检查

bashCopy code
[code]
    openclaw plugins inspect <id>openclaw plugins inspect <id> --runtimeopenclaw plugins inspect <id> --json
[/code]

Inspect 默认不导入插件运行时，会显示身份、加载状态、来源、清单能力、策略标志、诊断、安装元数据、包能力，以及任何检测到的 MCP 或 LSP 服务器支持。添加 `--runtime` 可加载插件模块，并包含已注册的钩子、工具、命令、服务、Gateway 网关方法以及 HTTP 路由。运行时检查会直接报告缺失的插件依赖；安装和修复保留在 `openclaw plugins install`、`openclaw plugins update` 和 `openclaw doctor --fix` 中。

插件拥有的 CLI 命令通常作为根 `openclaw` 命令组安装，但插件也可以在核心父级下注册嵌套命令，例如 `openclaw nodes`。在 `inspect --runtime` 的 `cliCommands` 下显示某个命令后，请按列出的路径运行它；例如，注册 `demo-git` 的插件可用 `openclaw demo-git ping` 验证。

每个插件会按其在运行时实际注册的内容分类：

  * **plain-capability** — 一种能力类型（例如仅提供商插件）
  * **hybrid-capability** — 多种能力类型（例如文本 + 语音 + 图像）
  * **hook-only** — 仅钩子，没有能力或界面
  * **non-capability** — 工具/命令/服务，但没有能力


参阅 [插件形态](</zh-CN/plugins/architecture#plugin-shapes>)，了解有关能力模型的更多内容。

### Doctor

bashCopy code
[code]
    openclaw plugins doctor
[/code]

`doctor` 会报告插件加载错误、清单/设备发现诊断以及兼容性提示。当一切正常时，它会打印 `No plugin issues detected.`

如果已配置的插件存在于磁盘上，但被加载器的路径安全检查阻止，配置验证会保留该插件条目，并将其报告为 `present but blocked`。请修复前面的被阻止插件诊断，例如路径所有权或全局可写权限，而不是移除 `plugins.entries.<id>` 或 `plugins.allow` 配置。

对于缺少 `register`/`activate` 导出等模块形态失败，请使用 `OPENCLAW_PLUGIN_LOAD_DEBUG=1` 重新运行，以便在诊断输出中包含紧凑的导出形态摘要。

### 注册表

bashCopy code
[code]
    openclaw plugins registryopenclaw plugins registry --refreshopenclaw plugins registry --json
[/code]

本地插件注册表是 OpenClaw 持久化的冷读模型，用于已安装插件身份、启用状态、来源元数据和贡献归属。正常启动、提供商所有者查找、渠道设置分类和插件清单都可以读取它，而无需导入插件运行时模块。

使用 `plugins registry` 检查持久化注册表是否存在、是否为当前版本或是否已过期。使用 `--refresh` 可基于持久化插件索引、配置策略以及清单/包元数据重建它。这是修复路径，不是运行时激活路径。

`openclaw doctor --fix` 也会修复与注册表相邻的受管 npm 漂移：如果受管插件 npm 根目录下孤立或恢复的 `@openclaw/*` 包遮蔽了内置插件，Doctor 会移除该过期包并重建注册表，使启动流程根据内置清单进行验证。Doctor 还会将宿主 `openclaw` 包重新链接到声明了 `peerDependencies.openclaw` 的受管 npm 插件中，使 `openclaw/plugin-sdk/*` 等包本地运行时导入在更新或 npm 修复后能够解析。

### 市场

bashCopy code
[code]
    openclaw plugins marketplace list <source>openclaw plugins marketplace list <source> --json
[/code]

市场列表接受本地市场路径、`marketplace.json` 路径、类似 `owner/repo` 的 GitHub 简写、GitHub 仓库 URL 或 git URL。`--json` 会打印解析后的来源标签，以及解析出的市场清单和插件条目。

## 相关

  * [构建插件](</zh-CN/plugins/building-plugins>)
  * [CLI 参考](</zh-CN/cli>)
  * [ClawHub](</zh-CN/clawhub>)


Was this useful?YesNo