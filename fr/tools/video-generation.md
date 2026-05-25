---
title: Génération de vidéos
source_url: https://docs.openclaw.ai/fr/tools/video-generation
scraped_at: 2026-05-25
---

OpenClaw agents peuvent générer des vidéos à partir de prompts textuels, d’images de référence ou de vidéos existantes. Seize backends de fournisseurs sont pris en charge, chacun avec des options de modèle, des modes d’entrée et des ensembles de fonctionnalités différents. L’agent choisit automatiquement le bon fournisseur en fonction de votre configuration et des clés d’API disponibles.

OpenClaw traite la génération vidéo comme trois modes d’exécution :

  * `generate` \- requêtes texte-vers-vidéo sans média de référence.
  * `imageToVideo` \- la requête inclut une ou plusieurs images de référence.
  * `videoToVideo` \- la requête inclut une ou plusieurs vidéos de référence.


Les fournisseurs peuvent prendre en charge n’importe quel sous-ensemble de ces modes. L’outil valide le mode actif avant l’envoi et signale les modes pris en charge dans `action=list`.

## Démarrage rapide

* ### Configurer l’authentification

Définissez une clé d’API pour n’importe quel fournisseur pris en charge :

bashCopy code
[code]
    export GEMINI_API_KEY="your-key"
[/code]

* ### Choisir un modèle par défaut (facultatif)

bashCopy code
[code]
    openclaw config set agents.defaults.videoGenerationModel.primary "google/veo-3.1-fast-generate-preview"
[/code]

* ### Demander à l’agent

> Générez une vidéo cinématographique de 5 secondes montrant un homard amical qui surfe au coucher du soleil.

L’agent appelle automatiquement `video_generate`. Aucune liste d’autorisation d’outils n’est nécessaire.

## Fonctionnement de la génération asynchrone

La génération vidéo est asynchrone. Quand l’agent appelle `video_generate` dans une session :

  1. OpenClaw envoie la requête au fournisseur et renvoie immédiatement un identifiant de tâche.
  2. Le fournisseur traite la tâche en arrière-plan (généralement de 30 secondes à plusieurs minutes selon le fournisseur et la résolution ; les fournisseurs lents adossés à une file d’attente peuvent s’exécuter jusqu’au délai d’expiration configuré).
  3. Quand la vidéo est prête, OpenClaw réveille la même session avec un événement interne d’achèvement.
  4. L’agent informe l’utilisateur et joint la vidéo terminée. Dans les discussions de groupe/canal qui utilisent une remise visible uniquement via l’outil de messagerie, l’agent relaie le résultat via l’outil de messagerie au lieu qu’OpenClaw le publie directement.


Lorsqu’une tâche est en cours, les appels `video_generate` en double dans la même session renvoient l’état de la tâche en cours au lieu de démarrer une autre génération. Utilisez `openclaw tasks list` ou `openclaw tasks show <taskId>` pour vérifier la progression depuis la CLI.

En dehors des exécutions d’agent adossées à une session (par exemple, les appels directs d’outil), l’outil revient à la génération en ligne et renvoie le chemin du média final dans le même tour.

Les fichiers vidéo générés sont enregistrés dans le stockage multimédia géré par OpenClaw lorsque le fournisseur renvoie des octets. Le plafond d’enregistrement par défaut des vidéos générées suit la limite des médias vidéo, et `agents.defaults.mediaMaxMb` l’augmente pour les rendus plus volumineux. Quand un fournisseur renvoie aussi une URL de sortie hébergée, OpenClaw peut livrer cette URL au lieu de faire échouer la tâche si la persistance locale rejette un fichier trop volumineux.

### Cycle de vie des tâches

État | Signification  
---|---  
`queued` | Tâche créée, en attente d’acceptation par le fournisseur.  
`running` | Le fournisseur traite la tâche (généralement de 30 secondes à plusieurs minutes selon le fournisseur et la résolution).  
`succeeded` | Vidéo prête ; l’agent se réveille et la publie dans la conversation.  
`failed` | Erreur du fournisseur ou délai d’expiration ; l’agent se réveille avec les détails de l’erreur.  
  
Vérifiez l’état depuis la CLI :

bashCopy code
[code]
    openclaw tasks listopenclaw tasks show <taskId>openclaw tasks cancel <taskId>
[/code]

