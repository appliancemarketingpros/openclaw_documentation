---
title: Venice AI
source_url: https://docs.openclaw.ai/ja-JP/providers/venice
scraped_at: 2026-05-25
---

Venice AI は、検閲なしモデルのサポートと、匿名化プロキシ経由で主要なプロプライエタリモデルへアクセスできる、**プライバシー重視の AI 推論** を提供します。すべての推論はデフォルトでプライベートです。あなたのデータで学習せず、ログも記録しません。

## OpenClaw で Venice を使う理由

  * オープンソースモデル向けの**プライベート推論** （ログ記録なし）。
  * 必要な場合に使える**検閲なしモデル** 。
  * 品質が重要な場合の、プロプライエタリモデル（Opus/GPT/Gemini）への**匿名化アクセス** 。
  * OpenAI 互換の `/v1` エンドポイント。


## プライバシーモード

Venice は 2 つのプライバシーレベルを提供します。これを理解することが、モデル選択の鍵です。

モード | 説明 | モデル  
---|---|---  
**プライベート** | 完全にプライベートです。プロンプト/応答は**保存もログ記録も一切されません** 。一時的です。 | Llama, Qwen, DeepSeek, Kimi, MiniMax, Venice Uncensored など。  
**匿名化** | メタデータを除去したうえで Venice 経由でプロキシされます。基盤プロバイダー（OpenAI, Anthropic, Google, xAI）は匿名化されたリクエストを受け取ります。 | Claude, GPT, Gemini, Grok  
  
## 機能

  * **プライバシー重視** : 「プライベート」（完全にプライベート）モードと「匿名化」（プロキシ）モードを選択可能
  * **検閲なしモデル** : コンテンツ制限のないモデルへアクセス
  * **主要モデルへのアクセス** : Venice の匿名化プロキシ経由で Claude, GPT, Gemini, Grok を使用
  * **OpenAI 互換 API** : 簡単に統合できる標準の `/v1` エンドポイント
  * **ストリーミング** : すべてのモデルでサポート
  * **関数呼び出し** : 一部のモデルでサポート（モデル機能を確認してください）
  * **Vision** : Vision 機能を持つモデルでサポート
  * **厳密なレート制限なし** : 極端な使用ではフェアユースのスロットリングが適用される場合があります


## はじめに

