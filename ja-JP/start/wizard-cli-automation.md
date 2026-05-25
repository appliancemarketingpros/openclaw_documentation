---
title: CLI 自動化
source_url: https://docs.openclaw.ai/ja-JP/start/wizard-cli-automation
scraped_at: 2026-05-25
---

`openclaw onboard` を自動化するには `--non-interactive` を使用します。

## ベースラインの非対話例

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice apiKey \  --anthropic-api-key "$ANTHROPIC_API_KEY" \  --secret-input-mode plaintext \  --gateway-port 18789 \  --gateway-bind loopback \  --install-daemon \  --daemon-runtime node \  --skip-bootstrap \  --skip-skills
[/code]

機械可読の概要を出力するには `--json` を追加します。

自動化でワークスペースファイルを事前に用意しており、オンボーディングでデフォルトのブートストラップファイルを作成したくない場合は、`--skip-bootstrap` を使用します。

プレーンテキスト値の代わりに、環境変数に基づく参照を認証プロファイルに保存するには `--secret-input-mode ref` を使用します。 環境変数参照と、設定済みプロバイダー参照（`file` または `exec`）の対話的な選択は、オンボーディングフローで利用できます。

非対話の `ref` モードでは、プロバイダーの環境変数がプロセス環境に設定されている必要があります。 対応する環境変数なしでインラインのキーフラグを渡すと、ただちに失敗するようになりました。

例:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice openai-api-key \  --secret-input-mode ref \  --accept-risk
[/code]

## プロバイダー別の例

Anthropic APIキーの例 bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice apiKey \  --anthropic-api-key "$ANTHROPIC_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Geminiの例 bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice gemini-api-key \  --gemini-api-key "$GEMINI_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Z.AIの例 bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice zai-api-key \  --zai-api-key "$ZAI_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Vercel AI Gatewayの例 bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice ai-gateway-api-key \  --ai-gateway-api-key "$AI_GATEWAY_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Cloudflare AI Gatewayの例 bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice cloudflare-ai-gateway-api-key \  --cloudflare-ai-gateway-account-id "your-account-id" \  --cloudflare-ai-gateway-gateway-id "your-gateway-id" \  --cloudflare-ai-gateway-api-key "$CLOUDFLARE_AI_GATEWAY_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Moonshotの例 bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice moonshot-api-key \  --moonshot-api-key "$MOONSHOT_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Mistralの例 bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice mistral-api-key \  --mistral-api-key "$MISTRAL_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Syntheticの例 bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice synthetic-api-key \  --synthetic-api-key "$SYNTHETIC_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

OpenCodeの例 bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice opencode-zen \  --opencode-zen-api-key "$OPENCODE_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Goカタログには `--auth-choice opencode-go --opencode-go-api-key "$OPENCODE_API_KEY"` に切り替えます。

Ollamaの例 bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice ollama \  --custom-model-id "qwen3.5:27b" \  --accept-risk \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

カスタムプロバイダーの例 bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice custom-api-key \  --custom-base-url "https://llm.example.com/v1" \  --custom-model-id "foo-large" \  --custom-api-key "$CUSTOM_API_KEY" \  --custom-provider-id "my-custom" \  --custom-compatibility anthropic \  --custom-image-input \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

`--custom-api-key` は任意です。省略すると、オンボーディングは `CUSTOM_API_KEY` を確認します。 OpenClaw は一般的なビジョンモデルIDを、画像対応として自動的にマークします。不明なカスタムビジョンIDには `--custom-image-input` を追加し、テキストのみのメタデータを強制するには `--custom-text-input` を追加します。

参照モードのバリエーション:

bashCopy code
[code]
    export CUSTOM_API_KEY="your-key"openclaw onboard --non-interactive \  --mode local \  --auth-choice custom-api-key \  --custom-base-url "https://llm.example.com/v1" \  --custom-model-id "foo-large" \  --secret-input-mode ref \  --custom-provider-id "my-custom" \  --custom-compatibility anthropic \  --custom-image-input \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

このモードでは、オンボーディングは `apiKey` を `{ source: "env", provider: "default", id: "CUSTOM_API_KEY" }` として保存します。

Anthropic setup-token は、サポートされているオンボーディングトークンパスとして引き続き利用できますが、OpenClaw は利用可能な場合、Claude CLI の再利用を優先するようになりました。 本番環境では、Anthropic APIキーを推奨します。

## 別のエージェントを追加する

`openclaw agents add <name>` を使用して、独自のワークスペース、セッション、認証プロファイルを持つ別個のエージェントを作成します。 `--workspace` なしで実行すると、ウィザードが起動します。

bashCopy code
[code]
    openclaw agents add work \  --workspace ~/.openclaw/workspace-work \  --model openai/gpt-5.5 \  --bind whatsapp:biz \  --non-interactive \  --json
[/code]

設定される内容:

  * `agents.list[].name`
  * `agents.list[].workspace`
  * `agents.list[].agentDir`


注記:

  * デフォルトのワークスペースは `~/.openclaw/workspace-<agentId>` に従います。
  * 受信メッセージをルーティングするには `bindings` を追加します（ウィザードでも可能です）。
  * 非対話フラグ: `--model`, `--agent-dir`, `--bind`, `--non-interactive`.


## 関連ドキュメント

  * オンボーディングハブ: [オンボーディング（CLI）](</ja-JP/start/wizard>)
  * 完全なリファレンス: [CLIセットアップリファレンス](</ja-JP/start/wizard-cli-reference>)
  * コマンドリファレンス: [`openclaw onboard`](</ja-JP/cli/onboard>)


Was this useful?YesNo