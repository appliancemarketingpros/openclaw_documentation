---
title: リセット
source_url: https://docs.openclaw.ai/ja-JP/cli/reset
scraped_at: 2026-05-25
---

# `openclaw reset`

ローカルの設定/状態をリセットします（CLIはインストールされたままです）。

オプション:

  * `--scope <scope>`: `config`、`config+creds+sessions`、または`full`
  * `--yes`: 確認プロンプトをスキップ
  * `--non-interactive`: プロンプトを無効化。`--scope`と`--yes`が必要
  * `--dry-run`: ファイルを削除せずに実行内容を表示


例:

bashCopy code
[code]
    openclaw backup createopenclaw resetopenclaw reset --dry-runopenclaw reset --scope config --yes --non-interactiveopenclaw reset --scope config+creds+sessions --yes --non-interactiveopenclaw reset --scope full --yes --non-interactive
[/code]

注意:

  * ローカル状態を削除する前に復元可能なスナップショットが欲しい場合は、先に`openclaw backup create`を実行してください。
  * `--scope`を省略すると、`openclaw reset`は対話型プロンプトを使用して削除対象を選択します。
  * `--non-interactive`は、`--scope`と`--yes`の両方が設定されている場合のみ有効です。


## 関連

  * [CLI reference](</ja-JP/cli>)


Was this useful?YesNo