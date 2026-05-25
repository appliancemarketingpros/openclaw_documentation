---
title: Crestodian
source_url: https://docs.openclaw.ai/ja-JP/cli/crestodian
scraped_at: 2026-05-25
---

# `openclaw crestodian`

Crestodian は OpenClaw のローカルセットアップ、修復、設定ヘルパーです。通常のエージェント経路が壊れている場合でも到達可能であり続けるように設計されています。

コマンドなしで `openclaw` を実行すると、対話型ターミナルで Crestodian が起動します。 `openclaw crestodian` を実行すると、同じヘルパーを明示的に起動します。

## Crestodian が表示する内容

起動時、対話型 Crestodian は `openclaw tui` と同じ TUI シェルを、Crestodian チャットバックエンドで開きます。チャットログは短い挨拶で始まります。

  * Crestodian を起動するタイミング
  * Crestodian が実際に使用しているモデルまたは決定的プランナー経路
  * 設定の有効性とデフォルトエージェント
  * 最初の起動プローブから見た Gateway 到達性
  * Crestodian が実行できる次のデバッグ操作


起動するためだけにシークレットをダンプしたり、Plugin CLI コマンドを読み込んだりはしません。TUI は引き続き通常のヘッダー、チャットログ、ステータス行、フッター、オートコンプリート、エディター操作を提供します。

設定パス、docs/source パス、ローカル CLI プローブ、API キーの有無、エージェント、モデル、Gateway の詳細を含む詳細なインベントリには `status` を使用します。

Crestodian は通常のエージェントと同じ OpenClaw リファレンス検出を使用します。Git チェックアウトでは、ローカルの `docs/` とローカルソースツリーを参照します。npm パッケージインストールでは、同梱されたパッケージドキュメントを使用し、<https://github.com/openclaw/openclaw> にリンクします。また、ドキュメントだけでは不十分な場合はソースを確認するよう明示的に案内します。

## 例

bashCopy code
[code]
    openclawopenclaw crestodianopenclaw crestodian --jsonopenclaw crestodian --message "models"openclaw crestodian --message "validate config"openclaw crestodian --message "setup workspace ~/Projects/work model openai/gpt-5.5" --yesopenclaw crestodian --message "set default model openai/gpt-5.5" --yesopenclaw onboard --modern
[/code]

Crestodian TUI 内では次のように使用します。

textCopy code
[code]
    statushealthdoctordoctor fixvalidate configsetupsetup workspace ~/Projects/work model openai/gpt-5.5config set gateway.port 19001config set-ref gateway.auth.token env OPENCLAW_GATEWAY_TOKENgateway statusrestart gatewayagentscreate agent work workspace ~/Projects/workmodelsset default model openai/gpt-5.5plugins listplugins search slackplugin install clawhub:openclaw-codex-app-serverplugin uninstall openclaw-codex-app-servertalk to work agenttalk to agent for ~/Projects/workauditquit
[/code]

## 安全な起動

Crestodian の起動経路は意図的に小さく保たれています。次の場合でも実行できます。

  * `openclaw.json` が存在しない
  * `openclaw.json` が無効
  * Gateway が停止している
  * Plugin コマンド登録が利用できない
  * まだエージェントが設定されていない


`openclaw --help` と `openclaw --version` は引き続き通常の高速経路を使用します。 非対話型の `openclaw` はルートヘルプを表示する代わりに短いメッセージで終了します。これは、コマンドなしのプロダクトが Crestodian だからです。

## 操作と承認

Crestodian は設定を場当たり的に編集するのではなく、型付き操作を使用します。

読み取り専用操作は即座に実行できます。

  * 概要を表示する
  * エージェントを一覧表示する
  * インストール済み Plugin を一覧表示する
  * ClawHub Plugin を検索する
  * モデル/バックエンドのステータスを表示する
  * ステータスまたはヘルスチェックを実行する
  * Gateway 到達性を確認する
  * 対話型修正なしで doctor を実行する
  * 設定を検証する
  * 監査ログパスを表示する


永続的な操作は、直接コマンドに `--yes` を渡さない限り、対話モードで会話による承認が必要です。

  * 設定を書き込む
  * `config set` を実行する
  * `config set-ref` を通じてサポート対象の SecretRef 値を設定する
  * setup/オンボーディングのブートストラップを実行する
  * デフォルトモデルを変更する
  * Gateway を起動、停止、または再起動する
  * エージェントを作成する
  * ClawHub または npm から Plugin をインストールする
  * Plugin をアンインストールする
  * 設定または状態を書き換える doctor 修復を実行する


