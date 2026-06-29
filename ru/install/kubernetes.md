---
title: Kubernetes
source_url: https://docs.openclaw.ai/ru/install/kubernetes
scraped_at: 2026-06-29
---

InstallHosting

Минимальная отправная точка для запуска OpenClaw в Kubernetes — не готовое к production-развертывание. Она охватывает основные ресурсы и рассчитана на адаптацию под вашу среду.

## Почему не Helm?

OpenClaw — это один контейнер с несколькими файлами конфигурации. Основная кастомизация находится в содержимом агента (Markdown-файлы, Skills, переопределения конфигурации), а не в шаблонизации инфраструктуры. Kustomize обрабатывает оверлеи без накладных расходов Helm-чарта. Если ваше развертывание станет сложнее, Helm-чарт можно наложить поверх этих манифестов.

## Что вам нужно

  * Работающий кластер Kubernetes (AKS, EKS, GKE, k3s, kind, OpenShift и т. д.)
  * `kubectl`, подключенный к вашему кластеру
  * API-ключ хотя бы для одного поставщика моделей


## Быстрый старт

bashCopy code
[code]
    # Replace with your provider: ANTHROPIC, GEMINI, OPENAI, or OPENROUTERexport &lt;PROVIDER&gt;_API_KEY="..."./scripts/k8s/deploy.sh kubectl port-forward svc/openclaw 18789:18789 -n openclawopen http://localhost:18789
[/code]

Получите настроенный общий секрет для Control UI. Этот скрипт развертывания по умолчанию создает аутентификацию по токену:

bashCopy code
[code]
    kubectl get secret openclaw-secrets -n openclaw -o jsonpath='{.data.OPENCLAW_GATEWAY_TOKEN}' | base64 -d
[/code]

Для локальной отладки `./scripts/k8s/deploy.sh --show-token` выводит токен после развертывания.

## Локальное тестирование с Kind

