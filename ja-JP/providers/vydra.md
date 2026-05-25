---
title: Vydra
source_url: https://docs.openclaw.ai/ja-JP/providers/vydra
scraped_at: 2026-05-25
---

バンドルされた Vydra plugin は次を追加します。

  * `vydra/grok-imagine` による画像生成
  * `vydra/veo3` と `vydra/kling` による動画生成
  * Vydra の ElevenLabs backed TTS ルートによる音声合成


OpenClaw は 3 つの機能すべてに同じ `VYDRA_API_KEY` を使用します。

プロパティ | 値  
---|---  
プロバイダー ID | `vydra`  
Plugin | バンドル済み、`enabledByDefault: true`  
認証 env var | `VYDRA_API_KEY`  
オンボーディングフラグ | `--auth-choice vydra-api-key`  
直接 CLI フラグ | `--vydra-api-key <key>`  
コントラクト | `imageGenerationProviders`, `videoGenerationProviders`, `speechProviders`  
ベース URL | `https://www.vydra.ai/api/v1`（`www` ホストを使用）  
  
## セットアップ

* ### 対話型オンボーディングを実行する

bashCopy code
[code]
    openclaw onboard --auth-choice vydra-api-key
[/code]

または env var を直接設定します。

bashCopy code
[code]
    export VYDRA_API_KEY="vydra_live_..."
[/code]

* ### デフォルト機能を選択する

以下の機能（画像、動画、音声）の 1 つ以上を選び、対応する設定を適用します。

## 機能

画像生成

デフォルトの画像モデル:

  * `vydra/grok-imagine`


これをデフォルトの画像プロバイダーとして設定します。

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "vydra/grok-imagine",      },    },  },}
[/code]

現在バンドルされているサポートは text-to-image のみです。Vydra のホスト型編集ルートはリモート画像 URL を想定しており、OpenClaw はバンドルされた plugin ではまだ Vydra 固有のアップロードブリッジを追加していません。

動画生成

登録済み動画モデル:

  * text-to-video 用の `vydra/veo3`
  * image-to-video 用の `vydra/kling`


Vydra をデフォルトの動画プロバイダーとして設定します。

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "vydra/veo3",      },    },  },}
[/code]

注意:

  * `vydra/veo3` は text-to-video のみとしてバンドルされています。
  * `vydra/kling` は現在、リモート画像 URL 参照を必要とします。ローカルファイルのアップロードは事前に拒否されます。
  * Vydra の現在の `kling` HTTP ルートは、`image_url` と `video_url` のどちらを必要とするかについて一貫していません。バンドルされたプロバイダーは、同じリモート画像 URL を両方のフィールドにマッピングします。
  * バンドルされた plugin は保守的なままで、アスペクト比、解像度、ウォーターマーク、生成音声などの未文書化のスタイル調整項目を転送しません。

動画ライブテスト

プロバイダー固有のライブカバレッジ:

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 \OPENCLAW_LIVE_VYDRA_VIDEO=1 \pnpm test:live -- extensions/vydra/vydra.live.test.ts
[/code]

バンドルされた Vydra ライブファイルは現在、次をカバーしています。

  * `vydra/veo3` text-to-video
  * リモート画像 URL を使用する `vydra/kling` image-to-video


必要に応じてリモート画像 fixture を上書きします。

bashCopy code
[code]
    export OPENCLAW_LIVE_VYDRA_KLING_IMAGE_URL="https://example.com/reference.png"
[/code]

音声合成

Vydra を音声プロバイダーとして設定します。

json5Copy code
[code]
    {  messages: {    tts: {      provider: "vydra",      providers: {        vydra: {          apiKey: "${VYDRA_API_KEY}",          voiceId: "21m00Tcm4TlvDq8ikWAM",        },      },    },  },}
[/code]

デフォルト:

  * モデル: `elevenlabs/tts`
  * ボイス ID: `21m00Tcm4TlvDq8ikWAM`


バンドルされた plugin は現在、動作確認済みのデフォルトボイスを 1 つ公開し、MP3 音声ファイルを返します。

## 関連

[**プロバイダーディレクトリ** 利用可能なすべてのプロバイダーを参照します。 ](</ja-JP/providers>) [**画像生成** 共有画像ツールパラメーターとプロバイダー選択。 ](</ja-JP/tools/image-generation>) [**動画生成** 共有動画ツールパラメーターとプロバイダー選択。 ](</ja-JP/tools/video-generation>) [**設定リファレンス** エージェントのデフォルトとモデル設定。 ](</ja-JP/gateway/config-agents#agent-defaults>)

Was this useful?YesNo