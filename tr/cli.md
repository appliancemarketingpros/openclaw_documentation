---
title: CLI referansı
source_url: https://docs.openclaw.ai/tr/cli
scraped_at: 2026-05-25
---

`openclaw`, ana CLI giriş noktasıdır. Her çekirdek komutun ya özel bir başvuru sayfası vardır ya da takma ad olduğu komutla birlikte belgelenir; bu dizin, komutları, genel bayrakları ve CLI genelinde geçerli olan çıktı biçimlendirme kurallarını listeler.

Kurulum komutlarını amaca göre kullanın:

  * `openclaw setup`, tam yönlendirmeli ilk katılım akışından geçmeden temel yapılandırmayı ve çalışma alanını oluşturur.
  * `openclaw onboard`, gateway, model kimlik doğrulaması, çalışma alanı, kanallar, Skills ve sağlık için tam yönlendirmeli ilk çalıştırma yoludur.
  * `openclaw configure`, mevcut bir kurulumun model kimlik doğrulaması, gateway, kanallar, plugin'ler veya Skills gibi hedeflenmiş bölümlerini değiştirir.
  * `openclaw channels add`, temel yapılandırma mevcut olduktan sonra kanal hesaplarını yapılandırır; yönlendirmeli kanal kurulumu için bayraksız, betikler için kanala özgü bayraklarla çalıştırın.


## Komut sayfaları

Alan | Komutlar  
---|---  
Kurulum ve ilk katılım | [`crestodian`](</tr/cli/crestodian>) · [`setup`](</tr/cli/setup>) · [`onboard`](</tr/cli/onboard>) · [`configure`](</tr/cli/configure>) · [`config`](</tr/cli/config>) · [`completion`](</tr/cli/completion>) · [`doctor`](</tr/cli/doctor>) · [`dashboard`](</tr/cli/dashboard>)  
Sıfırlama ve kaldırma | [`backup`](</tr/cli/backup>) · [`reset`](</tr/cli/reset>) · [`uninstall`](</tr/cli/uninstall>) · [`update`](</tr/cli/update>)  
Mesajlaşma ve ajanlar | [`message`](</tr/cli/message>) · [`agent`](</tr/cli/agent>) · [`agents`](</tr/cli/agents>) · [`acp`](</tr/cli/acp>) · [`mcp`](</tr/cli/mcp>)  
Sağlık ve oturumlar | [`status`](</tr/cli/status>) · [`health`](</tr/cli/health>) · [`sessions`](</tr/cli/sessions>)  
Gateway ve günlükler | [`gateway`](</tr/cli/gateway>) · [`logs`](</tr/cli/logs>) · [`system`](</tr/cli/system>)  
Modeller ve çıkarım | [`models`](</tr/cli/models>) · [`infer`](</tr/cli/infer>) · `capability` ([`infer`](</tr/cli/infer>) için takma ad) · [`memory`](</tr/cli/memory>) · [`commitments`](</tr/cli/commitments>) · [`wiki`](</tr/cli/wiki>)  
Ağ ve düğümler | [`directory`](</tr/cli/directory>) · [`nodes`](</tr/cli/nodes>) · [`devices`](</tr/cli/devices>) · [`node`](</tr/cli/node>)  
Çalışma zamanı ve sandbox | [`approvals`](</tr/cli/approvals>) · `exec-policy` (bkz. [`approvals`](</tr/cli/approvals>)) · [`sandbox`](</tr/cli/sandbox>) · [`tui`](</tr/cli/tui>) · `chat`/`terminal` ([`tui --local`](</tr/cli/tui>) için takma adlar) · [`browser`](</tr/cli/browser>)  
Otomasyon | [`cron`](</tr/cli/cron>) · [`tasks`](</tr/cli/tasks>) · [`hooks`](</tr/cli/hooks>) · [`webhooks`](</tr/cli/webhooks>)  
Keşif ve dokümantasyon | [`dns`](</tr/cli/dns>) · [`docs`](</tr/cli/docs>)  
Eşleştirme ve kanallar | [`pairing`](</tr/cli/pairing>) · [`qr`](</tr/cli/qr>) · [`channels`](</tr/cli/channels>)  
Güvenlik ve plugin'ler | [`security`](</tr/cli/security>) · [`secrets`](</tr/cli/secrets>) · [`skills`](</tr/cli/skills>) · [`plugins`](</tr/cli/plugins>) · [`proxy`](</tr/cli/proxy>)  
Eski takma adlar | [`daemon`](</tr/cli/daemon>) (gateway hizmeti) · [`clawbot`](</tr/cli/clawbot>) (ad alanı)  
Plugin'ler (isteğe bağlı) | [`path`](</tr/cli/path>) · [`voicecall`](</tr/cli/voicecall>) (yüklüyse)  
  
## Genel bayraklar

Bayrak | Amaç  
---|---  
`--dev` | Durumu `~/.openclaw-dev` altında yalıtır ve varsayılan bağlantı noktalarını kaydırır  
`--profile <name>` | Durumu `~/.openclaw-<name>` altında yalıtır  
`--container <name>` | Yürütme için adlandırılmış bir kapsayıcıyı hedefler  
`--no-color` | ANSI renklerini devre dışı bırakır (`NO_COLOR=1` de dikkate alınır)  
`--update` | [`openclaw update`](</tr/cli/update>) için kısayol (yalnızca kaynak kurulumları)  
`-V`, `--version`, `-v` | Sürümü yazdırır ve çıkar  
  
