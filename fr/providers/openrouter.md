---
title: OpenRouter
source_url: https://docs.openclaw.ai/fr/providers/openrouter
scraped_at: 2026-05-25
---

OpenRouter fournit une **API unifiée** qui achemine les requêtes vers de nombreux modèles derrière un seul endpoint et une seule clé d’API. Elle est compatible avec OpenAI, donc la plupart des SDK OpenAI fonctionnent en changeant l’URL de base.

## Bien démarrer

* ### Obtenir votre clé d’API

Créez une clé d’API sur [openrouter.ai/keys](<https://openrouter.ai/keys>).

* ### Exécuter l’intégration initiale

bashCopy code
[code]
    openclaw onboard --auth-choice openrouter-api-key
[/code]

* ### (Facultatif) Passer à un modèle spécifique

L’intégration initiale utilise `openrouter/auto` par défaut. Choisissez un modèle concret plus tard :

bashCopy code
[code]
    openclaw models set openrouter/<provider>/<model>
[/code]

## Exemple de configuration

json5Copy code
[code]
    {  env: { OPENROUTER_API_KEY: "sk-or-..." },  agents: {    defaults: {      model: { primary: "openrouter/auto" },    },  },}
[/code]

## Références de modèles

Exemples de secours inclus :

Référence de modèle | Notes  
---|---  
`openrouter/auto` | Routage automatique d’OpenRouter  
`openrouter/moonshotai/kimi-k2.6` | Kimi K2.6 via MoonshotAI  
`openrouter/moonshotai/kimi-k2.5` | Kimi K2.5 via MoonshotAI  
  
## Génération d’images

OpenRouter peut aussi prendre en charge l’outil `image_generate`. Utilisez un modèle d’image OpenRouter sous `agents.defaults.imageGenerationModel` :

json5Copy code
[code]
    {  env: { OPENROUTER_API_KEY: "sk-or-..." },  agents: {    defaults: {      imageGenerationModel: {        primary: "openrouter/google/gemini-3.1-flash-image-preview",        timeoutMs: 180_000,      },    },  },}
[/code]

OpenClaw envoie les requêtes d’image à l’API d’images des complétions de chat d’OpenRouter avec `modalities: ["image", "text"]`. Les modèles d’image Gemini reçoivent les indications `aspectRatio` et `resolution` prises en charge via `image_config` d’OpenRouter. Utilisez `agents.defaults.imageGenerationModel.timeoutMs` pour les modèles d’image OpenRouter plus lents ; le paramètre `timeoutMs` par appel de l’outil `image_generate` reste prioritaire.

## Génération de vidéos

OpenRouter peut aussi prendre en charge l’outil `video_generate` via son API asynchrone `/videos`. Utilisez un modèle vidéo OpenRouter sous `agents.defaults.videoGenerationModel` :

json5Copy code
[code]
    {  env: { OPENROUTER_API_KEY: "sk-or-..." },  agents: {    defaults: {      videoGenerationModel: {        primary: "openrouter/google/veo-3.1-fast",      },    },  },}
[/code]

OpenClaw soumet à OpenRouter des tâches de texte vers vidéo et d’image vers vidéo, interroge le `polling_url` renvoyé, puis télécharge la vidéo terminée depuis les `unsigned_urls` d’OpenRouter ou l’endpoint documenté du contenu de la tâche. Les images de référence sont envoyées par défaut comme images de première/dernière image ; les images marquées avec `reference_image` sont envoyées comme références d’entrée OpenRouter. Le modèle par défaut inclus `google/veo-3.1-fast` annonce les durées actuellement prises en charge de 4/6/8 secondes, les résolutions `720P`/`1080P` et les formats d’image `16:9`/`9:16`. La vidéo vers vidéo n’est pas enregistrée pour OpenRouter, car l’API amont de génération vidéo accepte actuellement le texte et les références d’image.

## Texte vers parole

OpenRouter peut aussi être utilisé comme fournisseur TTS via son endpoint compatible OpenAI `/audio/speech`.

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "openrouter",      providers: {        openrouter: {          model: "hexgrad/kokoro-82m",          voice: "af_alloy",          responseFormat: "mp3",        },      },    },  },}
[/code]

Si `messages.tts.providers.openrouter.apiKey` est omis, TTS réutilise `models.providers.openrouter.apiKey`, puis `OPENROUTER_API_KEY`.

## Parole vers texte (audio entrant)

OpenRouter peut transcrire les pièces jointes vocales/audio entrantes via le chemin partagé `tools.media.audio` en utilisant son endpoint STT (`/audio/transcriptions`). Cela s’applique à tout Plugin de canal qui transmet les contenus vocaux/audio entrants au précontrôle de compréhension des médias.

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "openrouter", model: "openai/whisper-large-v3-turbo" }],      },    },  },}
[/code]