適用された書き込みは次に記録されます。

textCopy code
[code]
    ~/.openclaw/audit/crestodian.jsonl
[/code]

検出は監査されません。適用された操作と書き込みのみがログに記録されます。

`openclaw onboard --modern` は、モダンなオンボーディングプレビューとして Crestodian を起動します。 通常の `openclaw onboard` は引き続きクラシックオンボーディングを実行します。

## セットアップブートストラップ

`setup` はチャット優先のオンボーディングブートストラップです。型付き設定操作のみを通じて書き込み、先に承認を求めます。

textCopy code
[code]
    setupsetup workspace ~/Projects/worksetup workspace ~/Projects/work model openai/gpt-5.5
[/code]

モデルが設定されていない場合、setup は次の順序で最初に使用可能なバックエンドを選択し、何を選んだかを伝えます。

  * 既存の明示的なモデル（すでに設定済みの場合）
  * `OPENAI_API_KEY` -> `openai/gpt-5.5`
  * `ANTHROPIC_API_KEY` -> `anthropic/claude-opus-4-7`
  * Claude Code CLI -> `claude-cli/claude-opus-4-7`
  * Codex CLI -> `codex-cli/gpt-5.5`


どれも利用できない場合でも、setup はデフォルトワークスペースを書き込み、モデルは未設定のままにします。Codex/Claude Code をインストールまたはログインするか、`OPENAI_API_KEY`/`ANTHROPIC_API_KEY` を公開してから setup を再実行します。

## モデル支援プランナー

Crestodian は常に決定的モードで起動します。決定的パーサーが理解できない曖昧なコマンドに対して、ローカルの Crestodian は OpenClaw の通常のランタイム経路を通じて、境界付けられた 1 回のプランナーターンを実行できます。まず、設定済みの OpenClaw モデルを使用します。使用可能な設定済みモデルがまだない場合は、マシン上にすでに存在するローカルランタイムにフォールバックできます。

  * Claude Code CLI: `claude-cli/claude-opus-4-7`
  * Codex app-server harness: `openai/gpt-5.5`
  * Codex CLI: `codex-cli/gpt-5.5`


モデル支援プランナーは設定を直接変更できません。リクエストを Crestodian の型付きコマンドのいずれかに変換する必要があり、その後は通常の承認および監査ルールが適用されます。Crestodian は何かを実行する前に、使用したモデルと解釈されたコマンドを表示します。設定なしのフォールバックプランナーターンは一時的であり、ランタイムがサポートする場合はツール無効で、一時的なワークスペース/セッションを使用します。

メッセージチャネルレスキューモードはモデル支援プランナーを使用しません。リモートレスキューは決定的なままです。これにより、壊れた、または侵害された通常のエージェント経路が設定エディターとして使われることを防ぎます。

## エージェントへの切り替え

自然言語セレクターを使用して Crestodian を離れ、通常の TUI を開きます。

textCopy code
[code]
    talk to agenttalk to work agentswitch to main agent
[/code]

`openclaw tui`、`openclaw chat`、`openclaw terminal` は引き続き通常のエージェント TUI を直接開きます。Crestodian は起動しません。

通常の TUI に切り替えた後、Crestodian に戻るには `/crestodian` を使用します。後続リクエストを含めることもできます。

textCopy code
[code]
    /crestodian/crestodian restart gateway
[/code]

TUI 内のエージェント切り替えでは、`/crestodian` が利用可能であることを示すパンくずが残ります。

## メッセージレスキューモード

メッセージレスキューモードは、Crestodian のメッセージチャネルエントリーポイントです。通常のエージェントが停止しているが、WhatsApp などの信頼済みチャネルがまだコマンドを受信できる場合に使用します。

サポート対象のテキストコマンド:

  * `/crestodian <request>`


オペレーターフロー:

textCopy code
[code]
    You, in a trusted owner DM: /crestodian statusOpenClaw: Crestodian rescue mode. Gateway reachable: no. Config valid: no.You: /crestodian restart gatewayOpenClaw: Plan: restart the Gateway. Reply /crestodian yes to apply.You: /crestodian yesOpenClaw: Applied. Audit entry written.
[/code]

エージェント作成は、ローカルプロンプトまたはレスキューモードからキューに入れることもできます。

