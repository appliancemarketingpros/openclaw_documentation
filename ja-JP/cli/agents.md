---
title: エージェント
source_url: https://docs.openclaw.ai/ja-JP/cli/agents
scraped_at: 2026-05-25
---

# `openclaw agents`

分離されたエージェント（ワークスペース + 認証 + ルーティング）を管理します。

関連:

  * [マルチエージェントルーティング](</ja-JP/concepts/multi-agent>)
  * [エージェントワークスペース](</ja-JP/concepts/agent-workspace>)
  * [Skills 設定](</ja-JP/tools/skills-config>): Skills の可視性設定。


## 例

bashCopy code
[code]
    openclaw agents listopenclaw agents list --bindingsopenclaw agents add work --workspace ~/.openclaw/workspace-workopenclaw agents add ops --workspace ~/.openclaw/workspace-ops --bind telegram:ops --non-interactiveopenclaw agents bindingsopenclaw agents bind --agent work --bind telegram:opsopenclaw agents unbind --agent work --bind telegram:opsopenclaw agents set-identity --workspace ~/.openclaw/workspace --from-identityopenclaw agents set-identity --agent main --avatar avatars/openclaw.pngopenclaw agents delete work
[/code]

## ルーティングバインディング

ルーティングバインディングを使うと、受信チャネルのトラフィックを特定のエージェントに固定できます。