Si une tâche vidéo est déjà `queued` ou `running` pour la session actuelle, `video_generate` renvoie l’état de la tâche existante au lieu d’en démarrer une nouvelle. Utilisez `action: "status"` pour vérifier explicitement sans déclencher une nouvelle génération.

## Fournisseurs pris en charge

Fournisseur | Modèle par défaut | Texte | Réf. image | Réf. vidéo | Authentification  
---|---|---|---|---|---  
Alibaba | `wan2.6-t2v` | ✓ | Oui (URL distante) | Oui (URL distante) | `MODELSTUDIO_API_KEY`  
BytePlus (1.0) | `seedance-1-0-pro-250528` | ✓ | Jusqu’à 2 images (modèles I2V uniquement ; première + dernière image) | - | `BYTEPLUS_API_KEY`  
BytePlus Seedance 1.5 | `seedance-1-5-pro-251215` | ✓ | Jusqu’à 2 images (première + dernière image via le rôle) | - | `BYTEPLUS_API_KEY`  
BytePlus Seedance 2.0 | `dreamina-seedance-2-0-260128` | ✓ | Jusqu’à 9 images de référence | Jusqu’à 3 vidéos | `BYTEPLUS_API_KEY`  
ComfyUI | `workflow` | ✓ | 1 image | - | `COMFY_API_KEY` ou `COMFY_CLOUD_API_KEY`  
DeepInfra | `Pixverse/Pixverse-T2V` | ✓ | - | - | `DEEPINFRA_API_KEY`  
fal | `fal-ai/minimax/video-01-live` | ✓ | 1 image ; jusqu’à 9 avec Seedance reference-to-video | Jusqu’à 3 vidéos avec Seedance reference-to-video | `FAL_KEY`  
Google | `veo-3.1-fast-generate-preview` | ✓ | 1 image | 1 vidéo | `GEMINI_API_KEY`  
MiniMax | `MiniMax-Hailuo-2.3` | ✓ | 1 image | - | `MINIMAX_API_KEY` ou OAuth MiniMax  
OpenAI | `sora-2` | ✓ | 1 image | 1 vidéo | `OPENAI_API_KEY`  
OpenRouter | `google/veo-3.1-fast` | ✓ | Jusqu’à 4 images (première/dernière image ou références) | - | `OPENROUTER_API_KEY`  
Qwen | `wan2.6-t2v` | ✓ | Oui (URL distante) | Oui (URL distante) | `QWEN_API_KEY`  
Runway | `gen4.5` | ✓ | 1 image | 1 vidéo | `RUNWAYML_API_SECRET`  
Together | `Wan-AI/Wan2.2-T2V-A14B` | ✓ | 1 image | - | `TOGETHER_API_KEY`  
Vydra | `veo3` | ✓ | 1 image (`kling`) | - | `VYDRA_API_KEY`  
xAI | `grok-imagine-video` | ✓ | 1 image de première frame ou jusqu’à 7 `reference_image`s | 1 vidéo | `XAI_API_KEY`  
  
Certains fournisseurs acceptent des variables d’environnement de clé d’API supplémentaires ou alternatives. Consultez les pages des fournisseurs individuelles pour plus de détails.

Exécutez `video_generate action=list` pour inspecter les fournisseurs, les modèles et les modes d’exécution disponibles à l’exécution.

### Matrice des capacités

Le contrat de mode explicite utilisé par `video_generate`, les tests de contrat et le balayage live partagé :

