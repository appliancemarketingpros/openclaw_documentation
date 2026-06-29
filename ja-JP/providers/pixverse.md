---
title: PixVerse
source_url: https://docs.openclaw.ai/ja-JP/providers/pixverse
scraped_at: 2026-06-29
---

ModelsProviders

OpenClaw は、ホスト型 PixVerse 動画生成用の公式外部 Plugin として `pixverse` を提供します。この Plugin は `videoGenerationProviders` contract に対して `pixverse` プロバイダーを登録します。

プロパティ | 値  
---|---  
プロバイダー ID | `pixverse`  
Plugin パッケージ | `@openclaw/pixverse-provider`  
認証環境変数 | `PIXVERSE_API_KEY`  
オンボーディングフラグ | `--auth-choice pixverse-api-key`  
直接 CLI フラグ | `--pixverse-api-key <key>`  
API | PixVerse Platform API v2（`video_id` 送信と結果ポーリング）  
デフォルトモデル | `pixverse/v6`  
デフォルト API リージョン | International  
  
## はじめに

* ### Install the plugin

bashCopy code
[code]
    openclaw plugins install clawhub:@openclaw/pixverse-provideropenclaw gateway restart
[/code]

* ### Set the API key

bashCopy code
[code]
    openclaw onboard --auth-choice pixverse-api-key
[/code]

ウィザードは、プロバイダー設定に `region` と `baseUrl` を書き込む前に、International エンドポイント （`https://app-api.pixverse.ai/openapi/v2`）または CN エンドポイント （`https://app-api.pixverseai.cn/openapi/v2`）のどちらを使用するかを確認します。

* ### Set PixVerse as the default video provider

bashCopy code
[code]
    openclaw config set agents.defaults.videoGenerationModel.primary "pixverse/v6"
[/code]

* ### Generate a video

エージェントに動画の生成を依頼します。PixVerse が自動的に使用されます。

## サポートされるモードとモデル

このプロバイダーは、OpenClaw の共有動画ツールを通じて PixVerse 生成モデルを公開します。

モード | モデル | 参照入力  
---|---|---  
テキストから動画 | `v6`（デフォルト）、`c1` | なし  
画像から動画 | `v6`（デフォルト）、`c1` | 1 個のローカルまたはリモート画像  
  
ローカル画像参照は、画像から動画へのリクエスト前に PixVerse にアップロードされます。リモート画像 URL は PixVerse の画像アップロードエンドポイントに `image_url` として渡されます。

オプション | サポートされる値  
---|---  
長さ | 1-15 秒  
解像度 | `360P`, `540P`, `720P`, `1080P`  
アスペクト比 | テキストから動画では `16:9`, `4:3`, `1:1`, `3:4`, `9:16`, `2:3`, `3:2`, `21:9`  
生成音声 | `audio: true`  
  
## プロバイダーオプション

動画プロバイダーは、次の任意のプロバイダー固有キーを受け付けます。

オプション | 型 | 効果  
---|---|---  
`seed` | number | サポートされる場合の決定論的 seed  
`negativePrompt` / `negative_prompt` | string | ネガティブプロンプト  
`quality` | string | `720p` などの PixVerse 品質  
`motionMode` / `motion_mode` | string | 画像から動画へのモーションモード  
`cameraMovement` / `camera_movement` | string | PixVerse カメラ移動プリセット  
`templateId` / `template_id` | number | 有効化された PixVerse template id  
  
## 設定

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "pixverse/v6",      },    },  },}
[/code]

## 高度な設定

API region

OpenClaw はデフォルトで International PixVerse API を使用します。キーが特定の PixVerse プラットフォームリージョンに属している場合は `models.providers.pixverse.region` を手動で設定するか、`openclaw onboard --auth-choice pixverse-api-key` を使用してセットアップウィザードで選択します。

リージョン値 | PixVerse API ベース URL  
---|---  
`international` | `https://app-api.pixverse.ai/openapi/v2`  
`cn` | `https://app-api.pixverseai.cn/openapi/v2`  
  
json5Copy code
[code]
    {  models: {    providers: {      pixverse: {        region: "cn", // "international" or "cn"        baseUrl: "https://app-api.pixverseai.cn/openapi/v2",        models: [],      },    },  },}
[/code]

Custom base URL

信頼できる互換プロキシ経由でルーティングする場合にのみ、`models.providers.pixverse.baseUrl` を設定します。 `baseUrl` は `region` より優先されます。

json5Copy code
[code]
    {  models: {    providers: {      pixverse: {        baseUrl: "https://app-api.pixverse.ai/openapi/v2",      },    },  },}
[/code]

Task polling

PixVerse は生成リクエストから `video_id` を返します。OpenClaw はタスクが成功、失敗、 またはタイムアウトするまで `/openapi/v2/video/result/{video_id}` をポーリングします。

## 関連

[**Video generation** 共有ツールのパラメーター、プロバイダー選択、非同期動作。 ](</ja-JP/tools/video-generation>) [**Configuration reference** 動画生成モデルを含むエージェントのデフォルト設定。 ](</ja-JP/gateway/config-agents#agent-defaults>)

Was this useful?YesNo

Open issue