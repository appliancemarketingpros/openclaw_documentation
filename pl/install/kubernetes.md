---
title: Kubernetes
source_url: https://docs.openclaw.ai/pl/install/kubernetes
scraped_at: 2026-05-25
---

Minimalny punkt wyjścia do uruchomienia OpenClaw na Kubernetes — nie jest to wdrożenie gotowe do produkcji. Obejmuje podstawowe zasoby i ma być dostosowane do Twojego środowiska.

## Dlaczego nie Helm?

OpenClaw to pojedynczy kontener z kilkoma plikami konfiguracyjnymi. Najważniejsze dostosowania dotyczą zawartości agentów (pliki markdown, Skills, nadpisania konfiguracji), a nie szablonów infrastruktury. Kustomize obsługuje nakładki bez narzutu wykresu Helm. Jeśli Twoje wdrożenie stanie się bardziej złożone, wykres Helm można nałożyć na te manifesty.

## Czego potrzebujesz

  * Działający klaster Kubernetes (AKS, EKS, GKE, k3s, kind, OpenShift itd.)
  * `kubectl` połączony z Twoim klastrem
  * Klucz API dla co najmniej jednego dostawcy modeli


## Szybki start

bashCopy code
[code]
    # Replace with your provider: ANTHROPIC, GEMINI, OPENAI, or OPENROUTERexport &lt;PROVIDER&gt;_API_KEY="..."./scripts/k8s/deploy.sh kubectl port-forward svc/openclaw 18789:18789 -n openclawopen http://localhost:18789
[/code]

Pobierz skonfigurowany współdzielony sekret dla Control UI. Ten skrypt wdrożeniowy domyślnie tworzy uwierzytelnianie tokenem:

bashCopy code
[code]
    kubectl get secret openclaw-secrets -n openclaw -o jsonpath='{.data.OPENCLAW_GATEWAY_TOKEN}' | base64 -d
[/code]

Do lokalnego debugowania `./scripts/k8s/deploy.sh --show-token` wypisuje token po wdrożeniu.

## Lokalne testowanie z Kind

