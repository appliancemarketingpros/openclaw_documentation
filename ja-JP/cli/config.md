---
title: 設定
source_url: https://docs.openclaw.ai/ja-JP/cli/config
scraped_at: 2026-05-25
---

`openclaw.json` の非対話的な編集用の構成ヘルパー: パスで値を get/set/patch/unset/file/schema/validate し、アクティブな構成ファイルを出力します。サブコマンドなしで実行すると、構成ウィザードを開きます (`openclaw configure` と同じ)。

## ルートオプション

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ii0tc2VjdGlvbiA8c2VjdGlvbg " type="string"> `openclaw config` をサブコマンドなしで実行するときに使う、繰り返し指定可能なガイド付きセットアップのセクションフィルター。

対応するガイド付きセクション: `workspace`、`model`、`web`、`gateway`、`daemon`、`channels`、`plugins`、`skills`、`health`。

## 例

bashCopy code
[code]
    openclaw config fileopenclaw config --section modelopenclaw config --section gateway --section daemonopenclaw config schemaopenclaw config get browser.executablePathopenclaw config set browser.executablePath "/usr/bin/google-chrome"openclaw config set browser.profiles.work.executablePath "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"openclaw config set agents.defaults.heartbeat.every "2h"openclaw config set agents.list[0].tools.exec.node "node-id-or-name"openclaw config set agents.defaults.models '{"openai/gpt-5.4":{}}' --strict-json --mergeopenclaw config set channels.discord.token --ref-provider default --ref-source env --ref-id DISCORD_BOT_TOKENopenclaw config set secrets.providers.vaultfile --provider-source file --provider-path /etc/openclaw/secrets.json --provider-mode jsonopenclaw config patch --file ./openclaw.patch.json5 --dry-runopenclaw config unset plugins.entries.brave.config.webSearch.apiKeyopenclaw config set channels.discord.token --ref-provider default --ref-source env --ref-id DISCORD_BOT_TOKEN --dry-runopenclaw config validateopenclaw config validate --json
[/code]

### `config schema`

生成された `openclaw.json` 用の JSON スキーマを JSON として stdout に出力します。

含まれる内容

  * 現在のルート構成スキーマに加えて、エディターツール向けのルート `$schema` 文字列フィールド。
  * Control UI で使用されるフィールド `title` と `description` のドキュメントメタデータ。
  * ネストしたオブジェクト、ワイルドカード (`*`)、配列項目 (`[]`) ノードは、一致するフィールドドキュメントが存在する場合、同じ `title` / `description` メタデータを継承します。
  * `anyOf` / `oneOf` / `allOf` ブランチも、一致するフィールドドキュメントが存在する場合、同じドキュメントメタデータを継承します。
  * ランタイムマニフェストを読み込める場合は、ベストエフォートのライブ Plugin + チャネルスキーマメタデータ。
  * 現在の構成が無効な場合でも、クリーンなフォールバックスキーマ。

関連するランタイム RPC

`config.schema.lookup` は、浅いスキーマノード (`title`、`description`、`type`、`enum`、`const`、共通の境界)、一致した UI ヒントメタデータ、直下の子要素の概要を含む、正規化された構成パスを 1 つ返します。Control UI またはカスタムクライアントで、パス単位のドリルダウンに使用します。

bashCopy code
[code]
    openclaw config schema
[/code]

他のツールで検査または検証したい場合は、ファイルにパイプします。

bashCopy code
[code]
    openclaw config schema > openclaw.schema.json
[/code]

### パス

パスにはドット表記またはブラケット表記を使用します。

bashCopy code
[code]
    openclaw config get agents.defaults.workspaceopenclaw config get agents.list[0].id
[/code]

特定のエージェントを対象にするには、エージェントリストのインデックスを使用します。

bashCopy code
[code]
    openclaw config get agents.listopenclaw config set agents.list[1].tools.exec.node "node-id-or-name"
[/code]

## 値

値は可能な場合 JSON5 として解析されます。それ以外の場合は文字列として扱われます。JSON5 解析を必須にするには `--strict-json` を使用します。`--json` はレガシーエイリアスとして引き続きサポートされます。

bashCopy code
[code]
    openclaw config set agents.defaults.heartbeat.every "0m"openclaw config set gateway.port 19001 --strict-jsonopenclaw config set channels.whatsapp.groups '["*"]' --strict-json
[/code]

`config get <path> --json` は、ターミナル用に整形されたテキストではなく、生の値を JSON として出力します。

これらのマップにエントリーを追加するときは `--merge` を使用します。

