---
title: バックグラウンドタスク
source_url: https://docs.openclaw.ai/ja-JP/automation/tasks
scraped_at: 2026-05-25
---

バックグラウンドタスクは、**メインの会話セッションの外部** で実行される作業を追跡します: ACP 実行、サブエージェントの生成、分離された cron ジョブの実行、CLI から開始された操作です。

タスクは、セッション、cron ジョブ、Heartbeat を置き換えるものではありません。切り離された作業で何が起きたか、いつ起きたか、成功したかどうかを記録する**アクティビティ台帳** です。

## TL;DR

  * タスクはスケジューラーではなく**記録** です。cron と Heartbeat が作業を_いつ_実行するかを決め、タスクは_何が起きたか_を追跡します。
  * ACP、サブエージェント、すべての cron ジョブ、CLI 操作はタスクを作成します。Heartbeat ターンは作成しません。
  * 各タスクは `queued → running → terminal` (succeeded、failed、timed_out、cancelled、または lost) を進みます。
  * Cron タスクは、cron ランタイムがまだジョブを所有している間はライブのままです。 メモリ内のランタイム状態がなくなった場合、タスク保守はタスクを lost としてマークする前に、まず永続化された cron 実行履歴を確認します。
  * 完了はプッシュ駆動です。切り離された作業は完了時に直接通知するか、 リクエスターのセッション/Heartbeat を起こせるため、ステータスのポーリングループは たいてい不適切な形です。
  * 分離された cron 実行とサブエージェント完了は、最終的なクリーンアップ帳簿の前に、子セッションで追跡されているブラウザータブ/プロセスをベストエフォートでクリーンアップします。
  * 分離された cron 配信は、子孫サブエージェント作業がまだ排出中の間は古い中間の親返信を抑制し、配信前に最終的な子孫出力が到着した場合はそれを優先します。
  * 完了通知はチャネルに直接配信されるか、次の Heartbeat 用にキューに入れられます。
  * `openclaw tasks list` はすべてのタスクを表示します。`openclaw tasks audit` は問題を表面化します。
  * ターミナル記録は 7 日間保持され、その後自動的に削除されます。


## クイックスタート

### 一覧表示と絞り込み

bashCopy code
[code]
    # すべてのタスクを一覧表示する (新しい順)openclaw tasks list # ランタイムまたはステータスで絞り込むopenclaw tasks list --runtime acpopenclaw tasks list --status running
[/code]

### 調査

bashCopy code
[code]
    # 特定のタスクの詳細を表示する (ID、実行 ID、またはセッションキー)openclaw tasks show <lookup>
[/code]

### キャンセルと通知

bashCopy code
[code]
    # 実行中のタスクをキャンセルする (子セッションを終了する)openclaw tasks cancel <lookup> # タスクの通知ポリシーを変更するopenclaw tasks notify <lookup> state_changes
[/code]

### 監査と保守

bashCopy code
[code]
    # ヘルス監査を実行するopenclaw tasks audit # 保守をプレビューまたは適用するopenclaw tasks maintenanceopenclaw tasks maintenance --apply
[/code]

### タスクフロー

bashCopy code
[code]
    # TaskFlow の状態を調査するopenclaw tasks flow listopenclaw tasks flow show <lookup>openclaw tasks flow cancel <lookup>
[/code]

## タスクを作成するもの

ソース | ランタイム種別 | タスク記録が作成されるタイミング | デフォルト通知ポリシー  
---|---|---|---  
ACP バックグラウンド実行 | `acp` | 子 ACP セッションを生成するとき | `done_only`  
サブエージェントのオーケストレーション | `subagent` | `sessions_spawn` 経由でサブエージェントを生成するとき | `done_only`  
Cron ジョブ (全種別) | `cron` | 各 cron 実行 (メインセッションと分離実行) | `silent`  
CLI 操作 | `cli` | Gateway 経由で実行される `openclaw agent` コマンド | `silent`  
エージェントメディアジョブ | `cli` | セッションに基づく `music_generate`/`video_generate` 実行 | `silent`  
  
