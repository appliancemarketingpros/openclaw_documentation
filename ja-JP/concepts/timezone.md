---
title: タイムゾーン
source_url: https://docs.openclaw.ai/ja-JP/concepts/timezone
scraped_at: 2026-05-25
---

OpenClaw はタイムスタンプを標準化し、モデルがプロバイダーごとのローカルクロックの混在ではなく、**単一の基準時刻** を見るようにします。タイムゾーンが現れるサーフェスは 3 つあり、それぞれ目的が異なります。

## 3 つのタイムゾーンサーフェス

サーフェス | 表示内容 | デフォルト | 設定方法  
---|---|---|---  
メッセージエンベロープ | 受信チャネルメッセージをラップします: `[Signal +1555 2026-01-18 00:19 PST] hello` | ホストローカル | `agents.defaults.envelopeTimezone`  
ツールペイロード | チャネルの `readMessages` 形式のツールは、生のプロバイダー時刻 + 正規化済みの `timestampMs` / `timestampUtc` を返します | UTC フィールドは常に存在 | 設定不可 — プロバイダーネイティブのタイムスタンプを保持  
システムプロンプト | **タイムゾーンのみ** を含む小さな `Current Date & Time` ブロック（キャッシュ安定性のため、時刻値は含めない） | `userTimezone` 未設定の場合はホストのタイムゾーン | `agents.defaults.userTimezone`  
  
システムプロンプトは、ターン間でプロンプトキャッシュを安定させるため、意図的に現在時刻を省略します。エージェントが現在時刻を必要とする場合は、`session_status` を呼び出します。

## ユーザータイムゾーンの設定

json5Copy code
[code]
    {  agents: {    defaults: {      userTimezone: "America/Chicago",    },  },}
[/code]

`userTimezone` が未設定の場合、OpenClaw は実行時にホストのタイムゾーンを解決します（設定の書き込みはありません）。`agents.defaults.timeFormat`（`auto` | `12` | `24`）は、エンベロープと下流サーフェスでの 12 時間/24 時間表示を制御しますが、システムプロンプトセクションでは制御しません。

## 上書きするタイミング

  * **UTC エンベロープを使用する** （`envelopeTimezone: "utc"`）のは、異なる地域のホスト間でタイムスタンプを安定させたい場合、または UTC に揃えたログを診断出力と一致させたい場合です。
  * **固定の IANA ゾーンを使用する** （例: `"Europe/Vienna"`）のは、Gateway ホストがあるゾーンにあり、ユーザーが別のゾーンにいる場合で、ホスト移行に関係なくエンベロープをユーザーのゾーンで読みたい場合です。
  * 会話にタイムスタンプのコンテキストが役立たない場合は、低トークンのエンベロープとして **`envelopeTimestamp: "off"` を設定します**。


完全な動作リファレンス、プロバイダーごとの例、経過時間の書式設定については、[日付と時刻](</ja-JP/date-time>)を参照してください。

## 関連

  * [日付と時刻](</ja-JP/date-time>) — エンベロープ/ツール/プロンプトの完全な動作と例。
  * [Heartbeat](</ja-JP/gateway/heartbeat>) — アクティブ時間はスケジューリングにタイムゾーンを使用します。
  * [Cron ジョブ](</ja-JP/automation/cron-jobs>) — cron 式はスケジューリングにタイムゾーンを使用します。


Was this useful?YesNo