Fournisseur | `generate` | `imageToVideo` | `videoToVideo` | Voies live partagées aujourd’hui  
---|---|---|---|---  
Alibaba | ✓ | ✓ | ✓ | `generate`, `imageToVideo` ; `videoToVideo` ignoré car ce fournisseur exige des URL vidéo `http(s)` distantes  
BytePlus | ✓ | ✓ | - | `generate`, `imageToVideo`  
ComfyUI | ✓ | ✓ | - | Non inclus dans le balayage partagé ; la couverture propre aux workflows réside avec les tests Comfy  
DeepInfra | ✓ | - | - | `generate` ; les schémas vidéo DeepInfra natifs sont texte-vers-vidéo dans le contrat groupé  
fal | ✓ | ✓ | ✓ | `generate`, `imageToVideo` ; `videoToVideo` uniquement avec Seedance reference-to-video  
Google | ✓ | ✓ | ✓ | `generate`, `imageToVideo` ; le `videoToVideo` partagé est ignoré car le balayage Gemini/Veo actuel adossé aux tampons n’accepte pas cette entrée  
MiniMax | ✓ | ✓ | - | `generate`, `imageToVideo`  
OpenAI | ✓ | ✓ | ✓ | `generate`, `imageToVideo` ; le `videoToVideo` partagé est ignoré car ce chemin d’organisation/d’entrée nécessite actuellement un accès inpaint/remix côté fournisseur  
OpenRouter | ✓ | ✓ | - | `generate`, `imageToVideo`  
Qwen | ✓ | ✓ | ✓ | `generate`, `imageToVideo` ; `videoToVideo` ignoré car ce fournisseur exige des URL vidéo `http(s)` distantes  
Runway | ✓ | ✓ | ✓ | `generate`, `imageToVideo` ; `videoToVideo` s’exécute uniquement lorsque le modèle sélectionné est `runway/gen4_aleph`  
Together | ✓ | ✓ | - | `generate`, `imageToVideo`  
Vydra | ✓ | ✓ | - | `generate` ; le `imageToVideo` partagé est ignoré car le `veo3` groupé est uniquement textuel et le `kling` groupé exige une URL d’image distante  
xAI | ✓ | ✓ | ✓ | `generate`, `imageToVideo` ; `videoToVideo` ignoré car ce fournisseur nécessite actuellement une URL MP4 distante  
  
## Paramètres de l’outil

### Obligatoire

Description textuelle de la vidéo à générer. Obligatoire pour `action: "generate"`.

### Entrées de contenu

Indications de rôle facultatives par position, correspondant à la liste d'images combinée. Valeurs canoniques : `first_frame`, `last_frame`, `reference_image`.

Indications de rôle facultatives par position, correspondant à la liste de vidéos combinée. Valeur canonique : `reference_video`.

Audio de référence unique (chemin ou URL). Utilisé pour la musique de fond ou comme référence vocale lorsque le fournisseur prend en charge les entrées audio.

Indications de rôle facultatives par position, correspondant à la liste audio combinée. Valeur canonique : `reference_audio`.

### Contrôles de style

Indication de rapport d'aspect telle que `1:1`, `16:9`, `9:16`, `adaptive` ou une valeur propre au fournisseur. OpenClaw normalise ou ignore les valeurs non prises en charge selon le fournisseur.

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InJlc29sdXRpb24iIHR5cGU9InN0cmluZyI Indication de résolution telle que `480P`, `720P`, `768P`, `1080P`, `4K` ou une valeur propre au fournisseur. OpenClaw normalise ou ignore les valeurs non prises en charge selon le fournisseur. OPENCLAW_DOCS_MARKER:paramClose:

Durée cible en secondes (arrondie à la valeur prise en charge la plus proche par le fournisseur).

Active l'audio généré dans la sortie lorsque c'est pris en charge. Distinct de `audioRef*` (entrées).