cron とメディアの通知デフォルト

メインセッションの cron タスクは、デフォルトで `silent` 通知ポリシーを使用します。追跡用の記録は作成しますが、通知は生成しません。分離された cron タスクもデフォルトは `silent` ですが、独自のセッションで実行されるため、より見えやすくなります。

セッションに基づく `music_generate` と `video_generate` の実行も `silent` 通知ポリシーを使用します。それでもタスク記録は作成されますが、完了は内部ウェイクとして元のエージェントセッションに返されるため、エージェントはフォローアップメッセージを書き、完成したメディアを自分で添付できます。グループ/チャネルの完了は通常の可視返信ポリシーに従うため、ソース配信で必要な場合、エージェントはメッセージツールを使用します。ツールのみの経路で完了エージェントがメッセージツール配信の証拠を生成できない場合、OpenClaw はメディアを非公開のままにするのではなく、完了フォールバックを元のチャネルに直接送信します。

同時 video_generate のガードレール

セッションに基づく `video_generate` タスクがまだアクティブな間、このツールはガードレールとしても機能します。同じセッション内で `video_generate` 呼び出しが繰り返された場合、2 つ目の同時生成を開始する代わりに、アクティブなタスクのステータスを返します。エージェント側から明示的な進行状況/ステータス参照が必要な場合は、`action: "status"` を使用してください。

タスクを作成しないもの

  * Heartbeat ターン - メインセッション。[Heartbeat](</ja-JP/gateway/heartbeat>) を参照
  * 通常の対話チャットターン
  * 直接の `/command` 応答


## タスクのライフサイクル
[code] 
    stateDiagram-v2
        [*] --> queued
        queued --> running : agent starts
        running --> succeeded : completes ok
        running --> failed : error
        running --> timed_out : timeout exceeded
        running --> cancelled : operator cancels
        queued --> lost : session gone > 5 min
        running --> lost : session gone > 5 min
[/code]

ステータス | 意味  
---|---  
`queued` | 作成済みで、エージェントの開始を待機中  
`running` | エージェントターンがアクティブに実行中  
`succeeded` | 正常に完了  
`failed` | エラーで完了  
`timed_out` | 設定されたタイムアウトを超過  
`cancelled` | オペレーターが `openclaw tasks cancel` で停止  
`lost` | 5 分間の猶予期間後に、ランタイムが権威ある裏付け状態を失った  
  
遷移は自動的に発生します。関連するエージェント実行が終了すると、タスクステータスはそれに合わせて更新されます。

エージェント実行の完了は、アクティブなタスク記録に対して権威があります。成功した切り離し実行は `succeeded` として最終化され、通常の実行エラーは `failed` として最終化され、タイムアウトまたは中止の結果は `timed_out` として最終化されます。オペレーターがすでにタスクをキャンセルしていた場合、またはランタイムが `failed`、`timed_out`、`lost` などのより強いターミナル状態をすでに記録していた場合、後から成功シグナルが来ても、そのターミナルステータスを格下げしません。

`lost` はランタイムを考慮します:

  * ACP タスク: 裏付けとなる ACP 子セッションメタデータが消えた。
  * サブエージェントタスク: 裏付けとなる子セッションが対象エージェントストアから消えた。
  * Cron タスク: cron ランタイムがそのジョブをアクティブとして追跡しなくなり、永続化された cron 実行履歴にもその実行のターミナル結果が示されていない。オフライン CLI 監査は、自身の空のプロセス内 cron ランタイム状態を権威として扱いません。
  * CLI タスク: 実行 ID/ソース ID を持つタスクはライブ実行コンテキストを使用するため、 子セッションまたはチャットセッションの行が残っていても、 Gateway が所有する実行が消えた後にそれらを生存状態には保ちません。実行 ID がないレガシー CLI タスクは、引き続き 子セッションへフォールバックします。Gateway に基づく `openclaw agent` 実行も 実行結果から最終化されるため、完了した実行が、スイーパーによって `lost` とマークされるまでアクティブのままにはなりません。


