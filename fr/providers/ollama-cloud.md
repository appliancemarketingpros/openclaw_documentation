---
title: Ollama Cloud
source_url: https://docs.openclaw.ai/fr/providers/ollama-cloud
scraped_at: 2026-06-29
---

ModelsProviders

Ollama Cloud est l’API de modèles hébergée d’Ollama. Elle permet à OpenClaw d’appeler directement des modèles hébergés par Ollama, sans installer de serveur Ollama local ni connecter une application Ollama locale en mode cloud. Utilisez l’ID de fournisseur `ollama-cloud` et des références de modèle comme `ollama-cloud/kimi-k2.6`.

Cette page concerne le routage direct exclusivement cloud. Le fournisseur utilise le style natif `/api/chat` d’Ollama, et non la route compatible OpenAI `/v1`. OpenClaw l’enregistre comme un ID de fournisseur distinct afin que les identifiants exclusivement cloud, la découverte du catalogue en direct et la sélection des modèles ne soient pas mélangés avec un hôte `ollama` local.

Utilisez cette page lorsque vous voulez un routage exclusivement cloud. Pour Ollama local, le routage hybride cloud-plus-local, les embeddings et les détails d’hôte personnalisé, consultez [Ollama](</fr/providers/ollama>).

## Configuration

Créez une clé d’API Ollama Cloud sur [ollama.com/settings/keys](<https://ollama.com/settings/keys>), puis exécutez :

bashCopy code
[code]
    openclaw onboard --auth-choice ollama-cloud
[/code]

Ou définissez :

bashCopy code
[code]
    export OLLAMA_API_KEY="<your-ollama-cloud-api-key>" # pragma: allowlist secret
[/code]

## Valeurs par défaut

  * Fournisseur : `ollama-cloud`
  * URL de base : `https://ollama.com`
  * Variable d’environnement : `OLLAMA_API_KEY`
  * Style d’API : Ollama natif `/api/chat`
  * Modèle d’exemple : `ollama-cloud/kimi-k2.6`


## Quand choisir Ollama Cloud

  * Vous voulez des modèles Ollama hébergés sans exécuter `ollama serve` localement.
  * Vous voulez la même forme d’API de chat native Ollama qu’OpenClaw utilise pour Ollama local, mais pointée vers `https://ollama.com`.
  * Vous voulez un chemin cloud simple pour les modèles qui sont déjà dans le catalogue hébergé d’Ollama.
  * Vous n’avez pas besoin de téléchargements de modèles locaux, de contrôle GPU local ni d’inférence uniquement LAN.


Utilisez plutôt [Ollama](</fr/providers/ollama>) lorsque vous voulez un routage exclusivement local ou cloud-plus-local via un hôte Ollama connecté. Utilisez plutôt un fournisseur compatible OpenAI lorsque vous avez besoin de la sémantique `/v1/chat/completions` ou de fonctionnalités propres au fournisseur de style OpenAI.

## Modèles

OpenClaw découvre les modèles Ollama Cloud à partir du catalogue hébergé en direct. Les ID hébergés couramment disponibles incluent :

  * `ollama-cloud/gpt-oss:20b`
  * `ollama-cloud/kimi-k2.6`
  * `ollama-cloud/deepseek-v4-flash`
  * `ollama-cloud/minimax-m2.7`
  * `ollama-cloud/glm-5`


Utilisez un ID de modèle provenant de votre catalogue hébergé actuel :

bashCopy code
[code]
    openclaw models list --provider ollama-cloudopenclaw models set ollama-cloud/kimi-k2.6
[/code]

Les ID de modèle sont des ID de catalogue cloud, pas des noms de téléchargement locaux. Si un nom de modèle fonctionne dans un hôte Ollama local mais est absent du catalogue hébergé, utilisez plutôt le fournisseur `ollama` avec cet hôte local.

## Test en direct

Pour les tests rapides avec clé d’API Ollama Cloud, pointez le test en direct Ollama vers le point de terminaison hébergé et choisissez un modèle dans votre catalogue actuel :

bashCopy code
[code]
    export OLLAMA_API_KEY="<your-ollama-cloud-api-key>" # pragma: allowlist secret OPENCLAW_LIVE_TEST=1 \OPENCLAW_LIVE_OLLAMA=1 \OPENCLAW_LIVE_OLLAMA_BASE_URL=https://ollama.com \OPENCLAW_LIVE_OLLAMA_MODEL=kimi-k2.6 \OPENCLAW_LIVE_OLLAMA_WEB_SEARCH=1 \pnpm test:live -- extensions/ollama/ollama.live.test.ts
[/code]

Le test rapide cloud exécute du texte, le flux natif et la recherche web. Il ignore les embeddings par défaut pour `https://ollama.com`, car les clés d’API Ollama Cloud peuvent ne pas autoriser `/api/embed`.

## Dépannage

  * Erreurs `Set OLLAMA_API_KEY` : fournissez une vraie clé d’API cloud. Le marqueur local `ollama-local` est réservé aux hôtes Ollama locaux ou privés.
  * Erreurs de modèle inconnu : exécutez `openclaw models list --provider ollama-cloud` et copiez exactement l’ID du modèle hébergé.
  * Problèmes d’appel d’outil ou de JSON brut sur des hôtes Ollama personnalisés : vérifiez si vous utilisez accidentellement une URL compatible OpenAI `/v1`. Les routes Ollama doivent utiliser l’URL de base native sans suffixe `/v1`.


## Connexe

  * [Ollama](</fr/providers/ollama>)
  * [Fournisseurs de modèles](</fr/concepts/model-providers>)
  * [Tous les fournisseurs](</fr/providers>)


Was this useful?YesNo

Open issue