Если у вас нет кластера, создайте его локально с помощью [Kind](<https://kind.sigs.k8s.io/>):

bashCopy code
[code]
    ./scripts/k8s/create-kind.sh           # auto-detects docker or podman./scripts/k8s/create-kind.sh --delete  # tear down
[/code]

Затем разверните как обычно с помощью `./scripts/k8s/deploy.sh`.

## Пошагово

### 1) Развертывание

**Вариант A** — API-ключ в окружении (один шаг):

bashCopy code
[code]
    # Replace with your provider: ANTHROPIC, GEMINI, OPENAI, or OPENROUTERexport &lt;PROVIDER&gt;_API_KEY="..."./scripts/k8s/deploy.sh
[/code]

Скрипт создает Kubernetes Secret с API-ключом и автоматически сгенерированным токеном Gateway, а затем выполняет развертывание. Если Secret уже существует, он сохраняет текущий токен Gateway и все ключи поставщиков, которые не меняются.

**Вариант B** — создать секрет отдельно:

bashCopy code
[code]
    export &lt;PROVIDER&gt;_API_KEY="..."./scripts/k8s/deploy.sh --create-secret./scripts/k8s/deploy.sh
[/code]

Используйте `--show-token` с любой из команд, если хотите вывести токен в stdout для локального тестирования.

### 2) Доступ к Gateway

bashCopy code
[code]
    kubectl port-forward svc/openclaw 18789:18789 -n openclawopen http://localhost:18789
[/code]

## Что развертывается

CodeCopy code
[code]
    Namespace: openclaw (configurable via OPENCLAW_NAMESPACE)├── Deployment/openclaw        # Single pod, init container + gateway├── Service/openclaw           # ClusterIP on port 18789├── PersistentVolumeClaim      # 10Gi for agent state and config├── ConfigMap/openclaw-config  # openclaw.json + AGENTS.md└── Secret/openclaw-secrets    # Gateway token + API keys
[/code]

## Кастомизация

### Инструкции агента

Отредактируйте `AGENTS.md` в `scripts/k8s/manifests/configmap.yaml` и разверните повторно:

bashCopy code
[code]
    ./scripts/k8s/deploy.sh
[/code]

### Конфигурация Gateway

Отредактируйте `openclaw.json` в `scripts/k8s/manifests/configmap.yaml`. Полный справочник см. в разделе [конфигурация Gateway](</ru/gateway/configuration>).

### Добавление провайдеров

Запустите повторно с экспортированными дополнительными ключами:

bashCopy code
[code]
    export ANTHROPIC_API_KEY="..."export OPENAI_API_KEY="..."./scripts/k8s/deploy.sh --create-secret./scripts/k8s/deploy.sh
[/code]

Существующие ключи провайдеров останутся в Secret, если вы их не перезапишете.

Или измените Secret напрямую:

bashCopy code
[code]
    kubectl patch secret openclaw-secrets -n openclaw \  -p '{"stringData":{"&lt;PROVIDER&gt;_API_KEY":"..."}}'kubectl rollout restart deployment/openclaw -n openclaw
[/code]

### Пользовательское пространство имен

bashCopy code
[code]
    OPENCLAW_NAMESPACE=my-namespace ./scripts/k8s/deploy.sh
[/code]

### Пользовательский образ

Отредактируйте поле `image` в `scripts/k8s/manifests/deployment.yaml`:

yamlCopy code
[code]
    image: ghcr.io/openclaw/openclaw:latest # primary; official Docker Hub mirror: openclaw/openclaw:latest
[/code]

### Открытие доступа за пределами port-forward

Манифесты по умолчанию привязывают Gateway к loopback внутри пода. Это работает с `kubectl port-forward`, но не работает с Kubernetes `Service` или путем Ingress, которому нужно обращаться к IP пода.

Если вы хотите открыть доступ к Gateway через Ingress или балансировщик нагрузки:

  * Измените привязку Gateway в `scripts/k8s/manifests/configmap.yaml` с `loopback` на не-loopback-привязку, соответствующую вашей модели развертывания
  * Оставьте аутентификацию Gateway включенной и используйте корректную точку входа с завершением TLS
  * Настройте Control UI для удаленного доступа с использованием поддерживаемой модели веб-безопасности (например, HTTPS/Tailscale Serve и явно разрешенные источники при необходимости)


## Повторное развертывание

bashCopy code
[code]
    ./scripts/k8s/deploy.sh
[/code]

Это применяет все манифесты и перезапускает под, чтобы подхватить любые изменения конфигурации или секретов.

## Удаление

bashCopy code
[code]
    ./scripts/k8s/deploy.sh --delete
[/code]

Это удаляет пространство имен и все ресурсы в нем, включая PVC.

## Заметки об архитектуре

  * По умолчанию Gateway привязывается к loopback внутри пода, поэтому включенная настройка предназначена для `kubectl port-forward`
  * Нет ресурсов уровня кластера — все находится в одном пространстве имен
  * Безопасность: `readOnlyRootFilesystem`, возможности `drop: ALL`, пользователь без root-прав (UID 1000)
  * Конфигурация по умолчанию оставляет Control UI на более безопасном пути локального доступа: привязка к loopback плюс `kubectl port-forward` на `http://127.0.0.1:18789`
  * Если вы выходите за пределы доступа с localhost, используйте поддерживаемую удаленную модель: HTTPS/Tailscale плюс подходящая привязка Gateway и настройки источников Control UI
  * Секреты генерируются во временном каталоге и применяются напрямую к кластеру — секретные данные не записываются в рабочую копию репозитория


## Структура файлов

CodeCopy code
[code]
    scripts/k8s/├── deploy.sh                   # Creates namespace + secret, deploys via kustomize├── create-kind.sh              # Local Kind cluster (auto-detects docker/podman)└── manifests/    ├── kustomization.yaml      # Kustomize base    ├── configmap.yaml          # openclaw.json + AGENTS.md    ├── deployment.yaml         # Pod spec with security hardening    ├── pvc.yaml                # 10Gi persistent storage    └── service.yaml            # ClusterIP on 18789
[/code]

## Связанные материалы

  * [Docker](</ru/install/docker>)
  * [Среда выполнения Docker VM](</ru/install/docker-vm-runtime>)
  * [Обзор установки](</ru/install>)


Was this useful?YesNo

Open issue