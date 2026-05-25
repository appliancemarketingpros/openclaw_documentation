---
title: セッションのプルーニング
source_url: https://docs.openclaw.ai/ja-JP/concepts/session-pruning
scraped_at: 2026-05-25
---

セッションのプルーニングは、各LLM呼び出しの前にコンテキストから**古いツール結果** をトリミングします。これにより、通常の会話テキストを書き換えることなく、蓄積したツール出力（exec結果、ファイル読み取り、検索結果）によるコンテキストの肥大化を抑えます。

## なぜ重要か

長いセッションでは、コンテキストウィンドウを膨らませるツール出力が蓄積します。これによりコストが増加し、必要以上に早く [Compaction](</ja-JP/concepts/compaction>) が必要になることがあります。

プルーニングは、特に**Anthropicのプロンプトキャッシュ** で効果的です。キャッシュTTLが期限切れになると、次のリクエストで完全なプロンプトが再キャッシュされます。プルーニングはキャッシュ書き込みサイズを減らし、コストを直接下げます。

## 仕組み

  1. キャッシュTTLが期限切れになるのを待ちます（デフォルトは5分）。
  2. 通常のプルーニング用に古いツール結果を見つけます（会話テキストはそのまま残します）。
  3. サイズの大きい結果を**ソフトトリム** します — 先頭と末尾を残し、`...` を挿入します。
  4. それ以外を**ハードクリア** します — プレースホルダーに置き換えます。
  5. TTLをリセットし、後続リクエストで新しいキャッシュを再利用できるようにします。


## レガシー画像クリーンアップ

OpenClawは、履歴内に生の画像ブロックやプロンプトハイドレーション用メディアマーカーが残るセッション向けに、別の冪等なリプレイビューも構築します。

  * **直近3つの完了済みターン** はバイト単位でそのまま保持されるため、最近のフォローアップに対するプロンプトキャッシュのプレフィックスは安定したままです。
  * リプレイビューでは、`user` または `toolResult` 履歴にある、すでに処理済みの古い画像ブロックを `[image data removed - already processed by model]` に置き換えられます。
  * `[media attached: ...]`、`[Image: source: ...]`、`media://inbound/...` のような古いテキストのメディア参照は、`[media reference removed - already processed by model]` に置き換えられます。現在ターンの添付マーカーはそのまま維持されるため、visionモデルは新しい画像を引き続きハイドレートできます。
  * 生のセッショントランスクリプトは書き換えられないため、履歴ビューアーでは元のメッセージエントリとその画像を引き続き表示できます。
  * これは通常のキャッシュTTLプルーニングとは別物です。後続ターンで繰り返し現れる画像ペイロードや古いメディア参照がプロンプトキャッシュを壊すのを防ぐために存在します。


## 賢いデフォルト

OpenClawはAnthropicプロファイルで自動的にプルーニングを有効にします。

Profile type | プルーニング有効 | Heartbeat  
---|---|---  
Anthropic OAuth/トークン認証（Claude CLI再利用を含む） | はい | 1時間  
APIキー | はい | 30分  
  
明示的な値を設定している場合、OpenClawはそれを上書きしません。

## 有効化または無効化

Anthropic以外のプロバイダーでは、プルーニングはデフォルトで無効です。有効にするには:

json5Copy code
[code]
    {  agents: {    defaults: {      contextPruning: { mode: "cache-ttl", ttl: "5m" },    },  },}
[/code]

無効にするには、`mode: "off"` を設定します。

## プルーニングとCompactionの違い

| プルーニング | Compaction  
---|---|---  
**何をするか** | ツール結果をトリムする | 会話を要約する  
**保存されるか** | いいえ（リクエストごと） | はい（トランスクリプト内）  
**対象範囲** | ツール結果のみ | 会話全体  
  
両者は相互補完的です。プルーニングは、Compactionサイクルの間、ツール出力を軽量に保ちます。

## さらに読む

  * [Compaction](</ja-JP/concepts/compaction>) \-- 要約ベースのコンテキスト削減
  * [Gateway Configuration](</ja-JP/gateway/configuration>) \-- すべてのプルーニング設定項目 (`contextPruning.*`)


## 関連

  * [Session management](</ja-JP/concepts/session>)
  * [Session tools](</ja-JP/concepts/session-tool>)
  * [Context engine](</ja-JP/concepts/context-engine>)


Was this useful?YesNo