* ### API キーを取得する

  1. [venice.ai](<https://venice.ai>) でサインアップします
  2. **Settings > API Keys > Create new key** に移動します
  3. API キーをコピーします（形式: `vapi_xxxxxxxxxxxx`）


* ### OpenClaw を設定する

好みのセットアップ方法を選択します。

### 対話型（推奨）

bashCopy code
[code]
    openclaw onboard --auth-choice venice-api-key
[/code]

これにより次のことが行われます。

  1. API キーの入力を求めます（または既存の `VENICE_API_KEY` を使用します）
  2. 利用可能なすべての Venice モデルを表示します
  3. デフォルトモデルを選択できます
  4. プロバイダーを自動的に設定します


### 環境変数

bashCopy code
[code]
    export VENICE_API_KEY="vapi_xxxxxxxxxxxx"
[/code]

### 非対話型

bashCopy code
[code]
    openclaw onboard --non-interactive \  --auth-choice venice-api-key \  --venice-api-key "vapi_xxxxxxxxxxxx"
[/code]

* ### セットアップを確認する

bashCopy code
[code]
    openclaw agent --model venice/kimi-k2-5 --message "Hello, are you working?"
[/code]

## モデル選択

セットアップ後、OpenClaw は利用可能なすべての Venice モデルを表示します。用途に基づいて選択してください。

  * **デフォルトモデル** : 強力なプライベート推論と Vision を備えた `venice/kimi-k2-5`。
  * **高機能オプション** : Venice の最も強力な匿名化経路を使う `venice/claude-opus-4-6`。
  * **プライバシー** : 完全にプライベートな推論には「プライベート」モデルを選択します。
  * **機能** : Venice のプロキシ経由で Claude, GPT, Gemini にアクセスするには「匿名化」モデルを選択します。


デフォルトモデルはいつでも変更できます。

bashCopy code
[code]
    openclaw models set venice/kimi-k2-5openclaw models set venice/claude-opus-4-6
[/code]

利用可能なすべてのモデルを一覧表示します。

bashCopy code
[code]
    openclaw models list --all --provider venice
[/code]

`openclaw configure` を実行し、**Model/auth** を選択して、**Venice AI** を選ぶこともできます。

## DeepSeek V4 のリプレイ動作

Venice が `venice/deepseek-v4-pro` や `venice/deepseek-v4-flash` などの DeepSeek V4 モデルを公開している場合、プロキシがそれを省略したときに、OpenClaw はアシスタントメッセージ上の必須 DeepSeek V4 `reasoning_content` リプレイプレースホルダーを補完します。Venice は DeepSeek ネイティブのトップレベル `thinking` 制御を拒否するため、OpenClaw はそのプロバイダー固有のリプレイ修正を、ネイティブ DeepSeek プロバイダーの thinking 制御とは分離して扱います。

## 組み込みカタログ（合計 41）

プライベートモデル（26）— 完全にプライベート、ログ記録なし モデル ID | 名前 | コンテキスト | 機能  
---|---|---|---  
`kimi-k2-5` | Kimi K2.5 | 256k | デフォルト、推論、Vision  
`kimi-k2-thinking` | Kimi K2 Thinking | 256k | 推論  
`llama-3.3-70b` | Llama 3.3 70B | 128k | 汎用  
`llama-3.2-3b` | Llama 3.2 3B | 128k | 汎用  
`hermes-3-llama-3.1-405b` | Hermes 3 Llama 3.1 405B | 128k | 汎用、ツール無効  
`qwen3-235b-a22b-thinking-2507` | Qwen3 235B Thinking | 128k | 推論  
`qwen3-235b-a22b-instruct-2507` | Qwen3 235B Instruct | 128k | 汎用  
`qwen3-coder-480b-a35b-instruct` | Qwen3 Coder 480B | 256k | コーディング  
`qwen3-coder-480b-a35b-instruct-turbo` | Qwen3 Coder 480B Turbo | 256k | コーディング  
`qwen3-5-35b-a3b` | Qwen3.5 35B A3B | 256k | 推論、Vision  
`qwen3-next-80b` | Qwen3 Next 80B | 256k | 汎用  
`qwen3-vl-235b-a22b` | Qwen3 VL 235B (Vision) | 256k | Vision  
`qwen3-4b` | Venice Small (Qwen3 4B) | 32k | 高速、推論  
`deepseek-v3.2` | DeepSeek V3.2 | 160k | 推論、ツール無効  
`venice-uncensored` | Venice Uncensored (Dolphin-Mistral) | 32k | 検閲なし、ツール無効  
`mistral-31-24b` | Venice Medium (Mistral) | 128k | Vision  
`google-gemma-3-27b-it` | Google Gemma 3 27B Instruct | 198k | Vision  
`openai-gpt-oss-120b` | OpenAI GPT OSS 120B | 128k | 汎用  
`nvidia-nemotron-3-nano-30b-a3b` | NVIDIA Nemotron 3 Nano 30B | 128k | 汎用  
`olafangensan-glm-4.7-flash-heretic` | GLM 4.7 Flash Heretic | 128k | 推論  
`zai-org-glm-4.6` | GLM 4.6 | 198k | 汎用  
`zai-org-glm-4.7` | GLM 4.7 | 198k | 推論  
`zai-org-glm-4.7-flash` | GLM 4.7 Flash | 128k | 推論  
`zai-org-glm-5` | GLM 5 | 198k | 推論  
`minimax-m21` | MiniMax M2.1 | 198k | 推論  
`minimax-m25` | MiniMax M2.5 | 198k | 推論  
匿名化モデル（15）— Venice プロキシ経由 モデル ID | 名前 | コンテキスト | 機能  
---|---|---|---  
`claude-opus-4-6` | Claude Opus 4.6 (via Venice) | 1M | 推論、Vision  
`claude-opus-4-5` | Claude Opus 4.5 (via Venice) | 198k | 推論、Vision  
`claude-sonnet-4-6` | Claude Sonnet 4.6 (via Venice) | 1M | 推論、Vision  
`claude-sonnet-4-5` | Claude Sonnet 4.5 (via Venice) | 198k | 推論、Vision  
`openai-gpt-54` | GPT-5.4 (via Venice) | 1M | 推論、Vision  
`openai-gpt-53-codex` | GPT-5.3 Codex (via Venice) | 400k | 推論、Vision、コーディング  
`openai-gpt-52` | GPT-5.2 (via Venice) | 256k | 推論  
`openai-gpt-52-codex` | GPT-5.2 Codex (via Venice) | 256k | 推論、Vision、コーディング  
`openai-gpt-4o-2024-11-20` | GPT-4o (via Venice) | 128k | Vision  
`openai-gpt-4o-mini-2024-07-18` | GPT-4o Mini (via Venice) | 128k | Vision  
`gemini-3-1-pro-preview` | Gemini 3.1 Pro (via Venice) | 1M | 推論、Vision  
`gemini-3-pro-preview` | Gemini 3 Pro (via Venice) | 198k | 推論、Vision  
`gemini-3-flash-preview` | Gemini 3 Flash (via Venice) | 256k | 推論、Vision  
`grok-41-fast` | Grok 4.1 Fast (via Venice) | 1M | 推論、Vision  
`grok-code-fast-1` | Grok Code Fast 1 (via Venice) | 256k | 推論、コーディング  
  
## モデル検出

OpenClaw には、読み取り専用のモデル一覧表示向けに、マニフェストを基にした Venice のシードカタログが付属しています。ランタイム更新では引き続き Venice API からモデルを検出でき、API に到達できない場合はマニフェストカタログにフォールバックします。

`/models` エンドポイントは公開されています（一覧表示に認証は不要）が、推論には有効な API キーが必要です。

## ストリーミングとツールサポート

機能 | 対応  
---|---  
**ストリーミング** | すべてのモデル  
**関数呼び出し** | ほとんどのモデル（API の `supportsFunctionCalling` を確認）  
**Vision/画像** | 「Vision」機能付きとしてマークされたモデル  
**JSON モード** | `response_format` 経由で対応  
  
## 料金

Venice はクレジットベースのシステムを使用します。現在の料金は [venice.ai/pricing](<https://venice.ai/pricing>) を確認してください。

  * **プライベートモデル** : 一般に低コスト
  * **匿名化モデル** : 直接 API 料金 + 少額の Venice 手数料に近い


### Venice（匿名化）と直接 API の比較

観点 | Venice（匿名化） | 直接 API  
---|---|---  
**プライバシー** | メタデータを削除し、匿名化 | 自分のアカウントに紐づく  
**レイテンシ** | +10-50ms（プロキシ） | 直接  
**機能** | ほとんどの機能に対応 | すべての機能  
**課金** | Venice クレジット | プロバイダー課金  
  
## 使用例

bashCopy code
[code]
    # Use the default private modelopenclaw agent --model venice/kimi-k2-5 --message "Quick health check" # Use Claude Opus via Venice (anonymized)openclaw agent --model venice/claude-opus-4-6 --message "Summarize this task" # Use uncensored modelopenclaw agent --model venice/venice-uncensored --message "Draft options" # Use vision model with imageopenclaw agent --model venice/qwen3-vl-235b-a22b --message "Review attached image" # Use coding modelopenclaw agent --model venice/qwen3-coder-480b-a35b-instruct --message "Refactor this function"
[/code]

## トラブルシューティング

API キーが認識されない bashCopy code
[code]
    echo $VENICE_API_KEYopenclaw models list | grep venice
[/code]

キーが `vapi_` で始まっていることを確認してください。

モデルを利用できない

Venice のモデルカタログは動的に更新されます。現在利用可能なモデルを確認するには、`openclaw models list` を実行してください。一部のモデルは一時的にオフラインになっている場合があります。

接続の問題

Venice API は `https://api.venice.ai/api/v1` にあります。ネットワークで HTTPS 接続が許可されていることを確認してください。

## 高度な設定

設定ファイルの例 json5Copy code
[code]
    {  env: { VENICE_API_KEY: "vapi_..." },  agents: { defaults: { model: { primary: "venice/kimi-k2-5" } } },  models: {    mode: "merge",    providers: {      venice: {        baseUrl: "https://api.venice.ai/api/v1",        apiKey: "${VENICE_API_KEY}",        api: "openai-completions",        models: [          {            id: "kimi-k2-5",            name: "Kimi K2.5",            reasoning: true,            input: ["text", "image"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 256000,            maxTokens: 65536,          },        ],      },    },  },}
[/code]

## 関連

[**モデル選択** プロバイダー、モデル参照、フェイルオーバー動作の選択。 ](</ja-JP/concepts/model-providers>) [**Venice AI** Venice AI のホームページとアカウント登録。 ](<https://venice.ai>) [**API ドキュメント** Venice API リファレンスと開発者向けドキュメント。 ](<https://docs.venice.ai>) [**料金** 現在の Venice クレジット料金とプラン。 ](<https://venice.ai/pricing>)

Was this useful?YesNo