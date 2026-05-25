---
title: Alibaba Model Studio
source_url: https://docs.openclaw.ai/ja-JP/providers/alibaba
scraped_at: 2026-05-25
---

OpenClaw には、Alibaba Model Studio（DashScope の国際名）の Wan モデル向け動画生成プロバイダーを登録する、バンドル済みの `alibaba` Plugin が付属しています。この Plugin はデフォルトで有効です。API キーを設定するだけで使用できます。

プロパティ | 値  
---|---  
プロバイダーID | `alibaba`  
Plugin | バンドル済み、`enabledByDefault: true`  
認証環境変数 | `MODELSTUDIO_API_KEY` → `DASHSCOPE_API_KEY` → `QWEN_API_KEY`（最初の一致が有効）  
オンボーディングフラグ | `--auth-choice alibaba-model-studio-api-key`  
直接 CLI フラグ | `--alibaba-model-studio-api-key <key>`  
デフォルトモデル | `alibaba/wan2.6-t2v`  
デフォルトのベース URL | `https://dashscope-intl.aliyuncs.com`  
  
## はじめに

* ### Set an API key

オンボーディングを使用して、`alibaba` プロバイダーにキーを保存します。

bashCopy code
[code]
    openclaw onboard --auth-choice alibaba-model-studio-api-key
[/code]

または、インストール/オンボーディング時にキーを直接渡します。

bashCopy code
[code]
    openclaw onboard --alibaba-model-studio-api-key <your-key>
[/code]

または、Gateway を起動する前に、受け付けられる環境変数のいずれかをエクスポートします。

bashCopy code
[code]
    export MODELSTUDIO_API_KEY=sk-...# or DASHSCOPE_API_KEY=...# or QWEN_API_KEY=...
[/code]

* ### Set a default video model

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "alibaba/wan2.6-t2v",      },    },  },}
[/code]

* ### Verify the provider is configured

bashCopy code
[code]
    openclaw models list --provider alibaba
[/code]

一覧には、バンドル済みの 5 つの Wan モデルすべてが含まれているはずです。`MODELSTUDIO_API_KEY` を解決できない場合、`openclaw models status --json` は不足している認証情報を `auth.unusableProfiles` の下に報告します。

## 組み込み Wan モデル

モデル参照 | モード  
---|---  
`alibaba/wan2.6-t2v` | テキストから動画（デフォルト）  
`alibaba/wan2.6-i2v` | 画像から動画  
`alibaba/wan2.6-r2v` | 参照から動画  
`alibaba/wan2.6-r2v-flash` | 参照から動画（高速）  
`alibaba/wan2.7-r2v` | 参照から動画  
  
## 機能と制限

バンドル済みプロバイダーは、DashScope の Wan 動画 API の上限に合わせています。3 つのモードすべてで、リクエストあたりの動画数と時間の上限は同じです。異なるのは入力形式のみです。

モード | 最大出力動画数 | 最大入力画像数 | 最大入力動画数 | 最大時間 | 対応する制御項目  
---|---|---|---|---|---  
テキストから動画 | 1 | n/a | n/a | 10 秒 | `size`, `aspectRatio`, `resolution`, `audio`, `watermark`  
画像から動画 | 1 | 1 | n/a | 10 秒 | `size`, `aspectRatio`, `resolution`, `audio`, `watermark`  
参照から動画 | 1 | n/a | 4 | 10 秒 | `size`, `aspectRatio`, `resolution`, `audio`, `watermark`  
  
リクエストで `durationSeconds` を省略した場合、プロバイダーは DashScope が受け付けるデフォルトの **5 秒** を送信します。最大 10 秒まで延長するには、[動画生成ツール](</ja-JP/tools/video-generation>)で `durationSeconds` を明示的に設定します。

## 高度な設定

Override the DashScope base URL

プロバイダーはデフォルトで国際版 DashScope エンドポイントを使用します。中国リージョンのエンドポイントを対象にするには、次のように設定します。

json5Copy code
[code]
    {  models: {    providers: {      alibaba: {        baseUrl: "https://dashscope.aliyuncs.com",      },    },  },}
[/code]

プロバイダーは AIGC タスク URL を構築する前に、末尾のスラッシュを取り除きます。

Auth env priority

OpenClaw は、環境変数から次の順序で Alibaba API キーを解決し、最初の空でない値を使用します。

  1. `MODELSTUDIO_API_KEY`
  2. `DASHSCOPE_API_KEY`
  3. `QWEN_API_KEY`


設定済みの `auth.profiles` エントリ（`openclaw models auth login` で設定）は、環境変数による解決を上書きします。プロファイルのローテーション、クールダウン、上書きの仕組みについては、[モデル FAQ の認証プロファイル](</ja-JP/help/faq-models#what-is-an-auth-profile>)を参照してください。

Relationship to the Qwen plugin

バンドル済みの両 Plugin は DashScope と通信し、重複する API キーを受け付けます。次のように使い分けます。

  * このページで説明している専用の Wan 動画プロバイダーを使用するには、`alibaba/wan*.*` ID を使います。
  * Qwen のチャット、埋め込み、メディア理解には `qwen/*` ID を使います（[Qwen](</ja-JP/providers/qwen>) を参照）。


認証環境変数の一覧は意図的に重複しているため、`MODELSTUDIO_API_KEY` を一度設定すれば両方の Plugin が認証されます。各 Plugin を個別にオンボーディングする必要はありません。

## 関連

[**Video generation** 共有の動画ツールパラメーターとプロバイダー選択。 ](</ja-JP/tools/video-generation>) [**Qwen** 同じ DashScope 認証を使用する Qwen のチャット、埋め込み、メディア理解のセットアップ。 ](</ja-JP/providers/qwen>) [**Configuration reference** エージェントのデフォルトとモデル設定。 ](</ja-JP/gateway/config-agents#agent-defaults>) [**Models FAQ** 認証プロファイル、モデル切り替え、「no profile」エラーの解決。 ](</ja-JP/help/faq-models>)

Was this useful?YesNo