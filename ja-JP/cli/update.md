---
title: 更新
source_url: https://docs.openclaw.ai/ja-JP/cli/update
scraped_at: 2026-05-25
---

# `openclaw update`

OpenClaw を安全に更新し、stable/beta/dev チャンネルを切り替えます。

**npm/pnpm/bun** 経由でインストールした場合（グローバルインストールで、git メタデータなし）、 更新は [更新](</ja-JP/install/updating>) のパッケージマネージャーフローで行われます。

## 使用方法

bashCopy code
[code]
    openclaw updateopenclaw update statusopenclaw update wizardopenclaw update --channel betaopenclaw update --channel devopenclaw update --tag betaopenclaw update --tag mainopenclaw update --dry-runopenclaw update --no-restartopenclaw update --yesopenclaw update --jsonopenclaw --update
[/code]

## オプション

  * `--no-restart`: 更新が成功した後に Gateway サービスの再起動をスキップします。Gateway を再起動するパッケージマネージャー更新では、コマンドが成功する前に、再起動後のサービスが想定された更新済みバージョンを報告することを検証します。
  * `--channel <stable|beta|dev>`: 更新チャンネルを設定します（git + npm。config に永続化されます）。
  * `--tag <dist-tag|version|spec>`: この更新に限り、パッケージターゲットを上書きします。パッケージインストールでは、`main` は `github:openclaw/openclaw#main` にマップされます。
  * `--dry-run`: config の書き込み、インストール、plugins の同期、再起動を行わずに、予定されている更新アクション（チャンネル/タグ/ターゲット/再起動フロー）をプレビューします。
  * `--json`: 機械判読可能な `UpdateRunResult` JSON を出力します。これには、 破損またはロード不能な管理対象 plugins がコア更新の成功後に 修復を必要とする場合の `postUpdate.plugins.warnings`、plugin に beta リリースがない場合の beta チャンネル plugin フォールバック詳細、更新後の plugin 同期中に npm plugin アーティファクトのドリフトが検出された場合の `postUpdate.plugins.integrityDrifts` が含まれます。
  * `--timeout <seconds>`: ステップごとのタイムアウト（デフォルトは 1800s）。
  * `--yes`: 確認プロンプト（たとえばダウングレード確認）をスキップします。


`openclaw update` には `--verbose` フラグはありません。予定されている チャンネル/タグ/インストール/再起動アクションをプレビューするには `--dry-run` を、 機械判読可能な結果には `--json` を、チャンネルと可用性の詳細だけが必要な場合は `openclaw update status --json` を使用します。更新前後の Gateway ログをデバッグしている場合、 コンソールの詳細度とファイルログレベルは別です。Gateway `--verbose` は ターミナル/WebSocket 出力に影響しますが、ファイルログには config の `logging.level: "debug"` または `"trace"` が必要です。[Gateway ログ](</ja-JP/gateway/logging>)を参照してください。

## `update status`

アクティブな更新チャンネル + git タグ/ブランチ/SHA（ソース checkout の場合）と、更新の可用性を表示します。

bashCopy code
[code]
    openclaw update statusopenclaw update status --jsonopenclaw update status --timeout 10
[/code]

オプション:

  * `--json`: 機械判読可能なステータス JSON を出力します。
  * `--timeout <seconds>`: チェックのタイムアウト（デフォルトは 3s）。


## `update wizard`

更新チャンネルを選択し、更新後に Gateway を再起動するかどうかを確認する 対話型フローです（デフォルトは再起動）。git checkout なしで `dev` を選択した場合は、 作成するかどうかを提示します。

オプション:

  * `--timeout <seconds>`: 各更新ステップのタイムアウト（デフォルト `1800`）


## 実行内容

チャンネルを明示的に切り替えると（`--channel ...`）、OpenClaw は インストール方法も整合させます。

  * `dev` → git checkout を確保し（デフォルト: `~/openclaw`、`OPENCLAW_GIT_DIR` で上書き）、 それを更新して、その checkout からグローバル CLI をインストールします。
  * `stable` → `latest` を使用して npm からインストールします。
  * `beta` → npm dist-tag `beta` を優先しますが、beta が 存在しない、または現在の stable リリースより古い場合は `latest` にフォールバックします。


Gateway コア自動アップデーター（config で有効な場合）は、稼働中の Gateway リクエストハンドラーの外で CLI 更新パスを起動します。コントロールプレーンの `update.run` パッケージマネージャー 更新は、パッケージ差し替え後に遅延なし、クールダウンなしの更新再起動を強制します。 古い Gateway プロセスが、新しいパッケージで削除されたファイルを指す メモリ内チャンクをまだ保持している可能性があるためです。

