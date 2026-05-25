---
title: Referencia de CLI
source_url: https://docs.openclaw.ai/es/cli
scraped_at: 2026-05-25
---

`openclaw` es el punto de entrada principal de la CLI. Cada comando principal tiene una página de referencia dedicada o está documentado con el comando del que es alias; este índice enumera los comandos, las marcas globales y las reglas de estilo de salida que se aplican en toda la CLI.

Usa los comandos de configuración según la intención:

  * `openclaw setup` crea la configuración base y el espacio de trabajo sin recorrer todo el flujo guiado de incorporación.
  * `openclaw onboard` es la ruta completa guiada de primer uso para gateway, autenticación de modelo, espacio de trabajo, canales, skills y salud.
  * `openclaw configure` cambia partes concretas de una configuración existente, como autenticación de modelo, gateway, canales, plugins o skills.
  * `openclaw channels add` configura cuentas de canal después de que exista la base; ejecútalo sin marcas para una configuración guiada de canales o con marcas específicas del canal para scripts.


## Páginas de comandos

Área | Comandos  
---|---  
Configuración e incorporación | [`crestodian`](</es/cli/crestodian>) · [`setup`](</es/cli/setup>) · [`onboard`](</es/cli/onboard>) · [`configure`](</es/cli/configure>) · [`config`](</es/cli/config>) · [`completion`](</es/cli/completion>) · [`doctor`](</es/cli/doctor>) · [`dashboard`](</es/cli/dashboard>)  
Restablecimiento y desinstalación | [`backup`](</es/cli/backup>) · [`reset`](</es/cli/reset>) · [`uninstall`](</es/cli/uninstall>) · [`update`](</es/cli/update>)  
Mensajería y agentes | [`message`](</es/cli/message>) · [`agent`](</es/cli/agent>) · [`agents`](</es/cli/agents>) · [`acp`](</es/cli/acp>) · [`mcp`](</es/cli/mcp>)  
Salud y sesiones | [`status`](</es/cli/status>) · [`health`](</es/cli/health>) · [`sessions`](</es/cli/sessions>)  
Gateway y registros | [`gateway`](</es/cli/gateway>) · [`logs`](</es/cli/logs>) · [`system`](</es/cli/system>)  
Modelos e inferencia | [`models`](</es/cli/models>) · [`infer`](</es/cli/infer>) · `capability` (alias de [`infer`](</es/cli/infer>)) · [`memory`](</es/cli/memory>) · [`commitments`](</es/cli/commitments>) · [`wiki`](</es/cli/wiki>)  
Red y Nodes | [`directory`](</es/cli/directory>) · [`nodes`](</es/cli/nodes>) · [`devices`](</es/cli/devices>) · [`node`](</es/cli/node>)  
Entorno de ejecución y sandbox | [`approvals`](</es/cli/approvals>) · `exec-policy` (consulta [`approvals`](</es/cli/approvals>)) · [`sandbox`](</es/cli/sandbox>) · [`tui`](</es/cli/tui>) · `chat`/`terminal` (alias de [`tui --local`](</es/cli/tui>)) · [`browser`](</es/cli/browser>)  
Automatización | [`cron`](</es/cli/cron>) · [`tasks`](</es/cli/tasks>) · [`hooks`](</es/cli/hooks>) · [`webhooks`](</es/cli/webhooks>)  
Descubrimiento y documentación | [`dns`](</es/cli/dns>) · [`docs`](</es/cli/docs>)  
Emparejamiento y canales | [`pairing`](</es/cli/pairing>) · [`qr`](</es/cli/qr>) · [`channels`](</es/cli/channels>)  
Seguridad y plugins | [`security`](</es/cli/security>) · [`secrets`](</es/cli/secrets>) · [`skills`](</es/cli/skills>) · [`plugins`](</es/cli/plugins>) · [`proxy`](</es/cli/proxy>)  
Alias heredados | [`daemon`](</es/cli/daemon>) (servicio de gateway) · [`clawbot`](</es/cli/clawbot>) (espacio de nombres)  
Plugins (opcional) | [`path`](</es/cli/path>) · [`voicecall`](</es/cli/voicecall>) (si está instalado)  
  
## Marcas globales

Marca | Propósito  
---|---  
`--dev` | Aísla el estado bajo `~/.openclaw-dev` y desplaza los puertos predeterminados  
`--profile <name>` | Aísla el estado bajo `~/.openclaw-<name>`  
`--container <name>` | Apunta a un contenedor con nombre para la ejecución  
`--no-color` | Desactiva los colores ANSI (también se respeta `NO_COLOR=1`)  
`--update` | Abreviatura de [`openclaw update`](</es/cli/update>) (solo instalaciones desde código fuente)  
`-V`, `--version`, `-v` | Imprime la versión y sale  
  
