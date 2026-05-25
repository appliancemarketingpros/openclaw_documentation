---
title: Venice AI
source_url: https://docs.openclaw.ai/fr/providers/venice
scraped_at: 2026-05-25
---

Venice AI fournit une **inférence IA axée sur la confidentialité** , avec prise en charge de modèles non censurés et accès aux principaux modèles propriétaires via leur proxy anonymisé. Toute inférence est privée par défaut — pas d'entraînement sur vos données, pas de journalisation.

## Pourquoi Venice dans OpenClaw

  * **Inférence privée** pour les modèles open source (pas de journalisation).
  * **Modèles non censurés** quand vous en avez besoin.
  * **Accès anonymisé** aux modèles propriétaires (Opus/GPT/Gemini) lorsque la qualité compte.
  * Points de terminaison `/v1` compatibles avec OpenAI.


## Modes de confidentialité

Venice propose deux niveaux de confidentialité — il est essentiel de les comprendre pour choisir votre modèle :

Mode | Description | Modèles  
---|---|---  
**Privé** | Entièrement privé. Les prompts/réponses ne sont **jamais stockés ni journalisés**. Éphémère. | Llama, Qwen, DeepSeek, Kimi, MiniMax, Venice Uncensored, etc.  
**Anonymisé** | Relayé via Venice avec les métadonnées supprimées. Le fournisseur sous-jacent (OpenAI, Anthropic, Google, xAI) voit des requêtes anonymisées. | Claude, GPT, Gemini, Grok  
  
## Fonctionnalités

  * **Axé sur la confidentialité** : choisissez entre les modes "privé" (entièrement privé) et "anonymisé" (relayé)
  * **Modèles non censurés** : accès à des modèles sans restrictions de contenu
  * **Accès aux grands modèles** : utilisez Claude, GPT, Gemini et Grok via le proxy anonymisé de Venice
  * **API compatible avec OpenAI** : points de terminaison `/v1` standard pour une intégration facile
  * **Streaming** : pris en charge sur tous les modèles
  * **Appel de fonctions** : pris en charge sur certains modèles (vérifiez les capacités du modèle)
  * **Vision** : prise en charge sur les modèles dotés de capacités de vision
  * **Aucune limite de débit stricte** : une limitation d'utilisation équitable peut s'appliquer en cas d'usage extrême


## Premiers pas

