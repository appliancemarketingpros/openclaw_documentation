---
title: Kubernetes
source_url: https://docs.openclaw.ai/id/install/kubernetes
scraped_at: 2026-05-25
---

Titik awal minimal untuk menjalankan OpenClaw di Kubernetes — bukan deployment siap produksi. Ini mencakup resource inti dan dimaksudkan untuk disesuaikan dengan lingkungan Anda.

## Mengapa bukan Helm?

OpenClaw adalah satu container dengan beberapa file konfigurasi. Kustomisasi yang penting ada pada konten agen (file markdown, skills, override konfigurasi), bukan templating infrastruktur. Kustomize menangani overlay tanpa overhead Helm chart. Jika deployment Anda menjadi lebih kompleks, Helm chart dapat dilapiskan di atas manifes ini.

## Yang Anda butuhkan

  * Cluster Kubernetes yang berjalan (AKS, EKS, GKE, k3s, kind, OpenShift, dll.)
  * `kubectl` yang terhubung ke cluster Anda
  * Kunci API untuk setidaknya satu penyedia model


## Mulai cepat

bashCopy code
[code]
    # Replace with your provider: ANTHROPIC, GEMINI, OPENAI, or OPENROUTERexport &lt;PROVIDER&gt;_API_KEY="..."./scripts/k8s/deploy.sh kubectl port-forward svc/openclaw 18789:18789 -n openclawopen http://localhost:18789
[/code]

Ambil shared secret yang dikonfigurasi untuk Control UI. Skrip deploy ini membuat autentikasi token secara default:

bashCopy code
[code]
    kubectl get secret openclaw-secrets -n openclaw -o jsonpath='{.data.OPENCLAW_GATEWAY_TOKEN}' | base64 -d
[/code]

Untuk debugging lokal, `./scripts/k8s/deploy.sh --show-token` mencetak token setelah deploy.

## Pengujian lokal dengan Kind

