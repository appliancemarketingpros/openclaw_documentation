---
title: Kubernetes
source_url: https://docs.openclaw.ai/ja-JP/install/kubernetes
scraped_at: 2026-05-25
---

Kubernetes で OpenClaw を実行するための最小限の出発点です。本番対応のデプロイではありません。コアリソースを扱い、環境に合わせて適応することを想定しています。

## なぜ Helm ではないのか？

OpenClaw は、いくつかの設定ファイルを含む単一コンテナです。重要なカスタマイズはインフラストラクチャのテンプレート化ではなく、エージェントのコンテンツ（Markdown ファイル、Skills、設定の上書き）にあります。Kustomize は Helm チャートのオーバーヘッドなしにオーバーレイを処理できます。デプロイがさらに複雑になった場合は、これらのマニフェストの上に Helm チャートを重ねることができます。

## 必要なもの

  * 稼働中の Kubernetes クラスター（AKS、EKS、GKE、k3s、kind、OpenShift など）
  * クラスターに接続済みの `kubectl`
  * 少なくとも 1 つのモデルプロバイダーの API キー


## クイックスタート

bashCopy code
[code]
    # Replace with your provider: ANTHROPIC, GEMINI, OPENAI, or OPENROUTERexport &lt;PROVIDER&gt;_API_KEY="..."./scripts/k8s/deploy.sh kubectl port-forward svc/openclaw 18789:18789 -n openclawopen http://localhost:18789
[/code]

Control UI 用に設定された共有シークレットを取得します。このデプロイスクリプトは、デフォルトでトークン認証を作成します。

bashCopy code
[code]
    kubectl get secret openclaw-secrets -n openclaw -o jsonpath='{.data.OPENCLAW_GATEWAY_TOKEN}' | base64 -d
[/code]

ローカルデバッグでは、`./scripts/k8s/deploy.sh --show-token` により、デプロイ後にトークンが出力されます。

## Kind を使ったローカルテスト

