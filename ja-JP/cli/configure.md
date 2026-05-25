---
title: 設定
source_url: https://docs.openclaw.ai/ja-JP/cli/configure
scraped_at: 2026-05-25
---

# `openclaw configure`

既存セットアップに対して対象を絞った変更を行うための対話型プロンプト: 認証情報、デバイス、エージェントのデフォルト、Gateway、チャンネル、プラグイン、Skills、ヘルスチェック。

初回実行の完全なガイド付き手順には `openclaw onboard`、ベースラインの設定/ワークスペースだけには `openclaw setup`、チャンネルアカウントのセットアップだけが必要な場合は `openclaw channels add` を使用します。

configure がプロバイダー認証の選択から開始される場合、デフォルトモデルと許可リストのピッカーはそのプロバイダーを自動的に優先します。Volcengine と BytePlus のようなペアのプロバイダーでは、同じ優先設定がそれぞれの coding-plan バリアント（`volcengine-plan/*`、`byteplus-plan/*`）にも一致します。優先プロバイダーフィルターによって空のリストになる場合、configure は空のピッカーを表示する代わりに、フィルターなしのカタログにフォールバックします。

Web 検索では、`openclaw configure --section web` によりプロバイダーを選択し、その認証情報を設定できます。一部のプロバイダーでは、プロバイダー固有の追加プロンプトも表示されます。

  * **Grok** は同じ `XAI_API_KEY` を使った任意の `x_search` セットアップを提示し、`x_search` モデルを選択できるようにします。
  * **Kimi** は Moonshot API リージョン（`api.moonshot.ai` と `api.moonshot.cn`）と、デフォルトの Kimi Web 検索モデルを尋ねる場合があります。


関連:

  * Gateway 設定リファレンス: [設定](</ja-JP/gateway/configuration>)
  * 設定 CLI: [設定](</ja-JP/cli/config>)


## オプション

  * `--section <section>`: 繰り返し指定できるセクションフィルター


利用可能なセクション:

  * `workspace`
  * `model`
  * `web`
  * `gateway`
  * `daemon`
  * `channels`
  * `plugins`
  * `skills`
  * `health`


注記:

  * Gateway をどこで実行するかを選択すると、常に `gateway.mode` が更新されます。それだけが必要な場合は、他のセクションを選ばずに「続行」を選択できます。
  * ローカル設定の書き込み後、選択したセットアップパスで必要な場合、configure は選択されたダウンロード可能なプラグインをインストールします。リモート Gateway 設定ではローカルプラグインパッケージはインストールされません。
  * チャンネル向けサービス（Slack/Discord/Matrix/Microsoft Teams）は、セットアップ中にチャンネル/ルーム許可リストの入力を求めます。名前または ID を入力できます。可能な場合、ウィザードは名前を ID に解決します。
  * デーモンのインストール手順を実行する場合、トークン認証にはトークンが必要で、`gateway.auth.token` が SecretRef 管理であれば、configure は SecretRef を検証しますが、解決済みのプレーンテキストトークン値を supervisor サービス環境メタデータに永続化しません。
  * トークン認証でトークンが必要で、設定済みのトークン SecretRef が未解決の場合、configure は実行可能な修復ガイダンスとともにデーモンのインストールをブロックします。
  * `gateway.auth.token` と `gateway.auth.password` の両方が設定されており、`gateway.auth.mode` が未設定の場合、configure は mode が明示的に設定されるまでデーモンのインストールをブロックします。


## 例

bashCopy code
[code]
    openclaw configureopenclaw configure --section webopenclaw configure --section model --section channelsopenclaw configure --section gateway --section daemon
[/code]

## 関連

  * [CLI リファレンス](</ja-JP/cli>)
  * [設定](</ja-JP/gateway/configuration>)


Was this useful?YesNo