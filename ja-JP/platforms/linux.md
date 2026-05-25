---
title: Linux アプリ
source_url: https://docs.openclaw.ai/ja-JP/platforms/linux
scraped_at: 2026-05-25
---

Gateway は Linux で完全にサポートされています。**Node が推奨ランタイムです** 。 Gateway には Bun は推奨されません (WhatsApp/Telegram の不具合)。

ネイティブ Linux コンパニオンアプリは計画中です。構築を手伝いたい場合はコントリビューションを歓迎します。

## 初心者向けクイックパス (VPS)

  1. Node 24 をインストールします (推奨。Node 22 LTS、現在は `22.16+`、も互換性のため引き続き動作します)
  2. `npm i -g openclaw@latest`
  3. `openclaw onboard --install-daemon`
  4. ラップトップから: `ssh -N -L 18789:127.0.0.1:18789 <user>@<host>`
  5. `http://127.0.0.1:18789/` を開き、設定済みの共有シークレットで認証します (デフォルトではトークン。`gateway.auth.mode: "password"` を設定した場合はパスワード)


完全な Linux サーバーガイド: [Linux サーバー](</ja-JP/vps>)。ステップごとの VPS 例: [exe.dev](</ja-JP/install/exe-dev>)

## インストール

  * [はじめに](</ja-JP/start/getting-started>)
  * [インストールと更新](</ja-JP/install/updating>)
  * 任意のフロー: [Bun (実験的)](</ja-JP/install/bun>)、[Nix](</ja-JP/install/nix>)、[Docker](</ja-JP/install/docker>)


## Gateway

  * [Gateway ランブック](</ja-JP/gateway>)
  * [設定](</ja-JP/gateway/configuration>)


## Gateway サービスのインストール (CLI)

次のいずれかを使用します。

CodeCopy code
[code]
    openclaw onboard --install-daemon
[/code]

または:

CodeCopy code
[code]
    openclaw gateway install
[/code]

または:

CodeCopy code
[code]
    openclaw configure
[/code]

プロンプトが表示されたら **Gateway サービス** を選択します。

修復/移行:

CodeCopy code
[code]
    openclaw doctor
[/code]

## システム制御 (systemd ユーザーユニット)

OpenClaw はデフォルトで systemd **ユーザー** サービスをインストールします。共有サーバーや常時稼働サーバーには **システム** サービスを使用します。`openclaw gateway install` と `openclaw onboard --install-daemon` は、現在の正規ユニットをすでに生成します。 カスタムのシステム/サービスマネージャー構成が必要な場合にのみ手動で作成してください。 完全なサービスガイダンスは [Gateway ランブック](</ja-JP/gateway>) にあります。

最小構成:

`~/.config/systemd/user/openclaw-gateway[-<profile>].service` を作成します。

CodeCopy code
[code]
    [Unit]Description=OpenClaw Gateway (profile: <profile>, v<version>)After=network-online.targetWants=network-online.target [Service]ExecStart=/usr/local/bin/openclaw gateway --port 18789Restart=alwaysRestartSec=5TimeoutStopSec=30TimeoutStartSec=30SuccessExitStatus=0 143KillMode=control-group [Install]WantedBy=default.target
[/code]

有効化します。

CodeCopy code
[code]
    systemctl --user enable --now openclaw-gateway[-<profile>].service
[/code]

## メモリ負荷と OOM kill

Linux では、ホスト、VM、またはコンテナ cgroup がメモリ不足になると、カーネルが OOM の対象プロセスを選択します。Gateway は長時間存続する セッションとチャネル接続を保持しているため、対象としては不適切な場合があります。そのため OpenClaw は、可能な場合は Gateway より前に一時的な子 プロセスが kill されるように調整します。

対象となる Linux の子プロセス起動では、OpenClaw は短い `/bin/sh` ラッパーを通して子プロセスを開始します。このラッパーは子プロセス自身の `oom_score_adj` を `1000` に引き上げてから、 実際のコマンドを `exec` します。子プロセスが自分自身の OOM kill される可能性を上げるだけなので、これは非特権操作です。

対象となる子プロセス面には次が含まれます。

  * スーパーバイザー管理のコマンド子プロセス、
  * PTY シェル子プロセス、
  * MCP stdio サーバー子プロセス、
  * OpenClaw が起動するブラウザー/Chrome プロセス。


このラッパーは Linux 専用で、`/bin/sh` が利用できない場合はスキップされます。 子プロセスの env で `OPENCLAW_CHILD_OOM_SCORE_ADJ=0`、`false`、 `no`、または `off` が設定されている場合もスキップされます。

子プロセスを確認するには:

bashCopy code
[code]
    cat /proc/<child-pid>/oom_score_adj
[/code]

対象の子プロセスで期待される値は `1000` です。Gateway プロセスは通常のスコアを維持する必要があり、通常は `0` です。

これは通常のメモリチューニングの代替にはなりません。VPS またはコンテナが繰り返し 子プロセスを kill する場合は、メモリ上限を増やす、並行処理を減らす、または systemd `MemoryMax=` やコンテナレベルのメモリ上限など、より強い リソース制御を追加してください。

## 関連

  * [インストール概要](</ja-JP/install>)
  * [Linux サーバー](</ja-JP/vps>)
  * [Raspberry Pi](</ja-JP/install/raspberry-pi>)


Was this useful?YesNo