クラスターがない場合は、[Kind](<https://kind.sigs.k8s.io/>) でローカルに作成します。

bashCopy code
[code]
    ./scripts/k8s/create-kind.sh           # auto-detects docker or podman./scripts/k8s/create-kind.sh --delete  # tear down
[/code]

その後、通常どおり `./scripts/k8s/deploy.sh` でデプロイします。

## 手順

### 1) デプロイ

**オプション A** — 環境変数の API キー（1 ステップ）:

bashCopy code
[code]
    # Replace with your provider: ANTHROPIC, GEMINI, OPENAI, or OPENROUTERexport &lt;PROVIDER&gt;_API_KEY="..."./scripts/k8s/deploy.sh
[/code]

スクリプトは、API キーと自動生成された Gateway トークンを含む Kubernetes Secret を作成してからデプロイします。Secret がすでに存在する場合、現在の Gateway トークンと、変更対象ではないプロバイダーキーは保持されます。

**オプション B** — シークレットを別に作成する:

bashCopy code
[code]
    export &lt;PROVIDER&gt;_API_KEY="..."./scripts/k8s/deploy.sh --create-secret./scripts/k8s/deploy.sh
[/code]

ローカルテスト用にトークンを stdout に出力したい場合は、どちらのコマンドでも `--show-token` を使用します。

### 2) Gateway にアクセスする

bashCopy code
[code]
    kubectl port-forward svc/openclaw 18789:18789 -n openclawopen http://localhost:18789
[/code]

## デプロイされるもの

CodeCopy code
[code]
    Namespace: openclaw (configurable via OPENCLAW_NAMESPACE)├── Deployment/openclaw        # Single pod, init container + gateway├── Service/openclaw           # ClusterIP on port 18789├── PersistentVolumeClaim      # 10Gi for agent state and config├── ConfigMap/openclaw-config  # openclaw.json + AGENTS.md└── Secret/openclaw-secrets    # Gateway token + API keys
[/code]

## カスタマイズ

### エージェント指示

`scripts/k8s/manifests/configmap.yaml` の `AGENTS.md` を編集して、再デプロイします。

bashCopy code
[code]
    ./scripts/k8s/deploy.sh
[/code]

### Gateway 設定

`scripts/k8s/manifests/configmap.yaml` の `openclaw.json` を編集します。完全なリファレンスについては、[Gateway 設定](</ja-JP/gateway/configuration>) を参照してください。

### プロバイダーを追加する

追加のキーをエクスポートして再実行します。

bashCopy code
[code]
    export ANTHROPIC_API_KEY="..."export OPENAI_API_KEY="..."./scripts/k8s/deploy.sh --create-secret./scripts/k8s/deploy.sh
[/code]

既存のプロバイダーキーは、上書きしない限り Secret に残ります。

または、Secret に直接パッチを適用します。

bashCopy code
[code]
    kubectl patch secret openclaw-secrets -n openclaw \  -p '{"stringData":{"&lt;PROVIDER&gt;_API_KEY":"..."}}'kubectl rollout restart deployment/openclaw -n openclaw
[/code]

### カスタム名前空間

bashCopy code
[code]
    OPENCLAW_NAMESPACE=my-namespace ./scripts/k8s/deploy.sh
[/code]

### カスタムイメージ

`scripts/k8s/manifests/deployment.yaml` の `image` フィールドを編集します。

yamlCopy code
[code]
    image: ghcr.io/openclaw/openclaw:latest # or pin to a specific version from https://github.com/openclaw/openclaw/releases
[/code]

### ポートフォワードを超えて公開する

デフォルトのマニフェストは、ポッド内の loopback に Gateway をバインドします。これは `kubectl port-forward` では機能しますが、ポッド IP に到達する必要がある Kubernetes `Service` や Ingress パスでは機能しません。

Ingress またはロードバランサー経由で Gateway を公開したい場合:

  * `scripts/k8s/manifests/configmap.yaml` の Gateway バインドを `loopback` から、デプロイモデルに合う非 loopback バインドに変更する
  * Gateway 認証を有効のままにし、適切に TLS 終端されたエントリポイントを使用する
  * サポートされている Web セキュリティモデルを使用して、Control UI をリモートアクセス用に設定する（たとえば、必要に応じて HTTPS/Tailscale Serve と明示的な許可オリジン）


## 再デプロイ

bashCopy code
[code]
    ./scripts/k8s/deploy.sh
[/code]

これにより、すべてのマニフェストが適用され、設定またはシークレットの変更を取り込むためにポッドが再起動されます。

## ティアダウン

bashCopy code
[code]
    ./scripts/k8s/deploy.sh --delete
[/code]

これにより、名前空間とその中のすべてのリソース（PVC を含む）が削除されます。

## アーキテクチャメモ

  * Gateway はデフォルトでポッド内の loopback にバインドされるため、含まれているセットアップは `kubectl port-forward` 用です
  * クラスタースコープのリソースはありません。すべてが単一の名前空間内にあります
  * セキュリティ: `readOnlyRootFilesystem`、`drop: ALL` capabilities、非 root ユーザー（UID 1000）
  * デフォルト設定では、Control UI はより安全なローカルアクセスパスに保たれます: loopback バインドと `kubectl port-forward` による `http://127.0.0.1:18789`
  * localhost アクセスを超える場合は、サポートされているリモートモデルを使用してください: HTTPS/Tailscale と、適切な Gateway バインドおよび Control UI オリジン設定
  * シークレットは一時ディレクトリで生成され、クラスターに直接適用されます。シークレット素材がリポジトリのチェックアウトに書き込まれることはありません


## ファイル構造

CodeCopy code
[code]
    scripts/k8s/├── deploy.sh                   # Creates namespace + secret, deploys via kustomize├── create-kind.sh              # Local Kind cluster (auto-detects docker/podman)└── manifests/    ├── kustomization.yaml      # Kustomize base    ├── configmap.yaml          # openclaw.json + AGENTS.md    ├── deployment.yaml         # Pod spec with security hardening    ├── pvc.yaml                # 10Gi persistent storage    └── service.yaml            # ClusterIP on 18789
[/code]

## 関連

  * [Docker](</ja-JP/install/docker>)
  * [Docker VM ランタイム](</ja-JP/install/docker-vm-runtime>)
  * [インストール概要](</ja-JP/install>)


Was this useful?YesNo