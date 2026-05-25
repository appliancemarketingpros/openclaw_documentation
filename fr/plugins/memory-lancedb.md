---
title: Mémoire LanceDB
source_url: https://docs.openclaw.ai/fr/plugins/memory-lancedb
scraped_at: 2026-05-25
---

`memory-lancedb` est un plugin de mémoire intégré qui stocke la mémoire à long terme dans LanceDB et utilise des embeddings pour le rappel. Il peut rappeler automatiquement les souvenirs pertinents avant un tour de modèle et capturer les faits importants après une réponse.

Utilisez-le quand vous voulez une base de données vectorielle locale pour la mémoire, avez besoin d’un point de terminaison d’embeddings compatible OpenAI, ou souhaitez conserver une base de données mémoire en dehors du magasin de mémoire intégré par défaut.

## Démarrage rapide

json5Copy code
[code]
    {  plugins: {    slots: {      memory: "memory-lancedb",    },    entries: {      "memory-lancedb": {        enabled: true,        config: {          embedding: {            provider: "openai",            model: "text-embedding-3-small",          },          autoRecall: true,          autoCapture: false,        },      },    },  },}
[/code]

Redémarrez le Gateway après avoir modifié la configuration du plugin :

bashCopy code
[code]
    openclaw gateway restart
[/code]

Vérifiez ensuite que le plugin est chargé :

bashCopy code
[code]
    openclaw plugins list
[/code]

## Embeddings adossés à un fournisseur

`memory-lancedb` peut utiliser les mêmes adaptateurs de fournisseur d’embeddings de mémoire que `memory-core`. Définissez `embedding.provider` et omettez `embedding.apiKey` pour utiliser le profil d’authentification configuré du fournisseur, la variable d’environnement, ou `models.providers.<provider>.apiKey`.

json5Copy code
[code]
    {  plugins: {    slots: {      memory: "memory-lancedb",    },    entries: {      "memory-lancedb": {        enabled: true,        config: {          embedding: {            provider: "openai",            model: "text-embedding-3-small",          },          autoRecall: true,        },      },    },  },}
[/code]

Ce chemin fonctionne avec les profils d’authentification fournisseur qui exposent des identifiants d’embeddings. Par exemple, GitHub Copilot peut être utilisé lorsque le profil/forfait Copilot prend en charge les embeddings :

json5Copy code
[code]
    {  plugins: {    slots: {      memory: "memory-lancedb",    },    entries: {      "memory-lancedb": {        enabled: true,        config: {          embedding: {            provider: "github-copilot",            model: "text-embedding-3-small",          },        },      },    },  },}
[/code]

OpenAI Codex / ChatGPT OAuth (`openai-codex`) n’est pas un identifiant d’embeddings OpenAI Platform. Pour les embeddings OpenAI, utilisez un profil d’authentification avec clé API OpenAI, `OPENAI_API_KEY`, ou `models.providers.openai.apiKey`. Les utilisateurs OAuth uniquement peuvent utiliser un autre fournisseur compatible avec les embeddings, comme GitHub Copilot ou Ollama.

## Embeddings Ollama

Pour les embeddings Ollama, privilégiez le fournisseur d’embeddings Ollama intégré. Il utilise le point de terminaison Ollama natif `/api/embed` et suit les mêmes règles d’authentification/base URL que le fournisseur Ollama documenté dans [Ollama](</fr/providers/ollama>).

json5Copy code
[code]
    {  plugins: {    slots: {      memory: "memory-lancedb",    },    entries: {      "memory-lancedb": {        enabled: true,        config: {          embedding: {            provider: "ollama",            baseUrl: "http://127.0.0.1:11434",            model: "mxbai-embed-large",            dimensions: 1024,          },          recallMaxChars: 400,          autoRecall: true,          autoCapture: false,        },      },    },  },}
[/code]

Définissez `dimensions` pour les modèles d’embeddings non standards. OpenClaw connaît les dimensions de `text-embedding-3-small` et `text-embedding-3-large` ; les modèles personnalisés ont besoin de cette valeur dans la configuration pour que LanceDB puisse créer la colonne vectorielle.

