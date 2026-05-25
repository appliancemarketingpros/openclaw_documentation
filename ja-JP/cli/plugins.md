---
title: Plugin
source_url: https://docs.openclaw.ai/ja-JP/cli/plugins
scraped_at: 2026-05-25
---

Gateway plugins、hook packs、互換バンドルを管理します。

[**Plugin システム** plugins のインストール、有効化、トラブルシューティングに関するエンドユーザー向けガイド。 ](</ja-JP/tools/plugin>) [**plugins の管理** インストール、一覧表示、更新、アンインストール、公開の簡単な例。 ](</ja-JP/plugins/manage-plugins>) [**Plugin バンドル** バンドル互換性モデル。 ](</ja-JP/plugins/bundles>) [**Plugin マニフェスト** マニフェストフィールドと設定スキーマ。 ](</ja-JP/plugins/manifest>) [**セキュリティ** Plugin インストールのセキュリティ強化。 ](</ja-JP/gateway/security>)

## コマンド

bashCopy code
[code]
    openclaw plugins listopenclaw plugins list --enabledopenclaw plugins list --verboseopenclaw plugins list --jsonopenclaw plugins search <query>openclaw plugins search <query> --limit 20openclaw plugins search <query> --jsonopenclaw plugins install <path-or-spec>openclaw plugins inspect <id>openclaw plugins inspect <id> --runtimeopenclaw plugins inspect <id> --jsonopenclaw plugins inspect --allopenclaw plugins info <id>openclaw plugins enable <id>openclaw plugins disable <id>openclaw plugins registryopenclaw plugins registry --refreshopenclaw plugins uninstall <id>openclaw plugins doctoropenclaw plugins update <id-or-npm-spec>openclaw plugins update --allopenclaw plugins marketplace list <marketplace>openclaw plugins marketplace list <marketplace> --json
[/code]

