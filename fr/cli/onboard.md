---
title: Intégration
source_url: https://docs.openclaw.ai/fr/cli/onboard
scraped_at: 2026-05-25
---

# `openclaw onboard`

Intégration guidée complète pour la configuration d’un Gateway local ou distant. Utilisez cette commande lorsque vous voulez qu’OpenClaw vous guide à travers l’authentification du modèle, l’espace de travail, le gateway, les canaux, les skills et l’état de santé dans un seul flux.

## Guides associés

[**CLI onboarding hub** Parcours du flux CLI interactif. ](</fr/start/wizard>) [**Onboarding overview** Comment l’intégration OpenClaw s’articule. ](</fr/start/onboarding-overview>) [**CLI setup reference** Sorties, éléments internes et comportement étape par étape. ](</fr/start/wizard-cli-reference>) [**CLI automation** Indicateurs non interactifs et configurations scriptées. ](</fr/start/wizard-cli-automation>) [**macOS app onboarding** Flux d’intégration pour l’app de barre de menus macOS. ](</fr/start/onboarding>)

## Exemples

bashCopy code
[code]
    openclaw onboardopenclaw onboard --modernopenclaw onboard --flow quickstartopenclaw onboard --flow manualopenclaw onboard --flow importopenclaw onboard --import-from hermes --import-source ~/.hermesopenclaw onboard --skip-bootstrapopenclaw onboard --mode remote --remote-url wss://gateway-host:18789
[/code]

`--flow import` utilise des fournisseurs de migration possédés par les plugins, tels que Hermes. Il ne s’exécute que sur une nouvelle configuration OpenClaw ; si une configuration, des identifiants, des sessions ou des fichiers de mémoire/identité d’espace de travail existent déjà, réinitialisez ou choisissez une nouvelle configuration avant l’importation.

`--modern` lance l’aperçu d’intégration conversationnelle Crestodian. Sans `--modern`, `openclaw onboard` conserve le flux d’intégration classique.

Pour les cibles `ws://` en texte brut sur réseau privé (réseaux de confiance uniquement), définissez `OPENCLAW_ALLOW_INSECURE_PRIVATE_WS=1` dans l’environnement du processus d’intégration. Il n’existe pas d’équivalent `openclaw.json` pour ce contournement d’urgence du transport côté client.

Fournisseur personnalisé non interactif :

bashCopy code
[code]
    openclaw onboard --non-interactive \  --auth-choice custom-api-key \  --custom-base-url "https://llm.example.com/v1" \  --custom-model-id "foo-large" \  --custom-api-key "$CUSTOM_API_KEY" \  --secret-input-mode plaintext \  --custom-compatibility openai \  --custom-image-input
[/code]

`--custom-api-key` est facultatif en mode non interactif. S’il est omis, l’intégration vérifie `CUSTOM_API_KEY`. OpenClaw marque automatiquement les ID de modèles de vision courants comme compatibles avec les images. Passez `--custom-image-input` pour les ID de vision personnalisés inconnus, ou `--custom-text-input` pour forcer des métadonnées texte uniquement.

LM Studio prend aussi en charge un indicateur de clé propre au fournisseur en mode non interactif :

bashCopy code
[code]
    openclaw onboard --non-interactive \  --auth-choice lmstudio \  --custom-base-url "http://localhost:1234/v1" \  --custom-model-id "qwen/qwen3.5-9b" \  --lmstudio-api-key "$LM_API_TOKEN" \  --accept-risk
[/code]

Ollama non interactif :

bashCopy code
[code]
    openclaw onboard --non-interactive \  --auth-choice ollama \  --custom-base-url "http://ollama-host:11434" \  --custom-model-id "qwen3.5:27b" \  --accept-risk
[/code]

`--custom-base-url` vaut par défaut `http://127.0.0.1:11434`. `--custom-model-id` est facultatif ; s’il est omis, l’intégration utilise les valeurs par défaut suggérées par Ollama. Les ID de modèles cloud tels que `kimi-k2.5:cloud` fonctionnent également ici.