## Çıktı modları

  * ANSI renkleri ve ilerleme göstergeleri yalnızca TTY oturumlarında işlenir.
  * OSC-8 köprüleri desteklendiği yerlerde tıklanabilir bağlantılar olarak işlenir; aksi halde CLI düz URL'lere geri döner.
  * `--json` (ve desteklendiği yerlerde `--plain`) temiz çıktı için biçimlendirmeyi devre dışı bırakır.
  * Uzun süren komutlar bir ilerleme göstergesi gösterir (desteklendiğinde OSC 9;4).


Palet için gerçek kaynak: `src/terminal/palette.ts`.

## Komut ağacı

Tam komut ağacı CodeCopy code
[code]
    openclaw [--dev] [--profile <name>] <command>crestodiansetuponboardconfigureconfig  get  set  unset  file  schema  validatecompletiondoctordashboardbackup  create  verifysecurity  auditsecrets  reload  audit  configure  applyresetuninstallupdate  wizard  statuschannels  list  status  capabilities  resolve  logs  add  remove  login  logoutdirectory  self  peers list  groups list|membersskills  search  install  update  list  info  checkplugins  list  inspect  install  uninstall  update  enable  disable  doctor  marketplace listmemory  status  index  searchpath  resolve  find  set  validate  emitcommitments  list  dismisswiki  status  doctor  init  ingest  compile  lint  search  get  apply  bridge import  unsafe-local import  obsidian status|search|open|command|dailymessage  send  broadcast  poll  react  reactions  read  edit  delete  pin  unpin  pins  permissions  search  thread create|list|reply  emoji list|upload  sticker send|upload  role info|add|remove  channel info|list  member info  voice status  event list|create  timeout  kick  banagentagents  list  add  delete  bindings  bind  unbind  set-identityacpmcp  serve  list  show  set  unsetstatushealthsessions  cleanuptasks  list  audit  maintenance  show  notify  cancel  flow list|show|cancelgateway  call  usage-cost  health  status  probe  discover  install  uninstall  start  stop  restart  rundaemon  status  install  uninstall  start  stop  restartlogssystem  event  heartbeat last|enable|disable  presencemodels  list  status  set  set-image  aliases list|add|remove  fallbacks list|add|remove|clear  image-fallbacks list|add|remove|clear  scaninfer (alias: capability)  list  inspect  model run|list|inspect|providers|auth login|logout|status  image generate|edit|describe|describe-many|providers  audio transcribe|providers  tts convert|voices|providers|status|enable|disable|set-provider  video generate|describe|providers  web search|fetch|providers  embedding create|providers  auth add|login|login-github-copilot|setup-token|paste-token  auth order get|set|clearsandbox  list  recreate  explaincron  status  list  get  add  edit  rm  enable  disable  runs  runnodes  status  describe  list  pending  approve  reject  rename  invoke  notify  push  canvas snapshot|present|hide|navigate|eval  canvas a2ui push|reset  camera list|snap|clip  screen record  location getdevices  list  remove  clear  approve  reject  rotate  revokenode  run  status  install  uninstall  stop  restartapprovals  get  set  allowlist add|removeexec-policy  show  preset  setbrowser  status  start  stop  reset-profile  tabs  open  focus  close  profiles  create-profile  delete-profile  screenshot  snapshot  navigate  resize  click  type  press  hover  drag  select  upload  fill  dialog  wait  evaluate  console  pdfhooks  list  info  check  enable  disable  install  updatewebhooks  gmail setup|runproxy  start  run  coverage  sessions  query  blob  purgepairing  list  approveqrclawbot  qrdocsdns  setuptuichat (alias: tui --local)terminal (alias: tui --local)
[/code]

Plugin'ler ek üst düzey komutlar ekleyebilir (örneğin `openclaw voicecall`).

## Sohbet eğik çizgi komutları

Sohbet mesajları `/...` komutlarını destekler. Bkz. [eğik çizgi komutları](</tr/tools/slash-commands>).

Öne çıkanlar:

  * `/status` — hızlı tanılama.
  * `/trace` — oturum kapsamlı plugin izleme/hata ayıklama satırları.
  * `/config` — kalıcı yapılandırma değişiklikleri.
  * `/debug` — yalnızca çalışma zamanında geçerli yapılandırma geçersiz kılmaları (bellek, disk değil; `commands.debug: true` gerektirir).


## Kullanım takibi

`openclaw status --usage` ve Control UI, OAuth/API kimlik bilgileri mevcut olduğunda sağlayıcı kullanımını/kotasını gösterir. Veriler doğrudan sağlayıcı kullanım uç noktalarından gelir ve `X% left` biçimine normalize edilir. Geçerli kullanım pencereleri olan sağlayıcılar: Anthropic, GitHub Copilot, Gemini CLI, OpenAI Codex, MiniMax, Xiaomi ve [z.ai](<http://z.ai>).

Ayrıntılar için bkz. [Kullanım takibi](</tr/concepts/usage-tracking>).

## İlgili

  * [Eğik çizgi komutları](</tr/tools/slash-commands>)
  * [Yapılandırma](</tr/gateway/configuration>)
  * [Ortam](</tr/help/environment>)


Was this useful?YesNo