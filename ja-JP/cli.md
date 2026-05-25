---
title: CLI リファレンス
source_url: https://docs.openclaw.ai/ja-JP/cli
scraped_at: 2026-05-25
---

`openclaw` はメインの CLI エントリポイントです。各コアコマンドには 専用のリファレンスページがあるか、そのエイリアス先のコマンドと一緒に文書化されています。この インデックスには、CLI 全体に適用されるコマンド、グローバルフラグ、出力スタイル規則を 一覧しています。

意図に応じてセットアップコマンドを使います。

  * `openclaw setup` は、完全なガイド付きオンボーディングフローを進めずに、ベースライン設定とワークスペースを作成します。
  * `openclaw onboard` は、Gateway、モデル認証、ワークスペース、チャネル、Skills、健全性に対応する、初回実行向けの完全なガイド付きパスです。
  * `openclaw configure` は、モデル認証、Gateway、チャネル、プラグイン、Skills など、既存セットアップの対象部分を変更します。
  * `openclaw channels add` は、ベースラインが存在した後にチャネルアカウントを設定します。ガイド付きチャネルセットアップにはフラグなしで実行し、スクリプトにはチャネル固有のフラグを指定して実行します。


## コマンドページ

領域 | コマンド  
---|---  
セットアップとオンボーディング | [`crestodian`](</ja-JP/cli/crestodian>) · [`setup`](</ja-JP/cli/setup>) · [`onboard`](</ja-JP/cli/onboard>) · [`configure`](</ja-JP/cli/configure>) · [`config`](</ja-JP/cli/config>) · [`completion`](</ja-JP/cli/completion>) · [`doctor`](</ja-JP/cli/doctor>) · [`dashboard`](</ja-JP/cli/dashboard>)  
リセットとアンインストール | [`backup`](</ja-JP/cli/backup>) · [`reset`](</ja-JP/cli/reset>) · [`uninstall`](</ja-JP/cli/uninstall>) · [`update`](</ja-JP/cli/update>)  
メッセージングとエージェント | [`message`](</ja-JP/cli/message>) · [`agent`](</ja-JP/cli/agent>) · [`agents`](</ja-JP/cli/agents>) · [`acp`](</ja-JP/cli/acp>) · [`mcp`](</ja-JP/cli/mcp>)  
健全性とセッション | [`status`](</ja-JP/cli/status>) · [`health`](</ja-JP/cli/health>) · [`sessions`](</ja-JP/cli/sessions>)  
Gateway とログ | [`gateway`](</ja-JP/cli/gateway>) · [`logs`](</ja-JP/cli/logs>) · [`system`](</ja-JP/cli/system>)  
モデルと推論 | [`models`](</ja-JP/cli/models>) · [`infer`](</ja-JP/cli/infer>) · `capability`（[`infer`](</ja-JP/cli/infer>) のエイリアス） · [`memory`](</ja-JP/cli/memory>) · [`commitments`](</ja-JP/cli/commitments>) · [`wiki`](</ja-JP/cli/wiki>)  
ネットワークとノード | [`directory`](</ja-JP/cli/directory>) · [`nodes`](</ja-JP/cli/nodes>) · [`devices`](</ja-JP/cli/devices>) · [`node`](</ja-JP/cli/node>)  
ランタイムとサンドボックス | [`approvals`](</ja-JP/cli/approvals>) · `exec-policy`（[`approvals`](</ja-JP/cli/approvals>) を参照） · [`sandbox`](</ja-JP/cli/sandbox>) · [`tui`](</ja-JP/cli/tui>) · `chat`/`terminal`（[`tui --local`](</ja-JP/cli/tui>) のエイリアス） · [`browser`](</ja-JP/cli/browser>)  
自動化 | [`cron`](</ja-JP/cli/cron>) · [`tasks`](</ja-JP/cli/tasks>) · [`hooks`](</ja-JP/cli/hooks>) · [`webhooks`](</ja-JP/cli/webhooks>)  
検出とドキュメント | [`dns`](</ja-JP/cli/dns>) · [`docs`](</ja-JP/cli/docs>)  
ペアリングとチャネル | [`pairing`](</ja-JP/cli/pairing>) · [`qr`](</ja-JP/cli/qr>) · [`channels`](</ja-JP/cli/channels>)  
セキュリティとプラグイン | [`security`](</ja-JP/cli/security>) · [`secrets`](</ja-JP/cli/secrets>) · [`skills`](</ja-JP/cli/skills>) · [`plugins`](</ja-JP/cli/plugins>) · [`proxy`](</ja-JP/cli/proxy>)  
レガシーエイリアス | [`daemon`](</ja-JP/cli/daemon>)（Gateway サービス） · [`clawbot`](</ja-JP/cli/clawbot>)（名前空間）  
プラグイン（任意） | [`path`](</ja-JP/cli/path>) · [`voicecall`](</ja-JP/cli/voicecall>)（インストールされている場合）  
  
## グローバルフラグ

フラグ | 目的  
---|---  
`--dev` | 状態を `~/.openclaw-dev` 配下に分離し、デフォルトポートをずらす  
`--profile <name>` | 状態を `~/.openclaw-<name>` 配下に分離する  
`--container <name>` | 実行対象の名前付きコンテナを指定する  
`--no-color` | ANSI カラーを無効化する（`NO_COLOR=1` も尊重されます）  
`--update` | [`openclaw update`](</ja-JP/cli/update>) の短縮形（ソースインストールのみ）  
`-V`, `--version`, `-v` | バージョンを表示して終了する  
  
