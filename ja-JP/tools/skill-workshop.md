---
title: スキルワークショップ
source_url: https://docs.openclaw.ai/ja-JP/tools/skill-workshop
scraped_at: 2026-06-29
---

CapabilitiesSkills

スキルワークショップは、ワークスペースのスキルを作成および更新するための OpenClaw の管理された経路です。

エージェントとオペレーターは、この経路でアクティブな `SKILL.md` ファイルを直接書きません。まず **proposal** を作成します。proposal は、提案されたスキル内容、対象バインディング、スキャナー状態、ハッシュ、サポートファイルのメタデータ、ロールバックメタデータを含む保留中のドラフトです。適用された場合にのみ、ライブスキルになります。

スキルワークショップが書き込むのはワークスペーススキルのみです。バンドル、Plugin、ClawHub、追加ルート、管理対象、個人エージェント、またはシステムスキルは変更しません。

## 仕組み

  * **まず proposal:** 生成されたスキル内容は `SKILL.md` ではなく `PROPOSAL.md` として保存されます。
  * **apply だけがライブ書き込み:** create、update、revise はアクティブなスキルを変更しません。
  * **ワークスペーススコープ:** 作成対象はワークスペースの `skills/` ルートです。更新は、書き込み可能なワークスペーススキルに対してのみ許可されます。
  * **上書きなし:** 対象スキルがすでに存在する場合、create は失敗します。
  * **ハッシュ束縛:** update proposal は現在の対象ハッシュに束縛され、apply の前にライブスキルが変更されると stale になります。
  * **スキャナーゲート:** apply は書き込み前にスキャンを再実行します。
  * **復旧可能:** apply はライブファイルを変更する前にロールバックメタデータを書き込みます。
  * **一貫したサーフェス:** チャット、CLI、Gateway はすべて同じスキルワークショップサービスを呼び出します。


## ライフサイクル

textCopy code
[code]
    create/update -> pendingrevise        -> pendingapply         -> appliedreject        -> rejectedquarantine    -> quarantinedtarget change -> stale
[/code]

`pending` の proposal のみが、改訂、適用、却下、または隔離できます。

## チャット

必要なスキルをエージェントに依頼します。エージェントは `skill_workshop` を呼び出し、proposal id を返します。

作成:

textCopy code
[code]
    Make a skill called morning-catchup that runs my Monday inbox routine.
[/code]

既存のワークスペーススキルを更新:

textCopy code
[code]
    Update trip-planning to also check seat maps before booking.
[/code]

保留中の proposal を反復:

textCopy code
[code]
    Show me the morning-catchup proposal.Revise it to also flag anything marked urgent.Apply the morning-catchup proposal.
[/code]

デフォルトでは、エージェント起点の `apply`、`reject`、`quarantine` は実行前に承認プロンプトを表示します。信頼できる環境でプロンプトをスキップするには、`skills.workshop.approvalPolicy` を `"auto"` に設定します。

## CLI

新しいスキル proposal を作成します:

bashCopy code
[code]
    openclaw skills workshop propose-create \  --name morning-catchup \  --description "Daily inbox catch-up: triage, archive, surface, draft, plan" \  --proposal ./PROPOSAL.md
[/code]

既存のワークスペーススキルに対する更新 proposal を作成します:

bashCopy code
[code]
    openclaw skills workshop propose-update trip-planning --proposal ./PROPOSAL.md
[/code]

一覧表示と確認:

bashCopy code
[code]
    openclaw skills workshop listopenclaw skills workshop inspect <proposal-id>
[/code]

承認前に改訂:

bashCopy code
[code]
    openclaw skills workshop revise <proposal-id> --proposal ./PROPOSAL.md
[/code]

proposal を完了します:

bashCopy code
[code]
    openclaw skills workshop apply <proposal-id>openclaw skills workshop reject <proposal-id> --reason "Duplicate"openclaw skills workshop quarantine <proposal-id> --reason "Needs security review"
[/code]

## Proposal の内容

保留中、proposal は proposal 専用 frontmatter を持つ `PROPOSAL.md` として保存されます:

markdownCopy code
[code]
    ---name: "morning-catchup"description: "Daily inbox catch-up: triage, archive, surface, draft, plan"status: proposalversion: "v1"date: "2026-05-30T00:00:00.000Z"---
[/code]

apply 時に、スキルワークショップはアクティブな `SKILL.md` を書き込み、proposal 専用フィールドである `status`、proposal `version`、proposal `date` を削除します。

## サポートファイル

提案されたスキルが `PROPOSAL.md` の横にファイルを必要とする場合は、`--proposal-dir` を使用します:

bashCopy code
[code]
    openclaw skills workshop propose-create \  --name weekly-update \  --description "Friday wrap-up: stats, highlights, next week's top three" \  --proposal-dir ./weekly-update-proposal
[/code]

ディレクトリには `PROPOSAL.md` が含まれている必要があります。サポートファイルは次の配下にある必要があります:

  * `assets/`
  * `examples/`
  * `references/`
  * `scripts/`
  * `templates/`


スキルワークショップは proposal とともにサポートファイルをスキャン、ハッシュ化、保存します。これらは apply 時にのみ、ライブ `SKILL.md` の横に書き込まれます。