bashCopy code
[code]
    openclaw config set agents.defaults.models '{"openai/gpt-5.4":{}}' --strict-json --mergeopenclaw config set models.providers.ollama.models '[{"id":"llama3.2","name":"Llama 3.2"}]' --strict-json --merge
[/code]

指定した値を完全な対象値にする意図がある場合にのみ、`--replace` を使用します。

## `config set` モード

`openclaw config set` は 4 つの代入スタイルに対応しています。

### 値モード

bashCopy code
[code]
    openclaw config set <path> <value>
[/code]

### SecretRef ビルダーモード

bashCopy code
[code]
    openclaw config set channels.discord.token \  --ref-provider default \  --ref-source env \  --ref-id DISCORD_BOT_TOKEN
[/code]

### Provider ビルダーモード

Provider ビルダーモードは `secrets.providers.<alias>` パスのみを対象にします。

bashCopy code
[code]
    openclaw config set secrets.providers.vault \  --provider-source exec \  --provider-command /usr/local/bin/openclaw-vault \  --provider-arg read \  --provider-arg openai/api-key \  --provider-timeout-ms 5000
[/code]

### バッチモード

bashCopy code
[code]
    openclaw config set --batch-json '[  {    "path": "secrets.providers.default",    "provider": { "source": "env" }  },  {    "path": "channels.discord.token",    "ref": { "source": "env", "provider": "default", "id": "DISCORD_BOT_TOKEN" }  }]'
[/code]

bashCopy code
[code]
    openclaw config set --batch-file ./config-set.batch.json --dry-run
[/code]

バッチ解析では、常にバッチペイロード (`--batch-json`/`--batch-file`) を信頼できる情報源として使用します。`--strict-json` / `--json` はバッチ解析の挙動を変更しません。

## `config patch`

多数のパスベースの `config set` コマンドを実行する代わりに、構成形式のパッチを貼り付けたりパイプしたりしたい場合は `config patch` を使用します。入力は JSON5 オブジェクトです。オブジェクトは再帰的にマージされ、配列とスカラー値は対象値を置き換え、`null` は対象パスを削除します。

bashCopy code
[code]
    openclaw config patch --file ./openclaw.patch.json5 --dry-runopenclaw config patch --file ./openclaw.patch.json5
[/code]

stdin 経由でパッチをパイプすることもできます。これはリモートセットアップスクリプトで便利です。

bashCopy code
[code]
    ssh openclaw-host 'openclaw config patch --stdin --dry-run' < ./openclaw.patch.json5ssh openclaw-host 'openclaw config patch --stdin' < ./openclaw.patch.json5
[/code]

パッチ例:

json5Copy code
[code]
    {  channels: {    slack: {      enabled: true,      mode: "socket",      botToken: { source: "env", provider: "default", id: "SLACK_BOT_TOKEN" },      appToken: { source: "env", provider: "default", id: "SLACK_APP_TOKEN" },      groupPolicy: "open",      requireMention: false,    },    discord: {      enabled: true,      token: { source: "env", provider: "default", id: "DISCORD_BOT_TOKEN" },      dmPolicy: "disabled",      dm: { enabled: false },      groupPolicy: "allowlist",    },  },  agents: {    defaults: {      model: { primary: "openai/gpt-5.5" },      models: {        "openai/gpt-5.5": { params: { fastMode: true } },      },    },  },}
[/code]

1 つのオブジェクトまたは配列を、再帰的にパッチするのではなく、指定した値そのものにしたい場合は `--replace-path <path>` を使用します。

bashCopy code
[code]
    openclaw config patch --file ./discord.patch.json5 --replace-path 'channels.discord.guilds["123"].channels'
[/code]

`--dry-run` は書き込みを行わずに、スキーマと SecretRef の解決可能性チェックを実行します。exec ベースの SecretRefs は、dry-run 中はデフォルトでスキップされます。dry-run で provider コマンドを意図的に実行したい場合は `--allow-exec` を追加します。

JSON パス/値モードは、SecretRefs と providers の両方で引き続きサポートされます。

bashCopy code
[code]
    openclaw config set channels.discord.token \  '{"source":"env","provider":"default","id":"DISCORD_BOT_TOKEN"}' \  --strict-json openclaw config set secrets.providers.vaultfile \  '{"source":"file","path":"/etc/openclaw/secrets.json","mode":"json"}' \  --strict-json
[/code]

## Provider ビルダーフラグ

Provider ビルダーの対象は、パスとして `secrets.providers.<alias>` を使用する必要があります。