Stocker les clés fournisseur sous forme de références plutôt qu’en texte brut :

bashCopy code
[code]
    openclaw onboard --non-interactive \  --auth-choice openai-api-key \  --secret-input-mode ref \  --accept-risk
[/code]

Avec `--secret-input-mode ref`, l’intégration écrit des références adossées à l’environnement au lieu de valeurs de clés en texte brut. Pour les fournisseurs adossés à un profil d’authentification, cela écrit des entrées `keyRef` ; pour les fournisseurs personnalisés, cela écrit `models.providers.<id>.apiKey` comme référence d’environnement (par exemple `{ source: "env", provider: "default", id: "CUSTOM_API_KEY" }`).

Contrat du mode non interactif `ref` :

  * Définissez la variable d’environnement du fournisseur dans l’environnement du processus d’intégration (par exemple `OPENAI_API_KEY`).
  * Ne passez pas d’indicateurs de clé en ligne (par exemple `--openai-api-key`) sauf si cette variable d’environnement est également définie.
  * Si un indicateur de clé en ligne est passé sans la variable d’environnement requise, l’intégration échoue immédiatement avec des instructions.


Options de jeton Gateway en mode non interactif :

  * `--gateway-auth token --gateway-token <token>` stocke un jeton en texte brut.
  * `--gateway-auth token --gateway-token-ref-env <name>` stocke `gateway.auth.token` comme `SecretRef` d’environnement.
  * `--gateway-token` et `--gateway-token-ref-env` s’excluent mutuellement.
  * `--gateway-token-ref-env` nécessite une variable d’environnement non vide dans l’environnement du processus d’intégration.
  * Avec `--install-daemon`, lorsque l’authentification par jeton exige un jeton, les jetons de gateway gérés par `SecretRef` sont validés mais ne sont pas persistés sous forme de texte brut résolu dans les métadonnées d’environnement du service superviseur.
  * Avec `--install-daemon`, si le mode jeton exige un jeton et que la `SecretRef` de jeton configurée n’est pas résolue, l’intégration échoue de manière fermée avec des instructions de remédiation.
  * Avec `--install-daemon`, si `gateway.auth.token` et `gateway.auth.password` sont tous deux configurés et que `gateway.auth.mode` n’est pas défini, l’intégration bloque l’installation jusqu’à ce que le mode soit défini explicitement.
  * L’intégration locale écrit `gateway.mode="local"` dans la configuration. Si un fichier de configuration ultérieur ne contient pas `gateway.mode`, traitez cela comme une configuration endommagée ou une modification manuelle incomplète, et non comme un raccourci de mode local valide.
  * L’intégration locale installe les plugins téléchargeables sélectionnés lorsque le chemin de configuration choisi les exige.
  * L’intégration distante écrit uniquement les informations de connexion du Gateway distant et n’installe pas de packages de plugins locaux.
  * `--allow-unconfigured` est une trappe d’échappement distincte pour l’exécution du gateway. Cela ne signifie pas que l’intégration peut omettre `gateway.mode`.


Exemple :

bashCopy code
[code]
    export OPENCLAW_GATEWAY_TOKEN="your-token"openclaw onboard --non-interactive \  --mode local \  --auth-choice skip \  --gateway-auth token \  --gateway-token-ref-env OPENCLAW_GATEWAY_TOKEN \  --accept-risk
[/code]

État de santé du gateway local non interactif :

  * À moins que vous ne passiez `--skip-health`, l’intégration attend qu’un gateway local joignable soit disponible avant de se terminer avec succès.
  * `--install-daemon` lance d’abord le chemin d’installation du gateway géré. Sans lui, vous devez déjà avoir un gateway local en cours d’exécution, par exemple `openclaw gateway run`.
  * Si vous voulez seulement écrire la configuration, l’espace de travail et le bootstrap dans l’automatisation, utilisez `--skip-health`.
  * Si vous gérez vous-même les fichiers d’espace de travail, passez `--skip-bootstrap` pour définir `agents.defaults.skipBootstrap: true` et ignorer la création de `AGENTS.md`, `SOUL.md`, `TOOLS.md`, `IDENTITY.md`, `USER.md`, `HEARTBEAT.md` et `BOOTSTRAP.md`.
  * Sur Windows natif, `--install-daemon` essaie d’abord les tâches planifiées et se rabat sur un élément de connexion dans le dossier de démarrage par utilisateur si la création de tâche est refusée.


