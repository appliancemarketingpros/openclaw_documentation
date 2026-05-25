---
title: Kubernetes
source_url: https://docs.openclaw.ai/nl/install/kubernetes
scraped_at: 2026-05-25
---

Een minimaal startpunt om OpenClaw op Kubernetes uit te voeren — geen productieklare deployment. Het behandelt de kernresources en is bedoeld om aan je omgeving te worden aangepast.

## Waarom geen Helm?

OpenClaw is één container met enkele configuratiebestanden. De interessante aanpassing zit in agentinhoud (Markdown-bestanden, Skills, configuratie-overschrijvingen), niet in infrastructuurtemplating. Kustomize verwerkt overlays zonder de overhead van een Helm chart. Als je deployment complexer wordt, kan een Helm chart bovenop deze manifests worden gelegd.

## Wat je nodig hebt

  * Een draaiend Kubernetes-cluster (AKS, EKS, GKE, k3s, kind, OpenShift, enz.)
  * `kubectl` verbonden met je cluster
  * Een API-sleutel voor ten minste één modelprovider


## Snelle start

bashCopy code
[code]
    # Replace with your provider: ANTHROPIC, GEMINI, OPENAI, or OPENROUTERexport &lt;PROVIDER&gt;_API_KEY="..."./scripts/k8s/deploy.sh kubectl port-forward svc/openclaw 18789:18789 -n openclawopen http://localhost:18789
[/code]

Haal het geconfigureerde gedeelde geheim op voor de Control UI. Dit deploy-script maakt standaard tokenauthenticatie aan:

bashCopy code
[code]
    kubectl get secret openclaw-secrets -n openclaw -o jsonpath='{.data.OPENCLAW_GATEWAY_TOKEN}' | base64 -d
[/code]

Voor lokale debugging drukt `./scripts/k8s/deploy.sh --show-token` het token af na de deployment.

## Lokaal testen met Kind

