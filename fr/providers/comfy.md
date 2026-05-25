---
title: ComfyUI
source_url: https://docs.openclaw.ai/fr/providers/comfy
scraped_at: 2026-05-25
---

OpenClaw inclut un plugin `comfy` pour les exécutions ComfyUI pilotées par workflow. Le plugin est entièrement piloté par workflow, donc OpenClaw n’essaie pas de mapper des contrôles génériques `size`, `aspectRatio`, `resolution`, `durationSeconds` ou de type TTS sur votre graphe.

Propriété | Détail  
---|---  
Fournisseur | `comfy`  
Modèles | `comfy/workflow`  
Surfaces partagées | `image_generate`, `video_generate`, `music_generate`  
Authentification | Aucune pour ComfyUI local ; `COMFY_API_KEY` ou `COMFY_CLOUD_API_KEY` pour Comfy Cloud  
API | ComfyUI `/prompt` / `/history` / `/view` et Comfy Cloud `/api/*`  
  
## Ce qui est pris en charge

  * Génération d’image à partir d’un JSON de workflow
  * Édition d’image avec 1 image de référence uploadée
  * Génération vidéo à partir d’un JSON de workflow
  * Génération vidéo avec 1 image de référence uploadée
  * Génération de musique ou d’audio via l’outil partagé `music_generate`
  * Téléchargement de sortie depuis un nœud configuré ou tous les nœuds de sortie correspondants


## Prise en main

Choisissez entre exécuter ComfyUI sur votre propre machine ou utiliser Comfy Cloud.

### Local

**Idéal pour :** exécuter votre propre instance ComfyUI sur votre machine ou votre LAN.

* ### Démarrer ComfyUI localement

Assurez-vous que votre instance ComfyUI locale est en cours d’exécution (par défaut `http://127.0.0.1:8188`).

* ### Préparer votre JSON de workflow

Exportez ou créez un fichier JSON de workflow ComfyUI. Notez les identifiants de nœuds du nœud d’entrée de prompt et du nœud de sortie que vous voulez qu’OpenClaw lise.

* ### Configurer le fournisseur

Définissez `mode: "local"` et pointez vers votre fichier de workflow. Voici un exemple minimal pour l’image :

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          mode: "local",          baseUrl: "http://127.0.0.1:8188",          image: {            workflowPath: "./workflows/flux-api.json",            promptNodeId: "6",            outputNodeId: "9",          },        },      },    },  },}
[/code]

* ### Définir le modèle par défaut

Pointez OpenClaw vers le modèle `comfy/workflow` pour la fonctionnalité que vous avez configurée :

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "comfy/workflow",      },    },  },}
[/code]

* ### Vérifier

bashCopy code
[code]
    openclaw models list --provider comfy
[/code]

### Comfy Cloud

**Idéal pour :** exécuter des workflows sur Comfy Cloud sans gérer des ressources GPU locales.

* ### Obtenir une clé API

Inscrivez-vous sur [comfy.org](<https://comfy.org>) et générez une clé API depuis le tableau de bord de votre compte.

* ### Définir la clé API

Fournissez votre clé par l’une des méthodes suivantes :

bashCopy code
[code]
    # Variable d’environnement (préférée)export COMFY_API_KEY="your-key" # Variable d’environnement alternativeexport COMFY_CLOUD_API_KEY="your-key" # Ou directement dans la configurationopenclaw config set plugins.entries.comfy.config.apiKey "your-key"
[/code]

* ### Préparer votre JSON de workflow

Exportez ou créez un fichier JSON de workflow ComfyUI. Notez les identifiants de nœuds du nœud d’entrée de prompt et du nœud de sortie.

* ### Configurer le fournisseur

Définissez `mode: "cloud"` et pointez vers votre fichier de workflow :

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          mode: "cloud",          image: {            workflowPath: "./workflows/flux-api.json",            promptNodeId: "6",            outputNodeId: "9",          },        },      },    },  },}
[/code]

* ### Définir le modèle par défaut

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "comfy/workflow",      },    },  },}
[/code]

* ### Vérifier

bashCopy code
[code]
    openclaw models list --provider comfy
[/code]

## Configuration

Comfy prend en charge des paramètres de connexion partagés de niveau supérieur plus des sections de workflow par fonctionnalité (`image`, `video`, `music`) :

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          mode: "local",          baseUrl: "http://127.0.0.1:8188",          image: {            workflowPath: "./workflows/flux-api.json",            promptNodeId: "6",            outputNodeId: "9",          },          video: {            workflowPath: "./workflows/video-api.json",            promptNodeId: "12",            outputNodeId: "21",          },          music: {            workflowPath: "./workflows/music-api.json",            promptNodeId: "3",            outputNodeId: "18",          },        },      },    },  },}
[/code]

