---
title: Xiaomi MiMo
source_url: https://docs.openclaw.ai/ja-JP/providers/xiaomi
scraped_at: 2026-05-25
---

Xiaomi MiMo は **MiMo** モデル向けの API プラットフォームです。OpenClaw には、同じ `XIAOMI_API_KEY` に対して OpenAI 互換のチャットプロバイダーと音声 (TTS) プロバイダーの両方を登録する、バンドル済みの `xiaomi` Plugin が含まれています。

プロパティ | 値  
---|---  
プロバイダー ID | `xiaomi`  
Plugin | バンドル済み、`enabledByDefault: true`  
認証環境変数 | `XIAOMI_API_KEY`  
オンボーディングフラグ | `--auth-choice xiaomi-api-key`  
直接 CLI フラグ | `--xiaomi-api-key <key>`  
コントラクト | チャット補完 + `speechProviders`  
API | OpenAI 互換 (`openai-completions`)  
ベース URL | `https://api.xiaomimimo.com/v1`  
デフォルトモデル | `xiaomi/mimo-v2-flash`  
TTS デフォルト | `mimo-v2.5-tts`、音声 `mimo_default`  
  
## はじめに

* ### API キーを取得する

[Xiaomi MiMo コンソール](<https://platform.xiaomimimo.com/#/console/api-keys>)で API キーを作成します。

* ### オンボーディングを実行する

bashCopy code
[code]
    openclaw onboard --auth-choice xiaomi-api-key
[/code]

または、キーを直接渡します。

bashCopy code
[code]
    openclaw onboard --auth-choice xiaomi-api-key --xiaomi-api-key "$XIAOMI_API_KEY"
[/code]

* ### モデルが利用可能であることを確認する

bashCopy code
[code]
    openclaw models list --provider xiaomi
[/code]

## 組み込みカタログ

モデル参照 | 入力 | コンテキスト | 最大出力 | 推論 | 注記  
---|---|---|---|---|---  
`xiaomi/mimo-v2-flash` | テキスト | 262,144 | 8,192 | なし | デフォルトモデル  
`xiaomi/mimo-v2-pro` | テキスト | 1,048,576 | 32,000 | あり | 大きなコンテキスト  
`xiaomi/mimo-v2-omni` | テキスト、画像 | 262,144 | 32,000 | あり | マルチモーダル  
  
## テキスト読み上げ

バンドル済みの `xiaomi` Plugin は、`messages.tts` 向けの音声プロバイダーとしても Xiaomi MiMo を登録します。テキストを `assistant` メッセージとして、任意のスタイル指示を `user` メッセージとして指定し、Xiaomi のチャット補完 TTS コントラクトを呼び出します。

プロパティ | 値  
---|---  
TTS ID | `xiaomi` (`mimo` エイリアス)  
認証 | `XIAOMI_API_KEY`  
API | `audio` 付きの `POST /v1/chat/completions`  
デフォルト | `mimo-v2.5-tts`、音声 `mimo_default`  
出力 | デフォルトでは MP3、設定時は WAV  
json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "xiaomi",      providers: {        xiaomi: {          apiKey: "xiaomi_api_key",          model: "mimo-v2.5-tts",          voice: "mimo_default",          format: "mp3",          style: "Bright, natural, conversational tone.",        },      },    },  },}
[/code]

サポートされている組み込み音声には、`mimo_default`、`default_zh`、`default_en`、`Mia`、`Chloe`、`Milo`、`Dean` が含まれます。`mimo-v2-tts` は古い MiMo TTS アカウント向けにサポートされています。デフォルトでは現在の MiMo-V2.5 TTS モデルを使用します。Feishu や Telegram などのボイスメモ対象では、OpenClaw は配信前に Xiaomi の出力を `ffmpeg` で 48kHz Opus にトランスコードします。

## 設定例

json5Copy code
[code]
    {  env: { XIAOMI_API_KEY: "your-key" },  agents: { defaults: { model: { primary: "xiaomi/mimo-v2-flash" } } },  models: {    mode: "merge",    providers: {      xiaomi: {        baseUrl: "https://api.xiaomimimo.com/v1",        api: "openai-completions",        apiKey: "XIAOMI_API_KEY",        models: [          {            id: "mimo-v2-flash",            name: "Xiaomi MiMo V2 Flash",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 8192,          },          {            id: "mimo-v2-pro",            name: "Xiaomi MiMo V2 Pro",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 1048576,            maxTokens: 32000,          },          {            id: "mimo-v2-omni",            name: "Xiaomi MiMo V2 Omni",            reasoning: true,            input: ["text", "image"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 32000,          },        ],      },    },  },}
[/code]

自動注入の動作

`XIAOMI_API_KEY` が環境に設定されているか、認証プロファイルが存在する場合、`xiaomi` プロバイダーは自動的に注入されます。モデルメタデータまたはベース URL を上書きしたい場合を除き、プロバイダーを手動で設定する必要はありません。

モデルの詳細

  * **mimo-v2-flash** — 軽量で高速な、汎用テキストタスクに適したモデルです。推論はサポートしません。
  * **mimo-v2-pro** — 長文ドキュメントのワークロード向けに、1M トークンのコンテキストウィンドウで推論をサポートします。
  * **mimo-v2-omni** — テキスト入力と画像入力の両方を受け付ける、推論対応のマルチモーダルモデルです。

トラブルシューティング

  * モデルが表示されない場合は、`XIAOMI_API_KEY` が設定され、有効であることを確認してください。
  * Gateway がデーモンとして実行される場合は、そのプロセスからキーを利用できるようにしてください (例: `~/.openclaw/.env` または `env.shellEnv` 経由)。


## 関連

[**モデル選択** プロバイダー、モデル参照、フェイルオーバー動作の選択。 ](</ja-JP/concepts/model-providers>) [**設定リファレンス** OpenClaw 設定の完全なリファレンス。 ](</ja-JP/gateway/configuration-reference>) [**Xiaomi MiMo コンソール** Xiaomi MiMo ダッシュボードと API キー管理。 ](<https://platform.xiaomimimo.com>)

Was this useful?YesNo