`adaptive` est une sentinelle propre au fournisseur : elle est transmise telle quelle aux fournisseurs qui déclarent `adaptive` dans leurs capacités (par exemple BytePlus Seedance l'utilise pour détecter automatiquement le rapport à partir des dimensions de l'image d'entrée). Les fournisseurs qui ne la déclarent pas exposent la valeur via `details.ignoredOverrides` dans le résultat de l'outil afin que l'abandon soit visible.

### Avancé

`"status"` renvoie la tâche de session actuelle ; `"list"` inspecte les fournisseurs.

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci Remplacement du fournisseur/modèle (par exemple `runway/gen4.5`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InRpbWVvdXRNcyIgdHlwZT0ibnVtYmVyIg Délai d'expiration facultatif de l'opération du fournisseur, en millisecondes. Lorsqu'il est omis, OpenClaw utilise `agents.defaults.videoGenerationModel.timeoutMs` s'il est configuré. OPENCLAW_DOCS_MARKER:paramClose:

Options propres au fournisseur sous forme d'objet JSON (par exemple `{"seed": 42, "draft": true}`). Les fournisseurs qui déclarent un schéma typé valident les clés et les types ; les clés inconnues ou les incompatibilités ignorent le candidat pendant le repli. Les fournisseurs sans schéma déclaré reçoivent les options telles quelles. Exécutez `video_generate action=list` pour voir ce que chaque fournisseur accepte.

Les entrées de référence sélectionnent le mode d'exécution :

  * Aucun média de référence → `generate`
  * Toute référence d'image → `imageToVideo`
  * Toute référence vidéo → `videoToVideo`
  * Les entrées audio de référence **ne** modifient pas le mode résolu ; elles s'appliquent par-dessus le mode sélectionné par les références d'image/vidéo, et ne fonctionnent qu'avec les fournisseurs qui déclarent `maxInputAudios`.


Le mélange de références d'image et de vidéo n'est pas une surface de capacité partagée stable. Préférez un seul type de référence par requête.

#### Repli et options typées

Certaines vérifications de capacité sont appliquées au niveau de la couche de repli plutôt qu'à la limite de l'outil, si bien qu'une requête qui dépasse les limites du fournisseur principal peut toujours s'exécuter sur un repli capable :

  * Un candidat actif ne déclarant aucun `maxInputAudios` (ou `0`) est ignoré lorsque la requête contient des références audio ; le candidat suivant est essayé.
  * Le `maxDurationSeconds` du candidat actif est inférieur au `durationSeconds` demandé sans liste `supportedDurationSeconds` déclarée → ignoré.
  * La requête contient `providerOptions` et le candidat actif déclare explicitement un schéma `providerOptions` typé → ignoré si les clés fournies ne sont pas dans le schéma ou si les types de valeurs ne correspondent pas. Les fournisseurs sans schéma déclaré reçoivent les options telles quelles (transmission rétrocompatible). Un fournisseur peut refuser toutes les options de fournisseur en déclarant un schéma vide (`capabilities.providerOptions: {}`), ce qui provoque le même contournement qu'une incompatibilité de type.


La première raison de contournement d'une requête est journalisée à `warn` afin que les opérateurs voient quand leur fournisseur principal a été écarté ; les contournements suivants sont journalisés à `debug` pour garder les longues chaînes de repli silencieuses. Si tous les candidats sont ignorés, l'erreur agrégée inclut la raison de contournement de chacun.

## Actions

Action | Ce qu'elle fait  
---|---  
`generate` | Par défaut. Crée une vidéo à partir de l'invite donnée et des entrées de référence facultatives.  
`status` | Vérifie l'état de la tâche vidéo en cours pour la session actuelle sans lancer une autre génération.  
`list` | Affiche les fournisseurs, modèles et leurs capacités disponibles.  
  
## Sélection du modèle

OpenClaw résout le modèle dans cet ordre :

  1. **Paramètre d'outil`model`** \- si l'agent en spécifie un dans l'appel.
  2. **`videoGenerationModel.primary`** depuis la configuration.
  3. **`videoGenerationModel.fallbacks`** dans l'ordre.
  4. **Détection automatique** \- fournisseurs disposant d'une authentification valide, en commençant par le fournisseur par défaut actuel, puis les fournisseurs restants dans l'ordre alphabétique.


Si un fournisseur échoue, le candidat suivant est essayé automatiquement. Si tous les candidats échouent, l'erreur inclut les détails de chaque tentative.

Définissez `agents.defaults.mediaGenerationAutoProviderFallback: false` pour utiliser uniquement les entrées explicites `model`, `primary` et `fallbacks`.

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "google/veo-3.1-fast-generate-preview",        fallbacks: ["runway/gen4.5", "qwen/wan2.6-t2v"],      },    },  },}
[/code]

## Notes sur les fournisseurs

Alibaba

Utilise le point de terminaison asynchrone DashScope / Model Studio. Les images et vidéos de référence doivent être des URL `http(s)` distantes.

BytePlus (1.0)

ID du fournisseur : `byteplus`.

Modèles : `seedance-1-0-pro-250528` (par défaut), `seedance-1-0-pro-t2v-250528`, `seedance-1-0-pro-fast-251015`, `seedance-1-0-lite-t2v-250428`, `seedance-1-0-lite-i2v-250428`.

Les modèles T2V (`*-t2v-*`) n'acceptent pas les entrées d'image ; les modèles I2V et les modèles généraux `*-pro-*` prennent en charge une seule image de référence (première image). Passez l'image positionnellement ou définissez `role: "first_frame"`. Les ID de modèle T2V sont automatiquement remplacés par la variante I2V correspondante lorsqu'une image est fournie.

Clés `providerOptions` prises en charge : `seed` (nombre), `draft` (booléen - force le 480p), `camera_fixed` (booléen).

BytePlus Seedance 1.5

