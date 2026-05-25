---
title: Referência da CLI
source_url: https://docs.openclaw.ai/pt-BR/cli
scraped_at: 2026-05-25
---

`openclaw` é o ponto de entrada principal da CLI. Cada comando principal tem uma página de referência dedicada ou é documentado junto ao comando do qual é alias; este índice lista os comandos, as flags globais e as regras de estilo de saída que se aplicam em toda a CLI.

Use os comandos de configuração por intenção:

  * `openclaw setup` cria a configuração e o workspace básicos sem percorrer todo o fluxo guiado de onboarding.
  * `openclaw onboard` é o caminho completo guiado de primeira execução para gateway, autenticação de modelo, workspace, canais, skills e integridade.
  * `openclaw configure` altera partes específicas de uma configuração existente, como autenticação de modelo, gateway, canais, plugins ou skills.
  * `openclaw channels add` configura contas de canal depois que a base já existe; execute sem flags para configuração guiada de canais ou com flags específicas de canal para scripts.


## Páginas de comandos

Área | Comandos  
---|---  
Configuração e onboarding | [`crestodian`](</pt-BR/cli/crestodian>) · [`setup`](</pt-BR/cli/setup>) · [`onboard`](</pt-BR/cli/onboard>) · [`configure`](</pt-BR/cli/configure>) · [`config`](</pt-BR/cli/config>) · [`completion`](</pt-BR/cli/completion>) · [`doctor`](</pt-BR/cli/doctor>) · [`dashboard`](</pt-BR/cli/dashboard>)  
Redefinição e desinstalação | [`backup`](</pt-BR/cli/backup>) · [`reset`](</pt-BR/cli/reset>) · [`uninstall`](</pt-BR/cli/uninstall>) · [`update`](</pt-BR/cli/update>)  
Mensagens e agentes | [`message`](</pt-BR/cli/message>) · [`agent`](</pt-BR/cli/agent>) · [`agents`](</pt-BR/cli/agents>) · [`acp`](</pt-BR/cli/acp>) · [`mcp`](</pt-BR/cli/mcp>)  
Integridade e sessões | [`status`](</pt-BR/cli/status>) · [`health`](</pt-BR/cli/health>) · [`sessions`](</pt-BR/cli/sessions>)  
Gateway e logs | [`gateway`](</pt-BR/cli/gateway>) · [`logs`](</pt-BR/cli/logs>) · [`system`](</pt-BR/cli/system>)  
Modelos e inferência | [`models`](</pt-BR/cli/models>) · [`infer`](</pt-BR/cli/infer>) · `capability` (alias para [`infer`](</pt-BR/cli/infer>)) · [`memory`](</pt-BR/cli/memory>) · [`commitments`](</pt-BR/cli/commitments>) · [`wiki`](</pt-BR/cli/wiki>)  
Rede e nós | [`directory`](</pt-BR/cli/directory>) · [`nodes`](</pt-BR/cli/nodes>) · [`devices`](</pt-BR/cli/devices>) · [`node`](</pt-BR/cli/node>)  
Runtime e sandbox | [`approvals`](</pt-BR/cli/approvals>) · `exec-policy` (veja [`approvals`](</pt-BR/cli/approvals>)) · [`sandbox`](</pt-BR/cli/sandbox>) · [`tui`](</pt-BR/cli/tui>) · `chat`/`terminal` (aliases para [`tui --local`](</pt-BR/cli/tui>)) · [`browser`](</pt-BR/cli/browser>)  
Automação | [`cron`](</pt-BR/cli/cron>) · [`tasks`](</pt-BR/cli/tasks>) · [`hooks`](</pt-BR/cli/hooks>) · [`webhooks`](</pt-BR/cli/webhooks>)  
Descoberta e documentação | [`dns`](</pt-BR/cli/dns>) · [`docs`](</pt-BR/cli/docs>)  
Pareamento e canais | [`pairing`](</pt-BR/cli/pairing>) · [`qr`](</pt-BR/cli/qr>) · [`channels`](</pt-BR/cli/channels>)  
Segurança e plugins | [`security`](</pt-BR/cli/security>) · [`secrets`](</pt-BR/cli/secrets>) · [`skills`](</pt-BR/cli/skills>) · [`plugins`](</pt-BR/cli/plugins>) · [`proxy`](</pt-BR/cli/proxy>)  
Aliases legados | [`daemon`](</pt-BR/cli/daemon>) (serviço de gateway) · [`clawbot`](</pt-BR/cli/clawbot>) (namespace)  
Plugins (opcionais) | [`path`](</pt-BR/cli/path>) · [`voicecall`](</pt-BR/cli/voicecall>) (se instalado)  
  
## Flags globais

Flag | Finalidade  
---|---  
`--dev` | Isola o estado em `~/.openclaw-dev` e desloca as portas padrão  
`--profile <name>` | Isola o estado em `~/.openclaw-<name>`  
`--container <name>` | Direciona um contêiner nomeado para execução  
`--no-color` | Desativa cores ANSI (`NO_COLOR=1` também é respeitado)  
`--update` | Atalho para [`openclaw update`](</pt-BR/cli/update>) (somente instalações por código-fonte)  
`-V`, `--version`, `-v` | Imprime a versão e sai  
  
