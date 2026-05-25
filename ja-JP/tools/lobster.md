---
title: ロブスター
source_url: https://docs.openclaw.ai/ja-JP/tools/lobster
scraped_at: 2026-05-25
---

Lobster は、OpenClaw が複数ステップのツールシーケンスを、明示的な承認チェックポイント付きの単一で決定的な操作として実行できるようにするワークフローシェルです。

Lobster は、切り離されたバックグラウンド作業の一段上にあるオーサリングレイヤーです。個別タスクを超えるフローオーケストレーションについては、[タスクフロー](</ja-JP/automation/taskflow>)（`openclaw tasks flow`）を参照してください。タスクアクティビティ台帳については、[`openclaw tasks`](</ja-JP/automation/tasks>) を参照してください。

## フック

アシスタントは、それ自体を管理するツールを構築できます。ワークフローを依頼すると、30 分後には、1 回の呼び出しで実行される CLI とパイプラインが手に入ります。Lobster は欠けていた要素です。決定的なパイプライン、明示的な承認、再開可能な状態を提供します。

## 理由

現在、複雑なワークフローには多数の往復ツール呼び出しが必要です。各呼び出しはトークンを消費し、LLM はすべてのステップをオーケストレーションする必要があります。Lobster はそのオーケストレーションを型付きランタイムに移します。

  * **多数ではなく 1 回の呼び出し** : OpenClaw は 1 回の Lobster ツール呼び出しを実行し、構造化された結果を取得します。
  * **承認が組み込み済み** : 副作用（メール送信、コメント投稿）は、明示的に承認されるまでワークフローを停止します。
  * **再開可能** : 停止したワークフローはトークンを返します。すべてを再実行せずに承認して再開できます。


## プレーンなプログラムではなく DSL を使う理由

Lobster は意図的に小さく作られています。目標は「新しい言語」ではなく、ファーストクラスの承認と再開トークンを備えた、予測可能で AI に扱いやすいパイプライン仕様です。

  * **承認/再開が組み込み済み** : 通常のプログラムは人間に確認できますが、独自にランタイムを作らない限り、永続的なトークンで _一時停止して再開_ することはできません。
  * **決定性 + 監査可能性** : パイプラインはデータなので、ログ記録、差分確認、再生、レビューが簡単です。
  * **AI 向けの制約されたサーフェス** : 小さな文法 + JSON パイプにより、「創造的な」コードパスを減らし、現実的な検証を可能にします。
  * **安全ポリシーが組み込み済み** : タイムアウト、出力上限、サンドボックスチェック、許可リストは、各スクリプトではなくランタイムによって強制されます。
  * **それでもプログラム可能** : 各ステップは任意の CLI やスクリプトを呼び出せます。JS/TS が必要な場合は、コードから `.lobster` ファイルを生成してください。


## 仕組み

OpenClaw は、埋め込みランナーを使用して Lobster ワークフローを **プロセス内** で実行します。外部 CLI サブプロセスは起動されません。ワークフローエンジンは Gateway プロセス内で実行され、JSON エンベロープを直接返します。 パイプラインが承認のために一時停止した場合、ツールは後で続行できるように `resumeToken` を返します。

## パターン: 小さな CLI + JSON パイプ + 承認

JSON を話す小さなコマンドを作り、それらを 1 回の Lobster 呼び出しにつなぎます。（以下のコマンド名は例です。自分のものに差し替えてください。）

bashCopy code
[code]
    inbox list --jsoninbox categorize --jsoninbox apply --json
[/code]

jsonCopy code
[code]
    {  "action": "run",  "pipeline": "exec --json --shell 'inbox list --json' | exec --stdin json --shell 'inbox categorize --json' | exec --stdin json --shell 'inbox apply --json' | approve --preview-from-stdin --limit 5 --prompt 'Apply changes?'",  "timeoutMs": 30000}
[/code]

パイプラインが承認を要求した場合、トークンで再開します。

jsonCopy code
[code]
    {  "action": "resume",  "token": "<resumeToken>",  "approve": true}
[/code]

AI がワークフローをトリガーし、Lobster がステップを実行します。承認ゲートにより、副作用は明示的かつ監査可能に保たれます。

例: 入力項目をツール呼び出しにマッピングします。

bashCopy code
[code]
    gog.gmail.search --query 'newer_than:1d' \  | openclaw.invoke --tool message --action send --each --item-key message --args-json '{"provider":"telegram","to":"..."}'
[/code]

## JSON 専用 LLM ステップ（llm-task）

**構造化された LLM ステップ** が必要なワークフローでは、任意の `llm-task` Plugin ツールを有効にし、Lobster から呼び出します。これにより、モデルで分類、要約、下書きを行いながらも、ワークフローを 決定的に保てます。

ツールを有効にします。