textCopy code
[code]
    create agent work workspace ~/Projects/work model openai/gpt-5.5/crestodian create agent work workspace ~/Projects/work
[/code]

リモートレスキューモードは管理サーフェスです。通常のチャットではなく、リモート設定修復として扱う必要があります。

リモートレスキューのセキュリティ契約:

  * サンドボックス化が有効な場合は無効です。エージェント/セッションがサンドボックス化されている場合、Crestodian はリモートレスキューを拒否し、ローカル CLI 修復が必要であることを説明する必要があります。
  * デフォルトの有効状態は `auto` です。ランタイムがすでにサンドボックス化されていないローカル権限を持つ、信頼済み YOLO 操作でのみリモートレスキューを許可します。
  * 明示的なオーナー ID が必要です。レスキューは、ワイルドカード送信者ルール、オープングループポリシー、未認証 Webhook、匿名チャネルを受け入れてはなりません。
  * デフォルトではオーナー DM のみです。グループ/チャネルレスキューには明示的なオプトインが必要です。
  * Plugin の検索と一覧表示は読み取り専用です。Plugin のインストールは、実行可能コードをダウンロードするため、デフォルトではローカル専用です。Plugin のアンインストールは、レスキューポリシーが永続的な書き込みを許可している場合、承認済み修復操作として許可できます。
  * リモートレスキューはローカル TUI を開いたり、対話型エージェントセッションに切り替えたりできません。エージェントの引き継ぎにはローカルの `openclaw` を使用します。
  * 永続的な書き込みには、レスキューモードでも引き続き承認が必要です。
  * 適用されたすべてのレスキュー操作を監査します。メッセージチャネルレスキューは、チャネル、アカウント、送信者、ソースアドレスメタデータを記録します。設定を変更する操作は、変更前後の設定ハッシュも記録します。
  * シークレットを決してエコーしません。SecretRef の検査では、値ではなく利用可否を報告する必要があります。
  * Gateway が稼働している場合は、Gateway の型付き操作を優先します。Gateway が停止している場合は、通常のエージェントループに依存しない最小限のローカル修復サーフェスのみを使用します。


設定の形:

jsoncCopy code
[code]
    {  "crestodian": {    "rescue": {      "enabled": "auto",      "ownerDmOnly": true,    },  },}
[/code]

`enabled` は次を受け入れる必要があります。

  * `"auto"`: デフォルト。有効なランタイムが YOLO であり、サンドボックス化がオフの場合にのみ許可します。
  * `false`: メッセージチャネルレスキューを一切許可しません。
  * `true`: オーナー/チャネルチェックに合格した場合にレスキューを明示的に許可します。これでも、サンドボックス化による拒否を迂回してはなりません。


デフォルトの `"auto"` YOLO 姿勢は次のとおりです。

  * サンドボックスモードが `off` に解決される
  * `tools.exec.security` が `full` に解決される
  * `tools.exec.ask` が `off` に解決される


リモートレスキューは Docker レーンでカバーされています。

bashCopy code
[code]
    pnpm test:docker:crestodian-rescue
[/code]

設定なしのローカルプランナーフォールバックは次でカバーされています。

bashCopy code
[code]
    pnpm test:docker:crestodian-planner
[/code]

オプトインのライブチャネルコマンドサーフェススモークは、`/crestodian status` に加え、レスキューハンドラーを通じた永続的な承認往復をチェックします。

bashCopy code
[code]
    pnpm test:live:crestodian-rescue-channel
[/code]

Crestodian を通じた新規設定なしセットアップは次でカバーされています。

bashCopy code
[code]
    pnpm test:docker:crestodian-first-run
[/code]

このレーンは空の状態ディレクトリから開始し、裸の `openclaw` を Crestodian にルーティングし、デフォルトモデルを設定し、追加エージェントを作成し、Plugin 有効化とトークン SecretRef を通じて Discord を設定し、設定を検証し、監査ログを確認します。QA Lab には、同じ Ring 0 フローのためのリポジトリ連携シナリオもあります。

bashCopy code
[code]
    pnpm openclaw qa suite --scenario crestodian-ring-zero-setup
[/code]

## 関連

  * [CLI リファレンス](</ja-JP/cli>)
  * [Doctor](</ja-JP/cli/doctor>)
  * [TUI](</ja-JP/cli/tui>)
  * [サンドボックス](</ja-JP/cli/sandbox>)
  * [セキュリティ](</ja-JP/cli/security>)


Was this useful?YesNo