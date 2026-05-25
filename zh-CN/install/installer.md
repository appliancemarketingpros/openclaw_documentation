---
title: 安装程序内部机制
source_url: https://docs.openclaw.ai/zh-CN/install/installer
scraped_at: 2026-05-25
---

OpenClaw 提供三个安装脚本，均由 `openclaw.ai` 提供。

脚本 | 平台 | 作用  
---|---|---  
`install.sh` | macOS / Linux / WSL | 按需安装 Node，通过 npm（默认）或 git 安装 OpenClaw，并可运行新手引导。  
`install-cli.sh` | macOS / Linux / WSL | 将 Node + OpenClaw 安装到本地前缀（`~/.openclaw`），支持 npm 或 git checkout 模式。无需 root 权限。  
`install.ps1` | Windows (PowerShell) | 按需安装 Node，通过 npm（默认）或 git 安装 OpenClaw，并可运行新手引导。  
  
## 快速命令

### install.sh

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash
[/code]

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash -s -- --help
[/code]

### install-cli.sh

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash
[/code]

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash -s -- --help
[/code]

### install.ps1

powershellCopy code
[code]
    iwr -useb https://openclaw.ai/install.ps1 | iex
[/code]

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -Tag beta -NoOnboard -DryRun
[/code]

* * *

## [install.sh](<http://install.sh>)

### 流程 ([install.sh](<http://install.sh>))

* ### 检测 OS

支持 macOS 和 Linux（包括 WSL）。如果检测到 macOS，会在缺少 Homebrew 时安装它。

* ### 默认确保 Node.js 24

检查 Node 版本，并在需要时安装 Node 24（macOS 上使用 Homebrew，Linux apt/dnf/yum 上使用 NodeSource 设置脚本）。为保持兼容性，OpenClaw 仍支持 Node 22 LTS，目前为 `22.16+`。

* ### 确保 Git

如果缺少 Git，则安装 Git。

* ### 安装 OpenClaw

  * `npm` 方法（默认）：全局 npm 安装
  * `git` 方法：克隆/更新仓库，使用 pnpm 安装依赖，构建，然后在 `~/.local/bin/openclaw` 安装包装器


* ### 安装后任务

  * 尽力刷新已加载的 Gateway 网关服务（`openclaw gateway install --force`，然后重启）
  * 在升级和 git 安装时运行 `openclaw doctor --non-interactive`（尽力而为）
  * 在适当时尝试新手引导（TTY 可用、新手引导未禁用，并且 bootstrap/配置检查通过）
  * 默认设置 `SHARP_IGNORE_GLOBAL_LIBVIPS=1`


### 源码 checkout 检测

如果在 OpenClaw checkout（`package.json` \+ `pnpm-workspace.yaml`）内运行，脚本会提供：

  * 使用 checkout（`git`），或
  * 使用全局安装（`npm`）


如果没有可用的 TTY，且未设置安装方法，它会默认使用 `npm` 并发出警告。

对于无效的方法选择或无效的 `--install-method` 值，脚本会以代码 `2` 退出。

### 示例 ([install.sh](<http://install.sh>))

### 默认

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash
[/code]

### 跳过新手引导

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash -s -- --no-onboard
[/code]

### Git 安装

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash -s -- --install-method git
[/code]

### 通过 npm 使用 GitHub main

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash -s -- --version main
[/code]

### 试运行

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash -s -- --dry-run
[/code]

标志参考 标志 | 描述  
---|---  
`--install-method npm|git` | 选择安装方法（默认：`npm`）。别名：`--method`  
`--npm` | npm 方法的快捷方式  
`--git` | git 方法的快捷方式。别名：`--github`  
`--version <version|dist-tag|spec>` | npm 版本、dist-tag 或包 spec（默认：`latest`）  
`--beta` | 如果可用则使用 beta dist-tag，否则回退到 `latest`  
`--git-dir <path>` | Checkout 目录（默认：`~/openclaw`）。别名：`--dir`  
`--no-git-update` | 对现有 checkout 跳过 `git pull`  
`--no-prompt` | 禁用提示  
`--no-onboard` | 跳过新手引导  
`--onboard` | 启用新手引导  
`--dry-run` | 打印操作但不应用更改  
`--verbose` | 启用调试输出（`set -x`，npm notice 级别日志）  
`--help` | 显示用法（`-h`）  
环境变量参考 变量 | 描述  
---|---  
`OPENCLAW_INSTALL_METHOD=git|npm` | 安装方法  
`OPENCLAW_VERSION=latest|next|main|<semver>|<spec>` | npm 版本、dist-tag 或包 spec  
`OPENCLAW_BETA=0|1` | 如果可用则使用 beta  
`OPENCLAW_GIT_DIR=<path>` | Checkout 目录  
`OPENCLAW_GIT_UPDATE=0|1` | 切换 git 更新  
`OPENCLAW_NO_PROMPT=1` | 禁用提示  
`OPENCLAW_NO_ONBOARD=1` | 跳过新手引导  
`OPENCLAW_DRY_RUN=1` | 试运行模式  
`OPENCLAW_VERBOSE=1` | 调试模式  
`OPENCLAW_NPM_LOGLEVEL=error|warn|notice` | npm 日志级别  
`SHARP_IGNORE_GLOBAL_LIBVIPS=0|1` | 控制 sharp/libvips 行为（默认：`1`）  
  