Pour les petits modèles d’embeddings locaux, réduisez `recallMaxChars` si vous voyez des erreurs de longueur de contexte provenant du serveur local.

## Fournisseurs compatibles OpenAI

Certains fournisseurs d’embeddings compatibles OpenAI rejettent le paramètre `encoding_format`, tandis que d’autres l’ignorent et renvoient toujours des vecteurs `number[]`. `memory-lancedb` omet donc `encoding_format` dans les requêtes d’embeddings et accepte soit des réponses sous forme de tableaux de flottants, soit des réponses float32 encodées en base64.

Si vous avez un point de terminaison d’embeddings brut compatible OpenAI qui n’a pas d’adaptateur fournisseur intégré, omettez `embedding.provider` (ou laissez-le à `openai`) et définissez `embedding.apiKey` ainsi que `embedding.baseUrl`. Cela préserve le chemin client direct compatible OpenAI.

Définissez `embedding.dimensions` pour les fournisseurs dont les dimensions de modèle ne sont pas intégrées. Par exemple, ZhiPu `embedding-3` utilise `2048` dimensions :

json5Copy code
[code]
    {  plugins: {    entries: {      "memory-lancedb": {        enabled: true,        config: {          embedding: {            apiKey: "${ZHIPU_API_KEY}",            baseUrl: "https://open.bigmodel.cn/api/paas/v4",            model: "embedding-3",            dimensions: 2048,          },        },      },    },  },}
[/code]

## Limites de rappel et de capture

`memory-lancedb` a deux limites de texte distinctes :

Paramètre | Par défaut | Plage | S’applique à  
---|---|---|---  
`recallMaxChars` | `1000` | 100-10000 | texte envoyé à l’API d’embeddings pour le rappel  
`captureMaxChars` | `500` | 100-10000 | longueur du message assistant admissible à la capture  
  
`recallMaxChars` contrôle le rappel automatique, l’outil `memory_recall`, le chemin de requête `memory_forget` et `openclaw ltm search`. Le rappel automatique privilégie le dernier message utilisateur du tour et ne revient à l’invite complète que lorsqu’aucun message utilisateur n’est disponible. Cela évite d’inclure les métadonnées de canal et les gros blocs d’invite dans la requête d’embeddings.

`captureMaxChars` contrôle si une réponse est assez courte pour être prise en compte pour la capture automatique. Il ne limite pas les embeddings de requête de rappel.

## Commandes

Lorsque `memory-lancedb` est le plugin Active Memory, il enregistre l’espace de noms CLI `ltm` :

bashCopy code
[code]
    openclaw ltm listopenclaw ltm search "project preferences"openclaw ltm stats
[/code]

Le plugin étend aussi `openclaw memory` avec une sous-commande `query` non vectorielle qui s’exécute directement sur la table LanceDB :

bashCopy code
[code]
    openclaw memory query --cols id,text,createdAt --limit 20openclaw memory query --filter "category = 'preference'" --order-by createdAt:desc
[/code]

  * `--cols <columns>` : liste autorisée de colonnes séparées par des virgules (par défaut `id`, `text`, `importance`, `category`, `createdAt`).
  * `--filter <condition>` : clause WHERE de style SQL ; limitée à 200 caractères et restreinte aux caractères alphanumériques, opérateurs de comparaison, guillemets, parenthèses et à un petit ensemble de signes de ponctuation sûrs.
  * `--limit <n>` : entier positif ; valeur par défaut `10`.
  * `--order-by <column>:<asc|desc>` : tri en mémoire appliqué après le filtre ; la colonne de tri est automatiquement incluse dans la projection.


Les agents reçoivent aussi des outils de mémoire LanceDB du plugin Active Memory :

  * `memory_recall` pour le rappel adossé à LanceDB
  * `memory_store` pour enregistrer les faits importants, préférences, décisions et entités
  * `memory_forget` pour supprimer les souvenirs correspondants


