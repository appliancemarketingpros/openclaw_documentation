---
title: Vault SecretRef
source_url: https://docs.openclaw.ai/ja-JP/plugins/vault
scraped_at: 2026-07-13
---

CapabilitiesPlugin guides

# Vault SecretRef

同梱の Vault Plugin を使用すると、OpenClaw は Gateway の起動時および再読み込み時に HashiCorp Vault から `exec` SecretRef を解決できます。OpenClaw は Vault への参照を設定に保存し、解決された値をメモリ内のシークレットスナップショットに保持します。解決された API キーが `openclaw.json` に書き戻されることはありません。

すでに Vault を運用している場合や、モデルプロバイダーのキーを OpenClaw の設定ファイル外に保存したい場合に使用します。SecretRef のランタイムモデルについては、[シークレット管理](</ja-JP/gateway/secrets>)を参照してください。

## 始める前に

必要なもの：

  * 同梱の `vault` Plugin を利用できる OpenClaw
  * 接続可能な Vault サーバー
  * OpenClaw が解決するシークレットパスへの読み取りアクセス権を持つクライアントトークンを生成できる Vault 認証
  * Gateway を起動する環境に `VAULT_ADDR` と、`VAULT_TOKEN`、`OPENCLAW_VAULT_AUTH_METHOD=token_file` と `VAULT_TOKEN_FILE` の組み合わせ、または設定済みの JWT/Kubernetes ログインのいずれかが含まれていること


リゾルバーは Node から HTTP 経由で Vault と通信します。Gateway が SecretRef を解決するために Vault CLI は必要ありません。

`openclaw vault` コマンドを実行する前に、同梱の Plugin を有効にします。

bashCopy code
[code]
    openclaw plugins enable vault
[/code]

## プロバイダーキーを Vault に保存する

OpenClaw のデフォルトは、Vault 開発サーバーの例に合わせて、`secret` にマウントされた KV v2 です。本番環境の Vault では、SecretRef ID を作成する前に `OPENCLAW_VAULT_KV_MOUNT` を実際の KV マウントパスに設定してください。OpenClaw のデフォルトでは、次の SecretRef ID：

textCopy code
[code]
    providers/openrouter/apiKey
[/code]

は、次の Vault フィールドを読み取ります。

textCopy code
[code]
    secret/data/providers/openrouter -> apiKey
[/code]

Vault CLI で作成する方法の一例：

bashCopy code
[code]
    export OPENROUTER_API_KEY=<openrouter-api-key>vault kv put secret/providers/openrouter apiKey="$OPENROUTER_API_KEY"
[/code]

OpenClaw にはルートトークンではなく、スコープを限定したクライアントトークンを使用してください。デフォルトの KV v2 レイアウトでは、モデルプロバイダーキー用の最小限のポリシーは次のようになります。

hclCopy code
[code]
    path "secret/data/providers/*" {  capabilities = ["read"]}
[/code]

## Gateway から Vault を利用できるようにする

コンテナ化されていないローカル Gateway では、OpenClaw を起動するシェルと同じシェルで Vault の設定をエクスポートします。デフォルトの認証方式では、`VAULT_TOKEN` から Vault クライアントトークンを読み取ります。

bashCopy code
[code]
    export VAULT_ADDR=https://vault.example.comexport VAULT_TOKEN=<vault-client-token>
[/code]

Vault Agent がトークンシンクファイルを書き込む場合は、トークンファイル認証を使用します。

bashCopy code
[code]
    export VAULT_ADDR=https://vault.example.comexport OPENCLAW_VAULT_AUTH_METHOD=token_fileexport VAULT_TOKEN_FILE=/vault/secrets/token
[/code]

プライベート CA で署名された Vault サーバーの場合、その CA をホストの信頼ストアにインストールし、Node のシステム信頼ストアを有効にします。

bashCopy code
[code]
    export NODE_USE_SYSTEM_CA=1
[/code]

または、PEM バンドルを直接指定します。

bashCopy code
[code]
    export NODE_EXTRA_CA_CERTS=/path/to/vault-ca.pem
[/code]

これらの変数は OpenClaw の起動時に存在している必要があります。Vault Plugin はこれらをリゾルバープロセスに転送します。

非対話型 JWT 認証では、ワークロード JWT ファイルと、タイプが `jwt` の Vault ロールを使用します。

bashCopy code
[code]
    export VAULT_ADDR=https://vault.example.comexport OPENCLAW_VAULT_AUTH_METHOD=jwtexport OPENCLAW_VAULT_AUTH_MOUNT=jwtexport OPENCLAW_VAULT_AUTH_ROLE=openclawexport OPENCLAW_VAULT_JWT_FILE=/var/run/secrets/tokens/vault
