---
title: Deepgram
source_url: https://docs.openclaw.ai/ja-JP/providers/deepgram
scraped_at: 2026-05-25
---

Deepgram は speech-to-text API です。OpenClaw では、 `tools.media.audio` を通じた受信音声/ボイスノートの文字起こし、および `plugins.entries.voice-call.config.streaming` を通じた Voice Call のストリーミング STT に使用されます。

バッチ文字起こしでは、OpenClaw は完全な音声ファイルを Deepgram にアップロードし、 文字起こし結果を返信パイプラインに注入します（`{{Transcript}}` \+ `[Audio]` block）。Voice Call のストリーミングでは、OpenClaw は live な G.711 u-law frame を Deepgram の WebSocket `listen` endpoint へ転送し、Deepgram が返す partial または final transcript を発行します。

Detail | Value  
---|---  
Website | [deepgram.com](<https://deepgram.com>)  
Docs | [developers.deepgram.com](<https://developers.deepgram.com>)  
Auth | `DEEPGRAM_API_KEY`  
Default model | `nova-3`  
  
## はじめに

* ### API key を設定する

Deepgram API key を環境変数に追加します。

CodeCopy code
[code]
    DEEPGRAM_API_KEY=dg_...
[/code]

* ### 音声 provider を有効化する

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "deepgram", model: "nova-3" }],      },    },  },}
[/code]

* ### ボイスノートを送る

接続済みの任意の channel から音声メッセージを送ってください。OpenClaw は Deepgram 経由でそれを文字起こしし、その transcript を返信パイプラインに注入します。

## 設定オプション

Option | Path | Description  
---|---|---  
`model` | `tools.media.audio.models[].model` | Deepgram model id（デフォルト: `nova-3`）  
`language` | `tools.media.audio.models[].language` | 言語ヒント（任意）  
`detect_language` | `tools.media.audio.providerOptions.deepgram.detect_language` | 言語検出を有効化（任意）  
`punctuate` | `tools.media.audio.providerOptions.deepgram.punctuate` | 句読点付与を有効化（任意）  
`smart_format` | `tools.media.audio.providerOptions.deepgram.smart_format` | スマート整形を有効化（任意）  
  
### 言語ヒントあり

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "deepgram", model: "nova-3", language: "en" }],      },    },  },}
[/code]

### Deepgram オプションあり

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        providerOptions: {          deepgram: {            detect_language: true,            punctuate: true,            smart_format: true,          },        },        models: [{ provider: "deepgram", model: "nova-3" }],      },    },  },}
[/code]

## Voice Call ストリーミング STT

バンドル済みの `deepgram` Plugin は、Voice Call Plugin 向けの realtime transcription provider も登録します。

Setting | Config path | Default  
---|---|---  
API key | `plugins.entries.voice-call.config.streaming.providers.deepgram.apiKey` | `DEEPGRAM_API_KEY` にフォールバック  
Model | `...deepgram.model` | `nova-3`  
Language | `...deepgram.language` | （未設定）  
Encoding | `...deepgram.encoding` | `mulaw`  
Sample rate | `...deepgram.sampleRate` | `8000`  
Endpointing | `...deepgram.endpointingMs` | `800`  
Interim results | `...deepgram.interimResults` | `true`  
json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        config: {          streaming: {            enabled: true,            provider: "deepgram",            providers: {              deepgram: {                apiKey: "${DEEPGRAM_API_KEY}",                model: "nova-3",                endpointingMs: 800,                language: "en-US",              },            },          },        },      },    },  },}
[/code]

## 注意

認証

認証は標準の provider auth 順序に従います。最も簡単なのは `DEEPGRAM_API_KEY` を使う方法です。

Proxy とカスタム endpoint

proxy を使用する場合は、`tools.media.audio.baseUrl` と `tools.media.audio.headers` で endpoint または header を上書きします。

出力動作

出力は他の provider と同じ音声ルールに従います（size cap、timeout、 transcript injection）。

## 関連

[**Media tools** 音声、画像、および動画処理パイプラインの概要。 ](</ja-JP/tools/media-overview>) [**Configuration** media tool 設定を含む完全な設定リファレンス。 ](</ja-JP/gateway/configuration>) [**Troubleshooting** 一般的な問題とデバッグ手順。 ](</ja-JP/help/troubleshooting>) [**FAQ** OpenClaw セットアップに関するよくある質問。 ](</ja-JP/help/faq>)

Was this useful?YesNo