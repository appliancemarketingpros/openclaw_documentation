---
title: Referensi CLI
source_url: https://docs.openclaw.ai/id/cli
scraped_at: 2026-05-25
---

`openclaw` adalah titik masuk CLI utama. Setiap perintah inti memiliki halaman referensi khusus atau didokumentasikan bersama perintah yang menjadi aliasnya; indeks ini mencantumkan perintah, flag global, dan aturan gaya output yang berlaku di seluruh CLI.

Gunakan perintah penyiapan sesuai tujuan:

  * `openclaw setup` membuat konfigurasi dasar dan workspace tanpa menjalankan alur onboarding terpandu penuh.
  * `openclaw onboard` adalah jalur first-run terpandu penuh untuk gateway, auth model, workspace, kanal, Skills, dan kesehatan.
  * `openclaw configure` mengubah bagian tertentu dari penyiapan yang sudah ada, seperti auth model, gateway, kanal, Plugin, atau Skills.
  * `openclaw channels add` mengonfigurasi akun kanal setelah dasar tersedia; jalankan tanpa flag untuk penyiapan kanal terpandu atau dengan flag khusus kanal untuk skrip.


## Halaman perintah

Area | Perintah  
---|---  
Penyiapan dan onboarding | [`crestodian`](</id/cli/crestodian>) · [`setup`](</id/cli/setup>) · [`onboard`](</id/cli/onboard>) · [`configure`](</id/cli/configure>) · [`config`](</id/cli/config>) · [`completion`](</id/cli/completion>) · [`doctor`](</id/cli/doctor>) · [`dashboard`](</id/cli/dashboard>)  
Reset dan uninstall | [`backup`](</id/cli/backup>) · [`reset`](</id/cli/reset>) · [`uninstall`](</id/cli/uninstall>) · [`update`](</id/cli/update>)  
Perpesanan dan agen | [`message`](</id/cli/message>) · [`agent`](</id/cli/agent>) · [`agents`](</id/cli/agents>) · [`acp`](</id/cli/acp>) · [`mcp`](</id/cli/mcp>)  
Kesehatan dan sesi | [`status`](</id/cli/status>) · [`health`](</id/cli/health>) · [`sessions`](</id/cli/sessions>)  
Gateway dan log | [`gateway`](</id/cli/gateway>) · [`logs`](</id/cli/logs>) · [`system`](</id/cli/system>)  
Model dan inferensi | [`models`](</id/cli/models>) · [`infer`](</id/cli/infer>) · `capability` (alias untuk [`infer`](</id/cli/infer>)) · [`memory`](</id/cli/memory>) · [`commitments`](</id/cli/commitments>) · [`wiki`](</id/cli/wiki>)  
Jaringan dan Node | [`directory`](</id/cli/directory>) · [`nodes`](</id/cli/nodes>) · [`devices`](</id/cli/devices>) · [`node`](</id/cli/node>)  
Runtime dan sandbox | [`approvals`](</id/cli/approvals>) · `exec-policy` (lihat [`approvals`](</id/cli/approvals>)) · [`sandbox`](</id/cli/sandbox>) · [`tui`](</id/cli/tui>) · `chat`/`terminal` (alias untuk [`tui --local`](</id/cli/tui>)) · [`browser`](</id/cli/browser>)  
Otomasi | [`cron`](</id/cli/cron>) · [`tasks`](</id/cli/tasks>) · [`hooks`](</id/cli/hooks>) · [`webhooks`](</id/cli/webhooks>)  
Discovery dan dokumen | [`dns`](</id/cli/dns>) · [`docs`](</id/cli/docs>)  
Pairing dan kanal | [`pairing`](</id/cli/pairing>) · [`qr`](</id/cli/qr>) · [`channels`](</id/cli/channels>)  
Keamanan dan Plugin | [`security`](</id/cli/security>) · [`secrets`](</id/cli/secrets>) · [`skills`](</id/cli/skills>) · [`plugins`](</id/cli/plugins>) · [`proxy`](</id/cli/proxy>)  
Alias lama | [`daemon`](</id/cli/daemon>) (layanan gateway) · [`clawbot`](</id/cli/clawbot>) (namespace)  
Plugin (opsional) | [`path`](</id/cli/path>) · [`voicecall`](</id/cli/voicecall>) (jika terinstal)  
  
## Flag global

Flag | Tujuan  
---|---  
`--dev` | Mengisolasi state di bawah `~/.openclaw-dev` dan menggeser port default  
`--profile <name>` | Mengisolasi state di bawah `~/.openclaw-<name>`  
`--container <name>` | Menargetkan container bernama untuk eksekusi  
`--no-color` | Menonaktifkan warna ANSI (`NO_COLOR=1` juga dihormati)  
`--update` | Singkatan untuk [`openclaw update`](</id/cli/update>) (hanya instalasi dari sumber)  
`-V`, `--version`, `-v` | Mencetak versi dan keluar  
  
