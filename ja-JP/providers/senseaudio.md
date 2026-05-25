---
title: SenseAudio
source_url: https://docs.openclaw.ai/ja-JP/providers/senseaudio
scraped_at: 2026-05-25
---

SenseAudio は OpenClaw の共有 `tools.media.audio` パイプラインを通じて、受信音声とボイスノート添付ファイルを文字起こしできます。OpenClaw はマルチパート音声を OpenAI 互換の文字起こしエンドポイントに投稿し、返されたテキストを `{{Transcript}}` と `[Audio]` ブロックとして注入します。

プロパティ | 値  
---|---  
プロバイダー ID | `senseaudio`  
Plugin | 同梱, `enabledByDefault: true`  
コントラクト | `mediaUnderstandingProviders` (音声)  
認証環境変数 | `SENSEAUDIO_API_KEY`  
デフォルトモデル | `senseaudio-asr-pro-1.5-260319`  
デフォルト URL | `https://api.senseaudio.cn/v1`  
Webサイト | [senseaudio.cn](<https://senseaudio.cn>)  
ドキュメント | [senseaudio.cn/docs](<https://senseaudio.cn/docs>)  
  
## はじめに

* ### API キーを設定する

bashCopy code
[code]
    export SENSEAUDIO_API_KEY="..."
[/code]

* ### 音声プロバイダーを有効にする

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "senseaudio", model: "senseaudio-asr-pro-1.5-260319" }],      },    },  },}
[/code]

* ### ボイスノートを送信する

接続済みの任意のチャネルを通じて音声メッセージを送信します。OpenClaw は音声を SenseAudio にアップロードし、返信パイプラインで文字起こしを使用します。

## オプション

オプション | パス | 説明  
---|---|---  
`model` | `tools.media.audio.models[].model` | SenseAudio ASR モデル ID  
`language` | `tools.media.audio.models[].language` | 任意の言語ヒント  
`prompt` | `tools.media.audio.prompt` | 任意の文字起こしプロンプト  
`baseUrl` | `tools.media.audio.baseUrl` or model | OpenAI 互換のベースを上書きする  
`headers` | `tools.media.audio.request.headers` | 追加リクエストヘッダー  
  
## 関連

  * [メディア理解 (音声)](</ja-JP/nodes/audio>)
  * [モデルプロバイダー](</ja-JP/concepts/model-providers>)


Was this useful?YesNo