Jika Anda tidak memiliki cluster, buat satu secara lokal dengan [Kind](<https://kind.sigs.k8s.io/>):

bashCopy code
[code]
    ./scripts/k8s/create-kind.sh           # auto-detects docker or podman./scripts/k8s/create-kind.sh --delete  # tear down
[/code]

Lalu deploy seperti biasa dengan `./scripts/k8s/deploy.sh`.

## Langkah demi langkah

### 1) Deploy

**Opsi A** — kunci API di environment (satu langkah):

bashCopy code
[code]
    # Replace with your provider: ANTHROPIC, GEMINI, OPENAI, or OPENROUTERexport &lt;PROVIDER&gt;_API_KEY="..."./scripts/k8s/deploy.sh
[/code]

Skrip ini membuat Kubernetes Secret dengan kunci API dan token Gateway yang dibuat otomatis, lalu melakukan deploy. Jika Secret sudah ada, skrip mempertahankan token Gateway saat ini dan kunci penyedia apa pun yang tidak sedang diubah.

**Opsi B** — buat secret secara terpisah:

bashCopy code
[code]
    export &lt;PROVIDER&gt;_API_KEY="..."./scripts/k8s/deploy.sh --create-secret./scripts/k8s/deploy.sh
[/code]

Gunakan `--show-token` dengan salah satu perintah jika Anda ingin token dicetak ke stdout untuk pengujian lokal.

### 2) Akses Gateway

bashCopy code
[code]
    kubectl port-forward svc/openclaw 18789:18789 -n openclawopen http://localhost:18789
[/code]

## Yang di-deploy

CodeCopy code
[code]
    Namespace: openclaw (configurable via OPENCLAW_NAMESPACE)├── Deployment/openclaw        # Single pod, init container + gateway├── Service/openclaw           # ClusterIP on port 18789├── PersistentVolumeClaim      # 10Gi for agent state and config├── ConfigMap/openclaw-config  # openclaw.json + AGENTS.md└── Secret/openclaw-secrets    # Gateway token + API keys
[/code]

## Kustomisasi

### Instruksi agen

Edit `AGENTS.md` di `scripts/k8s/manifests/configmap.yaml` dan deploy ulang:

bashCopy code
[code]
    ./scripts/k8s/deploy.sh
[/code]

### Konfigurasi Gateway

Edit `openclaw.json` di `scripts/k8s/manifests/configmap.yaml`. Lihat [Konfigurasi Gateway](</id/gateway/configuration>) untuk referensi lengkap.

### Tambahkan penyedia

Jalankan ulang dengan kunci tambahan yang diekspor:

bashCopy code
[code]
    export ANTHROPIC_API_KEY="..."export OPENAI_API_KEY="..."./scripts/k8s/deploy.sh --create-secret./scripts/k8s/deploy.sh
[/code]

Kunci penyedia yang ada tetap berada di Secret kecuali Anda menimpanya.

Atau patch Secret secara langsung:

bashCopy code
[code]
    kubectl patch secret openclaw-secrets -n openclaw \  -p '{"stringData":{"&lt;PROVIDER&gt;_API_KEY":"..."}}'kubectl rollout restart deployment/openclaw -n openclaw
[/code]

### Namespace kustom

bashCopy code
[code]
    OPENCLAW_NAMESPACE=my-namespace ./scripts/k8s/deploy.sh
[/code]

### Image kustom

Edit field `image` di `scripts/k8s/manifests/deployment.yaml`:

yamlCopy code
[code]
    image: ghcr.io/openclaw/openclaw:latest # or pin to a specific version from https://github.com/openclaw/openclaw/releases
[/code]

### Ekspos di luar port-forward

Manifes default mengikat Gateway ke loopback di dalam pod. Itu berfungsi dengan `kubectl port-forward`, tetapi tidak berfungsi dengan Kubernetes `Service` atau jalur Ingress yang perlu menjangkau IP pod.

Jika Anda ingin mengekspos Gateway melalui Ingress atau load balancer:

  * Ubah bind Gateway di `scripts/k8s/manifests/configmap.yaml` dari `loopback` ke bind non-loopback yang sesuai dengan model deployment Anda
  * Tetap aktifkan autentikasi Gateway dan gunakan entrypoint yang tepat dengan terminasi TLS
  * Konfigurasikan Control UI untuk akses jarak jauh menggunakan model keamanan web yang didukung (misalnya HTTPS/Tailscale Serve dan origin yang diizinkan secara eksplisit bila diperlukan)


## Deploy ulang

bashCopy code
[code]
    ./scripts/k8s/deploy.sh
[/code]

Ini menerapkan semua manifes dan memulai ulang pod untuk mengambil perubahan konfigurasi atau secret apa pun.

## Teardown

bashCopy code
[code]
    ./scripts/k8s/deploy.sh --delete
[/code]

Ini menghapus namespace dan semua resource di dalamnya, termasuk PVC.

## Catatan arsitektur

  * Gateway terikat ke loopback di dalam pod secara default, jadi setup yang disertakan ditujukan untuk `kubectl port-forward`
  * Tidak ada resource cluster-scoped — semuanya berada dalam satu namespace
  * Keamanan: kapabilitas `readOnlyRootFilesystem`, `drop: ALL`, pengguna non-root (UID 1000)
  * Konfigurasi default menjaga Control UI pada jalur akses lokal yang lebih aman: bind loopback plus `kubectl port-forward` ke `http://127.0.0.1:18789`
  * Jika Anda beralih dari akses localhost, gunakan model jarak jauh yang didukung: HTTPS/Tailscale plus bind Gateway yang sesuai dan pengaturan origin Control UI
  * Secret dibuat di direktori sementara dan diterapkan langsung ke cluster — tidak ada material secret yang ditulis ke checkout repo


## Struktur file

CodeCopy code
[code]
    scripts/k8s/├── deploy.sh                   # Creates namespace + secret, deploys via kustomize├── create-kind.sh              # Local Kind cluster (auto-detects docker/podman)└── manifests/    ├── kustomization.yaml      # Kustomize base    ├── configmap.yaml          # openclaw.json + AGENTS.md    ├── deployment.yaml         # Pod spec with security hardening    ├── pvc.yaml                # 10Gi persistent storage    └── service.yaml            # ClusterIP on 18789
[/code]

## Terkait

  * [Docker](</id/install/docker>)
  * [Runtime Docker VM](</id/install/docker-vm-runtime>)
  * [Ikhtisar instalasi](</id/install>)


Was this useful?YesNo