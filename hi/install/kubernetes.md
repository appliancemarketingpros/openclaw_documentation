---
title: Kubernetes
source_url: https://docs.openclaw.ai/hi/install/kubernetes
scraped_at: 2026-06-29
---

InstallHosting

OpenClaw को Kubernetes पर चलाने के लिए एक न्यूनतम शुरुआती बिंदु — production-ready deployment नहीं। यह core resources को कवर करता है और इसे आपके environment के अनुसार अनुकूलित करने के लिए बनाया गया है।

## Helm क्यों नहीं?

OpenClaw कुछ config files वाला एक single container है। मुख्य customization agent content (markdown files, skills, config overrides) में है, infrastructure templating में नहीं। Kustomize Helm chart के overhead के बिना overlays संभालता है। अगर आपका deployment अधिक जटिल हो जाता है, तो इन manifests के ऊपर Helm chart की layer जोड़ी जा सकती है।

## आपको क्या चाहिए

  * चल रहा Kubernetes cluster (AKS, EKS, GKE, k3s, kind, OpenShift, आदि)
  * आपके cluster से जुड़ा `kubectl`
  * कम से कम एक model provider के लिए API key


## Quick start

bashCopy code
[code]
    # Replace with your provider: ANTHROPIC, GEMINI, OPENAI, or OPENROUTERexport &lt;PROVIDER&gt;_API_KEY="..."./scripts/k8s/deploy.sh kubectl port-forward svc/openclaw 18789:18789 -n openclawopen http://localhost:18789
[/code]

Control UI के लिए configured shared secret प्राप्त करें। यह deploy script default रूप से token auth बनाती है:

bashCopy code
[code]
    kubectl get secret openclaw-secrets -n openclaw -o jsonpath='{.data.OPENCLAW_GATEWAY_TOKEN}' | base64 -d
[/code]

Local debugging के लिए, `./scripts/k8s/deploy.sh --show-token` deploy के बाद token print करता है।

## Kind के साथ local testing