## 出力モード

  * ANSI カラーと進行状況インジケーターは TTY セッションでのみ描画されます。
  * OSC-8 ハイパーリンクは、サポートされている場所ではクリック可能なリンクとして描画されます。そうでない場合、 CLI はプレーンな URL にフォールバックします。
  * `--json`（およびサポートされる場合は `--plain`）は、クリーンな出力のためにスタイルを無効化します。
  * 長時間実行されるコマンドは進行状況インジケーターを表示します（サポートされる場合は OSC 9;4）。


パレットの信頼できる情報源: `src/terminal/palette.ts`。

## コマンドツリー

完全なコマンドツリー CodeCopy code
[code]
    openclaw [--dev] [--profile <name>] <command>crestodiansetuponboardconfigureconfig  get  set  unset  file  schema  validatecompletiondoctordashboardbackup  create  verifysecurity  auditsecrets  reload  audit  configure  applyresetuninstallupdate  wizard  statuschannels  list  status  capabilities  resolve  logs  add  remove  login  logoutdirectory  self  peers list  groups list|membersskills  search  install  update  list  info  checkplugins  list  inspect  install  uninstall  update  enable  disable  doctor  marketplace listmemory  status  index  searchpath  resolve  find  set  validate  emitcommitments  list  dismisswiki  status  doctor  init  ingest  compile  lint  search  get  apply  bridge import  unsafe-local import  obsidian status|search|open|command|dailymessage  send  broadcast  poll  react  reactions  read  edit  delete  pin  unpin  pins  permissions  search  thread create|list|reply  emoji list|upload  sticker send|upload  role info|add|remove  channel info|list  member info  voice status  event list|create  timeout  kick  banagentagents  list  add  delete  bindings  bind  unbind  set-identityacpmcp  serve  list  show  set  unsetstatushealthsessions  cleanuptasks  list  audit  maintenance  show  notify  cancel  flow list|show|cancelgateway  call  usage-cost  health  status  probe  discover  install  uninstall  start  stop  restart  rundaemon  status  install  uninstall  start  stop  restartlogssystem  event  heartbeat last|enable|disable  presencemodels  list  status  set  set-image  aliases list|add|remove  fallbacks list|add|remove|clear  image-fallbacks list|add|remove|clear  scaninfer (alias: capability)  list  inspect  model run|list|inspect|providers|auth login|logout|status  image generate|edit|describe|describe-many|providers  audio transcribe|providers  tts convert|voices|providers|status|enable|disable|set-provider  video generate|describe|providers  web search|fetch|providers  embedding create|providers  auth add|login|login-github-copilot|setup-token|paste-token  auth order get|set|clearsandbox  list  recreate  explaincron  status  list  get  add  edit  rm  enable  disable  runs  runnodes  status  describe  list  pending  approve  reject  rename  invoke  notify  push  canvas snapshot|present|hide|navigate|eval  canvas a2ui push|reset  camera list|snap|clip  screen record  location getdevices  list  remove  clear  approve  reject  rotate  revokenode  run  status  install  uninstall  stop  restartapprovals  get  set  allowlist add|removeexec-policy  show  preset  setbrowser  status  start  stop  reset-profile  tabs  open  focus  close  profiles  create-profile  delete-profile  screenshot  snapshot  navigate  resize  click  type  press  hover  drag  select  upload  fill  dialog  wait  evaluate  console  pdfhooks  list  info  check  enable  disable  install  updatewebhooks  gmail setup|runproxy  start  run  coverage  sessions  query  blob  purgepairing  list  approveqrclawbot  qrdocsdns  setuptuichat (alias: tui --local)terminal (alias: tui --local)
[/code]

プラグインは追加のトップレベルコマンドを追加できます（例: `openclaw voicecall`）。

## チャットのスラッシュコマンド

チャットメッセージは `/...` コマンドをサポートします。[スラッシュコマンド](</ja-JP/tools/slash-commands>)を参照してください。

ハイライト:

  * `/status` — 簡易診断。
  * `/trace` — セッションスコープのプラグインのトレース/デバッグ行。
  * `/config` — 永続化される設定変更。
  * `/debug` — ランタイム限定の設定上書き（メモリ、ディスクではありません。`commands.debug: true` が必要です）。


## 使用量トラッキング

`openclaw status --usage` と Control UI は、OAuth/API 認証情報が利用可能な場合に プロバイダーの使用量/クォータを表示します。データはプロバイダーの使用量 エンドポイントから直接取得され、`X% left` に正規化されます。現在の使用量 ウィンドウを持つプロバイダー: Anthropic、GitHub Copilot、Gemini CLI、OpenAI Codex、MiniMax、 Xiaomi、[z.ai](<http://z.ai>)。

詳細は[使用量トラッキング](</ja-JP/concepts/usage-tracking>)を参照してください。

## 関連

  * [スラッシュコマンド](</ja-JP/tools/slash-commands>)
  * [設定](</ja-JP/gateway/configuration>)
  * [環境](</ja-JP/help/environment>)


Was this useful?YesNo