Als je geen cluster hebt, maak er dan lokaal een aan met [Kind](<https://kind.sigs.k8s.io/>):

bashCopy code
[code]
    ./scripts/k8s/create-kind.sh           # auto-detects docker or podman./scripts/k8s/create-kind.sh --delete  # tear down
[/code]

Deploy daarna zoals gebruikelijk met `./scripts/k8s/deploy.sh`.

## Stap voor stap

### 1) Deployen

**Optie A** — API-sleutel in de omgeving (één stap):

bashCopy code
[code]
    # Replace with your provider: ANTHROPIC, GEMINI, OPENAI, or OPENROUTERexport &lt;PROVIDER&gt;_API_KEY="..."./scripts/k8s/deploy.sh
[/code]

Het script maakt een Kubernetes Secret aan met de API-sleutel en een automatisch gegenereerd gateway-token, en deployt daarna. Als de Secret al bestaat, behoudt het script het huidige gateway-token en provider-sleutels die niet worden gewijzigd.

**Optie B** — maak het secret apart aan:

bashCopy code
[code]
    export &lt;PROVIDER&gt;_API_KEY="..."./scripts/k8s/deploy.sh --create-secret./scripts/k8s/deploy.sh
[/code]

Gebruik `--show-token` met een van beide opdrachten als je het token voor lokale tests naar stdout wilt laten afdrukken.

### 2) Toegang tot de Gateway

bashCopy code
[code]
    kubectl port-forward svc/openclaw 18789:18789 -n openclawopen http://localhost:18789
[/code]

## Wat wordt gedeployed

CodeCopy code
[code]
    Namespace: openclaw (configurable via OPENCLAW_NAMESPACE)├── Deployment/openclaw        # Single pod, init container + gateway├── Service/openclaw           # ClusterIP on port 18789├── PersistentVolumeClaim      # 10Gi for agent state and config├── ConfigMap/openclaw-config  # openclaw.json + AGENTS.md└── Secret/openclaw-secrets    # Gateway token + API keys
[/code]

## Aanpassing

### Agentinstructies

Bewerk de `AGENTS.md` in `scripts/k8s/manifests/configmap.yaml` en deploy opnieuw:

bashCopy code
[code]
    ./scripts/k8s/deploy.sh
[/code]

### Gateway-configuratie

Bewerk `openclaw.json` in `scripts/k8s/manifests/configmap.yaml`. Zie [Gateway-configuratie](</nl/gateway/configuration>) voor de volledige referentie.

### Providers toevoegen

Voer opnieuw uit met extra geëxporteerde sleutels:

bashCopy code
[code]
    export ANTHROPIC_API_KEY="..."export OPENAI_API_KEY="..."./scripts/k8s/deploy.sh --create-secret./scripts/k8s/deploy.sh
[/code]

Bestaande provider-sleutels blijven in de Secret staan, tenzij je ze overschrijft.

Of patch de Secret direct:

bashCopy code
[code]
    kubectl patch secret openclaw-secrets -n openclaw \  -p '{"stringData":{"&lt;PROVIDER&gt;_API_KEY":"..."}}'kubectl rollout restart deployment/openclaw -n openclaw
[/code]

### Aangepaste namespace

bashCopy code
[code]
    OPENCLAW_NAMESPACE=my-namespace ./scripts/k8s/deploy.sh
[/code]

### Aangepaste image

Bewerk het veld `image` in `scripts/k8s/manifests/deployment.yaml`:

yamlCopy code
[code]
    image: ghcr.io/openclaw/openclaw:latest # or pin to a specific version from https://github.com/openclaw/openclaw/releases
[/code]

### Beschikbaar maken buiten port-forward

De standaardmanifests binden de Gateway binnen de pod aan loopback. Dat werkt met `kubectl port-forward`, maar niet met een Kubernetes `Service` of Ingress-pad dat het pod-IP moet kunnen bereiken.

Als je de Gateway via een Ingress of load balancer wilt beschikbaar maken:

  * Wijzig de Gateway-bind in `scripts/k8s/manifests/configmap.yaml` van `loopback` naar een niet-loopback-bind die past bij je deploymentmodel
  * Houd Gateway-authenticatie ingeschakeld en gebruik een passend TLS-beëindigd toegangspunt
  * Configureer de Control UI voor externe toegang met het ondersteunde webbeveiligingsmodel (bijvoorbeeld HTTPS/Tailscale Serve en expliciet toegestane origins wanneer nodig)


## Opnieuw deployen

bashCopy code
[code]
    ./scripts/k8s/deploy.sh
[/code]

Dit past alle manifests toe en herstart de pod om eventuele configuratie- of secret-wijzigingen op te pakken.

## Verwijderen

bashCopy code
[code]
    ./scripts/k8s/deploy.sh --delete
[/code]

Dit verwijdert de namespace en alle resources daarin, inclusief de PVC.

## Architectuurnotities

  * De Gateway bindt standaard binnen de pod aan loopback, dus de meegeleverde setup is bedoeld voor `kubectl port-forward`
  * Geen cluster-scoped resources — alles staat in één namespace
  * Beveiliging: `readOnlyRootFilesystem`, `drop: ALL`-capabilities, niet-rootgebruiker (UID 1000)
  * De standaardconfiguratie houdt de Control UI op het veiligere pad voor lokale toegang: loopback-bind plus `kubectl port-forward` naar `http://127.0.0.1:18789`
  * Als je verder gaat dan toegang via localhost, gebruik dan het ondersteunde externe model: HTTPS/Tailscale plus de juiste Gateway-bind en origin-instellingen voor de Control UI
  * Secrets worden gegenereerd in een tijdelijke map en direct op het cluster toegepast — er wordt geen geheim materiaal naar de repo-checkout geschreven


## Bestandsstructuur

CodeCopy code
[code]
    scripts/k8s/├── deploy.sh                   # Creates namespace + secret, deploys via kustomize├── create-kind.sh              # Local Kind cluster (auto-detects docker/podman)└── manifests/    ├── kustomization.yaml      # Kustomize base    ├── configmap.yaml          # openclaw.json + AGENTS.md    ├── deployment.yaml         # Pod spec with security hardening    ├── pvc.yaml                # 10Gi persistent storage    └── service.yaml            # ClusterIP on 18789
[/code]

## Gerelateerd

  * [Docker](</nl/install/docker>)
  * [Docker VM-runtime](</nl/install/docker-vm-runtime>)
  * [Installatieoverzicht](</nl/install>)


Was this useful?YesNo