jsonCopy code
[code]
    {  "plugins": {    "entries": {      "llm-task": { "enabled": true }    }  },  "agents": {    "list": [      {        "id": "main",        "tools": { "alsoAllow": ["llm-task"] }      }    ]  }}
[/code]

### 重要な制限: 埋め込み Lobster と `openclaw.invoke`

同梱の Lobster Plugin は、Gateway 内でワークフローを **プロセス内** 実行します。この埋め込みモードでは、`openclaw.invoke` はネストされた OpenClaw CLI ツール呼び出し用の Gateway URL/認証コンテキストを自動的には継承しません。

つまり、このパターンは **現在、埋め込みランナーでは信頼できません** 。

lobsterCopy code
[code]
    openclaw.invoke --tool llm-task --action json --args-json '{ ... }'
[/code]

以下の例は、`openclaw.invoke` が正しい Gateway/認証コンテキストで既に構成されている環境で **スタンドアロン Lobster CLI** を実行する場合にのみ使用してください。

スタンドアロン Lobster CLI パイプラインで使用します。

lobsterCopy code
[code]
    openclaw.invoke --tool llm-task --action json --args-json '{  "prompt": "Given the input email, return intent and draft.",  "thinking": "low",  "input": { "subject": "Hello", "body": "Can you help?" },  "schema": {    "type": "object",    "properties": {      "intent": { "type": "string" },      "draft": { "type": "string" }    },    "required": ["intent", "draft"],    "additionalProperties": false  }}'
[/code]

現在、埋め込み Lobster Plugin を使用している場合は、次のいずれかを推奨します。

  * Lobster の外で直接 `llm-task` ツールを呼び出す、または
  * サポートされた埋め込みブリッジが追加されるまで、Lobster パイプライン内では非 `openclaw.invoke` ステップを使用する。


詳細と構成オプションについては、[LLM タスク](</ja-JP/tools/llm-task>)を参照してください。

## ワークフローファイル（.lobster）

Lobster は、`name`、`args`、`steps`、`env`、`condition`、`approval` フィールドを持つ YAML/JSON ワークフローファイルを実行できます。OpenClaw ツール呼び出しでは、`pipeline` をファイルパスに設定します。

yamlCopy code
[code]
    name: inbox-triageargs:  tag:    default: "family"steps:  - id: collect    command: inbox list --json  - id: categorize    command: inbox categorize --json    stdin: $collect.stdout  - id: approve    command: inbox apply --approve    stdin: $categorize.stdout    approval: required  - id: execute    command: inbox apply --execute    stdin: $categorize.stdout    condition: $approve.approved
[/code]

注:

  * `stdin: $step.stdout` と `stdin: $step.json` は、前のステップの出力を渡します。
  * `condition`（または `when`）は、`$step.approved` に基づいてステップをゲートできます。


## Lobster をインストールする

同梱の Lobster ワークフローはプロセス内で実行されるため、別個の `lobster` バイナリは不要です。埋め込みランナーは Lobster Plugin に同梱されています。