## Stockage

Par défaut, les données LanceDB résident sous `~/.openclaw/memory/lancedb`. Remplacez le chemin avec `dbPath` :

json5Copy code
[code]
    {  plugins: {    entries: {      "memory-lancedb": {        enabled: true,        config: {          dbPath: "~/.openclaw/memory/lancedb",          embedding: {            apiKey: "${OPENAI_API_KEY}",            model: "text-embedding-3-small",          },        },      },    },  },}
[/code]

`storageOptions` accepte des paires clé/valeur de chaînes pour les backends de stockage LanceDB et prend en charge l’expansion `${ENV_VAR}` :

json5Copy code
[code]
    {  plugins: {    entries: {      "memory-lancedb": {        enabled: true,        config: {          dbPath: "s3://memory-bucket/openclaw",          storageOptions: {            access_key: "${AWS_ACCESS_KEY_ID}",            secret_key: "${AWS_SECRET_ACCESS_KEY}",            endpoint: "${AWS_ENDPOINT_URL}",          },          embedding: {            apiKey: "${OPENAI_API_KEY}",            model: "text-embedding-3-small",          },        },      },    },  },}
[/code]

## Dépendances d’exécution

`memory-lancedb` dépend du paquet natif `@lancedb/lancedb`. OpenClaw empaqueté traite ce paquet comme faisant partie du paquet du plugin. Le démarrage du Gateway ne répare pas les dépendances des plugins ; si la dépendance manque, réinstallez ou mettez à jour le paquet du plugin et redémarrez le Gateway.

Si une ancienne installation journalise une erreur `dist/package.json` manquant ou `@lancedb/lancedb` manquant pendant le chargement du plugin, mettez OpenClaw à niveau et redémarrez le Gateway.

Si le plugin journalise que LanceDB n’est pas disponible sur `darwin-x64`, utilisez le backend mémoire par défaut sur cette machine, déplacez le Gateway vers une plateforme prise en charge, ou désactivez `memory-lancedb`.

## Dépannage

### La longueur d’entrée dépasse la longueur de contexte

Cela signifie généralement que le modèle d’embeddings a rejeté la requête de rappel :

textCopy code
[code]
    memory-lancedb: recall failed: Error: 400 the input length exceeds the context length
[/code]

Définissez une valeur `recallMaxChars` plus basse, puis redémarrez le Gateway :

json5Copy code
[code]
    {  plugins: {    entries: {      "memory-lancedb": {        config: {          recallMaxChars: 400,        },      },    },  },}
[/code]

Pour Ollama, vérifiez aussi que le serveur d’embeddings est joignable depuis l’hôte du Gateway :

bashCopy code
[code]
    curl http://127.0.0.1:11434/v1/embeddings \  -H "Content-Type: application/json" \  -d '{"model":"mxbai-embed-large","input":"hello"}'
[/code]

### Modèle d’embeddings non pris en charge

Sans `dimensions`, seules les dimensions d’embeddings OpenAI intégrées sont connues. Pour les modèles d’embeddings locaux ou personnalisés, définissez `embedding.dimensions` sur la taille de vecteur signalée par ce modèle.

### Le plugin se charge mais aucune mémoire n’apparaît

Vérifiez que `plugins.slots.memory` pointe vers `memory-lancedb`, puis exécutez :

bashCopy code
[code]
    openclaw ltm statsopenclaw ltm search "recent preference"
[/code]

Si `autoCapture` est désactivé, le plugin rappellera les souvenirs existants mais ne stockera pas automatiquement les nouveaux. Utilisez l’outil `memory_store` ou activez `autoCapture` si vous voulez une capture automatique.

## Connexe

  * [Vue d’ensemble de la mémoire](</fr/concepts/memory>)
  * [Active Memory](</fr/concepts/active-memory>)
  * [Recherche de mémoire](</fr/concepts/memory-search>)
  * [Memory Wiki](</fr/plugins/memory-wiki>)
  * [Ollama](</fr/providers/ollama>)


Was this useful?YesNo