---
title: Kubernetes
source_url: https://docs.openclaw.ai/fa/install/kubernetes
scraped_at: 2026-05-25
---

یک نقطه شروع حداقلی برای اجرای OpenClaw روی Kubernetes؛ نه یک استقرار آماده تولید. این راهنما منابع اصلی را پوشش می‌دهد و قرار است با محیط شما تطبیق داده شود.

## چرا Helm نه؟

OpenClaw یک کانتینر واحد با چند فایل پیکربندی است. سفارشی‌سازی مهم در محتوای عامل‌ها است (فایل‌های markdown، skills، بازنویسی‌های پیکربندی)، نه قالب‌سازی زیرساخت. Kustomize بدون سربار یک Helm chart، overlayها را مدیریت می‌کند. اگر استقرار شما پیچیده‌تر شود، می‌توان یک Helm chart را روی این manifestها لایه‌بندی کرد.

## آنچه نیاز دارید

  * یک کلاستر Kubernetes در حال اجرا (AKS، EKS، GKE، k3s، kind، OpenShift، و غیره)
  * `kubectl` متصل به کلاستر شما
  * یک کلید API برای حداقل یک ارائه‌دهنده مدل


## شروع سریع

bashCopy code
[code]
    # Replace with your provider: ANTHROPIC, GEMINI, OPENAI, or OPENROUTERexport &lt;PROVIDER&gt;_API_KEY="..."./scripts/k8s/deploy.sh kubectl port-forward svc/openclaw 18789:18789 -n openclawopen http://localhost:18789
[/code]

رمز مشترک پیکربندی‌شده برای رابط کاربری کنترل را بازیابی کنید. این اسکریپت استقرار به‌طور پیش‌فرض احراز هویت توکنی ایجاد می‌کند:

bashCopy code
[code]
    kubectl get secret openclaw-secrets -n openclaw -o jsonpath='{.data.OPENCLAW_GATEWAY_TOKEN}' | base64 -d
[/code]

برای اشکال‌زدایی محلی، `./scripts/k8s/deploy.sh --show-token` پس از استقرار، توکن را چاپ می‌کند.

## آزمایش محلی با Kind

