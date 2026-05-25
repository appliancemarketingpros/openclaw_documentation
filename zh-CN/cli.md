---
title: CLI 参考
source_url: https://docs.openclaw.ai/zh-CN/cli
scraped_at: 2026-05-25
---

`openclaw` 是主要的 CLI 入口点。每个核心命令都有专门的参考页面，或者记录在它所别名指向的命令中；本索引列出命令、全局标志，以及适用于整个 CLI 的输出样式规则。

按意图使用设置命令：

  * `openclaw setup` 创建基线配置和工作区，不会走完整的引导式新手引导流程。
  * `openclaw onboard` 是完整的引导式首次运行路径，覆盖 Gateway 网关、模型凭证、工作区、渠道、Skills 和健康检查。
  * `openclaw configure` 更改现有设置中的特定部分，例如模型凭证、Gateway 网关、渠道、插件或 Skills。
  * `openclaw channels add` 在基线存在后配置渠道账号；不带标志运行可进入引导式渠道设置，或带渠道专用标志用于脚本。


## 命令页面

区域 | 命令  
---|---  
设置和新手引导 | [`crestodian`](</zh-CN/cli/crestodian>) · [`setup`](</zh-CN/cli/setup>) · [`onboard`](</zh-CN/cli/onboard>) · [`configure`](</zh-CN/cli/configure>) · [`config`](</zh-CN/cli/config>) · [`completion`](</zh-CN/cli/completion>) · [`doctor`](</zh-CN/cli/doctor>) · [`dashboard`](</zh-CN/cli/dashboard>)  
重置和卸载 | [`backup`](</zh-CN/cli/backup>) · [`reset`](</zh-CN/cli/reset>) · [`uninstall`](</zh-CN/cli/uninstall>) · [`update`](</zh-CN/cli/update>)  
消息和智能体 | [`message`](</zh-CN/cli/message>) · [`agent`](</zh-CN/cli/agent>) · [`agents`](</zh-CN/cli/agents>) · [`acp`](</zh-CN/cli/acp>) · [`mcp`](</zh-CN/cli/mcp>)  
健康检查和会话 | [`status`](</zh-CN/cli/status>) · [`health`](</zh-CN/cli/health>) · [`sessions`](</zh-CN/cli/sessions>)  
Gateway 网关和日志 | [`gateway`](</zh-CN/cli/gateway>) · [`logs`](</zh-CN/cli/logs>) · [`system`](</zh-CN/cli/system>)  
Models 和推理 | [`models`](</zh-CN/cli/models>) · [`infer`](</zh-CN/cli/infer>) · `capability`（[`infer`](</zh-CN/cli/infer>) 的别名） · [`memory`](</zh-CN/cli/memory>) · [`commitments`](</zh-CN/cli/commitments>) · [`wiki`](</zh-CN/cli/wiki>)  
网络和节点 | [`directory`](</zh-CN/cli/directory>) · [`nodes`](</zh-CN/cli/nodes>) · [`devices`](</zh-CN/cli/devices>) · [`node`](</zh-CN/cli/node>)  
运行时和沙箱 | [`approvals`](</zh-CN/cli/approvals>) · `exec-policy`（见 [`approvals`](</zh-CN/cli/approvals>)） · [`sandbox`](</zh-CN/cli/sandbox>) · [`tui`](</zh-CN/cli/tui>) · `chat`/`terminal`（[`tui --local`](</zh-CN/cli/tui>) 的别名） · [`browser`](</zh-CN/cli/browser>)  
自动化 | [`cron`](</zh-CN/cli/cron>) · [`tasks`](</zh-CN/cli/tasks>) · [`hooks`](</zh-CN/cli/hooks>) · [`webhooks`](</zh-CN/cli/webhooks>)  
设备发现和文档 | [`dns`](</zh-CN/cli/dns>) · [`docs`](</zh-CN/cli/docs>)  
配对和渠道 | [`pairing`](</zh-CN/cli/pairing>) · [`qr`](</zh-CN/cli/qr>) · [`channels`](</zh-CN/cli/channels>)  
安全和插件 | [`security`](</zh-CN/cli/security>) · [`secrets`](</zh-CN/cli/secrets>) · [`skills`](</zh-CN/cli/skills>) · [`plugins`](</zh-CN/cli/plugins>) · [`proxy`](</zh-CN/cli/proxy>)  
旧版别名 | [`daemon`](</zh-CN/cli/daemon>)（Gateway 网关服务） · [`clawbot`](</zh-CN/cli/clawbot>)（命名空间）  
插件（可选） | [`path`](</zh-CN/cli/path>) · [`voicecall`](</zh-CN/cli/voicecall>)（如果已安装）  
  
## 全局标志

