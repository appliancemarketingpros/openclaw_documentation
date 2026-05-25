---
title: Kubernetes
source_url: https://docs.openclaw.ai/uk/install/kubernetes
scraped_at: 2026-05-25
---

Мінімальна відправна точка для запуску OpenClaw у Kubernetes — не готове до production розгортання. Вона охоплює основні ресурси та призначена для адаптації під ваше середовище.

## Чому не Helm?

OpenClaw — це один контейнер із кількома конфігураційними файлами. Найважливіше налаштування відбувається в контенті агента (markdown-файлах, skills, перевизначеннях конфігурації), а не в шаблонізації інфраструктури. Kustomize обробляє overlay без накладних витрат Helm-чарту. Якщо ваше розгортання стане складнішим, Helm-чарт можна нашарувати поверх цих маніфестів.

## Що потрібно

  * Запущений кластер Kubernetes (AKS, EKS, GKE, k3s, kind, OpenShift тощо)
  * `kubectl`, підключений до вашого кластера
  * API-ключ принаймні для одного провайдера моделей


## Швидкий старт

bashCopy code
[code]
    # Replace with your provider: ANTHROPIC, GEMINI, OPENAI, or OPENROUTERexport &lt;PROVIDER&gt;_API_KEY="..."./scripts/k8s/deploy.sh kubectl port-forward svc/openclaw 18789:18789 -n openclawopen http://localhost:18789
[/code]

Отримайте налаштований спільний секрет для інтерфейсу керування. Цей скрипт розгортання типово створює автентифікацію за токеном:

bashCopy code
[code]
    kubectl get secret openclaw-secrets -n openclaw -o jsonpath='{.data.OPENCLAW_GATEWAY_TOKEN}' | base64 -d
[/code]

Для локального налагодження `./scripts/k8s/deploy.sh --show-token` виводить токен після розгортання.

## Локальне тестування з Kind

