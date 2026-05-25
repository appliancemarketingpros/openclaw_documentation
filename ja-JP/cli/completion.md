---
title: 補完
source_url: https://docs.openclaw.ai/ja-JP/cli/completion
scraped_at: 2026-05-25
---

# `openclaw completion`

シェル補完スクリプトを生成し、必要に応じてシェルプロファイルにインストールします。

## 使用法

bashCopy code
[code]
    openclaw completionopenclaw completion --shell zshopenclaw completion --installopenclaw completion --shell fish --installopenclaw completion --write-stateopenclaw completion --shell bash --write-state
[/code]

## オプション

  * `-s, --shell <shell>`: 対象シェル（`zsh`、`bash`、`powershell`、`fish`。デフォルト: `zsh`）
  * `-i, --install`: source 行をシェルプロファイルに追加して補完をインストールします
  * `--write-state`: スクリプトを stdout に出力せず、補完スクリプトを `$OPENCLAW_STATE_DIR/completions` に書き込みます
  * `-y, --yes`: インストール確認プロンプトをスキップします


## 注

  * `--install` は、シェルプロファイルに小さな「OpenClaw Completion」ブロックを書き込み、キャッシュされたスクリプトを参照するようにします。
  * `--install` または `--write-state` を指定しない場合、このコマンドはスクリプトを stdout に出力します。
  * 補完生成ではコマンドツリーを事前に読み込むため、ネストされたサブコマンドも含まれます。


## 関連

  * [CLI リファレンス](</ja-JP/cli>)


Was this useful?YesNo