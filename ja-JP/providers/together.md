---
title: Together AI
source_url: https://docs.openclaw.ai/ja-JP/providers/together
scraped_at: 2026-05-25
---

[Together AI](<https://together.ai>) は、統一 API を通じて Llama、DeepSeek、Kimi などの主要なオープンソース モデルへのアクセスを提供します。

プロパティ | 値  
---|---  
プロバイダー | `together`  
認証 | `TOGETHER_API_KEY`  
API | OpenAI 互換  
ベース URL | `https://api.together.xyz/v1`  
  
## はじめに

* ### API キーを取得する

[api.together.ai/settings/api-keys](<https://api.together.ai/settings/api-keys>) で API キーを作成します。

* ### オンボーディングを実行する

bashCopy code
[code]
    openclaw onboard --auth-choice together-api-key
[/code]

* ### デフォルトモデルを設定する

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "together/moonshotai/Kimi-K2.5" },    },  },}
[/code]

### 非対話型の例

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice together-api-key \  --together-api-key "$TOGETHER_API_KEY"
[/code]

## 組み込みカタログ

OpenClaw には、このバンドル済み Together カタログが含まれています。

モデル参照 | 名前 | 入力 | コンテキスト | 注記  
---|---|---|---|---  
`together/moonshotai/Kimi-K2.5` | Kimi K2.5 | テキスト, 画像 | 262,144 | デフォルトモデル; 推論有効  
`together/zai-org/GLM-4.7` | GLM 4.7 Fp8 | テキスト | 202,752 | 汎用テキストモデル  
`together/meta-llama/Llama-3.3-70B-Instruct-Turbo` | Llama 3.3 70B Instruct Turbo | テキスト | 131,072 | 高速な指示モデル  
`together/meta-llama/Llama-4-Scout-17B-16E-Instruct` | Llama 4 Scout 17B 16E Instruct | テキスト, 画像 | 10,000,000 | マルチモーダル  
`together/meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8` | Llama 4 Maverick 17B 128E Instruct FP8 | テキスト, 画像 | 20,000,000 | マルチモーダル  
`together/deepseek-ai/DeepSeek-V3.1` | DeepSeek V3.1 | テキスト | 131,072 | 汎用テキストモデル  
`together/deepseek-ai/DeepSeek-R1` | DeepSeek R1 | テキスト | 131,072 | 推論モデル  
`together/moonshotai/Kimi-K2-Instruct-0905` | Kimi K2-Instruct 0905 | テキスト | 262,144 | セカンダリ Kimi テキストモデル  
  
## 動画生成

バンドル済みの `together` plugin は、共有 `video_generate` ツールを通じた 動画生成も登録します。

プロパティ | 値  
---|---  
デフォルト動画モデル | `together/Wan-AI/Wan2.2-T2V-A14B`  
モード | テキストから動画, 単一画像リファレンス  
サポートされるパラメーター | `aspectRatio`, `resolution`  
  
Together をデフォルトの動画プロバイダーとして使用するには:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "together/Wan-AI/Wan2.2-T2V-A14B",      },    },  },}
[/code]

環境に関する注記

Gateway がデーモン (launchd/systemd) として実行される場合は、 `TOGETHER_API_KEY` がそのプロセスで利用可能であることを確認してください (たとえば、`~/.openclaw/.env` または `env.shellEnv` 経由)。

トラブルシューティング

  * キーが機能することを確認します: `openclaw models list --provider together`
  * モデルが表示されない場合は、Gateway プロセスの正しい環境に API キーが設定されていることを確認してください。
  * モデル参照は `together/<model-id>` 形式を使用します。


## 関連

[**モデル選択** プロバイダールール、モデル参照、フェイルオーバー動作。 ](</ja-JP/concepts/model-providers>) [**動画生成** 共有動画生成ツールのパラメーターとプロバイダー選択。 ](</ja-JP/tools/video-generation>) [**設定リファレンス** プロバイダー設定を含む完全な設定スキーマ。 ](</ja-JP/gateway/configuration-reference>) [**Together AI** Together AI ダッシュボード、API ドキュメント、料金。 ](<https://together.ai>)

Was this useful?YesNo