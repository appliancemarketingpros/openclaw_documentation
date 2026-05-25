---
title: セットアップ
source_url: https://docs.openclaw.ai/ja-JP/cli/setup
scraped_at: 2026-05-25
---

# `openclaw setup`

ベースライン設定とエージェントワークスペースを初期化します。オンボーディングフラグが指定されている場合は、ウィザードも実行します。

## オプション

フラグ | 説明  
---|---  
`--workspace <dir>` | エージェントワークスペースディレクトリ (デフォルトは `~/.openclaw/workspace`; `agents.defaults.workspace` として保存されます)。  
`--wizard` | 対話型オンボーディングを実行します。  
`--non-interactive` | プロンプトなしでオンボーディングを実行します。  
`--mode <mode>` | オンボーディングモード: `local` または `remote`。  
`--import-from <provider>` | オンボーディング中に実行する移行プロバイダー。  
`--import-source <path>` | `--import-from` のソースエージェントホーム。  
`--import-secrets` | オンボーディング移行中に対応しているシークレットをインポートします。  
`--remote-url <url>` | リモート Gateway WebSocket URL。  
`--remote-token <token>` | リモート Gateway トークン (任意)。  
  
### ウィザードの自動トリガー

`openclaw setup` は、`--wizard` がなくても、これらのフラグのいずれかが明示的に指定されている場合にウィザードを実行します。

`--wizard`, `--non-interactive`, `--mode`, `--import-from`, `--import-source`, `--import-secrets`, `--remote-url`, `--remote-token`.

## 例

bashCopy code
[code]
    openclaw setupopenclaw setup --workspace ~/.openclaw/workspaceopenclaw setup --wizardopenclaw setup --wizard --import-from hermes --import-source ~/.hermesopenclaw setup --non-interactive --mode remote --remote-url wss://gateway-host:18789 --remote-token <token>
[/code]

## 注記

  * 単純な `openclaw setup` は、完全なオンボーディングフローを実行せずに設定とワークスペースを初期化します。
  * 単純な setup の後は、完全なガイド付きジャーニーには `openclaw onboard`、対象を絞った変更には `openclaw configure`、チャンネルアカウントの追加には `openclaw channels add` を実行してください。
  * Hermes の状態が検出された場合、対話型オンボーディングは移行を自動的に提案できます。インポートオンボーディングには新規 setup が必要です。オンボーディング外でのドライラン計画、バックアップ、上書きモードには [移行](</ja-JP/cli/migrate>) を使用してください。


## 関連

  * [CLI リファレンス](</ja-JP/cli>)
  * [オンボーディング (CLI)](</ja-JP/start/wizard>)
  * [はじめに](</ja-JP/start/getting-started>)
  * [インストール概要](</ja-JP/install>)


Was this useful?YesNo