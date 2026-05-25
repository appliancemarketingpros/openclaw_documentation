---
title: アンインストール
source_url: https://docs.openclaw.ai/ja-JP/cli/uninstall
scraped_at: 2026-05-25
---

# `openclaw uninstall`

gateway サービスとローカルデータをアンインストールします（CLI 自体は残ります）。

オプション:

  * `--service`: gateway サービスを削除
  * `--state`: 状態と設定を削除
  * `--workspace`: workspace ディレクトリを削除
  * `--app`: macOS アプリを削除
  * `--all`: サービス、状態、workspace、アプリを削除
  * `--yes`: 確認プロンプトをスキップ
  * `--non-interactive`: プロンプトを無効化。`--yes` が必要
  * `--dry-run`: ファイルを削除せず、実行される操作を表示


例:

bashCopy code
[code]
    openclaw backup createopenclaw uninstallopenclaw uninstall --service --yes --non-interactiveopenclaw uninstall --state --workspace --yes --non-interactiveopenclaw uninstall --all --yesopenclaw uninstall --dry-run
[/code]

注記:

  * 状態や workspace を削除する前に復元可能なスナップショットが必要な場合は、先に `openclaw backup create` を実行してください。
  * `--all` は、サービス、状態、workspace、アプリをまとめて削除する短縮形です。
  * `--non-interactive` には `--yes` が必要です。


## 関連

  * [CLI リファレンス](</ja-JP/cli>)
  * [アンインストール](</ja-JP/install/uninstall>)


Was this useful?YesNo