パッケージマネージャーインストールでは、`openclaw update` はパッケージマネージャーを呼び出す前に ターゲットパッケージのバージョンを解決します。npm グローバルインストールはステージングされた インストールを使用します。OpenClaw は新しいパッケージを一時 npm prefix にインストールし、 そこでパッケージ済みの `dist` インベントリを検証してから、そのクリーンなパッケージツリーを 実際のグローバル prefix に差し替えます。検証に失敗した場合、更新後の doctor、plugin 同期、 再起動作業は疑わしいツリーから実行されません。インストール済みバージョンが すでにターゲットと一致している場合でも、コマンドはグローバルパッケージインストールを更新し、 その後 plugin 同期、コアコマンド補完の更新、再起動作業を実行します。これにより、 パッケージ済み sidecar とチャンネル所有の plugin レコードを インストール済み OpenClaw ビルドと整合させつつ、完全な plugin コマンド補完の再構築は 明示的な `openclaw completion --write-state` 実行に残します。

ローカル管理対象 Gateway サービスがインストールされており、再起動が有効な場合、 パッケージマネージャー更新は、パッケージツリーを置き換える前に実行中のサービスを停止し、 更新済みインストールからサービスメタデータを更新し、サービスを再起動して、 再起動後の Gateway が想定されたバージョンを報告することを検証してから 成功を報告します。macOS では、更新後チェックで、アクティブプロファイルの LaunchAgent が ロード/実行中であり、設定済みの loopback ポートが 正常であることも検証します。plist がインストールされているのに launchd が監視していない場合、 OpenClaw は LaunchAgent を自動的に再ブートストラップし、その後 健全性/バージョン/チャンネル準備状態チェックを再実行します。新規ブートストラップでは RunAtLoad ジョブが直接ロードされるため、更新リカバリーは新しく 生成された Gateway に対して即座に `kickstart -k` を実行しません。Gateway がそれでも正常にならない場合、 コマンドは非ゼロで終了し、再起動ログパスに加えて、明示的な再起動、再インストール、 パッケージロールバック手順を出力します。`--no-restart` を指定した場合、 パッケージ置換は実行されますが、管理対象サービスは停止も 再起動もされないため、手動で再起動するまで、実行中の Gateway は古いコードを保持する可能性があります。

## Git checkout フロー

### チャンネル選択

  * `stable`: 最新の非 beta タグを checkout し、その後 build と doctor を実行します。
  * `beta`: 最新の `-beta` タグを優先しますが、beta が存在しない、または古い場合は最新の stable タグにフォールバックします。
  * `dev`: `main` を checkout し、その後 fetch と rebase を実行します。


### 更新ステップ

* ### クリーンな worktree を検証

未コミットの変更がないことが必要です。

* ### チャンネルを切り替え

選択したチャンネル（タグまたはブランチ）に切り替えます。

* ### upstream を fetch

Dev のみ。

* ### preflight build（dev のみ）

一時 worktree で TypeScript build を実行します。tip が失敗した場合、最大 10 commits までさかのぼって、build 可能な最新 commit を探します。この preflight 中に lint も実行するには `OPENCLAW_UPDATE_PREFLIGHT_LINT=1` を設定します。ユーザーの更新ホストは CI runners より小さいことが多いため、lint は制約された serial mode で実行されます。

* ### Rebase

選択した commit に rebase します（dev のみ）。

* ### 依存関係をインストール

リポジトリのパッケージマネージャーを使用します。pnpm checkout では、updater は pnpm workspace 内で `npm run build` を実行する代わりに、必要に応じて（まず `corepack`、次に一時的な `npm install pnpm@11` フォールバックで）`pnpm` をブートストラップします。

* ### Control UI を build

gateway と Control UI を build します。

* ### doctor を実行

最後の安全更新チェックとして `openclaw doctor` が実行されます。

* ### plugins を同期

plugins をアクティブチャンネルに同期します。Dev は同梱 plugins を使用し、stable と beta は npm を使用します。追跡対象の plugin インストールを更新します。

beta 更新チャンネルでは、default/latest ラインに従う追跡対象の npm および ClawHub plugin インストールは、 まず plugin `@beta` リリースを試します。plugin に beta リリースがない場合、 OpenClaw は記録済みの default/latest spec にフォールバックし、それを警告として報告します。 npm plugins では、beta パッケージが存在しても install validation に失敗した場合にも OpenClaw はフォールバックします。これらの plugin フォールバック警告によって コア更新が失敗することはありません。正確なバージョンと明示的なタグは 書き換えられません。

## `--update` 省略形

`openclaw --update` は `openclaw update` に書き換えられます（shell や launcher scripts に便利です）。

## 関連

  * `openclaw doctor`（git checkout では、先に update を実行することを提案します）
  * [開発チャンネル](</ja-JP/install/development-channels>)
  * [更新](</ja-JP/install/updating>)
  * [CLI リファレンス](</ja-JP/cli>)


Was this useful?YesNo