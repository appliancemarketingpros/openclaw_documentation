---
title: Automatisation de la CLI
source_url: https://docs.openclaw.ai/fr/start/wizard-cli-automation
scraped_at: 2026-05-25
---

Use `--non-interactive` pour automatiser `openclaw onboard`.

## Exemple de base non interactif

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice apiKey \  --anthropic-api-key "$ANTHROPIC_API_KEY" \  --secret-input-mode plaintext \  --gateway-port 18789 \  --gateway-bind loopback \  --install-daemon \  --daemon-runtime node \  --skip-bootstrap \  --skip-skills
[/code]

Ajoutez `--json` pour obtenir un résumé lisible par machine.

Utilisez `--skip-bootstrap` lorsque votre automatisation préremplit les fichiers de l’espace de travail et ne souhaite pas que l’onboarding crée les fichiers de bootstrap par défaut.

Utilisez `--secret-input-mode ref` pour stocker des références adossées à l’environnement dans les profils d’authentification au lieu de valeurs en clair. La sélection interactive entre les références d’environnement et les références de fournisseur configurées (`file` ou `exec`) est disponible dans le flux d’onboarding.

En mode `ref` non interactif, les variables d’environnement du fournisseur doivent être définies dans l’environnement du processus. Le passage d’indicateurs de clé en ligne sans la variable d’environnement correspondante échoue désormais immédiatement.

Exemple :

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice openai-api-key \  --secret-input-mode ref \  --accept-risk
[/code]

## Exemples propres aux fournisseurs

Exemple de clé d’API Anthropic bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice apiKey \  --anthropic-api-key "$ANTHROPIC_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Exemple Gemini bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice gemini-api-key \  --gemini-api-key "$GEMINI_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Exemple Z.AI bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice zai-api-key \  --zai-api-key "$ZAI_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Exemple Vercel AI Gateway bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice ai-gateway-api-key \  --ai-gateway-api-key "$AI_GATEWAY_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Exemple Cloudflare AI Gateway bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice cloudflare-ai-gateway-api-key \  --cloudflare-ai-gateway-account-id "your-account-id" \  --cloudflare-ai-gateway-gateway-id "your-gateway-id" \  --cloudflare-ai-gateway-api-key "$CLOUDFLARE_AI_GATEWAY_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Exemple Moonshot bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice moonshot-api-key \  --moonshot-api-key "$MOONSHOT_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Exemple Mistral bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice mistral-api-key \  --mistral-api-key "$MISTRAL_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Exemple Synthetic bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice synthetic-api-key \  --synthetic-api-key "$SYNTHETIC_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Exemple OpenCode bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice opencode-zen \  --opencode-zen-api-key "$OPENCODE_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Basculez vers `--auth-choice opencode-go --opencode-go-api-key "$OPENCODE_API_KEY"` pour le catalogue Go.

Exemple Ollama bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice ollama \  --custom-model-id "qwen3.5:27b" \  --accept-risk \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Exemple de fournisseur personnalisé bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice custom-api-key \  --custom-base-url "https://llm.example.com/v1" \  --custom-model-id "foo-large" \  --custom-api-key "$CUSTOM_API_KEY" \  --custom-provider-id "my-custom" \  --custom-compatibility anthropic \  --custom-image-input \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

`--custom-api-key` est facultatif. S’il est omis, l’onboarding vérifie `CUSTOM_API_KEY`. OpenClaw marque automatiquement les ID de modèles de vision courants comme compatibles avec les images. Ajoutez `--custom-image-input` pour les ID de vision personnalisés inconnus, ou `--custom-text-input` pour forcer les métadonnées en texte uniquement.

Variante en mode ref :

bashCopy code
[code]
    export CUSTOM_API_KEY="your-key"openclaw onboard --non-interactive \  --mode local \  --auth-choice custom-api-key \  --custom-base-url "https://llm.example.com/v1" \  --custom-model-id "foo-large" \  --secret-input-mode ref \  --custom-provider-id "my-custom" \  --custom-compatibility anthropic \  --custom-image-input \  --gateway-port 18789 \  --gateway-bind loopback
[/code]

Dans ce mode, l’onboarding stocke `apiKey` sous la forme `{ source: "env", provider: "default", id: "CUSTOM_API_KEY" }`.

Le jeton de configuration Anthropic reste disponible comme chemin de jeton d’onboarding pris en charge, mais OpenClaw privilégie désormais la réutilisation de Claude CLI lorsqu’elle est disponible. En production, préférez une clé d’API Anthropic.

## Ajouter un autre agent

Utilisez `openclaw agents add <name>` pour créer un agent distinct avec son propre espace de travail, ses sessions et ses profils d’authentification. L’exécution sans `--workspace` lance l’assistant.

bashCopy code
[code]
    openclaw agents add work \  --workspace ~/.openclaw/workspace-work \  --model openai/gpt-5.5 \  --bind whatsapp:biz \  --non-interactive \  --json
[/code]

Ce que cela définit :

  * `agents.list[].name`
  * `agents.list[].workspace`
  * `agents.list[].agentDir`


Remarques :

  * Les espaces de travail par défaut suivent `~/.openclaw/workspace-<agentId>`.
  * Ajoutez `bindings` pour router les messages entrants (l’assistant peut le faire).
  * Indicateurs non interactifs : `--model`, `--agent-dir`, `--bind`, `--non-interactive`.


## Documentation associée

  * Hub d’onboarding : [Onboarding (CLI)](</fr/start/wizard>)
  * Référence complète : [Référence de configuration CLI](</fr/start/wizard-cli-reference>)
  * Référence de commande : [`openclaw onboard`](</fr/cli/onboard>)


Was this useful?YesNo