## 配信と通知

タスクがターミナル状態に達すると、OpenClaw が通知します。配信経路は 2 つあります:

**直接配信** \- タスクにチャネルターゲット (`requesterOrigin`) がある場合、完了メッセージはそのチャネル (Telegram、Discord、Slack など) に直接送られます。グループとチャネルのタスク完了は、代わりにリクエスターセッション経由でルーティングされるため、親エージェントが可視返信を書けます。サブエージェント完了では、OpenClaw は利用可能な場合、バインド済みのスレッド/トピックルーティングも保持し、直接配信を諦める前に、リクエスターセッションに保存された経路 (`lastChannel` / `lastTo` / `lastAccountId`) から不足している `to` / アカウントを補完できます。

**セッションキュー配信** \- 直接配信が失敗した場合、または origin が設定されていない場合、更新はリクエスターのセッション内のシステムイベントとしてキューに入れられ、次の Heartbeat で表面化します。

つまり、通常のワークフローはプッシュベースです。切り離された作業を一度開始し、完了時にランタイムが起こすか通知するのに任せます。タスク状態をポーリングするのは、デバッグ、介入、または明示的な監査が必要な場合だけです。

### 通知ポリシー

各タスクについて、どれだけ通知を受け取るかを制御します:

ポリシー | 配信される内容  
---|---  
`done_only` (デフォルト) | ターミナル状態のみ (succeeded、failed など) - **これがデフォルトです**  
`state_changes` | すべての状態遷移と進行状況更新  
`silent` | 何も配信しない  
  
タスクの実行中にポリシーを変更します:

bashCopy code
[code]
    openclaw tasks notify <lookup> state_changes
[/code]

## CLI リファレンス

tasks list bashCopy code
[code]
    openclaw tasks list [--runtime <acp|subagent|cron|cli>] [--status <status>] [--json]
[/code]

出力列: タスク ID、種類、ステータス、配信、実行 ID、子セッション、概要。

tasks show bashCopy code
[code]
    openclaw tasks show <lookup>
[/code]

lookup トークンは、タスク ID、実行 ID、またはセッションキーを受け付けます。タイミング、配信状態、エラー、ターミナル概要を含む完全な記録を表示します。

tasks cancel bashCopy code
[code]
    openclaw tasks cancel <lookup>
[/code]

ACP とサブエージェントタスクでは、これは子セッションを終了します。CLI で追跡されるタスクでは、キャンセルはタスクレジストリに記録されます (別個の子ランタイムハンドルはありません)。ステータスは `cancelled` に遷移し、該当する場合は配信通知が送信されます。

tasks notify bashCopy code
[code]
    openclaw tasks notify <lookup> <done_only|state_changes|silent>
[/code]

tasks audit bashCopy code
[code]
    openclaw tasks audit [--json]
[/code]

運用上の問題を表面化します。問題が検出された場合、検出結果は `openclaw status` にも表示されます。

検出項目 | 重要度 | トリガー  
---|---|---  
`stale_queued` | warn | 10分を超えてキューに入っている  
`stale_running` | error | 30分を超えて実行中  
`lost` | warn/error | ランタイムに基づくタスク所有権が消失した。保持中の lost タスクは `cleanupAfter` まで警告となり、その後エラーになる  
`delivery_failed` | warn | 配信に失敗し、通知ポリシーが `silent` ではない  
`missing_cleanup` | warn | クリーンアップタイムスタンプがない終端タスク  
`inconsistent_timestamps` | warn | タイムライン違反（たとえば開始前に終了している）  
tasks maintenance bashCopy code
[code]
    openclaw tasks maintenance [--json]openclaw tasks maintenance --apply [--json]
[/code]

これを使用して、タスク、タスクフロー状態、古い cron 実行セッションレジストリ行の照合、クリーンアップのタイムスタンプ付与、プルーニングをプレビューまたは適用します。