開発や外部パイプライン用にスタンドアロン Lobster CLI が必要な場合は、[Lobster リポジトリ](<https://github.com/openclaw/lobster>)からインストールし、`lobster` が `PATH` 上にあることを確認してください。

## ツールを有効にする

Lobster は **任意** の Plugin ツールです（デフォルトでは有効ではありません）。

推奨（追加的で安全）:

jsonCopy code
[code]
    {  "tools": {    "alsoAllow": ["lobster"]  }}
[/code]

またはエージェントごとに設定します。

jsonCopy code
[code]
    {  "agents": {    "list": [      {        "id": "main",        "tools": {          "alsoAllow": ["lobster"]        }      }    ]  }}
[/code]

制限的な許可リストモードで実行する意図がない限り、`tools.allow: ["lobster"]` の使用は避けてください。

## 例: メールトリアージ

Lobster なし:

CodeCopy code
[code]
    User: "Check my email and draft replies"→ openclaw calls gmail.list→ LLM summarizes→ User: "draft replies to #2 and #5"→ LLM drafts→ User: "send #2"→ openclaw calls gmail.send(repeat daily, no memory of what was triaged)
[/code]

Lobster あり:

jsonCopy code
[code]
    {  "action": "run",  "pipeline": "email.triage --limit 20",  "timeoutMs": 30000}
[/code]

JSON エンベロープを返します（省略あり）。

jsonCopy code
[code]
    {  "ok": true,  "status": "needs_approval",  "output": [{ "summary": "5 need replies, 2 need action" }],  "requiresApproval": {    "type": "approval_request",    "prompt": "Send 2 draft replies?",    "items": [],    "resumeToken": "..."  }}
[/code]

ユーザーが承認 → 再開:

jsonCopy code
[code]
    {  "action": "resume",  "token": "<resumeToken>",  "approve": true}
[/code]

1 つのワークフロー。決定的。安全。

## ツールパラメータ

### `run`

ツールモードでパイプラインを実行します。

jsonCopy code
[code]
    {  "action": "run",  "pipeline": "gog.gmail.search --query 'newer_than:1d' | email.triage",  "cwd": "workspace",  "timeoutMs": 30000,  "maxStdoutBytes": 512000}
[/code]

引数付きでワークフローファイルを実行します。

jsonCopy code
[code]
    {  "action": "run",  "pipeline": "/path/to/inbox-triage.lobster",  "argsJson": "{\"tag\":\"family\"}"}
[/code]

### `resume`

承認後に停止したワークフローを続行します。

jsonCopy code
[code]
    {  "action": "resume",  "token": "<resumeToken>",  "approve": true}
[/code]

### 任意の入力

  * `cwd`: パイプラインの相対作業ディレクトリ（Gateway の作業ディレクトリ内に収まる必要があります）。
  * `timeoutMs`: この期間を超えた場合にワークフローを中止します（デフォルト: 20000）。
  * `maxStdoutBytes`: 出力がこのサイズを超えた場合にワークフローを中止します（デフォルト: 512000）。
  * `argsJson`: `lobster run --args-json` に渡される JSON 文字列（ワークフローファイルのみ）。


## 出力エンベロープ

Lobster は、次の 3 つのステータスのいずれかを持つ JSON エンベロープを返します。

  * `ok` → 正常に完了
  * `needs_approval` → 一時停止中。再開には `requiresApproval.resumeToken` が必要
  * `cancelled` → 明示的に拒否またはキャンセル済み


ツールは、エンベロープを `content`（整形済み JSON）と `details`（未加工オブジェクト）の両方で公開します。

## 承認

`requiresApproval` が存在する場合は、プロンプトを確認して判断します。

  * `approve: true` → 再開して副作用を続行
  * `approve: false` → キャンセルしてワークフローを完了


カスタム jq/heredoc 接着コードなしで承認リクエストに JSON プレビューを添付するには、`approve --preview-from-stdin --limit N` を使用します。再開トークンは現在コンパクトです。Lobster はワークフローの再開状態を状態ディレクトリに保存し、小さなトークンキーを返します。

## OpenProse

OpenProse は Lobster と相性がよいです。`/prose` を使用してマルチエージェントの準備をオーケストレーションし、その後、決定的な承認のために Lobster パイプラインを実行します。Prose プログラムが Lobster を必要とする場合は、`tools.subagents.tools` を介してサブエージェントに `lobster` ツールを許可してください。[OpenProse](</ja-JP/prose>) を参照してください。

## 安全性

  * **ローカルのプロセス内のみ** \- ワークフローは Gateway プロセス内で実行されます。Plugin 自体からのネットワーク呼び出しはありません。
  * **シークレットなし** \- Lobster は OAuth を管理しません。それを行う OpenClaw ツールを呼び出します。
  * **サンドボックス対応** \- ツールコンテキストがサンドボックス化されている場合は無効になります。
  * **強化済み** \- タイムアウトと出力上限は埋め込みランナーによって強制されます。


## トラブルシューティング

  * **`lobster timed out`** → `timeoutMs` を増やすか、長いパイプラインを分割します。
  * **`lobster output exceeded maxStdoutBytes`** → `maxStdoutBytes` を上げるか、出力サイズを減らします。
  * **`lobster returned invalid JSON`** → パイプラインがツールモードで実行され、JSON のみを出力していることを確認します。
  * **`lobster failed`** → 埋め込みランナーのエラー詳細について Gateway ログを確認します。


## さらに学ぶ

  * [Plugins](</ja-JP/tools/plugin>)
  * [Plugin ツールのオーサリング](</ja-JP/plugins/building-plugins#registering-agent-tools>)


## ケーススタディ: コミュニティワークフロー

公開例の 1 つに、3 つの Markdown 保管庫（個人、パートナー、共有）を管理する「second brain」CLI + Lobster パイプラインがあります。この CLI は、統計、受信箱一覧、古くなった項目のスキャンを JSON として出力します。Lobster はそれらのコマンドを `weekly-review`、`inbox-triage`、`memory-consolidation`、`shared-task-sync` などのワークフローに連結し、それぞれに承認ゲートを設けます。AI は利用可能な場合に判断（分類）を処理し、利用できない場合は決定的なルールにフォールバックします。

  * スレッド: <https://x.com/plattenschieber/status/2014508656335770033>
  * リポジトリ: <https://github.com/bloomedai/brain-cli>


## 関連

  * [自動化](</ja-JP/automation>) \- Lobster ワークフローのスケジューリング
  * [自動化の概要](</ja-JP/automation>) \- すべての自動化メカニズム
  * [ツール概要](</ja-JP/tools>) \- 利用可能なすべてのエージェントツール


Was this useful?YesNo