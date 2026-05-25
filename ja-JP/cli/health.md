---
title: ヘルス
source_url: https://docs.openclaw.ai/ja-JP/cli/health
scraped_at: 2026-05-25
---

# `openclaw health`

実行中の Gateway からヘルス情報を取得します。

## オプション

フラグ | デフォルト | 説明  
---|---|---  
`--json` | `false` | テキストではなく機械可読な JSON を出力します。  
`--timeout <ms>` | `10000` | ミリ秒単位の接続タイムアウトです。  
`--verbose` | `false` | 詳細ログを出力します。ライブプローブを強制し、エージェントごとの出力を展開します。  
`--debug` | `false` | `--verbose` のエイリアスです。  
  
例:

bashCopy code
[code]
    openclaw healthopenclaw health --jsonopenclaw health --timeout 2500openclaw health --verboseopenclaw health --debug
[/code]

注記:

  * デフォルトの `openclaw health` は、実行中の Gateway にヘルススナップショットを要求します。 Gateway に新しいキャッシュ済みスナップショットがすでにある場合、そのキャッシュ済みペイロードを返し、 バックグラウンドで更新できます。
  * `--verbose` はライブプローブを強制し、Gateway の接続詳細を出力し、設定済みの すべてのアカウントとエージェントにわたって人間が読める出力を展開します。
  * 複数のエージェントが設定されている場合、出力にはエージェントごとのセッションストアが含まれます。


## 関連

  * [CLI リファレンス](</ja-JP/cli>)
  * [Gateway ヘルス](</ja-JP/gateway/health>)


Was this useful?YesNo