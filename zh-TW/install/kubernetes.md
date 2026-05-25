---
title: Kubernetes
source_url: https://docs.openclaw.ai/zh-TW/install/kubernetes
scraped_at: 2026-05-25
---

在 Kubernetes 上執行 OpenClaw 的最小起點，不是可直接用於生產環境的部署。它涵蓋核心資源，並且預期你會依照自己的環境進行調整。

## 為什麼不用 Helm？

OpenClaw 是一個帶有一些設定檔的單一容器。有價值的自訂項目在於 agent 內容（Markdown 檔案、Skills、設定覆寫），而不是基礎架構樣板。Kustomize 可以處理覆寫層，不需要 Helm chart 的額外負擔。如果你的部署變得更複雜，可以在這些 manifests 之上再疊加 Helm chart。

## 你需要什麼

  * 一個正在執行的 Kubernetes 叢集（AKS、EKS、GKE、k3s、kind、OpenShift 等）
  * 已連線到叢集的 `kubectl`
  * 至少一個模型提供者的 API 金鑰


## 快速開始

bashCopy code
[code]
    # Replace with your provider: ANTHROPIC, GEMINI, OPENAI, or OPENROUTERexport &lt;PROVIDER&gt;_API_KEY="..."./scripts/k8s/deploy.sh kubectl port-forward svc/openclaw 18789:18789 -n openclawopen http://localhost:18789
[/code]

擷取已設定的 Control UI 共用密鑰。此部署指令碼預設會 建立 token 驗證：

bashCopy code
[code]
    kubectl get secret openclaw-secrets -n openclaw -o jsonpath='{.data.OPENCLAW_GATEWAY_TOKEN}' | base64 -d
[/code]

若要進行本機偵錯，`./scripts/k8s/deploy.sh --show-token` 會在部署後印出 token。

## 使用 Kind 進行本機測試