OpenClaw envoie les requêtes STT OpenRouter en JSON avec l’audio en base64 sous `input_audio` (contrat STT OpenRouter), et non sous forme d’envois de formulaire multipart OpenAI.

## Authentification et en-têtes

OpenRouter utilise en interne un jeton Bearer avec votre clé d’API.

Pour les requêtes OpenRouter réelles (`https://openrouter.ai/api/v1`), OpenClaw ajoute aussi les en-têtes documentés d’attribution d’application d’OpenRouter :

En-tête | Valeur  
---|---  
`HTTP-Referer` | `https://openclaw.ai`  
`X-OpenRouter-Title` | `OpenClaw`  
`X-OpenRouter-Categories` | `cli-agent,cloud-agent,programming-app,creative-writing,writing-assistant,general-chat,personal-agent`  
  
## Configuration avancée

Mise en cache des réponses

La mise en cache des réponses OpenRouter est facultative. Activez-la par modèle OpenRouter avec les paramètres de modèle :

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "openrouter/auto": {          params: {            responseCache: true,            responseCacheTtlSeconds: 300,          },        },      },    },  },}
[/code]

OpenClaw envoie `X-OpenRouter-Cache: true` et, lorsqu’il est configuré, `X-OpenRouter-Cache-TTL`. `responseCacheClear: true` force une actualisation pour la requête actuelle et stocke la réponse de remplacement. Les alias snake_case (`response_cache`, `response_cache_ttl_seconds` et `response_cache_clear`) sont également acceptés.

Cette mise en cache est distincte de la mise en cache des prompts du fournisseur et des marqueurs Anthropic `cache_control` d’OpenRouter. Elle n’est appliquée que sur les routes `openrouter.ai` vérifiées, pas sur les URL de base de proxy personnalisées.

Marqueurs de cache Anthropic

Sur les routes OpenRouter vérifiées, les références de modèles Anthropic conservent les marqueurs Anthropic `cache_control` propres à OpenRouter qu’OpenClaw utilise pour une meilleure réutilisation du cache de prompts sur les blocs de prompts système/développeur.

Préremplissage du raisonnement Anthropic

Sur les routes OpenRouter vérifiées, les références de modèles Anthropic avec le raisonnement activé suppriment les tours de préremplissage assistant finaux avant que la requête n’atteigne OpenRouter, conformément à l’exigence d’Anthropic selon laquelle les conversations de raisonnement se terminent par un tour utilisateur.

Injection de réflexion / raisonnement

Sur les routes non `auto` prises en charge, OpenClaw mappe le niveau de réflexion sélectionné vers les charges utiles de raisonnement du proxy OpenRouter. Les indications de modèles non prises en charge et `openrouter/auto` ignorent cette injection de raisonnement. Hunter Alpha ignore aussi le raisonnement proxy pour les références de modèles configurées obsolètes, car OpenRouter pourrait renvoyer le texte de réponse finale dans les champs de raisonnement pour cette route retirée.

Relecture du raisonnement DeepSeek V4

Sur les routes OpenRouter vérifiées, `openrouter/deepseek/deepseek-v4-flash` et `openrouter/deepseek/deepseek-v4-pro` complètent le `reasoning_content` manquant sur les tours assistant rejoués afin que les conversations de réflexion/outils conservent la forme de suivi requise par DeepSeek V4. OpenClaw envoie les valeurs `reasoning_effort` prises en charge par OpenRouter pour ces routes ; `xhigh` est le niveau annoncé le plus élevé, et les surcharges `max` obsolètes sont mappées vers `xhigh`.

Mise en forme des requêtes réservée à OpenAI

OpenRouter passe toujours par le chemin compatible OpenAI de style proxy, donc la mise en forme des requêtes native propre à OpenAI, comme `serviceTier`, Responses `store`, les charges utiles de compatibilité du raisonnement OpenAI et les indications de cache de prompts, n’est pas transmise.

Routes adossées à Gemini

Les références OpenRouter adossées à Gemini restent sur le chemin proxy-Gemini : OpenClaw y conserve le nettoyage des signatures de réflexion Gemini, mais n’active pas la validation de relecture Gemini native ni les réécritures d’amorçage.

Métadonnées de routage du fournisseur

Si vous transmettez le routage du fournisseur OpenRouter sous les paramètres de modèle, OpenClaw le transmet comme métadonnées de routage OpenRouter avant l’exécution des wrappers de flux partagés.

## Associé

[**Sélection de modèles** Choisir les fournisseurs, les références de modèles et le comportement de bascule. ](</fr/concepts/model-providers>) [**Référence de configuration** Référence complète de configuration pour les agents, modèles et fournisseurs. ](</fr/gateway/configuration-reference>)

Was this useful?YesNo