拒否されるサポートファイルパスには、絶対パス、隠しパスセグメント、パストラバーサル、重複するパス、proposal ディレクトリ由来の実行可能ファイル、非 UTF-8 テキスト、null バイト、標準サポートフォルダー外のファイルが含まれます。

## エージェントツール

モデルは `skill_workshop` を使用します:

textCopy code
[code]
    action: create | update | revise | list | inspect | apply | reject | quarantine
[/code]

エージェントは、生成されるスキル作業に `skill_workshop` を使用する必要があります。`write`、`edit`、`exec`、シェルコマンド、または直接のファイルシステム操作で proposal ファイルを作成または変更してはいけません。

## 承認と自律性

json5Copy code
[code]
    {  skills: {    workshop: {      autonomous: {        enabled: false,      },      allowSymlinkTargetWrites: false,      approvalPolicy: "pending",      maxPending: 50,      maxSkillBytes: 40000,    },  },}
[/code]

  * `autonomous.enabled`: 成功したターン後に、永続的な会話シグナルから OpenClaw が保留中の proposal を作成できるようにします。デフォルト: `false`。
  * `allowSymlinkTargetWrites`: 実際の対象が `skills.load.allowSymlinkTargets` に listed されているワークスペーススキルのシンボリックリンクを通じて、apply が書き込めるようにします。デフォルト: `false`。
  * `approvalPolicy: "pending"`: エージェント起点の `apply`、`reject`、または `quarantine` の前に承認プロンプトを要求します。
  * `approvalPolicy: "auto"`: その承認プロンプトをスキップします。エージェントは引き続きアクションを呼び出す必要があります。
  * `maxPending`: ワークスペースごとの保留中および隔離済み proposal 数を制限します。
  * `maxSkillBytes`: proposal 本文サイズを制限します。デフォルト: `40000`。


Proposal の説明は常に 160 バイトに制限されます。

## Gateway メソッド

textCopy code
[code]
    skills.proposals.listskills.proposals.inspectskills.proposals.createskills.proposals.updateskills.proposals.reviseskills.proposals.applyskills.proposals.rejectskills.proposals.quarantine
[/code]

読み取り専用メソッドには `operator.read` が必要です。変更メソッドには `operator.admin` が必要です。

## ストレージ

textCopy code
[code]
    &lt;OPENCLAW_STATE_DIR&gt;/skill-workshop/  proposals.json  proposals/<proposal-id>/    proposal.json    PROPOSAL.md    rollback.json    assets/    examples/    references/    scripts/    templates/
[/code]

デフォルトの状態ディレクトリ: `~/.openclaw`。

  * `proposal.json`: 正規の proposal レコード。
  * `proposals.json`: proposal フォルダーから再構築可能な高速一覧インデックス。
  * `PROPOSAL.md`: 保留中のスキル proposal。
  * `rollback.json`: apply がライブファイルを変更する前に書き込む復旧メタデータ。


## 制限

  * 説明: 160 バイト。
  * Proposal 本文: `skills.workshop.maxSkillBytes`（デフォルト 40,000）。
  * サポートファイル: proposal ごとに 64 個。
  * サポートファイルサイズ: 各 256 KB、合計 2 MB。
  * 保留中および隔離済み proposal: ワークスペースごとに `skills.workshop.maxPending`（デフォルト 50）。


## トラブルシューティング

問題 | 解決方法  
---|---  
`Skill proposal description is too large` | `description` を 160 バイト以下に短縮します。  
`Skill proposal content is too large` | proposal 本文を短縮するか、`skills.workshop.maxSkillBytes` を引き上げます。  
`Target skill changed after proposal creation` | 現在の対象に対して proposal を改訂するか、新しい proposal を作成します。  
`Proposal scan failed` | スキャナーの検出事項を確認してから、proposal を改訂または隔離します。  
`untrusted symlink target` | 意図的な共有スキルルートに対してのみ、`skills.load.allowSymlinkTargets` を設定し、`skills.workshop.allowSymlinkTargetWrites` を有効にします。  
`Support file paths must be under one of...` | サポートファイルを `assets/`、`examples/`、`references/`、`scripts/`、または `templates/` の配下に移動します。  
Proposal が一覧に表示されない | 選択された `--agent` ワークスペースと `OPENCLAW_STATE_DIR` を確認します。  
エージェントが `skill_workshop` を呼び出せない | アクティブなツールポリシーと実行モードを確認します。`coding` にはこのツールが含まれます。制限的な `tools.allow` ポリシーでは明示的に listed する必要があり、サンドボックス実行では通常のホスト側エージェントセッションまたは CLI を使用する必要があります。  
  
## 関連

  * 読み込み順序、優先順位、可視性については [Skills](</ja-JP/tools/skills>)
  * 手書きの `SKILL.md` の基本については [スキルの作成](</ja-JP/tools/creating-skills>)
  * 完全な `skills.workshop` schema については [Skills 設定](</ja-JP/tools/skills-config>)
  * `openclaw skills` コマンドについては [Skills CLI](</ja-JP/cli/skills>)


Was this useful?YesNo

Open issue