Nécessite le Plugin [`@openclaw/byteplus-modelark`](<https://www.npmjs.com/package/@openclaw/byteplus-modelark>). ID du fournisseur : `byteplus-seedance15`. Modèle : `seedance-1-5-pro-251215`.

Utilise l'API unifiée `content[]`. Prend en charge au maximum 2 images d'entrée (`first_frame` \+ `last_frame`). Toutes les entrées doivent être des URL `https://` distantes. Définissez `role: "first_frame"` / `"last_frame"` sur chaque image, ou passez les images positionnellement.

`aspectRatio: "adaptive"` détecte automatiquement le rapport à partir de l'image d'entrée. `audio: true` est mappé vers `generate_audio`. `providerOptions.seed` (nombre) est transmis.

BytePlus Seedance 2.0

Nécessite le Plugin [`@openclaw/byteplus-modelark`](<https://www.npmjs.com/package/@openclaw/byteplus-modelark>). ID du fournisseur : `byteplus-seedance2`. Modèles : `dreamina-seedance-2-0-260128`, `dreamina-seedance-2-0-fast-260128`.

Utilise l'API unifiée `content[]`. Prend en charge jusqu'à 9 images de référence, 3 vidéos de référence et 3 audios de référence. Toutes les entrées doivent être des URL `https://` distantes. Définissez `role` sur chaque ressource - valeurs prises en charge : `"first_frame"`, `"last_frame"`, `"reference_image"`, `"reference_video"`, `"reference_audio"`.

`aspectRatio: "adaptive"` détecte automatiquement le rapport à partir de l'image d'entrée. `audio: true` est mappé vers `generate_audio`. `providerOptions.seed` (nombre) est transmis.

ComfyUI

Exécution locale ou cloud pilotée par workflow. Prend en charge le texte-vers-vidéo et l’image-vers-vidéo via le graphe configuré.

fal

Utilise un flux adossé à une file d’attente pour les tâches de longue durée. OpenClaw attend jusqu’à 20 minutes par défaut avant de considérer qu’une tâche fal en file d’attente encore en cours a expiré. La plupart des modèles vidéo fal acceptent une seule référence d’image. Les modèles Seedance 2.0 référence-vers-vidéo acceptent jusqu’à 9 images, 3 vidéos et 3 références audio, avec au maximum 12 fichiers de référence au total.

Google (Gemini / Veo)

Prend en charge une référence d’image ou une référence vidéo. Les requêtes d’audio généré sont ignorées avec un avertissement sur le chemin de l’API Gemini, car cette API rejette le paramètre `generateAudio` pour la génération vidéo Veo actuelle.

MiniMax

Référence d’image unique uniquement. MiniMax accepte les résolutions `768P` et `1080P` ; les requêtes telles que `720P` sont normalisées vers la valeur prise en charge la plus proche avant la soumission.

OpenAI

Seule la surcharge `size` est transmise. Les autres surcharges de style (`aspectRatio`, `resolution`, `audio`, `watermark`) sont ignorées avec un avertissement.

OpenRouter

Utilise l’API `/videos` asynchrone d’OpenRouter. OpenClaw soumet la tâche, interroge `polling_url` et télécharge soit `unsigned_urls`, soit le point de terminaison documenté du contenu de la tâche. La valeur par défaut groupée `google/veo-3.1-fast` annonce des durées de 4/6/8 secondes, des résolutions `720P`/`1080P` et des formats d’image `16:9`/`9:16`.

Qwen

Même backend DashScope qu’Alibaba. Les entrées de référence doivent être des URL `http(s)` distantes ; les fichiers locaux sont rejetés dès le départ.

Runway

Prend en charge les fichiers locaux via des URI de données. Le vidéo-vers-vidéo nécessite `runway/gen4_aleph`. Les exécutions texte seul exposent les formats d’image `16:9` et `9:16`.

Together

Référence d’image unique uniquement.

Vydra

Utilise directement `https://www.vydra.ai/api/v1` pour éviter les redirections qui suppriment l’authentification. `veo3` est groupé en texte-vers-vidéo uniquement ; `kling` nécessite une URL d’image distante.

xAI

Prend en charge le texte-vers-vidéo, l’image-vers-vidéo avec une seule image initiale, jusqu’à 7 entrées `reference_image` via les `reference_images` xAI, ainsi que les flux distants de modification/extension vidéo.

## Modes de capacité des fournisseurs

Le contrat partagé de génération vidéo prend en charge des capacités propres à chaque mode plutôt que seulement des limites agrégées plates. Les nouvelles implémentations de fournisseurs devraient privilégier des blocs de mode explicites :

typescriptCopy code
[code]
    capabilities: {  generate: {    maxVideos: 1,    maxDurationSeconds: 10,    supportsResolution: true,  },  imageToVideo: {    enabled: true,    maxVideos: 1,    maxInputImages: 1,    maxInputImagesByModel: { "provider/reference-to-video": 9 },    maxDurationSeconds: 5,  },  videoToVideo: {    enabled: true,    maxVideos: 1,    maxInputVideos: 1,    maxDurationSeconds: 5,  },}
[/code]

Les champs agrégés plats tels que `maxInputImages` et `maxInputVideos` ne sont **pas** suffisants pour annoncer la prise en charge du mode de transformation. Les fournisseurs devraient déclarer explicitement `generate`, `imageToVideo` et `videoToVideo` afin que les tests en direct, les tests de contrat et l’outil partagé `video_generate` puissent valider la prise en charge des modes de manière déterministe.

Lorsqu’un modèle d’un fournisseur prend en charge davantage d’entrées de référence que le reste, utilisez `maxInputImagesByModel`, `maxInputVideosByModel` ou `maxInputAudiosByModel` au lieu d’augmenter la limite globale du mode.

## Tests en direct

Couverture en direct facultative pour les fournisseurs groupés partagés :

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 pnpm test:live -- extensions/video-generation-providers.live.test.ts
[/code]

Wrapper du dépôt :

bashCopy code
[code]
    pnpm test:live:media video
[/code]

Ce fichier en direct charge les variables d’environnement fournisseur manquantes depuis `~/.profile`, privilégie par défaut les clés d’API live/env avant les profils d’authentification stockés, et exécute un test de fumée adapté aux releases par défaut :

  * `generate` pour chaque fournisseur non-FAL de la passe.
  * Prompt de homard d’une seconde.
  * Plafond d’opération par fournisseur depuis `OPENCLAW_LIVE_VIDEO_GENERATION_TIMEOUT_MS` (`180000` par défaut).


FAL est facultatif, car la latence de la file d’attente côté fournisseur peut dominer le temps de release :

bashCopy code
[code]
    pnpm test:live:media video --video-providers fal
[/code]

Définissez `OPENCLAW_LIVE_VIDEO_GENERATION_FULL_MODES=1` pour exécuter aussi les modes de transformation déclarés que la passe partagée peut exercer en toute sécurité avec des médias locaux :

  * `imageToVideo` lorsque `capabilities.imageToVideo.enabled`.
  * `videoToVideo` lorsque `capabilities.videoToVideo.enabled` et que le fournisseur/modèle accepte une entrée vidéo locale adossée à un tampon dans la passe partagée.


Aujourd’hui, la voie de test en direct `videoToVideo` partagée couvre `runway` uniquement lorsque vous sélectionnez `runway/gen4_aleph`.

## Configuration

Définissez le modèle de génération vidéo par défaut dans votre configuration OpenClaw :

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "qwen/wan2.6-t2v",        fallbacks: ["qwen/wan2.6-r2v-flash"],      },    },  },}
[/code]

Ou via la CLI :

bashCopy code
[code]
    openclaw config set agents.defaults.videoGenerationModel.primary "qwen/wan2.6-t2v"
[/code]

## Connexe

  * [Alibaba Model Studio](</fr/providers/alibaba>)
  * [Tâches en arrière-plan](</fr/automation/tasks>) \- suivi des tâches pour la génération vidéo asynchrone
  * [BytePlus](</fr/concepts/model-providers#byteplus-international>)
  * [ComfyUI](</fr/providers/comfy>)
  * [Référence de configuration](</fr/gateway/config-agents#agent-defaults>)
  * [fal](</fr/providers/fal>)
  * [Google (Gemini)](</fr/providers/google>)
  * [MiniMax](</fr/providers/minimax>)
  * [Modèles](</fr/concepts/models>)
  * [OpenAI](</fr/providers/openai>)
  * [Qwen](</fr/providers/qwen>)
  * [Runway](</fr/providers/runway>)
  * [Together AI](</fr/providers/together>)
  * [Vue d’ensemble des outils](</fr/tools>)
  * [Vydra](</fr/providers/vydra>)
  * [xAI](</fr/providers/xai>)


Was this useful?YesNo