* * *

## [install-cli.sh](<http://install-cli.sh>)

### 流程 ([install-cli.sh](<http://install-cli.sh>))

* ### 安装本地 Node 运行时

将固定的受支持 Node LTS tarball（版本嵌入在脚本中并独立更新）下载到 `<prefix>/tools/node-v<version>` 并验证 SHA-256。

* ### 确保 Git

如果缺少 Git，则尝试通过 Linux 上的 apt/dnf/yum 或 macOS 上的 Homebrew 安装。

* ### 在前缀下安装 OpenClaw

  * `npm` 方法（默认）：使用 npm 安装到该前缀下，然后将包装器写入 `<prefix>/bin/openclaw`
  * `git` 方法：克隆/更新 checkout（默认 `~/openclaw`），并仍将包装器写入 `<prefix>/bin/openclaw`


* ### 刷新已加载的 Gateway 网关服务

如果 Gateway 网关服务已从同一前缀加载，脚本会运行 `openclaw gateway install --force`，然后运行 `openclaw gateway restart`，并尽力探测 Gateway 网关健康状况。

### 示例 ([install-cli.sh](<http://install-cli.sh>))

### 默认

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash
[/code]

### 自定义前缀 + 版本

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash -s -- --prefix /opt/openclaw --version latest
[/code]

### Git 安装

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash -s -- --install-method git --git-dir ~/openclaw
[/code]

### 自动化 JSON 输出

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash -s -- --json --prefix /opt/openclaw
[/code]

### 运行新手引导

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash -s -- --onboard
[/code]

标志参考 标志 | 描述  
---|---  
`--prefix <path>` | 安装前缀（默认：`~/.openclaw`）  
`--install-method npm|git` | 选择安装方法（默认：`npm`）。别名：`--method`  
`--npm` | npm 方法的快捷方式  
`--git`, `--github` | git 方法的快捷方式  
`--git-dir <path>` | Git checkout 目录（默认：`~/openclaw`）。别名：`--dir`  
`--version <ver>` | OpenClaw 版本或 dist-tag（默认：`latest`）  
`--node-version <ver>` | Node 版本（默认：`22.22.0`）  
`--json` | 发出 NDJSON 事件  
`--onboard` | 安装后运行 `openclaw onboard`  
`--no-onboard` | 跳过新手引导（默认）  
`--set-npm-prefix` | 在 Linux 上，如果当前前缀不可写，则强制 npm 前缀为 `~/.npm-global`  
`--help` | 显示用法（`-h`）  
环境变量参考 变量 | 描述  
---|---  
`OPENCLAW_PREFIX=<path>` | 安装前缀  
`OPENCLAW_INSTALL_METHOD=git|npm` | 安装方法  
`OPENCLAW_VERSION=<ver>` | OpenClaw 版本或 dist-tag  
`OPENCLAW_NODE_VERSION=<ver>` | Node 版本  
`OPENCLAW_GIT_DIR=<path>` | git 安装的 Git 检出目录  
`OPENCLAW_GIT_UPDATE=0|1` | 为现有检出切换 git 更新  
`OPENCLAW_NO_ONBOARD=1` | 跳过新手引导  
`OPENCLAW_NPM_LOGLEVEL=error|warn|notice` | npm 日志级别  
`SHARP_IGNORE_GLOBAL_LIBVIPS=0|1` | 控制 sharp/libvips 行为（默认值：`1`）  
  
* * *

## install.ps1

### 流程（install.ps1）

* ### 确保 PowerShell + Windows 环境

需要 PowerShell 5+。

* ### 默认确保 Node.js 24

如果缺失，会尝试通过 winget 安装，然后是 Chocolatey，再然后是 Scoop。Node 22 LTS（当前为 `22.16+`）仍受支持以保持兼容性。

