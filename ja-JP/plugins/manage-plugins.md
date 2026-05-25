---
title: Pluginを管理する
source_url: https://docs.openclaw.ai/ja-JP/plugins/manage-plugins
scraped_at: 2026-05-25
---

ほとんどのPluginワークフローは、いくつかのコマンドで完了します。検索、インストール、Gatewayの再起動、検証、そしてPluginが不要になったらアンインストールします。

## Pluginを一覧表示する

bashCopy code
[code]
    openclaw plugins listopenclaw plugins list --enabledopenclaw plugins list --verboseopenclaw plugins list --json
[/code]

スクリプトには `--json` を使用します。これにはレジストリ診断と、Pluginパッケージが `dependencies` または `optionalDependencies` を宣言している場合の各Pluginの静的な `dependencyStatus` が含まれます。

bashCopy code
[code]
    openclaw plugins list --json \  | jq '.plugins[] | {id, enabled, format, source, dependencyStatus}'
[/code]

`plugins list` はコールドインベントリチェックです。OpenClawが設定、マニフェスト、Pluginレジストリから検出できるものを表示します。すでに実行中のGatewayプロセスがPluginランタイムをインポートしたことを証明するものではありません。

## Pluginをインストールする

bashCopy code
[code]
    # Search ClawHub for plugin packages.openclaw plugins search "calendar" # Bare package specs try ClawHub first, then npm fallback.openclaw plugins install <package> # Force one source.openclaw plugins install clawhub:<package>openclaw plugins install npm:<package> # Install a specific version or dist-tag.openclaw plugins install clawhub:<package>@1.2.3openclaw plugins install clawhub:<package>@betaopenclaw plugins install npm:@scope/openclaw-plugin@1.2.3openclaw plugins install npm:@openclaw/codex # Install from git or a local development checkout.openclaw plugins install git:github.com/acme/openclaw-plugin@v1.0.0openclaw plugins install ./my-pluginopenclaw plugins install --link ./my-plugin
[/code]

Pluginコードをインストールした後、チャンネルを提供しているGatewayを再起動します。

bashCopy code
[code]
    openclaw gateway restartopenclaw plugins inspect <plugin-id> --runtime --json
[/code]

ツール、フック、サービス、Gatewayメソッド、Plugin所有のCLIコマンドなど、Pluginがランタイムサーフェスを登録した証拠が必要な場合は、`inspect --runtime` を使用します。

## Pluginを更新する

bashCopy code
[code]
    openclaw plugins update <plugin-id>openclaw plugins update <npm-package-or-spec>openclaw plugins update --all
[/code]

Pluginが `@beta` などのnpm dist-tagからインストールされていた場合、その後の `update <plugin-id>` 呼び出しでは記録済みのタグが再利用されます。明示的なnpm仕様を渡すと、今後の更新で追跡されるインストール先がその仕様に切り替わります。

bashCopy code
[code]
    openclaw plugins update @scope/openclaw-plugin@betaopenclaw plugins update @scope/openclaw-plugin
[/code]

2つ目のコマンドは、以前に正確なバージョンまたはタグに固定されていたPluginを、レジストリのデフォルトのリリースラインに戻します。

`openclaw update` がベータチャンネルで実行されると、デフォルトラインのnpmおよびClawHubのPluginレコードは、まず一致するPluginの `@beta` リリースを試します。そのベータリリースが存在しない場合、OpenClawは記録済みのデフォルト/最新仕様にフォールバックします。npm Pluginの場合、ベータパッケージが存在してもインストール検証に失敗したときにも、OpenClawはフォールバックします。正確なバージョンと、`@rc` や `@beta` などの明示的なタグは保持されます。

## Pluginをアンインストールする

bashCopy code
[code]
    openclaw plugins uninstall <plugin-id> --dry-runopenclaw plugins uninstall <plugin-id>openclaw plugins uninstall <plugin-id> --keep-filesopenclaw gateway restart
[/code]

アンインストールでは、Pluginの設定エントリ、Pluginインデックスレコード、許可/拒否リストのエントリ、および該当する場合はリンク済みのロードパスが削除されます。管理対象のインストールディレクトリは、`--keep-files` を渡さない限り削除されます。

Nixモード（`OPENCLAW_NIX_MODE=1`）では、Pluginのインストール、更新、アンインストール、有効化、無効化コマンドは無効になります。代わりに、そのインストールのNixソースでこれらの選択を管理してください。nix-openclawでは、agent-firstの[クイックスタート](<https://github.com/openclaw/nix-openclaw#quick-start>)を使用します。

## Pluginを公開する

外部Pluginは [ClawHub](<https://clawhub.ai>)、[npmjs.com](<http://npmjs.com>)、またはその両方に公開できます。

### ClawHubに公開する

ClawHubは、OpenClaw Plugin向けの主要な公開ディスカバリーサーフェスです。ユーザーはインストール前に、検索可能なメタデータ、バージョン履歴、レジストリスキャン結果を確認できます。

bashCopy code
[code]
    npm i -g clawhubclawhub loginclawhub package publish your-org/your-plugin --dry-runclawhub package publish your-org/your-pluginclawhub package publish your-org/your-plugin@v1.0.0
[/code]

ユーザーは次の方法でClawHubからインストールします。

bashCopy code
[code]
    openclaw plugins install clawhub:<package>openclaw plugins install <package>
[/code]

裸の形式でも、ClawHubが最初に確認されます。

### npmjs.comに公開する

ネイティブnpm Pluginには、Pluginマニフェストと `package.json` のOpenClawエントリポイントメタデータが必要です。

package.jsonCopy code
[code]
    {  "name": "@acme/openclaw-plugin",  "version": "1.0.0",  "type": "module",  "openclaw": {    "extensions": ["./dist/index.js"]  }}
[/code]

bashCopy code
[code]
    npm publish --access public
[/code]

ユーザーはnpmのみから次の方法でインストールします。

bashCopy code
[code]
    openclaw plugins install npm:@acme/openclaw-pluginopenclaw plugins install npm:@acme/openclaw-plugin@betaopenclaw plugins install npm:@acme/openclaw-plugin@1.0.0
[/code]

同じパッケージがClawHubでも利用可能な場合、`npm:` はClawHub検索をスキップし、npm解決を強制します。

## ソースの選択

  * **ClawHub** : OpenClawネイティブのディスカバリー、スキャン概要、バージョン、インストールヒントが必要な場合に使用します。
  * **[npmjs.com](<http://npmjs.com>)** : すでにJavaScriptパッケージを出荷している場合、またはnpmのdist-tag/プライベートレジストリワークフローが必要な場合に使用します。
  * **Git** : ブランチ、タグ、またはコミットから直接インストールしたい場合に使用します。
  * **ローカルパス** : 同じマシン上でPluginを開発またはテストしている場合に使用します。


## 関連

  * [Plugins](</ja-JP/tools/plugin>) \- 概要とトラブルシューティング
  * [`openclaw plugins`](</ja-JP/cli/plugins>) \- 完全なCLIリファレンス
  * [ClawHub](</ja-JP/clawhub/cli>) \- 公開とレジストリ操作
  * [Pluginの構築](</ja-JP/plugins/building-plugins>) \- Pluginパッケージを作成する
  * [Pluginマニフェスト](</ja-JP/plugins/manifest>) \- マニフェストとパッケージメタデータ


Was this useful?YesNo