## Modos de salida

  * Los colores ANSI y los indicadores de progreso se renderizan solo en sesiones TTY.
  * Los hipervínculos OSC-8 se renderizan como enlaces clicables donde hay compatibilidad; de lo contrario, la CLI recurre a URL simples.
  * `--json` (y `--plain` donde sea compatible) desactiva el estilo para obtener una salida limpia.
  * Los comandos de larga duración muestran un indicador de progreso (OSC 9;4 cuando es compatible).


Fuente de verdad de la paleta: `src/terminal/palette.ts`.

## Árbol de comandos

Árbol de comandos completo CodeCopy code
[code]
    openclaw [--dev] [--profile <name>] <command>crestodiansetuponboardconfigureconfig  get  set  unset  file  schema  validatecompletiondoctordashboardbackup  create  verifysecurity  auditsecrets  reload  audit  configure  applyresetuninstallupdate  wizard  statuschannels  list  status  capabilities  resolve  logs  add  remove  login  logoutdirectory  self  peers list  groups list|membersskills  search  install  update  list  info  checkplugins  list  inspect  install  uninstall  update  enable  disable  doctor  marketplace listmemory  status  index  searchpath  resolve  find  set  validate  emitcommitments  list  dismisswiki  status  doctor  init  ingest  compile  lint  search  get  apply  bridge import  unsafe-local import  obsidian status|search|open|command|dailymessage  send  broadcast  poll  react  reactions  read  edit  delete  pin  unpin  pins  permissions  search  thread create|list|reply  emoji list|upload  sticker send|upload  role info|add|remove  channel info|list  member info  voice status  event list|create  timeout  kick  banagentagents  list  add  delete  bindings  bind  unbind  set-identityacpmcp  serve  list  show  set  unsetstatushealthsessions  cleanuptasks  list  audit  maintenance  show  notify  cancel  flow list|show|cancelgateway  call  usage-cost  health  status  probe  discover  install  uninstall  start  stop  restart  rundaemon  status  install  uninstall  start  stop  restartlogssystem  event  heartbeat last|enable|disable  presencemodels  list  status  set  set-image  aliases list|add|remove  fallbacks list|add|remove|clear  image-fallbacks list|add|remove|clear  scaninfer (alias: capability)  list  inspect  model run|list|inspect|providers|auth login|logout|status  image generate|edit|describe|describe-many|providers  audio transcribe|providers  tts convert|voices|providers|status|enable|disable|set-provider  video generate|describe|providers  web search|fetch|providers  embedding create|providers  auth add|login|login-github-copilot|setup-token|paste-token  auth order get|set|clearsandbox  list  recreate  explaincron  status  list  get  add  edit  rm  enable  disable  runs  runnodes  status  describe  list  pending  approve  reject  rename  invoke  notify  push  canvas snapshot|present|hide|navigate|eval  canvas a2ui push|reset  camera list|snap|clip  screen record  location getdevices  list  remove  clear  approve  reject  rotate  revokenode  run  status  install  uninstall  stop  restartapprovals  get  set  allowlist add|removeexec-policy  show  preset  setbrowser  status  start  stop  reset-profile  tabs  open  focus  close  profiles  create-profile  delete-profile  screenshot  snapshot  navigate  resize  click  type  press  hover  drag  select  upload  fill  dialog  wait  evaluate  console  pdfhooks  list  info  check  enable  disable  install  updatewebhooks  gmail setup|runproxy  start  run  coverage  sessions  query  blob  purgepairing  list  approveqrclawbot  qrdocsdns  setuptuichat (alias: tui --local)terminal (alias: tui --local)
[/code]

Los plugins pueden añadir comandos adicionales de nivel superior (por ejemplo, `openclaw voicecall`).

## Comandos slash de chat

Los mensajes de chat admiten comandos `/...`. Consulta [comandos slash](</es/tools/slash-commands>).

Aspectos destacados:

  * `/status` — diagnóstico rápido.
  * `/trace` — líneas de traza/depuración de plugin con alcance de sesión.
  * `/config` — cambios de configuración persistidos.
  * `/debug` — anulaciones de configuración solo en tiempo de ejecución (memoria, no disco; requiere `commands.debug: true`).


## Seguimiento de uso

`openclaw status --usage` y la interfaz de control muestran el uso/cuota del proveedor cuando hay credenciales OAuth/API disponibles. Los datos provienen directamente de los endpoints de uso del proveedor y se normalizan como `X% left`. Proveedores con ventanas de uso actuales: Anthropic, GitHub Copilot, Gemini CLI, OpenAI Codex, MiniMax, Xiaomi y [z.ai](<http://z.ai>).

Consulta [Seguimiento de uso](</es/concepts/usage-tracking>) para más detalles.

## Relacionado

  * [Comandos slash](</es/tools/slash-commands>)
  * [Configuración](</es/gateway/configuration>)
  * [Entorno](</es/help/environment>)


Was this useful?YesNo