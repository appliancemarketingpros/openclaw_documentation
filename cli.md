---
title: CLI reference
source_url: https://docs.openclaw.ai/cli
scraped_at: 2026-07-20
---

ReferenceCLI commands

`openclaw` is the main CLI entry point. Each core command has a dedicated reference page or is documented with the command it aliases; this index lists the commands, global flags, and output styling rules that apply across the CLI.

Setup commands by intent:

  * `openclaw setup` and `openclaw onboard` verify inference first, then start OpenClaw for Gateway, workspace, channels, skills, and health setup.
  * `openclaw setup --baseline` creates the baseline config and workspace without walking the guided onboarding flow.
  * `openclaw configure` changes targeted parts of an existing setup: model auth, gateway, channels, plugins, or skills.
  * `openclaw channels add` configures channel accounts after the baseline exists; run without flags for guided setup, or with channel-specific flags for scripts.


## Command pages

Area | Commands  
---|---  
Setup and onboarding | [`openclaw`](</cli/openclaw>) · [`setup`](</cli/setup>) · [`onboard`](</cli/onboard>) · [`configure`](</cli/configure>) · [`config`](</cli/config>) · [`completion`](</cli/completion>) · [`doctor`](</cli/doctor>) · [`dashboard`](</cli/dashboard>)  
Reset, backup, and migration | [`backup`](</cli/backup>) · [`migrate`](</cli/migrate>) · [`reset`](</cli/reset>) · [`uninstall`](</cli/uninstall>) · [`update`](</cli/update>)  
Messaging and agents | [`message`](</cli/message>) · [`agent`](</cli/agent>) · [`agents`](</cli/agents>) · [`attach`](</cli/attach>) · [`acp`](</cli/acp>) · [`mcp`](</cli/mcp>)  
Health and sessions | [`status`](</cli/status>) · [`health`](</cli/health>) · [`sessions`](</cli/sessions>) · [`audit`](</cli/audit>)  
Gateway and logs | [`gateway`](</cli/gateway>) · [`logs`](</cli/logs>) · [`system`](</cli/system>)  
Models and inference | [`models`](</cli/models>) · [`promos`](</cli/promos>) · [`infer`](</cli/infer>) · `capability` (alias for [`infer`](</cli/infer>)) · [`memory`](</cli/memory>) · [`commitments`](</cli/commitments>) · [`wiki`](</cli/wiki>)  
Network and nodes | [`directory`](</cli/directory>) · [`nodes`](</cli/nodes>) · [`devices`](</cli/devices>) · [`node`](</cli/node>) · [`worker`](</cli/worker>)  
Runtime and sandbox | [`approvals`](</cli/approvals>) · `exec-policy` (see [`approvals`](</cli/approvals>)) · [`sandbox`](</cli/sandbox>) · [`tui`](</cli/tui>) · `chat`/`terminal` (aliases for [`tui --local`](</cli/tui>)) · [`browser`](</cli/browser>)  
Automation | [`cron`](</cli/cron>) · [`tasks`](</cli/tasks>) · [`hooks`](</cli/hooks>) · [`webhooks`](</cli/webhooks>) · [`transcripts`](</cli/transcripts>)  
Discovery and docs | [`dns`](</cli/dns>) · [`docs`](</cli/docs>)  
Pairing and channels | [`pairing`](</cli/pairing>) · [`qr`](</cli/qr>) · [`channels`](</cli/channels>)  
Security and plugins | [`security`](</cli/security>) · [`secrets`](</cli/secrets>) · [`skills`](</cli/skills>) · [`plugins`](</cli/plugins>) · [`proxy`](</cli/proxy>)  
Legacy aliases | [`daemon`](</cli/daemon>) (gateway service) · [`clawbot`](</cli/clawbot>) (namespace)  
Plugins (optional) | [`path`](</cli/path>) · [`policy`](</cli/policy>) · [`voicecall`](</cli/voicecall>) · [`workboard`](</cli/workboard>) (if installed)  
  
## Global flags

Flag | Purpose  
---|---  
`--dev` | Isolate state under `~/.openclaw-dev`, default gateway port 19001, and shift derived ports  
`--profile <name>` | Isolate state under `~/.openclaw-<name>` (`OPENCLAW_STATE_DIR`/`OPENCLAW_CONFIG_PATH`)  
`--container <name>` | Run the CLI inside a running Podman/Docker container named `<name>` (default: env `OPENCLAW_CONTAINER`)  
`--log-level <level>` | Override the global log level for file + console output  
`--no-color` | Disable ANSI colors (`NO_COLOR=1` is also respected)  
`--update` | Shorthand for [`openclaw update`](</cli/update>); works for both source checkouts and package installs  
`-V`, `--version`, `-v` | Print version and exit  
  
## Output modes

  * ANSI colors and progress indicators render only in TTY sessions.
  * OSC-8 hyperlinks render as clickable links where supported; otherwise the CLI falls back to plain URLs.
  * `--json` (and `--plain` where supported) disables styling for clean output.
  * Long-running commands show a progress indicator (OSC 9;4 when supported).


## Color palette

OpenClaw uses a lobster palette for CLI output:

