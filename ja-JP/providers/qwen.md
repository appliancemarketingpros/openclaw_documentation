---
title: Qwen
source_url: https://docs.openclaw.ai/ja-JP/providers/qwen
scraped_at: 2026-05-25
---

OpenClaw は現在、Qwen を正規 ID `qwen` を持つ第一級のバンドル済みプロバイダーとして扱います。バンドル済みプロバイダーは Qwen Cloud / Alibaba DashScope と Coding Plan エンドポイントを対象とし、互換性エイリアスとして従来の `modelstudio` ID も引き続き動作します。

  * プロバイダー: `qwen`
  * 推奨環境変数: `QWEN_API_KEY`
  * 互換性のために許可されるもの: `MODELSTUDIO_API_KEY`, `DASHSCOPE_API_KEY`
  * API スタイル: OpenAI 互換


## はじめに

プラン種別を選び、セットアップ手順に従います。

### Coding Plan (subscription)

**最適な用途:** Qwen Coding Plan を通じたサブスクリプションベースのアクセス。

* ### Get your API key

[home.qwencloud.com/api-keys](<https://home.qwencloud.com/api-keys>) から API キーを作成またはコピーします。

* ### Run onboarding

**グローバル** エンドポイントの場合:

bashCopy code
[code]
    openclaw onboard --auth-choice qwen-api-key
[/code]

**中国** エンドポイントの場合:

bashCopy code
[code]
    openclaw onboard --auth-choice qwen-api-key-cn
[/code]

* ### Set a default model

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "qwen/qwen3.5-plus" },    },  },}
[/code]

* ### Verify the model is available

bashCopy code
[code]
    openclaw models list --provider qwen
[/code]

### Standard (pay-as-you-go)

**最適な用途:** Coding Plan では利用できない可能性がある `qwen3.6-plus` などのモデルを含む、Standard Model Studio エンドポイントを通じた従量課金アクセス。

* ### Get your API key

[home.qwencloud.com/api-keys](<https://home.qwencloud.com/api-keys>) から API キーを作成またはコピーします。

* ### Run onboarding

**グローバル** エンドポイントの場合:

bashCopy code
[code]
    openclaw onboard --auth-choice qwen-standard-api-key
[/code]

**中国** エンドポイントの場合:

bashCopy code
[code]
    openclaw onboard --auth-choice qwen-standard-api-key-cn
[/code]

* ### Set a default model

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "qwen/qwen3.5-plus" },    },  },}
[/code]

* ### Verify the model is available

bashCopy code
[code]
    openclaw models list --provider qwen
[/code]

## プラン種別とエンドポイント

プラン | リージョン | Auth choice | エンドポイント  
---|---|---|---  
Standard (従量課金) | 中国 | `qwen-standard-api-key-cn` | `dashscope.aliyuncs.com/compatible-mode/v1`  
Standard (従量課金) | グローバル | `qwen-standard-api-key` | `dashscope-intl.aliyuncs.com/compatible-mode/v1`  
Coding Plan (サブスクリプション) | 中国 | `qwen-api-key-cn` | `coding.dashscope.aliyuncs.com/v1`  
Coding Plan (サブスクリプション) | グローバル | `qwen-api-key` | `coding-intl.dashscope.aliyuncs.com/v1`  
  
プロバイダーは auth choice に基づいてエンドポイントを自動選択します。正規の選択肢は `qwen-*` ファミリーを使用します。`modelstudio-*` は互換性専用として残ります。 config 内のカスタム `baseUrl` で上書きできます。

## 組み込みカタログ

OpenClaw は現在、このバンドル済み Qwen カタログを同梱しています。設定済みカタログはエンドポイントを認識します。Coding Plan 設定では、Standard エンドポイントでのみ動作することが判明しているモデルを省略します。

モデル参照 | 入力 | コンテキスト | 注記  
---|---|---|---  
`qwen/qwen3.5-plus` | テキスト、画像 | 1,000,000 | デフォルトモデル  
`qwen/qwen3.6-plus` | テキスト、画像 | 1,000,000 | このモデルが必要な場合は Standard エンドポイントを推奨  
`qwen/qwen3-max-2026-01-23` | テキスト | 262,144 | Qwen Max 系列  
`qwen/qwen3-coder-next` | テキスト | 262,144 | コーディング  
`qwen/qwen3-coder-plus` | テキスト | 1,000,000 | コーディング  
`qwen/MiniMax-M2.5` | テキスト | 1,000,000 | 推論が有効  
`qwen/glm-5` | テキスト | 202,752 | GLM  
`qwen/glm-4.7` | テキスト | 202,752 | GLM  
`qwen/kimi-k2.5` | テキスト、画像 | 262,144 | Alibaba 経由の Moonshot AI  
  
## 思考制御

推論対応の Qwen Cloud モデルでは、バンドル済みプロバイダーが OpenClaw の思考レベルを DashScope のトップレベル `enable_thinking` リクエストフラグに対応付けます。思考を無効にすると `enable_thinking: false` が送信されます。その他の思考レベルでは `enable_thinking: true` が送信されます。

## マルチモーダルアドオン

`qwen` Plugin は、**Standard** DashScope エンドポイントでもマルチモーダル機能を公開します (Coding Plan エンドポイントではありません)。

  * `qwen-vl-max-latest` による**動画理解**
  * `wan2.6-t2v` (デフォルト)、`wan2.6-i2v`、`wan2.6-r2v`、`wan2.6-r2v-flash`、`wan2.7-r2v` による **Wan 動画生成**