共通フラグ

  * `--provider-source <env|file|exec>`
  * `--provider-timeout-ms <ms>` (`file`, `exec`)

Env provider (--provider-source env)

  * `--provider-allowlist &lt;ENV_VAR&gt;` (繰り返し指定可能)

File provider (--provider-source file)

  * `--provider-path <path>` (必須)
  * `--provider-mode <singleValue|json>`
  * `--provider-max-bytes <bytes>`
  * `--provider-allow-insecure-path`

Exec provider (--provider-source exec)

  * `--provider-command <path>` (必須)
  * `--provider-arg <arg>` (繰り返し指定可能)
  * `--provider-no-output-timeout-ms <ms>`
  * `--provider-max-output-bytes <bytes>`
  * `--provider-json-only`
  * `--provider-env &lt;KEY=VALUE&gt;` (繰り返し指定可能)
  * `--provider-pass-env &lt;ENV_VAR&gt;` (繰り返し指定可能)
  * `--provider-trusted-dir <path>` (繰り返し指定可能)
  * `--provider-allow-insecure-path`
  * `--provider-allow-symlink-command`


堅牢化した exec provider の例:

bashCopy code
[code]
    openclaw config set secrets.providers.vault \  --provider-source exec \  --provider-command /usr/local/bin/openclaw-vault \  --provider-arg read \  --provider-arg openai/api-key \  --provider-json-only \  --provider-pass-env VAULT_TOKEN \  --provider-trusted-dir /usr/local/bin \  --provider-timeout-ms 5000
[/code]

## Dry run

`openclaw.json` に書き込まずに変更を検証するには、`--dry-run` を使用します。

bashCopy code
[code]
    openclaw config set channels.discord.token \  --ref-provider default \  --ref-source env \  --ref-id DISCORD_BOT_TOKEN \  --dry-run openclaw config set channels.discord.token \  --ref-provider default \  --ref-source env \  --ref-id DISCORD_BOT_TOKEN \  --dry-run \  --json openclaw config set channels.discord.token \  --ref-provider vault \  --ref-source exec \  --ref-id discord/token \  --dry-run \  --allow-exec
[/code]

Dry-run の挙動

  * ビルダーモード: 変更された refs/providers に対して SecretRef の解決可能性チェックを実行します。
  * JSON モード (`--strict-json`、`--json`、またはバッチモード): スキーマ検証に加えて SecretRef の解決可能性チェックを実行します。
  * 既知の非対応 SecretRef 対象サーフェスに対しても、ポリシー検証が実行されます。
  * ポリシーチェックは変更後の構成全体を評価するため、親オブジェクトの書き込み (たとえば `hooks` をオブジェクトとして設定すること) で非対応サーフェス検証を回避することはできません。
  * Exec SecretRef チェックは、コマンドの副作用を避けるため、dry-run 中はデフォルトでスキップされます。
  * Exec SecretRef チェックにオプトインするには、`--dry-run` とともに `--allow-exec` を使用します (これにより provider コマンドが実行される場合があります)。
  * `--allow-exec` は dry-run 専用であり、`--dry-run` なしで使用するとエラーになります。

\--dry-run --json フィールド

`--dry-run --json` は機械可読なレポートを出力します:

  * `ok`: dry-run が成功したかどうか
  * `operations`: 評価された割り当ての数
  * `checks`: schema/解決可能性チェックが実行されたかどうか
  * `checks.resolvabilityComplete`: 解決可能性チェックが完了まで実行されたかどうか (exec refs がスキップされた場合は false)
  * `refsChecked`: dry-run 中に実際に解決された refs の数
  * `skippedExecRefs`: `--allow-exec` が設定されていなかったためスキップされた exec refs の数
  * `errors`: `ok=false` の場合の構造化された schema/解決可能性の失敗


### JSON 出力の形状