## Modos de saída

  * Cores ANSI e indicadores de progresso são renderizados apenas em sessões TTY.
  * Hiperlinks OSC-8 são renderizados como links clicáveis onde houver suporte; caso contrário, a CLI retorna para URLs simples.
  * `--json` (e `--plain` onde houver suporte) desativa o estilo para saída limpa.
  * Comandos de longa execução mostram um indicador de progresso (OSC 9;4 quando suportado).


Fonte da verdade da paleta: `src/terminal/palette.ts`.

## Árvore de comandos

Árvore completa de comandos CodeCopy code
[code]
    openclaw [--dev] [--profile <name>] <command>crestodiansetuponboardconfigureconfig  get  set  unset  file  schema  validatecompletiondoctordashboardbackup  create  verifysecurity  auditsecrets  reload  audit  configure  applyresetuninstallupdate  wizard  statuschannels  list  status  capabilities  resolve  logs  add  remove  login  logoutdirectory  self  peers list  groups list|membersskills  search  install  update  list  info  checkplugins  list  inspect  install  uninstall  update  enable  disable  doctor  marketplace listmemory  status  index  searchpath  resolve  find  set  validate  emitcommitments  list  dismisswiki  status  doctor  init  ingest  compile  lint  search  get  apply  bridge import  unsafe-local import  obsidian status|search|open|command|dailymessage  send  broadcast  poll  react  reactions  read  edit  delete  pin  unpin  pins  permissions  search  thread create|list|reply  emoji list|upload  sticker send|upload  role info|add|remove  channel info|list  member info  voice status  event list|create  timeout  kick  banagentagents  list  add  delete  bindings  bind  unbind  set-identityacpmcp  serve  list  show  set  unsetstatushealthsessions  cleanuptasks  list  audit  maintenance  show  notify  cancel  flow list|show|cancelgateway  call  usage-cost  health  status  probe  discover  install  uninstall  start  stop  restart  rundaemon  status  install  uninstall  start  stop  restartlogssystem  event  heartbeat last|enable|disable  presencemodels  list  status  set  set-image  aliases list|add|remove  fallbacks list|add|remove|clear  image-fallbacks list|add|remove|clear  scaninfer (alias: capability)  list  inspect  model run|list|inspect|providers|auth login|logout|status  image generate|edit|describe|describe-many|providers  audio transcribe|providers  tts convert|voices|providers|status|enable|disable|set-provider  video generate|describe|providers  web search|fetch|providers  embedding create|providers  auth add|login|login-github-copilot|setup-token|paste-token  auth order get|set|clearsandbox  list  recreate  explaincron  status  list  get  add  edit  rm  enable  disable  runs  runnodes  status  describe  list  pending  approve  reject  rename  invoke  notify  push  canvas snapshot|present|hide|navigate|eval  canvas a2ui push|reset  camera list|snap|clip  screen record  location getdevices  list  remove  clear  approve  reject  rotate  revokenode  run  status  install  uninstall  stop  restartapprovals  get  set  allowlist add|removeexec-policy  show  preset  setbrowser  status  start  stop  reset-profile  tabs  open  focus  close  profiles  create-profile  delete-profile  screenshot  snapshot  navigate  resize  click  type  press  hover  drag  select  upload  fill  dialog  wait  evaluate  console  pdfhooks  list  info  check  enable  disable  install  updatewebhooks  gmail setup|runproxy  start  run  coverage  sessions  query  blob  purgepairing  list  approveqrclawbot  qrdocsdns  setuptuichat (alias: tui --local)terminal (alias: tui --local)
[/code]

Plugins podem adicionar outros comandos de nível superior (por exemplo, `openclaw voicecall`).

## Comandos de barra do chat

Mensagens de chat aceitam comandos `/...`. Veja [comandos de barra](</pt-BR/tools/slash-commands>).

Destaques:

  * `/status` — diagnósticos rápidos.
  * `/trace` — linhas de trace/debug de plugin com escopo de sessão.
  * `/config` — alterações de configuração persistidas.
  * `/debug` — substituições de configuração somente em runtime (memória, não disco; requer `commands.debug: true`).


## Rastreamento de uso

`openclaw status --usage` e a interface de controle exibem uso/cota do provedor quando credenciais OAuth/API estão disponíveis. Os dados vêm diretamente dos endpoints de uso dos provedores e são normalizados para `X% left`. Provedores com janelas de uso atuais: Anthropic, GitHub Copilot, Gemini CLI, OpenAI Codex, MiniMax, Xiaomi e [z.ai](<http://z.ai>).

Veja [Rastreamento de uso](</pt-BR/concepts/usage-tracking>) para detalhes.

## Relacionado

  * [Comandos de barra](</pt-BR/tools/slash-commands>)
  * [Configuração](</pt-BR/gateway/configuration>)
  * [Ambiente](</pt-BR/help/environment>)


Was this useful?YesNo