エージェントごとに表示される Skills も変えたい場合は、`openclaw.json` で `agents.defaults.skills` と `agents.list[].skills` を設定します。[Skills 設定](</ja-JP/tools/skills-config>) と [設定リファレンス](</ja-JP/gateway/config-agents#agents-defaults-skills>) を参照してください。

バインディングを一覧表示します:

bashCopy code
[code]
    openclaw agents bindingsopenclaw agents bindings --agent workopenclaw agents bindings --json
[/code]

バインディングを追加します:

bashCopy code
[code]
    openclaw agents bind --agent work --bind telegram:ops --bind discord:guild-a
[/code]

`accountId`（`--bind <channel>`）を省略すると、利用可能な場合、OpenClaw はチャネルのデフォルトと Plugin セットアップフックから解決します。

`bind` または `unbind` で `--agent` を省略すると、OpenClaw は現在のデフォルトエージェントを対象にします。

### バインディングスコープの動作

  * `accountId` なしのバインディングは、チャネルのデフォルトアカウントのみに一致します。
  * `accountId: "*"` はチャネル全体のフォールバック（すべてのアカウント）であり、明示的なアカウントバインディングより具体性が低くなります。
  * 同じエージェントに `accountId` なしの一致するチャネルバインディングがすでにあり、後から明示的または解決済みの `accountId` でバインドすると、OpenClaw は重複を追加せず、その既存のバインディングをその場でアップグレードします。


例:

bashCopy code
[code]
    # initial channel-only bindingopenclaw agents bind --agent work --bind telegram # later upgrade to account-scoped bindingopenclaw agents bind --agent work --bind telegram:ops
[/code]

アップグレード後、そのバインディングのルーティングは `telegram:ops` にスコープされます。デフォルトアカウントのルーティングも必要な場合は、明示的に追加してください（例: `--bind telegram:default`）。

バインディングを削除します:

bashCopy code
[code]
    openclaw agents unbind --agent work --bind telegram:opsopenclaw agents unbind --agent work --all
[/code]

`unbind` は `--all`、または 1 つ以上の `--bind` 値のどちらかを受け付けます。両方は指定できません。

## コマンドサーフェス

### `agents`

サブコマンドなしで `openclaw agents` を実行することは、`openclaw agents list` と同等です。

### `agents list`

オプション:

  * `--json`
  * `--bindings`: エージェントごとの件数や要約だけでなく、完全なルーティングルールを含めます


### `agents add [name]`

オプション:

  * `--workspace <dir>`
  * `--model <id>`
  * `--agent-dir <dir>`
  * `--bind <channel[:accountId]>`（繰り返し指定可）
  * `--non-interactive`
  * `--json`


注記:

  * 明示的な追加フラグを渡すと、コマンドは非対話パスに切り替わります。
  * 非対話モードでは、エージェント名と `--workspace` の両方が必要です。
  * `main` は予約済みであり、新しいエージェント ID として使用できません。
  * 対話モードでは、認証シードはポータブルな静的プロファイルのみをコピーします （デフォルトでは `api_key` と静的な `token`）。OAuth リフレッシュトークンプロファイルは、実際の `main` エージェントストアからの読み取り継承によってのみ 利用できます。 設定済みのデフォルトエージェントが `main` でない場合、新しいエージェントで OAuth プロファイルに個別にサインインしてください。


### `agents bindings`

オプション:

  * `--agent <id>`
  * `--json`


### `agents bind`

オプション:

  * `--agent <id>`（現在のデフォルトエージェントがデフォルト）
  * `--bind <channel[:accountId]>`（繰り返し指定可）
  * `--json`


### `agents unbind`

オプション:

  * `--agent <id>`（現在のデフォルトエージェントがデフォルト）
  * `--bind <channel[:accountId]>`（繰り返し指定可）
  * `--all`
  * `--json`


### `agents delete <id>`

オプション:

  * `--force`
  * `--json`


注記:

  * `main` は削除できません。
  * `--force` なしでは、対話的な確認が必要です。
  * ワークスペース、エージェント状態、セッショントランスクリプトディレクトリは完全削除されず、ゴミ箱に移動されます。
  * Gateway に到達できる場合、削除は Gateway 経由で送信されるため、設定とセッションストアのクリーンアップはランタイムトラフィックと同じ書き込み元を共有します。Gateway に到達できない場合、CLI はオフラインのローカルパスにフォールバックします。
  * 別のエージェントのワークスペースが同じパスである、このワークスペース内にある、またはこのワークスペースを含む場合、 ワークスペースは保持され、`--json` は `workspaceRetained`、 `workspaceRetainedReason`、`workspaceSharedWith` を報告します。


## ID ファイル

各エージェントワークスペースは、ワークスペースルートに `IDENTITY.md` を含めることができます:

  * 例のパス: `~/.openclaw/workspace/IDENTITY.md`
  * `set-identity --from-identity` はワークスペースルート（または明示的な `--identity-file`）から読み取ります


アバターパスはワークスペースルートからの相対パスとして解決されます。

## ID を設定する

`set-identity` はフィールドを `agents.list[].identity` に書き込みます:

  * `name`
  * `theme`
  * `emoji`
  * `avatar`（ワークスペース相対パス、http(s) URL、またはデータ URI）


オプション:

  * `--agent <id>`
  * `--workspace <dir>`
  * `--identity-file <path>`
  * `--from-identity`
  * `--name <name>`
  * `--theme <theme>`
  * `--emoji <emoji>`
  * `--avatar <value>`
  * `--json`


注記:

  * `--agent` または `--workspace` を使って対象エージェントを選択できます。
  * `--workspace` に依存していて、複数のエージェントがそのワークスペースを共有している場合、コマンドは失敗し、`--agent` を渡すよう求めます。
  * 明示的な ID フィールドが指定されていない場合、コマンドは `IDENTITY.md` から ID データを読み取ります。


`IDENTITY.md` から読み込みます:

bashCopy code
[code]
    openclaw agents set-identity --workspace ~/.openclaw/workspace --from-identity
[/code]

フィールドを明示的に上書きします:

bashCopy code
[code]
    openclaw agents set-identity --agent main --name "OpenClaw" --emoji "🦞" --avatar avatars/openclaw.png
[/code]

設定サンプル:

json5Copy code
[code]
    {  agents: {    list: [      {        id: "main",        identity: {          name: "OpenClaw",          theme: "space lobster",          emoji: "🦞",          avatar: "avatars/openclaw.png",        },      },    ],  },}
[/code]

## 関連

  * [CLI リファレンス](</ja-JP/cli>)
  * [マルチエージェントルーティング](</ja-JP/concepts/multi-agent>)
  * [エージェントワークスペース](</ja-JP/concepts/agent-workspace>)


Was this useful?YesNo