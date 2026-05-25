---
title: 滑走路
source_url: https://docs.openclaw.ai/ja-JP/providers/runway
scraped_at: 2026-05-25
---

OpenClaw には、ホスト型動画生成向けのバンドル済み `runway` プロバイダーが付属しています。この Plugin はデフォルトで有効化され、`videoGenerationProviders` コントラクトに対して `runway` プロバイダーを登録します。

プロパティ | 値  
---|---  
プロバイダー ID | `runway`  
Plugin | バンドル済み、`enabledByDefault: true`  
認証環境変数 | `RUNWAYML_API_SECRET`（正規）または `RUNWAY_API_KEY`  
オンボーディングフラグ | `--auth-choice runway-api-key`  
直接 CLI フラグ | `--runway-api-key <key>`  
API | Runway のタスクベースの動画生成（`GET /v1/tasks/{id}` ポーリング）  
デフォルトモデル | `runway/gen4.5`  
  
## はじめに

* ### API キーを設定する

bashCopy code
[code]
    openclaw onboard --auth-choice runway-api-key
[/code]

* ### Runway をデフォルトの動画プロバイダーに設定する

bashCopy code
[code]
    openclaw config set agents.defaults.videoGenerationModel.primary "runway/gen4.5"
[/code]

* ### 動画を生成する

エージェントに動画の生成を依頼します。Runway が自動的に使用されます。

## 対応モードとモデル

このプロバイダーは、3 つのモードに分かれた 7 つの Runway モデルを公開します。同じモデル ID が複数のモードに対応できます（たとえば `gen4.5` はテキストから動画と画像から動画の両方で動作します）。

モード | モデル | 参照入力  
---|---|---  
テキストから動画 | `gen4.5`（デフォルト）、`veo3.1`、`veo3.1_fast`、`veo3` | なし  
画像から動画 | `gen4.5`、`gen4_turbo`、`gen3a_turbo`、`veo3.1`、`veo3.1_fast`、`veo3` | ローカルまたはリモート画像 1 件  
動画から動画 | `gen4_aleph` | ローカルまたはリモート動画 1 件  
  
ローカル画像と動画の参照は、data URI 経由でサポートされています。

アスペクト比 | 許可される値  
---|---  
テキストから動画 | `16:9`、`9:16`  
画像と動画の編集 | `1:1`、`16:9`、`9:16`、`3:4`、`4:3`、`21:9`  
  
## 設定

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "runway/gen4.5",      },    },  },}
[/code]

## 高度な設定

環境変数のエイリアス

OpenClaw は `RUNWAYML_API_SECRET`（正規）と `RUNWAY_API_KEY` の両方を認識します。 どちらの変数でも Runway プロバイダーを認証できます。

タスクポーリング

Runway はタスクベースの API を使用します。生成リクエストを送信した後、OpenClaw は動画の準備が完了するまで `GET /v1/tasks/{id}` をポーリングします。このポーリング動作に追加の設定は必要ありません。

## 関連

[**動画生成** 共有ツールパラメーター、プロバイダー選択、非同期動作。 ](</ja-JP/tools/video-generation>) [**設定リファレンス** 動画生成モデルを含むエージェントのデフォルト設定。 ](</ja-JP/gateway/config-agents#agent-defaults>)

Was this useful?YesNo