遅いインストール、検査、アンインストール、またはレジストリ更新の調査では、 `OPENCLAW_PLUGIN_LIFECYCLE_TRACE=1` を付けてコマンドを実行します。トレースはフェーズごとのタイミングを stderr に書き込み、 JSON 出力は解析可能なままにします。[デバッグ](</ja-JP/help/debugging#plugin-lifecycle-trace>)を参照してください。

### インストール

bashCopy code
[code]
    openclaw plugins search "calendar"                   # search ClawHub pluginsopenclaw plugins install <package>                      # npm by defaultopenclaw plugins install clawhub:<package>              # ClawHub onlyopenclaw plugins install npm:<package>                  # npm onlyopenclaw plugins install npm-pack:<path.tgz>            # local npm pack through npm install semanticsopenclaw plugins install git:github.com/<owner>/<repo>  # git repoopenclaw plugins install git:github.com/<owner>/<repo>@<ref>openclaw plugins install <package> --force              # overwrite existing installopenclaw plugins install <package> --pin                # pin versionopenclaw plugins install <package> --dangerously-force-unsafe-installopenclaw plugins install <path>                         # local pathopenclaw plugins install <plugin>@<marketplace>         # marketplaceopenclaw plugins install <plugin> --marketplace <name>  # marketplace (explicit)openclaw plugins install <plugin> --marketplace https://github.com/<owner>/<repo>
[/code]

セットアップ時インストールをテストするメンテナーは、保護された環境変数で自動 Plugin インストールソースを上書きできます。 [Plugin インストールの上書き](</ja-JP/plugins/install-overrides>)を参照してください。

`plugins search` は ClawHub にインストール可能な Plugin パッケージを問い合わせ、 インストール可能なパッケージ名を出力します。検索対象はコード Plugin とバンドル Plugin のパッケージであり、Skills ではありません。ClawHub Skills には `openclaw skills search` を使用してください。

Config includes と無効な設定の修復

`plugins` セクションが単一ファイルの `$include` によって裏付けられている場合、`plugins install/update/enable/disable/uninstall` はそのインクルード先ファイルへ書き込み、`openclaw.json` は変更しません。ルート include、include 配列、兄弟上書き付き include は、フラット化せずフェイルクローズします。サポートされる形状については[設定 includes](</ja-JP/gateway/configuration>)を参照してください。

インストール中に設定が無効な場合、`plugins install` は通常フェイルクローズし、先に `openclaw doctor --fix` を実行するよう通知します。Gateway 起動時とホットリロード時には、無効な Plugin 設定は他の無効な設定と同様にフェイルクローズします。`openclaw doctor --fix` は無効な Plugin エントリを隔離できます。文書化されている唯一のインストール時例外は、`openclaw.install.allowInvalidConfigRecovery` に明示的にオプトインする plugins 向けの狭いバンドル済み Plugin 復旧経路です。

\--force と再インストール、update の違い

`--force` は既存のインストール先を再利用し、すでにインストール済みの Plugin または hook pack をその場で上書きします。同じ id を新しいローカルパス、アーカイブ、ClawHub パッケージ、または npm アーティファクトから意図的に再インストールする場合に使用します。すでに追跡されている npm Plugin の通常のアップグレードには、`openclaw plugins update <id-or-npm-spec>` を推奨します。

すでにインストール済みの Plugin id に対して `plugins install` を実行すると、OpenClaw は停止し、通常のアップグレードには `plugins update <id-or-npm-spec>` を案内し、現在のインストールを別ソースから本当に上書きしたい場合には `plugins install <package> --force` を案内します。

\--pin のスコープ

`--pin` は npm インストールにのみ適用されます。`git:` インストールではサポートされません。ソースを固定したい場合は、`git:github.com/acme/plugin@v1.2.3` のような明示的な git ref を使用してください。`--marketplace` でもサポートされません。マーケットプレイスインストールは npm spec ではなく、マーケットプレイスソースのメタデータを永続化するためです。

\--dangerously-force-unsafe-install

`--dangerously-force-unsafe-install` は、組み込みの危険コードスキャナーで誤検知が発生した場合の緊急用オプションです。組み込みスキャナーが `critical` の検出結果を報告してもインストールの続行を許可しますが、Plugin の `before_install` フックポリシーブロックはバイパスせず、スキャン失敗もバイパスしません。

この CLI フラグは Plugin の install/update フローに適用されます。Gateway ベースの Skill 依存関係インストールでは、対応する `dangerouslyForceUnsafeInstall` リクエスト上書きを使用します。一方、`openclaw skills install` は別個の ClawHub Skill ダウンロード/インストールフローのままです。

ClawHub で公開した Plugin がレジストリスキャンでブロックされた場合は、[ClawHub](</ja-JP/clawhub/security>) の公開者向け手順を使用してください。

Hook packs と npm specs

`plugins install` は、`package.json` で `openclaw.hooks` を公開する hook packs のインストールサーフェスでもあります。パッケージインストールではなく、フィルタ済みの hook 可視性と hook ごとの有効化には `openclaw hooks` を使用してください。

Npm specs は**レジストリ専用** です（パッケージ名 + 任意の**正確なバージョン** または **dist-tag** ）。Git/URL/file specs と semver 範囲は拒否されます。依存関係インストールは、シェルにグローバル npm インストール設定がある場合でも、安全のため project-local で `--ignore-scripts` を付けて実行されます。管理対象 Plugin の npm ルートは OpenClaw のパッケージレベル npm `overrides` を継承するため、ホストのセキュリティピンは巻き上げられた Plugin 依存関係にも適用されます。

npm 解決を明示したい場合は `npm:<package>` を使用してください。ローンチ移行期間中は、ベアパッケージ specs も npm から直接インストールされます。

ベア specs と `@latest` は安定版トラックに留まります。`2026.5.3-1` のような OpenClaw の日付付き補正版は、このチェックでは安定版リリースです。npm がそれらのいずれかをプレリリースに解決した場合、OpenClaw は停止し、`@beta`/`@rc` のようなプレリリースタグまたは `@1.2.3-beta.4` のような正確なプレリリースバージョンで明示的にオプトインするよう求めます。

ベアインストール spec が公式 Plugin id（例: `diffs`）に一致する場合、OpenClaw はカタログエントリを直接インストールします。同じ名前の npm パッケージをインストールするには、明示的なスコープ付き spec（例: `@scope/diffs`）を使用してください。

Git リポジトリ

git リポジトリから直接インストールするには `git:<repo>` を使用します。サポートされる形式には、`git:github.com/owner/repo`、`git:owner/repo`、完全な `https://`、`ssh://`、`git://`、`file://`、および `git@host:owner/repo.git` クローン URL が含まれます。インストール前にブランチ、タグ、またはコミットをチェックアウトするには、`@<ref>` または `#<ref>` を追加します。

Git インストールは一時ディレクトリへクローンし、指定された ref がある場合はそれをチェックアウトしてから、通常の Plugin ディレクトリインストーラーを使用します。つまり、マニフェスト検証、危険コードスキャン、パッケージマネージャーのインストール作業、インストール記録は npm インストールと同じように動作します。記録された git インストールには、ソース URL/ref と解決済みコミットが含まれるため、`openclaw plugins update` は後でソースを再解決できます。

git からインストールした後は、`openclaw plugins inspect <id> --runtime --json` を使用して、gateway メソッドや CLI コマンドなどのランタイム登録を検証します。Plugin が `api.registerCli` で CLI ルートを登録した場合は、OpenClaw ルート CLI からそのコマンドを直接実行します。例: `openclaw demo-plugin ping`。

アーカイブ

サポートされるアーカイブ: `.zip`、`.tgz`、`.tar.gz`、`.tar`。ネイティブ OpenClaw Plugin アーカイブには、展開された Plugin ルートに有効な `openclaw.plugin.json` が含まれている必要があります。`package.json` のみを含むアーカイブは、OpenClaw がインストール記録を書き込む前に拒否されます。

ファイルが npm-pack tarball であり、レジストリインストールで使用されるものと同じ管理対象 npm ルートのインストール経路をテストしたい場合は、 `npm-pack:<path.tgz>` を使用します。 これには `package-lock.json` 検証、巻き上げられた依存関係のスキャン、 npm インストール記録が含まれます。プレーンなアーカイブパスは引き続き、Plugin extensions ルート配下にローカルアーカイブとしてインストールされます。

Claude マーケットプレイスインストールもサポートされています。

ClawHub インストールは、明示的な `clawhub:<package>` ロケーターを使用します。

bashCopy code
[code]
    openclaw plugins install clawhub:openclaw-codex-app-serveropenclaw plugins install clawhub:openclaw-codex-app-server@1.2.3
[/code]

ベア npm-safe Plugin specs は、ローンチ移行期間中はデフォルトで npm からインストールされます。

bashCopy code
[code]
    openclaw plugins install openclaw-codex-app-server
[/code]

npm 専用解決を明示するには `npm:` を使用します。

bashCopy code
[code]
    openclaw plugins install npm:openclaw-codex-app-serveropenclaw plugins install npm:@scope/plugin-name@1.0.1
[/code]

OpenClaw は、インストール前に公開されている Plugin API / 最小 Gateway 互換性を確認します。選択した ClawHub バージョンが ClawPack アーティファクトを公開している場合、OpenClaw はバージョン付き npm-pack `.tgz` をダウンロードし、ClawHub ダイジェストヘッダーとアーティファクトダイジェストを検証してから、通常のアーカイブパスを通じてインストールします。ClawPack メタデータのない古い ClawHub バージョンは、引き続きレガシーなパッケージアーカイブ検証パスを通じてインストールされます。記録済みインストールは、後続の更新のために ClawHub ソースメタデータ、アーティファクト種別、npm integrity、npm shasum、tarball 名、ClawPack ダイジェスト情報を保持します。 バージョン指定なしの ClawHub インストールは、バージョン指定なしの記録済み spec を保持するため、`openclaw plugins update` は新しい ClawHub リリースを追従できます。`clawhub:pkg@1.2.3` や `clawhub:pkg@beta` などの明示的なバージョンまたはタグセレクタは、そのセレクタに固定されたままです。

#### マーケットプレイス省略記法

マーケットプレイス名が Claude のローカルレジストリキャッシュ `~/.claude/plugins/known_marketplaces.json` に存在する場合は、`plugin@marketplace` 省略記法を使用します。

bashCopy code
[code]
    openclaw plugins marketplace list <marketplace-name>openclaw plugins install <plugin-name>@<marketplace-name>
[/code]

マーケットプレイスソースを明示的に渡したい場合は、`--marketplace` を使用します。

bashCopy code
[code]
    openclaw plugins install <plugin-name> --marketplace <marketplace-name>openclaw plugins install <plugin-name> --marketplace <owner/repo>openclaw plugins install <plugin-name> --marketplace https://github.com/<owner>/<repo>openclaw plugins install <plugin-name> --marketplace ./my-marketplace
[/code]

### マーケットプレイスソース

  * `~/.claude/plugins/known_marketplaces.json` にある Claude の既知マーケットプレイス名
  * ローカルマーケットプレイスルートまたは `marketplace.json` パス
  * `owner/repo` のような GitHub リポジトリ省略記法
  * `https://github.com/owner/repo` のような GitHub リポジトリ URL
  * git URL


### リモートマーケットプレイスのルール

GitHub または git から読み込まれるリモートマーケットプレイスでは、Plugin エントリはクローンされたマーケットプレイスリポジトリ内にとどまる必要があります。OpenClaw はそのリポジトリからの相対パスソースを受け入れ、リモートマニフェスト内の HTTP(S)、絶対パス、git、GitHub、その他の非パス Plugin ソースを拒否します。

ローカルパスとアーカイブについて、OpenClaw は以下を自動検出します。

  * ネイティブ OpenClaw Plugin (`openclaw.plugin.json`)
  * Codex 互換バンドル (`.codex-plugin/plugin.json`)
  * Claude 互換バンドル (`.claude-plugin/plugin.json` またはデフォルトの Claude コンポーネントレイアウト)
  * Cursor 互換バンドル (`.cursor-plugin/plugin.json`)


### 一覧表示

bashCopy code
[code]
    openclaw plugins listopenclaw plugins list --enabledopenclaw plugins list --verboseopenclaw plugins list --jsonopenclaw plugins search <query>openclaw plugins search <query> --limit 20openclaw plugins search <query> --json
[/code]

有効化された Plugin のみを表示します。

テーブル表示から、ソース/オリジン/バージョン/有効化メタデータを含む Plugin ごとの詳細行に切り替えます。

機械可読なインベントリに加え、レジストリ診断とパッケージ依存関係のインストール状態を出力します。

`plugins search` はリモート ClawHub カタログ検索です。ローカル状態の検査、config の変更、パッケージのインストール、Plugin ランタイムコードの読み込みは行いません。検索結果には、ClawHub パッケージ名、ファミリー、チャネル、バージョン、概要、`openclaw plugins install clawhub:<package>` のようなインストールヒントが含まれます。

パッケージ化された Docker イメージ内でバンドル Plugin を扱う場合は、Plugin ソースディレクトリを、`/app/extensions/synology-chat` のような対応するパッケージ化済みソースパスの上に bind-mount します。OpenClaw は、そのマウントされたソースオーバーレイを `/app/dist/extensions/synology-chat` より前に検出します。単にコピーされたソースディレクトリは inert のままなので、通常のパッケージ化済みインストールは引き続きコンパイル済み dist を使用します。

ランタイム hook のデバッグには、次を使用します。

  * `openclaw plugins inspect <id> --runtime --json` は、モジュール読み込み済みの検査パスから登録済み hook と診断を表示します。ランタイム検査は依存関係をインストールしません。レガシーな依存関係状態をクリーンアップする、または config から参照されているダウンロード可能な Plugin の欠落を回復するには、`openclaw doctor --fix` を使用してください。
  * `openclaw gateway status --deep --require-rpc` は、到達可能な Gateway、サービス/プロセスヒント、config パス、RPC ヘルスを確認します。
  * 非バンドル会話 hook (`llm_input`, `llm_output`, `before_model_resolve`, `before_agent_reply`, `before_agent_run`, `before_agent_finalize`, `agent_end`) には `plugins.entries.<id>.hooks.allowConversationAccess=true` が必要です。


ローカルディレクトリのコピーを避けるには、`--link` を使用します (`plugins.load.paths` に追加されます)。

bashCopy code
[code]
    openclaw plugins install -l ./my-plugin
[/code]

### Plugin インデックス

Plugin インストールメタデータは、ユーザー config ではなく、機械管理の状態です。インストールと更新は、アクティブな OpenClaw 状態ディレクトリ配下の `plugins/installs.json` に書き込みます。そのトップレベルの `installRecords` マップは、壊れた Plugin マニフェストや欠落している Plugin マニフェストの記録を含む、インストールメタデータの永続的なソースです。`plugins` 配列は、マニフェストから派生したコールドレジストリキャッシュです。このファイルには編集禁止の警告が含まれ、`openclaw plugins update`、uninstall、診断、コールド Plugin レジストリで使用されます。

OpenClaw が config 内に同梱済みレガシー `plugins.installs` レコードを見つけた場合、ランタイム読み取りはそれらを `openclaw.json` を書き換えずに互換性入力として扱います。明示的な Plugin 書き込みと `openclaw doctor --fix` は、config 書き込みが許可されている場合、それらのレコードを Plugin インデックスへ移動し、config キーを削除します。いずれかの書き込みに失敗した場合、インストールメタデータが失われないように config レコードは保持されます。

### アンインストール

bashCopy code
[code]
    openclaw plugins uninstall <id>openclaw plugins uninstall <id> --dry-runopenclaw plugins uninstall <id> --keep-files
[/code]

`uninstall` は、`plugins.entries`、永続化された Plugin インデックス、Plugin allow/deny list エントリ、該当する場合はリンクされた `plugins.load.paths` エントリから Plugin レコードを削除します。`--keep-files` が設定されていない限り、uninstall は、OpenClaw の Plugin extensions ルート内にある追跡済み管理対象インストールディレクトリも削除します。Active Memory Plugin の場合、メモリスロットは `memory-core` にリセットされます。

### 更新

bashCopy code
[code]
    openclaw plugins update <id-or-npm-spec>openclaw plugins update --allopenclaw plugins update <id-or-npm-spec> --dry-runopenclaw plugins update @openclaw/voice-callopenclaw plugins update openclaw-codex-app-server --dangerously-force-unsafe-install
[/code]

更新は、管理対象 Plugin インデックス内の追跡済み Plugin インストールと、`hooks.internal.installs` 内の追跡済み hook-pack インストールに適用されます。

Plugin id と npm spec の解決

Plugin id を渡すと、OpenClaw はその Plugin に記録されたインストール spec を再利用します。つまり、以前に保存された `@beta` のような dist-tag や正確に固定されたバージョンは、後続の `update <id>` 実行でも引き続き使用されます。

npm インストールの場合は、dist-tag または正確なバージョンを含む明示的な npm パッケージ spec を渡すこともできます。OpenClaw はそのパッケージ名を追跡済み Plugin レコードに解決し、そのインストール済み Plugin を更新して、将来の id ベースの更新のために新しい npm spec を記録します。

バージョンやタグのない npm パッケージ名を渡した場合も、追跡済み Plugin レコードに解決されます。Plugin が正確なバージョンに固定されていて、レジストリのデフォルトリリースラインへ戻したい場合に使用します。

ベータチャネル更新

`openclaw plugins update` は、新しい spec を渡さない限り、追跡済み Plugin spec を再利用します。`openclaw update` はさらに、アクティブな OpenClaw 更新チャネルを認識します。ベータチャネルでは、デフォルトラインの npm および ClawHub Plugin レコードはまず `@beta` を試し、Plugin ベータリリースが存在しない場合は、記録済みの default/latest spec にフォールバックします。そのフォールバックは警告として報告され、コア更新を失敗させることはありません。正確なバージョンと明示的なタグは、そのセレクタに固定されたままです。

バージョン確認と integrity drift

ライブ npm 更新の前に、OpenClaw はインストール済みパッケージバージョンを npm レジストリメタデータと照合します。インストール済みバージョンと記録済みアーティファクト identity が、解決済みターゲットとすでに一致している場合、更新はダウンロード、再インストール、`openclaw.json` の書き換えなしでスキップされます。

保存済み integrity ハッシュが存在し、取得したアーティファクトハッシュが変わっている場合、OpenClaw はそれを npm アーティファクト drift として扱います。対話型の `openclaw plugins update` コマンドは、期待値と実際のハッシュを出力し、続行前に確認を求めます。非対話型の更新ヘルパーは、呼び出し元が明示的な継続ポリシーを指定しない限り fail closed します。

更新時の --dangerously-force-unsafe-install

`--dangerously-force-unsafe-install` は、Plugin 更新中に組み込みの危険コードスキャンが誤検知した場合の break-glass override として、`plugins update` でも利用できます。ただし、Plugin の `before_install` ポリシーブロックやスキャン失敗によるブロックは引き続きバイパスせず、Plugin 更新にのみ適用され、hook-pack 更新には適用されません。

### 検査

bashCopy code
[code]
    openclaw plugins inspect <id>openclaw plugins inspect <id> --runtimeopenclaw plugins inspect <id> --json
[/code]

Inspect は、デフォルトでは Plugin ランタイムを import せずに、identity、読み込み状態、ソース、マニフェスト機能、ポリシーフラグ、診断、インストールメタデータ、バンドル機能、検出された MCP または LSP サーバーサポートを表示します。Plugin モジュールを読み込み、登録済み hook、tool、command、service、gateway method、HTTP route を含めるには、`--runtime` を追加します。ランタイム検査は不足している Plugin 依存関係を直接報告します。インストールと修復は `openclaw plugins install`、`openclaw plugins update`、`openclaw doctor --fix` に残ります。

Plugin が所有する CLI コマンドは通常、ルート `openclaw` コマンドグループとしてインストールされますが、Plugin は `openclaw nodes` のようなコア親の下にネストされたコマンドを登録することもできます。`inspect --runtime` が `cliCommands` の下にコマンドを表示したら、一覧にあるパスで実行します。たとえば、`demo-git` を登録する Plugin は `openclaw demo-git ping` で検証できます。

各 Plugin は、ランタイムで実際に登録する内容によって分類されます:

  * **plain-capability** — 1 つの capability 種別（例: provider 専用 plugin）
  * **hybrid-capability** — 複数の capability 種別（例: テキスト + 音声 + 画像）
  * **hook-only** — hook のみで、capabilities や surfaces はない
  * **non-capability** — tools/commands/services はあるが capabilities はない


capability モデルの詳細は [Plugin 形状](</ja-JP/plugins/architecture#plugin-shapes>) を参照してください。

### Doctor

bashCopy code
[code]
    openclaw plugins doctor
[/code]

`doctor` は plugin の読み込みエラー、manifest/discovery 診断、compatibility notices を報告します。すべてが問題なければ `No plugin issues detected.` と表示します。

設定済みの plugin がディスク上に存在するものの、loader の path-safety チェックでブロックされている場合、config validation は plugin entry を保持し、`present but blocked` として報告します。`plugins.entries.<id>` や `plugins.allow` config を削除するのではなく、path ownership や world-writable permissions など、先行する blocked-plugin 診断を修正してください。

`register`/`activate` exports の欠落など module-shape の失敗については、`OPENCLAW_PLUGIN_LOAD_DEBUG=1` を指定して再実行すると、診断出力に compact な export-shape summary が含まれます。

### Registry

bashCopy code
[code]
    openclaw plugins registryopenclaw plugins registry --refreshopenclaw plugins registry --json
[/code]

ローカル plugin registry は、インストール済み plugin の identity、enablement、source metadata、contribution ownership に関する OpenClaw の永続化された cold read model です。通常の startup、provider owner lookup、channel setup classification、plugin inventory は、plugin runtime modules を import せずにこれを読み取れます。

永続化された registry が存在するか、最新か、古くなっているかを確認するには `plugins registry` を使用します。永続化された plugin index、config policy、manifest/package metadata から再構築するには `--refresh` を使用します。これは修復 path であり、runtime activation path ではありません。

`openclaw doctor --fix` は registry-adjacent な managed npm drift も修復します。managed plugin npm root 配下の孤立または復旧された `@openclaw/*` package が bundled plugin をシャドウしている場合、doctor はその古い package を削除し、startup が bundled manifest に対して検証されるよう registry を再構築します。Doctor はまた、`peerDependencies.openclaw` を宣言する managed npm plugins に host `openclaw` package を再リンクするため、更新や npm 修復の後でも `openclaw/plugin-sdk/*` などの package-local runtime imports が解決されます。

### Marketplace

bashCopy code
[code]
    openclaw plugins marketplace list <source>openclaw plugins marketplace list <source> --json
[/code]

Marketplace list は、ローカル marketplace path、`marketplace.json` path、`owner/repo` のような GitHub shorthand、GitHub repo URL、または git URL を受け付けます。`--json` は、解決された source label に加えて、解析された marketplace manifest と plugin entries を出力します。

## 関連

  * [Plugin の構築](</ja-JP/plugins/building-plugins>)
  * [CLI リファレンス](</ja-JP/cli>)
  * [ClawHub](</ja-JP/clawhub>)


Was this useful?YesNo