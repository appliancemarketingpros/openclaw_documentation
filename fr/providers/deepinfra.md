---
title: DeepInfra
source_url: https://docs.openclaw.ai/fr/providers/deepinfra
scraped_at: 2026-05-25
---

DeepInfra fournit une **API unifiée** qui achemine les requêtes vers les modèles open source et frontier les plus populaires derrière un seul point de terminaison et une seule clé API. Elle est compatible avec OpenAI, donc la plupart des SDK OpenAI fonctionnent en changeant l’URL de base.

## Obtenir une clé API

  1. Accédez à <https://deepinfra.com/>
  2. Connectez-vous ou créez un compte
  3. Accédez à Dashboard / Keys et générez une nouvelle clé API ou utilisez celle créée automatiquement


## Configuration CLI

bashCopy code
[code]
    openclaw onboard --deepinfra-api-key <key>
[/code]

Ou définissez la variable d’environnement :

bashCopy code
[code]
    export DEEPINFRA_API_KEY="<your-deepinfra-api-key>" # pragma: allowlist secret
[/code]

## Extrait de configuration

json5Copy code
[code]
    {  env: { DEEPINFRA_API_KEY: "<your-deepinfra-api-key>" }, // pragma: allowlist secret  agents: {    defaults: {      model: { primary: "deepinfra/deepseek-ai/DeepSeek-V3.2" },    },  },}
[/code]

## Surfaces OpenClaw prises en charge

Le Plugin intégré enregistre toutes les surfaces DeepInfra qui correspondent aux contrats de fournisseur OpenClaw actuels :

Surface | Modèle par défaut | Configuration/outil OpenClaw  
---|---|---  
Chat / fournisseur de modèle | `deepseek-ai/DeepSeek-V3.2` | `agents.defaults.model`  
Génération/édition d’images | `black-forest-labs/FLUX-1-schnell` | `image_generate`, `agents.defaults.imageGenerationModel`  
Compréhension des médias | `moonshotai/Kimi-K2.5` pour les images | compréhension des images entrantes  
Speech-to-text | `openai/whisper-large-v3-turbo` | transcription audio entrante  
Text-to-speech | `hexgrad/Kokoro-82M` | `messages.tts.provider: "deepinfra"`  
Génération de vidéos | `Pixverse/Pixverse-T2V` | `video_generate`, `agents.defaults.videoGenerationModel`  
Embeddings de mémoire | `BAAI/bge-m3` | `agents.defaults.memorySearch.provider: "deepinfra"`  
  
DeepInfra expose également le reclassement, la classification, la détection d’objets et d’autres types de modèles natifs. OpenClaw ne dispose pas actuellement de contrats de fournisseur de premier niveau pour ces catégories ; ce Plugin ne les enregistre donc pas encore.

## Modèles disponibles

OpenClaw découvre dynamiquement les modèles DeepInfra disponibles au démarrage. Utilisez `/models deepinfra` pour afficher la liste complète des modèles disponibles.

Tout modèle disponible sur [DeepInfra.com](<https://deepinfra.com/>) peut être utilisé avec le préfixe `deepinfra/` :

CodeCopy code
[code]
    deepinfra/MiniMaxAI/MiniMax-M2.5deepinfra/deepseek-ai/DeepSeek-V3.2deepinfra/moonshotai/Kimi-K2.5deepinfra/zai-org/GLM-5.1...and many more
[/code]

## Notes

  * Les références de modèles sont `deepinfra/<provider>/<model>` (par exemple, `deepinfra/Qwen/Qwen3-Max`).
  * Modèle par défaut : `deepinfra/deepseek-ai/DeepSeek-V3.2`
  * URL de base : `https://api.deepinfra.com/v1/openai`
  * La génération vidéo native utilise `https://api.deepinfra.com/v1/inference/<model>`.


## Connexe

  * [Fournisseurs de modèles](</fr/concepts/model-providers>)
  * [Tous les fournisseurs](</fr/providers>)


Was this useful?YesNo