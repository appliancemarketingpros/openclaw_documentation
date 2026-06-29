---
title: NovitaAI
source_url: https://docs.openclaw.ai/fr/providers/novita
scraped_at: 2026-06-29
---

ModelsProviders

NovitaAI est un fournisseur d’infrastructure d’IA hébergée avec une API de modèles compatible avec OpenAI. Dans OpenClaw, c’est un fournisseur de modèles intégré ; l’id du fournisseur est donc `novita`, les identifiants passent par le flux normal d’authentification des modèles, et les références de modèles ressemblent à `novita/deepseek/deepseek-v3-0324`.

Utilisez Novita lorsque vous voulez un accès hébergé à des routes de modèles à poids ouverts et de modèles tiers sans exécuter votre propre serveur d’inférence. Le catalogue intégré se concentre sur des modèles de chat pratiques pour les tours d’agent, notamment les routes DeepSeek, Moonshot, MiniMax, GLM et Qwen exposées par Novita.

Ce fournisseur utilise le point de terminaison compatible OpenAI de Novita. OpenClaw gère l’enregistrement du fournisseur, l’authentification, les alias, la normalisation des références de modèles et la sélection de l’URL de base ; Novita contrôle la disponibilité des modèles en direct, les autorisations de compte, la tarification et les limites de débit.

## Configuration

Créez une clé API sur [novita.ai/settings/key-management](<https://novita.ai/settings/key-management>), puis exécutez :

bashCopy code
[code]
    openclaw onboard --auth-choice novita-api-key
[/code]

Ou définissez :

bashCopy code
[code]
    export NOVITA_API_KEY="<your-novita-api-key>" # pragma: allowlist secret
[/code]

## Valeurs par défaut

  * Fournisseur : `novita`
  * Alias : `novita-ai`, `novitaai`
  * URL de base : `https://api.novita.ai/openai/v1`
  * Variable d’environnement : `NOVITA_API_KEY`
  * Modèle par défaut : `novita/deepseek/deepseek-v3-0324`


## Quand choisir Novita

  * Vous voulez un accès hébergé à des modèles à poids ouverts avec une API compatible avec OpenAI.
  * Vous voulez des routes des familles DeepSeek, Kimi, MiniMax, GLM ou Qwen via un seul compte fournisseur.
  * Vous voulez une autre voie de secours hébergée en plus d’OpenRouter, GMI, DeepInfra ou des API directes des fournisseurs.
  * Vous préférez l’hébergement de modèles côté fournisseur plutôt que de maintenir une infrastructure vLLM, SGLang, LM Studio ou Ollama.


Choisissez un fournisseur direct lorsque vous avez besoin de paramètres de requête natifs du fournisseur ou de contrats d’assistance. Choisissez un fournisseur local lorsque le modèle doit s’exécuter sur votre propre matériel ou derrière votre propre limite réseau.

## Modèles

Le catalogue intégré amorce des identifiants de routes NovitaAI couramment disponibles, notamment :

  * `novita/moonshotai/kimi-k2.5`
  * `novita/minimax/minimax-m2.7`
  * `novita/zai-org/glm-5`
  * `novita/deepseek/deepseek-v3-0324`
  * `novita/deepseek/deepseek-r1-0528`
  * `novita/qwen/qwen3-235b-a22b-fp8`


Le catalogue est un point de départ pour la sélection de modèles OpenClaw. Votre compte, votre région ou le catalogue actuel de Novita peuvent ajouter, supprimer ou restreindre des routes. Vérifiez le fournisseur depuis la CLI avant de définir une valeur par défaut durable :

bashCopy code
[code]
    openclaw models list --provider novita
[/code]

## Dépannage

  * `401` ou `403` : vérifiez la clé dans la page de gestion des clés de Novita et réexécutez `openclaw onboard --auth-choice novita-api-key` si le profil stocké est obsolète.
  * Erreurs de modèle inconnu : utilisez le `novita/<route-id>` exact renvoyé par `openclaw models list --provider novita`.
  * Routes lentes ou en échec : essayez une autre route de modèle Novita ou définissez Novita comme fournisseur de secours pour les charges de travail qui peuvent tolérer une variance propre au fournisseur.


## Associé

  * [Fournisseurs de modèles](</fr/concepts/model-providers>)
  * [Tous les fournisseurs](</fr/providers>)


Was this useful?YesNo

Open issue