اگر کلاستر ندارید، یکی را به‌صورت محلی با [Kind](<https://kind.sigs.k8s.io/>) ایجاد کنید:

bashCopy code
[code]
    ./scripts/k8s/create-kind.sh           # auto-detects docker or podman./scripts/k8s/create-kind.sh --delete  # tear down
[/code]

سپس طبق معمول با `./scripts/k8s/deploy.sh` مستقر کنید.

## گام‌به‌گام

### 1) استقرار

**گزینه A** — کلید API در محیط (یک مرحله):

bashCopy code
[code]
    # Replace with your provider: ANTHROPIC, GEMINI, OPENAI, or OPENROUTERexport &lt;PROVIDER&gt;_API_KEY="..."./scripts/k8s/deploy.sh
[/code]

اسکریپت یک Kubernetes Secret با کلید API و یک توکن Gateway تولیدشده به‌صورت خودکار ایجاد می‌کند، سپس مستقر می‌کند. اگر Secret از قبل وجود داشته باشد، توکن Gateway فعلی و هر کلید ارائه‌دهنده‌ای را که تغییر نمی‌کند حفظ می‌کند.

**گزینه B** — secret را جداگانه ایجاد کنید:

bashCopy code
[code]
    export &lt;PROVIDER&gt;_API_KEY="..."./scripts/k8s/deploy.sh --create-secret./scripts/k8s/deploy.sh
[/code]

اگر می‌خواهید توکن برای آزمایش محلی در stdout چاپ شود، با هرکدام از فرمان‌ها از `--show-token` استفاده کنید.

### 2) دسترسی به Gateway

bashCopy code
[code]
    kubectl port-forward svc/openclaw 18789:18789 -n openclawopen http://localhost:18789
[/code]

## چه چیزهایی مستقر می‌شوند

CodeCopy code
[code]
    Namespace: openclaw (configurable via OPENCLAW_NAMESPACE)├── Deployment/openclaw        # Single pod, init container + gateway├── Service/openclaw           # ClusterIP on port 18789├── PersistentVolumeClaim      # 10Gi for agent state and config├── ConfigMap/openclaw-config  # openclaw.json + AGENTS.md└── Secret/openclaw-secrets    # Gateway token + API keys
[/code]

## سفارشی‌سازی

### دستورالعمل‌های عامل

`AGENTS.md` را در `scripts/k8s/manifests/configmap.yaml` ویرایش کنید و دوباره مستقر کنید:

bashCopy code
[code]
    ./scripts/k8s/deploy.sh
[/code]

### پیکربندی Gateway

`openclaw.json` را در `scripts/k8s/manifests/configmap.yaml` ویرایش کنید. برای مرجع کامل، [پیکربندی Gateway](</fa/gateway/configuration>) را ببینید.

### افزودن ارائه‌دهنده‌ها

با کلیدهای اضافه exportشده دوباره اجرا کنید:

bashCopy code
[code]
    export ANTHROPIC_API_KEY="..."export OPENAI_API_KEY="..."./scripts/k8s/deploy.sh --create-secret./scripts/k8s/deploy.sh
[/code]

کلیدهای ارائه‌دهنده موجود در Secret باقی می‌مانند، مگر اینکه آن‌ها را بازنویسی کنید.

یا Secret را مستقیماً patch کنید:

bashCopy code
[code]
    kubectl patch secret openclaw-secrets -n openclaw \  -p '{"stringData":{"&lt;PROVIDER&gt;_API_KEY":"..."}}'kubectl rollout restart deployment/openclaw -n openclaw
[/code]

### namespace سفارشی

bashCopy code
[code]
    OPENCLAW_NAMESPACE=my-namespace ./scripts/k8s/deploy.sh
[/code]

### image سفارشی

فیلد `image` را در `scripts/k8s/manifests/deployment.yaml` ویرایش کنید:

yamlCopy code
[code]
    image: ghcr.io/openclaw/openclaw:latest # or pin to a specific version from https://github.com/openclaw/openclaw/releases
[/code]

### در دسترس قرار دادن فراتر از port-forward

manifestهای پیش‌فرض، Gateway را داخل pod به loopback متصل می‌کنند. این با `kubectl port-forward` کار می‌کند، اما با یک Kubernetes `Service` یا مسیر Ingress که باید به IP مربوط به pod برسد کار نمی‌کند.

اگر می‌خواهید Gateway را از طریق Ingress یا load balancer در دسترس قرار دهید:

  * اتصال Gateway را در `scripts/k8s/manifests/configmap.yaml` از `loopback` به یک اتصال غیرلوپ‌بک که با مدل استقرار شما سازگار است تغییر دهید
  * احراز هویت Gateway را فعال نگه دارید و از یک entrypoint مناسب با TLS-terminated استفاده کنید
  * رابط کاربری کنترل را برای دسترسی راه دور با استفاده از مدل امنیت وب پشتیبانی‌شده پیکربندی کنید (برای مثال HTTPS/Tailscale Serve و originهای مجاز صریح در صورت نیاز)


## استقرار دوباره

bashCopy code
[code]
    ./scripts/k8s/deploy.sh
[/code]

این کار همه manifestها را اعمال می‌کند و pod را restart می‌کند تا هرگونه تغییر پیکربندی یا secret اعمال شود.

## حذف استقرار

bashCopy code
[code]
    ./scripts/k8s/deploy.sh --delete
[/code]

این فرمان namespace و همه منابع داخل آن، از جمله PVC، را حذف می‌کند.

## نکات معماری

  * Gateway به‌طور پیش‌فرض داخل pod به loopback متصل می‌شود، بنابراین راه‌اندازی ارائه‌شده برای `kubectl port-forward` است
  * هیچ منبع cluster-scoped وجود ندارد؛ همه‌چیز در یک namespace واحد قرار دارد
  * امنیت: `readOnlyRootFilesystem`، قابلیت‌های `drop: ALL`، کاربر غیر root (UID 1000)
  * پیکربندی پیش‌فرض، رابط کاربری کنترل را روی مسیر دسترسی محلی ایمن‌تر نگه می‌دارد: اتصال loopback به‌همراه `kubectl port-forward` به `http://127.0.0.1:18789`
  * اگر از دسترسی localhost فراتر می‌روید، از مدل راه دور پشتیبانی‌شده استفاده کنید: HTTPS/Tailscale به‌همراه اتصال مناسب Gateway و تنظیمات origin رابط کاربری کنترل
  * Secretها در یک دایرکتوری موقت تولید و مستقیماً روی کلاستر اعمال می‌شوند؛ هیچ محتوای secret در checkout مخزن نوشته نمی‌شود


## ساختار فایل

CodeCopy code
[code]
    scripts/k8s/├── deploy.sh                   # Creates namespace + secret, deploys via kustomize├── create-kind.sh              # Local Kind cluster (auto-detects docker/podman)└── manifests/    ├── kustomization.yaml      # Kustomize base    ├── configmap.yaml          # openclaw.json + AGENTS.md    ├── deployment.yaml         # Pod spec with security hardening    ├── pvc.yaml                # 10Gi persistent storage    └── service.yaml            # ClusterIP on 18789
[/code]

## مرتبط

  * [Docker](</fa/install/docker>)
  * [زمان اجرای ماشین مجازی Docker](</fa/install/docker-vm-runtime>)
  * [نمای کلی نصب](</fa/install>)


Was this useful?YesNo