* ### 安装 OpenClaw

  * `npm` 方法（默认）：使用选定的 `-Tag` 进行全局 npm 安装，并从可写的安装器临时目录启动，因此在 `C:\` 等受保护文件夹中打开的 shell 仍可正常工作
  * `git` 方法：克隆/更新仓库，使用 pnpm 安装/构建，并在 `%USERPROFILE%\.local\bin\openclaw.cmd` 安装包装器


* ### 安装后任务

  * 尽可能将所需的 bin 目录添加到用户 PATH
  * 尽力刷新已加载的 Gateway 网关服务（`openclaw gateway install --force`，然后重启）
  * 在升级和 git 安装时运行 `openclaw doctor --non-interactive`（尽力而为）


* ### 处理失败

`iwr ... | iex` 和脚本块安装会报告终止错误，但不会关闭当前 PowerShell 会话。直接使用 `powershell -File` / `pwsh -File` 安装时，仍会为自动化退出并返回非零状态。

### 示例（install.ps1）

### 默认

powershellCopy code
[code]
    iwr -useb https://openclaw.ai/install.ps1 | iex
[/code]

### Git 安装

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -InstallMethod git
[/code]

### 通过 npm 使用 GitHub main

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -Tag main
[/code]

### 自定义 git 目录

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -InstallMethod git -GitDir "C:\openclaw"
[/code]

### 试运行

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -DryRun
[/code]

### 调试跟踪

powershellCopy code
[code]
    # install.ps1 has no dedicated -Verbose flag yet.Set-PSDebug -Trace 1& ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -NoOnboardSet-PSDebug -Trace 0
[/code]

标志参考 标志 | 描述  
---|---  
`-InstallMethod npm|git` | 安装方法（默认值：`npm`）  
`-Tag <tag|version|spec>` | npm dist-tag、版本或包规范（默认值：`latest`）  
`-GitDir <path>` | 检出目录（默认值：`%USERPROFILE%\openclaw`）  
`-NoOnboard` | 跳过新手引导  
`-NoGitUpdate` | 跳过 `git pull`  
`-DryRun` | 仅打印操作  
环境变量参考 变量 | 描述  
---|---  
`OPENCLAW_INSTALL_METHOD=git|npm` | 安装方法  
`OPENCLAW_GIT_DIR=<path>` | 检出目录  
`OPENCLAW_NO_ONBOARD=1` | 跳过新手引导  
`OPENCLAW_GIT_UPDATE=0` | 禁用 git pull  
`OPENCLAW_DRY_RUN=1` | 试运行模式  
  
* * *

## CI 和自动化

使用非交互式标志/环境变量以获得可预测的运行结果。

### install.sh（非交互式 npm）

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash -s -- --no-prompt --no-onboard
[/code]

### install.sh（非交互式 git）

bashCopy code
[code]
    OPENCLAW_INSTALL_METHOD=git OPENCLAW_NO_PROMPT=1 \  curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash
[/code]

### install-cli.sh（JSON）

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash -s -- --json --prefix /opt/openclaw
[/code]

### install.ps1（跳过新手引导）

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -NoOnboard
[/code]

* * *

## 故障排除

为什么需要 Git？

`git` 安装方法需要 Git。对于 `npm` 安装，仍会检查/安装 Git，以避免依赖项使用 git URL 时出现 `spawn git ENOENT` 失败。

为什么 npm 在 Linux 上遇到 EACCES？

某些 Linux 设置会将 npm 全局前缀指向 root 拥有的路径。`install.sh` 可以将前缀切换到 `~/.npm-global`，并将 PATH 导出追加到 shell rc 文件（当这些文件存在时）。

sharp/libvips 问题

脚本默认设置 `SHARP_IGNORE_GLOBAL_LIBVIPS=1`，以避免 sharp 针对系统 libvips 构建。要覆盖：

bashCopy code
[code]
    SHARP_IGNORE_GLOBAL_LIBVIPS=0 curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash
[/code]

Windows：“npm error spawn git / ENOENT”

安装 Git for Windows，重新打开 PowerShell，然后重新运行安装器。

Windows：“openclaw is not recognized”

运行 `npm config get prefix`，并将该目录添加到你的用户 PATH（Windows 上不需要 `\bin` 后缀），然后重新打开 PowerShell。

Windows：如何获取详细的安装器输出

`install.ps1` 目前未公开 `-Verbose` 开关。 使用 PowerShell 跟踪进行脚本级诊断：

powershellCopy code
[code]
    Set-PSDebug -Trace 1& ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -NoOnboardSet-PSDebug -Trace 0
[/code]

安装后找不到 openclaw

通常是 PATH 问题。请参阅 [Node.js 故障排除](</zh-CN/install/node#troubleshooting>)。

## 相关

  * [安装概览](</zh-CN/install>)
  * [更新](</zh-CN/install/updating>)
  * [卸载](</zh-CN/install/uninstall>)


Was this useful?YesNo