Token | Hex | Used for  
---|---|---  
`accent` | `#FF5A2D` | Headings, labels, primary highlights  
`accentBright` | `#FF7A3D` | Command names, emphasis  
`accentDim` | `#D14A22` | Secondary highlight text  
`info` | `#FF8A5B` | Informational values  
`success` | `#2FBF71` | Success states  
`warn` | `#FFB020` | Warnings, option flags, fallbacks  
`error` | `#E23D2D` | Errors, failures  
`muted` | `#8B7F77` | De-emphasis, metadata  
  
Palette source of truth: `packages/terminal-core/src/palette.ts`.

## Command tree

Full command tree

This map covers core commands and their primary subcommands. Plugin-added subcommands (for example under `skills`, `plugins`, and `wiki`) evolve independently; run `<command> --help` for the authoritative, current list.

CodeCopy code
[code]
    openclaw [--dev] [--profile <name>] <command>openclawsetuponboardconfigureconfig  get  set  unset  file  schema  validatecompletiondoctordashboardbackup  create  verifymigrate  list  plan <provider>  apply <provider>security  auditsecrets  reload  audit  configure  applyresetuninstallupdate  wizard  status  repairchannels  list  status  capabilities  resolve  logs  add  remove  login  logoutdirectory  self  peers list  groups list|membersskills  search  install  update  verify  workshop list|inspect|propose-create|propose-update|revise|apply|reject|quarantine  list  info  checkplugins  list  search  inspect  install  uninstall  update  enable  disable  doctor  build  validate  init  registry  marketplace list|entries|refreshworkboard  list  create  show  dispatchmemory  status  index  searchtranscripts  list  show  pathpath  resolve  find  set  validate  emitcommitments  list  dismisswiki  status  doctor  init  compile  lint  ingest  okf import  search  get  apply synthesis|metadata  bridge import  unsafe-local import  chatgpt import|rollback  obsidian status|search|open|command|dailymessage  send  broadcast  poll  react  reactions  read  edit  delete  pin  unpin  pins  permissions  search  thread create|list|reply  emoji list|upload  sticker send|upload  role info|add|remove  channel info|list  member info  voice status  event list|create  timeout  kick  banagentagents  list  add  delete  bindings  bind  unbind  set-identityattachacpmcp  serve  list  show  set  unsetstatushealthsessions  cleanupaudittasks  list  audit  maintenance  show  notify  cancel  flow list|show|cancelgateway  call  usage-cost  health  stability  diagnostics export  status  probe  discover  install  uninstall  start  stop  restart  rundaemon  status  install  uninstall  start  stop  restartlogssystem  event  heartbeat last|enable|disable  presencemodels  list  status  set  set-image  aliases list|add|remove  fallbacks list|add|remove|clear  image-fallbacks list|add|remove|clear  scan  auth list|add|login|setup-token|paste-token|paste-api-key|login-github-copilot  auth order get|set|clearpromos  list  claim <slug>infer (alias: capability)  list  inspect  model run|list|inspect|providers|auth login|logout|status  image generate|edit|describe|describe-many|providers  audio transcribe|providers  tts convert|voices|personas|providers|status|enable|disable|set-provider|set-persona  video generate|describe|providers  web search|fetch|providers  embedding create|providerssandbox  list  recreate  explaincron  status  list  get  add  edit  rm  enable  disable  runs  runnodes  status  describe  list  pending  approve  reject  rename  invoke  notify  push  canvas snapshot|present|hide|navigate|eval  canvas a2ui push|reset  camera list|snap|clip  screen record  location getdevices  list  remove  clear  approve  reject  rotate  revokenode  run  status  install  uninstall  stop  restartworkerapprovals  get  set  allowlist add|removeexec-policy  show  preset  setbrowser  status  start  stop  reset-profile  tabs  open  focus  close  profiles  create-profile  delete-profile  screenshot  snapshot  navigate  resize  click  type  press  hover  drag  select  upload  fill  dialog  wait  evaluate  console  pdfhooks  list  info  check  enable  disable  install  updatewebhooks  gmail setup|runproxy  start  run  coverage  sessions  query  blob  purgepairing  list  approveqrclawbot  qrdocsdns  setuptuichat (alias: tui --local)terminal (alias: tui --local)
[/code]

Plugins can add additional top-level commands, such as [`openclaw workboard`](</cli/workboard>) or `openclaw voicecall`.

## Chat slash commands

Chat messages support `/...` commands. See [slash commands](</tools/slash-commands>).

Highlights:

  * `/status` \- quick diagnostics.
  * `/trace` \- session-scoped plugin trace/debug lines.
  * `/config` \- persisted config changes.
  * `/debug` \- runtime-only config overrides (memory, not disk; requires `commands.debug: true`).


## Usage tracking

`openclaw status --usage` and the Control UI surface provider usage/quota when OAuth/API credentials are available. Data comes directly from provider usage endpoints and is normalized to `X% left`. Providers with current usage windows: Anthropic, Gemini CLI, GitHub Copilot, MiniMax, OpenAI Codex, Xiaomi, and z.ai.

See [Usage tracking](</concepts/usage-tracking>) for details.

## Related

  * [Slash commands](</tools/slash-commands>)
  * [Configuration](</gateway/configuration>)
  * [Environment](</help/environment>)


Was this useful?YesNo

Open issue