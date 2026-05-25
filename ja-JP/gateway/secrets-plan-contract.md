---
title: Secrets適用プランコントラクト
source_url: https://docs.openclaw.ai/ja-JP/gateway/secrets-plan-contract
scraped_at: 2026-05-25
---

このページでは、`openclaw secrets apply`によって強制される厳密なコントラクトを定義します。

ターゲットがこれらのルールに一致しない場合、設定を変更する前にapplyは失敗します。

## プランファイルの形式

`openclaw secrets apply --from <plan.json>`は、プランターゲットの`targets`配列を想定します。

json5Copy code
[code]
    {  version: 1,  protocolVersion: 1,  targets: [    {      type: "models.providers.apiKey",      path: "models.providers.openai.apiKey",      pathSegments: ["models", "providers", "openai", "apiKey"],      providerId: "openai",      ref: { source: "env", provider: "default", id: "OPENAI_API_KEY" },    },    {      type: "auth-profiles.api_key.key",      path: "profiles.openai:default.key",      pathSegments: ["profiles", "openai:default", "key"],      agentId: "main",      ref: { source: "env", provider: "default", id: "OPENAI_API_KEY" },    },  ],}
[/code]

## サポートされるターゲットスコープ

プランターゲットは、以下にあるサポート対象の資格情報パスに対して受け入れられます。

  * [SecretRef Credential Surface](</ja-JP/reference/secretref-credential-surface>)


## ターゲットタイプの動作

一般ルール:

  * `target.type`は認識される必要があり、正規化された`target.path`の形式と一致している必要があります。


既存のプランとの互換性のため、互換エイリアスは引き続き受け入れられます。

  * `models.providers.apiKey`
  * `skills.entries.apiKey`
  * `channels.googlechat.serviceAccount`


## パス検証ルール

各ターゲットは、以下すべてで検証されます。

  * `type`は認識されるターゲットタイプでなければなりません。
  * `path`は空でないドット区切りパスでなければなりません。
  * `pathSegments`は省略できます。指定する場合は、`path`と完全に同じパスに正規化されなければなりません。
  * 禁止セグメントは拒否されます: `__proto__`、`prototype`、`constructor`。
  * 正規化されたパスは、ターゲットタイプに登録されたパス形式と一致しなければなりません。
  * `providerId`または`accountId`が設定されている場合、それはパスにエンコードされたidと一致しなければなりません。
  * `auth-profiles.json`ターゲットでは`agentId`が必要です。
  * 新しい`auth-profiles.json`マッピングを作成する場合は、`authProfileProvider`を含めてください。


## 失敗時の動作

ターゲットが検証に失敗した場合、applyは次のようなエラーで終了します。

textCopy code
[code]
    Invalid plan target path for models.providers.apiKey: models.providers.openai.baseUrl
[/code]

無効なプランに対しては、書き込みは一切コミットされません。

## Execプロバイダー同意の動作

  * `--dry-run`は、デフォルトでexec SecretRefチェックをスキップします。
  * exec SecretRef/プロバイダーを含むプランは、`--allow-exec`が設定されていない限り、書き込みモードでは拒否されます。
  * execを含むプランを検証/適用する場合は、ドライランと書き込みコマンドの両方で`--allow-exec`を渡してください。


## ランタイムおよび監査スコープに関する注意

  * refのみの`auth-profiles.json`エントリ（`keyRef`/`tokenRef`）は、ランタイム解決と監査対象に含まれます。
  * `secrets apply`は、サポートされる`openclaw.json`ターゲット、サポートされる`auth-profiles.json`ターゲット、および任意の除去ターゲットを書き込みます。


## オペレーターチェック

bashCopy code
[code]
    # 書き込みなしでプランを検証openclaw secrets apply --from /tmp/openclaw-secrets-plan.json --dry-run # その後、実際に適用openclaw secrets apply --from /tmp/openclaw-secrets-plan.json # execを含むプランでは、両方のモードで明示的にオプトインopenclaw secrets apply --from /tmp/openclaw-secrets-plan.json --dry-run --allow-execopenclaw secrets apply --from /tmp/openclaw-secrets-plan.json --allow-exec
[/code]

無効なターゲットパスメッセージでapplyが失敗した場合は、`openclaw secrets configure`でプランを再生成するか、上記のサポートされる形式にターゲットパスを修正してください。

## 関連ドキュメント

  * [Secrets Management](</ja-JP/gateway/secrets>)
  * [CLI `secrets`](</ja-JP/cli/secrets>)
  * [SecretRef Credential Surface](</ja-JP/reference/secretref-credential-surface>)
  * [Configuration Reference](</ja-JP/gateway/configuration-reference>)


Was this useful?YesNo