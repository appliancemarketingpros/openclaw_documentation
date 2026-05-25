---
title: 移行ガイド
source_url: https://docs.openclaw.ai/ja-JP/install/migrating
scraped_at: 2026-05-25
---

OpenClaw は 3 つの移行パスをサポートしています。別のエージェントシステムからのインポート、既存インストールの新しいマシンへの移動、Plugin のインプレースアップグレードです。

## 別のエージェントシステムからインポートする

同梱の移行プロバイダーを使って、指示、MCP サーバー、Skills、モデル設定、（オプトインの）API キーを OpenClaw に取り込めます。変更前にプランがプレビューされ、レポートではシークレットが伏せ字になり、適用は検証済みバックアップによって保護されます。

[**Claude からの移行** `CLAUDE.md`、MCP サーバー、Skills、プロジェクトコマンドを含む Claude Code と Claude Desktop の状態をインポートします。 ](</ja-JP/install/migrating-claude>) [**Hermes からの移行** Hermes の設定、プロバイダー、MCP サーバー、メモリ、Skills、サポートされる `.env` キーをインポートします。 ](</ja-JP/install/migrating-hermes>)

CLI のエントリーポイントは [`openclaw migrate`](</ja-JP/cli/migrate>) です。オンボーディングでも、既知のソースが検出された場合に移行を提案できます（`openclaw onboard --flow import`）。

## OpenClaw を新しいマシンに移動する

**状態ディレクトリ** （デフォルトは `~/.openclaw/`）と**ワークスペース** をコピーして、次のものを保持します。

  * **設定** — `openclaw.json` とすべての Gateway 設定。
  * **認証** — エージェントごとの `auth-profiles.json`（API キーと OAuth）、および `credentials/` 配下のチャネルまたはプロバイダーの状態。
  * **セッション** — 会話履歴とエージェント状態。
  * **チャネル状態** — WhatsApp ログイン、Telegram セッションなど。
  * **ワークスペースファイル** — `MEMORY.md`、`USER.md`、Skills、プロンプト。


### 移行手順

* ### Gateway を停止してバックアップする

**古い** マシンで、コピー中にファイルが変更されないよう Gateway を停止してから、アーカイブを作成します。

bashCopy code
[code]
    openclaw gateway stopcd ~tar -czf openclaw-state.tgz .openclaw
[/code]

複数のプロファイル（例: `~/.openclaw-work`）を使っている場合は、それぞれを個別にアーカイブしてください。

* ### 新しいマシンに OpenClaw をインストールする

新しいマシンに CLI（必要に応じて Node も）を[インストール](</ja-JP/install>)します。オンボーディングによって新しい `~/.openclaw/` が作成されても問題ありません。次の手順で上書きします。

* ### 状態ディレクトリとワークスペースをコピーする

`scp`、`rsync -a`、または外部ドライブでアーカイブを転送し、展開します。

bashCopy code
[code]
    cd ~tar -xzf openclaw-state.tgz
[/code]

隠しディレクトリが含まれていること、ファイル所有者が Gateway を実行するユーザーと一致していることを確認してください。

* ### Doctor を実行して検証する

新しいマシンで [Doctor](</ja-JP/gateway/doctor>) を実行し、設定移行の適用とサービス修復を行います。

bashCopy code
[code]
    openclaw doctoropenclaw gateway restartopenclaw status
[/code]

Telegram または Discord がデフォルトの環境変数フォールバック（`TELEGRAM_BOT_TOKEN` または `DISCORD_BOT_TOKEN`）を使っている場合は、シークレット値を出力せずに、移行後の状態ディレクトリの `.env` にそれらのキーが含まれていることを確認します。

bashCopy code
[code]
    awk -F= '/^(TELEGRAM_BOT_TOKEN|DISCORD_BOT_TOKEN)=/ { print $1 "=present" }' ~/.openclaw/.env
[/code]

`openclaw doctor` は、有効なデフォルトの Telegram または Discord アカウントに設定済みトークンがなく、対応する環境変数を doctor プロセスから利用できない場合にも警告します。

### よくある落とし穴

プロファイルまたは状態ディレクトリの不一致

古い Gateway が `--profile` または `OPENCLAW_STATE_DIR` を使っていて、新しい Gateway が使っていない場合、チャネルはログアウト状態に見え、セッションは空になります。移行したものと**同じ** プロファイルまたは状態ディレクトリで Gateway を起動し、その後 `openclaw doctor` を再実行してください。

openclaw.json だけをコピーしている

設定ファイルだけでは不十分です。モデル認証プロファイルは `agents/<agentId>/agent/auth-profiles.json` 配下にあり、チャネルとプロバイダーの状態は `credentials/` 配下にあります。常に**状態ディレクトリ全体** を移行してください。

権限と所有者

root としてコピーした場合やユーザーを切り替えた場合、Gateway が認証情報を読み取れないことがあります。状態ディレクトリとワークスペースが、Gateway を実行するユーザーによって所有されていることを確認してください。

リモートモード

UI が**リモート** Gateway を指している場合、セッションとワークスペースを所有しているのはリモートホストです。ローカルのノート PC ではなく、Gateway ホスト自体を移行してください。[FAQ](</ja-JP/help/faq#where-things-live-on-disk>) を参照してください。

バックアップ内のシークレット

状態ディレクトリには、認証プロファイル、チャネル認証情報、その他のプロバイダー状態が含まれます。バックアップは暗号化して保存し、安全でない転送チャネルを避け、露出が疑われる場合はキーをローテーションしてください。

### 検証チェックリスト

新しいマシンで、次を確認します。

  * [ ] `openclaw status` で Gateway が実行中と表示される。
  * [ ] チャネルが引き続き接続されている（再ペアリング不要）。
  * [ ] ダッシュボードが開き、既存のセッションが表示される。
  * [ ] ワークスペースファイル（メモリ、設定）が存在する。


## Plugin をインプレースでアップグレードする

インプレース Plugin アップグレードでは、同じ Plugin ID と設定キーを保持しつつ、ディスク上の状態を現在のレイアウトへ移動する場合があります。Plugin 固有のアップグレードガイドは、それぞれのチャネルの近くにあります。

  * [Matrix 移行](</ja-JP/channels/matrix-migration>): 暗号化された状態の復旧制限、自動スナップショット動作、手動復旧コマンド。


## 関連

  * [`openclaw migrate`](</ja-JP/cli/migrate>): システム間インポートの CLI リファレンス。
  * [インストール概要](</ja-JP/install>): すべてのインストール方法。
  * [Doctor](</ja-JP/gateway/doctor>): 移行後のヘルスチェック。
  * [アンインストール](</ja-JP/install/uninstall>): OpenClaw をきれいに削除する。


Was this useful?YesNo