* ### Obtenir votre clé API

  1. Inscrivez-vous sur [venice.ai](<https://venice.ai>)
  2. Accédez à **Settings > API Keys > Create new key**
  3. Copiez votre clé API (format : `vapi_xxxxxxxxxxxx`)


* ### Configurer OpenClaw

Choisissez votre méthode de configuration préférée :

### Interactif (recommandé)

bashCopy code
[code]
    openclaw onboard --auth-choice venice-api-key
[/code]

Cela va :

  1. Demander votre clé API (ou utiliser `VENICE_API_KEY` existante)
  2. Afficher tous les modèles Venice disponibles
  3. Vous laisser choisir votre modèle par défaut
  4. Configurer le fournisseur automatiquement


### Variable d'environnement

bashCopy code
[code]
    export VENICE_API_KEY="vapi_xxxxxxxxxxxx"
[/code]

### Non interactif

bashCopy code
[code]
    openclaw onboard --non-interactive \  --auth-choice venice-api-key \  --venice-api-key "vapi_xxxxxxxxxxxx"
[/code]

* ### Vérifier la configuration

bashCopy code
[code]
    openclaw agent --model venice/kimi-k2-5 --message "Hello, are you working?"
[/code]

## Sélection du modèle

Après la configuration, OpenClaw affiche tous les modèles Venice disponibles. Choisissez selon vos besoins :

  * **Modèle par défaut** : `venice/kimi-k2-5` pour un raisonnement privé solide avec vision.
  * **Option à capacités élevées** : `venice/claude-opus-4-6` pour le chemin Venice anonymisé le plus performant.
  * **Confidentialité** : choisissez des modèles "privé" pour une inférence entièrement privée.
  * **Capacité** : choisissez des modèles "anonymisé" pour accéder à Claude, GPT et Gemini via le proxy de Venice.


Changez votre modèle par défaut à tout moment :

bashCopy code
[code]
    openclaw models set venice/kimi-k2-5openclaw models set venice/claude-opus-4-6
[/code]

Lister tous les modèles disponibles :

bashCopy code
[code]
    openclaw models list --all --provider venice
[/code]

Vous pouvez aussi exécuter `openclaw configure`, sélectionner **Model/auth** , puis choisir **Venice AI**.

## Comportement de rejeu DeepSeek V4

Si Venice expose des modèles DeepSeek V4 tels que `venice/deepseek-v4-pro` ou `venice/deepseek-v4-flash`, OpenClaw renseigne l'espace réservé de rejeu DeepSeek V4 requis `reasoning_content` sur les messages de l'assistant lorsque le proxy l'omet. Venice rejette le contrôle `thinking` natif de premier niveau de DeepSeek, donc OpenClaw conserve ce correctif de rejeu propre au fournisseur séparé des contrôles de pensée du fournisseur DeepSeek natif.

## Catalogue intégré (41 au total)

Modèles privés (26) — entièrement privés, aucune journalisation ID de modèle | Nom | Contexte | Fonctionnalités  
---|---|---|---  
`kimi-k2-5` | Kimi K2.5 | 256k | Par défaut, raisonnement, vision  
`kimi-k2-thinking` | Kimi K2 Thinking | 256k | Raisonnement  
`llama-3.3-70b` | Llama 3.3 70B | 128k | Général  
`llama-3.2-3b` | Llama 3.2 3B | 128k | Général  
`hermes-3-llama-3.1-405b` | Hermes 3 Llama 3.1 405B | 128k | Général, outils désactivés  
`qwen3-235b-a22b-thinking-2507` | Qwen3 235B Thinking | 128k | Raisonnement  
`qwen3-235b-a22b-instruct-2507` | Qwen3 235B Instruct | 128k | Général  
`qwen3-coder-480b-a35b-instruct` | Qwen3 Coder 480B | 256k | Codage  
`qwen3-coder-480b-a35b-instruct-turbo` | Qwen3 Coder 480B Turbo | 256k | Codage  
`qwen3-5-35b-a3b` | Qwen3.5 35B A3B | 256k | Raisonnement, vision  
`qwen3-next-80b` | Qwen3 Next 80B | 256k | Général  
`qwen3-vl-235b-a22b` | Qwen3 VL 235B (Vision) | 256k | Vision  
`qwen3-4b` | Venice Small (Qwen3 4B) | 32k | Rapide, raisonnement  
`deepseek-v3.2` | DeepSeek V3.2 | 160k | Raisonnement, outils désactivés  
`venice-uncensored` | Venice Uncensored (Dolphin-Mistral) | 32k | Non censuré, outils désactivés  
`mistral-31-24b` | Venice Medium (Mistral) | 128k | Vision  
`google-gemma-3-27b-it` | Google Gemma 3 27B Instruct | 198k | Vision  
`openai-gpt-oss-120b` | OpenAI GPT OSS 120B | 128k | Général  
`nvidia-nemotron-3-nano-30b-a3b` | NVIDIA Nemotron 3 Nano 30B | 128k | Général  
`olafangensan-glm-4.7-flash-heretic` | GLM 4.7 Flash Heretic | 128k | Raisonnement  
`zai-org-glm-4.6` | GLM 4.6 | 198k | Général  
`zai-org-glm-4.7` | GLM 4.7 | 198k | Raisonnement  
`zai-org-glm-4.7-flash` | GLM 4.7 Flash | 128k | Raisonnement  
`zai-org-glm-5` | GLM 5 | 198k | Raisonnement  
`minimax-m21` | MiniMax M2.1 | 198k | Raisonnement  
`minimax-m25` | MiniMax M2.5 | 198k | Raisonnement  
Modèles anonymisés (15) — via le proxy Venice ID de modèle | Nom | Contexte | Fonctionnalités  
---|---|---|---  
`claude-opus-4-6` | Claude Opus 4.6 (via Venice) | 1M | Raisonnement, vision  
`claude-opus-4-5` | Claude Opus 4.5 (via Venice) | 198k | Raisonnement, vision  
`claude-sonnet-4-6` | Claude Sonnet 4.6 (via Venice) | 1M | Raisonnement, vision  
`claude-sonnet-4-5` | Claude Sonnet 4.5 (via Venice) | 198k | Raisonnement, vision  
`openai-gpt-54` | GPT-5.4 (via Venice) | 1M | Raisonnement, vision  
`openai-gpt-53-codex` | GPT-5.3 Codex (via Venice) | 400k | Raisonnement, vision, codage  
`openai-gpt-52` | GPT-5.2 (via Venice) | 256k | Raisonnement  
`openai-gpt-52-codex` | GPT-5.2 Codex (via Venice) | 256k | Raisonnement, vision, codage  
`openai-gpt-4o-2024-11-20` | GPT-4o (via Venice) | 128k | Vision  
`openai-gpt-4o-mini-2024-07-18` | GPT-4o Mini (via Venice) | 128k | Vision  
`gemini-3-1-pro-preview` | Gemini 3.1 Pro (via Venice) | 1M | Raisonnement, vision  
`gemini-3-pro-preview` | Gemini 3 Pro (via Venice) | 198k | Raisonnement, vision  
`gemini-3-flash-preview` | Gemini 3 Flash (via Venice) | 256k | Raisonnement, vision  
`grok-41-fast` | Grok 4.1 Fast (via Venice) | 1M | Raisonnement, vision  
`grok-code-fast-1` | Grok Code Fast 1 (via Venice) | 256k | Raisonnement, codage  
  
## Découverte des modèles

OpenClaw fournit un catalogue d'amorçage Venice adossé à un manifeste pour la liste des modèles en lecture seule. L'actualisation à l'exécution peut toujours découvrir les modèles depuis l'API Venice et revient au catalogue du manifeste si l'API est injoignable.

Le point de terminaison `/models` est public (aucune authentification nécessaire pour la liste), mais l'inférence nécessite une clé API valide.

## Streaming et prise en charge des outils

Fonctionnalité | Prise en charge  
---|---  
**Streaming** | Tous les modèles  
**Appel de fonctions** | La plupart des modèles (vérifiez `supportsFunctionCalling` dans l’API)  
**Vision/images** | Modèles marqués avec la fonctionnalité « Vision »  
**Mode JSON** | Pris en charge via `response_format`  
  
## Tarification

Venice utilise un système basé sur des crédits. Consultez [venice.ai/pricing](<https://venice.ai/pricing>) pour les tarifs actuels :

  * **Modèles privés** : coût généralement inférieur
  * **Modèles anonymisés** : similaire à la tarification directe de l’API + petits frais Venice


### Venice (anonymisé) vs API directe

Aspect | Venice (anonymisé) | API directe  
---|---|---  
**Confidentialité** | Métadonnées supprimées, anonymisées | Votre compte est lié  
**Latence** | +10-50 ms (proxy) | Directe  
**Fonctionnalités** | La plupart des fonctionnalités prises en charge | Fonctionnalités complètes  
**Facturation** | Crédits Venice | Facturation du fournisseur  
  
## Exemples d’utilisation

bashCopy code
[code]
    # Use the default private modelopenclaw agent --model venice/kimi-k2-5 --message "Quick health check" # Use Claude Opus via Venice (anonymized)openclaw agent --model venice/claude-opus-4-6 --message "Summarize this task" # Use uncensored modelopenclaw agent --model venice/venice-uncensored --message "Draft options" # Use vision model with imageopenclaw agent --model venice/qwen3-vl-235b-a22b --message "Review attached image" # Use coding modelopenclaw agent --model venice/qwen3-coder-480b-a35b-instruct --message "Refactor this function"
[/code]

## Dépannage

API key not recognized bashCopy code
[code]
    echo $VENICE_API_KEYopenclaw models list | grep venice
[/code]

Assurez-vous que la clé commence par `vapi_`.

Model not available

Le catalogue de modèles Venice se met à jour dynamiquement. Exécutez `openclaw models list` pour voir les modèles actuellement disponibles. Certains modèles peuvent être temporairement hors ligne.

Connection issues

L’API Venice se trouve à `https://api.venice.ai/api/v1`. Assurez-vous que votre réseau autorise les connexions HTTPS.

## Configuration avancée

Config file example json5Copy code
[code]
    {  env: { VENICE_API_KEY: "vapi_..." },  agents: { defaults: { model: { primary: "venice/kimi-k2-5" } } },  models: {    mode: "merge",    providers: {      venice: {        baseUrl: "https://api.venice.ai/api/v1",        apiKey: "${VENICE_API_KEY}",        api: "openai-completions",        models: [          {            id: "kimi-k2-5",            name: "Kimi K2.5",            reasoning: true,            input: ["text", "image"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 256000,            maxTokens: 65536,          },        ],      },    },  },}
[/code]

## Associé

[**Model selection** Choix des fournisseurs, des références de modèles et du comportement de basculement. ](</fr/concepts/model-providers>) [**Venice AI** Page d’accueil de Venice AI et création de compte. ](<https://venice.ai>) [**API documentation** Référence de l’API Venice et documentation pour développeurs. ](<https://docs.venice.ai>) [**Pricing** Tarifs et forfaits actuels des crédits Venice. ](<https://venice.ai/pricing>)

Was this useful?YesNo