अगर आपके पास cluster नहीं है, तो [Kind](<https://kind.sigs.k8s.io/>) के साथ locally एक बनाएं:

bashCopy code
[code]
    ./scripts/k8s/create-kind.sh           # auto-detects docker or podman./scripts/k8s/create-kind.sh --delete  # tear down
[/code]

फिर हमेशा की तरह `./scripts/k8s/deploy.sh` के साथ deploy करें।

## Step by step

### 1) Deploy

**Option A** — environment में API key (एक step):

bashCopy code
[code]
    # Replace with your provider: ANTHROPIC, GEMINI, OPENAI, or OPENROUTERexport &lt;PROVIDER&gt;_API_KEY="..."./scripts/k8s/deploy.sh
[/code]

Script API key और auto-generated gateway token के साथ Kubernetes Secret बनाती है, फिर deploy करती है। अगर Secret पहले से मौजूद है, तो यह current gateway token और नहीं बदली जा रही provider keys को preserve करती है।

**Option B** — secret अलग से बनाएं:

bashCopy code
[code]
    export &lt;PROVIDER&gt;_API_KEY="..."./scripts/k8s/deploy.sh --create-secret./scripts/k8s/deploy.sh
[/code]

अगर आप local testing के लिए token को stdout पर print करना चाहते हैं, तो किसी भी command के साथ `--show-token` का उपयोग करें।

### 2) Gateway access करें

bashCopy code
[code]
    kubectl port-forward svc/openclaw 18789:18789 -n openclawopen http://localhost:18789
[/code]

## क्या deploy होता है

CodeCopy code
[code]
    Namespace: openclaw (configurable via OPENCLAW_NAMESPACE)├── Deployment/openclaw        # Single pod, init container + gateway├── Service/openclaw           # ClusterIP on port 18789├── PersistentVolumeClaim      # 10Gi for agent state and config├── ConfigMap/openclaw-config  # openclaw.json + AGENTS.md└── Secret/openclaw-secrets    # Gateway token + API keys
[/code]

## Customization

### Agent instructions

`scripts/k8s/manifests/configmap.yaml` में `AGENTS.md` edit करें और redeploy करें:

bashCopy code
[code]
    ./scripts/k8s/deploy.sh
[/code]

### Gateway config

`scripts/k8s/manifests/configmap.yaml` में `openclaw.json` edit करें। पूरी reference के लिए [Gateway configuration](</hi/gateway/configuration>) देखें।

### Providers जोड़ें

Additional keys export करके फिर से चलाएं:

bashCopy code
[code]
    export ANTHROPIC_API_KEY="..."export OPENAI_API_KEY="..."./scripts/k8s/deploy.sh --create-secret./scripts/k8s/deploy.sh
[/code]

Existing provider keys Secret में रहती हैं जब तक आप उन्हें overwrite नहीं करते।

या Secret को directly patch करें:

bashCopy code
[code]
    kubectl patch secret openclaw-secrets -n openclaw \  -p '{"stringData":{"&lt;PROVIDER&gt;_API_KEY":"..."}}'kubectl rollout restart deployment/openclaw -n openclaw
[/code]

### Custom namespace

bashCopy code
[code]
    OPENCLAW_NAMESPACE=my-namespace ./scripts/k8s/deploy.sh
[/code]

### Custom image

`scripts/k8s/manifests/deployment.yaml` में `image` field edit करें:

yamlCopy code
[code]
    image: ghcr.io/openclaw/openclaw:latest # primary; official Docker Hub mirror: openclaw/openclaw:latest
[/code]

### Port-forward से आगे expose करें

Default manifests gateway को pod के अंदर loopback से bind करते हैं। यह `kubectl port-forward` के साथ काम करता है, लेकिन ऐसे Kubernetes `Service` या Ingress path के साथ काम नहीं करता जिसे pod IP तक पहुंचना होता है।

अगर आप gateway को Ingress या load balancer के through expose करना चाहते हैं:

  * `scripts/k8s/manifests/configmap.yaml` में gateway bind को `loopback` से बदलकर अपने deployment model से matching non-loopback bind करें
  * Gateway auth enabled रखें और proper TLS-terminated entrypoint का उपयोग करें
  * Supported web security model का उपयोग करके remote access के लिए Control UI configure करें (उदाहरण के लिए HTTPS/Tailscale Serve और जरूरत होने पर explicit allowed origins)


## Re-deploy

bashCopy code
[code]
    ./scripts/k8s/deploy.sh
[/code]

यह सभी manifests apply करता है और किसी भी config या secret changes को pick up करने के लिए pod restart करता है।

## Teardown

bashCopy code
[code]
    ./scripts/k8s/deploy.sh --delete
[/code]

यह namespace और उसमें मौजूद सभी resources delete करता है, जिसमें PVC भी शामिल है।

## Architecture notes

  * Gateway default रूप से pod के अंदर loopback से bind होता है, इसलिए included setup `kubectl port-forward` के लिए है
  * कोई cluster-scoped resources नहीं — सब कुछ एक single namespace में रहता है
  * Security: `readOnlyRootFilesystem`, `drop: ALL` capabilities, non-root user (UID 1000)
  * Default config Control UI को safer local-access path पर रखता है: loopback bind plus `kubectl port-forward` to `http://127.0.0.1:18789`
  * अगर आप localhost access से आगे बढ़ते हैं, तो supported remote model का उपयोग करें: HTTPS/Tailscale plus appropriate gateway bind and Control UI origin settings
  * Secrets temp directory में generate होते हैं और directly cluster पर apply किए जाते हैं — repo checkout में कोई secret material नहीं लिखा जाता


## File structure

CodeCopy code
[code]
    scripts/k8s/├── deploy.sh                   # Creates namespace + secret, deploys via kustomize├── create-kind.sh              # Local Kind cluster (auto-detects docker/podman)└── manifests/    ├── kustomization.yaml      # Kustomize base    ├── configmap.yaml          # openclaw.json + AGENTS.md    ├── deployment.yaml         # Pod spec with security hardening    ├── pvc.yaml                # 10Gi persistent storage    └── service.yaml            # ClusterIP on 18789
[/code]

## Related

  * [Docker](</hi/install/docker>)
  * [Docker VM runtime](</hi/install/docker-vm-runtime>)
  * [Install overview](</hi/install>)


Was this useful?YesNo

Open issue