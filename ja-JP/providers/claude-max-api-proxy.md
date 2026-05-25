---
title: Claude Max APIプロキシ
source_url: https://docs.openclaw.ai/ja-JP/providers/claude-max-api-proxy
scraped_at: 2026-05-25
---

**claude-max-api-proxy** は、Claude Max/ProサブスクリプションをOpenAI互換APIエンドポイントとして公開するコミュニティツールです。これにより、OpenAI API形式をサポートする任意のツールで、そのサブスクリプションを使えるようになります。

## なぜこれを使うのか？

アプローチ | コスト | 向いている用途  
---|---|---  
Anthropic API | トークン課金（Opusで入力 ~$15/M、出力 ~$75/M） | 本番アプリ、大量利用  
Claude Max subscription | 月額$200の定額 | 個人利用、開発、無制限利用  
  
Claude Maxサブスクリプションを持っていて、OpenAI互換ツールで使いたい場合、このプロキシは一部ワークフローでコスト削減につながる可能性があります。本番利用では、API keyのほうがより明確なポリシー経路のままです。

## 仕組み

CodeCopy code
[code]
    Your App → claude-max-api-proxy → Claude Code CLI → Anthropic (via subscription)     (OpenAI format)              (converts format)      (uses your login)
[/code]

このプロキシは次を行います。

  1. `http://localhost:3456/v1/chat/completions`でOpenAI形式のリクエストを受け付ける
  2. それをClaude Code CLIコマンドへ変換する
  3. OpenAI形式でレスポンスを返す（ストリーミング対応）


## はじめに

* ### プロキシをインストールする

Node.js 20+とClaude Code CLIが必要です。

bashCopy code
[code]
    npm install -g claude-max-api-proxy # Claude CLIが認証済みであることを確認claude --version
[/code]

* ### サーバーを起動する

bashCopy code
[code]
    claude-max-api# サーバーは http://localhost:3456 で動作
[/code]

* ### プロキシをテストする

bashCopy code
[code]
    # ヘルスチェックcurl http://localhost:3456/health # モデル一覧curl http://localhost:3456/v1/models # Chat completioncurl http://localhost:3456/v1/chat/completions \  -H "Content-Type: application/json" \  -d '{    "model": "claude-opus-4",    "messages": [{"role": "user", "content": "Hello!"}]  }'
[/code]

* ### OpenClawを設定する

プロキシを、カスタムOpenAI互換エンドポイントとしてOpenClawへ向けます。

json5Copy code
[code]
    {  env: {    OPENAI_API_KEY: "not-needed",    OPENAI_BASE_URL: "http://localhost:3456/v1",  },  agents: {    defaults: {      model: { primary: "openai/claude-opus-4" },    },  },}
[/code]

## 組み込みカタログ

モデルID | 対応先  
---|---  
`claude-opus-4` | Claude Opus 4  
`claude-sonnet-4` | Claude Sonnet 4  
`claude-haiku-4` | Claude Haiku 4  
  
## 高度な設定

プロキシ型OpenAI互換に関する注意

この経路は、他のカスタム `/v1`バックエンドと同じプロキシ型OpenAI互換ルートを使います。

  * ネイティブOpenAI専用のリクエスト整形は適用されません
  * `service_tier`、Responsesの`store`、prompt-cacheヒント、および OpenAI reasoning互換ペイロード整形はありません
  * 隠されたOpenClaw attributionヘッダー（`originator`、`version`、`User-Agent`） はプロキシURLには注入されません

macOSでLaunchAgentによる自動起動

プロキシを自動実行するLaunchAgentを作成します。

bashCopy code
[code]
    cat > ~/Library/LaunchAgents/com.claude-max-api.plist << 'EOF'<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd"><plist version="1.0"><dict>  <key>Label</key>  <string>com.claude-max-api</string>  <key>RunAtLoad</key>  <true/>  <key>KeepAlive</key>  <true/>  <key>ProgramArguments</key>  <array>    <string>/usr/local/bin/node</string>    <string>/usr/local/lib/node_modules/claude-max-api-proxy/dist/server/standalone.js</string>  </array>  <key>EnvironmentVariables</key>  <dict>    <key>PATH</key>    <string>/usr/local/bin:/opt/homebrew/bin:~/.local/bin:/usr/bin:/bin</string>  </dict></dict></plist>EOF launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.claude-max-api.plist
[/code]

## リンク

  * **npm:** <https://www.npmjs.com/package/claude-max-api-proxy>
  * **GitHub:** <https://github.com/atalovesyou/claude-max-api-proxy>
  * **Issues:** <https://github.com/atalovesyou/claude-max-api-proxy/issues>


## 注意

  * これは**コミュニティツール** であり、AnthropicまたはOpenClawの公式サポート対象ではありません
  * Claude Code CLIが認証済みで、アクティブなClaude Max/Proサブスクリプションが必要です
  * プロキシはローカルで動作し、データをサードパーティサーバーへ送信しません
  * ストリーミングレスポンスは完全にサポートされています


## 関連

[**Anthropic provider** Claude CLIまたはAPI keyによるネイティブOpenClaw連携。 ](</ja-JP/providers/anthropic>) [**OpenAI provider** OpenAI/Codexサブスクリプション向け。 ](</ja-JP/providers/openai>) [**Model selection** すべてのプロバイダー、モデル参照、およびフェイルオーバー動作の概要。 ](</ja-JP/concepts/model-providers>) [**Configuration** 完全な設定リファレンス。 ](</ja-JP/gateway/configuration>)

Was this useful?YesNo