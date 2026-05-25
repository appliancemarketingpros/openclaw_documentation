---
title: Inworld
source_url: https://docs.openclaw.ai/ja-JP/providers/inworld
scraped_at: 2026-05-25
---

Inworld はストリーミング Text-to-speech (TTS) プロバイダーです。OpenClaw では、送信返信音声（既定では MP3、ボイスメモでは OGG_OPUS）と、音声通話などの電話チャネル向け PCM 音声を合成します。

OpenClaw は Inworld のストリーミング TTS エンドポイントに送信し、返された base64 音声チャンクを 1 つのバッファーに連結して、その結果を標準の返信音声パイプラインに渡します。

プロパティ | 値  
---|---  
プロバイダー ID | `inworld`  
Plugin | 同梱、`enabledByDefault: true`  
コントラクト | `speechProviders` (TTS のみ)  
認証環境変数 | `INWORLD_API_KEY` (HTTP Basic、Base64 ダッシュボード認証情報)  
ベース URL | `https://api.inworld.ai`  
既定の音声 | `Sarah`  
既定のモデル | `inworld-tts-1.5-max`  
出力 | MP3 (既定)、OGG_OPUS (ボイスメモ)、PCM 22050 Hz (電話)  
Web サイト | [inworld.ai](<https://inworld.ai>)  
ドキュメント | [docs.inworld.ai/tts/tts](<https://docs.inworld.ai/tts/tts>)  
  
## はじめに

* ### API キーを設定する

Inworld ダッシュボード (Workspace > API Keys) から認証情報をコピーし、環境変数として設定します。この値は HTTP Basic 認証情報としてそのまま送信されるため、再度 Base64 エンコードしたり、bearer トークンに変換したりしないでください。

CodeCopy code
[code]
    INWORLD_API_KEY=<base64-credential-from-dashboard>
[/code]

* ### messages.tts で Inworld を選択する

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "inworld",      providers: {        inworld: {          voiceId: "Sarah",          modelId: "inworld-tts-1.5-max",        },      },    },  },}
[/code]

* ### メッセージを送信する

接続済みチャネルから返信を送信します。OpenClaw は Inworld で音声を合成し、MP3 として配信します（チャネルがボイスメモを要求する場合は OGG_OPUS）。

## 設定オプション

オプション | パス | 説明  
---|---|---  
`apiKey` | `messages.tts.providers.inworld.apiKey` | Base64 ダッシュボード認証情報。`INWORLD_API_KEY` にフォールバックします。  
`baseUrl` | `messages.tts.providers.inworld.baseUrl` | Inworld API ベース URL を上書きします（既定は `https://api.inworld.ai`）。  
`voiceId` | `messages.tts.providers.inworld.voiceId` | 音声識別子（既定は `Sarah`）。  
`modelId` | `messages.tts.providers.inworld.modelId` | TTS モデル ID（既定は `inworld-tts-1.5-max`）。  
`temperature` | `messages.tts.providers.inworld.temperature` | サンプリング温度 `0..2`（任意）。  
  
## メモ

認証

Inworld は、単一の Base64 エンコード済み認証情報文字列による HTTP Basic 認証を使用します。Inworld ダッシュボードからそのままコピーしてください。プロバイダーは追加のエンコードなしで `Authorization: Basic <apiKey>` として送信するため、自分で Base64 エンコードしたり、bearer 形式のトークンを渡したりしないでください。同じ注意点については [TTS 認証メモ](</ja-JP/tools/tts#inworld-primary>) を参照してください。

モデル

サポートされるモデル ID: `inworld-tts-1.5-max` (既定)、`inworld-tts-1.5-mini`、`inworld-tts-1-max`、`inworld-tts-1`。

音声出力

返信は既定で MP3 を使用します。チャネルターゲットが `voice-note` の場合、OpenClaw は Inworld に `OGG_OPUS` を要求し、音声がネイティブの音声バブルとして再生されるようにします。電話音声合成では、電話ブリッジに渡すために 22050 Hz の生 `PCM` を使用します。

カスタムエンドポイント

`messages.tts.providers.inworld.baseUrl` で API ホストを上書きします。末尾のスラッシュは、リクエストが送信される前に削除されます。

## 関連

[**Text-to-speech** TTS の概要、プロバイダー、`messages.tts` 設定。 ](</ja-JP/tools/tts>) [**設定** `messages.tts` 設定を含む完全な設定リファレンス。 ](</ja-JP/gateway/configuration>) [**プロバイダー** 同梱されているすべての OpenClaw プロバイダー。 ](</ja-JP/providers>) [**トラブルシューティング** よくある問題とデバッグ手順。 ](</ja-JP/help/troubleshooting>)

Was this useful?YesNo