[/code]

JWT ファイルには、Vault ロールが受け入れるオーディエンスを持つ Kubernetes サービスアカウントトークンなど、投影されたワークロードトークンを使用してください。 対話型の OIDC ブラウザログインは人間による操作には便利ですが、Gateway のランタイムには非対話型 JWT ログインまたはトークンファイルが必要です。

Vault の Kubernetes 認証方式では、`kubernetes` を使用します。これは Pod として実行される Gateway を対象としています。デフォルトのマウントは `kubernetes`、デフォルトの JWT ファイルは標準のサービスアカウントトークンパスです。

bashCopy code
[code]
    export VAULT_ADDR=https://vault.example.comexport OPENCLAW_VAULT_AUTH_METHOD=kubernetesexport OPENCLAW_VAULT_AUTH_ROLE=openclaw
[/code]

Vault が Kubernetes 認証を `auth/kubernetes` 以外にマウントしている場合にのみ、`OPENCLAW_VAULT_AUTH_MOUNT` を設定します。サービスアカウントトークンがカスタムパスに投影されている場合にのみ、`OPENCLAW_VAULT_JWT_FILE` を設定します。

任意の設定：

bashCopy code
[code]
    export VAULT_NAMESPACE=<namespace-name>export OPENCLAW_VAULT_KV_MOUNT=secretexport OPENCLAW_VAULT_KV_VERSION=2
[/code]

現在のシェルから参照できる内容を確認します。

bashCopy code
[code]
    openclaw vault status
[/code]

Vault を使用するシークレットプロバイダーが複数設定されている場合は、エイリアスでプロバイダーを選択します。

bashCopy code
[code]
    openclaw vault status --provider-alias corp-vault
[/code]

`openclaw vault status` が `VAULT_TOKEN` を表示することはありません。トークン、トークンファイル、JWT ファイルが設定されているかどうかのみを報告します。

## SecretRef プランを生成して適用する

OpenRouter のモデルプロバイダー API キーを Vault にマッピングするプランを作成します。

bashCopy code
[code]
    openclaw vault setup \  --plan-out ./vault-secrets-plan.json \  --openrouter-id providers/openrouter/apiKey
[/code]

プランを適用して検証します。

bashCopy code
[code]
    openclaw secrets apply --from ./vault-secrets-plan.json --dry-run --allow-execopenclaw secrets apply --from ./vault-secrets-plan.json --allow-execopenclaw secrets audit --check --allow-execopenclaw secrets reload
[/code]

Vault Plugin は OpenClaw が管理する exec SecretRef プロバイダーを介して解決を行うため、`--allow-exec` を使用します。

Gateway がまだ実行されていない場合は、プランの適用後に `openclaw secrets reload` を実行する代わりに、通常どおり起動してください。

## さらにプロバイダーキーを設定する

組み込みのショートカット：

bashCopy code
[code]
    openclaw vault setup --openai-id providers/openai/apiKeyopenclaw vault setup --anthropic-id providers/anthropic/apiKeyopenclaw vault setup --openrouter-id providers/openrouter/apiKey
[/code]

1 つのプランに複数のプロバイダーキーを含める場合：

bashCopy code
[code]
    openclaw vault setup \  --plan-out ./vault-secrets-plan.json \  --openai-id providers/openai/apiKey \  --anthropic-id providers/anthropic/apiKey \  --openrouter-id providers/openrouter/apiKey
[/code]

ショートカットのない同梱プロバイダー、または設定済みの OpenAI 互換プロバイダーやカスタムモデルプロバイダーには、`--provider-key` を使用します。

bashCopy code
[code]
    openclaw vault setup \  --plan-out ./vault-secrets-plan.json \  --provider-key local-openai=providers/local-openai/apiKey \  --provider-key groq=providers/groq/apiKey
[/code]

各 `--provider-key <provider=id>` は、SecretRef を `models.providers.<provider>.apiKey` に書き込みます。カスタムプロバイダーの場合、プロバイダーの `baseUrl`、`api`、`models` の設定は作成されないため、先にそれらを設定してください。

既知の SecretRef ターゲットパスには、`--target <path=id>` を使用します。

bashCopy code
[code]
    openclaw vault setup \  --target channels.telegram.botToken=channels/telegram/botToken \  --target models.providers.openai.headers.x-api-key=providers/openai/proxyKey \  --target auth-profiles:main:profiles.openai.key=providers/openai/apiKey
[/code]

