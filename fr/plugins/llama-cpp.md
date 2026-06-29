---
title: Fournisseur llama.cpp
source_url: https://docs.openclaw.ai/fr/plugins/llama-cpp
scraped_at: 2026-06-29
---

CapabilitiesBundled plugin guides

`llama-cpp` est le Plugin de fournisseur externe officiel pour les embeddings GGUF locaux. Il possède la dépendance d’exécution `node-llama-cpp` utilisée par `memorySearch.provider: "local"`.

Installez-le avant d’utiliser les embeddings de mémoire locaux :

bashCopy code
[code]
    openclaw plugins install @openclaw/llama-cpp-provider
[/code]

Le paquet npm principal `openclaw` n’inclut pas `node-llama-cpp`. Conserver la dépendance native dans ce Plugin empêche les mises à jour npm normales d’OpenClaw de supprimer une exécution installée manuellement dans le répertoire du paquet OpenClaw.

## Configuration

Définissez le fournisseur de recherche en mémoire sur `local` :

json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        provider: "local",        local: {          modelPath: "hf:ggml-org/embeddinggemma-300m-qat-q8_0-GGUF/embeddinggemma-300m-qat-Q8_0.gguf",        },      },    },  },}
[/code]

Le modèle par défaut est `embeddinggemma-300m-qat-Q8_0.gguf`. Vous pouvez également faire pointer `local.modelPath` vers un fichier `.gguf` local.

## Exécution native

Utilisez Node 24 pour le parcours d’installation native le plus fluide. Les checkouts source utilisant pnpm peuvent devoir approuver et reconstruire la dépendance native :

bashCopy code
[code]
    pnpm approve-buildspnpm rebuild node-llama-cpp
[/code]

Pour des embeddings locaux avec moins de friction, utilisez plutôt un fournisseur de service local comme Ollama ou LM Studio.

Was this useful?YesNo

Open issue