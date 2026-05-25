---
title: Kubernetes
source_url: https://docs.openclaw.ai/it/install/kubernetes
scraped_at: 2026-05-25
---

Un punto di partenza minimale per eseguire OpenClaw su Kubernetes: non un deployment pronto per la produzione. Copre le risorse principali ed è pensato per essere adattato al tuo ambiente.

## Perché non Helm?

OpenClaw è un singolo container con alcuni file di configurazione. La personalizzazione più rilevante riguarda il contenuto degli agenti (file Markdown, Skills, override di configurazione), non il templating dell’infrastruttura. Kustomize gestisce gli overlay senza il sovraccarico di un chart Helm. Se il deployment diventa più complesso, è possibile aggiungere un chart Helm sopra questi manifest.

## Cosa serve

  * Un cluster Kubernetes in esecuzione (AKS, EKS, GKE, k3s, kind, OpenShift, ecc.)
  * `kubectl` connesso al tuo cluster
  * Una chiave API per almeno un provider di modelli


## Avvio rapido

bashCopy code
[code]
    # Replace with your provider: ANTHROPIC, GEMINI, OPENAI, or OPENROUTERexport &lt;PROVIDER&gt;_API_KEY="..."./scripts/k8s/deploy.sh kubectl port-forward svc/openclaw 18789:18789 -n openclawopen http://localhost:18789
[/code]

Recupera il segreto condiviso configurato per la Control UI. Questo script di deployment crea l’autenticazione tramite token per impostazione predefinita:

bashCopy code
[code]
    kubectl get secret openclaw-secrets -n openclaw -o jsonpath='{.data.OPENCLAW_GATEWAY_TOKEN}' | base64 -d
[/code]

Per il debug locale, `./scripts/k8s/deploy.sh --show-token` stampa il token dopo il deployment.

## Test locale con Kind

