---
title: Perplexity
source_url: https://docs.openclaw.ai/ja-JP/providers/perplexity-provider
scraped_at: 2026-05-25
---

Perplexity Plugin は、Perplexity Search API または OpenRouter 経由の Perplexity Sonar を通じて Web 検索機能を提供します。

プロパティ | 値  
---|---  
種類 | Web 検索プロバイダー（モデルプロバイダーではありません）  
認証 | `PERPLEXITY_API_KEY`（直接）または `OPENROUTER_API_KEY`（OpenRouter 経由）  
設定パス | `plugins.entries.perplexity.config.webSearch.apiKey`  
  
## はじめに

* ### API キーを設定する

対話型の Web 検索設定フローを実行します。

bashCopy code
[code]
    openclaw configure --section web
[/code]

または、キーを直接設定します。

bashCopy code
[code]
    openclaw config set plugins.entries.perplexity.config.webSearch.apiKey "pplx-xxxxxxxxxxxx"
[/code]

* ### 検索を開始する

キーが設定されると、エージェントは Web 検索に Perplexity を自動的に使用します。追加の手順は不要です。

## 検索モード

この Plugin は API キーのプレフィックスに基づいてトランスポートを自動選択します。

### ネイティブ Perplexity API (pplx-)

キーが `pplx-` で始まる場合、OpenClaw はネイティブの Perplexity Search API を使用します。このトランスポートは構造化された結果を返し、ドメイン、言語、日付フィルターをサポートします（下記のフィルタリングオプションを参照）。

### OpenRouter / Sonar (sk-or-)

キーが `sk-or-` で始まる場合、OpenClaw は Perplexity Sonar モデルを使用して OpenRouter 経由でルーティングします。このトランスポートは引用付きの AI 合成回答を返します。

キーのプレフィックス | トランスポート | 機能  
---|---|---  
`pplx-` | ネイティブ Perplexity Search API | 構造化された結果、ドメイン/言語/日付フィルター  
`sk-or-` | OpenRouter (Sonar) | 引用付きの AI 合成回答  
  
## ネイティブ API フィルタリング

ネイティブ Perplexity API を使用する場合、検索では次のフィルターがサポートされます。

フィルター | 説明 | 例  
---|---|---  
国 | 2 文字の国コード | `us`, `de`, `jp`  
言語 | ISO 639-1 言語コード | `en`, `fr`, `zh`  
日付範囲 | 新しさの期間 | `day`, `week`, `month`, `year`  
ドメインフィルター | 許可リストまたは拒否リスト（最大 20 ドメイン） | `example.com`  
コンテンツ予算 | レスポンスごと / ページごとのトークン上限 | `max_tokens`, `max_tokens_per_page`  
  
## 高度な設定

デーモンプロセス用の環境変数

OpenClaw Gateway がデーモン（launchd/systemd）として実行される場合は、`PERPLEXITY_API_KEY` がそのプロセスで利用できることを確認してください。

OpenRouter プロキシのセットアップ

Perplexity 検索を OpenRouter 経由でルーティングしたい場合は、ネイティブの Perplexity キーではなく `OPENROUTER_API_KEY`（プレフィックス `sk-or-`）を設定します。OpenClaw はプレフィックスを検出し、自動的に Sonar トランスポートへ切り替えます。

## 関連

[**Perplexity 検索ツール** エージェントが Perplexity 検索を呼び出し、結果を解釈する方法。 ](</ja-JP/tools/perplexity-search>) [**設定リファレンス** Plugin エントリを含む完全な設定リファレンス。 ](</ja-JP/gateway/configuration-reference>)

Was this useful?YesNo