## Mode output

  * Warna ANSI dan indikator progres hanya dirender dalam sesi TTY.
  * Hyperlink OSC-8 dirender sebagai tautan yang dapat diklik jika didukung; jika tidak, CLI menggunakan URL polos.
  * `--json` (dan `--plain` jika didukung) menonaktifkan gaya untuk output bersih.
  * Perintah yang berjalan lama menampilkan indikator progres (OSC 9;4 jika didukung).


Sumber kebenaran palet: `src/terminal/palette.ts`.

## Pohon perintah

Pohon perintah lengkap CodeCopy code
[code]
    openclaw [--dev] [--profile <name>] <command>crestodiansetuponboardconfigureconfig  get  set  unset  file  schema  validatecompletiondoctordashboardbackup  create  verifysecurity  auditsecrets  reload  audit  configure  applyresetuninstallupdate  wizard  statuschannels  list  status  capabilities  resolve  logs  add  remove  login  logoutdirectory  self  peers list  groups list|membersskills  search  install  update  list  info  checkplugins  list  inspect  install  uninstall  update  enable  disable  doctor  marketplace listmemory  status  index  searchpath  resolve  find  set  validate  emitcommitments  list  dismisswiki  status  doctor  init  ingest  compile  lint  search  get  apply  bridge import  unsafe-local import  obsidian status|search|open|command|dailymessage  send  broadcast  poll  react  reactions  read  edit  delete  pin  unpin  pins  permissions  search  thread create|list|reply  emoji list|upload  sticker send|upload  role info|add|remove  channel info|list  member info  voice status  event list|create  timeout  kick  banagentagents  list  add  delete  bindings  bind  unbind  set-identityacpmcp  serve  list  show  set  unsetstatushealthsessions  cleanuptasks  list  audit  maintenance  show  notify  cancel  flow list|show|cancelgateway  call  usage-cost  health  status  probe  discover  install  uninstall  start  stop  restart  rundaemon  status  install  uninstall  start  stop  restartlogssystem  event  heartbeat last|enable|disable  presencemodels  list  status  set  set-image  aliases list|add|remove  fallbacks list|add|remove|clear  image-fallbacks list|add|remove|clear  scaninfer (alias: capability)  list  inspect  model run|list|inspect|providers|auth login|logout|status  image generate|edit|describe|describe-many|providers  audio transcribe|providers  tts convert|voices|providers|status|enable|disable|set-provider  video generate|describe|providers  web search|fetch|providers  embedding create|providers  auth add|login|login-github-copilot|setup-token|paste-token  auth order get|set|clearsandbox  list  recreate  explaincron  status  list  get  add  edit  rm  enable  disable  runs  runnodes  status  describe  list  pending  approve  reject  rename  invoke  notify  push  canvas snapshot|present|hide|navigate|eval  canvas a2ui push|reset  camera list|snap|clip  screen record  location getdevices  list  remove  clear  approve  reject  rotate  revokenode  run  status  install  uninstall  stop  restartapprovals  get  set  allowlist add|removeexec-policy  show  preset  setbrowser  status  start  stop  reset-profile  tabs  open  focus  close  profiles  create-profile  delete-profile  screenshot  snapshot  navigate  resize  click  type  press  hover  drag  select  upload  fill  dialog  wait  evaluate  console  pdfhooks  list  info  check  enable  disable  install  updatewebhooks  gmail setup|runproxy  start  run  coverage  sessions  query  blob  purgepairing  list  approveqrclawbot  qrdocsdns  setuptuichat (alias: tui --local)terminal (alias: tui --local)
[/code]

Plugin dapat menambahkan perintah tingkat atas tambahan (misalnya `openclaw voicecall`).

## Perintah slash chat

Pesan chat mendukung perintah `/...`. Lihat [perintah slash](</id/tools/slash-commands>).

Sorotan:

  * `/status` — diagnostik cepat.
  * `/trace` — baris trace/debug Plugin dalam cakupan sesi.
  * `/config` — perubahan konfigurasi persisten.
  * `/debug` — override konfigurasi hanya runtime (memori, bukan disk; memerlukan `commands.debug: true`).


## Pelacakan penggunaan

`openclaw status --usage` dan Control UI menampilkan penggunaan/kuota penyedia saat kredensial OAuth/API tersedia. Data berasal langsung dari endpoint penggunaan penyedia dan dinormalisasi menjadi `X% left`. Penyedia dengan jendela penggunaan saat ini: Anthropic, GitHub Copilot, Gemini CLI, OpenAI Codex, MiniMax, Xiaomi, dan [z.ai](<http://z.ai>).

Lihat [Pelacakan penggunaan](</id/concepts/usage-tracking>) untuk detail.

## Terkait

  * [Perintah slash](</id/tools/slash-commands>)
  * [Konfigurasi](</id/gateway/configuration>)
  * [Lingkungan](</id/help/environment>)


Was this useful?YesNo