Se non hai un cluster, creane uno in locale con [Kind](<https://kind.sigs.k8s.io/>):

bashCopy code
[code]
    ./scripts/k8s/create-kind.sh           # auto-detects docker or podman./scripts/k8s/create-kind.sh --delete  # tear down
[/code]

Poi esegui il deployment come di consueto con `./scripts/k8s/deploy.sh`.

## Passo per passo

### 1) Esegui il deployment

**Opzione A** — chiave API nell’ambiente (un solo passaggio):

bashCopy code
[code]
    # Replace with your provider: ANTHROPIC, GEMINI, OPENAI, or OPENROUTERexport &lt;PROVIDER&gt;_API_KEY="..."./scripts/k8s/deploy.sh
[/code]

Lo script crea un Secret Kubernetes con la chiave API e un token Gateway generato automaticamente, poi esegue il deployment. Se il Secret esiste già, conserva il token Gateway corrente e le eventuali chiavi provider che non vengono modificate.

**Opzione B** — crea il secret separatamente:

bashCopy code
[code]
    export &lt;PROVIDER&gt;_API_KEY="..."./scripts/k8s/deploy.sh --create-secret./scripts/k8s/deploy.sh
[/code]

Usa `--show-token` con uno dei due comandi se vuoi stampare il token su stdout per il test locale.

### 2) Accedi al gateway

bashCopy code
[code]
    kubectl port-forward svc/openclaw 18789:18789 -n openclawopen http://localhost:18789
[/code]

## Cosa viene distribuito

CodeCopy code
[code]
    Namespace: openclaw (configurable via OPENCLAW_NAMESPACE)├── Deployment/openclaw        # Single pod, init container + gateway├── Service/openclaw           # ClusterIP on port 18789├── PersistentVolumeClaim      # 10Gi for agent state and config├── ConfigMap/openclaw-config  # openclaw.json + AGENTS.md└── Secret/openclaw-secrets    # Gateway token + API keys
[/code]

## Personalizzazione

### Istruzioni per l’agente

Modifica `AGENTS.md` in `scripts/k8s/manifests/configmap.yaml` ed esegui di nuovo il deployment:

bashCopy code
[code]
    ./scripts/k8s/deploy.sh
[/code]

### Configurazione del Gateway

Modifica `openclaw.json` in `scripts/k8s/manifests/configmap.yaml`. Consulta [Configurazione del Gateway](</it/gateway/configuration>) per il riferimento completo.

### Aggiungere provider

Esegui di nuovo con chiavi aggiuntive esportate:

bashCopy code
[code]
    export ANTHROPIC_API_KEY="..."export OPENAI_API_KEY="..."./scripts/k8s/deploy.sh --create-secret./scripts/k8s/deploy.sh
[/code]

Le chiavi provider esistenti restano nel Secret a meno che tu non le sovrascriva.

Oppure applica una patch direttamente al Secret:

bashCopy code
[code]
    kubectl patch secret openclaw-secrets -n openclaw \  -p '{"stringData":{"&lt;PROVIDER&gt;_API_KEY":"..."}}'kubectl rollout restart deployment/openclaw -n openclaw
[/code]

### Namespace personalizzato

bashCopy code
[code]
    OPENCLAW_NAMESPACE=my-namespace ./scripts/k8s/deploy.sh
[/code]

### Immagine personalizzata

Modifica il campo `image` in `scripts/k8s/manifests/deployment.yaml`:

yamlCopy code
[code]
    image: ghcr.io/openclaw/openclaw:latest # or pin to a specific version from https://github.com/openclaw/openclaw/releases
[/code]

### Esporre oltre il port-forward

I manifest predefiniti associano il Gateway a loopback all’interno del pod. Questo funziona con `kubectl port-forward`, ma non funziona con un `Service` Kubernetes o un percorso Ingress che deve raggiungere l’IP del pod.

Se vuoi esporre il Gateway tramite un Ingress o un bilanciatore di carico:

  * Cambia il bind del Gateway in `scripts/k8s/manifests/configmap.yaml` da `loopback` a un bind non loopback compatibile con il tuo modello di deployment
  * Mantieni l’autenticazione del Gateway abilitata e usa un entrypoint adeguato con terminazione TLS
  * Configura la Control UI per l’accesso remoto usando il modello di sicurezza web supportato (per esempio HTTPS/Tailscale Serve e origini consentite esplicite quando necessario)


## Rieseguire il deployment

bashCopy code
[code]
    ./scripts/k8s/deploy.sh
[/code]

Questo applica tutti i manifest e riavvia il pod per acquisire eventuali modifiche alla configurazione o ai secret.

## Rimozione

bashCopy code
[code]
    ./scripts/k8s/deploy.sh --delete
[/code]

Questo elimina il namespace e tutte le risorse al suo interno, incluso il PVC.

## Note sull’architettura

  * Il Gateway si associa per impostazione predefinita a loopback all’interno del pod, quindi la configurazione inclusa è per `kubectl port-forward`
  * Nessuna risorsa con ambito cluster: tutto risiede in un singolo namespace
  * Sicurezza: `readOnlyRootFilesystem`, capability `drop: ALL`, utente non root (UID 1000)
  * La configurazione predefinita mantiene la Control UI sul percorso più sicuro di accesso locale: bind loopback più `kubectl port-forward` verso `http://127.0.0.1:18789`
  * Se passi oltre l’accesso localhost, usa il modello remoto supportato: HTTPS/Tailscale più il bind Gateway appropriato e le impostazioni di origine della Control UI
  * I secret vengono generati in una directory temporanea e applicati direttamente al cluster: nessun materiale segreto viene scritto nel checkout del repository


## Struttura dei file

CodeCopy code
[code]
    scripts/k8s/├── deploy.sh                   # Creates namespace + secret, deploys via kustomize├── create-kind.sh              # Local Kind cluster (auto-detects docker/podman)└── manifests/    ├── kustomization.yaml      # Kustomize base    ├── configmap.yaml          # openclaw.json + AGENTS.md    ├── deployment.yaml         # Pod spec with security hardening    ├── pvc.yaml                # 10Gi persistent storage    └── service.yaml            # ClusterIP on 18789
[/code]

## Correlati

  * [Docker](</it/install/docker>)
  * [Runtime Docker VM](</it/install/docker-vm-runtime>)
  * [Panoramica dell’installazione](</it/install>)


Was this useful?YesNo