照合はランタイムを考慮します。

  * ACP/サブエージェントタスクは、対応する子セッションを確認します。
  * 子セッションに再起動リカバリの tombstone があるサブエージェントタスクは、復旧可能な対応セッションとして扱われず、lost としてマークされます。
  * Cron タスクは、cron ランタイムがまだジョブを所有しているかを確認し、その後 `lost` にフォールバックする前に、永続化された cron 実行ログ/ジョブ状態から終端ステータスを復旧します。インメモリの cron アクティブジョブ集合について権威を持つのは Gateway プロセスのみです。オフライン CLI 監査は耐久性のある履歴を使用しますが、そのローカル Set が空であることだけを理由に cron タスクを lost としてマークすることはありません。
  * 実行 ID を持つ CLI タスクは、子セッションやチャットセッション行だけでなく、所有しているライブ実行コンテキストを確認します。


完了時のクリーンアップもランタイムを考慮します。

  * サブエージェントの完了では、アナウンスのクリーンアップが続行する前に、子セッションに対して追跡されているブラウザタブ/プロセスをベストエフォートで閉じます。
  * 分離された cron の完了では、実行が完全に終了する前に、cron セッションに対して追跡されているブラウザタブ/プロセスをベストエフォートで閉じます。
  * 分離された cron の配信は、必要に応じて子孫サブエージェントのフォローアップを待ち、古い親の確認応答テキストをアナウンスする代わりに抑制します。
  * サブエージェント完了の配信では、最新の表示可能な assistant テキストを優先します。それが空の場合は、サニタイズ済みの最新 tool/toolResult テキストにフォールバックし、タイムアウトのみのツール呼び出し実行は短い部分進捗サマリーにまとめられることがあります。終端で失敗した実行は、取得済みの返信テキストを再生せずに失敗ステータスをアナウンスします。
  * クリーンアップの失敗が、実際のタスク結果を隠すことはありません。


maintenance を適用すると、OpenClaw は7日より古い `cron:<jobId>:run:<uuid>` セッションレジストリ行も削除します。その一方で、現在実行中の cron ジョブの行は保持し、cron 以外のセッション行には手を触れません。

tasks flow list | show | cancel bashCopy code
[code]
    openclaw tasks flow list [--status <status>] [--json]openclaw tasks flow show <lookup> [--json]openclaw tasks flow cancel <lookup>
[/code]

個別のバックグラウンドタスクレコードではなく、調整役のタスクフローに関心がある場合に使用します。

## チャットタスクボード（`/tasks`）

任意のチャットセッションで `/tasks` を使用すると、そのセッションにリンクされたバックグラウンドタスクを確認できます。ボードには、アクティブなタスクと最近完了したタスクが、ランタイム、ステータス、タイミング、進捗またはエラー詳細とともに表示されます。

現在のセッションに表示可能なリンク済みタスクがない場合、`/tasks` はエージェントローカルのタスク数にフォールバックするため、他セッションの詳細を漏らさずに概要を確認できます。

完全なオペレータ台帳には CLI を使用します: `openclaw tasks list`。

## ステータス統合（タスク負荷）

`openclaw status` には、一目でわかるタスクサマリーが含まれます。

CodeCopy code
[code]
    Tasks: 3 queued · 2 running · 1 issues
[/code]

サマリーは次を報告します。

  * **active** \- `queued` \+ `running` の数
  * **failures** \- `failed` \+ `timed_out` \+ `lost` の数
  * **byRuntime** \- `acp`、`subagent`、`cron`、`cli` ごとの内訳


`/status` と `session_status` ツールはいずれも、クリーンアップを考慮したタスクスナップショットを使用します。アクティブなタスクが優先され、古い完了済み行は非表示になり、最近の失敗はアクティブな作業が残っていない場合にのみ表示されます。これにより、ステータスカードは今重要な内容に集中できます。

## ストレージと maintenance

### タスクの保存場所

タスクレコードは SQLite の次の場所に永続化されます。

CodeCopy code
[code]
    $OPENCLAW_STATE_DIR/tasks/runs.sqlite