Якщо у вас немає кластера, створіть його локально за допомогою [Kind](<https://kind.sigs.k8s.io/>):

bashCopy code
[code]
    ./scripts/k8s/create-kind.sh           # auto-detects docker or podman./scripts/k8s/create-kind.sh --delete  # tear down
[/code]

Потім розгорніть як зазвичай за допомогою `./scripts/k8s/deploy.sh`.

## Покроково

### 1) Розгортання

**Варіант A** — API-ключ у середовищі (один крок):

bashCopy code
[code]
    # Replace with your provider: ANTHROPIC, GEMINI, OPENAI, or OPENROUTERexport &lt;PROVIDER&gt;_API_KEY="..."./scripts/k8s/deploy.sh
[/code]

Скрипт створює Kubernetes Secret з API-ключем і автоматично згенерованим токеном Gateway, а потім виконує розгортання. Якщо Secret уже існує, він зберігає поточний токен Gateway і всі ключі провайдерів, які не змінюються.

**Варіант B** — створіть secret окремо:

bashCopy code
[code]
    export &lt;PROVIDER&gt;_API_KEY="..."./scripts/k8s/deploy.sh --create-secret./scripts/k8s/deploy.sh
[/code]

Використайте `--show-token` з будь-якою командою, якщо хочете вивести токен у stdout для локального тестування.

### 2) Доступ до Gateway

bashCopy code
[code]
    kubectl port-forward svc/openclaw 18789:18789 -n openclawopen http://localhost:18789
[/code]

## Що розгортається

CodeCopy code
[code]
    Namespace: openclaw (configurable via OPENCLAW_NAMESPACE)├── Deployment/openclaw        # Single pod, init container + gateway├── Service/openclaw           # ClusterIP on port 18789├── PersistentVolumeClaim      # 10Gi for agent state and config├── ConfigMap/openclaw-config  # openclaw.json + AGENTS.md└── Secret/openclaw-secrets    # Gateway token + API keys
[/code]

## Налаштування

### Інструкції агента

Відредагуйте `AGENTS.md` у `scripts/k8s/manifests/configmap.yaml` і розгорніть повторно:

bashCopy code
[code]
    ./scripts/k8s/deploy.sh
[/code]

### Конфігурація Gateway

Відредагуйте `openclaw.json` у `scripts/k8s/manifests/configmap.yaml`. Повний довідник див. у [конфігурації Gateway](</uk/gateway/configuration>).

### Додавання провайдерів

Запустіть повторно з експортованими додатковими ключами:

bashCopy code
[code]
    export ANTHROPIC_API_KEY="..."export OPENAI_API_KEY="..."./scripts/k8s/deploy.sh --create-secret./scripts/k8s/deploy.sh
[/code]

Наявні ключі провайдерів залишаються в Secret, якщо ви їх не перезапишете.

Або оновіть Secret напряму:

bashCopy code
[code]
    kubectl patch secret openclaw-secrets -n openclaw \  -p '{"stringData":{"&lt;PROVIDER&gt;_API_KEY":"..."}}'kubectl rollout restart deployment/openclaw -n openclaw
[/code]

### Користувацький namespace

bashCopy code
[code]
    OPENCLAW_NAMESPACE=my-namespace ./scripts/k8s/deploy.sh
[/code]

### Користувацький образ

Відредагуйте поле `image` у `scripts/k8s/manifests/deployment.yaml`:

yamlCopy code
[code]
    image: ghcr.io/openclaw/openclaw:latest # or pin to a specific version from https://github.com/openclaw/openclaw/releases
[/code]

### Відкриття доступу за межами port-forward

Стандартні маніфести прив’язують Gateway до loopback усередині pod. Це працює з `kubectl port-forward`, але не працює з Kubernetes `Service` або шляхом Ingress, якому потрібно дістатися до IP pod.

Якщо ви хочете відкрити Gateway через Ingress або балансувальник навантаження:

  * Змініть прив’язку Gateway у `scripts/k8s/manifests/configmap.yaml` з `loopback` на не-loopback прив’язку, що відповідає вашій моделі розгортання
  * Залиште автентифікацію Gateway увімкненою та використовуйте належну вхідну точку із завершенням TLS
  * Налаштуйте інтерфейс керування для віддаленого доступу за підтримуваною моделлю веббезпеки (наприклад, HTTPS/Tailscale Serve і явні дозволені origins за потреби)


## Повторне розгортання

bashCopy code
[code]
    ./scripts/k8s/deploy.sh
[/code]

Це застосовує всі маніфести та перезапускає pod, щоб підхопити будь-які зміни конфігурації або secret.

## Видалення

bashCopy code
[code]
    ./scripts/k8s/deploy.sh --delete
[/code]

Це видаляє namespace і всі ресурси в ньому, включно з PVC.

## Архітектурні примітки

  * Gateway типово прив’язується до loopback усередині pod, тому включене налаштування призначене для `kubectl port-forward`
  * Немає ресурсів рівня кластера — усе розміщено в одному namespace
  * Безпека: `readOnlyRootFilesystem`, можливості `drop: ALL`, користувач без root-прав (UID 1000)
  * Стандартна конфігурація тримає інтерфейс керування на безпечнішому шляху локального доступу: прив’язка loopback плюс `kubectl port-forward` до `http://127.0.0.1:18789`
  * Якщо ви виходите за межі доступу через localhost, використовуйте підтримувану віддалену модель: HTTPS/Tailscale плюс відповідна прив’язка Gateway і налаштування origin для інтерфейсу керування
  * Secrets генеруються в тимчасовому каталозі та застосовуються безпосередньо до кластера — секретні матеріали не записуються в робочу копію репозиторію


## Структура файлів

CodeCopy code
[code]
    scripts/k8s/├── deploy.sh                   # Creates namespace + secret, deploys via kustomize├── create-kind.sh              # Local Kind cluster (auto-detects docker/podman)└── manifests/    ├── kustomization.yaml      # Kustomize base    ├── configmap.yaml          # openclaw.json + AGENTS.md    ├── deployment.yaml         # Pod spec with security hardening    ├── pvc.yaml                # 10Gi persistent storage    └── service.yaml            # ClusterIP on 18789
[/code]

## Пов’язане

  * [Docker](</uk/install/docker>)
  * [Середовище виконання Docker VM](</uk/install/docker-vm-runtime>)
  * [Огляд встановлення](</uk/install>)


Was this useful?YesNo