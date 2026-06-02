---
title: CLI reference
source_url: https://docs.openclaw.ai/cli
scraped_at: 2026-06-02
---

`openclaw` is the main CLI entry point. Each core command has either a dedicated reference page or is documented with the command it aliases; this index lists the commands, the global flags, and the output styling rules that apply across the CLI.

Use the setup commands by intent:

  * `openclaw setup` creates the baseline config and workspace without walking the full guided onboarding flow.
  * `openclaw onboard` is the full guided first-run path for gateway, model auth, workspace, channels, skills, and health.
  * `openclaw configure` changes targeted parts of an existing setup, such as model auth, gateway, channels, plugins, or skills.
  * `openclaw channels add` configures channel accounts after the baseline exists; run it without flags for guided channel setup or with channel-specific flags for scripts.


## Command pages

Area | Commands  
---|---  
Setup and onboarding | [`crestodian`](</cli/crestodian>) · [`setup`](</cli/setup>) · [`onboard`](</cli/onboard>) · [`configure`](</cli/configure>) · [`config`](</cli/config>) · [`completion`](</cli/completion>) · [`doctor`](</cli/doctor>) · [`dashboard`](</cli/dashboard>)  
Reset and uninstall | [`backup`](</cli/backup>) · [`reset`](</cli/reset>) · [`uninstall`](</cli/uninstall>) · [`update`](</cli/update>)  
Messaging and agents | [`message`](</cli/message>) · [`agent`](</cli/agent>) · [`agents`](</cli/agents>) · [`acp`](</cli/acp>) · [`mcp`](</cli/mcp>)  
Health and sessions | [`status`](</cli/status>) · [`health`](</cli/health>) · [`sessions`](</cli/sessions>)  
Gateway and logs | [`gateway`](</cli/gateway>) · [`logs`](</cli/logs>) · [`system`](</cli/system>)  
Models and inference | [`models`](</cli/models>) · [`infer`](</cli/infer>) · `capability` (alias for [`infer`](</cli/infer>)) · [`memory`](</cli/memory>) · [`commitments`](</cli/commitments>) · [`wiki`](</cli/wiki>)  
Network and nodes | [`directory`](</cli/directory>) · [`nodes`](</cli/nodes>) · [`devices`](</cli/devices>) · [`node`](</cli/node>)  
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
`--dev` | Isolate state under `~/.openclaw-dev` and shift default ports  
`--profile <name>` | Isolate state under `~/.openclaw-<name>`  
`--container <name>` | Target a named container for execution  
`--no-color` | Disable ANSI colors (`NO_COLOR=1` is also respected)  
`--update` | Shorthand for [`openclaw update`](</cli/update>) (source installs only)  
`-V`, `--version`, `-v` | Print version and exit  
  
## Output modes

  * ANSI colors and progress indicators render only in TTY sessions.
  * OSC-8 hyperlinks render as clickable links where supported; otherwise the CLI falls back to plain URLs.
  * `--json` (and `--plain` where supported) disables styling for clean output.
  * Long-running commands show a progress indicator (OSC 9;4 when supported).


Palette source of truth: `src/terminal/palette.ts`.

## Command tree

Full command tree CodeCopy code
[code]
    openclaw [--dev] [--profile <name>] <command>crestodiansetuponboardconfigureconfig  get  set  unset  file  schema  validatecompletiondoctordashboardbackup  create  verifysecurity  auditsecrets  reload  audit  configure  applyresetuninstallupdate  wizard  statuschannels  list  status  capabilities  resolve  logs  add  remove  login  logoutdirectory  self  peers list  groups list|membersskills  search  install  update  list  info  checkplugins  list  inspect  install  uninstall  update  enable  disable  doctor  marketplace listworkboard  list  create  show  dispatchmemory  status  index  searchtranscripts  list  show  pathpath  resolve  find  set  validate  emitcommitments  list  dismisswiki  status  doctor  init  ingest  compile  lint  search  get  apply  bridge import  unsafe-local import  obsidian status|search|open|command|dailymessage  send  broadcast  poll  react  reactions  read  edit  delete  pin  unpin  pins  permissions  search  thread create|list|reply  emoji list|upload  sticker send|upload  role info|add|remove  channel info|list  member info  voice status  event list|create  timeout  kick  banagentagents  list  add  delete  bindings  bind  unbind  set-identityacpmcp  serve  list  show  set  unsetstatushealthsessions  cleanuptasks  list  audit  maintenance  show  notify  cancel  flow list|show|cancelgateway  call  usage-cost  health  status  probe  discover  install  uninstall  start  stop  restart  rundaemon  status  install  uninstall  start  stop  restartlogssystem  event  heartbeat last|enable|disable  presencemodels  list  status  set  set-image  aliases list|add|remove  fallbacks list|add|remove|clear  image-fallbacks list|add|remove|clear  scaninfer (alias: capability)  list  inspect  model run|list|inspect|providers|auth login|logout|status  image generate|edit|describe|describe-many|providers  audio transcribe|providers  tts convert|voices|providers|status|enable|disable|set-provider  video generate|describe|providers  web search|fetch|providers  embedding create|providers  auth add|login|login-github-copilot|setup-token|paste-token  auth order get|set|clearsandbox  list  recreate  explaincron  status  list  get  add  edit  rm  enable  disable  runs  runnodes  status  describe  list  pending  approve  reject  rename  invoke  notify  push  canvas snapshot|present|hide|navigate|eval  canvas a2ui push|reset  camera list|snap|clip  screen record  location getdevices  list  remove  clear  approve  reject  rotate  revokenode  run  status  install  uninstall  stop  restartapprovals  get  set  allowlist add|removeexec-policy  show  preset  setbrowser  status  start  stop  reset-profile  tabs  open  focus  close  profiles  create-profile  delete-profile  screenshot  snapshot  navigate  resize  click  type  press  hover  drag  select  upload  fill  dialog  wait  evaluate  console  pdfhooks  list  info  check  enable  disable  install  updatewebhooks  gmail setup|runproxy  start  run  coverage  sessions  query  blob  purgepairing  list  approveqrclawbot  qrdocsdns  setuptuichat (alias: tui --local)terminal (alias: tui --local)
[/code]

Plugins can add additional top-level commands, such as [`openclaw workboard`](</cli/workboard>) or `openclaw voicecall`.

## Chat slash commands

Chat messages support `/...` commands. See [slash commands](</tools/slash-commands>).

Highlights:

  * `/status` — quick diagnostics.
  * `/trace` — session-scoped plugin trace/debug lines.
  * `/config` — persisted config changes.
  * `/debug` — runtime-only config overrides (memory, not disk; requires `commands.debug: true`).


## Usage tracking

`openclaw status --usage` and the Control UI surface provider usage/quota when OAuth/API credentials are available. Data comes directly from provider usage endpoints and is normalized to `X% left`. Providers with current usage windows: Anthropic, GitHub Copilot, Gemini CLI, OpenAI Codex, MiniMax, Xiaomi, and z.ai.

See [Usage tracking](</concepts/usage-tracking>) for details.

## Related

  * [Slash commands](</tools/slash-commands>)
  * [Configuration](</gateway/configuration>)
  * [Environment](</help/environment>)


Was this useful?YesNo