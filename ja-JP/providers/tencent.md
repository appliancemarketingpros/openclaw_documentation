---
title: Tencent Cloud (TokenHub)
source_url: https://docs.openclaw.ai/ja-JP/providers/tencent
scraped_at: 2026-05-25
---

Tencent Cloud は OpenClaw にバンドルされたプロバイダー Plugin として提供されます。TokenHub エンドポイント (`tencent-tokenhub`) を通じて、OpenAI 互換 API で Tencent Hy3 preview にアクセスできます。

プロパティ | 値  
---|---  
プロバイダー ID | `tencent-tokenhub`  
Plugin | バンドル済み、`enabledByDefault: true`  
認証環境変数 | `TOKENHUB_API_KEY`  
オンボーディングフラグ | `--auth-choice tokenhub-api-key`  
直接 CLI フラグ | `--tokenhub-api-key <key>`  
API | OpenAI 互換 (`openai-completions`)  
デフォルト base URL | `https://tokenhub.tencentmaas.com/v1`  
グローバル base URL | `https://tokenhub-intl.tencentmaas.com/v1` (上書き)  
デフォルトモデル | `tencent-tokenhub/hy3-preview`  
  
## クイックスタート

* ### TokenHub API キーを作成する

Tencent Cloud TokenHub で API キーを作成します。キーに制限付きアクセススコープを選択する場合は、許可モデルに **Hy3 preview** を含めてください。

* ### オンボーディングを実行する

OnboardingCopy code
[code]
    openclaw onboard --auth-choice tokenhub-api-key
[/code]

Direct flagCopy code
[code]
    openclaw onboard --non-interactive \--auth-choice tokenhub-api-key \--tokenhub-api-key "$TOKENHUB_API_KEY"
[/code]

Env onlyCopy code
[code]
    export TOKENHUB_API_KEY=...
[/code]

* ### モデルを確認する

bashCopy code
[code]
    openclaw models list --provider tencent-tokenhub
[/code]

## 非対話セットアップ

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice tokenhub-api-key \  --tokenhub-api-key "$TOKENHUB_API_KEY" \  --skip-health \  --accept-risk
[/code]

## 組み込みカタログ

モデル参照 | 名前 | 入力 | コンテキスト | 最大出力 | 注記  
---|---|---|---|---|---  
`tencent-tokenhub/hy3-preview` | Hy3 preview (TokenHub) | text | 256,000 | 64,000 | デフォルト。reasoning 対応  
  
Hy3 preview は、reasoning、長いコンテキストでの指示追従、コード、エージェントワークフロー向けの Tencent Hunyuan の大規模 MoE 言語モデルです。Tencent の OpenAI 互換の例では、モデル ID として `hy3-preview` を使用し、標準の chat-completions ツール呼び出しと `reasoning_effort` をサポートしています。

## 段階制料金

バンドルされたカタログには、入力ウィンドウ長に応じてスケールする段階制コストメタデータが含まれているため、手動の上書きなしでコスト見積もりが入力されます。

入力トークン範囲 | 入力レート | 出力レート | キャッシュ読み取り  
---|---|---|---  
0 - 16,000 | 0.176 | 0.587 | 0.059  
16,000 - 32,000 | 0.235 | 0.939 | 0.088  
32,000+ | 0.293 | 1.173 | 0.117  
  
レートは Tencent が公表している USD 建ての 100 万トークンあたりの価格です。異なるサーフェスが必要な場合にのみ、`models.providers.tencent-tokenhub` の下で料金を上書きしてください。

## 詳細設定

エンドポイントの上書き

OpenClaw はデフォルトで Tencent Cloud の `https://tokenhub.tencentmaas.com/v1` エンドポイントを使用します。Tencent は国際向け TokenHub エンドポイントも文書化しています。

bashCopy code
[code]
    openclaw config set models.providers.tencent-tokenhub.baseUrl "https://tokenhub-intl.tencentmaas.com/v1"
[/code]

TokenHub アカウントまたはリージョンで必要な場合にのみ、エンドポイントを上書きしてください。

デーモン向けの環境利用可能性

Gateway が管理サービス (launchd、systemd、Docker) として実行される場合、`TOKENHUB_API_KEY` はそのプロセスから見える必要があります。launchd、systemd、または Docker exec 環境が読み取れるように、`~/.openclaw/.env` または `env.shellEnv` 経由で設定してください。

## 関連

[**モデルプロバイダー** プロバイダー、モデル参照、フェイルオーバー動作の選択。 ](</ja-JP/concepts/model-providers>) [**設定リファレンス** プロバイダー設定を含む完全な設定スキーマ。 ](</ja-JP/gateway/configuration>) [**Tencent TokenHub** Tencent Cloud の TokenHub 製品ページ。 ](<https://cloud.tencent.com/product/tokenhub>) [**Hy3 preview モデルカード** Tencent Hunyuan Hy3 preview の詳細とベンチマーク。 ](<https://huggingface.co/tencent/Hy3-preview>)

Was this useful?YesNo