[/code]

レジストリは Gateway 起動時にメモリへ読み込まれ、再起動をまたいだ耐久性のために書き込みを SQLite に同期します。 Gateway は、SQLite の既定の autocheckpoint しきい値に加え、定期的な `TRUNCATE` チェックポイントとシャットダウン時の `TRUNCATE` チェックポイントを使用して、SQLite の先行書き込みログを制限します。

### 自動 maintenance

スイーパーは **60秒** ごとに実行され、4つの処理を行います。

* ### 照合

アクティブなタスクに、権威のあるランタイム上の裏付けがまだあるかを確認します。ACP/サブエージェントタスクは子セッション状態を使用し、cron タスクはアクティブジョブ所有権を使用し、実行 ID を持つ CLI タスクは所有している実行コンテキストを使用します。その裏付け状態が5分を超えて失われている場合、タスクは `lost` としてマークされます。

* ### ACP セッション修復

終端状態または孤立した親所有のワンショット ACP セッションを閉じます。また、古い終端状態または孤立した永続 ACP セッションは、アクティブな会話バインディングが残っていない場合にのみ閉じます。

* ### クリーンアップのタイムスタンプ付与

終端タスクに `cleanupAfter` タイムスタンプを設定します（endedAt + 7日）。保持期間中、lost タスクは監査で引き続き警告として表示されます。`cleanupAfter` が期限切れになるか、クリーンアップメタデータが欠落している場合はエラーになります。

* ### プルーニング

`cleanupAfter` の日付を過ぎたレコードを削除します。

## タスクと他システムの関係

タスクとタスクフロー

[タスクフロー](</ja-JP/automation/taskflow>) は、バックグラウンドタスクの上位にあるフローオーケストレーション層です。1つのフローは、そのライフタイム全体で managed または mirrored の同期モードを使用し、複数のタスクを調整することがあります。個別のタスクレコードを調べるには `openclaw tasks` を使用し、調整役のフローを調べるには `openclaw tasks flow` を使用します。

詳細は [タスクフロー](</ja-JP/automation/taskflow>) を参照してください。

タスクと cron

cron ジョブの**定義** は `~/.openclaw/cron/jobs.json` にあります。ランタイム実行状態は、その横の `~/.openclaw/cron/jobs-state.json` にあります。cron の**すべての** 実行はタスクレコードを作成します。メインセッションと分離実行の両方が対象です。メインセッションの cron タスクは、通知を生成せずに追跡できるよう、既定で `silent` 通知ポリシーになります。

[Cron ジョブ](</ja-JP/automation/cron-jobs>) を参照してください。

タスクと Heartbeat

Heartbeat 実行はメインセッションのターンであり、タスクレコードは作成しません。タスクが完了すると、Heartbeat のウェイクをトリガーし、結果をすぐに確認できるようにできます。

[Heartbeat](</ja-JP/gateway/heartbeat>) を参照してください。

タスクとセッション

タスクは `childSessionKey`（作業が実行される場所）と `requesterSessionKey`（開始した主体）を参照することがあります。セッションは会話コンテキストであり、タスクはその上にあるアクティビティ追跡です。

タスクとエージェント実行

タスクの `runId` は、作業を実行しているエージェント実行にリンクします。エージェントのライフサイクルイベント（開始、終了、エラー）はタスクステータスを自動的に更新するため、ライフサイクルを手動で管理する必要はありません。

## 関連

  * [自動化](</ja-JP/automation>) \- すべての自動化メカニズムの概要
  * [CLI: タスク](</ja-JP/cli/tasks>) \- CLI コマンドリファレンス
  * [Heartbeat](</ja-JP/gateway/heartbeat>) \- 定期的なメインセッションターン
  * [スケジュールされたタスク](</ja-JP/automation/cron-jobs>) \- バックグラウンド作業のスケジューリング
  * [タスクフロー](</ja-JP/automation/taskflow>) \- タスクの上位にあるフローオーケストレーション


Was this useful?YesNo