修飾子のないターゲットパスは `openclaw.json` に適用されます。既存の `auth-profiles.json` のターゲットには、`auth-profiles:<agentId>:<path>` を使用します。 ターゲットパスは、登録済みの OpenClaw SecretRef ターゲットである必要があります。setup コマンドは OpenClaw 内に任意の名前付きシークレットを作成しません。シークレットストアは引き続き Vault であり、OpenClaw は対応する設定フィールドにのみ SecretRef を保存します。

## SecretRef ID の形式

Vault SecretRef ID では、次の規則を使用します。

textCopy code
[code]
    <vault-secret-path>/<field>
[/code]

例：

SecretRef ID | デフォルトの KV v2 Vault 読み取り | 返されるフィールド  
---|---|---  
`providers/openrouter/apiKey` | `secret/data/providers/openrouter` | `apiKey`  
`providers/openai/apiKey` | `secret/data/providers/openai` | `apiKey`  
`teams/agent-prod/openrouter` | `secret/data/teams/agent-prod` | `openrouter`  
  
返される Vault フィールドは文字列である必要があります。

KV v1 の場合は、次を設定します。

bashCopy code
[code]
    export OPENCLAW_VAULT_KV_VERSION=1
[/code]

この場合、`providers/openrouter/apiKey` は次を読み取ります。

textCopy code
[code]
    secret/providers/openrouter -> apiKey
[/code]

## OpenClaw が保存する内容

Vault setup プランを適用すると、Plugin が管理するプロバイダーが保存されます。

jsonCopy code
[code]
    {  "source": "exec",  "pluginIntegration": {    "pluginId": "vault",    "integrationId": "vault"  }}
[/code]

認証情報フィールドはそのプロバイダーを参照します。

jsonCopy code
[code]
    { "source": "exec", "provider": "vault", "id": "providers/openrouter/apiKey" }
[/code]

解決された値は、アクティブなランタイムのシークレットスナップショット内にのみ存在します。

## コンテナとマネージドデプロイ

コンテナ化された Gateway でも、同じ Plugin と SecretRef 設定を使用します。コンテナには次を渡す必要があります。

  * `VAULT_ADDR`
  * 次のいずれかの認証ソース： 
    * `VAULT_TOKEN`
    * `OPENCLAW_VAULT_AUTH_METHOD=token_file` と `VAULT_TOKEN_FILE`
    * `OPENCLAW_VAULT_AUTH_METHOD=jwt` と `OPENCLAW_VAULT_AUTH_MOUNT`、`OPENCLAW_VAULT_AUTH_ROLE`、`OPENCLAW_VAULT_JWT_FILE`
    * `OPENCLAW_VAULT_AUTH_METHOD=kubernetes` と `OPENCLAW_VAULT_AUTH_ROLE`。必要に応じて `OPENCLAW_VAULT_AUTH_MOUNT` または `OPENCLAW_VAULT_JWT_FILE` を上書き
  * 任意の `VAULT_NAMESPACE`、`OPENCLAW_VAULT_KV_MOUNT`、`OPENCLAW_VAULT_KV_VERSION`


Kubernetes を使用する場合、Vault にクラスター用の Kubernetes 認証が設定されているときは、`OPENCLAW_VAULT_AUTH_METHOD=kubernetes` を推奨します。Vault がクラスターを汎用 JWT/OIDC 発行者として扱うよう設定されている場合にのみ、`OPENCLAW_VAULT_AUTH_METHOD=jwt` を使用します。どちらの方法も、Kubernetes Secret に有効期間の長い Vault トークンを保存するより適切です。Vault Agent のサイドカーまたはインジェクターを使用するデプロイでは、代わりに `token_file` を使用できます。

マルチテナントの Vault 構成では、テナントのルーティングを Vault ポリシーとデプロイ設定で管理してください。OpenClaw は固定のマウント、ロール、パスを必要としません。各 Gateway 環境で独自の `OPENCLAW_VAULT_KV_MOUNT`、`OPENCLAW_VAULT_AUTH_ROLE`、SecretRef ID を設定できます。1 つの共有 Gateway で異なる Vault ユーザーを同時に解決する必要がある場合は、異なる認証環境をラップするよう手動設定した exec プロバイダーを使用するか、個別の Vault 環境変数を持つ Gateway 環境にテナントを分割してください。

## 関連項目

  * [シークレット管理](</ja-JP/gateway/secrets>)
  * [`openclaw secrets`](</ja-JP/cli/secrets>)
  * [Plugin 一覧](</ja-JP/plugins/plugin-inventory>)


Was this useful?YesNo

Open issue