json5Copy code
[code]
    {  ok: boolean,  operations: number,  configPath: string,  inputModes: ["value" | "json" | "builder", ...],  checks: {    schema: boolean,    resolvability: boolean,    resolvabilityComplete: boolean,  },  refsChecked: number,  skippedExecRefs: number,  errors?: [    {      kind: "schema" | "resolvability",      message: string,      ref?: string, // present for resolvability errors    },  ],}
[/code]

### 成功例

jsonCopy code
[code]
    {  "ok": true,  "operations": 1,  "configPath": "~/.openclaw/openclaw.json",  "inputModes": ["builder"],  "checks": {    "schema": false,    "resolvability": true,    "resolvabilityComplete": true  },  "refsChecked": 1,  "skippedExecRefs": 0}
[/code]

### 失敗例

jsonCopy code
[code]
    {  "ok": false,  "operations": 1,  "configPath": "~/.openclaw/openclaw.json",  "inputModes": ["builder"],  "checks": {    "schema": false,    "resolvability": true,    "resolvabilityComplete": true  },  "refsChecked": 1,  "skippedExecRefs": 0,  "errors": [    {      "kind": "resolvability",      "message": "Error: Environment variable \"MISSING_TEST_SECRET\" is not set.",      "ref": "env:default:MISSING_TEST_SECRET"    }  ]}
[/code]

dry-run が失敗した場合

  * `config schema validation failed`: 変更後の config 形状が無効です。path/value または provider/ref オブジェクトの形状を修正してください。
  * `Config policy validation failed: unsupported SecretRef usage`: その credential を plaintext/string 入力に戻し、SecretRefs はサポート対象の surface でのみ使用してください。
  * `SecretRef assignment(s) could not be resolved`: 参照された provider/ref は現在解決できません (env var の欠落、無効な file pointer、exec provider の失敗、または provider/source の不一致)。
  * `Dry run note: skipped <n> exec SecretRef resolvability check(s)`: dry-run は exec refs をスキップしました。exec の解決可能性検証が必要な場合は `--allow-exec` を付けて再実行してください。
  * batch mode の場合は、失敗したエントリを修正し、書き込む前に `--dry-run` を再実行してください。


## 書き込みの安全性

`openclaw config set` およびその他の OpenClaw 所有の config writer は、disk にコミットする前に変更後の config 全体を検証します。新しい payload が schema validation に失敗した場合、または破壊的な上書きに見える場合、active config はそのまま残され、拒否された payload は隣に `openclaw.json.rejected.*` として保存されます。

小さな編集には CLI 書き込みを推奨します。

bashCopy code
[code]
    openclaw config set gateway.reload.mode hybrid --dry-runopenclaw config set gateway.reload.mode hybridopenclaw config validate
[/code]

書き込みが拒否された場合は、保存された payload を調べ、config 全体の形状を修正してください。

bashCopy code
[code]
    CONFIG="$(openclaw config file)"ls -lt "$CONFIG".rejected.* 2>/dev/null | headopenclaw config validate
[/code]

エディタでの直接書き込みも引き続き許可されますが、実行中の Gateway は検証が通るまでそれらを信頼されないものとして扱います。無効な直接編集は起動に失敗するか、hot reload によってスキップされます。Gateway は `openclaw.json` を書き換えません。prefixed/clobbered config を修復するか、last-known-good copy を復元するには `openclaw doctor --fix` を実行してください。[Gateway troubleshooting](</ja-JP/gateway/troubleshooting#gateway-rejected-invalid-config>) を参照してください。

whole-file recovery は doctor repair 専用です。Plugin schema の変更や `minHostVersion` のずれは、models、providers、auth profiles、channels、gateway exposure、tools、memory、browser、cron config などの無関係なユーザー設定をロールバックするのではなく、明示的に表面化されます。

## サブコマンド

  * `config file`: active config file path (`OPENCLAW_CONFIG_PATH` または既定の場所から解決) を出力します。この path は symlink ではなく通常ファイルを指している必要があります。


編集後に gateway を再起動してください。

## 検証

gateway を起動せずに、現在の config を active schema に対して検証します。

bashCopy code
[code]
    openclaw config validateopenclaw config validate --json
[/code]

`openclaw config validate` が成功するようになったら、同じ terminal で各変更を検証しながら、local TUI を使って埋め込み agent に active config と docs を比較させることができます。

bashCopy code
[code]
    openclaw chat
[/code]

その後、TUI 内で次を実行します。

textCopy code
[code]
    !openclaw config file!openclaw docs gateway auth token secretref!openclaw config validate!openclaw doctor
[/code]

典型的な修復ループ:

* ### docs と比較する

agent に現在の config を関連する docs page と比較させ、最小の修正を提案させます。

* ### 対象を絞った編集を適用する

`openclaw config set` または `openclaw configure` で対象を絞った編集を適用します。

* ### 再検証する

各変更後に `openclaw config validate` を再実行します。

* ### runtime の問題には doctor を使う

検証は通るのに runtime がまだ正常でない場合は、migration と repair の支援のために `openclaw doctor` または `openclaw doctor --fix` を実行します。

## 関連

  * [CLI リファレンス](</ja-JP/cli>)
  * [Configuration](</ja-JP/gateway/configuration>)


Was this useful?YesNo