Qwen をデフォルトの動画プロバイダーとして使うには:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: { primary: "qwen/wan2.6-t2v" },    },  },}
[/code]

## 高度な設定

Image and video understanding

バンドル済み Qwen Plugin は、**Standard** DashScope エンドポイントで画像と動画のメディア理解を登録します (Coding Plan エンドポイントではありません)。

プロパティ | 値  
---|---  
モデル | `qwen-vl-max-latest`  
サポートされる入力 | 画像、動画  
  
メディア理解は設定済みの Qwen 認証から自動解決されます。追加設定は不要です。メディア理解サポートには Standard (従量課金) エンドポイントを使用していることを確認してください。

Qwen 3.6 Plus availability

`qwen3.6-plus` は Standard (従量課金) Model Studio エンドポイントで利用できます。

  * 中国: `dashscope.aliyuncs.com/compatible-mode/v1`
  * グローバル: `dashscope-intl.aliyuncs.com/compatible-mode/v1`


Coding Plan エンドポイントが `qwen3.6-plus` に対して「unsupported model」エラーを返す場合は、Coding Plan のエンドポイント/キーの組み合わせではなく Standard (従量課金) に切り替えてください。

OpenClaw のバンドル済み Qwen カタログは Coding Plan エンドポイントで `qwen3.6-plus` を公開しませんが、`models.providers.qwen.models` の下で明示的に設定された `qwen/qwen3.6-plus` エントリは Coding Plan baseUrl でも尊重されるため、Aliyun がサブスクリプションで有効化した場合はそのモデルを opt-in できます。呼び出しが成功するかどうかは引き続きアップストリーム API が判断します。

Capability plan

`qwen` Plugin は、コーディング/テキストモデルだけでなく、Qwen Cloud サーフェス全体のベンダー本拠として位置付けられています。

  * **テキスト/チャットモデル:** 現在バンドル済み
  * **ツール呼び出し、構造化出力、思考:** OpenAI 互換トランスポートから継承
  * **画像生成:** プロバイダー Plugin レイヤーで計画中
  * **画像/動画理解:** Standard エンドポイントで現在バンドル済み
  * **音声/オーディオ:** プロバイダー Plugin レイヤーで計画中
  * **メモリエンベディング/再ランキング:** エンベディングアダプターサーフェス経由で計画中
  * **動画生成:** 共有動画生成機能経由で現在バンドル済み

Video generation details

動画生成では、OpenClaw はジョブ送信前に設定済みの Qwen リージョンを対応する DashScope AIGC ホストに対応付けます。

  * グローバル/Intl: `https://dashscope-intl.aliyuncs.com`
  * 中国: `https://dashscope.aliyuncs.com`


つまり、Coding Plan または Standard Qwen ホストのいずれかを指す通常の `models.providers.qwen.baseUrl` でも、動画生成は正しいリージョンの DashScope 動画エンドポイントで維持されます。

現在のバンドル済み Qwen 動画生成制限:

  * リクエストあたり最大 **1** 本の出力動画
  * 最大 **1** 枚の入力画像
  * 最大 **4** 本の入力動画
  * 最大 **10 秒** の長さ
  * `size`、`aspectRatio`、`resolution`、`audio`、`watermark` をサポート
  * 参照画像/動画モードでは現在、**リモート http(s) URL** が必要です。DashScope 動画エンドポイントはそれらの参照用にアップロードされたローカルバッファーを受け付けないため、ローカルファイルパスは事前に拒否されます。

Streaming usage compatibility

ネイティブ Model Studio エンドポイントは、共有 `openai-completions` トランスポート上でストリーミング使用量の互換性を公開します。OpenClaw は現在これをエンドポイント機能に基づいて判定するため、同じネイティブホストを対象とする DashScope 互換のカスタムプロバイダー ID は、組み込みの `qwen` プロバイダー ID を特に要求することなく、同じストリーミング使用量動作を継承します。

ネイティブストリーミング使用量互換性は、Coding Plan ホストと Standard DashScope 互換ホストの両方に適用されます。

  * `https://coding.dashscope.aliyuncs.com/v1`
  * `https://coding-intl.dashscope.aliyuncs.com/v1`
  * `https://dashscope.aliyuncs.com/compatible-mode/v1`
  * `https://dashscope-intl.aliyuncs.com/compatible-mode/v1`

Multimodal endpoint regions

マルチモーダルサーフェス (動画理解と Wan 動画生成) は Coding Plan エンドポイントではなく **Standard** DashScope エンドポイントを使用します。

  * グローバル/Intl Standard ベース URL: `https://dashscope-intl.aliyuncs.com/compatible-mode/v1`
  * 中国 Standard ベース URL: `https://dashscope.aliyuncs.com/compatible-mode/v1`

環境とデーモンの設定

Gateway をデーモン（launchd/systemd）として実行する場合は、`QWEN_API_KEY` が そのプロセスで利用できるようにしてください（たとえば `~/.openclaw/.env` または `env.shellEnv` 経由）。

## 関連

[**モデル選択** プロバイダー、モデル参照、フェイルオーバー動作の選択。 ](</ja-JP/concepts/model-providers>) [**動画生成** 共通の動画ツールパラメーターとプロバイダー選択。 ](</ja-JP/tools/video-generation>) [**Alibaba (ModelStudio)** 従来の ModelStudio プロバイダーと移行メモ。 ](</ja-JP/providers/alibaba>) [**トラブルシューティング** 一般的なトラブルシューティングと FAQ。 ](</ja-JP/help/troubleshooting>)

Was this useful?YesNo