Jeśli nie masz klastra, utwórz go lokalnie za pomocą [Kind](<https://kind.sigs.k8s.io/>):

bashCopy code
[code]
    ./scripts/k8s/create-kind.sh           # auto-detects docker or podman./scripts/k8s/create-kind.sh --delete  # tear down
[/code]

Następnie wdróż jak zwykle za pomocą `./scripts/k8s/deploy.sh`.

## Krok po kroku

### 1) Wdrożenie

**Opcja A** — klucz API w środowisku (jeden krok):

bashCopy code
[code]
    # Replace with your provider: ANTHROPIC, GEMINI, OPENAI, or OPENROUTERexport &lt;PROVIDER&gt;_API_KEY="..."./scripts/k8s/deploy.sh
[/code]

Skrypt tworzy Kubernetes Secret z kluczem API i automatycznie wygenerowanym tokenem Gateway, a następnie wdraża. Jeśli Secret już istnieje, zachowuje bieżący token Gateway oraz wszystkie klucze dostawców, które nie są zmieniane.

**Opcja B** — utwórz sekret osobno:

bashCopy code
[code]
    export &lt;PROVIDER&gt;_API_KEY="..."./scripts/k8s/deploy.sh --create-secret./scripts/k8s/deploy.sh
[/code]

Użyj `--show-token` z dowolnym poleceniem, jeśli chcesz wypisać token na stdout do lokalnego testowania.

### 2) Dostęp do Gateway

bashCopy code
[code]
    kubectl port-forward svc/openclaw 18789:18789 -n openclawopen http://localhost:18789
[/code]

## Co jest wdrażane

CodeCopy code
[code]
    Namespace: openclaw (configurable via OPENCLAW_NAMESPACE)├── Deployment/openclaw        # Single pod, init container + gateway├── Service/openclaw           # ClusterIP on port 18789├── PersistentVolumeClaim      # 10Gi for agent state and config├── ConfigMap/openclaw-config  # openclaw.json + AGENTS.md└── Secret/openclaw-secrets    # Gateway token + API keys
[/code]

## Dostosowanie

### Instrukcje agenta

Edytuj `AGENTS.md` w `scripts/k8s/manifests/configmap.yaml` i wdróż ponownie:

bashCopy code
[code]
    ./scripts/k8s/deploy.sh
[/code]

### Konfiguracja Gateway

Edytuj `openclaw.json` w `scripts/k8s/manifests/configmap.yaml`. Pełne odniesienie znajdziesz w [Konfiguracja Gateway](</pl/gateway/configuration>).

### Dodawanie dostawców

Uruchom ponownie z wyeksportowanymi dodatkowymi kluczami:

bashCopy code
[code]
    export ANTHROPIC_API_KEY="..."export OPENAI_API_KEY="..."./scripts/k8s/deploy.sh --create-secret./scripts/k8s/deploy.sh
[/code]

Istniejące klucze dostawców pozostają w Secret, chyba że je nadpiszesz.

Możesz też bezpośrednio spatchować Secret:

bashCopy code
[code]
    kubectl patch secret openclaw-secrets -n openclaw \  -p '{"stringData":{"&lt;PROVIDER&gt;_API_KEY":"..."}}'kubectl rollout restart deployment/openclaw -n openclaw
[/code]

### Niestandardowa przestrzeń nazw

bashCopy code
[code]
    OPENCLAW_NAMESPACE=my-namespace ./scripts/k8s/deploy.sh
[/code]

### Niestandardowy obraz

Edytuj pole `image` w `scripts/k8s/manifests/deployment.yaml`:

yamlCopy code
[code]
    image: ghcr.io/openclaw/openclaw:latest # or pin to a specific version from https://github.com/openclaw/openclaw/releases
[/code]

### Udostępnianie poza port-forward

Domyślne manifesty wiążą Gateway z loopback wewnątrz poda. Działa to z `kubectl port-forward`, ale nie działa z Kubernetes `Service` ani ścieżką Ingress, która musi dotrzeć do adresu IP poda.

Jeśli chcesz udostępnić Gateway przez Ingress lub load balancer:

  * Zmień powiązanie Gateway w `scripts/k8s/manifests/configmap.yaml` z `loopback` na powiązanie inne niż loopback, które pasuje do Twojego modelu wdrożenia
  * Pozostaw włączone uwierzytelnianie Gateway i użyj odpowiedniego punktu wejścia z terminacją TLS
  * Skonfiguruj Control UI do dostępu zdalnego przy użyciu obsługiwanego modelu bezpieczeństwa webowego (na przykład HTTPS/Tailscale Serve oraz jawnie dozwolonych źródeł, gdy są potrzebne)


## Ponowne wdrożenie

bashCopy code
[code]
    ./scripts/k8s/deploy.sh
[/code]

To stosuje wszystkie manifesty i restartuje poda, aby uwzględnić wszelkie zmiany konfiguracji lub sekretów.

## Usuwanie

bashCopy code
[code]
    ./scripts/k8s/deploy.sh --delete
[/code]

To usuwa przestrzeń nazw i wszystkie znajdujące się w niej zasoby, w tym PVC.

## Uwagi o architekturze

  * Gateway domyślnie wiąże się z loopback wewnątrz poda, więc dołączona konfiguracja jest przeznaczona dla `kubectl port-forward`
  * Brak zasobów o zasięgu klastra — wszystko znajduje się w jednej przestrzeni nazw
  * Bezpieczeństwo: `readOnlyRootFilesystem`, możliwości `drop: ALL`, użytkownik inny niż root (UID 1000)
  * Domyślna konfiguracja utrzymuje Control UI na bezpieczniejszej ścieżce dostępu lokalnego: powiązanie loopback plus `kubectl port-forward` do `http://127.0.0.1:18789`
  * Jeśli wychodzisz poza dostęp przez localhost, użyj obsługiwanego modelu zdalnego: HTTPS/Tailscale plus odpowiednie powiązanie Gateway i ustawienia źródeł Control UI
  * Sekrety są generowane w katalogu tymczasowym i stosowane bezpośrednio w klastrze — żaden materiał tajny nie jest zapisywany w kopii roboczej repozytorium


## Struktura plików

CodeCopy code
[code]
    scripts/k8s/├── deploy.sh                   # Creates namespace + secret, deploys via kustomize├── create-kind.sh              # Local Kind cluster (auto-detects docker/podman)└── manifests/    ├── kustomization.yaml      # Kustomize base    ├── configmap.yaml          # openclaw.json + AGENTS.md    ├── deployment.yaml         # Pod spec with security hardening    ├── pvc.yaml                # 10Gi persistent storage    └── service.yaml            # ClusterIP on 18789
[/code]

## Powiązane

  * [Docker](</pl/install/docker>)
  * [Środowisko uruchomieniowe Docker VM](</pl/install/docker-vm-runtime>)
  * [Przegląd instalacji](</pl/install>)


Was this useful?YesNo