标志 | 用途  
---|---  
`--dev` | 将状态隔离在 `~/.openclaw-dev` 下，并偏移默认端口  
`--profile <name>` | 将状态隔离在 `~/.openclaw-<name>` 下  
`--container <name>` | 将执行目标设为指定命名容器  
`--no-color` | 禁用 ANSI 颜色（也会遵守 `NO_COLOR=1`）  
`--update` | [`openclaw update`](</zh-CN/cli/update>) 的简写（仅限源码安装）  
`-V`, `--version`, `-v` | 打印版本并退出  
  
## 输出模式

  * ANSI 颜色和进度指示器仅在 TTY 会话中渲染。
  * 支持时，OSC-8 超链接会渲染为可点击链接；否则 CLI 会回退为纯 URL。
  * `--json`（以及支持处的 `--plain`）会禁用样式，以便获得干净输出。
  * 长时间运行的命令会显示进度指示器（支持时使用 OSC 9;4）。


调色板权威来源：`src/terminal/palette.ts`。

## 命令树

完整命令树 CodeCopy code
[code]
    openclaw [--dev] [--profile <name>] <command>crestodiansetuponboardconfigureconfig  get  set  unset  file  schema  validatecompletiondoctordashboardbackup  create  verifysecurity  auditsecrets  reload  audit  configure  applyresetuninstallupdate  wizard  statuschannels  list  status  capabilities  resolve  logs  add  remove  login  logoutdirectory  self  peers list  groups list|membersskills  search  install  update  list  info  checkplugins  list  inspect  install  uninstall  update  enable  disable  doctor  marketplace listmemory  status  index  searchpath  resolve  find  set  validate  emitcommitments  list  dismisswiki  status  doctor  init  ingest  compile  lint  search  get  apply  bridge import  unsafe-local import  obsidian status|search|open|command|dailymessage  send  broadcast  poll  react  reactions  read  edit  delete  pin  unpin  pins  permissions  search  thread create|list|reply  emoji list|upload  sticker send|upload  role info|add|remove  channel info|list  member info  voice status  event list|create  timeout  kick  banagentagents  list  add  delete  bindings  bind  unbind  set-identityacpmcp  serve  list  show  set  unsetstatushealthsessions  cleanuptasks  list  audit  maintenance  show  notify  cancel  flow list|show|cancelgateway  call  usage-cost  health  status  probe  discover  install  uninstall  start  stop  restart  rundaemon  status  install  uninstall  start  stop  restartlogssystem  event  heartbeat last|enable|disable  presencemodels  list  status  set  set-image  aliases list|add|remove  fallbacks list|add|remove|clear  image-fallbacks list|add|remove|clear  scaninfer (alias: capability)  list  inspect  model run|list|inspect|providers|auth login|logout|status  image generate|edit|describe|describe-many|providers  audio transcribe|providers  tts convert|voices|providers|status|enable|disable|set-provider  video generate|describe|providers  web search|fetch|providers  embedding create|providers  auth add|login|login-github-copilot|setup-token|paste-token  auth order get|set|clearsandbox  list  recreate  explaincron  status  list  get  add  edit  rm  enable  disable  runs  runnodes  status  describe  list  pending  approve  reject  rename  invoke  notify  push  canvas snapshot|present|hide|navigate|eval  canvas a2ui push|reset  camera list|snap|clip  screen record  location getdevices  list  remove  clear  approve  reject  rotate  revokenode  run  status  install  uninstall  stop  restartapprovals  get  set  allowlist add|removeexec-policy  show  preset  setbrowser  status  start  stop  reset-profile  tabs  open  focus  close  profiles  create-profile  delete-profile  screenshot  snapshot  navigate  resize  click  type  press  hover  drag  select  upload  fill  dialog  wait  evaluate  console  pdfhooks  list  info  check  enable  disable  install  updatewebhooks  gmail setup|runproxy  start  run  coverage  sessions  query  blob  purgepairing  list  approveqrclawbot  qrdocsdns  setuptuichat (alias: tui --local)terminal (alias: tui --local)
[/code]

插件可以添加额外的顶级命令（例如 `openclaw voicecall`）。

## 聊天斜杠命令

聊天消息支持 `/...` 命令。见[斜杠命令](</zh-CN/tools/slash-commands>)。

重点：

  * `/status` — 快速诊断。
  * `/trace` — 会话范围的插件跟踪/调试行。
  * `/config` — 持久化的配置更改。
  * `/debug` — 仅运行时配置覆盖（内存中，不写入磁盘；需要 `commands.debug: true`）。


## 用量跟踪

当 OAuth/API 凭证可用时，`openclaw status --usage` 和控制 UI 会显示提供商用量/配额。数据直接来自提供商用量端点，并规范化为 `X% left`。拥有当前用量窗口的提供商：Anthropic、GitHub Copilot、Gemini CLI、OpenAI Codex、MiniMax、Xiaomi 和 [z.ai](<http://z.ai>)。

详见[用量跟踪](</zh-CN/concepts/usage-tracking>)。

## 相关

  * [斜杠命令](</zh-CN/tools/slash-commands>)
  * [配置](</zh-CN/gateway/configuration>)
  * [环境](</zh-CN/help/environment>)


Was this useful?YesNo