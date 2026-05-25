---
title: Mistral
source_url: https://docs.openclaw.ai/fr/providers/mistral
scraped_at: 2026-05-25
---

OpenClaw inclut un Plugin Mistral intégré qui enregistre quatre contrats : complétions de chat, compréhension des médias (transcription par lots Voxtral), STT en temps réel pour Appel vocal (Voxtral Realtime) et embeddings mémoire (`mistral-embed`).

Propriété | Valeur  
---|---  
ID fournisseur | `mistral`  
Plugin | intégré, `enabledByDefault: true`  
Var. d’env auth | `MISTRAL_API_KEY`  
Option onboarding | `--auth-choice mistral-api-key`  
Option CLI directe | `--mistral-api-key <key>`  
API | compatible OpenAI (`openai-completions`)  
URL de base | `https://api.mistral.ai/v1`  
Modèle par défaut | `mistral/mistral-large-latest`  
Modèle d’embedding | `mistral-embed`  
Lot Voxtral | `voxtral-mini-latest` (transcription audio)  
Temps réel Voxtral | `voxtral-mini-transcribe-realtime-2602`  
  
## Bien démarrer

* ### Obtenez votre clé API

Créez une clé API dans la [console Mistral](<https://console.mistral.ai/>).

* ### Exécutez l’onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice mistral-api-key
[/code]

Ou passez directement la clé :

bashCopy code
[code]
    openclaw onboard --mistral-api-key "$MISTRAL_API_KEY"
[/code]

* ### Définissez un modèle par défaut

json5Copy code
[code]
    {  env: { MISTRAL_API_KEY: "sk-..." },  agents: { defaults: { model: { primary: "mistral/mistral-large-latest" } } },}
[/code]

* ### Vérifiez que le modèle est disponible

bashCopy code
[code]
    openclaw models list --provider mistral
[/code]

## Catalogue LLM intégré

[Mistral Medium 3.5](<https://docs.mistral.ai/models/model-cards/mistral-medium-3-5-26-04>) est le modèle Medium mixte actuel dans le catalogue intégré : poids denses 128B, entrée texte et image, contexte 256K, appel de fonctions, sortie structurée, codage et raisonnement ajustable via l’API Chat Completions. Utilisez `mistral/mistral-medium-3-5` lorsque vous voulez le nouveau modèle unifié agentique/codage de Mistral au lieu du modèle par défaut `mistral/mistral-large-latest`.

OpenClaw fournit actuellement ce catalogue Mistral intégré :

Réf. du modèle | Entrée | Contexte | Sortie max | Notes  
---|---|---|---|---  
`mistral/mistral-large-latest` | texte, image | 262,144 | 16,384 | Modèle par défaut  
`mistral/mistral-medium-2508` | texte, image | 262,144 | 8,192 | Mistral Medium 3.1  
`mistral/mistral-medium-3-5` | texte, image | 262,144 | 8,192 | Mistral Medium 3.5 ; raisonnement ajustable  
`mistral/mistral-small-latest` | texte, image | 128,000 | 16,384 | Mistral Small 4 ; raisonnement ajustable via l’API `reasoning_effort`  
`mistral/pixtral-large-latest` | texte, image | 128,000 | 32,768 | Pixtral  
`mistral/codestral-latest` | texte | 256,000 | 4,096 | Codage  
`mistral/devstral-medium-latest` | texte | 262,144 | 32,768 | Devstral 2  
`mistral/magistral-small` | texte | 128,000 | 40,000 | Raisonnement activé  
  
Après l’onboarding, exécutez un smoke test de Medium 3.5 sans démarrer le Gateway :

bashCopy code
[code]
    openclaw infer model run --local \  --model mistral/mistral-medium-3-5 \  --prompt "Reply with exactly: mistral-ok" \  --json
[/code]

Pour parcourir la ligne du catalogue intégré avant de modifier la configuration :

bashCopy code
[code]
    openclaw models list --all --provider mistral --plain
[/code]

## Transcription audio (Voxtral)

Utilisez Voxtral pour la transcription audio par lots via le pipeline de compréhension des médias.

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "mistral", model: "voxtral-mini-latest" }],      },    },  },}
[/code]

## STT en streaming pour Appel vocal

Le Plugin `mistral` intégré enregistre Voxtral Realtime comme fournisseur STT en streaming pour Appel vocal.

Paramètre | Chemin de config | Par défaut  
---|---|---  
Clé API | `plugins.entries.voice-call.config.streaming.providers.mistral.apiKey` | Se rabat sur `MISTRAL_API_KEY`  
Modèle | `...mistral.model` | `voxtral-mini-transcribe-realtime-2602`  
Encodage | `...mistral.encoding` | `pcm_mulaw`  
Fréquence d’échantillonnage | `...mistral.sampleRate` | `8000`  
Délai cible | `...mistral.targetStreamingDelayMs` | `800`  
json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        config: {          streaming: {            enabled: true,            provider: "mistral",            providers: {              mistral: {                apiKey: "${MISTRAL_API_KEY}",                targetStreamingDelayMs: 800,              },            },          },        },      },    },  },}
[/code]

## Configuration avancée

Raisonnement ajustable

`mistral/mistral-small-latest` (Mistral Small 4) et `mistral/mistral-medium-3-5` prennent en charge le [raisonnement ajustable](<https://docs.mistral.ai/studio-api/conversations/reasoning/adjustable>) sur l’API Chat Completions via `reasoning_effort` (`none` minimise la réflexion supplémentaire dans la sortie ; `high` expose les traces complètes de réflexion avant la réponse finale). Mistral recommande `reasoning_effort="high"` pour les cas d’usage agentiques et de code avec Medium 3.5.

OpenClaw mappe le niveau **thinking** de la session vers l’API de Mistral :

Niveau thinking OpenClaw | `reasoning_effort` Mistral  
---|---  
**off** / **minimal** | `none`  
**low** / **medium** / **high** / **xhigh** / **adaptive** / **max** | `high`  
  
Exemple de configuration limitée au modèle pour le raisonnement Medium 3.5 :

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "mistral/mistral-medium-3-5" },      models: {        "mistral/mistral-medium-3-5": {          params: { thinking: "high" },        },      },    },  },}
[/code]

Embeddings mémoire

Mistral peut servir des embeddings mémoire via `/v1/embeddings` (modèle par défaut : `mistral-embed`).

json5Copy code
[code]
    {  memorySearch: { provider: "mistral" },}
[/code]

Authentification et URL de base

  * L’authentification Mistral utilise `MISTRAL_API_KEY` (en-tête Bearer).
  * L’URL de base du fournisseur est par défaut `https://api.mistral.ai/v1` et accepte la forme de requête chat-completions standard compatible OpenAI.
  * Le modèle par défaut de l’onboarding est `mistral/mistral-large-latest`.
  * Remplacez l’URL de base sous `models.providers.mistral.baseUrl` uniquement lorsque Mistral publie explicitement un endpoint régional dont vous avez besoin.


## Connexe

[**Sélection de modèle** Choisir les fournisseurs, les références de modèles et le comportement de bascule. ](</fr/concepts/model-providers>) [**Compréhension des médias** Configuration de la transcription audio et sélection du fournisseur. ](</fr/nodes/media-understanding>)

Was this useful?YesNo