Comportement de l’intégration interactive avec le mode référence :

  * Choisissez **Use secret reference** lorsque vous y êtes invité.
  * Choisissez ensuite l’une des options suivantes : 
    * Variable d’environnement
    * Fournisseur de secrets configuré (`file` ou `exec`)
  * L’intégration effectue une validation préliminaire rapide avant d’enregistrer la référence. 
    * Si la validation échoue, l’intégration affiche l’erreur et vous permet de réessayer.


### Choix d’endpoints [Z.AI](<http://Z.AI>) non interactifs

bashCopy code
[code]
    # Promptless endpoint selectionopenclaw onboard --non-interactive \  --auth-choice zai-coding-global \  --zai-api-key "$ZAI_API_KEY" # Other Z.AI endpoint choices:# --auth-choice zai-coding-cn# --auth-choice zai-global# --auth-choice zai-cn
[/code]

Exemple Mistral non interactif :

bashCopy code
[code]
    openclaw onboard --non-interactive \  --auth-choice mistral-api-key \  --mistral-api-key "$MISTRAL_API_KEY"
[/code]

## Notes sur les flux

Flow types

  * `quickstart` : invites minimales, génère automatiquement un jeton de gateway.
  * `manual` : invites complètes pour le port, l’adresse d’écoute et l’authentification (alias de `advanced`).
  * `import` : exécute un fournisseur de migration détecté, prévisualise le plan, puis l’applique après confirmation.

Provider prefiltering

Lorsqu’un choix d’authentification implique un fournisseur préféré, l’intégration préfiltre les sélecteurs de modèle par défaut et de liste d’autorisation sur ce fournisseur. Pour Volcengine et BytePlus, cela correspond également aux variantes de plan de codage (`volcengine-plan/*`, `byteplus-plan/*`).

Si le filtre du fournisseur préféré ne renvoie encore aucun modèle chargé, l’intégration revient au catalogue non filtré au lieu de laisser le sélecteur vide.

Web-search follow-ups

Certains fournisseurs de recherche web déclenchent des invites de suivi propres au fournisseur :

  * **Grok** peut proposer une configuration facultative de `x_search` avec le même `XAI_API_KEY` et un choix de modèle `x_search`.
  * **Kimi** peut demander la région de l’API Moonshot (`api.moonshot.ai` ou `api.moonshot.cn`) et le modèle de recherche web Kimi par défaut.

Other behaviors

  * Comportement de portée DM de l’intégration locale : [Référence de configuration CLI](</fr/start/wizard-cli-reference#outputs-and-internals>).
  * Premier chat le plus rapide : `openclaw dashboard` (interface de contrôle, aucune configuration de canal).
  * Fournisseur personnalisé : connectez tout endpoint compatible OpenAI ou Anthropic, y compris des fournisseurs hébergés non listés. Utilisez Unknown pour la détection automatique.
  * Si un état Hermes est détecté, l’intégration propose un flux de migration. Utilisez [Migrate](</fr/cli/migrate>) pour les plans d’essai, le mode d’écrasement, les rapports et les correspondances exactes.


## Commandes de suivi courantes

bashCopy code
[code]
    openclaw channels addopenclaw configureopenclaw agents add <name>
[/code]

Utilisez plutôt `openclaw setup` lorsque vous avez seulement besoin de la configuration et de l’espace de travail de base. Utilisez `openclaw configure` plus tard pour des changements ciblés et `openclaw channels add` pour une configuration limitée aux canaux.

Was this useful?YesNo