如果你沒有叢集，請使用 [Kind](<https://kind.sigs.k8s.io/>) 在本機建立一個：

bashCopy code
[code]
    ./scripts/k8s/create-kind.sh           # auto-detects docker or podman./scripts/k8s/create-kind.sh --delete  # tear down
[/code]

然後照常使用 `./scripts/k8s/deploy.sh` 部署。

## 逐步操作

### 1) 部署

**選項 A** — 環境變數中的 API 金鑰（一步完成）：

bashCopy code
[code]
    # Replace with your provider: ANTHROPIC, GEMINI, OPENAI, or OPENROUTERexport &lt;PROVIDER&gt;_API_KEY="..."./scripts/k8s/deploy.sh
[/code]

此指令碼會使用 API 金鑰和自動產生的 Gateway token 建立 Kubernetes Secret，然後進行部署。如果 Secret 已存在，它會保留目前的 Gateway token，以及任何未變更的提供者金鑰。

**選項 B** — 個別建立 secret：

bashCopy code
[code]
    export &lt;PROVIDER&gt;_API_KEY="..."./scripts/k8s/deploy.sh --create-secret./scripts/k8s/deploy.sh
[/code]

如果你想為本機測試將 token 印到 stdout，任一指令都可以搭配使用 `--show-token`。

### 2) 存取 Gateway

bashCopy code
[code]
    kubectl port-forward svc/openclaw 18789:18789 -n openclawopen http://localhost:18789
[/code]

## 會部署什麼

CodeCopy code
[code]
    Namespace: openclaw (configurable via OPENCLAW_NAMESPACE)├── Deployment/openclaw        # Single pod, init container + gateway├── Service/openclaw           # ClusterIP on port 18789├── PersistentVolumeClaim      # 10Gi for agent state and config├── ConfigMap/openclaw-config  # openclaw.json + AGENTS.md└── Secret/openclaw-secrets    # Gateway token + API keys
[/code]

## 自訂

### Agent 指示

編輯 `scripts/k8s/manifests/configmap.yaml` 中的 `AGENTS.md`，然後重新部署：

bashCopy code
[code]
    ./scripts/k8s/deploy.sh
[/code]

### Gateway 設定

編輯 `scripts/k8s/manifests/configmap.yaml` 中的 `openclaw.json`。完整參考請見 [Gateway 設定](</zh-TW/gateway/configuration>)。

### 新增提供者

重新執行並匯出額外金鑰：

bashCopy code
[code]
    export ANTHROPIC_API_KEY="..."export OPENAI_API_KEY="..."./scripts/k8s/deploy.sh --create-secret./scripts/k8s/deploy.sh
[/code]

除非你覆寫現有提供者金鑰，否則它們會保留在 Secret 中。

或直接 patch Secret：

bashCopy code
[code]
    kubectl patch secret openclaw-secrets -n openclaw \  -p '{"stringData":{"&lt;PROVIDER&gt;_API_KEY":"..."}}'kubectl rollout restart deployment/openclaw -n openclaw
[/code]

### 自訂命名空間

bashCopy code
[code]
    OPENCLAW_NAMESPACE=my-namespace ./scripts/k8s/deploy.sh
[/code]

### 自訂映像檔

編輯 `scripts/k8s/manifests/deployment.yaml` 中的 `image` 欄位：

yamlCopy code
[code]
    image: ghcr.io/openclaw/openclaw:latest # or pin to a specific version from https://github.com/openclaw/openclaw/releases
[/code]

### 暴露到 port-forward 之外

預設 manifests 會將 Gateway 綁定到 pod 內的 loopback。這可搭配 `kubectl port-forward` 運作，但無法搭配需要連到 pod IP 的 Kubernetes `Service` 或 Ingress 路徑運作。

如果你想透過 Ingress 或負載平衡器暴露 Gateway：

  * 將 `scripts/k8s/manifests/configmap.yaml` 中的 Gateway 綁定從 `loopback` 改為符合你部署模型的非 loopback 綁定
  * 保持 Gateway 驗證啟用，並使用正確的 TLS 終止進入點
  * 使用支援的網頁安全模型為遠端存取設定 Control UI（例如 HTTPS/Tailscale Serve，以及需要時明確設定允許的 origins）


## 重新部署

bashCopy code
[code]
    ./scripts/k8s/deploy.sh
[/code]

這會套用所有 manifests，並重新啟動 pod 以套用任何設定或 secret 變更。

## 拆除

bashCopy code
[code]
    ./scripts/k8s/deploy.sh --delete
[/code]

這會刪除命名空間及其中的所有資源，包括 PVC。

## 架構注意事項

  * Gateway 預設會綁定到 pod 內的 loopback，因此隨附的設定適用於 `kubectl port-forward`
  * 沒有叢集範圍資源，所有內容都位於單一命名空間中
  * 安全性：`readOnlyRootFilesystem`、`drop: ALL` capabilities、非 root 使用者（UID 1000）
  * 預設設定會讓 Control UI 留在較安全的本機存取路徑：loopback 綁定加上 `kubectl port-forward` 到 `http://127.0.0.1:18789`
  * 如果你要超出 localhost 存取，請使用支援的遠端模型：HTTPS/Tailscale 加上適當的 Gateway 綁定與 Control UI origin 設定
  * Secrets 會在暫存目錄中產生並直接套用到叢集，不會將任何 secret material 寫入 repo checkout


## 檔案結構

CodeCopy code
[code]
    scripts/k8s/├── deploy.sh                   # Creates namespace + secret, deploys via kustomize├── create-kind.sh              # Local Kind cluster (auto-detects docker/podman)└── manifests/    ├── kustomization.yaml      # Kustomize base    ├── configmap.yaml          # openclaw.json + AGENTS.md    ├── deployment.yaml         # Pod spec with security hardening    ├── pvc.yaml                # 10Gi persistent storage    └── service.yaml            # ClusterIP on 18789
[/code]

## 相關

  * [Docker](</zh-TW/install/docker>)
  * [Docker VM runtime](</zh-TW/install/docker-vm-runtime>)
  * [安裝概觀](</zh-TW/install>)


Was this useful?YesNo