### Clés partagées

Clé | Type | Description  
---|---|---  
`mode` | `"local"` ou `"cloud"` | Mode de connexion.  
`baseUrl` | string | Vaut par défaut `http://127.0.0.1:8188` en local ou `https://cloud.comfy.org` en cloud.  
`apiKey` | string | Clé inline facultative, alternative aux variables d’environnement `COMFY_API_KEY` / `COMFY_CLOUD_API_KEY`.  
`allowPrivateNetwork` | boolean | Autoriser une `baseUrl` privée/LAN en mode cloud.  
  
### Clés par fonctionnalité

Ces clés s’appliquent à l’intérieur des sections `image`, `video` ou `music` :

Clé | Requise | Par défaut | Description  
---|---|---|---  
`workflow` ou `workflowPath` | Oui | \-- | Chemin vers le fichier JSON de workflow ComfyUI.  
`promptNodeId` | Oui | \-- | Identifiant du nœud qui reçoit le prompt texte.  
`promptInputName` | Non | `"text"` | Nom d’entrée sur le nœud de prompt.  
`outputNodeId` | Non | \-- | Identifiant du nœud à partir duquel lire la sortie. S’il est omis, tous les nœuds de sortie correspondants sont utilisés.  
`pollIntervalMs` | Non | \-- | Intervalle de polling en millisecondes pour la fin de tâche.  
`timeoutMs` | Non | \-- | Délai d’expiration en millisecondes pour l’exécution du workflow.  
  
Les sections `image` et `video` prennent aussi en charge :

Clé | Requise | Par défaut | Description  
---|---|---|---  
`inputImageNodeId` | Oui (lors du passage d’une image de référence) | \-- | Identifiant du nœud qui reçoit l’image de référence uploadée.  
`inputImageInputName` | Non | `"image"` | Nom d’entrée sur le nœud image.  
  
## Détails des workflows

Workflows d’image

Définissez le modèle d’image par défaut sur `comfy/workflow` :

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "comfy/workflow",      },    },  },}
[/code]

**Exemple d’édition avec image de référence :**

Pour activer l’édition d’image avec une image de référence uploadée, ajoutez `inputImageNodeId` à votre configuration image :

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          image: {            workflowPath: "./workflows/edit-api.json",            promptNodeId: "6",            inputImageNodeId: "7",            inputImageInputName: "image",            outputNodeId: "9",          },        },      },    },  },}
[/code]

Workflows vidéo

Définissez le modèle vidéo par défaut sur `comfy/workflow` :

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "comfy/workflow",      },    },  },}
[/code]

Les workflows vidéo Comfy prennent en charge le texte-vers-vidéo et l’image-vers-vidéo via le graphe configuré.

Workflows musicaux

Le plugin inclus enregistre un fournisseur de génération musicale pour les sorties audio ou musicales définies par workflow, exposé via l’outil partagé `music_generate` :

textCopy code
[code]
    /tool music_generate prompt="Warm ambient synth loop with soft tape texture"
[/code]

Utilisez la section de configuration `music` pour pointer vers votre JSON de workflow audio et votre nœud de sortie.

Rétrocompatibilité

La configuration d’image de niveau supérieur existante (sans section imbriquée `image`) fonctionne toujours :

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          workflowPath: "./workflows/flux-api.json",          promptNodeId: "6",          outputNodeId: "9",        },      },    },  },}
[/code]

OpenClaw traite cette forme héritée comme la configuration du workflow image. Vous n’avez pas besoin de migrer immédiatement, mais les sections imbriquées `image` / `video` / `music` sont recommandées pour les nouvelles installations.

Tests live

Une couverture live opt-in existe pour le plugin inclus :

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 COMFY_LIVE_TEST=1 pnpm test:live -- extensions/comfy/comfy.live.test.ts
[/code]

Le test live ignore les cas image, vidéo ou musique individuels sauf si la section de workflow Comfy correspondante est configurée.

## Related

[**Génération d’images** Configuration et utilisation de l’outil de génération d’images. ](</fr/tools/image-generation>) [**Génération vidéo** Configuration et utilisation de l’outil de génération vidéo. ](</fr/tools/video-generation>) [**Génération musicale** Configuration de l’outil de génération de musique et d’audio. ](</fr/tools/music-generation>) [**Répertoire des fournisseurs** Vue d’ensemble de tous les fournisseurs et des références de modèles. ](</fr/providers>) [**Référence de configuration** Référence complète de configuration, y compris les valeurs par défaut des agents. ](</fr/gateway/config-agents#agent-defaults>)

Was this useful?YesNo